# RESEARCH_LOG.md — The Bot Farm

`case-research` pass, 2026-09-01. 13 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
4 SOURCED, 9 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Hours from incident flag to the traffic surge (Appendix A)

Framed by the concept write-up itself as "six hours from now" narrative detail. No search
performed — this is an authorial scenario choice matching the Overview's countdown-clock framing.

**Outcome: ASSUMPTION.** MA1 = 6 hours. Decorative, not load-bearing.

## P02 — Maximum clusters safely suspendable per incident (Appendix A)

Framed by the concept write-up as a stated scenario constraint ("she only gets to act on one: the
platform's abuse tooling can suspend a cluster this size safely once per incident without a
slower, human-reviewed rollout"). No search performed — this is the authorial constraint that
forces the binary dilemma to exist at all.

**Outcome: ASSUMPTION.** MA2 = 1. Structural, not decorative — without it Aisha could suspend both
clusters and the case would have no dilemma.

## P03 / P04 — Ring Alpha / Wave Nine flagged-account counts, this incident (Appendix A, E)

In-scenario cluster sizes for a fictional platform (Verve) — not independently sourceable. Chose
250 (Ring Alpha) and 200 (Wave Nine), deliberately different sizes since two different detection
signals need not flag equally-sized clusters.

**Outcome: ASSUMPTION (both).** MA4 = 250, MA5 = 200. Verified algebraically (see Margin section
below) that neither value affects `margin_pct` at all — the primary metric's ratio,
confirmed-bots/false-positives, reduces to (1-p)/p where p is the modeled false-positive rate,
and cluster size cancels out completely. This is disclosed explicitly in both figures'
`sensitivity` field in `case.json`.

## P05 / P06 — Illustrative adjacency-sample connection lists, Cluster A / Cluster B (Appendix B, C)

Per the task's explicit instruction: built two small (10-account) illustrative adjacency-matrix
samples myself, labeled clearly as the case author's own construction and NOT real Verve platform
data (Verve is fictional; no real per-cluster connection data could exist for it). Cluster A ("Ring
Alpha") was built with 24 of 45 possible undirected edges (53.3% density) concentrated among 7 of
10 accounts, leaving 3 accounts on a sparser tail — deliberately not a complete clique, so the
sample isn't a caricature. Cluster B ("Wave Nine") was built with 7 of 45 possible edges (15.6%
density), scattered rather than clustered, consistent with "accounts that mostly target real users
rather than each other." All matrix entries, degree sums, edge counts, and density percentages
were computed with a Python script (not by hand) to guarantee arithmetic correctness; script and
raw output retained in the scratchpad for this session.

**Outcome: ASSUMPTION (both), correctly computed.** Not sourced externally — flagged as the
author's own worked construction per the task's explicit instruction, matching how `case.json`'s
`needs_source[]` entries for P05/P06 are recorded.

## P07 — Wave Nine's average sustained posting rate, this incident (Appendix C)

In-scenario figure for a fictional platform. Chose 340 posts/hour/account, deliberately set close
to but under the real, sourced technical ceiling found for P13 below (≈400 posts/hour, S2), so the
"extreme volume" framing is grounded against a real number rather than invented in isolation.

**Outcome: ASSUMPTION.** MA9 = 340 posts/hour/account. Does not enter the primary-metric
computation (Appendix E) — flavor/context only.

## P08 / P09 — Real published bot-detection benchmarks: combined-system accuracy and per-feature-class AUC ranges (Appendix D)

Searched: "Twitter bot detection precision recall connectivity features vs content volume
features research paper." Multiple candidates surfaced (BotSpot, BotArtist, various 2023-2025
papers); selected Varol, Ferrara, Davis, Menczer, Flammini, "Online Human-Bot Interactions:
Detection, Estimation, and Characterization" (arXiv:1703.03107) as the primary anchor — it is the
paper behind the widely-used Botometer/BotOrNot system, directly compares feature-class
performance (the exact connectivity-vs-volume tension this case needs), and is highly citable.

`WebFetch` on the arXiv abstract page and on the raw PDF (`arxiv.org/pdf/1703.03107`) both
returned readable content; the PDF was also downloaded and read directly with the `Read` tool
(page images) to visually confirm the exact wording, since one earlier `WebFetch` pass on a
different PDF in this same session had returned "corrupted/improperly encoded" text — decided to
verify this one at the image/OCR level rather than trust a single text-extraction pass.

Confirmed directly, in the paper's own text:
- "The best classification performance of 0.95 AUC was obtained by the Random Forest algorithm"
  (honeypot dataset, 5-fold cross-validation).
- "we measured false positive and false negative rates at 0.15 and 0.11 respectively in our
  extended dataset" (manually-annotated dataset, optimal threshold, human annotation as ground
  truth).
- Table 1: 1,150 features across 6 classes (User meta-data, Friends, Network, Content, Sentiment,
  Timing).
- "We achieved the best performance with user meta-data features; content features are also
  effective. Both yielded AUC above 0.9. Other feature classes yielded AUC above 0.8."

This last line is the case's real analytical fulcrum: it directly shows, in a real published
study, that connectivity/network-flavored signal is real and useful but the comparatively *weaker*
standalone predictor next to volume/content signal — the opposite of the naive "dense block = most
suspicious" intuition the case's Launch is built to surface.

**Outcome: SOURCED, HIGH.** S1.

## P10 — Real published social-network dataset density/clustering baseline (Appendix D)

Searched Stanford SNAP's dataset index (`snap.stanford.edu/data/index.html`) directly via
`WebFetch`, looking for a real, publicly documented social-graph dataset usable as a baseline for
"how dense do ordinary real friend circles actually look." Selected `ego-Facebook` (a well-known,
widely-cited SNAP dataset) and fetched its dedicated stats page
(`snap.stanford.edu/data/ego-Facebook.html`) directly to confirm exact figures rather than relying
on the index page's summary alone.

Confirmed directly: "Nodes: 4039", "Edges: 88234", "Average clustering coefficient: 0.6055".

Computed (by this case's author, from these two real published counts) the whole-graph density:
2×88234 / (4039×4038) = 1.08%. Decided NOT to use this whole-graph figure as the case's headline
comparison point, since it blends together many separate, mostly-disconnected friend circles and
would understate how dense one person's own local circle actually looks — used the real, directly
published 0.6055 local clustering-coefficient figure instead, which is the figure that actually
maps onto Ring Alpha's illustrative sample scale (a single tight sub-cluster, not a whole
multi-circle graph). Both figures are shown in Appendix D with this reasoning made explicit in the
appendix's own footnote, so a Hero checking the math isn't misled by the smaller whole-graph number.

**Outcome: SOURCED, HIGH.** S3.

## P11 / P12 — Modeled false-positive rates, Ring Alpha and Wave Nine (Appendix E)

Not independently sourceable — Verve is fictional and has no real detection-accuracy data of its
own. Per the task's explicit instruction, derived both as disclosed Modeling Assumptions anchored
to S1's real published figures, rather than invented from nothing:

- **MA6 (Ring Alpha, 20%).** S1's real combined-system false-positive rate is 0.15. S1 also shows
  connectivity/network features alone reach a real, lower standalone AUC (>0.80) than the combined
  system (0.95 AUC) or the content-features-alone group (>0.90). Modeled a ~30% degradation from
  the 0.15 baseline (0.15 × 1.3 = 0.195), rounded to a clean 20% operating rate.
- **MA7 (Wave Nine, 22.5%, surge-adjusted).** Ordinarily, S1 would predict volume/content-based
  detection should have a *lower* false-positive rate than connectivity-based detection (since its
  standalone AUC is real and higher, >0.90 vs. >0.80) — this is exactly what the counterfactual
  check below confirms. But the case's premise (from the concept write-up) is that this incident
  happens six hours before Verve's highest-traffic weekend, when real users' own posting volume
  spikes too — a real, general, industry-documented limitation of volume-based anomaly rules
  during high-traffic windows (searched for a specific, named real-platform incident to cite
  directly, but decided against using any of what was found — see the sensitivity note below).
  Modeled a 50% degradation from the same 0.15 baseline (0.15 × 1.5 = 0.225 = 22.5%).

**Sensitivity note on named-platform search results (SPEC §6 compliance).** A search for a
concrete real precedent of a platform walking back a volume-based suspension rule surfaced several
real, named incidents (X's 2026 "inauthentic behavior" suspension wave; Meta/Instagram's automated
moderation errors). Per this case's sensitivity flag (`CONCEPTS_formal-logic-vectors-matrices-
numbertheory_2026-08-23.md`, C8: "never about a named real platform, named real users, or real
account content — same register as Heist or Key Length"), deliberately chose NOT to cite any of
these specific named-platform incidents directly in `case.md`. MA7's basis is stated generically
("a real, general, industry-documented limitation of volume-based anomaly rules during high-traffic
windows") rather than pointing at one real, named platform's specific event — consistent with how
this case already uses X's *technical* API documentation (S2, a rate-limit fact, not an incident)
and SNAP's *dataset* statistics (S3, not an incident) as real proxies, while avoiding real
incident/harm narratives entirely.

**Outcome: ASSUMPTION (both).** MA6 = 20%, MA7 = 22.5%. MA7 flagged HIGH sensitivity — see Margin
section below.

## P13 — Real published social-platform API posting rate limit (Appendix F)

Searched: "Twitter X API tweet rate limit ... historical developer documentation." Attempted
`developer.twitter.com/en/docs/twitter-api/rate-limits` directly; it redirected (307) to
`docs.x.com`. Followed the redirect to the specific fundamentals page
(`docs.x.com/x-api/fundamentals/rate-limits`) and fetched it directly.

Confirmed directly: `POST /2/tweets` — "Per-App: 10,000/24hrs", "Per-User: 100/15min". This is a
real, current, primary-source technical ceiling (≈400 posts/hour sustained per user via the
standard API allowance), used only as a real-world proxy for "what level of automated posting
volume is even technically possible for one account" — not as a claim about Verve, which is
fictional and publishes no such figure of its own.

**Outcome: SOURCED, HIGH.** S2.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources: none
needs_source OPEN remaining: 0
```

## Margin (facilitator-only — computed here, not written into case.md)

Primary metric = confirmed-bot accounts removed ÷ real accounts wrongly suspended, per cluster,
using Appendix E's modeled false-positive rates (MA6, MA7). This ratio simplifies algebraically to
(1-p)/p, where p is the cluster's modeled false-positive rate — cluster size (MA4, MA5) cancels
out of the ratio entirely, verified explicitly:

```
Ring Alpha:  flagged=250, p=0.20  -> FP=50,  confirmed=200  -> ratio = 200/50  = 4.00
Wave Nine:   flagged=200, p=0.225 -> FP=45,  confirmed=155  -> ratio = 155/45  = 3.4444...
margin_pct = (4.00 - 3.4444) / 4.00 x 100 = 13.89% -> rounded 13.9%
Winner: Option A, Ring Alpha.
```

This is comfortably under SPEC §2's ~20% cap on the first construction — **no retune pass was
needed.**

**Counterfactual check (does MA7's surge premium actually drive the result?).** Reverting Wave
Nine's rate to the real, unscaled S1 baseline (p=0.15, i.e. no surge premium at all):

```
Wave Nine (no surge premium): flagged=200, p=0.15 -> FP=30, confirmed=170 -> ratio = 170/30 = 5.6667
margin (B beats A) = (5.6667 - 4.00) / 5.6667 x 100 = 29.4%
```

This flips the recommendation to Option B by a real, non-trivial margin. So the case's genuine
fulcrum is MA7 — whether a real traffic surge measurably degrades volume-based detection's real,
published ordinary-conditions advantage — not cluster size (proven irrelevant above), and not
Ring Alpha's own rate in isolation. This is the case's Twist material (`FACILITATOR.md`).

## SPEC §2 self-check

- Primary metric exists and is computable for both options: YES (confirmed-bots-per-false-positive,
  Appendix E).
- No structurally-zero-cost option: YES — both options carry a real, nonzero false-positive cost
  (neither cluster's modeled rate is 0%).
- Dilemma is not a foregone conclusion: YES — margin (13.9%) is well inside SPEC §2's ~20%
  guideline, and the counterfactual check shows the recommendation is genuinely sensitive to one
  disclosed modeling choice (MA7), not an artifact of an extreme, undefendable assumption.
- **Verdict: PASS.** No balance concern to flag for case-readiness. No MCS-46-style waiver needed
  or sought.

## Next step

Run `case-qa` on `the-bot-farm`.
