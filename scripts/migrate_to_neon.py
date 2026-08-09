#!/usr/bin/env python3
"""
scripts/migrate_to_neon.py — one-time seed: local readmodel/*.json + student_work/**
-> Neon Postgres, via the exact same app/store_postgres.py the live app uses.

Run once, by hand, right after Neon is provisioned (DATABASE_URL set in the
environment or passed via --database-url). Safe to re-run: it applies the
schema with CREATE TABLE IF NOT EXISTS, then does the same full-replace writes
PostgresStore.save() always does, so re-running just re-syncs from the current
local JSON files rather than duplicating rows.

_example-flagged rows are skipped (same as every other reader in this
project — admin_core.live()).

Usage:
    DATABASE_URL=postgresql://... python3 scripts/migrate_to_neon.py
    python3 scripts/migrate_to_neon.py --database-url postgresql://...
"""
import argparse, json, os, sys

APP_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app')
sys.path.insert(0, APP_DIR)

import admin_core  # noqa: E402
from store_postgres import PostgresStore  # noqa: E402

PROJECT_ROOT = os.path.dirname(APP_DIR)


def apply_schema(store):
    schema_path = os.path.join(PROJECT_ROOT, 'sql', 'schema.sql')
    with open(schema_path, encoding='utf-8') as f:
        ddl = f.read()
    with store._conn() as conn:
        with conn.cursor() as cur:
            cur.execute(ddl)
        conn.commit()
    print(f"[schema] applied {schema_path}")


def load_local(name):
    path = os.path.join(PROJECT_ROOT, 'readmodel', name)
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def migrate_programs(store, roster):
    with store._conn() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM programs")
            for pid, p in roster['programs'].items():
                cur.execute(
                    "INSERT INTO programs (id, badges, cases_per_badge, cases_required) VALUES (%s,%s,%s,%s)",
                    (pid, p['badges'], p['cases_per_badge'], p['cases_required']))
        conn.commit()
    print(f"[programs] {len(roster['programs'])} rows")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--database-url', default=None, help='defaults to $DATABASE_URL')
    ap.add_argument('--skip-schema', action='store_true', help='skip CREATE TABLE step (schema already applied)')
    ap.add_argument('--skip-files', action='store_true', help='skip uploading student_work/** file bytes')
    a = ap.parse_args()

    store = PostgresStore(dsn=a.database_url)

    if not a.skip_schema:
        apply_schema(store)

    roster_raw = load_local('roster.json')
    migrate_programs(store, roster_raw)
    roster = {"programs": roster_raw['programs'], "learners": admin_core.live(roster_raw['learners'])}
    store.save('roster.json', roster)
    print(f"[learners] {len(roster['learners'])} rows")

    subs_raw = load_local('submissions.json')
    subs = {
        "assignments": admin_core.live(subs_raw['assignments']),
        "submissions": admin_core.live(subs_raw['submissions']),
        "discussions": admin_core.live(subs_raw['discussions']),
        "scores": [s for s in subs_raw.get('scores', []) if not s.get('_example')],
    }
    store.save('submissions.json', subs)
    print(f"[assignments] {len(subs['assignments'])} rows")
    print(f"[submissions] {len(subs['submissions'])} rows")
    print(f"[discussions] {len(subs['discussions'])} rows")
    print(f"[scores] {len(subs['scores'])} rows")

    ov_path = os.path.join(PROJECT_ROOT, 'readmodel', 'score_overrides.json')
    if os.path.exists(ov_path):
        ov_raw = load_local('score_overrides.json')
        live_overrides = [o for o in ov_raw.get('overrides', []) if not o.get('_example')]
        # FIXED at the source (D-016, DECISIONS.md): guide_confirm.py's next_override_id()
        # now appends a __2/__3/... suffix when the same learner/case/criterion is
        # overridden again on the same date, so new rows shouldn't collide. This dedup
        # stays as a safety net for readmodel data written before the fix, or hand-edited
        # -- the flat JSON array doesn't enforce uniqueness (arrays never do);
        # score_overrides.id is a real Postgres primary key here, so it must be unique
        # before the INSERT. Both rows are real training signal (this file's own header:
        # "OVERRIDES ARE THE TRAINING SIGNAL") -- disambiguate rather than drop one.
        seen = {}
        for o in live_overrides:
            seen[o['id']] = seen.get(o['id'], 0) + 1
            if seen[o['id']] > 1:
                dup_id = o['id']
                o['id'] = f"{dup_id}__dup{seen[dup_id]}"
                print(f"[score_overrides] WARNING: id collision on {dup_id!r} -- "
                      f"renamed duplicate to {o['id']!r} (see guide_confirm.py id scheme)")
        store.save('score_overrides.json', {"overrides": live_overrides})
        print(f"[score_overrides] {len(live_overrides)} rows")

    dc_path = os.path.join(PROJECT_ROOT, 'readmodel', 'demoted_criteria.json')
    if os.path.exists(dc_path):
        store.save('demoted_criteria.json', load_local('demoted_criteria.json'))
        print("[demoted_criteria] synced")

    if not a.skip_files:
        sw_root = os.path.join(PROJECT_ROOT, 'student_work')
        n = 0
        for learner_id in sorted(os.listdir(sw_root)):
            learner_dir = os.path.join(sw_root, learner_id)
            if not os.path.isdir(learner_dir):
                continue  # skip loose top-level docs like UAT_LOG.md, DEMO_SCRIPT.md
            for case_id in sorted(os.listdir(learner_dir)):
                case_dir = os.path.join(learner_dir, case_id)
                if not os.path.isdir(case_dir):
                    continue
                for root, _, files in os.walk(case_dir):
                    for fn in files:
                        full = os.path.join(root, fn)
                        rel = os.path.relpath(full, PROJECT_ROOT)
                        with open(full, 'rb') as f:
                            content = f.read()
                        store.write_submitted_file(rel, learner_id, case_id, content)
                        n += 1
        print(f"[submitted_files] {n} files")

    print("\nMigration complete.")


if __name__ == '__main__':
    main()
