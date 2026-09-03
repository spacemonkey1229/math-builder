# RESEARCH_LOG.md — The Fee Ladder

`case-research` pass, 2026-09-01. 10 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md` /
`case.json.needs_source[]`. 3 SOURCED, 7 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED,
0 OPEN.

---

## P01 — Real, publicly disclosed custody fee schedule #1 (Appendix E, row 1)

Searched: `SEC EDGAR full text search custodian fee schedule tiered basis points "assets under
custody" N-CSR fee table` (WebSearch). Result surfaced a State Street Bank and Trust Company
"Form of Custodian Fee Schedule" exhibit. `WebFetch` returned HTTP 403 on the SEC Archives URL
(SEC blocks the fetcher's default UA); routed around it with `curl -A "MathBuilderCaseResearch
manan.atit@gmail.com"` directly against the raw `.htm` filing, which returned full page text.

Confirmed, in the raw filing text: "STATE STREET BANK and TRUST COMPANY. CUSTODIAN FEE SCHEDULE
THE GABELLI GLOBAL SMALL AND MID CAP VALUE TRUST ... I. Domestic Custody ... First $500 Million ...
.50 Basis Points ... Remainder ... .3875 Basis Points." Confirmed the filing/exhibit date via the
EDGAR directory listing (`Last Modified` column on the accession's file index): 2013-09-11.

**Outcome: SOURCED, HIGH.** S1. Real institutional custody bp-rate magnitude anchor at the low end
of the case's range — used to justify Appendix C/MA6's Tier 4 rate (0.50 bp, chosen to echo this
figure exactly) and cited directly in Appendix E.

## P02 — Real, publicly disclosed custody fee schedule #2, a different rate magnitude (Appendix E, row 2)

Searched: `"custody fee" schedule basis points tiered "first $" million SEC prospectus custodian
agreement` (WebSearch). Also attempted a targeted search for a real 4-tier schedule (`"1.00 basis
points" "first" billion custody "administration fee" ".75 basis points" ".50 basis points" SEC`) to
find a real multi-tier example; the two most promising named filings that search surfaced either
returned HTTP 403 even via `curl` retry with a descriptive User-Agent, or (for one, a Northern
Trust custody agreement) the fee schedule itself was not embedded as text in the filed exhibit
(Schedule C wasn't reproduced inline). Did not force a fit — moved to a different real filing
instead rather than guessing at redacted figures.

Fetched `d440242dex99g3.htm` (State Street / Green Century Funds) via `curl` with the same
descriptive User-Agent after a first `WebFetch` attempt also 403'd. Confirmed, in the raw filing
text: "STATE STREET BANK AND TRUST COMPANY GREEN CENTURY FUNDS CONFIDENTIAL FEE SCHEDULE AS OF
JULY 1, 2012 ... First $150mm in assets ... 7.0 bps ... Assets in excess of $150mm ... 4.0 bps ...
Monthly Minimum per Fund for the Green Century Funds ... $3,826.67."

**Outcome: SOURCED, HIGH.** S2. Real institutional custody bp-rate magnitude anchor at the high end
of the case's range (a smaller fund pays a materially higher bp rate than the larger Gabelli trust
in S1) — together S1 and S2 establish the real 0.3875-7.0 bp range Appendix C/MA5/MA6's fictional
rates were chosen inside of.

## P03 — Real, documented precedent: custody fee billing errors (Appendix F)

Searched: `SEC enforcement custody bank overbilled clients fee billing error settlement State
Street OR BNY Mellon` (WebSearch). Surfaced the SEC's own June 2019 press release on State Street.
`WebFetch` 403'd on `sec.gov/newsroom/press-releases/2019-114`; fetched successfully via `curl`
with the same descriptive User-Agent.

Confirmed, in the raw press release text: "State Street Bank and Trust Company has agreed to pay
over $88 million to settle charges for overcharging mutual funds and other registered investment
company clients for expenses related to the firm's custody of client assets. The overcharges
included a secret markup ... to the cost of sending secured financial messages through [SWIFT] ...
from 1998 to 2015, State Street collected $170 million from the overcharges, with $110 million
coming from the hidden SWIFT markup ... [State Street] agreed ... to pay disgorgement and
prejudgment interest of $48.78 million ... and to pay a civil penalty of $40 million." Confirmed
release date via the page's own "For Immediate Release" / "Last Reviewed or Updated" lines:
June 27, 2019.

**Outcome: SOURCED, HIGH.** S3. Real, real-world stakes anchor for what a custody bank's client
billing errors can cost once caught, years later — used in Background, Appendix F, and the
Facilitator Twist. Clearly kept attributed to State Street/SEC, not to Meridian (fictional).

## P04 — Today's client's total AUC (Appendix A)

Framed by the placeholder text itself as "stated in-scenario," i.e. an authorial narrative choice
sized to make a fee-quote error a materially large dollar amount — not independently sourceable
since Meridian and its client are both fictional.

**Outcome: ASSUMPTION.** MA1 = $850,000,000. Confirmed via `sensitivity_model.py`/the margin
computation that this choice does not affect `margin_pct` at all (the true recursive fee is
provably scale-invariant as a percentage of AUC — see P08 below).

## P05 — Time Cassidy gave Marcus (Appendix A)

Framed as "stated in-scenario," matching the Overview's live-call urgency. Not independently
sourceable (fictional scenario).

**Outcome: ASSUMPTION.** MA2 = under one hour. Flavor/urgency only, not load-bearing on
`margin_pct`.

## P06 — Estimated analyst time for a fully-documented Full Ladder computation (Appendix A)

Framed as "stated in-scenario" — this is what makes the dilemma real (Marcus genuinely cannot do
both within the deadline), but the specific hour count is not independently sourceable for a
fictional bank's fictional internal workpaper standard.

**Outcome: ASSUMPTION.** MA3 = approximately 3 hours. Structurally load-bearing (it is *why* the
dilemma exists), not numerically load-bearing on `margin_pct`.

## P07 — Number of tiers in Meridian's fee ladder (Appendix A)

Framed as "stated in-scenario" — a structural/narrative choice (enough tiers to be a genuine
"ladder," few enough to compute by hand in one case-study session).

**Outcome: ASSUMPTION.** MA4 = 4. Does not independently affect `margin_pct` (a consequence of
MA6's specific rate choices, not tier count alone).

## P08 — Quick-Quote Reference Card's flat rate (Appendix B)

Framed as "stated in-scenario" — Meridian is fictional, so no real published rate card exists to
source. Chosen deliberately, not arbitrarily: first computed the Full Ladder's true blended
effective rate exactly (see P09 — a fixed 4.499306 bp, independent of client AUC, an algebraic
consequence of the recursive definition's homogeneity), then chose a flat card rate close enough to
that true figure to keep `margin_pct` comfortably under SPEC §2's ~20% cap while still being large
enough in dollar terms, at institutional AUC scale, to be a genuine, defensible dilemma rather than
a rounding error.

**Outcome: ASSUMPTION.** MA5 = 3.90 basis points. Flagged HIGH sensitivity — this is one of the two
Modeling Assumptions (with MA6) that directly sets `margin_pct`; see `sensitivity_model.py`.

## P09 — The Full Ladder's four tier rates (Appendix C)

Framed as "stated in-scenario," but not arbitrary: chosen to (a) sit inside the real disclosed
0.3875-7.0 bp range established by S1/S2, (b) decline tier-over-tier the way both real cited
schedules do, and (c) set Tier 4 (the last/largest-balance tier) to 0.50 bp specifically to echo
S1's real Gabelli/State Street first-tier rate exactly, as a deliberate real-world anchor point.

Computed the resulting true blended effective rate by hand and confirmed by script (see the
`python3` verification block below): running the recursion B₀=P, Feeₖ=rₖ·Bₖ₋₁, Bₖ=Bₖ₋₁−Feeₖ for
k=1..4 with r=(0.0002, 0.000125, 0.000075, 0.00005) gives a total fee that is *exactly*
P×[1−(1−r₁)(1−r₂)(1−r₃)(1−r₄)] = P×0.04499306 → **4.499306 basis points**, for any P (a provable
algebraic consequence: Bₙ = B₀·∏(1−rₖ) is homogeneous of degree 1 in B₀, so the ratio Bₙ/B₀ — and
therefore the effective rate 1−Bₙ/B₀ — cannot depend on B₀ at all). Verified this numerically by
running the full tier-by-tier recursion at three different AUC values ($300M / $850M / $1.2B) and
confirming the resulting effective rate is 4.499306 bp in all three cases, matching D4's intended
finding.

**Outcome: ASSUMPTION.** MA6 = 2.00 / 1.25 / 0.75 / 0.50 bp (Tiers 1-4). Flagged HIGH sensitivity —
together with MA5, this sets `margin_pct` directly.

## P10 — AUC sizes for two additional comparison clients (Appendix D)

Framed as "stated in-scenario" — chosen deliberately to span materially smaller ($300M) and larger
($1.2B) institutional clients than today's client (P04's $850M), specifically to give students
real numbers to test D4's scale-invariance claim against, rather than just take the claim on faith.

**Outcome: ASSUMPTION.** MA7 = $300,000,000 and $1,200,000,000.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none (S1, S2, S3 all HIGH)
needs_source OPEN remaining: 0
```

## Margin (computed here, matches case.json's balance.margin_note)

Computed via a short Python verification script (not checked into the repo as a standalone file —
see `sensitivity_model.py` for the persistent, re-runnable version) at AUC = $850,000,000:

```
Tier 1 (2.00 bp on $850,000,000.00):        fee = $170,000.00   balance after = $849,830,000.00
Tier 2 (1.25 bp on $849,830,000.00):        fee = $106,228.75   balance after = $849,723,771.25
Tier 3 (0.75 bp on $849,723,771.25):        fee =  $63,729.28   balance after = $849,660,041.97
Tier 4 (0.50 bp on $849,660,041.97):        fee =  $42,483.00   balance after = $849,617,558.97
Full Ladder true total fee = $850,000,000.00 - $849,617,558.97 = $382,441.03

Quick-Quote fee = $850,000,000.00 x 0.000390 = $331,500.00

Gap = $331,500.00 - $382,441.03 = -$50,941.03  (Option A undercharges)
margin_pct = 50,941.03 / 382,441.03 x 100 = 13.32%
```

**This is comfortably under SPEC §2's ~20% cap.** No retune pass or waiver was needed. Both options
remain genuinely defensible per `FACILITATOR.md`'s `balance.argument_a` / `argument_b`: Option B
wins decisively on accuracy and long-run defensibility (Appendix F's precedent); Option A wins
decisively on meeting Appendix A's one-hour deadline and on today's competitive-quote pressure.

Re-ran the identical computation at AUC = $300,000,000 and AUC = $1,200,000,000 (Appendix D's other
two clients) to build D4: true fees $134,979.19 and $539,916.75 respectively; Quick-Quote fees
$117,000.00 and $468,000.00 respectively; `margin_pct` comes out to 13.32% at all three sizes (to 2
decimal places), confirming the case's scale-invariance finding is not an artifact of the specific
$850M figure chosen for today's client.

## SPEC §2 self-check

- **Primary metric exists:** yes — "Fee-quote error, as a percentage of the true
  recursively-computed annual fee" (verbatim from the concept sheet), computed above.
- **No structurally-zero-cost option:** confirmed — Option A costs real analyst-avoided time but a
  real, computable, recurring dollar accuracy cost (13.32% of the true fee, every year); Option B
  costs real analyst time (Appendix A, MA3) that genuinely exceeds today's deadline (MA2). Neither
  option is free.
- **Dilemma is not a foregone conclusion:** confirmed — `margin_pct` = 13.32%, well under the ~20%
  guideline, and the two options trade off on genuinely different axes (accuracy/defensibility vs.
  speed/deadline-compliance), not just "which number is bigger."
- **Verdict: PASS.** No concerns to flag for the next case-readiness stage on balance grounds.

## Sensitivity model

Built `sensitivity_model.py` (PARAMS/evaluate() contract, matching `the-mainline-margin`'s
pattern). `FLEX[]` sweeps `client_auc` (MA1), `quick_quote_rate_bp` (MA5), and the four tier rates
`tier1_bp`..`tier4_bp` (MA6) — the only Modeling Assumptions that feed the graded primary metric's
arithmetic. Confirms programmatically that `client_auc` never moves `margin_pct` (scale-invariance,
P08/P09 above) while `quick_quote_rate_bp` and the tier rates do, roughly linearly near the case's
chosen values.

## Next step

Run `case-qa` on `the-fee-ladder`.
