# Research Log — The Survey Slot

Every figure in case.md is either cited to a real source or disclosed as a stated Modeling
Assumption. This log records what was searched for each of the 8 `needs_source[]` entries.

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | A real, published statistic establishing that not every flagged transit candidate is a real planet, to ground The Candidate Watch's confirmation probability | "TESS Objects of Interest false positive rate percent published statistic" | Guerrero et al. 2021, TESS Prime Mission TOI catalog: 565/2,241 TOIs (~25.2%) reclassified false positive after follow-up | **SOURCED** — S1, HIGH confidence. Primary catalog publication, dated, unambiguous units (count/percent of TOIs). |
| P02 | A real per-target-star planet-candidate yield rate, to inform (not directly cite) the Sweep's per-field detection probability | "Kepler mission planet candidates per target star percentage yield rate"; corroborated with "4034 planet candidates 189516 target stars Kepler DR25 Thompson" | Thompson et al. 2018, Kepler DR25 catalog: 4,034 planet candidates among 189,516 target stars (~2.1%) | **SOURCED (informing, not direct)** — S2, HIGH confidence for the underlying statistic. Not used directly as the per-field, single-look rate this case needs (that would misapply a 4-year continuous-baseline per-star rate to a 20-minute per-field look) — informs MA3's basis instead, with the scale-up/scale-down reasoning stated explicitly in Appendix F. |
| P03 | A real, published transit-depth figure in scientific notation, for a real named planet, to ground Appendix E / Challenge D5 | "TOI-700 d transit depth ppm published value paper" | Rodriguez et al. 2020 (Spitzer confirmation paper): transit depth = 0.000613 (fraction) | **SOURCED** — S3, HIGH confidence. Primary confirmation-paper value, exact figure with clear units (fraction of stellar brightness). |
| P04 | A second real, published transit-depth figure for a different real planet, for the same deliverable | "Kepler-186f transit depth parts per million published value" | Wikipedia's Kepler-186f article: ~510 ppm, citing Quintana et al. 2014 | **SOURCED (secondary)** — S4, MEDIUM confidence. This is a republication of the discovery paper's figure rather than a direct fetch of Quintana et al. 2014 itself — graded MEDIUM rather than HIGH for that reason, per the case-research grading rules (tier 3, reputable secondary source citing a named primary paper). |
| P05 | Confirmation that the NASA Exoplanet Archive is a real, live, currently-operating public data portal reporting transit depth in this scientific-notation-adjacent (ppm) form, to ground the case in a genuinely explorable real dataset (not just two cherry-picked numbers) | "NASA Exoplanet Archive transit depth scientific notation example data table" | The Exoplanet Archive's own Transiting Planets Table column-definitions page confirms depth is reported in ppm | **SOURCED (context)** — S5, HIGH confidence. Not load-bearing in the arithmetic; establishes the real portal Appendix E is drawn from. |
| P06 | A real, published, real-time confirmation probability for one specific, still-unconfirmed transit candidate (i.e., a real number for "this exact candidate will confirm") | Not searched as a load-bearing figure — by definition, no public source can publish a real-time outcome for an event that has not yet happened for a specific still-unconfirmed object. Considered searching for a real, currently-flagged TOI to name directly, but naming one would require freezing its ephemeris/follow-up status at an "as of" date per SPEC §5 and would still not resolve the fundamental problem (no source publishes its future confirmation odds). | **NOT FOUND, as expected — and not the right kind of figure to seek.** Became MA2: the case's fictional candidate is assigned the real, cited TESS population-level rate (S1) as a stated modeling convention, disclosed in scenario_constructions. |
| P07 | A real per-field detection probability for a hypothetical new 12-field shallow transit survey | "TESS shallow survey per-field detection probability new fields"; "sky survey per-pointing new transit detection rate" — no completed survey publishes a directly comparable single-look, per-field figure, since real missions observe continuously over months to years rather than in one 20-minute look | **NOT FOUND.** Became MA3, informed by (not equal to) S2's real per-star yield rate, with the scale-up (many stars per field) and scale-down (20 minutes vs. 4 years) reasoning both stated explicitly. |
| P08 | A specific real observatory's specific nightly slot length, field count, flagged-field count, or same-night follow-up (downlink/battery) capacity | Not searched as load-bearing figures — this is internal, program-specific operational data no observatory publishes per night, the same class of finding as the concept sheet's own live-checked assessment for this concept (Data feasibility note on per-field rates) and consistent with the sibling case's (The Manifest Split) identical finding for terminal-operational data | **NOT FOUND, as expected.** Became MA1, MA4, MA5 — disclosed Modeling Assumptions sized to a plausible program scale, not any single real observatory's actual log. |

## Rejections

- A specific, currently-active real TOI or Kepler Object of Interest was considered as the named
  candidate for The Candidate Watch and explicitly rejected in favor of a fictional composite. Naming
  a real, still-unconfirmed candidate would require freezing its status at an "as of" date (SPEC §5's
  still-changing-entity rule) and would not actually resolve the core problem: no source publishes
  a real-time confirmation probability for a specific unconfirmed object before its next observation.
  The fictional-candidate-with-real-population-statistic approach (MA2, informed by S1) is the more
  honest construction.
- A per-star Kepler yield rate (2.1%, S2) was considered for direct use as the per-field Sweep
  detection probability and rejected: it is a 4-year continuous-baseline, per-star rate, not a
  20-minute, per-field (thousands-of-stars) rate — using it directly would conflate two different
  units of measurement (per star vs. per field; per continuous years vs. per single look). It instead
  informs MA3's basis, with both scaling directions stated.

## Status

All 8 `needs_source[]` entries in case.json are resolved: 3 SOURCED directly (S1, S3, S4), 1 SOURCED
as context (S5), and 5 became disclosed Modeling Assumptions (MA1-MA5), two of which (MA2, MA3) are
explicitly informed by real cited statistics (S1, S2) without claiming those statistics as the exact
value used. Zero `{{NEEDS_SOURCE}}` placeholders remain in case.md (verified by grep, see case-write
validation output). `case.json.status` set to `"qa"` for the next stage.

## Corrections found during case-readiness Tier 2, Probe 6 (data decay), 2026-09-18

A fresh subagent with live web access fetched all 5 cited URLs and found three real defects in the
original citations, which were corrected in case.md, case.json, and the published HTML:

- **S2 (Kepler DR25 star count).** The original claim cited "189,516 target stars" from Thompson et
  al. 2018. The subagent fetched the actual paper text (via `pdftotext`) and confirmed "4034 planet
  candidates" appears, but "189,516" does **not** appear anywhere in the paper — the paper instead
  describes Kepler as observing approximately 200,000 stars overall. The precise 189,516 figure had
  been carried over from an earlier WebSearch summary that was never verified against the primary
  source. Corrected to "4,034 candidates from roughly 200,000 target stars (a little over 2%)," which
  the paper's own text does support, and MA3's basis text updated accordingly. This does not change
  MA3's actual value (10%, an assumption informed by, not equal to, the Kepler rate).
- **S4 (Kepler-186f transit depth).** The original claim cited "~510 ppm" from Wikipedia's
  Kepler-186f article. The subagent fetched the live page and found no occurrence of "510," "ppm," or
  any stated transit depth — only the planet-to-star radius ratio (0.021). Corrected: S4 now cites
  the real, verified radius ratio (0.021) and this case derives the depth itself using the standard
  transit-depth relation depth = (Rp/Rs)² = 0.021² ≈ 4.41×10⁻⁴, marked `derived: true`. Appendix E,
  Appendix G, and the D5 checker in the published HTML were all updated to the corrected value
  (0.000441, not 0.000510).
- **S5 (NASA Exoplanet Archive unit convention).** The original claim characterized the archive's
  reporting convention as "ppm / scientific notation." The subagent fetched the live documentation
  page and found the actual column is labeled "Depth [%]" — a percentage, not ppm, and no "ppm"
  string appears anywhere on the page. Corrected S5's claim to accurately describe the archive's own
  percent-based column, while noting that the real source papers for the two planets used in this
  case (S3, S4) do report depths this small in scientific notation, which is what D5's exercise
  actually draws on.

All three corrections were verified against the live-fetched source text before being written, per
SPEC §5's "never write a number that looks sourced but is not" rule and MCS-21's "no URL from memory"
rule. P6 (data decay) verdict: PASS, after correction — the corrected citations were re-confirmed live
against the same fetched pages.
