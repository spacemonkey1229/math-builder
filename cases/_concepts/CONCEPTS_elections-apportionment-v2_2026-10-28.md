# Concept sheet v2 — Elections & Apportionment (`elections-apportionment`), revised after R1 round 1

**Single concept: The Eighty-Nine.** Tier T3. Data grade HIGH. Data as-of: Census 2020 and 2010 apportionment files, fetched 2026-10-28; no live figures.
Supersedes C1 of `CONCEPTS_elections-apportionment_2026-10-27.md`. C2/C3 are not carried forward.

**Margin convention (stated once, applied everywhere).** Margin = gap between the two options on a metric, divided by the *larger* of the two values on that metric (the option that is worse on a lower-is-better metric). Dividing by the smaller value instead gives a slightly bigger percent; both are shown only in the reconciliation table.

**Decision shape.** This is the one pick in the wave that is *not* a break-even on one parameter. The numbers are not tuned; the tension is **which yardstick of fairness the memo adopts**. Each option wins on one yardstick in 2020, and the winners swap in 2010. That is preserved from v1.

## Fixes applied

| # | R1 finding | Fix in v2 |
|---|---|---|
| a | "HH dominates max/min in every census / never loses" is false | Statement removed everywhere. Webster wins max/min in 2010 (1.50% / 1.48%, below) and in 2020 at House sizes 428-433. No optimality claim for either method: brute force on 5 states, 8 seats (populations 657, 186, 2810, 1146, 567) gives HH = Webster = seats (1,1,4,1,1) with max/min 6.161, but the best possible allocation is 5.036. So neither method minimises max/min. Added as a Discussion prompt, not as a fact the student must find. |
| a | 2010 margin: R1a 0.7% (resident pop) vs v1 1.5% | Reconciled below. Correct base is *apportionment population* (Table C2), which includes federal staff overseas. On that base HH 1.8847 vs Webster 1.8568; margin 1.48% (1.50% on the smaller value). On the resident-population proxy, HH 1.8800 vs Webster 1.8675; margin 0.66%. R1a's 0.7% is the proxy; v1's 1.5% was right for the correct base but unlabeled. Case uses Table C2 only. |
| b | 2020 numbers | Re-verified from Census tables (below). Margin now 3.95%, not 4.1%, under the convention. |
| c | Skills mis-mapped | Re-mapped (section Skills): absolute value is now forced by deliverable D4 (summed absolute seat error), not by the ratio; rounding is forced by the Webster hand-run (D3), not by the ratio; the square root in the priority formula is explicitly **not claimed** (spine has no root id); calculator step is stated as such. |
| d | Contested-method literature | Cited with both sides (section Sources). |
| e | Recommendation not concrete | Dated memo to a named audience; statute stated (section Protagonist and Dilemma). |
| f | Nonpartisan; protagonist name | New name, 0 hits in `cases/` (grep "Ashgrove" = 0, "Wilhelmina" = 0). No Priya/Mara/Okafor/Raman. No party, no state blamed; states appear only as data rows. |
| g | Keep non-break-even shape | Preserved; two-metric tension is the whole case. |

## Protagonist and framing (constructed, disclosed)

**Wilhelmina Ashgrove**, a fictional mathematical statistician on the apportionment team of the U.S. Census Bureau. Constructed framing: the Bureau does not choose the method; the method is fixed by statute (Huntington-Hill, "equal proportions", adopted 1941 and codified at 2 U.S.C. 2a). So the decision is the Bureau's *technical advice*: on **2027-03-01** (fictional date) she must send a one-page recommendation memo to the Director of the Census Bureau, for transmission to the congressional committees with census jurisdiction, on whether the Bureau should tell Congress to **keep** Huntington-Hill for the 2030 apportionment or **recommend a change in law to Webster** before then. The facts of 2020 and 2010 are real; the memo, its date and Wilhelmina are constructed.

**Hook (ending, not a phone-buzz):** she has the two printed one-page drafts side by side, one headed "No change", one headed "Amend the statute", and a single sentence from a spreadsheet cell ("New York would have needed about 89 more people") on a sticky note, stuck between them. She reaches for the stapler. (Facilitator may rewrite; ending is the memo about to be assembled, not a notification.)

## True story it rests on

2020 census: the 435th and final House seat went to Minnesota (its 8th) with priority value **762,997.705**; the first seat left out, the 436th, would have been New York's 27th at **762,994.353** (Census Bureau 2020 Priority Values file). Solving population = priority x sqrt(26 x 27): New York needed about **20,215,840** people vs its 20,215,751, a shortfall of **about 88.8, i.e. 89 people**. These are the Census Bureau's own published numbers. Also real: Montana's 1990 loss of its second seat led to *U.S. Department of Commerce v. Montana* (1992), in which the Supreme Court upheld the method (cite from memory in the case-research pass; see UNVERIFIED).

## Dilemma (binary, as SPEC 1.4)

You are Wilhelmina Ashgrove. Do you:
A.) Recommend the Bureau **keep Huntington-Hill** (equal proportions; no change in law needed) OR
B.) Recommend a **change in law to Webster** (Sainte-Lague, round at the half), effective for the 2030 apportionment?

The two methods give the same allocation for 46 states in 2020 and differ for **Montana, New York, Ohio and Rhode Island**. HH: Montana 2, New York 26, Ohio 15, Rhode Island 2. Webster: Montana 1, New York 27, Ohio 16, Rhode Island 1.

## Primary metric and the tension

The case does not pre-decide the yardstick. Students are given two, both computed on 2020 apportionment population, H = 435:

| Metric (lower is better) | A: Huntington-Hill | B: Webster | Winner (margin, convention) |
|---|---|---|---|
| (1) Max/min ratio of persons per representative | 1.8257 (Delaware 990,837 / Montana 542,704 (542,703.5)) | 1.9009 (Rhode Island 1,098,163 / Wyoming 577,719) | **A by 3.95%** |
| (2) Sum over 50 states of \|seats − exact quota\| | 12.07 | 11.67 | **B by 3.38%** |

The case's headline margin for `case.json` is 3.95% (metric 1) with 3.38% (metric 2) recorded as the counter-metric. Both are inside the 20% balance rule. Neither is hidden or tuned.

**Reversal in 2010 (apportionment population 309,183,463):**

| Metric | HH | Webster | Winner (margin) |
|---|---|---|---|
| (1) Max/min | 1.8847 (Montana / Rhode Island) | 1.8568 (Rhode Island / Wyoming) | **B by 1.48%** |
| (2) Sum of \|seats − quota\| | 11.87 | 11.92 | **A by 0.44%** |

Differing states in 2010: North Carolina (HH 13, Webster 14) and Rhode Island (HH 2, Webster 1). So the metric-1 winner and metric-2 winner swap between censuses; no method "dominates".

Other computed facts (from the same tables):
- House-size sweep, 2020 populations, H = 300 to 600: HH wins metric 1 at 127 sizes, Webster at 6 (H = 428-433, by 3.84%), 168 tie. 2010: HH 81, Webster 46 (H = 419-513), 174 tie. The 2020 flip sits just below the real House size of 435 (HH again wins at 434).
- Allocation check: my own HH run reproduces the Census-published seats in all of 1940-2020 (9 censuses), the integrity check.
- Ties on metric 1 in other censuses (1940, 1950, 1980, 1990, 2000) mean the *extreme* states get the same seats under both methods, even though other allocations may differ in a few states. 1970: HH wins 12.4%. 1960: HH wins 25.2% (outside the 20% cap; backtest footnote only).

### Reconciliation of 2010 (R1a vs v1)

| Base | HH max/min | Webster max/min | Margin |
|---|---|---|---|
| Apportionment population (Table C2, includes overseas federal staff) | 1.8847 | 1.8568 | 1.48% (1.50% if divided by the smaller) |
| Resident population proxy (Census apportionment.csv; 1,039,648 fewer people) | 1.8800 | 1.8675 | 0.66% |

The case uses apportionment population only and says why.

## Why it is close and balanced

HH wins the "worst gap" yardstick in 2020; Webster wins the "total distance from exact quota" yardstick in 2020 (largest single-state error 0.574 seats HH vs 0.499 Webster). In 2010 the winners swap on both yardsticks. A student can defend either recommendation with Census numbers, and must choose a yardstick and defend why it is the right idea of fairness. That is the actual intellectual history of the method fight.

**Cost of changing the law** (balance for A): HH is the current statutory method; switching requires an Act of Congress, with its own timing and uncertainty. A Webster recommendation therefore has to argue the gain (3.38% lower total quota error in 2020; a 2020 outcome where a state would have had one more seat) outweighs the cost of legislating before the 2030 count. A recommendation to keep HH has to argue that a 3.95% edge on the worst-gap yardstick, and a method used since 1941, justify no change.

## Deliverables (SPEC 1.5 item 3) and what each forces

- **D1. Priority table.** For each of Minnesota (8th seat) and New York (27th seat), compute HH priority = population / sqrt(n(n+1)) with calculator or spreadsheet, and confirm 762,997.705 vs 762,994.353. Then find how many more New York residents would have flipped the seat (about 89). Forces: division, subtraction, comparing values. *The square root is a calculator step and is **not** claimed as a skill.*
- **D2. Persons-per-representative table** for the 50 states under both methods, 2020; identify the maximum and minimum and compute the max/min ratio under each. Forces: division, ratio, comparing values.
- **D3. Webster by hand.** Find a divisor so that each state's population / divisor, rounded to the nearest whole number (at least 1), sums to 435; show at least three divisor trials. Forces rounding to a place value genuinely (the method *is* rounding at the half).
- **D4. Quota-error metric.** For each state compute exact quota (population x 435 / national total), the absolute difference |seats − quota| under each method, and the sum. Forces absolute value genuinely (an unsigned error is required, otherwise the errors cancel to zero).
- **D5. Margins.** Express each margin as a percent using the stated convention. Forces percent conversion.
- **D6. The memo.** One page, dated 2027-03-01, addressed to the Director of the Census Bureau, containing the recommendation, the yardstick chosen and why, the statutory note (HH is current law; Webster needs a change in law), and at least one original visual (e.g., bar chart of 2020 persons-per-representative for the four differing states under each method).
- **Extension (not required):** repeat D2-D5 for 2010 and say whether the recommendation changes.

## Spine skills (ids checked against `readmodel/standards_spine.json`; real n)

Claimed, each tied to a deliverable above:
- `measurement-ratio` (n=30), D2.
- `number-sense-how-to-compare-two-or-more-values` (n=55), D1, D2.
- `basic-operations-division` (n=31), D1, D2, D4.
- `basic-operations-how-to-subtract-multi-digit-numbers` (n=24), D1, D4.
- `measurement-how-to-round-a-number-to-a-specified-place-value` (n=40), D3.
- `advanced-operations-how-to-evaluate-an-absolute-value-expression` (n=5), D4.
- `advanced-numbers-how-to-convert-numbers-to-percents` (n=44), D5.

**Not claimed** (no spine id, or not forced): square root, `measurement-rounding` as a thin skill, `statistics-and-probability-population`. Honest scoring note: no signature skill hole is closed; the only mildly thin skill is absolute value (n=5 -> 6). The case's value is domain breadth, a non-break-even decision shape, and HIGH-grade official data.

## Sources and the contested-method record (SPEC 5: contested source)

Official data (fetched 2026-10-28, free, no login):
- Table C2, apportionment population and seats 1910-2020: `https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/apportionment-2020-tableC2.xlsx`
- 2020 Priority Values: `https://www2.census.gov/programs-surveys/decennial/2020/data/apportionment/2020PriorityValues.xlsx`
- Table 1 (2020 seats): `.../apportionment-2020-table01.xlsx`; historical CSV (resident population, used for the 2010 proxy only): `.../apportionment.csv`
- Landing page: `https://www.census.gov/data/tables/2020/dec/2020-apportionment-data.html`

Contested literature (the case says plainly that this is a live disagreement among experts and does not pick a side):
- *For change:* Ruoxi Li, "The Malapportionment of the US House of Representatives: 1940-2020", *PS: Political Science & Politics* (Cambridge University Press for APSA), 2022. Abstract: Huntington-Hill produced biased results, in the direction of small states, in 8 of 9 apportionments since its 1941 adoption; recommends Webster, the only unbiased divisor method. Found via search 2026-10-28; abstract read, full text not read. Related preprint: arXiv 2201.11787.
- *For keeping HH:* Census Bureau mathematician Laurence Ernst argued in the 1990s Montana litigation that for each bias measure on which Webster looks best, a different measure favours HH; the Court upheld HH (*U.S. Department of Commerce v. Montana*, 503 U.S. 442, 1992). Cited from memory plus one search summary; confirm before the case ships.
- Counter-framing used in the case: "bias" itself is defined differently by each side, which is the same argument as the two yardsticks above.

## Facilitator note (SPEC 6)

Nonpartisan and statutory. Do not map methods to parties or to winning/losing states; every state is a data row. Remind students the Bureau applies the method Congress set, and that "who gains a seat" under a method can change from census to census (it reversed between 2010 and 2020 on metric 1). If a student argues from a state they live in, ask them to restate the argument using only the yardstick. No illness, death, or family-hardship content.

## Still open

- Full text of Li (2022) not read: verify "8 of 9" and the exact bias measure before quoting. Volume/pages UNVERIFIED.
- Court citation (503 U.S. 442) and the Ernst argument: from memory/secondary summary; verify.
- Statutory wording: that equal proportions is codified at 2 U.S.C. 2a (via the 1941 Act) and that changing it needs an Act of Congress: UNVERIFIED against the U.S. Code text. Which committees hold census jurisdiction in the 2027 Congress: UNVERIFIED (hence "committees with census jurisdiction").
- Margin-convention ambiguity: dividing by the better option's value would give 4.11% and 3.50% (2020) instead of 3.95% and 3.38%; confirm the reviewers' intended denominator.
- The 5-state counterexample is a student prompt only; if used in Discussion, include the populations and the optimal allocation in the facilitator guide.
- Hook ending and Wilhelmina's backstory need drafting at write time; 2027-03-01 memo date is fictional.
