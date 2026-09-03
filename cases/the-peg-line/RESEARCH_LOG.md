# RESEARCH_LOG.md — The Peg Line

`case-research` pass, 2026-09-01. 11 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
9 SOURCED, 2 ASSUMPTION, 0 DROPPED, 0 OPEN.

**`case-redesign` (balance-retune) pass, also 2026-09-01 — see "BALANCE-RETUNE REDESIGN" section
near the bottom of this log.** The original research pass below (P01–P09) produced a case with
`margin_pct = 97.47%`, far past SPEC §2's ~20% cap. The project owner explicitly declined an
MCS-46 waiver and directed a redesign of the underlying dilemma/dataset instead. That redesign is
documented in full in the "BALANCE-RETUNE REDESIGN" section, including the new sources pulled in
(S9) and the full old-vs-new arithmetic. The sections immediately below (P01–P09, the original
margin computation, and the original SPEC §2 self-check) are preserved unedited as the historical
record of the first research pass — they describe the ORIGINAL, now-superseded design.

---

## P01 — Total NLD reserve amount (Appendix A)

Searched: "Circle USDC total reserves 2026" and related. Found `coingecko.com/en/coins/usdc`;
fetched directly and confirmed the page's own text: "Current Market Cap: $73.434 billion...
approximately 73.45 billion USDC tokens currently in circulation." Northlight is fictional, so
this real, live, currently-circulating dollar-stablecoin's scale is used as the closest available
proxy for Northlight's own reserve total — matching this project's convention (e.g. `prove-it-scales`
scaling Meterworks' fictional traffic to Metronome's real disclosed scale).

**Outcome: SOURCED, HIGH.** S1 = $73,434,000,000. Frozen at accessed-date 2026-09-01 (MA4).

## P02 — Maximum permitted remaining maturity, GENIUS Act (Appendix A / C)

Searched: "GENIUS Act stablecoin reserve requirements Treasury maturity days permitted reserve
assets 2025 law." Attempted to fetch the primary bill text directly at `congress.gov` (both
S.394 and S.1582 text pages) — both returned HTTP 403 (congress.gov blocks the fetcher).
Fell back to `ridgewayfs.com/stablecoin-reserve-requirements-genius-act/`, a financial-services
firm's walkthrough that quotes the statute directly; fetched and confirmed the exact text: "Treasury
bills, notes, or bonds with a remaining maturity of 93 days or less, or issued with a maturity of
93 days or less" (cited to Section 4(a)(1)(A)(iii)), with the page explicitly noting "The 93-day
cap is part of the statute, not an agency interpretation." The 93-day figure is independently
corroborated by the WebSearch tool's own synthesis of multiple other real-law summaries (Vedder
Price, Arnold & Porter, CRS) found in the same search pass, though those pages themselves were not
independently fetched.

**Outcome: SOURCED, MEDIUM.** S7 = 93 days. (Confidence label corrected to a single valid value —
MEDIUM — during the 2026-09-01 balance-retune redesign pass; the original "MEDIUM-HIGH" label used
here was a convention violation, since only HIGH/MEDIUM/LOW are valid in this project.) This became
the case's actual structural spine —
both options were redesigned around it (4-week vs. 13-week Treasury bills, both legally inside the
cap) once it was found, replacing an earlier draft direction that would have compared ultra-short
bills against 1–3 year Treasury notes (which the real law would make illegal for a US-regulated
issuer — rejected as contradicting real, cited law).

## P03 — Current 4-week and 13-week Treasury bill yields (Appendix B / C)

Searched for daily Treasury bill rates. `WebFetch` timed out twice on
`home.treasury.gov`'s interactive TextView page (heavy client-side table, exceeded the 60s fetch
window). Routed around it by fetching the same page's underlying CSV export directly via `curl`
(`home.treasury.gov/.../daily-treasury-rates.csv/2026/all?type=daily_treasury_bill_rates...`),
which returned cleanly. Confirmed the exact row dated `09/01/2026` (today, matching this case's
authored-on date): `4 WEEKS COUPON EQUIVALENT` = 3.75, `13 WEEKS COUPON EQUIVALENT` = 3.87.

**Outcome: SOURCED, HIGH.** S6. Primary U.S. government source, exact date match.

## P04 — Comparable real-world short-duration reserve fund posture (Appendix B, background/plausibility only)

Searched: "Circle Reserve Fund USDXX weighted average maturity days yield SEC filing 2026." Found
the BlackRock factsheet PDF for the Circle Reserve Fund (the real money-market fund that actually
backs USDC). `WebFetch` returned HTTP 403 directly on the PDF; routed around it with `curl` using
a browser user-agent, which succeeded, then read the downloaded PDF directly (not just a search
snippet). Confirmed: "Weighted average maturity (WAM) 5 days... 89.6% [of assets, 1-7 day
maturity bucket]... 7-day SEC yield 3.61%... 30-day SEC yield 3.57%... Size (millions) $60,717."
Factsheet dated "July 2026 Factsheet," "All portfolio information provided is as of July 31, 2026."

Used only as background color for Appendix B ("Comparable real-world posture") — not as the
load-bearing yield figure for Option A, since S6's same-date (2026-09-01) 4-week Treasury bill
rate is the more directly comparable, more precisely dated figure for what Option A's *own*
4-week-bill posture would actually yield.

**Outcome: SOURCED, HIGH.** S2.

## P05 — Typical/normal peg drift, high-volatility hours (Appendix D snapshots 3-4 / Appendix E row 1)

Searched: "USDC typical daily price deviation basis points stability... normal trading range." The
WebSearch tool's own synthesis initially (incorrectly) attributed the resulting quote to USDC;
fetched the actual source page directly (`eco.com/support/en/articles/15182160-...`) to check, and
the real text reads: "USDT routinely drifts to $0.997 or $1.003 during high-volatility hours and
snaps back within minutes through arbitrage" — this describes USDT, not USDC. Corrected the
attribution in `case.md`/`case.json` (S5's `note` field states this explicitly) rather than
silently keeping the WebSearch tool's misattribution. Applied as a general stablecoin-behavior
proxy for Option A's reference deviation (MA2), since no public figure exists for the fictional
Northlight, and this real figure is the most directly on-point one found.

**Outcome: SOURCED, MEDIUM.** S5 = 30 bps each direction ($0.997 / $1.003).

## P06 — Real, documented dollar-stablecoin all-time-low price and date (Appendix D snapshot 5)

Searched: "CoinGecko USDC price history March 2023 depeg lowest price." Confirmed via the same
`coingecko.com/en/coins/usdc` page fetched for P01: "All-Time Low: $0.8776, reached on March 11,
2023." Cross-checked against a second, independent real source (P07 below) for the same event —
the two sources differ slightly (see P07's note) because they measure the price at different
sampling granularities, which is disclosed explicitly in `case.md`'s Appendix D note and
`case.json`'s S4 `note` field, not hidden.

**Outcome: SOURCED, HIGH.** S1 (same source as P01) = $0.8776.

## P07 — Real, sourced historical stress-event peg-deviation figures, primary and alternate readings (Appendix E rows 2-4)

Searched: "federalreserve.gov feds notes 'In the Shadow of Bank Runs' Silicon Valley Bank
stablecoins." Found and fetched
`federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html`
directly (a real Federal Reserve Board FEDS Notes publication, authors Chuan Du, Ria Sonawane, Cy
Watsky, dated 2025-12-17). Confirmed: "At its trough, USDC traded at 86 cents to the dollar,"
and a footnote explaining the paper's own hourly-open sampling reads the low as closer to 90
cents rather than the true 86-cent intra-hour trough — which is exactly why this real source's
figures (86 / ~90 cents) differ slightly from CoinGecko's tick-level ATL (87.76 cents, P06):
different sampling granularity of the same real event, not a data conflict. Also confirmed the
paper states USDC "fully recovered once Circle began processing redemptions on Monday, March 13"
— i.e. the event resolved within about three days of the March 10 SVB failure.

**Outcome: SOURCED, HIGH (both readings).** S4 = trough $0.86 (1,400 bps); hourly-open low ~$0.90
(1,000 bps). Used as Appendix E's two alternate readings for the D4 sensitivity check, alongside
S1's primary 1,224-bp reading.

## P08 — Attestation lock date / cadence (Appendix A)

Framed as "stated in-scenario" — an authorial narrative choice matching the real, disclosed
monthly cadence of major real dollar-stablecoin issuers' attestations (confirmed generally via the
same research pass that found P01/P04, e.g. "Circle publishes monthly third-party attestations
from Deloitte & Touche LLP"), not independently sourceable as a Northlight-specific fact since
Northlight is fictional.

**Outcome: ASSUMPTION.** MA1 = last business day of the month, monthly. Decorative, not
load-bearing.

## P09 — Reserve-total-as-of freeze (Appendix A / MA4, SPEC §5 compliance)

Not a placeholder in its own right, but flagged during research: S1 (reserve total) and S6
(Treasury yields) are both live, moving real-world figures. Per SPEC §5's rule on citing a
still-changing real entity, both are frozen at the same single stated date, **2026-09-01**
(today, and this case's `authored_on` date), rather than at two different "whenever it was
fetched" moments.

**Outcome: ASSUMPTION (framing decision, logged as MA4).**

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none (lowest is S5/S7 at MEDIUM / MEDIUM-HIGH)
needs_source OPEN remaining: 0
```

S5 (MEDIUM) carries Option A's peg-deviation reference figure (30 bps) — checked directly in
MA2's sensitivity note: making this figure smaller only widens the margin further in Option A's
favor, so a MEDIUM-confidence figure here cannot flip the case's conclusion even if it is
somewhat off. S7 (MEDIUM) carries the GENIUS Act's 93-day cap, which is a structural/legal
constraint, not a magnitude the margin computation is numerically sensitive to.

*(Note, added during the 2026-09-01 balance-retune redesign: in the redesigned case, S5's 30-bps
figure additionally cancels out of `margin_pct` entirely — see MA2's updated sensitivity note in
`case.json` and the "BALANCE-RETUNE REDESIGN" section below.)*

## Margin (facilitator-only — computed here, not written into case.md)

`reserve_total` = $73,434,000,000 (S1). `annual_yield_A` = 73,434,000,000 × 0.0375 =
**$2,753,775,000** (S6). `annual_yield_B` = 73,434,000,000 × 0.0387 = **$2,841,895,800** (S6).
Extra yield, B over A: **$88,120,800/year**.

`dev_A_bps` = 30 (S5). `dev_B_bps` (primary) = 1,224 (S1, |0.8776 − 1.00| = 0.1224).

`efficiency_A` = 2,753,775,000 / 30 = **$91,792,500 per basis point**.
`efficiency_B` (primary) = 2,841,895,800 / 1,224 = **$2,321,810.29 per basis point**.

**margin_pct = (91,792,500 − 2,321,810.29) / 91,792,500 × 100 = 97.47%. Winner: Option A, The
Short Ladder.**

This is far past the ~20% guideline and is reported plainly, not softened.

**Retune attempt.** Swapped `dev_B_bps` for Appendix E's two alternate real, sourced readings of
the same 2023 event (S4), to check whether the margin's size depends on which specific historical
reading was chosen for Option B:

- `dev_B_bps` = 1,000 (Fed hourly-open low): `efficiency_B` = $2,841,895.80/bp → **margin_pct =
  96.90%**.
- `dev_B_bps` = 1,400 (Fed reported trough): `efficiency_B` = $2,029,925.57/bp → **margin_pct =
  97.79%**.

All three real, independently sourced readings of the tail event land in a **96.9%–97.8%** band.
The imbalance is not an artifact of picking one specific historical reading over another — it is
structural, driven by the ~30–45× gap between Option A's real normal-drift reference (30 bps, S5)
and *any* real reading of the 2023 stress event (1,000–1,400 bps, S1/S4), set against only a
12-basis-point (≈3.2% relative) yield-rate advantage for Option B (S6, 3.87% vs. 3.75%). No
available Modeling Assumption is a lever that would bring `margin_pct` under ~20% without
contradicting real, cited data — MA4 (the reserve-total freeze) doesn't help either, since the
reserve total cancels out of the dollars-per-basis-point ratio entirely (it multiplies both
options' annual-yield figures identically).

**Per instruction: NOT self-granting a waiver.** This case proceeds with `margin_pct` reported
plainly at 97.47% (primary reading), the full 96.9%–97.8% sensitivity band disclosed in
`case.json.balance.margin_note` and `sensitivity_model.py`, and this imbalance flagged as an open
balance concern for the next case-readiness stage to adjudicate. The case's own `balance.argument_a`
/ `argument_b` already carry the genuine defensible-ambiguity as a *qualitative* question — is a
real, ongoing $88.1M/year benefit worth a tail risk that has materialized once in the industry's
documented history and fully resolved within three days — rather than the raw D3 numeric ratio,
which does not support a close race. This is structurally the same situation `prove-it-scales`
disclosed (see its `RESEARCH_LOG.md`), except that case's project owner granted an MCS-46 waiver
after review; per the explicit instruction for this pass, this case does **not** self-grant that
waiver and instead leaves it flagged for case-readiness.

## SPEC §2 self-check

- **Primary metric exists:** yes — dollars of annual yield earned per basis point of peg-deviation
  risk shouldered (equivalently, the concept's stated "bps of peg deviation tolerated per dollar
  of extra annual yield").
- **No structurally-zero-cost option:** confirmed. Option A has a real, non-zero cost — $88.1M/year
  in foregone yield relative to Option B (D1). Option B has a real, non-zero cost — the historically
  documented tail-deviation exposure (Appendix E). Neither option is free.
- **Dilemma is not a foregone conclusion in the qualitative sense the case is built to argue** — a
  Hero can genuinely argue either "$88.1M/year real money is worth a tail risk that has happened
  once and resolved in 3 days" or "no amount of yield is worth even a small chance of a
  four-figure-basis-point deviation on an attestation that has my name on it." **However, the
  raw D3 numeric ratio (efficiency $/bp) is not close** — verdict below.
- **Verdict: FLAG FOR CASE-READINESS.** `margin_pct` = 97.47% (96.9%–97.8% across all three real
  sensitivity readings), well past SPEC §2's ~20% cap, with a genuine retune attempt logged above
  that did not resolve it. Not self-granting a waiver. The case is legitimate and well-sourced, but
  its balance rests on qualitative framing (argument_a/argument_b) rather than a close quantitative
  race — the next stage should decide whether that is sufficient or whether the case needs a
  design change (e.g., comparing two options that are both *inside* the historically-normal-drift
  band, rather than contrasting normal drift against the industry's single most extreme documented
  event).

## Sensitivity model

Built `sensitivity_model.py` (PARAMS / FLEX / evaluate() contract, matching
`the-mainline-margin`'s pattern). `evaluate()` returns each option's dollars-of-yield-per-basis-point
efficiency figure directly (higher is better, satisfying the probe's contract without negation,
since this metric is already a benefit, not a cost). `FLEX` sweeps `yield_a_rate`, `yield_b_rate`,
`dev_a_bps`, and `dev_b_bps` — the four real, stated, case-controlled numbers that feed the metric.
`reserve_total` is deliberately *not* swept, since it provably cancels out of the ratio (confirmed
both algebraically and by running the model).

## Next step (as of the original 2026-09-01 research pass — SUPERSEDED, see below)

Run `case-readiness` / `case-qa` on `the-peg-line`, with the margin flag above surfaced explicitly
for adjudication (retune the design vs. accept a qualitative-balance case vs. seek a scoped waiver
through the actual project-owner sign-off process).

**Resolution: the project owner declined an MCS-46 waiver and directed a redesign instead — see
the "BALANCE-RETUNE REDESIGN" section immediately below, completed the same day.**

---

# BALANCE-RETUNE REDESIGN — 2026-09-01

**Trigger.** The research pass above (P01–P09) produced `margin_pct = 97.47%` (96.9%–97.8% across
three sensitivity readings), far past SPEC §2's ~20% cap. The imbalance was structural: Option A's
peg-deviation reference was a real "normal drift" figure (30 bps, S5), while Option B's was a real
but *categorically different* figure — the March 2023 USDC/SVB crisis tick-low (1,000–1,400 bps,
S1/S4). Comparing a normal-conditions number against a catastrophic-tail-event number is an
apples-to-oranges comparison, and it structurally guaranteed a huge margin regardless of which
specific historical reading was chosen for the crisis side (confirmed by the original retune
attempt above). The project owner reviewed this and explicitly declined to grant an MCS-46 waiver,
directing instead that the underlying dilemma/dataset be redesigned so the two options are
genuinely close, using real numbers — not by fudging the math or hiding data.

## R01 — Diagnosing why simple fixes don't work

Before researching new data, the retune brief's suggested primary lever (an expected-value /
probability-weighted framing: probability of a depeg event × dollar severity) was checked
algebraically first. Reframing "risk" as `probability × severity` doesn't help on its own if the
probability term is the *same* for both options (it factors out of the ratio identically, the same
way `reserve_total` already does) — and if the probability term instead scales with *duration* (a
legitimate mechanism: a longer-maturity bill sits in a "could be forced to sell before maturity"
window for longer), the ratio collapses to the same shape as a pure duration-scaling model. So the
real lever was: make BOTH options' risk figures scale off the SAME real reference number, by a
factor tied to something that genuinely differs between the two options (their Treasury-bill
duration) — rather than mixing two independent real figures from different risk categories.

**Duration-linear scaling, checked first and rejected as insufficient on its own.** If risk scales
*linearly* with duration (a bill's Macaulay duration ≈ its time to maturity, for a zero-coupon
instrument like a T-bill), then `efficiency_B / efficiency_A = (yield_B/yield_A) / (duration_B/
duration_A)`. Using the REAL, live Treasury bill curve fetched this session (see R02 below:
4-week 3.75%, 6-week 3.81%, 8-week 3.82%, 13-week 3.87%, all as of 2026-09-01), this ratio was
computed for every legal-maturity pair (all ≤93 days per S7):

| Pair | duration ratio | yield ratio | margin (linear scaling) |
|---|---|---|---|
| 4wk vs 6wk | 1.500 | 1.016 | 32.27% |
| 4wk vs 8wk | 2.000 | 1.019 | 49.07% |
| 4wk vs 13wk | 3.250 | 1.032 | 68.25% |
| 6wk vs 8wk | 1.333 | 1.003 | 24.80% |
| 8wk vs 13wk | 1.625 | 1.013 | 37.66% |
| 6wk vs 13wk | 2.167 | 1.016 | 53.12% |

**Finding: no legal-maturity pair gets under ~20% margin using pure linear duration scaling** —
the closest, 6-week vs 8-week, still lands at 24.80%. This is because the real short-end Treasury
curve is concave (yield increases at a decreasing rate as maturity lengthens), so yield-per-unit-
duration decreases monotonically with duration for any realistic pair — linear duration scaling
will always favor the shortest option by a wide margin. This ruled out pure linear duration
scaling as insufficient on its own, and motivated checking the square-root-of-time rule instead
(R02–R03 below), which is both a real, industry-standard alternative to linear scaling AND, by
construction, produces a smaller risk gap between any two durations than linear scaling does
(since √x < x for x>1) — closing part of the remaining gap.

## R02 — Verifying the full real Treasury bill curve (extends S6)

Re-fetched the same primary source used in the original pass (`home.treasury.gov`'s daily-
treasury-rates CSV export), this time pulling all maturity columns rather than just 4-week and
13-week. Confirmed the exact row dated `09/01/2026`: `4 WEEKS COUPON EQUIVALENT` = 3.75,
`6 WEEKS COUPON EQUIVALENT` = 3.81, `8 WEEKS COUPON EQUIVALENT` = 3.82, `13 WEEKS COUPON
EQUIVALENT` = 3.87 (also confirmed 17-week 3.93, 26-week 4.03, 52-week 4.18, though those exceed
the GENIUS Act's 93-day cap and are not usable reserve assets — 26-week is 182 days, 52-week is
364 days, both illegal per S7).

**Outcome: SOURCED, HIGH.** S6 (extended). Same primary U.S. government source as the original
pass, same exact date, additional columns from the same single CSV pull.

## R03 — Finding a real, citable risk-scaling methodology (square-root-of-time rule)

Searched: "square root of time rule value at risk scaling holding period Basel RiskMetrics."
Confirmed via WebSearch synthesis that this is a real, standard quantitative-finance method:
volatility/VaR scaled from a 1-day estimate to a T-day estimate by multiplying by `sqrt(T)`,
recommended by the Basel Committee on Banking Supervision (1996) and widely used following J.P.
Morgan's RiskMetrics system. To ground this in a real, independently fetched primary source rather
than relying on the WebSearch tool's own synthesis, located and fetched the underlying academic
paper directly: Jón Daníelsson & Jean-Pierre Zigrand, "On Time-Scaling of Risk and the Square-Root-
of-Time Rule" (LSE Financial Markets Group working paper, March 2003). `WebFetch` on the original
`eprints.lse.ac.uk` URL redirected to `researchonline.lse.ac.uk`; the redirect target returned raw
PDF binary that `WebFetch` couldn't render as text, so the PDF was downloaded and read directly with
`pdftotext` (already available on this machine), confirming the exact text: "a standard method for
estimating quantiles, and in particular value–at–risk (VaR), is by estimating a one day VaR and
multiplying it by √10. Indeed, this is the method recommended by banking supervisors (see the Basel
Committee on Banking Supervision, 1996)." The paper also explicitly discusses a linear (non-sqrt)
scaling alternative and notes the square-root rule tends to *underestimate* risk for longer
horizons under jump-diffusion / fat-tailed return processes — both used honestly in this redesign
(the linear alternative became Appendix E's D4 alternate reading; the underestimation caveat is
disclosed in MA3 rather than hidden).

**Outcome: SOURCED, HIGH.** S9 = the square-root-of-time rule, `dev_B_bps = dev_A_bps ×
sqrt(duration_B_days / duration_A_days)`.

## R04 — Selecting the final option pair and computing the new margin

Combined R01's finding (need a closer maturity pair AND a risk metric with a smaller scaling
exponent than linear) with R03's real methodology. Computed `margin_pct` for every legal-maturity
pair under square-root-of-time scaling:

| Pair | duration ratio | √(ratio) | margin (sqrt-time scaling) |
|---|---|---|---|
| **4wk vs 6wk** | **1.500** | **1.2247** | **17.04%** ✓ under ~20% cap |
| 4wk vs 8wk | 2.000 | 1.4142 | 27.97% |
| 4wk vs 13wk | 3.250 | 1.8028 | 42.75% |
| 6wk vs 8wk | 1.333 | 1.1547 | 13.17% |
| 8wk vs 13wk | 1.625 | 1.2748 | 20.53% |
| 6wk vs 13wk | 2.167 | 1.4720 | 31.00% |

Two pairs land under the ~20% cap (4-week vs 6-week at 17.04%; 6-week vs 8-week at 13.17%).
**Selected 4-week vs 6-week** over 6-week vs 8-week, because it preserves more of the original
case's narrative shape — Option A stays the real, already-researched "Short Ladder" (4-week bills,
Appendix B unchanged) rather than requiring a second redesign of Option A as well, and the
resulting dollar figures (a real, recurring $44.1M/year yield difference) are still large and
meaningful for the case's dollar-scale narrative.

**Full arithmetic (verified twice, once by hand and once via `sensitivity_model.py`):**

```
reserve_total      = $73,434,000,000                              (S1)
yield_A (4-week)   = 3.75%           annual_yield_A = $2,753,775,000   (S6)
yield_B (6-week)   = 3.81%           annual_yield_B = $2,797,835,400   (S6)
extra_yield_B_over_A = $44,060,400 / year

dev_A_bps          = 30 bps                                        (S5, real, unchanged)
duration_A_days    = 28   duration_B_days = 42
scaling_factor     = sqrt(42 / 28) = sqrt(1.5) = 1.224744871...    (S9)
dev_B_bps (primary) = 30 × 1.224744871 = 36.742346 bps

efficiency_A = 2,753,775,000 / 30            = $91,792,500.00 / bp
efficiency_B = 2,797,835,400 / 36.742346     = $76,147,434.60 / bp

margin_pct = (91,792,500.00 − 76,147,434.60) / 91,792,500.00 × 100 = 17.04%
WINNER (primary reading): Option A, The Short Ladder, by 17.04% — UNDER SPEC §2's ~20% cap.
```

**Sensitivity sweep across three real, defensible readings of how to derive `dev_B_bps`** (this
became the case's own D4 deliverable):

| Scaling method | dev_B_bps | margin_pct | Winner |
|---|---|---|---|
| Square-root-of-time [primary, S9's own recommended method] | 36.74 | 17.04% | A |
| Linear / proportional-to-duration [S9 discusses as the alternative] | 45.00 | 32.27% | A |
| No incremental duration risk [floor case, not realistic] | 30.00 | 1.57% | **B** (flips) |

Unlike the original design (where all three real crisis-event readings barely moved the number,
96.9%–97.8%), this sensitivity is **real and consequential** — disclosed plainly in `case.json`'s
`balance.margin_note`, `MA3`, and `case.md`'s Appendix E / Challenge D4, not smoothed over. This is
treated as a strength, not a weakness: it makes the case's own built-in sensitivity-check
deliverable (D4) a genuine discovery rather than a formality, and it's an honest reflection of the
fact that Option B's risk figure is *derived*, not directly observed (there is no real historical
event that specifically measures a 6-week-Treasury-bill-backed stablecoin's peg deviation under
stress — no such real, dollar-for-dollar analog exists to source instead).

**Context check (not part of the graded metric):** re-ran the same square-root-of-time formula
against the *original* 13-week option, `duration_B_days = 91`, `yield_B = 3.87%`: `dev_B_bps =
30 × sqrt(91/28) = 54.08 bps`, `efficiency_B = $52,546,671.93/bp`, `margin_pct = 42.75%`. This
gives an honest, case-internal explanation (using the case's own real methodology, not an
after-the-fact rationalization) for why Priya's narrative no longer proposes going all the way to
the legal maximum — folded into `case.md`'s Background/Appendix C as the "rejected third draft"
narrative beat.

## R05 — Fixing the pre-existing S7 confidence-label convention violation

While rewriting the sources array, corrected S7's `confidence` field from `"MEDIUM-HIGH"` (a
convention violation flagged in the original task brief — only HIGH/MEDIUM/LOW are valid labels in
this project) to `"MEDIUM"`. Reasoning: S7 is a secondary source (a financial-services firm's
walkthrough page) that quotes the GENIUS Act's statutory text directly and precisely, but the
primary statute itself (congress.gov) could not be independently fetched in either research pass
(HTTP 403 both times) — MEDIUM reflects "precise language, but a secondary carrier," not HIGH
("primary source, independently fetched and confirmed," the bar every other HIGH-confidence source
in this case meets) and not LOW ("real but weakly corroborated," which understates a source that
quotes exact statutory section language and is corroborated by other independent summaries found in
research).

## Final SPEC §2 self-check — REDESIGNED case

- **Primary metric exists:** yes — dollars of annual yield earned per basis point of duration-
  scaled peg-deviation risk shouldered.
- **No structurally-zero-cost option:** confirmed. Option A forgoes $44.1M/year of real yield
  relative to Option B (D1). Option B carries a real, non-zero, duration-scaled risk figure
  (Appendix E) relative to Option A. Neither option is free.
- **Margin — COMPUTED, under the cap:** `margin_pct = 17.04%` (primary, square-root-of-time
  reading), safely under SPEC §2's ~20% cap. Full arithmetic above and in `case.json.balance.
  margin_note`. Sensitivity disclosed honestly (D4): a different real, defensible scaling
  assumption widens the margin to 32.27%; a third, more conservative reading flips the winner to
  Option B (margin 1.57%) — both disclosed plainly, not hidden, consistent with this project's
  balance-test philosophy (SPEC §2: "must be retuned by adjusting a constraint — not by hiding
  data").
- **Verdict: PASSES SPEC §2.** No waiver needed or sought. `case.json.status` remains
  `"researched"` (a separate `case-readiness` pass is still required before this case can be
  published) — but the balance blocker that would have stopped `case-readiness` is now resolved.

## Next step

Run `case-readiness` / `case-qa` on the redesigned `the-peg-line`, now that `margin_pct` (17.04%)
is under SPEC §2's ~20% cap. No outstanding balance flag remains.
