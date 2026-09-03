# Case Study: The Bot Farm

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Aisha Bello has two browser tabs open, and only one of them is about to matter.

The left tab shows a graph she has stared at for twenty minutes: a tight, near-solid block of
accounts, thick with connecting lines, all following and messaging each other in a pattern she has
flagged a dozen times before — a bot ring, or something that looks exactly like one. The right tab
shows a sparser graph, but underneath it a scrolling feed of raw posting timestamps that make her
stomach drop every time she refreshes: accounts posting faster than anyone sitting at a keyboard
plausibly could.

The countdown clock pinned to the top of Aisha's second monitor reads six hours. In six hours,
Verve's biggest live event of the year goes up, and with it the single largest traffic spike Trust
& Safety sees all year — real fans discovering the platform for the first time, riding the same
trending tag as whatever is trying to ride it with them.

Aisha's team lead already gave her the rule tonight: one cluster, one suspension, before the surge
hits. The abuse tooling can pull a cluster this size safely exactly once — anything past that needs
a slower, human-reviewed rollout Verve does not have six hours for.

She has narrowed it to two clusters. She cannot suspend both.

Her cursor sits over the button for the first one, hovering.

---

## Background

Aisha Bello is a Fraud Analyst on the Trust & Safety team at Verve, a mid-size social platform.
Six hours from now, Verve's annual live showcase — the single highest-traffic weekend of its
year — begins, and Trust & Safety's abuse-detection tooling has flagged two account clusters
riding the early buzz around the event's trending tag (SEE APPENDIX A). Verve's incident policy
lets Aisha recommend exactly one cluster for suspension before the surge; suspending a cluster
this size safely, without a slower human-reviewed rollout Verve does not have time for tonight,
can only be done once per incident (SEE APPENDIX A).

**Ring Alpha** is the first cluster: a set of accounts identified mainly by how densely they
connect to each other — heavy mutual following and messaging, visible as a dense block once the
connections are laid out in an adjacency matrix (SEE APPENDIX B). Dense mutual connectivity like
this is a textbook bot-ring signature. It is also, real published social-network data confirms,
close to what an ordinary tight-knit real friend group's own local connections typically look like
(SEE APPENDIX D) — so a dense block by itself does not settle the question.

**Wave Nine** is the second cluster: accounts whose defining signal is posting volume, not
connectivity — each one posting far more often than a real person typically could sustain,
especially with the event's surge still hours away (SEE APPENDIX C, APPENDIX F). Wave Nine's
accounts mostly interact with real users rather than each other, so their adjacency matrix is
comparatively sparse (SEE APPENDIX C).

Real published bot-detection research gives both signals a track record: connectivity-based
detection and volume-based detection are both established, real techniques, but neither performs
identically to the other, and neither performs identically under ordinary traffic conditions and
under a real traffic surge (SEE APPENDIX D). Aisha's actual decision has to weigh how many
confirmed bots each cluster's suspension would remove against how many real Verve accounts would
be wrongly caught in it (SEE APPENDIX E) — a fraction Verve's own event weekend makes more
consequential than usual, since some of the accounts a wrong call could catch are the exact
mid-size creators whose posts are about to carry Verve's highest-visibility traffic of the year.
Full source citations for every figure in this case are in APPENDIX G.

*Note: Verve is a scenario construction for this case — there is no real platform by this name. The full standards bridge for this case is in Appendix H.*

---

## Dilemma

You are Aisha Bello.

Do you:

**A.)** Suspend **Ring Alpha** — the cluster identified mainly by high mutual connectivity in its
adjacency matrix, despite only moderate posting-volume anomaly **OR**

**B.)** Suspend **Wave Nine** — the cluster identified mainly by extreme posting-volume anomaly,
despite lower mutual connectivity

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — Ring Alpha's adjacency matrix.** Build the 10×10 adjacency matrix for Ring Alpha's
  illustrative sample of accounts from the stated connection list (Appendix B), labeling every
  row and column and stating the matrix's dimensions.
- **D2 — Wave Nine's adjacency matrix.** Build the 10×10 adjacency matrix for Wave Nine's
  illustrative sample of accounts from the stated connection list (Appendix C), labeling every
  row and column and stating the matrix's dimensions.
- **D3 — A degree table and connectivity density for both clusters.** Compute each account's
  connection count directly from its adjacency matrix as a row sum (equivalently, the adjacency
  matrix multiplied by a column vector of ones), then use the total to compute each cluster's
  connectivity density: actual connections ÷ all possible connections.
- **D4 — A density interpretation memo.** Compare D3's two computed densities against Appendix
  D's real published bot-detection benchmarks, and explain in your own words why a dense
  adjacency-matrix block, on its own, does or does not prove a cluster is a bot ring.
- **D5 — A recommendation memo.** Using Appendix E's modeled confirmed-bot and false-positive
  counts, compute confirmed-bot accounts removed per real account wrongly suspended for both
  clusters, and recommend one — defended with D3/D4's density findings and Appendix A's
  one-cluster-only constraint.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Verve's Incident Constraints

| Quantity | Value |
|---|---|
| Hours from incident flag to the event's traffic surge | 6 hours [MA1] |
| Maximum clusters that can be safely suspended per incident, without a slower human-reviewed rollout | 1 [MA2] |
| Ring Alpha (Cluster A) — accounts flagged this incident | 250 [MA4] |
| Wave Nine (Cluster B) — accounts flagged this incident | 200 [MA5] |

*Note: Verve is a scenario construction for this case — there is no real platform by this name.*

---

## Appendix B: Cluster A — Ring Alpha, Illustrative Connectivity Sample

*This is a small, author-constructed illustrative sample (10 accounts) built to demonstrate the
matrix mechanism — it is not real Verve platform data. Connections shown: a follows/messages b,
mutually, for each listed pair.*

Connection list: A1–A2, A1–A3, A1–A4, A1–A5, A1–A6, A1–A7, A2–A3, A2–A4, A2–A5, A2–A6, A2–A7,
A3–A4, A3–A5, A3–A6, A3–A7, A4–A5, A4–A6, A4–A7, A5–A6, A5–A7, A6–A7, A7–A8, A8–A9, A9–A10.

**Adjacency matrix (1 = mutual follow/message, 0 = no connection):**

| | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 | A10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **A1** | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| **A2** | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| **A3** | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| **A4** | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| **A5** | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| **A6** | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
| **A7** | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 |
| **A8** | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| **A9** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| **A10** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

Matrix dimensions: 10×10. Total connections (edges): 24. Total possible connections (10 accounts,
undirected): 45. Wave Nine's posting-volume anomaly for this cluster is moderate — see Appendix E.

---

## Appendix C: Cluster B — Wave Nine, Illustrative Connectivity & Volume Sample

*This is a small, author-constructed illustrative sample (10 accounts) built to demonstrate the
matrix mechanism — it is not real Verve platform data.*

Connection list: B1–B2, B2–B3, B4–B5, B6–B7, B8–B9, B1–B9, B3–B10.

**Adjacency matrix (1 = mutual follow/message, 0 = no connection):**

| | B1 | B2 | B3 | B4 | B5 | B6 | B7 | B8 | B9 | B10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **B1** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| **B2** | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **B3** | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **B4** | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| **B5** | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **B6** | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| **B7** | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| **B8** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| **B9** | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| **B10** | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Matrix dimensions: 10×10. Total connections (edges): 7. Total possible connections (10 accounts,
undirected): 45.

**Average sustained posting rate, Wave Nine accounts, this incident:** 340 posts/hour per account
[MA9] — compare against Appendix F's real, published technical ceiling for what a standard
per-user API allowance permits (≈400 posts/hour, S2).

---

## Appendix D: Real Published Bot-Detection Benchmarks

| Item | Value |
|---|---|
| Combined multi-feature-class bot-detection system, cross-validated accuracy | 0.95 AUC (honeypot dataset) [S1] |
| Same combined system, false positive rate (manually-annotated "extended" dataset, optimal threshold) | 0.15 [S1] |
| Same combined system, false negative rate (same dataset/threshold) | 0.11 [S1] |
| Number of individual features used, across 6 feature classes (user meta-data, friends, network, content, sentiment, timing) | 1,150 [S1] |
| Single-feature-class accuracy: user meta-data features alone, or content features alone | AUC > 0.90 [S1] |
| Single-feature-class accuracy: "other" feature classes alone (includes network/connectivity features) | AUC > 0.80 [S1] |
| Real published social graph — Facebook ego-network dataset, nodes / edges | 4,039 nodes / 88,234 edges [S3] |
| Same dataset, average LOCAL clustering coefficient (how densely an ordinary user's own immediate circle connects) | 0.6055 (60.55%) [S3] |

*The real, published network-level density of the full Facebook ego-network dataset above (all
4,039 nodes at once) is only about 1.08% — but that whole-graph figure blends together many
separate, mostly-unconnected friend circles. The average LOCAL clustering coefficient (60.55%) is
the real figure that matters for this case: it measures how densely an ordinary real user's own
immediate circle connects to itself, which is exactly the scale Appendix B's Ring Alpha sample
matrix is built at.*

---

## Appendix E: Detection Model — Modeled False-Positive Rates and the Primary-Metric Computation

| Quantity | Ring Alpha (A) | Wave Nine (B) |
|---|---|---|
| Accounts flagged this incident | 250 [MA4] | 200 [MA5] |
| Modeled false-positive rate among suspended accounts | 20% [MA6] | 22.5% [MA7] |
| Modeled confirmed-bot accounts | 200 | 155 |
| Modeled real accounts wrongly suspended (false positives) | 50 | 45 |
| Confirmed-bot accounts removed per real account wrongly suspended | 4.00 | 3.44 |

*MA6 and MA7 are both derived from Appendix D's real, published combined-system false-positive
rate (0.15, S1) — see the Modeling Assumptions block below for the full derivation and basis of
each.*

---

## Appendix F: Real Platform Posting-Rate Ceiling

| Item | Value |
|---|---|
| Standard per-user posting allowance, a real, currently published social-platform API | 100 posts / 15 minutes (≈400 posts/hour sustained) [S2] |
| Same platform, per-app posting allowance | 10,000 posts / 24 hours [S2] |

*This is a real technical ceiling published by an existing platform's developer documentation,
used here only as a real-world proxy for what a fully-automated posting account can sustain —
Verve itself is fictional and publishes no such figure. See Appendix C for how it compares to
Wave Nine's stated posting rate.*

---

## Modeling Assumptions

> These figures are **not sourced** from Verve (a fictional platform) or, in most cases, from any
> external record at all. They are stated scenario assumptions chosen by the case author, or
> figures derived from real, cited research. A Hero may challenge any of them in discussion — that
> is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Hours from incident flag to the traffic surge | 6 hours | Matches the Overview's countdown-clock framing. | None — flavor only, not load-bearing. |
| MA2 | Maximum clusters safely suspendable per incident | 1 | Scenario constraint — this is what forces the binary choice in the Dilemma. | Structural — without it, Aisha could simply suspend both clusters and the dilemma would not exist. |
| MA4 | Ring Alpha accounts flagged this incident | 250 | Illustrative in-scenario cluster size. | **NONE on the margin.** The primary metric (confirmed bots removed per false positive) is confirmed÷FP = (1−p)/p, where p is the modeled false-positive rate — cluster size cancels out of that ratio algebraically. Changing MA4 changes only the raw headline counts in Appendix E, never the ratio or the recommendation. |
| MA5 | Wave Nine accounts flagged this incident | 200 | Illustrative in-scenario cluster size, independently sized from Ring Alpha's (different detection signals need not flag equal-sized clusters). | **NONE on the margin** — same reasoning as MA4. |
| MA6 | Ring Alpha's modeled false-positive rate | 20% | Derived from Appendix D's real, published combined-system false-positive rate (0.15, S1), scaled up ~30% and rounded to a clean 20%, reflecting that connectivity-only detection reaches a real published lower standalone accuracy (AUC > 0.80, S1) than the full multi-feature system (AUC = 0.95, S1). | MODERATE-HIGH. If Ring Alpha's rate were left at the real unscaled baseline (15%), its ratio would be 0.85/0.15 ≈ 5.67 — exactly tied with Wave Nine's *ordinary-conditions* ratio (see MA7's sensitivity note). |
| MA7 | Wave Nine's modeled false-positive rate, this incident (surge conditions) | 22.5% | Derived from the same real 0.15 baseline (S1), scaled up 50%. Basis: content/volume-based detection alone reaches a real published *higher* standalone accuracy in ordinary conditions (AUC > 0.90, S1) than connectivity-only detection — which would ordinarily predict a *lower* false-positive rate than Ring Alpha's. But this incident happens during Verve's highest-traffic weekend, when real users' own posting volume also spikes — a real, general, industry-documented limitation of volume-based anomaly rules during high-traffic windows. | **HIGH — the single most dilemma-relevant modeling choice in the case.** Under the real, unscaled baseline rate (15%, no surge premium), Wave Nine's ratio would be 0.85/0.15 ≈ 5.67, beating Ring Alpha's 4.00 by a real margin of about 29% — flipping the recommendation to Option B. The surge premium is what flips it back. |
| MA9 | Wave Nine's average sustained posting rate, this incident | 340 posts/hour/account | Illustrative in-scenario figure, chosen to sit close to (but under) Appendix F's real published technical ceiling of ≈400 posts/hour (S2) for a standard per-user API allowance. | LOW — flavor/context for why Wave Nine's volume signal reads as "extreme"; does not enter the primary-metric computation (Appendix E). |

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Combined multi-feature-class Twitter bot-detection system: cross-validated accuracy, false positive/negative rates, feature-class count, and per-feature-class standalone accuracy ranges | 0.95 AUC (honeypot); FP 0.15 / FN 0.11 (extended dataset); 1,150 features / 6 classes; user-metadata & content features alone AUC > 0.90; other classes (incl. network) alone AUC > 0.80 | Onur Varol, Emilio Ferrara, Clayton A. Davis, Filippo Menczer, Alessandro Flammini — ["Online Human-Bot Interactions: Detection, Estimation, and Characterization"](https://arxiv.org/abs/1703.03107) (arXiv:1703.03107) | 2017-03-27 | HIGH |
| S2 | Standard per-user and per-app posting rate limits, a real, currently published social-platform developer API | POST /2/tweets — 100 requests/15 min (per user); 10,000/24 hrs (per app) | X (Twitter) Developer Platform — [X API Fundamentals, Rate Limits](https://docs.x.com/x-api/fundamentals/rate-limits) | Current (accessed 2026-09-01) | HIGH |
| S3 | Real published social-network dataset: node/edge counts and average local clustering coefficient | 4,039 nodes; 88,234 edges; average clustering coefficient 0.6055 | Stanford SNAP — [ego-Facebook dataset](https://snap.stanford.edu/data/ego-Facebook.html) | Accessed 2026-09-01 (dataset undated) | HIGH |

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Matrix
- Matrix Dimension

**"How to…" questions**

- How to add and multiply matrices

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
