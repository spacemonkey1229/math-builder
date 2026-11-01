# Research Log — The Odd Lot

One row per placeholder that existed during authoring. Five real-data placeholders were SOURCED;
four operational/geometric placeholders returned NOT FOUND after a genuine search attempt and
became disclosed Modeling Assumptions (Appendix F). No fourth outcome was used.

| # | Placeholder | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Real basis for why cities have irregularly-shaped blocks like this case's assemblage | Searched "Broadway diagonal creates irregular triangular blocks Manhattan grid history"; fetched Museum of the City of New York's "Broadway and Its Bowties" (The Greatest Grid exhibit) page directly | Confirms the real, well-documented pattern: Broadway, a pre-grid road, cuts across the 1811 Manhattan grid and created the triangular/irregular blocks that became Union Square, Madison Square, Herald Square, Times Square, and Columbus Circle | **SOURCED** — S1, HIGH. Used for Appendix A's real-world grounding, not as a source for this case's own (constructed) parcel geometry. |
| P02 | Maximum FAR (floor area ratio) for a real residential zoning district | Searched "NYC zoning resolution R7-2 maximum floor area ratio FAR residence district table"; fetched NYC's official Zoning Resolution Section 23-22 page directly (zr.planning.nyc.gov) | R7-2 standard maximum residential FAR = 3.44 (5.01 with qualifying affordable/senior housing, not used in this case) | **SOURCED** — S2, HIGH. Direct primary .gov-equivalent source, fetched and read. |
| P03 | Required yard depth for a real residential zoning district | Searched "NYC zoning resolution required side yard rear yard depth R7 R8 district feet"; fetched NYC's official Zoning Resolution Section 24-36 page directly | R7 and R8 districts require a rear yard depth of not less than 30 feet at every rear lot line | **SOURCED** — S3, HIGH. Direct primary source, fetched and read. This is the case's single most load-bearing real citation. |
| P04 | Minimum area of a public plaza earning a real zoning bonus | Searched "NYC zoning resolution public plaza minimum area square feet bonus floor area requirement"; fetched NYC's official Zoning Resolution Section 37-712 page (via a related search result) directly | A public plaza shall contain an area of not less than 2,000 square feet (larger minimums apply in certain Special Districts, not used here) | **SOURCED** — S4, HIGH. Direct primary source. The case does not use the real floor-area bonus RATE (also found: 3.5 sq ft of bonus floor area per sq ft of plaza in most areas) in its arithmetic — only the minimum size threshold — to keep the deliverable's scope to one real, checkable number rather than adding an unused second calculation. |
| P05 | Average size of a new apartment unit, a real U.S. city | Searched "average square footage new NYC apartment unit size housing 2024 2025 report"; fetched RentCafe's "National Average Apartment Size" article directly | The fetched page confirmed a Brooklyn figure (714 sq ft) sourced to Yardi Matrix, dated 2026; a Manhattan figure appeared in the initial web-search summary but was **not** present in the article's actual fetched content | **SOURCED** — S5, HIGH, using ONLY the directly-confirmed Brooklyn figure (714 sq ft/unit). The Manhattan number from the search-engine summary was excluded — per case-research discipline, a figure that could not be independently verified via direct fetch is not cited, even when a search summary reports it. |
| P06 | A specific real address's exact surveyed parcel geometry for an assemblage matching this case's premise | Considered querying NYC's MapPLUTO/PLUTO parcel dataset (Socrata API, data.cityofnewyork.us) for a real irregular block; a direct API query attempt returned an empty result for the specific filter tried | Not pursued further — see rejection note below | **NOT FOUND (not pursued to a conclusion) → REDESIGN.** Rather than force a specific real parcel's data into a case that needs particular clean, tractable numbers for MS/HS arithmetic, the case uses a constructed scenario (MA1) explicitly grounded in the real, cited general pattern (S1) instead of one specific real surveyed address. This is a redesign decision (per case-research's third NOT FOUND exit), made deliberately rather than defaulting to a possibly-misleading precision from a real address whose specific dimensions were never actually confirmed. |
| P07 | Standard permit-review and zoning-lot-merger timelines for a real city | Searched for published municipal review-timeline data; general "how long does X take" guidance exists on many planning-department websites but nothing gave a clean, citable, comparable pair of figures for "standard permit review" vs. "lot-merger filing" specifically | Not found | **NOT FOUND → ASSUMPTION.** MA3 (6 months / 18 months), disclosed in Appendix F. |
| P08 | A single universal housing-production planning horizon used across cities | Searched for standard planning-horizon lengths; many real long-range housing plans exist (5-year, 10-year, and longer), but no single figure is "the" correct one to cite as universal | Not found (as expected — no universal figure should exist) | **NOT FOUND → ASSUMPTION.** MA4 (10 years base, disclosed twist to 5 years), disclosed in Appendix F. |

## Rejections worth recording (so the next pass doesn't re-run these)

- **NYC's MapPLUTO/PLUTO dataset via the Socrata API** (`data.cityofnewyork.us/resource/64uk-42ks.json`)
  is real and genuinely live (confirmed reachable), but a specific `$where` filter tried during this
  research (`address like '%FLATIRON%'`) returned an empty result set — likely a filter-syntax or
  field-name issue, not evidence the dataset itself is unavailable. A future pass wanting to ground a
  case in one specific real parcel's PLUTO data should query by borough+block+lot (BBL) rather than a
  free-text address match, and should confirm the exact field names via the dataset's own metadata
  endpoint first.
- The Flatiron Building (17,707 sq ft triangular parcel, per Wikipedia) was considered as a real,
  famous, citable irregular-parcel example, but a **triangle** does not exercise this case's target
  skill cluster (`irregular-polygon`, `convex`, `concave`, `regular-polygon`, the interior-angle-sum
  theorem) nearly as well as a parcel with more sides does — a triangle's interior angles trivially
  sum to 180° by a rule most students already know, and a triangle cannot be concave. Rejected in
  favor of the constructed pentagon/hexagon/pentagon partition, which forces every targeted skill
  genuinely (see LEARNING_GOALS.md).
- A specific NYC intersection or block was deliberately **not** named as a literal real address for
  this case's assemblage, to avoid implying a level of site-specific precision (exact parcel
  boundaries, exact ownership) this case does not actually have real data for — consistent with
  `domains.json`'s own urban-planning note that "if a case is set in a specific small municipality,
  expect to substitute a comparable city or state it as a constructed scenario," applied here even
  though NYC itself is far from small, because the specific ASSEMBLAGE is what would be overclaimed,
  not the city's general zoning rules (which ARE real and cited).
