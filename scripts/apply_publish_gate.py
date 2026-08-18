#!/usr/bin/env python3
"""
apply_publish_gate.py -- enforce MCS-41 (the publish gate) across the corpus.

WHY THIS EXISTS
---------------
On 2026-08-01 Cold Chain's status was deliberately corrected `published` -> `qa`
because it had not cleared a confirmed QA threshold. The rule behind that
correction was never written down, and the Aug 4-5 authoring batch then shipped
ten cases straight to `published` at TIER1_PASS -- no `sensitivity_model.py`
(so Tier 2 probe 5 returns NOT RUN), no `QA_REPORT.md`, and in most cases a
single `Interactive.html` instead of the full packet. `status: "published"` is
exactly what `admin_core.py` reads for assignability, so those cases became
assignable in the live admin app at a readiness level the designated proof case
had just been demoted for.

D-020 resolves that by tightening the bar: `published` requires TIER2_PASS.
This script applies it.

WHAT IT DOES
------------
Demotes `published` -> `qa` for every PIPELINE case whose `qa.state` is not
`TIER2_PASS`, in both places that matter:

  * `cases/<id>/case.json`        -- the authoring source of truth
  * `readmodel/cases_index.json`  -- what the app reads for assignability

DESIGN NOTES (these are deliberate)
-----------------------------------
* The demotion set is DERIVED at run time, never hardcoded. The corpus is being
  actively authored; a fixed id list goes stale within minutes.
* Demote only. Promotion is `case-publish`'s job and requires a human confirm
  (MCS-12) -- this script will never move a case UP, even one that now clearly
  qualifies. It names them instead.
* `legacy` cases are out of scope. They are not pipeline output and were never
  claimed to have passed a gate.
* Dry-run is the default. `--confirm` is required to write anything (MCS-12).
* Snapshots every file it touches before writing (MCS-22).
* Idempotent. A second run is a no-op and says so.

USAGE
-----
    python3 scripts/apply_publish_gate.py              # dry run, prints the plan
    python3 scripts/apply_publish_gate.py --confirm     # apply it
"""
import argparse
import datetime
import glob
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES_DIR = os.path.join(ROOT, 'cases')
CASES_INDEX = os.path.join(ROOT, 'readmodel', 'cases_index.json')
SNAPSHOT_DIR = os.path.join(ROOT, 'readmodel', '_snapshots')

# The bar. A case may hold `published` only at this gate state or better.
PASSING_STATES = {'TIER2_PASS', 'TIER3_PASS', 'VERIFIED'}


def load(path):
    with open(path) as fh:
        return json.load(fh)


def snapshot(path):
    """MCS-22 -- snapshot before every write to a frozen file."""
    os.makedirs(SNAPSHOT_DIR, exist_ok=True)
    stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    dest = os.path.join(SNAPSHOT_DIR, f'{os.path.basename(path)}.{stamp}')
    shutil.copy2(path, dest)
    return dest


def gate_state(case_json):
    return ((case_json.get('qa') or {}).get('state')) or 'NONE'


def packet_count(case_id):
    pub = os.path.join(CASES_DIR, case_id, 'published')
    return len(os.listdir(pub)) if os.path.isdir(pub) else 0


def survey():
    """Read every pipeline case on disk and classify it against the gate."""
    rows = []
    for path in sorted(glob.glob(os.path.join(CASES_DIR, '*', 'case.json'))):
        case_id = os.path.basename(os.path.dirname(path))
        try:
            doc = load(path)
        except (json.JSONDecodeError, OSError) as exc:
            # A case mid-write by another session. Never guess at its state.
            rows.append({'id': case_id, 'unreadable': str(exc)})
            continue
        rows.append({
            'id': case_id,
            'path': path,
            'doc': doc,
            'status': doc.get('status'),
            'gate': gate_state(doc),
            'has_model': os.path.exists(
                os.path.join(CASES_DIR, case_id, 'sensitivity_model.py')),
            'has_report': os.path.exists(
                os.path.join(CASES_DIR, case_id, 'QA_REPORT.md')),
            'packet': packet_count(case_id),
            'unreadable': None,
        })
    return rows


def git_dirty(rel_path):
    """True if rel_path has uncommitted modifications -- a concurrent-edit warning."""
    try:
        out = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain', '--', rel_path],
                             capture_output=True, text=True, timeout=15)
        return bool(out.stdout.strip())
    except (OSError, subprocess.SubprocessError):
        return False


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--confirm', action='store_true',
                    help='actually write the demotions (default is a dry run)')
    args = ap.parse_args()

    rows = survey()
    unreadable = [r for r in rows if r['unreadable']]
    readable = [r for r in rows if not r['unreadable']]

    demote = [r for r in readable
              if r['status'] == 'published' and r['gate'] not in PASSING_STATES]
    already_ok = [r for r in readable
                  if r['status'] == 'published' and r['gate'] in PASSING_STATES]
    # Cases that would now qualify but are NOT held at published. Named, never moved.
    could_promote = [r for r in readable
                     if r['status'] != 'published' and r['gate'] in PASSING_STATES]

    print(f'MCS-41 publish gate -- `published` requires qa.state in '
          f'{sorted(PASSING_STATES)}\n')
    print(f'{"case":20}{"status":11}{"qa.state":12}{"model":7}{"report":8}{"packet":7}verdict')
    print('-' * 78)
    for r in sorted(readable, key=lambda x: x['id']):
        if r in demote:
            verdict = 'DEMOTE -> qa'
        elif r in already_ok:
            verdict = 'ok'
        elif r in could_promote:
            verdict = 'eligible (case-publish must promote)'
        else:
            verdict = '-'
        print(f'{r["id"]:20}{str(r["status"]):11}{r["gate"]:12}'
              f'{"yes" if r["has_model"] else "no":7}'
              f'{"yes" if r["has_report"] else "no":8}{r["packet"]:<7}{verdict}')

    for r in unreadable:
        print(f'{r["id"]:20}{"UNREADABLE -- skipped (mid-write?): " + r["unreadable"][:40]}')

    print()
    if could_promote:
        print('Eligible for promotion but deliberately NOT moved by this script '
              '(MCS-12 -- run case-publish):')
        for r in could_promote:
            print(f'  - {r["id"]} (status={r["status"]}, gate={r["gate"]})')
        print()

    if not demote:
        print('Nothing to demote. The gate already holds.')
        return 0

    print(f'{len(demote)} case(s) to demote: {", ".join(r["id"] for r in demote)}')

    if not args.confirm:
        print('\nDRY RUN -- nothing written. Re-run with --confirm to apply.')
        return 0

    # Concurrent-edit guard. Warn loudly; the operator decides.
    if git_dirty('readmodel/cases_index.json'):
        print('\n!! readmodel/cases_index.json has uncommitted changes -- another '
              'session may be mid-write.\n'
              '!! A snapshot will be taken first, but consider waiting until the '
              'tree is quiet.')

    # 1. case.json -- the authoring source of truth.
    for r in demote:
        snapshot(r['path'])
        doc = r['doc']
        doc['status'] = 'qa'
        note = (f'status demoted published -> qa on '
                f'{datetime.date.today().isoformat()} per D-020/MCS-41: gate state '
                f'{r["gate"]} does not meet the published bar (TIER2_PASS).')
        qa = doc.setdefault('qa', {})
        qa['gate_note'] = note
        with open(r['path'], 'w') as fh:
            json.dump(doc, fh, indent=2, ensure_ascii=False)
            fh.write('\n')
        print(f'  wrote {os.path.relpath(r["path"], ROOT)}')

    # 2. cases_index.json -- what the app reads for assignability.
    if os.path.exists(CASES_INDEX):
        snap = snapshot(CASES_INDEX)
        print(f'  snapshot {os.path.relpath(snap, ROOT)}')
        index = load(CASES_INDEX)
        ids = {r['id'] for r in demote}
        touched = 0
        for entry in index.get('cases', []):
            if entry.get('id') in ids and entry.get('status') == 'published':
                entry['status'] = 'qa'
                touched += 1
        with open(CASES_INDEX, 'w') as fh:
            json.dump(index, fh, indent=2, ensure_ascii=False)
            fh.write('\n')
        print(f'  wrote readmodel/cases_index.json ({touched} entries)')

    print('\nDone. Now rebuild the derived views and redeploy for the live app to '
          'see it:\n'
          '  python3 app/build_pipeline.py\n'
          '  python3 app/build_dashboard.py\n'
          '  vercel --prod')
    return 0


if __name__ == '__main__':
    sys.exit(main())
