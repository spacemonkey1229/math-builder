# Research Log — The Mooring Choice

Concept sheet (`CONCEPTS_oceanography_2026-09-11.md`, C3) graded data feasibility MEDIUM and flagged
that no specific buoy/anchor spec document had been confirmed live. This session's research
confirmed that remains true: NDBC's public FAQ (`ndbc.noaa.gov/faq/hull.shtml`) names real hull
families (6-meter NOMAD spar, 3-/10-/12-meter discus) but does not publish exact dimensions, and no
public pyramidal-sinker spec sheet was found. The case was built accordingly: real material prices
and physical densities are SOURCED; hull and sinker *dimensions* are disclosed Modeling Assumptions
scaled to the real, named NDBC size class.

| # | Searched for | Found | Outcome |
|---|---|---|---|
| P01 | NDBC mooring sinker pyramid dimensions/weight spec | General boating-forum discussion of concrete mooring blocks (thehulltruth.com, sailboatowners.com); no NDBC-specific sinker spec sheet | NOT FOUND (load-bearing) — recommended exit: Modeling Assumption (MA5), informed by NDBC's own general confirmation that pyramidal sinkers are a real mooring-hardware category (S7) |
| P02 | NDBC 6-meter NOMAD spar hull dimensions (diameter, height) | NDBC's own hull FAQ confirms the hull exists and describes it qualitatively ("aluminum-hulled, boat-shaped," "no known capsizings") but no dimensioned drawing; a linked AOML PDF (`Nomadwebsite.pdf`) fetched but returned unreadable/encoded content | NOT FOUND (load-bearing) — recommended exit: Modeling Assumption (MA2), scaled to the real "6-meter" size class NDBC itself names (S6) |
| P03 | Current structural steel price, 2026 | Gordian's Steel Price Updates page: $2,660.55/ton, July 2026, explicitly labeled a national-average reference | SOURCED — S1, MEDIUM (aggregator/cost-estimating firm, not a single mill's own price sheet) |
| P04 | Density of steel | The Engineering ToolBox: 7,850 kg/m³ | SOURCED — S3, HIGH (standard engineering reference) |
| P05 | Ready-mix concrete price per cubic yard, 2026 | ConcreteNetwork.com: $179.95/yd³ national average | SOURCED — S4, MEDIUM (industry trade-info site) |
| P06 | Density of reinforced concrete | The Engineering ToolBox: 2,240–2,400 kg/m³ range for normal-strength concrete | SOURCED — S5, HIGH; case uses 2,400 (denser end, appropriate for reinforced) |
| P07 | Density of seawater | Wikipedia's Seawater article: 1,025 kg/m³ (1.025 kg/L), corroborated by NOAA-adjacent sources found in the same search pass (a direct NOAA oceanservice.noaa.gov density page 404'd this session) | SOURCED — S2, MEDIUM |
| P08 | Real basis for why a spherical mooring buoy needs added ballast | No specific published spec found; general naval-architecture principle (sphere lacks a natural low center of gravity a spar's shape provides) is well established but no single citable dollar/fraction figure exists for this exact buoy | NOT FOUND (load-bearing) — recommended exit: Modeling Assumption (MA6), flagged HIGH sensitivity, swept in `sensitivity_model.py` |

## Redesign note

The concept sheet's original framing implied the case might rest on a single found spec sheet for
both the buoy and the sinker. Neither was found live this session (confirmed, not assumed —
P01/P02/P08 above record genuine search attempts). Rather than drop the case, it was built the way
`case-research`'s own worked example (SKILL.md §"Worked example") recommends for exactly this
situation: keep the real, sourced material prices and physical constants (which *are* publicly
available and load-bearing), and disclose the geometric dimensions as stated Modeling Assumptions
scaled to a real, named reference size class — rather than either fabricating a fake spec-sheet
citation or abandoning the case.

## Verification

All 7 `sources[]` entries (S1–S7) were fetched directly this session (2026-09-18) via WebFetch;
each figure quoted in `case.json` was read from the fetched page content, not from memory. Two
fetch attempts failed outright (a direct NOAA density page, 404; an AOML-hosted NOMAD PDF, returned
unreadable binary/encoded content) and are recorded above as genuine NOT FOUND outcomes, not
silently retried into a different, unverified number.
