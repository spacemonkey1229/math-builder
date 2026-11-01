# CONCEPTS: hydrology-water (v3) - 2026-10-28

Slot: replacement for the rejected C1 Ellicott City "Thousand-Year Street" (A dominated; rainfall conflicts with NWS; single-source cost; deaths).
Verified sheet: every number below was fetched and computed by me on 2026-10-28 (scripts in the session scratchpad). Tags: **[CONFIRMED]** fetched and read;
**[DERIVED]** my computation from fetched data (recompute at research); **[UNVERIFIED]** not fetched, disclose or cut.

**Margin convention (stated once).** margin = gap / winner's value, where "winner's value" is the better of the two metric values; lower-is-better metrics use the lower value as denominator. SPEC 20% test applied to it.

**Target.** `hydrology-water` (domains.json: 0 of 9 signature skills uncovered), so I targeted *thin* spine skills (n<=2) that a deliverable truly forces. Weights per SKILL.md.

**Overlap check (cases_index.json + cases/).** Water-adjacent: creek-span (truss steel), deluge-gun (sprinkler arc), tide-window (keel clearance), total-flow (flood volume per dollar), how-long-can-we-last (emergency fund), flow-state (marketing), vent-cap (sheet metal). Nearest to my picks:
`alert-curve` (threshold trip vs curve check, confirmed incidents per false escalation) is the nearest to C1 (both are about alert thresholds); C1 differs in being about *calibrating a published standard against two seasons of paired lab data* and in the train/test baseline question, not escalation policy. `total-flow` is the nearest to C2 (reservoir/flood volume) but C2 is a two-clock reliability problem with no cost denominator. `field-watch` (days of buffer before a deadline) has a similar "buffer" metric to C2's runway; different domain and no uncertainty.

| Rank | Concept | Shape | Score | Data | Tier | Balance (brute-forced) |
|---|---|---|---|---|---|---|
| C1 | One Rule or Eight | pooling vs per-site calibration; answer depends on how you test (in-sample / next-season / random split) | 1.0 | HIGH | T3 | PASS, with caveat (B's wins are tie-break sensitive) |
| C2 | Which Cliff First | two-clock multi-criteria; answer depends on which hydrology record you replay | 1.2 (see note) | HIGH | T3 | PASS on full record; compact side 22% (2 pts over) |
| C3 | Four Labs, Eight Beaches | allocation (choose 4 of 8 = 70 plans); two plausible rules | 1.0 | HIGH | T3 | near-tie, noise-limited; weakest |

**Recommendation: C1.** Strongest human stake (a hot-Saturday swim flag at a named public beach), all data one open portal, both options verifiably win under different, defensible tests, and every claim is recomputable by a student. C2 is the better *water* case and worth writing second, but it needs an R1a ruling because it is a two-metric trade-off and its legal anchor (82.5 maf) is contested. C3 reuses C1's dataset, so do not build both in the same batch.

---

### C1 - One Rule or Eight   ·   score 1.0   ·   tier T3   ·   Data HIGH

**Frozen decision date.** 2016-10-31 (end of the 2016 beach season). Use only paired culture+DNA samples dated 2015-05 through 2016-09. Everything 2017 onward goes in the Twist.

**Protagonist.** Beatriz Vandermolen (fictional), a water-quality analyst at a big-city park district. The district has one rapid DNA test per beach per morning and must write next season's flag rule before the first Saturday of Memorial Day weekend. Personally at stake: if the rule is too lax, a child swims on a bad day; too strict, families get turned away from a clean beach and stop believing the red flag.

**Background hook (no numbers in the Overview).** Morning sample at a lakefront beach; culture result will not arrive until tomorrow, the DNA reading comes back by lunch; the lifeguard captain asks whether the flag goes up.

**The dilemma.**
A.) One Rule: fit a single citywide DNA threshold from the paired 2015-2016 samples and use it at all eight beaches OR
B.) Eight Rules: fit a separate threshold for each beach from its own paired samples.
(Reference line, not an option: the EPA/Park District published DNA action value of 1,000 CCE/100 mL [CONFIRMED in dataset description]. Students must compare both options against it.)

**Primary metric.** Wrong calls per 100 beach-days on data the rule did not see: (DNA flags a day culture calls clean) + (DNA misses a day culture calls over 235 CFU). Lower is better. Truth label = culture mean >= 235 CFU/100 mL, the Park District's own 2006-2016 standard. Disclose: culture is an incumbent standard, not illness.

**Scope fixed before looking (the three tests students must run; I defined these before computing the margins).**
(i) in-sample, all 629 pairs; (ii) fit on 2015, test on 2016 (the realistic forward test); (iii) 200+ random half-splits, fit on half, test on the other half.
Threshold grid: 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 1000, 1250, 1500, 2000, 3000 CCE; choose the threshold with the fewest wrong calls, ties go to the HIGHER threshold (fewer closures).

**Brute-force results [DERIVED, 629 paired samples, 8 beaches, 147 culture exceedances].**

| Test | A One Rule (wrong calls) | B Eight Rules | Winner / margin | EPA 1,000 reference |
|---|---|---|---|---|
| (i) in-sample, 629 pairs | 110 (T=400) | 98 | B by 12.2% | 133 |
| (ii) fit 2015 -> test 2016 (358 pairs) | 69 (T=500) | 65 | B by 6.2% | 76 |
| (ii') fit 2016 -> test 2015 (271 pairs) | 60 (T=250) | 60 | tie | 57 |
| (iii) random half-splits, mean of 200 (314 test pairs) | 56.6 | 59.1 | A by 4.4%; A wins 130 of 200, B 53 | 66.0 |

Both options win somewhere with margin <= 20% (B in-sample and next-season, A on random splits). Robustness grid (coarse/fine 50 grid x tie-break high/low): A's random-split advantage holds in all four variants (4% to 9%); B's next-season advantage holds only with the high tie-break (65 vs 69 and 67 vs 71) and flips to a 2-point A win with the low tie-break (70 vs 68). **Caveat to state in the case:** B's win next-season is within noise and tie-break-dependent; B's clear win is in-sample only, which is the overfitting lesson, not a decorative one.

**Hidden-dominator checks run.**
- EPA 1,000 vs a fitted threshold: the fitted citywide rule beats 1,000 in-sample (110 vs 133, 17%) and in random splits (56.6 vs 66.0, 17%), but 1,000 beats the fit in the reverse-year test (57 vs 60-69). Because EPA 1,000 is a fixed rule it is a reference line, not an option, so it cannot make B or A dominated. If the case made "EPA vs fitted" the binary, the fitted rule would win 5 of 6 protocols: I rejected that binary on this basis (it exists only because of the choice of truth label).
- Per-beach thresholds go to the 3,000 CCE grid ceiling at South Shore, Ohio Street and North Avenue in the all-data fit (few or no exceedances), i.e. DNA would essentially never flag them. This is the equity/safety tension that makes B arguable, and it is real in the data, not tuned.
- Duplicates: 629 rows, 627 unique (beach, date) pairs; immaterial, but dedupe at research.
- Yesterday's culture result (the old one-day-lag practice) misclassifies 201 of 599 days (33.6%), worse than "never flag" (147 of 629, 23%). Useful Appendix fact, not an option.

**Why it's close.** A pools information (more data per rule, steadier next season) but over-flags at clean beaches and under-flags at dirty ones; B tailors the rule to each beach but each rule rests on 36-94 paired samples with 2-37 exceedances each, so the thresholds jump around (63rd Street 250 vs 700 depending on which year you fit).

**Would close (thin spine skills; ids verified in standards_spine.json).**
| id | kind | n | forced by |
|---|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data | how-to | 1 | Deliverable: side-by-side box plots of DNA readings on exceedance vs clean days for the two beaches whose fitted thresholds disagree most (South Shore, Montrose) |
Already-covered skills it also exercises (spine n>=3 or not claimed): percent / rate of wrong calls, mean of 200 split results, ratio of flags to hits, comparing decimals.
Claim only 1 thin how-to. Do not add the terms "Independent Event" or "Non-linear": not forced.

**Data feasibility: HIGH.**
- City of Chicago Data Portal, "Beach Lab Data - Culture and DNA Tests" (id 9wd3-tqr2): 629 paired rows, 2015-2016, fields beach, culture_reading_mean, dna_reading_mean, timestamps. Free JSON/CSV via SODA, no key. [CONFIRMED fetched; row count 629 from API]
- "Beach Lab Data - Culture Tests" (hh4t-tnq8): 18,002 rows 2006-2016; "Beach Lab Data - DNA Tests" (hmqm-anjq): 17,594 rows 2015-2026. [CONFIRMED]
- Thresholds 235 CFU (culture) and 1,000 CCE (DNA) are stated in the dataset's own description page. [CONFIRMED]
- Licence: the portal exposes no licence field (licenseId null). City of Chicago Terms of Use / "public domain" status [UNVERIFIED: quote the portal terms at build]. Attribution: Chicago Park District.
- Rainfall (not needed for the recommended design): Chicago Park District "Beach Weather Stations - Automated Sensors" (k7hf-8y75) has hourly rain in mm; I used it in side checks only (rain >= 12.7 mm in 24 h flags 49 clean days to catch 39 of 127 exceedances; DNA at 500 beats every rain rule on wrong calls). [DERIVED]
Not confident: CPD's actual 2017+ flag rule [UNVERIFIED]; whether any beach-level change in lab method occurred between 2015 and 2016 [UNVERIFIED]; per-beach attendance [UNVERIFIED, none fetched].

**Twist (post-freeze, allowed only here) [DERIVED from dna.json].** The DNA-only series continues: share of DNA readings >= 1,000 CCE was 11.6% (2017), 14.7% (2018), 5.0% (2019), 9.3% (2021), 4.2% (2022), 2.3% (2023), 5.7% (2024), 6.0% (2025), 3.0% (2026 to date). Culture was not run beside DNA after 2016, so neither rule can be scored on 2017+; the lesson is that a rule calibrated in 2015-16 would drift in meaning as the water changed.

**Sensitivity (SPEC 6).** LOW-MEDIUM. Public-health framing, no deaths involved. Facilitator note: "wrong call" is relative to a lab standard, not illness; the beaches named are real public parks, so describe results neutrally and do not rank neighborhoods. Name the beaches or anonymize as Beach 1-8? Recommend real names (data is public) with the equity discussion handled in the facilitator note.

**Split risk.** NONE. **Coverage-inflation guard.** 1 thin skill claimed, well under 15.

**Ending suggestion.** Not a phone buzz or pen/paper: the lifeguard captain walks to the flag pole and looks back at her; Beatriz has the two threshold cards in her hand and the halyard is already clipped on.

---

### C2 - Which Cliff First   ·   score 1.2 (2 skills, 1 claimed how-to is a stretch)   ·   tier T3   ·   Data HIGH

(Rework of the old C2 "Whose Acre-Feet". The old A/B was a constructed counterfactual of a decision that did both moves; this version drops the Flaming Gorge lever and asks the single release-volume choice, which was a real, documented fork.)

**Frozen decision date.** 2022-04-29 (Reclamation announced the May 2022 action on 2022-05-03 [carried from the 2026-10-04 sheet, UNVERIFIED in this pass]). Use USGS data through 2022-04-01 only (last day I model from). Everything after goes in the Twist.

**Protagonist.** Teodoro Pruitt (fictional), a hydrologist in a river-operations office, who owns the one slide the downstream states and the power customers will both read.

**The dilemma.**
A.) Hold Glen Canyon Dam's annual release at 7.48 maf for the coming years OR
B.) Cut it to 7.00 maf.

**Two clocks (no single currency; honest multi-criteria).**
- Clock 1, the compact line: the ten-year total of USGS Lees Ferry flow (gauge 09380000) must not fall below 82.5 maf (75 maf plus a contested Mexico share) [the 82.5 interpretation is UNVERIFIED here; 75 maf is the Compact figure, and the Lower Basin reads it as 82.5]. Deterministic given the release.
- Clock 2, the power pool: Lake Powell elevation (USGS 09379900) falling under 3,490 ft [3,490 carried from the old sheet, UNVERIFIED in this pass]. Probabilistic; depends on which inflow record you replay.

**Primary metric.** Months of runway before the first cliff on Clock 1 or Clock 2, replaying historical inflow traces (the Index Sequential Method). Secondary (students must present both): feet of Powell above 3,490 at month 48.

**Scope fixed before looking.** Replay each historical water-year sequence starting April of year Y (Y = 1923-2016, 94 traces) into a monthly mass balance from the 2022-04-01 elevation of 3,523.1 ft [CONFIRMED USGS]. Records: full (1923-2016), stress (1988-2016), recent (2000-2016).

**Model [DERIVED, disclosed assumptions].** Inflow proxy = daily means of three USGS gauges (09180500 Colorado near Cisco, 09315000 Green River at Green River UT, 09379500 San Juan near Bluff), summed and x 1.04; evaporation 350 kaf/yr [UNVERIFIED assumption]; surface area A(E) = 77,000 + 270 x (E - 3,520) acres, fitted to the implied area from net inflow and elevation change over three windows (94,848; 82,132; 76,861 acres at the 2019, 2020, 2021 windows) [DERIVED from fetched data; Reclamation's area-capacity table not fetched, so the real curve is UNVERIFIED]. Release spread evenly by month; WY2022 remainder = target minus the Oct-Mar 2021-22 gauge total (3,405 kaf [CONFIRMED]).

**Brute-force results [DERIVED].**
| Clock / metric | A hold 7.48 | B cut 7.00 | Winner / margin |
|---|---|---|---|
| Clock 1 compact line crossed (WY, deterministic) | WY2026 (81.66 maf) | WY2025 (81.37 maf) | A by 12 months of 54 = 22.2% (2 pts over 20%) |
| Feet above 3,490 at month 48, median, full record | 158.2 | 176.7 | B by 10.5% |
| same, stress 1988-2016 | 97.6 | 119.6 | B by 18.4% |
| same, recent 2000-2016 | 90.9 | 113.2 | B by 19.7% |
| P(Powell < 3,490 within 24 months), full / stress / recent | 0.13 / 0.27 / 0.28 | 0.08 / 0.13 / 0.17 | B (relative gaps 38-52%, over 20%) |
| Months of runway to first cliff, mean, full / stress / recent | 48.1 / 41.9 / 40.2 | 39.4 / 37.4 / 36.1 | **A at every scope** (18.1% / 10.8% / 10.1%) |

**Honest balance verdict.** No option is dominated (A wins the compact clock, B wins Powell buffer and risk), but *on the single primary "months of runway" metric A wins every record*, because the compact clock is fixed and caps B at 42 months. So the case cannot be framed as one-metric/one-winner; it must be taught as a trade-off where the student chooses the metric (runway vs buffer vs risk) and defends it. That is the "metric-choice argument" shape the reviews asked for, but R1a must rule whether a case with no single primary metric is admissible. If not, drop C2. I did not tune: the release pair (7.48, 7.00) is the real fork; the 2-pt miss on Clock 1 is reported as is.

**Why it's close.** The extra 0.48 maf is worth about 6 ft of Powell and about one year on the compact line. Under the full record Powell almost never reaches the power pool (13% vs 8%); under the 1988-onward stress record it is a one-in-four event, so which "normal" you plan on flips which cliff worries you.

**Would close.** `measurement-volume` (term, n=2): acre-feet of storage = area x depth. `geometry-how-to-find-the-volume-of-a-cone` (n=2) is a stretch (a frustum slab); claim only if case-write forces it, else drop. `calculus-how-to-find-the-area-between-two-curves` (n=2) is tempting (gap between two cumulative-release curves) but is computed by subtraction; do not claim. Score is therefore small.

**Data feasibility: HIGH.** USGS NWIS daily values, no key: Lees Ferry 09380000 (WY1922-2021, 100 complete water years), Powell 09379900 elevation (daily from 2019-04-19), Cisco 09180500, Green River 09315000, Bluff 09379500. [CONFIRMED fetched.] USGS data are provisional where marked; USGS data policy (public domain, cite USGS) [UNVERIFIED: quote the data-use page]. Reclamation RISE (data.usbr.gov) is reachable but my location-search returned unfiltered results, so I did not use it; storage-elevation table [UNVERIFIED, not fetched].

**Twist [DERIVED from USGS, provisional].** Reclamation's actual action cut WY2022 to 7.00 maf (gauge total 7.07 maf, [CONFIRMED]). WY2023 was a wet year (8.73 maf at Lees Ferry). Ten-year Lees Ferry totals: 85.41 (WY2022), 85.87 (WY2023), 85.86 (WY2024), 84.22 (WY2025). Powell never reached 3,490: the daily low through 2026-10-26 is 3,516.4 ft on 2026-09-16. So the stress-record fear did not materialize in four years; the hold-vs-cut choice was never tested.

**Sensitivity (SPEC 6).** MEDIUM. Seven-state politics and the Compact reading: use neutral third person, present the 82.5 maf as a contested reading, no state blamed. Human stake for a 7th-12th grader: the lake that holds a dam that lights a few million homes and the drinking water of several large cities (customer counts [UNVERIFIED]); not a death-risk topic.

**Split risk.** NONE (but small new coverage). **Ending suggestion.** Teodoro stands at the elevation marker painted on the side of a boat ramp, 33 ft of dry concrete between the waterline and the line he is defending; he steps down onto the first dry slab.

---

### C3 - Four Labs, Eight Beaches   ·   score 1.0   ·   tier T3   ·   Data HIGH

**Frozen decision date.** 2016-10-31, same data as C1 (reuse a different beat of the same protagonist world only if C1 is not built; do not build both in one batch).

**Protagonist.** Aurelio Dellacroce (fictional), a district lab manager whose budget funds four rapid DNA tests a morning for eight beaches. The other four beaches get a rain rule (flag if >= 12.7 mm, half an inch, fell in the 24 hours before 08:00 at the beach's nearest weather station; Oak Street covers 12th St/Ohio/North Ave, 63rd Street station covers 63rd/South Shore/Calumet/Rainbow, Foster covers Montrose [DERIVED mapping, an assumption: coordinates not checked]).

**The dilemma.**
A.) Put the four DNA tests at the four dirtiest beaches (most culture exceedances in the 2015 data) OR
B.) Put them at the four beaches where the rain rule was wrong most often in 2015.

**Primary metric.** Wrong calls in 2016 (DNA threshold 1,000 CCE where tested; rain rule elsewhere), plans chosen from 2015 data only. Lower is better.

**Brute force [DERIVED].** There are C(8,4) = 70 possible plans. 2016 wrong calls across all 70: best 63 (12th St, 63rd St, Rainbow, South Shore), median 73, worst 82 (evaluated on the 2016 pairs that have a near-complete 24 h rain record; 525 of 629 pairs across both seasons qualify). Rule A picks {63rd, Calumet, Montrose, Rainbow}: 78 wrong. Rule B picks {Calumet, Montrose, Rainbow, South Shore}: 74 wrong. Margin B over A 5.4%. In-sample 2015: A 42, B 41. With DNA threshold 500: A 71, B 70. With a 6.35 mm rain rule: 97 vs 94 (3.2%) at 1,000 and 90 vs 90 at 500.
**Balance verdict.** Neither rule dominates, but both lose to the unconstrained best plan by 11-15 calls, and the A-B gap (0-4 calls) is inside year-to-year noise; I cannot show a scope where A wins. A and B each differ by one beach. Weakest of the three. Treat as an extension to C1 or as a "Challenge 3" deliverable, not a standalone case.

**Would close.** `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination` (how-to, n=2): forced by the 70-plan count. Order does not matter, so do not claim permutation. Score 1.0.

**Data.** Same Chicago portal sets as C1 plus k7hf-8y75 hourly rain [CONFIRMED]. **UNVERIFIED:** station-to-beach mapping; gaps in the rain record (61 of 629 pairs have no rain data in the 24 h window; 525 have >= 18 of 24 hours).

**Sensitivity.** LOW. **Twist.** As C1.

---

## Verification log (what I actually fetched, 2026-10-28)
- Chicago Data Portal (SODA): 9wd3-tqr2 (629 paired rows), hh4t-tnq8 (18,002), hmqm-anjq (17,594), 2ivx-z93u (34,967 combined), k7hf-8y75 (hourly rain, 31,242 rows for 2015-05 to 2016-10; Foster, Oak St, 63rd St). Dataset description with 235 CFU / 1,000 CCE thresholds read from /api/views/9wd3-tqr2.json.
- USGS NWIS daily values: 09380000 (1921-10-01 start), 09180500, 09315000, 09379500, 09379900 (2019 onward), plus a 2021-2026 pull of 09380000 and 09379900 for the Twist.
- NRCS AWDB (SNOTEL Tony Grove Lake 823:UT:SNTL) and USGS Logan River 10109000: fetched and tested as a "which normal" snowpack-trigger idea, REJECTED: the 1981-2010 and 1991-2020 April-1 medians are both 35.3 in at that station, so there is no baseline effect to argue about, and Jul-Sep flow is regulated.
- US Drought Monitor county API (usdmdataservices.unl.edu) reachable; not used.
- Reclamation RISE API reachable but location search unreliable; not used.
- Not verified: licences of USGS / City of Chicago data (policy-level public domain [UNVERIFIED]); Reclamation area-capacity table; 3,490 ft and 82.5 maf figures; May 2022 action details; all protagonists fictional (names checked absent from cases/: Vandermolen, Beatriz, Teodoro, Pruitt, Aurelio, Dellacroce).
