# Learning Goals — The Weekly Rate

Bidirectional deliverable ↔ skill matrix (case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 weekly cost-function derivation | advanced-operations-variable, advanced-operations-constant, advanced-operations-coefficient, advanced-operations-term, advanced-operations-like-terms, advanced-operations-distributive-property, advanced-operations-how-to-add-and-subtract-an-expression-with-variables, statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data |
| D2 break-even system | statistics-and-probability-system-of-equations, statistics-and-probability-how-to-solve-a-system-of-linear-equations, advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides, measurement-rounding, measurement-how-to-round-a-number-to-a-specified-place-value |
| D3 net-savings x-intercept | statistics-and-probability-x-intercept, statistics-and-probability-y-intercept, advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side, advanced-operations-how-to-evaluate-a-variable-expression-substitution-property |
| D4 distractor read (Appendix B graph) | statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o, statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d, statistics-and-probability-slope, statistics-and-probability-y-intercept |
| D5 graph of both real options | statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation, statistics-and-probability-slope, statistics-and-probability-y-intercept |
| D6 total-cost-at-horizon comparison | advanced-operations-how-to-evaluate-a-variable-expression-substitution-property, advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number, advanced-numbers-how-to-convert-numbers-to-percents, basic-operations-addition, basic-operations-how-to-add-multi-digit-numbers, basic-operations-multiplication, basic-operations-how-to-multiply-any-two-numbers |

## The forces-test, applied

*Could a competent student produce this deliverable correctly without ever performing this skill?*

- **D1** cannot be written without naming variables/constants/coefficients/terms, combining the two
  per-week charges (like terms) via the distributive property, and deriving a slope-intercept
  equation from the itemized rate data (not handed a formula). No shortcut skips these.
- **D2** requires literally writing two linear equations and solving them as a system — treating it
  as "guess and check" fails the "showing your work" requirement and produces an unroundable,
  undefendable answer under Socratic questioning.
- **D3** requires simplifying B(w) − A(w) to one weekly-rate term (like terms again, in the opposite
  direction from D1) and solving a one-variable equation for its root — the x-intercept — plus
  substituting w = 0 for the y-intercept (evaluate/substitution).
- **D4** is the deliberate distractor test: a student must read slope and y-intercept off a graph
  they were not handed a formula for, and separately argue *why it doesn't belong* in the recommendation
  — that argument itself only works if they can name what makes Whizz's plan structurally different
  from Zoomo's (a fixed deposit plus a different weekly rate the case never asked them to compare).
- **D5** requires graphing two derived, non-trivial lines (not just plotting given points) over a wide
  enough window to show the real intersection, which only exists past week 100.
- **D6** requires substituting w = 91 into both D1 functions, subtracting, and converting to a percent
  of the correct base (the more expensive option, not an arbitrary one) — the exact class of error
  that produces a wrong margin even with correct raw numbers.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 28    new_coverage: 0 (reinforcement case, see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Every skill in `case.json.standards[]` appears in at least one deliverable's skills list above, and
every deliverable maps to a non-empty skills list. No padding: `advanced-numbers-how-to-convert-numbers-to-percents`
and `advanced-numbers-percent`/`advanced-numbers-how-to-find-the-percent-of-a-number` were checked against
D6 specifically (converting the dollar difference to a percent of the higher total) rather than assumed
from the case's general subject matter.
