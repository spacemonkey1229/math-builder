# Learning Goals — Air Traffic Controller

Bidirectional deliverable ↔ skill matrix (case-write.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — steady-state fuel-flow rate (mean of Appendix E's plateaued readings, rounded to 1 decimal) | statistics-and-probability-mean, statistics-and-probability-how-to-find-the-mean-of-a-set-of-data, number-sense-place-value, measurement-how-to-round-a-number-to-a-specified-place-value, measurement-rounding |
| D2 — total fuel burned, Option A (pre-failure burn + D1 rate x 1,200 mi) | advanced-numbers-how-to-multiply-decimal-numbers, measurement-how-to-convert-an-amount-with-compound-units, measurement-how-to-convert-between-units-of-time, measurement-how-to-add-and-subtract-time, measurement-distance, number-sense-distance |
| D3 — total fuel burned, Option B (pre-failure burn + D1 rate x 1,214 mi) | advanced-numbers-how-to-multiply-decimal-numbers, measurement-how-to-convert-an-amount-with-compound-units, measurement-distance, number-sense-distance |
| D4 — fuel-remaining comparison table, gallons and liters | basic-operations-how-to-subtract-multi-digit-numbers, advanced-numbers-how-to-subtract-decimal-numbers, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, measurement-unit, number-sense-how-to-compare-two-or-more-values |
| D5 — cruise-performance lookup (current weight + altitude -> Appendix C) | measurement-weight, number-sense-weight, measurement-how-to-convert-an-amount-from-one-unit-to-another-unit, measurement-how-to-find-a-missing-amount-in-a-proportion, measurement-proportion, basic-operations-how-to-subtract-multi-digit-numbers |

## Forces test

"Could a competent student produce this deliverable correctly without ever performing this skill?" applied to every cell above:

- D1 cannot be produced without averaging (mean) a subset of the table, without knowing which readings have "plateaued" (a genuine judgment call the case forces by design), without rounding to a specified place, and without correctly identifying the tenths digit to round to it.
- D2/D3 cannot be produced without converting the pre-failure time (mph, hours, minutes) into a compound-unit fuel-burn figure, and without multiplying a decimal rate by a decimal distance.
- D4 cannot be produced without subtracting decimals/multi-digit totals from the tank capacity, and without converting the gallon results to liters (the case's own dual-unit convention from Appendix F).
- D5 cannot be produced without converting burned gallons to a weight in kilograms, subtracting that weight from the takeoff weight, and using the result (a value that falls between two listed table rows) to select the correct bracket — a real proportion/interpolation judgment.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 20    new_coverage: 1
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Every skill in `standards[]` appears in at least one deliverable's skill list above (checked by hand against case.json). Every deliverable (D1-D5) has a non-empty skill list. No skill was added because it "sounded related" without a deliverable that actually requires it — see the forces test above for each.
