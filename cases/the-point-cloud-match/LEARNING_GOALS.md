# Learning Goals — The Point Cloud Match

Bidirectional deliverable ↔ skill matrix. `case.json.standards[]` is the authority for ids.

**Reinforcement case, not a gap-closing case.** This case's concept sheet originally scored
`geometry-congruent`, `geometry-similar`, `geometry-how-to-reflect-a-figure-across-the-y-axis`,
and `geometry-quadrant` as prospective `new_coverage[]`. Verified live against
`readmodel/standards_spine.json` on 2026-09-12: all four now show **n=2**, covered by Company
Front / The Repeat Match (the first three) and Airstrike / Urban Planner (quadrant) — cases that
published the same day, concurrently with this case's authoring. `new_coverage[]` is therefore
correctly empty (see `case.json.reinforcement_note` for the full adjacent-coverage check). This
case still has real pedagogical value: it is a further data point on a still-thin skill group
(every skill in Geometry/Coordinate Plane and Geometry/Transformations sits at n=2 or n=3, not
n=5+), using a genuinely different scenario (point-cloud/photogrammetry registration) from the
architectural and survey framings of its sibling cases — same precedent as Pixel Snap and The
Repeat Match.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — scan-scale note, scientific notation | `advanced-operations-scientific-notation`, `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `measurement-ratio` |
| D2 — congruence-or-similarity audit | `geometry-congruent`, `geometry-similar`, `geometry-coordinate-pair-also-ordered-pair`, `geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane`, `geometry-transformation`, `geometry-rotation`, `geometry-translation` |
| D3 — reflection test and quadrant map | `geometry-how-to-reflect-a-figure-across-the-y-axis`, `geometry-quadrant`, `geometry-reflection`, `geometry-coordinate-pair-also-ordered-pair` |
| D4 — translation-offset system | `statistics-and-probability-system-of-equations`, `geometry-translation`, `geometry-coordinate-pair-also-ordered-pair` |
| D5 — registration-error-per-minute ratio and deadline check | `measurement-ratio` |

## Reverse check — every claimed standard traced back to a deliverable

| Skill id | Kind | Forced by |
|---|---|---|
| `geometry-congruent` | term | D2 |
| `geometry-similar` | term | D2 |
| `geometry-how-to-reflect-a-figure-across-the-y-axis` | how-to | D3 |
| `geometry-quadrant` | term | D3 |
| `geometry-coordinate-pair-also-ordered-pair` | term | D2, D3, D4 |
| `geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane` | how-to | D2 |
| `geometry-transformation` | term | D2 |
| `geometry-translation` | term | D2, D4 |
| `geometry-rotation` | term | D2 |
| `geometry-reflection` | term | D3 |
| `advanced-operations-scientific-notation` | term | D1 |
| `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` | how-to | D1 |
| `measurement-ratio` | term | D1, D5 |
| `advanced-numbers-how-to-find-the-percent-of-a-number` | how-to | D1 |
| `statistics-and-probability-system-of-equations` | term | D4 |

## The "forces" test applied

For each mapping above: *could a competent student produce this deliverable correctly without
ever performing this skill?*

- **D2** cannot be answered without computing coordinate-pair distances, and cannot be *decided*
  (congruent vs. similar vs. neither) without genuinely distinguishing a rotation/translation
  relationship from a scale change — the deliverable's own instruction requires stating which.
- **D3** cannot be answered without actually reflecting a point across the y-axis and reading off
  each point's quadrant — the deliverable asks for both explicitly, on real coordinates.
- **D4** cannot be answered without setting up and solving a two-equation system for (Δx, Δy) —
  there is no shortcut that skips solving for the offset.
- **D1** cannot be answered without converting real, sourced vertex/triangle counts into
  scientific notation and computing a percent of a whole.
- **D5** cannot be answered without forming and comparing a millimeters-per-minute ratio for each
  option — that ratio *is* the case's primary metric.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 15    new_coverage: 0 (reinforcement case, see note above)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```
