Case Study: The Setpoint Call
MS | Math | Case Study | 2026 | Adventure

## Overview

The label applicator on Line 3 hums at its usual clip, and Marisol Feng watches from the catwalk as cases stack up at the palletizer below, half her attention already on the spreadsheet glowing on her tablet. The plant just landed the biggest co-packing contract in its history — a national sports-drink brand, every bottle running through this exact line — and somebody upstairs wants a speed number by the end of her shift.

Her tablet has two tabs open. One is a quote from the guarding contractor: new interlocked panels, sensor curtains, the whole retrofit Line 3 would need to legally run faster than it does today. The other is her own derivative, half-finished, chasing the exact speed where cost per bottle bottoms out before climbing again. That speed keeps landing past the line's current rated ceiling — which means the contractor's quote isn't optional if she wants to actually reach it.

Her shift lead leans over the rail. "Corporate needs the speed setpoint locked before the contract's first production week. Not next week — this week." Marisol nods without looking up. Below her, the labeler spins bottle after bottle past its glue wheel, steady, ordinary, waiting on a number she hasn't found the courage to write down yet.

## Background

Marisol Feng is the process engineer responsible for Line 3 at Bellcross Bottling, a contract manufacturer that fills and labels beverages under other companies' brands. Bellcross has just signed a multi-month exclusive co-packing agreement with a national sports-drink brand, and every bottle in that agreement will run on Line 3's rotary labeler. Marisol is accountable for setting the line's operating speed for the life of the contract — a single number that determines the plant's cost per bottle for months to come (SEE APPENDIX A).

Line 3's labeler currently runs no faster than its manufacturer-rated, ANSI/PMMI-compliant maximum safe speed — the ceiling set by the machine's existing guarding and interlock configuration (SEE APPENDIX B). Running faster than that ceiling without matching guarding upgrades is not just inadvisable, it is a documented machine-safety-standard violation. Marisol and her shift lead have started calling the choice by its two paths. **The Guarding Upgrade** means paying a contractor now to install the additional interlocked guarding the safety standard requires to legally clear Line 3 for a higher operating speed — the speed Marisol's own cost model says minimizes cost per bottle — before the new contract's first production week begins (SEE APPENDIX C). **The Rated Cap** means leaving Line 3's guarding as it is and running the entire contract at the labeler's current rated ceiling — no retrofit, no capital outlay, but also no access to the lower cost per bottle the math says is possible above that ceiling (SEE APPENDIX B, APPENDIX C).

A faster line does not automatically mean a cheaper bottle, however: Line 3's cost per bottle depends on both how fast it runs and how much retrofit capital that speed required, spread across every bottle the new contract will actually produce (SEE APPENDIX C). The guarding contractor has exactly one install slot before the contract's first production week — after that, the next available slot is too late to matter for this decision. The vocabulary and "how to…" procedures this case will ask you to research are listed in (SEE APPENDIX E); every priced or sourced figure is documented in (SEE APPENDIX D).

## Dilemma

You are Marisol Feng.
Do you:
A.) Fund The Guarding Upgrade — retrofit Line 3's guarding now to legally clear it for the calculus-derived cost-minimizing speed OR
B.) Hold The Rated Cap — keep Line 3 at its current rated maximum safe speed for the life of the contract, with no capital outlay

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A total-cost-per-bottle function TC(r), where r is Line 3's operating speed in bottles
    per minute: using Appendix A's cost-rate-per-minute function CR(r) and time-per-bottle
    function MPU(r), combine them as TC(r) = CR(r) × MPU(r) — showing how you built each factor
    before multiplying.
    D2. Using the product rule (and the power rule where a factor contains a 1/r term),
    differentiate TC(r) with respect to r, set TC'(r) = 0, and solve algebraically for the speed
    r* that minimizes cost per bottle — showing every step of the product-rule algebra, including
    which terms cancel.
    D3. Using both the first derivative test and a concavity (second-derivative) check, confirm
    that r* is a genuine local minimum and not a local maximum. In your own words, explain what
    a local maximum would look like on this same cost curve, and state whether TC(r) actually has
    one for r > 0.
    D4. A check of r* against Appendix B's rated safe-speed ceiling: state whether the
    unconstrained calculus optimum is legally reachable under Line 3's current guarding, then
    evaluate TC(r) at both r* and the rated ceiling — showing every calculation.
    D5. A total-cost-per-bottle comparison over the life of the new contract for both real paths:
    for The Guarding Upgrade, combine TC(r*) with Appendix C's retrofit cost spread evenly across
    Appendix C's contract volume; for The Rated Cap, use TC at the rated ceiling with no retrofit
    cost added. State which path has the lower true cost per bottle and by how much, in dollars
    and as a percent.
    D6. An original visual display (a graph of TC(r), built in Desmos or by hand, or an
    equivalent chart) showing cost per bottle versus line speed, with r* and the rated ceiling
    both labeled.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Line 3's Cost Structure

The two factors that combine into Line 3's total cost per bottle, TC(r), where r is the line's
operating speed in bottles per minute. Referenced from Background and Dilemma; forces Challenge 3
(D1, D2, D3).

| | Value |
|---|---|
| Base cost rate to operate Line 3, independent of speed — attendant labor (fully burdened) plus baseline utilities/compressed air draw ($ per minute) — the constant *a* in CR(r) = a + b·r | $0.90/min (labor+burden $0.45/min from [S1]+[S2]/MA2; baseline utility draw $0.45/min, MA1) |
| Incremental cost rate per unit of speed increase — additional power draw, mechanical wear, and defect/rework cost per added bottle-per-minute of speed ($ per (bottle/min), the coefficient *b* in CR(r) = a + b·r) | $0.0004/(bottle/min) (MA3, informed by [S3]'s industrial electricity price) |
| Fixed downstream handling time per bottle — final case-packing/palletizing time that does not depend on labeler speed (minutes per bottle, the constant *d* in MPU(r) = 1/r + d) | 0.02 min/bottle (MA4) |

## Appendix B — Line 3's Rated Speed and the Safety Standard

The speed ceiling Line 3 cannot legally exceed without additional guarding, and the standard that
sets it. Referenced from Background and Dilemma; forces Challenge 3 (D3, D4, D6).

| | Value |
|---|---|
| Line 3's current manufacturer-rated maximum safe operating speed, at its existing guarding/interlock configuration (bottles per minute) | 150 bottles/min (MA5, within the 100–500 bpm industry range for rotary labelers [S4]) |
| The machine-guarding safety standard requiring a risk assessment (and, where warranted, added guarding/interlocking) whenever a packaging machine's operating parameters — including speed — change | ANSI/PMMI B155.1, *Safety Requirements for Packaging Machinery and Packaging-Related Converting Machinery* [S6] |

## Appendix C — The Two Paths' Costs and the Contract

The capital cost of each real path and the volume it must be justified against. Referenced from
Background and Dilemma; forces Challenge 3 (D5).

| | Value |
|---|---|
| Guarding/interlock retrofit cost to legally clear Line 3 for a higher operating speed (USD, one-time) | $44,000 (MA6, extending the per-door interlock cost range in [S5] to a full-line retrofit: turret access panels, infeed/outfeed conveyor guarding, and an updated safety PLC) |
| Total bottle volume the new co-packing contract will run on Line 3 over its life (bottles) | 10,000,000 bottles (MA7) |
| Guarding contractor's install lead time relative to the contract's first production week | One install slot, six weeks out (MA8 — matches Background's own stated urgency, not an independent estimate) |

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author/researcher, because a genuine multi-tier search found no public source publishing them
> for a specific bottling line or a one-off safety retrofit. A Hero may challenge them in
> discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Baseline utility/compressed-air draw component of the base cost rate *a* | $0.45/min | No public source publishes a per-minute utility draw for a specific rotary labeler; set at rough parity with the sourced labor+burden component so neither dominates the base rate arbitrarily. | Shifts *a* directly, which moves r* and the theoretical minimum, but does not independently flip which real option wins (see case.json.sensitivity_disclosure). |
| MA2 | Labor burden multiplier applied to [S1]'s $20.78/hr median wage | 1.3× (within the documented 1.25×–1.4× range [S2]) | [S2] documents a manufacturing labor burden of roughly 1.25×–1.4× base wage (payroll taxes, benefits, workers' comp); 1.3× is the range's lower-middle value. | Shifts the sourced-labor component of *a*; not independently flexed (bundled into *a*, which sensitivity_model.py treats as a derived/cited quantity, not a stated scenario assumption). |
| MA3 | Incremental cost rate, *b*, in CR(r) = a + b·r | $0.0004/(bottle/min) | No public source models a per-speed-unit cost coefficient for a rotary labeler. The value is a smooth approximation of a real, documented mechanism — higher machine speed increases motor power draw (informed by [S3]'s industrial electricity price) and increases defect/rework/jam rate (a well-documented packaging-line phenomenon) — applied as a stated scenario simplification. | This is the assumption the case's cost curve is most sensitive to: it sets both the location of r* and how steeply cost rises past it. See case.json.sensitivity_disclosure for the ±50% flex result. |
| MA4 | Fixed downstream handling time per bottle, *d*, in MPU(r) = 1/r + d | 0.02 min/bottle | No public source publishes a per-bottle downstream case-packing/palletizing time for a specific line; 0.02 min/bottle (a 50 bottle/min-equivalent downstream station) is a representative order of magnitude for that process step. | Sets the scale at which cost per bottle is minimized (r* = √(a/(b·d))) together with MA3. |
| MA5 | Line 3's current rated maximum safe operating speed | 150 bottles/min | Protagonist-specific: Line 3 is an older, conservatively-guarded machine within the industry's documented 100–500 bpm range [S4], not a new high-speed installation. | Directly sets how far below r* the current legal ceiling sits — the gap this whole case is about. |
| MA6 | Guarding/interlock retrofit cost | $44,000 | No public source prices a full-line retrofit; [S5] prices a single interlocked door at $1,500–$5,000. This case's retrofit covers multiple hazard zones (turret access panels, infeed/outfeed conveyor guarding, an updated safety PLC), not one door — $44,000 extends that per-door range to a comprehensive, multi-zone scope. | The single most load-bearing protagonist-specific number in the case: it is what The Guarding Upgrade must recover across Appendix C's contract volume. |
| MA7 | Total contract volume on Line 3 | 10,000,000 bottles | Protagonist-specific: a multi-month exclusive co-packing commitment at realistic line utilization (well under running 24/7 at r*'s ~335 bpm for the full period). | Sets how thinly the retrofit's fixed cost is spread — this case's load-bearing, dilemma-flipping dial (see case.json.sensitivity_disclosure). |
| MA8 | Guarding contractor's install lead time | One slot, six weeks out | Matches the Background's own stated urgency verbatim — not an independent estimate. | None — fixed by the narrative, not a sensitivity lever. |

## Appendix D — Sources

All sourced (non-assumption) figures in this case are cited here (SEE APPENDIX D).

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Median wage, Packaging and Filling Machine Operators and Tenders | $20.78/hour ($43,220/year) | O\*NET OnLine (attributing U.S. Bureau of Labor Statistics 2025 wage data) — [Summary Report for 51-9111.00](https://www.onetonline.org/link/summary/51-9111.00) | 2025 | MEDIUM |
| S2 | Manufacturing labor burden rate (payroll taxes, benefits, workers' comp as a multiplier on base wage) | 1.25×–1.4× base wage | Rippling — [How To Calculate Labor Burden: Complete 2025 Guide](https://www.rippling.com/blog/labor-burden) | 2025 | MEDIUM |
| S3 | Average U.S. industrial-sector retail electricity price | 9.17 cents/kWh | U.S. Energy Information Administration — [Electricity Monthly Update](https://www.eia.gov/electricity/monthly/update/end-use.php) | June 2026 | HIGH |
| S4 | Rotary bottle/container labeling machine speed range, industry-wide | 100–500 bottles per minute | Quadrel — [Rotary Labeling Machines](https://www.quadrel.com/rotary-labeling-machines/) | accessed 2026-09-09 | MEDIUM |
| S5 | Safety-rated interlock door retrofit cost (switch, controller, wiring), per door | $1,500–$5,000 | The Safety Geek — [Interlocked vs Fixed Guards](https://thesafetygeek.com/interlocked-guards-vs-fixed-guards/) | accessed 2026-09-09 | LOW |
| S6 | ANSI/PMMI B155.1 — scope for packaging machinery safety (new/modified/rebuilt machinery performing packaging functions), current edition released July 2023 | Standard exists; current edition ANSI/PMMI B155.1-2023 | PMMI — [Standards, Technical Reports, Regulations and Directives](https://www.pmmi.org/standards-and-regulations) (corroborated by The ANSI Blog — [ANSI/PMMI B155.1-2023: Packaging Machinery Safety Requirements](https://blog.ansi.org/ansi/ansi-pmmi-b155-1-2023-packaging-machinery-safety/)) | 2023 (current edition) | MEDIUM |

Notes:
- **S1 note:** O\*NET OnLine republishes BLS wage data with attribution; the primary BLS OEWS table for this occupation (bls.gov/oes) could not be fetched directly during this research pass (index page only, no occupation-level figures without downloading a data file) — O\*NET's summary is used as the best available accessible republication. Graded MEDIUM for that reason.
- **S2 note:** a general manufacturing-industry HR/accounting benchmark, not specific to beverage co-packing or this occupation; corroborated in direction (not exact multiplier) by several other industry sources found in the same search pass.
- **S4 note:** a general manufacturer capability statement across many labeler models, not a single machine's spec sheet; actual rated speed depends on bottle size, label length, and guarding configuration — used here to bound MA5's protagonist-specific value to a realistic industry range, not as Line 3's own rated speed.
- **S5 note:** a safety-equipment blog/consultant page, not a manufacturer price list or a standards body — graded LOW and used only as a basis for MA6's stated assumption, never as the retrofit's own literal cost.
- **S6 note:** confirms the standard's real existence, current edition, and general risk-assessment methodology (including re-assessment on a change to machine operating parameters); the exact clause language tying guarding level to a specific numeric speed threshold sits behind ANSI's paywall and is not claimed here — the case treats "how much added guarding a speed increase requires" as MA6's assumption, grounded in the standard's real, public risk-assessment principle rather than a quoted clause.

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Derivative
- Critical Point
- Concavity

**"How to…" questions**

- How to find a derivative using the power rule
- How to use the product rule to differentiate a product of functions
- How to find critical points of a function
- How to use the first derivative test to classify a critical point
- How to solve an optimization problem using derivatives
- How to find the percent of a number

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
