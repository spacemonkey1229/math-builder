# Concepts — Investment-manager cases (v4) — 2026-10-23

Requested by the user after the v3 round: keep the investment-manager thread from the Gao case, with real stories and real asset-allocation decisions.
Three concepts. **Every number below was computed from real files** (Damodaran `histretSP.xls`, 1928-2025, downloaded to the session scratchpad; Wikipedia's lottery-jackpot table; CBS Sports and Wikipedia pages) and must be recomputed from fresh downloads in case-research.
Spine: no n==0 skills, so the reinforcement-carve-out bar applies (>= 2 thin skills genuinely forced). Rubric unchanged: score = sum(1.0 how-to / 0.6 term) x availability. Project rule from `REVIEW_BRIEF_non-sports-slots_2026-10-04.md`: **the metric must not let one option dominate, and no invented parameter may set the answer.** Where a concept is weak on that rule, it says so.

| Concept | Domain | Score | Tier | Thin forced | Data | Self-assessment |
|---|---|---|---|---|---|---|
| **C1 The Deferred Deal** | markets-investing | 8.6 | T4 | 6 | HIGH | Strong: real story, exact reproduction, real two-sided bet |
| **C2 The Four Payments** | education / household money | 9.6 | T4 | 2 | HIGH | Strong after reframing: asset allocation is the decision |
| C3 The Jackpot Choice | games-and-gambling | 6.2 | T4 | 3 | HIGH | **Weakest: cash option dominates on historical data unless the winner's mandate is stated** |

**Overlap note (me):** C1 and C3 both price a stream of annuity-due payments, so they share math. They differ in the question (C1: can you beat a quoted rate? C3: what rate is the quote hiding?). Reviewers should say whether both are needed. Corpus search found no Bonilla, lottery, tuition or 529 case.

---

### C1 — The Deferred Deal   ·   score 8.6   ·   tier T4
**Protagonist.** Marcus Hale (fictional), a finance executive for a baseball club in January 2000. The club has just released an aging star but still owes his 2000 salary of $5.9M. The player's agent offers to take the money later, with interest. Personally at stake: the owner is counting on him to make the deferral pay for the team.
**The dilemma.** A.) Pay the $5.9M now in 2000 and be done OR B.) Defer it at **8% interest**, to be repaid in **25 equal yearly payments from 2011 to 2035**, and invest the $5.9M in the meantime.
**The real story (verified).** Bobby Bonilla and the Mets. Released in January 2000 with $5.9M still owed; the Mets agreed to defer it at 8% over 25 years starting 2011; payment **$1,193,248.20 each July 1**; ownership believed investments with Bernie Madoff would earn more than 8%; Madoff's Ponzi scheme collapsed; the deferred balance "swelled to $29.8 million from 2000-11" (CBS Sports, fetched 2026-10-23; other outlets agree).
**The math reproduces to the dollar (computed).** $5.9M x 1.08^11 = **$13.757M**. The present value at 2011 of 25 payments with the first paid immediately (an **annuity due**, the same timing as Gao's reserve) at 8% is **$13.757M** at a payment of **$1.1932M**, matching the published $1,193,248.20. Total paid about **$29.83M**. Students rebuild the contract from two facts and check it.
**Primary metric.** Net position in 2011 = value of the invested $5.9M minus the $13.757M owed (A = $0). B beats A when the pool grows past 2.33x in 11 years, i.e. above **8% a year**.
**Why it's close (computed from 1928-2025 data).**
| | Share of 88 overlapping 11-year windows at or above 8%/yr | Median annualized |
|---|---|---|
| S&P 500 | **67.0%** | 10.5% |
| 60/40 stocks/bonds | **52.3%** | 8.5% |
| 10-year T-bond | 20.5% | 3.9% |
| 3-month T-bill | 11.4% | 2.9% |
So for stocks the bet looks good (two windows in three), and for safe assets it is a loser. What actually happened, calendar 2001-2011: S&P **1.45%/yr** ($5.9M became about **$6.9M**, against $13.76M owed), T-bond 6.4%, 60/40 4.3%. The bad decade (2000 -9.0%, 2001 -11.8%, 2002 -22.0%) was one of the worst 11-year stretches on record. Hindsight vs foresight is the case's second lesson.
**Independence lesson.** 88 overlapping windows are really **8 non-overlapping 11-year blocks** (annualized S&P: 1.8, 7.6, 17.6, 8.6, 7.7, 15.5, 10.9, 7.0). Only **4 of 8 (50%)** cleared 8%, not 67%. Students see how overlap inflates confidence.
**Deliverables -> skills (all genuinely forced):**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D1 value of $5.9M after 11 years at 8% |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D1 / D4 interest and shares |
| calculus-series | term | Series | 2 ◀ thin | D2 PV of 25 payments as a finite geometric series |
| calculus-sequence | term | Sequence | 3 ◀ thin | D2 the payment/discount-factor sequence |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D2 balance(t+1) = balance(t) x 1.08 - payment, then closed form |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 | D2 |
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin | D3 box plot of 88 rolling 11-year annualized S&P returns |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin | D3 |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin | D3 |
| statistics-and-probability-median | term | Median | 8 | D3 |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D3 average of the 8 non-overlapping blocks |
**Data feasibility: HIGH.** Damodaran, *Historical Returns on Stocks, Bonds and Bills 1928-2025* (`stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls`), downloaded and parsed; the file's "date updated" cell is stale but it contains 1928-2025. Contract facts: CBS Sports (fetched), Yahoo, CNBC (403 to fetch), CNN via search. Not confident about: the contract text itself (secondary sources only), the exact date the deferral was agreed, and whether the $5.9M was due July 2000 or paid over the season (the case approximates 2000 to 2011 as 11 calendar years 2001-2011; state this).
**Constructed binary, stated in the case.** The real owners did choose B. A is the road not taken; the case is written from January 2000 with only information available then, and the 2001-2011 outcome is a separate hindsight deliverable.
**Extension (not counted).** Flip the viewpoint: the player's agent, deciding between an 8% promise from a team and investing cash himself; adds counterparty (credit) risk.
**Sensitivity (SPEC §6).** NONE. The Madoff fraud is mentioned as a fact, not dramatized; the case never accuses a named person of wrongdoing beyond what is reported.
**Split risk.** NONE (11 skills).

### C2 — The Four Payments   ·   score 9.6   ·   tier T4
**Protagonist.** Ayo Bankole (fictional), a planner at a credit-union advice desk. A grandmother has given her granddaughter's family **$50,000** to cover **four years of in-state public college**, starting in five years. Personally at stake: the first tuition bill lands the fall after the market has either helped or hurt, and the family cannot make up a shortfall.
**The dilemma (asset allocation).** A.) Put the $50,000 in a **70% stocks / 30% bonds** mix and hold it OR B.) Put it in a **30% stocks / 70% bonds** mix and hold it.
**Primary metric.** Share of 9-year historical windows in which **all four tuition bills are paid in full**. Secondary: median leftover, worst shortfall.
**Setup (verified or to verify).** Tuition and fees, in-state public four-year, 2025-26: **$11,950** (College Board *Trends in College Pricing 2025*, from a search summary: verify on the College Board page). Bills grow **3.5% a year** (stated assumption; recheck against College Board's multi-year series) and are paid at the **start** of years 6, 7, 8, 9 (annuity-due timing, as in Gao): about $14,193, $14,690, $15,204, $15,736, **total $59,822**.
**Computed from 1928-2025 data (90 overlapping 9-year windows).**
| Allocation | All four bills paid | Mean shortfall | Worst shortfall | Median leftover |
|---|---|---|---|---|
| A 70/30 | **92.2%** | $774 | $21,105 | $36,711 |
| B 30/70 | **96.7%** | $128 | $4,886 | $15,464 |
**Why it's close.** B is safer: fewer failures and a much smaller worst case. A leaves more money over when it works (median leftover $36.7K against $15.5K) but fails in about 1 window in 13, sometimes badly. That is Gao's liability-first logic in a family's hands: the extra upside does not help a family that only needed the four bills. The gap on the primary metric is about 5%, within the balance rule. **Funding level matters:** at $55,000 B pays every bill in all windows and the margin vanishes; at $45,000 it widens. The case fixes the lump sum at $50,000 and shows the sensitivity.
**Why "glide path" was rejected.** A glide into T-bills lost to static 70/30 at every funding level (all four paid in 81% vs 92% of windows at $50K) because T-bills do not keep up with tuition inflation. Students may test this as an extension.
**The diversification hook.** Stock-bond correlation over 1928-2025 is **+0.02**; **+0.15** for 1928-1999 but **-0.37** for 2000-2025. Bonds rose **+20.1%** in 2008 when stocks fell **-36.6%**; in **2022** both fell (stocks -18.0%, bonds -17.8%). Students plot all 98 years and decide how much to trust bonds as the stabilizer.
**Independence lesson.** 90 overlapping windows are about **10 independent 9-year blocks**.
**Deliverables -> skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| statistics-and-probability-scatter-plot | term | Scatter Plot | 10 | D1 stock vs bond annual returns, 1928-2025 |
| statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data | how-to | How to create a scatter plot given a set of data | 12 | D1 |
| statistics-and-probability-correlation | term | Correlation | 5 | D2 sign flips: +0.15 (1928-99) vs -0.37 (2000-25) |
| statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data | how-to | How to identify correlation given a scatter plot or set of data | 5 | D2 |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 4 | D2 |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 4 | D2 |
| statistics-and-probability-outlier | term | Outlier | 5 | D2 2022 (stocks -18.0%, bonds -17.8%) breaks the pattern |
| calculus-sequence | term | Sequence | 3 ◀ thin | D3 four tuition bills growing 3.5% a year |
| calculus-series | term | Series | 2 ◀ thin | D3 total of the four bills |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D3 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D4 allocation weights |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 26 | D4 weighted portfolio return |
**Spine note.** Line of best fit, correlation and outlier were thickened by another case on 2026-10-19 (n=4-5), so only series (n=2) and sequence (n=3) count as thin here: the carve-out bar (>= 2) is met, but narrowly. The correlation and scatter work still carries the asset-allocation argument.
**Data feasibility: HIGH.** Damodaran file (downloaded and parsed); College Board *Trends in College Pricing* (`research.collegeboard.org/trends/college-pricing/highlights`, to fetch). Tuition growth rate and the lump sum are stated assumptions.
**Sensitivity (SPEC §6).** NONE (a family savings decision); a classroom note that some students' families carry college debt.
**Split risk.** NONE (12 skills).

### C3 — The Jackpot Choice   ·   score 6.2   ·   tier T4   ·   WEAKEST
**Protagonist.** Renata Voss (fictional), a financial advisor with a client who has just won a record Powerball jackpot. Personally at stake: her client's family trust has promised a thirty-year schedule of gifts to a hospital and to relatives.
**The dilemma.** A.) Take the **cash option** and invest it to pay the schedule yourself OR B.) Take the **30-year annuity** that pays the schedule automatically.
**Real figures (Wikipedia jackpot table, fetched 2026-10-23).** Dec 24 2025: advertised **$1.817B**, cash **$834.9M** (45.9%). Nov 7 2022: $2.04B, cash $997.6M (48.9%). Sep 6 2025: $1.787B, $820.6M (45.9%). Oct 11 2023: $1.765B, $774.1M (43.9%). Jan 13 2016: $1.5864B, $983.5M (**62.0%**). Annuity: 30 graduated payments over 29 years, each **5%** higher than the last (Wikipedia; primary source MUSL to verify).
**What the math reveals (computed).** The first annuity payment is jackpot x 0.05/(1.05^30 - 1) = **1.505%** of the jackpot, the last **6.195%**; for $1.817B that is **$27.35M rising to $112.57M**. Setting the annuity's present value equal to the cash value gives the **interest rate the lottery implicitly uses**: **2.84%** (Jan 2016), **4.43%** (Nov 2022), **4.87%** (Dec 2025), **4.88%** (Sep 2025), **5.21%** (Oct 2023). It rises and falls like Treasury yields (students compare to FRED DGS20/DGS30 on those dates; to verify).
**The balance problem (computed, read this).** Withdrawing exactly the annuity schedule from the $834.9M cash, invested in 1928-2025 returns (69 overlapping 30-year windows, only **3 independent**): **100% stocks** pays the schedule in 94.2% of windows; **60/40 in 95.7%**; 30/70 in 92.8%; **100% T-bond in 47.8%**; T-bills in 39.1%. With stocks or 60/40 the cash wins on both success rate and leftover (median leftover in the billions); with bonds only, the annuity wins. So the "decision" collapses into "what will the cash earn," i.e. into asset allocation, and the author should not pretend otherwise. As written, A dominates for any stock-heavy winner, so **this concept only works if the case imposes a certainty mandate** (e.g. "the schedule must be met in 99% of historical windows," Gao's "high degree of certainty") that 60/40 cannot meet. That mandate is a stated judgment, not data.
**Primary metric (proposed).** Share of historical 30-year windows in which the cash option, invested at the chosen allocation, pays every scheduled payment.
**Deliverables -> skills:**
| id | kind | label | spine n | forced by |
|---|---|---|---|---|
| calculus-series | term | Series | 2 ◀ thin | D1 30 graduated payments as a geometric series |
| calculus-sequence | term | Sequence | 3 ◀ thin | D1 |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin | D1 payment(t+1) = 1.05 x payment(t) to closed form |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 | D2 |
| advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole | how-to | How to find a whole given the percent and the part of the whole | 4 | D2 jackpot from cash share |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 44 | D2 cash share of each draw |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 90 | D3 |
**Data feasibility: HIGH** for the jackpot table and Damodaran; MUSL (Multi-State Lottery Association) rules and Treasury yields on each draw date to fetch.
**Sensitivity (SPEC §6).** FLAG: gambling subject matter. Facilitator note; the case is about the arithmetic of an offer, not about playing. Taxes are excluded as a stated simplification (the Wharton packet does the same), but a real winner owes large federal and state tax on either choice.
**Split risk.** NONE (7 skills). **Open question for reviewers:** is C3 distinct enough from C1, and is the mandate-driven balance acceptable? If not, drop it or fold its implied-rate discovery into C1 as an extra deliverable.
