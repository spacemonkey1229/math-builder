# Research Log — The Draft Line

All research performed 2026-09-18 via live WebSearch/WebFetch. One row per placeholder from
`case-write`'s 12 `{{NEEDS_SOURCE}}` tokens.

| # | What was needed | Searched / fetched | Found | Outcome |
|---|---|---|---|---|
| P01 | Suez Canal Authority's charted maximum permitted transit draft | WebSearch "Suez Canal Authority maximum permitted draft 2025 2026 meters navigation circular"; WebFetch of the SCA's own Canal Characteristics page | SCA's own page: 66 ft / 20.1 m, tied to a 1,006 m² cross-sectional-area limit; also states this depth lets 100% of container ships transit at full load | **SOURCED** — S1, HIGH. This last fact (100% of container ships already fit) is exactly why the case's scenario vessel's draft is disclosed as an above-limit Modeling Assumption rather than a claim about any real ship's normal operation. |
| P02 | A stated vessel class/TEU capacity for the disclosed scenario vessel | WebSearch for real ULCV classes near 18,000 TEU | Wikipedia's Triple E-class container ship page (18,000 TEU nominal, real, in service since 2013) | **SOURCED (context)** — S2, MEDIUM. Informs MA1's plausible scale; the case's own M/V Coral Meridian is explicitly disclosed as fictional. |
| P03 | Stated laden draft for the scenario vessel | Not independently searched — no public source publishes any real vessel's actual voyage-specific laden draft (commercial, AIS-derived data), consistent with the concept sheet's own explicit call | N/A | **ASSUMPTION** — MA2, set 0.3 m above S1's real 20.1 m limit, disclosed and basis stated (dense-cargo-mix scenario). |
| P04 | Stated draft-change-per-TEU rate | WebSearch "average weight of loaded shipping container TEU tonnes typical statistic" | marineinsight.com / freightamigo.com: typical loaded-container payload commonly cited 15-20 t/TEU | **ASSUMPTION (informed)** — MA3, 0.15 cm/TEU. No public source gives a vessel's exact draft-per-TEU rate; the loaded-weight figures above informed the basis, not a direct citation to this exact combined rate. |
| P05 | Stated/sourced service speed for the scenario vessel | WebSearch "large container ship fuel consumption tons per day at sea 18000 TEU OR 20000 TEU service speed" | Multiple sources report modern ULCV service speeds in the 18-25 knot range; transportgeography.org's fuel-consumption page gives 21 kn / 24 kn data points for an 8,000-TEU class ship | **ASSUMPTION (informed)** — MA4, 20 knots, within the real reported range. |
| P06 | Real published nautical-mile distance, Suez route | WebSearch "Suez Canal distance nautical miles vs Cape of Good Hope Rotterdam Singapore route comparison"; WebFetch of porteconomicsmanagement.org's Shanghai-Rotterdam routing page | 10,600 nm via Suez (16-knot non-stop transit ~27 days, not used directly) | **SOURCED** — S3, HIGH. |
| P07 | Real published nautical-mile distance, Cape route | Same fetch as P06 | 13,800 nm via Cape (16-knot non-stop transit ~35 days, not used directly) | **SOURCED** — S3, HIGH. |
| P08 | Suez Canal toll for a vessel of this class/size | WebSearch "Suez Canal Authority tolls calculator container ship toll USD per TEU"; WebFetch of the SCA's own live Tolls Table page (returned "There is no data to show" — requires interactive vessel-category selection, not a static table); WebFetch of two PDF rate schedules (ISS-Shipping, JICA — both returned unreadable binary/compressed-stream content, not extractable text); WebSearch for reported real dollar toll figures (gCaptain, ICS Shipping — surcharge percentages only, no absolute dollar figures); WebFetch of a secondary trade-analysis blog (Ballast Markets) | Ballast Markets: Suez tolls commonly reported in the $300,000-$800,000 range for 15,000-24,000 TEU container ships | **ASSUMPTION (informed)** — MA5, $650,000. No primary, freely-fetchable rate table could be reached this session — a genuine NOT FOUND at the tier-1/tier-2 source level, consistent with the concept sheet's own MEDIUM-confidence call on this exact figure. Informed by S6 (MEDIUM secondary) as a plausibility range, not cited as if S6 were the primary source. |
| P09 | Stated/sourced fuel consumption rate for the scenario vessel | Same searches as P05; WebFetch of transportgeography.org's dedicated Fuel Consumption by Containership Size and Speed page | An 8,000-TEU containership: ~150 t/day at 21 kn, ~225 t/day at 24 kn, citing Notteboom & Carriou (2009) | **SOURCED (context) / ASSUMPTION (value used)** — S5, HIGH for the cited data point; MA7, 200 t/day, is a disclosed scaled extrapolation for the case's larger 18,000-TEU vessel, not a direct citation. |
| P10 | Real, current fuel-oil spot price usable as a bunker-fuel proxy | WebSearch "EIA petroleum No. 6 fuel oil spot price"; WebFetch of EIA's own U.S. Gulf Coast Ultra-Low Sulfur No. 2 Diesel spot price series (live, HIGH-confidence government data, most recent value $5.206/gal, 2026-09-15); WebSearch for VLSFO/bunker benchmarks; WebFetch of Ballast Markets | EIA's real, dated diesel spot price was found and fetched successfully, but converting it to a per-metric-ton bunker price via a density assumption produced an implausibly high figure (~$1,600/ton) relative to real reported VLSFO prices (~$500-600/ton) — ULSD (a refined, low-sulfur road/rail diesel) is a materially different, pricier product than the heavier blended fuel oil (VLSFO) large ships actually bunker | **REJECTED as primary basis, ASSUMPTION (informed) used instead** — MA6, $600/metric ton, informed by Ballast Markets' real, dated VLSFO benchmark (S6, MEDIUM) instead of the EIA diesel figure. Ship & Bunker (a live bunker-specific index) returned HTTP 403 this session, consistent with the concept sheet's own prior note that this source is bot-blocked. |
| P11 | Real, current average container freight rate per TEU, Asia-Europe lane | WebSearch "Freightos Baltic Index OR Drewry World Container Index average freight rate per FEU Asia Europe current 2026"; WebFetch of Drewry's own live World Container Index page | Drewry's own page: Shanghai-Rotterdam $3,626/FEU, assessment dated 2026-09-17 (one day before this research session) | **SOURCED** — S4, HIGH. Derived to $1,813/TEU via the standard 2 TEU/FEU convention. |
| — | Stated daily vessel operating cost beyond fuel (crew, insurance, schedule risk) | Not independently searched as a load-bearing figure — no public source publishes a specific vessel's daily non-fuel operating cost, which is proprietary fleet-management data | N/A | **ASSUMPTION** — MA8, $25,000/day, disclosed with a general-order-of-magnitude basis. |

## Rejections

- **EIA U.S. Gulf Coast ULSD spot price ($5.206/gal, 2026-09-15)** — real, live, HIGH-confidence government
  data, successfully fetched — but explicitly **not used** as the case's bunker fuel price. Converting it
  to a per-metric-ton figure via a standard density assumption produced ~$1,600/ton, far above real
  reported VLSFO (heavy marine bunker fuel) prices of ~$500-600/ton. Using a refined road/rail diesel
  price as a stand-in for deep-sea bunker fuel would have materially overstated the Cape Diversion's
  real fuel cost disadvantage. Kept only as a documented rejection, not cited in `case.json.sources[]`.
- **A social-media (X/Twitter) post** citing Suez toll figures in the initial search sweep — excluded
  outright, unverifiable provenance, below this project's sourcing floor regardless of plausibility.
- **quartzmountain.org**, a general-content/FAQ aggregator giving a $10-30/TEU and $200,000-500,000
  toll range — found, and not used; no stated author, methodology, or primary citations of its own.
  Ballast Markets (S6) was preferred as a more clearly-dated, named-analysis MEDIUM source instead.
- **Two Suez Canal toll rate-schedule PDFs** (ISS-Shipping's "Transit-Dues-Rates-Schedules.pdf" and a
  JICA report's Chapter 5 toll-structure PDF) — both fetched, both returned unreadable binary/compressed
  stream content rather than extractable text on this session's tooling. Not used; the search effort
  moved to secondary trade-press sources instead, per case-research's "at least two distinct search
  framings and a direct fetch of the most likely primary publisher" bar having been genuinely met and
  exhausted for this figure.

## Status

All 12 `{{NEEDS_SOURCE}}` placeholders closed: 4 SOURCED directly from a primary/HIGH source (S1 draft
limit, S3 both route distances, S4 freight rate), 1 SOURCED-as-context feeding a disclosed assumption
(S2 vessel scale), and 7 disclosed ASSUMPTIONS (MA1-MA8, several informed by real published reference
data per the table above). Zero figures were fabricated or presented as sourced when they were not.
`case.json.status` set to `"researched"`.
