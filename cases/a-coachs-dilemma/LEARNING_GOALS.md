# Learning Goals — A Coach's Dilemma

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 real FT%/PPP conversions | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-decimal, number-sense-place-value, basic-operations-division |
| D2 naive "gut check" comparison | statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, number-sense-how-to-compare-two-or-more-values |
| D3 corrected expected-points comparison | statistics-and-probability-dependent-event, statistics-and-probability-conditional-probability, statistics-and-probability-how-to-determine-the-probability-of-a-compound-event, statistics-and-probability-how-to-determine-the-probability-of-conditional-events, advanced-numbers-percent, number-sense-how-to-compare-two-or-more-values |
| D4 foul-budget calculation | basic-operations-division, basic-operations-quotient, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value, number-sense-place-value, number-sense-how-to-compare-two-or-more-values |
| D5 original bar graph | number-sense-bar-graph, basic-operations-division, basic-operations-quotient |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** requires converting real makes/attempts (187/471, 28/73) into percentages (dividing a decimal, then expressing it as a percent) rounded to one decimal place, plus converting a real Offensive Rating (points per 100 possessions) into points per possession by dividing by 100. Genuinely forces `advanced-numbers-percent`, `-how-to-convert-numbers-to-percents`, `-how-to-divide-decimal-numbers`, `advanced-numbers-decimal`, `number-sense-place-value`, `basic-operations-division`.
- **D2** is impossible without recognizing "expected points from two free throws" as an application of probability to a real event/outcome (each free throw is an event with two outcomes, make or miss) and comparing the result to the Clippers' real points-per-possession. Genuinely forces `statistics-and-probability-probability`, `-event`, `-outcome`, `number-sense-how-to-compare-two-or-more-values`.
- **D3** cannot be produced without recognizing that "Jordan misses the second free throw AND the Clippers grab the offensive rebound" is a dependent, conditional sequence (the rebound chance only applies given the miss occurred) — a genuinely different mechanic from a simple independent-event calculation, and requires computing that conditional/compound probability and comparing the corrected total to D2's raw comparison. Genuinely forces `statistics-and-probability-dependent-event`, `-conditional-probability`, `-how-to-determine-the-probability-of-a-compound-event`, `-how-to-determine-the-probability-of-conditional-events`, `advanced-numbers-percent`, `number-sense-how-to-compare-two-or-more-values`.
- **D4** requires using real division/subtraction against the real 6-foul rule (6 fouls minus 4 already accumulated = 2 remaining) and rounding/place-value discipline when recomputing the Clippers' backup-center-adjusted points-per-possession, then comparing that adjusted figure against the case's other numbers. Genuinely forces `basic-operations-division`, `-quotient`, `measurement-rounding`, `-how-to-round-a-number-to-a-specified-place-value`, `number-sense-place-value`, `number-sense-how-to-compare-two-or-more-values`.
- **D5** requires computing/pulling forward division-based percentage and points-per-possession figures from D2-D4 for at least three comparison points and rendering them as bars with labeled axes/categories. Genuinely forces `number-sense-bar-graph`, `basic-operations-division`, `basic-operations-quotient`.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 18    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting: every claimed skill was checked against
`readmodel/standards_spine.json` before writing and none is `n == 0` — this case reinforces skills
the spine already has real coverage for. The full `n == 0` list (dominated by geometry, pre-calculus,
calculus, and discrete-math skills this case's real basketball-analytics math has no honest reach
into) was checked and nothing fit without padding. `new_coverage[]` is `[]`, honestly, per the
reinforcement carve-out on T1-10 (`skills/case-readiness/SKILL.md`, added 2026-08-17) — this case
is a fresh authoring pass, not a legacy conversion, so the legacy-conversion carve-out does not
apply; the reinforcement carve-out is the correct one and `case.json.reinforcement_note` records
the required evidentiary basis for it.
