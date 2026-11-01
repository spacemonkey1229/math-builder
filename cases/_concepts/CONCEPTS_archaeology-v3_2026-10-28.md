# CONCEPTS: archaeology (Deep Time & Language), v3 - 2026-10-28

Round-3 re-brainstorm. Replaces `CONCEPTS_archaeology_2026-10-03.md` (C1 Twenty-Eight Rings rejected by R1a: degenerate metric at equal spend, wrong 14C figure). That C1 is NOT revived: its fixes needed the paper's ring table and a sourced spike-catch probability, neither of which I could supply. C2 (human remains) and C3 (no dataset) are not revived either (SPEC 6 / lesson 5).

**Margin convention (stated once):** margin = gap / winner's value, on the stated primary metric. Dates: all analysis below was run in Python on files fetched 2026-10-28 into the session scratchpad.

**Honest summary.** I ran brute-force checks on three designs. Only C1 is a clean two-sided result at a scope I fixed before looking; its weakness is bin-sensitivity (disclosed, and made part of the case). C2 is a tie on its headline metric, so it needs a second criterion before it can be a binary. C3 fails a one-metric balance test (pollen dominates) and is offered only as a reserve / Twist source. Nothing here is a confident GO on all three reviewers; C1 is the recommended build.

Evidence tags: **[FETCHED]** file opened and computed on this session; **[UNVERIFIED]** not fetched; **[ASSUMPTION]** disclosed modelling choice.

| Rank | Concept | Story | Shape | Feasibility |
|---|---|---|---|---|
| C1 | The Busiest Century | New Mexico radiocarbon dates, dates vs sites | metric-choice / definition-dependent | HIGH (data in hand, CC0) |
| C2 | One Core or Two | Dating a historic timber building from tree rings | allocation of a fixed wood budget | MEDIUM-HIGH (data in hand; stake needs second criterion) |
| C3 | Seed or Pollen | White Sands footprints, USGS data release | accuracy vs precision (method choice) | HIGH data / LOW balance (reserve) |

**Recommendation: build C1**, with the bin-sensitivity table inside the case and the facilitator note on Ancestral Pueblo communities.

---

## C1 - The Busiest Century   -   tier T3

**Story.** A regional museum is designing the wall-sized headline of a new gallery: "In what century were the most people living here?" The evidence is the public record of radiocarbon dates from New Mexico sites. Two defensible readings of "most": count the dates (where researchers have measured the most), or count the sites (how many different places show activity). They name different centuries. The student must pick one for the headline and defend it, including why one heavily dug site can drag a date count.

**Protagonist.** Fictional composite, disclosed: **Linnea Dalgleish**, exhibit developer at a county museum (name absent from all of cases/ and concepts/). Stake: the headline is carved into the gallery wall in 3 days; school groups read it first. Ending: she stands in the empty gallery with the sign-maker's proof and a ruler (not a phone buzz, not pen/paper).

**Dilemma.** A.) Headline the peak by number of dates (700 cal BP bin) OR B.) Headline the peak by number of distinct sites (1200 cal BP bin).

**Data [FETCHED].** p3k14c release 2025.07 (Zenodo 16394072, repo `people3k/p3k14c`), file `inst/p3k14c_scrubbed_fuzzed.csv`, 173,946 rows, 18 columns (Age, Error, Material, SiteID, SiteName, Province...). README states **Data: CC-0, attribution requested** (the repo's R-package LICENSE is MIT and text is CC-BY; the 2022 reviewers said CC0 for data, consistent). Calibration with IntCal20 `intcal20.14c` from intcal.org [FETCHED; header cites Reimer et al. 2020, Radiocarbon 62; CC BY status per the earlier R1b review, not re-checked]. US coordinates are fuzzed to county scale (disclose; irrelevant here).

**Computation (my pipeline, [ASSUMPTION] disclosed as method).** Keep rows with SiteID, 100 < Age < 8000 14C BP, 0 < Error < 300; each date assigned its IntCal20 median calibrated age (normal likelihood, curve error added in quadrature); bins of 100 calendar years aligned at BP (0 = 1950 CE). New Mexico: 3,678 dates, 870 sites.

Scope fixed BEFORE looking: all eight US states with at least 1,500 usable dates and 150 sites (AZ, CA, CO, IL, NM, TX, UT, WY); the rule "bins aligned at BP, 100-yr, dates vs distinct sites" was written first. Result: dates and sites disagree on the peak bin in exactly NM at 100-yr (and in several states at 500-yr offsets; see fragility). NM 100-yr bin table (dates / sites):

| bin (cal BP) | dates | sites |
|---|---|---|
| 700-799 | **294** | 130 |
| 1200-1299 | 268 | **155** |
| 800-899 | 245 | 131 |
| 1100-1199 | 220 | 145 |

Margins (gap/winner): by dates, 700 beats 1200 by (294-268)/294 = **8.8%**; by sites, 1200 beats 700 by (155-130)/155 = **16.1%**. Both options win on their own metric with margin <= 20%. Third-option dominance check: no other bin is top-2 on either metric except 800 (245 dates, 131 sites), which is below the dates winner and the sites winner on its own best metric (mean of the two rankings: 800 is 3rd on dates and 3rd on sites; the metric each option wins on stays with it). A "thousand-year plateau" answer (the honest scientific reading) is the Twist-level argument, not a third option.

**Fragility, stated plainly (the case's real lesson).** The split is not robust to the bin rule. NM, dates vs sites peak: 100-yr: 700 vs 1200 (split); 200-yr: 600 (524 dates) vs 1000 (216 sites) (split); 500-yr BP-aligned: 500-999 (1,064 dates) vs 1000-1499 (379 sites; 4.6% and 13.2% margins) (split); 500-yr offset 250 and 1000-yr bins: both metrics agree. Utah splits at 500-yr BP-aligned and not at 100-yr; Arizona, CO, TX, CA, IL, WY agree at 100-yr. Reviewers should judge whether a binary that appears under the BP-aligned convention (and not under all shifts) is "one invented rule". I argue it is the standard published convention, and the sensitivity table is itself a deliverable, but this is the main risk. Fallback if R1a rejects: reframe so the student chooses the bin width and sees the answer move (a definition-dependent answer), dropping the 20% claim.

**Why dates mislead (real, from the data [FETCHED]).** Dates per site: median 2, maximum 149 (a single NM site holds 149 of 3,678); top sites hold 94, 66, 46, 37. A few heavily dated sites inflate date counts. Sites miscount the other way: a site with one stray date counts as much as a village with 100.

**Would close (skills with n <= 2; ids checked in standards_spine.json):**
| id | kind | label | forced by |
|---|---|---|---|
| statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data (n=1) | how-to | box-and-whisker plot | deliverable: box plot of dates-per-site, showing the outliers |
| statistics-and-probability-non-linear (n=2) | term | non-linear | weak; drop from claim unless the IntCal20 curve plot is a deliverable (it is optional). Claim 1 skill honestly. |
Also exercises already-covered mean/median/range, bar chart, percent, ratio. Score floor ~1.0 (one thin how-to).

**Deliverables (core 4):** (1) 100-yr table of dates and sites for NM; (2) box plot of dates per site; (3) the same peak under two other bin rules; (4) one-sentence headline plus the sentence that defends it.

**Sensitivity (SPEC 6).** Sites are ancestral to living Pueblo and other Native communities. Facilitator note: frame as "what the evidence shows about when places were in use"; no "vanished", "abandoned", "mystery"; no ranking of peoples; a century is a measure of researcher effort as much as of population. Dates are of charcoal, wood, bone etc.; no human remains discussed.
**Overlap.** None (no archaeology or radiocarbon-bins case; `the-survey-slot` is astronomy; `the-reserve-asymptote` is actuarial). Metric-choice shape matches the elections model, not a one-parameter break-even.
**Facts to freeze (SPEC 5):** database release 2025.07; as-of 2026-10-28; later releases only in the Twist.
**UNVERIFIED:** IntCal20 licence text (not re-read); whether the museum framing needs a real museum named (keep fictional); that students can reproduce the median-calibration step without code (provide a pre-calibrated NM extract as an appendix; mark the extract as derived).

---

## C2 - One Core or Two   -   tier T3-T4

**Story.** A town wants a state historic-register plaque for its old timber mill, which requires a felling date in a stated range. A tree-ring lab can take a fixed amount of wood from the building (a conservator's cap on total rings removed). Spend it on one long core of ~90 rings from the biggest beam (A), or on two ~45-ring cores from two different beams (B)? The date is found by sliding the ring pattern along a reference chronology and picking the offset with the best match.

**Protagonist.** Fictional composite: **Haruto Nakagawa**, building conservator at a county historical commission (name absent from cases/). Stake: a wrong plaque year; the commission's volunteers and school-group tours are scheduled around the date. Ending: the first core tube is held up to the window light, no phone, no pen over paper.

**Data [FETCHED].** NOAA NCEI International Tree-Ring Data Bank (ITRDB) .rwl files, Southwest "Archaeological+Modern" chronologies: az570 (Canyon de Chelly), az572 (Flagstaff), az578 (Hopi Mesa), co652 (Mancos + Mesa Verde), ut543 (Natural Bridges), nm613 (Cebolleta Mesa): 563 series of at least 150 rings. NOAA paleo data are public; terms page not re-read [UNVERIFIED licence wording]. The "timber" series are real archaeological and living-tree ring series; the mill story is a disclosed scenario (the case never claims these specific beams are from a mill).

**Computation [FETCHED, run 2026-10-28].** Series detrended by ratio to an 11-yr moving average; reference = mean of the other series at the same site (at least 5 overlapping); score = Pearson r at each candidate offset; "correct" = best offset is the true year. Fixed before looking: equal wood budget (90 rings vs 45+45 ending in the same felling year), 3 random seeds, all six sites.
- 363 trials: A correct 79.6%, B correct 79.6% (288 both right, 73 both wrong, 1 A-only, 1 B-only). Margin 0.0% on the headline metric. The two designs tie; success is determined by the site chronology, not the design: co652 100%, az570 82.5%, az578 81.8%, ut543 68.4%, az572 57.4%, nm613 46.7% (identical for A and B at each site).
- Side result, single 50-ring core, correlation vs sign-agreement (percent GLK): r right 79.5%, GLK right 66.7% over 156 trials; they pick different years in 32% of trials; GLK is uniquely right in 1.
**Balance verdict: NOT YET a binary.** A tie on accuracy is fine for SPEC 2 only if the case supplies a real second criterion that separates them: B guards against one idiosyncratic tree and gives two beams' worth of provenance, A gives continuous ring-run and leaves one beam intact. Those are qualitative here. To build, add one sourced quantity (for example the lab's per-core fee from a published price list [UNVERIFIED, not fetched]) or turn the case into the 3-way choice of which site-quality tier to trust. R1a should decide.

**Would close:** `statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-combination` (n=2; choosing which 2 of k beams to core: C(k,2) is a deliverable), `statistics-and-probability-independent-event` (n=2; are two cores from one site independent? the data say no: A and B tie), `statistics-and-probability-multistage-sampling` (n=2; site then tree then segment). Also box plot (n=1) of per-site success rate. Score floor ~2.2 if all four are forced.
**Overlap.** None (no tree-ring or dendrochronology case; grep of cases/*/case.md for tree.ring/dendro returns only mentions in airplane-manufacturer, cooling-curve, fast-food, which are unrelated "tree" mentions).
**Sensitivity.** Several of the archaeological series come from Ancestral Pueblo and Navajo-area sites; keep the case about a historic mill and a building plaque, never about those communities. No human remains.
**UNVERIFIED:** the register's felling-date requirement (invented scenario, disclose; do not name a real register rule); lab fee; that the pass rate of 79.6% generalises (six sites, one detrending choice); ITRDB terms.

---

## C3 - Seed or Pollen   -   tier T4 (RESERVE; fails the one-metric balance test)

**Story.** White Sands, New Mexico: human footprints (including those of teenagers and children) in a dry lakebed, dated to roughly 23,000-21,000 years ago from seeds of an aquatic plant, Ruppia cirrhosa. Critics said aquatic plants can carry old carbon (reservoir effect). The team can date more seeds, date terrestrial conifer pollen (hard: ~75,000 grains per date), or date the sediment by optically stimulated luminescence (OSL).

**Data [FETCHED].** USGS data release (ScienceBase item 647782fed34e3ac335becbb0, DOI 10.5066/P9E36U4B, released 2023-10-05; Pigati et al. 2023, Science 382:73-75, DOI 10.1126/science.adh5007). Files: radiocarbon table (11 seed dates, 3 pollen dates, 3 pollen blanks/standards, elevation per sample), OSL table (3 minimum ages: 21.5+-1.9, 20.6+-2.1, 18.0+-1.8 ka, 2-sigma). USGS public-domain style; metadata states "public domain, also contains copyrighted materials as noted in the text" [FETCHED].
Computed: pollen calibrated ages 23.43+-2.49, 22.77+-2.36, 22.64+-2.35 ka; error-weighted mean 22.92 ka, 2-sigma half-width 0.57 (lower bound 22.35). Seeds at the same three horizons: 22.08, lower bound ~22.04. Seed age vs elevation, n=11: slope about 49 years per cm, r = -0.79 (older deeper, as stratigraphy requires).

**Balance check (failed).** Metric "lower 95% bound on age, minus an assumed reservoir offset R for seeds, pollen unaffected": pollen 22.35 beats seeds (22.23 minus R) at every R from 0 to 2.5 ka (margins 0.5%-11.7%, always B): option A is dominated. OSL's lower bounds (19.6, 18.5, 16.2) lose to both on that metric. Adding a cost makes it one break-even on one parameter. So as a binary it is a one-sided "precision vs accuracy" lesson, not a defensible fork.
**Best use.** Keep as the Twist for C1-style radiocarbon cases or a short "interpret the table" exercise: the seed ages agree with pollen, as the real study found. Fails lesson 2 (single parameter) and lesson 1 (dominating option).
**Would close:** none that C1/C2 do not. `statistics-and-probability-non-linear` not forced.
**Sensitivity.** Footprints, not remains; keep to dating, not "who they were".
**UNVERIFIED:** Pigati 2023 prose (only the USGS tables and a search summary read); original Bennett et al. 2021 seed values; pollen-effort cost.

---

## Checks run (summary for the caller)
- C1: all-state scan (8 groups) for dates-vs-sites peak split; NM 100-yr margins 8.8% (dates) and 16.1% (sites); bin-width/offset sensitivity table; a site-weighted variant (each site's dates sum to 1) was run only at 250/500/1000-yr bins and followed the site count there; NOT run at 100-yr (untested).
- C2: 363 equal-budget trials, tie at 79.6%; per-site rates; side metric test r vs GLK on 156 trials.
- C3: lower-bound dominance across R in [0, 2.5]: B (pollen) always wins; OSL dominated; seed vs elevation fit.
- Names checked absent from cases/ and concepts: Dalgleish, Nakagawa. Forbidden names avoided.
- Rejected ideas: L'Anse aux Meadows rework (needs the paper's table); Richard III (remains, sourced blocked); Stonehenge A303 (no dataset); Treasure-Act "is it treasure" (definition only, no math); mound/amphora volume cases (decision not found).
