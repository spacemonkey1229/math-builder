# RESEARCH_LOG.md — The Rig Budget

## REDESIGN PASS — balance retune, 2026-09-01

**Why this pass exists.** The original `case-research` pass (below, preserved for the audit trail)
computed `margin_pct = 45.0%` from a "compose once vs. apply per vertex" cost model (Option A / The
Composed Bind = 1 + V matrix multiplications per bone per frame; Option B / The Sequential Bind =
2V, where V = vertices skinned per bone). That model is well over SPEC §2's ~20% balance cap, and a
retune attempt (flexing V across Unity's entire real, cited mobile mesh-density range, S1/S2) only
moved the margin from 45.0% to 49.0%. The project owner reviewed this and explicitly declined an
MCS-46-style waiver, directing a redesign of the underlying dilemma/dataset instead of a numeric
patch. Full task brief: find a genuinely different, real, comparably-costed technique pair in the
same domain (game-rigging matrices), or a different real parameter regime, or (with care) a
reframed metric — not fudged numbers.

**Why the old model could never work, proven algebraically (kept from the original pass).**
margin(V) = (2V − (1+V)) / (2V) = (V−1)/(2V). This is bounded: it approaches 50% as V grows and only
falls toward 0% as V → 1 (a bone whose transform has essentially one downstream reader — composing
buys nothing over just applying once). No value of V inside Unity's real, cited mobile mesh-density
range (S1: <30 bones; S2: 300–1500 polygons — giving V ≈ 10 to 54) gets anywhere near ~20%. This is
a structural property of the "cache a fixed cost once, amortize it over V reads" shape itself, not
a modeling artifact fixable by picking different real numbers inside that shape. Any two-option
comparison of the form "1 fixed cost + V unit costs" vs. "2V unit costs" has the same problem for
any realistic V — so the fix had to replace the *shape* of the comparison, not just its inputs.

**What was tried, direction by direction (per the task brief's four suggested directions).**

1. **A different, real, comparably-costed technique pair (direction 1 — this is what worked).**
   Searched: "dual quaternion skinning vs linear blend skinning cost per vertex operations
   comparison" and "GPU Gems dual quaternion skinning vertex shader instruction count." Found and
   fetched the actual peer-reviewed source directly — Kavan, Collins, Žára, O'Sullivan, "Skinning
   with Dual Quaternions" (SI3D 2007) — via `curl` against
   `users.cs.utah.edu/~ladislav/kavan07skinning/kavan07skinning.pdf`, and read the full PDF text
   directly (not a WebFetch summary; every quoted figure below was confirmed against the actual
   paper text, including reading Figure 11's chart values). This paper reports **real, measured
   GPU runtimes** (Figure 11, GeForce 6600 GT column) for skinning a 5002-vertex, 54-joint
   character mesh under five different blending techniques: LBS (linear blend skinning) = 0.32 ms,
   DQB (direct quaternion blending, Hejl 2004) = 0.39 ms, Log-matrix blending = n/a on GPU, SBS
   (spherical blend skinning) = n/a on GPU, DLB (dual quaternion linear blending, this paper's own
   proposed method) = 0.46 ms.

   Computed margins directly from these real numbers: LBS vs. DLB (the paper's headline method) =
   (0.46−0.32)/0.46 = 30.4% — still over the ~20% guideline. **LBS vs. DQB (Hejl's earlier, simpler
   method) = (0.39−0.32)/0.39 = 17.9% — under the ~20% guideline, on real, directly-measured,
   peer-reviewed data.** This became the new Option A / Option B pair.

   This pair also turned out to fit the case's Matrices skill target *better* than the original
   pipeline framing: LBS's actual per-vertex operation, at a multi-bone blend zone, is a **weighted
   sum of matrices** — `v' = (Σ wᵢCⱼᵢ) v` — literally "how to add and multiply matrices" (scalar
   multiply each bone's matrix by its weight, then add), not just apply one precomposed matrix. And
   the paper's own Section 3.1 explains, in exact and citable terms, *why* this real technique has a
   real defect: "the blended matrix... is no longer a rigid transformation... the skin collapsing
   effects visualize the fact that the set of orthonormal matrices is not closed under addition."
   That is a real, published, hand-verifiable claim about a 2×2 rotation matrix's **determinant** —
   which let Challenge D3 be rebuilt to *prove* the real "candy-wrapper" artifact by hand (a
   two-bone, 50/50 blend of a 0° and a 90° rotation matrix has determinant 0.5, not 1), rather than
   just asserting it. This is a strictly stronger tie between the case's math and its dilemma than
   the original version had.

   Also found DQB's own real, documented limitation in the same source (Section 3.1): it fixes the
   blended transform's center of rotation, which "works perfectly" at simple two-bone joints (the
   source's own example: an elbow) but produces artifacts at more complex multi-bone joints (armpit,
   dorsum). This supplied a genuine, real, sourced qualitative counterweight to Option B's cost
   premium — Option B is not a strictly-better fix, it trades one real defect for a different real
   one — which is exactly the kind of two-sided tension SPEC's balance test wants.

2. **A different parameter regime for the original model (direction 2 — not pursued once direction
   1 succeeded).** Considered searching for real, sourced low vertices-per-bone use cases (simple
   prop rigs, accessory attachment points) that might bring V close to 1.5–2. Not pursued once
   direction 1 produced a clean, real, under-cap margin from a genuinely different technique pair —
   pursuing this in parallel risked ending up with an under-motivated, cherry-picked V just to hit a
   number, which is exactly what SPEC §2 warns against ("must be retuned by adjusting a constraint —
   not by hiding data").

3. **A reframed metric with an offsetting real cost for Option A (direction 3 — not needed).**
   Considered converting Option A's per-bone matrix write-back into a memory-bandwidth-equivalent
   operation count using real CPU/GPU cache-latency figures, to partially offset its raw
   multiplication-count advantage. Not pursued: direction 1's real, directly-measured GPU
   benchmark (S6) already gives an honest, real, apples-to-apples cost figure for both options
   without needing to construct a hand-built "operation-equivalent" conversion, which the task
   brief itself flagged as needing unusual care to stay non-hand-wavy.

4. **A different scope/constraint (direction 4 — not needed).** The task suggested comparing two
   mathematically distinct decompositions of the same transform, or a different asset-budget
   scenario. Not needed: direction 1 stayed inside the same rigging/matrices domain, the same
   protagonist and studio, and even *strengthened* (rather than replaced) the existing single-bone
   R/S/M/determinant/system-solve deliverables by adding a second, genuinely dilemma-relevant
   worked example (the shoulder blend-zone) alongside them, rather than discarding them.

**What changed, concretely.**
- **Old dilemma:** Compose-once-per-bone ("The Composed Bind") vs. never-cache-anything
  ("The Sequential Bind"), for every bone on the rig, with cost measured as a pure operation count
  derived from Fenwick's own (fictional) bone count and mesh density.
- **New dilemma:** At the rig's small number of real multi-bone blend zones (shoulder, underarm,
  cape mount), blend directly by summing weighted matrices ("The Direct Blend" / linear blend
  skinning) vs. blend via an intermediate quaternion representation ("The Quaternion Blend" / direct
  quaternion blending), with cost taken directly from a real, peer-reviewed, measured GPU benchmark
  (S6) of these two specific, real, industry-documented techniques.
- **Old margin:** 45.0%, structurally incapable of dropping under ~20% anywhere in the real cited
  mesh-density range (proven algebraically above).
- **New margin:** 17.9%, computed directly from real measured data (S6): margin_pct =
  (0.39 − 0.32) / 0.39 × 100 = 17.9%. Under SPEC §2's ~20% cap. No retuning of any Modeling
  Assumption was needed to get here — the margin comes from a real citation, not from adjusting a
  dial inside a fixed formula.
- **Honesty disclosure carried forward (MA7, `case.json`):** S6's benchmark mesh (5002 vertices, 54
  joints) and GPU (GeForce 6600 GT, a 2007-era desktop part) differ in scale and hardware generation
  from Fenwick's fictional mobile hero rig and target device. No real, published, mobile-specific
  head-to-head LBS-vs-DQB benchmark was found in this pass's research. This case uses S6's real
  measured *relative* cost (17.9%) directly, without fabricating a rescaling factor to "Fenwick's
  own phone" — the same treatment Appendix E already gives S5 (real precedent, not a Fenwick
  measurement). If a mobile-specific benchmark surfaces in a future pass, it should replace S6/MA7.

**Files touched in this pass:** `case.json` (primary_metric, options, margin_pct, sources S6–S8,
balance block, needs_source, modeling_assumptions, sensitivity_note, deliverables, appendices
titles), `case.md` (Overview, Background, Dilemma, Challenges, Appendices A–D, F, G, Modeling
Assumptions), `FACILITATOR.md`, `LEARNING_GOALS.md`, `sensitivity_model.py`. `status` remains
`"researched"` (not advanced to a readiness/published state) — a separate `case-readiness`/`case-qa`
pass should still run on this redesigned version. `reinforcement_note` is unchanged (its stale
coverage-count correction is unrelated to this balance redesign and this redesign does not change
any skill's coverage count).

---

## Original `case-research` pass, 2026-09-01 (superseded above; preserved for audit trail)

8 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`'s original version.
5 SOURCED, 3 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Recommended maximum bone count for a mobile character rig (Appendix A)

Searched: "Unity mobile skinned mesh recommended bone count character rig performance guidance."
`WebSearch` surfaced Unity's own manual pages, including a legacy version
(`docs.unity3d.com/560/...`). Fetched the current (6000.3) manual page first via `WebFetch` — it no
longer states a mobile-vs-desktop bone-count split. Fetched the legacy 5.6 manual page instead, and
independently confirmed the exact wording myself by `curl`-ing the raw HTML and stripping tags
(not just trusting the WebFetch tool's summary): "A bone hierarchy in a typical desktop game uses
somewhere between fifteen and sixty bones... You can achieve very good quality on desktop platforms
and fairly good quality on mobile platforms with about thirty bones. Ideally, keep the number below
thirty for mobile devices, and don't go too far above thirty for desktop games."

**Outcome: SOURCED, HIGH.** S1. Anchors MA1 = 28 bones (just under the real 30-bone mobile
ceiling).

## P02 — Recommended polygon/vertex density per mesh for a mobile character (Appendix A)

Same page as P01 (`docs.unity3d.com/560/Documentation/Manual/ModelingOptimizedCharacters.html`).
Confirmed directly via the same raw-HTML fetch: "For mobile devices, somewhere between 300 and 1500
polygons per mesh will give good results, whereas for desktop platforms the ideal range is about
1500 to 4000."

**Outcome: SOURCED, HIGH.** S2. Anchors MA2 = 300 polygons (the real low end of the cited mobile
range, chosen deliberately as the leaner end).

## P03 — Derived vertices-per-bone figure (Appendix A)

Not independently searched — this is arithmetic derived from P01/P02's own real cited figures
(MA2 ÷ MA1 = 300 ÷ 28 = 10.71...), plus one disclosed simplification: treating total mesh vertex
count as approximately equal to the polygon count in MA2, rather than deriving an exact
vertices-per-triangle ratio (which depends on the mesh's specific triangulation and was not
available to source for a fictional mesh). Rounded down to a whole number, 10, for clean arithmetic
in the student-facing tables; the unrounded value (10.71) is checked separately below (Modeling
Assumptions block, MA3) and confirmed not to change the margin meaningfully (45.0% vs. 45.3%).

**Outcome: ASSUMPTION (derived).** MA3 = 10 vertices/bone.

## P04 — Real published guidance on choosing a target frame rate for a mobile action game (Appendix A)

Searched: "mobile game target frame rate 30fps 60fps performance budget skinning matrix." Found and
fetched (via `curl`, confirmed against raw HTML) `dev.to/oceanviewgames/mobile-game-optimization-a-
unity-developers-checklist-dnk`, a real, dated (2026-02-07, per the page's `datetime` attribute)
article by a named studio (Ocean View Games). Confirmed the exact quote: "60fps - Required for
action games, competitive multiplayer, and any game where input responsiveness is critical...
30fps - Acceptable for turn-based strategy, puzzles, narrative games, and educational titles."

**Outcome: SOURCED, HIGH.** S4. Justifies MA4 = 60 fps, since Fenwick's game is stated as a
real-time action combat game (Background).

## P05 — Real published mobile frame-time budget in ms at 60 fps and 30 fps (Appendix A, Appendix F)

Searched the same result set as P04; found `gamedevcheatsheet.com/frame-budget`, also published by
Ocean View Games (same studio as S4). Fetched and confirmed via raw HTML (not just the WebFetch
tool's summary): "For 60fps mobile, you have about 16.6ms per frame total. Aim for a CPU budget of
8-10ms and a GPU budget of 8-10ms, with 2-3ms of headroom for thermal throttling and OS overhead.
For 30fps, double those numbers." No publication date is visible anywhere on the page (checked for
JSON-LD `datePublished`/`dateModified` — none found), so this source is graded MEDIUM rather than
HIGH despite being a real, named, directly-confirmed source.

**Outcome: SOURCED, MEDIUM.** S3. Used as context (Appendix F), not as a load-bearing figure in
Appendix D's own primary-metric arithmetic, which uses only bone count, vertices-per-bone, and
frame rate — not milliseconds.

## P06 — Stated in-scenario deadline, days from case launch to certification pass (Appendix A)

Framed by the placeholder text itself as "stated in-scenario," matching the Overview's "the
performance lab picks up the build at 9 AM" framing — not independently sourceable since Fenwick
Games is fictional. No search performed.

**Outcome: ASSUMPTION.** MA5 = 1 day. Decorative, not load-bearing.

## P07 — Stated in-scenario sample rotation and stretch matrices for the shoulder-bone keyframe (Appendix B)

Framed as "stated in-scenario," pure narrative/pedagogical flavor used only to give D1–D4 concrete
numbers to practice matrix mechanics on — not sourceable and not dilemma-relevant (does not appear
anywhere in `balance.margin_basis`). Chosen deliberately so R is an exact rotation matrix (a
3-4-5-triangle angle, cos=0.8, sin=0.6, giving det(R)=1 exactly) and S is a simple diagonal scale,
so the by-hand arithmetic in D2–D4 comes out to clean numbers Heroes can hand-check.

**Outcome: ASSUMPTION.** MA6 = R=[[0.8,-0.6],[0.6,0.8]], S=[[1.5,0],[0,0.5]].

## P08 — Real published worked example of CPU-side per-vertex skinning cost exceeding a frame budget (Appendix E)

Searched: "game engine optimization precompute cache combined transform matrix rotation scale
translation per frame skeletal animation performance," then more specifically for CPU skinning cost
benchmarks. Found `github.com/raduacg/game-mechanics-optimizations`. `WebFetch`'s summary of the
file looked plausible but, per this project's MCS-21 hard rule (verify actual content, not a
fetcher summary), fetched the raw file directly via `curl` against
`raw.githubusercontent.com/raduacg/game-mechanics-optimizations/main/53_gpu_skinning.md` and
confirmed the exact text myself: "Skinning 100 characters with 50 bones and 5000 vertices each on
CPU requires 25M vertex transformations per frame at 60fps = 1.5B transforms/sec. At 100
cycles/transform = 150B cycles = 60ms on a 2.5GHz CPU, exceeding 16.67ms budget by 3.6x." Also
confirmed via the GitHub API (`api.github.com/repos/raduacg/game-mechanics-optimizations`) that the
repository is real and dated (created 2025-11-15).

This is a personal collection of "171 game mechanics techniques, performance optimizations and
player experience tips" (per the repo's own description) rather than a peer-reviewed benchmark —
its cycle-count and clock-speed figures are stated as round, illustrative numbers within the source
itself, not independently measured. Used only as documented precedent (Appendix E, real worked
example of the general cost shape this case's own arithmetic produces), not as a load-bearing
figure anywhere in Appendix D's own operation-count computation.

**Outcome: SOURCED, MEDIUM.** S5.

## Attempted but not used — real citation for "compose once vs. reapply every time"

Searched: "game engine optimization precompute cache combined transform matrix... skeletal
animation performance." Found and fetched (via `r.jina.ai` proxy, after a direct fetch returned
HTTP 403) a GameDev.net article, "Skeletal Animation Optimization Tips and Tricks." Confirmed
directly that this article does **not** discuss combining rotation/scale/translation into one
matrix as an optimization, nor quantify matrix-multiplication cost per bone — its optimizations are
about keyframe data reduction, SIMD for LERP/SLERP, multithreading, and LOD, a different topic.

**Outcome: not used, no substitute needed.** The concept sheet's own "Data feasibility" note states
this core engineering fact "needs no external citation — it's a computation the case derives
directly" (same as the recursion-vs-iteration cost model in `prove-it-scales`), so no citation was
required for it in the first place; this search was a genuine attempt at additional real-world
grounding beyond what the concept sheet asked for, and it came up empty. Logged here so a future
pass doesn't waste time re-discovering the same dead end.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none (lowest grade used is MEDIUM: S3, S5)
needs_source OPEN remaining: 0
```

## Margin (facilitator-only — computed here, not written into case.md)

Per bone, per frame (Appendix D): Option A (The Composed Bind) = 1 (compose R·S) + 10 (apply, one
per skinned vertex at MA3's 10 vertices/bone) = **11** matrix multiplications. Option B (The
Sequential Bind) = 10 × 2 (rotate then stretch, applied fresh per skinned vertex) = **20**.
**margin_pct = (20-11)/20 × 100 = 45.0%. Winner on the raw metric: Option A.**

This is well past the ~20% guideline and is reported plainly, not softened, per instruction. A
retune pass was attempted: flexed MA2 (mesh polygon count) across its *entire* real, cited range
(S2: 300 to 1500 polygons) while holding MA1 (bone count) at its real cited ceiling (28-30 bones,
S1). At the stated low end (300 polys / 28 bones ≈ 10 verts/bone): margin = 45.0%. At the high end
(1500 polys / 28 bones ≈ 53.6 verts/bone): Option A = 1+53.6 = 54.6, Option B = 2×53.6 = 107.1,
margin = (107.1-54.6)/107.1 = 49.0%. So across the *entire* real, sourced range for mobile mesh
density, margin_pct only moves between 45.0% and 49.0% — it never gets close to SPEC §2's ~20%
guideline.

This is structural, not a modeling artifact: writing margin as a function of V = vertices/bone,
margin(V) = (V−1)/(2V), which trends toward 50% as V grows and only falls toward 0% as V → 1 (a
bone whose transform is read by essentially one downstream consumer). No value of V inside Unity's
real, cited mobile mesh-density range (S1, S2) brings the margin under ~20%; only an unrealistically
sparse rig (V ≈ 1.5–2) would, and asserting that would contradict the real cited guidance rather
than respect it, so it was not done.

**This is flagged as an open balance concern for case-readiness — it is not resolved by the retune
attempted above, and this session did NOT self-grant an MCS-46-style waiver.** Per this project's
own process, that requires actual project-owner sign-off, which was not sought in this
case-research pass. The case's real, disclosed qualitative counterweight — Option B's
no-caching/no-staleness safety property, and its lower authoring/debugging burden for a small
studio's single rigger — is written into `case.json.balance.argument_b` and `FACILITATOR.md`, and
the Twist (a bone with only 1 downstream vertex, where the margin collapses to 0%) is built to
surface that the aggregate 45.0% figure is not uniform across the rig — but neither of those
resolves the raw-metric margin itself. Flagging plainly for the next `case-readiness` stage to
adjudicate.

## SPEC §2 self-check (ORIGINAL PASS — superseded, see REDESIGN PASS at top of file)

- Balance test: **FLAGGED** at the time — margin_pct = 45.0%, over the ~20% guideline, confirmed
  structural via a genuine retune attempt across the entire real cited range for the one lever that
  mattered (mesh density). This flag is what triggered the 2026-09-01 REDESIGN PASS documented at
  the top of this file. See the new self-check immediately below for the current, post-redesign
  state.

---

## SPEC §2 self-check — POST-REDESIGN (current)

- Primary metric exists and is directly computable: yes — real, measured GPU skin-deformation cost
  per frame, taken directly from a peer-reviewed source (S6, Appendix D), not derived from
  Fenwick's own scenario numbers.
- No structurally-zero-cost option: correct — Option B (The Quaternion Blend) is not free; it costs
  17.9% more on the real measured metric. Option A (The Direct Blend) is not free either — it is
  real, measured, cheaper, and is mathematically provable (by hand, D3(b)) to produce an invalid
  rigid transform at the shoulder blend-zone (det(M_blend) = 0.5, not 1), a real, documented defect
  (S7).
- Dilemma is not a foregone conclusion: Option B has a real, sourced, qualitative advantage
  (always-valid rigid transform, S8) that the raw ms metric does not capture on its own, AND a real,
  sourced limitation of its own at more complex blend zones (S8) — so "ship the always-correct one"
  is not automatically right either. This is a genuine two-sided tension grounded entirely in real,
  peer-reviewed sources, not an invented trade-off.
- Balance test: **PASSES.** margin_pct = 17.9%, computed directly from real, measured, peer-reviewed
  data (S6) — under SPEC §2's ~20% guideline. No waiver needed, and none was sought. Full arithmetic:
  `case.json.balance.margin_note`.
- Honesty disclosure carried into `case.json` (MA7): S6's benchmark used a differently-scaled,
  2007-era desktop test rig, not Fenwick's own mobile hardware. The 17.9% figure is used as a real,
  sourced relative-cost measurement — the best available real data for this specific technique
  pair — not as a literal claim about Fenwick's own device. Flagged for `case-readiness` to confirm
  this treatment is acceptable, and for a future pass to replace S6/MA7 if a mobile-specific
  LBS-vs-DQB benchmark is ever found.

## Next step

Run `case-qa` on `the-rig-budget`'s redesigned version. Confirm the balance test now passes cleanly
on real numbers (margin_pct 17.9%, S6/S7/S8) and confirm MA7's benchmark-scale disclosure is an
acceptable honesty trade-off, not a hidden weakness. Also still flag `LEARNING_GOALS.md`'s note and
`case.json.reinforcement_note` for the concept-log maintainer (unrelated to this balance redesign,
still open): the concept sheet's C3 write-up states this case "thickens the entire Matrices group
from n=1 to n=2," but `readmodel/standards_spine.json` already showed `n=2` for the whole group at
authoring time (covered by The Multiplier Recruit and The Skin Pack Atlas) — this case actually
thickens it to `n=3`.
