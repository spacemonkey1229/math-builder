# Guide Notes: The Skin Pack Atlas

**Case:** The Skin Pack Atlas · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Pre-Calculus/Matrices — Matrix / Matrix Dimension / Determinant / Identity Matrix /
how to add and multiply matrices / how to find the determinant of a 2x2 matrix / how to solve a
system of equations using a matrix (see `case.json.standards[]` for exact ids). **This is a
second-pass/redundancy case** — all 7 skill ids already carry `n=1` coverage from
`the-multiplier-recruit`, so `new_coverage: []` is correct and expected here, not a gap. This case
exists to give the Pre-Calculus/Matrices group a second, structurally distinct case in a different
real-world domain (mobile game GPU/texture hardware, not regional economics).

Drafted at write time, 2026-08-30. `margin_pct` resolved by `case-research`, 2026-08-30: 13.6% —
**recomputed 2026-08-30 in a staleness-remediation re-research pass, triggered by a human review
flag that two of the case's cited sources (a 2013 Unity blog, a 2017 DeviceAtlas blog) were too
stale for a case about current mobile hardware distribution. New figure: 14.9%. Winning option
unchanged: B (The Anchor Atlas, 4096×4096).** See the worked arithmetic and full margin note below
and in `case.json`'s `balance` object; see `RESEARCH_LOG.md`'s 2026-08-30 section for the full
research trail on what was replaced and why.

## Intro

Frame the format before any numbers: "You are Alicia Tran, the only technical artist at a
seven-person indie studio. Tonight's skin pack has to ship in one of two builds. One looks
noticeably better. The other one you know works everywhere. You have twenty minutes." Let the room
sit with that tension before Launch.

## Launch

Show the two renders side by side with only the visual difference visible — no device data yet.
Ask for a gut read: "Which one do you ship?" Most rooms will pick the crisper one on looks alone.
Do not correct that instinct yet — it is exactly what the case is built to test.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Crest Atlas — the sharper one?" Show of hands, both
options, no discussion. Record the count for the Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow. Heroes will want to just compare "which looks nicer" or assume the safe option
(Anchor Atlas) is obviously correct because it never fails. Push: "Alicia isn't being asked which
texture looks better in a screenshot. She's being asked which one keeps the most *paying players*
able to play at all — and whether a device failing to load a texture costs the studio the same
amount no matter who's holding that device." If the room arrives at "we need a number that accounts
for both hardware failure *and* how much a player is worth" on its own, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening Appendix B: build
the install-base matrix M (D1), find its inverse and check the identity-matrix verification (D2),
confirm the determinant is nonzero first (D3), solve for revenue-per-install by device tier (D4),
then apply that to the whole install base for each atlas option (D5). Re-ask: "Now that we can see
the steps — is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's three Modeling Assumptions honestly: MA1 (Tanager Games and *Molt* are
fictional — the install and revenue figures are invented business numbers, built to match real,
cited current regional chipset-vendor data even though the studio itself isn't real), MA2
(chipset-vendor share — MediaTek in India, Transsion-brand devices in Nigeria — is used as a
stand-in for "capped below 8192," a real and current but still imperfect proxy), and **MA3, new as
of the 2026-08-30 re-research pass**: the model's Value-tier cap describes the Mali-400 GPU, which
ARM discontinued in **2015** — the budget chips that actually dominate these markets today
(Unisoc T612/T615, MediaTek Helio-class) run newer Mali-G52/G57-class GPUs that support OpenGL ES
3.2 and Vulkan, tiers the Mali-400 never reached. Ask which assumption is load-bearing for the
comparison (MA1 is — different assumed revenue splits between India and Nigeria change the solved
D4 vector) and which one biases the result in a known direction (MA3 — unlike MA2's two-sided
uncertainty, MA3 points one way: it likely means the model *overstates* Option A's true 2026
failure rate, not understates it. A room that reasons its way to "so the safe choice might be even
safer than the numbers say, not less safe" has found the real teeth of this case's current
sourcing, not just repeated the arithmetic).

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D3 as a room (build the matrix, invert it, check the
determinant), then split into two desks for D4 — one solves for Flagship-tier revenue-per-install,
one cross-checks the Value-tier figure — before reconvening for D5's shared decision table.

**Facilitator-only arithmetic note (recomputed 2026-08-30, staleness-remediation pass — supersedes
the case-research pass's original arithmetic, which used the now-superseded S1/S2 sources; see
`RESEARCH_LOG.md`).**

Inputs (Appendix A, [MA1] for installs/revenue, [S1'/S2'] for tier shares): India 40,000 installs
(53% Flagship / 47% Value), $19,780/month revenue; Nigeria 20,000 installs (49.3% Flagship / 50.7%
Value), $9,409/month revenue.

```
M = [ 21,200  18,800 ]     (India:   40,000 x 0.53, 40,000 x 0.47)
    [  9,860  10,140 ]     (Nigeria: 20,000 x 0.493, 20,000 x 0.507)

det(M) = 21,200(10,140) - 18,800(9,860) = 214,968,000 - 185,368,000 = 29,600,000   (nonzero -> invertible)

M^-1 = (1/29,600,000) [ 10,140  -18,800 ]
                       [ -9,860   21,200 ]

v = [19,780; 9,409]   (reported total monthly revenue, India; Nigeria)

r = M^-1 v = [0.80; 0.15]
   -> $0.80/month revenue per Flagship-tier active install
   -> $0.15/month revenue per Value-tier active install
```

Totals: 31,060 Flagship-tier installs, 28,940 Value-tier installs, 60,000 installs overall;
$24,848/month Flagship-tier revenue of $29,189/month total revenue.

D5 decision table:

| | Device-count % rendering successfully | Revenue-weighted % rendering successfully |
|---|---|---|
| Option A — Crest Atlas (8192) | 31,060 / 60,000 = **51.8%** | $24,848 / $29,189 = **85.1%** |
| Option B — Anchor Atlas (4096) | **100%** (fixed, by construction) | **100%** (fixed, by construction) |

**Recommendation and margin:** Option B wins. Margin = (100 − 85.1) / 100 = **14.9%**, comfortably
inside SPEC §2's ~20% cap. This is the case's intended twist made concrete: a Hero who stops at
Appendix C's raw device-share numbers sees Option A failing on roughly half of *devices* in
Tanager's two growth markets and would call it reckless; the revenue-weighted number tells a
materially less alarming story — a 14.9-percentage-point gap in *revenue* at risk, not the near-even
split of *devices* Appendix C's raw share suggests — real, and still enough to favor the safer
option once weighed against the sourced narrative (support tickets and refund requests already
happening in these exact markets). Do not read the 85.1% figure aloud to Heroes before D4 is
solved — it is the number the whole matrix exercise exists to produce.

**A second layer, if a room gets this far (MA3).** Even 85.1% is likely too pessimistic for
Option A: the model's Value-tier cap describes the Mali-400 GPU (discontinued by ARM in 2015), not
the newer Mali-G52/G57-class chips that actually dominate India/Nigeria's budget segment today —
which mostly clear well past 4096px. If a Hero raises this, don't treat it as breaking the case:
walk them to the conclusion that it makes Option B's margin *conservative* (an overestimate of
Option A's real risk), not wrong. The recommendation doesn't flip; the honesty of the number
improves.

**Argument for A (The Crest Atlas).** Full detail ships to every Flagship-tier device. The
Value-tier devices that fail outright skew toward Tanager's lowest-revenue-per-install segment
(per the D4 solve) — so the *revenue-weighted* failure rate should read meaningfully smaller than
the raw device-count failure rate. The case's tension is real only if this gap is large enough to
make Option A defensible despite a nonzero failure rate.

**Argument for B (The Anchor Atlas).** Every device Tanager has ever tested loads it — the
revenue-weighted success rate is a fixed 100% by construction, an unconditional guarantee Option A
cannot match at any margin. It costs some visual polish, never a paying player.

**The margin.** `margin_pct` = **14.9%**, Option B (Anchor Atlas) wins. `margin_basis`: compare
D5's revenue-weighted success percentage for Option A (85.1%) against Option B's fixed 100%. See
the worked arithmetic above.

## Twist

**Twist: N/A.** As with the project's other strongest structurally-driven cases, the surprise here
is mathematical, not narrative: the moment a Hero realizes that "percent of devices that fail" and
"percent of *revenue* that fails" are not the same number, and that the gap between them is exactly
what D4's matrix solve was for. A Hero who stops at Appendix C's raw device-share percentages will
never notice this on their own.

## Immediate recommit

Re-vote immediately after D5's decision table lands. Ask by name: "Now that you've seen 85.1%
instead of 51.8% — does that change your vote, or does it just tell you that 'roughly half of
devices' was the wrong number to vote on in the first place?" That distinction — noticing which
number the decision actually turns on — is the transferable skill, not the vote itself.

## The trap

A Hero who reads Appendix C, sees a large device-count share on Value-tier (budget chipset-family)
GPUs in Tanager's fastest-growing markets, and stops there will conclude the Crest Atlas is an obviously
reckless choice — "you'd be breaking the game for a third of your fastest-growing markets." That
conclusion never asks whether those failing devices are worth the same to the studio as the
devices that succeed. Watch for a pitch that cites only Appendix C's device-share percentages and
never opens Appendix A or D4's solved revenue-per-install vector.

**A second, quieter trap.** A Hero can build and solve the matrix correctly, produce a genuinely
smaller revenue-weighted failure rate for Option A than the device-count rate suggested, and still
be wrong to recommend Option A if that revenue-weighted rate remains too far below Option B's fixed
100% once SPEC §2's 20% margin cap is checked. Correct matrix work does not by itself make Option A
the right call — it only makes the comparison honest. Press for the actual D5 number before
accepting a recommendation either way.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on their choice for the multiplier reason, or did they just guess right?

## Deep conflict — two threads (up to 20 min)

1. **Device-count failure vs. revenue-weighted failure.** Is it fair for a studio's technical
   decision to weight a paying player's hardware failure as "worth less" than a bigger spender's,
   even when both players are locked out of content they already own? Where's the line between
   sound business math and treating some players as disposable?
2. **How much should Alicia trust a proxy?** Chipset-vendor share stands in for "capped below
   8192×8192," but Appendix E discloses two real gaps: some non-MediaTek/Transsion devices may also
   be capped (MA2), and — the sharper current finding (MA3) — the budget chips this proxy actually
   counts have mostly moved past the Mali-400-era cap the model assumes, meaning the proxy likely
   *overcounts* Option A's true failure rate instead. Does the case's recommendation still hold once
   a Hero sees that — and how would Alicia find out before shipping, not after the support tickets
   arrive?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — visual comparison only, gut-check vote |
| 3:00–8:00 | Anchor 1 vote recorded; Anchor 2 pressure-tests "better, measured how?" |
| 8:00–12:00 | Anchor 3 — name the five-step process before opening Appendix B |
| 12:00–15:00 | Anchor 4 — surface MA1–MA3, ask which is load-bearing vs. which biases direction |
| 15:00–30:00 | Data Deep Dive — D1–D5 worked in two desks, reconvene for the shared table |
| **~25:00** | **NAME THE TRAP** — device-count failure rate is not revenue-weighted failure rate; this case's twist is mathematical, it drops here |
| 30:00–40:00 | Deep conflict — weighting players by spend; trusting the chipset-vendor proxy |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## Socratic questions

1. Appendix C shows a real, sizable share of Android GPUs capped below the Crest Atlas's dimension — why isn't that percentage, by itself, the answer to Alicia's decision?
2. Your D4 solve gives two different revenue-per-install numbers for Flagship-tier and Value-tier devices — what would have to be true about those two numbers for the Crest Atlas to become the clearly wrong choice, even before you finish D5?
3. Appendix E discloses that the chipset-vendor proxy for "Value-tier" is built on GPU generations (Mali-G52/G57) that mostly clear well past the old Mali-400's 4096px cap — does that make Option A look better or worse than this case's numbers suggest, and why does the direction of that bias matter more here than its exact size?
4. You computed a determinant for M before inverting anything — what would it have meant for Alicia's whole model if that determinant had come out to zero?
5. If Tanager's Nigeria market kept growing much faster than India's, would you expect the revenue-weighted failure rate for the Crest Atlas to get better, worse, or stay the same — and why does that depend on which market has the higher Value-tier share?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for the raw device-count percentage first, and how much nudging it took
  to get to the revenue-weighting question.
- Whether the identity-matrix verification step (D2) was treated as a real check on the inverse or
  as a box to tick before D4.
- Whether the "this proxy is now probably too pessimistic" direction of MA3 was noticed
  independently, and whether Heroes correctly concluded it strengthens rather than undermines
  Option B's case.

## Standards Touched On

Matrix · Matrix Dimension · Determinant · Identity Matrix · How to add and multiply matrices · How
to find the determinant of a 2x2 matrix · How to solve a system of equations using a matrix

## Facilitator note — margin resolved (case-research, 2026-08-30; recomputed in staleness-remediation pass, 2026-08-30)

`margin_pct` = **14.9%** (superseded from 13.6%), winning option unchanged: **B (The Anchor Atlas,
4096×4096)**. This case's original two GPU-hardware sources (a 2013 Unity blog, a 2017 DeviceAtlas
blog) were flagged in human review as too stale for a case about *current* mobile hardware
distribution. A full re-research pass replaced them with current (2025) chipset-vendor data
(Counterpoint Research for India, Statcounter-via-Intelpoint for Nigeria), added a current academic
source (an April 2025 arXiv empirical study on mobile-game GPU compatibility bugs) and Google's own
live Android distribution dashboard, and — most importantly — honestly disclosed a new finding
(MA3): the model's Value-tier cap describes a GPU (Mali-400) that ARM discontinued in 2015, while
the budget chips that actually dominate these markets today run newer silicon that mostly clears
that cap. Sourced/assumed figures: Appendix A's install/revenue figures are MA1 (disclosed invented
studio business figures, recomputed to match updated tier shares); Appendix A/C's device-tier
shares (India 47%/53%, Nigeria 50.7%/49.3% Value/Flagship) are real, current, cited data (S1', S2');
Appendix C's texture-cap ladder is unchanged historical hardware-capability data (S3–S6), now
supplemented by S7 (academic) and S8 (Google's live dashboard). See `RESEARCH_LOG.md`'s 2026-08-30
section for the full remediation trail and `case.json`'s `balance.margin_note` for the recomputed
worked arithmetic. This case is ready to schedule.

## Facilitator note — sensitivity (SPEC §6)

This case carries no SPEC §6 sensitivity — it is a routine shipping/engineering trade-off (which
texture atlas a small studio ships), per the concept sheet's own assessment. No facilitator flag is
needed beyond normal classroom awareness that some Heroes may have family or friends who develop or
play mobile games on lower-cost devices in the markets named in this case.
