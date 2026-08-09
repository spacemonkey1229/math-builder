"""app/store_local.py — the store adapter backing the local stdlib admin server.

Thin wrapper around exactly the file I/O admin_server.py always did: read/write
readmodel/*.json on real disk, snapshot before every write (MCS-22), real files
under student_work/. materialized_project() is a no-op context manager -- local
mode already has a real project directory, so there's nothing to bridge.
"""
import contextlib, datetime, json, os, shutil


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

    @contextlib.contextmanager
    def materialized_project(self, file_paths=None):
        # Nothing to bridge -- the real project directory already has everything
        # score_submission.py / guide_confirm.py need to read and write.
        yield self.project
