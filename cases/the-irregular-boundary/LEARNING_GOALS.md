# LEARNING_GOALS.md — The Irregular Boundary

Bidirectional deliverable ↔ skill matrix. Domain: Geometry / Quadrilaterals And Polygons.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Squared Block diagram | geometry-convex, geometry-quadrilateral |
| D2 — Reclaimed Line diagram | geometry-concave, geometry-irregular-polygon |
| D3 — Disputed-strip classification note | geometry-parallelogram |
| D4 — Usable-acreage and perimeter comparison table | geometry-convex, geometry-quadrilateral, geometry-concave, geometry-irregular-polygon |
| D5 — Cost-and-loss comparison table | geometry-concave, geometry-irregular-polygon |
| D6 — Net-dollars-per-acre recommendation | geometry-convex, geometry-concave, geometry-irregular-polygon, geometry-quadrilateral, geometry-parallelogram |

## Reverse check — every claimed skill, and what forces it

| Skill (spine id) | n (before this case) | Forced by |
|---|---|---|
| geometry-convex | 2 | D1, D4, D6 |
| geometry-concave | 1 | D2, D4, D5, D6 |
| geometry-irregular-polygon | 1 | D2, D4, D5, D6 |
| geometry-quadrilateral | 1 | D1, D4, D6 |
| geometry-parallelogram | 0 | D3, D6 |

"Forces" test applied: could a competent student produce this deliverable correctly without ever
performing this skill? For each row above, no — D1 cannot be drawn or labeled without identifying
the boundary as a convex quadrilateral; D2 cannot be drawn or labeled without classifying vertices
as convex/reflex and naming the whole shape an irregular polygon; D3 requires recognizing the
disputed strip's shape as a parallelogram to state its area/orientation correctly; D4, D5, and D6
each depend on the classification work done in D1–D3 to compute or state their numbers correctly
(a student who mis-classifies Option B as convex, for instance, will not know to look for reflex-
vertex turning-margin loss in D5, and will get D6 wrong).

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 6    claimed skills: 5    new_coverage: 1
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```
