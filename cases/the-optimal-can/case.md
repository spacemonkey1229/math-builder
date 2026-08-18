Case Study: The Optimal Can
MS | Math | Case Study | 2026 | Launchpad

## Overview

The forming press on Line 3 punches out another shell, and Priya Anand watches it ride the star
wheel toward the necker with the same rhythm it has held all shift. On her second monitor, a
spreadsheet is open to a single cell she has rebuilt four times since lunch. Somewhere down the
line a shell drops and rattles across the guarding before an operator scoops it up without looking.
The can no one dropped costs money whether it falls or not, and that is the whole problem on her
screen.

Thursday's capital review has one slot left, and her supervisor already told her it is hers if she
wants it. The pitch is simple to say out loud: change the shape of the can, use less aluminum for
the same twelve ounces, save money on every can Ridgeline stamps from now on. It is much less
simple to defend in a room that will ask her, in front of the plant manager, exactly how many
months it takes to get the retooling money back — and whether that number is one she is willing to
put her name on.

Her coffee has gone cold next to the keyboard. The math itself she trusts. What she does not yet
know, with the die order due to the toolroom by Friday if this is going anywhere, is whether the
number on this line beats the number finance is going to hold her to.

She pulls up two folders side by side: the shape Ridgeline runs today, and the shape calculus says
is the true minimum. Somewhere between them is Thursday's answer.

## Background

Priya Anand is a packaging and process engineer at Ridgeline Canning, a contract beverage canner
that fills and cans carbonated and still beverages under co-packing agreements for a roster of
regional brands. She owns the material-cost line item for the aluminum can body on Ridgeline's
lines, and any change to that line item — including a request for retooling capital — is hers to
propose and defend.

Every can Ridgeline stamps on this line must hold the same fill volume it holds today: this is the
brand client's own bottling specification, fixed by contract, and it is not a variable either
option below is allowed to change (SEE APPENDIX A). What can change is the can body's proportions —
its radius and height — as long as the enclosed volume stays exactly the same.

Two options are in front of her.

**Hold The Line** keeps the can body at the industry-standard proportions Ridgeline's forming and
necking tooling already cuts. Nothing on the floor changes. The retooling cost is zero (SEE
APPENDIX A).

**The Slim Retool** re-cuts the forming dies to the proportions that a calculus optimization
identifies as the minimum-surface-area shape for a cylinder holding the same fixed volume — using
less aluminum sheet for every can, at the cost of a one-time die-and-tooling changeover on Line 3
(SEE APPENDICES A, B AND C).

Both options are modeled as a plain right circular cylinder — a flat top, a flat bottom, and a
straight sidewall — because that is the shape the classic surface-area-minimization problem solves
for, and because the two designs differ from each other only in radius and height, not in the
material they are cut from or the process that forms them (SEE APPENDIX A). Aluminum for the can
body is priced the same for either shape (SEE APPENDIX B), and Ridgeline's plant leadership will
not fund the retool unless the material savings pay back the die-and-tooling cost within the
capital-approval window finance holds every line-level retooling request to (SEE APPENDIX C). Where
a figure in this case is not a matter of public record, it is stated as an explicit modeling
assumption (SEE APPENDIX D) rather than guessed, and every sourced figure is listed in
(SEE APPENDIX E). The vocabulary and the "how to…" skills this case will ask of you are listed in
**APPENDIX G** — that is where Challenge 1 sends you. Real photos and further reading on can
manufacturing and aluminum pricing, beyond what the challenges require, are gathered in
**APPENDIX F**.

## Dilemma

You are Priya Anand.
Do you:
A.) Recommend Hold The Line — keep the industry-standard can body, zero retooling cost OR
B.) Recommend The Slim Retool — re-cut the dies to the calculus-optimal proportions

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. The surface-area function for a closed cylinder of fixed volume, written symbolically as a
    function of radius alone, S(r), with the fixed-volume substitution shown — and its derivative
    dS/dr, found using the power rule and reported as the instantaneous rate of change of surface
    area with respect to radius.
    D2. The critical-point work: dS/dr set equal to zero and solved for the critical radius r*,
    followed by the first derivative test (or an equivalent concavity check) proving r* is a local
    minimum of S(r) and not a local maximum — with the resulting height h* computed from r* and the
    fixed volume.
    D3. A material-cost comparison table: total surface area, aluminum weight, and material cost
    per can for Hold The Line's body versus The Slim Retool's body (SEE APPENDICES A AND B), with
    the percent reduction in surface area and in cost shown.
    D4. An annual-savings and payback calculation at Ridgeline's stated annual can volume for this
    line (SEE APPENDIX C): net annual material savings, the retooling cost's payback period in
    months, and a break-even calculation — the minimum annual can volume at which The Slim Retool
    pays back within plant leadership's stated capital-approval window.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Two Can Geometries

Both options hold the same fixed fill volume, set by the beverage brand's own bottling
specification and never itself a variable in this case:

| | Value |
|---|---|
| Fixed fill volume per can | 12 US fluid ounces = 21.65625 in³ exactly, by the legal US fluid-ounce/cubic-inch definition (1 US gallon = 231 in³ exactly, 128 fl oz per gallon) — a definitional conversion, not a figure requiring a market or industry source |

**Hold The Line — the industry-standard body.** Ridgeline's existing forming and necking tooling
cuts the body to the Can Manufacturers Institute's published standard body outside diameter for a
12 fl oz can (SEE APPENDIX E):

| | Value |
|---|---|
| Standard body outside diameter | **2.602 in** (nominal 2.600 in) [S1] |
| Standard body radius | **1.301 in** — one-half the diameter above |
| Cylinder height at the fixed fill volume, this radius | derived: h = V / (π r²) = 21.65625 / (π × 1.301²) = **4.0727 in** — shown as the student's own work in D1, not sourced |
| Total surface area at these dimensions | derived: S = 2πr² + 2πrh = **43.9266 in²** — the student's own work in D1 |
| Published overall (flanged) can height, for reference only | **4.812 in** [S1] — **not used** as the model's cylinder height; a real can's dome, neck and flange make its true fill volume smaller than a plain cylinder of this diameter and this overall height would hold (a naive cylinder at 2.602 in × 4.812 in holds about 25.6 in³, roughly 18% more than the actual 21.65625 in³ fill volume), so this case derives the model's height from the fixed volume instead (see the value directly above) and states this published figure only so a Hero can see the size of that simplification |
| Retooling cost for Hold The Line | $0 — no die or tooling change |

**The Slim Retool — the calculus-optimal body.** The radius and height that minimize total surface
area for a closed cylinder of this same fixed volume, found by the optimization work in D1 and D2:

| | Value |
|---|---|
| Optimal radius r* | derived in D1/D2: r* = (V / 2π)^(1/3) = **1.5105 in** — the student's own work |
| Optimal height h* | derived in D1/D2: h* = V / (π r*²) = **3.0211 in** (h*/r* = 2.0000 exactly, the classic result — the student's own work) |
| Total surface area at r*, h* | derived: S(r*) = **43.0101 in²**, a **2.0866%** reduction from Hold The Line's 43.9266 in² — the student's own work |
| Retooling cost for The Slim Retool | **$600,000** [MA2] — a stated Modeling Assumption; no public price exists for a one-off die-and-tooling changeover on a specific beverage-can forming/necking line (SEE APPENDIX D) |

## Appendix B — Aluminum Material and Pricing

| | Value |
|---|---|
| Can-body aluminum alloy | 3104-H19 or an equivalent beverage-can-body sheet alloy |
| Density of 3104-H19 aluminum sheet | **0.0983 lb/in³** (2.72 g/cc) [S2] |
| Can-body sheet thickness (gauge), assumed uniform for both options | **0.0043 in** [MA1] — a stated Modeling Assumption (SEE APPENDIX D) |
| Current aluminum price | **$2.42 per pound** — US spot market price of primary aluminum ingot, January 2026 [S3] |

The sheet thickness is held identical for both options: retooling changes only the forming die's
diameter, not the coil stock Ridgeline buys, so any weight difference between the two can bodies
comes entirely from the difference in surface area computed in Appendix A.

## Appendix C — Production Volume, Retooling Cost, and the Payback Bar

| | Value |
|---|---|
| Ridgeline's annual can volume on this line | **300,000,000 cans per year** [MA3] — a stated Modeling Assumption (SEE APPENDIX D) |
| Retooling cost for The Slim Retool | **$600,000** [MA2] (same figure as Appendix A) |
| Plant leadership's capital-approval payback ceiling | **24 months** [MA4] — a stated Modeling Assumption (SEE APPENDIX D) |

## Appendix D — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and APPENDIX G names the skills a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Can-body sheet thickness (gauge), held identical for both options | **0.0043 in** | Several trade and technical sources describe modern draw-and-wall-ironed (DWI) beverage-can sidewalls as roughly 0.0037–0.0049 in thick, but no single manufacturer or standards-body datasheet stating an exact gauge was located and fetched to a primary source, so this case fixes the midpoint of that commonly cited range. | Affects the **absolute** weight and dollar figures in D3 and D4, and therefore the payback period, but **cannot** change the surface-area or surface-area-percent comparison in D1–D3, which is thickness-independent (the same thickness multiplies both options' weight equally). At the range's low end (0.00215 in, −50%) payback stretches to about 51 months; at its high end (0.00645 in, +50%) payback drops to about 17 months — this single assumption alone can flip the verdict against the 24-month ceiling in either direction. |
| MA2 | Retooling cost: a die-and-tooling changeover on Ridgeline's existing Line 3 forming/necking equipment to the new body diameter | **$600,000** | No public price exists for a one-off die-and-tooling changeover specific to this line; a general corporate capital-budgeting range of roughly one to three years' payback is commonly cited for manufacturing equipment retooling, but no source states a dollar figure for this specific job, so the case fixes a value representative of a die-and-tooling-only changeover (new die sets, neck and flange re-tooling, changeover trials) rather than a full new production line. | Directly load-bearing on the payback period, linearly: halving it (to $300,000) drops payback to about 13 months (clears the 24-month ceiling); raising it 50% (to $900,000) stretches payback to about 38 months (misses it by a wide margin). |
| MA3 | Ridgeline Canning's annual can production volume on this line | **300,000,000 cans per year** | Ridgeline Canning is fictional, so no public production figure can exist for it. The value is grounded in real published can-line throughput: modern high-speed beverage can lines run at roughly 2,000–2,400 cans per minute at full rate, and a contract canner running one line across multiple client SKUs with realistic changeovers and downtime — well under full-rate, round-the-clock operation — landing at 300 million cans a year (an average of roughly 570 cans per minute if run continuously, or a higher instantaneous rate for fewer hours per day) is an ordinary volume for a single mid-size contract line. | Directly load-bearing on the payback period, linearly, in the opposite direction from MA2: halving it (150 million cans/yr) stretches payback to about 51 months; raising it 50% (450 million cans/yr) drops it to about 17 months. |
| MA4 | Plant leadership's capital-approval payback ceiling for a line-level retooling request | **24 months** | Ridgeline's specific finance policy is not public. A payback period of roughly one to three years is widely described in general capital-budgeting practice as an acceptable range for manufacturing equipment investments; this case fixes Ridgeline's policy at the middle of that range. | This is the **threshold** the other three assumptions are measured against, not an input to the payback calculation itself — it does not change the computed payback period, only whether that period counts as a "yes." Moving it to 30 months would flip the verdict to B at the base-case figures; moving it to 20 months makes A's margin wider. |

## Appendix E — Sources

| # | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Standard body outside diameter and overall (flanged) height for a 12 fl oz beverage can | 2.602 in diameter (nominal 2.600 in); 4.812 in overall flanged height | Can Manufacturers Institute, 202 Beverage Can and End Specifications, published on Can Central ([link](https://www.cancentral.com/beverage-cans__trashed/standards/)) | 2026-08-13 | HIGH — the standards body itself, the primary publisher of US beverage-can body dimensions |
| S2 | Density of aluminum alloy 3104-H19, the standard beverage-can-body sheet alloy | 0.0983 lb/in³ (2.72 g/cc) | MatWeb Material Property Data, datasheet MA3104H19, data point sourced by MatWeb to the Aluminum Association, Inc.; matweb.com itself returned HTTP 403 on direct fetch, so the identical datasheet was fetched via a university-hosted archival mirror ([link](https://gab.wallawalla.edu/~larry.aamodt/engr325/MaterialData_9035.pdf)) | 2026-08-13 | MEDIUM — the figure is explicitly flagged by MatWeb as "AA; Typical" and the datasheet states its Aluminum-Association-sourced data points are "NOT FOR DESIGN," so this is a typical/representative value for the alloy family rather than a guaranteed specification figure. It is applied identically to both can shapes, so it scales the size of the weight and dollar answers and cannot by itself change which shape has less material. |
| S3 | Current US market price of primary aluminum ingot | $2.42 per pound | U.S. Geological Survey, National Minerals Information Center, *Mineral Industry Surveys: Aluminum in January 2026* — "The January 2026 average U.S. spot market price of primary aluminum ingot was $2.42 per pound, 10 percent more than that in December 2025 and 71 percent more than that in January 2025." ([link](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/mis-202601-alumi_0.pdf)) | 2026-08-13 | HIGH — a primary US government source, a stated month, unambiguous units, and the exact quantity the case needs (not a proxy). Published July 2026; the "as of" cutoff for every dollar figure in this case is the January 2026 average this report states. |

## Appendix F — Learn More

These are real, currently-live resources for a curious Hero who wants to go beyond what the
challenges require — background on beverage-can manufacturing, real-world can dimensions, and
aluminum market economics. None of these is required to complete any Challenge.

- [Drink can — Wikipedia](https://en.wikipedia.org/wiki/Drink_can) — an overview of beverage-can
  history, materials, and the cold-forming manufacturing process that turns a flat aluminum disc
  into a can body like the ones on Ridgeline's line.
- [Beverage Can Standards — Can Manufacturers Institute](https://www.cancentral.com/beverage-cans__trashed/standards/) —
  the actual published industry specification sheet for standard 12 fl oz can body dimensions, the
  same document Appendix E draws the Hold The Line diameter from.
- [Aluminum Statistics and Information — USGS National Minerals Information Center](https://www.usgs.gov/centers/national-minerals-information-center/aluminum-statistics-and-information) —
  the U.S. Geological Survey's public data on aluminum supply, demand, and pricing, the same
  government source family this case's aluminum price (Appendix E, S3) comes from.
- [Section 4.8: Optimization — Paul's Online Math Notes](https://tutorial.math.lamar.edu/Classes/CalcI/Optimization.aspx) —
  a free calculus reference that works through this exact problem type step by step: minimizing
  the material used in a cylindrical can of fixed volume using derivatives.

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Critical Point
- Local Maximum
- Local Minimum
- Concavity
- Derivative
- Instantaneous Rate Of Change

**"How to…" questions**

- How to find critical points of a function
- How to use the first derivative test to classify a critical point
- How to solve an optimization problem using derivatives
- How to find a derivative using the power rule
- How to convert an amount with compound units
- How to find the percent of a number

<!-- FACILITATOR ONLY -->

## Balance argument (facilitator only — never shipped to students)

**Argument for A (Hold The Line).** At the stated retooling cost ($600,000, MA2) and Ridgeline's
stated annual volume (300,000,000 cans/yr, MA3), The Slim Retool saves only **$0.000938 per can**
(2.0866% of the standard body's $0.044933 material cost) — because the true calculus optimum is
not that much better than the standard proportions to begin with. That comes to **$281,268.82 a
year**, and $600,000 ÷ $281,268.82 × 12 = **25.60 months** to pay back — about **6.24% longer**
than plant leadership's stated 24-month ceiling. The shape genuinely uses less metal, on every can,
forever, and it still does not clear the bar this year.

**Argument for B (The Slim Retool).** The saving is small per can but it is **permanent**, not a
one-time event: every can Ridgeline stamps on this line for the rest of the tooling's working life
carries the same 2.09% material-cost reduction, and the case's own break-even calculation shows the
gap to approval is narrow — Ridgeline would only need **319,978,587 cans/yr** (about 6.7% more than
the stated 300,000,000) for the retooling to clear the 24-month ceiling on its own numbers. A
contract canner's volume on any one client line is exactly the kind of figure that moves with a
single new contract, and 6.7% is a thin margin to be confidently wrong about.

**Margin.** `margin_pct` = **6.24**, computed as the percentage by which the retooling's actual
annual savings ($281,268.82) falls short of the annual savings required to hit the 24-month ceiling
($300,000.00). Hold The Line wins the case's own numbers, but narrowly, and the verdict is directly
sensitive to three separately stated assumptions (MA1 sheet thickness, MA2 retooling cost, MA3
annual volume) — flexing any single one of them ±50% is enough to flip the recommendation in either
direction (see Appendix D). That fragility is disclosed here and in FACILITATOR.md as the case's
own headline finding, not hidden.

**The trap.** A Hero who computes only the surface-area reduction (2.09%, D1–D2) and treats a
"smaller shape uses less material, therefore retool" conclusion as self-evident has skipped the
entire second half of the case — D3's per-can dollar conversion and D4's payback calculation are
where the actual decision lives, and a shape that is unambiguously better on material can still be
the wrong capital call this year. The second half of the same trap runs the other way: a Hero who
sees "25.6 months against a 24-month ceiling" and calls it a clean, decisive "no" has missed how
thin that 6.24% margin is against assumptions the case states plainly are not sourced.

**Sensitivity note (SPEC §6).** None required — the stakes are commercial and professional (a
material-cost line item and a capital-review recommendation), not personal loss or family hardship.
Both can shapes are legal, safe, and already run somewhere in the industry; nothing in this case
asks a Hero to trade safety for money.
