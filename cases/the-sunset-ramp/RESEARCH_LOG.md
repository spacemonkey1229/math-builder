# RESEARCH_LOG — The Sunset Ramp

One row per placeholder from `case-write` (15 total, P01–P15), what was searched, what was found
or not, and what was rejected and why.

## P01 — Battery ramp-rate capability / response time

Searched: "grid-scale lithium-ion battery storage response time ramp rate seconds to full power
NREL"; "NREL OR DOE report battery storage milliseconds sub-second full power response frequency
regulation grid-scale lithium-ion"; "FERC OR NERC battery storage full output one second seconds
ramp capability report ancillary services ruling". Fetched: `docs.nrel.gov/docs/fy23osti/85878.pdf`
(DNS failure, unreachable); `nerc.com/globalassets/programs/rapa/ra/master_esat_report.pdf` (HTTP
403); Modo Energy's *Ramp rates in Dynamic frequency response services*, which explicitly states
batteries "can go from zero to full charge or discharge almost instantaneously," corroborated by
multiple frequency-regulation sources citing 100–500 ms response times. **Outcome: SOURCED as S4**,
MEDIUM confidence (a qualitative/order-of-magnitude characterization, not one manufacturer
datasheet). Derived the case's working number — 12,000 MW/min — from a conservative 1-second
full-power assumption, since the exact millisecond figure is not load-bearing to the dilemma (the
battery's binding constraint is its bounded 4-hour duration, not its ramp rate).

## P02 — Solar PV capital cost, USD/kW

Searched: "EIA Capital Cost and Performance Characteristics 2025 solar PV battery storage
combustion turbine peaker overnight capital cost $/kW". Found and fetched
`eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf` (the EIA/Sargent &
Lundy AEO2025 capital cost study). WebFetch could not parse the PDF's tables (binary/FlateDecode
streams); pivoted to the Read tool against the locally-cached PDF, which renders pages as images
readable by the model. Table 1-2 (Cost & Performance Summary Table), Case 16 — Solar PV with
Single-Axis Tracking, 150 MWAC: **$1,502/kW**. **Outcome: SOURCED as S1.**

## P03 — Battery storage capital cost, USD/kW or USD/kWh

Same source and table as P02. Case 19 — Battery Energy Storage System, Lithium Ion, 150 MW / 600
MWh: **$1,744/kW ($436/kWh)**. The reference case's 4-hour duration exactly matches this case's
battery (800 MWh / 200 MW = 4 hours), so no duration-adjustment assumption was needed. **Outcome:
SOURCED as S2.**

## P04 — Peaker minimum ramp rate after start, MW/min

Searched: "GE LM6000 aeroderivative gas turbine ramp rate MW per minute fast start peaker". Fetched
GE Vernova's own LM6000 product page: "aeroderivative gas turbines achieve a nominal ramp rate of
around 50 MW/min" (contrasted with ~5 MW/min for reciprocating engines). Also fetched GE Vernova's
LM6000 Fast Start Upgrade page, which gives start-time-to-full-load options (5/8/10 minutes from a
cold start) but no explicit MW/min figure for post-start ramping — rejected as the primary figure
because it describes total start sequence time (including light-off and warm-up), not the "after
start" ramp rate the case specifically asks for. **Outcome: SOURCED as S3**, MEDIUM confidence (a
manufacturer class-level statement, not confirmed to scale linearly with unit count for a specific
120 MW plant).

## P05 — Peaker capital cost, USD/kW

Same EIA/Sargent & Lundy AEO2025 study as P02/P03. Case 3 — Aeroderivative Combustion Turbines,
Simple Cycle, 4×54 MW gross, 211 MW net: **$1,606/kW**. This reference case is the same
aeroderivative class as the S3 ramp-rate figure, keeping the peaker's cost and ramp-rate figures
technologically consistent. **Outcome: SOURCED as S1** (same source record as P02).

## P06–P15 — The five hourly net-load/generation data points (Appendix B)

This was the case's central, load-bearing dataset and the hardest to source. Attempts, in order:

1. **EIA Hourly Electric Grid Monitor** (`eia.gov/electricity/gridmonitor/dashboard/...`) — the
   tool named in the original concept brief. Fetched directly; it is a JavaScript single-page
   dashboard application. WebFetch returns only navigation markup, no underlying data. Rejected:
   not fetchable as static content.
2. **EIA legacy Electricity Data Browser** (`eia.gov/electricity/data/browser/`) — same failure
   mode, a JS SPA with no server-rendered data table or CSV link exposed to a static fetch.
   Rejected.
3. **EIA API v2** (`api.eia.gov`) — the programmatic route the dashboard itself likely uses.
   Requires a registered API key. Registering for one was not attempted: this project's operating
   rules treat account/credential creation as out of scope for an autonomous research pass.
   Rejected on that basis, not a data-availability basis.
4. **CAISO legacy Daily Renewables Watch** (`content.caiso.com/green/renewrpt/
   YYYYMMDD_DailyRenewablesWatch.txt`) — a known historical public URL pattern (confirmed via
   search results describing its format: hourly rows for GEOTHERMAL, BIOMASS, WIND TOTAL, SOLAR
   PV, SOLAR THERMAL, etc.). Tried two dates (2026-08-10, 2023-08-15): both returned HTTP 404.
   CAISO's own site confirms this report line was revised/consolidated into "Today's Outlook" at
   an unspecified date; the legacy endpoint appears discontinued. Rejected: genuinely gone.
5. **CAISO Today's Outlook / Supply** (`caiso.com/todays-outlook/supply`) — the current tool.
   Confirmed (via its own page text) that it supports historical date selection and CSV export,
   but export happens client-side in the browser; no static or query-parameterized download URL
   was discoverable. Rejected: not fetchable without interactive browser automation.
6. **CAISO OASIS** (`oasis.caiso.com`) — CAISO's actual public data API, no registration required.
   Returns ZIP-wrapped XML/CSV. Not attempted to completion: WebFetch converts HTML to markdown
   and is not equipped to unpack a binary ZIP response, and the exact `queryname` for actual
   (not forecast) renewable generation by fuel type could not be confirmed from public
   documentation in the time available. Rejected: not tractable with the tools on hand this pass.
7. **Academic literature** — fetched an arXiv paper on CAISO net-load ramp forecasting
   (`arxiv.org/pdf/2012.07117`); WebFetch could not extract text from the PDF (image/binary
   content), and the abstract page alone did not contain numeric results. Rejected: inaccessible.
8. **CAISO's own "Fast Facts" PDF** (`flexibleresourceshelprenewables_fastfacts.pdf`) — a real,
   primary CAISO document, but WebFetch could not extract its text (compressed PDF streams), and
   its metadata shows it dates to 2013 (a projection for the year 2020) — not "real recent" data
   even if it had been readable. Rejected on both fetchability and recency grounds.
9. **EIA "Today in Energy" articles** on the duck curve and CAISO solar (`id=67784`, `id=46117`,
   `id=56880`) — all fetched successfully as text, but each discusses the phenomenon qualitatively
   or in aggregate (percent-of-days, GW of installed capacity) without a per-hour or per-date MW
   table. Rejected as the primary table source, but retained as background confirming the duck
   curve is real and current.
10. **Industry/market-analytics sources** — gridstatus.io's spring-2025 CAISO blog post and
    FactSet's "From Duck to Canyon" article both gave real, dated, but still aggregate figures
    (e.g., "net load levels swing well over 24 GW in 8 hours," "the average evening ramp can
    sometimes exceed 20 GW in the spring") — directionally useful but not a usable per-hour table.
11. **Modo Energy's CAISO flexible-ramping research note** gave the one genuinely specific,
    hour-scoped figure found in this whole search: **"On average, [net load] increases 6.5 GW in
    the 6pm hour."** This became the anchor for the Modeling Assumption.

**Outcome: NOT FOUND** for a directly-sourced, timestamped table, after a genuine multi-avenue
attempt across primary (EIA, CAISO) and secondary (academic, industry-analytics) sources. **Exit
taken: Stated Modeling Assumption (MA1), combined with a scope redesign** — the case's D1/D2
modeling target was changed from "solar generation" specifically to "net system load" (the
quantity actually well-documented for CAISO's evening ramp), and a five-point hourly table was
constructed to reproduce the one real, cited figure (Modo Energy's 6.5 GW / 6pm-hour average)
exactly, with the surrounding points shaped to a realistic evening-ramp curve. This redesign does
not touch the Overview, Dilemma, or boilerplate Challenge sections, and does not change the
claimed skill set or the LEARNING_GOALS mapping — only the specific physical quantity graphed and
differentiated (net load rising is numerically the same ramp the case's dilemma is about: how much
*other* generation has to replace the sun). Documented in `case.md` Appendix C (MA1) and
`case.json.modeling_assumptions[0]`.

## Background text: "same fixed capital budget"

The originally-drafted Background claimed the capital committee had authorized the *same* fixed
capital budget for either resource. Once P02/P03/P05 were sourced, the two options' real total
capital costs came out to $649,200,000 (A) and $192,720,000 (B) — not close to equal. Rather than
force or hide a false equality, Background was edited during this research pass to describe the
committee evaluating two bids "on the same basis: cost per unit of ramp-rate capability delivered,
not total price tag" — which is accurate, keeps the primary metric doing the real comparison work,
and does not touch the Overview, Dilemma, or boilerplate Challenge sections.

## Supplemental appendix materials (SPEC §1.6 / case-research §6)

Not separately gathered this pass beyond the sources above (no Desmos graph, Google Maps route, or
news-article appendix was added). The case's real-world grounding is carried entirely by the five
cited sources (S1–S5), which include one EIA-commissioned engineering cost study, one manufacturer
product page, and two industry grid/battery-market research notes — flagged here so a later pass
can add a duck-curve news article or a Desmos plot of P(t) if desired.

## Next step

Run `case-qa` on `the-sunset-ramp`.
