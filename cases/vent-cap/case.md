Case Study: Vent Cap
MS | Math | Case Study | 2026-27 | Heroes Academy

## Overview

Mara Okafor — six months into her first job as a CNC nesting engineer, the same eye for the numbers that got her through last year's marching-band drill charts now pointed at a laser cutter instead of a football field — has forty minutes before the afternoon cutting run locks in.

Her supervisor drops a purchase order on her desk: seventy roof ventilator caps, due Friday, for a warehouse retrofit job. Two flat-pattern layouts sit open on her screen, both technically correct, both able to produce the exact same finished part. One nests fast and tight. The other cuts one weld out of every single cap.

"Whichever one goes to the laser in the next half hour is the one we're building," her supervisor says. "Tell me it's the right one."

Mara pulls up the cost sheet. Steel is steel — the price per sheet doesn't change based on which layout she picks. What changes is how many sheets seventy caps actually need, and how many seams the weld cell has to close, one at a time, seventy times over.

## Background

Mara Okafor is a CNC nesting engineer at a sheet-metal fabrication shop, responsible for laying out parts on stock sheet before they go to the laser cutter, and for flagging which layout is actually cheaper to run — not just which one looks tighter on screen.

The job: **70 pyramid-shaped roof ventilator caps**, each a square-based pyramid open at the bottom, base 12 inches on a side, with each of its four triangular faces having a slant height of 10 inches (SEE APPENDIX B). Every cap is cut from **16-gauge steel, sold in 4 ft × 8 ft (48 in × 96 in) sheets** (SEE APPENDIX C; gauge/thickness reference in APPENDIX A). Two flat-pattern layouts are on the table.

**The 4-Panel Cut** cuts each cap's four triangular faces as four separate flat panels. Separate triangles nest tightly against each other on a sheet — Mara's nesting software reports **14 caps' worth of panels per sheet** with this layout (SEE APPENDIX D). Assembly requires **four weld seams per cap**, one along each edge where two faces meet.

**The 3-Panel Fold** pre-joins one adjacent pair of triangular faces into a single folded panel before cutting, leaving two faces separate. That folded panel's outline is less efficient to nest than a lone triangle — Mara's software reports **12 caps' worth of panels per sheet** with this layout (SEE APPENDIX D). Assembly requires only **three weld seams per cap**, since one seam is already closed by the fold.

Every sheet costs the same regardless of layout (SEE APPENDIX C). Every weld seam costs the same regardless of which layout produced it — a fixed per-seam labor cost, not a per-sheet one (SEE APPENDIX E). The total job cost is sheets needed × sheet price, plus total seams × seam cost — two separate line items that move in opposite directions as the layout changes.

Before either layout was finalized, Mara's team also had to correctly identify what shape they were actually nesting the net of — get the face count or edge count wrong, and the whole flat-pattern layout is wrong before a single panel is cut.

All figures in this case are sourced in APPENDIX F, or stated as explicit modeling assumptions in APPENDIX E where no public figure exists. The vocabulary and the "how to…" skills this case will ask of you are listed in APPENDIX H — that is where Challenge 1 sends you. (SEE APPENDIX G for further reading on nesting, cutting-stock optimization, and laser cutting.)

## Dilemma

You are Mara Okafor.
Do you:
A.) Run The 4-Panel Cut — four separate triangular panels per cap, tighter nesting, four weld seams OR
B.) Run The 3-Panel Fold — one pre-joined folded panel per cap, looser nesting, three weld seams

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. Correctly name the vent cap's 3D shape, and state its number of faces and number of
    edges as actually fabricated — remember it is open at the bottom, so there is no base panel
    to cut or count — showing how you counted each.
    D2. For each layout, describe the net that gets cut from the sheet (how many pieces, what
    shape each piece is). Then verify that the weld seam connecting any two adjacent triangular
    faces is the same length on every seam in the cap — the edges have to be congruent for the
    seam to close cleanly — and show the calculation that proves it.
    D3. A material cost comparison: using each layout's caps-per-sheet figure, find how many
    sheets 70 caps actually requires under each layout, and the total material cost.
    D4. A labor cost comparison: using each layout's seams-per-cap figure, find the total number
    of weld seams for all 70 caps under each layout, and the total labor cost.
    D5. A total cost verdict: combine D3 and D4 for each layout, state the dollar difference and
    the percentage margin, and give your recommendation.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Sheet Metal Gauge Reference

| | Value |
|---|---|
| 16-gauge steel thickness | 0.0598 in (1.519 mm) [S1] |
| Standard sheet widths | 36 in or 48 in [S1] |

## Appendix B — The Vent Cap

A square-based pyramid, open at the bottom (no base panel — it sits over a roof vent opening).

| | Value |
|---|---|
| Base edge length | 12 in |
| Slant height (apothem of each triangular face, base-edge midpoint to apex) | 10 in |
| Each triangular face's area | 0.5 × 12 × 10 = 60 sq in |
| Total surface area (4 faces) | 240 sq in = 1.6667 sq ft |

This is Mara's own team's part design for this job — not a public part drawing (fabrication shop
part files are proprietary).

## Appendix C — Stock & Pricing

| | Value |
|---|---|
| Sheet size | 48 in × 96 in (4 ft × 8 ft), 16-gauge hot-rolled steel |
| Price per sheet | $68.39 [S3] |
| Order quantity | 70 caps |

## Appendix D — Nesting Layouts

| | The 4-Panel Cut | The 3-Panel Fold |
|---|---|---|
| Panels per cap | 4 separate triangles | 1 folded pair + 2 separate triangles = 3 pieces |
| Weld seams per cap | 4 | 3 |
| Caps' worth of panels per sheet | 14 | 12 |

Mara's own nesting-software output for this specific part and layout — not a public benchmark
(real nesting results depend on the exact part geometry and software used; see Appendix F for the
general industry benchmark datasets that exist for this class of problem).

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and Appendix H names the skill a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Per-seam weld labor cost | **$3.00/seam** | Derived, not quoted: a small tack/spot weld on light-gauge steel, done repeatedly on a production line (not a one-off retail service call), takes roughly 6-7 minutes including positioning, at the real average direct-labor wage for a sheet metal worker (S5, $26.28/hr) — 6.85 min × $26.28/hr ÷ 60 = $3.00. The real retail price for a one-off "simple tack weld or short seam" runs $20-$50 (S4), but that figure includes a shop's overhead, minimum-charge, and profit margin for a single customer job — not the marginal cost of the 70th identical weld on a production run. | Directly load-bearing. Flexed ±50% in Tier 2 probe 5: margin ranges 4.80%-15.39%, Option B stays cheaper throughout. |
| MA2 | Caps-per-sheet for each layout | **14 (4-Panel Cut) / 12 (3-Panel Fold)** | Mara's own nesting-software output for this specific authored part; no public database of real factory nesting results exists (SPEC/domain note). Grounded in a real, general nesting fact: two congruent triangles nest edge-to-edge with almost no gap, while a folded composite panel's less regular outline nests less efficiently — the same reason ESICUP/OR-Library nesting benchmark problems (Appendix F) exist as a hard, well-studied class of problem. | Not swept in Tier 2 probe 5 (case-authored part geometry, not a stated numeric assumption in the FLEX sense) — see RESEARCH_LOG.md for the general reasoning. |
| MA3 | Steel market volatility | Not a fixed value in this appendix — steel sheet prices have swung 30-50%+ over months in past tariff/demand cycles, real and well-documented. Appendix C's $68.39 price is a snapshot, not a guarantee. | Real, general commodity-price behavior, not derived from a specific 2026 event. | Not a factor at the price in Appendix C. Could matter if the market moves before the order ships. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | 16-gauge steel thickness and standard sheet widths | 0.0598 in; 36 in / 48 in widths | sheetmetal.me, "Sheet Metal Gauge Chart" ([link](https://sheetmetal.me/sheet-metal-gauge-chart/)) | 2026-08-12 | HIGH |
| S3 | 16-gauge, 48in × 96in hot-rolled steel sheet price | $68.39/sheet | M&K Metal Co., product listing ([link](https://www.mkmetal.net/hrsheet16gax48x96)) | 2026-08-12 | MEDIUM — the page itself labels this "sample pricing... call to confirm current pricing" |
| S4 | Retail cost of a simple tack weld or short seam | $20-$50 | tzrmetal.com, "Sheet Metal Fabrication Cost Breakdown & Tips" ([link](https://tzrmetal.com/sheet-metal-fabrication-cost/)) | 2026-08-12 | HIGH — used as context/upper-bound for MA1, not directly as the per-seam cost |
| S5 | Average hourly pay, sheet metal worker | $26.28/hr | PayScale, "Average Hourly Pay for Sheet Metal Worker," 2026 data ([link](https://www.payscale.com/research/US/Job=Sheet_Metal_Worker/Hourly_Rate)) | 2026-08-12 | HIGH |
| S6 | Real academic benchmark datasets for nesting/cutting-and-packing problems exist (context for MA2, not a specific figure) | n/a | ESICUP, "Cutting & Packing Data Sets" ([link](https://www.euro-online.org/websites/esicup/data-sets/)) | 2026-08-12 | HIGH — cited to establish that irregular nesting is a real, well-studied problem class, not to supply this case's specific part data |

## Appendix G — Learn More

Curious about the real-world math and industry behind this case? These resources go beyond what
the challenges require.

- [Nesting (manufacturing process) — Wikipedia](https://en.wikipedia.org/wiki/Nesting_(process)) — explains how real CNC shops lay out cutting patterns on flat stock to minimize wasted material, the same problem Mara's nesting software is solving.
- [Cutting stock problem — Wikipedia](https://en.wikipedia.org/wiki/Cutting_stock_problem) — the formal optimization problem (cutting standard-sized material into pieces with minimal waste) that underlies caps-per-sheet decisions like the one in this case.
- [Net (polyhedron) — Wikipedia](https://en.wikipedia.org/wiki/Net_(polyhedron)) — background on how 3-D solids unfold into flat 2-D nets, the same idea behind unfolding the vent cap's triangular faces before they're cut.
- [Laser cutting — Wikipedia](https://en.wikipedia.org/wiki/Laser_cutting) — how CNC laser cutters like the one that will cut Mara's panels actually work, including precision and material considerations for sheet metal.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Face
- Edge
- Pyramid
- Net
- 3-Dimensional
- Congruent

**"How to…" questions**

- How to draw the net of a 3-D shape
- How to name a 3-D shape
- How to divide decimal numbers
- How to find the percent of a number
- How to multiply any two numbers

<!-- FACILITATOR ONLY -->

## Balance argument

**Argument for A (The 4-Panel Cut).** Tighter nesting (14 caps/sheet vs. 12) means fewer sheets
bought — real, disclosed savings on the material line. For a shop watching sheet count, "waste
less steel" is the obvious, defensible instinct, and it's not wrong on that one line item.

**Argument for B (The 3-Panel Fold).** One fewer weld seam per cap, seventy times over, adds up:
210 fewer seams total. Labor is the line item that actually swings this job's total cost more than
material does, at a $3.00/seam production rate — a real number derived from a real wage, not
picked to force an outcome.

**Margin.** Option B beats Option A by **11.98%** on total job cost (5 sheets + 280 seams = $1,181.95
for A; 6 sheets + 210 seams = $1,040.34 for B) — inside SPEC §2's ~20% cap, and stable under a ±50%
flex of the per-seam labor rate (4.80%-15.39%, B cheaper throughout). `margin_pct`: 11.98.

**Five Socratic questions (draft).**

1. Option A wins on material (fewer sheets) and loses on labor (more seams). Which line item
   actually decides this job — and would a shop owner watching only the steel budget have gotten
   the wrong answer?
2. D2 asks you to verify every weld seam in the cap is the same length. Why does that matter to
   whoever's running the weld cell, not just to the person doing the geometry?
3. MA1's $3.00/seam is derived from a wage and a time estimate, not quoted from a price list. What
   would you want to see before you trusted it — and what happens to the verdict if a seam
   actually takes twice as long?
4. The 3-Panel Fold needs one panel with an awkward, less-efficient shape to save one weld. Is
   there a batch size small enough that this trade stops being worth it?
5. Mara has thirty minutes. What does she tell her supervisor?

**The trap.** Most Heroes will look at "14 caps/sheet vs. 12 caps/sheet," conclude the tighter
nesting must be cheaper, and stop — treating material as the whole cost story because it's the
number the nesting software puts front and center. It misses that labor, priced per seam rather
than per sheet, moves in the opposite direction and by a larger dollar amount for this specific
job size. A pitch that reports caps-per-sheet and never prices out the seams has not actually
costed the job.

**Sensitivity note (SPEC §6).** None required — the stakes here are a production deadline and a
job-costing decision, not personal loss or hardship.
