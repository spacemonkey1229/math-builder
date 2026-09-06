# Learning Goals — The Sightline Vote

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-09-05.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — labeled site diagram: point, line segment, ray, vertex, degree labels | `geometry-point`, `geometry-line-segment`, `geometry-ray`, `geometry-vertex`, `geometry-degree` |
| D2 — current skew: four angles, acute/obtuse, supplementary adjacents, congruent verticals | `geometry-acute-angle`, `geometry-obtuse-angle`, `geometry-adjacent-angles`, `geometry-supplementary-angles`, `geometry-vertical-angles`, `geometry-fundamentals-of-geometry-congruent`, `geometry-how-to-find-angle-measures-of-intersecting-lines` |
| D3 — Squared Corner: right angles, ADA ramp complementary split | `geometry-perpendicular-lines`, `geometry-right-angle`, `geometry-complementary-angles` |
| D4 — Offset Bypass: parallel lane, transversal, angle-pair reasoning | `geometry-parallel-lines`, `geometry-transversal-line`, `geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an` |
| D5 — safety-score-per-dollar comparison, verdict | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-find-the-percent-of-a-number` (all already covered) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 21    new_coverage: 0 (see reinforcement_note)
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to every claimed skill** (*could a competent Hero produce the deliverable
correctly without ever performing this skill?*):

- `geometry-point` — D1 requires marking a specific surveyed reference point on the diagram; a
  Hero who cannot identify what a point actually is (a single fixed location, no size or
  direction) cannot label one correctly and distinctly from the vertex.
- `geometry-line-segment` — D1 requires labeling a specific curb edge with both endpoints named; a
  Hero must know a segment is bounded on both ends (unlike a ray or a line) to label it correctly.
- `geometry-ray` — D1 requires marking the driver's sightline as a ray from a fixed point extending
  one direction down Kellner Avenue; confusing this with a segment or a full line mislabels the
  diagram.
- `geometry-vertex` — D1 requires marking where the two road centerlines meet in every diagram (three
  diagrams: current, A, B); D2/D3/D4 all require naming this same point as the vertex of the angles
  being computed.
- `geometry-degree` — every angle value computed in D2/D3/D4 must be labeled with its degree measure
  on the diagram and in the written work; a Hero who cannot express an angle measure in degrees
  cannot complete any of D2-D4.
- `geometry-acute-angle`, `geometry-obtuse-angle` — D2 explicitly requires classifying each of the
  four current-intersection angles as one or the other, from the computed 50°/130° values, not
  asserted from memory.
- `geometry-adjacent-angles` — D2 requires showing each adjacent pair (sharing a ray and a vertex)
  sums to 180°; a Hero who cannot identify which angle pairs are actually adjacent at this
  intersection (as opposed to vertical) cannot complete the supplementary check correctly.
- `geometry-supplementary-angles` — D2 requires the arithmetic verification that adjacent pairs sum
  to 180°, not just naming the relationship.
- `geometry-vertical-angles` — D2 requires identifying the two angle pairs formed opposite each
  other at the crossing and showing each pair is congruent — the defining structure of a vertical
  pair, not a label applied after the fact.
- `geometry-fundamentals-of-geometry-congruent` — D2 requires the actual congruence claim (the two
  acute angles measure the same; the two obtuse angles measure the same) with the arithmetic to back
  it, not just the word "congruent" written down.
- `geometry-how-to-find-angle-measures-of-intersecting-lines` — D2's entire method (deriving all
  four angles at a crossing from one given angle) is this exact procedure, applied to a real,
  non-perpendicular crossing.
- `geometry-perpendicular-lines` — D3 requires recognizing and stating that The Squared Corner's
  redesign makes Kellner Avenue and Birch Hollow Road perpendicular — the term's actual defining
  property (crossing at 90°), not incidental vocabulary.
- `geometry-right-angle` — D3 requires confirming each of the four new angles measures exactly 90°
  and classifying it correctly.
- `geometry-complementary-angles` — D3 requires the ADA curb ramp's two split angles (35° given, 55°
  found) to be shown summing to 90° — an arithmetic check, not a label.
- `geometry-parallel-lines` — D4 requires stating and using the fact that the new connector lane is
  built parallel to the platted lot line; the whole angle-transfer argument depends on this being
  true, not assumed loosely.
- `geometry-transversal-line` — D4 requires identifying Kellner Avenue as the transversal crossing
  both the lot line and the new parallel connector lane — the structure the angle-pair reasoning
  depends on.
- `geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an`
  — D4's entire method (given the lot line's 75° angle to Kellner Avenue, find the connector lane's
  angle to Kellner Avenue using the parallel relationship) is this exact procedure.

D5 intentionally claims no new or already-covered-but-forced skill beyond ordinary arithmetic — it
is the case's real, load-bearing comparison (the actual safety-score-per-dollar verdict this case
is built around), consistent with the anti-inflation doctrine used by `roofline-call`'s D5.

No skill here is claimed on the strength of "the case is about angles generally" — each one traces
to a specific requirement in a specific deliverable, verified against the exact wording of D1–D4
above.

## Reinforcement note (why new_coverage[] is legitimately empty)

Every one of these 18 skills already sits at `n=2` in `standards_spine.json`'s Geometry /
Fundamentals Of Geometry group — the entire group is already covered by two prior cases apiece, so
this case cannot push any of them to zero-coverage-closed no matter how it is written. Checked for
adjacent uncovered coverage before accepting this: the only `n=0` skill anywhere in the Geometry
domain is `geometry-how-to-find-the-volume-of-a-sphere` (Surface Area And Volume group), and no
deliverable in an intersection-angle redesign case can honestly force it — there is no sphere and
no volume anywhere in this case's real geometry, and padding it into `standards[]` would be exactly
the fabricated mapping the forcing test above exists to catch. See `case.json.reinforcement_note`.
