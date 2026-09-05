# Case Study: The Quiet Thief

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Jordan Reyes is thumb-deep in a retirement-savings app at 11:40 p.m., the phone brightness turned
down so it doesn't wake anyone else in the apartment. A text from Priya Nair is still open above
it — a screenshot of Priya's own retirement account balance, sent with nothing but "look what all
those years add up to 😳." Priya started putting money away not long after college and never
stopped. Jordan meant to do the same and didn't, and tonight is the first night Jordan has actually
opened this app instead of closing the reminder notification.

The plan had always been vague and confident at the same time: *start later, catch up by putting
in more.* Jordan even said it out loud once, to a coworker, like it was obvious. Nobody had ever
actually run the numbers on what "putting in more" would need to mean.

The app has a blank field waiting for a monthly contribution amount. Jordan's cursor blinks in it.
Somewhere between Priya's screenshot and this blank field is a real number — not a vibe, not a
guess, an actual dollar figure — and Jordan can't type anything into that box honestly until it's
found.

---

## Background

A **retirement account** is a savings account meant to be left alone and grown for decades: money
goes in on a regular schedule (here, a fixed amount every month), it earns a return over time the
same way any invested money does, and it is not touched until the saver actually retires.

Growing that money usually means **investing** it in the stock market rather than leaving it in
plain cash, so it can grow at the stock market's own long-run average rate instead of sitting
still — in practice, a saver's monthly contribution buys into a single fund that already holds a
mix of many companies' stock, rather than the saver picking companies one at a time. This case uses
the **S&P 500** — a widely-tracked bundle of 500 large U.S. companies, and the most common
stand-in for "the stock market" generally — as the source for that growth rate; its long-run
average return is one of the two real-world rates Appendix C provides. Because the
money sits untouched for so long, two forces work on it the whole time — investment growth, which
grows the balance, and inflation, which shrinks what each of those dollars can actually buy by the
time they're spent. This case is about keeping both forces in view at once,
not just the first one.

Jordan Reyes and Priya Nair are close friends who started their careers around the same time.
Priya began contributing to a retirement account at age 25 and has never stopped (SEE APPENDIX A).
Jordan meant to do the same thing and didn't, for reasons that don't matter anymore — a decade
passed, and Jordan is only now opening a retirement account at age 35 (SEE APPENDIX B). Both
friends plan to retire at the same standard retirement age, and both intend for their account
balance at that point to be worth the same amount in **today's spending power** — not just the
same number of raw dollars, since inflation quietly shrinks what a dollar buys every year it sits
uninvested or under-invested (SEE APPENDIX C).

Jordan has narrowed the decision to two named contribution plans. **The Bridge Plan** commits
Jordan to whatever higher monthly contribution is actually required, starting now, to close the
ten-year gap and reach the exact same real, inflation-adjusted account balance as Priya's by the
same retirement age Priya is targeting. **The Extended Plan** keeps Jordan's monthly contribution
lower — Jordan is not willing to assume the Bridge Plan's larger monthly number is affordable
without seeing it first — but still reaches that same real target balance, by giving the account
two additional years to grow before Jordan actually retires (SEE APPENDIX B).

Both plans are computed using the same **real rate of return**: the long-run average nominal
return an investor actually earns, adjusted downward for the long-run average rate at which
inflation erodes purchasing power (SEE APPENDIX C). That adjustment is not optional — the whole
point of comparing "today's dollars" is that raw, un-adjusted growth overstates what a dollar
saved today will actually be worth decades from now. The specific ages, contribution amount, and
plan-length figures this case uses are stated scenario choices, disclosed openly rather than
buried in a data table (SEE APPENDIX D). Jordan has one more week to decide before the retirement
app's contribution amount is locked in for the year.

The vocabulary and the "how to…" skills this case will ask you to research are listed in the final
appendix — that is where Challenge 1 sends you (SEE APPENDIX F). All figures in this case are
sourced (SEE APPENDIX E).

---

## Dilemma

You are Jordan Reyes.

Do you:

**A.)** Commit to the **Bridge Plan** — raise your monthly contribution to the exact, higher
dollar amount required, in today's real purchasing power, to reach Priya's same target retirement
balance by retiring at the same age Priya plans to retire **OR**

**B.)** Commit to the **Extended Plan** — keep your monthly contribution at a lower dollar amount,
and reach that same real target retirement balance only by working two additional years past the
age Priya plans to retire

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case
study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would
choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — The real rate of return, derived, not given.** Convert Appendix C's sourced nominal
  average return and sourced average inflation rate from percents to numbers, then derive the
  annual **real (inflation-adjusted) rate of return** using
  `real rate = (1 + nominal rate) / (1 + inflation rate) − 1`. Then convert that annual real rate
  into an equivalent **monthly** real rate using `(1 + annual real rate)^(1/12) − 1`, showing the
  exponential expression evaluated step by step — the fractional exponent first, then the
  subtraction — not a single plugged-in decimal with no shown work.
- **D2 — Priya's real retirement balance.** The **future-value-of-an-annuity formula**
  `FV = PMT × [((1 + r)^n − 1) / r]` models exactly Priya's situation: the same fixed amount
  contributed every month, each contribution then growing at a steady rate for whatever time is
  left until retirement. Using D1's derived monthly real rate, Appendix A's monthly contribution,
  and Appendix A's number of months, compute Priya's account balance in today's real dollars at
  retirement. Show the `(1 + r)^n` exponent term evaluated as its own explicit step before it is
  combined with anything else.
- **D3 — The Bridge Plan's required contribution.** Rearrange D2's formula to solve for the
  monthly contribution instead of the balance:
  `PMT = FV × r / [(1 + r)^n − 1]`. Using D2's target balance, D1's monthly real rate, and
  Appendix B's Bridge Plan number of months, compute the exact monthly contribution the Bridge Plan
  requires. State this amount as a percent increase over Priya's own monthly contribution from
  Appendix A.
- **D4 — The Extended Plan's required contribution, and the margin between the two plans.** Repeat
  D3's method using Appendix B's Extended Plan number of months (two additional years) instead of
  the Bridge Plan's. Then compute the percent by which the Extended Plan's required monthly
  contribution is lower than the Bridge Plan's D3 figure — this percent is the real, computed gap
  between the two plans this case asks you to weigh.
- **D5 — The nominal-rate comparison.** Recompute D3's Bridge Plan monthly contribution one more time,
  but this time use Appendix C's un-adjusted **nominal** rate of return in place of D1's derived
  real rate. Show this "nominal-rate" contribution amount side by side with D3's correct,
  real-rate contribution amount, and compute the percent by which the nominal-rate figure
  understates the true amount required.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Priya's Early Plan

The account Jordan is trying to match.

| Quantity | Value |
|---|---|
| Priya's age when she started contributing | 25* |
| Priya's monthly contribution amount | $400/month [MA2] (stated modeling assumption — see Appendix D) |
| Shared target retirement age (both friends) | 67 [S1] |
| Number of months Priya's account grows before retirement | 504 months (67 − 25 = 42 years × 12) |

*Narrative detail, stated in Overview/Background — not independently researched; see
RESEARCH_LOG.md.

**Social Security** is a separate U.S. federal program that pays retirees a monthly benefit; that
benefit is simply larger the longer someone waits to start claiming it, up to a point, and [S1]'s
"full retirement age" (67) is the specific age most commonly used as the standard target when
planning around that program. This case borrows that one age only as a shared, standard target age
for both friends' own separate savings — it is not saying Priya's or Jordan's account is a Social
Security benefit; each account is a private one each of them controls.

Referenced from Background and forces D2's future-value computation.

---

## Appendix B — Jordan's Two Plans

The two candidate contribution plans this case's Dilemma asks you to choose between.

| Quantity | Value |
|---|---|
| Jordan's age now (ten years after Priya started) | 35* |
| Bridge Plan retirement age (same as Priya's) | 67 [S1] |
| Bridge Plan number of months Jordan's account grows | 384 months (67 − 35 = 32 years × 12) |
| Extended Plan retirement age (two years past Priya's) | 69 (67 + 2, see Modeling Assumption MA3) |
| Extended Plan number of months Jordan's account grows | 408 months (69 − 35 = 34 years × 12) |

*Narrative detail, stated in Overview/Background — not independently researched; see
RESEARCH_LOG.md.

Referenced from Background and forces D3's and D4's required-contribution computations.

---

## Appendix C — Growth and Inflation Assumptions

The two real-world rates that D1's derivation combines, and the mechanism (inflation) this case is
named for.

| Quantity | Value |
|---|---|
| Long-run average annual nominal rate of return, diversified U.S. stock index (S&P 500, dividends reinvested) | 10% (rounded) [S2] |
| Long-run average annual U.S. inflation rate (Consumer Price Index, CPI-U) | 3.1% [S3] |

A **dividend** is a small cash payment a company sometimes sends to anyone who owns its stock, out
of its own profits; "dividends reinvested" means that cash is automatically used to buy more stock
instead of being paid out, which is the standard, complete way a long-run stock-index return like
[S2] is measured. The **Consumer Price Index (CPI-U)** [S3] is built by regularly checking the
price of the same fixed list of everyday purchases — groceries, rent, gas, and the like — across
many U.S. cities and tracking how that total price changes year over year; that year-over-year
change is what "the inflation rate" means throughout this case.

"Nominal" here means the raw, un-adjusted growth rate an account actually earns; it is the number
before inflation is taken into account. "Real" (used throughout this case) means that same kind of
number after inflation's effect has been removed, so it reflects actual buying power rather than a
raw dollar count.

Referenced from Background and forces D1's real-rate derivation, D2–D4's growth computations, and
D5's nominal-vs-real comparison.

---

## Appendix D — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Priya's and Jordan's starting ages | Priya 25, Jordan 35 (a ten-year gap) | Chosen narrative constants to set up a clean, round ten-year late start — the exact scenario the concept behind this case is built to examine. Not tied to any real person. | Every case computation scales with the size of this gap; a smaller gap would shrink the dollar difference between Priya's and Jordan's plans, and a larger gap would grow it, but it does not change the direction of the case's point — starting later always costs more in real terms. |
| MA2 | Both savers' planned monthly contribution amount | $400/month | A common, round, early-career monthly retirement-contribution figure used for comparability between the two friends. The case is deliberately built around the *mechanics* of catching up (timing plus inflation), not around what a specific income level can or cannot afford, so this figure is fixed as a scenario constant rather than derived from a specific salary. | This figure scales every dollar amount in the case (Priya's target balance, and both of Jordan's required contributions) up or down proportionally, but it does **not** change the percent margin between the Bridge and Extended Plans (D4), nor the percent understatement computed in D5 — those are ratios between quantities that both scale by the same factor, so they are unaffected by this assumption's exact value. |
| MA3 | Extended Plan's retirement-age delay | 2 years past Priya's retirement age | A deliberately modest, realistic delay — not a decade, not a single year — chosen so the Extended Plan is a genuine, comparably-weighted alternative to the Bridge Plan rather than an obviously inferior or obviously superior one. | Changing this delay changes the size of the gap between the Bridge and Extended Plans' required contributions (D4) — a longer delay narrows the gap further, a shorter delay widens it — without changing which plan asks for more money sooner. |

---

## Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Social Security full retirement age, for anyone born in 1960 or later | 67 | Social Security Administration — [Benefits Planner: Retirement Age and Benefit Reduction](https://www.ssa.gov/benefits/retirement/planner/agereduction.html) | current policy, no further phase-in scheduled | HIGH |
| S2 | Long-run average annual return, diversified U.S. equity ("equity" here just means stock) index (S&P 500), dividends reinvested | 10% (rounded; underlying figures 9.98%–10.22%) | The Motley Fool — [What Is the Average Stock Market Return?](https://www.fool.com/investing/how-to-invest/stocks/average-stock-market-return/) (9.98%/yr since 1928); officialdata.org — [S&P 500 since 1928](https://www.officialdata.org/us/stocks/s-p-500/1928) (10.22%/yr since 1928, dividends reinvested) | accessed 2026-09-04 | MEDIUM |
| S3 | Long-run average annual U.S. inflation rate (Consumer Price Index, CPI-U) | 3.1% | Federal Reserve Bank of Minneapolis — [Consumer Price Index, 1913–](https://www.minneapolisfed.org/about-us/monetary-policy/inflation-calculator/consumer-price-index-1913-) | index series covers 1913–2025, accessed 2026-09-04 | HIGH |

The **Federal Reserve Bank of Minneapolis** is one of twelve regional banks that make up the
U.S. Federal Reserve System (the country's central bank); like the other eleven, it publishes its
own public economic research and data tools, including the historical CPI series cited above.

Deriving the real (inflation-adjusted) rate of return from S2 and S3 above — and everything that
follows from it — is Challenge 3's own D1–D5 work; it is not pre-computed here. Full research
trail and rejected leads are in `RESEARCH_LOG.md`.

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Exponent (also Power)
- Base
- Percent

**"How to…" questions**

- How to evaluate an exponential expression
- How to evaluate an expression with multiple operations with exponents (Order Of Operations)
- How to convert percents to numbers
- How to find the percent of a number

---

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
