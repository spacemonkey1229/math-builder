Case Study: The Culling Volume
MS | Math | Case Study | 2026 | Adventure

## Overview

Marisol Tan has the frame-budget spreadsheet open on one monitor and a wireframe view of the open world — the scene drawn as bare outline edges only, nothing filled in — on the other. Friday's review meeting has one job for her team: cut milliseconds off the frame, or the next content patch — a district full of new streets, pipework, and signage — doesn't ship. Her culling system, the code that decides which of the world's thousands of background props even get considered for drawing each frame, is at the top of the offenders list.

She drags a lamppost mesh into the profiler and watches its bounding shape balloon around it — a single sphere, fat enough to swallow the pole, the fixture, and about a swimming pool's worth of empty air besides. Every one of the thin, tall props scattered across the map gets the same treatment: one cheap number, one enormous sphere, and an object that stays "possibly visible" to the engine long after the camera has actually looked away.

The fix sitting in her branch replaces that sphere with a tighter-fitting capsule for exactly this class of object — poles, pipes, posts, anything long and thin. It fits close. It also costs more math, every single one of thousands of times a frame. Marisol pulls up both numbers side by side, cursor hovering between the two candidate builds, the review meeting nineteen minutes away.

## Background

Marisol Tan is a rendering/engine programmer responsible for occlusion culling on an open-world game currently mid-way through a content patch. A game's picture is drawn by two different processors working together: the CPU (the general-purpose processor that runs the game's logic, including the culling test itself) decides what to draw, and the GPU — the graphics processing unit, a processor built specifically for the massively parallel math of turning 3-D geometry into an on-screen picture — actually draws it. Culling is the process that decides, every frame, which of the world's objects are worth asking the GPU to draw at all — an object judged "not possibly visible" this frame is skipped entirely, saving real time (SEE APPENDIX A). Real game engines run this test using a simplified stand-in shape for each object rather than its actual mesh, because testing thousands of full meshes every frame is far too slow (SEE APPENDIX A).

Right now, every prop in the world — no matter its shape — is tested against the camera using a single bounding sphere, sized just large enough to fully contain the object. For a compact prop this fits reasonably well. For a long, thin prop — a lamppost, a length of pipe, a sign post — a sphere sized to reach the object's farthest tip is enormous relative to the object's real volume, which means the object keeps testing as "possibly visible" long after it has actually left the camera's view. Every object still marked "possibly visible" costs the GPU a draw call — one request, with all its texture and shader information attached, to actually render that object's geometry — plus the shading work (the per-pixel color/lighting math) that draw call triggers; wasting both on something the player can no longer see is exactly what a tighter-fitting bounding shape avoids (SEE APPENDIX B). The fix under review swaps the bounding shape for exactly this class of long, thin prop from a sphere to a capsule — a cylinder capped with two hemispheres — which hugs a long thin object far more tightly, at the cost of a more expensive per-object math check every single frame (SEE APPENDIX A, APPENDIX B).

Three representative prop types carry this decision: a lamppost, a length of industrial pipe, and a sign post with a pyramidal cap, each built from real or realistically-bounded dimensions (SEE APPENDIX B). The world places many copies of each across the map every frame (SEE APPENDIX C), and both the culling-test cost and the cost of wasted, needlessly-considered-visible volume are priced in Appendix D. Marisol has to recommend one bounding-shape policy for this entire class of prop before the review starts. Real engines — Unreal Engine among them — document using exactly this kind of simplified bounding geometry, sphere or otherwise, to decide visibility every frame (SEE APPENDIX E). Every sourced or assumed figure in this case is documented in (SEE APPENDIX E), and the vocabulary and "how to…" procedures needed to build and compare both options are listed in (SEE APPENDIX F).

## Dilemma

You are Marisol Tan.
Do you:
A.) Keep a single bounding sphere for every long, thin prop — one cheap distance check, a lot of wasted volume OR
B.) Switch long, thin props to a bounding capsule — a tighter fit, at a higher per-object compute cost

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. For each of the three representative props (Appendix B), a complete volume AND surface
    area calculation of the prop's real shape, decomposed into its component solids (a cylinder
    plus a cone, or a cylinder plus a square pyramid), shown step by step.
    D2. For each prop, the bounding sphere's volume (Option A — radius equal to half the prop's
    total height) and the "wasted" volume (sphere volume minus the prop's real volume from D1),
    per prop and as a scene-wide total using Appendix C's prop counts.
    D3. For each prop, the bounding capsule's volume (Option B — a cylinder spanning the prop's
    full height at the prop's own widest radius, capped by two hemispheres) and its wasted volume,
    per prop and as a scene-wide total.
    D4. Using Appendix D's cost figures, each option's total added per-frame cost in
    milliseconds — the culling-test cost across every tested prop, plus the wasted-volume
    render/overdraw cost — shown step by step for both options, with the margin between them.
    D5. A one-paragraph written recommendation naming which bounding-shape policy has the lower
    total per-frame cost, and explicitly addressing which of Appendix D's cost figures the
    recommendation is most sensitive to.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — What Occlusion Culling Actually Tests

Referenced in Background. Every frame, a real-time renderer has to decide which of a scene's
objects are worth asking the GPU to draw. Testing every object's exact, detailed mesh against the
camera every frame would itself cost more time than it saves — so real engines test a simplified
stand-in shape instead: a sphere, a box, a capsule, or some other simple solid that is quick to
check mathematically. Unreal Engine's own documentation describes exactly this approach: an
actor's bounds are built from simplified shapes rather than the real mesh, precisely because the
simplified check is what makes culling fast enough to run every single frame across an entire
world's worth of objects (SEE APPENDIX E, [S3]).

Two properties of a stand-in shape matter for this case: how *cheap* the shape is to test
(fewer/simpler arithmetic operations means a faster check), and how *tightly* the shape fits the
real object (a loose fit means the object is treated as "possibly visible" for longer than it
actually is, which costs real rendering time on an object the player cannot see).

## Appendix B — Three Representative Props

Referenced in Background and Challenge 3 (D1, D2, D3). Three long, thin prop types stand in for
this entire class of object. Each is built from a cylinder plus either a cone or a square pyramid.

| Prop | Component 1 | Component 2 | Total height |
|---|---|---|---|
| Lamppost | Cylinder pole: radius 0.075 m, height 6.1 m (MA1) | Cone light-fixture cap: radius 0.15 m, height 0.3 m (MA2) | 6.4 m |
| Industrial pipe | Cylinder: radius 0.0841 m, height 4.0 m (MA3) | — (single cylinder) | 4.0 m |
| Sign post | Cylinder post: radius 0.05 m, height 2.5 m (MA4) | Square pyramid cap: base side 0.2 m, height 0.15 m (MA5) | 2.65 m |

**Bounding sphere construction (Option A):** radius = half the prop's total height (a sphere large
enough to reach the object's farthest tip from its center).

**Bounding capsule construction (Option B):** a cylindrical body spanning the prop's *full* total
height, at a radius equal to the prop's own widest cross-section (its widest component's radius,
or half its widest component's diagonal for the square pyramid cap), capped by two hemispheres of
that same radius — this guarantees the capsule fully contains the prop, with the hemispherical
caps as pure extra headroom beyond the prop's own extent.

The lamppost pole's height (6.1 m) is chosen within a real, cited range for standard street light
poles (SEE APPENDIX E, [S1]). The industrial pipe's radius (0.0841 m = 6.625 in outside diameter
÷ 2) is a real, cited standard pipe dimension (SEE APPENDIX E, [S2]) — 6-inch nominal pipe size,
Schedule 40. All other dimensions (MA1–MA5) are stated Modeling Assumptions — see Modeling
Assumptions below.

## Appendix C — Scene Prop Counts

Referenced in Challenge 3 (D2, D3, D4). The number of each prop type actively tested for culling
in a typical loaded world region, per frame (MA6).

| Prop | Count tested per frame |
|---|---|
| Lamppost | 600 |
| Industrial pipe | 600 |
| Sign post | 600 |
| **Total** | **1,800** |

## Appendix D — Cost Inputs

Referenced in Challenge 3 (D4).

| Item | Value |
|---|---|
| Per-object culling-test cost, bounding sphere (Option A) | 0.0005 ms (MA7) |
| Per-object culling-test cost, bounding capsule (Option B) | 0.0015 ms (MA8) |
| Rendering/overdraw cost per liter of wasted (needlessly-still-visible) bounding volume | 0.00000002 ms per liter, equivalently **0.02 ms per 1,000,000 liters (1 million liters)** (MA9) |

**What "rendering/overdraw cost" means here:** a bounding shape that wastes more volume keeps its
object marked "possibly visible" over a larger space and for more time than the object's own real
shape would justify — which costs real GPU time (extra draw calls, extra shading) on an object the
player cannot actually see. MA9 converts that wasted volume into an approximate millisecond cost so
it can be added to the culling-test cost on the same footing.

**A decimal-point warning, stated explicitly because this is where hand-calculation most often goes
wrong:** 0.00000002 has seven leading zeros after the decimal point, and it is very easy to
mis-place one when multiplying by hand. Working in **millions of liters** avoids this: multiply your
wasted-volume total (in liters) by 0.000001 to convert it to millions of liters, then multiply by
0.02 ms — not by 0.00000002 directly — to get the render cost in milliseconds. Worked example, using
a placeholder number that is *not* one of this case's own wasted-volume totals: a wasted volume of
50,000,000 liters = 50 million liters; 50 × 0.02 ms = **1.0 ms**, not 1,000 ms and not 0.001 ms.
Check that your own D4 answer is in the right order of magnitude (a handful of milliseconds, not
thousands and not a tiny fraction) before moving on.

## Modeling Assumptions

> These figures are **not sourced from an external publisher**. They are stated scenario
> assumptions chosen by the case author. A Hero may challenge these numbers in discussion — that
> is a legitimate move, and the Sensitivity column shows exactly where the challenge would matter.
>
> MA1 and MA3's basis columns cite real research: a lighting-equipment retailer's published pole
> height range, and the ASME B36.10 steel pipe dimension standard — see Appendix E for what each
> source is and how it is used.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Lamppost pole height | 6.1 m (20 ft) | Chosen within a real, cited standard street-light pole range of 15–30 ft [S1] — 20 ft sits toward the lower (residential-scale) end. | Affects the lamppost's total height and therefore its bounding sphere radius directly — a taller pole makes the sphere option's waste even larger, strengthening the case for a capsule. |
| MA2 | Lamppost fixture cap (cone) dimensions | radius 0.15 m, height 0.3 m | No public source publishes a specific decorative light-fixture housing's dimensions — this is a stated scenario detail for a plausible flared fixture cap. | Minor — the cap is small relative to the pole; changing it barely moves either bounding shape's volume. |
| MA3 | Industrial pipe length | 4.0 m | No public source publishes a specific prop's pipe segment length — only the pipe's diameter is a real published standard [S2]; length is a scenario choice for a plausible prop-sized segment. | Directly scales both the sphere's and the capsule's volume for this prop; does not change which option wins on its own. |
| MA4 | Sign post height | 2.5 m | No public source publishes a specific game prop's exact post height; chosen as a plausible sign-post scale. | Minor relative to the lamppost and pipe's contribution to the scene total. |
| MA5 | Sign post pyramidal cap dimensions | base side 0.2 m, height 0.15 m | No public source publishes this decorative cap's dimensions — a stated scenario detail. | Minor — small relative to the post. |
| MA6 | Scene prop counts (Appendix C) | 600 of each prop type per frame | No public source publishes any specific game's actual per-frame prop density; chosen as a plausible large-open-world scale. | Scales both options' totals together — sensitivity_model.py's flex sweep shows this does not flip the winner on its own (both totals move proportionally). |
| MA7 | Per-object culling-test cost, bounding sphere | 0.0005 ms | No public source publishes an exact per-object nanosecond/millisecond cost for a bounding-sphere visibility test at this level of specificity — this is a stated engineering estimate for a simple distance-squared-vs-radius-squared check, the cheapest class of geometric test. | This is one of the case's most sensitive dials — see Sensitivity Disclosure. |
| MA8 | Per-object culling-test cost, bounding capsule | 0.0015 ms (3× the sphere cost) | No public source publishes this either — a capsule test (point-to-segment distance, then compare to radius) is genuinely more arithmetic than a sphere test, and 3× is a stated, moderate estimate of that extra cost, not a measured benchmark. | This is one of the case's most sensitive dials — see Sensitivity Disclosure. |
| MA9 | Rendering/overdraw cost per liter of wasted bounding volume | 0.00000002 ms/liter | No public source ties "liters of wasted bounding volume" directly to a millisecond rendering cost — this is a constructed scenario conversion, the case's central modeling choice, calibrated so both the CPU-cost term and the wasted-volume term matter to the final answer rather than one trivially dominating. | This is the case's single most sensitive dial — see Sensitivity Disclosure. |

## Appendix E — Sources

All sourced (non-assumption) figures and facts in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Standard street light pole height range | 15 to 30 foot poles (standard product range) | LED Lighting Supply — [Street Light Poles](https://www.ledlightingsupply.com/light-poles/poles-by-project/street-light-poles) | accessed 2026-09-18 | MEDIUM |
| S2 | 6-inch nominal pipe size (NPS), Schedule 40 steel pipe, outside diameter | 6.625 inches | Engineering ToolBox, citing ASME/ANSI B36.10/19 — [Steel Pipes Dimensions](https://www.engineeringtoolbox.com/steel-pipes-dimensions-d_43.html) | accessed 2026-09-18 | HIGH |
| S3 | Real game engines build an actor's visibility bounds from simplified geometric shapes (a sphere and a box), not the real mesh, specifically to make per-frame visibility testing fast | qualitative — "The bounds of an Actor is made up of two parts: a sphere and a box... The bounding sphere enables fast collision detection through simple distance calculations, while the bounding box is a closer match to the shape of the object" | Epic Games — [Visibility and Occlusion Culling in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/visibility-and-occlusion-culling-in-unreal-engine) | accessed 2026-09-18 | HIGH |
| S4 | Occlusion culling (skipping rendering work for hidden objects) is a real, standard, currently-documented technique across major game engines | qualitative — grounds Appendix A's framing | Unity Technologies — [Occlusion culling](https://docs.unity3d.com/Manual/OcclusionCulling.html) | accessed 2026-09-18 | HIGH |

**Who these sources are:** LED Lighting Supply [S1] is a lighting-equipment retailer whose published
product-range page states standard pole height offerings. Engineering ToolBox [S2] is a widely used
public engineering-reference site, here citing the real ASME/ANSI B36.10/19 steel pipe dimension
standard directly. Epic Games [S3] and Unity Technologies [S4] are the publishers of Unreal Engine
and Unity, two of the real-world game engines this case's dilemma is modeled on. See
`RESEARCH_LOG.md` for the full search trail, including what was searched and rejected for the
per-object test cost and rendering-cost figures now recorded as Modeling Assumptions MA7–MA9 above.

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

(none claimed as vocabulary-kind terms for this case's skill set — see the "how to…" list below)

**"How to…" questions**

- How to find the surface area of a pyramid
- How to find the surface area of a cylinder
- How to find the volume of a pyramid
- How to find the volume of a cylinder
- How to find the volume of a cone
- How to find the volume of a sphere

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
