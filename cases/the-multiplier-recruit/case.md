Case Study: The Multiplier Recruit
MS | Math | Case Study | 2026 | Adventure

## Overview

The email from the site-selection consultant landed at 4:52 the night before, and Ben Okafor has
read it eleven times since. Both offers are still open. Both close in eighteen hours. On his desk
are two folders, each thick with letterhead and site plans, and one number he cannot stop
thinking about: the Calder County Industrial Development Authority has exactly one incentive
package to hand out this fiscal year, and the board votes at nine tomorrow morning.

To his left, Meridian Forgeworks — a precision-components manufacturer that would buy steel,
tooling, and packaging from a dozen local shops Ben already knows by name. To his right, Cascade
Distribution — a regional logistics center that would hire more people outright and open a
building on the county's biggest vacant industrial lot within the year. His predecessor used to
settle calls like this with a gut feeling and a spreadsheet of direct hires. Ben pulls up the
regional input-output worksheet instead, the one the board has never once asked him to actually
show his work on. Tonight, he thinks, they will.

He opens both employer packets side by side, uncaps a pen, and starts building the matrix.

## Background

Ben Okafor is the regional economic development analyst for the Calder County Industrial
Development Authority (IDA). He is responsible for recommending which employer the IDA should
recruit with the county's single annual incentive package, and accountable to the IDA board for
showing that his recommendation is not just a guess (SEE APPENDIX A). Two employers have each
submitted a formal relocation offer, and the IDA can fund only one:

**The Anvil Bid** — recruiting **Meridian Forgeworks**, a precision-components manufacturer that
would hire 140 people directly and purchase most of its steel, tooling, and packaging from local
suppliers already operating in Calder County (SEE APPENDIX A).

**The Waypoint Bid** — recruiting **Cascade Distribution**, a regional logistics and distribution
center that would hire 310 people directly, more than double Meridian's direct headcount, but
would purchase comparatively little from other Calder County businesses once its building and
racking are installed (SEE APPENDIX A).

Both employers would receive the exact same incentive rate per direct job they create — Calder
County's incentive program pays a flat dollar amount per net new full-time job, modeled on a real,
publicly published state incentive schedule (SEE APPENDIX D). Read only by that headline rate, the
two bids are identical: the same dollars per direct job, every time. That is exactly why the
headline rate cannot be the number the board votes on.

What the flat per-job rate does not capture is what economists call the regional multiplier
effect: money a new employer spends locally on suppliers and services gets spent again by those
suppliers' own workers, and again by the next round of local vendors, before it finally leaks out
of the county. A manufacturer that buys heavily from local suppliers keeps more of each dollar
circulating inside Calder County than a distribution center that buys comparatively little
locally — even if the distribution center hires more people directly. The real federal tool for
measuring exactly this effect is the U.S. Bureau of Economic Analysis's Regional Input-Output
Modeling System, RIMS II (SEE APPENDIX C) — the same tool practicing regional economic developers
like Ben actually use, priced per region ordered directly from BEA. Calder County's IDA has never
purchased a RIMS II table for its own county, so Ben has to build his own regional model by hand,
calibrated to real, published RIMS II multiplier examples (SEE APPENDICES B and C), starting from
the same kind of county-level baseline employment picture the real U.S. Census Bureau's County
Business Patterns program publishes for every U.S. county [S4] (SEE APPENDIX F).

Ben's recommendation must be judged on one number: **total regional jobs supported — direct,
indirect, and induced — per $10,000 of incentive spent**, found by solving Calder County's
two-sector regional economy as a system of linear equations using matrices (SEE APPENDICES B, D
and E). Every sourced and assumed figure in this case is listed in **APPENDIX F**, and the
vocabulary and "how to…" skills this case will ask of you are listed in **APPENDIX G** — that is
where Challenge 1 sends you.

## Dilemma

You are Ben Okafor.
Do you:
A.) Recommend The Anvil Bid — recruit Meridian Forgeworks, the manufacturer with heavier local
supplier purchasing OR
B.) Recommend The Waypoint Bid — recruit Cascade Distribution, the logistics center with more
direct jobs

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A labeled 2×2 regional technical coefficient matrix, **A** (SEE APPENDIX B): every entry
    defined in words (which sector buys how much from which, per dollar of that sector's own
    output), with the matrix's dimensions stated.
    D2. The identity matrix **I** and the computed matrix **(I − A)**, with every entry of
    **(I − A)** shown as an arithmetic step, not just a final grid.
    D3. The determinant of **(I − A)**, computed by hand using the 2×2 determinant formula, with a
    one-sentence explanation of why a nonzero determinant is required before the system in D4 can
    be solved at all.
    D4. The solved total-regional-jobs vector **x = (I − A)⁻¹d** for **each** employer's direct-jobs
    vector **d** (SEE APPENDIX A), showing the full matrix arithmetic used to solve the system —
    not just the final numbers.
    D5. A final decision table (SEE APPENDICES A and D): for Meridian Forgeworks and for Cascade
    Distribution, direct jobs, total regional jobs supported (from D4), incentive dollars owed at
    Calder County's flat per-job rate, and jobs supported per $10,000 of incentive — with your
    recommendation stated and defended using that last column.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Employer Bids

| | Meridian Forgeworks (The Anvil Bid) | Cascade Distribution (The Waypoint Bid) |
|---|---|---|
| Industry | Durable-goods manufacturing (precision metal components) | Trade, transportation & warehousing (regional distribution center) |
| Direct jobs created (net new, full-time) | **140** [MA3] | **310** [MA3] |
| Regional sector assigned in the model (SEE APPENDIX B) | Sector 1 — Manufacturing | Sector 2 — Trade, Transportation & Warehousing |
| Direct-jobs vector **d** used in D4 | d = [140, 0]ᵀ | d = [0, 310]ᵀ |

Both employers are fictional companies invented for this case (SEE APPENDIX E, MA3); their direct
headcounts are the case's own stated scenario numbers, sized to be realistic for a manufacturer
and a distribution center of the kind that regularly compete for a single county incentive
package.

## Appendix B — Calder County's Regional Technical Coefficient Matrix

Ben's model divides Calder County's economy into two sectors for this decision:

- **Sector 1 — Manufacturing** (Meridian Forgeworks's industry)
- **Sector 2 — Trade, Transportation & Warehousing** (Cascade Distribution's industry)

Each entry of the technical coefficient matrix **A** below is the number of dollars a sector must
buy **from Calder County businesses** — not from outside the region — to produce one additional
dollar of its own output. Column 1 is Sector 1's local buying pattern; column 2 is Sector 2's.

|  | buys from Sector 1 (Mfg) | buys from Sector 2 (Trade/Trans/Whse) |
|---|---|---|
| **to produce $1 of Sector 1 output** | 0.20 | 0.05 |
| **to produce $1 of Sector 2 output** | 0.08 | 0.10 |

$$A = \begin{bmatrix} 0.20 & 0.05 \\ 0.08 & 0.10 \end{bmatrix}$$

**These four numbers are a stated Modeling Assumption, not a purchased RIMS II table for Calder
County (SEE APPENDIX E, MA1).** Calder County is fictional, so BEA has no county to sell a
multiplier table for — and even for a real county, that table costs $520 (SEE APPENDIX C, S1). The
values above were chosen by Ben's office so that solving the system in D4 reproduces regional
output-multiplier magnitudes close to the real, published RIMS II examples in Appendix C: this
matrix's own column sums, once inverted, land at **1.369** for Sector 1 and **1.187** for Sector 2
— within a few hundredths of the real 1.3616 (manufacturing) and 1.1810 (a real comparison
service industry) figures BEA has actually published for a real U.S. county (SEE APPENDIX C, S2).
The direction the assumption encodes — manufacturing re-spends more of each dollar locally than
trade/distribution does — matches real, published national data: manufacturing's intermediate
inputs run **52.1%** of output nationally against **36.5%** for services (SEE APPENDIX C, S2), a
real gap in the same direction this matrix assumes, even though that national figure is not itself
regional and is not one of the four numbers used directly.

## Appendix C — Real RIMS II Reference Data (BEA)

This appendix is real, published federal data, reproduced here so you can check Appendix B's
assumption against it — it is **not** Calder County's own data.

| Claim | Value | Source |
|---|---|---|
| Price to order RIMS II multipliers for one region (county or contiguous-county group) | **$520 per region**, all industries | [S1] |
| RIMS II's current data vintage | 2024 regional data, 2017 national benchmark input-output data, released May 2026 | [S1] |
| Real Type I final-demand output multiplier, "Miscellaneous manufacturing," Butler County, OH | **1.3616** | [S2] |
| Real Type I final-demand output multiplier, "Management of companies" (a service industry), Butler County, OH | **1.1810** | [S2] |
| National intermediate-input share of output, Manufacturing (2012 data) | **52.1%** | [S2] |
| National intermediate-input share of output, Services (2012 data) | **36.5%** | [S2] |

**What a Type I final-demand multiplier means.** For every extra $1 of output a region's
final-demand delivers to one industry, the multiplier is the total dollar change in output across
**every** industry in the region once the resulting local supply-chain purchases (but not
household spending — that is what makes it "Type I," not "Type II") ripple through. A multiplier
of 1.3616 means $1.00 of new manufacturing demand produces $1.3616 of total regional output. This
is exactly the same idea Appendix B's matrix computes by hand: **(I − A)⁻¹** applied to a demand
vector *is* a Leontief-style multiplier calculation, the same family of math behind BEA's own
published RIMS II tables.

## Appendix D — Calder County Incentive Schedule

| | Value |
|---|---|
| Incentive paid per net new full-time direct job (flat rate, both bids) | **$3,000 per job** [S3, MA2] |
| Meridian Forgeworks (140 direct jobs) — total incentive owed | 140 × $3,000 = **$420,000** |
| Cascade Distribution (310 direct jobs) — total incentive owed | 310 × $3,000 = **$930,000** |

**This rate is a stated Modeling Assumption, anchored to a real, currently active state program**
(SEE APPENDIX E, MA2): Florida's Qualified Target Industry (QTI) Tax Refund pays **$3,000 per net
new full-time job** (base rate; $6,000 in a designated rural community), under Section 288.106,
Florida Statutes (SEE APPENDIX F, S3). Calder County is not Florida and does not run the QTI
program — this case borrows QTI's real base per-job rate as a realistic, defensible flat rate for
a fictional county's own incentive program, disclosed here rather than presented as Calder
County's own passed legislation.

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Calder County's regional technical coefficient matrix **A** (Appendix B) | a₁₁=0.20, a₁₂=0.05, a₂₁=0.08, a₂₂=0.10 | Calder County is fictional, so no purchased RIMS II table exists for it; a real county's own table costs $520 (Appendix C, S1) and was not purchased for this exercise. These four values were chosen so the resulting Sector-1 and Sector-2 output multipliers (1.369 and 1.187) land within a few hundredths of BEA's own real, published Type I multiplier examples for a real county — Butler County, OH: 1.3616 (manufacturing) and 1.1810 (a comparison service industry) — and preserve the real, sourced direction that manufacturing carries a higher local multiplier than trade/distribution in a county-sized region (Appendix C, S2). | The case's entire primary-metric margin depends on these four numbers. A different real county's own purchased RIMS II table would give different exact multipliers — that dependency is disclosed here, not hidden. |
| MA2 | Calder County's flat incentive rate, $3,000 per net new direct job (Appendix D) | $3,000/job | Anchored to Florida's real Qualified Target Industry (QTI) Tax Refund base rate of $3,000 per net new full-time job under Section 288.106, Florida Statutes (Appendix F, S3). Calder County does not run Florida's actual QTI program; this case borrows its real base rate as a realistic flat-rate stand-in. | Because both bids are paid the same flat per-job rate, this rate cancels out of the *comparison* between A and B in relative terms — raising or lowering it changes both incentive totals proportionally and does not by itself flip which option wins. It does change the absolute size of the "jobs per $10,000" numbers in D5. |
| MA3 | Direct job counts: Meridian Forgeworks 140; Cascade Distribution 310 (Appendix A) | 140 and 310 | Meridian Forgeworks and Cascade Distribution are both fictional companies invented for this case; there is no real employer to source their hiring plans from. The values were chosen to be realistic for a mid-size precision manufacturer and a regional distribution center respectively, and so that Cascade's direct-jobs lead over Meridian (more than double) is large enough to make the naive "more direct jobs wins" read genuinely tempting. | The case's margin is sensitive to the ratio between these two headcounts — the answer is sensitive to this value, which is exactly why D5 asks you to compute the actual multiplier-adjusted comparison rather than compare the two headcounts directly. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | Price and current data vintage to order RIMS II multipliers for one region | $520 per region, all industries; 2024 regional data with 2017 national benchmark input-output data, released May 2026 | U.S. Bureau of Economic Analysis. "RIMS II: Regional Input-Output Modeling System — Order Multipliers." ([apps.bea.gov/regional/rims/rimsii/](https://apps.bea.gov/regional/rims/rimsii/)) | 2026-08-18 | HIGH — primary federal source, official ordering page, fetched directly |
| S2 | Real Type I final-demand output multipliers (Butler County, OH, manufacturing vs. a service industry) and national intermediate-input shares of output by sector | Multipliers: 1.3616 (miscellaneous manufacturing), 1.1810 (management of companies), Butler County, OH; shares: 52.1% (manufacturing), 36.5% (services), 2012 data | Franklin H, McComb T, Rzeznik SJ. "Benchmark Update of the Regional Input-Output Modeling System." *Survey of Current Business* 99(12), December 2019, U.S. Bureau of Economic Analysis. Table 1 and Table 7. ([apps.bea.gov/scb/2019/12-december/pdf/1219-rims2.pdf](https://apps.bea.gov/scb/2019/12-december/pdf/1219-rims2.pdf)) | 2026-08-18 | HIGH — primary BEA journal article, named authors, dated, fetched directly; the two 2012/2017-vintage multiplier columns of Table 7 are used here (the article's own most recent benchmark at time of publication), not the older 2007/2016 columns also shown in that table |
| S3 | Florida's Qualified Target Industry (QTI) Tax Refund per-job incentive rate | $3,000 per net new full-time equivalent job (base rate); $6,000 in a Rural Community (county) | Enterprise Florida, Inc. "Qualified Target Industry Tax Refund" program fact sheet. Statutory reference: Section 288.106, Florida Statutes. ([selectflorida.org/wp-content/uploads/incentive-qualified-target-industry-tax-refund.pdf](https://selectflorida.org/wp-content/uploads/incentive-qualified-target-industry-tax-refund.pdf)) | 2026-08-18 | MEDIUM — official state economic-development agency fact sheet with a specific statutory citation and unambiguous per-job dollar figures, but the PDF itself carries no visible publication or last-updated date, and Enterprise Florida's functions have since moved to the Florida Department of Commerce, so this exact one-page document's currency cannot be independently confirmed in this session — used here only as the real-program anchor for a stated Modeling Assumption (Appendix E, MA2), not as Calder County's own passed rate |
| S4 | Existence, geographic scope, and measures of the U.S. Census Bureau's County Business Patterns (CBP) program | Annual series; establishment counts, employment (week of March 12), first-quarter and annual payroll; county-level detail; most recent available at time of access was 2023 data | U.S. Census Bureau. "County Business Patterns (CBP)." ([census.gov/programs-surveys/cbp.html](https://www.census.gov/programs-surveys/cbp.html)) | 2026-08-18 | HIGH — primary federal program page, fetched directly. Used only to establish that CBP is the real tool an analyst like Ben would consult for county baseline employment (see Background); no specific CBP employment figure for a real county is used as a load-bearing number anywhere in this case, because Calder County itself is fictional (see RESEARCH_LOG.md for the attempted, unsuccessful search for a substitute real county's current-year CBP figures) |

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Matrix
- Matrix Dimension
- Determinant
- Identity Matrix

**"How to…" questions**

- How to add and multiply matrices
- How to find the determinant of a 2x2 matrix
- How to solve a system of equations using a matrix

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
