# Learning Goals — The Mirror Cut

Bidirectional deliverable ↔ skill matrix. `case-write`, 2026-09-05.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — translate the bracket twice down the sheet, label new coordinates | `geometry-translation`, `geometry-how-to-translate-a-figure-on-the-coordinate-plane` |
| D2 — reflect across x-axis + translate to build the interlocked pair; find and verify the line of symmetry | `geometry-reflection`, `geometry-how-to-reflect-a-figure-across-the-x-axis`, `geometry-symmetry`, `geometry-line-of-symmetry` |
| D3 — rotate 180° about the D2 midpoint; show it matches D2's outline | `geometry-rotation`, `geometry-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees` |
| D4 — rotate the bounding box 90° CCW about the origin | `geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise` |
| D5 — find the scale factor to the existing gauge; dilate to a new gauge | `geometry-scale-factor`, `geometry-how-to-find-the-scale-factor-of-a-dilation`, `geometry-dilation`, `geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor` |
| D6 — full nesting takeoff, net cost per bracket, verdict | `advanced-numbers-how-to-multiply-decimal-numbers`, `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-find-the-percent-of-a-number` (all already covered) |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 16    new_coverage: 0
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS (new_coverage[] genuinely empty -- see case.json.reinforcement_note)
```

**Forcing test applied to each claimed skill** (*could a competent Hero produce the deliverable
correctly without ever performing this skill?*):

- `geometry-translation` / `how-to-translate-a-figure-on-the-coordinate-plane` — D1 requires
  producing the actual translated vertex coordinates for two successive copies; a Hero who cannot
  translate a point cannot produce correct coordinates, only a correct-looking sketch.
- `geometry-reflection` / `how-to-reflect-a-figure-across-the-x-axis` — D2 requires computing the
  reflected vertex coordinates directly from the original ((x, y) → (x, −y)), not just describing
  "flipping it over."
- `geometry-symmetry`, `geometry-line-of-symmetry` — D2 requires identifying the specific
  horizontal line the interlocked pair is symmetric about (y = −0.125) and verifying, with the
  actual vertex coordinates, that corresponding points are equidistant from it. A Hero who cannot
  find or test a line of symmetry cannot complete this half of D2.
- `geometry-rotation` / `how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees` — D3 requires
  computing the 180°-rotated coordinates about a specific, non-origin point and comparing them,
  point for point, against D2's independently-derived reflection. This is not satisfiable by
  assertion; the two coordinate sets either match or they don't.
- `how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise` — D4 requires
  applying the 90° CCW rotation rule ((x, y) → (−y, x)) to four bounding-box corners and reporting
  the resulting dimensions; a Hero who cannot apply the rule gets the wrong bounding box.
- `geometry-scale-factor` / `how-to-find-the-scale-factor-of-a-dilation` — D5 requires computing
  the ratio between the gauge's coordinates and the bracket's own coordinates, not naming the
  concept.
- `geometry-dilation` / `how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor` — D5's
  second half requires applying a *given* scale factor to the bracket's coordinates to produce a
  new gauge's vertices — the inverse operation from the first half, both genuinely required.

D6 intentionally claims no *new* skill and no *new* Transformations skill — it is the case's real,
load-bearing comparison (the actual net-cost-per-bracket verdict this case is built around) but
exercises only already-covered arithmetic (multiplication, division, percent), consistent with the
anti-inflation doctrine (same pattern as Roofline Call's D5).

No skill here is claimed on the strength of "the case is about nesting generally" — each one traces
to a specific, checkable requirement in a specific deliverable.

## Why `new_coverage[]` is genuinely empty (not padding)

The approved concept named 12 concrete Geometry/Transformations skill ids as candidates. All 12
were verified against `readmodel/standards_spine.json` on 2026-09-05 and **all 12 already have
`n>=2`** — the entire Transformations group is pre-covered by earlier cases in this corpus. Two
more terms (`geometry-reflection`, `geometry-rotation`) that this case's own deliverables clearly
also force were added for vocabulary completeness (Appendix H's terms list); both are likewise
`n>=3`/`n>=4`. A full spine sweep for any skill anywhere in the project sitting at `n==0` turned up
exactly six: `number-sense-depth`, `number-sense-digit`,
`geometry-how-to-find-the-volume-of-a-sphere`,
`calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions`,
`calculus-taylor-series`, `calculus-how-to-find-the-taylor-series-of-a-function-at-a-point` — none
of which this case's actual math (2-D coordinate transformations on a bracket outline, a linear
cost takeoff) forces or comes close to forcing. Claiming any of them would be exactly the fabricated
mapping this check exists to catch. `case.json.reinforcement_note` records this check per the
2026-08-17 T1-10 reinforcement carve-out.

## Of the 12 explicitly-named candidate skills, 11 are forced; 1 was deliberately dropped

`geometry-how-to-reflect-a-figure-across-the-y-axis` is **not** claimed. The case's mirrored
layout only needs a horizontal-seam mirror (rows alternating up/down, forced via reflection across
the x-axis in D2) — there is no genuine second, vertical-seam mirroring operation anywhere in this
case's actual deliverables. Adding a second nesting axis purely to also claim the y-axis reflection
how-to would be padding with no independent forcing test to pass, exactly the kind of fake mapping
this check exists to catch. The other 11 of the 12 named candidates are all genuinely forced, as
detailed above.
