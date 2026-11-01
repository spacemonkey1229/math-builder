# Concepts — Urban Planning & Zoning — 2026-09-18

Target picked: **Geometry / Quadrilaterals And Polygons** — the thinnest fully-reachable group for
this domain. A live spine query found **zero** true `n==0` skills left anywhere in the 322-skill
spine (the corpus has no untouched skill remaining as of this run), so per `skills/case-readiness/
SKILL.md`'s reinforcement carve-out, `new_coverage[]` will legitimately be empty with a
`reinforcement_note` for any freshly-authored case today. Ranking below is by thin-skill density
(`n<=4`), cross-checked against `readmodel/domains.json`'s `urban-planning` entry, whose own
`signature_skills` list (`geometry-area`, `geometry-polygon`, `geometry-irregular-polygon`,
`geometry-convex`, `geometry-concave`, …) sits at `n` between 2 and 29 in the live spine — thinner
than the domain sheet's `uncovered_signature_skills: []` implies at a glance, and exactly the
group this file targets.

| Concept | Score | Tier | Thin skills forced (n<=4) |
|---|---|---|---|
| **C1 — The Odd Lot** | 7.8 | T3 | 8 |
| C2 — The Walkshed Park | 5.3 | T2 | 3 |
| C3 — The Lane Conversion | 4.2 | T2 | 2 |

**Recommendation:** write **C1 — The Odd Lot**. It closes the entire thin Quadrilaterals-And-
Polygons cluster relevant to real parcel geometry (`polygon`, `irregular-polygon`, `convex`,
`concave`, `regular-polygon`, the interior-angle-sum theorem and its how-to) with every skill
forced by an actual deliverable — a zoning analyst genuinely has to classify parcel shapes,
verify a surveyed parcel's angles sum correctly, and compute realizable floor area on an irregular
lot versus a consolidated regular one. It also maps directly onto `domains.json`'s own decision
archetype ("upzone the transit corridor... or spread... across low-rise neighbourhoods" is the same
lot-shape-vs-yield tension this case runs at parcel scale) and uses the domain's own HIGH-grade,
live free data sources (NYC's MapPLUTO parcel dataset via Socrata; NYC Zoning Resolution bulk
regulations) directly. Kill C3 (Lane Conversion) — its polygon use (a bike-lane buffer strip as a
long thin rectangle) never actually forces `convex`/`concave`/the interior-angle theorem; it's a
perimeter-and-width problem wearing a polygon-shaped costume.

---

### C1 — The Odd Lot   ·   score 7.8   ·   tier T3

**Protagonist.** Priya Chandrasekaran, zoning analyst in a mid-sized city's Department of City
Planning. She has to sign off on a build-out recommendation for an irregularly-shaped infill
block before the community board meeting, and the number of realizable housing units is what the
board will hold her to.

**The dilemma.** A.) Recommend **Plat As-Is** — subdivide the block along its existing irregular
parcel boundaries (inherited from a pre-grid-era survey), which needs no lot-line changes and can
go to the board immediately OR B.) Recommend **Replat & Consolidate** — merge the irregular
parcels into fewer regular rectangular/near-regular lots, which requires a lot-consolidation
process (owner agreements, a replat filing) that delays the recommendation by months but realizes
more buildable floor area per acre once yard/setback rules are applied to regular versus irregular
(and in places, concave) lot shapes.

**Primary metric.** Realizable dwelling units per acre after required zoning yards/setbacks are
subtracted from each lot's actual buildable footprint.

**Why it's close.** Plat As-Is is faster and touches no existing property lines, but an irregular
or concave parcel loses proportionally more of its area to required setbacks than a regular one
does — a setback is measured perpendicular from every lot line, so a lot with more sides, sharper
interior angles, or a concave notch bleeds more of its interior into the required-yard zone per
square foot of lot area than a compact rectangular lot does. Replat & Consolidate recovers that
lost area but costs real process time, during which the city's housing target clock is still
running — genuinely close once a specific block's real parcel geometry and the city's real bulk
zoning setback figures are in hand.

**Would close (8 skills, 3 how-to / 5 term, n between 2 and 4):**

| id | kind | label | n |
|---|---|---|---|
| geometry-polygon | term | Polygon | 3 |
| geometry-irregular-polygon | term | Irregular Polygon | 3 |
| geometry-convex | term | Convex | 4 |
| geometry-concave | term | Concave | 2 |
| geometry-regular-polygon | term | Regular Polygon | 4 |
| geometry-sum-of-the-interior-angles-of-a-polygon-theorem | term | Sum of the interior angles of a polygon theorem | 3 |
| geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles | how-to | How to find the measure of an interior angle of a polygon given the other angles | 4 |
| geometry-how-to-find-the-area-of-a-regular-polygon | how-to | How to find the area of a regular polygon | 7 |

**Already-covered skills it also exercises (reinforcing):** `geometry-area`, `geometry-perimeter`,
`measurement-ratio`, `measurement-proportion` (floor-area-ratio is literally a ratio/proportion).

**Data feasibility: HIGH.** Named sources I expect to exist: NYC's MapPLUTO / PLUTO parcel
dataset (NYC Department of City Planning, distributed live via NYC Open Data / Socrata —
`data.cityofnewyork.us`) for real lot dimensions, lot area, and lot shape on a real, specific,
irregularly-platted block; the NYC Zoning Resolution's published bulk regulations (required yard/
setback depths by zoning district — a real, citable, stable primary source at
`zr.planning.nyc.gov`) for the setback figures the case's arithmetic actually needs. Not
confident about: the exact per-lot construction/consolidation process cost and timeline (almost
certainly a disclosed Modeling Assumption, since a specific replat's legal/negotiation cost is not
publicly tabulated); this case substitutes a real NYC block for the general "specific small
municipality" case per `domains.json`'s own data-availability note, since NYC is the domain's own
named HIGH-grade source.

**Sensitivity (SPEC §6).** NONE — a zoning capacity decision carries no death/illness/family-
hardship stake.

**Split risk.** NONE — 8 scored skills plus 4 reinforcing is within the honest 8–15 range.

---

### C2 — The Walkshed Park   ·   score 5.3   ·   tier T2

**Protagonist.** A parks-and-open-space planner choosing between siting one large park or four
smaller pocket parks, judged by how many residents fall within a 400 m walk.

**The dilemma.** A.) One large centrally-sited park OR B.) Four smaller pocket parks distributed
across the neighborhood.

**Primary metric.** Residents within a 400 m walkshed per acre of park land.

**Why it's close.** One large park has more total green space per site but a smaller combined
walkshed footprint (walksheds are circles of fixed radius around each site — four smaller circles
cover more distinct ground than one big one, up to the point they'd overlap); pocket parks win on
coverage but lose on economies of scale in park amenities.

**Would close (3 skills):** `geometry-how-to-find-the-area-of-a-circle`, `geometry-radius`,
`statistics-and-probability-population` (residents-within-radius is a population-density
calculation).

**Data feasibility: MEDIUM.** OpenStreetMap gives real building footprints/amenities for walkshed
work but computing actual walk-network distance (not straight-line radius) requires routing
tools beyond this case's scope; a straight-line-radius simplification would need to be disclosed.
Population-within-radius would likely need Census block-group density as a proxy, not exact.

**Sensitivity (SPEC §6).** NONE.

**Split risk.** NONE, but thinner (3 skills) than C1 and its core math (circle area) is a
Perimeter-And-Area skill already at higher `n`, not the genuinely thin Quadrilaterals cluster.

---

### C3 — The Lane Conversion   ·   score 4.2   ·   tier T2

**Protagonist.** A transportation planner deciding whether to convert two travel lanes to a
protected bike lane or keep the lanes and widen the sidewalk instead.

**The dilemma.** A.) Convert two lanes to a protected bike lane OR B.) Keep the lanes, widen the
sidewalk.

**Primary metric.** Square feet of usable public right-of-way reallocated per dollar of
restriping/construction cost.

**Would close (2 skills):** `geometry-perimeter`, `measurement-proportion`.

**Data feasibility: MEDIUM.** Real published bike-lane cost-per-mile figures exist (several DOTs
publish these); sidewalk-widening cost is more scattered.

**Split risk.** On inspection, this concept's polygon shape is a long, thin rectangle — it never
actually forces `convex`, `concave`, or the interior-angle-sum theorem the target group needs.
Killed for this reason; it's a perimeter/rate problem, not a polygon-classification one.
