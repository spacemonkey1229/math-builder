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
import functools, os, sys

_APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_ROOT_DIR = os.path.dirname(_APP_DIR)
_CASES_DIR = os.path.join(_ROOT_DIR, 'cases')
if _APP_DIR not in sys.path:
    sys.path.insert(0, _APP_DIR)

import admin_core
from admin_html import render_admin_html
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
    session.clear()
    return redirect('/login')


@app.before_request
def require_auth():
    if request.path in ('/login', '/logout') or request.path.startswith('/static') \
            or request.path.startswith('/cases/'):
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


@app.route('/cases/<case_id>/published/<filename>')
def case_interactive_html(case_id, filename):
    # The student-facing interactive case page -- deliberately NOT behind
    # the admin passcode (see require_auth() above): a student doing the
    # actual work has no admin login, and never should need one. Scoped
    # tightly on purpose: published/ folders also hold guide-only material
    # (Facilitator Guide, Guide Notes .docx) that must never be reachable
    # here, so only an exact "<...> Interactive.html" filename with no path
    # separators in either segment is servable -- everything else 404s.
    if '/' in case_id or '..' in case_id or '/' in filename or '..' in filename \
            or not filename.endswith(' - Interactive.html'):
        return jsonify({"error": "not found"}), 404
    directory = os.path.join(_CASES_DIR, case_id, 'published')
    path = os.path.join(directory, filename)
    if not os.path.isfile(path):
        case_json = os.path.join(_CASES_DIR, case_id, 'case.json')
        return jsonify({
            "error": "not found", "_debug": True,
            "cases_dir_exists": os.path.isdir(_CASES_DIR),
            "cases_dir_listing": sorted(os.listdir(_CASES_DIR)) if os.path.isdir(_CASES_DIR) else None,
            "case_json_exists": os.path.isfile(case_json),
            "case_dir_listing": sorted(os.listdir(os.path.join(_CASES_DIR, case_id))) if os.path.isdir(os.path.join(_CASES_DIR, case_id)) else None,
            "published_dir_exists": os.path.isdir(directory),
            "published_listing": sorted(os.listdir(directory)) if os.path.isdir(directory) else None,
        }), 404
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
    lid = admin_core.do_add_learner(get_store(), b.get('display_name'), b.get('program'), b.get('cohort'),
                                     b.get('status'), b.get('id'))
    return {"ok": True, "id": lid}


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
