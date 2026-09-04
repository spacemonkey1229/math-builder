#!/usr/bin/env python3
"""
admin_server.py — local-only admin UI for managing students.

Introduces the one deviation TECH_STACK.md flags for a future decision: a
local HTTP server. Needed because "manage students" means real writes to
readmodel/roster.json + submissions.json, and real subprocess calls to
skills/submission-score/scripts/*.py — neither of which a static file://
page can do. Still no hosting, no deploy, no multi-user auth: binds to
127.0.0.1 only, one operator, one machine, the same "runs locally, opened by
the person running it" spirit as the rest of the stack. See DECISIONS.md D-015.

Run:
    python3 app/admin_server.py [--port 8420] [--project .]

Then open http://127.0.0.1:8420/ in a browser. Stop with Ctrl-C.

This is a thin HTTP-routing shim over app/admin_core.py, which holds the
actual case-track/submission-score rules and is store-agnostic (see
app/store_local.py). A second, hosted variant (app/admin_web/app.py, backed
by Neon Postgres via app/store_postgres.py) runs the exact same admin_core
logic behind a live Vercel URL -- see DECISIONS.md for that decision. This
file stays the zero-dependency, no-network-required local path.
"""
import argparse, json, os, re, sys, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import admin_core
from admin_html import render_admin_html
from class_html import render_class_case_html, render_class_review_html
from store_local import LocalFileStore

STORE = None  # set in main()
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(APP_DIR)
CASES_DIR = os.path.join(ROOT_DIR, 'cases')
STATIC_HTML = {
    '/dashboard.html': 'dashboard.html', '/student.html': 'student.html',
    '/app/dashboard.html': 'dashboard.html', '/app/student.html': 'student.html',
}


def _student_html_path(learner_id):
    """One role-locked build per learner, e.g. student-ben-okafor.html --
    build_dashboard.py writes these next to the shared, data-free landing
    page at student.html. learner_id comes straight off the URL, so it's
    restricted to the same slug shape build_dashboard.py emits."""
    if not re.match(r'^[a-z0-9][a-z0-9-]*$', learner_id):
        return None
    path = os.path.join(APP_DIR, f'student-{learner_id}.html')
    return path if os.path.isfile(path) else None


def _case_html_path(case_id, filename):
    """Same scoping as admin_web/app.py's case_interactive_html(): only the
    student-audience files under cases/<id>/published/ (Interactive.html,
    Case Study.docx, Data.xlsx -- see admin_core.is_student_published_file())
    are servable -- published/ also holds guide-only .docx material that must
    never be reachable this way."""
    if '/' in case_id or '..' in case_id or '/' in filename or '..' in filename \
            or not admin_core.is_student_published_file(case_id, filename):
        return None
    path = os.path.join(CASES_DIR, case_id, 'published', filename)
    return path if os.path.isfile(path) else None


# --------------------------------------------------------------- server ----
class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _json(self, code, obj):
        body = json.dumps(obj).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get('Content-Length', 0) or 0)
        raw = self.rfile.read(length) if length else b'{}'
        try:
            return json.loads(raw or b'{}')
        except json.JSONDecodeError:
            raise admin_core.ApiError(400, "malformed JSON body")

    def _serve_page(self):
        body = render_admin_html(hosted=False).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_html_file(self, path, missing_msg):
        if not os.path.isfile(path):
            return self._json(404, {"error": missing_msg})
        with open(path, 'rb') as f:
            body = f.read()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    _CONTENT_TYPES = {
        '.html': 'text/html; charset=utf-8',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    }

    def _serve_case_file(self, path, missing_msg):
        # Like _serve_html_file, but for cases/<id>/published/* -- now also
        # docx/xlsx (see admin_core.is_student_published_file()), which need
        # their own Content-Type and a download disposition rather than the
        # inline text/html every other route here serves.
        if not os.path.isfile(path):
            return self._json(404, {"error": missing_msg})
        with open(path, 'rb') as f:
            body = f.read()
        ext = os.path.splitext(path)[1].lower()
        content_type = self._CONTENT_TYPES.get(ext, 'application/octet-stream')
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        if ext != '.html':
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(path)}"')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = urllib.parse.urlparse(self.path)
        if p.path in ('/', '/index.html'):
            return self._serve_page()
        if p.path in STATIC_HTML:
            filename = STATIC_HTML[p.path]
            return self._serve_html_file(os.path.join(APP_DIR, filename),
                                          f"{filename} not built yet -- run app/build_dashboard.py")
        m = re.match(r'^/cases/([^/]+)/published/([^/]+)$', urllib.parse.unquote(p.path))
        if m:
            path = _case_html_path(m.group(1), m.group(2))
            if path is None:
                return self._json(404, {"error": "not found"})
            return self._serve_case_file(path, "not found")
        m = re.match(r'^/(?:app/)?student-([^/]+)\.html$', urllib.parse.unquote(p.path))
        if m:
            path = _student_html_path(m.group(1))
            if path is None:
                return self._json(404, {"error": "not found"})
            return self._serve_html_file(path, "not found")
        m = re.match(r'^/class/([a-z0-9][a-z0-9-]*)$', urllib.parse.unquote(p.path))
        if m:
            try:
                case = admin_core.get_case_brief(m.group(1))
            except admin_core.ApiError as e:
                return self._json(e.code, {"error": e.msg})
            body = render_class_case_html(case).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            return self.wfile.write(body)
        if p.path == '/class-review':
            qs = urllib.parse.parse_qs(p.query)
            case_id = (qs.get('case_id') or [None])[0]
            rows = admin_core.do_list_class_submissions(STORE, case_id)
            case_titles = {}
            for cid in {r['case_id'] for r in rows}:
                try:
                    case_titles[cid] = admin_core.get_case_brief(cid)['title']
                except admin_core.ApiError:
                    pass
            weekly_debrief = admin_core.do_get_weekly_debrief(STORE)
            body = render_class_review_html(rows, case_id, case_titles, weekly_debrief).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            return self.wfile.write(body)
        if p.path == '/class-review/export':
            qs = urllib.parse.parse_qs(p.query)
            case_id = (qs.get('case_id') or [None])[0]
            if not case_id:
                return self._json(400, {"error": "case_id is required"})
            try:
                text = admin_core.do_export_case_debrief_bundle(STORE, case_id)
            except admin_core.ApiError as e:
                return self._json(e.code, {"error": e.msg})
            body = text.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Disposition', f'attachment; filename="{case_id}-submissions.txt"')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            return self.wfile.write(body)
        m = re.match(r'^/class-photo/(.+)$', urllib.parse.unquote(p.path))
        if m:
            data = STORE.get_submitted_file(m.group(1))
            if data is None:
                return self._json(404, {"error": "not found"})
            import mimetypes
            ctype = mimetypes.guess_type(m.group(1))[0] or 'application/octet-stream'
            self.send_response(200)
            self.send_header('Content-Type', ctype)
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            return self.wfile.write(data)
        if p.path == '/api/state':
            try:
                return self._json(200, admin_core.build_state(STORE))
            except Exception as e:
                return self._json(500, {"error": f"{type(e).__name__}: {e}"})
        if p.path == '/api/suggest-cases':
            qs = urllib.parse.parse_qs(p.query)
            lid = (qs.get('learner_id') or [None])[0]
            if not lid:
                return self._json(400, {"error": "learner_id is required"})
            try:
                return self._json(200, {"suggestions": admin_core.suggest_cases(STORE, lid)})
            except admin_core.ApiError as e:
                return self._json(e.code, {"error": e.msg})
        if p.path == '/api/class-dashboard':
            try:
                return self._json(200, admin_core.build_class_dashboard(STORE))
            except Exception as e:
                return self._json(500, {"error": f"{type(e).__name__}: {e}"})
        if p.path == '/api/learners/csv-template':
            body = admin_core.CSV_TEMPLATE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/csv; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="learners-template.csv"')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            return self.wfile.write(body)
        self._json(404, {"error": "not found"})

    def do_POST(self):
        p = urllib.parse.urlparse(self.path)
        try:
            if p.path == '/api/upload':
                ct = self.headers.get('Content-Type', '')
                length = int(self.headers.get('Content-Length', 0) or 0)
                raw = self.rfile.read(length)
                fields, files = admin_core.parse_multipart(raw, ct)
                path = admin_core.do_upload(STORE, fields, files)
                return self._json(200, {"ok": True, "path": path})

            if p.path == '/api/class-submit':
                ct = self.headers.get('Content-Type', '')
                length = int(self.headers.get('Content-Length', 0) or 0)
                raw = self.rfile.read(length)
                fields, files = admin_core.parse_multipart(raw, ct)
                by_name = {name: (filename, data) for name, filename, data in files}
                sid = admin_core.do_class_submit(STORE, fields.get('case_id'), None,
                                                  fields.get('student_name'), fields.get('answer_text'),
                                                  by_name.get('photo'), by_name.get('pdf'))
                return self._json(200, {"ok": True, "id": sid})

            if p.path == '/api/learners/bulk-csv':
                ct = self.headers.get('Content-Type', '')
                length = int(self.headers.get('Content-Length', 0) or 0)
                raw = self.rfile.read(length)
                fields, files = admin_core.parse_multipart(raw, ct)
                if not files:
                    raise admin_core.ApiError(400, "no CSV file in upload")
                _, _, data = files[0]
                added, skipped = admin_core.do_bulk_add_learners_csv(STORE, data.decode('utf-8-sig', 'replace'))
                return self._json(200, {"ok": True, "added": added, "skipped": skipped})

            b = self._read_json()
            if p.path == '/api/learner/add':
                lid, passcode = admin_core.do_add_learner(STORE, b.get('display_name'), b.get('program'),
                                                            b.get('cohort'), b.get('status'), b.get('id'),
                                                            b.get('goals'))
                self._json(200, {"ok": True, "id": lid, "passcode": passcode})
            elif p.path == '/api/learner/goals':
                admin_core.do_set_learner_goals(STORE, b['learner_id'], b.get('goals'))
                self._json(200, {"ok": True})
            elif p.path == '/api/learner/passcode/reset':
                passcode = admin_core.do_reset_passcode(STORE, b['learner_id'])
                self._json(200, {"ok": True, "passcode": passcode})
            elif p.path == '/api/learner/status':
                admin_core.do_set_learner_status(STORE, b['learner_id'], b['status'])
                self._json(200, {"ok": True})
            elif p.path == '/api/learner/delete':
                counts = admin_core.do_delete_learner(STORE, b['learner_id'])
                self._json(200, {"ok": True, "removed": counts})
            elif p.path == '/api/learner/self-assessment':
                admin_core.do_set_self_assessment(STORE, b['learner_id'], b.get('interests', []),
                                                   b.get('note'), b.get('captured_by'),
                                                   b.get('grade_level'), b.get('current_branch'))
                self._json(200, {"ok": True})
            elif p.path == '/api/learner/self-assessment/review':
                admin_core.do_review_self_assessment(STORE, b['learner_id'], b.get('reviewed_by'))
                self._json(200, {"ok": True})
            elif p.path == '/api/assign':
                aid = admin_core.do_assign(STORE, b['learner_id'], b['case_id'], b.get('due_on'),
                                            b.get('badge_index'), b.get('assigned_by'))
                self._json(200, {"ok": True, "id": aid})
            elif p.path == '/api/assign/withdraw':
                admin_core.do_withdraw(STORE, b['assignment_id'])
                self._json(200, {"ok": True})
            elif p.path == '/api/submission/record':
                sid = admin_core.do_record_submission(STORE, b['learner_id'], b['case_id'], b.get('artifacts', {}),
                                                        b.get('source'))
                self._json(200, {"ok": True, "id": sid})
            elif p.path == '/api/discussion/add':
                did, n = admin_core.do_add_discussion(STORE, b['learner_id'], b['case_id'], b.get('date'),
                                                        b.get('mode', 'live'), b.get('recorded_by'), b.get('note'))
                self._json(200, {"ok": True, "id": did, "count": n})
            elif p.path == '/api/review':
                admin_core.do_review(STORE, b['submission_id'], b['outcome'], b.get('review_note'),
                                      b.get('reviewed_by'))
                self._json(200, {"ok": True})
            elif p.path == '/api/complete':
                admin_core.do_complete(STORE, b['assignment_id'], b.get('badge_index'))
                self._json(200, {"ok": True})
            elif p.path == '/api/score':
                out = admin_core.do_score(STORE, b['learner_id'], b['case_id'], b.get('file_paths', []),
                                           b.get('note'))
                self._json(200, {"ok": True, "report": out})
            elif p.path == '/api/guide-confirm':
                out = admin_core.do_guide_confirm(STORE, b['learner_id'], b['case_id'], b.get('by'),
                                                    b.get('overrides', []), b.get('scored_on'))
                self._json(200, {"ok": True, "report": out})
            elif p.path == '/api/badge/award':
                admin_core.do_award_badge(STORE, b['learner_id'], b['badge_index'], b.get('awarded_by'))
                self._json(200, {"ok": True})
            elif p.path == '/api/class-review':
                admin_core.do_review_class_submission(STORE, b['submission_id'], b.get('review_note'), 'guide')
                self._json(200, {"ok": True})
            elif p.path == '/api/weekly-debrief':
                admin_core.do_set_weekly_debrief(STORE, b.get('label'), b.get('url'))
                self._json(200, {"ok": True})
            else:
                self._json(404, {"error": "not found"})
        except admin_core.ApiError as e:
            self._json(e.code, {"error": e.msg})
        except KeyError as e:
            self._json(400, {"error": f"missing required field: {e}"})
        except Exception as e:
            self._json(500, {"error": f"{type(e).__name__}: {e}"})


def main():
    global STORE
    ap = argparse.ArgumentParser()
    ap.add_argument('--port', type=int, default=8420)
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--host', default='127.0.0.1', help='binds to localhost only by default -- do not change '
                                                          'this without adding auth first')
    a = ap.parse_args()
    project = os.path.abspath(a.project)
    for req in ('readmodel/roster.json', 'readmodel/submissions.json', 'readmodel/cases_index.json'):
        if not os.path.exists(os.path.join(project, req)):
            sys.exit(f"missing {req} under {project} -- run with --project pointing at the Math Builder root")
    STORE = LocalFileStore(project)
    srv = ThreadingHTTPServer((a.host, a.port), Handler)
    print(f"Math Builder Admin — http://{a.host}:{a.port}/   (project: {project})")
    print("Local only. Ctrl-C to stop.")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == '__main__':
    main()
