#!/usr/bin/env python3
"""
cohort_rollup — which criteria did the GROUP struggle with?

    python3 skills/submission-score/scripts/cohort_rollup.py --case cold-chain
    python3 skills/submission-score/scripts/cohort_rollup.py --case cold-chain --cohort 2026-fall-adventure

A criterion where most of a cohort lands Not Yet is feedback on the CASE, not on
the learners.  If eleven of fourteen Heroes fail C4, the deliverables are
ambiguous.  If most fail C5, the case never showed them what an original visual
looks like.  If most fail C7, the case gave them no reason to notice the metric
was theirs to choose — or, per RUBRIC's own open question, C7 is simply too hard
at this tier and the criterion is wrong, not the Heroes.

Output ends with the line that matters: what to hand back to `case-readiness`.
"""
import argparse, json, os
from collections import Counter

WEIGHTS = {"C1": 5, "C2": 20, "C3": 20, "C4": 15, "C5": 15, "C6": 15, "C7": 10}
NAMES = {"C1": "research link", "C2": "the pitch", "C3": "correctness", "C4": "deliverables",
         "C5": "visual + appendix", "C6": "discussion", "C7": "framing the question"}
# criterion -> what a cohort-wide failure implicates in the CASE
CASE_IMPLICATION = {
    "C1": "Appendix G's 'how to…' list may not map to anything findable online — check the labels.",
    "C2": "the dilemma may not feel like a real fork; if nobody can take a side, the balance test "
          "passed on paper only. Re-run Tier 2 probe 2 (both-sides solve).",
    "C3": "the appendix data may be ambiguous, or an unstated convention is forcing different "
          "answers. Re-run Tier 2 probe 5 (assumption sensitivity) and probe 1 (cold solve).",
    "C4": "Challenge 3's deliverables are ambiguous or under-specified. This is the most directly "
          "fixable case defect on the list.",
    "C5": "the case never modelled what an ORIGINAL visual looks like, or its own appendices are "
          "so chart-shaped that copying is the path of least resistance.",
    "C6": "more likely a RECORDING gap than a learner gap — C6 depends on data nobody habitually "
          "records. Check the guide's habit before you touch the case.",
    "C7": "either the case gave no reason to question the metric, or — per RUBRIC's open question "
          "— C7 is too hard at this tier and the criterion is wrong, not the Heroes.",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', required=True)
    ap.add_argument('--cohort', default=None)
    ap.add_argument('--project', default=os.getcwd())
    ap.add_argument('--threshold', type=float, default=0.5)
    ap.add_argument('--include-unconfirmed', action='store_true')
    a = ap.parse_args()

    subs = json.load(open(os.path.join(a.project, 'readmodel', 'submissions.json'), encoding='utf-8'))
    roster = json.load(open(os.path.join(a.project, 'readmodel', 'roster.json'), encoding='utf-8'))
    cohort_of = {l['id']: l.get('cohort') for l in roster.get('learners', []) if not l.get('_example')}

    rows = [s for s in subs.get('scores', []) if s['case_id'] == a.case]
    if a.cohort:
        rows = [s for s in rows if cohort_of.get(s['learner_id']) == a.cohort]
    conf = [s for s in rows if s.get('status') == 'confirmed']
    used = rows if a.include_unconfirmed else conf

    print(f"COHORT ROLL-UP — case {a.case}" + (f" · cohort {a.cohort}" if a.cohort else ""))
    print(f"  {len(rows)} score record(s), {len(conf)} confirmed"
          + ("" if a.include_unconfirmed else "; unconfirmed EXCLUDED (use --include-unconfirmed)"))
    if not used:
        print("\nNOTHING TO ROLL UP. Zero is not a finding — it means no confirmed scores exist "
              "for this case yet. Do not read a cohort signal out of an empty set.")
        return

    n = len(used)
    print(f"\n{'crit':<5} {'':<20} {'NotYet':>7} {'Prof':>6} {'Exem':>6} {'%NotYet':>8}  signal")
    struggled = []
    for k in WEIGHTS:
        cnt = Counter(s['criteria'][k]['level'] for s in used)
        ny = cnt['Not Yet']
        frac = ny / n
        sig = ''
        if frac >= a.threshold:
            sig = 'COHORT-WIDE — this is feedback on the CASE'
            struggled.append((k, frac))
        elif frac >= a.threshold / 2:
            sig = 'watch'
        print(f"{k:<5} {NAMES[k]:<20} {ny:>7} {cnt['Proficient']:>6} {cnt['Exemplary']:>6} "
              f"{frac:>7.0%}  {sig}")

    elig = sum(1 for s in used if s.get('badge_eligible'))
    scores = sorted(s['growth_score'] for s in used)
    med = scores[len(scores) // 2]
    print(f"\nmastery gate: {elig}/{n} badge-eligible")
    print(f"growth score: min {scores[0]} · median {med} · max {scores[-1]}   "
          f"(never averaged with the gate, never shown to a learner as a grade)")

    lowconf = Counter()
    for s in used:
        for k in WEIGHTS:
            if s['criteria'][k].get('confidence') == 'LOW':
                lowconf[k] += 1
    if lowconf:
        print("\nmachine LOW-confidence rate (how much of this table is a guess):")
        for k, v in lowconf.most_common():
            print(f"  {k} {v}/{n} = {v/n:.0%}")

    print("\n--- HAND BACK TO case-readiness ---")
    if not struggled:
        print("  nothing cohort-wide. The distribution is about the learners, not the case.")
    for k, frac in sorted(struggled, key=lambda x: -x[1]):
        print(f"  {k} ({NAMES[k]}) — {frac:.0%} Not Yet. {CASE_IMPLICATION[k]}")
    print("\n  File this against the case, not the cohort. A criterion most of a room fails is a "
          "case defect until proven otherwise.")


if __name__ == '__main__':
    main()
