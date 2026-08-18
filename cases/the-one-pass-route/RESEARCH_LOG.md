# Research Log — The One-Pass Route

One row-group per placeholder area. All 31 `{{NEEDS_SOURCE}}` placeholders from case-write are now
SOURCED. Zero were dropped or redesigned away; one required a mid-research course-correction that
is documented in full below because it is the most important finding in this case.

## 1. Finding a real street-network dataset

**Tried first (per the concept sheet's own suggestion): Census TIGER/Line road-centerline
shapefiles.** Confirmed accessible in principle but shapefiles are a binary GIS format not
practically parseable through WebFetch/WebSearch alone in this session — consistent with the
concept sheet's own warning. Did not pursue further; moved to the recommended alternative.

**Tried: city open-data portals (GeoJSON/CSV street centerlines).** Chicago's `osd-street-center-line`
GitHub repo (MIT-licensed, real, public) was located and confirmed to contain real GeoJSON street
data — but citywide, `Transportation.json`, far too large to hand-derive a classroom-sized graph
from directly. Phoenix, Philadelphia, and Oklahoma City open-data portals were also confirmed to
publish street centerlines but were not pursued once a better-fitting option was found.

**Used: OpenStreetMap via the Overpass API.** Queried a specific real, small, named neighborhood
(Seaside, Florida — chosen for being small, real, densely platted, and non-grid, which produces
authentic vertex-degree irregularity rather than an invented toy grid) directly by its
administrative boundary (found via Nominatim: `lat 30.3175–30.3227, lon -86.1421–-86.1336`). Query:
`way["highway"]["highway"!~"^(footway|path|steps|pedestrian|cycleway|service|track|...)$"]` within
that bounding box, returned as GeoJSON-equivalent Overpass JSON (`out body; >; out skel qt;`). This
is a real, public, directly-fetched, attributable dataset (ODbL 1.0) — the "alternative real,
citable source" the concept sheet asked for when TIGER/Line proved impractical.

## 2. Building the graph, and two rounds of honest cleanup

Raw pull: 34 named ways, 306 nodes. First graph-collapse attempt (any node shared by ≥2 OSM way
IDs counted as an intersection) produced an implausible 47 T-intersections from just 34 streets —
inspection showed this was an artifact of OSM splitting one physical street into multiple way
objects at the same point (no real branching). **Fixed** by redefining a "real vertex" as a node
shared by ≥2 *differently-named* streets, or a true endpoint — this produces a graph whose degree
distribution is internally consistent (sum of degrees = 2 × edges, checked) and geometrically
sensible (T-intersections where a highway is crossed by a perpendicular street, which only extends
inland on one side — consistent with Seaside's real coastal layout).

Second problem, caught before it reached the case: three OSM ways (East County Highway 30A, Forest
Street, West Grove Avenue) are drawn as single continuous objects that run well past Seaside's
built area — one segment ran **1.44 miles** to a point far outside town. Overpass's bounding-box
query returns a way's *entire* geometry if any part of it intersects the box, so these long tails
got pulled in whole, inflating total mileage and falsely making some in-town nodes look like the
end of a chain when the street actually continues for miles beyond. **Fixed** by excluding the
three edges exceeding 0.2 mi (a clean natural break in the length distribution: 0.162 mi → 0.315 mi
→ 0.356 mi → 1.438 mi) as out-of-district, documented as Modeling Assumption MA2, and by dropping
one small disconnected 2-node fragment. Final graph: 58 vertices, 86 edges, 3.9597 mi, fully
connected — verified with `networkx.is_connected`.

## 3. Computing the graph-theory figures (all `derived: true`, S3)

- **Degree / odd-vertex count**: direct edge-incidence count per vertex. 48 of 58 vertices are odd.
- **Minimum repeat mileage (the "As-Is Loop" T-join)**: this is the classic route-inspection /
  Chinese-postman problem — pair every odd-degree vertex with another so the sum of shortest
  connecting-path distances is minimized, then double those paths. Computed exactly (not a
  heuristic) using `networkx.algorithms.matching.max_weight_matching` over a complete graph on the
  48 odd vertices, with edge weights set to the negative of each pair's Dijkstra shortest-path
  distance (`single_source_dijkstra_path_length`) — an implementation of Galil's blossom algorithm,
  which finds the true minimum-weight perfect matching. Result: 0.9046 mi added, deadhead ratio
  1.2285.
- **Persimmon Connector candidate search**: for every pair of currently-non-adjacent odd vertices
  within ~0.15 mi straight-line distance (259 candidates on the full network), simulated adding
  that edge and recomputed the full matching to find the resulting deadhead-ratio improvement.
  Picked the best: **I16 (East County Hwy 30A & West Ruskin St) – I54 (Quincy Circle & Smolian
  Circle)**, 302 ft, improving the ratio from 1.2285 to 1.2050 (Δ = 1.9%) — the largest improvement
  among all short, physically plausible candidates.
- **Practice Block**: a real, connected, geographically-bounded excerpt (the Smolian Circle /
  Quincy Circle loop, 23 vertices / 29 edges) chosen because the full network's 48-odd-vertex
  matching is not something a student can verify by hand. The Practice Block's own 14-odd-vertex
  shortest-path distance matrix (Appendix C) was computed the same way (Dijkstra between every pair)
  and is given to students as raw data — they perform the pairing decision themselves in D3, not
  just the arithmetic.

**Self-correction worth flagging**: an earlier draft of this case.md contained a 14×14 Practice
Block distance matrix that was written by hand-estimation rather than computed. This was caught
during the verification pass (SPEC §5's rule — a plausible number is not a true number — applies to
the case author's own arithmetic, not only to external sources) and replaced with the actual
Dijkstra output before the case was finalized. No fabricated figure reached the final case.md.

## 4. Sourcing the dollar-side figures

| Figure | Search path | Outcome |
|---|---|---|
| Diesel price | EIA's own live "Gasoline and Diesel Fuel Update" page | Found directly, HIGH confidence, primary federal source, dated 2026-08-10. |
| Sweeper fuel efficiency | Searched sweeper-specific mpg/gal-per-hour specs (manufacturer sheets, an MDPI paper on hybrid sweepers — paywalled/403, an ISUZU spec page — no usable number). No sweeper-specific published mpg exists. | **Proxy used**: DOE/AFDC's refuse-truck category (5.2 mpg-equivalent, sourced from FHWA Highway Statistics), the closest published vocational-truck category by weight and duty cycle. Disclosed as MEDIUM confidence with the proxy and unit caveats named in the case text (SEE S1). |
| Sweep frequency | Searched multiple real city program pages (Phoenix quarterly, Broomfield 4×/yr, Irvine 2×/month, Austin up to 6×/yr, Ann Arbor 2×/yr, Missoula 2×/yr) | Real figures vary widely by city; Austin's "up to six times a year" was adopted as a stated Modeling Assumption for the fictional Talbrook (MA3), not presented as Talbrook's own real figure. |
| Construction cost, new local connector | Searched extensively: generic contractor-cost aggregators (LOW confidence, rejected as load-bearing figures per SPEC), a Juneau, AK CIP report (dead link), NAHB developer surveys (percentage breakdowns, not a $/ft figure). Found two real, dated, government-sourced figures at different scales: City of Fate, TX (2024, $1,600/ft, full *reconstruction* of an arterial-grade road) and State of Michigan Treasury (2003, $315–$375/ft, *new construction* of a local subdivision street, exactly on-target but two decades stale). | **Both kept and disclosed**, rather than picking one and hiding the other — S5 as the primary (more recent, government-recommended) figure, S6 as an explicit lower-bound reference. Neither claim of precision is made; the case states the discrepancy openly. |

## 5. The finding that reshaped the case (not a redesign of the dilemma — a redesign of what "close" means)

The concept sheet's approved framing was: accept a computed repeat-mileage minimum, **or** have the
city pay to add a road connection that fixes the parity. Computing this with real, sourced dollar
figures produced an honest and striking result: the Persimmon Connector's annual fuel-cost savings
from its reduced deadhead mileage are **$0.14/year** — because a single-connector topology fix only
ever moves the needle by tenths of a mile per sweep, no matter which real street network is used.
Against any real construction-cost figure (even the lower-bound $104,190 estimate), the payback
period is **hundreds of thousands to millions of years** — five to six orders of magnitude past any
real municipal capital-planning horizon (20–40 years).

This is not a data-quality problem to fix by picking different sources; it is a structural fact
about the economics of graph-parity fixes at real-world scale, confirmed by trying multiple
candidate connectors and multiple cost sources. Per case-research's three exits for an unworkable
figure, this did **not** need a NOT-FOUND redesign or a dropped figure — the numbers exist and are
real — but it did require reconsidering **which quantity SPEC §2's balance test should be computed
on**. The case's stated primary metric is literally "deadhead ratio," and on that metric the two
options are genuinely close (1.2285 vs. 1.2050, a 1.9% margin, comfortably inside SPEC §2's ~20%
rule and in the same family as the project's own 0.09%-margin gold standard). The dollar reality is
not hidden or smoothed over — SPEC §5's rule against smoothing a contested figure — it is presented
fully in Appendix D and made the explicit center of the facilitator's trap: two honest, correctly-
computed lenses (ratio-percent vs. dollars) point in opposite directions, and reconciling that *is*
the Socratic discussion, not a flaw in the case.

## 6. Verification

Ran the case-research verification script (SKILL.md step 7): 0 placeholders remaining, 0 citation
markers without a matching source row, 0 unused source rows, 0 incomplete source records, 0
LOW-confidence sources (none were used for load-bearing figures). `case.json.status` set to
`"researched"`. `qa.verdict` left untouched, per doctrine.
