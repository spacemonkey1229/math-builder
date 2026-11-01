# Learning Goal Check — Firm Power

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 descriptive-statistics table | statistics-and-probability-quartiles, statistics-and-probability-median, statistics-and-probability-range, statistics-and-probability-outlier |
| D2 missing-data reconstruction | statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-, statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data |
| D3 peak-window and capacity sizing | advanced-numbers-how-to-find-the-percent-of-a-number, measurement-how-to-convert-an-amount-with-compound-units |
| D4 unit conversion and equation | measurement-how-to-convert-an-amount-with-compound-units, advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side |
| D5 total-cost comparison | measurement-how-to-convert-an-amount-with-compound-units |

## Forces-test notes

- **D1** cannot be produced without computing quartiles, median, and range from the real
  24-value data set, and cannot be produced without actually testing (not asserting) whether a
  value lies outside the 1.5×IQR fence — a student who skips the arithmetic and just eyeballs
  "no outliers" has not shown the outlier work the deliverable explicitly requires.
- **D2** cannot be produced without solving `missing = 24 × mean − sum(23 known values)`, which is
  the literal definition of the missing-data-element skill, and the verification step forces a
  genuine mean computation over all 24 values (not a restatement of the given number).
- **D3** requires taking 3% of several real CAISO figures (Appendix E) and converting between the
  resulting raw MW figures and the MWh needed over the peak window — a percent-of-a-number step
  chained into a compound-unit (MW × hours → MWh) step.
- **D4** requires converting $18.92/kW-month into $/MW-year (three chained unit conversions:
  kW→MW, month→year, and combining them) and then isolating a variable in
  `Budget = X(MW) × Net_CONE($/MW-yr)` — a genuine multi-step equation, not a single lookup.
- **D5** requires multiplying each option's real $/MWh rate by D3's MWh figure to get a total
  dollar cost — a third, independent application of the compound-unit-conversion skill in a
  different direction (rate × quantity → total) from D3's and D4's uses of it.

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 10    new_coverage: 0 (reinforcement_note, see case.json)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```
