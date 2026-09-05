# Research Log — The Minimum-Payment Trap

Stage 3 (`case-research`) run on `cases/the-minimum-payment-trap/`. 5 `{{NEEDS_SOURCE}}`
placeholders enumerated (P01-P04, plus one derived monthly-rate row). Worked in load-bearing order:
the starting balance and APR first (everything else is computed from them), then the minimum-
payment formula, then the CARD Act 36-month disclosure and its derived dollar value.

## P01 — Starting credit card balance

**Searched:**
- "average credit card balance 2026 Americans carrying debt"
- "Federal Reserve New York household debt credit card average balance per borrower 2025 2026"
- "CFPB average revolving credit card balance report"

**Fetched directly:**
- `https://www.newyorkfed.org/newsevents/news/research/2025/20251105` (NY Fed Household Debt and
  Credit Report, Q3 2025, published 2025-11-05) — real, dated, primary source. Reports aggregate
  credit card balances ($1.23 trillion, Q3 2025) but does NOT break out an average balance per
  borrower or per indebted household — aggregate-only, not usable for a single representative
  balance figure.
- `https://www.lendingtree.com/credit-cards/study/credit-card-debt-statistics/` — LendingTree's own
  analysis of anonymized credit reports from 400,000+ users. States: "the national average card
  debt among Americans with any type of debt in Q1 2026 was $7,756, up 1.9% from $7,615 in Q1
  2025." Also notes (citing Federal Reserve survey data) that only 45% of adult cardholders carried
  a balance for at least one month in the past year, but does not separately break out an average
  balance *conditional on* revolving — the $7,756 figure is the average among those who report any
  card debt, the closest available proxy for "a representative starting balance for a cardholder
  who carries a balance."

**Outcome:** SOURCED as [S1], $7,756, MEDIUM confidence (well-attributed private aggregator with a
large, dated panel; not a government statistical release, and a population average standing in for
one fictional cardholder's specific balance, not a measurement of her account).

## P02 — Average APR

**Searched:**
- "CFPB average credit card APR 2025 2026 consumer credit card market report"
- "credit card interest rates 2024 2025 CARD Act report"

**Fetched directly:**
- `https://www.consumerfinance.gov/data-research/research-reports/the-consumer-credit-card-market-2025/`
  — CFPB's own landing page for its seventh biennial CARD Act report to Congress, "The Consumer
  Credit Card Market 2025," published 2025-12-30. Landing page confirms the report and date but
  does not itself state the APR figure in fetchable text.
- `https://www.orrick.com/en/Insights/2026/01/Trends-and-Takeaways-from-the-2025-Credit-CARD-Act-Report`
  — a law firm's published summary of the same CFPB report, quoting it directly: "The average APR
  for general-purpose cards reached 25.2 percent, the highest since 2015, mostly due to changes in
  the underlying prime rate," for 2024 data. Also confirms industry-wide interest charges rose to
  $160 billion in 2024 from $105 billion in 2022 (used only as narrative color, not a case figure).
- Cross-checked against an older CFPB analysis (NBC News, 2024-02-22 article) reporting 22.8% for
  2023 data — confirms the 25.2% figure is the more recent, correct year (2024 data, not 2023) and
  is not a stale or superseded number.

**Outcome:** SOURCED as [S2], 25.2%, HIGH confidence (primary federal regulator report, dated,
unambiguous, the figure the case needs directly rather than a proxy).

## P03 — Minimum payment formula

**Searched:**
- "CFPB minimum payment formula credit card 1% of balance plus interest floor $25 $35"
- "consumerfinance.gov minimum payment calculation explainer"
- "Chase Citi Discover how minimum payment calculated"

**Found and considered:**
- CFPB Regulation Z, Appendix M1 to Part 1026 (Repayment Disclosures) — a regulatory illustration
  uses "2 percent of the outstanding balance on the account or $20, whichever is greater" as an
  EXAMPLE for computing the repayment-disclosure box, but the regulation itself does not mandate
  any specific minimum-payment formula for issuers to actually use in billing — it only requires
  disclosure of *whatever* formula an issuer already uses. Considered as a case figure but rejected
  in favor of a real issuer's own published, currently-used formula (a stronger, more concrete
  citation than a regulatory illustration that issuers are not required to follow).
- `https://www.chase.com/personal/credit-cards/education/basics/how-to-calculate-your-minimum-credit-card-payment`
  — fetched directly. Chase's own page states its minimum payment is "a flat fee of $40 or 1% of
  your statement balance, plus any interest and late fees since the last billing cycle — whichever
  is greater" (with balances under $40 paid in full). The same page discloses that other issuers use
  different methods: a pure percentage (1-3% of balance), a pure flat fee ($25, $35, or another
  fixed amount), or Chase's own interest-plus-percentage method — confirming this is one real,
  documented, currently-in-use formula, not necessarily universal.

**Outcome:** SOURCED as [S3], HIGH confidence (a major issuer's own published formula, a primary
source for its own product), $40 floor / 1% of balance + interest. The case discloses, in Appendix
B's own "Note on issuer variation," that not every card uses this exact formula.

## P04 — The 36-month fixed-payment disclosure amount

**Searched/fetched:**
- `https://www.consumerfinance.gov/rules-policy/regulations/1026/m1/` — CFPB Regulation Z, Appendix
  M1 to Part 1026, fetched directly. Confirms the CARD Act requires issuers to calculate and
  disclose, on every statement: (1) the time and total cost to pay off the balance making only
  minimum payments, (2) "the estimated monthly payment amount that would be required to pay off the
  outstanding balance shown on the statement within 36 months," and its total cost, and (3) the
  interest savings from paying the 36-month amount instead of the minimum. This is a real, primary,
  mandatory federal disclosure requirement — not a case-invented framing.

**Derivation (shown in full, not asked of the student — see case.json.sources[S4].note):**
Standard fixed-payment loan-amortization formula, applied to [S1]'s $7,756 balance at [S2]'s 25.2%
APR (monthly rate r = 0.252/12 = 0.021), solved for a 36-month payoff:

```
payment = balance x r / (1 - (1 + r)^-36)
        = 7756 x 0.021 / (1 - 1.021^-36)
        = 162.876 / 0.526558...
        = 309.1982...
        ≈ $309.20
```

Verified by simulation (`sensitivity_model.py`): paying exactly $309.20/month against this balance
and rate reaches a $0.00 ending balance at exactly month 36, with $3,375.11 in total interest paid
over those 36 months.

**Outcome:** SOURCED/DERIVED as [S4]. The regulatory requirement itself is HIGH confidence, primary,
dated (accessed 2026-09-04); the specific $309.20 dollar figure is a derivation from S1 x S2 using a
standard, well-known formula (the same one CFPB's own rule requires issuers to run), not a
separately published number anywhere.

## Note on why no Modeling Assumption was needed

Unlike `cases/the-deferred-repair`, this case needed no `Modeling Assumptions` block: every figure
the case's math depends on (starting balance, APR, minimum-payment formula, 36-month payment) is
either a real published statistic, a real regulatory requirement, a real issuer's own published
formula, or a straightforward derivation from those three using a standard, checkable formula. No
NOT-FOUND figure forced a stated scenario assumption this pass.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Starting balance | SOURCED (S1) | $7,756 | MEDIUM |
| P02 | APR | SOURCED (S2) | 25.2% | HIGH |
| P03 | Minimum payment formula | SOURCED (S3) | $40 floor / 1% + interest | HIGH |
| P04 | 36-month disclosure requirement + derived payment | SOURCED (S4, derived) | $309.20 | HIGH |
| — | Monthly interest rate | derived from S2 | 2.1% | n/a (arithmetic) |

Sourced: 4 (S1-S4). Assumption: 0. Dropped: 0. Open: 0.

## Next step

Run `case-readiness` on `the-minimum-payment-trap`.
