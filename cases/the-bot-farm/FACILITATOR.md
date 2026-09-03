# FACILITATOR.md — The Bot Farm

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Bot Farm · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Matrices — Matrix, Matrix Dimension, and How to add and multiply matrices (see
`case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01) — all 13 `{{NEEDS_SOURCE}}` tokens closed (4
SOURCED, 9 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `13.9` (see Balance below) — comfortably under SPEC §2's ~20% cap
on the first construction, no MCS-46 waiver needed. Not yet run through `case-qa`.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **Varol, Ferrara, Davis, Menczer, Flammini — "Online Human-Bot Interactions" (arXiv:1703.03107,
  2017)** — the real academic anchor for the whole case. A real Twitter bot-detection framework
  using 1,150 features across 6 classes (user meta-data, friends, network, content, sentiment,
  timing). Combined system: 0.95 AUC, real FP/FN rates of 0.15/0.11. Crucially, single-feature-class
  models show user-metadata and content (volume-flavored) features alone reach AUC > 0.90, while
  "other" classes including network/connectivity features alone reach only AUC > 0.80 — i.e., in
  the real literature, connectivity signal is the comparatively *weaker* standalone predictor. This
  is the real basis for MA6/MA7's false-positive-rate modeling, and it is a genuinely counter-
  intuitive real finding worth surfacing in discussion: Cluster A's "textbook" signal is real, but
  the literature says it's the less individually reliable of the two.
- **Stanford SNAP ego-Facebook dataset** — real dataset, 4,039 nodes, 88,234 edges, average LOCAL
  clustering coefficient 0.6055. This is the real evidence behind the case's central ambiguity
  claim: ordinary real friend circles cluster locally at ~60%, which is in the same range as Ring
  Alpha's illustrative sample density (53.3%) — a dense block genuinely does not, by itself, prove
  a bot ring.
- **X (Twitter) Developer Platform, API rate limits (docs.x.com)** — real, current, primary-source
  technical ceiling (100 posts/15 min per user via the standard API). Used only as a proxy for
  "how much posting volume is even technically possible for a single automated account," grounding
  Wave Nine's stated 340 posts/hour figure without inventing a platform-specific number for the
  fictional Verve.

## Intro

Frame the format: Aisha has one shot, six hours, and two flagged clusters — this is a real kind of
call Trust & Safety teams make under real time pressure, not a made-up scenario. Name the opener:
"You get to suspend exactly one of these two clusters tonight. Whichever one you don't pick keeps
running through the platform's biggest weekend of the year. Which one goes?"

## Launch

Show Appendix B and C's two adjacency matrices side by side, with no density/degree numbers
computed yet — just the raw grids of 1s and 0s. Ask: "Just looking at the two grids, which looks
more like a bot ring to you?" Most rooms will point at Ring Alpha's dense block immediately. Do not
confirm or correct. Record the split — Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Wave Nine — the sparser-looking cluster?" Show of hands,
both options, no discussion. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'looks like a bot ring'?"**

Let confusion grow on purpose. Heroes will want to jump straight to "the dense one is obviously the
bots." Push: "What would a real, innocent, tight-knit group of friends' connections look like on
this same kind of grid? Would it look different from Ring Alpha's?" If the room lands on "we can't
actually tell just by looking at density," the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Name the actual steps before touching the appendices: build both adjacency matrices (D1, D2);
compute degree and density for both (D3); compare those densities against what real published
research says about connectivity signal vs. volume signal (D4); and use a real confirmed-bots-per-
false-positive computation, not a gut read, to make the call (D5). Re-ask: "Is our question still
the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface honestly: Verve is fictional, so its actual false-positive rates for either detection method
don't exist to look up — Appendix E's rates are modeled, derived from real published academic
figures (Appendix D), not measured at Verve itself. Ask which of the case's assumptions is most
load-bearing. The honest answer: MA7, Wave Nine's surge-elevated false-positive rate, is the single
assumption that actually decides the case — remove the surge premium and the real math favors the
other cluster.

## Data Deep Dive

Now, and only now, the numbers. Walk D1-D3 together as a room, cold-calling for the degree/density
computation specifically (row sums, or equivalently the matrix times a ones-vector). Then walk D4's
comparison against Appendix D's real AUC figures. Then D5's final ratio computation — this is where
a Hero who built a correct matrix but never connects it to Appendix D's real research will visibly
struggle to defend a recommendation.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly: "Here's something Appendix E doesn't say outright. The false-positive rate you used
for Wave Nine — 22.5% — isn't the real academic baseline. The real published number, if this
weren't happening during Verve's highest-traffic weekend of the year, is 15%. At 15%, Wave Nine's
ratio isn't 3.44. It's 5.67. That beats Ring Alpha's 4.00. If tonight weren't surge night, the real
math would tell you to suspend the *other* cluster."

"So: is the math wrong? Or did the situation itself — the surge, six hours out — actually change
which cluster is the better call, in a way you'd only catch by checking the assumption, not just
trusting the density picture?"

**Facilitator-only: what this does and doesn't change.** MA6/MA7 are real, disclosed modeling
choices, not hidden data — a sharp Hero could have found this by re-deriving Appendix E from
Appendix D's real 0.15 baseline themselves before the twist even drops. That is exactly the kind of
check the Twist rewards.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why the dense one is more suspicious — or isn't" (Anchor 2). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name D1-D5, surface which figures are real vs. modeled. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call the degree/density computation and the final ratio. |
| **25:00** | **DROP THE TWIST** — the real 15%-vs-22.5% baseline reveal, delivered slowly. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just changed — the math, or your read of the situation?" |
| 30:00–40:00 | Threaded deep conflict — see below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **A dense block is real signal, but not proof.** Ring Alpha's 53.3% illustrative density is real
   and matches a genuine, published bot-ring pattern — but Appendix D's real 60.55% local
   clustering-coefficient figure shows ordinary real friend circles cluster almost this densely too.
   Push: "What would you need, beyond the density number alone, to be confident Ring Alpha isn't
   just a real creator collab?"
2. **Cluster size looks like it should matter. It doesn't.** A Hero who assumes suspending the
   *bigger* cluster (250 vs. 200) automatically catches more bots has missed that the ratio itself
   — confirmed bots per false positive — is algebraically independent of cluster size. Push: "If
   Ring Alpha had 500 accounts flagged instead of 250, would that change which cluster you'd pick?
   Prove it."
3. **The surge is not decoration — it's the whole fulcrum.** MA7 exists because a real, general
   pattern (volume-based rules degrade during real traffic surges) applies here. Push: "If this
   incident happened on an ordinary Tuesday instead of six hours before the biggest weekend of the
   year, would your recommendation change? Why?"

## The trap

Heroes will treat "denser matrix = more suspicious = suspend it" as sufficient on its own, without
ever computing Appendix D's real comparison (connectivity-alone AUC > 0.80 vs. content/volume-alone
AUC > 0.90) or noticing that Appendix E's rates are *modeled*, not measured — missing that the real
lever in this case is whether the surge specifically degrades Option B's usual advantage, not which
cluster's picture "looks" more like a bot ring.

## Socratic questions

1. Ring Alpha's illustrative matrix is 53.3% dense, and a real published social-graph dataset shows ordinary friend circles cluster at about 60.55% locally — does that real comparison make you more or less confident Ring Alpha is a bot ring, and why?
2. The primary metric's ratio, confirmed bots per false positive, works out to exactly (1-p)/p, where p is the modeled false-positive rate — what does that tell you about whether cluster size (Appendix A) was ever actually relevant to your decision?
3. Appendix E's two false-positive rates (20% and 22.5%) are both modeled, not measured — if you only trusted the real, unscaled academic baseline (15%) for both clusters, would your recommendation change, and what does that tell you about which assumption actually did the work?
4. The twist reveals that under ordinary (non-surge) conditions, the real math favors Wave Nine — was the original recommendation wrong, or was it right for conditions that no longer apply six hours from now?
5. If Aisha had ten hours instead of six, would you expect that to change which cluster she should suspend, and what would have to be true about the incident for more time to actually change the math rather than just feeling like it should?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Matrix · Matrix Dimension · How to add and multiply matrices

## Balance argument (SPEC §2)

**Argument for A (Ring Alpha).** Real, published bot-ring signature (dense adjacency-matrix block);
connectivity signal is comparatively insensitive to a one-time traffic surge, unlike a volume
threshold. At Appendix E's modeled rates: 4.00 confirmed bots removed per real account wrongly
suspended.

**Argument for B (Wave Nine).** Real academic literature (Varol et al. 2017) shows volume/content
signal alone is the *stronger* individual predictor in ordinary conditions (AUC > 0.90 vs. > 0.80
for connectivity alone) — and Ring Alpha's dense block is also textbook-consistent with a real
tight creator group (S3's real 60.55% local clustering figure). Even at the surge-adjusted rate,
Wave Nine still removes 3.44 confirmed bots per real account wrongly caught — a real, working
alternative, not a clearly inferior one.

**Margin — COMPUTED 2026-09-01.** `margin_pct: 13.9`. **Winner: Option A, Ring Alpha.** Ratio =
(1-p)/p for each cluster's modeled false-positive rate p (MA6=20%, MA7=22.5%): A = 4.00, B = 3.44.
margin_pct = (4.00-3.44)/4.00 × 100 = 13.9% — comfortably under SPEC §2's ~20% guideline on the
first construction; no retune pass was needed.

**Counterfactual, checked explicitly.** Reverting Wave Nine's rate to the real, unscaled academic
baseline (15%, i.e. removing the surge premium MA7 supplies) flips the winner: B's ratio becomes
5.67, beating A's 4.00 by 29.4%. This is the case's real fulcrum and the Twist's payload — not
cluster size (proven algebraically irrelevant), not Ring Alpha's density in isolation, but whether
the surge genuinely degrades volume-based detection's real, published ordinary-conditions advantage.

## Facilitator note — sensitivity (SPEC §6)

Keep this framed strictly as a detection-method tradeoff on a fictional platform (Verve) with no
named real users or real account content — consistent with the case's design intent. No harassment/
moderation-harm framing; the stakes are "correctly identify automated accounts" vs. "wrongly
suspend a real person," not any individual's identity or content.
