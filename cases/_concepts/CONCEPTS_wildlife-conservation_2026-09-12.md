# Concept sheet — Wildlife & Biodiversity Conservation (`wildlife-conservation`)

**Target and why.** `readmodel/domains.json`'s `wildlife-conservation` entry is HIGH authoring
priority / HIGH data grade / **0 existing cases** — an untouched domain with the best data
grade in the file. It is also a natural fit for SPEC §6: every one of its own
`decision_archetypes[]` is already framed as protection (acres protected, nests saved, patrols
funded), not destruction, so no reframing was needed.

**A scoring note, cross-checked live this session.** The spine-wide sweep from the oceanography
brief (2026-09-11) holds: **zero skills anywhere in the 437-skill spine are at true `n==0`.**
I re-verified every id below against the live `standards_spine.json` rather than trusting the
domain file or the skill's own worked example — and it's a good thing I did: `domains.json`'s
`signature_skills[]` for this domain (sampling methods, area, perimeter, proportion) are **all
already well-covered** (n=9 to n=27), not thin at all. None of them score. The real gaps this
domain can honestly close sit in **peripheral geometry and probability groups** that a
conservation case can pull in legitimately (triangulation, patch-shape geometry, enclosure nets,
survey-design combinatorics) — scored against `gap_queue.json`'s own `n<=2` thin convention,
every skill below tagged with its live `n`.

| # | Concept | Score | Tier | Group(s) fully thin-closed |
|---|---|---|---|---|
| C1 | The Camera Grid | **5.2** | T3 | Statistics And Probability / Probability (4/15 remaining) |
| C2 | The Patrol Triangle | **5.6** | T2 | Geometry / Triangles (6/10 remaining) |
| C3 | The Ferret Ledger | **4.6** | T3 | Statistics And Probability / Displaying Data (3/14 remaining) |
| C4 | The Holding Pen | **4.2** | T2 | Geometry / Visual Perceptibility (3/11 remaining) |
| C5 | The Corridor Fringe | **2.4** | T2 | none (partial: Quadrilaterals And Polygons, 11/22 remaining) |

**Recommendation.** Write **C2, The Patrol Triangle** first — highest score, HIGH data
feasibility with a confirmed live source, and it closes every remaining thin skill in
Geometry/Triangles outright. **C1, The Camera Grid** is the strongest runner-up and the most
domain-authentic (occupancy-modeling camera-trap design is real wildlife-biology practice) —
write it second. **C3, The Ferret Ledger** has the single best-confirmed data source of the five
(USFWS's own black-footed ferret page, fetched live this session, already carries real
survival-rate numbers) and should follow. Hold **C4** — real but its enclosure-cost source is
still just a category guess. Kill **C5** for this round: no group-closure bonus, and its best
land-cost source (Trust for Public Land) 403'd live; acreage/boundary data is solid (USGS PAD-US,
confirmed live) but per-acre purchase cost is not, so the case's primary metric would rest on an
unconfirmed number.

---

### C1 — The Camera Grid   ·   score 5.2   ·   tier T3

**Protagonist.** Priya Nakamura, a wildlife biologist running an occupancy survey for a state
fish-and-wildlife agency, who has to commit to one camera-trap protocol before the field season's
single funding window closes.

**The dilemma.** A.) Deploy 12 cameras for 60 nights each (fewer independent sampling units, but
each one accumulates many detection opportunities) OR B.) deploy 40 cameras for 18 nights each
across a finer grid (more independent sampling units, but each has fewer nights to register a
detection).

**Primary metric.** Probability of detecting the species at a site over the full survey ÷ dollars
spent per site — because raw detections favor whichever protocol just runs longer, but occupancy
modeling (real wildlife-biology practice: MacKenzie-style detection probability) cares about the
*chance* of missing a species that's actually there, not the total count.

**Why it's close.** Treating each camera-night as an independent event, cumulative detection
probability is `1 − (1 − p)^n`: Protocol A's fewer, longer-running cameras rack up a higher `n`
per site (favors A), but Protocol B's finer grid means more *independent* spatial sampling units
covering ground A's 12 cameras simply don't reach — arranging which grid cells get a camera is a
combinations problem, and rotating a limited camera pool across two sampling passes is a
permutations problem. Neither protocol dominates until both the per-site detection math and the
spatial-coverage math are laid side by side.

**Would close (4 skills, 2 how-to / 2 term, all currently n=2, all of Statistics And
Probability/Probability's remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-independent-event | term | Independent Event | 2 |
| statistics-and-probability-permutation | term | Permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation | how-to | How to determine the number of outcomes of a permutation | 2 |
| statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination | how-to | How to determine the number of outcomes of a combination | 2 |

**Already-covered skills it also exercises.** `measurement-how-to-find-a-missing-amount-in-a-proportion`
(n=12, converting camera-nights and grid cells to a per-site cost); `statistics-and-probability-sample`
/ `population` (n=9 / n=11, framing the surveyed grid cells as a sample of the full habitat).

**Data feasibility: MEDIUM.** Named sources I expect to exist: Snapshot Serengeti / eMammal
camera-trap datasets (Zooniverse-hosted, openly licensed detection records) and published USGS
occupancy-modeling protocols documenting real camera counts, night counts, and per-camera cost. I
did not fetch a live URL for a specific published camera-trap cost-and-detection dataset this
session — the category is well-established in wildlife science, but I have not confirmed one
specific free document, so this stays MEDIUM rather than HIGH. Not confident about: a real
per-camera daily cost figure; likely a stated Modeling Assumption cited to a manufacturer price.

**Sensitivity (SPEC §6).** None required — a survey-design/budget decision, no personal stakes.

**Split risk.** None — 4 scored skills plus reinforcement, well under the 8–15 range.

---

### C2 — The Patrol Triangle   ·   score 5.6   ·   tier T2

**Protagonist.** Derek Osei, a park ranger and patrol-sector lead at a wildlife reserve, who has
to recommend one patrol pattern before the dry-season poaching spike begins.

**The dilemma.** A.) Run the Perimeter Loop — patrol routes shaped as long, narrow scalene
triangles hugging the reserve boundary, covering more edge but leaving the interior thin OR B.)
Run the Interior Web — a denser network of smaller, more equal-sided triangular sectors radiating
from three fixed ranger outposts, covering less total ground per patrol but triangulating any
reported sighting faster.

**Primary metric.** Minutes of ranger travel time to reach a reported incident location, per
square kilometer of reserve actually inside a triangle a patrol covers that day — a ratio, since
the Interior Web's smaller sectors respond faster but the Perimeter Loop's larger ones simply
cover more area per patrol shift.

**Why it's close.** The Perimeter Loop's routes are long scalene triangles — no side or angle
equal, which is exactly why they're efficient at hugging an irregular boundary but slow to
respond from any one point. The Interior Web's sectors are closer to equilateral, which by the
triangle inequality theorem lets three outposts triangulate a sighting's approximate location
fastest when the reporting angles from two posts are known — but three equal-ish sectors leave
real gaps an acute-vs-obtuse comparison of sector shape has to justify. Response time favors B;
ground coverage per patrol-hour favors A.

**Would close (6 skills, all term, all currently n=2, all of Geometry/Triangles's remaining thin
skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-acute-triangle | term | Acute Triangle | 2 |
| geometry-obtuse-triangle | term | Obtuse Triangle | 2 |
| geometry-scalene-triangle | term | Scalene Triangle | 2 |
| geometry-equilateral-triangle | term | Equilateral Triangle | 2 |
| geometry-leg | term | Leg | 2 |
| geometry-triangle-inequality-theorem | term | Triangle Inequality Theorem | 2 |

**Already-covered skills it also exercises.** `geometry-area` (n=11, area of each patrol sector);
`measurement-how-to-find-elapsed-time` (n=12, response-time comparison).

**Data feasibility: MEDIUM–HIGH.** Named sources checked live this session: SMART (Spatial
Monitoring and Reporting Tool, `https://www.smartconservationtools.org/`) — confirmed live,
maintained by an active partnership including WWF, WCS, and Panthera, and explicitly supports
patrol/law-enforcement tracking as a core use case. I could not confirm a specific public dataset
with real patrol-route coverage numbers on that visit (the homepage describes the tool, not a
downloadable dataset), so I am not grading this HIGH. USGS PAD-US
(`https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-overview`) — confirmed
live this session, free national download, gives real reserve boundary/area data to size the
patrol sectors against. Not confident about: real ranger travel-speed and staffing-cost figures —
likely a stated Modeling Assumption.

**Sensitivity (SPEC §6).** Low-level flag: patrol/anti-poaching context implies a human threat
off-page. No casualty math is required or implied — the case is pure coverage geometry — but the
facilitator note should say so explicitly so a discussion doesn't drift into speculating about
confrontations.

**Split risk.** None — 6 skills, one coherent patrol-design deliverable.

---

### C3 — The Ferret Ledger   ·   score 4.6   ·   tier T3

**Protagonist.** Renata Osei, a reintroduction-program biologist for a state wildlife agency,
choosing where to release the next cohort of a captive-bred, endangered species before the
funder's site-commitment deadline.

**The dilemma.** A.) Release the new cohort at Site 1 — an established colony with a longer
track record but more variable year-to-year survival OR B.) release at Site 2 — a newer colony
with a shorter record but visibly tighter survival numbers so far.

**Primary metric.** 12-month post-release survival rate per dollar of monitoring cost — a ratio,
because the site with the higher raw survival count isn't automatically the better choice if it
also costs far more to monitor closely enough to trust that number.

**Why it's close.** A box-and-whisker plot of each site's post-release survival data shows Site
2's numbers cluster tighter (favors trusting B) — but a scatter/best-fit look at survival against
years-since-release shows Site 1's longer record includes a downturn Site 2 hasn't lived long
enough to reveal, which reads as a *non-linear* trend the shorter record can't rule out. The case
turns on recognizing that a tighter recent cluster isn't the same as a longer-proven trend, not on
which site simply "looks better."

**Would close (3 skills, 2 how-to / 1 term, all of Statistics And Probability/Displaying Data's
remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | How to create a box and whisker plot given a set of data | 1 |
| statistics-and-probability-non-linear | term | Non-linear | 2 |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 2 |

**Already-covered skills it also exercises.** `statistics-and-probability-scatter-plot` /
`how-to-create-a-scatter-plot-given-a-set-of-data` (n=9 each); `statistics-and-probability-sample`
(n=9, framing tracked individuals as a sample of the released cohort).

**Data feasibility: HIGH.** Named source confirmed live this session: USFWS's black-footed ferret
species page (`https://www.fws.gov/species/black-footed-ferret-mustela-nigripes`) — fetched live
and already carries real numbers usable as the case's disclosed baseline: Conata Basin, South
Dakota annual survival rates of 70% (juvenile females), 50% (adult females), 38% (males); Shirley
Basin, Wyoming's average of 100 breeding adults (2012); Meeteetse, Wyoming's mean life expectancy
of 0.9 years for the last wild population. Not confident about: a full multi-year, multi-cohort
survival time series for two specific sites in one place — `case-research` will likely need to
assemble the year-by-year distribution from USFWS recovery-program reports rather than finding one
downloadable table, and the case should use a stated, disclosed composite (not a named real site
pair) if the full series can't be sourced cleanly.

**Sensitivity (SPEC §6).** One-line facilitator flag: the case involves animal mortality data
(38–70% survival, i.e., meaningful death rates in a real endangered species). Frame stays on
protection (maximizing survival), consistent with SPEC §6 guidance — no optimization of death
counts as an abstract quantity — but the underlying numbers are real animal deaths and the
facilitator should be told that going in.

**Split risk.** None — 3 skills, small, single deliverable arc.

---

### C4 — The Holding Pen   ·   score 4.2   ·   tier T2

**Protagonist.** Marcus Whitfield, a conservation-program field manager building a soft-release
enclosure for a reintroduction cohort, who has to order fencing material before the cohort arrives
from the breeding facility.

**The dilemma.** A.) Build a rectangular-prism holding pen — simple to fence, familiar to the
crew, but wastes corner space the animals rarely use OR B.) build a hexagonal-prism pen — better
matches the animals' natural range-use pattern (fewer wasted corners) but the crew has never
fabricated hexagonal fence panels and has to work from a cut net/pattern for the first time.

**Primary metric.** Dollars of fencing material per square meter of usable enclosure floor space
— usable space, not total footprint, since corner area animals avoid doesn't count as protection
regardless of which shape "looks bigger" on paper.

**Why it's close.** The hexagonal prism has fewer faces meeting at sharper corners, so more of its
enclosed area counts as "usable" range space — but it has more distinct edges to weld and requires
drawing and cutting an unfamiliar net before fabrication can start, a real labor-time cost the
rectangular design doesn't carry. Counting faces and edges is not decoration here — it's literally
the fence-panel and weld-seam count each design requires.

**Would close (3 skills, 1 how-to / 2 term, all of Geometry/Visual Perceptibility's remaining thin
skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-face | term | Face | 2 |
| geometry-edge | term | Edge | 2 |
| geometry-how-to-draw-the-net-of-a-3-d-shape | how-to | How to draw the net of a 3-D shape | 2 |

**Already-covered skills it also exercises.** `geometry-area` (n=11, usable floor space);
`geometry-how-to-find-the-surface-area-of-a-prism` (n=3, fencing material for the rectangular
option).

**Data feasibility: MEDIUM.** I have not identified and confirmed a specific free source for
enclosure-size standards or fencing costs this session — the category is plausible (USDA APHIS
Animal Welfare Act minimum-enclosure-size regulations are public, and IUCN's Reintroduction and
Translocation guidelines document space recommendations), but I did not fetch a live URL for
either this session, so it stays MEDIUM, not HIGH. Not confident about: real welded-wire fencing
per-linear-foot pricing — likely a stated Modeling Assumption cited to a supplier catalog.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 3 skills, small, single deliverable arc.

---

### C5 — The Corridor Fringe   ·   score 2.4   ·   tier T2   ·   (hold — see Recommendation)

**Protagonist.** Alicia Ferreira, a land trust's acquisition manager, who has one purchase budget
and has to recommend a single parcel before a competing developer's offer expires. (This concept
follows `domains.json`'s own decision archetype #1 almost verbatim: "Buy 900 acres of prime
habitat or 3,200 acres of degraded land that connects two existing reserves.")

**The dilemma.** A.) Buy Parcel 1 — a smaller, oddly-shaped remnant of prime old-growth habitat
with a concave boundary (a chunk already cleared for a old logging road bites into it) OR B.) buy
Parcel 2 — a much larger trapezoidal strip of degraded farmland that would directly connect two
existing reserves into one corridor.

**Primary metric.** Core acres protected (total parcel area minus an edge-effect buffer strip
along the perimeter) per dollar — because raw acreage favors the large degraded parcel
automatically; core, edge-effect-adjusted acreage is the number that actually reflects protected
habitat value.

**Why it's close.** Parcel 1's concave, irregular (five-sided/pentagon-like) boundary means a
larger fraction of its total area sits near an edge, shrinking its core-acreage figure more than
its raw acreage suggests — but it's already prime habitat, needing no restoration. Parcel 2's
long, narrow trapezoidal shape has an even worse edge-to-core ratio per acre, but its sheer size
and corridor-connecting function mean its degraded land will eventually count as protected core
once restored — a timeline argument, not a shape argument, and the case has to keep the two
honest instead of collapsing them into one number.

**Would close (4 skills, all term, none close the group — 4 of Geometry/Quadrilaterals And
Polygons's 11 remaining thin skills):**

| id | kind | label | n |
|---|---|---|---|
| geometry-pentagon | term | Pentagon | 1 |
| geometry-concave | term | Concave | 2 |
| geometry-trapezoid | term | Trapezoid | 2 |
| geometry-n-gon | term | N-gon | 1 |

**Already-covered skills it also exercises.** `geometry-area` (n=11); `geometry-perimeter` (n=6);
`geometry-how-to-find-the-measure-of-the-perimeter-of-a-polygon` (n=6).

**Data feasibility: MEDIUM.** Named sources checked live this session: USGS PAD-US
(`https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-overview`) — confirmed
live, free national protected-area boundary/acreage data, good for sizing real parcel shapes.
The National Conservation Easement Database (`https://conservationeasement.us/`) — confirmed live
but explicitly states it is **no longer actively updated** (as of January 2025) and now points
users to PAD-US instead; its legacy homepage still shows real historical totals (221,256
easements, ~37.98M acres) but is not a source to cite as current. Trust for Public Land's
Land and Water Conservation Fund page returned **HTTP 403 Forbidden** when fetched live — could
not confirm per-acre cost data there. Not confident about: a real per-acre purchase-price figure
for either parcel type — this is the concept's weak point, and without it the primary metric
would rest on an unconfirmed number, which is why this concept is held rather than promoted.

**Sensitivity (SPEC §6).** None required.

**Split risk.** None — 4 skills, but scored low precisely because it does not close its group;
recommend not writing until a real per-acre cost source is found, not splitting.
