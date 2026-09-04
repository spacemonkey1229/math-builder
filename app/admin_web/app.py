"""app/admin_web/app.py — the hosted (Vercel + Neon) admin app.

Same route table, same ADMIN_HTML frontend, same admin_core rules as the local
stdlib server (app/admin_server.py) -- the only things that differ are the
store (Postgres instead of real files, see app/store_postgres.py) and the
addition of a login gate, since this one is reachable over the internet.

Auth is deliberately minimal: a single shared passcode (ADMIN_PASSCODE env
var) behind a signed session cookie (FLASK_SECRET_KEY env var). This is an
explicit, named stopgap -- see DECISIONS.md -- not a design endorsement. The
agreed next step is a real auth provider; this is what unblocks a live demo
today.
"""
import functools, os, re, sys
from urllib.parse import unquote

_APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ROOT_DIR = os.path.dirname(_APP_DIR)
_CASES_DIR = os.path.join(_ROOT_DIR, 'cases')
if _APP_DIR not in sys.path:
    sys.path.insert(0, _APP_DIR)

import admin_core
from admin_html import render_admin_html
from student_portal_html import render_student_portal_html
from store_postgres import PostgresStore

from flask import Flask, Response, jsonify, redirect, request, send_from_directory, session

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or 'dev-only-insecure-secret-do-not-deploy-with-this'
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

_store = None


def get_store():
    global _store
    if _store is None:
        _store = PostgresStore()
    return _store


LOGIN_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math Builder — Admin</title>
<style>
:root{{--paper:#FAF8F4;--ink:#16140F;--muted:#5F594E;--rule:#DED8CC;--accent:#22406B;--flag:#A93A1E;--flag-soft:#F8E7E1}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Arial,sans-serif;background:var(--paper);
  color:var(--ink);display:flex;align-items:center;justify-content:center;height:100vh}}
form{{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:32px;min-width:280px;
  box-shadow:0 4px 14px rgba(24,20,12,.06)}}
h1{{font-size:17px;margin:0 0 4px}}
p.sub{{font-size:12px;color:var(--muted);margin:0 0 18px}}
input{{width:100%;padding:9px 10px;border:1px solid var(--rule);border-radius:6px;margin-bottom:14px;
  box-sizing:border-box;font-size:14px}}
button{{width:100%;padding:9px;background:var(--accent);color:#fff;border:none;border-radius:6px;
  cursor:pointer;font-weight:600;font-size:14px}}
.err{{color:var(--flag);background:var(--flag-soft);border-radius:6px;padding:8px 10px;font-size:13px;
  margin-bottom:14px}}
</style></head><body>
<form method="post" action="/login">
<h1>Math Builder — Admin</h1>
<p class="sub">Enter the shared passcode to continue.</p>
{err}
<input type="password" name="passcode" placeholder="Passcode" autofocus>
<button type="submit">Enter</button>
</form></body></html>"""


def _authed():
    return session.get('authed') is True


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return LOGIN_HTML.format(err='')
    expected = os.environ.get('ADMIN_PASSCODE')
    if not expected:
        return LOGIN_HTML.format(err='<div class="err">Server has no ADMIN_PASSCODE configured.</div>'), 500
    if request.form.get('passcode', '') == expected:
        session['authed'] = True
        return redirect('/')
    return LOGIN_HTML.format(err='<div class="err">Wrong passcode.</div>'), 401


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('authed', None)
    return redirect('/login')


_STUDENT_FILE_RE = re.compile(r'^/(?:app/)?student(?:-[a-z0-9][a-z0-9-]*)?\.html$')

STUDENT_LOGIN_HTML = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Math Builder — My Cases</title>
<style>
:root{{--paper:#FAF8F4;--ink:#16140F;--muted:#5F594E;--rule:#DED8CC;--accent:#22406B;--flag:#A93A1E;--flag-soft:#F8E7E1}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Arial,sans-serif;background:var(--paper);
  color:var(--ink);display:flex;align-items:center;justify-content:center;height:100vh}}
form{{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:32px;min-width:280px;
  box-shadow:0 4px 14px rgba(24,20,12,.06)}}
h1{{font-size:17px;margin:0 0 4px}}
p.sub{{font-size:12px;color:var(--muted);margin:0 0 18px}}
input{{width:100%;padding:9px 10px;border:1px solid var(--rule);border-radius:6px;margin-bottom:14px;
  box-sizing:border-box;font-size:14px}}
button{{width:100%;padding:9px;background:var(--accent);color:#fff;border:none;border-radius:6px;
  cursor:pointer;font-weight:600;font-size:14px}}
.err{{color:var(--flag);background:var(--flag-soft);border-radius:6px;padding:8px 10px;font-size:13px;
  margin-bottom:14px}}
</style></head><body>
<form method="post" action="/student-login">
<h1>Math Builder — My Cases</h1>
<p class="sub">Enter your learner id and passcode — ask your guide if you don't have them.</p>
{err}
<input type="text" name="learner_id" placeholder="Learner id (e.g. maya-w)" autofocus autocapitalize="off" autocorrect="off">
<input type="password" name="passcode" placeholder="Passcode" inputmode="numeric">
<button type="submit">Enter</button>
</form></body></html>"""


@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'GET':
        return STUDENT_LOGIN_HTML.format(err='')
    lid = (request.form.get('learner_id') or '').strip().lower()
    passcode = (request.form.get('passcode') or '').strip()
    try:
        learner = admin_core.do_student_login(get_store(), lid, passcode)
    except admin_core.ApiError as e:
        return STUDENT_LOGIN_HTML.format(err=f'<div class="err">{e.msg}</div>'), e.code
    session['student_id'] = learner['id']
    return redirect('/student')


@app.route('/student-logout', methods=['POST'])
def student_logout():
    session.pop('student_id', None)
    return redirect('/student-login')


_STUDENT_API_RE = re.compile(r'^/api/student/')
_CLASS_CASE_RE = re.compile(r'^/class/[a-z0-9][a-z0-9-]*$')


@app.before_request
def require_auth():
    # student.html (the data-free landing page) and student-<learner-id>.html
    # (and their /app/ aliases) are build_dashboard.py's separate, genuinely
    # redacted, role-locked builds -- guide notes and the full read-model
    # stripped out, unlike dashboard.html which keeps the full data behind
    # its cosmetic-only Guide/Student toggle and must stay behind the
    # passcode.
    if request.path in ('/login', '/logout', '/student-login', '/student-logout') \
            or _STUDENT_FILE_RE.match(request.path) \
            or request.path.startswith('/static') or request.path.startswith('/cases/'):
        return
    # The weekly-class landing page (/class/<case_id>) and its submit endpoint
    # are the one other unauthenticated surface: a walk-up student has no
    # admin login and no pre-registered passcode, by design (see
    # admin_core.py's "weekly class cases" section). /class-review and
    # /class-photo/... (the facilitator's view of what came in) are NOT
    # exempted here -- those stay behind the admin passcode like everything
    # else, since they show every student's name and work.
    if _CLASS_CASE_RE.match(request.path) or request.path == '/api/class-submit':
        return
    # The live student portal (/student + /api/student/*) has its own, separate
    # per-learner passcode session -- never the admin one. A learner never gets
    # (and never needs) an admin login just to see their own cases.
    if request.path == '/student' or _STUDENT_API_RE.match(request.path):
        if not session.get('student_id'):
            if request.path.startswith('/api/'):
                return jsonify({"error": "not authenticated as a student"}), 401
            return redirect('/student-login')
        return
    if not _authed():
        if request.path.startswith('/api/'):
            return jsonify({"error": "not authenticated"}), 401
        return redirect('/login')


def json_api(fn):
    """Mirrors admin_server.py's single try/except around the whole do_POST
    dispatch, but per-route since Flask routes are separate functions."""
    @functools.wraps(fn)
    def wrapper(*a, **kw):
        try:
            return jsonify(fn(*a, **kw))
        except admin_core.ApiError as e:
            return jsonify({"error": e.msg}), e.code
        except KeyError as e:
            return jsonify({"error": f"missing required field: {e}"}), 400
        except Exception as e:
            return jsonify({"error": f"{type(e).__name__}: {e}"}), 500
    return wrapper


@app.route('/')
@app.route('/index.html')
def index():
    return render_admin_html(hosted=True)


@app.route('/dashboard.html')
@app.route('/student.html')
@app.route('/app/dashboard.html')
@app.route('/app/student.html')
def static_html():
    # Read-only curriculum/tracker views -- static build output, shipped as
    # part of the deployment bundle (app/), never written to at runtime. Both
    # the bare and /app/-prefixed paths are registered because a case page's
    # "Back to My Cases" link is a relative ../../../app/student.html, which
    # is correct from cases/<id>/published/ but resolves under /app/ once
    # hosted -- see the /cases/... route below.
    return send_from_directory(_APP_DIR, request.path.rsplit('/', 1)[-1])


@app.route('/student-<learner_id>.html')
@app.route('/app/student-<learner_id>.html')
def student_html(learner_id):
    # One role-locked build per learner (see build_dashboard.py's
    # student_file_path()). Same scoping discipline as case_interactive_html()
    # below: learner_id is attacker-controlled, so it's checked against the
    # exact slug shape the builder emits before ever touching the filesystem.
    if not re.match(r'^[a-z0-9][a-z0-9-]*$', learner_id):
        return jsonify({"error": "not found"}), 404
    filename = f'student-{learner_id}.html'
    if not os.path.isfile(os.path.join(_APP_DIR, filename)):
        return jsonify({"error": "not found"}), 404
    return send_from_directory(_APP_DIR, filename)


@app.route('/cases/<case_id>/published/<filename>')
def case_interactive_html(case_id, filename):
    # The student-facing case files (Interactive.html, Case Study.docx,
    # Data.xlsx) -- deliberately NOT behind the admin passcode (see
    # require_auth() above): a student doing the actual work has no admin
    # login, and never should need one. Scoped tightly on purpose:
    # published/ folders also hold guide-only material (Facilitator Guide,
    # Guide Notes .docx) that must never be reachable here -- see
    # admin_core.is_student_published_file()'s own docstring for the
    # audience check this relies on, and its 2026-08-21 fix notes for why
    # this route used to reject every non-Interactive.html file, breaking
    # the dashboard's own docx/xlsx download links for the entire corpus.
    #
    # Diagnosed 2026-08-12: Vercel's Python WSGI adapter hands Flask a
    # PATH_INFO that is still percent-encoded (e.g. "...Robotics%20Engineer
    # %20-%20Interactive.html"), which violates the WSGI spec (PATH_INFO
    # must already be decoded) -- Werkzeug trusts that and never decodes
    # it, so every filename containing a space (all of them) failed the
    # suffix check below and 404'd before ever touching the filesystem.
    # Decoding defensively here is a no-op on a normal, already-decoded
    # string, so this is safe regardless of which WSGI server is in front.
    case_id = unquote(case_id)
    filename = unquote(filename)
    if '/' in case_id or '..' in case_id or '/' in filename or '..' in filename \
            or not admin_core.is_student_published_file(case_id, filename):
        return jsonify({"error": "not found"}), 404
    directory = os.path.join(_CASES_DIR, case_id, 'published')
    path = os.path.join(directory, filename)
    if not os.path.isfile(path):
        return jsonify({"error": "not found"}), 404
    return send_from_directory(directory, filename)


@app.route('/api/state')
def api_state():
    try:
        return jsonify(admin_core.build_state(get_store()))
    except Exception as e:
        return jsonify({"error": f"{type(e).__name__}: {e}"}), 500


@app.route('/api/learners/csv-template')
def api_csv_template():
    return Response(admin_core.CSV_TEMPLATE, mimetype='text/csv',
                     headers={'Content-Disposition': 'attachment; filename="learners-template.csv"'})


@app.route('/api/suggest-cases')
def api_suggest_cases():
    lid = request.args.get('learner_id')
    if not lid:
        return jsonify({"error": "learner_id is required"}), 400
    try:
        return jsonify({"suggestions": admin_core.suggest_cases(get_store(), lid)})
    except admin_core.ApiError as e:
        return jsonify({"error": e.msg}), e.code


@app.route('/api/learner/self-assessment', methods=['POST'])
@json_api
def api_self_assessment():
    b = request.get_json(force=True) or {}
    admin_core.do_set_self_assessment(get_store(), b['learner_id'], b.get('interests', []),
                                       b.get('note'), b.get('captured_by'),
                                       b.get('grade_level'), b.get('current_branch'))
    return {"ok": True}


@app.route('/api/learner/self-assessment/review', methods=['POST'])
@json_api
def api_self_assessment_review():
    b = request.get_json(force=True) or {}
    admin_core.do_review_self_assessment(get_store(), b['learner_id'], b.get('reviewed_by'))
    return {"ok": True}


@app.route('/api/upload', methods=['POST'])
@json_api
def api_upload():
    f = request.files.get('file')
    if not f:
        raise admin_core.ApiError(400, "no file in upload")
    fields = {k: v for k, v in request.form.items()}
    files = [('file', f.filename, f.read())]
    path = admin_core.do_upload(get_store(), fields, files)
    return {"ok": True, "path": path}


@app.route('/api/learners/bulk-csv', methods=['POST'])
@json_api
def api_bulk_csv():
    f = request.files.get('file')
    if not f:
        raise admin_core.ApiError(400, "no CSV file in upload")
    text = f.read().decode('utf-8-sig', 'replace')
    added, skipped = admin_core.do_bulk_add_learners_csv(get_store(), text)
    return {"ok": True, "added": added, "skipped": skipped}


@app.route('/api/learner/add', methods=['POST'])
@json_api
def api_learner_add():
    b = request.get_json(force=True) or {}
    lid, passcode = admin_core.do_add_learner(get_store(), b.get('display_name'), b.get('program'),
                                               b.get('cohort'), b.get('status'), b.get('id'), b.get('goals'))
    return {"ok": True, "id": lid, "passcode": passcode}


@app.route('/api/learner/goals', methods=['POST'])
@json_api
def api_learner_goals():
    b = request.get_json(force=True) or {}
    admin_core.do_set_learner_goals(get_store(), b['learner_id'], b.get('goals'))
    return {"ok": True}


@app.route('/api/learner/passcode/reset', methods=['POST'])
@json_api
def api_learner_passcode_reset():
    b = request.get_json(force=True) or {}
    passcode = admin_core.do_reset_passcode(get_store(), b['learner_id'])
    return {"ok": True, "passcode": passcode}


@app.route('/api/class-dashboard')
def api_class_dashboard():
    try:
        return jsonify(admin_core.build_class_dashboard(get_store()))
    except Exception as e:
        return jsonify({"error": f"{type(e).__name__}: {e}"}), 500


@app.route('/api/learner/status', methods=['POST'])
@json_api
def api_learner_status():
    b = request.get_json(force=True) or {}
    admin_core.do_set_learner_status(get_store(), b['learner_id'], b['status'])
    return {"ok": True}


@app.route('/api/learner/delete', methods=['POST'])
@json_api
def api_learner_delete():
    b = request.get_json(force=True) or {}
    counts = admin_core.do_delete_learner(get_store(), b['learner_id'])
    return {"ok": True, "removed": counts}


@app.route('/api/assign', methods=['POST'])
@json_api
def api_assign():
    b = request.get_json(force=True) or {}
    aid = admin_core.do_assign(get_store(), b['learner_id'], b['case_id'], b.get('due_on'),
                                b.get('badge_index'), b.get('assigned_by'))
    return {"ok": True, "id": aid}


@app.route('/api/assign/withdraw', methods=['POST'])
@json_api
def api_withdraw():
    b = request.get_json(force=True) or {}
    admin_core.do_withdraw(get_store(), b['assignment_id'])
    return {"ok": True}


@app.route('/api/submission/record', methods=['POST'])
@json_api
def api_record_submission():
    b = request.get_json(force=True) or {}
    sid = admin_core.do_record_submission(get_store(), b['learner_id'], b['case_id'], b.get('artifacts', {}),
                                           b.get('source'))
    return {"ok": True, "id": sid}


@app.route('/api/discussion/add', methods=['POST'])
@json_api
def api_discussion_add():
    b = request.get_json(force=True) or {}
    did, n = admin_core.do_add_discussion(get_store(), b['learner_id'], b['case_id'], b.get('date'),
                                           b.get('mode', 'live'), b.get('recorded_by'), b.get('note'))
    return {"ok": True, "id": did, "count": n}


@app.route('/api/review', methods=['POST'])
@json_api
def api_review():
    b = request.get_json(force=True) or {}
    admin_core.do_review(get_store(), b['submission_id'], b['outcome'], b.get('review_note'), b.get('reviewed_by'))
    return {"ok": True}


@app.route('/api/complete', methods=['POST'])
@json_api
def api_complete():
    b = request.get_json(force=True) or {}
    admin_core.do_complete(get_store(), b['assignment_id'], b.get('badge_index'))
    return {"ok": True}


@app.route('/api/score', methods=['POST'])
@json_api
def api_score():
    b = request.get_json(force=True) or {}
    out = admin_core.do_score(get_store(), b['learner_id'], b['case_id'], b.get('file_paths', []), b.get('note'))
    return {"ok": True, "report": out}


@app.route('/api/guide-confirm', methods=['POST'])
@json_api
def api_guide_confirm():
    b = request.get_json(force=True) or {}
    out = admin_core.do_guide_confirm(get_store(), b['learner_id'], b['case_id'], b.get('by'),
                                       b.get('overrides', []), b.get('scored_on'))
    return {"ok": True, "report": out}


@app.route('/api/badge/award', methods=['POST'])
@json_api
def api_badge_award():
    b = request.get_json(force=True) or {}
    admin_core.do_award_badge(get_store(), b['learner_id'], b['badge_index'], b.get('awarded_by'))
    return {"ok": True}


# ------------------------------------------------------------ student portal
@app.route('/student')
def student_portal():
    return render_student_portal_html()


@app.route('/api/student/state')
def api_student_state():
    try:
        return jsonify(admin_core.build_student_state(get_store(), session['student_id']))
    except admin_core.ApiError as e:
        return jsonify({"error": e.msg}), e.code


@app.route('/api/student/submit', methods=['POST'])
@json_api
def api_student_submit():
    # learner_id is deliberately never read from the request body -- always the
    # session's own id, so a student can only ever submit as themselves. Same
    # reuse of do_record_submission as the guide-facing /api/submission/record;
    # calling it again on an already-'reviewed' assignment (outcome revise/
    # not-accepted) is exactly how a resubmission after feedback works.
    b = request.get_json(force=True) or {}
    sid = admin_core.do_record_submission(get_store(), session['student_id'], b['case_id'],
                                           b.get('artifacts', {}), 'student-portal')
    return {"ok": True, "id": sid}


@app.route('/api/student/self-assessment', methods=['POST'])
@json_api
def api_student_self_assessment():
    b = request.get_json(force=True) or {}
    admin_core.do_set_self_assessment(get_store(), session['student_id'], b.get('interests', []),
                                       b.get('note'), 'student', b.get('grade_level'), b.get('current_branch'))
    return {"ok": True}


@app.route('/api/student/rate', methods=['POST'])
@json_api
def api_student_rate():
    b = request.get_json(force=True) or {}
    rid = admin_core.do_rate_case(get_store(), session['student_id'], b['case_id'], b.get('stars'), b.get('note'))
    return {"ok": True, "id": rid}


# --------------------------------------------------------- weekly class ----
# See admin_core.py's "weekly class cases" section for why this is a
# separate, simpler lane from the roster/assignment/rubric flow above: one
# link per case, a walk-up student types their name, no login. HTML lives in
# class_html.py, shared with app/admin_server.py's local route for the same
# page (same reuse pattern as admin_html.py/student_portal_html.py).
import html as _html

from class_html import render_class_case_html, render_class_review_html


@app.route('/class/<case_id>')
def class_case_page(case_id):
    try:
        case = admin_core.get_case_brief(case_id)
    except admin_core.ApiError as e:
        return f"<p>{_html.escape(e.msg)}</p>", e.code
    return render_class_case_html(case)


@app.route('/api/class-submit', methods=['POST'])
@json_api
def api_class_submit():
    case_id = request.form.get('case_id', '')
    student_name = request.form.get('student_name', '')
    answer_text = request.form.get('answer_text', '')
    pf = request.files.get('photo')
    photo_file = (pf.filename, pf.read()) if pf and pf.filename else None
    df = request.files.get('pdf')
    pdf_file = (df.filename, df.read()) if df and df.filename else None
    sid = admin_core.do_class_submit(get_store(), case_id, None, student_name, answer_text, photo_file, pdf_file)
    return {"ok": True, "id": sid}


@app.route('/class-review')
def class_review_page():
    case_id = request.args.get('case_id') or None
    rows = admin_core.do_list_class_submissions(get_store(), case_id)
    # Real titles for the group headers -- get_case_brief() raises on a
    # since-unpublished/renamed case, so a lookup miss falls back to the bare
    # slug (handled by render_class_review_html itself) rather than 500ing
    # the whole review page over one stale case_id.
    case_titles = {}
    for cid in {r['case_id'] for r in rows}:
        try:
            case_titles[cid] = admin_core.get_case_brief(cid)['title']
        except admin_core.ApiError:
            pass
    weekly_debrief = admin_core.do_get_weekly_debrief(get_store())
    return render_class_review_html(rows, case_id, case_titles, weekly_debrief)


@app.route('/api/weekly-debrief', methods=['POST'])
@json_api
def api_set_weekly_debrief():
    b = request.get_json(force=True) or {}
    admin_core.do_set_weekly_debrief(get_store(), b.get('label'), b.get('url'))
    return {"ok": True}


@app.route('/class-review/export')
def class_review_export():
    case_id = request.args.get('case_id')
    if not case_id:
        return jsonify({"error": "case_id is required"}), 400
    try:
        text = admin_core.do_export_case_debrief_bundle(get_store(), case_id)
    except admin_core.ApiError as e:
        return f"<p>{_html.escape(e.msg)}</p>", e.code
    return Response(text, mimetype='text/plain; charset=utf-8', headers={
        'Content-Disposition': f'attachment; filename="{case_id}-submissions.txt"'})


@app.route('/api/class-review', methods=['POST'])
@json_api
def api_class_review():
    b = request.get_json(force=True) or {}
    admin_core.do_review_class_submission(get_store(), b['submission_id'], b.get('review_note'), 'guide')
    return {"ok": True}


@app.route('/class-photo/<path:rel_path>')
def class_photo(rel_path):
    # Same Vercel WSGI quirk documented on case_interactive_html() above:
    # PATH_INFO arrives still percent-encoded (e.g. a filename with spaces
    # stays "%20"), which violates the WSGI spec, so Werkzeug's normal
    # auto-decode never runs and rel_path shows up literally containing
    # "%20" instead of a space -- a guaranteed DB lookup miss. Decoding
    # defensively here is a no-op on an already-decoded string (local dev),
    # so it's safe regardless of which WSGI server is in front.
    rel_path = unquote(rel_path)
    data = get_store().get_submitted_file(rel_path)
    if data is None:
        return jsonify({"error": "not found"}), 404
    import mimetypes
    ctype = mimetypes.guess_type(rel_path)[0] or 'application/octet-stream'
    return Response(data, mimetype=ctype)
