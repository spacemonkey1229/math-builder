Case Study: The Rig Budget
MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Two browser tabs, one laptop, one deadline. Dana Ruiz has the hero character's rig open in both.

The performance lab picks up the build at 9 AM — the studio's one certified test bench, a mid-tier
phone bolted to a rig that logs every dropped frame and won't let a submission through if the hero
character stutters during combat. Dana has been staring at the same skeleton for forty minutes,
and one seam in particular: the shoulder, where the upper-arm bone and the torso bone both pull on
the same handful of vertices at once. Everywhere else on the rig, one bone controls one patch of
mesh, clean and simple. At the shoulder — and the underarm, and the cape's mounting point — two or
more bones share the vertices, and *how* their transforms get blended together is a real choice
with a real cost.

Branch one blends directly. It takes each of the two bones' transform matrices, multiplies each by
how much influence it has on that vertex, and adds the two weighted matrices together — one sum,
applied once. Branch two blends differently: it converts each bone's rotation to a different kind
of number first, blends *those*, and only converts back to a matrix at the very end. Dana's already
written the sticky note for the art director: *works with either branch, no model changes either
way.* That part's settled.

What isn't settled is which branch survives contact with a phone slower than Dana's laptop — and
whether the cheaper branch is actually safe to ship, because Dana has a nagging memory of a
"candy-wrapper" bug from a previous job, right at a seam exactly like this one. Dana pulls up a
blank sheet, sketches two rotation matrices — R1 and R2 — and starts adding.

---

## Background

Dana Ruiz is a Technical Artist / Rigger at Fenwick Games, a small mobile-game studio building an
action combat game for phones. Dana owns the transform pipeline for the hero character's skeletal
rig — the system that takes each bone's rotation for the current animation frame and turns it into
the numbers that actually move the character's mesh on screen (SEE APPENDIX A). Most of the rig is
simple: one bone, one patch of mesh, one straightforward matrix multiplication, unaffected by
today's decision (SEE APPENDIX B, the elbow-bone example in D1/D2). But at a handful of **blend
zones** — the shoulder, the underarm, the cape's mounting point — two or more bones share
influence over the same vertices, and the two working pipelines below disagree about how to
combine them:

**The Direct Blend** (linear blend skinning) takes each influencing bone's transform matrix,
multiplies it by that bone's weight, and adds the weighted matrices together directly — one
combined matrix, applied once per shared vertex. It is the fastest option, real-world measured, and
it is the de facto industry-standard technique (SEE APPENDIX B). But a straight sum of two rotation
matrices is not itself guaranteed to be a valid rigid rotation — real, published graphics research
explains exactly why, and this case's own Challenge D3 proves it by hand for Fenwick's own shoulder
seam.

**The Quaternion Blend** (direct quaternion blending) converts each influencing bone's rotation to
a quaternion first, blends the quaternions instead of the raw matrices, and only converts the
result back into a matrix at the end, before applying it to the vertex. Real, measured GPU cost:
higher than The Direct Blend's, by an amount Appendix D's raw figures let you work out yourself.
Real, published upside: it always produces a valid rigid transformation. Real, published downside:
it has its own documented failure mode at more complex blend zones (SEE APPENDIX C).

Neither pipeline changes what bones exist or how the rig is authored — both are drop-in choices for
how the engine blends shared vertices at the same handful of seams (SEE APPENDIX B and APPENDIX C).
What they do not share is measured GPU compute cost, or how each one behaves mathematically at a
seam like the shoulder (SEE APPENDIX D). Fenwick's hero rig, its target frame rate, and its frame
budget are all sized to real, published mobile-game guidance; the two blending techniques' relative
cost and behavior are sized to real, published, peer-reviewed graphics research, not to Fenwick's
own (fictional) numbers (SEE APPENDIX A, APPENDIX D, and APPENDIX F). A real, documented example
also exists of the more general kind of per-vertex transform cost this case is built on, blowing
well past a studio's frame budget once it is computed honestly instead of estimated by feel (SEE
APPENDIX E). Every sourced and assumed figure in this case is listed in **APPENDIX G**, and the
vocabulary and "how to…" skills this case will ask of you are listed in **APPENDIX H** — that is
where Challenge 1 sends you.

---

## Dilemma

You are Dana Ruiz.

Do you:

**A.)** Ship **The Direct Blend** — blend a shared vertex's transform by directly summing the influencing bones' weighted matrices, applied once **OR**

**B.)** Ship **The Quaternion Blend** — blend a shared vertex's transform by converting each influencing bone's rotation to a quaternion, blending those, and converting back to a matrix before applying it

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — The rotation matrix R and the stretch (scale) matrix S for the hero's elbow bone at the
sample animation keyframe (SEE APPENDIX B).** The elbow is a single-bone segment, unaffected by
today's decision. Write both as explicit 2×2 matrices, and state each matrix's dimensions.
- **D2 — Two combined matrices, computed by hand.** (a) The elbow bone's M = R·S, with every entry
shown as an arithmetic step of 2×2 matrix multiplication. (b) The shoulder blend-zone's
M_blend = w1·R1 + w2·R2, with every entry shown as an arithmetic step of scalar matrix
multiplication and matrix addition (SEE APPENDIX B).
- **D3 — Two determinants, computed by hand using the 2×2 determinant formula.** (a) The elbow
bone's det(M), compared to the identity matrix I's determinant. (b) The shoulder blend-zone's
det(M_blend), also compared to I. Explain in two or three sentences what M_blend's determinant
reveals about The Direct Blend's real, documented visual defect at that seam — and why the elbow
bone's own M does not have the same problem.
- **D4 — Recover M_blend by solving a system of equations.** Given two known point-mappings the
engine logged under M_blend (SEE APPENDIX B), set up and solve the resulting system of linear
equations using matrix methods to find M_blend's four entries, and confirm your answer matches
D2(b)/D3(b).
- **D5 — The Skin-Blend Cost & Determinant Table and recommendation memo.** Using Appendix D's real
measured GPU cost figures (ms per frame) for The Direct Blend and The Quaternion Blend, plus your
own D3(b) determinant finding, build a table comparing: measured cost, % of Fenwick's real frame
budget consumed, and whether each option is mathematically guaranteed to avoid the shoulder seam's
collapse artifact. State which pipeline Dana should recommend, defended with your D2–D4 work and
Appendix D's numbers.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Fenwick Games' Hero Rig & Device Performance Constraints

| Quantity | Value |
|---|---|
| Studio | Fenwick Games (fictional small mobile-game studio) |
| Game genre | Action combat, real-time, phone-only |
| Hero rig bone count | 28 bones [MA1] — context; no longer feeds margin_pct (see Appendix D) |
| Hero mesh polygon count (both pipelines use the identical mesh) | 300 polygons [MA2] — context; no longer feeds margin_pct |
| Number of real multi-bone blend zones on the hero rig | 3 (shoulder, underarm, cape mounting point) — stated in-scenario |
| Target frame rate | 60 frames per second [MA3] |
| Frame time budget at 60 fps | 16.6 ms per frame [S3] |
| Days from case launch to the certification pass | 1 day [MA4] |
| Does either pipeline require reworking the hero model or rig? | No — both pipelines are drop-in choices for how the engine blends shared vertices at the same blend zones (SEE APPENDIX B, APPENDIX C) |

*Note: Fenwick Games is a scenario construction for this case — there is no real studio by this
name.*

---

## Appendix B: Option A — The Direct Blend (Linear Blend Skinning)

| Spec | Value |
|---|---|
| Single-bone sample used in D1–D3(a) | Hero's elbow bone (one bone, no blending — unaffected by today's decision), at one stated animation keyframe |
| Elbow bone's rotation matrix R at this keyframe | $R = \begin{bmatrix} 0.8 & -0.6 \\ 0.6 & 0.8 \end{bmatrix}$ (a 36.87° rotation — cos = 0.8, sin = 0.6) [MA5] |
| Elbow bone's stretch (scale) matrix S at this keyframe | $S = \begin{bmatrix} 1.5 & 0 \\ 0 & 0.5 \end{bmatrix}$ (stretched 1.5× along the bone's long axis, squashed to 0.5× across it) [MA5] |
| Blend-zone sample used in D2(b)–D4 | Hero's shoulder blend-zone, one shared vertex influenced by two bones, at the same keyframe |
| Bone 1's rotation matrix R1 (upper-arm bone, at rest) | $R_1 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ (0°, the identity — no rotation) [MA6] |
| Bone 2's rotation matrix R2 (torso/shoulder-blade bone) | $R_2 = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ (a 90° rotation) [MA6] |
| Blend weights at the shared vertex | w1 = 0.5, w2 = 0.5 — equal influence, the simplest defensible choice for a vertex sitting midway on the seam [MA6] |
| The Direct Blend's rule | $M_{blend} = w_1 R_1 + w_2 R_2$ — sum the *weighted* matrices directly, once, then apply to the vertex |
| Two known point-mappings under M_blend, for D4 | v1 = (1, 1) maps to w1_pt = (0, 1); v2 = (2, −1) maps to w2_pt = (1.5, 0.5) |
| Why a directly-summed blend matrix can distort the mesh | "The blended matrix (sum of the weighted bone matrices) is no longer a rigid transformation, but a general affine one (potentially containing scale and shear factors)... the skin collapsing effects visualize the fact that the set of orthonormal matrices is not closed under addition." [S7] |
| Real measured GPU cost (comparable rigged mesh) | **0.32 ms per frame** [S6] |

---

## Appendix C: Option B — The Quaternion Blend (Direct Quaternion Blending)

| Spec | Value |
|---|---|
| The Quaternion Blend's rule | Convert each influencing bone's rotation to a quaternion, blend the quaternions (not the raw matrices), then convert the blended result back into a matrix and apply it to the vertex once |
| Real, published guarantee this technique provides | Always produces a mathematically valid rigid transformation — the collapse mechanism in Appendix B (S7) cannot occur |
| Real, documented limitation | "This is the principle of [Hejl 2004]: the vertices rotate around the nearest joint. In cases similar to that of the elbow (two bones connected by a joint), this works perfectly. However, for more complex joint influences, such as those usually occurring around the armpit or dorsum, artifacts result from the fact that the center of rotation is fixed and does not adapt to the actual posture." [S8] |
| Does the shoulder blend-zone (D1–D4's sample, a simple two-bone joint) fall into the "works perfectly" case or the "artifacts" case, per S8? | "Works perfectly," per the source's own two-bone-joint example — but the underarm and cape mounting point are more complex, multi-bone regions where the same source's documented limitation applies |
| Real measured GPU cost (comparable rigged mesh) | **0.39 ms per frame** [S6] |

---

## Appendix D: Skin-Blend Cost & Determinant Model

**Real, measured GPU cost per frame** (S6, Figure 11, GeForce 6600 GT, a 5002-vertex/54-joint
comparably-rigged character mesh — the best available real, published head-to-head measurement of
these two specific techniques; see Modeling Assumption MA7 for why this is not rescaled to
Fenwick's own mobile hardware):

| | The Direct Blend (A) | The Quaternion Blend (B) |
|---|---|---|
| Measured GPU cost, per frame | **0.32 ms** | **0.39 ms** |
| Fenwick's real frame budget [S3] | 16.6 ms/frame | 16.6 ms/frame |
| Mathematically guaranteed to avoid the shoulder seam's collapse artifact (D3(b))? | **No** — det(M_blend) = 0.5, not 1 | **Yes** — always produces a valid rigid transform |
| Real documented limitation elsewhere on the rig | "Candy-wrapper" collapse at any blend zone (S7) | Fixed-rotation-center distortion at complex multi-bone zones like the underarm (S8) |

*These figures are real, measured, and sourced (S6) — not derived from Appendix A's bone count or
mesh density, unlike the case's original (2026-09-01 case-research) version. D5 asks you to combine
this table's raw per-frame costs with Appendix F's frame budget yourself — work the percentages and
the relative-cost comparison out; they are not given here. See the Modeling Assumptions block for
the full retune history and for MA7's honest disclosure about the benchmark mesh's scale.*

---

## Appendix E: Documented Precedent — CPU Skinning Cost at Scale

| Item | Value |
|---|---|
| A real, published worked example showing CPU-side per-vertex transform cost blowing past a stated 60 fps frame budget | "Skinning 100 characters with 50 bones and 5000 vertices each on CPU requires 25M vertex transformations per frame at 60fps = 1.5B transforms/sec. At 100 cycles/transform = 150B cycles = 60ms on a 2.5GHz CPU, exceeding 16.67ms budget by 3.6x." [S5] |
| What fixes it, per the same source | Moving the per-vertex transform work to the GPU: "reducing 60ms CPU work to <1ms GPU work" [S5] |

*This appendix documents a real, external, worked example of the same kind of cost this case's
Appendix D computes — per-vertex matrix transform work multiplying out to a real budget problem
once bone count and mesh density are both large enough. It is cited as industry precedent for why
this arithmetic matters, not as a Fenwick Games measurement — Fenwick's own hero rig (Appendix A)
is far smaller than the 100-character, 50-bone-each example in this source.*

---

## Modeling Assumptions

> These figures are **not sourced** from Fenwick Games (a fictional studio) or, in most cases,
> from any external record at all. They are stated scenario assumptions chosen by the case
> author, in several cases anchored to real published mobile-rigging guidance. A Hero may
> challenge any of them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Hero rig bone count (Appendix A) | 28 bones | Anchored to Unity's real, published guidance: "Ideally, keep the number below thirty for mobile devices" [S1]. 28 sits just under that real ceiling. Context only — see below. | No longer feeds margin_pct (which now comes directly from S6's real measured comparison, Appendix D). Retained for rig-scale context only. |
| MA2 | Hero mesh polygon count (Appendix A) | 300 polygons | Anchored to the real, published low end of Unity's mobile mesh-density guidance: "somewhere between 300 and 1500 polygons per mesh will give good results" for mobile devices [S2]. Context only — see below. | No longer feeds margin_pct. Retained for rig-scale context only. |
| MA3 | Target frame rate (Appendix A) | 60 fps | Fenwick's game is a real-time action combat game; real, published guidance states 60 fps is "required for action games, competitive multiplayer, and any game where input responsiveness is critical" [S4]. | Used only to frame Appendix D's "share of frame budget" row against the real 16.6ms/frame budget (S3) — does not change margin_pct. |
| MA4 | Days from case launch to certification pass | 1 day | Matches the Overview's "the performance lab picks up the build at 9 AM" framing. | None — flavor only, not load-bearing. |
| MA5 | The elbow bone's R and S matrices at the stated keyframe (Appendix B) | R = [[0.8,−0.6],[0.6,0.8]], S = [[1.5,0],[0,0.5]] | Illustrative — chosen so R is an exact rotation matrix (det = 1, a 3-4-5-triangle angle for clean arithmetic) and S is a simple diagonal stretch. Not meant to represent Fenwick's actual animation data (which does not exist, since Fenwick is fictional). The elbow is a single-bone segment, unaffected by today's blend-technique decision. | None for the primary metric — D1–D3(a) use these numbers only to practice ordinary single-bone matrix mechanics. |
| MA6 | The shoulder blend-zone's R1, R2, and blend weights (Appendix B) | R1 = [[1,0],[0,1]], R2 = [[0,−1],[1,0]], w1 = w2 = 0.5 | Illustrative — chosen so R1 = identity keeps the by-hand blend-sum simple to check entry-by-entry, while still being a genuine instance of S7's documented mechanism (a weighted sum of two real rotation matrices need not itself be rigid). Equal weighting is the simplest defensible choice for a vertex on the seam midway between two bones. Not sourced (Fenwick's animation data does not exist) — a clearly-labeled scenario premise. | This IS load-bearing for D2(b)/D3(b)'s determinant demonstration (det(M_blend) = 0.5, not 1) — but does not feed Appendix D's real measured cost comparison, which comes directly from S6 regardless of which specific weights/angles this worked example uses. |
| MA7 | Treating S6's real measured per-frame costs for the two techniques as representative of Fenwick's own mobile pipeline choice | Appendix D's raw 0.32 ms / 0.39 ms figures, used directly, not independently rescaled | S6's benchmark used a 5002-vertex, 54-joint mesh on a 2007-era desktop GPU (GeForce 6600 GT) — a different scale and hardware generation than Fenwick's fictional mobile hero rig. No real, published, mobile-specific LBS-vs-DQB benchmark was found during this case's research (see RESEARCH_LOG.md). Rather than fabricate a rescaling factor, this case uses S6's real measured costs directly, the same way Appendix E already uses S5 as documented precedent rather than a Fenwick-specific measurement. | This is the redesign's central honesty disclosure — Appendix D's costs are real and sourced as "the best available real, published, head-to-head measurement of these two techniques," not a literal claim about Fenwick's own phone. |

**Retune history (SPEC §2).** The case's original (2026-09-01 case-research) version computed
its primary metric from bone count and mesh density (a "compose once vs. apply per vertex" model),
structurally incapable of landing inside SPEC §2's guideline anywhere in Unity's real cited mobile
mesh-density range (S1, S2) — see `RESEARCH_LOG.md` for the full history and the algebraic proof of
why. This version replaces that model entirely with a different, real, published technique pair
(S6/S7/S8), with no retuning of Fenwick's own scenario figures required. Work D5's own table to see
where the two techniques actually land.

---

## Appendix F: How the Frame Budget Applies

| Quantity | Value |
|---|---|
| Frame time budget at 60 fps | 16.6 ms per frame [S3] |
| Frame time budget at 30 fps, for comparison | "For 30fps, double those numbers" [S3] — about 33 ms per frame |
| Recommended CPU budget slice, of the 16.6 ms total at 60 fps | 8–10 ms [S3] |
| The Direct Blend's measured cost, as a share of the 16.6 ms budget | 0.32 / 16.6 ≈ 1.9% [S6, S3] |
| The Quaternion Blend's measured cost, as a share of the 16.6 ms budget | 0.39 / 16.6 ≈ 2.4% [S6, S3] |

*Unlike the case's original version, Appendix D now computes real measured milliseconds directly
(S6), so this appendix's frame-budget context plugs in directly — no CPU-cycle-cost conversion is
needed. Appendix E's real worked example shows the more general kind of per-vertex transform
arithmetic that genuinely can blow a real 60 fps budget once bone count and mesh density are large
enough; this specific blend-zone decision, by contrast, only ever costs a few percent of the
budget either way — a real, disclosed reason the margin here is a "which costs less, by how much"
question rather than a "does it fit" one.*

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Recommended maximum bone count for a mobile character rig | "Ideally, keep the number below thirty for mobile devices, and don't go too far above thirty for desktop games." | Unity Technologies — ["Modeling characters for optimal performance"](https://docs.unity3d.com/560/Documentation/Manual/ModelingOptimizedCharacters.html), Unity 5.6 Manual | Legacy manual, accessed 2026-09-01 | HIGH — primary vendor documentation, exact quote confirmed directly from the page's raw HTML |
| S2 | Recommended polygon count per mesh for a mobile character | "For mobile devices, somewhere between 300 and 1500 polygons per mesh will give good results, whereas for desktop platforms the ideal range is about 1500 to 4000." | Unity Technologies — ["Modeling characters for optimal performance"](https://docs.unity3d.com/560/Documentation/Manual/ModelingOptimizedCharacters.html), Unity 5.6 Manual | Legacy manual, accessed 2026-09-01 | HIGH — same page as S1, exact quote confirmed directly from the page's raw HTML |
| S3 | Frame time budget at 60 fps and 30 fps for mobile games | "For 60fps mobile, you have about 16.6ms per frame total. Aim for a CPU budget of 8-10ms and a GPU budget of 8-10ms, with 2-3ms of headroom for thermal throttling and OS overhead. For 30fps, double those numbers." | Ocean View Games — ["Frame Budget Calculator for Unity Game Development"](https://gamedevcheatsheet.com/frame-budget) | Undated page, accessed 2026-09-01 | MEDIUM — real, named studio's published guidance page, exact quote confirmed directly, but the page carries no visible publication date |
| S4 | Which target frame rate real published guidance recommends for an action mobile game | "60fps - Required for action games, competitive multiplayer, and any game where input responsiveness is critical. Demands aggressive optimization across all systems. 30fps - Acceptable for turn-based strategy, puzzles, narrative games, and educational titles." | Ocean View Games — ["Mobile Game Optimization: A Unity Developer's Checklist"](https://dev.to/oceanviewgames/mobile-game-optimization-a-unity-developers-checklist-dnk) | 2026-02-07 | HIGH — real, named studio's published article, exact quote confirmed directly, dated |
| S5 | A real, published worked example of CPU-side per-vertex transform (skinning) cost exceeding a 60 fps frame budget | "Skinning 100 characters with 50 bones and 5000 vertices each on CPU requires 25M vertex transformations per frame at 60fps = 1.5B transforms/sec. At 100 cycles/transform = 150B cycles = 60ms on a 2.5GHz CPU, exceeding 16.67ms budget by 3.6x." | raduacg — ["53. GPU Skinning (Skeletal Animation)"](https://github.com/raduacg/game-mechanics-optimizations/blob/main/53_gpu_skinning.md), *game-mechanics-optimizations* (GitHub) | Repository created 2025-11-15, accessed 2026-09-01 | MEDIUM — real, dated, fetched-and-confirmed repository, but a personal collection of technique notes rather than a peer-reviewed benchmark; its 100 cycles/transform and 2.5 GHz figures are stated as round illustrative numbers within the source itself, not independently measured. Used only as documented precedent (Appendix E), not as a load-bearing figure in Appendix D's own arithmetic. |
| S6 | Real, published, head-to-head measured GPU runtime cost of linear blend skinning (LBS) vs. direct quaternion blending (DQB), on a comparably-rigged character mesh | Figure 11 (GeForce 6600 GT column): LBS = 0.32 ms, DQB = 0.39 ms, DLB (dual quaternion) = 0.46 ms, for a 5002-vertex, 54-joint model. | Kavan, Collins, Žára, O'Sullivan (Trinity College Dublin / Czech Technical University in Prague) — ["Skinning with Dual Quaternions"](https://users.cs.utah.edu/~ladislav/kavan07skinning/kavan07skinning.pdf), SI3D 2007 | Published 2007, accessed 2026-09-01 | HIGH — peer-reviewed published paper, full PDF fetched and Figure 11's exact reported values confirmed directly, not a search snippet |
| S7 | Real, published mathematical explanation of why linear blend skinning's per-vertex blended matrix can fail to be a valid rigid transformation | "The blended matrix (sum of the weighted bone matrices) is no longer a rigid transformation, but a general affine one (potentially containing scale and shear factors)... the skin collapsing effects visualize the fact that the set of orthonormal matrices is not closed under addition." | Kavan et al. — same paper as S6, Section 3.1 | Published 2007, accessed 2026-09-01 | HIGH — same paper, same direct full-text confirmation |
| S8 | Real, published, documented limitation of direct quaternion blending (fixed rotation center) | "In cases similar to that of the elbow (two bones connected by a joint), this works perfectly. However, for more complex joint influences, such as those usually occurring around the armpit or dorsum, artifacts result from the fact that the center of rotation is fixed and does not adapt to the actual posture." | Kavan et al. — same paper as S6, Section 3.1 | Published 2007, accessed 2026-09-01 | HIGH — same paper, same direct full-text confirmation |

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Matrix
- Matrix Dimension
- Determinant
- Identity Matrix

**"How to…" questions**

- How to add and multiply matrices
- How to find the determinant of a 2x2 matrix
- How to solve a system of equations using a matrix

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
