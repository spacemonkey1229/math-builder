Case Study: The Minimum-Payment Trap
MS | Math | Case Study | 2026 | Adventure

## Overview

The banking app is still open from her lunch break, the cursor blinking in a field labeled "Pay other amount." Priya Shenoy taps out of it, taps back in, and taps out again. Behind her, the break room microwave beeps three times before someone else claims it. Her phone buzzes with a calendar reminder she set months ago and mostly ignores now: *Talk to a lender — next spring.* She and her partner have been saying "once the card is under control" for longer than either of them wants to admit out loud.

The app shows two buttons, side by side, the same size, the same shade of blue: "Pay minimum" and "Pay other amount." One of them is already filled in with a number the bank chose for her. The other is blank, waiting.

Her charge nurse badge is still clipped to her scrub top from the shift she just left. She has exactly one break left before she has to decide, sign back in, and go stand in a supply closet for ten minutes pretending to count gauze.

Her thumb hovers over the blank field.

## Background

Priya Shenoy has worked as a charge nurse for six years, and the balance sitting on her card did not come from one bad decision — it came from a stretch last year when her hours were cut and a string of ordinary costs (rent, a car repair, a month of groceries) went on the card one at a time because there was nothing else to put them on. Her hours are back to normal now. The debt is not.

She and her partner want to sit down with a mortgage lender for a pre-approval conversation eighteen months from now, and the card balance is the specific thing standing between "we're ready to ask" and "not yet" — the number they've told each other they need to see, on the statement, the month they finally make that appointment (SEE APPENDIX A). Neither of them has asked a lender to confirm exactly what "meaningfully lower" needs to mean; it's the goalpost they set for themselves, not a number a bank gave them. Every month the card is open, her issuer runs the same two numbers and shows them to her: the minimum payment required this cycle (SEE APPENDIX B), calculated fresh off whatever the balance happens to be that month, and a second, fixed number the card statement is required by federal disclosure rules to show — the flat monthly payment that would clear the entire balance in exactly three years if she paid that same amount every single month (SEE APPENDIX C). The vocabulary and "how to…" procedures needed to work through those figures are listed in (SEE APPENDIX D). All figures in this case are cited in (SEE APPENDIX E).

The two numbers look similar today, both somewhere in the low hundreds of dollars. Priya's cousin, who works in a call center for a different card issuer, told her once that the two numbers only look similar in month one — that the gap between them is designed to widen, not stay put, because one of them recalculates itself smaller every time the balance drops, and the other one does not move at all. Priya doesn't fully believe that yet; she wants to see it in the actual numbers before she decides which button to tap this month, and every month after, for as long as it takes.

She has already decided she isn't refinancing, transferring the balance to a new card, or asking a lender for anything before the eighteen-month mark — those are separate conversations for a later day. Tonight's decision is narrower: does she keep tapping "Pay minimum," or does she commit to tapping "Pay other amount" and typing in the fixed payment from Appendix C, every month, no matter how small the required minimum drops to?

## Dilemma

You are Priya Shenoy.
Do you:
A.) Tap "Pay minimum" every month, letting the required payment shrink as the balance shrinks — The Minimum Track OR
B.) Tap "Pay other amount" every month and enter the fixed payment from Appendix C, holding it constant even as the required minimum drops below it — The Fixed Push

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A recursively defined monthly balance model for EACH strategy: state the base case (Month
    0 balance, from Appendix A) and the recursive step (Month n balance = Month n-1 balance x (1 +
    monthly interest rate) - that month's payment) for The Minimum Track and for The Fixed Push,
    writing each strategy's own payment rule into its recursive step using Appendix B's minimum-
    payment formula and Appendix C's fixed payment.
    D2. An eighteen-month month-by-month table for EACH strategy, built by iterating your D1
    recursive formula one month at a time: month number, that month's interest charged, that
    month's payment, how much of the payment went to principal, and the ending balance — every
    row computed from the PREVIOUS row's ending balance, never from Appendix A's original balance.
    D3. An eighteen-month totals comparison, summed from your D2 tables: total interest paid and
    total principal paid under each strategy over the eighteen months, plus the percent margin
    between the two strategies' eighteen-month interest totals, with your arithmetic shown.
    D4. Continuing your D1 recursive model past month eighteen, find how many total months (and
    years) The Minimum Track takes to reach a $0 balance, and the total interest paid over that
    ENTIRE payoff — contrasted with The Fixed Push's own total months and total interest to reach
    $0. Then, for EACH strategy, recompute both figures a second way: freeze every month's interest
    charge (and, for The Minimum Track, the minimum-payment formula's balance term) at Appendix A's
    original $7,756 instead of recalculating it on that month's own ending balance, and report the
    resulting wrong total months and wrong total interest for each strategy. A written explanation
    of why this shortcut is wrong, and whether it makes total months and total interest come out
    too high or too low, for EACH strategy separately — the two quantities do not necessarily move
    in the same direction, and do not necessarily move the same way for both strategies.
    D5. A percent breakdown for each strategy's eighteen-month totals from D3: of every dollar
    paid, what percent went to interest and what percent went to principal.
    D6. An original visual display (a line graph or bar chart) comparing the two strategies' month-
    by-month balances across the eighteen months, built from your D2 figures.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Her Card, Today

Referenced in Background and Challenge 3 (D1, D2, D4).

| | Value |
|---|---|
| Outstanding balance (Month 0) | $7,756 [S1] |
| Annual Percentage Rate (APR) | 25.2% [S2] |
| Monthly interest rate (APR / 12) | 2.1% (25.2% / 12), derived |

## Appendix B — How Her Minimum Payment Is Calculated

Referenced in Background and Challenge 3 (D1, D2, D4). This is the formula her issuer prints on
the back of every statement, and it is the formula The Minimum Track uses every month.

| Minimum payment due this cycle | = the GREATER of: |
|---|---|
| Flat-fee floor | $40 [S3] |
| Percent-plus-interest calculation | 1% of the statement balance, plus that cycle's accrued interest and any late fees [S3] |

**Note on issuer variation:** not every card uses this exact formula. Some issuers use a flat 1-3%
of balance with no separate interest term; others use a flat dollar floor of $25 or $35 instead of
$40 [S3]. This case uses one major issuer's own published formula as the representative real-world
version.

## Appendix C — The Statement's Required Disclosure

Referenced in Background and Challenge 3 (D1, D2, D4). Federal disclosure rules require every
credit card statement to show a fixed monthly payment amount that would clear the entire balance
shown on that statement within 36 months, calculated once, off that statement's balance and APR
[S4].

| | Value |
|---|---|
| Fixed monthly payment to clear Appendix A's balance in exactly 36 months | $309.20 [S4], derived from [S1] and [S2] |

This is the number The Fixed Push commits to paying every month — not recalculated later, even
after the balance drops far below its original $7,756.

## Appendix D — "How To…" Math Questions To Research

**Vocabulary terms**

- Recursive Formula
- Base Case
- Percent

**"How to…" questions**

- How to write a recursive formula for a sequence
- How to find the percent of a number

## Appendix E — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | National average credit card balance among Americans carrying any card debt | $7,756 | LendingTree — [2026 Credit Card Debt Statistics](https://www.lendingtree.com/credit-cards/study/credit-card-debt-statistics/) | Q1 2026 | MEDIUM |
| S2 | Average APR, general-purpose credit cards | 25.2% | CFPB — [The Consumer Credit Card Market 2025](https://files.consumerfinance.gov/f/documents/cfpb_consumer-credit-card-market-report_2025.pdf) | 2024 data, published 2025-12-30 | HIGH |
| S3 | Minimum payment formula: greater of a flat $40 floor, or 1% of statement balance plus that cycle's interest and late fees | $40 floor / 1% + interest | Chase — [How To Calculate Your Minimum Credit Card Payment](https://www.chase.com/personal/credit-cards/education/basics/how-to-calculate-your-minimum-credit-card-payment) | accessed 2026-09-04 | HIGH |
| S4 | CARD Act requirement that statements disclose the fixed monthly payment needed to clear the balance in 36 months | regulatory requirement | CFPB — [Regulation Z, Appendix M1 to Part 1026 — Repayment Disclosures](https://www.consumerfinance.gov/rules-policy/regulations/1026/m1/) | accessed 2026-09-04 | HIGH |

The $309.20 fixed payment in Appendix C is derived from S1's balance and S2's APR using the
standard fixed-payment loan formula (the same calculation the CARD Act requires issuers to run for
this box) — not a plugged formula the student needs to reproduce; see `RESEARCH_LOG.md` for the
arithmetic. See `RESEARCH_LOG.md` for the full search trail.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
