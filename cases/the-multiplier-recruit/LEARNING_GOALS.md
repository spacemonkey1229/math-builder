# Learning Goals — The Multiplier Recruit

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — labeled 2×2 technical coefficient matrix **A** | pre-calculus-matrix, pre-calculus-matrix-dimension |
| D2 — identity matrix **I** and computed **(I − A)** | pre-calculus-identity-matrix, pre-calculus-how-to-add-and-multiply-matrices |
| D3 — determinant of **(I − A)**, by hand | pre-calculus-determinant, pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix |
| D4 — solved total-jobs vector **x = (I − A)⁻¹d** for each employer | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix, pre-calculus-how-to-add-and-multiply-matrices |
| D5 — final decision table (jobs supported per $10,000 of incentive) | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |

**"Forces" test applied to each row:**

- D1: a student cannot write a valid 2×2 matrix without knowing what a matrix is and being able to
  state its dimensions — both are load-bearing to producing the artifact at all, not decoration.
- D2: naming and using the identity matrix **I** is unavoidable to build **(I − A)** in the first
  place; computing every entry of the difference is a matrix-arithmetic operation in the same
  family the spine groups under "add and multiply matrices."
- D3: the determinant is computed directly, by the named 2×2 formula, and its role (confirming the
  system is solvable) is stated in the student's own words — both the term and the how-to are
  load-bearing, not just mentioned.
- D4: this is the deliverable the entire case turns on — solving a 2×2 system via a matrix method
  is the how-to skill itself, and applying **(I − A)⁻¹** to a demand vector is matrix
  multiplication, so it also reinforces D2's how-to skill from a different angle.
- D5: the decision table cannot be built without D4's solved vectors — a student who skipped D4 has
  nothing to put in the "total regional jobs supported" column. It reinforces, rather than
  introduces, the matrix-solving how-to; it introduces no new spine skill of its own.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 7
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```
