# FACILITATOR.md — The Rig Budget

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Rig Budget · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Pre-Calculus / Matrices — Matrix, Matrix Dimension, Determinant, Identity Matrix,
How to add and multiply matrices, How to find the determinant of a 2x2 matrix, How to solve a
system of equations using a matrix (see `case.json.standards[]` for exact ids).

**Status:** Balance-redesigned (2026-09-01) after the original `case-research` pass's 45.0% margin
was flagged as structurally over SPEC §2's ~20% cap (see `RESEARCH_LOG.md`'s REDESIGN PASS section
for the full history). The dilemma, sources, deliverables, and balance model below are the
**current, redesigned version**. `case.json.status` is `"researched"`. `margin_pct` is `17.9` —
real, sourced, and under SPEC §2's cap. Not yet run through `case-qa`; treat the numbers as
sourced-and-computed but not yet QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **Unity's own published mobile-rigging guidance** (Unity 5.6 Manual, still live) states plainly:
  keep bone counts "below thirty for mobile devices," and keep mobile meshes in the "300 to 1500
  polygons" range (S1, S2). Fenwick Games itself is fictional, but the rig it builds is sized to
  match what a real mobile studio would actually ship. After the redesign, these two figures are
  **context only** — they size Appendix A's rig, but no longer feed margin_pct.
- **Ocean View Games' two published guides** (a frame-budget calculator and a Unity optimization
  checklist, same real studio, both fetched and confirmed) supply the real "60fps for action games"
  genre guidance and the real "16.6ms per frame at 60fps" budget figure (S3, S4) — still fully
  load-bearing for Appendix D/F's "share of frame budget" context.
- **raduacg/game-mechanics-optimizations (GitHub)** (S5) — a real, dated, personal collection of
  game optimization technique notes — includes a genuinely useful worked example: skinning 100
  characters at 50 bones/5000 vertices each blows a 60fps CPU budget by 3.6x on paper, and moving
  the same per-vertex transform work to the GPU collapses it to under 1ms. Still real precedent for
  "per-vertex matrix work adds up faster than intuition suggests" (Appendix E) — unaffected by the
  redesign.
- **Kavan, Collins, Žára, O'Sullivan, "Skinning with Dual Quaternions" (SI3D 2007)** — the redesign's
  new load-bearing source (S6/S7/S8). This is a real, peer-reviewed graphics-research paper, fetched
  and read in full (not summarized). It reports **real, measured GPU runtimes**: linear blend
  skinning (LBS) = 0.32 ms/frame, direct quaternion blending (DQB) = 0.39 ms/frame, for a
  comparably-rigged character mesh — a real 17.9% margin. It also explains, in exact citable terms,
  why LBS's weighted-sum-of-matrices approach can produce an invalid (non-rigid) blended transform
  at a multi-bone seam — the real mechanism behind the "candy-wrapper" artifact well-known in
  character animation — and documents DQB's own real limitation (a fixed rotation center that
  "works perfectly" at simple two-bone joints like an elbow, but distorts more complex multi-bone
  joints like the armpit or dorsum).
- **The actual engineering fact this case is now built on:** most of a character rig is single-bone
  (one bone, one patch of mesh — unaffected by today's decision, see D1/D2(a)/D3(a)'s elbow-bone
  example). Only at real multi-bone **blend zones** (shoulder, underarm, cape mount) does the
  engine have to choose *how* to combine two or more bones' transforms for the same shared vertex —
  and that choice has a real, measured cost (S6) and a real, provable mathematical consequence
  (S7, via the determinant), grounded entirely in the peer-reviewed graphics literature rather than
  in this case author's own derivation (contrast the original version, where the "compose once vs.
  redo every time" cost model needed no external citation because it followed from ordinary linear
  algebra alone — that fact is still true and still appears in D1/D2(a), it just no longer drives
  margin_pct).

## Intro

Frame the format: this is a real device-performance-budget decision the night before a
certification pass, not a worksheet. Name the opener — "You're the only rigger who touched this
system. Tomorrow morning a phone that's slower than your laptop is going to tell you whether you
were right." Mention, once, that "how do you blend two bones' influence on the same vertex" is a
real, decades-old, still-unsettled question in the game industry — not a toy problem invented for
the case; the two named techniques (linear blend skinning and quaternion blending) are real,
still-used, industry-standard tools.

## Launch

Show the two branches side by side exactly as the Overview describes them — one sums the two
bones' weighted matrices directly, the other converts to quaternions first, blends those, and
converts back — with no numbers yet. Ask: "Which one would you ship, just from what you see here?"
Do not confirm or correct. Most rooms will split roughly along "simpler math sounds safer" vs.
"there must be a reason the fancier one exists"; record the split, Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with The Quaternion Blend — the version that converts to a
different kind of number before blending?" Show of hands, both options, no discussion yet. Record
the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'costs less compute'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which one is faster,"
but push on what "costs less compute" actually means in a way you could count, and what "better"
even means if both options draw the character correctly most of the time: "If both pipelines draw
the exact same-looking hero on screen almost everywhere, what number are we actually comparing?
Milliseconds? Something about correctness?" If the room lands on "we need to count something
specific — a real measured cost — AND check whether the cheaper option is even mathematically
valid," the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room lands on "we need real cost data AND a correctness check," ask them to name the
actual steps before touching the appendices: write R and S for a plain single-bone (elbow) transform
to warm up (D1); compose that AND the shoulder blend-zone's two-bone weighted sum by hand (D2);
check both are valid, non-degenerate transforms via their determinants — this is where the shoulder
blend-zone's math gets interesting (D3); confirm you can recover the blend-zone's matrix a different
way, by solving a system (D4); then bring in the real measured GPU cost data and build the
recommendation table (D5). Re-ask: "Is our question still the right one, now that we can see the
steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Fenwick Games' own exact bone count, mesh density, and animation
data are all stated scenario assumptions — Fenwick is a fictional studio, so none of these can be
independently verified the way real, published mobile-rigging guidance can. More importantly,
surface MA7: the real measured GPU cost data (S6) comes from a 2007-era desktop benchmark on a
differently-sized mesh, not from Fenwick's own mobile hardware. Ask: "Does that matter for Dana's
decision? What would we need to be more sure?" The honest answer: the *relative* cost (17.9% more
for the Quaternion Blend) is the real, sourced, load-bearing number; nobody has published a
mobile-specific version of this exact benchmark, and this case says so plainly rather than
pretending otherwise.

## Data Deep Dive

Now, and only now, the numbers (once `case-research` has closed Appendix D). Walk D1's elbow R/S,
D2's two hand-computed matrices (elbow M and shoulder M_blend), D3's two determinant checks, and
D4's system-solve together as a room, cold-calling for D5 specifically — this is where a Hero who
correctly computed det(M_blend) = 0.5 in D3 but never connects it back to the real "candy-wrapper"
defect described in Appendix B (S7) will visibly struggle to answer "so what does a determinant of
0.5 actually mean for how the hero looks on screen?"

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses, once Appendix D is sourced: "Every deliverable you just did — D1
through D4 — was worked at the shoulder. And per the *same real source* that documents The
Quaternion Blend's advantage, the shoulder is exactly the case where it 'works perfectly': two
bones, one clean joint, like an elbow. But the hero rig has two *other* blend zones you haven't
touched: the underarm, and the cape's mounting point — both influenced by three or more bones at
once, not two. What does Appendix C's own source say happens to The Quaternion Blend at
*those* joints?"

Work it live if the room hasn't already: reread S8/Appendix C together — "artifacts result from the
fact that the center of rotation is fixed and does not adapt to the actual posture," specifically at
joints "more complex" than a two-bone hinge, with the source's own examples being "the armpit or
dorsum." The underarm is functionally that exact case.

"So — for the shoulder, where you just proved The Direct Blend visibly collapses (det = 0.5) and The
Quaternion Blend is documented to work perfectly, does your recommendation still hold? And for the
underarm and the cape mount, where The Quaternion Blend has its *own* real documented problem — does
it matter *at all* which pipeline Dana ships there? Does Dana have to pick one pipeline for the
*whole* rig, or could the answer be different blend-zone by blend-zone?"

**Facilitator-only: what this does and doesn't change.** This does not change Appendix D's real
17.9% measured cost margin — that number is real regardless of which blend zone you're standing at.
What it breaks is the unstated assumption that "The Quaternion Blend is the safe, correct choice"
is a fact about the whole rig, rather than a fact this case only actually demonstrated at one
(the simplest) blend zone. A Hero who has not noticed this will answer "is Option B safe at the
underarm" with the same confidence they'd answer for the shoulder — and that confidence is not
earned by the source they actually read.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just fair" (Anchor 2 — what does "costs less compute" actually mean, and what would "not mathematically valid" even mean here?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface MA7's benchmark-scale caveat. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call D3's determinant finding and D5's real-cost table specifically. |
| **25:00** | **DROP THE TWIST** — the underarm/cape blend zones, delivered slowly, with pauses. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — the math, or the assumption that one blend zone's answer covers the whole rig?" |
| 30:00–40:00 | Threaded deep conflict — see the three named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **A real fix at one joint is a real risk at another.** The Quaternion Blend is documented to
   "work perfectly" at the shoulder but to have its own real artifact at more complex joints (S8).
   Push: "Is 'ship one blending technique for the whole rig' even the right question, once you've
   seen the underarm? What would it cost Dana to mix techniques blend-zone by blend-zone — and is
   that cost worth paying, for a studio where Dana is the only rigger?"
2. **A cheap technique that's provably wrong some of the time is still cheap.** The Direct Blend's
   real advantage is 17.9% less GPU cost, every frame, forever. Push: "D3(b) proved the shoulder's
   blended matrix has determinant 0.5, not 1 — a real, visible defect. Is a 17.9% performance win
   worth shipping a technique you can prove, by hand, produces the wrong math at a joint players
   will actually see move?"
3. **17.9% of what, exactly, and how sure are we of that number?** A Hero who reports "Option B
   costs 17.9% more" without engaging MA7's disclosure — that this figure comes from a 2007-era
   desktop GPU benchmark on a bigger mesh than Fenwick's own — has not actually finished thinking
   about D5. Push: "Would you ship a recommendation on this number alone? What would you want to
   verify before you trusted it on Fenwick's actual target phone?"

## The trap

Heroes will treat "The Direct Blend is cheaper" as obviously settling the case and recommend it
without ever engaging with the real, provable defect D3(b) surfaces (det(M_blend) = 0.5) — treating
a 17.9% performance win as free when it is not mathematically free at all. A second, opposite trap:
Heroes who see D3(b)'s defect will treat "ship The Quaternion Blend, it's mathematically correct" as
automatically settling the case, without ever reading Appendix C's own source (S8) closely enough to
notice that "correct at the shoulder" is not the same claim as "correct everywhere on the rig" — the
Twist exists specifically to catch a Hero who has not asked "does this source's guarantee hold for
every blend zone, or just the one I checked?"

## Socratic questions

1. D3(b) shows the shoulder blend-zone's Direct-Blend matrix has determinant 0.5, not 1 — a real, provable defect. D5 shows The Quaternion Blend costs 17.9% more in real measured GPU time to avoid that defect. If you were Dana, which number would you weigh more heavily, and does your answer depend on whether players can actually see the shoulder seam during combat?
2. Appendix C's own source says The Quaternion Blend "works perfectly" at simple two-bone joints like the shoulder, but has a real, different artifact at more complex joints like the underarm. If you were designing Fenwick's rig pipeline, would you use one blending technique for every blend zone, or would you let Dana choose zone by zone? What would that decision cost to build and maintain?
3. MA7 discloses that the real 17.9% cost figure comes from a differently-sized, 2007-era desktop benchmark, not from Fenwick's own mobile hardware. Does a real, sourced, but not-perfectly-matched number still count as "real data" for a decision like this? What would change your answer?
4. Appendix E describes a real example where per-vertex transform cost blew a 60fps budget by 3.6x on CPU, fixed almost completely by moving the work to the GPU. Both of today's options already run on the GPU and use only about 2% of Fenwick's real frame budget each. Does that change how much this specific decision should matter to Dana, compared to other things Dana could spend the same day optimizing?
5. The case's original design (before this version) compared caching a bone's transform once per frame vs. redoing it every time it's read, and could never get the two options closer than 45% apart no matter which real numbers were plugged in. This version compares two entirely different, real, published techniques instead, and lands at 17.9%. What does that difference tell you about when "the numbers are lopsided" means the dilemma is genuinely one-sided, versus when it means you're comparing the wrong two things?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the twist
should be pressed to explain the move using D3's/D5's actual numbers, not just the twist's emotional
weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Matrix · Matrix Dimension · Determinant · Identity Matrix · How to add and multiply matrices · How
to find the determinant of a 2x2 matrix · How to solve a system of equations using a matrix

## Balance argument (SPEC §2)

**Argument for A (The Direct Blend).** Real, measured GPU cost of 0.32 ms per frame for a
comparably-rigged character mesh (S6) — the cheapest option, and the de facto industry-standard
technique. But a weighted SUM of the influencing bones' rigid-transform matrices is not itself
guaranteed to be a rigid transformation (S7); D3(b)'s hand-computed shoulder-blend-zone matrix
M_blend = 0.5·R1 + 0.5·R2 has determinant 0.5, not 1 — a real, provable instance of the documented
"candy-wrapper" collapse the graphics industry has known about for two decades.

**Argument for B (The Quaternion Blend).** Real, measured GPU cost of 0.39 ms per frame for the same
comparably-rigged mesh (S6) — 17.9% more than The Direct Blend — but it always produces a valid
rigid transformation, eliminating D3(b)'s determinant-collapse problem. Per the same real source, it
"works perfectly" at simple two-bone joints like the shoulder (S8). Its real, documented cost is not
on the compute metric: at more complex multi-bone joints elsewhere on the rig (the underarm, the
cape mount), the same fixed-rotation-center mechanism produces a different real, documented artifact
(S8) — so Option B is a different trade-off, not a strictly better fix.

**Margin — COMPUTED 2026-09-01 (balance redesign, superseding the case-research pass's 45.0%).**
`margin_pct: 17.9`. **Winner on the raw metric: Option A, The Direct Blend.** Per frame, for a
comparably-rigged mesh: Option A = 0.32 ms (S6), Option B = 0.39 ms (S6). margin_pct =
(0.39-0.32)/0.39 × 100 = 17.9%.

**This margin is UNDER SPEC §2's ~20% guideline, on real, measured, peer-reviewed data.** No retune
of Fenwick's own scenario numbers was needed or performed — margin_pct comes directly from S6, a
real published benchmark, not from Appendix A's bone count or mesh density (which no longer feed
the primary metric at all — see MA1/MA2's updated role in `case.json`). **Honesty disclosure (MA7):**
S6's benchmark mesh (5002 vertices, 54 joints, GeForce 6600 GT) differs in scale and hardware
generation from Fenwick's fictional mobile hero rig. This case uses S6's real measured *relative*
cost directly rather than fabricating a rescaling factor to "Fenwick's own phone" — flagged plainly
for `case-readiness` to confirm this treatment is acceptable (see RESEARCH_LOG.md).

**What this means for facilitation.** The case's genuine tension is a real, close numeric race
(17.9%) on real measured cost, SHARPENED by a genuine mathematical correctness question the numeric
race alone doesn't resolve: Option A is cheaper but D3(b) proves it produces an invalid transform at
the shoulder seam; Option B fixes that but (per the Twist) only at simple two-bone joints, not at
the rig's more complex blend zones. A room that only argues "17.9% is real but modest, ship A, it's
cheaper" has done the arithmetic but not engaged with D3(b)'s determinant finding or the Twist's
scope question. Full arithmetic trail: `case.json.balance.margin_note`.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine mobile game-engineering performance math — no subject-matter sensitivity flag
applies.
