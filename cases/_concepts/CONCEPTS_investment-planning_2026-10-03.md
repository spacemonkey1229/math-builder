# Concepts — Investment Case Decomposition (Wharton WGY "Gao" case) — 2026-10-03

> **SUPERSEDED 2026-10-04** by `CONCEPTS_investment-planning-v2_2026-10-04.md` (math sound, concepts lacked soul).

**Source material (not committed to the repo):** Wharton Global Youth Investment Competition case packet (4 pp), a
companion Excel model (8 sheets), and a high-school game-plan HTML. Target domain: `markets-investing`
(+ `pricing-household-money`). Spine sweep: **zero skills at n==0**, so this runs on the reinforcement-carve-out basis
(`skills/case-readiness/SKILL.md`); the bar is "genuinely forces thin (n<=3) skills," not "closes a hole."

**IP / integrity note.** The packet is a live 2026 competition prompt. None of these concepts reuse its client, numbers,
or wording: each has a fictional protagonist, a different decision, and real public data in place of the workbook's
*assumed* returns. We borrow the **math structure**, not the case. Confirm that is acceptable before any of it ships.

## Step 1 — Skills broken apart

| # | Skill module in the Gao work | Math it actually is | Spine reach | Castable? |
|---|---|---|---|---|
| M1 | Timeline / beginning-of-year timing | counting periods (2033-2027 = 6, 2033-2028 = 5) | arithmetic only | folded in |
| M2 | Compound growth to 2033 | V = 300000(1+r)^6 + 150000(1+r)^5 | exponent, evaluate exponential (n=8) | support only |
| M3 | Weighted portfolio return | weighted mean | **no weighted-mean skill in spine**; mean (27), percent-of (89) | no: thick |
| M4 | Bear / base / bull scenarios | range, min / max, sensitivity | range (8) | support only |
| M5 | Reserve = PV of annuity due | finite geometric series, discount factor | series (2), sequence (3), recursive to explicit (3) | **yes, C2** |
| M6 | Reserve ladder 30/30/40 | percent partition, matching | percent-of (89), pie (33) | no: thick |
| M7 | Residual and flexibility cushion | F = (V-R)(1-c), multi-step equation | solve multi-step (4), substitution (8) | support only |
| M8 | Sponsor range with stated confidence | percentiles, quartiles, box plot | quartiles (3), box term (3), box how-to (1) | **yes, C1** |
| M9 | Probability of funding / Monte Carlo | independence, combinations, experimental probability | independent (2), combination how-to (2) | **yes, C3** |
| M10 | Sequence-of-returns risk | recursion with varying r; order matters once cash flows exist | recursive (4), missing-element-of-mean (1) | **yes, C2** |
| M11 | Diversification / volatility | correlation, scatter, line of best fit | line of best fit (3+3), correlation (4+4) | **yes, C4** |
| M12 | Inflation on facility cost | percent change, real vs nominal | thick; overlaps `the-quiet-thief` | no |
| M13 | Exhibits and chart literacy | histogram, box, scatter, pie | covered by C1, C4 | folded in |
| M14 | IPS, memo, Q&A | writing | not math; standard pitch deliverable | n/a |

**Spine gap worth logging (not a case):** present value, compound interest, weighted mean, nth root / logarithm and standard
deviation have no spine skill. The whole finance family leans on exponent (8) and percent-of (89) for lack of anything better.

## Step 2 — Rubric (the case-brainstorm one, applied unchanged)

`score = sum(weight) x availability`, weight 1.0 how-to / 0.6 term, no group bonus (no group is fully closed).
Gates, in order: **SPEC §0** (binary decision, math is the only defense) -> **balance** (margin <= ~20%, structurally plausible)
-> **carve-out** (>= 2 thin skills genuinely forced) -> **free-data** (named, fetched source) -> **corpus overlap / title
collision** -> **domain diversity** -> **coverage-inflation** (<= 15 skills). Data checked live today: Damodaran
`histretSP.xls` (1928-2025; S&P 500, 10-yr T-bond, 3-mo T-bill; free) and FRED `DGS10` (live, last obs 2026-10-01).

| Concept | Score | Tier | Thin forced (n<=3) | How-to / term | Data | Verdict |
|---|---|---|---|---|---|---|
| **C1 The Sponsor Range** | 8.0 | T4 | 3 | 5 / 5 | HIGH | **Write** |
| **C2 The Reserve Gamble** | 7.8 | T4 | 4 | 6 / 3 | HIGH | **Write** |
| C3 The Coin-Flip Decade | 7.4 | T3 | 2 | 5 / 4 | HIGH | Write (after C1/C2 reviews) |
| C4 The Stabilizer | 7.0 | T4 | 2 | 4 / 5 | HIGH | Hold |
| K5 The Equity Share | 3.6 | T3 | 0 | 3 / 1 | HIGH | **Kill** |
| K6 The Deflating Pledge | n/a | T3 | 0 | | HIGH | **Kill** |
| K7 The Perpetual Pledge | n/a | T4 | 2 | | MEDIUM | **Kill** |

**Recommendation.** Write **C1** and **C2**; they carry the two real decisions in the Gao work (what to *promise*, how to *fund*)
and force 7 of the corpus's thinnest skills between them. C3 is a sound third but shares C1's dataset, so sequence it after
the R1 round. C4 is good math but weaker on thin skills (2) and sits closest to `investment-portfolio`. **Domain-diversity
warning:** all four land in the money cluster, which already holds 16 case-slots (insurance-actuarial 5, markets-investing 4, pricing-household-money 7). Recommend writing **at most two now** and
treating C2's structure (fund a fixed schedule of future payments from a risky pool) as a template to transplant into an
under-used domain (a city seawall fund, a plant decommissioning trust) in a later batch.

---

### C1 — The Sponsor Range   ·   score 8.0   ·   tier T4
**Protagonist.** Dev Raman, associate at a boutique wealth firm, who must give a nonprofit artist-residency founder one dollar
range to quote donors two years before the money is needed. Personally at stake: his name is on the range if the founder misses it.
**The dilemma.** A.) Quote the Cautious Range: floor at the 10th percentile and ceiling at the median of historical 6-year
outcomes OR B.) Quote the Middle-Half Range: floor at the 25th percentile and ceiling at the 75th.
**Primary metric.** Promised floor dollars per percentage point of historical windows that miss it.
**Why it's close.** A's floor is safer but signals less commitment to donors; B promises more and misses more often. Overlapping
6-year windows are not independent (only ~16 non-overlapping ones exist in 1928-2025), so the miss rate itself is uncertain, and
that is the argument B's defender and A's defender both have to handle.
**Would close (10 skills, 5 how-to / 5 term):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-quartiles | term | Quartiles | 3 ◀ thin |
| statistics-and-probability-box-and-whisker-plot | term | Box And Whisker Plot | 3 ◀ thin |
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 ◀ thin |
| statistics-and-probability-median | term | Median | 8 |
| statistics-and-probability-range | term | Range | 8 |
| statistics-and-probability-outlier | term | Outlier | 4 |
| statistics-and-probability-how-to-create-a-histogram-given-a-set-of-data | how-to | How to create a histogram given a set of data | 19 |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data | 25 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 |
**Already-covered skills it also exercises.** percent conversions, decimals, line graph reading.
**Data feasibility: HIGH.** Damodaran, "Historical Returns on Stocks, Bonds and Bills: 1928-2025" (`stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls`) — fetched today, free .xls. FRED for T-bill cross-check.
Not confident about: the contribution-split assumption (what share of the 2033 pot is "available") is a disclosed Modeling Assumption.
**Sensitivity (SPEC §6).** NONE — a donor-communication decision, no hardship stakes.
**Split risk.** NONE.

### C2 — The Reserve Gamble   ·   score 7.8   ·   tier T4
**Protagonist.** Marisol Vega, treasurer of a community arts nonprofit, who must lock down ten annual $50,000-style
operating payments before pledging any money to a building. Personally at stake: a missed payment ends the program mid-run.
**The dilemma.** A.) Fund the Ladder Reserve: a Treasury-matched reserve sized by present value, certain to pay all ten OR
B.) Fund the Growth Reserve: a smaller 60/40 reserve that frees more capital for the building but fails in some historical decades.
**Primary metric.** Dollars of capital freed per percentage point of historical 10-year windows in which the ten payments fail.
**Why it's close.** B frees real dollars at a small, quantifiable failure rate; A is certain but ties up more. Whether a few
percent failure counts as "high certainty" is exactly the judgment the student must defend, and the freed amount is large
enough to matter to the building. The order-of-returns insight (same average return, different outcome once money is withdrawn)
is the mathematical heart: students show a mean alone does not determine survival.
**Would close (9 skills, 6 how-to / 3 term):**
| id | kind | label | spine n |
|---|---|---|---|
| calculus-series | term | Series | 2 ◀ thin |
| calculus-sequence | term | Sequence | 3 ◀ thin |
| discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula | how-to | How to convert a recursive formula to an explicit formula | 3 ◀ thin |
| discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence | how-to | How to write a recursive formula for a sequence | 4 |
| discrete-mathematics-recursive-formula | term | Recursive Formula | 4 |
| statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining- | how-to | How to find a missing data element given the mean and the remaining elements of its set | 1 ◀ thin |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number | 89 |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 42 |
**Already-covered skills it also exercises.** percent conversions, decimals, line graph.
**Data feasibility: HIGH.** Damodaran `histretSP.xls` (rolling 10-year windows from 1928-2025); FRED `DGS1`-`DGS10`
and Treasury par yield curve for the ladder's discount rates (FRED live today).
Not confident about: exact ladder yields at a chosen date; resolve by fixing a dated Treasury curve as a cited input.
**Sensitivity (SPEC §6).** NONE.
**Split risk.** NONE (9 skills). Guardrail: the missing-element-of-mean how-to must be forced only on the planner's stated
*average* return (an arithmetic mean), never on compounded growth, or it is a false claim and `case-write` will flag it.
`calculus-how-to-determine-whether-a-series-converges-or-diverges` (n=2) is an optional perpetuity stretch, **not counted**.

### C3 — The Coin-Flip Decade   ·   score 7.4   ·   tier T3
**Protagonist.** Tamsin Okoye, risk analyst at a regional credit union's investment committee. Personally at stake: she signs the model memo.
**The dilemma.** A.) Model the next six years as independent up/down years and quote the binomial odds OR B.) Use historical
6-year blocks, which keep real clustering of good and bad years.
**Primary metric.** Probability that at least four of six years are positive, under each model (percentage points apart).
**Why it's close.** Independence makes the arithmetic clean (C(6,k) paths, p^k(1-p)^(6-k)) and the real year-to-year dependence is weak but nonzero, so the two answers sit near each other without being identical.
**Would close (9 skills, 5 how-to / 4 term):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 ◀ thin |
| statistics-and-probability-combination | term | Combination | 4 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 ◀ thin |
| statistics-and-probability-experimental-probability | term | Experimental Probability | 4 |
| statistics-and-probability-conditional-probability | term | Conditional Probability | 5 |
| statistics-and-probability-how-to-determine-the-probability-of-a-compound-event | how-to | How to determine the probability of a compound event | 7 |
| statistics-and-probability-how-to-determine-the-probability-of-a-single-event | how-to | How to determine the probability of a single event | 14 |
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | How to evaluate an exponential expression | 8 |
| advanced-numbers-how-to-convert-numbers-to-percents | how-to | How to convert numbers to percents | 42 |
**Data feasibility: HIGH.** Damodaran `histretSP.xls`.
**Sensitivity (SPEC §6).** NONE. **Split risk.** NONE. **Weakness:** only 2 thin skills and same dataset as C1; hence sequenced third.

### C4 — The Stabilizer   ·   score 7.0   ·   tier T4
**Protagonist.** Ines Calloway, portfolio analyst choosing the stabilizing sleeve of a six-year plan.
**The dilemma.** A.) Intermediate Treasury bonds OR B.) T-bills as the 25% stabilizer.
**Primary metric.** Dollars of loss cushioned in the five worst stock years, per percentage point of average return given up.
**Why it's close.** Bonds cushion most bad stock years but not 2022, a real outlier that breaks the pattern a line of best fit suggests.
**Would close (9 skills, 4 how-to / 5 term):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-scatter-plot | term | Scatter Plot | 9 |
| statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data | how-to | How to create a scatter plot given a set of data | 11 |
| statistics-and-probability-correlation | term | Correlation | 4 |
| statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data | how-to | How to identify correlation given a scatter plot or set of data | 4 |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 ◀ thin |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 ◀ thin |
| statistics-and-probability-outlier | term | Outlier | 4 |
| statistics-and-probability-slope | term | Slope | 10 |
| statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data | how-to | How to write a linear equation given a set of data | 10 |
**Data feasibility: HIGH.** Damodaran `histretSP.xls`.
**Sensitivity (SPEC §6).** NONE. **Split risk.** NONE. **Weakness:** 2 thin skills; nearest neighbour `investment-portfolio` (different math: Sharpe vs regression).

### Killed
- **K5 The Equity Share** (65/35 vs 40/60): forces zero thin skills (weighted mean has no spine skill; mean and percent-of are saturated) and
  overlaps `investment-portfolio`. Its deliverable is better absorbed as a C1 sub-step.
- **K6 The Deflating Pledge** (nominal vs inflation-indexed promise): overlaps `the-quiet-thief` on real purchasing power; no thin skills.
- **K7 The Perpetual Pledge** (ten payments vs endowing forever): not close (perpetuity costs several times more, far outside the ~20% balance rule),
  and funding past 2042 is out of the packet's own scope.

**Next step:** run the R1a / R1b / R1c review on C1-C3 (the sports-science wave used the same brief format), then
`Approve a concept, then run case-write on it.`
