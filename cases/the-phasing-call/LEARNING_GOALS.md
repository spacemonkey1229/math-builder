# LEARNING GOALS — The Phasing Call

Bidirectional deliverable ↔ skill matrix, per `skills/case-write/SKILL.md` step 10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 polar-to-rectangular conversion of the tracked station position | pre-calculus-polar-coordinate, pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates |
| D2 parametric position equations x(t), y(t) for each profile | pre-calculus-parametric-equation, pre-calculus-parameter |
| D3 eliminate-the-parameter rectangular equation + intercept-time check | pre-calculus-how-to-eliminate-the-parameter-to-find-a-rectangular-equation |
| D4 autonomous-flight/consumables-reserve percent calculation | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 graphed polar boundary of each profile's phase-angle tolerance band | pre-calculus-how-to-graph-a-polar-equation, pre-calculus-polar-coordinate |
| D6 launch-window calendar calculation (days per 30-day window) | measurement-how-to-convert-an-amount-with-compound-units |
| D7 primary-metric comparison table (hours reserve per calendar day of flexibility) | advanced-numbers-how-to-find-the-percent-of-a-number, measurement-how-to-convert-an-amount-with-compound-units |
| D8 recommendation, defended and flip-tested (re-derives the D7 ratio under a changed input to find the flip point) | advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
deliverables: 8    claimed skills: 9    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

- Every claimed skill in `standards[]` is forced by at least one deliverable above.
- Every deliverable D1–D8 maps to at least one claimed skill. D8 (the recommendation) reuses
  `advanced-numbers-how-to-find-the-percent-of-a-number` because stating "what would have to
  change...to flip" requires recomputing D7's ratio under a changed input, not a fresh skill —
  matching the pattern in `the-transfer-window`'s own D6 and `the-search-box`'s own D5.
- `pre-calculus-how-to-graph-a-polar-equation` is forced specifically by D5 (the graphed
  phase-angle-tolerance-band polar boundary) — without D5 this skill would be an UNREACHABLE
  SKILL claim, the same defect the-search-box's own D4 (graphed polar boundary) exists to avoid.
- `new_coverage` is honestly `0` — see `case.json`'s `reinforcement_note` for the full SPEC §8
  carve-out justification (the entire Pre-Calculus/Polar And Parametric group is already at n=1,
  covered by `Feedback`, and this case's real deliverables reach exactly those 6 skills and no
  adjacent uncovered one).
