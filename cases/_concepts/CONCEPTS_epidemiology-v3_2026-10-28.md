# CONCEPTS: epidemiology v3 (3 ranked concepts, fresh brainstorm) - 2026-10-28

Tags: **[CONFIRMED]** fetched and parsed this session; **[DERIVED]** recomputed in python from the fetched files this session; **[ASSUMPTION]** disclosed scenario input; **[UNVERIFIED]** not fetched/confirmed.
The Pool Size and The Flat Dose stay rejected (twin of the-overlap-call; label forbids vial reuse) and are not re-proposed. v1 (`CONCEPTS_epidemiology_2026-09-18.md`, The Surge Trigger) is already built; no concept here re-uses "when to trigger on a curve".

**Margin convention (stated once, used everywhere).** Margin = (winner's value - loser's value) / winner's value. Break-even moves are stated as a percent change of the *current* value and labeled as such.

**Why these three.** Existing epidemiology-adjacent cases: cold-chain (cooler packing), the-overlap-call (union vs intersection testing), the-vein-to-vein-window (thaw time), the-trial-size (cluster survey), the-sample-plan (ANSI Z1.4), the-parity-check (error bits), the-surge-trigger, six-degrees-of-exposure (hub vs random vaccination), medical-statician, the-marginal-detection. None compares *rates across populations*, which is the daily work of the Public Health Data Analyst career in `readmodel/domains.json`. All three concepts below sit there, with three different shapes: **metric choice**, **baseline choice**, **model-and-window choice**. None is a single-parameter break-even.

**Brainstormed and killed with computation (do not revive without a repair).**
- *School-level measles catch-up, rate vs head-count* (CDPH kindergarten file, [CONFIRMED] fetchable). Scan of 14 counties showed the modeled outcome saturates (a capped vaccination removes the whole modeled outbreak at either school) and the file has reporting oddities (a 702-student charter with MMR2 = 23% beside OTHERS = 79%); naming real schools also stigmatizes. Killed.
- *Wastewater vs county case-rate as the early signal* (NWSS + CDC county transmission, [CONFIRMED] fetchable). Backtest on TX/OH/GA, May 2023-Apr 2024: Spearman rho against next-week county admissions was 0.05-0.13 for both signals, with only 2 usable weeks per state (cases suppressed). No usable signal, so no decision. Killed.
- *Cause-vs-cause in Louisiana (stroke vs unintentional injuries)*: balanced across benchmarks (3% / 5.5% / 12%), but heart disease, cancer and Alzheimer's beat both at every benchmark (2,307 / 1,046 / 593 excess deaths vs 458 / 444), so the binary exists only through a Background exclusion rule. Killed. Kentucky (C2) is the one state where the two finalists are the true top two under all four benchmarks.
- *COVID age-priority (75+ vs essential workers)*: 75+ wins deaths-averted per dose by about an order of magnitude on any published age-specific rate. Fails the 20% test. Killed.
- *Hospital-trigger backtest, one-vs-two-dose, NNV by age, rapid-test PPV*: reduce to one break-even on one parameter, or to a dominating option, or sit too close to the-surge-trigger / the-overlap-call. Not written up.

---

## Ranking

| Rank | Concept | Shape | Tier | Margin (gap/winner) | Data | Recommendation |
|---|---|---|---|---|---|---|
| **C1** | **The Retirement State** (Florida vs Georgia) | Metric choice: crude vs age-adjusted rate | T3 | Crude: FL ahead 17.8%. Age-adjusted: GA ahead 15.3% | HIGH, all fetched | **PICK** |
| C2 | The Benchmark (Kentucky heart disease vs cancer) | Baseline choice: what counts as "excess"? | T3 | 6.9% (A) to 19.1% (B) across 4 fixed benchmarks | HIGH, all fetched | Backup (A is thin, see 2.4) |
| C3 | The Crossover (Oklahoma heart disease vs cancer deaths) | Model-and-window choice for a forecast | T4 | 0.7%-3.1% across 8 fixed variants | HIGH, all fetched | Third (same cause pair as C2) |

**Common data spine.** NCHS Leading Causes of Death, `bi63-dtpu` on data.cdc.gov ([CONFIRMED] fetched 2026-10-28; licence "Public Domain U.S. Government", terms https://www.usa.gov/government-works; columns year, cause_name, state, deaths, aadr; age-adjusted to the 2000 US standard population; 1999-2017; 10 causes + All causes; 50 states, DC and "United States"). Population: Census `nst-est2019-alldata.csv` ([CONFIRMED] fetched; POPESTIMATE2010-2019). Crude rates here are **[DERIVED]** deaths / Census population x 100,000; CDC WONDER's published crude rates use NCHS's own population bridge and may differ at the rounding level: **[UNVERIFIED]** until `case-research` compares. No flip below depends on a gap smaller than 7%.

---

## C1. The Retirement State   ·   tier T3   ·   epidemiology (public-health data analysis)

**Protagonist.** Wilhelmina Thornbury (fictional; 0 grep hits for "Thornbury" in `/cases` and `readmodel`; first name to be re-grepped at write time), program officer at a regional health foundation. Not on the banned list.

**Overview seed (150-300 words in the case; no numbers).** In medias res at a light table in the foundation's conference room the night before the board meets. Wilhelmina has two transparent maps of the same Southeast, shaded from the same data, and Florida is dark on one and pale on the other. Her grandfather moved to Florida at seventy "for the sun"; her college roommate is from Georgia, where the high school stadium doubles as the county's blood-pressure screening site. The charter says the Fund exists "to reduce the burden of death in the communities it serves," and two trustees who never agree have each asked her which map is the honest one. Ending (new; not a phone-buzz, not a pen over paper): she lays one transparency over the other on the light table and watches two states trade colors. Stops there.

**Background constraints.** One award, one state, one year. The board has narrowed the finalists to two (ASSUMPTION, stated). Decision date frozen at **July 2019**, using the latest final NCHS year, **2017** [UNVERIFIED release month; `case-research` to confirm]. No 2018+ number appears before the Twist. Scenario assumption: the board has only the two rates it was handed (true of the open dataset: totals and age-adjusted rates, no age-specific rows).

**The dilemma.**
You are Wilhelmina Thornbury.
Do you:
A.) Award the Fund to Florida, whose residents die at the higher *crude* rate OR
B.) Award the Fund to Georgia, whose residents die at the higher *age-adjusted* rate.

**Primary metric.** The state's 2017 all-cause death rate per 100,000 relative to the U.S. rate on the same basis, read two ways (crude; age-adjusted). The case's question is which reading the Fund's charter should trust.

**Computed [DERIVED, python from `bi63-dtpu` + Census, 2026-10-28].**
- U.S. 2017: 2,813,503 deaths; population 324,985,539; crude **865.7**; age-adjusted **731.9**.
- Florida: 203,636 deaths; pop 20,963,613; crude **971.4** (12.2% above U.S.); age-adjusted **672.1** (8.2% below U.S.); crude/adjusted 1.445.
- Georgia: 83,098 deaths; pop 10,410,330; crude **798.2** (7.8% below U.S.); age-adjusted **793.7** (8.4% above U.S.); crude/adjusted 1.006.
- **Crude: Florida wins by 17.8%** ((971.4-798.2)/971.4). **Age-adjusted: Georgia wins by 15.3%** ((793.7-672.1)/793.7). Each state is "worse than average" under exactly one lens.
- Ranks among 50 states + DC: Florida 17th on crude, 44th on age-adjusted; Georgia 42nd on crude, 13th on age-adjusted.
- Signed excess deaths versus the U.S. age-adjusted rate: Florida (672.1 - 731.9) x 209.64 = **-12,536**; Georgia (793.7 - 731.9) x 104.10 = **+6,434**. Versus the U.S. crude rate: Florida +22,147; Georgia -7,028.
- **Robustness [DERIVED]:** the same flip holds in every year 2010-2017 (Florida crude 922.2 -> 971.4, Georgia 733.8 -> 798.2; Florida age-adjusted 701.1 -> 672.1, Georgia 845.4 -> 793.7). Not a one-year artifact.

**Pre-fixed scope and balance tests (scope fixed before looking at results).** All 1,275 pairs among 50 states + DC, 2017 all-cause. **280 pairs reverse order between crude and age-adjusted.** Florida-Georgia is the largest-population such pair (both over 10 million) with both margins under 20%. Swaps available if a reviewer prefers a different story: Colorado-Hawaii (15.2% / 11.8%), New York-Texas (11.7% / 15.2%). **Dominance check:** no lens in the data gives either state a >20% win; no lens makes one state win on both. **Invented-rule check:** crude and age-adjusted are the two standard published rates; nothing the case invents decides the winner. A reviewer will say age-adjusted is "the correct one"; 1.1 below is the answer.

**Why it's close / what the student must defend.**
1.1 *For Florida (A):* a Fund that pays for care and capacity (hospice beds, home health, ambulances, bereavement support; the charter's wording is "the burden of death in the communities it serves") must be sized to deaths that actually happen. Florida has 203,636 against Georgia's 83,098 (2.45x), at a crude rate 17.8% higher per resident. Age adjustment erases exactly the thing a services grant must serve: an older population.
1.2 *For Georgia (B):* compare like with like. At the same ages a Georgian dies at 1.18 times a Floridian's rate (793.7 / 672.1); Georgia is 8.4% above the U.S. and 13th-worst, while Florida is 8.2% below the U.S. Georgia would need 6,434 fewer deaths a year to match the nation; Florida already has 12,536 fewer than the national age-adjusted rate predicts. Prevention dollars do more where risk at a given age is higher; Florida's crude rate is high largely because people retire there.
1.3 The student decides which question the charter asks and defends it to a trustee who disagrees. Metric choice, not a threshold.

**Deliverables (SPEC 1.5 section 3).**
1. A table with crude and age-adjusted rates for Florida, Georgia and the U.S., and each state's signed percent above/below the U.S. on each basis.
2. Signed excess deaths vs the U.S. age-adjusted rate for each state (rate gap x population in hundred-thousands); explain why Florida's is negative.
3. The "age factor" crude / age-adjusted for each state and a sentence on what it measures.
4. One original visual: box-and-whisker plots of all 51 jurisdictions' crude rates and, on the same scale, their age-adjusted rates, with Florida and Georgia marked.
5. A paragraph stating which basis the Fund should use, and what a services grant versus a prevention grant each needs.

**Spine skills (only those the deliverables force; ids checked in `readmodel/standards_spine.json`).** Thin ones marked.
- `advanced-numbers-how-to-multiply-with-negative-numbers` (**n=2**): deliverable 2, (672.1 - 731.9) x 209.64.
- `advanced-numbers-how-to-divide-with-negative-numbers` (**n=2**): deliverable 1, -59.8 / 731.9 = -8.2%.
- `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data` (**n=1**): deliverable 4 (student builds it from 51 values).
- `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90): supporting only, not claimed as new.

**Twist (post-decision; the ONLY place later data appears).** CDC provisional COVID-19 death counts and rates by jurisdiction (`mpx5-t7tu`, [CONFIRMED] fetched, data as of 2026-09-17, public domain), cumulative 2020-01-01 to 2026-09-12: Florida crude 399.6 vs Georgia 360.4 per 100,000 (Florida ahead 9.8%); age-adjusted Florida 270.1 vs Georgia 342.0 (Georgia ahead 21.0%). The same reversal under a new disease.

**Facilitator note (SPEC 6).** All-cause mortality: some students have lost grandparents. Frame the Hero as a professional comparing statistics; do not ask students to value one age group's deaths over another's; say plainly that age adjustment is a statistical device, not a verdict on older residents.

**Data feasibility: HIGH.** `bi63-dtpu`, Census, `mpx5-t7tu` [CONFIRMED]. [UNVERIFIED]: NCHS 2017 release month; WONDER crude-rate agreement; percent of each state aged 65+ (the Census age-file URLs I tried returned 404; use ACS S0101 so the case can say "x% of Floridians are 65+").

---

## C2. The Benchmark   ·   tier T3   ·   epidemiology (public-health data analysis)

**Protagonist.** Gideon Szalai (fictional; 0 grep hits for "Szalai" or "Gideon"), epidemiologist in a state health department's chronic-disease unit in Kentucky.

**Overview seed (no numbers).** In medias res: Gideon is at the break-room whiteboard because the commissioner has just asked a one-line question, "Which one do I fund, heart or cancer?" Two columns on the board each give a different answer depending on where he draws the line called "normal." His mother-in-law, a retired school bus driver in Paducah, is on both lists: a stent and a lump check. Ending: he wheels the whiteboard to the window; the afternoon light washes the two columns into one glare and the commissioner is already in the doorway. Stops at the instant of decision (no marker, no phone).

**Background constraints.** One state prevention line for the year, one program. Heart disease and cancer are Kentucky's two largest excess causes under every benchmark below (checked; the third, chronic lower respiratory disease, is 1,051-1,874 against the pair's 1,376-3,207). "Excess deaths" is the department's planning measure: deaths above what the state would have if its age-adjusted rate matched a benchmark (a CDC "potentially excess deaths" idea; exact CDC benchmark definition **[UNVERIFIED]**). Program-effect assumption (stated, with sensitivity): either program can close the same fraction of its excess. Decision date **mid-2019** with 2017 data (release month UNVERIFIED, as in C1).

**The dilemma.**
You are Gideon Szalai.
Do you:
A.) Fund the cancer program, Kentucky's worst rate in the nation and the larger excess against the U.S. average OR
B.) Fund the heart disease program, the larger excess against what the best-performing states achieve.

**Primary metric.** Excess deaths per year = (Kentucky's 2017 age-adjusted rate minus the benchmark rate) x population / 100,000, per cause, under four benchmarks fixed in advance.

**Computed [DERIVED, python].** Kentucky 2017: pop 4,452,268. Heart: 10,343 deaths, age-adjusted **195.9** (9th highest of 51). Cancer: 10,145 deaths, age-adjusted **185.7** (the highest of all 51). U.S.: heart 165.0, cancer 152.5. State spread: heart rates 119.1 to 237.2 (quartiles 145.8 / 158.0 / 186.2); cancer rates 120.3 to 185.7 (quartiles 145.9 / 154.2 / 164.5).

| Benchmark (fixed before looking) | Heart bench | Cancer bench | Heart excess | Cancer excess | Winner | Margin |
|---|---|---|---|---|---|---|
| U.S. average | 165.0 | 152.5 | 1,376 | 1,478 | **Cancer (A)** | **6.9%** |
| Mean of the best 26 states (half) | 144.5 | 144.1 | 2,288 | 1,851 | Heart (B) | 19.1% |
| Mean of the best 5 (top 10%) | 128.1 | 130.4 | 3,020 | 2,464 | Heart (B) | 18.4% |
| Mean of the best 3 | 123.9 | 126.6 | 3,207 | 2,630 | Heart (B) | 18.0% |
| (extra) single best state | 119.1 | 120.3 | 3,419 | 2,912 | Heart (B) | 14.8% |

Other lenses, same data: percent above the U.S. rate: cancer +21.8%, heart +18.7% (A ahead); national rank: cancer 1st, heart 9th (A ahead); raw 2017 deaths: heart 10,343 vs cancer 10,145 (B by 1.9%). Why it flips: heart-disease state rates spread much wider (119 to 237) than cancer's (120 to 186), so moving the benchmark from "typical" to "best" raises heart's excess faster.

**Pre-fixed scope and balance tests.** Scope: 51 jurisdictions x 10 causes x 4 benchmarks (U.S., best half, best 10%, best 3). Filter: cause pairs that are both in a state's top two under *all four* benchmarks and whose winner flips. **Exactly one state qualifies: Kentucky (heart vs cancer).** Max margin 19.1% (<=20%). Heart wins at every best-k average from k=1 to about k=40 (13-19%); cancer wins only at the U.S.-average benchmark. **A wins 1 of 4 fixed benchmarks.** That asymmetry is disclosed.

**Why it's close / what the student must defend.**
2.1 *For cancer (A):* worst rate in the country; against the national yardstick the larger gap in absolute (1,478 vs 1,376 deaths) and relative (+21.8% vs +18.7%) terms; "excess vs the U.S. average" is what a federal reviewer would compute.
2.2 *For heart (B):* against what top states already achieve, heart's excess is 14.8-19.1% larger; an "achievable" benchmark is how preventable deaths are planned; raw deaths are higher.
2.3 *Possible balance repair, UNVERIFIED:* a years-of-life lens (cancer deaths occur at younger ages) could give A a second win, but age-at-death by cause is not in `bi63-dtpu`; `case-research` would need CDC WISQARS/NCHS tables. If cancer wins on life-years by 5-15%, add it as a third lens and the case is genuinely multi-criteria. If not, C2 stays a backup.
2.4 *Weakness to know:* A wins on one benchmark family only. That is why C2 is ranked second.

**Deliverables.**
1. Excess-death table for both causes under all four benchmarks (rate gap x population; "mean of the best k states" with k stated).
2. Percent above benchmark and national rank for each cause.
3. Box-and-whisker plots of the 51 state rates for heart and for cancer on one axis, Kentucky and each benchmark marked, showing why the spreads differ.
4. A recommendation naming the benchmark the department should adopt, plus what changes if a program can close only half of one cause's gap.

**Spine skills (checked).** `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data` (**n=1**, deliverable 3). `statistics-and-probability-mean` (n=28) and `advanced-numbers-how-to-find-the-percent-of-a-number` (n=90) are supporting only. One thin skill forced; that is why C2 ranks below C1 on spine value.

**Twist.** The department adopts the best-5 benchmark. Later (2018-2022) U.S. heart-disease death rates stop falling. The source for later years is CDC WONDER **[UNVERIFIED, not fetched; `bi63-dtpu` ends at 2017]**. Repair if WONDER stays unreachable: move the decision date earlier (decide with 2011 data, reveal 2012-2017 from the same file).

**Facilitator note (SPEC 6).** Cancer and heart disease touch nearly every family. State-level statistics, not individuals; no personal stories requested; never frame a family's illness as a good or bad investment.

**Data feasibility: HIGH** (`bi63-dtpu`, Census [CONFIRMED]). [UNVERIFIED]: CDC benchmark definition; age at death; Twist source.

---

## C3. The Crossover   ·   tier T4   ·   epidemiology (forecasting)

**Protagonist.** Hollis Dieterle (fictional; 0 grep hits), analyst at the Oklahoma State Department of Health writing a five-year chronic-disease navigator grant.

**Overview seed (no numbers).** In medias res: a projector and a remote on a conference table, and on the screen one line sliding down and one sliding up. The commissioner keeps asking "where do they cross?" because the funder will pay for a navigator network only for the cause that will be larger when the grant ends. Ending: Hollis drags the chart's right edge two years further out and the lines stop agreeing with each other. (Not a phone; not a pen.)

**Background constraints.** Decision frozen at **September 2015**, using the latest final NCHS year then available, **2012** [UNVERIFIED release dates]. Data: Oklahoma annual death counts, heart disease and cancer, 1999-2012. Forecast target: calendar 2017 (the grant's last year). Counts not rates, because the funder pays for patients served (stated). SPEC T4 assumption: the student chooses and defends the fit window and the curve family.

**The dilemma.**
You are Hollis Dieterle.
Do you:
A.) Propose the cancer navigator network, betting cancer deaths pass heart disease deaths by 2017 OR
B.) Propose the heart disease navigator network, betting heart disease is still the larger cause in 2017.

**Primary metric.** Projected 2017 Oklahoma deaths per cause, on a stated fit window and curve family.

**Computed [DERIVED, python from `bi63-dtpu`].** Oklahoma deaths 1999 -> 2012: heart 11,263 -> 9,198; cancer 7,312 -> 8,040.

| Fit window | Model | Cancer 2017 | Heart 2017 | Winner | Margin |
|---|---|---|---|---|---|
| 1999-2012 | linear | 8,179 | 8,064 | Cancer | 1.4% |
| 1999-2012 | exponential | 8,194 | 8,252 | Heart | 0.7% |
| 2003-2012 | linear | 8,433 | 8,169 | Cancer | 3.1% |
| 2003-2012 | exponential | 8,470 | 8,308 | Cancer | 1.9% |
| 2005-2012 | linear | 8,435 | 8,643 | Heart | 2.4% |
| 2005-2012 | exponential | 8,464 | 8,685 | Heart | 2.5% |
| 2008-2012 | linear | 8,620 | 8,740 | Heart | 1.4% |
| 2008-2012 | exponential | 8,658 | 8,768 | Heart | 1.3% |

Full window: cancer +52.7 deaths/year (+0.69%/yr); heart -183.6 deaths/year (-1.78%/yr). **Cancer wins 3 of 8 pre-fixed variants, heart 5 of 8; max margin 3.1%** (SPEC gold standard is 0.09%). R-squared: cancer 0.79 (1999-2012), 0.92 (2003-2012); heart 0.90 (1999-2012), 0.41 (2008-2012; short windows fit poorly).

**Pre-fixed scope and balance tests.** Scope fixed in advance: 4 start years (1999, 2003, 2005, 2008) x 2 model families x end year 2012 x target 2017 x 51 jurisdictions x all cause pairs. Filter: each side wins 2-6 of 8 variants, max margin <=20%, min R-squared >=0.3. **Seven pairs survived; Oklahoma heart vs cancer is the cleanest 3/5 split** (others: DC cancer/heart 2/6, Tennessee CLRD/injuries 6/2, Virginia CLRD/stroke 6/2, Michigan Alzheimer's/stroke 2/6, New Jersey flu/suicide 6/2, Arkansas stroke/injuries 2/6). A mixed program is not allowed (single winner). **Invented-rule check:** window and model are the student's own choices; no hidden rule.

**Why it's close / what the student must defend.**
3.1 *For cancer (A):* the long-run trend rises; the full-window linear fit and the 2003 window both cross before 2017; waiting for heart to fall further is behind the curve.
3.2 *For heart (B):* the larger cause in every year through 2012 (9,198 vs 8,040, a 12.6% lead); the 2005 and 2008 windows put it ahead in 2017 under both models; a decline cannot go on forever.
3.3 The deciding judgments: how far back to look, and whether a decline is a line or a curve. The answer should be a fan of projections, not a number.

**Deliverables.**
1. Scatter plot 1999-2012 with a line of best fit for each cause plus one exponential curve.
2. Projected 2017 for each cause under at least two windows, and a sentence on why they differ.
3. The year each model has the lines cross (including "never").
4. A recommendation stating the window and model, and what evidence would change your mind.

**Spine skills (checked).**
- `statistics-and-probability-non-linear` (**n=2**): deliverables 1 and 3 (exponential vs line).
- `advanced-numbers-how-to-multiply-with-negative-numbers` (**n=2**): deliverable 2, -183.6/yr x 5 years.
- `statistics-and-probability-how-to-draw-a-line-of-best-fit-given-a-set-of-data` (n=4), `advanced-operations-how-to-evaluate-an-exponential-expression` (n=8): supporting only.
Two thin skills forced.

**Twist (the ONLY place later data appears).** The same file holds the answer [CONFIRMED]: Oklahoma 2013-2017 heart 9,721 / 9,868 / 10,310 / 10,209 / 10,772; cancer 8,039 / 7,934 / 8,280 / 8,115 / 8,203. In 2017 heart (10,772) exceeded cancer (8,203) by **23.8%**; heart deaths *rose* 17.1% from 2012 and no window or model forecast it. Population growth and aging also raise counts; students can discuss count vs rate.

**Facilitator note (SPEC 6).** As C2: statewide figures only; no personal stories requested.

**Data feasibility: HIGH** (`bi63-dtpu` [CONFIRMED]). [UNVERIFIED]: NCHS release dates for the "as of September 2015" claim.

**Caveats a reviewer will raise.** (a) Margins are near-ties (0.7%-3.1%): the case is "defend your judgment," not "compute the winner"; keep deliverables from implying one answer. (b) Same cause pair as C2 (different state, different shape). If both are wanted, swap C3 to another survivor (all other survivors are 2/6 or 6/2, so lopsided).

---

## Recommendation

**Build C1 The Retirement State.** It is symmetric (each state wins under one standard lens, by 17.8% and 15.3%), robust across all eight years 2010-2017, uses only standard published rates (no case-invented rule), forces three thin spine skills (n = 2, 2, 1) through named deliverables, and carries a hook every student has (grandparents who retire to Florida). Its Twist (same reversal under COVID-19) is fetched and cited.

## Verification summary

| Check | C1 | C2 | C3 |
|---|---|---|---|
| Both options win somewhere | FL on crude, GA on age-adjusted (both <20%) | cancer at U.S. benchmark; heart at the other 3 benchmarks (<=19.1%) | cancer 3 of 8, heart 5 of 8 (<=3.1%) |
| Scope fixed before results | all 1,275 state pairs, 2017 | 51 x 10 causes x 4 benchmarks, top-2 under all four | 51 x all pairs x 4 windows x 2 models |
| Hidden dominating option | none (two-state shortlist; no lens gives >20% to one) | none (CLRD third, far below); A thin, flagged | none (single winner needed) |
| Invented rule | none | benchmark idea is standard; exact CDC wording UNVERIFIED | window and model are the student's, stated |
| Shape | metric choice | baseline choice | model-and-window choice |
| Twin of existing case | none | none | the-surge-trigger is curve *timing*, not forecast-model choice |
| Thin skills (n<=2) forced | multiply neg (2), divide neg (2), box-whisker how-to (1) | box-whisker how-to (1) | non-linear (2), multiply neg (2) |

## UNVERIFIED items (collected)

1. NCHS final-data release months for 2017 and 2012 (the "as of" dates).
2. Agreement of derived crude rates with CDC WONDER (rounding level; C1's 17.8% is not near a threshold).
3. Percent of each state's population aged 65+ (Census age-file URLs returned 404; use ACS S0101).
4. CDC's exact "potentially excess deaths" benchmark definition (C2).
5. Age at death / years of life lost by cause (C2 repair path; not in the file).
6. Post-2017 source for C2's Twist (C1's and C3's Twists are fetched).
7. CDC WONDER API: three POST attempts to `wonder.cdc.gov/controller/datarequest/D76` returned HTTP 500, so no age-specific death counts were pulled; everything uses the Socrata dataset instead.
8. Licence terms for `bi63-dtpu`, `mpx5-t7tu` and Census are public domain per their metadata ([CONFIRMED] for the two data.cdc.gov views); Census terms not separately read.
