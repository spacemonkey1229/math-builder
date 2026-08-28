"""app/store_local.py — the store adapter backing the local stdlib admin server.

Thin wrapper around exactly the file I/O admin_server.py always did: read/write
readmodel/*.json on real disk, snapshot before every write (MCS-22), real files
under student_work/. materialized_project() is a no-op context manager -- local
mode already has a real project directory, so there's nothing to bridge.
"""
import contextlib, datetime, json, os, shutil

from admin_core import ApiError


class LocalFileStore:
    def __init__(self, project):
        self.project = project

    def _snapshot(self, filenames):
        ts = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
        snap_dir = os.path.join(self.project, 'readmodel', '_snapshots')
        os.makedirs(snap_dir, exist_ok=True)
        for fn in filenames:
            src = os.path.join(self.project, 'readmodel', fn)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(snap_dir, f"{fn}.{ts}"))

    def load(self, name):
        path = os.path.join(self.project, 'readmodel', name)
        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def save(self, name, data):
        self._snapshot([name])
        path = os.path.join(self.project, 'readmodel', name)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def write_submitted_file(self, path, learner_id, case_id, content, content_type=None):
        full = os.path.join(self.project, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'wb') as f:
            f.write(content)

    def get_submitted_file(self, path):
        full = os.path.join(self.project, path)
        if not os.path.isfile(full):
            return None
        with open(full, 'rb') as f:
            return f.read()

    def _load_class_submissions(self):
        path = os.path.join(self.project, 'readmodel', 'class_submissions.json')
        if not os.path.isfile(path):
            return []
        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def _save_class_submissions(self, rows):
        path = os.path.join(self.project, 'readmodel', 'class_submissions.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(rows, f, indent=2)

    def add_class_submission(self, row):
        rows = self._load_class_submissions()
        rows.append({**row, "submitted_on": datetime.datetime.now().isoformat(),
                     "reviewed_on": None, "reviewed_by": None, "review_note": None})
        self._save_class_submissions(rows)

    def list_class_submissions(self, case_id=None):
        rows = self._load_class_submissions()
        rows = [r for r in rows if not case_id or r['case_id'] == case_id]
        return sorted(rows, key=lambda r: r['submitted_on'], reverse=True)

    def review_class_submission(self, submission_id, review_note, reviewed_by):
        rows = self._load_class_submissions()
        row = next((r for r in rows if r['id'] == submission_id), None)
        if not row:
            raise ApiError(404, f"class submission {submission_id} not found")
        row['reviewed_on'] = datetime.datetime.now().isoformat()
        row['reviewed_by'] = reviewed_by
        row['review_note'] = review_note
        self._save_class_submissions(rows)

    @contextlib.contextmanager
    def materialized_project(self, file_paths=None):
        # Nothing to bridge -- the real project directory already has everything
        # score_submission.py / guide_confirm.py need to read and write.
        yield self.project
