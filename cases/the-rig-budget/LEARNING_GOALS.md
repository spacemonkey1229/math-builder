# LEARNING_GOALS.md — The Rig Budget

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — R and S matrices for the elbow bone (single-bone segment), dimensions stated | pre-calculus-matrix, pre-calculus-matrix-dimension |
| D2 — elbow's M = R·S AND shoulder blend-zone's M_blend = w1·R1 + w2·R2, both computed by hand | pre-calculus-how-to-add-and-multiply-matrices |
| D3 — determinant of elbow's M AND shoulder blend-zone's M_blend, each vs. identity matrix's determinant | pre-calculus-determinant, pre-calculus-identity-matrix, pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix |
| D4 — recover M_blend by solving a system of equations | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |
| D5 — Skin-Blend Cost & Determinant Table (real measured ms/frame, % of frame budget, determinant-based correctness) | pre-calculus-matrix-dimension, pre-calculus-how-to-add-and-multiply-matrices |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without stating two
actual 2×2 matrices and their dimensions; D2 requires carrying out real 2×2 matrix multiplication
entry-by-entry for the elbow AND real scalar-multiply-then-add matrix arithmetic for the shoulder
blend-zone, not just stating final answers; D3 requires the actual 2×2 determinant formula, applied
twice, with a comparison to the identity matrix's determinant (1) as the "no transform" baseline —
and, for the blend-zone case, correctly reading what a determinant below 1 means for the real
"candy-wrapper" defect the case's sources describe; D4 cannot be completed without setting up and
solving a real system of linear equations for M_blend's four unknown entries; D5 requires combining
real sourced GPU-cost figures (ms per frame) with the D3(b) determinant finding into a single
recommendation table — a student who never engaged with either the real cost data or what a
determinant below 1 means cannot build this table correctly.

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
`readmodel/standards_spine.json` (covered_by: `["The Multiplier Recruit", "The Skin Pack Atlas"]`),
confirmed by direct grep of the spine file at authoring time — not `n=1` as the concept sheet's own
write-up claimed ("thickens the entire Matrices group from n=1 to n=2 ... currently covered by
exactly one case"). `new_coverage[]` is correctly set to `[]` per SPEC §4's literal rule either way
(no skill in this group is at `n=0`), but this case actually thickens the group from `n=2` to
`n=3`, not `n=1` to `n=2`. `case.json` carries a `reinforcement_note` explaining this, matching the
disclosed-correction pattern used by `the-course-correction` for the same kind of stale
concept-sheet coverage count. Flagged for `case-qa` to confirm rather than silently treated as a
zero-new-coverage defect, and flagged for the concept-log maintainer to correct the concept sheet's
own C3 write-up.
