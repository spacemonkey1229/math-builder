# Case Study: The Plaza Bid

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Marcus Ibe has two tile samples lined up on his desk under the office's harsh fluorescent light, and a bid due before the city procurement office closes for the day.

He's a junior estimator at Solvane Tile & Stone, six months into the job, and this is the first plaza contract his boss has trusted him to price on his own. The city wants real cut tile for its new downtown plaza — not stamped concrete — and the request for proposal that arrived last week names the client committee's preferred pattern in bold: an octagon-and-square combination, the kind you see in old train-station floors. Marcus's boss wants the regular hexagon instead — one repeating shape, cleaner geometry, nothing for the client's committee to argue with at the vertices.

Marcus has spent the morning on the phone with a tile supplier's rep and an hour with a tape measure and a legal pad, and now he has two spreadsheets open side by side. One says the octagon-and-square job is the safer bid. The other says it isn't. They can't both be right, and the number he types into the cell marked "$ / sq ft, installed" is the number that either wins his firm the contract or costs it money for the next six months.

His boss is standing in the doorway, coat already on, waiting for an answer before she leaves for the client meeting.

Marcus picks up his pen.

---

## Background

Marcus Ibe is a junior estimator at Solvane Tile & Stone, a small architectural tile-design firm that bids fixed-price installation contracts for public and commercial projects. Solvane is bidding on the tile-installation contract for the City of Ashford's new downtown plaza — a rectangular public gathering space the city's request for proposal specifies at 45 feet by 30 feet, 1,350 square feet total (SEE APPENDIX A). The winning bid is a single fixed price per square foot, installed, materials and labor both included; if Solvane's actual costs run over that number, the firm eats the difference, and if Marcus bids too high to protect against that risk, the contract goes to a competitor.

Ashford's design committee has stated a preference for an octagon-and-square combination pattern: two octagon tiles and one square tile meeting at every interior vertex, a classic look. Marcus's supervisor has pushed back in favor of a regular hexagon pattern instead, arguing that a single repeating shape is simpler to install and easier to defend if the committee raises questions later. Neither option is off the table — the RFP allows either pattern, as long as the bid states which one Solvane is pricing and can defend the number (SEE APPENDIX C and APPENDIX D for each pattern's underlying geometry and the specific manufactured tile line Marcus is pricing from a live supplier catalog).

Both patterns require cutting tile along every edge of the plaza's rectangular boundary, because neither tile line's manufactured sheet size divides the plaza's stated dimensions evenly (SEE APPENDIX E) — cut-off tile is material Solvane still has to pay for. Standard installation practice also adds a baseline waste allowance for ordinary breakage and field cuts, on top of whatever the sheet geometry itself wastes (SEE APPENDIX E). Installed cost also includes labor, priced per square foot of finished plaza — and mosaic-scale tile is documented to take longer to install than larger-format tile, a real cost that never shows up on the supplier's price list at all (SEE APPENDIX F).

The bid is due at Ashford's procurement office by the end of this week (SEE APPENDIX A). Before pricing either option, Solvane also wants to know the largest square staging block that divides the plaza's dimensions evenly, so identical panels can be pre-assembled off-site rather than built tile-by-tile on location (SEE APPENDIX B). Full source citations for every figure in this case are in Appendix G, and the full standards bridge for this case is in Appendix H.

*Note: Solvane Tile & Stone and the City of Ashford are scenario constructions for this case — neither is a real company or municipality.*

---

## Dilemma

You are Marcus Ibe.

Do you:

**A.)** Bid the plaza tiled in **the regular hexagon pattern** — a single repeating shape that tessellates the plane with zero gaps **OR**

**B.)** Bid the plaza tiled in **the client's preferred octagon-and-square combination pattern** — two shapes meeting at every vertex, priced from a different manufactured tile line

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — An interior-angle-sum tessellation proof for both patterns.** Using the sum of the interior angles of a polygon theorem, compute the interior angle of a regular hexagon and show that three hexagons meeting at a vertex sum to exactly 360°. Then compute the interior angle of a regular octagon and show that three octagons alone do *not* sum to 360° at a vertex — and show that two octagons plus one square *does*. State in your own words why this proves the client's pattern needs two shapes to close a vertex and Marcus's boss's pattern needs only one.
- **D2 — A staging-block computation using the greatest common factor.** Using the plaza's stated length and width (Appendix A), find the greatest common factor of the two dimensions and use it to determine the largest square staging block that divides the plaza evenly with no leftover partial block, and how many such blocks the plaza requires in each direction.
- **D3 — A cut-waste computation for both tiling options.** Using each option's real manufactured sheet size (Appendices C and D) against the plaza's dimensions, compute how many sheets must be purchased for each option (rounding up every partial row and column), add the standard installation waste allowance (Appendix E), and express each option's total waste as a percentage of the tile actually purchased.
- **D4 — A total installed cost table.** For each option, compute material cost (sheets purchased × price per square foot) and labor cost (plaza square footage × labor rate, including any pattern-specific labor premium), then compute each option's total installed cost per square foot of the plaza (Appendices E and F).
- **D5 — A recommendation memo.** State which pattern Marcus should bid, defended with D1's geometry, D3's waste percentages, and D4's total installed cost per square foot — including how close the two options actually come, and whether that margin is comfortable enough for Solvane to bid it with confidence given what is riding on getting the number right.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Ashford Plaza — Bid Constraints

| Quantity | Value |
|---|---|
| Plaza dimensions (length × width) | 45 ft × 30 ft [MA1] |
| Plaza area | 1,350 sq ft (45 × 30) [derived from MA1] |
| Days from case launch to bid submission deadline | 4 days [MA2] |
| Bid form | A single fixed price, dollars per square foot, materials and labor included | 
| Bidder's risk | Solvane absorbs any cost overrun above the bid; a bid priced too high risks losing the contract to a competitor |

*Note: Ashford's plaza dimensions are a stated scenario Modeling Assumption for this case, not a real public plaza's recorded blueprint.*

---

## Appendix B: Staging-Block Planning (Greatest Common Factor)

| Quantity | Value |
|---|---|
| Plaza length | 45 ft [MA1] |
| Plaza width | 30 ft [MA1] |
| Greatest common factor of 45 and 30 | 15 (45 = 3² × 5; 30 = 2 × 3 × 5; GCF = 3 × 5 = 15) [computed] |
| Largest square staging block that divides both dimensions evenly | 15 ft × 15 ft |
| Blocks needed along the 45 ft length | 3 (45 ÷ 15) [computed] |
| Blocks needed along the 30 ft width | 2 (30 ÷ 15) [computed] |
| Total staging blocks | 6 (3 × 2) [computed] |

*This computation is independent of which tiling pattern is chosen — it only uses the plaza's stated dimensions (Appendix A) — and applies to either option's staging plan.*

---

## Appendix C: Option A — The Regular Hexagon Pattern

| Quantity | Value |
|---|---|
| Number of sides | 6 |
| Interior angle of a regular hexagon | 120° — (6 − 2) × 180° ÷ 6 = 720° ÷ 6 = 120° [computed] |
| Number of hexagons meeting at each interior vertex in a full tessellation | 3 [computed] |
| Sum of interior angles at each vertex | 360° (120° × 3) — confirms zero-gap tessellation [computed] |
| Product line being priced | Daltile Color Wheel Mosaic, Arctic White, 1.5″ hexagon, ceramic mosaic sheet [S1] |
| Price per square foot (as listed) | $6.59 / sq ft (current listed price; regular list price shown as $9.39 / sq ft) [S1] |
| Manufactured sheet "actual size" | 11 ⅝ in × 10 ¼ in [S1] |
| Manufacturer-stated coverage per sheet | 0.81 sq ft / sheet [S1] |

---

## Appendix D: Option B — The Octagon-and-Square Combination Pattern

| Quantity | Value |
|---|---|
| Number of sides (octagon) | 8 |
| Interior angle of a regular octagon | 135° — (8 − 2) × 180° ÷ 8 = 1,080° ÷ 8 = 135° [computed] |
| Sum of three octagons' interior angles at one vertex | 405° (135° × 3) — exceeds 360°, so three octagons alone cannot meet at a single vertex without overlapping [computed] |
| Vertex configuration actually used | Two octagons + one square: 135° + 135° + 90° = 360° — confirms the combination tessellates with zero gaps [computed] |
| Product line being priced | Daltile Octagon & Dot 6501, Matte White with Gray Gloss Dots, ceramic mosaic sheet [S2] |
| Price per square foot (as listed) | $9.69 / sq ft [S2] |
| Manufactured sheet "actual size" | 12 in × 12 in (exactly 1 sq ft) [S2] |
| Manufacturer-stated coverage per sheet | 1.00 sq ft / sheet [S2] |

---

## Appendix E: Cut-Waste and Material Purchase Computation

Sheet footprint (bounding rectangle) is used to determine how many whole-sheet positions are needed to span the plaza in each direction, rounding up every partial row and column (real cut tile is still purchased, even for a partial row) [methodology — see Modeling Assumptions, MA5].

| Quantity | Option A (Hexagon) | Option B (Octagon + Square) |
|---|---|---|
| Sheet footprint (bounding rectangle) | 11 ⅝ in × 10 ¼ in = 0.96875 ft × 0.854167 ft [S1] | 12 in × 12 in = 1 ft × 1 ft [S2] |
| Sheet positions across plaza length (45 ft), rounded up | 47 (45 ÷ 0.96875 = 46.45, round up) [computed] | 45 (45 ÷ 1 = 45, exact) [computed] |
| Sheet positions across plaza width (30 ft), rounded up | 36 (30 ÷ 0.854167 = 35.12, round up) [computed] | 30 (30 ÷ 1 = 30, exact) [computed] |
| Total sheet positions (grid) | 1,692 (47 × 36) [computed] | 1,350 (45 × 30) [computed] |
| Standard installation waste allowance (breakage, field cuts) | 10% [S3] | 10% [S3] |
| Sheets to purchase (grid positions × 1.10, rounded up) | 1,862 (1,692 × 1.10 = 1,861.2, round up) [computed] | 1,485 (1,350 × 1.10 = 1,485, exact) [computed] |
| Purchased coverage (sheets purchased × manufacturer coverage per sheet) | 1,508.22 sq ft (1,862 × 0.81) [computed] | 1,485 sq ft (1,485 × 1.00) [computed] |
| Waste % (purchased coverage vs. plaza's 1,350 sq ft net area) | 10.5% — (1,508.22 − 1,350) ÷ 1,508.22 [computed] | 9.1% — (1,485 − 1,350) ÷ 1,485 [computed] |
| Material cost (purchased coverage × price per sq ft) | $9,939.17 (1,508.22 × $6.59) [computed] | $14,389.65 (1,485 × $9.69) [computed] |

---

## Appendix F: Installed Labor Cost Data

| Quantity | Value |
|---|---|
| Published range, U.S. tile-installation labor cost | $3 – $15 / sq ft [S4] |
| Base labor rate used in this case | $9.00 / sq ft — midpoint of the published range [MA3] |
| Documented direction: small-format / mosaic tile takes longer to install than larger-format tile | Confirmed, no single published percentage found [S4], [S5], [S6] |
| Labor premium applied to Option A (hexagon mosaic — more grout lines, more precision cutting per sheet) | +15% [MA4] |
| Labor rate, Option A (Hexagon) | $10.35 / sq ft ($9.00 × 1.15) [computed] |
| Labor rate, Option B (Octagon + Square — clean square-grid sheet repeat, no premium applied) | $9.00 / sq ft [computed] |
| Labor cost, Option A (rate × 1,350 sq ft plaza) | $13,972.50 [computed] |
| Labor cost, Option B (rate × 1,350 sq ft plaza) | $12,150.00 [computed] |
| **Total installed cost, Option A** (material + labor, Appendix E + this appendix) | **$23,911.67** ($9,939.17 + $13,972.50) [computed] |
| **Total installed cost, Option B** (material + labor, Appendix E + this appendix) | **$26,539.65** ($14,389.65 + $12,150.00) [computed] |
| **Total installed cost per square foot, Option A** | **$17.71 / sq ft** ($23,911.67 ÷ 1,350) [computed] |
| **Total installed cost per square foot, Option B** | **$19.66 / sq ft** ($26,539.65 ÷ 1,350) [computed] |

---

## Modeling Assumptions

> These figures are stated scenario assumptions chosen by the case author, or values derived by
> anchoring inside a real, cited published range. A Hero may challenge any of them in discussion —
> that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Plaza dimensions | 45 ft × 30 ft (1,350 sq ft) | Stated scenario dimensions — Ashford's plaza is fictional, so no real blueprint exists to cite. Chosen to have a clean, computable GCF (15) for Appendix B. | HIGH — every downstream computation (Appendices B, E, F) depends on these exact dimensions. Different dimensions would change the grid-rounding waste for Option A materially (since its sheet footprint does not divide evenly into most whole-foot dimensions) while leaving Option B's grid-rounding waste at 0% for any whole-foot dimensions. |
| MA2 | Days from case launch to bid deadline | 4 days | Narrative flavor, matching the Overview's same-week urgency. | None — flavor only, not load-bearing. |
| MA3 | Base labor rate | $9.00 / sq ft | Midpoint of the real published $3–$15/sq ft range (S4). No more specific published rate exists for this scenario's fictional job. | MEDIUM — raising or lowering the base rate scales both options' labor cost proportionally, but Option A's labor is always 15% higher than Option B's at any base rate, so the *qualitative* labor gap does not depend on this choice; the *margin_pct* does shift somewhat (see sensitivity_model.py). |
| MA4 | Labor premium for Option A (hexagon mosaic installation) | +15% | No single published percentage exists for a hexagon-vs-square-grid mosaic labor premium; general contractor guidance (S4, S5, S6) confirms mosaic/small-format tile takes measurably longer to install than larger-format tile, but only qualitatively. 15% is a round, moderate value chosen inside the general "pattern work adds extra labor time" range those sources describe. | HIGH — this is the single most decision-relevant modeling choice in the case. At 0% premium, Option A's total cost drops to $22,089.17 ($16.36/sq ft), widening its win margin to 16.8%. Between a 36% and 38% premium, Option A's total cost rises past Option B's, which *flips* the winner. See sensitivity_model.py — the winner flips near a 37% premium, more than double the 15% value used. |
| MA5 | Cut-waste computed via each sheet's bounding-rectangle grid fit, rather than modeling the true offset/staggered hexagon-row pattern within a sheet | Grid-rounding method (Appendix E) | A full staggered-hex-offset cutting model is beyond MS-level geometry; the bounding-rectangle grid method is the same simplification real estimators use for a first-pass material takeoff before a detailed cut list. | MEDIUM — a more precise staggered-offset model would likely lower Option A's computed waste slightly (since a honeycomb offset can nest partial hexagons more efficiently along one edge than a plain rectangular grid assumes), which would *strengthen* Option A's case, not weaken it — so this simplification is conservative in the direction of understating, not overstating, Option A's advantage. |

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Hexagon mosaic tile: price per square foot and manufactured sheet size | $6.59/sq ft (listed; regular list $9.39/sq ft); sheet 11⅝″×10¼″; coverage 0.81 sq ft/sheet | Stone & Tile Shoppe, Inc. — [Daltile Color Wheel Mosaic 0190/0790, Arctic White, 1½″ Hexagon Ceramic Mosaic](https://stoneandtileshoppe.com/products/color-wheel-mosaic-0190-0790-arctic-white-1_1_2-hexagon-ceramic-mosaic) | Accessed 2026-09-01 | HIGH |
| S2 | Octagon-and-dot mosaic tile: price per square foot and manufactured sheet size | $9.69/sq ft; sheet 12″×12″ (1 sq ft exactly); coverage 1.00 sq ft/sheet | Stone & Tile Shoppe, Inc. — [Daltile Octagon & Dot 6501, Matte White with Gray Gloss Dots, 2″ Octagon Ceramic Mosaic](https://stoneandtileshoppe.com/collections/octagon-mosaics/products/octagon-dot-6501-matte-white-with-gray-gloss-dots-2-octagon-ceramic-mosaic) | Accessed 2026-09-01 | HIGH |
| S3 | Standard tile installation waste allowance for a straight layout in a simple rectangular room | ~10% | MakeCalcs — [Tile Waste Factor by Laying Pattern](https://makecalcs.net/blog/tile-waste-factor-guide) | Accessed 2026-09-01 | MEDIUM — an independent installation-calculator/blog source, not a manufacturer or trade-association standard, but a specific, quantified figure. |
| S4 | Published U.S. tile-installation labor cost range, and qualitative confirmation that intricate/small tile costs more labor | $3–$15/sq ft; "small, intricate tiles are more time-consuming and costly to install" | Angi — [How Much Does Tile Installation Cost? (2026 Data)](https://www.angi.com/articles/tile-installation-cost.htm) | Accessed 2026-09-01 | HIGH |
| S5 | Qualitative confirmation, intricate/mosaic tile costs more labor | "Tiny, intricate designs...typically cost more to install because they're more difficult and time-consuming"; overall labor range $8–$20/sq ft | HomeGuide — [How Much Does Tile Installation Cost? (2026 Guide)](https://homeguide.com/costs/tile-installation-cost) | Accessed 2026-09-01 | MEDIUM |
| S6 | Qualitative confirmation, mosaic tile costs more labor | "Small tile / mosaics: slower layout + more grout + more cleanup"; standard tile range $4–$25/sq ft | EstimationPro — [Labor Price for Tile Installation: 2026 Cost Guide](https://estimationpro.ai/tools/blog/labor-price-for-tile-installation) | Accessed 2026-09-01 | MEDIUM |

*No number in this case's geometry (interior angles, tessellation vertex sums, greatest common factor) requires a citation — those are computed directly from the polygons' own definitions and the plaza's stated dimensions.*

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Hexagon
- Octagon
- Regular Polygon
- Sum of the interior angles of a polygon theorem
- Greatest Common Factor
- Percent

**"How to…" questions**

- How to find the measure of an interior angle of a polygon given the other angles
- How to find the greatest common factor of a set of numbers
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
