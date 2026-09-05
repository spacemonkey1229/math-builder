# Case Study: Free Money, With Strings

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

The enrollment portal is still open in the next browser tab, a progress bar frozen at "Step 2 of 3: Retirement Contributions." Devon Okafor's new laptop still has the plastic film on one corner of the trackpad. Three days into the job, and this is the first form nobody in orientation actually walked through — HR just said "you have until Friday" and moved on to parking passes.

A notification slides in from the banking app on Devon's phone: the automatic minimum payment on the student loan cleared this morning, same as it does every month, quietly, without asking permission. Devon minimizes it and goes back to the portal's contribution-percentage field, cursor blinking in an empty box.

A coworker two desks over, headphones in, catches Devon's expression and leans back in her chair without taking them out. "First time doing the 401(k) thing?" she mouths, then holds up a hand — five fingers, then one more — and points at the screen before turning back to her own monitor.

Devon doesn't know what that means yet. The portal wants one number: a percentage of every paycheck, starting the very next one. Whatever gets typed into that box today doesn't change again until next year's open enrollment. Devon rereads the plan summary PDF for the third time, opens a blank note instead, and starts typing numbers before deleting all of them.

The cursor keeps blinking in the empty box.

---

## Background

Devon Okafor started as a Junior Systems Analyst this week, the first full-time job since finishing a bachelor's degree. The role carries a starting annual base salary (SEE APPENDIX A).

The employer offers a **401(k) plan** — a retirement savings account, named after the section of U.S. tax law that created it, into which Devon can have a percentage of every paycheck deposited automatically, invested for growth until retirement decades away. This particular plan offers a **matching contribution**: a real, separate deposit of the company's own money — not a bonus, not a reimbursement, just free money added on top — for every dollar Devon contributes from each paycheck, up to a stated cap expressed as a percentage of *Devon's own* salary contribution (not a percentage of the combined total once the match is added in). Beyond that cap, the company match stops entirely — Devon's own contributions still grow the account, but the employer stops adding anything (SEE APPENDIX A). The plan's enrollment portal only accepts changes once a year, during a scheduled **open enrollment period** — a fixed window most employers use for benefit elections — so the contribution percentage chosen this week is locked in until the next one, roughly a year away.

Devon also carries a **federal student loan** — a loan for college costs, backed and administered by the U.S. government rather than a bank, at a fixed interest rate set once and never changing (SEE APPENDIX B). Like most loans, it comes with a required minimum monthly payment set by a **standard payoff schedule** — a fixed plan that spreads the balance and its interest evenly over a set number of years so it reaches exactly zero on time. That minimum payment is identical no matter which strategy Devon picks, so it is background context rather than a number either strategy's math needs. Anything paid beyond that minimum is entirely optional and entirely Devon's choice where to send it instead.

Devon's coworkers have nicknamed the two realistic contribution strategies under discussion in the break room. The first, **Match & Move**, contributes exactly enough to the 401(k) to capture the full employer match and not a dollar more, then redirects every other available dollar toward extra, above-minimum payments on the student loan. The second, **Stack & Grow**, contributes well beyond the match cap — at the level a widely publicized retirement-savings guideline recommends (SEE APPENDIX A) — into the 401(k), and pays only the required minimum on the loan.

Because the match cap creates a hard line — every dollar below it gets matched, every dollar above it does not — the *return Devon earns on the next dollar contributed* is not a single steady number. It is one rate below the cap and a different, lower rate above it, changing abruptly right at that one specific dollar amount rather than tapering off gradually. Mathematicians call a rate defined at, and changing sharply around, one specific point an **instantaneous rate of change** — Challenge 3's D3 asks you to compute and compare that rate on both sides of the cap, for each strategy.

Devon has no other savings goal competing for these dollars right now, no employer stock plan, and no ability to renegotiate either the match formula or the loan's interest rate (SEE APPENDIX C for the modeling assumptions the comparison rests on). All figures in this case are sourced in (SEE APPENDIX E). For optional background reading on the math concepts involved, not required for any Challenge, SEE APPENDIX D.

The vocabulary and "how to…" skills this case will ask of you are listed in **Appendix F** — that is where Challenge 1 sends you.

---

## Dilemma

You are Devon Okafor.

Do you:

**A.)** Choose **Match & Move** — contribute only up to the employer match cap, and direct every extra available dollar toward paying down the student loan faster than the minimum OR

**B.)** Choose **Stack & Grow** — contribute well beyond the match cap into the 401(k), and pay only the minimum required on the student loan

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    - **D1 — A contribution ledger for each strategy**, showing, per pay period and per year: Devon's own 401(k) contribution, the employer match dollars earned, and the dollar amount redirected to the "extra" destination (loan paydown for Match & Move; additional 401(k) contribution for Stack & Grow) — with every percentage converted to a dollar amount and shown as its own line. (Assume Devon is paid twice a month — 24 pay periods a year — for the per-pay-period rows; this choice does not change any D2-D4 total, since it applies equally to both strategies.)
    - **D2 — A ten-year projected value for each strategy's two accounts** (the 401(k) balance and the loan-payoff value, or the larger 401(k)-only balance, as applicable), using the compound-growth calculation from Appendix C's stated growth assumption, with the exponent step of the calculation shown explicitly, not just the final number.
    - **D3 — A marginal-return table** comparing the rate of return earned on the last dollar contributed just *below* the employer match cap to the rate of return earned on the next dollar contributed just *above* it, for both strategies — computed as the match percentage (if any) that dollar receives immediately, on top of whichever ongoing annual growth rate from Appendix C applies to it — and naming, in your own words, why this rate changes abruptly right at the cap rather than gradually.
    - **D4 — A total ten-year value comparison and recommendation**, combining each strategy's two account values from D2 into one total figure per strategy, stating the dollar and percent margin between them, and naming which strategy your data supports.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Job and the 401(k) Match

| | Value |
|---|---|
| Role | Junior Systems Analyst |
| Annual base salary | $72,744/yr [S1] |
| Employer 401(k) match rate | 50% of each dollar contributed [S2] |
| Employer match cap | 6% of salary contributed [S2] |
| "Stack & Grow" contribution rate | 15% of pay, including any employer match [S3] |
| Annual IRS contribution limit (401(k)) — the technical term for this is the "elective deferral" limit, meaning the most an employee may choose to have withheld from their own paychecks in a year | $24,500 [S4] — shown for reference only; neither strategy approaches this limit at the salary above |

---

## Appendix B: Devon's Student Loan

| | Value |
|---|---|
| Loan type | A federal student loan (a government-backed loan taken out for college, at a fixed rate set once and never changing) |
| Outstanding balance | $28,613 [S5] |
| Fixed annual interest rate | 6.39% [S6], for loans first disbursed July 1, 2025 through June 30, 2026 |
| Minimum monthly payment | Set by a standard 10-year payoff schedule; already budgeted for under both strategies, so it is the same cost either way and does not enter D1-D4's math |

---

## Appendix C: Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Assumed average annual investment growth rate applied to 401(k) balances over the ten-year horizon | 10% per year [S7] | No one can know a real future investment return in advance; this case fixes a single assumed annual growth rate, disclosed openly, so both strategies can be compared on the same footing. The value is a round figure based on the **S&P 500** (a widely-tracked index of 500 large U.S. companies' stock, commonly used as a stand-in for "the U.S. stock market")'s long-run historical **nominal** average annual return — "nominal" here means the raw, un-adjusted growth rate actually earned, before accounting for inflation — which is not a promise of future results. | The answer is sensitive to this value. |
| MA2 | Comparison horizon | 10 years | A round, plausible early-career planning window — long enough for compounding to matter, short enough that Devon's actual tenure at this employer is a reasonable real-world horizon to reason about. | The answer is sensitive to this value. |
| MA3 | Extra dollars redirected under Match & Move are treated as earning a guaranteed return equal to the loan's own interest rate for the full ten-year horizon, whether or not the loan itself is still outstanding the whole time | Loan's stated rate (Appendix B) | Paying extra principal on a fixed-rate loan is mathematically equivalent to earning a guaranteed return equal to that loan's interest rate, since it is interest that would otherwise accrue and compound against Devon. Because the extra-dollar amount is large relative to the loan balance, Devon's loan is likely paid off well before year ten; this case models Devon then continuing to place those same dollars somewhere just as safe and just as guaranteed — an ordinary bank savings account, or a certificate of deposit (CD, a bank product that pays a fixed, guaranteed interest rate in exchange for leaving the money untouched for a set period) — paying that same guaranteed rate, rather than switching to the assumed market rate — a disclosed simplification that keeps "guaranteed" meaning guaranteed for the entire comparison, so the two strategies differ only in *where* the extra dollars go, not in when a rate change happens. | N/A — this is a modeling simplification tied to the already-sourced loan rate, not an independent value with its own sensitivity range. |

---

## Appendix D: Learn More

Want to go beyond the required math? These are real, freely available resources — not required for any Challenge, but useful if you want more background.

- [Compound interest — Wikipedia](https://en.wikipedia.org/wiki/Compound_interest) — background on how the exponential-growth calculation in Challenge 3's D2 works.
- [401(k) — Wikipedia](https://en.wikipedia.org/wiki/401(k)) — background on how an employer match plan works generally, for context on Appendix A.
- [Employer matching program — Wikipedia](https://en.wikipedia.org/wiki/Employer_matching_program) — background specifically on how match caps and match rates are structured.
- [Rate of change (mathematics) — Wikipedia](https://en.wikipedia.org/wiki/Rate_of_change_(mathematics)) — background on the "instantaneous rate of change" idea Background introduces and Challenge 3's D3 asks you to apply.
- [Retirement Topics — 401(k) and Profit-Sharing Plan Contribution Limits — IRS](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits) — why a 401(k) gets special tax treatment in the first place, and why the IRS caps how much can go in each year (Appendix A, Source S4).
- [Annual enrollment — Wikipedia](https://en.wikipedia.org/wiki/Annual_enrollment) — why employers only let you change your 401(k) contribution rate (and other benefit elections) during a specific window each year, rather than any time.
- [Subsidized and Unsubsidized Loans — Federal Student Aid, U.S. Dept. of Education](https://studentaid.gov/understand-aid/types/loans/subsidized-unsubsidized) — what makes Devon's loan "federal" rather than private, and what protections/terms that guarantees (Appendix B, Source S6).
- [Amortization schedule — Wikipedia](https://en.wikipedia.org/wiki/Amortization_schedule) — how a fixed loan payment is split between interest and principal each month, and why more of it goes to principal over time (Appendix B).
- [Certificate of deposit — Wikipedia](https://en.wikipedia.org/wiki/Certificate_of_deposit) — what makes a CD different from a regular savings account (a fixed term and rate, in exchange for not withdrawing early).

**Employer match mechanics below the cap, in plain terms:** the match in Appendix A only ever matches dollars Devon actually contributes, up to 6% of pay — contributing 3% of pay gets a match on that 3%; contributing 0% gets no match at all. There's no partial credit for "meaning to" contribute; the match tracks Devon's real contribution dollar-for-dollar until it hits the 6% ceiling, then stops entirely.

## Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Entry-level Systems Analyst annual salary, national average | $72,744/yr | Salary.com — [Entry Level Systems Analyst Salary](https://www.salary.com/research/salary/position/entry-level-systems-analyst-salary) | As of September 1, 2026 | MEDIUM — real, dated national compensation-data aggregator; a proxy for the case's fictional "Junior Systems Analyst" title. |
| S2 | Most common employer 401(k) matching formula | 50 cents per dollar contributed, on the first 6% of pay | ASPPA-Net — [What Are the Most Common Matching Formulas?](https://www.asppa-net.org/news/2021/6/what-are-most-common-matching-formulas/), reporting Vanguard "How America Saves" data | 2020 plan-year data (most recent published formula-prevalence breakdown found; Vanguard's newer 25th-edition report publishes only the average match rate, 4.7%, not a formula breakdown — see RESEARCH_LOG.md) | MEDIUM — real, attributed republication of primary data from Vanguard, a **recordkeeper** (the company a 401(k) plan hires to track balances, contributions, and match calculations for its employees); the underlying survey year (2020) is older than ideal, disclosed here rather than hidden. |
| S3 | Recommended total retirement savings rate, including employer match | 15% of **pre-tax pay** (salary before any taxes are withheld, not take-home pay) | Fidelity — [Retirement Guidelines](https://www.fidelity.com/viewpoints/retirement/retirement-guidelines) | Live guidance page, accessed 2026-09-04 | HIGH — primary source (a major retirement-plan provider's own published guidance), unambiguous units, explicitly states its own assumptions (starting age 25, retiring at 67, 45% income replacement). |
| S4 | 2026 IRS 401(k) employee elective deferral contribution limit | $24,500/yr | Internal Revenue Service — [Retirement Topics – 401(k) and Profit-Sharing Plan Contribution Limits](https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits) | 2026 | HIGH — primary government source, unambiguous units. Used for reference only; not load-bearing to the dilemma. |
| S5 | Average federal education loan debt, bachelor's degree borrowers | $28,613 | Education Data Initiative — [Average Debt for a Bachelor's Degree](https://educationdata.org/average-debt-for-a-bachelors-degree) | Updated November 24, 2025; covers AY 2025-26 | MEDIUM — a well-established, frequently-cited education-finance data aggregator; not a primary government release, but methodology and update date are stated. |
| S6 | Federal Direct Unsubsidized Loan interest rate, undergraduate | 6.39%/yr | Federal Student Aid (U.S. Dept. of Education) — [Interest Rates for Direct Loans First Disbursed Between July 1, 2025 and June 30, 2026](https://fsapartners.ed.gov/knowledge-center/library/electronic-announcements/2025-05-30/interest-rates-direct-loans-first-disbursed-between-july-1-2025-and-june-30-2026) | Effective for loans disbursed July 1, 2025 – June 30, 2026 | HIGH — primary government source, dated, unambiguous, fixed for the life of a loan disbursed in this window. |
| S7 | S&P 500 long-run historical average annual nominal return, counting reinvested dividends (cash payouts companies make to stockholders, assumed reinvested to buy more stock) | 10.47%/year since 1926 | OfficialData.org — [S&P 500 Returns since 1926](https://www.officialdata.org/us/stocks/s-p-500/1926) | Accessed 2026-09-04, covers 1926–2026 | MEDIUM — a well-documented historical-returns calculator/aggregator, not a primary index provider; used only as the disclosed historical basis for Modeling Assumption MA1, never presented as a guaranteed future return. Rounded to 10% in MA1 for a clean modeling figure. |

**Derivations shown:**
- Both strategies' 6%-of-salary employee contribution: $72,744 [S1] × 6% [S2] = $4,364.64/yr.
- Employer match on that (both strategies get it): $4,364.64 × 50% [S2] = $2,182.32/yr.
- Stack & Grow's total employee contribution: $72,744 [S1] × 15% [S3] = $10,911.60/yr.
- Match & Move's "extra" dollars redirected to the loan: $72,744 [S1] × (15% [S3] − 6% [S2]) = $6,546.96/yr.

## Appendix F — "How To…" Math Questions To Research

**Vocabulary**

Percent · Exponent (also Power) · Instantaneous Rate Of Change

**How to…**

- How to find the percent of a number
- How to convert percents to numbers
- How to evaluate an exponential expression
