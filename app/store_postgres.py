"""app/store_postgres.py — the store adapter backing the hosted Vercel + Neon app.

Maps the same JSON-document shapes app/admin_core.py already operates on
(roster.json's {programs, learners}, submissions.json's four arrays,
score_overrides.json's {overrides}, demoted_criteria.json's {demoted,
last_audit}) onto the normalized tables in sql/schema.sql.

Design notes:
- Every save() is a full DELETE + re-INSERT of the affected table(s), inside one
  transaction. These tables are small (a handful to low hundreds of rows for a
  studio's roster) so this is simple and correct rather than fast-but-fiddly --
  matches the source JSON files' own "the whole document is authoritative on
  every write" semantics, and avoids having to diff old vs. new rows.
- load(name) for anything other than the four mutable documents (roster.json,
  submissions.json, score_overrides.json, demoted_criteria.json) reads a static,
  read-only file bundled with the deployment -- cases_index.json,
  curriculum_tree.json, etc. are build-time content, never written at runtime,
  so they ship as files in the repo rather than living in Postgres. New case
  publishes need a redeploy to become assignable in the live admin app -- a
  known, documented limitation, not an oversight (see DECISIONS.md).
- materialized_project() bridges to score_submission.py / guide_confirm.py,
  which are real subprocess scripts that read/write real files on disk. It
  builds a temp directory shaped like the project root (symlinked read-only
  cases/ + skills/, the four mutable JSON docs written out from Postgres, any
  requested submitted files written out from the submitted_files table), runs
  the script exactly as app/store_local.py's no-op version does, then reads
  the (now-mutated) JSON docs and any new files back out and syncs them into
  Postgres. Vercel Python functions get a writable /tmp, which is all this
  needs.
"""
import contextlib, datetime, json, os, shutil, tempfile

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from admin_core import ApiError

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MUTABLE_DOCS = ('roster.json', 'submissions.json', 'score_overrides.json', 'demoted_criteria.json')


def _to_iso(d):
    return d.isoformat() if d is not None else None


def _to_date(s):
    return datetime.date.fromisoformat(s) if s else None


# Columns added after this table's first deploy. Applied idempotently (ADD COLUMN
# IF NOT EXISTS) the first time a store connects in a given process, same
# statements as sql/schema.sql -- so a live deploy self-migrates on its first
# request instead of needing someone to run psql/migrate_to_neon.py by hand
# against Neon before the new code can work. Safe to re-run.
_MIGRATIONS = (
    "ALTER TABLE learners ADD COLUMN IF NOT EXISTS goals text NOT NULL DEFAULT ''",
    "ALTER TABLE learners ADD COLUMN IF NOT EXISTS passcode text",
    """CREATE TABLE IF NOT EXISTS ratings (
        id         text PRIMARY KEY,
        learner_id text NOT NULL,
        case_id    text NOT NULL,
        stars      int  NOT NULL CHECK (stars BETWEEN 1 AND 5),
        note       text,
        rated_on   date NOT NULL
    )""",
    "CREATE UNIQUE INDEX IF NOT EXISTS ratings_learner_case_uq ON ratings(learner_id, case_id)",
    "CREATE INDEX IF NOT EXISTS ratings_case_idx ON ratings(case_id)",
)


class PostgresStore:
    def __init__(self, dsn=None):
        self.dsn = dsn or os.environ['DATABASE_URL']
        self._ensure_schema()

    def _ensure_schema(self):
        with self._conn() as conn:
            with conn.cursor() as cur:
                for stmt in _MIGRATIONS:
                    cur.execute(stmt)
            conn.commit()

    def _conn(self):
        return psycopg.connect(self.dsn)

    # --------------------------------------------------------- load/save ---
    def load(self, name):
        if name == 'roster.json':
            return self._load_roster()
        if name == 'submissions.json':
            return self._load_submissions()
        if name == 'score_overrides.json':
            return self._load_score_overrides()
        if name == 'demoted_criteria.json':
            return self._load_demoted_criteria()
        return self._load_bundled(name)

    def save(self, name, data):
        if name == 'roster.json':
            return self._save_roster(data)
        if name == 'submissions.json':
            return self._save_submissions(data)
        if name == 'score_overrides.json':
            return self._save_score_overrides(data)
        if name == 'demoted_criteria.json':
            return self._save_demoted_criteria(data)
        raise ValueError(f"{name} is static bundled content -- never written by the admin app")

    def _load_bundled(self, name):
        path = os.path.join(PROJECT_ROOT, 'readmodel', name)
        with open(path, encoding='utf-8') as f:
            return json.load(f)

    # ------------------------------------------------------------ roster ---
    def _load_roster(self):
        with self._conn() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute("SELECT id, badges, cases_per_badge, cases_required, badge_names FROM programs")
                programs = {r['id']: {"badges": r['badges'], "cases_per_badge": r['cases_per_badge'],
                                       "cases_required": r['cases_required'],
                                       **({"badge_names": r['badge_names']} if r['badge_names'] else {})}
                            for r in cur.fetchall()}
                cur.execute("""SELECT id, display_name, program, cohort, status, started_on, badges_earned,
                                      drive_folder_id, drive_folder_url, notes, self_assessment, goals, passcode
                               FROM learners""")
                learners = [{
                    "id": r['id'], "display_name": r['display_name'], "program": r['program'],
                    "cohort": r['cohort'], "status": r['status'], "started_on": _to_iso(r['started_on']),
                    "badges_earned": r['badges_earned'], "drive_folder_id": r['drive_folder_id'],
                    "drive_folder_url": r['drive_folder_url'], "notes": r['notes'],
                    "goals": r['goals'] or '', "passcode": r['passcode'],
                    **({"self_assessment": r['self_assessment']} if r['self_assessment'] is not None else {}),
                } for r in cur.fetchall()]
        return {"programs": programs, "learners": learners}

    def _save_roster(self, data):
        # programs is static config admin_core never mutates -- only learners is
        # ever actually different from what's already stored.
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM learners")
                for l in data['learners']:
                    sa = l.get('self_assessment')
                    cur.execute(
                        """INSERT INTO learners (id, display_name, program, cohort, status, started_on,
                                                  badges_earned, drive_folder_id, drive_folder_url, notes,
                                                  self_assessment, goals, passcode)
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (l['id'], l['display_name'], l['program'], l.get('cohort'), l['status'],
                         _to_date(l['started_on']), Jsonb(l.get('badges_earned', [])),
                         l.get('drive_folder_id'), l.get('drive_folder_url'), l.get('notes', ''),
                         Jsonb(sa) if sa is not None else None, l.get('goals', ''), l.get('passcode')))
            conn.commit()

    # ------------------------------------------------------- submissions ---
    def _load_submissions(self):
        with self._conn() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute("""SELECT id, learner_id, case_id, assigned_on, due_on, assigned_by, badge_index,
                                      status, notes FROM assignments""")
                assignments = [{
                    "id": r['id'], "learner_id": r['learner_id'], "case_id": r['case_id'],
                    "assigned_on": _to_iso(r['assigned_on']), "due_on": _to_iso(r['due_on']),
                    "assigned_by": r['assigned_by'], "badge_index": r['badge_index'],
                    "status": r['status'], "notes": r['notes'],
                } for r in cur.fetchall()]

                cur.execute("""SELECT id, assignment_id, learner_id, case_id, submitted_on, artifacts, source,
                                      drive_artifacts, reviewed_on, reviewed_by, review_note, outcome
                               FROM submissions""")
                submissions = [{
                    "id": r['id'], "assignment_id": r['assignment_id'], "learner_id": r['learner_id'],
                    "case_id": r['case_id'], "submitted_on": _to_iso(r['submitted_on']),
                    "artifacts": r['artifacts'], "source": r['source'], "drive_artifacts": r['drive_artifacts'],
                    "reviewed_on": _to_iso(r['reviewed_on']), "reviewed_by": r['reviewed_by'],
                    "review_note": r['review_note'], "outcome": r['outcome'],
                } for r in cur.fetchall()]

                cur.execute("SELECT id, learner_id, case_id, date, mode, recorded_by, note FROM discussions")
                discussions = [{
                    "id": r['id'], "learner_id": r['learner_id'], "case_id": r['case_id'],
                    "date": _to_iso(r['date']), "mode": r['mode'], "recorded_by": r['recorded_by'],
                    "note": r['note'],
                } for r in cur.fetchall()]

                cur.execute("""SELECT id, learner_id, case_id, scored_on, status, criteria, badge_eligible,
                                      growth_score, surface_first, confirmed_by, confirmed_on, overrides, report
                               FROM scores""")
                scores = [{
                    "id": r['id'], "learner_id": r['learner_id'], "case_id": r['case_id'],
                    "scored_on": _to_iso(r['scored_on']), "status": r['status'], "criteria": r['criteria'],
                    "badge_eligible": r['badge_eligible'], "growth_score": float(r['growth_score']),
                    "surface_first": r['surface_first'], "confirmed_by": r['confirmed_by'],
                    "confirmed_on": _to_iso(r['confirmed_on']), "overrides": r['overrides'], "report": r['report'],
                } for r in cur.fetchall()]
                cur.execute("SELECT id, learner_id, case_id, stars, note, rated_on FROM ratings")
                ratings = [{
                    "id": r['id'], "learner_id": r['learner_id'], "case_id": r['case_id'],
                    "stars": r['stars'], "note": r['note'], "rated_on": _to_iso(r['rated_on']),
                } for r in cur.fetchall()]
        return {"assignments": assignments, "submissions": submissions, "discussions": discussions,
                "scores": scores, "ratings": ratings}

    def _save_submissions(self, data):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM assignments")
                for a in data['assignments']:
                    cur.execute(
                        """INSERT INTO assignments (id, learner_id, case_id, assigned_on, due_on, assigned_by,
                                                     badge_index, status, notes)
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (a['id'], a['learner_id'], a['case_id'], _to_date(a['assigned_on']),
                         _to_date(a.get('due_on')), a.get('assigned_by'), a.get('badge_index'), a['status'],
                         a.get('notes')))

                cur.execute("DELETE FROM submissions")
                for s in data['submissions']:
                    cur.execute(
                        """INSERT INTO submissions (id, assignment_id, learner_id, case_id, submitted_on,
                                                     artifacts, source, drive_artifacts, reviewed_on, reviewed_by,
                                                     review_note, outcome)
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (s['id'], s['assignment_id'], s['learner_id'], s['case_id'], _to_date(s['submitted_on']),
                         Jsonb(s.get('artifacts', {})), s['source'],
                         Jsonb(s['drive_artifacts']) if s.get('drive_artifacts') is not None else None,
                         _to_date(s.get('reviewed_on')), s.get('reviewed_by'), s.get('review_note'),
                         s.get('outcome')))

                cur.execute("DELETE FROM discussions")
                for d in data['discussions']:
                    cur.execute(
                        """INSERT INTO discussions (id, learner_id, case_id, date, mode, recorded_by, note)
                           VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                        (d['id'], d['learner_id'], d['case_id'], _to_date(d['date']), d['mode'],
                         d.get('recorded_by'), d.get('note')))

                cur.execute("DELETE FROM scores")
                for s in data.get('scores', []):
                    cur.execute(
                        """INSERT INTO scores (id, learner_id, case_id, scored_on, status, criteria,
                                                badge_eligible, growth_score, surface_first, confirmed_by,
                                                confirmed_on, overrides, report)
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (s['id'], s['learner_id'], s['case_id'], _to_date(s['scored_on']), s['status'],
                         Jsonb(s['criteria']), s['badge_eligible'], s['growth_score'],
                         Jsonb(s.get('surface_first', [])), s.get('confirmed_by'), _to_date(s.get('confirmed_on')),
                         Jsonb(s.get('overrides', [])), s.get('report')))

                cur.execute("DELETE FROM ratings")
                for r in data.get('ratings', []):
                    cur.execute(
                        """INSERT INTO ratings (id, learner_id, case_id, stars, note, rated_on)
                           VALUES (%s,%s,%s,%s,%s,%s)""",
                        (r['id'], r['learner_id'], r['case_id'], r['stars'], r.get('note'),
                         _to_date(r['rated_on'])))
            conn.commit()

    # --------------------------------------------------- score_overrides ---
    def _load_score_overrides(self):
        with self._conn() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute("""SELECT id, learner_id, case_id, score_id, criterion, machine_level, guide_level,
                                      "from", "to", machine_confidence, reason, by, on_date
                               FROM score_overrides""")
                rows = cur.fetchall()
        overrides = [{
            "id": r['id'], "learner_id": r['learner_id'], "case_id": r['case_id'], "score_id": r['score_id'],
            "criterion": r['criterion'], "machine_level": r['machine_level'], "guide_level": r['guide_level'],
            "from": r['from'], "to": r['to'], "machine_confidence": r['machine_confidence'],
            "reason": r['reason'], "by": r['by'], "on": _to_iso(r['on_date']),
        } for r in rows]
        return {"overrides": overrides}

    def _save_score_overrides(self, data):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM score_overrides")
                for o in data.get('overrides', []):
                    cur.execute(
                        """INSERT INTO score_overrides (id, learner_id, case_id, score_id, criterion,
                                                          machine_level, guide_level, "from", "to",
                                                          machine_confidence, reason, by, on_date)
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (o['id'], o['learner_id'], o['case_id'], o['score_id'], o['criterion'],
                         o['machine_level'], o['guide_level'], o['from'], o['to'], o.get('machine_confidence'),
                         o['reason'], o['by'], _to_date(o['on'])))
            conn.commit()

    # ------------------------------------------------------- demoted_crit --
    def _load_demoted_criteria(self):
        with self._conn() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute("SELECT doc FROM demoted_criteria_doc WHERE id = 1")
                row = cur.fetchone()
        if row:
            return row['doc']
        return {"demoted": {}, "last_audit": {"n_confirmed": 0, "n_overrides": 0, "run_on": None}}

    def _save_demoted_criteria(self, data):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO demoted_criteria_doc (id, doc) VALUES (1, %s)
                       ON CONFLICT (id) DO UPDATE SET doc = EXCLUDED.doc""",
                    (Jsonb(data),))
            conn.commit()

    # ------------------------------------------------------------- files ---
    def write_submitted_file(self, path, learner_id, case_id, content, content_type=None):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO submitted_files (path, learner_id, case_id, content, content_type)
                       VALUES (%s,%s,%s,%s,%s)
                       ON CONFLICT (path) DO UPDATE SET content = EXCLUDED.content,
                         content_type = EXCLUDED.content_type, uploaded_on = now()""",
                    (path, learner_id, case_id, content, content_type))
            conn.commit()

    def _fetch_submitted_file(self, path):
        with self._conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT content FROM submitted_files WHERE path = %s", (path,))
                row = cur.fetchone()
        if not row:
            raise ApiError(404, f"submitted file not found: {path}")
        return bytes(row[0])

    # --------------------------------------------------- scoring bridge ----
    @contextlib.contextmanager
    def materialized_project(self, file_paths=None):
        tmp = tempfile.mkdtemp(prefix='mb_')
        try:
            for name, real in (('cases', 'cases'), ('skills', 'skills')):
                dst = os.path.join(tmp, name)
                src = os.path.join(PROJECT_ROOT, real)
                try:
                    os.symlink(src, dst)
                except OSError:
                    shutil.copytree(src, dst)

            rm = os.path.join(tmp, 'readmodel')
            os.makedirs(rm, exist_ok=True)
            for name in MUTABLE_DOCS:
                with open(os.path.join(rm, name), 'w', encoding='utf-8') as f:
                    json.dump(self.load(name), f, indent=2)

            for path in (file_paths or []):
                content = self._fetch_submitted_file(path)
                full = os.path.join(tmp, path)
                os.makedirs(os.path.dirname(full), exist_ok=True)
                with open(full, 'wb') as f:
                    f.write(content)

            yield tmp
        finally:
            rm = os.path.join(tmp, 'readmodel')
            for name in MUTABLE_DOCS:
                p = os.path.join(rm, name)
                if os.path.exists(p):
                    with open(p, encoding='utf-8') as f:
                        self.save(name, json.load(f))

            sw = os.path.join(tmp, 'student_work')
            if os.path.isdir(sw):
                for root, _, files in os.walk(sw):
                    for fn in files:
                        full = os.path.join(root, fn)
                        rel = os.path.relpath(full, tmp)
                        parts = rel.split(os.sep)
                        learner_id = parts[1] if len(parts) > 1 else 'unknown'
                        case_id = parts[2] if len(parts) > 2 else 'unknown'
                        with open(full, 'rb') as f:
                            self.write_submitted_file(rel, learner_id, case_id, f.read())

            shutil.rmtree(tmp, ignore_errors=True)
