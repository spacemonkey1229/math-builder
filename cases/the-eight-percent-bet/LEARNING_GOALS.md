# Learning Goals — The Eight-Percent Bet

Bidirectional deliverable ↔ skill matrix (case-write §10, MCS-10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Debt on the first payment date | advanced-operations-how-to-evaluate-an-exponential-expression, advanced-numbers-how-to-find-the-percent-of-a-number |
| D2 — Repayment schedule three ways | discrete-mathematics-recursive-formula, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence, discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula, calculus-sequence, calculus-series, advanced-operations-how-to-evaluate-an-exponential-expression |
| D3 — Pool-to-debt ratio across history (box plot) | statistics-and-probability-quartiles, statistics-and-probability-box-and-whisker-plot, statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data, statistics-and-probability-median, advanced-operations-how-to-evaluate-an-exponential-expression |
| D4 — Non-overlapping blocks | statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 — What actually happened | advanced-operations-how-to-evaluate-an-exponential-expression, advanced-numbers-how-to-find-the-percent-of-a-number |
| D6 — Shortfall plan at a chosen funding rate | advanced-numbers-how-to-find-the-percent-of-a-number, calculus-series |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 12    new_coverage: 0 (reinforcement_note on file)
UNMAPPED DELIVERABLES: none — every deliverable maps to at least one skill.
UNREACHABLE SKILLS: none — every claimed skill in standards[] is forced by at least one deliverable:
  how-to-evaluate-an-exponential-expression                    -> D1, D2, D3, D5
  how-to-find-the-percent-of-a-number                          -> D1, D4, D5, D6
  recursive-formula                                            -> D2
  how-to-write-a-recursive-formula-for-a-sequence              -> D2
  how-to-convert-a-recursive-formula-to-an-explicit-formula    -> D2
  sequence                                                     -> D2
  series                                                       -> D2, D6
  probability-quartiles                                        -> D3
  probability-box-and-whisker-plot                             -> D3
  probability-how-to-create-a-box-and-whisker-plot-given-a-set -> D3
  probability-median                                           -> D3
  probability-how-to-find-the-mean-of-a-set-of-data            -> D4
RESULT: PASS
```

## Why each thin or low-coverage skill is genuinely forced

- **calculus-series (n=2):** D2(c) requires writing the sum of the discounted payments term by term and collapsing it with the finite geometric-series formula; D6 re-uses the same annuity logic at other rates. A student cannot satisfy D2(c) without the series.
- **how-to-create-a-box-and-whisker-plot (n=1), quartiles, box-and-whisker-plot (n=3):** D3 requires a labeled box plot of the full set of ratios.
- **calculus-sequence, recursive formula, how-to-write-a-recursive-formula, how-to-convert-to-explicit (n=3-4):** D2(a) and D2(b) require the recursion and its explicit form, and the solve for the payment.

## Reinforcement carve-out

All twelve claimed skills already have n>0 in the live spine (no skill anywhere has n==0), so `new_coverage[]` is empty and `case.json.reinforcement_note` records what was checked. "Thin" is n in {1,2} (the spine's `totals.thin_1_2`): this case forces two thin skills (calculus-series n=2, the box-and-whisker how-to n=1); skills at n=3 are real reinforcement, not thin.

