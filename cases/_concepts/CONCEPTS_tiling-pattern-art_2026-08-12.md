# Concept sheet — Tessellation, Tiling & Pattern Art (`tiling-pattern-art`)

Single-concept sheet. Target pre-selected from `ROADMAP.md` §B4 item 1 ("Tiling / pattern
commission — hits the polygon *and* transformation clusters at once") rather than generated from
a fresh gap-queue scan. Approved by the user's standing instruction to work Queue 1 in order
(2026-08-12 session).

### C1 — Plaza Pavers · score ~19.3 (raw 22.6 how-to/term-weighted + 2.0 group bonus toward the
Quadrilaterals And Polygons ceiling) · tier T3

**Protagonist.** Priya Nakamura, senior designer at Cascadia Hardscape Design & Build, submitting
the firm's final bid on a public plaza restoration. Personally at stake: her firm's owner handed
her sole lead on this bid as a test, and the city's arts commission has published a hard per-square-
foot cost cap that a rival firm has already underbid using the cheap option.

**The dilemma.** A.) The Hex Grid — pave the full plaza in one regular-hexagon paver, edge to
edge, zero interior cut waste OR B.) The Weave Pattern — pave in the commission's preferred
octagon-and-square paver combination (matching the plaza's original historic pavement), which
needs cut pavers at every straight border.

**Primary metric.** Total installed cost per square foot of finished plaza (materials + cutting
labor + waste).

**Why it's close.** The Weave Pattern uses two paver SKUs and needs mitred cuts at every straight
edge, which is real labor and real waste — but its larger paver footprint per piece means fewer
total units to set (less per-unit labor) than the alternative, and its historic match may carry
its own value to the commission that a pure cost comparison doesn't capture. The Hex Grid has zero
interior waste but the plaza's non-hexagonal rectangular border still forces some edge cutting of
its own — just less than the Weave Pattern's.

**Would close (25 skills, 18 how-to+term-weighted / mix — see table):**

| id | kind | label |
|---|---|---|
| geometry-transformation | term | Transformation |
| geometry-translation | term | Translation |
| geometry-symmetry | term | Symmetry |
| geometry-line-of-symmetry | term | Line Of Symmetry |
| geometry-clockwise | term | Clockwise |
| geometry-counter-clockwise | term | Counter-Clockwise |
| geometry-how-to-translate-a-figure-on-the-coordinate-plane | how-to | How to translate a figure on the coordinate plane |
| geometry-how-to-reflect-a-figure-across-the-x-axis | how-to | How to reflect a figure across the X-Axis |
| geometry-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-clockwise | how-to | How to rotate a figure on the coordinate plane 90 degrees clockwise |
| geometry-pentagon | term | Pentagon |
| geometry-hexagon | term | Hexagon |
| geometry-heptagon | term | Heptagon |
| geometry-octagon | term | Octagon |
| geometry-nonagon | term | Nonagon |
| geometry-decagon | term | Decagon |
| geometry-dodecagon | term | Dodecagon |
| geometry-rhombus | term | Rhombus |
| geometry-kite | term | Kite |
| geometry-n-gon | term | N-gon |
| geometry-vertical-angles | term | Vertical Angles |
| geometry-supplementary-angles | term | Supplementary Angles |
| basic-operations-greatest-common-factor | term | Greatest Common Factor |
| basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers | how-to | How to find the greatest common factor of a set of numbers |
| geometry-sum-of-the-interior-angles-of-a-polygon-theorem | term | Sum of the interior angles of a polygon theorem |
| geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles | how-to | How to find the measure of an interior angle of a polygon given the other angles |

Deliberately **excludes** dilation, scale factor, congruent, similar, reflect-across-Y-axis,
rotate-90-CCW, rotate-180 — `ROADMAP.md` reserves those for concepts 2/3/6 in the same queue
(drill design, sheet-metal nesting, image registration), so this case does not compete with them
for `new_coverage[]`.

**Already-covered skills it also exercises.** `geometry-regular-polygon` (n=1), `geometry-reflection`
(n=1), `geometry-rotation` (n=1) — all already covered elsewhere, listed in `standards[]` but not
`new_coverage[]`.

**Data feasibility: MEDIUM**, matching `domains.json`'s own grade for this domain — the geometry
leg is HIGH (interior-angle math is provable, not sourced) but the cost leg needs live retailer
data. Named sources I expect to exist:
- A real hardscape paver manufacturer's published spec sheet for a hexagonal and an octagon+square
  paver set (e.g. Belgard, Techo-Bloc, Unilock product pages) — module dimensions, HIGH.
- Angi/HomeGuide or a comparable contractor-cost aggregator's published $/sq ft ranges for simple
  vs. cut/intricate paver patterns — MEDIUM (aggregated, not a single primary source).
- A real US public plaza renovation project's published footprint and budget (a city capital-
  improvement or public-art-commission document) as the basis for this case's fictional plaza's
  figures — MEDIUM, will likely need assembling from more than one document.

Sources I am NOT confident about: an exact historic-pattern-match cost premium (if the commission's
preference for matching history carries a stated dollar value anywhere public) — likely a stated
Modeling Assumption.

**Sensitivity (SPEC §6).** None required — stakes are commercial (a firm's bid, a career test), not
personal loss or hardship.

**Split risk.** None. 25 skills against a group ceiling in the high 20s (Transformations has 20
total skills group-wide, Quadrilaterals And Polygons has 22) is within the single-case range this
project has already shipped (Cold Chain, Tide Window both ran double-digit `new_coverage[]`).

## Recommendation

Write C1 as specified. It is the only concept on this sheet — Queue 1 (`ROADMAP.md` §B4) already
ranked and pre-selected it as item 1, and the user's session instruction is to work the queue in
order, so this sheet documents the concept rather than re-litigating the ranking.

**Next step:** approved by queue order — proceed to `case-write`.
