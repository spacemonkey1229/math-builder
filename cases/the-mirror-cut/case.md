Case Study: The Mirror Cut
MS | Math | Case Study | 2026-27 | Heroes Academy

## Overview

Sam Delgado has the nesting file open on one monitor and the bid deadline open on the other:
9:00 AM tomorrow.

Sam runs production at Kestrel Sheet Metal, a six-person shop that has never bid on anything this
big. The contract is for a regional solar installer's racking brackets — the same bracket, stamped
and laser-cut from steel, year after year, mounted under every panel the company installs across
the region. Whichever nesting layout the quote is built on tonight is the layout the shop runs for
the life of the contract. Underquote the steel and Kestrel eats the difference on every bracket, for
years. Overquote it and one of the two much bigger shops also bidding on this job wins on price
alone, and Kestrel doesn't get a second chance at a contract this size.

Sam pulls up both nesting files side by side on the cutting-software screen. One lays every bracket
down the sheet in the same orientation, straight rows, easy to check at a glance — the programmer's
first pass, the one anybody in the shop could run without a second look. The other alternates every
other bracket upside-down, tucked into the gap the first one leaves — tighter, more steel actually
turned into parts, but a longer, fussier toolpath that takes the machine more time to cut.

The shop's laser tech leans into the doorway. "Whichever file you send to the machine tonight is
the one we're quoting the customer on. Which one actually wins?"

Sam pulls up the takeoff spreadsheet and starts counting brackets per sheet.

## Background

Sam Delgado is the production lead at Kestrel Sheet Metal, a small job shop that fabricates
custom steel brackets and mounting hardware. Sam is responsible for the number that goes on
tomorrow's bid: the true cost to cut one finished bracket, because that number becomes the price
Kestrel quotes for the entire contract — a fixed quantity of **40,000 identical brackets every
year, for three years**, the largest order the shop has ever bid on.

A laser-cutting nesting file is the arrangement of parts on a steel sheet before the machine ever
fires. **Nesting** software lays copies of a part down on a rectangular sheet using **translations**
(sliding a copy to a new position without turning it), **reflections** (flipping a copy over a
line, producing its mirror image), **rotations** (turning a copy about a fixed point), and
**dilations** (scaling a copy up or down by a **scale factor**, used here to build the small
checking gauges the shop verifies parts against, not the production parts themselves). Two nesting
files are on the table for the same bracket.

**The Straight Run** repeats the bracket down the sheet in the same orientation every time — every
copy is a plain **translation** of the one before it. It is the layout a new hire could run on day
one: nothing to double-check, nothing that can be loaded upside-down by mistake.

**The Mirror Cut** alternates the bracket's orientation from row to row — every other copy is a
**reflection** of its neighbor across the seam between them, tucked so its narrow end nests into
the wide end of the row above. That interlocking is what turns more of each sheet into finished
brackets instead of scrap — but it is a longer, more careful toolpath: more places the laser has to
lift and re-pierce the metal instead of cutting one long continuous line, and a slower pass near
every seam where two mirrored brackets sit close enough together that heat from one cut can warp
the part waiting next to it (SEE APPENDIX E).

The bracket itself is Sam's own part drawing, not a public design: a single flat trapezoid, corners
at exact coordinates on a plan-view coordinate grid, in inches (SEE APPENDIX A). Every sheet is the
same commercially stocked **48 in × 120 in steel sheet**, 16-gauge cold-rolled (SEE APPENDIX B),
priced by the pound. Every cut — simple or mirrored — costs the shop machine time at the laser's
real cutting speed and pierce time, priced at the shop's blended machine-and-labor rate (SEE
APPENDIX C). The full sheet-by-sheet comparison, including how many finished brackets each layout
actually yields per sheet, is in APPENDIX D. All figures in this case are sourced in APPENDIX F, or
stated as an explicit modeling assumption in APPENDIX E where no public figure exists for this
exact shop, this exact part. The vocabulary and the "how to…" skills this case will ask of you are
listed in APPENDIX H — that is where Challenge 1 sends you. (SEE APPENDIX G for further reading on
nesting software and laser-cutting cost.)

## Dilemma

You are Sam Delgado.
Do you:
A.) Send The Mirror Cut to the machine tonight — every other bracket reflected and interlocked, more
brackets per sheet, a longer and more careful toolpath OR
B.) Send The Straight Run to the machine tonight — every bracket in the same orientation, simpler
and faster to program and to run, more scrap per sheet

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A coordinate-plane sketch (or plot) of the bracket's four vertices (SEE APPENDIX A), showing
    The Straight Run layout built by translating the bracket twice down the sheet — label each
    translated copy's new vertex coordinates directly on the sketch.
    D2. A coordinate-plane sketch showing The Mirror Cut's interlocking pair: reflect the bracket
    across the x-axis, then translate the reflected copy by the stated kerf spacing (SEE APPENDIX
    E) so it nests against the original. Give the new copy's four vertex coordinates, identify the
    line of symmetry of the two-part interlocked pair, and verify with coordinates that the pair is
    actually symmetric about that line.
    D3. Show that rotating the original bracket 180° about the midpoint you identified in D2
    produces the exact same interlocked outline (as a set of points) that D2's reflection-then-
    translation produced — compute the rotated coordinates and compare them directly to D2's.
    D4. The two-part interlocked block from D2/D3 has to fit the laser bed either way it's loaded.
    Rotate the block's bounding-box corners 90° counterclockwise about the origin and give the new
    bounding box's dimensions.
    D5. The shop's quality-control station checks a sample bracket against a scaled-down gauge (SEE
    APPENDIX A). Find the scale factor of the dilation that maps the full-size bracket to the
    existing gauge, then use a stated new scale factor to dilate the bracket's coordinates and find
    the vertices of a second gauge at that new size.
    D6. A full nesting takeoff comparing both layouts: brackets per sheet, material cost per
    bracket, and machine-time cost per bracket for each layout (SEE APPENDIX D) — combined into net
    cost per finished bracket, the case's primary comparison number. State which layout wins on
    that number and by how much.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Bracket Coordinate Reference

Sam's own part drawing for this contract — not a public design, but built entirely from real,
standard coordinate-plane geometry. All coordinates are plan-view, in inches, one grid unit = 1 in.

| Vertex | Coordinates (in) |
|---|---|
| A (bottom-left) | (0, 0) |
| B (bottom-right) | (6, 0) |
| C (top-right) | (4.5, 4) |
| D (top-left) | (1.5, 4) |

| | Value |
|---|---|
| Shape | Isosceles trapezoid, bottom edge AB parallel to top edge DC |
| Bottom width (AB) | 6.0 in |
| Top width (DC) | 3.0 in |
| Height | 4.0 in |
| Perimeter | 17.544 in |
| Area (shoelace formula on A, B, C, D) | 18.0 sq in |
| Bounding box | 6.0 in wide × 4.0 in tall |

**QC checking gauge.** The shop's existing quality-control gauge is a scaled-down copy of this same
outline, used to spot-check a sample bracket at the machine without pulling out the full-size
drawing:

| Vertex | Gauge coordinates (in) |
|---|---|
| A′ | (0, 0) |
| B′ | (3, 0) |
| C′ | (2.25, 2) |
| D′ | (0.75, 2) |

## Appendix B — Sheet Stock & Material Pricing

| | Value |
|---|---|
| Sheet size, both layouts | 48 in × 120 in [S1] |
| Sheet thickness / gauge | 16-gauge (0.060 in) cold-rolled steel [S2] |
| Weight per square inch | 0.017 lb/sq in [S2] |
| Sheet weight (48 in × 120 in) | 97.92 lb |
| Price per pound | $2.94/lb [S2] |
| Material cost per sheet | $287.88 |
| Kerf / part-to-part spacing margin used in the takeoff | 0.25 in, both layouts |

## Appendix C — Cutting, Piercing & Machine-Rate Reference

| | Value |
|---|---|
| Laser cutting speed, The Straight Run, 16-gauge mild steel | 25 m/min → 984.25 in/min [S3] |
| Pierce time per pierce, thin-gauge steel | 0.3 sec [S4] |
| Wage, metal and plastic machine workers (U.S. median) | $22.94/hr [S5] |
| Fiber-laser machine operating cost (oxygen assist, carbon steel) | $7.00/hr [S6] |
| Blended machine-and-labor rate used in this case | $29.94/hr |
| Real-world material-yield improvement, mirrored vs. simple nesting | 10–15%, case uses 12% [S7] |

## Appendix D — Nesting Takeoff

| | The Straight Run (B) | The Mirror Cut (A) |
|---|---|---|
| Slot per bracket (bounding box + 0.25 in margin) | 6.25 in × 4.25 in | 6.25 in × 4.25 in (pre-yield) |
| Brackets per sheet | 196 | 219 |
| Material cost per sheet | $287.88 | $287.88 |
| Material cost per bracket | $1.4688 | $1.31454 |
| Pierces per bracket (SEE APPENDIX E, MA1) | 1 | 2 |
| Cut speed used (SEE APPENDIX E, MA2) | 984.25 in/min (full speed) | 688.975 in/min (70% of full speed) |
| Cut time per bracket | 1.0695 sec | 1.5278 sec |
| Pierce time per bracket | 0.3 sec | 0.6 sec |
| Machine-time cost per bracket | $0.01139 | $0.01770 |
| **Net cost per finished bracket (material + machine time)** | **$1.48019** | **$1.33224** |
| Brackets needed per year | 40,000 | 40,000 |
| Sheets needed per year | 204.1 | 182.6 |

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and Appendix H names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Pierces per bracket, The Mirror Cut, as a multiple of The Straight Run's one pierce per bracket | **2× (2 pierces/bracket)** | Tightly interlocked, mirrored nests are commonly pre-pierced ahead of full contour cutting to manage heat buildup between closely spaced parts, rather than cut as one continuous pass — a real, documented nesting practice (SEE APPENDIX F). No public per-shop study times this exact multiplier for this exact part geometry; the 2× figure is the case author's own estimate from how the operation is actually sequenced. | Not enough on its own to flip the primary metric (material cost dominates the per-bracket total). Flexed ±50% in Tier 2 probe 5. |
| MA2 | Cutting speed, The Mirror Cut, as a fraction of The Straight Run's sourced cutting speed | **70% (a 30% slowdown)** | Closely nested, alternating-orientation parts require the machine to sequence and pace cuts so heat has room to dissipate between adjacent brackets rather than building up and warping them — a real, documented general phenomenon in laser nesting (SEE APPENDIX F). No public per-shop study measures this exact slowdown for this exact geometry; 70% is the case author's own estimate. | Same as MA1 — moves the machine-time line but does not by itself flip the primary metric. Flexed ±50% in Tier 2 probe 5. |
| MA3 | Rejected-part rate from heat-affected-zone distortion, each layout | **The Straight Run: 1%. The Mirror Cut: 4%.** | Heat-affected-zone buildup between closely nested, alternating-orientation parts is a real, documented distortion risk (SEE APPENDIX F); The Mirror Cut's tighter spacing carries more of that risk than The Straight Run's more open layout. No public per-shop reject-rate study exists for this exact part and nest, so both values are the case author's own estimate. | The answer is sensitive to this value. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Standard stocked steel sheet size for laser cutting | 48 in × 120 in | Fabworks, "Max Cuttable Size for Laser Cutting" ([link](https://www.fabworks.com/faq/max-size)) | 2026-09-05 | MEDIUM — one job shop's own stocked-inventory size, generalized to "standard"; commonly corroborated elsewhere as a common commercial size, but not a national standards-body figure |
| S2 | 16-gauge (0.060 in) cold-rolled steel sheet: price and weight-per-area | $2.94/lb; 2.448 lb per 12 in × 12 in plate | SpeedyMetals, "16ga (.060") Cold Rolled, Steel Sheet" ([link](https://www.speedymetals.com/pc-2683-8244-00598-cold-rolled-steel-sheet.aspx)) | 2026-09-05 | MEDIUM — small-quantity, cut-to-size retail pricing, not a bulk mill/production contract price; a shop buying full sheets in volume would likely pay less per pound. Weight-per-area figure used to compute full-sheet weight. |
| S3 | Fiber-laser cutting speed, ~1.5 mm (16-gauge) carbon steel, 2 kW, oxygen/air assist | 25–30 m/min (case uses 25 m/min, the low end of the range) | StyleCNC, "How Fast And Thick Can Fiber Lasers Cut Through Metal?" ([link](https://www.stylecnc.com/blog/fiber-laser-cutting-metal-thickness-speed-power.html)) | 2026-09-05 | MEDIUM — a manufacturer-facing reference chart giving a range, not a single-machine spec sheet; case picks the conservative (slower) end of the sourced range |
| S4 | Pierce time, thin-gauge carbon steel | 0.3–3 sec, depending on thickness and power (case uses 0.3 sec, the low end, for thin 16-gauge stock) | Kasu Laser, "How Long Does Laser Cutting Take? Speed & Lead Times" ([link](https://kasulaser.com/how-long-does-laser-cutting-take/)) | 2026-09-05 | MEDIUM — a job-shop's general guidance page giving a range across thicknesses, not a single-thickness spec; case picks the low end appropriate to thin 16-gauge stock |
| S5 | Median wage, metal and plastic machine workers, United States | $22.94/hr (median annual $47,700), May 2025 | U.S. Bureau of Labor Statistics, Occupational Outlook Handbook, "Metal and Plastic Machine Workers" ([link](https://www.bls.gov/ooh/production/metal-and-plastic-machine-workers.htm)) | 2026-09-05 | HIGH — primary U.S. government labor statistics source |
| S6 | Fiber-laser operating cost, oxygen cutting, carbon steel, 6 kW machine | $7.00/hr (electricity + assist gas + consumables, excludes labor and depreciation) | Arcus CNC, "Laser Cutter Cost Breakdown: Machine, Maintenance, and Operations" ([link](https://arcuscnc.com/laser-cutter-cost/)) | 2026-09-05 | MEDIUM — a single vendor's worked cost breakdown for one machine class, used here as a stand-in for Kestrel's own unstated machine, combined with S5's labor wage to build this case's blended rate |
| S7 | Real-world material-yield improvement from mirrored/advanced nesting vs. basic nesting | 10–15% direct material savings from tighter part clustering (case uses 12%, a value picked within the sourced range) | SLTL Group, "Nesting Software and Material Optimization: How Manufacturers Save Up to 20 Percent Cost" ([link](https://www.sltl.com/nesting-software-and-material-optimization-how-manufacturers-save-up-to-20-percent-cost/)) | 2026-09-05 | MEDIUM — a nesting-software vendor's own published figure; directionally consistent with other vendor sources found (e.g. true-shape nesting quoted elsewhere at 10–15%), but no independent third-party audit was found |
| S8 | Heat-affected-zone buildup and distortion risk between closely nested parts; cut-sequencing/cooling mitigation | "Tight clusters of cuts concentrate heat in one area"; "Sequence cuts so heat is spread across the sheet instead of stacked in one spot, and let an area cool before cutting next to it." | Reger Laser, "Understanding Thermal Stress and Part Distortion in Laser Cutting" ([link](https://www.regerlaser.com/understanding-thermal-stress-in-laser-cutting/)); corroborated by Hightech Industry Group, "How to Prevent Material Warping During Laser Cutting" ([link](https://htindustryco.com/blog/how-to-prevent-material-warping-during-laser-cutting/)) | 2026-09-05 | MEDIUM — general, real, well-corroborated phenomenon across two independent fabrication-industry sources; used as the basis for MA1/MA2/MA3's mechanism, not for their specific numeric values, which remain stated assumptions |

## Appendix G — Learn More

Curious about the real-world math and industry behind this case? These resources go beyond what
the challenges require.

- [Nesting (manufacturing) — Wikipedia](https://en.wikipedia.org/wiki/Nesting_(process)) — background on nesting algorithms and why manufacturers optimize part layout on stock material.
- [SigmaNEST — nesting software](https://www.sigmanest.com/en/sigmanest) — a real, widely used commercial nesting package referenced throughout the sheet-metal fabrication industry.
- [Laser cutting — Wikipedia](https://en.wikipedia.org/wiki/Laser_cutting) — background on how a fiber laser cuts sheet metal, including piercing and kerf.
- [Board foot / sheet-good pricing conventions](https://en.wikipedia.org/wiki/Board_foot) — a related unit-pricing convention from a different material trade (lumber), useful for comparing how different fabrication industries price by weight or volume.
- [Heat-affected zone — Wikipedia](https://en.wikipedia.org/wiki/Heat-affected_zone) — the metallurgical effect behind Appendix E's MA1–MA3 heat-management assumptions.
- [Rotation (mathematics) — Wikipedia](https://en.wikipedia.org/wiki/Rotation_(mathematics)) — background on rotating coordinates about a fixed point, used in D3 and D4.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Translation
- Reflection
- Rotation
- Symmetry
- Line Of Symmetry
- Dilation
- Scale Factor

**"How to…" questions**

- How to translate a figure on the coordinate plane
- How to reflect a figure across the X-Axis
- How to rotate a figure on the coordinate plane 90 degrees counterclockwise
- How to rotate a figure on the coordinate plane 180 degrees
- How to dilate a figure on the coordinate plane given a scale factor
- How to find the scale factor of a dilation
- How to multiply decimal numbers
- How to divide decimal numbers
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
