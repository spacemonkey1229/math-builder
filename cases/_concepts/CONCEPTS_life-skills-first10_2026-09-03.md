# Concept sheet — first 10 life-skills cases

Source: the life-skills taxonomy drafted 2026-09-03 (7 clusters: cash flow & money mechanics,
debt & credit, major purchase decisions, employment & income, taxes & tax-advantaged accounts,
insurance & risk, long-horizon growth), cross-checked against the coverage audit of the same date
(113 published cases) and `readmodel/standards_spine.json`'s live `covered_by[]`/`n` fields.

**Priority order in this sheet is topic-first, skill-second**, per the ask: the four true
zero-coverage life topics (job offers, car ownership/leasing, Roth vs. Traditional IRA, car
maintenance) come first regardless of which skill they land on; the remaining six fill out the
taxonomy's other clusters, each one *then* aimed at a genuinely thin or zero-coverage skill group
where a real fit exists — none is forced onto a skill it doesn't naturally need.

**These are concepts only** — nothing here has been through `case-research` or `case-write`. No
source has been checked yet; feasibility is an honest best guess. All skill ids/`n` counts pulled
live from `standards_spine.json` on 2026-09-03, not from memory.

---

## 1. The Two Offers (Job Offer Comparison — Salary + Benefits Crossover)
**Topic gap closed:** #4 Employment & income — zero coverage in the library (audit finding: no
case compares job offers at all).
**Narrative.** A new graduate has two real offers on the table with a decision deadline in days:
Offer A is higher base salary with a smaller signing bonus and standard benefits; Offer B is
lower base but a larger signing bonus, an employer 401k match, and remote-work savings on
commuting/parking. Neither is strictly better — the answer depends on how long they expect to
stay before the comparison flips.
**Problem.** Model each offer's cumulative take-home value as a function of time (months on the
job), including the one-time bonus, recurring salary, and estimated commute/COL cost as a
constant per-month drag on one offer. The two lines cross at some point — the dilemma is finding
that crossover and deciding which side of it the learner's actual plans put them on.
**Primary metric.** Cumulative net value ($) per month of tenure, for each offer, as linear
functions of time.
**Would close:** `statistics-and-probability-system-of-equations` (n=2),
`statistics-and-probability-how-to-solve-a-system-of-linear-equations` (n=2); reinforces
`statistics-and-probability-how-to-write-a-linear-equation-given-a-set-of-data` (n=7) and the
slope-from-data skill (n=3).
**Rubric.** Must force the learner to actually set up and solve two linear equations for their
intersection (not eyeball a chart); trap: a learner who only compares day-one numbers (bonus size
or starting salary) without extending to a time horizon will pick the wrong offer for anyone
staying more than ~1 year.
**Margin target.** 10–15%. Real offer-comparison spreadsheets genuinely cross at different points
depending on assumptions — a defensible, not-engineered margin should fall out naturally.
**Feasibility.** HIGH — this is standard personal-finance content (NerdWallet/Ramsey-style offer
calculators exist publicly); no exotic sourcing needed, just realistic dollar figures.

---

## 2. The Breakeven Mile (Car Ownership vs. Rideshare)
**Topic gap closed:** #3 Major purchase decisions — zero coverage (audit: `car-purchase` is a
dead legacy stub; no case addresses ownership vs. rideshare/lease).
**Narrative.** A city resident is deciding whether to keep a car or go car-free and rely on
Uber/Lyft plus occasional rentals. Car ownership means fixed costs (insurance, loan/depreciation,
registration) whether or not it's driven, plus a smaller per-mile cost (gas, tires, oil); rideshare
has zero fixed cost but a much higher per-mile rate. The right answer depends entirely on annual
mileage, which the learner has to estimate honestly from their own commute/errands pattern.
**Problem.** A.) **Own** — total annual cost = fixed costs + (low per-mile rate × miles driven).
B.) **Rideshare-only** — total annual cost = high per-mile rate × miles driven, no fixed cost.
Find the breakeven mileage where the two lines cross.
**Primary metric.** Total annual transportation cost ($) as a function of miles driven per year.
**Would close:** reinforces the same system-of-linear-equations skills as #1 if paired
deliberately, or — if written with a *nonlinear* ownership-cost curve (depreciation accelerates
with mileage, so average cost-per-mile isn't constant) — can instead target the zero-coverage
`calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions` (n=0) by having
the learner minimize average cost-per-mile `C(m)/m`. Recommend writing the calculus-track version
specifically because it's a real zero-coverage close, not just reinforcement.
**Rubric.** Trap: a learner who compares costs at one arbitrary mileage (e.g. "my current
commute") without solving for the actual crossover will get a fragile, non-generalizable answer.
**Margin target.** 8–12%.
**Feasibility.** HIGH — AAA publishes real annual cost-of-ownership tables by vehicle class; Uber/
Lyft per-mile averages are publicly estimated in cost-of-living research.

---

## 3. Pay Now or Pay Later (Traditional vs. Roth IRA)
**Topic gap closed:** #5 Taxes & tax-advantaged accounts — zero coverage (audit: IRA only ever
appears as a net-worth line item, never as the actual dilemma).
**Narrative.** A 24-year-old with their first real paycheck has to pick a retirement account type
before their first contribution posts. A Traditional IRA takes the tax break today (contribution
reduces this year's taxable income) but taxes the full amount, growth included, on withdrawal
decades later. A Roth IRA taxes the contribution now, at today's known rate, but nothing on
withdrawal — including 40 years of growth. The dilemma is genuinely about *which* tax rate is
better to pay it at: today's, or an unknown future one.
**Problem.** Model the same annual contribution compounding for ~40 years under both plans, taxed
at today's marginal rate (Roth, paid up front) vs. an assumed future retirement-year rate
(Traditional, paid on withdrawal). Show that the two are mathematically identical *only* if the
tax rate never changes — the entire real-world decision rides on whether the learner expects to
be in a higher or lower bracket at retirement.
**Primary metric.** After-tax value at retirement ($), for each account type, as a function of
the assumed future tax rate.
**Would close:** reinforces `advanced-operations-how-to-evaluate-an-exponential-expression` (n=5)
and `advanced-numbers-how-to-find-the-percent-of-a-number` (n=63, well-covered — this is
reinforcement, not a close); genuinely closes the thin
`advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`
(n=2) if the compounding formula is built up from raw multiplication rather than a single plugged
formula.
**Rubric.** Trap: a learner who assumes "Roth is just better" (common personal-finance folk
wisdom) without running the algebra under a *lower* future tax-rate assumption should discover
Traditional wins in that case — the case only works if it's genuinely bracket-dependent, not a
foregone conclusion.
**Margin target.** 5–10% — deliberately tight, since the honest answer is "it depends," and the
case should reward getting the actual crossover condition right, not picking a side.
**Feasibility.** MEDIUM-HIGH — IRS contribution/bracket figures are public and exact; the compound
-growth math is standard, but writing a genuinely two-sided (not Roth-biased) narrative takes care.

---

## 4. The Deferred Repair (Preventive vs. Reactive Car Maintenance)
**Topic gap closed:** #3 Major purchase decisions / car maintenance — zero coverage (audit: no
case addresses maintenance economics at all).
**Narrative.** A driver's car needs a $40 preventive service (e.g., a coolant flush) the shop
flags at a routine oil change. Skipping it costs nothing today, but carries a real, quantifiable
probability of a much larger failure (e.g., a $1,200 engine repair) within the next year if
skipped repeatedly. The dilemma isn't "always fix everything" — some flagged services genuinely
have low failure risk and aren't worth the cost; the skill is telling which is which.
**Problem.** Compare **expected cost** of preventive spending now vs. **expected cost** of the
probability-weighted large repair later: `P(failure) × repair cost` vs. the certain, smaller
maintenance cost. Use real published failure-rate ranges for a couple of specific services so the
comparison isn't arbitrary.
**Primary metric.** Expected dollar cost per year, comparing "always do the preventive service"
vs. "skip and pay only if it fails."
**Would close:** `statistics-and-probability-conditional-probability` (n=3) and
`statistics-and-probability-how-to-determine-the-probability-of-compound-event` (n=4) if framed
as repeated-year risk (probability of failure *at least once* over several years of skipping).
**Rubric.** Trap: a learner who compares the preventive cost to the repair cost directly (ignoring
the probability weighting) will always say "just pay for the repair when it happens" — the
expected-value framing is the entire point.
**Margin target.** 10–15%. Real failure-rate data (e.g., from RepairPal, CarMD annual repair
studies) should be close enough that the answer isn't obvious either way.
**Feasibility.** MEDIUM — need a specific, sourced failure-rate table for at least one real
maintenance item; CarMD/RepairPal publish some of this publicly, worth confirming before writing.

---

## 5. The Real Cost of Breaking It (Signing and Breaking a Lease)
**Topic gap closed:** #2 Debt & credit / lease mechanics — tangential-only today (audit:
`rent-vs-own` is rent-vs-buy-a-house, not lease terms; no case walks through lease math itself).
**Narrative.** A renter is comparing two apartments: one with a lower monthly rent but a large
non-refundable move-in fee and a steep early-termination penalty; the other with slightly higher
rent, a smaller deposit, and a lease that can be broken for one month's rent. The "cheaper" one on
the sticker price isn't necessarily cheaper once the real risk of needing to move early (job
change, roommate falling through) is priced in.
**Problem.** Compute **effective monthly cost** for each lease under two scenarios — staying the
full term, and needing to break it at, say, month 6 — amortizing the up-front deposit/fees and any
termination penalty across the months actually lived there.
**Primary metric.** Effective cost per month actually lived in the unit, under both a
"stay full term" and a "break early" scenario.
**Would close:** `advanced-numbers-how-to-find-a-whole-given-the-percent-and-the-part-of-the-whole`
(n=2) if framed as "the deposit is what percent of one month's rent, and what's the true total
cost as a percent of a full year's rent"; reinforces `measurement-proportion` (n=17) and
`measurement-ratio` (n=25).
**Rubric.** Trap: a learner who only compares sticker monthly rent picks the wrong apartment for
anyone with a real (even moderate) chance of needing to leave early.
**Margin target.** 8–12%.
**Feasibility.** HIGH — lease terms, deposits, and termination-fee structures are standard and
easy to source realistically from any real rental listing.

---

## 6. How Long Can We Last (Emergency Fund Sizing)
**Topic gap closed:** #1 Cash flow & money mechanics / emergency fund — distinct from the
already-covered "budgeting" topic (audit found `phone-plan`/`family-trip` cover budgeting itself,
but nothing addresses *how much* to hold in reserve or why 3–6 months, not a round number).
**Narrative.** A household with irregular income (one salaried earner, one freelance/1099 earner
with variable months) is deciding how large an emergency fund to build before investing anything
beyond it. "3 to 6 months of expenses" is the common rule of thumb — the case's job is to make the
learner derive *which* end of that range fits their specific income volatility, not just quote the
rule.
**Problem.** Given a household's fixed essential monthly expenses and a realistic income-variance
pattern (e.g., freelance income ranging ±40% month to month, with occasional zero-income months),
compute the fund size needed to cover a realistic bad stretch, using the household's own income
data rather than a generic multiplier.
**Primary metric.** Months of essential-expense coverage provided by a given fund size, tested
against the household's actual worst realistic income stretch.
**Would close:** reinforces `advanced-numbers-percent` family (well-covered, n=57) and
`measurement-ratio`/`proportion` (n=25/17) — this concept is intro-tier and mostly a
reinforcement/thickening case rather than a zero-coverage close; include it for topic completeness
in the taxonomy, not skill urgency.
**Rubric.** Trap: a learner who just multiplies "3 months × expenses" without checking it against
the actual income-variance pattern given will undersize the fund for the specific household shown.
**Margin target.** 10–15%.
**Feasibility.** HIGH — no exotic sourcing; realistic freelance-income variability is easy to
model plausibly.

---

## 7. The Minimum-Payment Trap (Credit Card APR and Compounding Debt)
**Topic gap closed:** #2 Debt & credit / credit cards — zero coverage (no case in the library
addresses revolving debt or APR compounding against the consumer).
**Narrative.** Someone carries a credit card balance and is deciding between paying only the
minimum each month versus paying a fixed larger amount. The card's APR compounds daily or monthly
against the unpaid balance — the dilemma is seeing, concretely, how much of each minimum payment
is actually going to interest versus principal, and how many years "minimum only" really takes.
**Problem.** Model the balance month-over-month as a recursive relationship: `new balance =
(old balance × (1 + monthly rate)) − payment`. Compare the total interest paid and payoff time
under the minimum-payment path vs. a fixed higher payment.
**Primary metric.** Total interest paid ($) and months-to-payoff, under each payment strategy.
**Would close:** targets the thin `Discrete Mathematics / Proof And Recursion` group (thin=4 of 7)
by building the balance explicitly as a recursive sequence rather than a plugged amortization
formula — genuine, natural fit since minimum-payment balances *are* a recursive sequence.
**Rubric.** Trap: a learner who computes interest on the *original* balance only (simple interest,
not compounding on the shrinking-then-barely-shrinking balance) will badly underestimate total
interest paid.
**Margin target.** 10–15% — real credit card math is dramatic enough (minimum payments can take
15–20+ years on a modest balance) that the case doesn't need to be engineered for tension.
**Feasibility.** HIGH — CFPB publishes real minimum-payment disclosure formulas and requirements;
this is extremely well-documented, public, and standard.

---

## 8. Deductible Roulette (Car/Renters Insurance Deductible Tradeoff)
**Topic gap closed:** #6 Insurance & risk / non-health insurance — distinct from the already-
"Full"-covered healthcare-insurance topic (audit found `insurance` covers health marketplace
plans; nothing covers auto/renters deductible choice).
**Narrative.** A driver is choosing between a low-deductible policy (higher monthly premium, less
out-of-pocket if a claim happens) and a high-deductible policy (lower premium, more exposure per
claim). The right choice depends on the actual probability of filing a claim in a given year,
which varies by driving history/location — not on gut feel about which "feels safer."
**Problem.** Compute **expected annual cost** = premium + (probability of a claim in a year ×
expected out-of-pocket under that deductible), for both policies, using a realistic claim-
frequency estimate.
**Primary metric.** Expected total annual cost ($) under each deductible option.
**Would close:** `statistics-and-probability-conditional-probability` (n=3) and
`statistics-and-probability-how-to-determine-the-probability-of-a-single-event` (n=10, well-
covered — reinforcement); genuinely closes/reinforces the compound-event skill (n=4) if framed
over a multi-year window.
**Rubric.** Trap: a learner who picks the low-deductible plan by default ("safer") without running
the expected-value math will overpay in the large majority of realistic claim-frequency scenarios
— the case should make clear when high-deductible is actually the better bet.
**Margin target.** 8–12%.
**Feasibility.** MEDIUM-HIGH — insurance industry claim-frequency data (III.org, NAIC) is public
and can ground realistic probabilities.

---

## 9. Free Money, With Strings (Employer 401k Match)
**Topic gap closed:** #5 Taxes & tax-advantaged accounts / employer match — zero coverage (no
case addresses whether/how much to contribute to capture an employer match).
**Narrative.** A new employee has to choose a 401k contribution percentage. The employer matches
contributions up to a cap (e.g., 50% match on the first 6% of salary contributed) — contributing
less than the cap leaves guaranteed matching money on the table; contributing more than the cap is
still fine, just no longer matched. The case is about correctly identifying *where the match
stops mattering*, not "contribute as much as possible."
**Problem.** Model take-home-reduction vs. total retirement-account growth (own contribution +
match + investment growth) as contribution percentage increases from 0% past the match cap,
showing the effective "instant return" the match provides only up to that cap.
**Primary metric.** Effective rate of return on each additional percentage point of contribution,
as a function of contribution percentage (a step change at the match cap).
**Would close:** reinforces `calculus-instantaneous-rate-of-change` (n=3, thin) if framed as "the
marginal benefit of the next dollar contributed" changing discontinuously at the match cap —
genuine, if modest, fit for a thin skill.
**Rubric.** Trap: a learner who treats the match as a flat percentage bonus on *all* contributions
(rather than only up to the cap) will overstate the benefit of contributing beyond the cap.
**Margin target.** 10–15% — the "free money up to the cap, ordinary return after" structure is a
real step-function, not an engineered one.
**Feasibility.** HIGH — 401k match structures are standard, public, and easy to source accurately.

---

## 10. The Quiet Thief (Inflation and the Cost of Waiting to Save)
**Topic gap closed:** #7 Long-horizon growth / inflation — zero coverage (audit found
`investment-portfolio` covers saving/investing surplus income, but nothing isolates inflation's
erosion of purchasing power or the cost, in real terms, of delaying saving).
**Narrative.** Two savers put aside the same dollar amount per month for retirement — one starts
at age 25, the other waits until 35 to start, "planning to catch up later" by contributing more.
The case shows, in real (inflation-adjusted) dollars, exactly how much more the late starter has
to contribute to end up in the same place, and why "catching up" is mathematically harder than it
sounds once both compounding growth and inflation are modeled together.
**Problem.** Model both savers' account balances growing at a real (inflation-adjusted) rate of
return, and solve for the monthly contribution the late starter needs to match the early starter's
ending balance at a fixed retirement age.
**Primary metric.** Required monthly contribution ($, in today's dollars) for the late starter to
match the early starter's real ending balance.
**Would close:** reinforces `advanced-operations-how-to-evaluate-an-exponential-expression` (n=5)
and the exponent-with-order-of-operations skill (n=2, thin) if the real-rate-of-return formula
`(1 + nominal)/(1 + inflation) − 1` is derived rather than given.
**Rubric.** Trap: a learner who uses nominal (not inflation-adjusted) growth rates will understate
how much harder the late starter's catch-up really is.
**Margin target.** 10–15%.
**Feasibility.** HIGH — historical inflation and market-return averages are public and
well-documented (BLS CPI data, S&P 500 long-run real return figures).

---

## Summary table

Grouped by the 7 taxonomy clusters from the 2026-09-03 life-skills draft, in that cluster's
original order. Within a cluster, the true zero-coverage life topics are marked 🔴; everything
else in this batch is a real but lower-severity gap.

| Cluster (taxonomy) | # | Concept | Life-skills topic | Skill(s) closed/reinforced | Feasibility (sourcing) |
|---|---|---|---|---|---|
| 1. Cash flow & money mechanics | 6 | How Long Can We Last | Emergency fund sizing | Percent/ratio (reinforcement) | HIGH |
| 2. Debt & credit | 5 | The Real Cost of Breaking It | Signing/breaking a lease | Percent-of-whole (n=2, closes) | HIGH |
| 2. Debt & credit | 7 | The Minimum-Payment Trap | Credit card APR / minimum payments | Proof & recursion (thin group) | HIGH |
| 3. Major purchase decisions | 2 | The Breakeven Mile | 🔴 Car ownership vs. rideshare | Quotient rule (n=0, closes — calc-track option) | HIGH |
| 3. Major purchase decisions | 4 | The Deferred Repair | 🔴 Car maintenance (preventive vs. reactive) | Conditional/compound probability (n=3/4) | MEDIUM |
| 4. Employment & income decisions | 1 | The Two Offers | 🔴 Job offer comparison | System of linear equations (n=2, closes) | HIGH |
| 5. Taxes & tax-advantaged accounts | 3 | Pay Now or Pay Later | 🔴 Roth vs. Traditional IRA | Exponents w/ order of ops (n=2, closes) | MEDIUM-HIGH |
| 5. Taxes & tax-advantaged accounts | 9 | Free Money, With Strings | Employer 401k match | Instantaneous rate of change (n=3, thin) | HIGH |
| 6. Insurance & risk | 8 | Deductible Roulette | Car/renters insurance deductible | Conditional probability (n=3) | MEDIUM-HIGH |
| 7. Long-horizon growth | 10 | The Quiet Thief | Inflation / cost of waiting to save | Exponents w/ order of ops (n=2, reinforces) | HIGH |

**Cluster coverage check:** all 7 taxonomy clusters get at least one concept in this first batch;
clusters 2, 3, and 5 (the ones with the most sub-topics in the original draft) get two each.
Nothing was drafted yet for "hourly vs. salary vs. 1099" or "negotiating a raise" (cluster 4) or
"marginal tax brackets" as its own case distinct from Roth/IRA (cluster 5) — candidates for a
second batch if this one lands well.

---

## Prioritization: need score + Tier 1 / Tier 2 pass feasibility

**Scoring method.** Two independent 1–5 scores, averaged into a Priority:
- **Topic need** — how uncovered the life-skills topic is today (5 = the audit's true
  zero-coverage gaps; lower = tangential existing coverage or a sub-topic of an already-"Full"
  topic).
- **Skill need** — how much the mapped math skill is actually starved in `standards_spine.json`
  (5 = genuinely closes a zero-coverage skill; 1 = pure reinforcement of an already well-covered
  skill, kept only for topic completeness).

**Tier 1 / Tier 2 feasibility is graded separately from sourcing feasibility** (the "Feasibility"
column above is about finding real numbers; this is about actually clearing the pipeline's gates):
- **Tier 1 risk** grades against `tier1_structural.py`'s hardest-to-satisfy checks for this kind
  of case: T1-03 (dilemma must be genuinely binary, "You are `<X>`.") and T1-09 (the balance
  test / SPEC §2 ~20% real-margin cap — an option that's a landslide winner blocks). A few of
  these concepts are naturally an *optimization* ("how much to contribute," "how big a fund")
  rather than a clean two-option dilemma, which is a real T1-03 risk until reframed.
- **Tier 2 risk** grades against the 6-probe rubric (cold solve, both-sides, trap, twist,
  sensitivity, data decay) — mainly whether the trap already designed above is sharp enough to
  survive a "twist" probe (change one assumption) without collapsing.

| # | Concept | Topic need | Skill need | **Priority** | Tier 1 risk | Tier 2 risk |
|---|---|---|---|---|---|---|
| 1 | The Two Offers | 5 | 5 | **5.0** | LOW — clean two-offer binary, dollar figures cite easily | LOW — trap (single-point comparison) already sharp |
| 2 | The Breakeven Mile | 5 | 5 | **5.0** | LOW-MED — calc-track version needs a real nonlinear depreciation curve sourced, or T1-08 citation gaps | LOW — breakeven trap is sharp and twist-resistant (change annual mileage) |
| 5 | The Real Cost of Breaking It | 4 | 5 | **4.5** | LOW — binary, lease terms cite easily from any real listing | LOW — trap holds under a twist (change the early-exit month) |
| 3 | Pay Now or Pay Later | 5 | 4 | **4.5** | MED — T1-09 balance test is genuinely tight here (5–10% target); a landslide toward either account under realistic brackets risks a BLOCKER without an MCS-46 waiver | LOW-MED — twist probe (flip the future-bracket assumption) is actually built into the design, which helps |
| 4 | The Deferred Repair | 5 | 3 | **4.0** | MED — needs a real, specific, citable failure-rate table (T1-08); generic "repairs happen sometimes" won't clear sourcing | LOW-MED — sensitivity probe (multi-year repeated-risk) needs the recursion to be genuine, not just single-year |
| 7 | The Minimum-Payment Trap | 4 | 3 | **3.5** | LOW — CFPB minimum-payment formulas are exact and public, binary framing is clean | LOW — trap (simple- vs. compound-interest confusion) is sharp |
| 8 | Deductible Roulette | 3 | 3 | **3.0** | MED — claim-frequency data is usually aggregate/industry-wide, not the specific-driver-profile citation T1-08 wants; risk of a `{{NEEDS_SOURCE}}` gap | LOW-MED — trap (default-to-low-deductible bias) is solid |
| 9 | Free Money, With Strings | 3 | 3 | **3.0** | MED-HIGH — this is a percentage-optimization, not a natural A/B; needs explicit reframing (e.g. "contribute to the match cap" vs. "skip the match and pay down debt instead") to satisfy T1-03's binary-dilemma requirement | MED — once reframed as binary, trap (flat-bonus misconception) should hold |
| 10 | The Quiet Thief | 3 | 2 | **2.5** | LOW-MED — BLS CPI and S&P long-run return data are public and exact; two-saver framing is naturally binary | LOW — trap (nominal vs. real rate) is sharp and twist-resistant |
| 6 | How Long Can We Last | 2 | 1 | **1.5** | MED — "how big should the fund be" is a sizing exercise, not inherently a binary dilemma; needs reframing into two explicit fund-size options (e.g. a fixed 3-month target vs. a variance-based target) to pass T1-03 | MED — trap exists but is milder than the others; lowest stakes if it slips |

**Reading this:** #1 and #2 are the only concepts that are simultaneously highest-need on both
axes *and* low pipeline risk — the strongest candidates to send to `case-research` first. #3 and
#4 are high-need but carry real Tier 1 sourcing/balance risk that should be checked *before*
committing to `case-write`, not discovered after. #9 and #6 both need a structural reframe
(binary-dilemma shape) before they're pipeline-ready at all, independent of their lower priority
scores — worth fixing the framing in the concept sheet itself before either goes to research.

---

## Master table — everything in one place, sorted by Priority

| Rank | # | Concept | Cluster | Topic (🔴 = zero-coverage) | Narrative (one-line) | Skill mapped | Rubric / trap | Margin | Topic need | Skill need | **Priority** | Tier 1 risk | Tier 2 risk | Sourcing feasibility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | The Two Offers | 4. Employment & income | 🔴 Job offer comparison | Two real offers (higher salary/smaller bonus vs. lower salary/bigger bonus+match); answer flips on tenure length | System of linear equations (n=2, closes) | Comparing only day-one numbers picks the wrong offer for anyone staying >~1 year | 10–15% | 5 | 5 | **5.0** | LOW — clean binary, dollar figures cite easily | LOW — trap already sharp | HIGH |
| 2 | 2 | The Breakeven Mile | 3. Major purchase decisions | 🔴 Car ownership vs. rideshare | Fixed+low-per-mile ownership vs. zero-fixed/high-per-mile rideshare; find the breakeven mileage | Quotient rule (n=0, closes — calc-track option) | Comparing cost at one arbitrary mileage instead of solving the crossover gives a fragile answer | 8–12% | 5 | 5 | **5.0** | LOW-MED — calc-track version needs a sourced nonlinear depreciation curve | LOW — breakeven trap is twist-resistant | HIGH |
| 3 | 5 | The Real Cost of Breaking It | 2. Debt & credit | Signing/breaking a lease | Low-rent/steep-penalty lease vs. higher-rent/easy-exit lease, compared under "stay" and "break early" | Percent-of-whole (n=2, closes) | Comparing only sticker rent misses effective cost for anyone with real odds of leaving early | 8–12% | 4 | 5 | **4.5** | LOW — binary, lease terms cite easily | LOW — trap holds under a twist | HIGH |
| 4 | 3 | Pay Now or Pay Later | 5. Taxes & tax-advantaged accounts | 🔴 Roth vs. Traditional IRA | Roth (tax now) vs. Traditional (tax later); identical only if tax rate never changes | Exponents w/ order of ops (n=2, closes) | Assuming "Roth is always better" without testing a lower future rate — Traditional must be able to win | 5–10% (tight) | 5 | 4 | **4.5** | MED — T1-09 balance test is genuinely tight; landslide risk without an MCS-46 waiver | LOW-MED — twist (flip future bracket) is built in | MEDIUM-HIGH |
| 5 | 4 | The Deferred Repair | 3. Major purchase decisions | 🔴 Car maintenance (preventive vs. reactive) | Pay for a flagged preventive service now vs. risk a much larger repair later | Conditional/compound probability (n=3/4) | Comparing preventive cost to repair cost directly, ignoring probability weighting | 10–15% | 5 | 3 | **4.0** | MED — needs a real, specific, citable failure-rate table | LOW-MED — sensitivity probe needs genuine multi-year recursion | MEDIUM |
| 6 | 7 | The Minimum-Payment Trap | 2. Debt & credit | Credit card APR / minimum payments | Minimum-only payments vs. a fixed higher payment against a compounding balance | Recursion (thin: Discrete Math/Proof & Recursion) | Computing interest on the original balance only badly underestimates total interest paid | 10–15% | 4 | 3 | **3.5** | LOW — CFPB formulas exact and public, binary framing clean | LOW — trap is sharp | HIGH |
| 7 | 8 | Deductible Roulette | 6. Insurance & risk | Car/renters insurance deductible | Low- vs. high-deductible policy, decided on real claim-frequency data instead of gut feel | Conditional probability (n=3) | Defaulting to "low deductible = safer" without expected value overpays in most scenarios | 8–12% | 3 | 3 | **3.0** | MED — claim-frequency data is usually aggregate, not driver-specific; `{{NEEDS_SOURCE}}` risk | LOW-MED — trap is solid | MEDIUM-HIGH |
| 8 | 9 | Free Money, With Strings | 5. Taxes & tax-advantaged accounts | Employer 401k match | Contribution % chosen around the match cap — free return up to the cap, ordinary return after | Instantaneous rate of change (n=3, thin) | Treating the match as a flat bonus on all contributions overstates benefit past the cap | 10–15% | 3 | 3 | **3.0** | MED-HIGH — not a natural binary dilemma; needs reframing into an explicit A/B to satisfy T1-03 | MED — holds once reframed | HIGH |
| 9 | 10 | The Quiet Thief | 7. Long-horizon growth | Inflation / cost of waiting to save | Two savers, same monthly amount, 10 years apart — shows how much harder catch-up is in real dollars | Exponents w/ order of ops (n=2, reinforces) | Using nominal instead of inflation-adjusted rates understates the late starter's gap | 10–15% | 3 | 2 | **2.5** | LOW-MED — BLS/S&P data public and exact, naturally binary | LOW — trap is sharp and twist-resistant | HIGH |
| 10 | 6 | How Long Can We Last | 1. Cash flow & money mechanics | Emergency fund sizing | Irregular-income household sizes a fund against real income variance, not the generic "3–6 months" rule | Percent/ratio (reinforcement) | Multiplying "3 months × expenses" without checking actual volatility undersizes the fund | 10–15% | 2 | 1 | **1.5** | MED — a sizing exercise, not inherently binary; needs reframing into two explicit fund-size options | MED — trap exists but milder, lowest stakes if it slips | HIGH |
