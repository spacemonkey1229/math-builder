Case Study: The Fee Route
MS | Math | Case Study | 2026 | Adventure

## Overview

Priya Nair has the routing dashboard open on one monitor and a support ticket open on the other, and neither screen is making her feel good about tomorrow's migration window. Fernbrook Refill Co.'s AI reorder agent — the little background service that watches every customer's smart water-filter sensor and fires off a replacement-cartridge charge the instant a filter reads low — has been quietly running on the card network since launch. Today it fires off thousands of these charges again, one sensor at a time, each one a few dollars or less, each one carrying its own slice of interchange fee.

A Slack thread from the platform engineering channel is still open in the corner: a rival subscription brand just posted, half-bragging and half-panicked, that switching its own reorder agent to a stablecoin settlement rail cut its per-transaction fee to almost nothing — and then, three weeks later, ate a five-figure loss on a wave of disputed charges nobody could claw back. Priya has read the thread twice.

The migration ticket is sitting in her queue, approved by finance, waiting only on her sign-off: flip Fernbrook's reorder agent from the card rail to the stablecoin rail by Friday, or don't. She has the network map taped above her desk — banks, processors, a custodian, a settlement ledger, every arrow between them — and a blinking cursor in the ticket's one open field: Approve or Hold.

Her coffee's gone cold. The migration either happens tonight or it doesn't happen this quarter.

## Background

Priya Nair is the Payments Infrastructure Lead at Fernbrook Refill Co., a small subscription company that sells smart-home consumable refills — water-filter cartridges, air-purifier pods — through sensors that detect low supply and trigger an automatic reorder. Fernbrook's AI reorder agent, not a human, initiates every one of these purchases: it holds its own small balance, watches sensor data, and fires a payment the instant a threshold is crossed. Priya owns the agent's payment-routing configuration and is accountable for both the fee line on Fernbrook's income statement and the dispute-loss line, with no one else on the four-person payments team empowered to override her sign-off before Friday.

Every one of these reorder-agent purchases currently settles over the traditional card network: the customer's card issuer, a card-network switch, and Fernbrook's acquiring processor each sit on the path the money travels, and each one takes a cut (SEE APPENDIX A for the full settlement network map, SEE APPENDIX B for the card rail's real, published fee schedule). The alternative on the table is a stablecoin settlement rail: the agent's own on-chain balance moves through a stablecoin ledger to a custodian bank that converts it back to dollars in Fernbrook's account, at a near-zero published fee (SEE APPENDIX A, SEE APPENDIX C). The catch, stated plainly in Fernbrook's own vendor contract for each rail, is chargeback recourse: the card rail's dispute-resolution process lets Fernbrook recover most of the value of a disputed charge, while the stablecoin rail offers no recourse mechanism at all — once funds settle on-chain, a successful fraud or dispute event is a total, unrecoverable loss (SEE APPENDIX D for how often that is expected to happen and how much of a disputed charge each rail actually leaves on Fernbrook's books).

The two options sit on Priya's whiteboard under their working names: **The Card Bridge**, keeping every reorder-agent transaction on the existing card-network settlement path, and **The Coin Rail**, migrating every reorder-agent transaction to the stablecoin settlement path. Whichever Priya recommends applies to all of Fernbrook's reorder-agent volume — there is no partial migration option before Friday's window closes. The vocabulary and "how to…" procedures needed to work through the settlement network are listed in (SEE APPENDIX E), and every sourced or assumed figure in this case is documented in (SEE APPENDIX F).

Priya has to recommend one rail, defend the expected net-revenue math behind it using the actual settlement network graph, and file the migration ticket before she leaves tonight.

## Dilemma

You are Priya Nair.
Do you:
A.) The Card Bridge — keep every reorder-agent transaction on the existing card-network settlement path OR
B.) The Coin Rail — migrate every reorder-agent transaction to the stablecoin settlement path

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A labeled drawing of the settlement network as a weighted graph — every vertex from
    Appendix A's node list and every edge with its fee weight written on it — plus an explicit
    identification of at least one cycle in the graph (a closed loop of vertices and edges), and
    a sentence stating what that cycle means for Fernbrook's settlement options.
    D2. A shortest-path determination: using Appendix A's weighted graph, compute the total
    weighted cost of both candidate paths between the Issuing Bank (IB) and the Custodian (CU) —
    one path routes through the Card Network Hub directly to the Custodian, the other routes all
    the way through the Acquiring Processor and Merchant Bank Account first — show the arithmetic
    for each, and state which path is mathematically the shortest and why.
    D3. An Euler-audit determination: using the degree of every vertex in Appendix A's graph
    (how many edges touch it), determine whether the settlement network graph has an Euler
    circuit, an Euler path, or neither, and justify your answer by actually counting each
    vertex's degree.
    D4. An expected-net-revenue-retained table comparing Option A (The Card Bridge's path,
    Issuing Bank to Card Network Hub to Acquiring Processor to Merchant Bank Account) and Option
    B (The Coin Rail's path, Agent Wallet to Stablecoin Ledger to Custodian to Merchant Bank
    Account): total weighted path fee, expected fraud/dispute loss, and net revenue retained per
    $1,000 processed for each — using Appendix B, C, and D's figures, shown step by step.
    D5. A one-paragraph written recommendation, using correct graph-theory vocabulary (vertex,
    edge, path, weighted graph, cycle) throughout, that names which rail retains more net revenue
    per $1,000 processed and explicitly addresses why comparing the two rails' raw per-transaction
    fee percentages alone, without weighting each rail's real expected fraud-loss exposure, would
    have been misleading.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — Settlement Network Map

Referenced in Background and Challenge 3 (D1, D2, D3). Fernbrook's payments team maintains this
map of every node and connection in its two available settlement rails, current as of this
quarter's vendor contracts.

**Vertices (nodes):**

| Vertex | What it is |
|---|---|
| IB | Issuing Bank — the customer's own card-issuing bank |
| CN | Card Network Hub — the Visa/Mastercard settlement switch |
| AQ | Acquiring Processor — Fernbrook's card processor |
| CU | Custodian / Off-Ramp Bank — converts stablecoin balances back to USD |
| ST | Stablecoin Settlement Ledger — the on-chain USDC settlement layer |
| AW | Agent Wallet — the reorder agent's own on-chain stablecoin balance |
| MB | Merchant Bank Account — Fernbrook's own settlement account, where funds land either way |

**Edges (connections) and their weights (fee per transaction):**

| Edge | Weight (fee) | What it represents |
|---|---|---|
| IB — CN | 0.14% [S2] | Card network assessment fee |
| CN — AQ | 1.89% + $0.10 [S1] | Card interchange fee |
| AQ — MB | 0% (MA — no additional acquirer-to-merchant-bank transfer fee modeled) | Acquirer settles into Fernbrook's own bank account |
| CN — CU | 0.30% (MA2) | A real, publicly announced card-network-to-stablecoin-custodian settlement pilot — not used by either of Fernbrook's two options, shown for completeness of the network map |
| AW — ST | $0.01 [S5] | On-chain network fee to move the agent's stablecoin balance onto the settlement ledger |
| ST — CU | 0.05% (MA — informed by [S6]) | Off-ramp conversion fee |
| CU — MB | 0% (MA — no additional custodian-to-merchant-bank wire fee modeled) | Custodian wires converted USD into Fernbrook's own bank account |

**Option A (The Card Bridge)'s path:** IB → CN → AQ → MB.
**Option B (The Coin Rail)'s path:** AW → ST → CU → MB.
The CN — CU edge exists in the real network but is not part of either option under decision this
week — Fernbrook's current acquiring contract does not route through it. It is included here
because it is a real connection in the settlement graph, not because it is one of the two choices.

## Appendix B — The Card Bridge: Fee & Dispute-Recovery Data

Referenced in Background and Challenge 3 (D4).

| Item | Value |
|---|---|
| Card network assessment fee (IB–CN edge) | 0.14% [S2] |
| Card-not-present interchange fee (CN–AQ edge) | 1.89% + $0.10 [S1] |
| Share of a disputed transaction Fernbrook ultimately loses under the card rail's chargeback / dispute-resolution process | 20% (MA1) |

## Appendix C — The Coin Rail: Fee & Fraud-Exposure Data

Referenced in Background and Challenge 3 (D4).

| Item | Value |
|---|---|
| On-chain network fee (AW–ST edge) | $0.01 [S5] |
| Off-ramp / custodial conversion fee (ST–CU edge) | 0.05% (MA — informed by [S6]) |
| Share of a disputed transaction Fernbrook ultimately loses on the stablecoin rail (no recourse mechanism exists) | 100% — this is definitional, not sourced: once a stablecoin transaction settles on-chain there is no dispute-resolution process to recover any portion of it. |

## Appendix D — Transaction Profile & Fraud-Incidence Assumption

Referenced in Background and Challenge 3 (D4). These two figures apply to both rails equally —
what differs between the rails is not how often a disputed transaction happens, but how much of
it each rail actually recovers (Appendix B and C above).

| Item | Value |
|---|---|
| Average value of one reorder-agent transaction | $1.30 (MA3) |
| Probability that a given reorder-agent transaction becomes a fraud or dispute event | 0.90% (MA4) |

## Modeling Assumptions

> These figures are **not sourced from an external publisher**. They are stated scenario
> assumptions chosen by the case author because no public report measures Fernbrook's own
> transaction profile, a merchant's exact dispute-recovery share under a specific chargeback
> configuration, or the per-transaction rate of a novel, not-yet-priced card-network-to-stablecoin
> settlement pilot. A Hero may challenge these numbers in discussion — that is a legitimate move,
> and the sensitivity column shows exactly where the challenge would matter.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Merchant-borne loss share of a disputed transaction on the Card Bridge (chargeback/dispute-recovery process) | 20% | No source publishes an exact merchant-borne loss share for one specific dispute-resolution configuration. Set well below 100% to reflect that card-network liability-shift and dispute tools genuinely recover most — but not all — of a disputed charge's value for a merchant using standard authentication, while still leaving some fraud genuinely uncollectable even with recourse. | The case's recommendation is sensitive to this figure — work the comparison yourself with a different plausible loss share rather than taking 20% as unchallengeable fact. |
| MA2 | Card-network-to-stablecoin-custodian settlement pilot rate (CN–CU edge) | 0.30% | No public source discloses a per-transaction rate for this specific, real, publicly announced pilot service (a card network settling transactions to a stablecoin custodian instead of a traditional acquirer). Set between the pure on-chain settlement rate (near-zero) and the full card interchange rate, reflecting that a hybrid card-network/stablecoin settlement product should cost less than pure card interchange but more than pure on-chain transfer, since it still uses card-network infrastructure. | Does not change which option wins this case's own current numbers, since this edge is not part of either option's actual path — it exists only for the network-map and cycle/Euler-audit deliverables. |
| MA3 | Average reorder-agent transaction value | $1.30 | No source publishes Fernbrook's own transaction sizes (a fictional company). Set low and disclosed, consistent with real, published 2026 industry reporting (see Appendix F) that AI-agent-initiated payments run frequent, small-value transactions specifically because a flat per-transaction fee becomes proportionally large at small transaction sizes even when the percentage fee stays modest. | This is one of the case's most load-bearing figures — the flat per-transaction fee on each rail (Appendix A) becomes a much larger or smaller share of the total cost depending on this value. Work the comparison yourself with a different plausible transaction size before assuming the recommendation is unaffected. |
| MA4 | Probability a given reorder-agent transaction becomes a fraud/dispute event | 0.90% | No source measures a fraud/dispute incidence rate specific to AI-agent-initiated, card-not-present micro-transactions. Informed by real, cited aggregate card-fraud data: the Nilson Report's own worldwide figure of 6.58 cents of fraud loss per $100 of total card volume in 2023 [S3] (0.0658%, spanning all card-present and card-not-present transactions combined, with chargeback recovery already netted in), and the Federal Reserve Bank of Kansas City's published finding that card-not-present fraud rates are meaningfully higher than card-present fraud rates and have been rising [S4]. Since every reorder-agent transaction in this case is card-not-present by construction (no physical card is ever present), 0.90% is set well above the blanket all-transaction-types aggregate to reflect a card-not-present-only channel, while still being a single order of magnitude, not multiple orders, above the cited aggregate. | This is the single assumption the case's recommendation is most sensitive to, because it drives both rails' expected-loss figures directly and the two rails' recovery shares (MA1 vs. the Coin Rail's definitional 100%) amplify it very differently. Work Challenge 3 (D4) again with a different plausible incidence rate before assuming the recommendation is unaffected. |

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Graph (Vertices And Edges)
- Vertex
- Edge
- Path
- Cycle
- Weighted Graph

**"How to…" questions**

- How to find the shortest path between two vertices in a weighted graph
- How to determine whether a graph has an Euler path or circuit

## Appendix F — Sources

All sourced (non-assumption) figures in this case are cited here. Sources marked "supplemental"
are not directly quoted for a value used in this case's arithmetic; they inform the basis column
of a Modeling Assumption (see above) and are cited for transparency about what real research
shaped that assumption.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Visa card-not-present interchange reimbursement rate, U.S., consumer credit, "Product 1 / All Other Products" fee program | 1.89% + $0.10 | Visa — [Visa USA Interchange Reimbursement Fees](https://usa.visa.com/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf) | 18 Apr 2026 | HIGH |
| S2 | Visa network assessment fee, U.S., credit transactions | 0.14% | Chargebacks911 — [Visa Interchange: 2026 Processing Rates & Fees, Explained](https://chargebacks911.com/visa-interchange-fees/) | 2026 | MEDIUM |
| S3 | Global card fraud loss rate, 2023 | 6.58 cents per $100 of total volume ($33.83 billion total) | Nilson Report, republished via GlobeNewswire — [Payment Card Fraud Losses Approach $34 Billion](https://www.globenewswire.com/news-release/2025/01/06/3004931/0/en/Payment-Card-Fraud-Losses-Approach-34-Billion.html) | 6 Jan 2025 | MEDIUM (supplemental — press-release republication of Nilson Report's own paywalled data, informs MA4's basis, not directly used as this case's value) |
| S4 | Card-not-present fraud rates run meaningfully higher than card-present fraud rates and have continued to rise | Card-present dual-message networks 14.2 basis points, single-message 5.1 basis points (2023); card-not-present rates for both network types described as higher and rising | Federal Reserve Bank of Kansas City — [New Data on Card-Present and Card-Not-Present Fraud Rates in the United States](https://www.kansascityfed.org/research/payments-system-research-briefings/new-data-on-card-present-and-card-not-present-fraud-rates-in-the-united-states/) | 25 Feb 2026 | HIGH (supplemental — a real primary Federal Reserve research briefing; informs MA4's basis, not directly used as this case's value, since it does not state an exact card-not-present percentage) |
| S5 | Typical on-chain transaction fee on a low-cost settlement network (Base), simple transfer example | Approximately $0.002–$0.02 per transaction | Base (Coinbase) — [Network Fees — Base Documentation](https://docs.base.org/base-chain/network-information/network-fees) | accessed 2026-09-09 | MEDIUM (fee varies with underlying Ethereum L1 network conditions; case uses $0.01, within the documented range) |
| S6 | Circle's tiered USDC cash-out (redemption) fee schedule, in effect since September 2025 | 0.03% floor, rising to 0.1% for withdrawals above $15 million | Cointelegraph (citing a Bloomberg report), republished via TradingView — [Circle raises USDC cash-out fees, affecting large-scale redemptions](https://tr.tradingview.com/news/cointelegraph%3Afbf74367c094b%3A0-circle-raises-usdc-cash-out-fees-affecting-large-scale-redemptions) | 29 Oct 2025 (reported) | MEDIUM (supplemental — real, dated news reporting of a real tiered fee schedule; informs the ST–CU off-ramp assumption's basis, not a per-transaction merchant rate) |
| S7 | Real-world context: AI payment agents are being built to favor stablecoin settlement rails over card networks for their speed, low fees, and 24/7 settlement | Directional industry finding, no specific fee comparison quantified in this article | Payment Executive — [Agentic Commerce 2026: The Payments Revolution Where AI Agents Actually Buy Stuff](https://www.paymentexecutive.com/post/agentic-commerce-2026-the-payments-revolution-where-ai-agents-actually-buy-stuff) | 8 Jun 2026 | MEDIUM (supplemental — establishes that this case's underlying dilemma reflects a real, live 2026 industry dynamic, not a value used in arithmetic) |

**Who these sources are:** Visa and Mastercard are the two dominant card networks whose published
interchange and assessment fees set most of the real cost of "The Card Bridge." Circle is the
company that issues USDC, the stablecoin most commonly used in the settlement pilots this case
describes. Base is a low-cost blockchain network (built by Coinbase) that many stablecoin
settlement flows use because its transaction fees are small. The Nilson Report is the payments
industry's most widely cited source for aggregate card fraud statistics; the Federal Reserve Bank
of Kansas City is a regional Federal Reserve bank that publishes independent payments-system
research.

S1 and S2 are used directly as values in this case's arithmetic (Appendix A/B). S5 is used
directly for the AW–ST edge. S3, S4, and S6 are real, dated, named-source figures that inform
Modeling Assumptions MA2 and MA4's chosen values without being the values themselves — see the
Modeling Assumptions table above for exactly how each is used. S7 establishes that this case's
real-world dilemma is a live, current industry dynamic. See `RESEARCH_LOG.md` for the full search
trail.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
