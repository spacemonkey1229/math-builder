# Case Study: The Fee Ladder

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Marcus Alvarez has two browser tabs open, and a phone that keeps lighting up on the desk beside
his keyboard.

The first tab holds Meridian Trust & Custody's real fee ladder — the actual schedule that decides
what a client pays, rung by rung, each rung computed off whatever balance survived the rung
before it. Marcus has walked this exact sequence by hand for institutional clients before. Done
right, it takes real, unhurried time.

The second tab holds Meridian's own Quick-Quote Reference Card — one flat rate, printed once,
never recalculated per client. Marcus could read that single number over the phone and be done
before the client on the other end finishes their coffee.

The phone belongs to Cassidy, over in Institutional Relationships, who is on the line with a
pension fund's CFO right now, promising a number soon. Every few minutes another text lands: *any
update?* This client is large enough that today's quote sets the tone for a multi-year custody
relationship — and Meridian is not the only bank in the room. A competing custodian is already
circling with a number of its own.

Marcus's cursor sits between the two tabs.

Cassidy needs an answer before that call ends, and Marcus has exactly one number to send back.

---

## Background

Marcus Alvarez is a Securities Settlement Operations Analyst on the custody operations team at
Meridian Trust & Custody Company, a custody bank that holds and administers institutional clients'
securities and charges an annual custody fee for the service. Sales has an inbound institutional
client — a pension fund moving its assets under custody (AUC) to Meridian — and needs a defensible
fee quote today, before the deal goes to a competing custodian (SEE APPENDIX A).

Meridian's real, internal fee schedule is a fee ladder of four rate tiers. Unlike a standard
bracket-style schedule, where each tier's rate applies to a fixed dollar range of the *original*
balance, Meridian's ladder applies each tier's rate to whatever balance is left *after* the
previous tier's own fee has already been subtracted — each tier's charge depends recursively on
the tier before it (SEE APPENDIX C). Computing it exactly, tier by tier, with documentation a
client's own finance team and Meridian's compliance desk can both check, takes real analyst time
Marcus does not have before Cassidy's call ends (SEE APPENDIX A).

Meridian also keeps a Quick-Quote Reference Card: a single flat effective rate, set once per AUC
size band by the pricing desk, meant to be read off in seconds when a fast answer is what the sales
desk needs (SEE APPENDIX B). It is not recalculated for any specific client's exact balance.

Two options are on Marcus's screen. **The Quick-Quote** is the flat card rate, applied directly to
this client's AUC — fast enough to make Cassidy's deadline, but an approximation of what the real
ladder would actually charge. **The Full Ladder** is the exact recursive tier-by-tier computation —
defensible down to the last cent, but not something Marcus can finish before Cassidy needs an
answer (SEE APPENDIX A).

Real, publicly disclosed custody fee schedules from other custodian banks confirm that fee rates
in this business genuinely are quoted in fractions of a basis point at the scale of a large
institutional account, and that they genuinely are structured as multi-tier ladders — Meridian's
own ladder's rate *magnitudes* sit inside that real, disclosed range (SEE APPENDIX E). Getting a
custody fee quote wrong is not a hypothetical risk in this industry: a real, documented case exists
of a major custody bank paying tens of millions of dollars over a fee-billing dispute with its own
clients (SEE APPENDIX F). Full source citations for every figure in this case are in Appendix G, and the full standards bridge for this case is in Appendix H.

---

## Dilemma

You are Marcus Alvarez.

Do you:

**A.)** Quote **the Quick-Quote** — Meridian's flat, single closed-form effective rate off the
reference card, applied directly to the client's total AUC **OR**

**B.)** Compute **the Full Ladder** — the true recursive tier-by-tier fee, running this client's
exact balance through all four rungs of Meridian's real schedule step by step

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A recursive formula for the balance sequence.** Using Appendix C's four tier rates, write
  the recursive definition for the client's remaining balance after each tier: state B₀ (the
  starting AUC), state the recursive rule that gives Bₖ in terms of Bₖ₋₁ and tier k's rate, then use
  that rule to walk this client's exact balance (Appendix A) through all four tiers, tier by tier,
  showing every fee and every remaining balance.
- **D2 — An explicit (non-recursive) formula, derived from D1's recursion.** Starting from D1's
  recursive rule, substitute Bₖ₋₁'s own definition into itself repeatedly until Bₙ is written
  directly in terms of B₀ and the four tier rates only — with no Bₖ term on the right-hand side for
  any k between 1 and n. Show every substitution step. Use the resulting explicit formula to
  compute the same total fee you found in D1, and confirm the two methods agree.
- **D3 — A fee-quote error table.** For this client's AUC (Appendix A), compute the Quick-Quote fee
  (Appendix B's flat rate applied directly to the balance) and the Full Ladder fee (D1/D2's true
  recursive total). Report the dollar gap between them and the percentage error, defined as the gap
  divided by the Full Ladder's true fee.
- **D4 — A sensitivity check across client sizes.** Repeat D3's fee-quote-error computation for the
  other two client AUC sizes in Appendix D. State, in your own words, whether the Quick-Quote
  card's percentage error gets better, gets worse, or stays the same as client size changes — and
  explain, using D2's explicit formula, *why* it behaves that way.
- **D5 — A recommendation memo.** State which method Marcus should actually use for today's quote,
  defended with D3/D4's error numbers, Appendix A's deadline, and Appendix F's precedent on what a
  wrong custody fee number can cost a bank over the life of a client relationship.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Meridian's Quoting Constraints

| Quantity | Value |
|---|---|
| Client's total assets under custody (AUC) being quoted today | $850,000,000 [MA1] |
| Time Cassidy gave Marcus to produce a number | Under one hour [MA2] |
| Estimated analyst time to complete a fully-documented Full Ladder computation (tier-by-tier, with compliance-ready workpapers) | Approximately 3 hours [MA3] |
| Number of tiers in Meridian's internal fee ladder | 4 [MA4] |

*Note: Meridian Trust & Custody Company is a scenario construction for this case — there is no
real company by this name.*

---

## Appendix B: Option A — The Quick-Quote (Flat Reference-Card Rate)

| Spec | Value |
|---|---|
| Meridian's published Quick-Quote Reference Card rate, $500 million–$1 billion institutional custody band | 3.90 basis points [MA5] |
| Is this rate recalculated for each specific client's exact balance? | No — it is fixed per AUC size band, set once by the pricing desk. |
| Time to produce a quote using this method | Well under Appendix A's one-hour deadline. |

---

## Appendix C: Option B — The Full Ladder (Meridian's True Recursive Fee Schedule)

| Tier (k) | Rate (rₖ) | Applies to |
|---|---|---|
| 1 | 2.00 basis points [MA6] | B₀ — the full incoming AUC |
| 2 | 1.25 basis points [MA6] | B₁ — the balance remaining after Tier 1's fee is subtracted |
| 3 | 0.75 basis points [MA6] | B₂ — the balance remaining after Tier 2's fee is subtracted |
| 4 | 0.50 basis points [MA6] | B₃ — the balance remaining after Tier 3's fee is subtracted |

**The recursive rule:** B₀ = the client's starting AUC. For each tier k = 1, 2, 3, 4: this tier's
fee is Feeₖ = rₖ × Bₖ₋₁, and the balance carried into the next tier is Bₖ = Bₖ₋₁ − Feeₖ. The Full
Ladder's total annual fee is B₀ − B₄ (the sum of all four tiers' fees).

*Note: this is what makes the ladder genuinely recursive rather than a standard marginal-bracket
schedule — each tier's rate applies to the balance left over after the previous tier's own fee has
already been taken out, not to a fixed dollar range of the original AUC. Producing this computation
fully documented takes the analyst time stated in Appendix A.*

---

## Appendix D: Client AUC Sizes in This Quarter's Institutional Pipeline

| Client | Assets Under Custody (AUC) |
|---|---|
| Client 1 | $300,000,000 [MA7] |
| Client 2 — today's client (SEE APPENDIX A) | $850,000,000 [MA1] |
| Client 3 | $1,200,000,000 [MA7] |

---

## Appendix E: Real Disclosed Institutional Custody Fee Schedules

| Custodian Bank | Fund | Fee Structure | Source |
|---|---|---|---|
| State Street Bank and Trust Company | The Gabelli Global Small and Mid Cap Value Trust | Domestic custody: 0.50 basis points on the first $500 million; 0.3875 basis points on the remainder | [S1] |
| State Street Bank and Trust Company | Green Century Funds | Custody, fund accounting, NAV, and foreign custody: 7.0 basis points on the first $150 million; 4.0 basis points on assets in excess of $150 million | [S2] |

*These are two real, filed custody fee schedules from a real custodian bank, disclosed as exhibits
to real fund custody agreements filed with the SEC. Both are standard marginal-bracket schedules,
not the balance-after-fee recursive structure Appendix C uses — Meridian's ladder is a stated
scenario construction (Modeling Assumptions MA1, MA5, MA6), but its basis-point rate magnitudes
(0.40–2.00 bp) sit inside the real range these two disclosed schedules span (0.3875–7.0 bp).*

---

## Appendix F: Documented Precedent — Custody Fee Billing Errors

| Item | Value |
|---|---|
| A real SEC enforcement action against a major custody bank for years of undisclosed markups and overcharges on custody-related client expenses | State Street Bank and Trust Company agreed to pay over $88 million — $48.78 million in disgorgement and prejudgment interest, plus a $40 million civil penalty — after the SEC found the firm collected $170 million in overcharges from thousands of registered investment company custody clients between 1998 and 2015, including $110 million from an undisclosed markup added to SWIFT messaging fees billed to clients [S3]. |

*This appendix documents a real, external precedent for the reputational and regulatory stakes of
getting a custody bank's client billing wrong — it is cited as industry precedent, not as an
incident at Meridian itself, which is fictional.*

---

## Modeling Assumptions

> These figures are **not sourced** from Meridian (a fictional company) or from any external
> record. They are stated scenario assumptions chosen by the case author, with rate *magnitudes*
> anchored to the two real, cited custody fee schedules in Appendix E. A Hero may challenge any of
> them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Today's client's total AUC | $850,000,000 | Scenario choice — large enough to make a fee-quote error a materially large dollar amount, matching the Overview's "sets the tone for a multi-year relationship" framing. | None on `margin_pct` — see MA6's sensitivity note: the Full Ladder's percentage effective rate is mathematically independent of AUC size (D4's own finding), so `margin_pct` does not change if MA1 changes. Changes only the dollar-size of the gap. |
| MA2 | Time Cassidy gave Marcus | Under one hour | Matches the Overview's live-call urgency. | None — flavor only, not load-bearing on the numeric margin. |
| MA3 | Estimated analyst time for a fully-documented Full Ladder computation | ~3 hours | Illustrative — a defensible, compliance-ready workpaper takes materially longer than the deadline in MA2 allows, which is what makes this a genuine dilemma rather than "just do both." | None — flavor only, not load-bearing on the numeric margin, but structurally load-bearing on why the dilemma exists at all. |
| MA4 | Number of tiers in Meridian's ladder | 4 | Scenario choice — enough tiers to be a genuine "ladder," few enough to compute by hand within a case-study session. | Does not affect `margin_pct` (see MA6). |
| MA5 | Quick-Quote Reference Card flat rate, $500M–$1B band | 3.90 basis points | Scenario choice, set inside the real disclosed custody bp-rate range (Appendix E, 0.3875–7.0 bp) and chosen close enough to MA6's true blended rate (4.499 bp, see MA6) that both options are genuinely defensible on `margin_pct`, per SPEC §2. | **HIGH — this is the case's real fulcrum.** Moving MA5 up or down directly moves `margin_pct`; see `case.json`'s `sensitivity_note` and `sensitivity_model.py` for the full sweep. |
| MA6 | The Full Ladder's four tier rates | 2.00 / 1.25 / 0.75 / 0.50 basis points (Tiers 1–4) | Scenario choice — a declining-rate ladder, consistent with how real custody fee schedules charge lower marginal rates as scale grows (Appendix E), with magnitudes chosen inside the real disclosed 0.3875–7.0 bp range. Tier 4's rate (0.50 bp) was chosen to closely echo Appendix E's real Gabelli/State Street first-tier rate (also 0.50 bp). | **HIGH.** These four rates set the Full Ladder's true blended effective rate at exactly 4.499306 basis points, for *any* client AUC (this is a provable, scale-invariant consequence of the recursive definition in Appendix C — see D4/`sensitivity_note`). `margin_pct` is the percentage gap between MA5 and this fixed 4.499306 bp figure. |
| MA7 | Client 1 and Client 3's AUC (Appendix D) | $300,000,000 and $1,200,000,000 | Scenario choice — spans a materially smaller and a materially larger institutional client than today's client, to stress-test whether the Quick-Quote's error is client-size-dependent (D4). | None on `margin_pct` — D4's own finding is that the percentage error is identical at all three sizes (see `balance.margin_note`). |

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Real, filed custody fee schedule, State Street Bank and Trust Company, domestic custody, The Gabelli Global Small and Mid Cap Value Trust | First $500 million: 0.50 basis points; remainder: 0.3875 basis points | State Street Bank and Trust Company / The Gabelli Global Small and Mid Cap Value Trust — [Form of Custodian Fee Schedule](https://www.sec.gov/Archives/edgar/data/1585855/000119312513364152/d594745dex999b.htm), Exhibit 99(9)(b) | Filed 2013-09-11 | HIGH |
| S2 | Real, filed custody fee schedule, State Street Bank and Trust Company, Green Century Funds | First $150 million: 7.0 basis points; excess of $150 million: 4.0 basis points; monthly minimum $3,826.67 per fund | State Street Bank and Trust Company / Green Century Funds — [Amended Fee Schedule to the Custodian Agreement](https://www.sec.gov/Archives/edgar/data/877232/000119312512483058/d440242dex99g3.htm), Exhibit 99(g)(3) | As of 2012-07-01 | HIGH |
| S3 | Real SEC enforcement action: State Street Bank and Trust Company overcharged custody clients | $170 million in overcharges collected 1998–2015 ($110 million from an undisclosed SWIFT messaging markup); settlement of $48.78 million disgorgement/prejudgment interest plus a $40 million civil penalty (over $88 million total) | U.S. Securities and Exchange Commission — [State Street Settles SEC Charges for Adding Undisclosed Markups on Client Expenses](https://www.sec.gov/newsroom/press-releases/2019-114), Press Release 2019-114 | 2019-06-27 | HIGH |

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Recursive Formula

**"How to…" questions**

- How to write a recursive formula for a sequence
- How to convert a recursive formula to an explicit formula

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
