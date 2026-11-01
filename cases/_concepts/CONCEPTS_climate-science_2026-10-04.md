# CONCEPTS: climate-science (Earth, Climate & Environment) - 2026-10-04

Target: domain `climate-science` (domains.json: 0 existing cases, authoring priority gap; signature skills are line of best fit / slope / correlation / negative numbers). Overlap check: no case in cases_index.json or cases/_concepts/ is climate or phenology (nearest: oceanography / tide-window, hydrology Ellicott City sheet, both different data and story).
Tags: [CONFIRMED] fetched and read this session; [DERIVED] my Python on the fetched data (scripts in session scratchpad, rerunnable from the URLs below); [UNVERIFIED] not confirmed.

## Ranking
| Rank | Concept | Balance test | Verdict |
|---|---|---|---|
| C1 | The Two Saturdays (DC cherry blossoms: Mar 27 vs Apr 3, 2027) | PASSES as an honest close call (sign flips inside the plausible range, real data, no invented price) | Recommend |
| C2 | The Short Record (is 1998-2012 long enough to call?) | FAILS (14+ yr windows significant in current GISTEMP; "pause" mostly a start-year/dataset artifact) | Do not recommend; evidence module only |
| (rejected) | Last-frost planting date, DC | FAILS (frost after Apr 10 essentially never occurs in 35 yr) | Dropped |

## Cold-solve summary (all on real fetched data)
Data: NPS/EPA-derived DC peak bloom 1921-2026 (GMU repo `washingtondc.csv`, 106 yr; NPS Bloom Watch page agrees 2004-2026) and NOAA GHCN-Daily station USW00013743 (Washington Reagan National) daily TMAX/PRCP via `https://www.ncei.noaa.gov/data/global-historical-climatology-network-daily/access/USW00013743.csv` (12 MB, fetched, units tenths C / tenths mm).

C1 metric: P(joint success) = share of years in which the Saturday-nearest-date event falls within peak bloom +/- k days AND that day has TMAX >= H F and precipitation < 0.1 in. Parameters swept, none invented as prices: k (viewing window) 4-10 d, H 50/55/60 F, record start 1990/1995/2000/2005/2010/2015 to 2025.
- Mean-date targets, 1990-2025 (n=36), k=7, H=55: Sat near Mar 21 joint 0.14; Mar 24 0.22; **Mar 28 0.31 (bloom 0.61, weather 0.42)**; Apr 1 0.42; **Apr 4 0.42 (bloom 0.61, weather 0.69)**; Apr 7 0.33; Apr 11 0.22 (bloom 0.25, weather 0.64); Apr 15 0.11. [DERIVED]
- The tradition date (parade, Sat near Apr 11) is dominated by Mar 28 in 52 of 54 parameter cells (B-A > 0 in 52, < 0 in 2; range -0.08 to +0.35). So the binary is NOT "March vs mid-April".
- **The real binary, A = Sat near Apr 4 (2027: Apr 3, Petalpalooza slot) vs B = Sat near Mar 28 (2027: Mar 27, Blossom Kite Festival slot), B minus A joint probability** (H=55) for k = 4,5,6,7,8,10:
  - 1990-2025: -0.03, -0.03, -0.08, -0.11, -0.17, -0.19
  - 1995-2025: 0.00, 0.00, -0.06, -0.10, -0.13, -0.16
  - 2000-2025: 0.00, -0.04, -0.12, -0.15, -0.23, -0.23
  - 2005-2025: +0.05, 0.00, -0.10, -0.14, -0.24, -0.24
  - 2010-2025: +0.12, +0.06, -0.06, -0.12, -0.25, -0.19
  - 2015-2025 (n=11): +0.36, +0.36, +0.18, +0.09, -0.09, -0.09
  - Across all 108 cells (6 record windows x 6 k x 3 H): B wins 34, A wins 57, ties 17. **Sign flips with k and with the record start.** Mechanism: B wins on bloom alignment (peak is early and getting earlier), A wins on weather (Mar 28 TMAX >= 55 F and dry only 42% of years vs 69% for Apr 4). Full record 1948-2025 (n=78), k=7: A 0.37 vs B 0.28.
- Fairness caveat [DERIVED]: A leads in most cells, so this is "close, tilting A on long records, B on a narrow viewing window and recent years", not 50/50. Differences of 0.05-0.10 are 2-4 years of 36; with n this small the honest reading is that the data cannot cleanly separate them, and the case should say so (sampling noise is part of the lesson).
- Bloom trend [DERIVED]: peak-bloom slope -0.85 d/decade (1921-2026, r = -0.35); -1.75 d/decade from 1990 (r = -0.26); -2.89 d/decade from 2000 (r = -0.32). Mean Mar-day-of-peak (Mar 1 = day 1): 1921-50 35.3; 1951-80 37.2; 1981-2010 32.1; 2011-2026 28.2. Residual SD about 6.7 days, so no method predicts a given year well (backtest MAE 5.5-5.9 d for 10-yr mean vs 30-yr trend; both forecast Mar 26 for 2027, hit counts differ by at most 3 of 27-37 years either way).

C2 (hiatus) cold solve, NASA GISTEMP v4 Land-Ocean J-D anomalies 1880-2025 (`https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv`, fetched). OLS trend +/- 95% CI (deg C/decade): 1998-2012 +0.134 +/- 0.106 (significant); 1983-2012 +0.175 +/- 0.038; 1951-2012 +0.134 +/- 0.016. Window length ending 2012: 8 yr -0.007 +/- 0.215 (not sig), 10 yr +0.059 +/- 0.152 (no), 12 yr +0.073 +/- 0.107 (no), 14 yr +0.171 +/- 0.111 (yes), 16+ yr yes. Residual lag-1 autocorrelation for 1998-2012 is about 0 (n_eff 15), so autocorrelation correction does not rescue the "pause" (it only flips if r1 >= 0.2, not what the data show). Of 62 fifteen-year windows starting 1950-2011, 19 are non-significant, mostly 1950-1963 and a few 1979-87 starts. [DERIVED] Result: the answer is set by choosing a start year, and for any honest window of 14+ years the call is "yes, warming". No two-sided decision. Fails.

## C1 - The Two Saturdays   .   score see note   .   tier T2
**Protagonist.** A fictional events director (name to be invented in case-write) at the National Cherry Blossom Festival, Inc. (a real 501(c)(3), confirmed on its site) who must give the festival's one big outdoor Saturday a date. Personally at stake: the Saturday crowd either meets the blossoms or meets bare branches / a cold rain.
**The dilemma.** A.) Put the flagship event on Saturday April 3, 2027 (the later, warmer slot; Petalpalooza's real 2027 date) OR B.) Put it on Saturday March 27, 2027 (the earlier, bloom-aligned slot; the Blossom Kite Festival's real 2027 date).
**Primary metric.** Probability (share of past years) that the Saturday is both within a viewing window of peak bloom and comfortable (TMAX >= 55 F, under 0.1 in precipitation): joint hits per year, from real records.
**Why it's close.** B is closer to the bloom (peak is getting earlier, about 1.7-2.9 days per decade in recent windows) but March 27-28 is dry and warm only about 42% of years versus about 69% for April 3-4. Which one wins depends on how forgiving the viewing window is and how far back you trust the record; the sign of B minus A flips (see cold solve). The tradition date (Apr 10 parade) loses to both, which is a finding students can discover.
**Would close (thickens thin skills; none is at n <= 2, so zero strict gap-queue closures):**
| id | kind | label | spine n |
|---|---|---|---|
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | How to draw a line of best fit given a set of data | 3 |
| statistics-and-probability-line-of-best-fit | term | Line Of Best Fit | 3 |
| statistics-and-probability-how-to-identify-the-slope-of-a-line-given-a-set-of-data-or-a-graph-o | how-to | How to identify the slope of a line given a set of data... | 6 |
| statistics-and-probability-how-to-identify-correlation-given-a-scatter-plot-or-set-of-data | how-to | How to identify correlation given a scatter plot or set of data | 4 |
| statistics-and-probability-correlation | term | Correlation | 4 |
| statistics-and-probability-how-to-draw-a-line-of-a-set-of-data-given-its-linear-equation | how-to | How to draw a line of a set of data given its linear equation | 4 |
| statistics-and-probability-how-to-determine-the-probability-of-a-compound-event | how-to | How to determine the probability of a compound event (bloom AND weather) | 7 |
| statistics-and-probability-how-to-determine-the-probability-of-conditional-events | how-to | How to determine the probability of conditional events | 5 |
Ids verified present in readmodel/standards_spine.json. Raw weight about 6 how-to x 1.0 + 2 term x 0.6 = 7.2 if counted, but ranking per SKILL.md counts only n <= 2 gaps, so honest score is thickening value only; the case's main value is opening a 0-case domain with a signature-skill fit.
**Already-covered skills it also exercises.** mean, median, range, outlier (statistics ids above), scatter plot, absolute value (negative-number slopes, "days earlier" as negatives: advanced-numbers-negative-number).
**True story.** The festival's real 2027 schedule is published (Opening Mar 20, Blossom Kite Festival Mar 27, Petalpalooza Apr 3, Parade Apr 10; festival Mar 20 - Apr 11, 2027) [CONFIRMED via nationalcherryblossomfestival.org, fetched; the Apr 3 Petalpalooza and Mar 27 kite dates are read from the site's event listing]. 2026: festival Mar 20 - Apr 12; kite Mar 28, Petalpalooza Apr 4, parade Apr 11 [CONFIRMED site + FOX5]; NPS forecast on Mar 5 predicted peak Mar 29 - Apr 1 [CONFIRMED FOX5 summary], actual peak Mar 26 [CONFIRMED NPS Bloom Watch, last updated Mar 26 2026]. So the Mar 28 slot was 2 days past peak and the Apr 4 slot 9 days past: a real forecast miss students can check. 2017: late freeze Mar 14-16 cost about half the blossoms [CONFIRMED NPS footnote; GHCN shows 22.1 F on Mar 15 2017 [DERIVED]]. Earliest peak on record is Mar 15, 1990; Mar 17 in 2000 and 2024 [CONFIRMED: NPS page and the series agree]. Whether the festival's date choices were actually made on bloom grounds is UNVERIFIED (their site states no rule); the case must present the director as a fictional decision-maker framed on real dates, not claim the real org reasoned this way.
**Data feasibility: HIGH.** Real, free, student-explorable:
- NPS Bloom Watch table (nps.gov/subjects/cherryblossom/bloom-watch.htm): stage dates 2004-2026, peak bloom defined as 70% of Yoshino blossoms open [CONFIRMED]. US federal; reuse terms: standard NPS web content, no copyright statement seen [UNVERIFIED terms, treat as US-government public domain but confirm].
- Peak bloom 1921-2026 CSV: github.com/GMU-CherryBlossomCompetition/peak-bloom-prediction, `data/washingtondc.csv` (fields location, lat, long, alt, year, bloom_date, bloom_doy) [CONFIRMED]; its README says DC data are sourced from the EPA Climate Indicators page and "see the source for copyright details" [CONFIRMED]; repo license is CC BY-NC-SA 4.0 "unless otherwise noted", Kyoto data copyright Yasuyuki Aono (non-commercial credit) [CONFIRMED]. Use the NPS page or EPA as the cited source for DC, not the repo license; check EPA terms.
- NOAA GHCN-Daily, station USW00013743, daily TMAX/TMIN/PRCP, via NCEI access CSV (fields STATION, DATE, PRCP, TMAX, TMIN, ...; tenths of C and mm) [CONFIRMED fetched]. Terms: NCEI/GHCN readme asks for citation (Menne et al. 2012, doi 10.1175/JTECH-D-11-00103.1; dataset doi 10.7289/V5D21VHZ) [CONFIRMED]; I did not find a formal reuse license statement, NCEI data are US federal data generally not copyright-restricted with citation requested, no warranty [per search summary; treat the exact legal wording as UNVERIFIED].
- NOAA Climate at a Glance (named in domains.json): city time series CSV confirmed live, e.g. `https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/city/time-series/USW00013743/tmin/3/3/1948-2026.csv` returns Date,Value rows (Washington Reagan Jan-Mar min temperature) [CONFIRMED]. **Reuse terms: the pages I fetched contain no explicit license text (grep for public domain / reuse / copyright found nothing on the portal page; the NCEI /about/disclaimer and /faq URLs I tried returned 404).** Safe wording for the case: "NOAA NCEI Climate at a Glance, US federal data, cite NOAA NCEI; reuse terms not stated on the portal page." Marked UNVERIFIED terms.
Sources I am NOT confident about: the weather thresholds (55 F, 0.1 in) are comfort assumptions, disclosed and swept (50/55/60 F gave the same sign pattern), not sourced facts; the viewing window k is a judgment, swept 4-10 d; actual 2027 event dates could change.
**Sensitivity (SPEC §6).** NONE. (Mention that this is a school-age friendly festival; no deaths or accident site.)
**Split risk.** NONE.
**Reviewer caution.** A and B forecast nearly the same bloom date; the dilemma lives in the weather-versus-bloom tradeoff and the choice of horizon, not in a forecast disagreement. Do not describe it as a 50/50 coin flip: on long records A leads; the case should make students find which assumptions flip it.

## C2 - The Short Record   .   NOT RECOMMENDED   .   tier T3
**Protagonist.** A fictional junior analyst at a national weather service in 2013 deciding whether the press release may say the 15-year trend 1998-2012 shows warming. Real context: the IPCC AR5 (2013) "hiatus" discussion (details UNVERIFIED, not fetched).
**The dilemma.** A.) Report the 1998-2012 trend as a real warming signal OR B.) Say a 15-year record is too short to call and wait for 30 years.
**Why it fails.** See cold solve: with current NASA GISTEMP v4, the 1998-2012 trend is +0.134 +/- 0.106 C/decade, significant; windows of 14+ years are significant; only windows of 12 years or fewer are not. B is not defensible for the stated window, so A dominates. The lesson (start-year cherry-picking) is real and strong; use it as an evidence module in C1 or another case, not as a decision case. Data: NASA GISTEMP LIVE and fetched; reuse terms UNVERIFIED here (not checked this session; NASA GISS asks for citation).
**Would close.** Same line-of-best-fit / slope / correlation skills as C1 plus negative-number slopes.

## Rejected during the cold solve
- Last-frost planting date (DC, GHCN): probability of a 32 F freeze after Apr 10 is 0.08 on 1937-2025 and 0.00 on 1991-2025 or 2006-2025; mean last-frost date moved from Mar-day 28.6 (1937-66) to 23.4 (1997-2025). Any planting decision after Apr 10 is dominated by "plant"; no balance without an invented crop price.
- Sea wall vs buyout and ski-season investment: every plausible version needs an invented dollar parameter; not pursued.
- Nenana Ice Classic (Alaska breakup guess): data likely good but it is a lottery, a gambling flag for a middle-school corpus; not fetched.

## Honest verdict
C1 passes the balance test as a close call from real data: the sign of B minus A flips with the viewing-window width and the record start (34 B-wins, 57 A-wins, 17 ties over 108 parameter cells), with the mechanism (bloom alignment vs weather) visible in two columns of real numbers. Weaknesses to flag to reviewers: the margin is a few years out of 36 so noise dominates; the thresholds are assumptions (swept, same pattern); A leads on long records; zero strict gap-queue skills closed (all n of 3-7). C2 does not pass. Nothing was written outside cases/_concepts/.
