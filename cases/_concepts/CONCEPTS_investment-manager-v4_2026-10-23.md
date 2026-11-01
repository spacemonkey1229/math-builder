# Concepts — Investment-manager cases (v7, round-3 fixes) — 2026-10-23

**Supersedes** `CONCEPTS_investment-manager-v3_2026-10-23.md`. Findings and fixes: `REVIEW_BRIEF_investment-manager_2026-10-23.md` (rounds 1-3).
**Renamed:** C1 is now **The Eight-Percent Bet** (the old title was one word from the published case "The Deferred Repair").
**C3 (The Jackpot Choice) stays ON HOLD** pending the user's decision; its implied-rate idea survives only as one optional closing question in C1.
**Data terms.** User instruction: *assume we meet Damodaran's usage terms.* Recorded as an assumption; his usage-rules page was not retrievable.
Every stock/bond figure was recomputed from `histretSP.xls` (1928-2025; S&P 500 total return, 10-year T-bond, 3-month T-bill) in the session scratchpad; recompute from a fresh download in case-research.

| Concept | Domain | Score | Tier | Thin forced | Data |
|---|---|---|---|---|---|
| **C1 The Eight-Percent Bet** | markets-investing | 9.6 | T4 | 6 | HIGH |
| **C2 The Average Lies** | education-systems | 7.8 | T4 | 3 | HIGH |

**Batch notes for the facilitator guide.** (1) C1 and C2 look like they teach opposite lessons from the same data: in C1 stocks help a pool *reach a target while saving*; in C2 bonds help a fund *pay bills while withdrawing*. The guide names this contrast. (2) The Damodaran table is also cited by the published case `the-quiet-thief`; three corpus items use it. (3) C1 and C2 share the rolling-window engine and an allocation question; they differ in question, metric and lesson (C1: does a deferral beat 8%? C2: what does a steady-return calculator hide?). (4) markets-investing becomes a fifth case in a LOW-priority domain; the user asked for these cases; add no further finance cases. (5) `domain_coverage.json` is a 2026-09-14 snapshot; re-tally before approval.

---

### C1 — The Eight-Percent Bet   ·   score 9.6   ·   tier T4
**Protagonist.** Marcus Hale (fictional), finance director of the **Harbor City Gulls** (fictional club). The club has released an aging star but owes him his $5.9M salary for the 2000 season. The player's agent offers to be paid later, with interest.
**Personally at stake (stated carefully).** If the invested money falls short, **the pool pays the checks first and the roster budget Hale controls covers only the shortfall**; if it ends with a surplus, **the club keeps the surplus** (it becomes player-development money). The league-minimum salary in 2000 was **$200,000** (the lowest a major-league team could pay one player; FanGraphs, Baseball Almanac). The deal's payment of $1,193,248 a year equals about six such players; a **$4.9M shortfall at the start of 2011** means finding about **$425,000 a year for 25 years, two roster spots every season**.
**The dilemma.** A.) Pay the **$5.9M now** OR B.) Defer it at **8% interest** and repay in **25 equal payments** (the first 11 years later, the last 35 years after signing), investing the $5.9M under the club's **policy: 60% stocks / 40% 10-year Treasuries, rebalanced to 60/40 each January** (a stated constraint; other allocations appear as sensitivity).
**Timeline convention and what is tested (stated in student text).** The case invests on **January 1, 2000** and treats the first payment as due **January 1, 2011**, each later payment on January 1 (the real first payment was July 1, 2011; the case simplifies). Both sides are valued on **January 1, 2011**: the pool has earned the 11 calendar years **2000-2010**, and the debt has grown at 8% for 11 years. **This is a one-date snapshot**; it does not follow the pool through 2011-2035. If the pool is short on that date, the case assumes the club funds the gap in equal yearly amounts over the 25 payments **at 8%** (the rate the debt grows). That is where $425K a year comes from ($4.91M divided by the annuity-due factor 11.53).
**Student-chosen assumption (T4).** In D6 the student chooses and defends **how the pool should be invested after 2011** (keep 60/40, move to Treasuries, other) and what happens to a surplus or a shortfall; the 8% funding rate above is a stated default the student may change.
**Primary metric.** Pool ratio on January 1, 2011 = value of the invested $5.9M divided by the **$13.757M** owed then. B beats A when the ratio is at least 1; A has no pool and no debt, so the comparison is the sign of the net position (stated plainly).
**Reproduction (computed).** $5.9M x 1.08^11 = **$13.757M**; the annuity-due payment on that at 8% is **$1.1932M** a year (the real figure is $1,193,248.20; R1b recomputed it exactly); 25 x that = **$29.83M**, the undiscounted total reported in the press.
**Why it's close (computed; 88 rolling 11-year windows of calendar years, 1928-2025).**
| Allocation | Pool at or above owed | Median pool / owed | 10th pct | 90th pct |
|---|---|---|---|---|
| **60/40, rebalanced (the club's policy)** | **52.3%** | **1.051** | 0.681 | 1.704 |
| 100% stocks (sensitivity) | 67.0% | 1.285 | 0.619 | 2.388 |
| 100% 10-year T-bond (sensitivity) | 20.5% | 0.655 | 0.523 | 1.158 |
(With buy-and-hold instead of annual rebalancing the 60/40 median is 1.085 and the share 53.4%; the case states rebalancing and shows this as a note.) At the club's policy the median outcome is **5%** above what is owed: a near coin flip with a wide spread, inside the ~20% balance rule. With 100% stocks it is 28.5%, outside it, which is why the allocation is policy and not a free choice.
**What actually happened (whole calendar years).** **2000-2010** at 60/40 returned **3.75% a year**: pool **$8.85M**, **$4.91M short**; at 100% stocks **0.39% a year**, pool $6.16M, $7.60M short; at 100% T-bonds 6.46%, pool $11.74M, $2.02M short. All three fell short of 8%. (2001-2011 at 60/40: 4.33%, pool $9.41M, $4.35M short.)
**Independence lesson.** The 88 overlapping windows are really **8 non-overlapping 11-year blocks**; the number at or above 8% depends on where the blocks start: at 60/40 **3 to 5 of 8** (37.5-62.5%), for 100% stocks **4 to 7 of 8** across start years 1928-1938.
**Deliverables -> skills (D2 requires the balance table and the written 25-term sum, so recursion, the closed form and the series are all forced):**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D1 $5.9M x 1.08^11 = $13.757M |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D1/D3 interest, ratios, shares |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D2 the deferred account as a recursion |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D2 balance(t+1) = 1.08 x (balance(t) - payment(t)), a year-by-year table 2000-2035 |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D2 derive the closed form for the balance and solve for the payment that leaves exactly $0 after 2035 |
| calculus-sequence | term | Sequence | 3 ◀ thin | D2 the 25 payments and the balance sequence |
| calculus-series | term | Series | 2 ◀ thin | D2 write the sum of the 25 discounted payments term by term, then collapse it with the geometric-series formula and compare with the table |
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin | D3 box plot of the 88 rolling 11-year pool ratios at 60/40 |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin | D3 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin | D3 |
| statistics-and-probability-median | term | Median | 8 | D3 |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D4 mean of the non-overlapping blocks |
**The reveal (an optional, teacher-read paragraph after the student text).** *"The numbers in this case come from a real deal. In 2000 a New York baseball club still owed former All-Star Bobby Bonilla $5.9 million of salary for that season. The two sides agreed to defer the money at 8% interest. Starting July 1, 2011, and every July 1 through 2035, the club pays him $1,193,248.20. Check your answer to D2 against that number. (This case moved the first payment to January 1 to keep the clock simple.)"* No fraud story, no owner named.
**Appendix for the facilitator (not student-facing; terms "reported").** Sources: CBS Sports 2026 (`cbssports.com/mlb/news/bobby-bonilla-day-why-the-mets-still-owe-former-mlb-all-star-more-than-1m-per-year-on-july-1/`: $5.9M, 8%, 25 years, $1,193,248.20 each July 1 through 2035); ESPN 2024 (`espn.com/mlb/story/_/id/40430232/`, Dan Mullen: "In 2000, the Mets agreed to buy out the remaining $5.9 million"); Jon Heyman, CBS 2013 (`cbssports.com/mlb/news/what-you-dont-know-about-bonilla-and-saberhagen-mets-deals`: the club suggested deferring; the player's agent says "They came to us. It was their idea."; the rate was "precisely 8 percent"). Release timing varies by source (after the 1999 season vs January 2000), so the case says "in 2000." The $29.8M quoted in the press is the **undiscounted sum of the 25 payments**, not a grown balance. No primary contract text was found. A separate second reported deferral ($500,000 a year, 2004-2028, with the Orioles per CBS 2026) is not used. **Facilitator-only note on financial fraud.** Reporting says the real club's ownership had money with Bernard Madoff, who pleaded guilty on March 12, 2009 and was sentenced to 150 years on June 29, 2009 (ABC News; KPBS). NBC News reports the owners reached a settlement with the trustee in 2012 "agreeing to pay $162 million" (`nbcnews.com/business/markets/mets-owners-madoff-trustee-settle-162-million-flna484802`); JTA reports that lawyers for the owners "said their clients had no idea the investments were fraudulent" (`timesofisrael.com/mets-owners-settle-lawsuit-in-madoff-ponzi-scheme/`). None of this appears in student text; no owner is named.
**Optional closing question.** Powerball's cash option is the prize-pool amount needed to fund a 30-payment annuity whose payments rise 5% a year; both options are before tax (`powerball.com/faqs`). Solving for the interest rate gives **4.87%** for the December 24, 2025 draw ($1.817B advertised, $834.9M cash; a powerball.com page and lottonumbers.com agree on the cash figure; re-verify the draw page). "Is that jackpot paying like a 4.9% bond, and how does it compare with the 8% in this case?" One question, no second dataset.
**Data feasibility: HIGH.** Damodaran file (usage terms assumed met per the user). Contract facts are secondary-sourced.
**Sensitivity (SPEC §6).** None in student text; facilitator note above.
**Split risk.** NONE (12 skills).

### C2 — The Average Lies   ·   score 7.8   ·   tier T4
**Protagonist.** Ayo Bankole (fictional), a planner at a credit-union advice desk, and **Mara**, the granddaughter (fictional, a high-school freshman, who speaks in the meeting). A grandmother has given the family **$50,000** for Mara's **four years of in-state public college tuition and fees**, starting in five years; she wants **whatever is left over** to go toward Mara's graduate school.
**Mara's lines (student text).** *"What if the market drops the year before I start?"* · *"If there's money left, can it pay for grad school?"* · *"The calculator says we have plenty. Why are you still worried?"*
**The hook.** Every online college-savings calculator asks for one number: an assumed **steady annual return**. Ayo runs it. The calculator says the family needs far less than the grandmother gave. The case asks whether that is true.
**The dilemma (asset allocation).** A.) A **70% stocks / 30% bonds** mix, held to the last bill OR B.) A **30% stocks / 70% bonds** mix.
**Primary metric.** The **share of historical 9-year windows in which all four bills are paid in full** at the grandmother's **$50,000**. **Second axis (symmetric):** the share of windows in which the family also has at least **$20,000 left** at the end of year 9. Neither mix dominates:
| At $50,000, 3.5% tuition growth (90 windows) | A (70/30) | B (30/70) |
|---|---|---|
| All four bills paid | **92.2%** (fails in 7) | **96.7%** (fails in 3) |
| Bills paid **and** at least $20,000 left | **64.4%** | 34.4% |
| Median leftover (failures counted as $0) | **$36.7K** | $15.5K |
Leftover threshold sensitivity (bills paid and at least this much left): **$10K** A 80.0% / B 73.3%; **$20K** A 64.4% / B 34.4%; **$30K** A 56.7% / B 21.1%. The pattern (B safer, A richer) holds at tuition growth of 2.4% and 3.97% (the measured band).
**Student-chosen assumptions (T4).** The student chooses and defends (a) the **tuition growth rate** within the measured band **2.40% to 3.97% a year** and (b) how much **leftover** is worth wanting (the threshold above), and tests the funding levels below.
**Setup (sourced, confirmed by R1b).** College Board *Trends in College Pricing 2025* (Excel data, Table CP-4, in-state public four-year tuition and fees, current dollars): **2005-06 $5,490; 2015-16 $9,430; 2025-26 $11,950** (CP-1); growth **2.40%/yr over 10 years, 3.97%/yr over 20**. Sticker price; net tuition and fees for first-time full-time in-state students is an estimated $2,300 (so sticker is the conservative input). **Scope:** tuition and fees only (housing and food are $13,900; the published cost of attendance is $30,990 including books, transport and personal expenses; none modeled). Bills at 3.5% growth (the case's illustrative middle rate) are due at the **start** of years 6, 7, 8, 9 from today: about $14,193, $14,690, $15,204, $15,736, **total about $59,822** (annuity-due timing; the timing convention is borrowed from the source investment case and is not named in student text). **Window and dates:** each window is 9 consecutive calendar years; each January the balance earns that year's return after any bill is paid; the last bill is due at the start of year 9 (index 8); leftover is measured at the **end of year 9**, one year after the last bill (about $34.2K for A and $14.9K for B just after the last bill, before that year's return).
**The calculator vs history (the heart of the case; computed).** The calculator's steady rate is each mix's own 1928-2025 average annual return, the **geometric (compound) mean: A 8.83%, B 6.63%** (the arithmetic mean, 9.75% and 6.93%, is the contrast). The closed-form lump sum for the four bills at that rate (a finite geometric series), and what it really delivers:
| | Calculator lump sum | Share of the 90 windows in which that lump sum pays all four bills | Lump sum for 95% of windows | **Planning gap** |
|---|---|---|---|---|
| A (70/30) | **$34,545** | **54.4%** (about 54 of 100 nine-year stretches since 1928) | $53,722 | **+$19,177 (+56%)** |
| B (30/70) | **$39,417** | **36.7%** | $49,813 | **+$10,396 (+26%)** |
The calculator names one number and **no probability**. Its practical reliability is the 54% and 37% above. **It also reverses the ranking:** it says A is cheaper ($34.5K vs $39.4K); history says B needs less at every reliability target above 85% (at 85% they tie, $226 apart), because returns bounce around and **the order of returns matters once money is being withdrawn**.
**Sequence experiment (illustrative, not proof).** At $50,000, A fails in **7** windows; running the same nine returns in **reverse order**, **6 of the 7 pay all four bills**; B fails in 3, and **3 of 3** pay. Same returns, same average, a different order and (mostly) a different result.
**Funding levels (a deliverable).** The two mixes pay all four bills equally often at about **$42,100 at 2.4% growth, $45,200 at 3.5%, $46,600 at 4.0%** (the first dollar level from which B ties or leads and stays ahead; the curves cross within roughly $1,000 because there are only 90 windows). Below it A pays more often; above it B does. **Fragility, disclosed:** $50,000 sits only $187 above B's 95% lump sum ($49,813), so the "B pays, A does not" reading at $50,000 rests on a thin margin; at $45,000 A leads (84.4% vs 83.3%) and at $55,000 B leads (100% vs 95.6%).
**Deliverables -> skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| calculus-sequence | term | Sequence | 3 ◀ thin | D1 four tuition bills growing at a stated rate |
| calculus-series | term | Series | 2 ◀ thin | D2 the calculator: lump sum at a steady return, a finite geometric series |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 | D3 balance(t+1) = (balance(t) - bill(t)) x (1 + return(t)) for each historical window |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D3 |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D3 with a steady return the recursion collapses to the D2 closed form: show they match |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D2 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D5 planning gap as a percent |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 44 | D4 share of windows in which a plan pays all four bills |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D2 arithmetic mean of each mix, by year, as the contrast to the geometric (compound) average the calculator uses |
The geometric mean is not a spine skill (logged as a spine gap, like present value and compound interest); the case teaches it as the compound average and checks it by growing $1 through all 98 years and taking the 98th root. Scatter and correlation were removed; the stock-bond relationship may appear as an optional discussion only (for the record: +0.15 for 1928-1999, n=72, and -0.37 for 2000-2025, n=26, differ at the 5% level, Fisher z about 2.2, but the split is chosen after the fact).
**D6 (discussion, not a graded skill).** Same average, different order: show the reversed-order experiment and ask what a calculator hides.
**Data feasibility: HIGH.** Damodaran file (usage terms assumed met per the user); College Board Excel (`research.collegeboard.org/media/xlsx/Trends-in_College-Pricing-2025-excel-data.xlsx`, attribute the College Board).
**Facilitator-only legal/tax note.** $50,000 exceeds the 2026 annual gift-tax exclusion of **$19,000** per recipient (IRS Rev. Proc. 2025-32 §4.42(1), `irs.gov/pub/irs-drop/rp-25-32.pdf`); tuition is excluded only if "paid directly to the qualifying educational organization" (26 CFR 25.2503-6, `law.cornell.edu/cfr/text/26/25.2503-6`), which a lump sum given to a family is not; the FAFSA stopped counting grandparent-owned 529 distributions as student income (the 2022-23 form asked about them at question 44i; the 2026-27 form has no such item; the reason for the change rests on secondary sources). The case models a gift, not tax advice.
**Domain.** `education-systems`.
**Sensitivity (SPEC §6).** Facilitator note: family money stress; some students' families carry college debt or have no college fund.
**Split risk.** NONE (9 skills).

### C3 — The Jackpot Choice   ·   ON HOLD
All round-1 reviewers: DROP as a standalone binary. Awaiting the user's decision.
