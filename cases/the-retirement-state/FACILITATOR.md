# Guide Notes: The Retirement State

MS/HS | Guide Notes | Adventure | 2026-27
**Case:** The Retirement State · **Tier:** T2 · **Band:** MS-core · **Studio:** MS Adventure
**Primary metric:** a state's 2017 all-cause death rate per 100,000 residents, read two ways: crude (derived: deaths / Census July 1 estimate) and age-adjusted (NCHS-published). The higher rate on a basis is the state that basis points the award at. Rates are the main deliverable; raw counts are out of scope.
**Margin convention (used everywhere below):** gap divided by the HIGHER of the two values, as a percent. **Crude basis: Florida 971.4 vs Georgia 798.2, gap 173.2 points, margin 17.8%. Age-adjusted basis: Georgia 793.7 vs Florida 672.1, gap 121.6 points, margin 15.3%.** Both under the SPEC §2 cap of about 20%. (Dividing by the lower rate instead gives 21.7% and 18.1%; the convention is stated once and D2 tells students to use the higher rate.)
**Status:** researched 2026-10-28. Every figure below is from the 2026-10-28 retrieval of NCHS `bi63-dtpu`, Census `nst-est2019-alldata.csv` and `sc-est2018-alldata6.csv`, and (Twist only) CDC `mpx5-t7tu`; see `data_pull.py`, `RESEARCH_LOG.md`. Never state these to students before Anchor 4 / the Data Deep Dive.

---

## Read first: what this case is and is not

It is a **metric-choice** case. The two states are not "good" and "bad"; each is above the U.S. average on exactly one of the two standard published readings of the same year's deaths, and the student must decide which reading the Fund's charter ("lower the death rate in the communities it serves") asks for. No assumption can be flexed to make the answer fall out; the answer depends on what the student believes the grant buys.

**Rates are the deliverable; counts are out of scope, and the case says why.** Florida had 203,636 deaths against Georgia's 83,098, 2.45 times as many (Florida ahead by 59.2% of its own count), because it has 2.01 times as many residents. The ratio of the two death counts divided by the ratio of the two populations is 1.217, which is exactly the crude-rate ratio (971.4 / 798.2). A count mostly measures size. If a student raises it, use Socratic question 5; do not let the room turn "who has more deaths" into the optimization quantity (SPEC §6).

**Why this pair, stated honestly.** The concept sheet claimed Florida-Georgia is "the largest-population pair" that reverses with both margins under 20%. That claim was false: among the nine states with 10 million or more residents in 2017, the reversing pairs with both margins under 20% also include New York-Texas (11.7% / 15.2%), Florida-Illinois (11.6% / 7.2%), Illinois-Texas (18.5% / 1.6%), Pennsylvania-Ohio (0.0% / 8.5%) and others. The true rule, now printed in Appendix E, is: of the 1,275 pairs among the 50 states and DC, 280 reverse order between the two rates; 241 of those have both gaps under 20% (gap / higher rate); and Florida-Georgia is the one of the 241 whose **smaller** gap is largest (15.3%). Next: Alaska-California 12.5%, Florida-Nevada 12.2%, Colorado-Hawaii 11.8%, New York-Texas 11.7%. Florida-Georgia is also the pair with the largest swing in rank between the two rates (56 places). **Provenance:** the pair was proposed at concept stage and the rule was written afterwards as a checkable description of why it stands out; it is not a pre-registered search, and a facilitator who is asked should say so. Hawaii-Utah and Alaska-Hawaii have larger smaller-gaps (16.5%, 17.5%) but one of their other gaps exceeds 20%.

## The real numbers (facilitator reference, never in case.md)

| | Florida | Georgia | United States |
|---|---|---|---|
| Deaths 2017 (NCHS) | 203,636 | 83,098 | 2,813,503 |
| Residents, July 1 2017 (Census V2019) | 20,963,613 | 10,410,330 | 324,985,539 |
| Crude rate, derived | **971.4** (971.38) | **798.2** (798.23) | **865.7** (865.73) |
| NCHS-published crude rate (NVSR 68-9, Table 12), cross-check | 970.4 | 796.8 | 863.8 |
| Age-adjusted rate (NCHS) | **672.1** | **793.7** | **731.9** |
| Crude vs U.S., signed percent | **+12.2%** | **-7.8%** | 0 |
| Age-adjusted vs U.S., signed percent | **-8.2%** (-8.17) | **+8.4%** (+8.44) | 0 |
| Age factor (crude / age-adjusted) | **1.445** | **1.006** | **1.183** |
| Share aged 65+ (Census V2018, July 1 2017) | 20.1% (4,209,641 of 20,976,812) | 13.5% (1,406,519 of 10,413,055) | 15.6% (50,793,923 of 325,147,121) |
| Rank of 51 on crude (1 = highest) | 17 | 42 | n/a |
| Rank of 51 on age-adjusted | 44 | 13 | n/a |
| Rank of 51 on share aged 65+ | 1 | 47 | n/a |

The derived crude rates differ from NCHS's published crude rates by 0.10% (Florida), 0.18% (Georgia) and 0.22% (U.S.) because NCHS uses its own July 1, 2017 population estimates (the 2010-census series as of 2017), while the case uses Census's Vintage 2019 series. Across all 51 jurisdictions the largest difference is 1.35% (New Jersey; New York 1.32%). Using NCHS's published crude rates, Florida's margin is 17.9% and its crude rank is 18th, not 17th. Nothing flips. Two age-adjusted rates in the open file differ from NCHS's printed table by 0.1 (New Hampshire 717.3 vs 717.2, Wyoming 714.6 vs 714.5); neither state is near a quartile.

**Gap checks (D2).** Crude gap 173.2 points = 17.8% of Florida's 971.4. Age-adjusted gap 121.6 points = 15.3% of Georgia's 793.7. In the gap/lower convention: 21.7% and 18.1%.

**Box plots (D3).** Median-of-halves, 51 values (Appendix C plus the student's own Florida and Georgia crude values).

| | min | Q1 | median | Q3 | max | IQR | fences | outliers |
|---|---|---|---|---|---|---|---|---|
| Crude | 581.6 (Utah) | 815.7 (Idaho) | 907.2 (North Carolina) | 984.6 (South Carolina) | 1281.0 (West Virginia) | 168.9 | 562.35 / 1237.95 | 1281.0 West Virginia |
| Age-adjusted | 584.9 (Hawaii) | 700.1 (Utah) | 735.7 (Texas) | 793.7 (Georgia) | 957.1 (West Virginia) | 93.6 | 559.7 / 934.1 | 951.3 Mississippi, 957.1 West Virginia |

Florida: crude 971.4 sits inside the box, above the median and below Q3; age-adjusted 672.1 is below Q1. Georgia: crude 798.2 is just below Q1 (815.7); age-adjusted 793.7 is exactly Q3 (it is the 38th value). Rank correlation between the two rankings across the 51 is 0.75, so most of the map agrees; 280 of 1,275 pairs (22%) disagree.

**Earlier years (D4; Appendix D plus 2017).** The reversal holds in every year 2010-2017.

| Year | FL crude | GA crude | gap / higher | FL aadr | GA aadr | gap / higher |
|---|---|---|---|---|---|---|
| 2010 | 922.2 | 733.8 | 20.4% | 701.1 | 845.4 | 17.1% |
| 2011 | 913.1 | 726.8 | 20.4% | 677.1 | 815.7 | 17.0% |
| 2012 | 918.7 | 735.7 | 19.9% | 669.9 | 808.6 | 17.2% |
| 2013 | 926.6 | 753.0 | 18.7% | 663.4 | 806.2 | 17.7% |
| 2014 | 937.0 | 763.7 | 18.5% | 662.0 | 801.9 | 17.4% |
| 2015 | 948.8 | 785.4 | 17.2% | 662.9 | 808.1 | 18.0% |
| 2016 | 957.2 | 790.4 | 17.4% | 666.6 | 800.4 | 16.7% |
| 2017 | 971.4 | 798.2 | 17.8% | 672.1 | 793.7 | 15.3% |

Honest limit: in 2010 and 2011 the crude margin is 20.4%, just over the cap, and the 2017 age-adjusted gap is the smallest of the eight years. 2017 is chosen because it is the last year in the Fund's data pack, not because it is the most balanced; the stable fact across the eight years is the reversal, not a margin. The 2010 crude rates use Census's July 1 estimate, whereas NCHS's published 2010 rate uses the April 1 census count, so students' 2010 crude rates are slightly different from NCHS's own (not shown to students).

**Other years' 65+ shares are not in the case.** The Census age file used here is Vintage 2018; the share is a ratio of the file's own two columns, so it is internally consistent but not identical to Appendix A's residents.

## Argument for A: Florida (The Crude Map)

A services-and-capacity argument. The crude rate is the death rate the people of the state actually experience: 971.4 per 100,000 in Florida against 798.2 in Georgia, 17.8% higher and 12.2% above the U.S., and Florida is 17th highest of 51 on this reading while Georgia is 42nd. NCHS describes the crude rate as the average chance of dying for persons in the entire population; whatever the Fund buys that responds to deaths as they occur (hospice and home-health capacity, ambulance coverage, bereavement support, grief counseling) must be sized to the age mix that is actually there. Age adjustment answers "what would Florida's rate be if its residents were as young as the standard population?", a state that does not exist. The reversal is no accident: Florida's crude rate is above Georgia's in every year 2010-2017, by 17.2% to 20.4%. And the charter says "death rate", not "age-adjusted death rate".

## Argument for B: Georgia (The Adjusted Map)

A like-with-like and prevention argument. Age adjustment removes the one difference that is not about care or risk: Florida's population is the oldest of the 51 (20.1% aged 65+ against Georgia's 13.5%), so its age factor is 1.445 against Georgia's 1.006. Once ages are held fixed, Georgia's rate is 793.7 against Florida's 672.1, a 15.3% gap in the other direction; Georgia is 8.4% above the U.S. and 13th highest, Florida 8.2% below and 44th. NCHS's own purpose for the measure is comparing populations with different age structures (Statistical Notes No. 20). A prevention grant (blood-pressure screening, smoking cessation, injury prevention) changes the risk at a given age; the place where risk at a given age is higher is where those dollars have more to do. Georgia's crude rate is 798.2 and its age-adjusted rate 793.7, so for Georgia the two readings agree; Florida's two readings are 299.3 points apart.

**Weak points on each side (name them if the room does not).** A: a crude rate rises with age structure alone, so it will point at any old state regardless of care or risk; it does not say whether the deaths were avoidable. B: NCHS itself calls the age-adjusted rate a construct or index, not a direct measure of mortality risk; it depends on the choice of standard population (the year 2000 here), and a services grant sized to it would under-size Florida. Neither reading says anything about causes of death; the files do not hold them.

## The margin

**17.8% (crude) and 15.3% (age-adjusted), gap divided by the higher rate**, both inside the cap, and symmetric to within 2.5 points: each state "wins" one basis. **Robustness (one change at a time):** NCHS-published crude rates instead of derived: Florida by 17.9%; 2016 instead of 2017: Florida crude 17.4%, Georgia age-adjusted 16.7%; 2010: 20.4% and 17.1% (the crude margin just over the cap). No variant removes the reversal. **No lens gives either state a margin over 20% in 2012-2017.**

**Blended-index view (facilitator only; `sensitivity_model.py`).** If the board weighted the two readings with weight *w* on crude and 1-*w* on age-adjusted, using each state's rate relative to the U.S. on each basis, the two states tie at *w* = 0.454. An equal split (*w* = 0.5) gives Florida 1.020 vs Georgia 1.003, a 1.7% gap; *w* = 0.25 gives Georgia by 7.7%; *w* = 0.75 gives Florida by 11.3%. This is the cleanest statement of the instability: the verdict depends on how much weight the charter puts on each reading, and the weight is a judgment, not a measurement. It is disclosed in `case.json.sensitivity_disclosure[]`. Students are not given *w*; do not introduce it before the close.

## Five Socratic questions

1. In D1 Florida's crude rate is 12.2% above the U.S. and its age-adjusted rate is 8.2% below the same national figure. How can one state be both above and below the U.S. average, and what does Florida's age factor of 1.445, next to Georgia's 1.006, tell you about who lives there?
2. In D2 the crude gap is 173.2 points and the age-adjusted gap 121.6 points. Dividing each by the higher rate gives 17.8% and 15.3%; dividing by the lower rate gives 21.7% and 18.1%. Does that choice of denominator change which state either rate points at, and does it change which rate you would trust?
3. In D3 Florida is 17th on crude and 44th on age-adjusted, while Georgia is 42nd and 13th. If a grant is meant to change the risk of dying at a given age, which rank would you look at, and what would you have to believe about what the money buys?
4. In D4 the order of the two states is the same on both rates in every year from 2010 to 2017. Does that settle which rate to use, or does it show only that the disagreement is not a one-year accident?
5. Florida had 2.45 times Georgia's deaths but 2.01 times its residents, and the case puts raw counts out of scope. What is the ratio 2.45 divided by 2.01, where have you seen that number already, and why would an award sized by deaths mislead the Fund?

## The trap

The confident wrong answer comes in two mirror images, and a fresh reader judged the first the likelier opener (it is the rate the student just derived by hand, and it has the bigger visible gap): **"Crude is the real death rate and adjusted is made up, so Florida,"** and **"Age-adjusted is the scientific rate and crude is the naive one, so Georgia, end of story."** Both treat one rate as simply correct and skips the question the case is built to force: *which question is the charter asking?* The crude rate answers "how many deaths per resident are happening here, at the ages that live here?"; the age-adjusted rate answers "how risky is it to be a given age here?" A services grant and a prevention grant ask different questions, and a Hero who cannot say which one the Fund is buying has not defended anything. Second-level traps: (1) **mixing the two yardsticks** by comparing Florida's +12.2% (crude) with Georgia's +8.4% (age-adjusted) and giving the award to the bigger percent, a comparison of numbers measured against different standards; (2) **dropping the sign**, reading -8.2% as "8.2% above"; (3) **using the count** (Florida has 59.2% more deaths) as if it were a rate; (4) **dividing the gap by the lower rate** and reporting 21.7% as "over the 20% line" (a convention error, not a finding); (5) **median-of-halves errors** in D3 (leaving the median inside both halves, or building quartiles from an unsorted list) and reading rank 1 as the lowest rate. Further slips seen in cold solves: (6) **inverting the age factor** (adjusted / crude = 0.69) or reading it as "how old the state is"; (7) **rounding early** (whole-number rates) so one-decimal answers drift; (8) **ties**: Rhode Island and Vermont tie at 962.1 on crude, which affects no quartile or fence here but needs a stated rule if a student asks; (9) **treating the Twist as out of scope** because of the all-cause scope line, or ignoring it because CDC says counts should not be compared across states (it says counts; the case uses rates, only to show which way each reading points). Also watch for the opposite error: dismissing age adjustment because Florida "just has old people", which turns a statistical device into a verdict on older residents (see the sensitivity note).

## Intro

Frame the format first: this is a decision about which question to ask, not a hunt for a correct number. Name the opener: "You're Lindiwe Haverstock. The board chair has just walked in and asked which map we are looking at." Say once, plainly, that the numbers are statistics about whole states and that nobody is asked to talk about anyone they know.

## Launch

Show the two map names with no numbers (the award is a one-year grant paid to health programs in the chosen state): The Crude Map and The Adjusted Map. Ask: "If all you knew was those two names, which map would you hand a board that has to give one award?" Take answers without correcting. Record the split.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.** "Is anyone courageous enough to stand with The Adjusted Map?" Show of hands for each option, no discussion. Record the count; Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'which state has the higher death rate' the right question?"** and "What do you mean by 'death rate'?" Let confusion grow: the rate people experience, the rate at a given age, the rate if every state were the same age? "Wow, this is a challenging problem." Do not let anyone reach for the count; if they do, "counts follow the number of residents" and move on.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"** Steer toward: compute both rates for both states, put them against the U.S. and against the other 49 jurisdictions, check whether the picture is a one-year result, then decide what the grant is for. Re-ask: "Is our question still the right question?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"** Surface: what the grant buys (services versus prevention); what the charter means; whether 2017 is typical; whether the standard population matters; whether the two states were fairly shortlisted; whether a rate can hide different causes of death. Ask which one would change their stand.

## Data Deep Dive

Now the numbers. Let students build the rates table (D1) and the gaps and age factors (D2), then the 51-jurisdiction box plots (D3) and the earlier-years check (D4). Hold back the idea of a single "right" rate until the age factor and the ranks are on the board. Facilitator-only arithmetic is in "The real numbers" above.

## Twist

**New information, delivered at 15:00 and read slowly:** "Years later, the CDC counts deaths from a disease that did not exist in 2017: COVID-19. Same two states, same two kinds of rate, per 100,000 residents, added up from January 2020 through the week ending September 12, 2026 (data as of September 17, 2026)."

| Cumulative 2020-01-01 to 2026-09-12 | Florida | Georgia | United States |
|---|---|---|---|
| COVID-19 crude death rate | 399.6 | 360.4 | 374.5 |
| COVID-19 age-adjusted death rate | 270.1 | 342.0 | 311.4 |
| Annualized crude / age-adjusted (CDC's own columns) | 59.7 / 40.4 | 53.9 / 51.1 | 56.0 / 46.6 |

Say first: "This is not new input to the 2017 decision. It asks whether the disagreement between the two readings recurs for a different cause of death, so the Appendix E scope rule is intact." Read the annualized row before the cumulative one, and say that 399.6 is about 6.7 years added up, so it cannot be set beside 971.4 (one year). State once that CDC's age-adjusted COVID-19 rates use the same year-2000 standard population as Appendix B (CDC publishes them on that basis; students are not asked to verify it). If challenged that provisional data cannot be compared across states: CDC's caution is about counts; the case reads only which way each rate points, and the 9.8% and 21.0% gaps differ by under 0.1 point from the annualized columns' 9.7% and 20.9%. Source row: `case.json` S9 (CDC, retrieved 2026-10-28; post-decision, deliberately outside MA2 and not in case.md). Expect most of the room not to move: the Twist is a targeted probe of the bigger-gap argument, not a room-wide turn. Pause. Then put this to the room: **"If you argued that your reading is stronger because its gap is bigger, say it again with these numbers."** In 2017 the crude gap (17.8%) was bigger than the age-adjusted gap (15.3%); here it is the reverse (9.8% against 21.0%). Ask who changes their plan.

**What it does.** The disagreement between the two readings comes back under a different disease: Florida is above the U.S. on the crude rate (+6.7%) and below on the age-adjusted rate (-13.3%); Georgia is below on crude (-3.8%) and above on age-adjusted (+9.8%). But the *sizes* change: the crude gap shrinks to 9.8% (gap / higher, Florida ahead) while the age-adjusted gap grows to **21.0%** (Georgia ahead), over the 20% line (the 2010 and 2011 crude gaps were 20.4%, barely over; nothing else in the case is over). (This is a post-decision observation, not a balance test; the cap applies to the decision, not to the Twist.) Four positions break: (0) **"Florida's case is stronger because the crude gap is bigger"** (a point the cold solvers made on the 2017 numbers): the order of the two gaps reverses, so "bigger gap wins" now favors Georgia; (1) **"The two readings are about equally strong, so call it a coin flip"** (17.8% against 15.3% in 2017) now looks lopsided; (2) **"Split the difference"** (equal weight, *w* = 0.5), which favored Florida by 1.7% on 2017 data, favors Georgia by 6.5% on the Twist numbers (`sensitivity_model.evaluate_twist`); (3) **"2017 was a one-year accident"** loses ground, because the reversal reappears with a different cause of death. What stays unsettled: the crude rate still points at Florida, and the question the Fund's charter asks has not changed. Nobody is obviously right: the age-adjusted camp has stronger numbers but still has to say what a prevention dollar buys, and the crude camp has weaker numbers but still serves the people who are actually there.

**Cautions to read out.** (a) These are cumulative over 6.7 years, so 399.6 cannot be compared with 971.4, which is one year's all-cause rate; compare the two states within the table. CDC's annualized columns put them on a per-year footing. (b) CDC calls these provisional counts, coded to U07.1, and warns that recent weeks are incomplete and that data timeliness varies by state, so counts should not be compared across states; the rates are used here only to show which way each reading points. (c) One disease has a steeper age gradient than all causes: the COVID age factors are 1.479 (Florida), 1.054 (Georgia) and 1.203 (U.S.), higher than the all-cause 1.445, 1.006 and 1.183.

Follow-up: **"What just broke in your original model? Were you wrong, or just missing information?"** The 2017 comparison was right for 2017; what it could not show is that the disagreement between the two readings is a property of the two states' age structures, not of one year or one disease, and that its size is not fixed.

## Immediate recommit

15:00-20:00. "You have 60 seconds. Are you changing your plan?" Who reverses, who stays, and why. Ask the stayers: what number would make you reverse?

## Deep conflict — two threads (20-30 min)

1. **What does the charter's "death rate" ask for?** Services (size to the people who are here) or prevention (size to risk at a given age)? Whose job is it to decide, the foundation's or the data's?
2. **Is an adjusted number still a rate?** NCHS calls it a construct. Florida's age-adjusted rate is 672.1, but no Floridian lives in the standard population. If it is not what anyone experiences, why use it to give away money, and what do we lose by ignoring it?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00-3:00 | Launch: read the two map names with no numbers, cold-call a gut read, stand/sit vote (Anchor 1) |
| 3:00-10:00 | Position defense: *"Convince us your map is the honest one, not just the familiar one."* |
| 10:00-15:00 | Pressure-test: *"Whose map is most fragile if we change the question the charter asks?"* |
| **15:00** | **DROP THE TWIST** (the same two readings reappear under COVID-19, with new gaps), slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? *"What just broke?"* |
| 20:00-30:00 | Threaded deep conflict (services versus prevention; is an adjusted number still a rate) |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Close

**VOTE AGAIN.** "Did we ask the right question?" and "What math was new to you, and how did you attack it?" Ask whether anyone changed their vote because of the age factor, because of the earlier years, or because of the Twist.

## Lessons Learned

- A rate is a ratio, and different denominators answer different questions; before comparing two rates, ask what each one holds fixed.
- A statistical adjustment is a device for one question (what if the ages were the same?), not a verdict on a population.
- Two standard measures of the same year can reverse the order of two states, and the size of the disagreement is itself data.
- A count follows the size of a population; a rate follows the risk. Decide which one the decision is about.

## Standards Touched On

Ratio and proportion (D1, D2), signed percent difference and division with negative numbers (D1), percents (D1, D2, D4), box-and-whisker plot construction with quartiles, median and outliers (D3), comparing values (D3, D4). New coverage: none, since no spine skill is at n=0; the box-and-whisker how-to (n=1) is forced by D3 and divide-with-negatives (n=2) by D1. `advanced-numbers-how-to-multiply-with-negative-numbers` was dropped from the concept's claim list because its only deliverable (signed excess deaths) is not allowed by SPEC §6. The case carries a `reinforcement_note`.

## Cohort bands (MCS-25)

- **Full (12-20):** anchors and the 45-minute plan as written.
- **Compressed (6-11):** Anchors 2-3 combine into one pass; the deep-conflict section runs one thread (services versus prevention); total runtime shortens proportionally.
- **1:1 / pair (1-2):** no vote; a stated initial position instead; the guide plays devil's advocate directly (argue the other map); the twist still lands, and "who reverses" becomes "would you reverse, and why".

## Facilitator note — sensitivity (SPEC §6)

All-cause mortality statistics: the subject is death, and some students will have lost someone, including older relatives. Frame the Hero as a professional comparing statistics for whole states. **No personal stories are requested; do not ask anyone to say whether they know someone who died or who moved.** Do not ask students to value one age group's deaths over another's: say plainly that age adjustment is a statistical device for comparing populations, not a verdict on older residents, and that a high crude rate in an older state is not a failure of that state. Keep the discussion on rates, ranks and what a grant buys. The Fund, its charter and the analyst's maps are fictional. If a student says "people retire there," respond that the Census age counts show Florida's population is older but cannot say why, and move on. The data are public statewide statistics; no individual, county or facility is identified.

## Sensitivity (P5) and disclosed instabilities

Every number is cited or derived, so the only dial is the weight on each reading (`w_crude`), which the case does not state and the dilemma itself asks the student to choose. Flexing it ±50% around an equal split changes the winner: w = 0.25 gives Georgia by 7.7%; w = 0.75 gives Florida by 11.3% (Probe 5 convention, gap / lower index); the tie is at 0.454. That is the case's finding rather than a defect, and is disclosed in `case.json.sensitivity_disclosure[]` (category F: a value judgment no research can supply). No stated assumption in Appendix F is numeric; MA1-MA5 are scope choices. The population-vintage choice moves the crude rates by 0.1%-0.2% for these three and 1.35% at most for any jurisdiction, and changes no verdict.

## Grading note

Students rounding differently get slightly different figures: crude rates from Appendix A are 971.4, 798.2, 865.7 (971.38, 798.23, 865.73 before rounding); signed percent differences are +12.2%, -7.8% (crude) and -8.2%, +8.4% (age-adjusted); age factors 1.445, 1.006, 1.183 (1.4453, 1.0057, 1.1828 from rounded rates). Accept answers within 0.1 point on rates, 0.1% on percents and 0.01 on age factors. A student who builds D3 quartiles with a different convention (for example including the median in both halves) will get Q1 and Q3 within a few points of the guide's; accept if the convention is stated. For D4, accept either denominator convention if it is named, but D2 and D4 ask for "percent of the higher rate."
