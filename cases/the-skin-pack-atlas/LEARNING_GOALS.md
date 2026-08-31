# Learning Goal Matrix — The Skin Pack Atlas

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 labeled 2×2 install-base matrix M, dimensions stated | pre-calculus-matrix, pre-calculus-matrix-dimension |
| D2 identity matrix I and M⁻¹, verified via M·M⁻¹ = I | pre-calculus-identity-matrix, pre-calculus-how-to-add-and-multiply-matrices |
| D3 determinant of M, 2×2 formula, invertibility explanation | pre-calculus-determinant, pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix |
| D4 solved revenue-per-install vector r = M⁻¹v, full matrix arithmetic | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix, pre-calculus-how-to-add-and-multiply-matrices |
| D5 final decision table using D4's rates | pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 7    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

Reasoning per skill (bidirectional "forces" test — could a competent student produce the
deliverable without performing the skill? If yes, the mapping is fake):

- **pre-calculus-matrix** — D1 requires building and labeling a matrix; cannot be done without
  the concept of a matrix.
- **pre-calculus-matrix-dimension** — D1 explicitly requires the student to state M's dimensions
  (2×2); this is the only place that vocabulary is forced, and it is forced there.
- **pre-calculus-identity-matrix** — D2 requires naming and using I as the target of the
  M · M⁻¹ verification step; a student who doesn't know what I is cannot perform that check.
- **pre-calculus-how-to-add-and-multiply-matrices** — D2's verification step (multiplying M by
  M⁻¹ entry by entry) and D4's application of M⁻¹ to v both require matrix multiplication.
- **pre-calculus-determinant** — D3 requires computing and naming the determinant.
- **pre-calculus-how-to-find-the-determinant-of-a-2x2-matrix** — D3 explicitly requires the 2×2
  determinant formula, shown as an arithmetic step, not just a final number.
- **pre-calculus-how-to-solve-a-system-of-equations-using-a-matrix** — D4 requires solving the
  system via matrix inversion; D5 requires applying that solved vector to a real decision, which
  cannot be produced correctly without having solved the system first.

`new_coverage` is intentionally `0` / `[]` — see the case's authoring note: this is a
second-pass/redundancy case in the same Pre-Calculus/Matrices group as the already-published
`the-multiplier-recruit` (which set `n=1` on all seven of these skill ids). This case exists to
give the standards group a second, structurally distinct case (a different protagonist, a
different real-world domain — mobile game texture atlases and GPU hardware rather than regional
economic multipliers), not to close a coverage gap.
