# Learning Goals — Creek Span

Bidirectional deliverable ↔ skill matrix (case-write SKILL.md §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 elevation sketch, side lengths labeled | geometry-triangle |
| D2 salvage-fit Triangle Inequality check | geometry-triangle-inequality-theorem |
| D3 Warren Line triangle classification | geometry-equilateral-triangle, geometry-acute-triangle |
| D4 Low Line interior + end triangle classification | geometry-leg, geometry-obtuse-triangle, geometry-scalene-triangle |
| D5 fabrication takeoff & cost per foot | advanced-numbers-how-to-multiply-decimal-numbers, advanced-numbers-how-to-divide-decimal-numbers, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
  deliverables: 5    claimed skills: 10    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## Notes on the "forces" test

- **D2 / Triangle Inequality Theorem.** A student cannot correctly determine whether the 3.5-ft
  salvage pieces close either panel's web triangle without applying the theorem directly — this
  is the case's one genuinely load-bearing use of it: it decides which option can use free steel
  and which cannot.
- **D3 / Equilateral + Acute.** A student who only names "equilateral" without checking the
  angles has not shown the second half of the deliverable — D3 explicitly requires using the
  side lengths to justify the *acute* classification, not just asserting it.
- **D4 / Leg, Obtuse, Scalene.** Three distinct skills, each forced by a distinct labeled
  sub-part: naming the base/legs of the isosceles interior triangle (Leg), classifying its angle
  (Obtuse), and classifying the non-repeating end triangle by side length (Scalene) — a student
  cannot produce a correct D4 without performing all three.
- **D5 / decimal + percent operations.** The takeoff requires multiplying weights by price/ft
  and wage rates (decimal multiplication), dividing total cost by a 9-ft-longer chord run and by
  the 24-ft span (decimal division), and stating the margin between options as a percent.
- **geometry-triangle (D1).** Labeling every "web triangle" on a dimensioned sketch requires the
  student to correctly identify what does and does not constitute a triangle in the truss
  elevation (as opposed to, e.g., a chord run or a rectangle formed by two panels) before any
  classification in D3/D4 can happen.

## Reinforcement, not new coverage

Every one of the six Geometry/Triangles skills this case targets already has `n=1` in
`readmodel/standards_spine.json` (checked before writing — see `case.json.reinforcement_note`).
`new_coverage[]` is correctly empty; this case exists to give each skill a second, independent
context (structural engineering / truss fabrication) rather than to close a zero-coverage gap.
