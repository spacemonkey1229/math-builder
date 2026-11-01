# CONCEPTS: hydrology-water (Earth, Climate & Environment) - 2026-10-03

Slot: one of four non-sports slots paired with the sports-science wave. Working direction was "flood-frequency / return-period call
from public gauge data". This is a **verified** concept sheet (web fetched 2026-10-04). Tags: **[CONFIRMED]** fetched and read by me;
**[DERIVED]** my own computation from fetched data (recompute at research); **[UNVERIFIED]** not confirmed, cut or disclose.

**Target.** Domain `hydrology-water`; `readmodel/domains.json` lists 0 of 9 signature skills uncovered, so there are no zero-coverage holes to
close. I scored only skills at `n <= 3` ("thin"), weights per SKILL.md. Scores are therefore small; rank on story and data too.

**Overlap check (cases_index.json).** Existing: `deluge-gun` (sprinkler arcs), `creek-span` (bridge steel cost), `tide-window`,
`total-flow` (acre-feet of floodwater per $1k across two design storms), `the-contrapositive-claim` (flood-damage insurance clause).
None is Ellicott City, Oroville or Lake Powell. Closest: `total-flow` (design-storm flood volume). C1 must differ: its spine is
return period / exceedance probability and a rainfall-vs-gauge mismatch, not volume-over-capacity per dollar.

| Rank | Concept | Event | Score | Data | Tier |
|---|---|---|---|---|---|
| C1 | The Thousand-Year Street | Ellicott City MD floods, 2016 and 2018 | 3.2 | HIGH | T3 |
| C2 | Whose Acre-Feet | Lake Powell / Flaming Gorge drought response, May 2022 | 2.0 | HIGH | T2 |
| C3 | The Weir at 901 | Oroville Dam spillway crisis, Feb 2017 | 1.0 | HIGH | T2 |

**Recommendation.** Write **C1**. It is the direct fit to the release-plan direction (return period from public data), the data is free and
already confirmed, and it has a built-in modelling lesson (the famous "1-in-1000" is a rainfall statistic, and the nearest big USGS gauge
barely registered the flood). Kill-or-defer **C3** first: richest data but the heaviest sensitivity (188,000 evacuated), and it closes almost
no thin skills. C2 is a good backup and the best "reservoir volume" case the domain one-liner promises.

---

### C1 - The Thousand-Year Street   ·   score 3.2   ·   tier T3
**Protagonist.** Priya Raman (fictional), a county stormwater engineer in a Maryland county, who must put a recommendation on the County
Executive's desk before the council votes the capital budget; her own family business sits on the street in question. Personally at stake: she
signs the design memo.
**The dilemma.** A.) Build the current Safe-and-Sound package with the shorter North Tunnel, designed to the county 100-year standard, cheaper and
sooner OR B.) Extend the North Tunnel (about 5,000 ft, 18 ft diameter) so a 2016-class storm leaves under half a foot on Main Street, at a much
higher cost and a later finish.
**Primary metric.** Expected 30-year flood damage avoided per dollar of added capital cost (ratio; probability from the return period
by 1-(1-p)^30, damage from flood depth). Fallback metric if damage curve is too soft: feet-of-Main-Street-depth removed per $10M.
**Why it's close.** The extended tunnel wins on the rare extreme event (about 3.5 ft down to under 0.5 ft in a 2016-class storm) but a 2016-class
storm has an annual probability near 0.001 on the rainfall record, so its expected-value payoff is small per dollar. The cheaper package wins
on expected value if the 1-in-1000 label is right, and loses badly if the label is wrong (two such storms arrived 22 months apart). The case
turns on whether a student trusts the return-period statistic, and independence of the two events.
**Would close (4 skills counted, 2 how-to / 2 term; all at n <= 3):**
| id | kind | label |
|---|---|---|
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | How to find the volume of a cylinder (the tunnel bore: 18 ft diameter x 5,000 ft; compare to the flow it must carry) |
| statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data | how-to | Fit peak flow vs ln(return period) from the gauge's annual peaks (Gumbel-type plotting-position line) |
| statistics-and-probability-line-of-best-fit | term | Line of best fit |
| statistics-and-probability-independent-event | term | Independent event (2016 and 2018 storms; p of two in 22 months) |
**Already-covered skills it also exercises.** `measurement-how-to-convert-an-amount-with-compound-units` (cfs, gal/s, acre-feet),
`advanced-operations-how-to-evaluate-an-exponential-expression` ((1-p)^n), `statistics-and-probability-how-to-determine-the-probability-of-a-compound-event`,
`advanced-numbers-how-to-find-the-percent-of-a-number`, `statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data`.
**Data feasibility: HIGH.** Sources I fetched:
- USGS NWIS annual peak flows, site 01589000 Patapsco River at Hollofield MD, free RDB at `nwis.waterdata.usgs.gov/nwis/peak?site_no=01589000&agency_cd=USGS&format=rdb`. [CONFIRMED] 69 peaks on file; top four: 80,600 cfs (1972-06-22, Agnes), 46,500 (1975), 36,000 (1933), 22,800 (2016-07-30). The 2018 peak there was 12,100 cfs (2018-06-03). [DERIVED] Weibull T = (n+1)/rank gives about 17.5 yr for 2016 and about 5.4 yr for 2018 at that gauge.
- NOAA Atlas 14 PFDS point estimates, free CSV at `hdsc.nws.noaa.gov/cgi-bin/new/fe_text_mean.csv?lat=39.2670&lon=-76.7983&data=depth&units=english&series=pds` (301-redirects, use -L). [CONFIRMED] 60-min: 3.05 in (100-yr), 4.10 in (1000-yr); 2-hr: 3.85 in (100-yr), 5.45 in (1000-yr). Coordinates are my approximation of Old Ellicott City; the file header says "Ohio River Basin" (a labelling quirk), recheck at research.
- NWS Sterling event page: 6.17 in in 90 min at the Ellicott City gauge, 2 deaths, NWS says rainfall probability at 5 min to 3 hr durations was at most 1/1000. [CONFIRMED]. NWS/USGS stage rise "just over 13 ft in 100 minutes" for the Patapsco at Ellicott City. [CONFIRMED]
- Howard County Executive pages (howardcountymd.gov): May 13 2019 plan announcement (Option 3G.7.0, 4 demolitions vs 10, under 1 ft vs 4.5 ft in a 100-yr storm, $113.5M to $140.5M); March 2021 extended North Tunnel release; extended tunnel cuts a 2016-type storm from about 3.5 ft to under 0.5 ft. [CONFIRMED via fetch and search snippets; reread the 2021 release for exact wording]
- Cost trail: search results show a $141M Kiewit construction award, a revised North Tunnel budget of $252M, a roughly $430.5M Safe-and-Sound planning total, completion Fall 2027. [UNVERIFIED: aggregator snippets (citizenportal.ai, CBS), re-source from county financial report PDFs before use. Do not use the cost of the *extension alone*; the increment is not yet found.]
Sources I am NOT confident about: the cost of the extension versus the shorter tunnel at decision time (2021), the county flood-depth modelling method, and any damage-per-foot curve. Likely a labelled Modeling Assumption with a sensitivity table. The Tiber-Hudson branches have no USGS peak series of their own (tributary of about 3 sq mi, [UNVERIFIED] drainage area), and that is the point of the case, but state it as a limitation.
**Sensitivity (SPEC §6).** Two people died on 2016-07-30. Facilitator flag: frame as protection of a street, never recount the deaths for effect; note the 2018 flood also killed a National Guardsman [UNVERIFIED].
**Split risk.** NONE (4 thin skills claimed).
**Balance-test note.** Not dominated: B wins depth in the extreme tail and public-safety optics; A wins cost, speed, expected value, and fewer disruptions. Margin is plausible at 5-20% once added cost is sourced, otherwise tune the 30-year horizon, which is a disclosed assumption.

---

### C2 - Whose Acre-Feet   ·   score 2.0   ·   tier T2
**Protagonist.** Dana Whitcomb (fictional), a Reclamation water-operations analyst in the Upper Colorado region, who must tell the Commissioner's office where 500,000 acre-feet comes from this spring. Personally at stake: her name is on the 24-Month Study that both states will read.
**The dilemma.** A.) Draw an extra 500,000 acre-feet from upstream Flaming Gorge Reservoir to prop up Lake Powell OR B.) Cut Glen Canyon Dam's annual release further (past the 7.00 maf already set) by the same 500,000 acre-feet, leaving it in Powell and sending less to Lake Mead.
**Primary metric.** Feet of Lake Powell elevation gained per foot of source-reservoir elevation lost (ratio of volume-over-area on each side). Secondary: acre-feet per foot at each reservoir.
**Why it's close.** The same volume lifts Powell by dV/A_Powell but lowers Flaming Gorge by dV/A_FG, and the surface areas differ a lot, so A pushes the cost onto a smaller reservoir (recreation, fish, Wyoming and Utah). B costs nothing upstream but starves Lake Mead and the Lower Basin and raises compact-delivery questions. The protagonist is defending 3,525 ft (35 ft above the 3,490 ft minimum power pool).
**Would close (2 skills, 2 how-to / 0 term):**
| id | kind | label |
|---|---|---|
| geometry-how-to-find-the-volume-of-a-cone | how-to | Model a reservoir basin as an inverted cone/frustum from two storage-elevation points to estimate surface area at a given elevation |
| geometry-how-to-find-the-volume-of-a-prism | how-to | Slab method: dV = area x depth between two elevations |
(Cone modelling is a stretch; confirm in case-write that it is forced and not decorative, else drop to prism only, score 1.0.)
**Already-covered skills it also exercises.** `measurement-how-to-convert-an-amount-with-compound-units`, `measurement-how-to-find-a-missing-amount-in-a-proportion`, `advanced-numbers-how-to-find-the-percent-of-a-number`, `advanced-operations-scientific-notation` terms.
**Data feasibility: HIGH.** Sources I fetched:
- Reclamation Upper Colorado Historic Data tool (`usbr.gov/rsvrWater/HistoricalApp.html`): daily and monthly elevation, storage, inflow, release for Powell and Flaming Gorge, Excel/table/graph output. [CONFIRMED page content] Terms: no restrictive terms stated, min/max overlays use WY1980-2010.
- Reclamation RISE API (`data.usbr.gov/rise/api/...`), free JSON. [CONFIRMED reachable; my location-name query returned unfiltered results, so Powell's location id is UNVERIFIED]
- May 2022 action: 500,000 af from Flaming Gorge plus 480,000 af by cutting Glen Canyon releases from 7.48 to 7.00 maf, about 1 million af to Powell by April 2023; Powell at 3,522 ft, lowest since filling; 3,490 ft minimum power pool [CONFIRMED via Reclamation/AOP and news results]. The 24-Month Study PDF (`usbr.gov/lc/region/g4000/24mo/2022/MAY22.pdf`) is a compressed PDF I could not text-extract; read it manually.
Sources I am NOT confident about: Flaming Gorge surface area and the area-capacity tables (need Reclamation area-capacity table); how much Flaming Gorge water is lost in transit [UNVERIFIED, a Colorado Sun piece exists]; the legal framing of option B (the 2022 decision made both moves, so this binary is a constructed counterfactual, disclose it).
**Sensitivity (SPEC §6).** NONE. Politically charged across seven states; keep both sides in neutral third person.
**Split risk.** NONE.
**Balance-test note.** Risk of near-domination: option A can look cheaper if recreation harm is not priced. Needs a sourced cost of lost Flaming Gorge hydropower or a fixed delivery penalty on B.

---

### C3 - The Weir at 901   ·   score 1.0   ·   tier T2
**Protagonist.** Marcus Ohlsen (fictional), a State Water Project operations engineer at a state water agency on the afternoon of 2017-02-09, with a damaged spillway chute and a storm still coming. Personally at stake: if the emergency weir fails, he made the call.
**The dilemma.** A.) Keep the main spillway at a moderate release (protecting the eroding chute) and accept that the lake may rise to the 901 ft emergency spillway crest, never used before OR B.) Raise the main spillway release hard now to keep the lake below 901 ft, at the cost of accelerating chute erosion and flooding the Feather River channel.
**Primary metric.** Hours of buffer before the lake reaches 901 ft per 10,000 cfs of release (storage buffer divided by net inflow, converted from cfs-days to acre-feet).
**Why it's close.** B buys time on the clock and A protects the structure; both could fail, and the forecast inflow is uncertain. Real history: the lake did rise to 901 ft on 2017-02-11, the emergency spillway ran for the first time, headward erosion threatened the weir, and the release was pushed to 100,000 cfs on 2017-02-12.
**Would close (1 skill counted, 1 how-to / 0 term):**
| id | kind | label |
|---|---|---|
| geometry-how-to-find-the-volume-of-a-prism | how-to | Storage band as area x depth between 890.9 ft and 901 ft, area back-solved from CDEC storage |
**Already-covered skills it also exercises.** `measurement-how-to-convert-an-amount-with-compound-units` (cfs to acre-feet per day), `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`, `measurement-how-to-find-a-missing-amount-in-a-proportion`.
**Data feasibility: HIGH.** Source I fetched: California Data Exchange Center (CDEC), station ORO, hourly/daily CSV, free: `cdec.water.ca.gov/dynamicapp/req/CSVDataServlet?Stations=ORO&SensorNums=6,15,76,23&dur_code=D&Start=2017-02-06&End=2017-02-14`. [CONFIRMED] Daily mean values: elevation 850.85 (Feb 6), 890.92 (Feb 9), 899.44 (Feb 10), 902.57 (Feb 11); storage 2,819,768 af (Feb 6) to 3,396,134 af (Feb 9), 3,578,367 af (Feb 11); inflow 48,795 cfs (Feb 6) to 155,498 cfs (Feb 9); outflow 11,687 cfs (Feb 8) rising to 60,697 (Feb 10), 99,999 (Feb 13). Wikipedia timeline [CONFIRMED]: damage first noted Feb 7, 901 ft crest, 12,600 cfs over the weir on Feb 11, 100,000 cfs main spillway Feb 12, 188,000 evacuated. DWR Independent Forensic Team final report (Jan 2018) exists [CONFIRMED by search, not read].
Sources I am NOT confident about: the exact planned vs actual release schedule on Feb 8-10 and the forecast the operators saw [UNVERIFIED, read the IFT report], the 901 ft storage figure (take from CDEC or the DWR area-capacity table), downstream channel capacity.
**Sensitivity (SPEC §6).** HIGH. Mass evacuation of 188,000 people and a possible 30-ft wall of water. Needs a facilitator note (hindsight bias, no one was killed, do not dramatize the evacuation). Recommend deprioritizing for a younger cohort.
**Split risk.** NONE, but under-claims skills; the case is mostly well-covered math.
**Balance-test note.** Strong hindsight bias: students know A led to the weir erosion. Mitigate by giving only the information available on Feb 9.

---

## Verification log (what I actually fetched, 2026-10-04)
- USGS NWIS peak RDB for 01589000 (69 peaks, values above) and 01586000 North Branch Patapsco at Cedarhurst (not used; 2016 peak 2,120 cfs there, 2018-07-25 peak 8,670 cfs). Daily mean at 01589000 on 2016-07-30 was only 2,380 cfs, which shows how a 90-minute flash flood hides inside a daily mean (useful teaching point). USGS waterservices iv/dv endpoints respond.
- NOAA Atlas 14 PFDS CSV (values above).
- NWS Sterling 2016 event page; Howard County 2019 plan page; web search for the extended tunnel, Safe-and-Sound costs, May 2022 Powell action, Oroville timeline.
- Reclamation Historic Data page, RISE API reachability; CDEC ORO CSV.
- Not verified: USGS and NOAA reuse terms (both US-government public-domain by policy [UNVERIFIED, quote the data-use pages]); Reclamation 24-Month Study PDF content; 2018 flood fatality; all fictional protagonists are invented.

---

## Round 2 revision - C1 "The Thousand-Year Street" (2026-10-04)

Original C1 text above is kept unchanged and is **superseded where it conflicts**. Tags as before: [CONFIRMED] fetched and read, [DERIVED] my computation, [UNVERIFIED] not confirmed.

### Verdict (stated first)
**Does NOT pass the balance test. No honest two-sided dilemma exists in the documented 2021 tunnel-extension decision. Recommendation: DROP C1 as a decision case; swap to C2 (Lake Powell) as the hydrology slot, unreviewed by me, needs its own round-1 review.** The rainfall-vs-gauge lesson is real and strong but is a statistics lesson, not a purchase dilemma; it can be folded into another case as an evidence module (see end). Nothing below is a pass claim.

### 1. The real decision and why it is not two-sided as documented
Howard County release of 25 Mar 2021 (howardcountymd.gov/News032521c) [CONFIRMED by fetch; Patch repeats it]: extended North Tunnel is about 5,000 ft starting near 8800 Frederick Rd; eliminates three West End projects (8777 culvert, 8600 culvert, 8552 berm/bypass); "anticipated to be cost neutral with the elimination of the West End projects"; saves at least 9 buildings from demolition (incl. Earlougher's Tavern, Tersiguel's); 2016-type storm depth on Main Street about 3.5 ft down to under 0.5 ft; about 10 easements, only 3 from the extension; construction goal 2022; WIFIA loan funding. The real alternative was the 2019 plan (Option 3G.7.0, $113.5M-$140.5M all-in with 4 demolitions per my earlier fetch) with a shorter North Tunnel plus the West End projects.
By the county's own account the extension is **cost-neutral, saves more buildings, and removes more water**: it dominates. That is not a dilemma. The only documented costs that could make it two-sided are not decision-time numbers:
- Cost of the West End projects: **not found** in any county document I could open (financial reports list only current sub-projects; West End projects are gone). So "cost neutral" cannot be checked.
- Extension increment: The Banner figure (1,600 ft / $77M becoming about 1 mile / $141M, increment $64M) is **single news source, not re-sourced**; I could not find it in county documents. If used it must be labelled "as reported by The Banner" and is not a county figure. [UNVERIFIED]
- Hindsight costs (county Q3 FY2026 Safe & Sound financial report, cc.howardcountymd.gov, [CONFIRMED]): North Tunnel original estimate (as given to Council, May 2025) $267.2M, revised $252M (drop of Rogers Ave drop structure); whole C0337 program $430.4M original estimate / $425.6M revised; 2019 all-in plan was $113.5M-$140.5M. County also says construction costs rose over 25% since 2019 (News013023). Completion now fall 2027 versus the 2022 construction goal in 2021. These show the *outcome* was far costlier than the 2021 framing, but they are hindsight and the report does not give the counterfactual West End cost, so no fair comparison exists.

### 2. Computations (Python, run 2026-10-04) - does either option dominate?
(a) Original metric, 30-year hit probability 1-(1-p)^30: p=0.001 -> 2.96%; 0.002 -> 5.83%; 0.005 -> 13.96%; 0.01 -> 26.03%. Even at p=0.01 the expected-value case for the expensive option is weak; reviewers were right that the original metric lets A dominate at p=0.001.
(b) Extension vs West End, net added cost = $64M x (f - g), f = extension overrun factor, g = West End overrun factor (hypothetical, both unsourced). Per-building cost uses the 9 buildings saved:
| f \ g | 1.0 | 1.25 | 1.5 |
|---|---|---|---|
| 1.0 | $0 | -$16M | -$32M |
| 1.25 | +$16M ($1.8M/bldg) | $0 | -$16M |
| 1.5 | +$32M ($3.6M/bldg) | +$16M | $0 |
| 1.9 (actual NT estimate $267.2M / $141M = 1.90) | +$57.6M ($6.4M/bldg) | +$41.6M ($4.6M/bldg) | +$25.6M ($2.8M/bldg) |
Reading: when f <= g the extension is cheaper AND better (dominates). It only becomes two-sided if the extension overran more than the alternative would have, a condition no source establishes. Whether it is "worth" $2.8M-$6.4M per saved building is a values call, but it rests entirely on assumed g, so the margin is invented, not documented. **Balance test: not computed as passing; fails on sourcing.**

### 3. Rainfall figure (R1b point 2) - re-checked against weather.gov/lwx/ellicottcityflood2016 and USGS FS 2021-3025
- NWS page table (image ellicottcitypcpn.png, read directly), gauge **ELYM2, the Howard County automated rain gauge at the county government facility, Ellicott City**: 60 min 4.56 in; **90 min 5.48 in**; 2 h 5.96 in (6:50-8:50 pm); storm total **6.60 in**. 
- **The sheet's "6.17 in in 90 min" is wrong/stale** (NWS says its table was updated 2 Aug 2016). Use 5.48 in / 90 min.
- **"10.63 in in 1h25m at the Howard County gauge" does NOT appear on the NWS page** (text or table) or in my web search. It cannot be sourced from the cited page; I did not find it anywhere. Do not use it unless the reviewer supplies a citation. ELYM2 is the only gauge the NWS page names; MRMS radar estimates over 6 in near Ellicott City are a separate (radar) product.
- 1-in-1000: NWS HDSC says observed rainfall at the Ellicott City gauge for 5 min to 3 h has probability <= 1/1000 per year. USGS adds May 27 2018: 6.56 in total at ELYM2 (5.00 in from 3:53-5:53 pm), "essentially the same probability" (0.1 percent), though ELYM2 was outside the heaviest 2018 rainfall.
- NOAA Atlas 14 (my earlier fetch, coordinates approximate): 60 min 100-yr 3.05 in, 1000-yr 4.10 in; 2 h 100-yr 3.85, 1000-yr 5.45. Observed 4.56 (60 min) and 5.96 (2 h) exceed the 1000-yr values. [DERIVED]

### 4. 2018 peak date and regulation (R1a point 4)
- USGS 01589000 (Hollofield) peak file re-pulled: 69 peaks, 2016-07-30 = 22,800 cfs (14.24 ft). The 12,100 cfs peak is dated **2018-06-03**, a **different storm** from the Ellicott City flood of **27 May 2018**. USGS FS 2021-3025 gives Hollofield flows for the 27 May 2018 event as 6,100 cfs (6.89 ft), (the fact sheet writes "May 30" in one place; I treat it as a typo of 27 May; flag it). The 6,100 value is below that year's annual peak so 27 May 2018 is not in the annual-peak list at all. Remove "2018 peak 12,100 / T about 5.4 yr" from the sheet.
- Qualification codes: 55 peaks code 6 ("affected by regulation or diversion"), 2 code "2,6", 1 code 5, 1 "2,7,Bd" (1933 estimated), 10 blank. So 58 of 69 carry code 6: Gumbel fits are **not clean frequency analysis** (upstream reservoir regulation, Liberty). My Gumbel (method of moments, all 69 values, ignoring codes), [DERIVED]: T(2016 peak 22,800) about 9 yr (Weibull 17.5 yr); Q100 about 45,200 cfs. Treat as classroom illustration with this caveat, not as hydrology.
- Useful contrast: the Patapsco gauge sees a large regulated basin; the Main Street problem is three tiny creeks (Hudson 1.26 mi2, Tiber 0.53, New Cut 1.53; confluence 3.68 mi2) with USGS indirect peaks 2016/2018 (cfs): Hudson 2,750/3,000; Tiber 2,100/2,700; New Cut 3,320/6,160. [CONFIRMED USGS FS 2021-3025] Two storms with rainfall at the 1/1000 level produce river-gauge ranks of only about 9-17 yr (2016) and nothing (27 May 2018): this is the genuine "rainfall frequency vs gauge frequency" lesson.
- Label-vs-record probabilities [DERIVED]: if the true annual p of such rain at the gauge is 0.001, P(two in a 22-month window) = 1.7e-6 for one site; in an 80-yr record about 1.5e-4. But across N independent sites, expected "double clusters" in 80 yr = 0.15 (N=1,000), 1.5 (N=10,000), 15 (N=100,000): a cluster somewhere is not astonishing, one at *this* gauge is. At true p=0.01, P(>=2 in 80 yr) = 19%; p=0.02 -> 48%. This teaches independence, selection effect, and the limits of a 1/1000 label.

### 5. Human stakes and hook (R1c)
- Drop the fictional "Priya Raman, family business on the street" entirely. Real, named losses if ever discussed: two people died on 30 Jul 2016 (names not retrieved here, use public NWS/press, facilitator-flagged); the 2018 death is **Sgt. Eddison Hermond Jr., 39, Maryland Army National Guard, off duty, swept away trying to rescue a shop owner on 27 May 2018** (Baltimore Sun, ABC, Fox5, WUSA9 [CONFIRMED via search; CBS was the reviewer's cite]). No dramatization; a case would use at most a single factual line with consent-style facilitator notes.
- Regional-hook problem: Ellicott City is Baltimore-metro local. Stronger hook that matches the real mathematics: "A label says 1 in 1,000. It happened twice in 22 months at the same rain gauge. Is the label wrong, or are you unlucky?" That is a universal question (any student has seen a 'once in a century' headline).
- But it is an inference question; to be a *Math Builder* dilemma it needs a spend. The only real spend (tunnel) fails the balance test (section 2). Therefore not a case as-is.

### 6. Recommendation
1. **DROP C1 as a dilemma case.** No sourced cost for the alternative, the extension increment is single-source news, and the county's documented position is that its choice dominates. Inventing the missing West End cost would create the very "tuned" dilemma the review flagged.
2. **Swap to C2 "Whose Acre-Feet" (Lake Powell / Flaming Gorge, May 2022)** from this sheet as the hydrology slot; it needs a fresh round-1 review (I have not verified it).
3. Optionally salvage the statistics (ELYM2 table, Atlas 14 comparison, Hollofield regulated peaks, the N-sites clustering computation) as an evidence module for a future flood/insurance case where a real premium or deductible gives the two-sided choice (cf. existing `the-contrapositive-claim`).
4. Do not propagate to the case list: the unconfirmed "10.63 in" figure, the "2018-06-03 = Ellicott City 2018 flood" date, the Priya Raman protagonist.

Sources: howardcountymd.gov/News032521c; weather.gov/lwx/ellicottcityflood2016 (+ ellicottcitypcpn.png); pubs.usgs.gov/fs/2021/3025/fs20213025.pdf; nwis.waterdata.usgs.gov peak RDB 01589000 (pulled 2026-10-04); cc.howardcountymd.gov Q3 FY2026 Safe and Sound Financial Report; howardcountymd.gov/News052422b, News013023, News020325; Baltimore Sun/Fox5/ABC coverage of Sgt. Hermond.
