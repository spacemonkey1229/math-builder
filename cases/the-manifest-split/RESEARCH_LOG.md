# Research Log — The Manifest Split

case-write left zero `{{NEEDS_SOURCE}}` placeholders as blank numbers; every figure was written
directly as either a citation target or a scenario assumption, per the concept sheet's own
feasibility call (MEDIUM — the classification system is real and public; the actual per-sailing
counts and terminal timing data are not). This log records what was searched for each.

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | The real classification system that makes "hazmat-flagged" a genuine operational category | "IMO IMDG Code hazard classes 1-9 list official" | IMO's own IMDG Code page; corroborated by Wikipedia's "Dangerous goods" article, which cites the Code directly | **SOURCED** — S1, HIGH confidence. Used for Appendix A (context/vocabulary, not load-bearing arithmetic). |
| P02 | A real per-container reefer inspection time, to inform the Split Lanes reefer check assumption | "reefer container plug in inspection time terminal minutes genset check" | Royal Cold Storage's port-pickup pre-trip inspection guide, describing a "five-minute inspection" | **SOURCED (supplemental)** — S2, MEDIUM. A single company blog with no stated author/date is not strong enough to be the load-bearing value itself, so it informs MA5's basis as a plausibility floor rather than being cited as the value used. |
| P03 | A real terminal re-handle/transfer time, to inform the re-handle cost assumption | "container terminal yard crane rehandle move average time seconds minutes"; "container terminal yard crane moves per hour gantry crane productivity benchmark" | Multiple sources converge on ~25-35 (commonly cited "more than 30") yard-crane moves per hour, i.e. a floor of roughly 2 minutes per single crane cycle | **SOURCED (supplemental)** — S3, MEDIUM. A single crane cycle is not the same as a full re-handle (which can include un-stacking, a yard-truck move, and re-queuing at the second lane), so this is used only as a floor informing MA6's basis, not the value itself. |
| P04 | Real, decorative context establishing containerized/maritime shipping's real-world scale, for the Background's texture (non-load-bearing) | "container shipping percent of world trade by volume UNCTAD statistic" | UNCTAD's Review of Maritime Transport 2025: maritime transport carries more than 80% of goods traded worldwide by volume | **SOURCED** — S4, HIGH confidence, from the domain's own live-confirmed UNCTAD source (per the concept sheet's live spot-check). Context only. |
| — | A real, specific per-sailing hazmat/reefer flag-count breakdown for any named terminal | Not searched — per the concept sheet's own assessment (Data feasibility: MEDIUM, "I did not attempt a live check ... I have no single named document to check ... will almost certainly be a disclosed, stated scenario") this is internal gate-scan/operational data no terminal publishes. Two direct attempts in a prior maritime-shipping concept-sheet pass (Port of Los Angeles container statistics, Ship & Bunker) both returned HTTP 403 (bot-blocked), corroborating that terminal-level operational data of this kind is not realistically public. | **NOT FOUND, as expected.** Became MA1 (H=90, R=130, union=195) — a disclosed, stated Modeling Assumption, sized to a plausible mid-sized-terminal scale rather than any real named terminal's actual data. |
| — | A real, specific per-container inspection-time figure for a generalist (dual-certified) crew vs. a specialist (single-purpose) crew, for either the hazmat or reefer check | Same searches as P02/P03; no terminal-operations study distinguishing generalist vs. specialist crew check-time was found | **NOT FOUND.** Became MA2-MA4, disclosed Modeling Assumptions, with MA4/MA5 informed by S2/S3 as floors and MA2/MA3 set higher on the general (not terminal-specific) principle that task-switching between two procedures costs more than single-task specialization. |
| — | A real, dated bulletin naming an exact count of lithium-ion-battery-in-reefer containers reclassified as hazmat, for the FACILITATOR.md twist | Not searched as a load-bearing figure — the underlying regulatory reality (lithium-ion cells are a real IMDG Class 9 category, increasingly shipped refrigerated) is well established and cited via S1, but no single real bulletin naming a specific reclassified-container count for this scenario exists to cite | **NOT FOUND / not applicable as a citation target.** The twist's +30-container reclassification is disclosed in case.json.scenario_constructions as a scenario construction grounded in a real regulatory category, not a citation to one specific real event. |

## Rejections

None of the four sourced claims (S1-S4) were rejected once found. Two candidate sources considered
and NOT used as the primary basis for a load-bearing figure:
- A specific numeric "X minutes per hazmat exam" figure from U.S. CBP customs-exam guides (VACIS:
  24-48 hours; Intensive exam: 5-10+ business days) was found and explicitly rejected as the basis
  for MA2/MA4. Those figures describe a multi-day U.S. Customs and Border Protection compliance
  exam process, not the terminal's own internal placard/documentation verification lane this case
  models — using a multi-day CBP exam duration as a per-container "check time" inside a single
  overnight shift would misrepresent what kind of check this case's lane actually performs.
- RTG (rubber-tired gantry) crane benchmarks in the 240-360-moves-per-hour range (a different,
  much faster crane-span configuration than the "more than 30 moves/hour" figure used) were found
  and not used, since the 30-moves/hour figure is the one consistently cited across sources as a
  general terminal-productivity benchmark, and using the faster RTG-specific figure would overstate
  what a real re-handle involves.

## Status

All figures in case.md are either cited (S1-S4) or disclosed as Modeling Assumptions (MA1-MA6, per
case.json.modeling_assumptions and case.md Appendix D). Zero `{{NEEDS_SOURCE}}` placeholders remain.
`case.json.status` set to `"researched"`.
