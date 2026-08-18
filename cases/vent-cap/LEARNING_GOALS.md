# Learning Goals — Vent Cap

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-08-12.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — name the shape, count faces/edges | `geometry-how-to-name-a-3-d-shape`, `geometry-face`, `geometry-edge`, `geometry-pyramid`, `geometry-3-dimensional` |
| D2 — describe each layout's net; verify seam-edge congruence | `geometry-how-to-draw-the-net-of-a-3-d-shape`, `geometry-fundamentals-of-geometry-congruent`, `geometry-net` |
| D3 — material cost (sheets needed) | `advanced-numbers-how-to-divide-decimal-numbers` (already covered) |
| D4 — labor cost (total seams) | `basic-operations-how-to-multiply-any-two-numbers` (already covered) |
| D5 — total cost verdict | `advanced-numbers-how-to-find-the-percent-of-a-number` (already covered) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 10    new_coverage: 6
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `how-to-name-a-3-d-shape` — D1 explicitly requires naming the vent cap's shape correctly (a
  square pyramid); a Hero who cannot apply the naming convention (base shape + "pyramid") cannot
  complete this deliverable.
- `face`, `edge` — D1 requires stating both counts *and* showing how they were counted (not just
  quoting a memorized number for "a pyramid"), which requires understanding what a face and an
  edge actually are on this specific open-bottomed shape (4 triangular faces, no base face; 8
  edges — 4 base edges + 4 slant edges — a genuine count a Hero has to work out, not recall).
- `pyramid` — the term itself, forced by D1's naming requirement and used throughout D2-D5's
  descriptions of "the pyramid," "each triangular face," etc.
- `how-to-draw-the-net-of-a-3-d-shape` — D2 explicitly requires describing each layout's net
  (piece count and shape); there is no way to compare "4 separate triangles" against "1 folded
  pair + 2 triangles" without unfolding the 3D shape into its flat net first.
- `fundamentals-of-geometry-congruent` — D2 explicitly requires verifying every weld seam edge is
  the same length using the sum/difference of the two other known measurements (base edge and
  slant height, via the Pythagorean relationship), a basic equal-measure congruence check distinct
  from the Transformations-group sense of "congruent" (which Company Front already closed via a
  transformation-preserves-shape argument) — this is a side-length equality check on a static
  figure, the sense this Fundamentals-of-Geometry duplicate label actually names.

D3/D4/D5 intentionally claim no new skill — they are real, load-bearing deliverables (the actual
dollar comparison this case is built around) but exercise only already-covered arithmetic
(division with ceiling/rounding, multiplication, sum, percent difference), so nothing new is
claimed for them, consistent with the anti-inflation doctrine.

No skill here is claimed on the strength of "the case is about manufacturing generally" — each one
traces to a specific verb in a specific deliverable.
