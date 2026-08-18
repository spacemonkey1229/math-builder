# Concept sheet — Surveying, Mapping & GPS (`surveying-geodesy`)

Single-concept sheet, target pre-selected from `ROADMAP.md` §B4 item 5 ("Survey monument dispute").
Approved by the user's standing instruction to work Queue 1 in order.

**Rescope note.** `domains.json`'s 21 `signature_skills` for this domain are mostly already absorbed:
9 are covered by legacy cases (Airstrike, Airplane Manufacturer, Castle Security, Robotics Engineer)
plus Company Front/Plaza Pavers from this run. Of the 9 genuinely zero-coverage skills, 3
(`pre-calculus-vector`, `pre-calculus-how-to-find-the-magnitude-and-direction-of-a-vector`,
`pre-calculus-matrix`) are Pre-Calculus tier, not MS-tier — appropriate for **Queue 2**, not this
case. The remaining **6 zero-coverage MS geometry skills** — all from ROADMAP's own suggested angle
"parallel lines and transversals" framing — are the ones this concept closes.

### C1 — Survey Monument Dispute · tier T2

**Protagonist.** Priya Chandrasekaran, a deputy county surveyor for Park County, Montana, called
to resolve which of two candidate iron pins marks the true SW corner of a disputed parcel near
Gardiner before a fence contractor breaks ground on the wrong line.

**The dilemma.** A.) Pin 1 (the older, weathered pin) OR B.) Pin 2 (a newer pin found 4.2 ft away)
— which one is the corner the original 1962 plat actually describes?

**The real geometry.** The recorded plat states the parcel's north and south fence lines are
parallel (a standard rural-deed convention), and the west boundary — the line connecting the NW
and SW corners — is the transversal that cuts them. The NW corner's monument is intact and
undisputed, with a plat-recorded interior angle. Because co-interior (same-side interior) angles
between two parallel lines and a transversal sum to 180°, the SW corner's *expected* interior angle
is derivable from the NW corner's — this is real geometry, not a metaphor, and forces
`geometry-transversal-line` and `geometry-how-to-find-angle-measures-given-parallel-lines-a-
transversal-line-and-at-least-one-an` (SPEC §1's forcing test: there is no other route to the
expected angle).

Each candidate pin, tied in with a total-station shot to the same known reference line, implies its
own *actual* angle at the corner — computed via `geometry-how-to-find-angle-measures-of-
intersecting-lines` (two intersecting lines: the west boundary and the shot to each pin). The pin
whose actual angle is closest to the plat's expected angle is the real corner.

A secondary cross-check ties each candidate pin to the NW corner and a third known reference point,
forming a triangle; classifying each triangle (acute/obtuse/scalene, from its own three angles)
against the plat's own recorded traverse-shape note is a second, independent piece of evidence —
forcing `geometry-acute-triangle`, `geometry-obtuse-triangle`, `geometry-scalene-triangle` (SPEC
§1's forcing test: a student must actually compute all three angles/sides to classify, not guess).

**Primary metric.** Absolute angular deviation (degrees) between each candidate pin's actual corner
angle and the plat's expected angle — smaller deviation wins. Same shape as a cost-minimization
metric (lower is better), so `sensitivity_model.py` reuses the verified ceiling-collapse transform
from Plaza Pavers/Company Front/Vent Cap/Apron Order.

**Why it's close.** Both pins are plausible: Pin 1 is the physically older monument (age favors
authenticity) but its angle deviates more from the plat's math; Pin 2 is newer (could be a rival's
more recent — and wrong — encroachment marker, OR could be a legitimate resurvey correction) but
its angle is closer to the recorded plat. The case does not resolve "older = more legitimate";
it forces the angle math to actually decide it.

**Would close (6 skills, all new zero-coverage):**

| id | kind | label |
|---|---|---|
| geometry-transversal-line | vocab | Transversal Line |
| geometry-how-to-find-angle-measures-of-intersecting-lines | how-to | How to find angle measures of intersecting lines |
| geometry-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-an | how-to | How to find angle measures given parallel lines, a transversal line, and at least one angle |
| geometry-acute-triangle | vocab | Acute Triangle |
| geometry-obtuse-triangle | vocab | Obtuse Triangle |
| geometry-scalene-triangle | vocab | Scalene Triangle |

**Data feasibility: HIGH**, matching `domains.json`'s own grade for this domain. The domain's own
data-availability note is explicit that the strongest real teaching asset here is a real NGS
monument datasheet a student can independently verify (Challenge 1's own research target), while
site-specific field notes for any one dispute are necessarily invented-but-declared (no public
database of real property-line disputes' raw field books exists). This case follows that exact
convention: **S1** is a real, live-fetched NGS datasheet (PID QX0584, "D 565," Gardiner MT — real
coordinates, real elevation, real description, confirmed reachable 2026-08-12) cited as the case's
real-world grounding and Challenge 1 research target, establishing the domain's data and monument
conventions are real; the specific disputed parcel's angles, pin locations, and traverse notes are
Priya's own field survey for this case (MA1, invented-but-declared, same convention as every prior
case's authored-but-undisclosed-publicly domain data — Cold Chain's route, Plaza Pavers' border
cut, Vent Cap's nesting result, Apron Order's marker layout).

**Sensitivity (SPEC §6).** None required — the stakes are a fence-line resurvey decision and a
professional judgment call, not personal loss or hardship.

**Split risk.** None — 6 skills, each with its own genuinely distinct, motivated deliverable. The
3 Pre-Calculus vector/matrix skills this domain also carries zero-coverage are deliberately left
for Queue 2 rather than stretched into this MS-tier case.

## Recommendation

Write C1 as specified — only concept on this sheet, pre-selected by queue order.
**Next step:** approved by queue order — proceed to `case-write`.
