# Learning Goals — The Clampband Margin

Bidirectional deliverable ↔ skill matrix (SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 stack-up table across a growing supplier count | pre-calculus-limit, pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph |
| D2 horizontal asymptote identified algebraically | pre-calculus-asymptote, pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation, pre-calculus-limit |
| D3 margin-threshold continuity check | pre-calculus-continuity-informal, pre-calculus-limit |
| D4 current three-supplier margin | pre-calculus-limit |
| D5 original visual (asymptote + threshold graph) | pre-calculus-asymptote, pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation, pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 5    new_coverage: 0

UNMAPPED DELIVERABLES: none
  - D1 forces pre-calculus-limit (estimating the limiting trend of two sequences from a
    table) and pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph directly — a
    student cannot produce this table's stated conclusion ("how each method's predicted
    tolerance behaves as n keeps growing") without estimating a limit from tabulated values.
  - D2 forces pre-calculus-asymptote and pre-calculus-how-to-identify-a-vertical-or-horizontal-
    asymptote-from-a-function-s-equation by name — the deliverable explicitly requires the
    algebraic identification method, not a table read.
  - D3 forces pre-calculus-continuity-informal — determining whether a pass/fail outcome
    against a fixed threshold changes smoothly or jumps requires the informal continuity
    concept (a function's value tracking a trend without an abrupt break, versus not).
  - D4 forces pre-calculus-limit — evaluating the n=3 case requires understanding what each
    stack-up function converges toward/behaves like near its actual operating point, tying
    the base case back to the trend established in D1–D3.
  - D5 is the graph that visually demonstrates the asymptote (D2) and any discontinuity in
    pass/fail status (D3), and requires reading the trend from a graph
    (pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph) to place the marks correctly.

UNREACHABLE SKILLS: none
  - pre-calculus-limit: forced by D1, D2, D4 (see above).
  - pre-calculus-asymptote: forced by D2 and D5.
  - pre-calculus-continuity-informal: forced by D3.
  - pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph: forced by D1 and D5.
  - pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation:
    forced by D2 and D5.

RESULT: PASS
```

**Note on new_coverage:** this is a second-pass / redundancy case. All 5 claimed skills
(Pre-Calculus / Introduction To Limits) already have `n >= 1` coverage via the previously
published case `the-reserve-asymptote`. `new_coverage` is deliberately `[]` — this case exists
to give the same Introduction To Limits group a second, structurally different worked example
(a real aerospace tolerance-stack problem rather than an actuarial reserve problem), not to open
new spine coverage. This is expected for this batch, not an error.

**Note on the two "already-covered, do-not-score" skills from the concept sheet**
(`geometry-perimeter-and-area`, `advanced-operations-scientific-notation`): neither is claimed in
`standards[]`. `advanced-operations-scientific-notation` resolves to a real spine id but no
deliverable above forces it as written (small-tolerance unit handling appears only as flavor in
Appendix C, not as a required calculation), so claiming it would create an UNREACHABLE SKILL.
`geometry-perimeter-and-area` does not resolve to any id in `readmodel/standards_spine.json` at
all (the closest real ids are `geometry-perimeter` and `geometry-area`, both separate terms) — an
unverifiable id is a hard stop per SKILL.md §1, so it is left out rather than guessed at.
