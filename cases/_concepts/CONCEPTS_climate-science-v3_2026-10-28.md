# Concept sheet v3 - Climate & Atmospheric Science (`climate-science`), 2026-10-28

Re-brainstorm after round 1 (old sheet CONCEPTS_climate-science_2026-10-04.md: C1 cherry-blossom Saturday NOT revived; C2 hiatus already failed). Tags: [FETCHED] downloaded this session; [DERIVED] my Python on fetched data (scratchpad scripts, rerunnable from the URLs); [UNVERIFIED] not fetched.

**Margin convention (once):** margin = |A - B| / max(A, B) on the stated metric.

## Ranking
| Rank | Concept | Shape | Verdict |
|---|---|---|---|
| C1 | The Tap Date (Vermont sugarmaker) | Baseline/definition-dependent choice + trend lines | RECOMMEND |
| C2 | The Piling Height (marina, which trend line) | Model-choice by back-test | Weak: balance only in aggregate; see caveats |
| C3 | The Plow Line (road opening vs hiring) | Predictor-choice by correlation | Sketch only, nothing fetched; do not build without a cold solve |

Rejected after brute force this session (do not retry): (a) school start date, Aug-24 vs post-Labor-Day (Baltimore BWI, Tmax>=85..95 F, 3 record windows): post-Labor-Day has fewer hot instructional days in 15/15 cells (margins 5-20%), so A is dominated. (b) Preseason practice 6-9 am vs 6-9 pm by heat index (NOAA ISD hourly, ATL/TPA/BHM/CAE/RDU, Aug 1-21, 2014-2025): morning has lower share of hours at HI>=90/95/100 at every site and threshold (e.g. Tampa HI>=100: 1.1% vs 11.7%; mean HI Tampa 85.7 vs 92.1), dominated. (c) Drought-trigger rule vs US Drought Monitor (Lancaster Co. NE): best F1 about 0.43, no clean rule; not a case. (d) Last-frost planting: dominated (old sheet).

---
## C1 - The Tap Date   (tier T3)
**Protagonist.** Ansel Pelletier (fictional; 0 hits for "Pelletier"/"Ansel" in cases/ and _concepts/), runs a family sugarhouse near Burlington, Vermont, with a 1,800-tap bush and two relatives who take unpaid leave for the season. **Scenario inputs (labelled, not sourced):** taps, crew, and that each tap hole is usable for about six weeks (42 days) before it dries out. Decision date frozen: **2026-01-26**; only seasons 1949-2025 are available to students; the 2026 outcome is Twist only.
**Dilemma.** A.) Tap on **Feb 20** (six-week window Feb 20 - Apr 2) OR B.) Tap on **Mar 1** (Mar 1 - Apr 11).
**Metric.** Run days = days with Tmax >= 35 F and Tmin <= 27 F (freeze-thaw day; the definition is an assumption, disclosed and swept) counted inside the 42-day window, averaged over a record chosen by the student. Higher is better.
**Why it is balanced (computed, scope fixed before looking: station, 42 d, 35/27 F, two start dates).** [DERIVED from FETCHED GHCN-Daily USW00014742, Burlington Intl Airport, 1949-2025 seasons, zero missing TMAX/TMIN days in window]
| Record used | Feb 20 | Mar 1 | Winner (margin) |
|---|---|---|---|
| 1950-1979 | 12.2 | 13.87 | B by 12.0% (A better in 8 years, B in 17) |
| 1991-2020 | 13.03 | 12.80 | A by 1.8% |
| 1996-2025 | 12.67 | 12.07 | A by 4.7% (A 17 yrs, B 9) |
| 2006-2025 | 12.15 | 11.50 | A by 5.3% |
| 1950-2025 | 12.67 | 13.01 | B by 2.6% |
Sweep of 27 definitions (Tmax 33/35/37, Tmin 25/27/30, length 35/42/49 d): for 1950-79 B wins in 24 of 27 cells (all margins <= 17.3%); for 1996-2025 A wins in 22 of 27 (margins <= 12.8%). Winner flips with the baseline and, near the edge, with the definition. Every printed margin <= 17.3%.
Trend lines (run days vs year, least squares): Feb 20 slope +0.03 per decade (1950-2025) vs Mar 1 -0.34 per decade; lines cross about 1997 (1950-2025 fit), 1990 (1976-2025), 1994 (1996-2025). Extrapolated 2027 values 12.8 vs 11.7 (full fit). Year-to-year SD about 2.6-3.1 run days; paired difference 1996-2025 mean +0.60, SE 0.41, so the recent edge is only about 1.5 SE: students must decide whether it is signal.
**Dominance checks.** Continuous start-date sweep (every 3 days Feb 1 - Mar 21, 42-day window): best start Mar 3 (14.2) for 1950-79, Feb 16-19 (13.7/12.7) for 1980-2009 and 1996-2025, Feb 19 (11.8) for 2011-2025; both options sit within 1.5 run days of the optimum in every baseline, so neither is a strawman and neither is dominated by a third date. Hedge (half the taps each date): 1996-2025 mean 12.37, SD 2.64 vs A 12.67/2.63 and B 12.07/3.10: lies between A and B on the mean, does not dominate; it is a legitimate extension talking point. Not modelled (named as outside the model): sap sugar content falls late in season, labor, retapping, tap-hole health; the 6-week life is a disclosed assumption [UNVERIFIED against UVM Proctor Maple Research Center guidance].
**Human stake.** A family's one-shot season and the relatives' leave; consequences are scenario inputs (e.g. "each run day is about one boil").
**Twin check.** grep of cases/*/case.md and cases_index.json: no maple/tapping/phenology case; no "run days" metric. Different template from field-watch (satellite trend), tide-window.
**Skills (spine ids verified in standards_spine.json; n in parentheses).**
- statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data (3), -line-of-best-fit (3): scatter of run days vs year for each start date, fitted by hand.
- statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o (6): the -0.34 vs +0.03 per decade comparison.
- statistics-and-probability-correlation (4) / how-to-identify-correlation...: r of run days with year.
- statistics-and-probability-non-linear (2, thin): forced by the start-date sweep, a hump not a line; students must say why a line cannot choose the date.
- statistics-and-probability-how-to-write-a-linear-equation-given-a-graph-of-a-line-of-a-set-of-d (3): write both lines, solve for the crossing year (two linear equations).
- advanced-numbers-negative-number (signs of the slopes). Only non-linear is thin (n=2); all claims forced by deliverables D1 scatter+fit, D2 crossing year, D3 sweep table.
**Data.** HIGH. NOAA NCEI GHCN-Daily, `https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00014742.csv` [FETCHED, 12 MB, units tenths of C; I convert to F]. Cite Menne et al. 2012 (doi 10.1175/JTECH-D-11-00103.1); formal reuse wording UNVERIFIED (US federal, citation requested). Station changes/homogenization not checked [UNVERIFIED].
**Twist (post-decision, Twist only).** 2026 season windows (file contains data through 2026-05-31): Feb 20 window 15 run days, Mar 1 window 15 run days: a tie [DERIVED]. 2025: 11 vs 11; 2024: 9 vs 7. The tie is the lesson: one season cannot adjudicate a 0.6-day edge.
**Sensitivity.** None. Facilitator note: livelihood framing only; do not imply any family should have known.
**Ending (not phone, not pen).** He walks the sap line in January snow, hangs the first bucket-lid on the nail by the sugarhouse door, and has to choose which date goes on the chalkboard. (Facilitator may rewrite.)

---
## C2 - The Piling Height   (tier T3; weak balance, read caveats)
**Protagonist.** Joaquin Tavares (0 hits "Tavares"), co-owner of a small marina at Sewells Point, Norfolk, VA, ordering concrete pilings with a 30-year life. Dates: decision frozen 2026-01 (data through 2025). Scenario input: piling top is set with a freeboard on the 2055 mean sea level estimate.
**Dilemma.** A.) Project 2055 sea level from the **full-record linear trend** OR B.) from the **most recent 30-year linear trend**. Which line should set the number?
**Metric.** Back-test: fit with data through year T, predict annual mean sea level for T+1..2025, mean absolute error (mm). Lower is better. Scope fixed in advance: 4 NOAA gauges (Baltimore 8574680, Annapolis 8575512, Sewells Point 8638610, The Battery 8518750) x origins T = 2000, 2005, 2010 (12 cells).
**Computed.** [DERIVED from FETCHED CO-OPS monthly MSL, API `datagetter?product=monthly_mean`, annual means of years with >=11 months] Aggregate MAE: full-record 41.7 mm, last-30 35.2 mm, margin 15.6%. Cell wins: last-30 9 of 12, full-record 3 of 12. Whole-record rates: Baltimore 3.34, Annapolis 3.91, Sewells Pt 4.83, Battery 3.20 mm/yr; 1996-2025 rates 5.26, 6.49, 5.97, 4.65. 2055 vs 2025 gap between the two lines: 34-78 mm (1.3-3.1 in). A quadratic fit back-tested worse than the full linear fit in most tested cells (e.g. Annapolis T=1990 MAE 115 vs 38 mm; Sewells Pt T=2010 was the exception, 32 vs 41) and is not offered as an option.
**Caveats (why rank 2).** (1) Per-cell margins reach 49% (Sewells Point T=2005/2010) so the 20% test holds only in aggregate; (2) A wins only 3 of 12, so the case is lopsided toward B on this scope, close mainly at Baltimore 2000 and Annapolis 2005/2010; (3) the design difference (1.3-3.1 in) is small against a freeboard, which may make the decision feel trivial; (4) stake is a business owner, thin for students. Would need a decision-relevant second metric (days overtopped, needs daily highs, not fetched) before build.
**Skills.** line of best fit (3), slope (6), non-linear (2, thin; the quadratic comparison forces it only if a quadratic deliverable stays in), negative-number (sign of prediction errors). Absolute error forced by MAE.
**Data.** HIGH, NOAA CO-OPS (US federal, citation requested; terms UNVERIFIED). Datum is station datum (STND) in the monthly table; vertical land motion is included in relative sea level, say so.

---
## C3 - The Plow Line   (sketch, NOT computed)
**Idea.** Glacier National Park, Montana: the Going-to-the-Sun Road's full opening date varies by weeks (latest openings July 13 in 2011, 2020 and 2022 per NPS Logan Pass page via search summary [UNVERIFIED, table not fetched]). A West Glacier lodge owner must commit to a seasonal-staff start date in April using a forecast. Shape: predictor choice: regress opening date on April-1 snow water equivalent (NRCS SNOTEL, public) vs March temperature (GHCN) and compare correlation and residual spread.
**Status.** Neither the NPS table nor SNOTEL data fetched; balance, dominance and margin not tested; hiring cost would be a scenario input and risks a single break-even. Grade MEDIUM-LOW. Skills would be line of best fit, correlation, slope (all n>=3).

---
## Recommendation
Build **C1 The Tap Date**. It is the only concept with a tested balance at a pre-fixed scope, human stake, real student-explorable NOAA data, a trend-vs-noise lesson (the signal is about 1.5 SE), and a Twist that is honest (2026 ties).

## UNVERIFIED list
6-week tap-hole life; freeze-thaw run-day definition as a sap-flow proxy; sugar-content decline; station homogeneity of Burlington record; NCEI/CO-OPS formal reuse wording; GHCN citation DOI as remembered; NPS Glacier dates; all C3 content. Nothing was written outside cases/_concepts/.
