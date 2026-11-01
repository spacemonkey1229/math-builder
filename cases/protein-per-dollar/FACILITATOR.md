# Guide Notes: Protein Per Dollar

MS | Guide Notes | Adventure | 2026
**Tier:** T2 (MS-core) · **Primary metric:** grams of protein per dollar at the August 2024 BLS national average prices (higher is better) · **Margin:** 8.9% (gap divided by the winner's value; Chicken wins) · **SPEC Section 6:** applies (food insecurity and family hardship; boxed note below).

> **SPEC §6 facilitator note (read first).** This case touches food insecurity and family hardship. Some students and their families may use pantries. Frame the Hero as a professional making a budget decision. Do not ask students to imagine specific families going without. Treat the dry-beans exclusion as a funding rule (which money may be spent on what), never as a judgment on what families "should" eat. If a student shares a personal experience, thank them and return to the decision; do not ask anyone to speak from their own household.

**Status: figures are facilitator-only and recomputed in python from the FRED CSVs fetched 2026-10-28.** The three nutrition inputs (MA3 to MA5) are UNVERIFIED because USDA FoodData Central was unreachable from the authoring sandbox; re-confirm them before the guide quotes a margin to students.

---

## Argument for A — Eggs

History says the egg is usually the better protein buy. Across the 224 months in Appendix B, eggs deliver more protein per dollar than chicken in 209 of them (93%); the median is 42.1 grams per dollar for eggs and 30.7 for chicken. Chicken has led only in three stretches: June to December 2015 (7 months), November 2022 to April 2023 (6 months), and the latest two months, July and August 2024. Both earlier stretches reversed within a year. Two months before the order, in June 2024, eggs were ahead by 9.1% (27.76 against 25.22 grams per dollar). And because the order is price-floating (MA2), the call is cheap to lose: if the egg price falls 8.9% from $3.204 to $2.918 a dozen, eggs match chicken, and every dollar after that favors eggs. Eggs are also easy for families to cook and for children to accept.

## Argument for B — Chicken

The decision is made at the prices the board will plan with. At August 2024 prices chicken delivers 25.82 grams per dollar against 23.52 for eggs, a lead of 8.9% (gap divided by the winner), which is 82,955 grams over the quarter (929,696 against 846,742). Chicken's price has been stable ($3.946 to $4.229 a pound from June 2023 to August 2024), while eggs have swung, so chicken carries much less price risk. Betting on eggs is a bet that a run of two months will end within a quarter; the earlier runs lasted 7 and 6 months. The egg price has to fall 8.9% to erase the gap, but chicken only needs to rise 9.8% ($3.952 to $4.339) to lose its lead, so the margin is thin on both sides and chicken is the option that is ahead now.

## The margin

**Convention (stated once):** margin = (winner's value − loser's value) ÷ winner's value on the primary metric. (25.82 − 23.52) ÷ 25.82 = **8.9%**, inside the SPEC §2 cap of about 20%. The same gap measured against the loser's value is 9.8%; that is chicken's break-even price rise, so keep the two straight: eggs must fall 8.9%, chicken must rise 9.8%, both as percent changes of the August 2024 price. If a student uses a different protein value for chicken (23.1 rather than 22.5 grams per 100 g) the margin is 11.3%; the call does not change.

| Quantity (August 2024) | Eggs | Chicken | Dry beans (D6) |
|---|---|---|---|
| Price | $3.204 per dozen | $3.952 per pound | $1.711 per pound |
| Protein per unit | 75.36 g per dozen | 102.06 g per pound | 97.98 g per pound |
| Grams of protein per dollar | 23.52 | 25.82 | 57.26 |
| Units per month on $12,000 | 3,745 dozen | 3,036 pounds | not orderable |
| Grams per month | 282,247 | 309,899 | n/a |
| Grams per quarter | 846,742 | 929,696 | n/a |
| Break-even price for the other option to match | $4.339 per pound for chicken (up 9.8%) | $2.918 per dozen for eggs (down 8.9%) | n/a |

Quarter difference: 82,955 grams (about 83 kilograms). A 50/50 split of the budget gives 24.67 grams per dollar, which lies between 23.52 and 25.82; any blend is a weighted average of the two endpoints and so can never beat the better pure option on this metric. Dry beans deliver 57.26 grams per dollar, which is 2.22 times chicken's rate and 31.4 grams per dollar more; the rule costs about that.

## Five Socratic questions

1. Your D1 table gives grams of protein per dollar for each option. By what percent does the winner beat the other, divided by which value, and why does that choice of denominator change the number you quote to the board (8.9% versus 9.8%)?
2. D3 gives a break-even price for each option. Which is the more believable move over one quarter, an egg price 8.9% lower or a chicken price 9.8% higher, and what does Appendix B say about how far each price has moved in a single quarter?
3. Your D5 chart shows eggs above chicken for most of 2006 to 2024, with only a few stretches where chicken leads. How long did the two earlier stretches last, and what does a run length of seven months tell you about betting on a reversal inside one quarter?
4. D4's blends sit between the two pure options. If a split can never beat the better pure option on grams per dollar, why might the board chair still prefer one, and what does that tell you about what the metric leaves out?
5. D6 prices the funding rule. Dry beans deliver more than twice chicken's grams per dollar; what does the pantry give up under the rule, who decided it, and what would you want to know before asking the food bank to change it?

## The trap

A hurried student will take the confident wrong answer in one of several forms:
1. **Comparing dollars per unit instead of protein per dollar.** A dozen eggs ($3.204) is cheaper than a pound of chicken ($3.952), so eggs "win." The units differ: 75.36 grams of protein in the dozen against 102.06 in the pound. The student who compares the two prices directly never notices that the units hold different amounts of protein.
2. **"Eggs win 93% of the time, so pick eggs."** The history is a reason to expect a reversal, not a fact about the quarter. The decision is made at today's prices, and the order floats with price: a student has to say how much weight a run length deserves against a lead that exists today.
3. **Misreading the nutrition values.** A hurried student will treat 12.56 as grams of protein per egg (giving 150.7 grams per dozen, 47 grams per dollar) or will skip the 12.56% and use 600 grams per dozen. Eggs then "win" nearly two to one and the break-even is a huge price drop. Ask for the units on every column of the D1 table. (Found by the P3 cold reader.)
4. **Reading the break-evens as symmetric.** A student will compute one gap of about 9% and write "eggs down 9%, chicken up 9%." The two percents differ (8.9% and 9.8%) because each is measured from a different price; dividing the gap by the loser instead of the winner gives 9.8% for the margin.
5. **Reading the margin as a certainty.** A margin of 8.9% on three assumed nutrition values and two month-old prices is a thin lead; the student who says "chicken wins by 8.9%, so it is settled" has not checked what moves it. The honest position names the break-even prices and the assumption they rest on.

## Intro

Frame the format in two sentences: a purchasing decision, a binary choice, and a pitch defended against peers. Name the opener: "Eggs or chicken, and you have until the 9:00 a.m. cutoff." Read the SPEC §6 note to yourself again before you begin; do not read it aloud.

## Launch

Show the cold-room image only if the room already knows what a food pantry does; otherwise have one volunteer say in a sentence where pantries get their food. Give the order rule in plain words: one protein per quarter, the monthly spend fixed, units shipped each month equal the spend divided by that month's price.

## Anchor 1 — Take a stand and vote

"Eggs or chicken? Stand on the side of the room for the one you would order. No reasons yet." Record the split. Ask one student on each side for a single reason, and do not comment.

## Anchor 2 — What is the problem we are solving?

"What does the board want?" Let the room argue: more food, more protein, more variety, lower price, fewer complaints. Ask: "Is grams per dollar the right question?" and "What do you mean by 'better' protein?" Let the confusion grow; then say: "Wow, this is a challenging problem." Do not give the metric yet beyond what the case states.

## Anchor 3 — What is the process?

"If we have the prices and the nutrition numbers, how will we decide?" Draw the steps: put both options in the same unit, scale to the budget, compare. Re-ask: "Is our question still the right question?" Ask what the order rule means: why does it matter that the supplier prices each month?

## Anchor 4 — What don't we know?

"Do we need to make assumptions? Which are critical?" Collect: the protein per egg, the protein per pound of chicken, the stand-in for the supplier's price, next quarter's prices. Ask which one would change the answer if it were off by 5%; then by 50%.

## Data Deep Dive

Now, and only now, the numbers. Walk D1 to D3 on the board with the table above hidden; let students bring their own values. Watch for the forms of the trap. Show the break-evens last and ask where a typical price month sits relative to them. Do **not** mention anything that happened after August 2024.

## Twist

**Twist (post-decision; this is the only place later prices appear).** After the vote, tell the room: "It is now January. The quarter you ordered is over. Here is what the supplier charged." Show the monthly BLS average prices for the quarter ordered (Oct, Nov, Dec 2024): eggs $3.370, $3.649, $4.146 a dozen; chicken $4.037, $4.011, $4.104 a pound. Grams of protein per dollar: eggs 22.36, 20.65, 18.18; chicken 25.28, 25.45, 24.87. A pantry that ordered Eggs got 734,290 grams in the quarter, 13.3% fewer than planned; a pantry that ordered Chicken got 907,135 grams, 2.4% fewer than planned. The simple average of the three monthly egg prices ($3.722 a dozen) was 16.2% above August and 27.5% above the D3 break-even of $2.918 (the egg price that matches August chicken). Because the pantry spends equal dollars each month, the price actually paid per dozen is the harmonic mean, $3.695 (15.3% above August); expect a student who divides $36,000 by the dozens shipped to get that figure. If the room asks about the next quarter: January to March 2025 egg prices were $4.953, $5.897 and $6.227 (the peak in the window).

Say it slowly, with pauses. Then: "You have sixty seconds. Are you changing your plan, or not?" Follow with the transferable question: **"What just broke in your original model? Were you wrong, or just missing information?"** The twist invalidates the reversion position (eggs usually win, so wait it out) but does not make Chicken obviously right: the Eggs argument predicted correctly that high egg prices were unusual, it only got the timing wrong; and a student who chose Chicken on the 8.9% alone was right without having tested the reason. Push on both: "Was the run-length history the wrong evidence, or only the wrong timescale?"

**Does the twist survive the case's assumptions?** Under MA2 (the order floats) the egg quarter is repriced month by month, as above. If a student reads the order as locking the August price instead, the twist has no effect, which is why MA2 states the floating rule in Background and Appendix A. `sensitivity_model.py` `evaluate_twist()` reproduces the figures.

## Close

Re-vote: "Did we ask the right question?" Count who moved and why. Ask: "What math was new to you, and how did you attack it?" and "What did the metric leave out that the board should have asked about?"

## Lessons Learned

- A rate is only comparable once both options are in the same unit.
- A margin is a statement about today; a break-even is a statement about how much has to change.
- A decision made well can turn out badly (and the reverse); separate the choice from the outcome.
- A rule that limits choices has a price; name it before deciding whether it is worth keeping.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on Eggs or Chicken; no explanation |
| 3:00–10:00 | Position defense: "Convince us why it is better, not just cheaper." Anchors 2 and 3 run here before any numbers |
| 10:00–15:00 | Pressure-test the models: "Whose plan is most fragile?" Collect assumptions (Anchor 4) and the break-even prices |
| **15:00** | **DROP THE TWIST**: show the quarter's actual prices slowly, with pauses |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your original model?" |
| 20:00–30:00 | Threaded deep conflict (two named threads): run-length history versus today's lead; what the metric leaves out versus what the funding rule costs (D6) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Sensitivity note (SPEC §2 stability)

The verdict is **not stable under large swings in the assumptions**, and the guide should say so. Under a plus-or-minus 50% swing: the quarter's egg or chicken price relative to the August price (MA2) flips the winner (forecasts); the egg weight, egg protein and chicken protein values (MA3 to MA5) also flip it, but those are physically implausible swings. Under a plus-or-minus 5% swing on each nutrition value Chicken stays ahead (margins from 4.1% to 13.5%). The budget (MA1) does not move the margin. Disclosed in `case.json.sensitivity_disclosure[]`; reproduce with `python3 sensitivity_model.py`. The three nutrition values are UNVERIFIED (USDA FoodData Central unreachable 2026-10-28).

## Standards touched on

Ratio and equivalent ratios (D1, D2, D4, D5, D6), percent of a number (D3, D6). New coverage: none (the spine has no skill at n = 0); the case carries a `reinforcement_note`.

## Cohort bands

See `case.json.cohort_bands[]`: Full (12-20), Compressed (6-11), 1:1 / pair (1-2).
