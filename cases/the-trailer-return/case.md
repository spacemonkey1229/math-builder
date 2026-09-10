Case Study: The Trailer Return
MS | Math | Case Study | 2026 | Adventure

## Overview

Denise Okafor is standing in the Public Works yard at 5:15 in the morning with a grease-stained
route map bungeed to a clipboard, watching her breath fog over the diesel exhaust of Truck 4. The
recycling truck idles behind her, hopper empty, waiting on the same tangled loop it runs every
collection day through the Bay Fruit Streets — Strawberry, Nectarine, Peach, Plum, Pine, and Fig,
crossed by Bay, Mason, Madison, Monroe, Jefferson, Randolph, and Tazewell. She already knows how
this morning ends: the driver will finish the far corner of Monroe, then double back down blocks
he already emptied, just to bring the truck home to the yard the way the route always has to. A courier company's flatbed quote is open on her phone — enough truck-hauling capacity to pick
Truck 4 up wherever it finishes and haul it back light, no retracing required. Her supervisor wants
a one-page recommendation on his desk before the Thursday budget meeting: keep closing the loop the
way it's always been closed, or pay someone else to close it for them. Denise pulls up the street
grid on her phone, starts counting corners, and does not put the truck in gear yet.

## Background

Denise Okafor is the Recycling Route Coordinator for the Department of Public Works in the town of
Averyton. Fifteen years on this route have made her genuinely proud of the work — she still keeps a
hand-annotated paper street map bungeed to Truck 4's dash, because, as she puts it, the GPS "argues
with her" about which streets are actually one-way or blocked by construction, and her paper map has
never once been wrong. She is not chasing a badge for it; shaving even a few minutes off a route is a
real, satisfying win to her, not just a box her supervisor asked her to check. Practical, a little
stubborn about trusting her own eyes on the pavement over what a screen tells her, but no luddite —
she just knows these streets better than any app does. She is responsible for the weekly single-stream
recycling route through the Bay Fruit Streets district — a 68-intersection, 102-block-segment street grid along the town's original
harbor-front plat — and is accountable to her supervisor for the truck's daily diesel cost, which
comes out of the same line item as every other route in town (SEE APPENDIX A). She does not set the
town's labor contract or its fuel budget, but her route-design memo is what her supervisor uses to
decide whether Averyton pays an outside hauling contractor for anything beyond the truck's own
tires.

Every collection route that has to cover every block exactly once and return to where it started is
what a mathematician calls an Euler circuit — and a route can only close into one if, at every
intersection in its graph, an even number of block-segments meet there (SEE APPENDIX H). Denise's
own count of the Bay Fruit Streets grid found 34 intersections where an odd number
of streets meet — corners where the truck cannot simply pass through and continue, because every
incoming block needs an outgoing one to pair with it. Today, Truck 4 handles those odd corners by
backtracking: at each one it re-drives a segment it has already emptied, so the loop still closes
back at the yard. That backtracking is not free — every repeated block is diesel the town pays for
and driving time down streets that produce nothing for that day's collection totals.

Denise has priced out a different fix. **The Closed Loop** is today's standing practice: Truck 4
runs the whole grid as one closed circuit, returning under its own power to the yard every morning,
repeat mileage and all. **The Trailer Return** would keep the truck's collection path itself
almost unchanged, but drop the requirement that it drive itself home — instead, a contracted
flatbed hauler picks the truck up wherever its most efficient path happens to end and trailers it
back to the yard. Mathematically, dropping the "must return to the start" requirement turns the
question from *does this graph have an Euler circuit?* into *does this graph have an Euler path?* —
a route that covers every block exactly once but is allowed to start and end at two different
corners (SEE APPENDIX H). That relaxation lets Denise leave the single worst pair of odd corners
unmatched instead of pairing all of them, which is real, computable savings in repeat mileage — at
the real, quoted cost of a flatbed hauler (SEE APPENDICES B, C, D, E and F). All figures in this
case are sourced in (SEE APPENDIX G).

## Dilemma

You are Denise Okafor.
Do you:
A.) Recommend keeping The Closed Loop — Truck 4 continues driving itself back to the yard every
collection day, under today's full closed-circuit repeat mileage OR
B.) Recommend The Trailer Return — contract a flatbed hauler to retrieve Truck 4 from wherever its
shortest open path ends, cutting repeat mileage at the cost of a daily hauling fee

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A vertex-degree table for every corner in the Bay Fruit Streets Practice Block (a real
    26-intersection excerpt of the full grid, Appendix B), each vertex labeled EVEN or ODD.
    D2. A written Euler determination for the full 68-intersection Bay Fruit Streets grid: does it
    have an Euler circuit, an Euler path, or neither — justified by the specific odd-vertex count
    given in Appendix A, using the rule in Appendix G.
    D3. A closed-circuit repeat-mileage computation for the Practice Block: pair every odd vertex
    with another odd vertex using the shortest-path distance table in Appendix C, and compute the
    Practice Block's resulting deadhead ratio (total block-segments driven ÷ total block-segments
    that exist).
    D4. An open-path repeat-mileage computation for the same Practice Block: re-run the pairing in
    D3, but this time leave exactly one pair of odd vertices unmatched as your route's start and
    end corners, choosing whichever pair minimizes the mileage left to pair — then compute the new
    deadhead ratio and compare it to D3's.
    D5. A cost comparison table for the full grid: total daily diesel cost under The Closed Loop
    (Option A) versus total daily diesel cost plus the flatbed hauling fee under The Trailer Return
    (Option B), using Appendix D's official deadhead-ratio figures and Appendix E's cost data.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Bay Fruit Streets Grid

| Figure | Value |
|---|---|
| Intersections (vertices) | 68 [S3] |
| Block segments (edges) | 102 [S3] |
| Total street mileage | 7.3245 mi [S3] |
| Odd-degree intersections | 34 [S3] |
| Degree distribution | 9 dead ends (degree 1) · 8 pass-throughs (degree 2) · 25 three-way corners (degree 3) · 26 four-way corners (degree 4) [S3] |

**How this appendix was built.** The Bay Fruit Streets grid is modeled directly on the real,
present-day street network of the historic downtown grid of Cape Charles, Virginia — Bay, Mason,
Madison, Monroe, Jefferson, Randolph, and Tazewell Avenues crossing Strawberry, Nectarine, Peach,
Plum, Pine, and Fig Streets, plus Park Row — fetched live from OpenStreetMap via the Overpass API
[S3]. Raw way geometry was collapsed into a vertex/edge graph the same way a route planner would:
a vertex is any point where 2+ differently-named streets meet or a true dead end occurs; an edge is
the summed haversine-distance length of an uninterrupted same-named run between two such vertices.
Four segments (Old Cape Charles Road, Bayshore Road, Marina Road, Harbor Street) that run well past
this grid toward the marina and the highway were excluded as outside Denise's assigned district
(SEE APPENDIX F, MA2). This is a real, present-day street layout, standing in for the fictional
town of Averyton's Bay Fruit Streets district (SEE APPENDIX F, MA1) — no fictional town has a real,
public street-centerline dataset of its own.

## Appendix B — Practice Block Vertex-Degree Table

A real 26-intersection excerpt of the full grid — Mason, Madison, Monroe, Randolph, and Tazewell
Avenues crossing Pine, Strawberry, Peach, and Plum Streets, plus a short leg of Park Row — small
enough to hand-compute D1, D3, and D4 on before tackling the full 68-vertex grid in D2/D5.

| Vertex | Streets meeting here | Degree | EVEN/ODD |
|---|---|---|---|
| A | Monroe Avenue, Pine Street | 3 | ODD |
| B | Monroe Avenue, Pine Street | 3 | ODD |
| C | Madison Avenue, Pine Street | 2 | EVEN |
| D | Mason Avenue, Pine Street | 2 | EVEN |
| E | Pine Street, Randolph Avenue | 3 | ODD |
| F | Pine Street, Tazewell Avenue | 3 | ODD |
| G | Randolph Avenue, Strawberry Street | 4 | EVEN |
| H | Strawberry Street, Tazewell Avenue | 4 | EVEN |
| I | Monroe Avenue, Strawberry Street | 4 | EVEN |
| J | Park Row, Strawberry Street | 3 | ODD |
| K | Madison Avenue, Strawberry Street | 3 | ODD |
| L | Mason Avenue, Strawberry Street | 3 | ODD |
| M | Park Row (dead end) | 1 | ODD |
| N | Peach Street, Randolph Avenue | 4 | EVEN |
| O | Peach Street, Tazewell Avenue | 3 | ODD |
| P | Madison Avenue (dead end) | 2 | EVEN |
| Q | Mason Avenue, Peach Street | 3 | ODD |
| R | Peach Street, Tazewell Avenue | 3 | ODD |
| S | Mason Avenue, Peach Street | 3 | ODD |
| T | Peach Street, Randolph Avenue | 4 | EVEN |
| U | Plum Street, Randolph Avenue | 3 | ODD |
| V | Plum Street, Tazewell Avenue | 3 | ODD |
| W | Plum Street (mid-block) | 2 | EVEN |
| X | Plum Street (mid-block) | 2 | EVEN |
| Y | Madison Avenue, Plum Street | 2 | EVEN |
| Z | Mason Avenue, Plum Street | 2 | EVEN |

Total Practice Block street mileage: 2.4636 mi [S3]. Odd-degree count: 14 of 26. [S3]

## Appendix C — Practice Block Shortest-Path Distances (Odd Vertices Only)

Straight-line-along-street shortest-path mileage between every pair of the Practice Block's 14 odd
vertices, computed over the Practice Block's own street segments (Appendix B). Distances a student
does not need for a valid pairing are included deliberately — not every pair needs to appear in
your matching.

| | A | B | E | F | J | K | L | M | O | Q | R | S | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** | — | 0.0000 | 0.1189 | 0.0644 | 0.1478 | 0.1671 | 0.1553 | 0.2417 | 0.1076 | 0.1857 | 0.1076 | 0.1857 | 0.1937 | 0.1288 |
| **B** | 0.0000 | — | 0.1189 | 0.0644 | 0.1478 | 0.1671 | 0.1553 | 0.2417 | 0.1076 | 0.1857 | 0.1076 | 0.1857 | 0.1937 | 0.1288 |
| **E** | 0.1189 | 0.1189 | — | 0.0545 | 0.1004 | 0.1610 | 0.0365 | 0.1839 | 0.0532 | 0.0668 | 0.0532 | 0.0668 | 0.0748 | 0.0099 |
| **F** | 0.0644 | 0.0644 | 0.0545 | — | 0.0834 | 0.1027 | 0.0909 | 0.1773 | 0.0432 | 0.1213 | 0.0432 | 0.1213 | 0.1293 | 0.0644 |
| **J** | 0.1478 | 0.1478 | 0.1004 | 0.0834 | — | 0.0335 | 0.0713 | 0.0939 | 0.1298 | 0.1852 | 0.1298 | 0.1852 | 0.1652 | 0.1103 |
| **K** | 0.1671 | 0.1671 | 0.1610 | 0.1027 | 0.0335 | — | 0.1047 | 0.1274 | 0.1631 | 0.2186 | 0.1631 | 0.2186 | 0.1986 | 0.1437 |
| **L** | 0.1553 | 0.1553 | 0.0365 | 0.0909 | 0.0713 | 0.1047 | — | 0.0227 | 0.0897 | 0.1032 | 0.0897 | 0.1032 | 0.1112 | 0.0463 |
| **M** | 0.2417 | 0.2417 | 0.1839 | 0.1773 | 0.0939 | 0.1274 | 0.0227 | — | 0.1761 | 0.2316 | 0.1761 | 0.2316 | 0.2116 | 0.1567 |
| **O** | 0.1076 | 0.1076 | 0.0532 | 0.0432 | 0.1298 | 0.1631 | 0.0897 | 0.1761 | — | 0.0589 | 0.0000 | 0.0589 | 0.0669 | 0.0120 |
| **Q** | 0.1857 | 0.1857 | 0.0668 | 0.1213 | 0.1852 | 0.2186 | 0.1032 | 0.2316 | 0.0589 | — | 0.0589 | 0.0000 | 0.0080 | 0.0630 |
| **R** | 0.1076 | 0.1076 | 0.0532 | 0.0432 | 0.1298 | 0.1631 | 0.0897 | 0.1761 | 0.0000 | 0.0589 | — | 0.0589 | 0.0669 | 0.0120 |
| **S** | 0.1857 | 0.1857 | 0.0668 | 0.1213 | 0.1852 | 0.2186 | 0.1032 | 0.2316 | 0.0589 | 0.0000 | 0.0589 | — | 0.0080 | 0.0630 |
| **U** | 0.1937 | 0.1937 | 0.0748 | 0.1293 | 0.1652 | 0.1986 | 0.1112 | 0.2116 | 0.0669 | 0.0080 | 0.0669 | 0.0080 | — | 0.0549 |
| **V** | 0.1288 | 0.1288 | 0.0099 | 0.0644 | 0.1103 | 0.1437 | 0.0463 | 0.1567 | 0.0120 | 0.0630 | 0.0120 | 0.0630 | 0.0549 | — |

All values in miles, [S3]. A distance of 0.0000 means the two vertices are effectively the same
corner (opposite sides of one intersection).

## Appendix D — Official Full-Grid Numbers (Both Options)

| | Option A — The Closed Loop | Option B — The Trailer Return |
|---|---|---|
| Repeat mileage required | 1.5155 mi [S3] | 1.1882 mi [S3] |
| Total mileage driven | 8.8400 mi [S3] | 8.5127 mi [S3] |
| Deadhead ratio (driven ÷ serviced) | 1.2069 | 1.1622 |
| Odd vertices paired | all 34 | 32 of 34 (2 left as start/end) |
| Unmatched start/end pair | n/a — closed circuit | dead end of Monroe Avenue near the harbor side & the north end of Strawberry Street [S3] |

**How this appendix was built.** Both figures come from the same computation applied to the full
68-vertex, 102-edge grid in Appendix A: the minimum-weight matching of all odd-degree vertices
using shortest-path distances between them (an exact optimum via a blossom-algorithm matching, not
a heuristic or hand-estimate) [S3]. For Option A, every one of the 34 odd vertices is paired. For
Option B, every possible single pair of odd vertices was tested as the route's unmatched start/end
corners, and the pair whose removal minimizes the remaining matching cost was kept — the dead end
of Monroe Avenue and the north end of Strawberry Street, the two corners farthest from the rest of
the odd-vertex cluster. This case treats Truck 4's daily start point as already flexible near the
yard each morning (SEE APPENDIX F, MA3); Option B only changes which single corner the flatbed
hauler needs to retrieve the truck from.

## Appendix E — Cost Data

| Figure | Value |
|---|---|
| Refuse-vehicle fuel economy | 5.2392 mpg (gasoline-gallon-equivalent) [S1] |
| U.S. average on-highway diesel price | $5.967 / gal, week of 2026-09-07 [S2] |
| Fuel cost per mile driven | $1.1391 / mi (computed: $5.967 ÷ 5.2392) |
| Flatbed hauling fee, Option B only | $115 / collection day [S6, MA4] |
| Refuse/recyclable collector mean wage (for reference; identical under both options) | $22.99 / hr [S5] |

Fuel cost per mile is a derived figure: diesel price divided by fuel economy, both cited above.
Denise's crew is paid the same wage either way — the flatbed hauler is a separate contracted
service, not a change to the crew's own hours — so wage cost is not part of the comparison in D5,
included here only as reference context your pitch may cite.

## Appendix F — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The Bay Fruit Streets grid's identity | Modeled using the real, public street layout of the historic downtown grid of Cape Charles, Virginia (OpenStreetMap contributors, ODbL license) as a structural stand-in for the fictional town of Averyton's Bay Fruit Streets district | Averyton is fictional, so no real street-network data exists for it. Cape Charles is a real, small, historically-platted coastal town with a genuinely irregular grid — the kind of authentic dead-end and T-intersection irregularity a hand-drawn grid could not honestly provide — and its full network is public and directly downloadable via the Overpass API. | The entire case — the 34-odd-vertex count, both deadhead ratios, the specific best open-path pair — depends on this specific real network's actual topology. A different real town would give different numbers, though the qualitative finding (a real street grid has plenty of odd-degree corners, and relaxing the closed-circuit requirement produces a real but modest repeat-mileage improvement) reflects a general graph-theory pattern, not an artifact of this one town. |
| MA2 | District boundary treatment | Old Cape Charles Road, Bayshore Road, Marina Road, and Harbor Street — four OSM-mapped segments extending toward the marina and the highway — were excluded from the grid | These streets are real pavement, but OpenStreetMap draws them running well past any sensible reading of a compact downtown recycling route, similar to any real route supervisor's district having a boundary drawn somewhere. | Vertices where an excluded segment used to continue are treated as this district's own edge, not literal dead ends. This does not change the odd/even parity of any vertex that remains in-district. |
| MA3 | Truck 4's daily start point | Treated as already flexible and near the Public Works yard each morning; only the route's single END corner is optimized between options | The case does not model a specific yard address outside the mapped grid, so it holds the start point constant across both options and lets only the deliberately-relaxed constraint (must the truck also END back at the yard) vary — which is the actual mathematical difference between an Euler circuit and an Euler path. | If the yard were instead modeled at a fixed, specific corner inside the grid, the exact best open-path pair could shift, though the general result (relaxing the return requirement removes some, not all, repeat mileage) would not. |
| MA4 | Flatbed hauling fee | $115 per collection day, Option B only | No public rate exists for a same-day in-town flatbed pickup of a loaded municipal collection truck specifically. 2026 published flatbed-towing rates for a standard vehicle run $75–150 for the hookup fee plus $3.50–7.00 per mile [S6]; this case uses a value near the low end of that hookup-fee range, since the in-town return leg from either candidate end corner to the yard is short. | This is the swing figure between the two options' raw dollar totals — the case is sensitive to it, but not to its exact direction: even a Trailer Return fee cut in half remains far larger than the fuel savings it is meant to offset (SEE Appendix E). |

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Refuse-vehicle fuel economy | 5.2392 mpg (gasoline-gallon-equivalent) | U.S. DOE Alternative Fuels Data Center — [Average Fuel Economy by Major Vehicle Category](https://afdc.energy.gov/data/10310) (FHWA Highway Statistics 2024) | 2024 | HIGH |
| S2 | U.S. average on-highway diesel price | $5.967/gal | U.S. EIA — [Gasoline and Diesel Fuel Update](https://www.eia.gov/petroleum/gasdiesel/) | week of 2026-09-07 | HIGH |
| S3 | Bay Fruit Streets street-network graph and all derived figures (Appendices A, B, C, D) | 68 vertices; 102 edges; 7.3245 mi; 34 odd vertices; closed 1.5155 mi repeat / 8.8400 mi driven / 1.2069 ratio; open 1.1882 mi repeat / 8.5127 mi driven / 1.1622 ratio | OpenStreetMap contributors — Cape Charles, VA street data via the [Overpass API](https://overpass-api.de/api/interpreter) | fetched 2026-09-09 | HIGH |
| S5 | Refuse/recyclable collector mean wage (reference only) | $22.99/hr | U.S. Bureau of Labor Statistics — [OEWS May 2023, 53-7081](https://www.bls.gov/oes/2023/may/oes537081.htm) | May 2023 | HIGH |
| S6 | Flatbed towing rate range (basis for MA4) | $75–150 hookup + $3.50–7.00/mi | TowingServiceHub — [Flatbed Towing Cost 2026](https://towingservicehub.com/blog/flatbed-towing-cost) | 2026 | MEDIUM |

All figures above were fetched live on the accessed date shown; a dead link should be treated as
link rot, not as a reason to doubt the figure, since every load-bearing number is reproduced
in-document in Appendices A–E.

## Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Graph (Vertices And Edges)
- Vertex
- Edge
- Path
- Cycle
- Weighted Graph

**"How to…" questions**

- How to determine whether a graph has an Euler path or circuit
- How to find the shortest path between two vertices in a weighted graph
