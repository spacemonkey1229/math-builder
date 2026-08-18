# RESEARCH LOG — The Optimal Can

**Stage 3, `case-research`, run 2026-08-13.** Opened with **9** `{{NEEDS_SOURCE}}` tokens in
`case.md` (two of them the same figure — the retooling cost — repeated in Appendix A and Appendix
C); closed with **0**. Every URL below was fetched with `WebFetch` (or reached via search plus a
direct fetch of the primary page) and confirmed to carry the figure cited before it was written
into the case. Nothing was filled from memory.

| Outcome | Raw tokens |
|---|---|
| SOURCED | 4 (P01, P02, P03, P06) |
| ASSUMPTION (stated in Appendix D) | 5 (P04, P05, P07, P08, P09) |
| DROPPED | 0 |
| Still OPEN | **0** |

---

## What was searched, what was found, and what was rejected

### P01 / P02 · Standard can body diameter and overall height

**Searched:** the primary US standards body for beverage can dimensions.
**Rejected without using a figure from them:** a run of SEO/aggregator "can dimensions" sites
(measuresnest.com, candimension.com, pdmeasurement.com, cansizedimensions.com, queendimensions.com,
cansdimension.com, dimensionschart.com, feet2inches.com) that all report the same figures without
attribution — none of these were used as the citation even though several converged on numbers
close to the eventual sourced value, per SPEC §5's rule against citing what was not fetched from a
primary source.
**Found:** the **Can Manufacturers Institute** publishes its own **202 Beverage Can and End
Specifications** table on Can Central. Fetched directly: Body Outside Diameter "2.602 ± .007"
(nominal 2.600 in), Flange Can Height "4.812 ± .015" in (**S1**). This is the standards body
itself — the best possible source class for this figure.

**A modeling decision made from this data, not a further search.** The published overall/flanged
height (4.812 in) is **not** used as the model cylinder's height. A plain cylinder at the sourced
diameter and this height would hold about 25.6 in³ — roughly 18% more than the case's actual
21.65625 in³ fill volume — because a real can's domed bottom, tapered neck and flange are not
capturable by a right-circular-cylinder model. Rather than silently use a height that is
inconsistent with the stated fixed volume, the case derives the model's height from the sourced
radius and the fixed volume (h = V/πr²) and states the published overall height only as reference
context with the discrepancy named openly (SPEC §1.6 — real, over-complete data the case explains
rather than hides).

### P03 · Density of the can-body aluminum alloy

**Searched:** a primary or well-attributed technical materials source for 3104-H19 or 3004-H19,
the standard beverage-can-body sheet alloys.
**Rejected:** direct fetch of `matweb.com` — returned **HTTP 403**.
**Found:** the identical MatWeb datasheet content (MA3104H19), reproduced in a university
engineering-course materials-data archive at `gab.wallawalla.edu`, which mirrors MatWeb's own
formatting and explicitly credits the Aluminum Association, Inc. as the data provider. Density:
0.0983 lb/in³ (2.72 g/cc) (**S2**).

Graded **MEDIUM**, not HIGH: MatWeb itself flags this figure "AA; Typical" and states that
Aluminum-Association-sourced data points on its datasheets are "NOT FOR DESIGN" — a representative
value for the alloy family, not a guaranteed specification figure. Applied identically to both can
shapes in this case, so it scales the size of the answer and cannot change which shape uses less
material.

### P04 · Can-body sheet thickness (gauge) — **stated Modeling Assumption (MA1)**

**Searched:** a primary manufacturer or standards-body datasheet stating an exact sidewall gauge
for a DWI (draw-and-wall-ironed) beverage can body.
**Rejected:** every source found was a trade/DIY article citing a range (roughly 0.0037–0.0049 in)
without a single, consistent, attributable primary figure — asmr.education, arhfoundation.org,
aluminiummagazine.com, prestogroup.com, thefabricator.com among them. None carried the kind of
unambiguous, dated, primary provenance SPEC §5 requires for a load-bearing figure.
**Exit taken: stated Modeling Assumption** (`case-research` §5, exit 1). **MA1 = 0.0043 in**, the
midpoint of the commonly cited range, in the visible Modeling Assumptions block. Its sensitivity is
written down: it is a linear multiplier on the absolute weight/dollar figures and therefore on the
payback period, but it cannot affect the surface-area-percent comparison in D1–D3 at all, since the
same thickness multiplies both can shapes' weight equally.

### P05 / P08 · Retooling cost — **stated Modeling Assumption (MA2)**, one figure, two appendix rows

**Searched:** a public price for a die-and-tooling changeover on an existing beverage-can
forming/necking line.
**Rejected:** general capital-budgeting articles (Wikipedia's *Payback period*, leanmanufacture.net,
sensorfact.eu, cmmonline.com and others) — these describe *typical acceptable payback ranges* for
manufacturing capital generally, which informed MA4 below, but none state a dollar figure for this
specific kind of changeover. No manufacturer or trade-press figure for a beverage-can die
changeover was located.
**Exit taken: stated Modeling Assumption** (exit 1), as anticipated in the brainstorm sheet before
research began. **MA2 = $600,000**, representative of a die-and-tooling-only changeover (new die
sets, neck/flange re-tooling, changeover trials) rather than a full new production line. Directly
and linearly load-bearing on the payback period.

### P06 · Current aluminum price

**Searched:** a primary, dated, US market price for primary aluminum ingot.
**Attempt 1 — FRED (`PALUMUSDM`, "Global price of Aluminum").** A real, public IMF-sourced monthly
series with search-visible values (e.g. February 2026 at $3,065.19/metric ton), but **every direct
fetch of fred.stlouisfed.org returned HTTP 403** (both the series page and the `fredgraph.csv`
export), so no page from this series was actually fetched and it was **not cited**, per SPEC §5 and
MCS-21's rule against citing a URL not fetched.
**Attempt 2 — investing.com commodities page.** Fetched successfully but carries no stated
reporting date beyond a live timestamp, and is a continuously live quote rather than a dated period
average — rejected on the same "undated live quantity" grounds SPEC §5 requires (compare
`cases/wind-triangle`'s rejection of the IATA Jet Fuel Price Monitor for the same reason).
**Found:** the **U.S. Geological Survey**, National Minerals Information Center, *Mineral Industry
Surveys: Aluminum in January 2026* (published July 2026). Fetched directly (via the PDF's page
text, extracted with the `Read` tool after `WebFetch` returned the binary): "The January 2026
average U.S. spot market price of primary aluminum ingot was $2.42 per pound, 10 percent more than
that in December 2025 and 71 percent more than that in January 2025" (**S3**). A primary US
government source, a stated month, unambiguous units ($/lb, matching what the case needs directly
rather than a $/metric-ton figure requiring a further unit conversion), graded **HIGH**.

**"As of" handling, per SPEC §5.** Every dollar figure in this case is frozen at the January 2026
average this report states, published July 2026. No part-month or undated figure is used anywhere
in the case.

### P07 · Ridgeline's annual can volume on this line — **stated Modeling Assumption (MA3)**

Ridgeline Canning is fictional; no production figure for it can exist publicly. Rather than assume
a number with no real anchor, the assumption is **grounded in real published can-line throughput**:
search results converged on modern high-speed beverage can lines running roughly 2,000–2,400 cans
per minute at full rate (thefabricator.com, packworld.com, and multiple can-line-equipment vendor
pages). **MA3 = 300,000,000 cans/year**, a volume consistent with a single mid-size contract-canner
line running well under full-rate, round-the-clock operation (an average of roughly 570 cans/minute
if run continuously, or a higher instantaneous rate across fewer hours per day) — an ordinary
figure for one line serving multiple client SKUs with realistic changeovers and downtime, not a
figure this case claims is Ridgeline's actual number.

### P09 · Plant leadership's capital-approval payback ceiling — **stated Modeling Assumption (MA4)**

Ridgeline's specific finance policy is not public and cannot be, being fictional. General
capital-budgeting sources (Wikipedia's *Payback period*, leanmanufacture.net, cmmonline.com,
themanufacturingacademy.com) converge on roughly **one to three years** as a commonly cited
acceptable payback range for manufacturing equipment investment, without prescribing a single
number for any specific company. **MA4 = 24 months**, the midpoint of that range. This assumption
functions as the case's **threshold**, not an input to the payback calculation itself — it decides
whether a given payback period counts as a "yes," but does not change the computed 25.60-month
figure.

---

## Derived arithmetic, in the open

| Quantity | Value | How |
|---|---|---|
| Fixed volume | 21.65625 in³ | 12 US fl oz × (231/128) in³/fl oz — exact by the legal fluid-ounce definition |
| Standard radius | 1.301 in | one-half the CMI diameter [S1] |
| Standard height | 4.0727 in | V / (π r²) |
| Standard surface area | 43.9266 in² | 2πr² + 2πrh |
| Optimal radius r* | 1.5105 in | (V / 2π)^(1/3), solving dS/dr = 0 |
| Optimal height h* | 3.0211 in | V / (π r*²); confirms h*/r* = 2 exactly |
| Optimal surface area | 43.0101 in² | 2πr*² + 2πr*h* |
| Surface-area reduction | 2.0866% | (S_std − S_opt) / S_std × 100 |
| Weight per can, standard / optimal | 0.018567 lb / 0.018180 lb | S × thickness [MA1] × density [S2] |
| Material cost per can, standard / optimal | $0.044933 / $0.043995 | weight × price/lb [S3] |
| Savings per can | $0.000938 (2.0866%) | cost_std − cost_opt |
| Annual savings | $281,268.82 | savings/can × 300,000,000 cans/yr [MA3] |
| Payback period | 25.598 months | retool cost [MA2] ÷ annual savings × 12 |
| Required annual savings for a 24-month payback [MA4] | $300,000.00 | retool cost ÷ (24/12) |
| `margin_pct` | **6.24** | (required − actual annual savings) / required × 100 |
| Break-even annual volume | 319,978,587 cans/yr | required annual savings ÷ savings per can |

Sensitivity (±50% one dial at a time, from the base case): thickness [MA1] 0.00215–0.00645 in →
payback 51.2–17.1 months; retooling cost [MA2] $300,000–$900,000 → payback 12.8–38.4 months; annual
volume [MA3] 150M–450M cans/yr → payback 51.2–17.1 months. **Each of the three numeric assumptions
alone is capable of flipping the verdict** against the 24-month ceiling [MA4] in either direction —
this fragility is disclosed in `case.json.modeling_assumptions[]`, in `case.md` Appendix D, and in
the facilitator-only balance section, not hidden.

## Handed back to `case-readiness`

Zero placeholders remain. `case.json.status` = `researched`. `qa.verdict` is left `null` — that is
`case-readiness`'s field to set, not this stage's. Next step: `case-qa` / `case-readiness` on
`the-optimal-can`.
