# Learning Goal Check — Player Of The Year

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 Methodology A composite table (5 z-scores + average, all 14 finalists) | statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-negative-number, advanced-numbers-how-to-subtract-with-negative-numbers, advanced-numbers-how-to-divide-with-negative-numbers, advanced-numbers-how-to-divide-decimal-numbers, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D2 Methodology B composite table (RoleZ, TeamMult, CompositeB, all 14 finalists) | statistics-and-probability-mean, advanced-numbers-negative-number, advanced-numbers-how-to-subtract-with-negative-numbers, advanced-numbers-how-to-divide-with-negative-numbers, advanced-numbers-how-to-multiply-with-negative-numbers, advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-without-exponents-or, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D3 Force ranking, 1–14, under each methodology, side by side | number-sense-how-to-compare-two-or-more-values |
| D4 Two original visual displays comparing the two methodologies | number-sense-bar-graph, statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data |
| D5 Written margin comparison (points and percent gap) between #1/#2 under each methodology | number-sense-how-to-compare-two-or-more-values, advanced-numbers-how-to-divide-decimal-numbers, measurement-rounding |

## Forcing test applied

*Could a competent student produce this deliverable correctly without ever performing this
skill?*

- **D1** cannot be produced without finding the mean of five z-scores (mean, how-to-find-mean),
  computing each z-score as `(value − national mean) / SD` which routinely yields negative
  differences and negative results (negative-number, subtract-with-negatives, divide-with-
  negatives — e.g. Anna Stevenson's Kills/Set z-score is `(2.79 − 2.333) / 0.784`, and several
  finalists' Aces/Set z-scores are steeply negative), dividing decimal quantities throughout, and
  rounding the final composite to a stated, comparable number of decimal places.
- **D2** additionally requires evaluating `TeamMult(RPI) = 1 + 0.5 × (1 − (RPI − 1) / 49)` in the
  correct operation order (order-of-operations) and then multiplying a RoleZ average — which is
  negative for roughly half the field — by that positive multiplier (multiply-with-negatives,
  multiply-decimals).
- **D3** cannot be produced without directly comparing 14 computed values against each other
  under each methodology to assign a rank (compare-two-or-more-values).
- **D4** requires an original bar graph or scatter plot, not a screenshot of the data tables —
  forces bar-graph and scatter-plot construction skills directly.
- **D5** requires computing the point gap and the percent gap between the top two finalists under
  each system and comparing those two gaps to each other (compare-two-or-more-values,
  divide-decimals for the percent-gap calculation, rounding for a reportable percent).

## Result

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 14    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

`new_coverage[]` is empty by design — see `case.json.new_coverage_note` for the full spine check
(no z-score, standard-deviation, weighted-average, or composite-score skill exists anywhere in
`readmodel/standards_spine.json`; every one of this case's 14 claimed skills is genuine
supporting arithmetic/statistics/graphing coverage already present in the spine at n≥1). This
triggers the legacy-conversion carve-out (SPEC §8 / `tier1_structural.py` T1-10), downgrading the
empty-`new_coverage[]` condition from a BLOCKER to a recorded, accepted GAP.
