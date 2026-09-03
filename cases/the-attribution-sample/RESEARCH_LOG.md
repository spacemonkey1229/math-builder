# RESEARCH_LOG.md — The Attribution Sample

`case-write` + `case-research` combined pass, 2026-09-01. 14 `{{NEEDS_SOURCE}}` placeholders
enumerated against `case.json.needs_source[]` (matching case.md's Appendix A-G figures).
5 SOURCED, 9 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Global average mobile app install fraud rate (Appendix G / Appendix F S1)

Searched: "AppsFlyer State of App Marketing fraud rate report install fraud percentage." Found
`appsflyer.com/company/newsroom/pr/global-exposure-install-ad-fraud/` among the results. Fetched
it directly. Confirmed exact quote: "The overall app install fraud rate...averaged at 13.2% in H1
2020." This is AppsFlyer's own newsroom page, a primary source, with a clear "H1 2020" date.

Used as historical global-scale context (Appendix G) — the concept brief specifically asked for
"the overall scale (e.g. overall install fraud rate range)" as an anchor, separate from the
per-channel figures used in Appendix D.

**Outcome: SOURCED, HIGH.** S1.

## P02 — Install-fraud-rate ranges by ad-channel type (Appendix D rows for SAN/DSP/Affiliate,
Appendix G row 2)

Searched: "AppsFlyer install fraud rate by ad channel type paid social vs paid search vs ad
networks gaming." Found `rocketshiphq.com/appsflyer-mobile-fraud-report-2025-summary/`. Fetched it
directly. Confirmed exact ranges quoted: Self-Attributing Networks (Meta, Google, TikTok, Apple
Search Ads) 1-8% (Android 2-8%, iOS 1-4% by network); Tier-1 DSPs 12-20% Android / 5-10% iOS;
Influencer/CPI Networks 15-30% Android / 5-12% iOS; also gaming-vertical-specific figures (casual
gaming 18-22% Android, midcore/hardcore 14-18% Android). Page states a publication date of
2026-03-22.

This is a secondary source (a marketing blog summarizing AppsFlyer's report), not the primary
report itself — the primary report's landing page (`appsflyer.com/resources/reports/
state-fraud-marketers/`) was also fetched directly but did not expose these specific channel-level
ranges on the page text (landing/summary page only; the full downloadable report was not
accessible). Used RocketShip HQ's page since it quotes specific, dated, channel-type figures
directly attributable to AppsFlyer's data, with the caveat that it is a third-party summary.

**Outcome: SOURCED, MEDIUM (secondary/blog source, not the primary report itself).** S2. Anchors
MA9 (SAN, 5%, middle of the real 1-8% range), MA10 (DSP, 15%, middle of the real 12-20% range),
and MA11 (Affiliate, 15%, low end of the real 15-30% range).

## P03 — Owned-media install-fraud-rate figure (Appendix D row "Owned & Boosted Media," Appendix F
S3)

Searched: "AppsFlyer install fraud rate by ad channel type" (same search as P02) and separately
fetched `appsflyer.com/company/newsroom/pr/organic-traffic-ad-fraud/` directly (AppsFlyer's own
newsroom page, not a third-party summary). Confirmed exact quote: "Owned media fraud rose 221%
year over year, from 3.4% to 11%." Cross-confirmed the identical figure on a second, independent
fetch of `ppc.land/organic-traffic-is-now-mobile-advertisings-biggest-fraud-blind-spot/`, which
quotes the same AppsFlyer 2026 report.

This is a real, precise, directly-reported figure that matched the case's channel-design needs
closely enough to use directly rather than as a range-anchored assumption — Appendix D's "Owned &
Boosted Media" channel is set to exactly 11% fraud / 89% true-install rate, sourced, not assumed.

**Outcome: SOURCED, HIGH.** S3. This is the only one of the four per-channel fraud-rate figures in
Appendix D that is a direct citation rather than a Modeling Assumption anchored to a range.

## P04 — Share of all install fraud from affiliate channels (Background context, Appendix G row 4)

Same fetch as P03 (`appsflyer.com/company/newsroom/pr/organic-traffic-ad-fraud/`). Confirmed exact
quote: "affiliates carrying nearly 40% of all fraud." Cross-confirmed on the `ppc.land` fetch:
"Affiliates account for nearly 40 per cent of fraudulent installs."

Used as qualitative Background/Appendix G context supporting why the case's small Influencer/
Affiliate channel deserves particular scrutiny — not itself a per-click fraud-rate figure and not
load-bearing for any deliverable's arithmetic.

**Outcome: SOURCED, HIGH.** S4.

## P05 — iOS install-fraud-rate trend (Appendix F S5)

Same fetch as P03/P04. Confirmed exact quote: "iOS fraud dropped 33 per cent year over year,
falling from 17.5 per cent in Q1 2025 to 11.7 per cent in Q1 2026" (ppc.land, quoting the AppsFlyer
report; corroborated on AppsFlyer's own newsroom page: "iOS fraud dropped 33% year over year, from
17.5% in Q1 2025 to 11.7% in Q1 2026, crossing below Android for the first time").

Included in the Sources appendix as real, dated, industry-trend context. Not load-bearing for any
deliverable's arithmetic — included for realism/color, matching the pattern of contextual sources
in other researched cases in this corpus.

**Outcome: SOURCED, HIGH.** S5.

## P06 — Report deadline framing (Appendix A)

Framed by the placeholder text itself as "stated in-scenario" — an authorial narrative choice
(Friday afternoon → Monday morning), not a real-world fact to source. No search performed.

**Outcome: ASSUMPTION.** MA1. Decorative, matches the Overview's framing, not load-bearing.

## P07 — Weekend analyst-hours budget (Appendix A)

No public per-analyst "weekend verification-hours budget" standard exists to source — this is an
internal operational constraint specific to a fictional company (Verafly) and role. Chosen
deliberately, not searched: set to 13 hours so that Option B's actual computed total (12.95 hr,
Appendix E/F) fits with only a few minutes of slack, while Option A's total (10.1 hr) leaves nearly
3 hours of slack — a genuine, disclosed narrative design choice, not a hidden thumb on the scale
(both options DO fit within the stated budget; neither is eliminated outright).

**Outcome: ASSUMPTION.** MA2.

## P08 — Total weekly pooled click volume (Appendix A)

Searched informally alongside P01/P02 for "mobile game weekly ad click volume" scale context; no
single citable figure fits Verafly's specific (fictional) situation exactly, and the exact total
population size is not load-bearing for any deliverable (both options' sample sizes are fixed at
400 regardless of total population, since the case treats each channel's population as effectively
unlimited relative to its own sample — no finite-population correction is used, appropriate at this
scale and tier). Chose an illustrative, plausible figure.

**Outcome: ASSUMPTION.** MA3. Flavor/scale only.

## P09 — Channel count, names, and click-volume shares (Appendix A)

Framed as "stated in-scenario" — a scenario design choice. The four channel *types* (Self-
Attributing Networks, Programmatic/DSP, Owned & Boosted Media, Influencer/Affiliate) are all real,
named categories drawn directly from S1-S5's own vocabulary, so the channel *taxonomy* is grounded
in real industry terminology even though the specific *share split* (62/26/10/2%) is an authorial
choice, deliberately built so the Influencer/Affiliate channel is small (2%) but not zero — this is
the case's real fulcrum (see `sensitivity_model.py`'s FLEX list, `share_affiliate`).

**Outcome: ASSUMPTION.** MA4. Flagged HIGH sensitivity in case.json's modeling_assumptions[].

## P10/P11 — Option A total sample size and setup time (Appendix B)

Framed as "stated in-scenario" — an operational choice by Derek's team (a standard weekly SRS batch
size), not something with a real external benchmark to search for.

**Outcome: ASSUMPTION (both).** MA5 (400 clicks), MA6 (0.5 hr setup).

## P12/P13 — Option B minimum sample floor and setup time (Appendix C)

Same as P10/P11 — an internal design choice for the stratified sampling plan, not independently
sourceable. The floor (40 clicks) was chosen deliberately so the Affiliate channel's resulting
standard error (5.65pp, Appendix E) is materially better than Option A's (12.62pp) without being an
unrealistically enormous oversample.

**Outcome: ASSUMPTION (both).** MA7 (40-click floor), MA8 (1.4 hr setup).

## P14 — Per-click verification time by channel (Appendix E)

Framed as "stated in-scenario" — narratively justified (API-integrated channels verify faster than
manually-reconciled ones) rather than independently sourceable; no public benchmark exists for
"minutes to manually verify one ad-attribution click" at this granularity.

**Outcome: ASSUMPTION.** MA12. Flagged as the single biggest driver of Option B's extra
verification time in case.json's modeling_assumptions[].

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none — S2 is MEDIUM (secondary/blog summary),
    all others are HIGH (primary AppsFlyer newsroom pages)
needs_source OPEN remaining: 0
```

S2 (MEDIUM) is the only non-HIGH source, and it anchors three Modeling Assumptions (MA9, MA10,
MA11) that are themselves explicitly labeled as assumptions, not direct citations — the case never
claims S2's ranges as exact per-channel figures, only as the real published range each assumption
was chosen inside of. This satisfies the rule that a lower-confidence source may inform but not
masquerade as a precise, load-bearing citation.

## Margin (case-research)

Primary metric: pooled (whole-report) standard error, percentage points, divided by total
analyst-hours. Computed twice, independently, with consistent results:

**By hand (case.md/case.json, using whole-click-integer sample sizes as a student would actually
draw them):** Pooled SE_A = 1.369pp (n: SAN 248, DSP 104, Owned 40, Affiliate 8). Pooled SE_B =
1.407pp (n: SAN 227, DSP 96, Owned 37, Affiliate 40). Hours_A = 9.6 (verification) + 0.5 (setup) =
10.1 hr. Hours_B = 11.55 + 1.4 = 12.95 hr. Ratio_A = 1.369/10.1 = 0.1355 pp/hr. Ratio_B =
1.407/12.95 = 0.1086 pp/hr. **margin_pct = (0.1355-0.1086)/0.1355 × 100 = 19.83%.**

**By `sensitivity_model.py` (same inputs, exact fractional proportional allocation instead of
rounding each channel to a whole click count):** margin_pct = 19.68%. The two figures differ by
~0.15 percentage points purely from integer rounding of sample counts (case.md rounds Owned's
Option-B allocation from 36.73 to 37, etc.) — both are well under the ~20% cap and agree on the
winner. `case.json.balance.margin_pct` uses the hand-computed, whole-click figure (19.83%) since
that is what a student actually working the deliverables would compute from Appendix E's printed
integer sample sizes.

**Winner: Option B, The Channel-Stratified Sample** — lower attribution error per analyst-hour.
This is genuinely close (under SPEC §2's ~20% cap on the first computation), so **no retune pass
was needed** and no MCS-46-style waiver applies.

`sensitivity_model.py`'s FLEX sweep (±50% on each of `share_affiliate`, `n_total_a`,
`setup_hours_a`, `floor_affiliate_b`, `setup_hours_b`, `time_affiliate`, `p_affiliate`) does not
flip the winner in any single-dial test — Option B wins on the primary metric across the entire
sweep. This is disclosed plainly: the case's real tension is not "which option wins the ratio,"
which is fairly robust to any one assumption changing by half, but the *qualitative* stakes
underneath it — Option A leaves far more schedule slack against Appendix A's 13-hour weekend budget
(10.1 hr vs. 12.95 hr) and Option B is the only option that makes the small, board-deck-flagged
Affiliate channel's estimate usable at all (5.65pp SE vs. 12.62pp). A Hero who only checks D4's
ratio and stops has not engaged with either of those two real, disclosed considerations.

## SPEC §2 self-check

- Primary metric exists and is computable from stated appendix data: yes (pooled SE ÷ hours).
- No structurally-zero-cost option: confirmed — both options cost real analyst-hours (10.1 hr and
  12.95 hr respectively; neither is free), and both options fit inside the stated 13-hour budget
  (Option B with only ~0.06 hr / ~4 minutes of slack — a real, tight fit, not a guaranteed miss).
- Dilemma is not a foregone conclusion: confirmed — Option B wins the stated primary metric by a
  genuinely close 19.83% margin, while Option A wins decisively on total time cost/schedule slack
  and is the option most Heroes will likely gravitate to on gut instinct ("faster, and it's the same
  400 clicks either way") — exactly the kind of case where the "obvious" fast choice and the
  primary-metric winner diverge, which is the productive tension SPEC §0 wants.
- **Verdict: PASS.** Flagging one open judgment call for the next case-readiness session: this
  case's per-channel true-install-rate assumptions (Appendix D / MA9-MA11) are themselves values
  chosen *within* real published ranges (S2), not the ranges' endpoints — a QA reviewer may
  reasonably want to stress-test the margin at the *opposite* end of MA11's range (e.g., Affiliate
  fraud at 30% instead of 15%) to confirm the qualitative small-channel-risk argument still holds;
  `sensitivity_model.py`'s `p_affiliate` FLEX entry supports exactly that check and it does not
  flip D4's winner.

## Next step

Run `case-qa` on `the-attribution-sample`.
