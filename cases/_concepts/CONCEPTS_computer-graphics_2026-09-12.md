# Concept sheet — Computer Graphics & Animation (`computer-graphics`)

**Target and why (one line, per skill's own instruction).** Computer Graphics & Animation is
ranked HIGH authoring priority / HIGH data grade / **0 existing cases** in `readmodel/domains.json`
(as of this read) — the requested target for this run.

**A scoring-context correction, found by cross-checking live (per this session's instructions).**
`domains.json`'s "0 existing cases" claim for `computer-graphics` is stale. Two cases already in
the corpus are graphics cases in every functional sense — `cases/the-rig-budget/case.json`
(GPU skin-deformation compute cost, two skinning algorithms) and `cases/the-skin-pack-atlas/case.json`
(texture-atlas memory vs. install-base coverage) — and between them they closed **all 7 skills**
in Pre-Calculus/Matrices (now sitting at n=5–6, not thin). Three more existing cases
(`wind-triangle`, `the-crosswind-cut`, `the-course-correction`) closed all 7 skills in
Pre-Calculus/Vectors to n=3 each. **This means the domain's own listed `signature_skills[]` —
mostly matrix and vector terms — are not the gap here.** I checked every signature skill live
against `standards_spine.json`: of the 18 listed, only `geometry-similar` (n=2) is thin; the other
17 are already at n=3–7. The "matrix transformations are a strong fit" framing is true of the
*subject matter* but not of *remaining spine gaps* — so I pivoted the five concepts below onto the
skills that are genuinely thin (`n<=2`, this session's confirmed sweep convention — no true zeros
exist anywhere in the 437-skill spine) and that a graphics job can honestly force: the three
remaining Transformations skills, the one remaining Coordinate Plane skill, and four thin
groups a graphics case can legitimately touch — Triangles, Quadrilaterals And Polygons, Surface
Area And Volume, and Polar And Parametric / Trigonometric Functions. All n-values below were
pulled live from `readmodel/standards_spine.json` this session, not from `gap_queue.json`'s
abbreviated view or `domains.json`'s signature-skill list.

| # | Concept | Score | Tier | Group(s) fully gap-closed |
|---|---|---|---|---|
| C1 | The Point Cloud Match | **6.8** | T3 | Geometry/Transformations (3/3 remaining thin); Geometry/Coordinate Plane (1/1 remaining thin) |
| C2 | The Orbit Equation | **5.28** | T3 | Pre-Calculus/Polar And Parametric (3/3 remaining thin); Pre-Calculus/Trigonometric Functions (3/3 remaining thin) |
| C3 | The Culling Volume | **4.8** | T2 | Geometry/Surface Area And Volume (6/6 remaining thin) |
| C4 | The Sliver Triangle | **3.36** | T2 | Geometry/Triangles (6/6 remaining thin) |
| C5 | The Hitbox Call | **1.8** | T1/T2 | none fully closed (partial: Geometry/Quadrilaterals And Polygons, 5 of 11 remaining thin) |

**Recommendation.** Write **C1, The Point Cloud Match** first. It is the only concept in this
batch with a genuinely HIGH, named, verified-live data source — the Stanford 3D Scanning
Repository (`domains.json`'s own listed source, and I re-confirmed it live this session) publishes
real point-cloud/mesh vertex data for the Bunny and Dragon scans, which is exactly what a
registration-error case needs — and it closes two full groups (all 4 remaining thin skills between
Transformations and Coordinate Plane) with a job (photogrammetry technician) that is literally one
of `domains.json`'s own three listed careers for this domain. **C2** is the strong second pick —
it closes two full groups too (Polar/Parametric and Trig Functions, 6 skills total) — but I am
grading its data feasibility MEDIUM, not HIGH: camera-orbit radius, clipping bounds, and framing
targets are levelling/production choices with no external dataset behind them, only real,
well-documented *technique* (Unity/Unreal camera-rail and look-at conventions). **C3** is a solid
third pick with the same honest caveat — bounding-volume culling is real, documented engine
practice, but the prop dimensions being compared are necessarily a stated production scenario, not
a sourced dataset. **C4** clears the Cold Chain 4.2 calibration floor by a small margin only
because of its full-group bonus; its "triangle quality defect" metric is the part of this whole
batch closest to an invented number, so if written it needs its metric anchored hard to something
real (see its data-feasibility note) or it should be re-scoped. **Kill C5 for now** — it closes no
full group, scores under the Cold Chain floor, and its best grounding (physics-engine convex
collider requirements) is a real technical fact but not a quantifiable external data source; it is
included only to show the honest bottom of this domain's current option set, not as a
write-next candidate.

**The honest feasibility pattern across this whole domain.** Computer Graphics & Animation is
genuinely thinner on sourceable data than a domain like Oceanography. Tooling (Blender, GeoGebra)
and a handful of real reference meshes (Stanford repository, NASA Open Data) are free and
verifiable — that is where this domain's HIGH grade actually comes from — but there is no
public, numeric equivalent of "NOAA tide tables" for render-farm minutes, GPU triangle throughput
under specific shading loads, or animation-pipeline labor cost. A case needing those will
legitimately need a `Modeling Assumptions` block for the production-specific numbers, with only
the underlying reference geometry (where used) pulled from a real, named, checkable source. None
of the five concepts below claims a fabricated dataset; where a number cannot be sourced, the note
below says so plainly.

---

### C1 — The Point Cloud Match   ·   score 6.8   ·   tier T3

**Protagonist.** Priya Kessler, a 3-D scanning/photogrammetry technician at a small VFX
digitization studio, whose scan has to be delivered aligned to the client's reference model by
end of day or the studio eats the re-shoot cost.

**The dilemma.** A.) Accept the scanning rig's automatic alignment, which the software reports as
converged, and ship the file OR B.) Manually re-register the scan by hand against three known
marker points, because Priya suspects the rig's camera flipped one pass and mirrored part of the
mesh.

**Primary metric.** Registration error (millimeters of point-to-point mismatch) per minute of
technician time spent — a ratio, because the automatic method is free in time but may leave real
error uncorrected, while the manual method costs time but can catch what the software can't.

**Why it's close.** The rig's software reports a "converged" alignment, but a mirrored scan pass
(a real, documented photogrammetry artifact) can converge to a *low but wrong* error if the
matching algorithm accidentally paired mirrored features — checking this requires deciding whether
two mesh sections are congruent (same size and shape, alignable by rotation/translation alone) or
merely similar (same shape, different scale — a sign the scanner's calibration drifted) — and
whether one arm of the scan is a reflection of the other rather than a rotation, which the rig's
solver cannot distinguish on its own without a human checking marker coordinates by quadrant.
Manual correction catches the mirror error but costs billable time the studio may not recover.

**Would close (4 skills, 1 how-to / 3 term — all of Transformations' and Coordinate Plane's
remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-congruent | term | Congruent | 2 |
| geometry-similar | term | Similar | 2 |
| geometry-how-to-reflect-a-figure-across-the-y-axis | how-to | How to reflect a figure across the Y-Axis | 2 |
| geometry-quadrant | term | Quadrant | 2 |

**Already-covered skills it also exercises.** `geometry-coordinate-pair-also-ordered-pair` (n=6,
marker positions), `geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane`
(n=3, point-to-point registration error itself), `geometry-transformation` / `geometry-translation`
/ `geometry-rotation` (n=3–5, describing the rig's attempted alignment).

**Data feasibility: HIGH.** Named source confirmed live this session:
- Stanford 3D Scanning Repository (`http://graphics.stanford.edu/data/3Dscanrep/`) — the Bunny and
  Dragon scans are real multi-pass range-scan datasets with real vertex coordinates and known
  registration challenges (they are the canonical academic test case for point-cloud alignment).
  `case-research` can pull actual coordinate subsets rather than inventing marker positions.

Not confident about: a specific published dollar rate for VFX photogrammetry technician time or a
studio's per-scan billing rate — that stays a stated Modeling Assumption, disclosed as such.

**Sensitivity (SPEC §6).** None.

**Split risk.** None — 4 skills, one coherent deliverable (align, detect the mirror, quantify the
manual-correction trade).

---

### C2 — The Orbit Equation   ·   score 5.28   ·   tier T3

**Protagonist.** Devon Achebe, a gameplay camera engineer on a boss-fight cutscene team, who has to
lock the camera path before the animation team blocks the fight and cannot easily re-time it.

**The dilemma.** A.) Drive the boss-fight camera on a fixed-radius circular orbit around the boss,
computed in polar coordinates (angle in, position out) OR B.) Drive it on a variable-radius polar
curve (radius changes with angle) for a more dramatic push-in during the boss's telegraphed attack.

**Primary metric.** Percent of the frame the boss occupies, averaged over the fight, per
millisecond of per-frame camera-path computation — a ratio, because the fixed-radius orbit is
cheap to compute but under-frames the boss during the attack, while the variable-radius curve
frames the attack better but costs more math per frame and risks clipping into the arena wall if
the radius shrinks too far.

**Why it's close.** Camera waypoints are authored in rectangular (x, y) level coordinates but the
orbit itself has to be reasoned about in polar terms — converting between the two is exactly how a
camera engineer checks whether the variable-radius path ever comes closer to the boss than the
arena's collision radius allows. Graphing the candidate polar equation is how Devon catches a
clipping frame before it ships. The camera's facing direction at each frame is a tangent to the
path, and its angle is read the same way a unit-circle angle gives sine/cosine/tangent components
— genuinely forced, because "which way is the camera looking" is not optional information in a
cutscene.

**Would close (6 skills, 2 how-to / 4 term — all of Polar And Parametric's and Trigonometric
Functions' remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| pre-calculus-polar-coordinate | term | Polar Coordinate | 2 |
| pre-calculus-how-to-convert-a-point-between-rectangular-and-polar-coordinates | how-to | How to convert a point between rectangular and polar coordinates | 2 |
| pre-calculus-how-to-graph-a-polar-equation | how-to | How to graph a polar equation | 2 |
| pre-calculus-unit-circle | term | Unit Circle | 2 |
| pre-calculus-tangent-function | term | Tangent Function | 2 |
| pre-calculus-how-to-find-the-sine-cosine-and-tangent-of-an-angle-using-the-unit-circle | how-to | How to find the sine, cosine, and tangent of an angle using the unit circle | 2 |

**Already-covered skills it also exercises.** `pre-calculus-vector` / `pre-calculus-dot-product`
(n=3, camera facing vs. boss-facing alignment check), `geometry-coordinate-pair-also-ordered-pair`
(n=6, the authored rectangular waypoints).

**Data feasibility: MEDIUM.** No specific external dataset applies — this is real technique on a
stated production scenario, honestly. What is real and checkable: Unity's and Unreal Engine's
published documentation on camera-rail/orbit and look-at conventions (confirms the *method* is
standard industry practice, not invented). Not confident about, and necessarily a Modeling
Assumption: the specific arena radius, boss hitbox size, and target framing percentage — these are
scenario numbers a `case-research` pass would state and justify, not source.

**Sensitivity (SPEC §6).** None.

**Split risk.** None — 6 skills, one arc (author the orbit → convert to check clipping → graph to
verify → derive facing).

---

### C3 — The Culling Volume   ·   score 4.8   ·   tier T2

**Protagonist.** Marisol Tan, a rendering/engine programmer responsible for occlusion culling on an
open-world game, whose frame-budget review is Friday and whose culling system is currently the
single biggest CPU cost on the list.

**The dilemma.** A.) Give every prop in the world a single bounding sphere for the culling test
(one radius, one cheap distance check) OR B.) Give elongated props (pipes, ladders, lampposts) a
bounding capsule instead — a cylinder with hemispherical caps — which fits them tighter but costs
more per-object math every frame.

**Primary metric.** Liters of "wasted" bounding volume (the bounding shape's volume minus the
prop's real volume) per millisecond of extra per-frame culling-test cost — a ratio, because the
sphere is fast but wastes enormous volume on a long thin prop (which means it stays "on screen" to
the culling system, and gets drawn, long after the real prop has left the camera's view), while the
capsule wastes little volume but costs more compute across thousands of props per frame.

**Why it's close.** A long thin prop modeled as a bounding sphere needs a sphere radius equal to
half its longest dimension, which makes the sphere's volume enormous relative to the prop's actual
cylinder-plus-cone or cylinder-plus-pyramid shape — that comparison is exactly a volume and surface
area calculation across the primitive solids in this group. Surface area also matters here because
a rough estimate of a prop's shading cost scales with its surface area, not its volume, so the two
options trade off differently depending on which budget (compute-per-frame or shading-cost) the
team is protecting.

**Would close (6 skills, all how-to — all of Surface Area And Volume's remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-how-to-find-the-surface-area-of-a-pyramid | how-to | How to find the surface area of a pyramid | 2 |
| geometry-how-to-find-the-surface-area-of-a-cylinder | how-to | How to find the surface area of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-pyramid | how-to | How to find the volume of a pyramid | 2 |
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | How to find the volume of a cylinder | 2 |
| geometry-how-to-find-the-volume-of-a-cone | how-to | How to find the volume of a cone | 2 |
| geometry-how-to-find-the-volume-of-a-sphere | how-to | How to find the volume of a sphere | 2 |

**Already-covered skills it also exercises.** `geometry-face` / `geometry-edge` (n=2 each — but not
claimed for scoring here since C1/this concept would need to genuinely force naming faces/edges on
the bounding primitives, which this metric does not require; left uncounted deliberately rather
than stuffed in).

**Data feasibility: MEDIUM.** Named and checkable: Unity's and Unreal Engine's published
documentation on bounding-volume occlusion culling (confirms this is real, standard engine
practice, not invented). Not confident about: real published per-object culling-test millisecond
costs for a specific engine/hardware pair — that would be a stated Modeling Assumption unless
`case-research` finds a specific published engine-profiling benchmark, which I have not verified
exists at this level of specificity.

**Sensitivity (SPEC §6).** None.

**Split risk.** None — 6 skills, one deliverable (compute both bounding volumes and surface areas
for 2–3 representative props, compare the ratio).

---

### C4 — The Sliver Triangle   ·   score 3.36   ·   tier T2

**Protagonist.** Owen Reyes, a technical artist on a mobile game's asset-optimization team,
responsible for retopologizing a hero character's high-poly sculpt down to a game-ready mesh
before the art director signs off.

**The dilemma.** A.) Run the automatic decimation tool at an aggressive triangle-count target
(fast, but produces some very thin "sliver" triangles at the joints) OR B.) Manually retopologize
the joint areas by hand to keep triangles close to equilateral (slower, but avoids the shading
artifacts sliver triangles cause).

**Primary metric.** Shading-artifact count per thousand exported triangles — a ratio, because the
automatic method produces a mesh fast but a higher artifact rate, while the hand-retopologized mesh
takes longer but should produce fewer artifacts per triangle shipped.

**Why it's close.** Classifying the decimator's output triangles — how many are acute, how many are
obtuse (the sliver problem: a very obtuse triangle is nearly degenerate and shades poorly), whether
any are scalene versus the hand-built mesh's more equilateral ones, and whether the shortest two
sides plus the longest side ever approach the triangle inequality's boundary (a near-failure of the
inequality is exactly what a "sliver" is, geometrically) — is the actual audit Owen has to run to
decide whether the automatic pass is good enough to ship.

**Would close (6 skills, all term — all of Triangles' remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-acute-triangle | term | Acute Triangle | 2 |
| geometry-obtuse-triangle | term | Obtuse Triangle | 2 |
| geometry-leg | term | Leg | 2 |
| geometry-equilateral-triangle | term | Equilateral Triangle | 2 |
| geometry-scalene-triangle | term | Scalene Triangle | 2 |
| geometry-triangle-inequality-theorem | term | Triangle Inequality Theorem | 2 |

**Flagging this concept's own weak point honestly:** all 6 claimed skills are terms (weight 0.6
each), and no how-to is forced — this is close to the "vocabulary stuffing" pattern the parent
skill warns against. It clears the group-bonus threshold and the Cold Chain floor only because the
group is fully closed, not because the case is rich in procedure. If written, `case-write` should
be pushed to find a genuine how-to (e.g., an actual decimation-ratio or mesh-quality calculation)
or the concept should be honestly scored lower.

**Already-covered skills it also exercises.** `geometry-how-to-find-the-perimeter-of-a-triangle`
and similar, if present at higher n — not verified for this sheet; `case-write` should re-check.

**Data feasibility: LOW-MEDIUM.** Real and checkable: published mobile GPU triangle-throughput
specs exist (chipset vendor spec sheets) and would ground the "triangle budget" side of the
scenario. Not confident about, and this is the honest gap: a real, sourced "shading artifact per
triangle" defect rate does not exist as public data — it would have to be a stated Modeling
Assumption, disclosed as invented for the scenario, not sourced.

**Sensitivity (SPEC §6).** None.

**Split risk.** None structurally, but see the vocabulary-stuffing flag above — recommend
`case-write` add a procedural deliverable before treating this as ready.

---

### C5 — The Hitbox Call   ·   score 1.8   ·   tier T1/T2

**Protagonist.** Nadia Osei, a gameplay/physics tools engineer on a 2-D platformer, who has to ship
collision shapes for a new level pack by end of sprint.

**The dilemma.** A.) Build precise multi-vertex collision polygons that trace each platform's exact
outline, including a few genuinely concave (non-convex) platforms OR B.) Approximate every platform
with the nearest of four convex quadrilateral templates (parallelogram, rhombus, trapezoid, kite),
since most physics engines require convex colliders and a concave shape must be decomposed into
convex pieces before the engine will accept it.

**Primary metric.** Wasted collision area (pixels² of mismatch between the true platform outline
and its collider) per millisecond of physics-step time saved — a ratio, because the precise
concave colliders (after required decomposition into convex pieces) cost more per physics step but
match the art exactly, while the quad-template approximation is cheap per step but silently changes
where the player can stand or fall.

**Why it's close.** Recognizing that a platform's outline is concave forces the actual convex-
decomposition requirement most 2-D physics engines impose; classifying the remaining convex
outlines as a parallelogram, rhombus, trapezoid, or kite is how Nadia picks the cheapest template
that still matches each platform's real proportions.

**Would close (5 skills, all term — partial coverage of Quadrilaterals And Polygons, 5 of its 11
remaining thin skills; no full-group bonus):**

| id | kind | label | n |
|---|---|---|---|
| geometry-concave | term | Concave | 2 |
| geometry-parallelogram | term | Parallelogram | 2 |
| geometry-rhombus | term | Rhombus | 2 |
| geometry-trapezoid | term | Trapezoid | 2 |
| geometry-kite | term | Kite | 2 |

**Not claimed, deliberately:** `geometry-pentagon` / `heptagon` / `nonagon` / `decagon` /
`dodecagon` / `n-gon` — real platform outlines in this scenario do not genuinely force naming
polygons by side-count above four sides; claiming them would be exactly the coverage-inflation the
parent skill warns against.

**Already-covered skills it also exercises.** None identified beyond the above.

**Data feasibility: MEDIUM, honestly capped.** Real and checkable: the convex-collider requirement
itself is real, documented behavior in mainstream 2-D physics engines (Box2D and derivatives) — a
genuine technical fact, not invented. Not confident about, and this is the binding constraint on
this concept's score: there is no external dataset for "wasted collision area vs. physics-step
time" at any level of specificity; every number in this case would be a stated Modeling
Assumption. Combined with a raw score with no full-group bonus, this concept does not clear the
Cold Chain 4.2 calibration floor and should not be the next write.

**Sensitivity (SPEC §6).** None.

**Split risk.** None, but recommend killing or substantially reworking before it is written — see
the Recommendation above.
