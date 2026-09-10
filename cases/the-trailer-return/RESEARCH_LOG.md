# Research Log — The Trailer Return

One row per placeholder from the original case-write draft: what was searched, what was found,
what was rejected and why.

## P01 — Refuse-vehicle fuel economy (Appendix E)

Searched: DOE Alternative Fuels Data Center refuse-truck category (the same category used by a
prior case as a sweeper-truck proxy — here it is a direct, on-topic match since Truck 4 genuinely
is a refuse/recycling collection vehicle). Fetched `https://afdc.energy.gov/data/10310` live
2026-09-09: 5.2392 mpg (gasoline-gallon-equivalent), FHWA Highway Statistics 2024 Table VM-1.
**FOUND, HIGH confidence.** → S1.

## P02 — Diesel fuel price (Appendix E)

Searched EIA's weekly Gasoline and Diesel Fuel Update. Fetched
`https://www.eia.gov/petroleum/gasdiesel/` live 2026-09-09: $5.967/gal, week of 2026-09-07 (a
real, reported all-time nominal weekly high for U.S. on-highway diesel). **FOUND, HIGH
confidence.** → S2.

## P03 — Real street network for the fictional Bay Fruit Streets grid (Appendices A-D)

No real town named "Averyton" exists (fictional, by design). Selected a real, small, irregular
historic-grid town as a structural stand-in, following the same pattern established by
`cases/the-one-pass-route` (which used Seaside, FL). Chose Cape Charles, Virginia's historic
downtown grid — a real fruit-and-founder-named street grid (Strawberry/Nectarine/Peach/Plum/
Pine/Fig Streets crossing Bay/Mason/Madison/Monroe/Jefferson/Randolph/Tazewell Avenues) — deliberately
a DIFFERENT real town from the one already used by `the-one-pass-route`, to avoid reusing the same
underlying dataset for two published cases.

Geocoded via Nominatim (`nominatim.openstreetmap.org`), then fetched raw way geometry via the
Overpass API (`overpass-api.de/api/interpreter`) for a bounding box covering the named-street grid
(37.2620,-76.0230,37.2720,-76.0100), highway types residential/tertiary/unclassified/living_street
with a name tag, live 2026-09-09. An initial wider query (full admin boundary, then a looser
highway-type filter including `service` roads) returned 341 and then 227/316 vertices/edges —
too large and including golf-resort and service-road clutter well outside a walkable historic grid
— **rejected** in favor of the tighter, named-arterial-only bounding-box query, which produced a
clean 68-vertex, 102-edge connected graph after excluding four segments (Old Cape Charles Road,
Bayshore Road, Marina Road, Harbor Street) that run toward the marina/highway well past the grid
(documented as MA2). **FOUND and derived, HIGH confidence.** → S3.

Vertex/edge collapse, degree computation, and both the closed-circuit (Chinese-Postman-style,
minimum-weight matching of all 34 odd vertices) and open-path (minimum-weight matching after
testing every candidate pair of odd vertices as an unmatched start/end and keeping the cheapest)
mileage computations were run with `networkx`'s exact blossom-algorithm `min_weight_matching` over
all-pairs Dijkstra shortest-path distances — an exact optimum, not a heuristic, matching the
methodology of `the-one-pass-route`. A 26-vertex geographic sub-box (Mason/Madison/Monroe/
Randolph/Tazewell Avenues x Pine/Strawberry/Peach/Plum Streets) was extracted as the Practice
Block and the same computation re-run on it alone for D1/D3/D4's hand-computable scale.

## P04 — Refuse/recyclable collector wage, reference context (Appendix E)

Searched BLS OEWS for SOC 53-7081. The current/index page (`bls.gov/oes/current/oes537081.htm`)
and the May-2025-dated index page both list only download links, not the occupation's own figure,
on the reachable HTML content. Fetched the most recent occupation-specific table with a clean,
directly-readable figure: `https://www.bls.gov/oes/2023/may/oes537081.htm` (May 2023: $22.99/hr
national mean), live 2026-09-09. **FOUND, HIGH confidence, though not the newest possible vintage**
— disclosed in S5's note. Not decisive to the dilemma (the crew is paid identically under both
options in this case's own model), included as reference context only, per case-write's rule
against decorative-but-unused numbers being treated as load-bearing constraints. → S5.

## P05 — Flatbed hauling fee (Appendix E / MA4)

Searched for a municipal-fleet-specific or heavy-collection-vehicle-specific same-day flatbed
hauling rate. **NOT FOUND** — no public rate exists for hauling a loaded municipal rear-loader
specifically; real quotes for this exact service would require contacting a heavy-duty rotator
operator directly, which this session cannot do. Found and fetched a real, dated, live consumer/
light-vehicle flatbed-towing rate range instead: `https://towingservicehub.com/blog/flatbed-towing-
cost`, live 2026-09-09 — $75-150 hookup fee plus $3.50-7.00/mile, 2026. Per case-research doctrine's
three exits for a NOT FOUND on a load-bearing figure, this became a **stated Modeling Assumption**
(MA4: $115/day, near the low end of the real hookup-fee range, given the short in-town return leg),
not a claimed sourced figure — disclosed explicitly in Appendix F with its real basis and honest
caveat that a real quote for this specific, heavier service would likely run higher. **Sensitivity
checked via `sensitivity_model.py`:** flexing this value +/-50% never changes the dollar-lens
winner (Option A remains far cheaper across the whole tested range), so this assumption is
load-bearing to the exact margin but not to either verdict.

## P06 — Second-truck / overtime framing (rejected design, kept for the record)

An earlier design for this case modeled Option B as "lease a second truck and split the zone into
two collection zones," with the dilemma framed around avoiding crew overtime. This was
**rejected before writing case.md**, for an honest, computed reason: splitting the real 68-vertex
grid into two roughly-equal sub-zones by longitude produced COMBINED total driven mileage
(9.4261 mi) that was actually *higher* than the single-truck total (8.8400 mi), and this zone's
real, computed collection time (using a real "194 carts/hour" automated-collection productivity
figure) came to well under an hour even including drive time — nowhere near long enough to
plausibly cross a real overtime threshold at this town's real scale, meaning any dollar comparison
built around avoided overtime would have required inflating fictional numbers disproportionate to
the real network data, which SPEC §5 and case-research doctrine both forbid. The redesign — an
open-path (Euler-path) relaxation of the same single-truck closed circuit, using a real flatbed
hauling service instead of a second crew — kept every real computed figure honest and produced a
genuinely close (3.70%) primary-metric margin without needing to distort any input. This rejection
and its reasoning is preserved here per case-research doctrine's own worked example (§ "Outcome B"),
which treats finding and documenting exactly this kind of redesign as the actual job.

## Verification sweep

```
placeholders remaining in case.md: 0
citation markers with no source row: none (S1, S2, S3, S5, S6 all present in sources[])
source rows never cited in case.md: none
LOW-confidence sources: none (S6 is MEDIUM, used only as an assumption's basis, not load-bearing on its own)
```

Next step: `Run case-readiness on the-trailer-return.` (not run in this session, per task scope).
