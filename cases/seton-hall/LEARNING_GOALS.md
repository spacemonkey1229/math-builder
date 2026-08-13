# Learning Goals — Seton Hall

Bidirectional deliverable ↔ skill matrix (case-write SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 scatter plot | statistics-and-probability-scatter-plot, statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data, geometry-coordinate-plane, geometry-x-axis, geometry-y-axis, geometry-origin, geometry-coordinate-pair-also-ordered-pair, geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane |
| D2 original algorithm | advanced-operations-operation, advanced-operations-variable, advanced-operations-constant, advanced-operations-coefficient, advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-without-exponents-or, advanced-operations-how-to-evaluate-a-variable-expression-substitution-property, statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data, advanced-numbers-decimal, advanced-numbers-decimal-number |
| D3 ranked table | advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, number-sense-how-to-compare-two-or-more-values |
| D4 rating-differential comparison | advanced-numbers-how-to-subtract-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value, number-sense-greater-than, number-sense-less-than, number-sense-how-to-compare-two-or-more-values |
| D5 recommendation | advanced-numbers-percent, advanced-numbers-how-to-convert-numbers-to-percents, number-sense-how-to-compare-two-or-more-values |

## Test applied

"Forces" = could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- D1 cannot be produced without plotting real ordered pairs on a labeled x/y coordinate plane — every listed skill is mechanically required to draw a correct, labeled scatter plot.
- D2 cannot be produced without defining variables, assigning coefficients, and evaluating a multi-operation expression (the "Power Score" formula) — decimal operations are forced because every Appendix B input column is a decimal.
- D3 cannot be produced without applying D2's formula across 25 rows (repeated decimal add/multiply), rounding the output for a readable table, and comparing/ordering the 25 results — mean/how-to-find-the-mean is forced if a Hero's algorithm averages multiple rank columns (the case's own MA1 curation logic and a common student approach).
- D4 cannot be produced without subtracting two decimal ratings, optionally dividing (e.g. a per-game rate), rounding to one decimal as instructed, and stating a greater-than/less-than comparison in words.
- D5 cannot be produced without converting the AP/NET/Power-Score comparison into a percent-style statement of how close the case is (mirroring case.md's own 6.25% margin) and comparing at least two ranking systems.

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 30    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

`new_coverage` is honestly 0 for this legacy conversion — every claimed skill already has `n > 0` in `readmodel/standards_spine.json` (checked in case.json's `new_coverage_note`). This is not a gap-closing case; it is a real-data, well-balanced (6.25% margin) T3 case whose value is quality and reach, not new coverage. Reported plainly rather than padding `standards[]` to manufacture a false entry.
