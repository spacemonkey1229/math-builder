# CONCEPTS: agriculture-food (Food, Energy & Resources) - 2026-10-27

Verified concept sheet. Tags: **[CONFIRMED]** = fetched and read by me this session; **[DERIVED]** = my own computation from fetched data (recomputed in code, all numbers below);
**[ASSUMPTION]** = disclosed constructed input; **[UNVERIFIED]** = not fetched.

**Target.** Domain `agriculture-food` (`readmodel/domains.json`): 0 of 10 signature skills uncovered (ratio n=30, proportion n=21, mean n=28, percent-of n=90, etc.), so there are no
zero-coverage holes to close. I targeted only skills at n<=7 that a farm/food decision naturally exercises; scores are small by construction. Rank on story, data and balance.

**Overlap check.** `cases_index.json`: existing agriculture-food cases are `food-rationing` (family calorie days), `fast-food`, `catering`. Nothing on commodity prices, crop choice,
grain marketing, or protein-per-dollar. `cases/_concepts/`: the only farm-adjacent hit is `next10-careers-gapclose` C8 `the-irregular-boundary` (Nebraska pivot-field boundary
geometry, already built) - unrelated math and decision. No prior sheet for agriculture-food.

**Source reachability (important).** From this sandbox every `*.usda.gov` host failed DNS (`nass.usda.gov`, `quickstats.nass.usda.gov`, `ers.usda.gov`, `ams.usda.gov`),
so **NASS QuickStats, ERS Commodity Costs & Returns and AMS are [UNVERIFIED] for this sheet** even though domains.json lists NASS as LIVE. Confirmed-live substitutes (all fetched,
HTTP 200, data parsed): FRED CSV endpoint (BLS average retail prices; IMF global commodity prices), Our World in Data grapher CSVs (FAOSTAT yields), USDA FoodData Central API
(`api.nal.usda.gov`, DEMO_KEY - this host resolves). Recommend `case-research` re-test NASS from a normal network before writing C2.

| Rank | Concept | Story | Score* | Data | Tier | Margin (computed) |
|---|---|---|---|---|---|---|
| C1 | Protein Per Dollar | Egg-price shock (avian flu) vs chicken breast at a food pantry, Aug 2024 | 2.0 | HIGH | T2 | chicken wins by 9.8% |
| C2 | The March Price | Plant corn or soybeans on 400 acres, March 2024 prices | 1.2 | MEDIUM | T4 | soybeans win by 8.1% |
| C3 | Sell Or Store | Sell corn at harvest or bin it until June, Oct 2017 | 0.6 | MEDIUM | T3 | sell wins by 3.5% |

*score = (sum of how-to weights 1.0 of thin skills claimed) x availability factor (HIGH 1.0, MEDIUM 0.6; C2/C3 scored MEDIUM because the cost input is assumed). Small because the domain has no holes; none exceeds the 15-skill inflation guard.

**Recommendation.** Write **C1** first: it is the only concept built entirely on confirmed live public data (BLS prices + USDA nutrient values), needs no invented costs, and the
margin (9.8%) is in the target band with a real both-sides story (eggs win ~89% of months since 2006, chicken wins in the spike months, and the spike was live news). C2 is the
richest T4 lesson (planning price vs realized price) but its cost gap is a disclosed assumption until NASS/ERS can be fetched. C3 is a good T3 backup.

---

### C1 - Protein Per Dollar   ·   score 2.0   ·   tier T2
**Protagonist.** Ms. Okafor (fictional), purchasing coordinator for a mid-size community food pantry that buys a fixed $12,000 a month of fresh protein for its client
families. She places the standing order for the next quarter on a Friday in August 2024 and cannot change it for 13 weeks.
**Story.** Real and recognizable: egg prices rose through 2024 as avian influenza (HPAI) hit laying flocks, then peaked in early 2025. Protagonist and pantry are constructed
and disclosed as such; all prices are real BLS national averages.
**The dilemma.** A.) Spend the protein budget on Grade A large eggs OR B.) Spend it on fresh boneless skinless chicken breast.
**Primary metric.** Grams of protein per dollar at the August 2024 price. Eggs: 12 x 50 g x 12.56 g/100 g = 75.36 g per dozen (large egg 243 g / 4.86 = 50 g from the FDC portion
table); chicken breast: 453.6 g x 22.5 g/100 g = 102.06 g per lb.
**Computed [DERIVED] (code, Aug 2024).** Eggs $3.204/dozen -> 23.52 g/$. Chicken breast $3.952/lb -> 25.82 g/$. Chicken ahead by 9.8% (25.82/23.52 - 1).
**Both options win somewhere [DERIVED].** Over the 248 months where both BLS series exist (Jan 2006 - Sep 2026): eggs win 220 months, chicken wins 28 (the 2015 spike, mid-2024
to mid-2025, and Jan 2023). Jan 2024: eggs $2.522 vs chicken $4.086 -> 29.88 vs 24.98 g/$, eggs ahead by 19.6%. Break-even egg price at Aug 2024 chicken price: $2.918/dozen
(actual $3.204 is 9.8% above it). Break-even chicken price at the Aug 2024 egg price: $4.339/lb. Margin <= 20% at the decision point; nobody dominates across time.
**Why it's close / what the student must defend.** Static answer in Aug 2024 is chicken by under 10%. But the egg price is climbing month by month (Aug $3.204 -> Sep $3.821 ->
Dec $4.146 -> Feb 2025 $5.897) while chicken is flat ($3.95-$4.10), and a 13-week standing order locks the quantity. Does the Hero buy on today's ratio, or on the trend? Raw
price, edible portion (shell loss), and ratio-vs-range thinking all matter; the metric is deliberately only protein, so the student must say what it leaves out (fat, kid
acceptance, cold storage).
**Spine skills.** `measurement-how-to-find-equivalent-ratios` (n=7; unit-rate comparison as scaled ratios), `statistics-and-probability-range` (n=9; spread of monthly
protein-per-dollar since 2006). Supporting, already heavy: `measurement-ratio`, `advanced-numbers-how-to-find-the-percent-of-a-number`. n<=2 skills closed: 0 (domain has none).
**Data feasibility - HIGH.**
- FRED series `APU0000708111` Eggs, Grade A, Large, per dozen, US city average (BLS): [CONFIRMED] fetched CSV via `https://fred.stlouisfed.org/graph/fredgraph.csv?id=APU0000708111`,
  title confirmed from `https://fred.stlouisfed.org/series/APU0000708111`.
- FRED series `APU0000FF1101` Chicken breast, boneless, per lb (BLS, from Jan 2006): [CONFIRMED] same method.
- USDA FoodData Central API (`https://api.nal.usda.gov/fdc/v1/food/171287` eggs 12.56 g protein/100 g; `/food/171077` chicken breast skinless boneless raw 22.5 g/100 g;
  `/food/173734` black beans 21.6 g/100 g): [CONFIRMED] fetched with DEMO_KEY. Free, student-explorable with `https://fdc.nal.usda.gov/`.
- Note for research: dry beans (`APU0000714233`, $1.67/lb) would beat both on protein/$ (about 58 g/$), so the dilemma is deliberately framed as "which fresh protein the
  cooler-based pantry orders"; research should disclose that bound rather than hide it.

---

### C2 - The March Price   ·   score 1.2   ·   tier T4
**Protagonist.** Dana Whitfield (fictional), operator of 400 tillable acres (about 162 ha) of Illinois-type cropland, deciding in March 2024 what to plant; seed and fertilizer
commitments are made now and cannot be reversed for a year.
**Story.** Recognizable: the corn-vs-soybean rotation decision every Corn Belt farm faces each spring, made on March prices and judged in October.
**The dilemma.** A.) Plant all 400 acres to corn OR B.) Plant all 400 acres to soybeans.
**Primary metric.** Expected net return per hectare = national-average yield x March price - per-hectare cost. Costs are a disclosed assumption: corn $1,700/ha, soybeans
$1,000/ha (a $700/ha gap, about $283/acre) [ASSUMPTION]. The case's main lesson is that the break-even cost gap is a derived quantity the Hero can solve for.
**Computed [DERIVED].** March 2024 IMF prices: maize $190.23/t, soybeans $433.53/t; 2024 US yields (FAOSTAT via OWID): maize 11.253 t/ha, soybeans 3.413 t/ha.
Corn gross $2,140.7/ha, soy gross $1,479.4/ha. Net: corn $440.7, soy $479.4 -> **soybeans win by $38.7/ha = 8.1% (of the larger net)**, 8.8% of corn's net.
Break-even cost gap = $661.3/ha; break-even corn price $193.67/t (+1.8% vs March); break-even soybean price $422.18/t (-2.6%).
**Both options win somewhere [DERIVED] (same costs, March planning prices, 2014-2024).** Corn wins 2014, 2021, 2022, 2023; soybeans win 2015-2020 and 2024. Margin by year ranges
from 1.9% (2019) to 70.8% (2017), so the case picks a near-tie year on purpose. **Planning vs realized twist:** at October 2024 prices ($189.59 maize, $368.49 soy) corn nets
$433.5/ha and soy $257.5/ha, corn ahead 40.6%. March information flips with the harvest-price move, which is the T4 lesson.
**Why it's close.** At a $661/ha break-even gap and a $700/ha assumed gap, a 3% move in soybean price or 2% move in corn price flips the call; students defend the cost
assumption and whether to trust March prices (Hero should state the assumption per SPEC T4).
**Spine skills.** `advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-both-sides` (n=3; solve corn net = soy net for break-even price), `measurement-how-to-find-equivalent-ratios`
(n=7; t/ha and acre/ha conversion, price ratio). Supporting: `statistics-and-probability-mean`. n<=2 skills closed: 0.
**Data feasibility - MEDIUM-HIGH (prices and yields HIGH; costs ASSUMED).**
- FRED `PMAIZMTUSDM` (IMF, global price of maize, US Dollars per metric ton, monthly) and `PSOYBUSDM` (soybeans): [CONFIRMED] fetched via `fredgraph.csv?id=...` (1992-2026).
  Caveat: global (US Gulf) benchmark, not Illinois cash price - disclose.
- OWID/FAOSTAT yields `https://ourworldindata.org/grapher/maize-yields.csv` and `.../soybean-yields.csv`: [CONFIRMED] fetched; United States rows through 2024/2025.
  National average yield, not a farm yield - disclose.
- Cost per acre: USDA ERS Commodity Costs and Returns and NASS QuickStats county yields / prices received: **[UNVERIFIED]** (usda.gov hosts unreachable here). If a research pass
  confirms ERS, replace the $700/ha assumption with the published corn-minus-soy cost gap and re-run; the margin must be recomputed then.

---

### C3 - Sell Or Store   ·   score 0.6   ·   tier T3
**Protagonist.** Marcus Hale (fictional), 600-acre corn grower with on-farm bin space for his whole crop, deciding in October 2017 whether to sell at harvest or hold until June.
**Story.** Recognizable: the oldest marketing decision in agriculture ("carry" vs "cash at harvest"), exactly the third archetype in the domain's decision_archetypes.
**The dilemma.** A.) Sell the whole crop at the October 2017 harvest price OR B.) Store it and sell in June 2018 at that month's price.
**Primary metric.** Net dollars per tonne after storage cost = price received - storage cost (bin/handling $0.05 per bushel per month and 6% annual interest on the harvest-time value,
over 8 months) [ASSUMPTION, typical Extension-style figures, UNVERIFIED]. 1 tonne of corn = 39.368 bu.
**Computed [DERIVED].** Oct 2017 maize $148.72/t; June 2018 $165.14/t (+11.0%). Storage cost = 8 x 0.05 x 39.368 + 0.06 x 8/12 x 148.72 = $21.70/t. Store nets $143.44 vs $148.72 sell,
**sell wins by 3.5%**. Break-even June price: $170.42/t.
**Both options win somewhere [DERIVED].** Over harvest years 1992-2024 (33 years), storing beats selling in 8 (1994, 1995, 2006, 2007, 2010, 2018, 2020, 2021) and loses in 25. The
adjacent year is the mirror: Oct 2018 $160.37 -> June 2019 $195.17, store nets $173.01, **store wins by 7.9%**. Years within 10% either way: 1994, 2003, 2006, 2015, 2017, 2018, 2024.
**Why it's close.** An 11.0% price rise sounds like a win but is just under the 14.6% needed to cover storage ($21.70 on $148.72); the decision is whether the Hero treats the historical hit rate (8/33, about 24%) as a base rate, and how
a few large winners (2007 +75%, 2020 +57%) skew the mean versus the median.
**Spine skills.** `statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-` (n=1; "what June price would the 2017 gain need so the mean gain
across seasons covers storage?"), `statistics-and-probability-mean` (n=28, supporting). Closes 1 skill at n<=2.
**Data feasibility - MEDIUM-HIGH (prices HIGH; storage cost ASSUMED).**
- FRED `PMAIZMTUSDM` monthly maize price: [CONFIRMED] fetched (1992-2026); global US Gulf benchmark, not local cash basis.
- Storage rates and local basis (NASS prices received, university Extension budgets, CME futures spreads): **[UNVERIFIED]**. Research must source a published storage rate
  or keep it disclosed; the 3.5% margin moves with it (a $0.40/bu all-in storage cost is within sensitivity).
