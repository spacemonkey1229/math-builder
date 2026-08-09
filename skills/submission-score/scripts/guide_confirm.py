#!/usr/bin/env python3
"""
guide_confirm — the human promotion step, and the ONLY writer of
readmodel/score_overrides.json.

    python3 skills/submission-score/scripts/guide_confirm.py \
        --learner avery-n --case cold-chain --by "M. Patel" \
        --override C3=Proficient --reason "Hero declared their own assumption" \
        [--override C7=Exemplary --reason "..."] [--write]

Flips a `machine-first-pass` record to `confirmed`, records WHO confirmed and
WHAT they overrode, and appends every override to readmodel/score_overrides.json.

WHY THE LOG EXISTS.  Overrides are the training signal. A criterion the machine
gets wrong is invisible one submission at a time and obvious across forty. Run
`--audit` to see the per-criterion override rate; **a criterion the machine gets
wrong more than ~30% of the time should be demoted to "guide only"** — removed
from the machine first pass entirely rather than left producing a verdict a guide
has to undo. Silently tolerating a 40%-wrong criterion is worse than not scoring
it, because it anchors the guide.
"""
import argparse, datetime, json, os, shutil, sys

LEVELS = {"Not Yet": 0, "Proficient": 70, "Exemplary": 100}
WEIGHTS = {"C1": 5, "C2": 20, "C3": 20, "C4": 15, "C5": 15, "C6": 15, "C7": 10}
DEMOTE_AT = 0.30
MIN_N = 8          # below this, a rate is noise, not a signal


def snapshot(project, filenames):
    """MCS-22 -- nothing is superseded silently. Same pattern as case-reconcile's
    snapshot(): copy the frozen file to readmodel/_snapshots/<file>.<timestamp>
    before this script overwrites it."""
    ts = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    snap_dir = os.path.join(project, 'readmodel', '_snapshots')
    os.makedirs(snap_dir, exist_ok=True)
    for fn in filenames:
        src = os.path.join(project, 'readmodel', fn)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(snap_dir, f"{fn}.{ts}"))


def load(project):
    sp = os.path.join(project, 'readmodel', 'submissions.json')
    op = os.path.join(project, 'readmodel', 'score_overrides.json')
    subs = json.load(open(sp, encoding='utf-8'))
    ovr = json.load(open(op, encoding='utf-8')) if os.path.exists(op) else {"overrides": []}
    return sp, op, subs, ovr


def find_duplicate_ids(overrides):
    """score_overrides.json's own schema declares id 'Unique.' A flat JSON array
    doesn't enforce that -- Postgres does (score_overrides.id is a primary key,
    see scripts/migrate_to_neon.py) -- so this has to be checked by hand.
    Returns {id: count} for every id that appears more than once."""
    seen = {}
    for o in overrides:
        seen[o['id']] = seen.get(o['id'], 0) + 1
    return {k: v for k, v in seen.items() if v > 1}


def next_override_id(overrides, learner, case, date, criterion):
    """<learner>__<case>__<date>__<criterion>, with a numeric suffix for a second
    (or third...) override of the same criterion for the same learner/case on the
    same day -- e.g. two scoring runs (two submissions) confirmed on the same
    date. Without the suffix these collide (see D-016 in DECISIONS.md)."""
    base = f"{learner}__{case}__{date}__{criterion}"
    prior = sum(1 for o in overrides
                if o.get('learner_id') == learner and o.get('case_id') == case
                and o.get('criterion') == criterion and o.get('on') == date)
    return base if prior == 0 else f"{base}__{prior + 1}"


def audit(project, write=False):
    """Compute the per-criterion override rate and, per MCS-31, ACTUALLY demote
    any criterion crossing DEMOTE_AT at n >= MIN_N — not just print a suggestion.

    Enforcement point: writes readmodel/demoted_criteria.json. score_submission.py
    reads this file and refuses to guess on a demoted criterion (see MCS-31 and
    the HARD LIMIT block in score_submission.py). Without --write this is report-only,
    matching the previous (unenforced) behaviour.
    """
    _, _, subs, ovr = load(project)
    real = [o for o in ovr.get('overrides', []) if not o.get('_example')]
    scored = [s for s in subs.get('scores', []) if s.get('status') == 'confirmed']
    n = len(scored)

    dupes = find_duplicate_ids(ovr.get('overrides', []))
    if dupes:
        print(f"ID COLLISION — {len(dupes)} id(s) shared by more than one row "
              f"(violates score_overrides.json's own 'id: Unique' invariant):")
        for did, count in dupes.items():
            print(f"  {did!r} appears {count} times")
        print()

    print(f"OVERRIDE AUDIT — {n} confirmed record(s), {len(real)} override(s)")
    if n < MIN_N:
        print(f"  n = {n} < {MIN_N}. Rates below this are noise. Reporting counts only.\n")
    print(f"{'crit':<5} {'overrides':>9} {'rate':>7}  disposition")
    demoted = {}
    for k in WEIGHTS:
        c = sum(1 for o in real if o.get('criterion') == k)
        rate = (c / n) if n else 0.0
        if n < MIN_N:
            disp = "insufficient data"
        elif rate > DEMOTE_AT:
            disp = f"DEMOTE TO GUIDE ONLY — machine wrong {rate:.0%} > {DEMOTE_AT:.0%}"
            demoted[k] = {"rate": round(rate, 3), "n": n, "overrides": c,
                          "demoted_on": datetime.date.today().isoformat()}
        elif rate > DEMOTE_AT * 0.66:
            disp = "watch"
        else:
            disp = "ok"
        print(f"{k:<5} {c:>9} {rate:>6.0%}  {disp}")
    dirs = {}
    for o in real:
        dirs.setdefault(o.get('criterion'), []).append((o.get('from'), o.get('to')))
    print("\nDIRECTION OF ERROR (this is the bias, and it is the point):")
    for k, v in sorted(dirs.items()):
        up = sum(1 for a, b in v if LEVELS.get(b, 0) > LEVELS.get(a, 0))
        print(f"  {k}: {up} raised, {len(v) - up} lowered  "
              f"-> machine reads {'HARSH' if up > len(v) - up else 'GENEROUS'} on {k}")
    if not real:
        print("  (no real overrides yet — the example row is excluded from every count)")

    dc_path = os.path.join(project, 'readmodel', 'demoted_criteria.json')
    if write:
        snapshot(project, ['demoted_criteria.json'])
        doc = {
            "_schema": {
                "purpose": "MCS-31 enforcement record. Populated only by "
                           "`guide_confirm.py --audit --write`, never by hand. "
                           "score_submission.py reads this file at the start of every "
                           "scoring run and refuses to auto-score a listed criterion — "
                           "it emits level:null, confidence:GUIDE_ONLY instead of a guess.",
                "demoted": "criterion -> {rate, n, overrides, demoted_on}. Presence in "
                           "this dict IS the demotion. Removing a key un-demotes it "
                           "(e.g. after the detector is fixed) — do that by hand, "
                           "deliberately, with a DECISIONS.md row."
            },
            "demoted": demoted,
            "last_audit": {"n_confirmed": n, "n_overrides": len(real),
                           "run_on": datetime.date.today().isoformat()}
        }
        json.dump(doc, open(dc_path, 'w', encoding='utf-8'), indent=1)
        if demoted:
            print(f"\nWROTE {dc_path} — DEMOTED: {', '.join(demoted)}")
        else:
            print(f"\nWROTE {dc_path} — no criterion crosses the threshold yet "
                  f"(n={n} confirmed record(s)).")


def check_unique(project):
    """Regression check: exit 1 if any two rows in score_overrides.json share an
    id. Standalone (no --write side effects) so it's safe to run in a Tier-1-style
    gate. Root cause fixed in next_override_id(); this guards the data itself,
    including rows written before that fix (see D-016 in DECISIONS.md)."""
    _, _, _, ovr = load(project)
    rows = ovr.get('overrides', [])
    dupes = find_duplicate_ids(rows)
    if dupes:
        print(f"FAIL — {len(dupes)} duplicate id(s) among {len(rows)} override row(s):")
        for did, count in dupes.items():
            print(f"  {did!r} appears {count} times")
        sys.exit(1)
    print(f"PASS — {len(rows)} override row(s), all ids unique")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--learner'); ap.add_argument('--case')
    ap.add_argument('--by'); ap.add_argument('--scored-on', default=None)
    ap.add_argument('--override', action='append', default=[], metavar='Cn=Level')
    ap.add_argument('--reason', action='append', default=[])
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--audit', action='store_true')
    ap.add_argument('--check', action='store_true',
                    help='regression check: exit 1 if score_overrides.json has duplicate ids')
    a = ap.parse_args()

    if a.check:
        check_unique(a.project); return
    if a.audit:
        audit(a.project, write=a.write); return
    for req in ('learner', 'case', 'by'):
        if not getattr(a, req):
            sys.exit(f"--{req} is required (or use --audit)")

    sp, op, subs, ovr = load(a.project)
    recs = [s for s in subs.get('scores', [])
            if s['learner_id'] == a.learner and s['case_id'] == a.case
            and (a.scored_on is None or s['scored_on'] == a.scored_on)]
    if not recs:
        sys.exit(f"no score record for {a.learner} / {a.case}. Run score_submission.py --write first.")
    rec = sorted(recs, key=lambda s: s['scored_on'])[-1]
    if rec['status'] == 'confirmed':
        print(f"NOTE: already confirmed by {rec['confirmed_by']} on {rec['confirmed_on']}. "
              f"Re-confirming appends, it does not erase.")

    today = datetime.date.today().isoformat()
    if len(a.reason) not in (0, len(a.override)):
        sys.exit("give one --reason per --override. An unexplained override is not a training "
                 "signal, it is noise.")
    applied = []
    for i, spec in enumerate(a.override):
        k, _, new = spec.partition('=')
        k, new = k.strip(), new.strip()
        if k not in WEIGHTS:
            sys.exit(f"unknown criterion {k!r}")
        if new not in LEVELS:
            sys.exit(f"unknown level {new!r}; use Not Yet / Proficient / Exemplary")
        old = rec['criteria'][k]['level']
        reason = a.reason[i] if i < len(a.reason) else None
        if not reason:
            sys.exit(f"override {k} has no --reason")
        rec['criteria'][k]['level'] = new
        rec['criteria'][k]['set_by'] = 'guide'
        applied.append({"criterion": k, "from": old, "to": new, "reason": reason})
        oid = next_override_id(ovr.setdefault('overrides', []), a.learner, a.case, today, k)
        ovr['overrides'].append({
            "id": oid,
            "learner_id": a.learner, "case_id": a.case, "score_id": rec['id'],
            "criterion": k, "machine_level": old, "guide_level": new,
            "from": old, "to": new,
            "machine_confidence": rec['criteria'][k].get('confidence'),
            "reason": reason, "by": a.by, "on": today})

    rec['status'] = 'confirmed'
    rec['confirmed_by'] = a.by
    rec['confirmed_on'] = today
    rec['overrides'] = rec.get('overrides', []) + applied
    rec['badge_eligible'] = all(LEVELS[rec['criteria'][k]['level']] >= 70 for k in WEIGHTS)
    rec['growth_score'] = round(
        sum(WEIGHTS[k] * LEVELS[rec['criteria'][k]['level']] for k in WEIGHTS) / 100.0, 1)

    print(f"CONFIRM  {a.learner} / {a.case}  by {a.by} on {today}")
    for o in applied:
        print(f"  override {o['criterion']}: {o['from']} -> {o['to']}   ({o['reason']})")
    if not applied:
        print("  no overrides — the machine pass was accepted as written")
    print(f"  badge_eligible = {rec['badge_eligible']}   growth_score = {rec['growth_score']}")
    print(f"  status = confirmed")

    if a.write:
        snapshot(a.project, ['submissions.json', 'score_overrides.json'])
        json.dump(subs, open(sp, 'w', encoding='utf-8'), indent=2)
        json.dump(ovr, open(op, 'w', encoding='utf-8'), indent=2)
        print(f"\nWROTE {sp}\nWROTE {op}")
    else:
        print("\n(dry run — pass --write to persist)")


if __name__ == '__main__':
    main()
