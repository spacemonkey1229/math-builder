# LEARNING_GOALS.md — The Cold Start

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — matrix dimension and sparsity comparison (Option A's item-similarity matrix vs. Option B's ratings matrix, including the premiere's row/column fill count and a new account's row sparsity) | pre-calculus-matrix, pre-calculus-matrix-dimension |
| D2 — worked matrix addition (P + U) plus identity-matrix explanation of Option A | pre-calculus-how-to-add-and-multiply-matrices, pre-calculus-identity-matrix |
| D3 — determinant of the adjustment matrix U, and what a nonzero determinant implies | pre-calculus-determinant, pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix |
| D4 — weighted-blend system of equations, set up and solved as a matrix equation | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |
| D5 — recommendation memo, defended with Appendix D's per-100-starters table plus D1-D4 | pre-calculus-matrix, pre-calculus-matrix-dimension |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be produced without actually
stating both matrices' dimensions and computing filled-vs-total-cell ratios (a copied number
without the computation would not answer "why does 'sparse' not mean 'empty' for Option B"); D2
requires performing element-by-element matrix addition and correctly invoking the identity matrix's
"leaves it unchanged" property, not just describing Option A qualitatively; D3 requires the actual
2×2 determinant formula (ad − bc), not just asserting invertibility; D4 requires setting up a real
2-equation, 2-unknown linear system in matrix form and solving it by a named matrix method (row
reduction, inverse, or Cramer's rule) — a student who never built the system cannot report which
method they used; D5 requires weighing Appendix D's per-100-starters numbers against D1's sparsity
finding and at least one of D2–D4's matrix results, so a student who skipped the matrix work has
no numerical or structural basis for the recommendation.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 7 claimed skills (`pre-calculus-matrix`, `pre-calculus-matrix-dimension`,
`pre-calculus-determinant`, `pre-calculus-identity-matrix`, and their three how-tos) already show
`n=2` in `readmodel/standards_spine.json`, covered by "The Multiplier Recruit" and "The Skin Pack
Atlas." This is expected and matches the concept sheet's own framing: `CONCEPTS_formal-logic-
vectors-matrices-numbertheory_2026-08-23.md`'s C6 write-up explicitly describes this case as
thickening "the Matrices group from n=1/2 to n=2/3." `new_coverage[]` is set to `[]` per SPEC §4's
literal rule (a skill already at `n>=1` cannot be claimed as newly-closed), and `case.json` carries
a `reinforcement_note` explaining that this case exists to reinforce a thinly-covered 7-skill
Matrices group (only 2 prior cases), not to close a zero-coverage gap. Flagged for `case-qa` to
confirm rather than silently treated as a normal zero-new-coverage defect.
