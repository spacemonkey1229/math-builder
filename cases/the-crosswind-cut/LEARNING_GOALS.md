# Learning Goals — The Crosswind Cut

Bidirectional deliverable ↔ skill matrix, run per `case-write` step 10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 thrust-and-current table (total available thrust per configuration, built by summing each motor's thrust vector) | pre-calculus-vector, pre-calculus-magnitude-of-a-vector, pre-calculus-how-to-add-and-subtract-vectors |
| D2 crosswind-cancellation vector diagram (crosswind vector, heading unit vector, corrective thrust vector via subtraction) | pre-calculus-vector, pre-calculus-magnitude-of-a-vector, pre-calculus-unit-vector, pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector, pre-calculus-how-to-add-and-subtract-vectors |
| D3 net forward-progress thrust table (dot product of thrust vector with heading unit vector, net of D2) | pre-calculus-dot-product, pre-calculus-unit-vector, pre-calculus-how-to-find-the-dot-product-of-two-vectors |
| D4 thrust-per-amp comparison table (advertised vs. net-forward-progress rate, evaluated as a variable expression) | advanced-operations-variable |
| D5 battery-reserve check (percentage of mandatory reserve remaining at touchdown) | advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 9    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Notes:
- All 5 Challenge-3 deliverables (D1–D5) have a non-empty skills column.
- All 9 skills in `case.json.standards[]` are forced by at least one deliverable:
  the 7 concept-locked Pre-Calculus/Vectors skills (Vector, Magnitude (Of A Vector), Unit Vector,
  Dot Product, and their three "how to…" pairs) are forced by D1–D3; the two round-out skills
  named in the concept sheet (Variable; How to find the percent of a number) are forced by D4 and
  D5 respectively.
- `new_coverage: []` is expected and correct for this case: this is a **second-pass /
  redundancy** case per the batch instructions — the target skill group (Pre-Calculus/Vectors)
  already carries `n == 1` coverage on all 7 claimed skills before this case exists (verified
  against `readmodel/standards_spine.json`), and the two round-out skills (`advanced-operations-variable`,
  n=9; `advanced-numbers-how-to-find-the-percent-of-a-number`, n=55) are also already covered.
  This is not a validation failure — it is the expected shape of a redundancy-batch case.
