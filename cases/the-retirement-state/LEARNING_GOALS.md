# Learning Goals: The Retirement State

Bidirectional deliverable <-> skill matrix (case-write step 10). "Forces" test: could a competent student produce the deliverable correctly without ever performing the skill? If yes, the mapping is fake and the skill is not claimed.

| Deliverable | Skills it forces (spine ids) | Why it is forced |
|---|---|---|
| D1 rates table | measurement-ratio; measurement-proportion; measurement-how-to-find-a-missing-amount-in-a-proportion; advanced-numbers-how-to-convert-numbers-to-percents; advanced-numbers-how-to-divide-with-negative-numbers; advanced-numbers-negative-number | A crude rate is the ratio of deaths to residents scaled to a population of 100,000 (a missing amount in a proportion); the signed percent difference from the U.S. needs (rate - U.S. rate) / U.S. rate, which divides a negative number by a positive one for Florida's age-adjusted rate and Georgia's crude rate. |
| D2 gaps and the age factor | measurement-ratio; advanced-numbers-how-to-convert-numbers-to-percents | The age factor is crude / age-adjusted, a ratio of two rates; the gap is stated as a percent of the higher rate. |
| D3 box plots of 51 jurisdictions | statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data; statistics-and-probability-box-and-whisker-plot; statistics-and-probability-quartiles; statistics-and-probability-median; statistics-and-probability-outlier; number-sense-how-to-compare-two-or-more-values | The student builds both plots from 51 raw values (median-of-halves quartiles, 1.5 x IQR fences, outliers) and ranks Florida and Georgia on each basis. |
| D4 the earlier years | number-sense-how-to-compare-two-or-more-values; advanced-numbers-how-to-convert-numbers-to-percents | Two comparisons per year (which state is higher on each basis) and the gap as a percent of the higher rate. |

Dropped from the concept sheet: `advanced-numbers-how-to-multiply-with-negative-numbers` (it was forced only by a signed excess-deaths deliverable, which SPEC 6 does not allow; no rates-based deliverable multiplies a negative number).

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 12    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Reinforcement, not new coverage: every one of the 322 spine skills has n >= 1 (checked against `readmodel/standards_spine.json` on 2026-10-28), so no skill can honestly sit in `new_coverage[]`; see `case.json.reinforcement_note`. The thinnest skills claimed are `how-to-create-a-box-and-whisker-plot` (n=1) and `how-to-divide-with-negative-numbers` (n=2). The divide-with-negatives claim is honest but thin: it is forced by D1's signed percent differences, not by the dilemma itself.
