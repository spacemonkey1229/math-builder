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
from store_local import LocalFileStore

STORE = None  # set in main()
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(APP_DIR)
CASES_DIR = os.path.join(ROOT_DIR, 'cases')
STATIC_HTML = {
    '/dashboard.html': 'dashboard.html', '/student.html': 'student.html',
    '/app/dashboard.html': 'dashboard.html', '/app/student.html': 'student.html',
}


def _case_html_path(case_id, filename):
    """Same scoping as admin_web/app.py's case_interactive_html(): only an
    exact '<...> Interactive.html' file directly under cases/<id>/published/
    is servable -- published/ also holds guide-only .docx material that must
    never be reachable this way."""
    if '/' in case_id or '..' in case_id or '/' in filename or '..' in filename \
            or not filename.endswith(' - Interactive.html'):
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
            return self._serve_html_file(path, "not found")
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
                lid = admin_core.do_add_learner(STORE, b.get('display_name'), b.get('program'), b.get('cohort'),
                                                 b.get('status'), b.get('id'))
                self._json(200, {"ok": True, "id": lid})
            elif p.path == '/api/learner/status':
                admin_core.do_set_learner_status(STORE, b['learner_id'], b['status'])
                self._json(200, {"ok": True})
            elif p.path == '/api/learner/delete':
                counts = admin_core.do_delete_learner(STORE, b['learner_id'])
                self._json(200, {"ok": True, "removed": counts})
            elif p.path == '/api/learner/self-assessment':
                admin_core.do_set_self_assessment(STORE, b['learner_id'], b.get('interests', []),
                                                   b.get('note'), b.get('captured_by'))
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
