# Research Log — The Marginal Detection

One row per placeholder from the case-write draft, per `skills/case-research/SKILL.md`.

| Placeholder | What was searched | What was found | Outcome |
|---|---|---|---|
| P1 — the candidate's full 20-point overnight light curve | Searched AAVSO's WebObs/API and the NASA Exoplanet Archive for a specific, already-flagged "marginal 3-sigma" candidate's raw per-point light curve. AAVSO's own site (`aavso.org`) returned HTTP 403 to direct fetch this session (likely bot-blocking); the Exoplanet Archive's per-target light curves are all for *confirmed* planets with deep, unambiguous transits (e.g. HD 189733 b at 2.4%), not a marginal, still-unconfirmed candidate. | No survey publishes a specific still-unconfirmed candidate's raw pipeline output — this is proprietary, in-progress data by nature; a real marginal candidate's identity and data are typically embargoed until confirmed or dropped. Confirmed as **NOT FOUND**, exactly as the approved concept sheet (`CONCEPTS_astronomy_2026-09-12.md`, C3) itself flagged as the likely outcome. | **Stated Modeling Assumption (MA1).** Constructed a 20-point dataset bounded by TESS's own published photometric-precision figures [S1] and scaled well below a real confirmed transit's depth [S5], with a deliberately non-linear (quadratic) drift shape so the naive line-of-best-fit and box-and-whisker reads land on opposite sides of the case's own 3.0 threshold. |
| P2 — the survey's own follow-up significance threshold | Searched for any published survey's internal "worth a follow-up slot" policy threshold (as distinct from a formal discovery threshold). Found extensive documentation of Kepler's formal 7.1-sigma *discovery* pipeline threshold [S2], but no public survey publishes an internal, pre-discovery "worth another look" bar — this is operational, not a scientific publication. | **NOT FOUND** for a specific survey's internal policy number. | **Stated Modeling Assumption (MA2).** Set at 3.0, explicitly well below Kepler's real 7.1-sigma discovery bar [S2], with the basis and the gap between the two explained in Appendix C. |
| P3 — TESS photometric precision, ppm | Searched "TESS photometric precision ppm per hour stellar magnitude instrument handbook"; fetched the HEASARC EM-planning PDF (failed to parse — binary/compressed) and the IOPscience "Photometry of 10 Million Stars… Part II" article (parsed cleanly). | **FOUND.** 200 ppm/hour pre-flight design target at TESS magnitude 10; ~20 ppm in-flight noise floor for the brightest stars. Peer-reviewed, dated November 2020. | **SOURCED [S1].** Confidence HIGH. |
| P4 — Kepler's formal detection significance threshold | Searched "Kepler pipeline 7.1 sigma detection threshold source Jenkins Twicken paper"; fetched the arXiv abstract for Tenenbaum et al. 2012 (`arXiv:1212.2915`), which explicitly states the 7.1-sigma lower cutoff for detections. | **FOUND.** 7.1 standard deviations (Multiple Event Statistic), with the false-alarm-rate reasoning behind the choice. Peer-reviewed preprint, submitted December 2012. | **SOURCED [S2].** Confidence HIGH. |
| P5 — AAVSO's founding/scale/role | Attempted to fetch `aavso.org` directly (HTTP 403 — the live site blocks this session's fetcher, though it is a real, live, publicly reachable organization site any browser can load). Fell back to a web search, which surfaced AAVSO's Wikipedia article with founding year, scale, and role, cross-checked against multiple independent search snippets citing AAVSO's own "30+ million observations" announcement. | **FOUND**, via a secondary source since the primary site would not serve this session's fetcher. Founded 1911; largest variable-star-observer organization; tens of millions of shared observations. | **SOURCED [S3].** Confidence MEDIUM (secondary/encyclopedia source; qualitative use only, no numeric figure from this source enters the case's arithmetic). |
| P6 — NASA Exoplanet Archive's role | Fetched `exoplanetarchive.ipac.caltech.edu` directly this session (successful, live). | **FOUND.** Live, NASA/Caltech-IPAC-operated, the standard public confirmed-exoplanet database. | **SOURCED [S4].** Confidence HIGH. |
| P7 — HD 189733 b transit depth (scale-comparison figure) | Fetched the NASA Exoplanet Archive's HD 189733 b overview page directly. | **FOUND.** Transit depth δ ≈ 2.4% (≈24,000 ppm), cross-checked against a second solution on the same page (2.585%, consistent within a few tenths of a percent — used the rounder, more commonly cited 2.4% figure). Orbital period, planet radius, and stellar radius also confirmed but not used as load-bearing case figures. | **SOURCED [S5].** Confidence HIGH. |

## Rejected / not used

- A specific, already-published "marginal 3-sigma candidate" light curve, as a genuinely
  documented borderline case: searched, not found, and not expected to be found — the concept
  sheet itself predicted this outcome, and NOT FOUND on a load-bearing figure of this kind is
  exactly the honest result the pipeline is built to surface rather than paper over.
- AAVSO's own site content: not directly fetchable this session (HTTP 403). Not treated as a dead
  or fake source — it is a real, live, independently-verifiable organization (confirmed via
  multiple independent search results) — just not fetchable by this session's tool, so the
  citation uses a secondary source and is graded MEDIUM rather than HIGH accordingly.

## Next step

`Run case-readiness on the-marginal-detection.`
