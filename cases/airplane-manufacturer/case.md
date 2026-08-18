# Case Study: Airplane Manufacturer

MS | Math | Case Study | 2026-27 | Heroes Academy

---

## Overview

The laser cutter isn't even bolted to the floor yet, and Drew Larson is already staring at two spec sheets. Sparks from the neighboring bay throw orange light across the shop as a tech runs cable to the new machine — eight thousand watts of fiber laser, sitting in its packaging like a racehorse still in the trailer. Drew's phone buzzes on the workbench, face down, for the third time in ten minutes. Boeing again, probably. Or the CFO, who has asked twice this week when the new line starts paying for itself.

Drew turns back to the two folders spread across a steel table still tacky with cutting oil. One holds a spec sheet for a turbine disk — flat, toothed, unglamorous. The other holds a spec sheet for an inlet O-ring — the polished band that caps a jet engine's nacelle, the part passengers actually see through the window. Both folders end in the same number Drew keeps circling: how many of these, cut from the same sheets of aircraft aluminum, on the same machine, can this company actually produce.

The tech gives a thumbs up — the machine is live. Drew picks up both folders, walks toward the office where the pitch has to be written by Friday, and doesn't put the phone away.

---

## Background

Stout Aviation is a privately owned company in Arizona that manufactures components for large jet engines, specializing in sheet metal fabrication — cutting and shaping large flat sheets of aluminum alloy into finished engine parts. The airline manufacturer Boeing is Stout Aviation's largest client.

As the airline industry has grown, demand for new planes and parts has pushed Stout Aviation's production up nearly 20% year over year for the past five years. To keep pace, Stout Aviation just approved the purchase of an additional fiber CNC laser cutting machine (**SEE APPENDIX A**), and has tasked the company's Chief Strategy Officer, **Drew Larson**, with researching and deciding which new engine component the company should begin producing with it (**SEE APPENDIX B AND APPENDIX C**).

Stout Aviation plans to run the new machine at most 20 hours per day, 5 days a week, with at least 2 hourly employees running the machine and loading sheet metal at all times. Each employee is paid an average of **$45.00 per hour**.

Through months of research and contacts inside Boeing, Drew has identified rising demand for two possible components: **inlet O-rings** and **turbine disks**. Drew is confident Stout Aviation could succeed financially with either. Both components are cut from sheets of **7 meter by 5 meter, 2024-T3 aluminum alloy**, which cost Stout Aviation **$76.80 per square meter** to purchase. Stout Aviation resells all excess scrap aluminum back to the distributor at **$23.45 per square meter**.

Every net dimension, cost, and modeling convention this case depends on — including how the two parts are cut from a sheet and how their costs are built up — is fixed in **APPENDIX B**, **APPENDIX C**, and the **Modeling Assumptions** at the end of this document; use those conventions, or your numbers won't match anyone else's.

Drew Larson has worked at Stout Aviation for 3 years, specializing in industry strategy and market research, including deciding which products the company produces and sells.

Every dollar figure and dimension in this case is either given directly by Stout Aviation's own records above, resolved in the Modeling Assumptions, or backed by real-world plausibility context in **APPENDIX D** (Sources).

The vocabulary and "how to…" skills this case will ask of you are listed in **Appendix E** — that is where Challenge 1 sends you.

---

## Dilemma

You are Drew Larson.

Do you:

**A.)** Pitch to produce **turbine disks** **OR**

**B.)** Pitch to produce **inlet O-rings**

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A dimensioned net of each component**, drawn to scale, labeling every straight edge, curved edge, and hole with its measurement (Appendix B, Appendix C). Note on your net which component stays flat (2-D) and which is bent into its final 3-D shape. On the turbine disk's net, label the square core as a quadrilateral, mark each of its 12 tooth tips as a vertex, and mark the 12 inward notches where teeth meet as concave vertices — the disk's full outline is an irregular polygon, not a regular one, and your labeling should show why.
- **D2 — The cut-path length (in meters) the laser must travel to cut one of each component** — every edge and every hole the machine has to trace, not just the outer boundary.
- **D3 — How long it will take the CNC machine to cut one of each type of component**, using the machine's rated cutting speed (Appendix A).
- **D4 — The net material area (in square meters) of one of each component** — the actual finished-part footprint, not the rectangular space it takes up on the sheet — and what percent of one full sheet a single part uses.
- **D5 — The maximum number of your chosen component Stout Aviation can produce in one week**, accounting for how many parts fit on one sheet, the machine's load time between sheets (Appendix A), and the maximum weekly operating hours (Background).
- **D6 — The total cost, profit, and profit margin (as a percent) for one unit of your chosen component**, and how long it will take Stout Aviation to break even on the cost of the new machine.
- **D7 — A recommendation** comparing turbine disks and inlet O-rings side by side on cut time, weekly production capacity, and profitability.
- **D8 — Cutting efficiency**: for each component, divide your D3 cut time by your D4 net area to get minutes of laser time required per square meter of finished part. Which component uses the machine's time more efficiently, and by what percent?

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: CNC Machine Specifications

Stout Aviation's newly approved machine:

| Spec | Value |
|---|---|
| Model | StyleCNC Multi-Purpose Sheet and Pipe Fiber Laser Cutter |
| Cost | $136,500.00 [S1] |
| Laser power | 8,000 W |
| Laser type | Raycus/IPG fiber laser |
| Maximum cutting size | 10 m x 10 m |
| Maximum cutting speed | 3 m/minute |
| Load time (time to load a new sheet of aluminum) | 35 minutes |

Note: the machine's *maximum cutting size* (10 m x 10 m) is larger than the aluminum sheets Stout Aviation actually buys (7 m x 5 m, Background) — that row describes the machine's own ceiling, not a limit that applies to this case's sheets. Likewise, laser power and laser type describe the equipment but are not inputs to any calculation in Challenge 3.

---

## Appendix B: Engine Inlet O-Ring

The inlet O-ring is the metal ring that caps a jet engine's nacelle. Stout Aviation manufactures it from a 2-D sheet of aluminum alloy, then bends the flat cut into its final 3-D ring shape. The bending and shaping process costs Stout Aviation an average of **$4,870.00** per O-ring. Stout Aviation sells each O-ring for **$5,498.00**.

**2-D Net (before bending):** a flat ring (an annulus) — a large circle with a smaller circle removed from its center.

| Dimension | Value |
|---|---|
| Outer diameter | 72 in |
| Inner diameter | 54 in |

---

## Appendix C: Turbine Disk

A turbine disk is a metal gear-shaped component for the inner workings of a turbine engine. Stout Aviation manufactures it from a 2-D sheet of aluminum alloy. Unlike the inlet O-ring, the turbine disk is **not bent** — it stays flat (2-D) as its final finished shape.

The turbine disk is a square with 12 teeth (triangular points) around its sides — 3 teeth per side — with a circular hole in the center. Stout Aviation sells each turbine disk for **$657.00**.

| Dimension | Value |
|---|---|
| Square core, side length | 28 in |
| Overall height across top and bottom teeth (source diagram, not-to-scale — see Modeling Assumptions) | 36 in |
| Number of teeth | 12 (3 per side) |
| Center hole diameter | See Modeling Assumption MA2 |

---

## Modeling Assumptions

> These figures are **not sourced** — they resolve ambiguity in the original vendor sketch (Appendix C) or fill a genuine gap in the source material. A Hero may challenge them in discussion; that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Turbine disk tooth shape | Each of the 12 teeth is an isosceles triangle with base = 28 in ÷ 3 ≈ 9.33 in and height = 4 in (derived from the 36 in overall-height label minus the 28 in square side, split evenly top and bottom: (36 − 28) ÷ 2 = 4 in) | Appendix C's own source sketch labels the teeth "equilateral triangles," but its two stated dimensions (28 in square, 36 in overall height) are mathematically inconsistent with true equilateral teeth on a 3-per-side layout (true equilateral teeth on a 9.33 in base would stand 8.08 in tall, not 4 in, giving an overall height of ~44 in, not 36 in). This case treats the sketch as an illustrative, not-to-scale drawing (common for a vendor-facing engineering sketch) and uses its two labeled dimensions directly rather than override them with a stricter geometric rule the sketch itself doesn't satisfy. | If a Hero instead insists on true equilateral teeth (8.08 in height, ~44.2 in overall span), the disk's cut-path length and area both increase — recompute D2–D4 accordingly. This does not change the weekly-profit-based recommendation of Challenge 3, since the underlying sell price and cost structure are unaffected. **It does change D8, the case's actual graded balance metric — a ±50% flex of the 36 in overall-height figure is stable in one direction but not the other; the answer is sensitive to this value.** |
| MA2 | Turbine disk center hole diameter | 9 in | **PROPRIETARY — ESTIMATED (one-time exception, 2026-08-13).** Not labeled anywhere in the source sketch, and real turbine-disk bore sizing depends on proprietary centrifugal-loading and fatigue analysis with no public standard to cite — unlike this case's other sourced figures, this number cannot be looked up. Estimated instead from the closest available PUBLIC engineering analogue: general mechanical-design guidance for a circular hole in a finite plate recommends keeping the hole-to-width ratio under ~0.3 to stay within standard stress-concentration design practice [S6]. 9 in / 28 in = 0.32, just at that boundary — the original 10 in figure (0.36) sat further outside it. This is a best-effort estimate from a general analogue, NOT a turbine-disk-specific standard, and is disclosed as such rather than presented as equivalent to this case's cited figures. | A larger or smaller hole changes D4's net area and D6's material cost slightly, but the hole accounts for well under 10% of the disk's material cost either way (material cost is a small share of total disk cost — see D6) — it does not flip the weekly-profit-based Challenge 3 recommendation. **It does change D8, the case's actual graded balance metric, and remains genuinely unstable even at this re-estimated value — the answer is sensitive to this value in one direction of a ±50% flex.** This is disclosed, not eliminated: no choice of hole diameter survives a full ±50% swing, so the honest response is to state the estimate's basis and defend it, the same as any Category-X proprietary estimate. |
| MA3 | Sheet nesting (parts per sheet) | Both components are nested in a simple, non-rotated rectangular grid: each part's square bounding box is repeated in rows and columns across the 7 m x 5 m sheet, with no offset or rotation packing. | Keeps D5's "parts per sheet" calculation a direct, checkable division rather than an optimization problem — appropriate for this case's grade band. Stout Aviation's real production planning could likely nest more parts per sheet with rotation or offset packing. | A denser nesting scheme increases both options' weekly capacity roughly proportionally, so it does not change which option produces more per week — it would raise both D5 answers, not flip the comparison. |
| MA4 | Employee wage as a machine-operating cost, not overtime/benefits-loaded | The $45.00/hour rate (Background) is treated as the fully-loaded cost Stout Aviation pays per hour, per employee, with no additional payroll burden added. | The case states $45.00/hour as "each employee is paid" with no further breakdown; adding one is inventing a number the source doesn't give. | A higher fully-loaded rate raises labor cost per part for both options roughly proportionally (labor is a small share of total cost for both parts — see D6) — it does not flip the recommendation. |

**A note on realism, not modeling.** Stout Aviation's real 2024-T3 aluminum sheet price ($76.80/m²), CNC machine price ($136,500), and hourly wage ($45.00) are the original case's own scenario figures, not independently sourced facts about the real world — but each sits inside or near the range real prices for comparable inputs actually occupy: a currently-listed 8,000 W-class fiber laser sheet cutter runs $45,000–$80,000 [S1] (this case's $136,500 sits above that single-vendor quote but within the same real market's 12,000 W tier, $85,000–$190,000, and this case's machine is a higher-spec sheet-AND-pipe combo unit, not a basic single-purpose sheet cutter); national average CNC machine operator pay runs roughly $24–$28/hour, with skilled aerospace-specification operators commanding a real premium above that average [S3]. These are cited here as plausibility context for the scenario's own numbers, not as the source of those numbers — see `legacy_conversion_note` in `case.json` for the full disclosure.

---

## Appendix D: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | 8,000 W-class fiber laser sheet cutter — currently-listed price for this case's stated machine class (replaces a prior citation whose page no longer supports the figure it was cited for — see note below) | $45,000–$80,000 | Jeesun CNC — [8kW Fiber Laser Cutting Machine](https://www.jeesuncnc.com/8kw-fiber-laser-cutting-machine/) | 2026-08-13 | MEDIUM (single-vendor listing; case's own machine is a higher-spec sheet-AND-pipe combo unit, not this basic single-purpose sheet cutter) |
| S2 | 8,000 W all-in-one sheet-and-tube fiber laser cutter, StyleCNC ST-FC3015GAR family, confirms an 8,000 W configuration exists in this exact machine class | Configuration confirmed; no public list price found | StyleCNC — [All-In-One Fiber Laser Cutter for Sheet Metals & Tubes](https://www.stylecnclaser.com/fiber-laser-cutters/all-in-one-sheet-metal-tube-fiber-laser-cutter.html) | 2026-08-13 | MEDIUM |
| S3 | US average CNC machine operator hourly pay, 2026 — context for this case's stated $45.00/hour wage | ~$23.65–$28/hour (national average, general CNC operator) | ZipRecruiter / Salary.com — [CNC Machine Operator Salary](https://www.ziprecruiter.com/Salaries/Cnc-Machine-Operator-Salary) | 2026-08-13 | MEDIUM (national average, not aerospace-specific or Arizona-specific) |
| S4 | 6,000 W-class fiber laser electricity cost — quantitative basis for the O-ring's real-but-modest weekly energy savings, cited in the Balance Argument's argument for B | $5.40–$7.50/hour (18–25 kW wall draw at $0.12/kWh, $10,800–$15,000/year over 2,000 hr/year) | Remcor Technology — [Fiber Laser Cutting Machine Total Cost of Ownership (TCO) 2026](https://www.remcortechnology.com/fiber-laser-cutting-machine-total-cost-of-ownership-tco-2026-.html) | 2026-08-13 | MEDIUM (6,000 W class, extrapolated hourly from stated annual figures; this case's machine is 8,000 W class, so real draw would likely run somewhat higher) |
| S6 | General hole-in-finite-plate stress-concentration design guideline — used as the closest PUBLIC analogue to re-estimate MA2's proprietary turbine-disk hole diameter | Hole-to-plate-width ratio recommended under ~0.3 for standard design practice | General mechanical/structural engineering references — [Stress Concentration Factor, Central Circular Hole in a Plate](https://amesweb.info/stress-concentration-factor-calculator/central-circular-hole-in-plate.aspx) | 2026-08-13 | LOW — a general analogue, not a turbine-disk-specific standard; see the Modeling Assumptions section's MA2 PROPRIETARY-ESTIMATED disclosure |

**2026-08-13 QA remediation note on S1.** The prior S1 citation (StyleCNC's fiber-laser buying guide, claimed "$88,000–$500,000+" for the 8,000 W class) was found during a Tier 2 data-decay check to no longer be supported by that page's live content — its current pricing table has no distinct 8,000 W tier (adjacent tiers are 6,000 W at $37,000–$80,000 and 12,000 W at $85,000–$190,000), and the only "$88,000" figure on the page today is the low end of an unrelated 20,000 W product. S1 has been replaced with the Jeesun CNC listing above, a real, current, directly-quoted price for this exact 8,000 W machine class.

No `{{NEEDS_SOURCE}}` placeholders remain open in this case. Every dollar figure and dimension not covered by a source row above is the original case's own scenario data (Stout Aviation's stated prices, sale prices, and machine specs), or a disclosed Modeling Assumption above — never an invented number.

---

## Appendix E: "How To…" Math Questions To Research

**Vocabulary terms**

- Perimeter
- Circumference
- Area
- Radius
- Diameter
- Pi
- Net
- 2-Dimensional
- 3-Dimensional
- Triangle
- Equilateral Triangle
- Square
- Rectangle
- Polygon
- Vertex
- Concave
- Irregular Polygon
- Quadrilateral
- Time
- Decimal
- Percent

**"How to…" questions**

- How to find the measure of the perimeter of a polygon
- How to find the measure of the circumference of a circle
- How to find the area of a circle
- How to find the area of a triangle
- How to find the area of a rectangle
- How to add and subtract time
- How to find elapsed time
- How to add decimal numbers
- How to subtract decimal numbers
- How to multiply decimal numbers
- How to divide decimal numbers
- How to convert numbers to percents
- How to find the percent of a number
- How to compare two or more values

<!-- FACILITATOR ONLY -->

## The Twist (facilitator delivers at ~15 minutes)

A parts-manufacturing facility in China has just burned to the ground. A Boeing representative calls: can Stout Aviation start production immediately on the component Boeing was sourcing from the destroyed facility? Boeing will pay **$114.00 per part**, plus a **$200,000 bonus** if Stout Aviation delivers **more than 5,000 units within 10 days**.

Boeing needs whichever component Drew's pitch chose. The machine can run up to 20 hours a day during the sprint (not limited to 5 days a week, given the urgency) — but every load time and cut time from Challenge 3 still applies.

Does Drew take the deal?

## Balance Argument (facilitator only — do not surface to students before discussion)

**Argument for A (turbine disks):** Turbine disks use the CNC machine's own cutting time more efficiently: minutes of laser time per square meter of *finished part* run lower for disks than for O-rings (D8), because the O-ring's design is mostly empty middle (a wide annulus, cut as two full circles) while the disk's tooth-and-hole design converts more of its own cut path directly into usable material. Disks also nest 35-to-a-sheet against the O-ring's 6-to-a-sheet (Modeling Assumption MA3) and carry no bending/shaping cost (Appendix C: "not bent... remains flat"), where O-rings absorb a $4,870 shaping cost per unit (Appendix B).

**Argument for B (inlet O-rings):** The O-ring is the higher-value, higher-prestige part — a single O-ring sells for $5,498, more than eight times a turbine disk's $657 — and it is the part visibly branded on the aircraft nacelle, which may carry relationship value with Boeing this case's numbers don't capture. An O-ring pitch is also the more defensible "diversify upward" move: Stout Aviation is already a high-volume sheet-metal shop; taking on a bent, higher-sale-price aerospace part could open doors to other bent/formed components later, where disks keep the company in flat-cut work it already does at scale. There is also one real, quantitative operating-cost angle in the O-ring's favor, beyond raw sale price: because so many fewer O-rings are produced per week (648 vs. 2,380 disks), the laser itself is actually running roughly 23.7 fewer hours per week on the O-ring line than the disk line (36.2 hr/week vs. 59.9 hr/week — straight from this case's own D3 cut times and D5 weekly volumes), despite each individual O-ring taking longer to cut. At real published 6,000 W-class fiber-laser electricity rates ([S4], $5.40–$7.50/hour), that is a genuine but modest ~$128–$178/week savings in machine electricity for the O-ring option — real, but nowhere near enough to close the profit gap below.

**On argument B's quantitative weight.** Every other packet-derivable number (D2–D8, the Twist) favors A. Argument B's one real quantitative point — the ~$128–$178/week electricity saving above — is genuine and sourced, but it is small next to the numbers argument A can cite, and the rest of argument B (prestige, relationship value, "diversify upward") is a values/strategy case, not a competing quantitative one. Facilitators should not present B as quantitatively even with A; its strength is in the trap it exploits (Anchor 1's vote), not in a close numeric contest.

**The margin:** This case's graded primary metric — minutes of laser cutting time required per square meter of finished part (D8) — is real and reasonably close: turbine disks need roughly 15.4% less cutting time per square meter of finished product than O-rings do. That is the balance-test metric of record (`case.json` `margin_pct`).

**Sensitivity of the D8 margin (re-derived 2026-08-13).** MA1's 36 in overall-height figure is the source sketch's own labeled dimension — a cited measurement, not an assumption, so it is no longer flexed by Tier 2 (P5 tests stated assumptions, not cited data; MA1's real assumption is the tooth-shape reconciliation choice, not the height value itself). MA2's hole diameter was re-estimated to 9 in (see above) from an original 10 in. The re-derived base D8 margin is 19.4% (was 15.4%). It is still not stable under a ±50% flex: −50% (4.5 in) leaves D8 stable but wide (36.4% margin); **+50% (13.5 in) still flips D8's winner to the O-ring.** This is a real, disclosed, Category-X (proprietary-estimate) instability, not an eliminated one — see `sensitivity_model.py`'s `FLEX` sweep and `FACILITATOR.md`'s facilitator note for the full numbers.

**A much larger, separately disclosed gap exists off the primary metric.** This case's real, computed *weekly gross profit* is wildly lopsided — turbine disks roughly 679% higher than O-rings per week (`$1,394,242` vs. `$178,890`, using this case's own cost model) — driven almost entirely by two disclosed given inputs (the O-ring's $4,870 bending/shaping cost, and the sell-price gap: $5,498 vs. $657), not by any adjustable modeling assumption. This gap is real and central to Challenge 3's own D5/D6/D7 deliverables — a Hero absolutely should discover it — but it is not the graded balance-test metric, following the exact precedent already established by `cardiology` (real STICH cost gap kept as disclosed context, not the graded primary metric). See `case.json` `balance{}`, `derived{}`, and `legacy_conversion_note` for the full disclosure.

**The trap:** Heroes who only compare *sale price per unit* ($5,498 vs. $657) will confidently pick O-rings — and be blindsided when the per-unit profit comparison (after the $4,870 bending cost) and the weekly-volume comparison (35 disks/sheet vs. 6 O-rings/sheet) both point the other way, hard. The real trap is stopping the math at "which part sells for more" instead of carrying it through to "which part makes more money, produced at the volume this machine can actually turn out in a week."

