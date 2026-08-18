# LEARNING GOALS — Plaza Pavers

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 "Ruled Out" polygon reference table | geometry-pentagon, geometry-hexagon, geometry-heptagon, geometry-octagon, geometry-nonagon, geometry-decagon, geometry-dodecagon, geometry-n-gon, geometry-regular-polygon, geometry-sum-of-the-interior-angles-of-a-polygon-theorem, geometry-rhombus, geometry-kite |
| D2 coordinate-plane transformation diagram | geometry-transformation, geometry-translation, geometry-symmetry, geometry-line-of-symmetry, geometry-clockwise, geometry-counter-clockwise, geometry-how-to-translate-a-figure-on-the-coordinate-plane, geometry-how-to-reflect-a-figure-across-the-x-axis, geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise, geometry-reflection, geometry-rotation |
| D3 border-cut worksheet | geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles, geometry-vertical-angles, geometry-supplementary-angles |
| D4 grid-modulus (GCF) calculation | basic-operations-greatest-common-factor, basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers |
| D5 installed-cost-per-sq-ft table | geometry-area, geometry-how-to-find-the-area-of-a-regular-polygon, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 31    new_coverage: 25
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Forces test applied to each mapping** ("could a competent student produce this deliverable
without ever performing this skill?"):

- D1 — no. The table's own columns (interior angle, tiles-alone-or-not) cannot be filled without
  computing each n-gon's interior angle and applying the tiling test; naming rhombus/kite forces
  distinguishing "doesn't tile" from "tiles but was rejected anyway," which forces knowing both
  shapes by name.
- D2 — no. "Show how the unit is built from a starting tile" cannot be satisfied by describing
  the pattern in words; it requires an actual translate/reflect/rotate sequence with directions
  and symmetry lines marked on a real coordinate grid.
- D3 — no. Finding a missing angle on an irregular cut piece requires the interior-angle-sum
  theorem; labeling vertical/supplementary pairs requires knowing those relationships by name,
  not just "the angles add up."
- D4 — no. "Largest jig size with no partial-inch remainder on both directions" is the textbook
  GCF question restated in trade language; there's no way to answer it without computing a GCF.
- D5 — no, though this deliverable also leans on already-covered arithmetic (percent-of-a-number
  for waste-factor math); `geometry-area` and `geometry-how-to-find-the-area-of-a-regular-polygon`
  are forced because "cost per square foot" requires knowing the plaza's and each paver's area.

**Already-covered skills also exercised, not claimed in `new_coverage[]`:** `geometry-regular-polygon`
(n=1), `geometry-reflection` (n=1), `geometry-rotation` (n=1), `geometry-area` (n=6),
`geometry-how-to-find-the-area-of-a-regular-polygon` (n=6), `advanced-numbers-how-to-find-the-percent-of-a-number`
(n=17).
