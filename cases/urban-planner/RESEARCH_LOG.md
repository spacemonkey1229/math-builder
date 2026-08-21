# Research Log — Urban Planner

Stage 3 (`case-research`). This case was written with **zero** placeholders left in the source
material's own numbers, because the original docx (`Case Study_ City Planner.docx`) had almost no
load-bearing data of its own — its site appendices (C/D/E) were empty except for each site's name.
Every figure below was researched fresh via WebSearch/WebFetch on 2026-08-20, not pulled from the
source docx.

## P01/P02 — City Hall coordinates and the degree-to-mile conversion

Searched: `Portland City Hall address coordinates 1221 SW 4th Avenue latitude longitude`. Found via
a Google Maps listing: 45.515014°N, 122.679122°W (S1). The degree-to-mile conversion (1° lat ≈
69.0 mi, 1° lon ≈ 69.172 × cos(lat) mi) is a standard NOAA/USGS small-area planar approximation
(S2), not specific to this case — verified against the Wikipedia "Geographic coordinate system"
article's "Length of a degree" section.

## P03 — Westmoreland Park coordinates

Searched and fetched Wikipedia's "Westmoreland Park" article directly: 45.47056°N, 122.63972°W
(S3), citing Portland Parks & Recreation. Graded MEDIUM (secondary republication of a primary GIS
coordinate, but the coordinate itself is unambiguous and current).

## P04 — Hayden Island coordinates and total area

Searched and fetched Wikipedia's "Hayden Island, Portland, Oregon" article directly: 45.61190°N,
122.67606°W, total neighborhood area 1.69 sq mi (S4). Graded MEDIUM (secondary; area traces to
standard Census gazetteer convention for a named place, not a specific parcel survey).

## P05 — Hayden Island road distance (sanity-check figure only)

A WebSearch synthesis attributed "nine miles north of downtown Portland" to hayden-island.com,
a community overview site with no visible date or stated methodology. Graded LOW and used **only**
as a sanity check against the case's own computed straight-line distance (6.69 mi) — case.md
explicitly explains why a road-distance figure should come out larger than a straight-line one, so
students are not confused by the gap. Never used as a load-bearing input to any deliverable.

## P06/P07 — Westmoreland Park and Eastmoreland Golf Course acreage

Fetched the official City of Portland parks pages directly:
- `portland.gov/parks/westmoreland-park` → 43.09 acres (S6). HIGH — primary publisher.
- `portland.gov/parks/eastmoreland-golf-course` → 138.50 acres (S7). HIGH — primary publisher.
An earlier Wikipedia figure for Westmoreland Park (42.01 acres) conflicted slightly with the
portland.gov figure; the primary-publisher figure (43.09, portland.gov) was used per the source
tier-priority rule (skills/case-research/SKILL.md §2).

## P08 — Real reference density for capacity estimation

This was the hardest figure to source. Searched several framings for "Safe Rest Village capacity
per acre" with no direct hit — no source publishes a density figure. Redesigned the search to find
a real, individual built site's size *and* capacity, then compute the density myself: fetched
`portland.gov`'s official SE Reedway Safe Rest Village page directly, which states "approximately
130,000 square feet" and "120 sleeping units" (S8). This is the case's real reference density
(40.21 units/acre, derived, shown as such in case.md Appendix C) — a genuine tier-1 primary source
for both inputs to the derivation, not an estimate.

## P09/P10/P11 — Program budget, village count, average capacity

- Fetched `portland.gov/council/documents/report/accepted/864-2023` directly (an official accepted
  city council report): total program budget $56.3 million, 2021–2024 (S9). This document also
  states FY2022–23 total expenses of $19.9 million across three categories (Acquisition &
  Construction / Site Maintenance / Shelter Operations) — noted but not used in this case's
  arithmetic, since it does not isolate build-out cost from operating cost.
- A WebSearch synthesis reported a per-site cost breakdown ($350k–500k site development,
  $130k–200k service structures, $1.5–3M/yr operating) attributed to unnamed sources; attempted to
  verify this against the primary council document (864-2023) directly and it was **not present
  there** — the council report gives only the aggregate $56.3M figure. Per the "never cite a source
  you did not fetch" rule, this per-site breakdown was **not used**; the case instead derives a
  single cost-per-resident-unit rate from the two figures that *were* independently verified (S9,
  S11), which is a more defensible (if coarser) real number.
- Fetched Portland Mercury's "Portland Leaders Unveil Locations for All Six Safe Rest Villages"
  directly: confirms 6 villages were originally authorized (S10). MEDIUM (news reporting on a city
  announcement, not the council document itself, but a named, dated, specific source).
- Fetched Portland Tribune's "Multnomah Safe Rest Village could become Portland's largest"
  directly: "Portland's eight camps average 49 sleeping pods, with the largest having 60" (S11).
  MEDIUM (news reporting citing city program data). Note: the program had grown to 8 camps by the
  time of this November 2023 article, more than the original 6 the $56.3M budget (S9) was
  authorized for — this case uses the original 6-village authorization consistently with S9's own
  budget period, and states this explicitly in S10's `note` field so the mismatch is visible rather
  than smoothed over.

## P12 — Current federal mileage rate

Searched `IRS standard mileage rate 2026 business rate per mile` and fetched the IRS newsroom
release directly: the rate started 2026 at 72.5 cents/mile and was raised mid-year to 76 cents/mile
effective July 1, 2026 (S12). Per SPEC §5's "still-changing real entity" rule, the case states the
effective date explicitly and uses the current (higher, more recent) rate rather than an
unqualified "the IRS rate."

## Rejected / not used

- A per-village cost breakdown ($350k–500k development + $130k–200k structures) — could not verify
  against a primary source after a direct fetch of the likely originating council document; dropped
  rather than cited on a secondary aggregator's word alone (see P09–P11 above).
- KOIN and Axios articles on the Safe Rest Village annual report (resident counts served) — both
  returned HTTP 403 on direct fetch and were not used for any load-bearing figure.
- birdallianceoregon.org's West Hayden Island page — returned HTTP 403 on direct fetch. The related,
  real fact that West Hayden Island's undeveloped northwest portion is mostly floodplain/wetland
  habitat (confirmed instead via OPB's 2025 article on the West Hayden Island conservation easement
  and hayden-island.com's own description of the island's levee-protected geography) is used only
  as the **facilitator-only twist** in FACILITATOR.md/sensitivity_model.py — it is not a case.md
  figure and does not require the same sourcing rigor as a student-facing appendix number, but its
  factual basis is real, not invented.

## Summary table

| Placeholder | Value | Confidence | Source |
|---|---|---|---|
| P01 City Hall coords | 45.515014, -122.679122 | HIGH | Google Maps |
| P02 degree-to-mile conversion | 69.0 / 69.172×cos(lat) | HIGH | NOAA/USGS convention |
| P03 Westmoreland Park coords | 45.47056, -122.63972 | MEDIUM | Wikipedia |
| P04 Hayden Island coords + area | 45.61190, -122.67606; 1.69 sq mi | MEDIUM | Wikipedia |
| P05 Hayden Island road distance | ~9 mi | LOW (sanity check only) | hayden-island.com |
| P06 Westmoreland Park acreage | 43.09 ac | HIGH | portland.gov |
| P07 Eastmoreland Golf Course acreage | 138.50 ac | HIGH | portland.gov |
| P08 Reedway SRV size + capacity | 130,000 sq ft; 120 units | HIGH | portland.gov |
| P09 SRV program budget 2021-24 | $56.3M | HIGH | portland.gov council doc 864-2023 |
| P10 villages originally authorized | 6 | MEDIUM | Portland Mercury |
| P11 average village capacity | 49 pods | MEDIUM | Portland Tribune |
| P12 2026 federal mileage rate | $0.76/mi (from Jul 1) | HIGH | IRS.gov |

**NOT FOUND count: 0.** Every placeholder was either sourced directly (11 of 12) or resolved as a
declared Modeling Assumption where no public figure exists (developed-footprint percent, resident
occupancy per unit, the "northwest half" split, shuttle frequency, the flat cost-per-unit
application, and the example scoring weights — Appendix F, MA1–MA6). Next step: `case-readiness`.
