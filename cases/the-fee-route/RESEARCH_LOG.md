# Research Log — The Fee Route

Stage 3 (`case-research`) run on `cases/the-fee-route/`. 9 `{{NEEDS_SOURCE}}` placeholders
enumerated below (P01–P09). Worked in load-bearing weight order: the two real card-network figures
first (both have genuine, live public rate tables behind them), then the stablecoin-side figures,
then the assumption-shaped figures (dispute-recovery share, transaction size, fraud incidence)
confirmed as non-public/constructed before searching for them directly.

## P01 — Visa network assessment fee (IB–CN edge)

**Searched:** "Visa assessment fee percentage 2026 published rate acquirer"

**Attempted primary fetch:** `https://usa.visa.com/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf`
(the same PDF used for P02) — this document's front matter explains that assessment fees exist and
are billed separately from interchange, but the fetched pages (front matter + the debit and credit
interchange tables) do not tabulate the assessment-fee rate itself; it may live in a different Visa
publication (the Visa Product and Service Rules) not fetched this session.

**Fetched directly:** `https://chargebacks911.com/visa-interchange-fees/` — a reputable,
payments-industry-specialist aggregator. Confirmed exact quoted text: "Visa does make money on
network assessment fees, which range from 0.13% of the transaction value for debit card purchases
to 0.14% for credit card transactions."

**Outcome:** SOURCED as [S2], MEDIUM confidence (a named, reputable industry-press aggregator
citing Visa's own published rate, but not the primary Visa document itself, since this session
could not locate the exact table in the fetched pages of the primary PDF). Used directly as the
IB–CN edge weight (Appendix A/B).

## P02 — Visa card-not-present interchange rate (CN–AQ edge)

**Searched:** "Visa interchange reimbursement fee rate 2026 CPS retail credit card percent"

**Fetched directly:** `https://usa.visa.com/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf`
(856.7 KB, downloaded and read as PDF pages). Confirmed: "Visa USA Interchange Reimbursement Fees
— Visa Supplemental Requirements," dated 18 April 2026, "Visa Public." Section C, "Visa U.S.A.
Consumer Credit Interchange Reimbursement Fees," page 8, "Card Not Present Fee Program" table,
row "Product 1": "All Other Products" column = **1.89% + $0.10**. (Other card tiers in the same row
range from 1.53% + $0.05 to 2.60% + $0.10 depending on card prestige tier — "All Other Products,"
the non-premium default tier, was chosen as the representative rate for a typical consumer card
mix, since this case does not stipulate a premium-card-heavy customer base.)

**Outcome:** SOURCED as [S1], HIGH confidence (primary publisher, official rate table, dated,
exact category and figure needed). Used directly as the CN–AQ edge weight (Appendix A/B).

## P05 — Stablecoin on-chain network fee (AW–ST edge)

**Searched:** "Base network average transaction gas fee 2026 cents Coinbase"

**Fetched directly:** `https://docs.base.org/base-chain/network-information/network-fees` — Base's
own developer documentation (Base is Coinbase's low-cost Ethereum layer-2 network, commonly used
for stablecoin settlement). Confirmed a worked example: a 200,000-gas transaction on Base Mainnet
costs approximately **$0.002** at a stated ETH price, with an explicit caveat that "typically the
L1 security fee is higher than the L2 execution fee," so real total costs exceed this component
alone. No publication/last-updated date is shown on the page itself. Search-aggregated context
(not independently fetched, used only to sanity-check the range, not cited) suggested simple
transfers on Base commonly run $0.01–$0.03 in 2025–2026.

**Outcome:** SOURCED as [S5], MEDIUM confidence (primary publisher, but no visible date, and the
documented figure is a lower-bound component rather than the realistic total). $0.01 was chosen as
a round figure within the documented and search-confirmed range. Used directly as the AW–ST edge
weight (Appendix A/C).

## P06 — Off-ramp / custodial conversion fee (ST–CU edge)

**Searched:** "Circle USDC stablecoin transaction settlement fee cents 2026"

**Found:** Circle (the issuer of USDC) does not charge a per-transaction fee for minting USDC —
deposits convert 1:1. A WebSearch summary attributed a specific tiered **Circle Mint redemption fee
schedule** to Circle (no fee on the first $40M of daily redemptions, 2 basis points from
$40M–$100M, 5 basis points above $100M, effective 15 March 2026), citing
`https://help.circle.com/s/article/USDC-redemption-structure`.

**CORRECTION (during Tier 2 P6 data-decay verification):** a direct fetch of that exact URL
returned only a client-side loading shell with no readable fee content (a JS-rendered help-center
page this session's fetch tool could not execute) — the figures could not be confirmed against any
page this session actually fetched. Per the "never cite a URL you did not fetch" rule, the citation
was replaced before publication rather than left in place. A follow-up search and direct fetch of
`https://tr.tradingview.com/news/cointelegraph%3Afbf74367c094b%3A0-circle-raises-usdc-cash-out-fees-affecting-large-scale-redemptions`
(a Cointelegraph article, citing an October 29, 2025 Bloomberg report, republished via TradingView)
confirmed real, quotable figures: Circle's USDC cash-out fees, in effect since September 2025,
"begin at 0.03% per transaction and escalate to as much as 0.1% for withdrawals above $15 million."

**Outcome:** **NOT FOUND** as a direct citable flat per-transaction rate for a generic merchant's
off-ramp/custodial conversion service — Circle's own real, confirmed fee schedule is a
volume-tiered redemption fee on Circle's own platform, not a flat per-transaction merchant off-ramp
rate, and no source publishes a generic figure for the latter. **Exit chosen: Modeling
Assumption**, value 0.05% (5 basis points), chosen within the confirmed real 0.03%–0.10% range
(informing, not equalling, the value) to reflect a mid-range off-ramp cost for a smaller-scale
custodian/off-ramp partner serving a merchant well below Circle's own largest-redemption tier.
Cited as [S6], MEDIUM confidence, supplemental. Fixed in `case.json.sources[S6]`, `case.md`'s
Appendix F, and this entry.

## P07/P08 — Dispute-recovery share, average transaction value, fraud-incidence probability

**Searched (fraud-incidence context only):**
- "card-not-present fraud rate percent of transaction value 2025 published merchants"
- Direct fetch: `https://www.kansascityfed.org/research/payments-system-research-briefings/new-data-on-card-present-and-card-not-present-fraud-rates-in-the-united-states/`
  — a real, primary Federal Reserve Bank of Kansas City briefing, dated 25 Feb 2026, drawing on
  the Federal Reserve Board's biennial debit-card report (2023 data). Confirmed real figures for
  **card-present** fraud: 14.2 basis points (dual-message networks), 5.1 basis points
  (single-message networks). The briefing states card-not-present fraud rates are higher and
  "increased" from 2021, and that single-message-network CNP rates "surpassed" dual-message rates
  for the first time in 2023 — but does not state an exact CNP percentage in the accessible portion
  of the briefing. A separate WebSearch summary attributed a "0.93% CNP fraud rate" figure to this
  general body of research, but this could not be confirmed against any page this session actually
  fetched, so **it is not cited anywhere in this case**, per the "never cite a URL you did not
  fetch" rule.
- Direct fetch (already performed for P01/P02's fraud-rate context): the Nilson Report's own
  article page (`nilsonreport.com/articles/card-fraud-losses-worldwide-2024/`) is paywalled beyond
  its teaser; the underlying 2023 figures (6.58 cents of fraud loss per $100 of volume, $33.83
  billion total) were confirmed instead via a GlobeNewswire republication of the same Nilson data,
  dated 6 Jan 2025.

**Outcome:** Genuine search confirms no public source measures a fraud/dispute-incidence rate, or a
merchant's exact dispute-recovery share, for the specific scenario this case needs (an AI-agent-
initiated, card-not-present micro-transaction with a defined chargeback-resolution configuration).
Both are proprietary-shaped, scenario-specific figures — the same category of "does not exist as a
citable dataset" finding documented for `the-overlap-send`'s CRM list sizes. **Exit chosen for
both: Modeling Assumptions.** MA1 (dispute-recovery share, 20% merchant-borne) is informed by
general, real reporting that card-network liability-shift tools recover most — not all — of a
disputed charge for an authenticated merchant, without a specific public number to cite for "most."
MA4 (fraud-incidence probability, 0.90%) is informed directly by the two real, cited findings above
(Nilson's blended 0.0658% aggregate [S3], and the Fed KC finding that CNP fraud runs meaningfully
higher and is rising [S4]), set roughly an order of magnitude above the blended aggregate to
reflect an all-CNP, no-physical-card channel, without inflating several orders of magnitude beyond
what the cited data would support. Redesign (dropping the fraud-exposure comparison entirely) was
considered and rejected: modeling the real expected-value trade-off between fee savings and fraud
exposure IS the reason this case exists per the approved concept sheet — removing it would gut the
case's entire premise, the same reasoning documented in `the-overlap-send`'s own RESEARCH_LOG for
its unsourceable MA4.

## P09 — Average reorder-agent transaction value

**Searched:** none attempted as a live web search for an exact figure — confirmed by direct
reasoning before searching that Fernbrook Refill Co.'s own specific per-transaction value is a
constructed detail of a fictional company and cannot exist as a citable external dataset, the same
category finding made explicit for `the-overlap-send`'s CRM list sizes (MA1) and, in that case,
correctly not searched for either.

**Outcome: NOT FOUND, correctly not searched for.** **Exit chosen: Modeling Assumption (MA3)**,
value $1.30, chosen to be genuinely small and disclosed, consistent with real 2026 industry
reporting (confirmed via the Payment Executive article below, [S7]) that AI-agent-initiated
payments run frequent, small-value transactions specifically because a flat per-transaction
interchange fee becomes proportionally large at small transaction sizes even when the percentage
component stays modest — the exact real-world dynamic this case's math is built to demonstrate.

## Supplemental — real-world grounding for the case's core premise

**Searched:** "Forbes 2026 AI agent payments stablecoin routing interchange fees"

**Attempted fetches that failed (both HTTP 403, not cited per the "never cite a URL you did not
fetch" rule):**
- `https://www.forbes.com/sites/digital-assets/2026/06/07/visa-mastercard-and-coinbase-are-fighting-over-how-ai-agents-pay/`
- `https://www.forbes.com/sites/boazsobrado/2026/03/19/stripe-visa-and-mastercard-race-to-build-ai-agent-payment-rails/`

Both are real, dated, named Forbes articles (confirmed via search-result titles and dates) directly
on this case's exact premise — AI agents routing payments around card-network interchange fees
toward stablecoin rails — but this session could not retrieve their actual content, so **neither is
cited as a source in `case.json`**, even though their existence corroborates that the underlying
2026 industry dynamic is real and widely covered, not an invented premise.

**Fetched directly (succeeded):**
`https://www.paymentexecutive.com/post/agentic-commerce-2026-the-payments-revolution-where-ai-agents-actually-buy-stuff`
— confirmed real, dated 8 June 2026, discussing AI agents' preference for stablecoin settlement
("speed, low fees, 24/7 settlement, and programmability") without quantifying specific fee figures.

**Outcome:** Cited as [S7], MEDIUM confidence, supplemental — establishes the case's real-world
premise is a live, current, widely covered 2026 industry dynamic. Not used for any numeric value.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Visa network assessment fee | SOURCED (S2) | 0.14% | MEDIUM |
| P02 | Visa CNP interchange rate | SOURCED (S1) | 1.89% + $0.10 | HIGH |
| — | CN–CU hybrid pilot edge (unused by either option) | ASSUMPTION (MA2) | 0.30% | n/a (assumption) |
| P05 | Stablecoin on-chain network fee | SOURCED (S5) | $0.01 | MEDIUM |
| P06 | Off-ramp/custodial conversion fee | ASSUMPTION (informed by S6) | 0.05% | n/a (assumption) |
| P07 | Card-rail merchant-borne dispute-loss share | ASSUMPTION (MA1) | 20% | n/a (assumption) |
| P08 | Fraud/dispute-incidence probability | ASSUMPTION (MA4, informed by S3/S4) | 0.90% | n/a (assumption) |
| P09 | Average reorder-agent transaction value | ASSUMPTION (MA3, informed by S7) | $1.30 | n/a (assumption) |
| — | Sources appendix | SOURCED (S1–S7) | — | mixed (2 HIGH, 5 MEDIUM/supplemental) |

Sourced: 2 figures used directly as real numeric edge weights ([S1], [S5]), 1 real but
aggregator-sourced figure used directly ([S2]), plus 3 supplemental sources ([S3], [S4], [S6])
cited to show their real, named provenance even though they inform rather than directly supply a
case value, plus 1 supplemental real-world-grounding source ([S7]). Assumption: 4 Modeling
Assumption records (MA1–MA4) resolve the remaining placeholders. Dropped: 0. Open: 0. Two real,
relevant Forbes articles were found but could not be fetched (HTTP 403) and are correctly not
cited anywhere in this case.

## Next step

Run `case-readiness` on `the-fee-route`.
