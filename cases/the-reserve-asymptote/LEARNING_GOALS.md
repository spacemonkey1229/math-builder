# LEARNING GOAL CHECK — The Reserve Asymptote

Bidirectional deliverable ↔ spine-skill matrix, per `case-write` SKILL.md §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — one-sided limit estimate from the real table | `pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph`, `pre-calculus-limit`, `calculus-one-sided-limit`, `calculus-limit` |
| D2 — limit evaluated algebraically from the equation | `pre-calculus-asymptote`, `pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation`, `calculus-how-to-evaluate-a-limit-algebraically`, `calculus-limit`, `pre-calculus-limit` |
| D3 — continuity determination at age 100 | `pre-calculus-continuity-informal`, `calculus-continuity`, `calculus-discontinuity`, `calculus-how-to-determine-whether-a-function-is-continuous-at-a-point` |
| D4 — single-cohort dollar gap at age 100 | `calculus-how-to-evaluate-a-limit-algebraically`, `pre-calculus-limit` (applies the D2 limit value as a priced dollar figure and requires re-reading D1/D3's continuity finding to know which real-table value governs age 100) |
| D5 — portfolio-wide margin | `calculus-continuity`, `calculus-discontinuity`, `pre-calculus-continuity-informal` (a student cannot correctly price the age-100 cohort inside the blended average without having correctly determined, from D3, that the Full Table is discontinuous there and the Smooth Curve is not) |
| D6 — original visual (Challenge 2b) | `pre-calculus-asymptote`, `calculus-discontinuity`, `pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation` |

## Reverse check — every claimed skill traced to a deliverable

| Skill id | Kind | Forced by |
|---|---|---|
| `pre-calculus-limit` | term | D1, D2, D4 |
| `pre-calculus-asymptote` | term | D2, D6 |
| `pre-calculus-continuity-informal` | term | D3, D5 |
| `pre-calculus-how-to-estimate-a-limit-from-a-table-or-graph` | how-to | D1 |
| `pre-calculus-how-to-identify-a-vertical-or-horizontal-asymptote-from-a-function-s-equation` | how-to | D2, D6 |
| `calculus-limit` | term | D1, D2 |
| `calculus-one-sided-limit` | term | D1 |
| `calculus-continuity` | term | D3, D5 |
| `calculus-discontinuity` | term | D3, D5, D6 |
| `calculus-how-to-evaluate-a-limit-algebraically` | how-to | D2, D4 |
| `calculus-how-to-determine-whether-a-function-is-continuous-at-a-point` | how-to | D3 |

## The "forces" test applied

*Could a competent student produce this deliverable correctly without ever performing this skill?*

- **D1** cannot be done without reading a table and estimating a one-sided limit from it — that
  is the deliverable's entire content.
- **D2** cannot be done without algebraic limit evaluation and asymptote identification from an
  equation — the instruction explicitly forbids estimating from a graph here, forcing the
  algebraic route.
- **D3** cannot be done without the formal continuity test (compare one-sided limit to the
  function's value at the point) — a student who "eyeballs" continuity from the graph in D6
  without doing the D1/D2 comparison will get the *kind* of discontinuity wrong (they could guess
  "it looks off" but could not correctly classify it as a jump discontinuity, nor correctly
  determine that the Smooth Curve *is* continuous there, without the test).
- **D4** requires plugging the correct governing value into a dollar calculation — a student who
  has not done D1–D3 correctly will price the age-100 cohort under the Full Table with the wrong
  number (something near $347 instead of the real $1,000), because they will not have determined
  that the real function jumps there.
- **D5** requires D4's per-cohort logic applied across the whole block; a student who mis-prices
  age 100 mis-prices the entire portfolio margin.
- **D6** requires plotting a genuine jump discontinuity and a genuine horizontal asymptote — a
  student who has not correctly computed either from D2/D3 cannot draw them correctly.

## Result

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 11    new_coverage: 11
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

All 11 skills currently show `n == 0` in `readmodel/standards_spine.json` (verified 2026-08-18),
so `new_coverage[]` is the full claimed list.
