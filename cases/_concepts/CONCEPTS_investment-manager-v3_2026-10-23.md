# Concepts — Investment-manager cases (v6, round-2 fixes and reshape) — 2026-10-23

**Supersedes** `CONCEPTS_investment-manager-v2_2026-10-23.md`. Round-1 and round-2 findings: `REVIEW_BRIEF_investment-manager_2026-10-23.md`. User instruction 2026-10-23: reshape C2, fix C1, run round 3.
**C3 (The Jackpot Choice) stays ON HOLD** (all round-1 reviewers recommend DROP; the user asked for it by name and has not confirmed a drop). Its implied-rate idea survives only as one optional closing question in C1.
**Data terms.** User instruction: *assume we meet Damodaran's usage terms.* Recorded as an assumption; his usage-rules page was not retrievable.
Every number below was recomputed from `histretSP.xls` (1928-2025, S&P 500 total return, 10-year T-bond, 3-month T-bill) in the session scratchpad; recompute from a fresh download in case-research.

| Concept | Domain | Score | Tier | Thin forced | Data | What changed |
|---|---|---|---|---|---|---|
| **C1 The Deferred Deal** | markets-investing | 9.6 | T4 | 6 | HIGH | one valuation date; rebalancing stated; balance table required; Madoff out of student text; roster-dollar stake; teacher reveal |
| **C2 The Average Lies** (was The Four Payments) | education-systems | 7.8 | T4 | 3 | HIGH | reshaped: the steady-return calculator vs history; new metrics; no scatter/correlation; sources fixed |

---

### C1 — The Deferred Deal   ·   score 9.6   ·   tier T4
**Protagonist.** Marcus Hale (fictional), finance director of the **Harbor City Gulls** (fictional club). The club has released an aging veteran but owes him his $5.9M salary for the 2000 season. The player's agent offers to be paid later, with interest. **Personally at stake:** the owner has told Hale that any shortfall in the deferred account comes out of the roster budget he controls. The 2000 league-minimum salary was about $200,000 (**scenario assumption; verify**); the deal's annual payment of $1,193,248 equals about **six minimum-salary players a year for 25 years**, and a $4.9M shortfall means finding about **$425,000 a year through 2035, two roster spots every season**.
**The dilemma.** A.) Pay the **$5.9M now** OR B.) Defer it at **8% interest** and repay in **25 equal payments** (the first 11 years later, the last 35 years after signing), investing the $5.9M under the club's **policy: 60% stocks / 40% 10-year Treasuries, rebalanced to 60/40 each January** (a stated constraint; other allocations appear as sensitivity).
**Timeline convention (stated).** To keep the arithmetic on one clock, the case invests on **January 1, 2000** and treats the first payment as due **January 1, 2011**, with each later payment on January 1. Both sides of the ledger are valued at the same date, January 1, 2011: the pool has earned the 11 calendar years **2000-2010**, and the debt has grown at 8% for 11 years. (The real first payment was July 1, 2011; the case says it is simplifying.)
**Primary metric.** Pool ratio on January 1, 2011 = value of the invested $5.9M divided by the **$13.757M** owed then. B beats A when the ratio is at least 1; A has no pool and no debt, so the comparison is the sign of the net position (stated plainly).
**Reproduction (computed).** $5.9M x 1.08^11 = **$13.757M**; the annuity-due payment on that at 8% is **$1.1932M** a year (the real figure is $1,193,248.20); 25 x that = **$29.83M**, the undiscounted total reported in the press.
**Why it's close (computed; 88 rolling 11-year windows of calendar years, 1928-2025).**
| Allocation | Pool at or above owed | Median pool / owed | 10th pct | 90th pct |
|---|---|---|---|---|
| **60/40, rebalanced (the club's policy)** | **52.3%** | **1.051** | 0.681 | 1.704 |
| 100% stocks (sensitivity) | 67.0% | 1.285 | 0.619 | 2.388 |
| 100% 10-year T-bond (sensitivity) | 20.5% | 0.655 | 0.523 | 1.158 |
(R1a: with buy-and-hold instead of annual rebalancing the 60/40 median is 1.085 and the share 53.4%; the case states rebalancing and shows this as a note.) At the club's policy the median outcome is **5%** above what is owed, a near coin flip with a wide spread: inside the ~20% balance rule. With 100% stocks it is 28.5%, outside it, which is why the allocation is policy and not a free choice.
**What actually happened (whole calendar years).** **2000-2010** at 60/40 returned **3.75% a year**: pool **$8.85M**, **$4.91M short**; at 100% stocks **0.39% a year**, pool $6.16M, $7.60M short; at 100% T-bonds 6.46%, pool $11.74M, $2.02M short. All three fell short of 8%. (The window one year later, 2001-2011, gives 60/40 4.33%, pool $9.41M, $4.35M short; same conclusion.)
**Independence lesson.** The 88 overlapping windows are really **8 non-overlapping 11-year blocks**. The number at or above 8% depends on where the blocks start: at 60/40 it ranges **3 to 5 of 8** (37.5-62.5%) across start years 1928-1938; for 100% stocks **4 to 7 of 8** (50-87.5%).
**Deliverables -> skills (D2 is now a required balance table, so recursion and the closed form are forced, not optional):**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D1 $5.9M x 1.08^11 = $13.757M |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D1/D3/D5 interest, ratios, shares |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D2 the deferred account as a recursion |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D2 balance(t+1) = 1.08 x (balance(t) - payment(t)), a year-by-year table 2000-2035 |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D2 derive the closed form for the balance and solve for the payment that leaves exactly $0 after 2035 |
| calculus-sequence | term | Sequence | 3 ◀ thin | D2 the 25 payments and the balance sequence |
| calculus-series | term | Series | 2 ◀ thin | D2 check the payment with the finite geometric-series formula |
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin | D3 box plot of the 88 rolling 11-year pool ratios at 60/40 |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin | D3 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin | D3 |
| statistics-and-probability-median | term | Median | 8 | D3 |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D4 mean of the non-overlapping blocks |
**The reveal (an optional, teacher-read paragraph at the end of the student text).** *"The numbers in this case come from a real deal. In January 2000 a New York baseball club released outfielder Bobby Bonilla but still owed him $5.9 million for the season. The two sides agreed to defer the money at 8% interest. Starting in 2011, and every July 1 through 2035, the club sends him a check for $1,193,248.20. Check your answer to D2 against that number."* No fraud story, no owner named.
**Appendix for the facilitator (not student-facing).** Sources, labeled "reported": CBS Sports (cbssports.com/mlb/news/bobby-bonilla-day-why-the-mets-still-owe-former-mlb-all-star-more-than-1m-per-year-on-july-1/); ESPN 2024 (espn.com/mlb/story/_/id/40430232/...); CBS 2013 ("precisely 8 percent," and the proposer dispute: one report says the club proposed the deferral, the player's agent says it was the club's idea; reports differ). The $29.8M cited by outlets is the sum of the 25 payments, not a grown balance. No primary contract text was found. Bonilla also has a second reported deferral whose counterparty and end year (2028 vs 2029) conflict across sources; the case does not use it. **Facilitator-only fraud note:** reporting says the real club's ownership was invested with Bernard Madoff, who pleaded guilty on March 12, 2009 and was sentenced to 150 years on June 29, 2009, and that the owners agreed in 2012 to pay up to $162 million to the trustee while insisting they knew nothing of the fraud (NBC News; AP). None of this appears in student text; no owner is named.
**Optional closing question.** Powerball's cash option is the prize-pool amount needed to fund a 30-payment annuity whose payments rise 5% a year (powerball.com/faqs; both options are before tax). Solving for the interest rate gives **4.87%** for the December 24, 2025 draw ($1.817B advertised, $834.9M cash). "Is that jackpot paying like a 4.9% bond, and how does it compare with the 8% in this case?" One question, no second dataset.
**Data feasibility: HIGH.** Damodaran file (usage terms assumed met per the user; the "date updated" cell is stale but the 2025 row is complete). Contract facts are secondary-sourced and labeled reported.
**Sensitivity (SPEC §6).** None in student text; facilitator note on financial fraud (above).
**Split risk.** NONE (12 skills).

### C2 — The Average Lies   ·   score 7.8   ·   tier T4
**Protagonist.** Ayo Bankole (fictional), a planner at a credit-union advice desk, and **Mara**, the granddaughter (fictional, a high-school freshman, who sits in every meeting). A grandmother has given the family **$50,000** for Mara's **four years of in-state public college tuition and fees**, starting in five years; she wants **whatever is left over** to go toward Mara's graduate school. Personally at stake: Mara's first bill lands five years from now, and the family cannot make up a shortfall.
**The hook.** Every online college-savings calculator asks for one number: an assumed **steady annual return**. Ayo runs it. The calculator says the family needs far less than the grandmother gave. The case asks whether that is true.
**The dilemma (asset allocation).** A.) A **70% stocks / 30% bonds** mix, held to the last bill (the more growth, the larger the leftover for graduate school) OR B.) A **30% stocks / 70% bonds** mix (the safer path to all four bills).
**Setup (sourced).** Tuition and fees, in-state public four-year, 2025-26: **$11,950**, sticker price (College Board, *Trends in College Pricing 2025*, `research.collegeboard.org/trends/college-pricing/highlights`). Net tuition and fees for first-time full-time in-state students is an estimated $2,300 in 2025 dollars; sticker is the conservative planning input. **Scope:** tuition and fees only (the in-state budget including housing and food is $30,990 a year; not modeled). The bills grow at a stated rate and are due at the **start** of years 6, 7, 8 and 9 from today (annuity-due timing, as in Gao): at 3.5% growth, about $14,193, $14,690, $15,204, $15,736, **total $59,822**. **Growth rate:** a derived estimate, not a College Board headline. Endpoints give **2.4% a year over ten years** ($9,410 for 2015-16 to $11,950 for 2025-26 = 2.42%); a 20-year rate is **unverified** (compute from the College Board Excel series). The case uses 3.5% and shows 2.4% and 4.0%; 4.0% is flagged as an unverified upper case.
**Primary metric.** The **smallest lump sum that pays all four bills in full in at least 95% of historical 9-year windows** (the family's stated "high degree of certainty," shown also at 90 and 100%). **Balance, stated as an explicit trade-off (R1a):** B wins this metric (it needs less) but A wins the second axis the grandmother values, the leftover. Neither dominates.
| Reliability target | Smallest lump sum, A (70/30) | Smallest lump sum, B (30/70) | B needs less by |
|---|---|---|---|
| 90% | $48,159 | $46,177 | 4.1% |
| **95%** | **$53,722** | **$49,813** | **7.3%** |
| 100% | $68,499 | $53,918 | 21.3% |
At the grandmother's **$50,000**: A pays all four bills in **92.2%** of the 90 windows (fails in 7), B in **96.7%** (fails in 3); median leftover **$36.7K (A)** vs **$15.5K (B)** (failures counted as $0); the largest total unpaid is about **$21,100 (A)** vs **$4,900 (B)** (defined as the sum of unpaid bills at their due dates; one reviewer's different timing convention gave about $22,400 for A: reconcile in research).
**The calculator vs history (the new heart of the case; computed).** The calculator's steady rate is each mix's own 1928-2025 average annual return, the **geometric mean: A 8.83%, B 6.63%** (the arithmetic mean, 9.75% and 6.93%, is a sensitivity). The closed-form lump sum for the four bills at that rate (a finite geometric series):
| | Calculator lump sum (geometric mean) | Share of historical windows in which that lump sum pays all four bills | Lump sum for 95% reliability | **Planning gap** |
|---|---|---|---|---|
| A (70/30) | **$34,545** | **54.4%** | $53,722 | **+$19,177 (+56%)** |
| B (30/70) | **$39,417** | **36.7%** | $49,813 | **+$10,396 (+26%)** |
**The calculator reverses the ranking.** It says A is cheaper ($34.5K vs $39.4K); history says B is cheaper at every reliability target above 85% (at 85% they tie). A plan built on the average funds the family only **54% of the time** with the stock-heavy mix and **37%** with the bond-heavy one. Why: returns bounce around, and **the order of returns matters once money is being withdrawn**. The case's sequence experiment (computed): of the **7 windows** in which A fails at $50,000, running the very same returns in **reverse order** makes **6 of the 7 pay all four bills**; of B's 3 failures, **all 3** pay. Same returns, same average, different order, different result. That is Gao's third structure.
**Break-even funding (a band, not a point; computed).** The two mixes pay all four bills equally often at a lump sum of about **$42,100 at 2.4% growth, $45,200 at 3.5%, and $46,600 at 4.0%** (the first dollar level from which B ties or leads and stays ahead; the curves cross within a band of roughly $1,000 because there are only 90 windows). Below it the stock-heavy mix gives better odds; above it the bond-heavy mix does. The grandmother's $50,000 sits above it.
**Independence lesson.** 90 overlapping windows are about **10 independent 9-year blocks**.
**Deliverables -> skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| calculus-sequence | term | Sequence | 3 ◀ thin | D1 four tuition bills growing at a stated rate |
| calculus-series | term | Series | 2 ◀ thin | D2 the calculator: lump sum at a steady return, a finite geometric series |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D3 balance(t+1) = (balance(t) - bill(t)) x (1 + return(t)) for each historical window |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D3 |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D3 with a steady return, the recursion collapses to the D2 closed form: show they match |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D2 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D5 planning gap as a percent |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 44 | D4 share of windows in which the calculator plan pays all four bills |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D2/D6 average return of each mix; same average, different order |
Removed from v2: scatter plot and correlation (R1a: the 2000 split is post hoc and n=26; R1c: not needed). The stock-bond relationship may appear as an optional discussion after D6, not a forced skill. For the record: the correlation of +0.15 (1928-1999, n=72) vs -0.37 (2000-2025, n=26) differs at the 5% level (Fisher z about 2.2, p about 0.03), but the split is chosen after the fact.
**D6 (discussion, not a graded skill).** Same average return, different order: show the reversed-order experiment above and ask what a calculator hides.
**Data feasibility: HIGH.** Damodaran file (usage terms assumed met per the user); College Board highlights page (confirmed).
**Facilitator-only legal/tax note.** $50,000 exceeds the 2026 annual gift-tax exclusion of $19,000 per recipient (IRS gift-tax FAQ, confirmed); the exclusion for tuition paid directly to a school (26 CFR 25.2503-6; verify) does not cover a lump sum given to a family; the FAFSA treatment of grandparent-owned 529 plans changed (secondary source only; verify on studentaid.gov). The case models a gift, not tax advice.
**Domain.** `education-systems`.
**Sensitivity (SPEC §6).** Facilitator note: family money stress; some students' families carry college debt or have no college fund.
**Split risk.** NONE (9 skills).

### C3 — The Jackpot Choice   ·   ON HOLD
All round-1 reviewers: DROP as a standalone binary (cash dominates for any stock-heavy winner unless an invented "certainty mandate" is imposed; the annuity-due math duplicates C1). Awaiting the user's decision. Only the closing question above survives in C1.
