# Learning Goals — Insurance

Bidirectional deliverable ↔ skill matrix (case-write §10). "Forces" test applied strictly: could a
competent student produce this deliverable correctly without ever performing this skill? If yes,
the mapping is fake and was cut.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total premium budget for each option | measurement-currency, advanced-numbers-decimal, advanced-numbers-how-to-multiply-decimal-numbers, basic-operations-multiplication |
| D2 — total out-of-pocket budget for each option + each plan's stated out-of-pocket maximum | measurement-currency, advanced-numbers-decimal, advanced-numbers-decimal-number, basic-operations-addition, advanced-numbers-how-to-add-decimal-numbers, advanced-numbers-how-to-subtract-decimal-numbers, advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-percent, advanced-numbers-how-to-convert-percents-to-numbers, advanced-numbers-how-to-find-the-percent-of-a-number, number-sense-how-to-compare-two-or-more-values |
| D3 — probability-and-mean justification for expected unplanned visits | statistics-and-probability-probability, statistics-and-probability-event, statistics-and-probability-outcome, statistics-and-probability-theoretical-probability, statistics-and-probability-experimental-probability, statistics-and-probability-how-to-determine-the-probability-of-a-single-event, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data |
| D4 — original algorithm with variables/constants/coefficients | advanced-operations-variable, advanced-operations-constant, advanced-operations-coefficient, advanced-operations-term, advanced-operations-expression, advanced-operations-how-to-evaluate-a-variable-expression-substitution-property, advanced-numbers-how-to-convert-numbers-to-percents |
| D5 — bar graph (total cost) + pie chart / cap comparison | number-sense-bar-graph, statistics-and-probability-pie-chart, number-sense-data, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 32    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**new_coverage note:** this is a legacy conversion. All 32 claimed skills were already tagged to
"Health Insurance" in `readmodel/standards_spine.json`'s `covered_by[]` from the prior corpus pass
(percent, decimal arithmetic, probability, mean, and the variable/constant/coefficient/term
vocabulary group all list "Health Insurance" directly), or are directly forced by D4's algorithm
deliverable even where the exact id (`advanced-operations-expression`, n=4) is currently credited
to other cases' titles instead — case-write may claim any spine-valid skill in `standards[]`, not
only ones already tagged to this title; the `n==0` requirement applies specifically to
`new_coverage[]`, not to `standards[]` as a whole. Every one of the candidate skills already has
`n >= 1` — none had `n == 0`. `new_coverage[]` is genuinely empty and reported plainly rather than
padded: this legacy case closes no net-new gap in the standards spine, it reinforces skills the
corpus already covers elsewhere.
