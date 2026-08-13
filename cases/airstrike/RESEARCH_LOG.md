# Research Log — Airstrike

Legacy conversion. This case had no `{{NEEDS_SOURCE}}` placeholders in the classic case-write
sense — case-write was not run as a separate stage; the legacy docx was converted directly to a
fully-populated `case.md` because its only genuinely "researchable" figures were real hardware
specs already named in the source text (F-16 speed, ICBM-analog range, SRBM-analog range). What
follows is the research trail for those three, plus the disposition of every other legacy-source
figure.

## P01 — F-16 Fighting Falcon maximum speed

- Searched: `F-16 Fighting Falcon maximum speed km/h Mach 2 official Air Force fact sheet`.
- Found: multiple USAF wing fact sheets and Lockheed Martin's own "F-16 Fighting Falcon Fast Facts"
  PDF, all converging on **1,500 mph / Mach 2** as the stated maximum speed.
- Attempted direct fetch of `af.mil` wing fact-sheet pages (`183wg.ang.af.mil`, `169fw.ang.af.mil`)
  and the Lockheed Martin PDF: all three returned HTTP 403 or unparseable binary content when
  fetched directly.
- Outcome: **SOURCED, confidence MEDIUM** (not HIGH) — the figure is corroborated across several
  independent public fact sheets via search-tool synthesis, but no single primary document was
  successfully fetched and read directly during this pass. Recorded as case.json `sources[].id
  = "S1"`. 1,500 mph converts to ~2,410 km/h, within 1% of the legacy source's stated 2,400 km/h —
  kept the legacy value (2,400 km/h) since it is effectively the same figure, just cited now.

## P02 — ICBM-analog (DF-5-class) range

- Searched: `DF-5 CSS-4 ICBM range km CSIS Missile Threat`.
- Fetched directly: `https://missilethreat.csis.org/missile/df-5-ab/` — CSIS Missile Threat
  Project, a tier-1/tier-2 authoritative public defense-analysis source.
- Found: **12,000 km** effective range for the DF-5 (CSS-4), 1-3 MT warhead yield.
- Outcome: **SOURCED, confidence HIGH.** This corrects the legacy source's stated 15,000 km — the
  legacy figure had drifted from the real published range. Updated case.md Appendix C and
  case.json `sources[].id = "S2"`. The narrative claim that "every city in the continental United
  States is within range" still holds at 12,000 km from this case's fictional region, so no other
  text needed to change.

## P03 — SRBM-analog (TR-1 Temp-class) range

- Searched: `"TR-1 Temp" missile short range ballistic`.
- Fetched directly: `https://en.wikipedia.org/wiki/TR-1_Temp`.
- Found: the TR-1 Temp is a real, historical (in service 1969-1989, decommissioned under the INF
  Treaty) Soviet mobile SRBM, NATO name SS-12 Scaleboard. Range **800 km** for the SS-12 variant,
  **900 km** for the SS-22 variant. Single 500 kt warhead reported for the base system.
- Outcome: **SOURCED, confidence HIGH.** The legacy source's stated 900 km matches the SS-22
  variant's real range exactly — kept as-is, now cited. Recorded as case.json `sources[].id =
  "S3"`, with a disclosure note that this is real historical hardware being used as a technical
  analog inside a fictional present-day scenario, not a claim that the system is currently in
  service anywhere.

## Figures NOT sourced — disposition

Two figures from the legacy source could not be traced to any real, citable study and were
**not** presented as sourced. Per case-research SKILL.md §5, both became explicit, disclosed
Modeling Assumptions rather than silently-kept numbers:

- **SRBM intercept rate (5.6%).** Searched for public unclassified intercept-rate figures for
  regional allied missile-defense systems; found only classified or contested figures with no
  single defensible public value. **NOT FOUND → Modeling Assumption MA2** (case.md Appendix D).
  Flagged as the case's single most load-bearing assumption — see `sensitivity_model.py`'s `FLEX`
  and FACILITATOR.md's sensitivity note.
- **Population-at-risk per warhead class** (1,000,000 / 750,000 / 500,000 / 250,000 / 100,000 for
  5.2 MT / 3.1 MT / 1 MT / 100 kt / 50 kt). These are the legacy source's own stated casualty
  thresholds for a strike on an unnamed "major urban center." Because the target is fictional (not
  a real named city), there is no real study to cite for these exact numbers, even though they are
  the right order of magnitude for what public nuclear-effects modeling tools produce for a dense
  urban strike at these yields. **NOT FOUND as a citable per-city figure → Modeling Assumption
  MA3** (case.md Appendix D).

## Figures kept as real, reproduced data (not researched, extracted)

The 15-site coordinate map and its warhead-class colors (case.md Appendix A) were not researched —
they were extracted directly from an image embedded in the legacy source docx (a hand-plotted
Desmos-style scatter plot) and reproduced verbatim as a table. This is real data specific to this
case's own DIA-survey scenario, not a claim about any real missile deployment, so it does not
require external sourcing — it required accurate extraction, which was done by reading the image's
pixel coordinates against its own drawn axes and confirming warhead-class colors against the
source docx's run-level font-color metadata (five colors, one per warhead class, extracted via
`python-docx`'s run.font.color.rgb).

## Placeholder count reconciliation

`case.md` ships with **zero** `{{NEEDS_SOURCE}}` tokens remaining — every figure is either cited
(Appendix E, 3 sources) or declared a Modeling Assumption (Appendix D, 4 assumptions, 2 of which
carry no public source and 2 of which are definitional/tactical conventions).
