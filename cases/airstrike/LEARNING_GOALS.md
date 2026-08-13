# Learning Goals — Airstrike

Bidirectional deliverable <-> skill matrix (case-write SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 coordinate table & plotted diagram | geometry-coordinate-plane, geometry-x-axis, geometry-y-axis, geometry-origin, geometry-quadrant, geometry-coordinate-pair-also-ordered-pair, geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane |
| D2 flight-path distances | geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane, geometry-pythagorean-theorem, geometry-right-triangle, geometry-hypotenuse, measurement-distance |
| D3 flight-path times | measurement-time, measurement-how-to-convert-an-amount-with-compound-units, measurement-how-to-convert-between-units-of-time, measurement-how-to-find-elapsed-time, measurement-how-to-round-a-number-to-a-specified-place-value |
| D4 sites not reached / population impact | advanced-numbers-how-to-convert-numbers-to-percents, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-how-to-add-multi-digit-numbers, statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-how-to-determine-the-probability-of-a-single-event |
| D5 bar graph | number-sense-bar-graph |
| D6 recommendation | number-sense-how-to-compare-two-or-more-values |

## Forces test applied

For each mapping above: *could a competent student produce this deliverable correctly without ever
performing this skill?* — No, checked individually:

- **D1** cannot be produced without plotting real ordered pairs on a labeled x/y coordinate plane
  and naming each point's quadrant relative to the origin.
- **D2** cannot be produced without applying the distance formula (itself the Pythagorean theorem
  on the right triangle formed by the coordinate differences) between every consecutive pair of
  points on a route.
- **D3** cannot be produced without converting the F-16's km/h speed into a compound km/min rate,
  converting that into elapsed minutes per leg, and rounding to a stated place value.
- **D4** cannot be produced without multiplying a population figure by a decimal survival
  probability (94.4%, the complement of the 5.6% intercept event) and summing multi-digit
  population totals across sites.
- **D5** cannot be produced without constructing an actual bar graph comparing two operations'
  totals.
- **D6** cannot be produced without directly comparing two computed totals and stating which is
  larger and by how much.

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 26    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage` is genuinely 0 for this legacy conversion — see `case.json.new_coverage_note` for
the skill-by-skill check that confirmed no claimed skill had `n == 0` in the spine, and the search
of every plausibly-related spine group that turned up only one unrelated `n == 0` skill
(`number-sense-depth`) in the entire spine. This case closes no coverage gap; it is being converted
for its own pedagogical value (coordinate-plane routing + compound-unit rate + probability-discount
reasoning under real hardware specs) and because SPEC.md §6 explicitly names it as a case worth
converting well rather than retiring.
