# Learning Goals — The Marginal Call

Bidirectional deliverable ↔ skill matrix. Run at case-write time per skills/case-write/SKILL.md
step 10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — total production-cost function C(x) | calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D2 — quotient-rule differentiation of A(x)=C(x)/x, critical point, first derivative test | calculus-derivative, calculus-how-to-find-a-derivative-using-the-power-rule, calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions, calculus-critical-point, calculus-how-to-find-critical-points-of-a-function, calculus-how-to-use-the-first-derivative-test-to-classify-a-critical-point, calculus-local-minimum, calculus-how-to-solve-an-optimization-problem-using-derivatives |
| D3 — average-cost comparison table (dollars + percent) | advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — net-cost-per-board-foot-sold (carrying-cost penalty) | advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 — graph of A(x) with x*, both batch sizes labeled | calculus-critical-point, calculus-local-minimum |
| D6 — financing memo (deposit vs. credit line) | advanced-numbers-how-to-find-the-percent-of-a-number |

## Forcing test applied to every row

*Could a competent student produce this deliverable correctly without ever performing this skill?*

- **D1** cannot be built without setting up the objective function the rest of the case optimizes —
  that setup step is the first move of "how to solve an optimization problem using derivatives."
- **D2** is the core of the case: a student cannot differentiate C(x)/x without the quotient rule
  (the whole reason this case exists — n=0 in the spine before this case), cannot compute the
  quotient rule's u' term without the power rule (C(x) is a polynomial in x), cannot find x* without
  setting the derivative to zero and solving (critical points), and cannot certify x* as the batch
  size that actually minimizes cost — rather than maximizes it or is a saddle — without the first
  derivative test and the vocabulary of a local minimum.
- **D3** requires stating the dollar gap as a percent of the larger value — direct percent-of-a-
  number work, and it is the step where a student first sees how close the two real options are.
- **D4** requires computing a carrying-cost dollar amount as a percentage of the unsold board feet's
  value, then dividing by a different denominator than D3 used — the step that can flip D3's raw
  answer once unsold inventory is priced in.
- **D5** cannot be drawn correctly without knowing what a critical point and a local minimum look
  like on the average-cost curve — a student who doesn't understand D2 will not know where to mark
  x* or why the curve should look U-shaped there.
- **D6** requires taking a percent of a dollar figure (the deposit) and subtracting it from another
  dollar figure (the credit line) — a direct application of percent-of-a-number to a real dollar
  gap.

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 9    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```
