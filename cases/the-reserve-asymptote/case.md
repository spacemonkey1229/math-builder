# Case Study: The Reserve Asymptote

MS | Math | Case Study | 2026-27 | Heroes Academy

*(Band: HS-entry / HS. This case uses precalculus and calculus vocabulary — limits, asymptotes, and continuity — and is written for a Hero who has finished algebra and is ready for a first, informal pass at calculus reasoning.)*

---

## Overview

Harlan Voss reads the same line of the spreadsheet for the third time, because the third time it still doesn't smooth out the way it's supposed to.

It's 6:50 on a Tuesday evening and the office is empty except for the hum of the server closet down the hall. Highline Life & Annuity files its new longevity-annuity reserve basis with the state insurance department in eleven days, and Harlan is the analyst whose initials go at the bottom of the actuarial memorandum. Next to a cold cup of coffee sits a printout with a single circled number: the reserve rate the model assigns to a policyholder turning exactly one hundred years old this filing year.

Two spreadsheets are open side by side. The left one holds the formula his mentor taught him three years ago — a clean, smooth curve that grinds through every attained age in seconds and has never once caused a filing to bounce. The right one holds the actual published mortality table, age by age, exactly as printed, with a jump near the top that the smooth formula quietly glides past.

Both spreadsheets are supposed to produce the same thing: the dollars of reserve required per thousand dollars of promised benefit. They don't agree — not by a little, and not everywhere, but very sharply in exactly one place.

Harlan minimizes his email, opens a blank sheet of scratch paper, and writes both formulas at the top of the page. He has eleven days to decide which one goes in the filing.

---

## Background

Harlan Voss is a senior actuarial analyst at Highline Life & Annuity Company, a regional insurer. He is one of two analysts responsible for the reserve basis behind Highline's newest product, the Horizon Series — a single-premium immediate annuity that pays monthly income for as long as the policyholder lives, including the small but real number of policyholders who live past age 100. Harlan's manager signs the filing, but the supporting math carries Harlan's initials, and it is Harlan who has to explain any of it if a regulator's own actuary asks a question during review.

Highline must submit its statutory reserve basis for the Horizon Series to the state insurance department in **11 days** (SEE APPENDIX A). The basis is a single, filed methodology — Highline cannot submit two competing calculations and let the regulator pick one, and it cannot swap methods later without a full refiling.

Two methods are on the table.

**The Smooth Curve.** Highline's actuaries have a closed-form formula they have used for years: one smooth equation that estimates the dollar reserve required per $1,000 of promised benefit at any attained age, built to track the real published mortality data closely and to keep climbing gradually toward its long-run ceiling as age increases (SEE APPENDIX B). It is one line in a spreadsheet, it has never triggered a regulatory objection on any other Highline product, and it never has a break in it — it is a single smooth curve for every age from 0 to 120.

**The Full Table.** The alternative is to price every attained age directly off the actual published mortality table, exactly as printed — including the table's own closing convention at its oldest recorded age, where every survivor still living is treated as certain to die within that final interval (SEE APPENDIX C). It is slower to compute by hand, and it produces a number that jumps sharply at that boundary — which happens to be the exact age band where Highline's own block of Horizon Series contracts still has real survivors on the books this filing year (SEE APPENDIX D).

Both methods are legitimate starting points; nothing in Highline's filing rules requires one over the other. What differs is how each one treats a single attained age, and how much of Highline's in-force block sits exactly there. Background on both the industry's standard mortality tables and the mathematical model behind "smooth toward an asymptote" is in APPENDIX E. Every external source cited anywhere in this case is collected in APPENDIX G. The vocabulary and "how to…" skills this case asks you to research are listed in APPENDIX H — that is where Challenge 1 sends you.

---

## Dilemma

You are Harlan Voss.

Do you:

**A.)** Recommend **the Smooth Curve** — price every attained age with Highline's closed-form asymptotic formula **OR**

**B.)** Recommend **the Full Table** — price every attained age directly off the published mortality table, including its closing convention at the top

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A one-sided limit estimate from the real table.** Using the published mortality table in Appendix C, estimate the one-sided limit of the Full Table reserve function as attained age approaches 100 **from below**. Show the table values you used to make the estimate, and state your estimate in dollars per $1,000 of face value.
- **D2 — A limit evaluated algebraically from the equation.** Using the Smooth Curve formula in Appendix B, identify its horizontal asymptote directly from the equation (show your algebra), then evaluate the limit of the formula as attained age approaches 100 **algebraically** — not by estimating from a graph. State whether this limit equals the formula's actual value at age 100.
- **D3 — A continuity determination.** Using your results from D1 and D2, determine whether the Full Table reserve function is continuous at attained age 100. State the formal test you used (comparing the one-sided limit to the function's actual value there) and name the specific kind of discontinuity, if any. Then do the same test for the Smooth Curve formula at age 100, and say why the two functions come out differently.
- **D4 — The single-cohort dollar gap.** Compute the dollars of reserve required per $1,000 of face value, under each method, for a Horizon Series policyholder who is exactly attained age 100 this filing year. State the dollar gap and the percentage gap between the two methods **for that one age**.
- **D5 — The portfolio-wide margin.** Using Highline's Horizon Series in-force block in Appendix D, compute the blended dollars of reserve required per $1,000 of **total** face value in force, under each method, across the whole block. State the margin between the two methods as a percentage. Then state what share of the *total dollar difference* between the two methods comes from the single age-100 cohort alone.
- **D6 — An original visual.** Graph both reserve functions — the Smooth Curve formula and the Full Table function — for attained ages 85 through 105 on the same axes (by hand or with a graphing tool). Clearly mark the discontinuity in the Full Table function and the horizontal asymptote of the Smooth Curve formula. This satisfies Challenge 2(b).

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Filing Constraint

| Quantity | Value |
|---|---|
| Days remaining until Highline's statutory reserve filing is due | 11 |
| Number of competing reserve methodologies Highline may submit in one filing | 1 |
| Whether Highline may change methodology after the filing is approved without a full refiling | No |
| Horizon Series product type | Single-premium immediate annuity, lifetime income |
| Filing document Harlan's math supports | The actuarial memorandum accompanying the statutory reserve filing |

*Note: Highline Life & Annuity Company and the Horizon Series product are a scenario construction for this case — there is no real insurer by this name. The filing rule stated above (one methodology per filing, no mid-cycle swap) reflects standard actuarial filing practice and is used here as the case's hard constraint, not as a citation to any specific state's regulation.*

---

## Appendix B: The Smooth Curve — Formula and Derivation

Highline's Smooth Curve formula estimates the dollars of reserve required per $1,000 of face value, $C_A(x)$, at attained age $x$:

$$C_A(x) = 1000 - 851.8963 \cdot (0.973722)^{(x-90)}$$

*(Rounded to four and six decimal places respectively so the equation is easy to copy into a calculator; using these rounded coefficients reproduces every value in the table below to the penny.)*

**How this formula was built (see Modeling Assumptions, Appendix F, MA1 for the full account):** the formula is an exponential-approach-to-an-asymptote curve, calibrated so that it passes through the two real published data points at $x=90$ and $x=99$ from Appendix C, and set to approach a long-run asymptote of **$1,000 per $1,000 of face value** as $x \to \infty$ — the same ultimate number the Full Table converges to eventually, since every insured individual eventually dies with certainty. The formula assumes that ultimate value is approached *smoothly*, rather than reached abruptly at any single age.

| Attained age $x$ | $C_A(x)$, dollars per $1,000 face |
|---|---|
| 90 | 148.10 |
| 91 | 170.49 |
| 92 | 192.29 |
| 93 | 213.51 |
| 94 | 234.18 |
| 95 | 254.30 |
| 96 | 273.90 |
| 97 | 292.98 |
| 98 | 311.56 |
| 99 | 329.65 |
| 100 | 347.27 |
| 105 (for your D6 graph) | 428.64 |

The formula is defined and continuous for every real number $x$ except $x = -50$ (where the base exponential expression would require dividing by zero in an equivalent rational form) — far outside any attained age that matters to this case.

---

## Appendix C: The Full Table — U.S. Life Table, 2022

This is the real, published mortality table Highline's regulator would recognize as a legitimate valuation basis: **Table 1, "Life table for the total population: United States, 2022,"** from the CDC's National Vital Statistics Reports [S1]. $q_x$ is the probability that a person alive at exact age $x$ dies before reaching age $x+1$. The dollars of reserve required per $1,000 of face value under the Full Table method is $C_B(x) = 1000 \cdot q_x$.

| Attained age $x$ | $q_x$ | $C_B(x)$, dollars per $1,000 face |
|---|---|---|
| 90 | 0.148104 | 148.10 |
| 91 | 0.164457 | 164.46 |
| 92 | 0.181983 | 181.98 |
| 93 | 0.200630 | 200.63 |
| 94 | 0.220320 | 220.32 |
| 95 | 0.240942 | 240.94 |
| 96 | 0.262361 | 262.36 |
| 97 | 0.284411 | 284.41 |
| 98 | 0.306908 | 306.91 |
| 99 | 0.329650 | 329.65 |
| **100 and over** | **1.000000** | **1000.00** |

The last row is not a typo and it is not a rounding artifact — it is exactly how the source table defines it. The published table does not continue age-by-age past 99. Instead, everyone still alive at exact age 100 is grouped into a single open-ended interval, "100 and over," and by the definition of the table, the probability that a person in that open interval eventually dies **within that interval** is exactly 1 — because there is no higher age band left for them to be counted in. This is a standard, real convention for closing out the top of a published life table, not something specific to this case [S1].

*Source [S1]: National Center for Health Statistics, "United States Life Tables, 2022," National Vital Statistics Reports, Vol. 74, No. 2 (April 8, 2025), Table 1. Values above were read directly from the report's published data file: ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/74-02/Table01.xlsx, accessed 2026-08-18. Report: cdc.gov/nchs/data/nvsr/nvsr74/nvsr74-02.pdf.*

---

## Appendix D: Highline's Horizon Series In-Force Block

Highline's Horizon Series block, as of this filing year, has contracts still in force at each attained age from 90 through the open "100 and over" group. Each contract has a face value of $1,000 (SEE APPENDIX F, MA2, for how this block was built).

| Attained age $x$ | Contracts in force | Face value in force |
|---|---|---|
| 90 | 112 | $112,000 |
| 91 | 95 | $95,000 |
| 92 | 80 | $80,000 |
| 93 | 65 | $65,000 |
| 94 | 52 | $52,000 |
| 95 | 41 | $41,000 |
| 96 | 31 | $31,000 |
| 97 | 23 | $23,000 |
| 98 | 16 | $16,000 |
| 99 | 11 | $11,000 |
| **100 and over** | **8** | **$8,000** |
| **Total** | **534** | **$534,000** |

---

## Appendix E: The Real Industry Table and the Real Asymptotic Model

Two real, published facts sit behind this case's dilemma.

**The industry's own standard annuity mortality table has the same shape of problem.** U.S. life insurers pricing annuities generally use the Society of Actuaries' **2012 Individual Annuity Mortality (2012 IAM) Basic Table** — a published table covering ages 0 through 120 (SOA Table Identity 2581 for males, 2582 for females), publicly viewable at the SOA's own mortality table library [S3]. It was built by blending several different graduation methods across different age ranges rather than one formula for the whole table — which is exactly the kind of construction that can create a seam at the boundary between methods. This case uses the CDC's population life table (Appendix C) instead of reproducing the 2012 IAM Basic Table's own numbers, because this case's author could not independently verify specific digit-level values from the SOA table's interactive lookup tool; the CDC table is downloaded directly from a government data file and every value in Appendix C can be checked against that file. (SEE APPENDIX F, MA3.)

**The "smooth asymptotic" idea in the Smooth Curve formula is a real, named actuarial and demographic technique.** When statisticians need to model mortality at the very oldest ages — where raw death counts get too small to trust — the standard method is the **Kannisto model**, a logistic-curve formula for the force of mortality that is built to approach a fixed asymptote smoothly as age increases, rather than to keep changing shape forever. It is the method the Human Mortality Database itself uses to close out life tables at the oldest ages, and by design it is fit to, and applied for, ages above 95 [S4]. Highline's Smooth Curve formula in Appendix B is this same *style* of model — a smooth curve engineered to approach a fixed long-run value — applied here as a stated, illustrative version rather than a full statistical fit (SEE APPENDIX F, MA1).

The Society of Actuaries has also published real methodology guidance specifically on annuity reserving practice: the **"2012 Individual Annuity Reserving Report & Table"** (SOA Payout Annuity Table Team, September 28, 2011), prepared at the request of the NAIC's Life Actuarial Task Force to guide how the 2012 IAM table should be used for statutory annuity reserves [S2]. It establishes that the choice of *how* to apply a mortality table to reserving — not just *which* table — is a real, filed, professional decision, which is exactly the decision this case asks Harlan to make.

---

## Appendix F: Modeling Assumptions

> These figures and formulas are **not sourced** in the way Appendices C and E are. They are stated scenario assumptions chosen by the case author, built from real public data where possible. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value / method used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The Smooth Curve's specific formula parameters | $C_A(x) = 1000 - 851.8963(0.973722)^{(x-90)}$ — an exponential-approach-to-asymptote curve, asymptote fixed at $1{,}000, calibrated to pass exactly through the real published $C_B(90)$ and $C_B(99)$ values from Appendix C | No public source publishes a single firm's own closed-form mortality-smoothing formula (they are proprietary). The Kannisto model (Appendix E, [S4]) establishes that this general *style* of formula — a smooth curve approaching a fixed asymptote — is genuine, real, standard actuarial and demographic practice for old-age mortality. This case constructs one specific, worked example in that family, anchored to two real data points, rather than reproducing a real firm's proprietary parameters. | The case's central finding — that the Full Table has a boundary the Smooth Curve does not — holds for any smooth, boundary-free formula in this family, not just this exact one. Changing the calibration would shift the exact dollar figures in D2, D4, and D5 without changing which method is continuous at age 100. |
| MA2 | The size and shape of Highline's Horizon Series in-force block (Appendix D) | Contract counts by attained age are the real CDC survivorship values $l_x$ from Appendix C's source table, scaled down by a factor of 200 and rounded to whole contracts, to represent a plausible in-force block for a regional insurer | Highline is a fictional company; no real in-force block exists to cite. The *shape* of the age distribution (proportionally more contracts at younger attained ages, fewer at older ones) is built from real national survivorship data rather than invented outright, so the relative weighting between ages is grounded in a real source even though the absolute company size is a stated scenario choice. | The portfolio-wide margin in D5 is sensitive to this scaling — a block with proportionally more contracts exactly at "100 and over" would produce a larger margin; a block with fewer would produce a smaller one. |
| MA3 | Use of the CDC population life table (Appendix C) in place of the SOA 2012 IAM Basic Table's own values | All worked numbers in this case use CDC Table 1 (2022), not the SOA table | The SOA 2012 IAM Basic Table is real and public, but its specific $q_x$ digit values could not be independently verified from its interactive online lookup tool during research for this case. The CDC table is a direct government data-file download and every value in it is independently checkable. Both tables share the same real-world structural feature this case is built around: a published mortality table that stops publishing single-year rates at some top age and closes with a special convention there. | None — this is a substitution of dataset, not a numeric assumption that could flip the dilemma. |

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | U.S. total-population life table, $q_x$ by single year of age, ages 90–99, and the "100 and over" open-group closure convention ($q=1$) | See Appendix C table | National Center for Health Statistics (CDC), "United States Life Tables, 2022," *National Vital Statistics Reports* Vol. 74, No. 2 ([report PDF](https://www.cdc.gov/nchs/data/nvsr/nvsr74/nvsr74-02.pdf); [data file](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/74-02/Table01.xlsx)) | Published 2025-04-08 (2022 data year) | HIGH |
| S2 | Existence and purpose of a real, published SOA methodology report specifically on annuity reserving practice tied to the 2012 IAM table | "2012 Individual Annuity Reserving Report & Table," prepared for NAIC's Life Actuarial Task Force | Society of Actuaries, Payout Annuity Table Team ([soa.org](https://www.soa.org/resources/experience-studies/2011/2012-ind-annuity-reserving-rpt/)) | 2011-09-28 | HIGH |
| S3 | Existence, coverage (ages 0–120), and blended-graduation-method construction of the SOA 2012 Individual Annuity Mortality (2012 IAM) Basic Table | SOA Table Identity 2581 (male) / 2582 (female) | Society of Actuaries mortality table library ([mort.soa.org](https://mort.soa.org/ViewTable.aspx?TableIdentity=2581)) | Accessed 2026-08-18 | MEDIUM — public and real, but specific numeric $q_x$ digits from this table are **not** used anywhere in this case's calculations (see MA3) |
| S4 | The Kannisto model is a real, named, logistic-curve mortality model with a horizontal asymptote, standard practice for closing out life tables at the oldest ages (applied for ages above 95) | Definition and stated age range of application | Human Mortality Database, "Methods Protocol for the Human Mortality Database," v6 ([mortality.org](https://www.mortality.org/File/GetDocument/Public/Docs/MethodsProtocolV6.pdf)) | Accessed 2026-08-18 | HIGH |

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Limit
- Asymptote
- Continuity (Informal)
- Limit
- One-Sided Limit
- Continuity
- Discontinuity

**"How to…" questions**

- How to estimate a limit from a table or graph
- How to identify a vertical or horizontal asymptote from a function's equation
- How to evaluate a limit algebraically
- How to determine whether a function is continuous at a point

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
