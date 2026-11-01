# Concepts — Investment-manager cases (v5, revised after R1 round 1) — 2026-10-23

**Supersedes** C1 and C2 in `CONCEPTS_investment-manager_2026-10-23.md`; the round-1 findings are in `REVIEW_BRIEF_investment-manager_2026-10-23.md`.
**C3 (The Jackpot Choice) is ON HOLD.** All three reviewers recommend DROP (cash dominates unless an invented "certainty mandate" is imposed; math redundant with C1). The user asked for it by name, so the drop awaits the user's confirmation; its one new finding (the cash option's implied discount rate, 2.84% in Jan 2016 to about 4.9% in Dec 2025) is offered here as a C1 extension.
**Data terms.** User instruction 2026-10-23: *assume we meet Damodaran's usage terms.* The reviewers could not retrieve his usage-rules page, so this is an assumption, not a verified fact; it is recorded here.
All numbers recomputed from `histretSP.xls` (1928-2025) in the session scratchpad; recompute from a fresh download in case-research.

| Concept | Domain | Score | Tier | Thin forced | Data | Round-1 findings addressed |
|---|---|---|---|---|---|---|
| **C1 The Deferred Deal** | markets-investing | 9.6 | T4 | 6 | HIGH | allocation fixed, alignment, blocks range, sources, names, Madoff wording, stake |
| **C2 The Four Payments** | education-systems | 10.4 | T3 | 3 | HIGH | funding break-even, A's reason, scope, growth rate, gift note, correlation downgraded |

---

### C1 — The Deferred Deal   ·   score 9.6   ·   tier T4
**Protagonist.** Marcus Hale (fictional), finance director of the **Harbor City Gulls** (fictional club), January 2000. The club has released an aging veteran but still owes his 2000 salary of **$5.9M**. His agent offers to be paid later, with interest. **Personally at stake:** in July 2011 the club also owes its first payment on a new stadium loan; if the deferred pool falls short, the club must raise ticket prices or cut payroll that summer, and Hale signs the plan.
**The dilemma.** A.) Pay the **$5.9M now**, in 2000 OR B.) Defer it at **8% interest**, repaid in **25 equal payments from July 2011 to July 2035**, and invest the $5.9M under the club's **investment policy: at most 60% equities, the rest in 10-year Treasuries (a 60/40 mix)**. (The allocation is a stated constraint of the club, not a student choice; other allocations appear as sensitivity.)
**Primary metric.** Pool ratio in 2011 = value of the invested $5.9M divided by the **$13.757M** owed then. B beats A when the ratio is at least 1 (A has no pool and no debt; the comparison is the sign of the net position, stated plainly).
**Real analogue (appendix, sourced and labeled "reported").** The case is modeled on a real 2000 deal, Bobby Bonilla and the Mets: released in January 2000 with $5.9M of salary still owed; deferred at 8% over 25 years from 2011; **$1,193,248.20 each July 1**. The case's overview names no real person or club. Appendix sources: CBS Sports (cbssports.com ... bobby-bonilla-day...), ESPN, CBS 2013 ("precisely 8 percent"). Stated conflicts: who proposed the deferral (a 2013 report says the Mets proposed it; the player's agent says it was the Mets' idea; reports differ), which of Bonilla's two deferrals the case uses (this one: $5.9M, 2011-2035; the second is $500K a year 2004-2028), and that terms are reported, not read from a contract. The $29.8M figure quoted by outlets is the **undiscounted sum of the 25 payments**, not a grown balance. If the appendix mentions the owners' Madoff investments, it states only what is reported (they were invested with Bernard Madoff; the ESPN 2024 account says an account "promised double-digit returns"; Madoff pleaded guilty and was sentenced in 2009; in 2012 the owners settled the trustee's suit for $162M and denied wrongdoing) and attributes no motive to any person.
**The math reproduces (computed).** $5.9M x 1.08^11 = **$13.757M**; an annuity due of 25 payments at 8% worth $13.757M pays **$1.1932M** a year; 25 x that = **$29.83M**. Students rebuild the real figure from two facts.
**Why it's close (computed, 88 overlapping 11-year windows, 1928-2025).**
| Allocation | B ends at or above what's owed | Median pool / owed | 10th percentile | 90th percentile |
|---|---|---|---|---|
| **60/40 (the club's policy)** | **52.3%** | **1.051** | 0.681 | 1.704 |
| 100% stocks (sensitivity) | 67.0% | 1.285 | 0.619 | 2.388 |
| 100% 10-year T-bond (sensitivity) | 20.5% | 0.655 | 0.523 | 1.158 |
At the club's 60/40 policy, the median outcome is **5%** above the amount owed, a coin flip with a wide spread (10th to 90th percentile: 0.68 to 1.70). That sits well inside the ~20% balance rule. With 100% stocks the median is 28.5% above, outside it, which is why the allocation is fixed by policy; students may vary it and see the margin move.
**What actually happened, and the alignment caveat.** The real window ran about **July 2000 to July 2011**; the case uses whole calendar years. **2000-2010** at 60/40 returned **3.75%/yr** (pool $8.85M, net -$4.91M); **2001-2011**: 4.33%/yr (pool $9.41M, net -$4.35M). Both shown; the conclusion is the same. "One of the worst stretches on record" is dropped as unverified; the case says only that both windows fell well short of 8%.
**Independence lesson.** 88 overlapping windows are really **8 non-overlapping 11-year blocks**. The number of blocks at or above 8% depends on where the blocks start: at 60/40 it ranges **3 to 5 of 8** (37.5-62.5%) across start years 1928-1938; for 100% stocks **4 to 7 of 8** (50-87.5%). Students find the range.
**Extension (not counted): the jackpot's hidden rate.** Powerball's cash option is the prize-pool amount needed to fund a 30-payment annuity whose payments rise 5% a year; solving for the interest rate gives **4.87%** for the Dec 2025 draw ($1.817B advertised, $834.9M cash) and 2.84% for Jan 2016, rising and falling roughly with 30-year Treasury yields. Students compare it to the Mets' 8%. (Source: powerball.com FAQ and draw pages; to verify.)
**Deliverables -> skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D1 $5.9M x 1.08^11 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D1/D3 interest, shares, ratios |
| calculus-series | term | Series | 2 ◀ thin | D2 PV of 25 payments as a finite geometric series |
| calculus-sequence | term | Sequence | 3 ◀ thin | D2 the 25 payments and their discount factors |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D2 balance(t+1) = 1.08 x (balance(t) - payment) |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D2 closed form, then solve for the payment |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D2 |
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin | D3 box plot of 88 rolling 11-year 60/40 outcomes |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin | D3 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin | D3 |
| statistics-and-probability-median | term | Median | 8 | D3 |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D3 mean of the non-overlapping blocks |
**Data feasibility: HIGH.** Damodaran, *Historical Returns on Stocks, Bonds and Bills 1928-2025* (`stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls`; the file's "date updated" cell is stale but the 2025 row is complete); usage terms assumed met per the user. Contract facts: reported by multiple outlets; no primary text found.
**Sensitivity (SPEC §6).** Facilitator note on financial fraud (Madoff, appendix only). No living person is named in the overview.
**Split risk.** NONE (12 skills).

### C2 — The Four Payments   ·   score 10.4   ·   tier T3
**Protagonist.** Ayo Bankole (fictional), a planner at a credit-union advice desk. A grandmother has given her granddaughter's family **$50,000** to pay **four years of in-state public college tuition and fees**, starting in five years. The grandmother also wants **whatever is left over** to go toward the granddaughter's graduate school. Personally at stake: the first bill lands five years from now, after the market has either helped or hurt, and the family cannot make up a shortfall.
**The dilemma (asset allocation).** A.) A **70% stocks / 30% bonds** mix, held to the last bill: the more growth, the larger the leftover for graduate school OR B.) A **30% stocks / 70% bonds** mix: the safer path to all four bills.
**Primary metric.** The **smallest lump sum** that pays all four bills in full in at least **95%** of historical 9-year windows. (A quantile, as in the Compact; the 95% reliability target is the family's stated risk tolerance, Gao's "high degree of certainty," and is shown at 85, 90, 95 and 100%.)
**Setup.** Tuition and fees, in-state public four-year, 2025-26: **$11,950** (College Board *Trends in College Pricing 2025*, confirmed by R1b on the College Board page; **sticker price, not net**; net is an estimated $2,300 in 2025 dollars, so sticker is the conservative planning input). The bills grow at a stated rate and are paid at the **start** of years 6, 7, 8, 9 (annuity-due timing, as in Gao). **Scope:** tuition and fees only (the College Board in-state budget with housing and food is $30,990 a year; the case says so and does not model it). Growth rate: College Board's own series shows real published prices falling about 7% over 2015-25; a CPI-deflated derivation gives about **2.4% a year nominal over 10 years and about 4.0% over 20**; the case uses **3.5%** and shows 2.4% and 4.0%.
**Computed from 1928-2025 data (90 overlapping 9-year windows; bills total $59,822 at 3.5%).**
| Reliability target | Smallest lump sum, 70/30 (A) | Smallest lump sum, 30/70 (B) | B needs less by |
|---|---|---|---|
| 85% | $45,471 | $45,245 | 0.5% |
| 90% | $48,159 | $46,177 | 4.1% |
| **95%** | **$53,722** | **$49,813** | **7.3%** |
| 100% | $68,499 | $53,918 | 21.3% |
**The funding break-even (a deliverable, not a hidden parameter).** The two mixes pay all four bills equally often at a lump sum of about **$45,000-$46,000**; below it the stock-heavy mix gives better odds, above it the bond-heavy mix does. At the grandmother's **$50,000**: A pays all bills in **92.2%** of windows, B in **96.7%**. The break-even is about **$43K at 2.4% growth, $45K at 3.5%, $46K at 4.0%**, so it is stable. Students find it, and see the $50,000 sits just above it.
**Why it's close.** At 95% reliability B needs 7% less money, a small margin. But A leaves a **median $36.7K** over at $50,000 (B: $15.5K, with failures counted as $0), which is exactly the money the grandmother wants for graduate school; B almost never fails (worst shortfall $4.9K against $21.1K for A). The family must decide how much certainty the first four bills deserve compared with the leftover. That is the Gao liability-first question in a family's hands.
**Independence lesson.** 90 overlapping windows are about **10 independent 9-year blocks**.
**The diversification discussion (not a claim).** Students plot all 98 years of stock vs bond returns and describe the relationship: correlation is **+0.15 for 1928-1999 (n=72) and -0.37 for 2000-2025 (n=26)**; bonds rose 20.1% in 2008 when stocks fell 36.6%; in 2022 both fell. The deliverable asks them to say what 26 years can and cannot show (the two correlations are not significantly different), not to assert that bonds protect.
**Deliverables -> skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| calculus-sequence | term | Sequence | 3 ◀ thin | D1 four tuition bills growing at a stated rate |
| calculus-series | term | Series | 2 ◀ thin | D2 lump sum needed at a steady return, by closed-form geometric series |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D3 balance(t+1) = (balance(t) - bill(t)) x (1 + return) |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D3 |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D1/D2 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D4 allocation weights |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 44 | D4 share of windows with all bills paid |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D4 weighted portfolio return |
| statistics-and-probability-scatter-plot | term | Scatter Plot | 10 | D5 stock vs bond returns, 98 years |
| statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data | how-to | How to create a scatter plot given a set of data | 12 | D5 |
| statistics-and-probability-correlation | term | Correlation | 5 | D5 describe the relationship in two eras, and say what n=26 can and cannot show |
| statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data | how-to | How to identify correlation given a scatter plot or set of data | 5 | D5 |
**Data feasibility: HIGH.** Damodaran file (usage terms assumed met per the user); College Board *Trends in College Pricing* (`research.collegeboard.org/trends/college-pricing/highlights`, confirmed).
**Legal/tax note for the facilitator, not student text.** $50,000 exceeds the 2026 annual gift-tax exclusion of $19,000 per recipient (the excess needs a gift-tax return); tuition paid directly to a school is exempt, but a lump sum to a family is not; FAFSA treatment of grandparent-owned 529 plans changed; verify on IRS.gov and studentaid.gov before publishing any advice-like statement. The case models a gift, not tax advice.
**Domain.** `education-systems` (4 existing, MEDIUM priority).
**Sensitivity (SPEC §6).** Facilitator note: family money stress; some students' families carry college debt or have no college fund.
**Split risk.** NONE (12 skills).

### C3 — The Jackpot Choice   ·   ON HOLD
Unchanged from the prior sheet. All three reviewers: DROP as a standalone. Awaiting the user's decision.
