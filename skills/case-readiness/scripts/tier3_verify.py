#!/usr/bin/env python3
"""
TIER 3 — VERIFIED-STATE GATE  (mechanical, blocking)

Wires MCS-29: "a VERIFIED case must have a filed RUN_REPORT before allowing
the VERIFIED state or a doctrine-ledger checkmark." Until this script existed
that rule was CODIFIED prose with no enforcement point — anyone could hand-edit
case.json.qa.state to "VERIFIED" and the ledger would trust it.

    python3 skills/case-readiness/scripts/tier3_verify.py --case cold-chain
    python3 skills/case-readiness/scripts/tier3_verify.py --all

What it checks, per case:
  1. If case.json.qa.state == "VERIFIED", at least one cases/<id>/runs/RUN_*.md
     must exist.
  2. That file must be FILLED, not the blank template — Guide and Date in
     Section 1 must be non-empty and not placeholder underscores.
  3. Section 8 (design-vs-delivery attribution) must have at least one row
     completed — an unfilled Section 8 defeats the entire point of Tier 3
     (see the docstring in templates/RUN_REPORT.md).

A case with qa.state != "VERIFIED" is not checked here — Tiers 1-2 own that.
This script is deliberately narrow: it is the one gate between "someone typed
VERIFIED into a JSON file" and "a doctrine-ledger checkmark is trustworthy."

Exit 0 = every VERIFIED claim in the project is backed by a real run.
Exit 1 = at least one VERIFIED claim has no (or no filled) RUN_REPORT.
"""
import argparse, glob, json, os, re, sys


def find_cases(project):
    return sorted(
        os.path.basename(os.path.dirname(p))
        for p in glob.glob(os.path.join(project, 'cases', '*', 'case.json'))
    )


def check_one(project, case_id):
    cdir = os.path.join(project, 'cases', case_id)
    cj_path = os.path.join(cdir, 'case.json')
    if not os.path.exists(cj_path):
        return {"case": case_id, "state": None, "result": "SKIP", "reason": "no case.json"}

    c = json.load(open(cj_path, encoding='utf-8'))
    state = (c.get('qa') or {}).get('state')

    if state != "VERIFIED":
        return {"case": case_id, "state": state, "result": "N/A",
                "reason": "not claiming VERIFIED — Tier 3 does not apply yet"}

    runs = sorted(glob.glob(os.path.join(cdir, 'runs', 'RUN_*.md')))
    if not runs:
        return {"case": case_id, "state": state, "result": "FAIL",
                "reason": f"qa.state is VERIFIED but no cases/{case_id}/runs/RUN_*.md exists. "
                          f"MCS-29 violated — this checkmark is not earned."}

    problems = []
    for r in runs:
        txt = open(r, encoding='utf-8').read()
        m = re.search(r'\|\s*Guide\s*\|\s*([^|]*)\|', txt)
        guide_val = (m.group(1).strip() if m else "")
        m2 = re.search(r'\|\s*Date\s*\|\s*([^|]*)\|', txt)
        date_val = (m2.group(1).strip() if m2 else "")
        if not guide_val or set(guide_val) <= set('_ '):
            problems.append(f"{os.path.basename(r)}: Section 1 'Guide' field is blank")
        if not date_val or set(date_val) <= set('_ '):
            problems.append(f"{os.path.basename(r)}: Section 1 'Date' field is blank")

        sec8 = re.search(r'##\s*8\s*[—-].*?(?=\n##\s*9|\Z)', txt, re.S)
        if not sec8 or not re.search(r'\|\s*(?:the case|i lost|can\'?t tell)', sec8.group(0), re.I):
            problems.append(f"{os.path.basename(r)}: Section 8 (design-vs-delivery attribution) "
                             f"has no completed row — the run report exists but Tier 3's actual "
                             f"purpose (telling artifact failure from facilitation failure) was "
                             f"never done")

    if problems:
        return {"case": case_id, "state": state, "result": "FAIL",
                "reason": "; ".join(problems)}

    return {"case": case_id, "state": state, "result": "PASS",
            "reason": f"{len(runs)} filled run report(s) on file"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--project', default=os.getcwd())
    a = ap.parse_args()
    if not a.case and not a.all:
        sys.exit("give --case <id> or --all")

    cases = find_cases(a.project) if a.all else [a.case]
    results = [check_one(a.project, c) for c in cases]

    print(f"{'case':<20} {'qa.state':<12} {'result':<6} reason")
    for r in results:
        print(f"{r['case']:<20} {str(r['state']):<12} {r['result']:<6} {r['reason']}")

    failed = [r for r in results if r['result'] == 'FAIL']
    if failed:
        print(f"\nMCS-29 VIOLATED on {len(failed)} case(s). These may NOT be marked ✅ in "
              f"DOCTRINE_LEDGER.md, regardless of what qa.state currently says.")
        sys.exit(1)
    print("\nNo unearned VERIFIED claims found.")
    sys.exit(0)


if __name__ == '__main__':
    main()
