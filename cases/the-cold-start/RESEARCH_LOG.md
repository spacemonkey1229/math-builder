# RESEARCH_LOG.md — The Cold Start

`case-research` pass, 2026-09-01. 11 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`'s
drafting pass. 6 SOURCED, 5 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 / P02 — Reference catalog scale and mature-platform account scale (Appendix A, B, C)

Northline is fictional, so no real "streaming catalog size" figure exists to source directly.
Searched: "MovieLens 25M dataset sparsity ratings matrix percentage filled." Fetched
`grouplens.org/datasets/movielens/25m/` directly. Confirmed exact stated figures: "25 million
ratings and one million tag applications applied to 62,000 movies by 162,000 users."

Used as a real, sourced proxy for "a media catalog and user base at this scale" — the same pattern
as `prove-it-scales`' use of AWS Organizations' real 5-level nesting depth as a proxy for a
fictional billing platform. Both the catalog scale (62,000) and the mature-platform account scale
(162,000) come from this one real, confirmed source.

**Outcome: SOURCED, HIGH (both).** S1.

## P05 — Sparsity of the reference ratings matrix (Appendix C)

Derived directly from S1's three real, confirmed figures: 25,000,000 ÷ (162,000 × 62,000) =
25,000,000 ÷ 10,044,000,000 = 0.0024891 = **0.2489% filled → 99.751% empty.** Also computed a new
account's own row sparsity after the Ratings Gate: 10 filled ÷ 62,000 possible columns = 0.0161%
filled — used in D1 to make the "sparse is not empty" distinction concrete.

**Outcome: SOURCED (derived from S1), HIGH.**

## P06 / P07 (anchor) — Required ratings count and measured historical dropout on that exact gate (Appendix C)

Searched: `"onboarding" "rating" step before recommendation abandonment study cold start` and then
specifically `Rashid "Getting to Know You" learning new user preferences recommender systems
number of ratings requested new user`. Found and fetched the actual PDF at
`cs.fit.edu/~pkc/apweb/related/rashid-iui02.pdf` (Rashid, Albert, Cosley, Lam, McNee, Konstan,
Riedl — "Getting to Know You: Learning New User Preferences in Recommender Systems," IUI '02).

This is a direct, exact real-world match to Option B's premise, not an approximate proxy: the
paper's Experimental Design section states plainly, "When a new user joins MovieLens, the system
presents pages of ten movies until the user rates ten or more movies" — the real MovieLens
platform's actual 2002 onboarding design used exactly the "rate ≥10 items before recommendations"
mechanic this case's Option B is built on.

The paper's live online experiment (Table 1, "Population of the experimental groups") reports real
measured dropout during that exact onboarding gate: 351 total new users during the ten-day
experimental period, 49 dropouts, 302 completed = **13.96% dropout, 86.04% completion.**
Per-strategy rows ranged from 10.99% (Popularity strategy, 91 total/10 dropouts) to 21.05%
(Classique strategy, 76 total/16 dropouts); the case uses the 351/49/302 aggregate row, since
Option A/B do not correspond to any single one of the paper's four item-selection strategies.

Confirmed via direct PDF extraction (not just a search snippet) — both the "ten movies... ten or
more" quote and Table 1's exact numbers were read directly off the rendered page images.

**Outcome: SOURCED, HIGH.** S2. Used directly for Appendix C's "required ratings = 10" row and the
"measured historical dropout" row, AND used as the real historical anchor/floor for MA3 (see
below) — not as the modeled 2026 value itself.

## P03 — Days from case launch to launch review (Appendix A)

Framed by the placeholder text itself as "stated in-scenario" — an authorial narrative choice
matching the Overview's "forty minutes before the standup" / Thursday-review, Friday-premiere
framing, not a real-world fact to source. No search performed.

**Outcome: ASSUMPTION.** MA1 = 3 days. Decorative, not load-bearing.

## P04 — Modeled click-through rate, Option A, among all accounts reaching the shelf (Appendix B)

Searched for any published click-through-rate figure specific to an unpersonalized "trending/new
releases" recommendation shelf for a same-week premiere. No platform publishes this — it is
commercially sensitive, proprietary analytics data, and Northline itself is fictional. No further
search attempted once it was clear this class of figure is not publicly disclosed by any real
platform (the closest real analog, Netflix's Gomez-Uribe & Hunt figure, measures aggregate
influence on viewing hours platform-wide, not a per-title unpersonalized-shelf CTR, and was used
instead only as Background stakes framing — see P10 below).

**Outcome: ASSUMPTION.** MA2 = 20%. Flagged HIGH sensitivity — the most narratively-invented
number in the case; see the Margin section below for how much it moves the result.

## P08 — Modeled click-through rate, Option B, among completers (Appendix C)

Same search effort and same conclusion as P04 — no platform publishes per-title recommendation
click-through data broken out by whether the user completed a ratings-based onboarding gate. This
is inherently unpublishable, proprietary business data for any real company, and doubly
unavailable for a fictional one.

**Outcome: ASSUMPTION.** MA4 = 35%. Flagged MEDIUM sensitivity.

## P07 (modeled value) — Modeled 2026 dropout for Northline's cohort (Appendix C)

This is the case's single most important modeling decision, and it required an explicit escalation
beyond a simple "not found → assumption" call. Two real, cited data points exist that bear on it:

1. S2's real, measured 13.96% dropout on the *exact same onboarding mechanic* (rate ≥10 items
   before recommendations) — but measured on a 2002, self-selected, already-engaged MovieLens
   research-community population, not a general 2026 sign-up cohort.
2. S4 (below): Baymard Institute's real, confirmed 17% cart-abandonment figure attributed
   specifically to "too long / complicated checkout process" — a real, general digital-friction
   number, but from an even *shorter, lower-friction, already-purchase-intent* flow (checkout, not
   a 10-item preference-elicitation task for an app the user hasn't even tried yet).

Searched further for a modern, specific, confirmed "X% dropout per additional required onboarding
step" figure to use directly instead of modeling a value: `"multi-step" signup funnel percent drop
off per step benchmark study published data`, `onboarding funnel drop-off rate per additional step
required before first value app signup research`. Several aggregator pages (amraandelma.com and a
WebSearch auto-summary) surfaced a specific, precise-looking claim — "reducing the sign-up form
from 7 fields to 3 fields cut overall funnel abandonment by 44.7%," attributed to "UXCam's 2026
SaaS Onboarding Benchmark Study." **This claim was explicitly checked and rejected**: `WebFetch`
was run directly against UXCam's own actual blog post (`uxcam.com/blog/drop-off-rates/`), and that
primary page contains **no such statistic and no such study** — the 44.7% figure and its
attribution do not appear on the page it is credited to. Per MCS-21's rule (fetch the actual page
and confirm the claim appears in it, not just a search snippet), this figure is treated as
unconfirmed and is **not used anywhere in this case**, despite appearing confidently worded across
multiple secondary sources.

Having ruled that out, no other confirmable modern figure specific to "abandonment per required
onboarding step" was found. This matches the concept sheet's own stated expectation exactly
("expect a stated Modeling Assumption anchored to general onboarding-friction research, not a
literal transferred number").

**Outcome: ASSUMPTION, explicitly anchored above two real floors.** MA3 = 40%, anchored above S2's
real 13.96% (dated/wrong-population) and S4's real 17% (shorter/lower-friction flow), on the
qualitative (real, transferable) basis that additional required pre-value steps increase
abandonment, without claiming a specific transferred magnitude. Flagged **HIGH** sensitivity — see
Margin section.

## P10 — Real streaming-recommender stakes figure (Background)

Searched: `Gomez-Uribe Hunt "Netflix Recommender System" ACM TMIS 80% of hours watched come from
recommendations`. The primary ACM page (`dl.acm.org/doi/10.1145/2843948`) returned HTTP 403 on
direct fetch, as did a ResearchGate mirror. Routed to a reputable secondary source that names and
footnotes the original paper: `newamerica.org/insights/why-am-i-seeing-this/case-study-netflix/`,
fetched directly. Confirmed exact quote: "driving approximately 80 percent of hours of content
streamed on the platform," cited in the page's own footnote 238 to Gomez-Uribe, C.A. and Hunt, N.,
"The Netflix Recommender System: Algorithms, Business Value, and Innovation," ACM TMIS 6(4), 2015.

**Outcome: SOURCED, MEDIUM-HIGH (primary paper's exact wording not independently confirmed since
the ACM page 403'd; the claim and its citation were confirmed on a reputable, directly-fetched
secondary page).** S3. Used only for Background stakes framing — does not feed Appendix D's metric
arithmetic.

## P11 (anchor) — Real general checkout/signup-friction abandonment figure (MA3 basis)

Searched: `Baymard Institute checkout form fields conversion rate reduce number of fields`. Fetched
`baymard.com/lists/cart-abandonment-rate` directly. Confirmed exact quote: "17% of US online
shoppers have abandoned an order due to a 'too long / complicated checkout process.'" Also checked
`baymard.com/blog/checkout-flow-average-form-fields` directly: confirmed "the average checkout
flow in 2024 is 5.1 steps long and contains 11.3 form fields" — used as supporting context in
MA3's basis, not as a separate cited figure, since it does not itself state an abandonment rate.

**Outcome: SOURCED, HIGH.** S4. Used only as a real lower-bound anchor for MA3 (see above) — not
as a literal transferred dropout rate for the Ratings Gate.

## P09 — Appendix E worked-example matrices (P, U, target blend)

Framed as illustrative scenario numbers for a hand-worked pedagogical example (matrix addition,
identity-matrix framing, determinant, system of equations) — not claimed as real platform data
anywhere in case.md, and does not feed Appendix D's primary-metric arithmetic.

**Outcome: ASSUMPTION.** MA5. No sensitivity — pedagogical only.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources: none (S1-S4 all HIGH or MEDIUM-HIGH)
needs_source OPEN remaining: 0
```

## Margin (facilitator-only — computed here, not written into case.md)

**Pass 1 — literal historical dropout (S2's real 13.96%, completion 86.04%).**
Option A = 100 × 0.20 (MA2) = 20.0 clicks/100 starters.
Option B = 86.04 × 0.35 (MA4) = 30.11 clicks/100 starters.
margin_pct = (30.11 − 20.0) / 30.11 × 100 = **33.6%** — over SPEC §2's ~20% cap.

**Retune pass (per SPEC §2's own instruction — adjust a constraint, do not hide data).** S2's real
13.96% figure is measured on a dated (2002), self-selected, already-engaged research-community
population, not a general 2026 friend-referral streaming cohort. This is a legitimate,
disclosed basis for retuning the *modeled* dropout constraint (MA3), anchored above two real,
cited floors (S2's own 13.96%, and S4's real 17% checkout-complexity figure from an even shorter,
lower-friction flow) rather than inventing an unanchored number. Retuned MA3 = 40%.

**Pass 2 — retuned (MA3 = 40% modeled dropout, completion 60.0).**
Option A = 100 × 0.20 (MA2) = 20.0 clicks/100 starters.
Option B = 60.0 × 0.35 (MA4) = 21.0 clicks/100 starters.
**margin_pct = (21.0 − 20.0) / 21.0 × 100 = 4.76%. Winner: Option B, The Ratings Gate,** by a
genuinely close margin.

**Additional sensitivity checked:** at MA2 (Option A's CTR) = 12% instead of 20% (a stricter "more
buried" reading of Appendix B), Option A = 12.0, margin widens to (21.0−12.0)/21.0 = 42.9% — MA2
is also a real driver of how close this case reads, not just MA3. Both are disclosed as HIGH
sensitivity in `case.json.modeling_assumptions[]`.

This is **not** softened or hidden: both passes are reported plainly, in `case.json`'s
`balance.margin_note`, in `FACILITATOR.md`'s Balance section (which doubles as the case's Twist —
the Twist itself is "the more real your data gets, the less close this case is"), and here. No
MCS-46-style waiver was needed or requested, since the retuned figure lands within the ~20% cap.

## SPEC §2 self-check

- Primary metric exists: yes (recommendations clicked per 100 starters, Appendix D). PASS
- No structurally-zero-cost option: PASS — Option A costs nothing in onboarding friction but pays
  a real opportunity cost (buried premiere, MA2's modest 20% CTR); Option B costs real dropout
  (MA3) for a real personalization gain (MA4). Neither option is free on the metric.
- Dilemma is not a foregone conclusion: PASS at the case's own modeled values (margin 4.76%,
  genuinely close) — but flagged for the next readiness stage that the case's own appendices
  disclose a real, cited counterfactual (S2's literal figure) under which the margin is NOT close
  (33.6%). This is disclosed by design, not a defect, but case-qa should confirm the disclosure
  itself (not the closeness) is what's being certified here.
- Verdict: **PASS**, with the above disclosure flagged for case-qa's attention.

## Next step

Run `case-qa` on `the-cold-start`.
