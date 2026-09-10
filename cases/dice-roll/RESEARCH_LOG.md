# Research Log — Dice Roll

This case was authored and researched in a single combined pass: every figure was either
live-fetched and cited (below), or, where no public figure exists, disclosed directly in
`case.md`'s Appendix D as a stated Modeling Assumption. No `{{NEEDS_SOURCE}}` placeholder was
ever left unresolved.

## P01 — Colorado's county count

- Searched: "Colorado risk-limiting audit statute 64 counties Secretary of State 2026"
- Fetched: verifiedvoting.org/auditlaw/colorado/ — confirms 64 counties, cites C.R.S. §1-7-515.
- Outcome: SOURCED → S1. HIGH confidence (nonpartisan election-law tracking organization
  citing the Department of State's own figures; county count is a stable fact).

## P02 — The RLA statute itself (requirements, 2017 start date)

- Searched: "Colorado Revised Statutes 1-7-515 risk-limiting audit"
- Fetched: law.justia.com's reproduction of C.R.S. §1-7-515 (2024 codification).
- Outcome: SOURCED → S2. HIGH confidence (a legal-code republication service; cross-checked
  against the Secretary of State's own 2026 press release, below).

## P03 — Every county conducts its own RLA after every statewide election

- Fetched: sos.state.co.us press release, "Colorado Begins Post-Election Audit of 2026 Primary"
  (2026-07-13).
- Outcome: SOURCED → S3. HIGH confidence (primary publisher — the Secretary of State's own
  newsroom).

## P04 — The public dice-roll random-seed process

- Searched: '"risk-limiting audit" Colorado "dice" random seed public roll procedure'
- Fetched: the same 2026-07-13 SOS press release — confirms 20 ten-sided dice rolled publicly,
  each roll one digit of a 20-digit seed, and gives the actual seed used for the 2026 Primary
  (49006417086137856424).
- Outcome: SOURCED → S4. HIGH confidence. Used only as real-world context in Appendix B — the
  case's own Statewide Draw county selection is stated as a separate given fact, not mechanically
  derived from this real seed, to avoid overstating what this teaching exercise reproduces of
  Colorado's actual (far more complex) ballot-level RLA software.

## P05 — Driving distance, Denver to each of the 12 county seats

- Searched two batched queries covering all 12 county seats via TravelMath/Trippy driving-
  distance results.
- Outcome: SOURCED → S5. MEDIUM confidence (aggregated mapping-service lookups, not a single
  government source; standard highway-route driving distance, adequate precision for a mileage
  reimbursement calculation, but not a primary source).
- Rejected: did not attempt a government GIS/DOT source for driving distances — Colorado DOT does
  not publish a point-to-point mileage table, and building one from raw GIS data was out of scope
  for a set of 12 lookups better served by an existing mapping-distance query.

## P06 — 2024 county and statewide population estimates

- Searched: "Colorado county population 2024 census estimates Jefferson Douglas Larimer Boulder
  El Paso total state population"
- Outcome: SOURCED → S6. MEDIUM confidence — figures trace to U.S. Census Bureau Vintage 2024
  estimates but were retrieved via a secondary aggregator (World Population Review / Colorado
  Demographics) rather than fetched directly from census.gov's own table interface. Non-
  load-bearing to the cost balance test; used only for the D6 pie chart.
- Rejected: did not pursue a direct census.gov QuickFacts fetch for all 12 counties individually
  — the aggregator's Vintage-2024-sourced figures were internally consistent and sufficient for a
  non-load-bearing display deliverable.

## P07 — Colorado state mileage reimbursement rate

- Searched: "Colorado state employee mileage reimbursement rate 2026 fiscal rules"
- Attempted fetch: osc.colorado.gov's own fiscal-rules page — returned HTTP 403 to automated
  fetch (blocked).
- Fetched instead: University of Colorado Payroll & Benefit Services blog post reproducing the
  state's own rate and effective date, explicitly citing the state fiscal rule (CRS 24-9-104) and
  the underlying IRS-rate-based formula (90% of the prevailing IRS mileage rate).
- Outcome: SOURCED → S7. HIGH confidence (an official university payroll office's own
  republication of the state's rate, with an exact number and exact effective date, one step
  removed from the blocked primary page).

## P08 — FY2026 federal per diem (lodging + M&IE)

- Searched: "GSA per diem rates 2026 standard CONUS lodging rate FY2026"
- Fetched: gsa.gov's own press release confirming FY2026 rates are unchanged from FY2025,
  effective 2025-10-01 through 2026-09-30 — but the fetched text did not surface the specific
  dollar breakdown.
- Fetched: gsa.gov/travel/plan-a-trip/per-diem-rates directly — same result, dollar figures live
  behind an interactive lookup tool not captured by automated fetch.
- Fetched: perdiemworld.com's GSA-data summary page, confirming $110/night lodging + $68/day
  M&IE for the FY2026 standard CONUS rate.
- Outcome: SOURCED → S8. Split confidence: the "rates unchanged for FY2026" claim is HIGH
  (GSA's own primary release); the specific $110/$68 dollar split is MEDIUM (confirmed only via
  a secondary aggregator, since the primary page's interactive tool wasn't fetchable).

## P09 — Are SRS/systematic/cluster/multistage the standard sampling toolkit? (2026-09-10 clarity pass)

- Prompted by facilitator feedback that the case didn't make clear whether the four sampling
  methods it asks a Hero to use are a standard toolkit or something unusual/case-invented, and
  didn't state the dilemma, the two options, or the relevance of the dice clearly enough near the
  top of the case.
- Searched: "openstax introductory statistics well-known random sampling methods stratified
  cluster systematic", then fetched the matching OpenStax page directly.
- Fetched: openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-
  data-and-sampling — confirms the exact framing: "Other well-known random sampling methods are
  the stratified sample, the cluster sample, and the systematic sample," introduced immediately
  after simple random sampling in the textbook's own sampling-methods section.
- Rejected: an initial attempt to find an election-observation-specific source (OSCE/ODIHR
  methodology, searching for whether real election-monitoring programs use stratified/cluster
  sampling to pick observation sites) did not turn up a citable, specific claim — OSCE's own
  Election Observation Handbook describes deployment as only "pseudo-random" and explicitly not
  standardized. Rather than overclaim that real election-monitoring programs use these methods,
  the case instead cites the general statistics-education framing (these are the standard toolkit
  taught in any first stats course) and explicitly discloses, in the Background text itself, that
  whether Colorado's real Division uses one of these methods for site-visit selection specifically
  is not public record — consistent with the case's existing Modeling Assumption disclosure
  pattern rather than a second, riskier sourcing claim.
- Outcome: SOURCED → S9. HIGH confidence (a primary open-access statistics textbook, directly
  fetched and quoted verbatim).

## Not sourced — stated as Modeling Assumptions (see `case.md` Appendix D)

- **MA1 — overnight threshold (150 mi one-way):** No public Division policy states this cutoff
  for the compliance-monitoring program specifically. Two search framings ("Colorado state
  employee same-day travel policy mileage threshold overnight") returned only general per diem
  eligibility rules, not a specific distance threshold. Declared as a stated assumption with a
  disclosed basis (a ~2.5-hour one-way drive as the practical limit for a same-day round trip
  that still leaves working time to observe an audit session).
- **MA2 — loaded compliance-monitor daily cost ($450/day):** Attempted to source a Colorado
  classified-analyst salary figure via the DHR pay-plan tables (dhr.colorado.gov); the pay-plan
  lookup is an interactive table not captured by automated fetch, and a BLS OEWS search for
  Colorado "Statistician" median wages likewise did not return a specific figure through
  automated search. Declared as a stated assumption consistent with general public-sector
  classified-analyst salary bands, loaded for benefits and overhead. This is the case's single
  most load-bearing assumption (see `sensitivity_model.py` FLEX and `FACILITATOR.md`).
- **MA3 — 5 site visits this cycle:** No public figure exists for the Division's internal
  travel/staff-day budget for this specific monitoring program. Declared as a stated assumption;
  applies identically to both options, so it is not itself a source of bias between A and B.
- **MA4 — 12-county working roster standing in for the full 64-county state:** A scope
  simplification, not a sourced-or-unsourced numeric fact — disclosed directly in Appendix D.

## Supplemental materials gathered

- The real 20-digit RLA seed and dice-roll ceremony (S4) doubles as the case's narrative hook
  (Overview) and as Appendix B's real-world grounding — verified live, not recalled from memory.

## Verification

- `case.md` placeholder count: 0 remaining.
- Every `[S<n>]` marker in `case.md` has a matching row in Appendix E; every Appendix E row is
  cited at least once in the text.
- No LOW-confidence source carries a constraint or a dilemma-flipping quantity; the two MEDIUM
  sources (S5 distances, S6 population, S8's dollar split) are either non-load-bearing (S6) or
  cross-checked against a HIGH-confidence primary fact from the same source family (S8's
  rate-unchanged claim; S5's aggregate figures are internally consistent across two independent
  lookup services).

Next step: run `case-qa` on `dice-roll`.
