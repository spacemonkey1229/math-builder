# Case Study: The Peg Line

MS | Math | Case Study | 2026 | Adventure

---

## Overview

Priya Nathan has the attestation template open in one tab and a Treasury rate sheet open in the other, and she keeps toggling between them instead of typing.

It's the last afternoon before Northlight Financial's monthly reserve attestation locks for the auditors, and Priya is the reserves analyst whose name goes on the internal recommendation memo that decides how the company's dollar-pegged token, NLD, is going to be backed for the next cycle. Two draft allocations sit side by side on her second monitor. One keeps almost everything parked in the shortest paper the desk trades — bills that mature back into cash in about a month, over and over, so there's barely a day where the money isn't sitting as good as cash. The other stretches part of the ladder out to a somewhat longer maturity, chasing a better rate the desk has been eyeing all quarter.

Her manager, Devraj, drops into the chair across from her desk without being asked. "Compliance signed off on both," he says. "Board wants a number, not a vibe. How much extra are we actually making, and what are we trading for it?"

There had been a third draft on Priya's monitor an hour ago — reserves stretched all the way out to the longest maturity the law allows. She killed it herself, before Devraj even saw it, once her own numbers showed the extra risk grew faster than the extra yield did. She minimizes that old draft before Devraj can ask about it.

---

## Background

Priya Nathan is the Treasury/Reserves Analyst at Northlight Financial, the issuer of NLD, a U.S.-dollar-pegged stablecoin. Northlight is a scenario construction for this case — there is no real company by this name — but it operates the way real regulated stablecoin issuers operate: every dollar of NLD in circulation must be backed 1:1 by reserve assets, and Northlight publishes a third-party-attested reserve report every month disclosing the total reserve amount and its composition (SEE APPENDIX A).

Since 2025, U.S. federal law has fixed exactly which reserve assets are allowed at all: the GENIUS Act permits cash, insured bank deposits, and U.S. Treasury bills, notes, or bonds — but only with a remaining maturity of 93 days or less (SEE APPENDIX A). That cap is not a Northlight policy choice; it is written into the statute itself, and it is the same for every U.S.-regulated issuer. Both of Priya's two live drafts sit *well* inside that legal boundary — the question in front of her isn't about the legal ceiling at all.

**The Short Ladder** rolls almost the entire reserve into 4-week Treasury bills, re-bought every four weeks — the shortest maturity the desk regularly trades, and close to the posture Northlight has held since launch (SEE APPENDIX B).

**The Extended Ladder** shifts part of the reserve toward 6-week Treasury bills — a real, meaningfully longer maturity than the Short Ladder, though still less than half of what the GENIUS Act would actually allow (SEE APPENDIX C).

Every basis point of additional yield the Extended Ladder earns is real, recurring income for Northlight, computed against a reserve total in the tens of billions of dollars (SEE APPENDIX A). But a bill that hasn't matured yet still has to be sold at whatever price the market offers if Northlight needs the cash before maturity — a redemption wave, a rate shock, a stressed week — and the longer a bill's remaining life, the more its price can move against a sudden rate change before it matures back to par. That's the real trade-off: a small, real yield edge against a small, real increase in how far the reserve's price could ever drift from $1.00 (SEE APPENDIX D and APPENDIX E). Priya's monthly attestation locks today; whichever ladder she recommends is what auditors sign off on for the next cycle.

---

## Dilemma

You are Priya Nathan.

Do you:

**A.)** Recommend **the Short Ladder** — roll reserves almost entirely into 4-week Treasury bills, minimizing how far the reserve price can ever drift from $1.00 **OR**

**B.)** Recommend **the Extended Ladder** — shift part of the reserve into 6-week Treasury bills for more yield, still well inside the GENIUS Act's legal ceiling

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A scientific-notation reserve table.** Write Northlight's total reserve amount (Appendix A) in scientific notation, then compute each option's total annual dollar yield (reserve total × annual yield rate, Appendix B/C) and write both results in scientific notation, showing every intermediate step of the conversion. Every external figure this table relies on is drawn from the real, live sources cited in full in Appendix F.
- **D2 — An absolute-value peg-deviation worksheet.** For each of the five price snapshots in Appendix D, compute the peg deviation as an absolute-value expression, `|price − $1.00|`, in dollars, then convert that to basis points. Label each snapshot "small" or "historically large" by comparing it to Appendix E's reference deviations.
- **D3 — A yield-per-risk efficiency table.** For both options, divide D1's annual dollar yield by the option's duration-scaled peg-deviation figure in basis points (Appendix E) to get "dollars of annual yield earned per basis point of peg-deviation risk shouldered." State the percent difference between the two options' figures.
- **D4 — A sensitivity check.** Appendix E gives two different real, defensible ways of scaling Option B's risk figure to its longer duration — plus a "no extra risk" floor case. Recompute D3's efficiency table using each alternate reading for Option B, and state in your own words whether your recommendation would change under each one.
- **D5 — A recommendation memo.** State which ladder Priya should recommend, defended with D1's dollar figures, D3/D4's efficiency numbers, and Appendix A's hard constraint that both ladders are already inside the GENIUS Act's legal ceiling — so the choice is genuinely about how much yield is worth how much peg-deviation risk, not about legality.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Northlight's Reserve & Regulatory Constraints

| Quantity | Value |
|---|---|
| Total NLD reserve amount (used as Northlight's own reserve total for this case) | $73,434,000,000 [S1] |
| Attestation lock date (this cycle) | The last business day of the month [MA1] |
| Maximum permitted remaining maturity for any Treasury bill/note/bond held as stablecoin reserve, under the GENIUS Act (Section 4(a)(1)(A)(iii)) | 93 days [S7] |
| Frequency of Northlight's published reserve attestation | Monthly [MA1] |

*Note: Northlight Financial and the NLD stablecoin are a scenario construction for this case — there is no real company or token by this name. The reserve total is scaled to match a real, currently circulating U.S.-dollar stablecoin's disclosed size (Appendix F), used as a stand-in for Northlight's own (fictional) balance sheet.*

---

## Appendix B: Option A — The Short Ladder (4-Week Treasury Bills)

| Spec | Value |
|---|---|
| Instrument | U.S. Treasury bills, 4-week (28-day) maturity, continuously re-bought at each maturity |
| Annual yield (coupon-equivalent), as of 2026-09-01 | 3.75% [S6] |
| Typical time-to-maturity outstanding at any moment | Averages roughly half of 28 days, i.e. about 2 weeks |
| Comparable real-world posture | Close to the maturity profile the actual Circle Reserve Fund (USDXX), the money-market fund backing USDC, discloses: a 5-day weighted average maturity and 89.6% of assets maturing within 7 days [S2] |

---

## Appendix C: Option B — The Extended Ladder (6-Week Treasury Bills)

| Spec | Value |
|---|---|
| Instrument | U.S. Treasury bills, 6-week (42-day) maturity, continuously re-bought at each maturity |
| Annual yield (coupon-equivalent), as of 2026-09-01 | 3.81% [S6] |
| Maximum legally permitted maturity for this asset class, GENIUS Act | 93 days — 42-day bills sit well inside the ceiling, at less than half the legal maximum [S7] |
| Time-to-maturity outstanding at any moment | Averages roughly half of 42 days, i.e. about 3 weeks — 1.5× longer than Option A |

*Background, not part of the graded metric: a third draft, using 13-week (91-day) bills — the longest maturity the GENIUS Act allows — was on Priya's desk earlier. Using this case's own duration-scaling method (Appendix E), that draft's risk figure works out to about 54 bps against Option A's 30 bps, which made its yield-per-risk efficiency fall well short of both live options — why it's no longer on the table.*

---

## Appendix D: Five Peg-Price Snapshots (for the absolute-value worksheet, D2)

| Snapshot | NLD market price |
|---|---|
| 1 — an ordinary trading minute | $0.9997 |
| 2 — an ordinary trading minute | $1.0004 |
| 3 — a high-volatility hour, typical stablecoin drift | $0.9970 [S5] |
| 4 — a high-volatility hour, typical stablecoin drift | $1.0030 [S5] |
| 5 — the lowest recorded tick during a real, documented dollar-stablecoin reserve stress event | $0.8776 [S1] |

*Snapshots 3–5 are real, sourced price points from the stablecoin market (Appendix F) — not Northlight's own trading history, since Northlight is fictional — used here as realistic inputs for the absolute-value calculation. Snapshot 5 is real historical color: a documented, real, and far more severe reserve-related event than anything either live option here is actually being sized against (SEE Appendix E's note) — included so a Hero has to decide for themselves whether it's "small" or "historically large" relative to the case's own reference points, not so it can be mistaken for either option's risk figure.*

---

## Appendix E: Peg-Deviation Risk by Ladder Duration (for D3's efficiency table)

| Reference | Deviation from $1.00 | Basis points | How it's derived |
|---|---|---|---|
| Option A's real reference deviation (4-week ladder) | $0.0030 | 30 bps | Real, documented normal high-volatility-hour peg drift [S5] |
| Option B's risk-scaled reference deviation (6-week ladder) — **primary reading, used in D3** | $0.003674 | 36.74 bps | 30 bps × √(42 ÷ 28) — the square-root-of-time rule, the real method banking regulators use to scale a risk estimate from a shorter holding period to a longer one [S5, S9] |
| Alternate reading (for D4): linear duration scaling | $0.0045 | 45.00 bps | 30 bps × (42 ÷ 28) — scaling risk directly in proportion to duration, instead of by its square root [S9] |
| Alternate reading (for D4): no incremental duration risk (a floor case, not a realistic claim) | $0.0030 | 30.00 bps | Same as Option A — included only to establish a lower bound, not as a real prediction |

*Important note, stated plainly: both of Option B's risk figures above are *derived* — scaled from Option A's real, sourced 30 bps figure using a real, citable scaling method (S9) — not directly observed prices for a 6-week ladder specifically, since no such real, dollar-for-dollar historical event exists to measure. The "how it's derived" column shows exactly how, so a Hero can check the arithmetic and challenge the choice of method — that is a legitimate, intended move in Challenge D4.*

---

## Modeling Assumptions

> These figures are **not sourced** from Northlight (a fictional company) or, in one case, derived
> rather than directly observed. They are stated scenario assumptions chosen by the case author, or
> real external figures/methods applied to Northlight as the closest available proxy. A Hero may
> challenge any of them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Attestation lock date / cadence | Last business day of the month; monthly | Matches the real, disclosed cadence of major U.S. dollar stablecoin issuers' third-party attestations (Appendix F). Decorative framing detail, not load-bearing for the math. | None. |
| MA2 | Appendix D/E's "normal drift" figure (30 bps) is attributed to USDT specifically in its own source, not to Northlight/NLD | 30 bps, applied as Option A's real reference deviation and as the base figure Option B's derived deviation scales from | No public figure exists specifically for a fictional company; the sourced figure describes real stablecoin behavior generally and is the best available real analog. | Does not change `margin_pct` at all — it cancels out of the ratio between the two options' efficiency figures, since Option B's deviation is a fixed multiple of it. Load-bearing only for the displayed dollar-per-bp numbers, not for which option wins. |
| MA3 | Option B's peg-deviation risk figure is derived by scaling Option A's real 30 bps figure to Option B's own duration, using the square-root-of-time rule — the real method (recommended by banking regulators) for scaling a risk estimate across holding periods | 36.74 bps (primary reading) | See Appendix F, S9: a real academic paper confirming the formula and its real regulatory (Basel Committee) endorsement. | **HIGH — this is the single assumption the whole balance computation turns on.** See RESEARCH_LOG.md and D4: the square-root-of-time reading (primary) keeps Option A's advantage under 20%; a linear-scaling reading widens it; a "no extra risk" floor case flips the recommendation to Option B entirely. |
| MA4 | Reserve total ($73,434,000,000) is a live, moving market figure (Appendix F, S1), frozen here at a single as-of date | 2026-09-01 | Per this project's own rule on citing a still-changing real quantity: every live figure in this case (reserve total, both Treasury yields) is frozen at the same single date, 2026-09-01, stated explicitly. | Does not change `margin_pct` — the reserve total cancels out of the dollars-per-basis-point ratio (D3), since it multiplies both options' annual-yield figures identically. It is load-bearing only for D1's absolute dollar figures. |

---

## Appendix F: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Total circulating supply of a real, major U.S.-dollar stablecoin (used as Northlight's reserve-total proxy); and that same stablecoin's all-time-low price and date | Market cap $73.434 billion; ATL $0.8776 on 2023-03-11 | [CoinGecko — USDC](https://www.coingecko.com/en/coins/usdc) | Accessed 2026-09-01 | HIGH (real, live, precisely dated, directly confirmed on the page) |
| S2 | Weighted average maturity and short-maturity concentration of a real money-market fund backing a major dollar stablecoin's reserves | WAM 5 days; 89.6% of assets maturing within 1–7 days; 7-day SEC yield 3.61%; 30-day SEC yield 3.57%; fund size $60,717 million | BlackRock — [Circle Reserve Fund (Institutional shares), July 2026 Factsheet](https://www.blackrock.com/cash/literature/fact-sheet/circle-reserve-fund-institutional-fact-sheet.pdf) | As of 2026-07-31 | HIGH (primary-source factsheet, PDF fetched and confirmed directly) |
| S4 | A real Federal Reserve publication's account of a 2023 dollar-stablecoin reserve-related depeg: trough price, an alternate hourly-open-price reading, and days to full recovery | Trough $0.86 (1,400 bps); hourly-open low ≈$0.90 (1,000 bps); full recovery by the 3rd day | Chuan Du, Ria Sonawane, Cy Watsky (Federal Reserve Board) — ["In the Shadow of Bank Runs: Lessons from the Silicon Valley Bank Failure and Its Impact on Stablecoins"](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html), FEDS Notes | 2025-12-17 | HIGH (Federal Reserve primary publication, fetched and confirmed directly) |
| S5 | Typical/normal dollar-stablecoin peg drift during high-volatility trading hours | "Routinely drifts to $0.997 or $1.003... snaps back within minutes through arbitrage" (30 bps each direction) | [Eco — "Stablecoin Depeg: What Causes It and How to Spot Risk"](https://eco.com/support/en/articles/15182160-stablecoin-depeg-what-causes-it-and-how-to-spot-risk) | Accessed 2026-09-01 | MEDIUM (real, fetched and confirmed directly; describes USDT specifically, applied here as a general stablecoin-behavior proxy — see MA2) |
| S6 | Real, current U.S. Treasury bill coupon-equivalent yields, 4-week, 6-week, 8-week and 13-week maturities | 4-week: 3.75%; 6-week: 3.81%; 8-week: 3.82%; 13-week: 3.87% | U.S. Department of the Treasury — [Daily Treasury Bill Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates) | 2026-09-01 | HIGH (primary government source, CSV data fetched and confirmed directly for the exact date) |
| S7 | The GENIUS Act's statutory maturity cap on Treasury securities held as payment-stablecoin reserves | "Treasury bills, notes, or bonds with a remaining maturity of 93 days or less, or issued with a maturity of 93 days or less" — Section 4(a)(1)(A)(iii) | [Ridgeway Financial Strategies — "Stablecoin Reserve Requirements After the GENIUS Act"](https://www.ridgewayfs.com/stablecoin-reserve-requirements-genius-act/), quoting the statute (GENIUS Act of 2025, P.L. 119-27) | Accessed 2026-09-01 | MEDIUM (secondary source, but quotes precise statutory section language directly; the 93-day figure is independently corroborated by multiple other real-law summaries found in research) |
| S9 | The square-root-of-time rule: the standard, regulator-recommended method for scaling a risk/volatility estimate from a shorter holding horizon to a longer one | T-period risk = 1-period risk × √T; "recommended by banking supervisors (see the Basel Committee on Banking Supervision, 1996)" | Jón Daníelsson & Jean-Pierre Zigrand (LSE Financial Markets Group) — ["On Time-Scaling of Risk and the Square-Root-of-Time Rule"](https://researchonline.lse.ac.uk/id/eprint/24827/1/dp439.pdf) | March 2003 (working paper); accessed 2026-09-01 | HIGH (real academic working paper, fetched and confirmed directly as PDF text) |

---

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Scientific Notation
- Absolute Value

**"How to…" questions**

- How to write a number in scientific notation given its standard notation
- How to evaluate an absolute value expression

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
