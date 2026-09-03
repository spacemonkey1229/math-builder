# LEARNING_GOALS.md — The Rig Split

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — set up Option A's system in matrix form (unknowns, equations, coefficient matrix, dimensions) | pre-calculus-matrix, pre-calculus-matrix-dimension, pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |
| D2 — solve Option A via a matrix method, incl. determinant (via 2x2 minors), identity-matrix check, multiplication verification | pre-calculus-determinant, pre-calculus-identity-matrix, pre-calculus-how-to-add-and-multiply-matrices, pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix, pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |
| D3 — set up and solve Option B's own system, compare coefficient matrices | pre-calculus-matrix, pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |
| D4 — blended-productivity comparison table from the solved rig-days | pre-calculus-how-to-add-and-multiply-matrices |
| D5 — recommendation memo with sensitivity check | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without actually
defining three unknowns, writing three linear equations from the case's own stated constraints, and
expressing them as a genuine coefficient matrix (with a stated dimension); D2 requires an actual
matrix solve (elimination or inverse), an actual determinant computation built from real 2x2 minors
(there is no way to "fake" this and still get the case's real numeric result), and an actual
multiplication check; D3 requires repeating the same structural work for a second, differently
constrained system, which is what makes the "is this the same coefficient matrix" question
answerable at all; D4 requires converting matrix-solved unknowns into the case's real primary
metric via real multiplication and addition against Appendix D's sourced rates; D5 requires solving
a genuine breakeven equation (how many downtime days flip the winner) — a student who never
actually solved D1-D2's system correctly cannot get a numerically correct breakeven value, since
it depends on the real solved rig-day allocations.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 7 claimed skills (`pre-calculus-matrix`, `pre-calculus-matrix-dimension`,
`pre-calculus-determinant`, `pre-calculus-identity-matrix`,
`pre-calculus-how-to-add-and-multiply-matrices`,
`pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix`,
`pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix`) already show `n=2` in
`readmodel/standards_spine.json`. This is expected and matches the concept sheet's own framing
(C7: "0 new skills — thickens the Matrices group"): `new_coverage[]` is set to `[]` per SPEC §4's
literal rule (a skill already at `n>=1` cannot be claimed as newly-closed), and `case.json` carries
a `reinforcement_note` explaining that this case exists to thicken coverage on the seven-skill
Pre-Calculus/Matrices group via a genuine system-of-equations application (structurally distinct
from a matrix-arithmetic application), not to close a zero-coverage gap. This is a deliberate,
disclosed deviation from SPEC §4's "no reason to exist" framing for this one case — flagged for
`case-qa` to confirm rather than silently treated as a normal zero-new-coverage case.
