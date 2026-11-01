# Guide Notes: The Last Seat

MS | Guide Notes | Adventure | 2026-27
**Tier:** T3 (MS-stretch / HS-entry) · **Primary metric:** Yardstick 1, the ratio of the largest to the smallest persons-per-representative across the 50 states, 2020, lower is better · **Margin:** 4.11% (gap divided by the winner's value, the margin convention of Appendix C). Huntington-Hill (Option A) is ahead on Yardstick 1 by 4.11%; Webster (Option B) is ahead on Yardstick 2 (total distance from exact share) by 3.50%. **Neither option wins on both yardsticks; that is the design.** Read the sensitivity note before Lessons Learned.

---

## Intro

Heroes, you work at the Census Bureau and you do not get to pick the method. Congress did. Your job is to tell the Director what the numbers say and what it would cost to change them. Before we start: nobody in this case is a villain, and no state is. Every state in this room's data is a row in a table. We are comparing two ways of rounding, not two groups of people.

## Launch

Put one fact on the board: *In 2020 the last of the 435 House seats went to one state and the very next seat, the one that would have been number 436, belonged to another. The Census Bureau published the two scores to seven digits.* Ask: *"Is it fair that a seat can come down to a rounding rule?"*

Let them argue for two minutes, then: *"Wilhelmina can't change the count. She can only tell the Director whether the rounding rule should change."*

> **Hero name: Keep Equal Proportions, or Amend To Webster? Commit out loud.**

Teach-from-scratch note: many Heroes will not know what apportionment is. Draw 50 boxes with one seat each, then show the 385 remaining seats being handed out in a line (Appendices A and E). Do not skip this.

---

## Anchor 1 — Take a stand and vote

Option A (Keep Equal Proportions) or Option B (Amend To Webster). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start computing yet.

- What is the question in one sentence? "Which method is fairer?" "Which method leaves the smallest gap between the most- and least-represented state?" "Which method puts every state closest to its exact share?" "Is a change worth the trouble of a new law?" Those sound alike and are not the same question.
- Someone will say "the one that's the law is the one that's right." Push: *"The Bureau runs it because Congress wrote it down. Does that tell us it is the better rule, or only the current one?"*
- Someone will say "just pick whichever gives the smaller number." Push: *"Smaller number of what?"* Do not rescue them.
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh. 'Which method is fair?' might have more than one correct answer."*

**The trap to let them walk into (two forms).** (1) Most Heroes will compute Yardstick 1, see Huntington-Hill ahead (1.8257 against 1.9009), and stop: *HH wins, keep it.* They miss that Yardstick 2 points the other way (12.07 against 11.67, Webster ahead) and that the argument is about which yardstick is the right idea of fairness. A recommendation that never says why it adopts one yardstick over the other has not answered the question. (2) A subtler trap: assuming the method that wins in 2020 wins every census. It does not; see the Twist. Arithmetic slips to watch: using n(n+1) instead of n(n-1) in the priority formula, rounding early (so the 89 becomes 88), and computing the margin from rounded values (4.12% and 3.43% instead of 4.11% and 3.50%; Appendix C says to use unrounded values). A third wrong path: treating the margin as the argument. 4.11% and 3.50% are both small; the discussion is about what each measures.

## Anchor 3 — What is the process?

- If we have to produce Webster's seats ourselves, what do we do first? (A divisor; the national average is a sensible first trial.)
- If we find two ratios and two sums, how will we decide which yardstick the memo should adopt, before we see the numbers?
- How do we express a gap between two methods as a percent, and what do we divide by? (The margin convention: the better, smaller value.)
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What does the case assume that the real world might not? (MA2: House size and the 50 states stay as they are.)
- Is 435 a fact or a choice? Who can change it? **Have them try a different House size and see how much the comparison moves.** (Sensitivity: see the note below. Do not read the numbers aloud.)
- Appendix D says experts disagree and that part of the disagreement is what "bias" means. What would you need to know to trust one side?
- What do we expect the next census to do to these two methods? (This is the case's built-in opening for the twist; don't tip it.)

---

## Data Deep Dive

Now the numbers. Work them on the board with them.

**Step 1: the last seat (D1).** Minnesota's 8th seat: 5,709,752 divided by the square root of 8 x 7 gives a priority value of 762,997.705. New York's 27th seat: 20,215,751 divided by the square root of 27 x 26 gives 762,994.353. Minnesota is higher by 3.352. For New York to reach Minnesota's value its population would have to be 762,997.705 x the square root of 27 x 26, which is 20,215,839.82; the shortfall is 88.82, so the smallest whole number of extra residents is **89**. (The Census Bureau's own file lists both values, S2.)

**Step 2: Webster by hand (D2).** National average 761,169 gives 435 seats total. Other trials: 760,000 gives 435; 762,000 gives 433; 755,000 gives 437. Every divisor from about 758,008 to 761,300 gives exactly 435 (758,007 gives 436). Webster agrees with the current seats in 46 states and differs in four:

| State | Population | Current (HH) seats | Webster seats | Exact quota |
|---|---|---|---|---|
| Montana | 1,085,407 | 2 | 1 | 1.4260 |
| New York | 20,215,751 | 26 | 27 | 26.5588 |
| Ohio | 11,808,848 | 15 | 16 | 15.5141 |
| Rhode Island | 1,098,163 | 2 | 1 | 1.4427 |

**Step 3: the worst gap (D3).** Current seats: largest persons per representative is Delaware at 990,837; smallest is Montana at 542,703.5; ratio **1.8257**. Webster seats: largest is Rhode Island at 1,098,163; smallest is Wyoming at 577,719; ratio **1.9009**. Huntington-Hill is ahead on this yardstick.

**Step 4: distance from exact share (D4).** Sum of |seats - quota| over 50 states: current seats **12.07** (12.0742); Webster **11.67** (11.6658). Largest single error: 0.574 (Montana, current seats) against 0.499 (Minnesota, Webster). Signed differences cannot be added because the seats and quotas both sum to 435, so the errors cancel to zero.

**Step 5: the margins (D5).** Yardstick 1: (1.9009 - 1.8257) / 1.8257 = **4.11%**, Huntington-Hill ahead. Yardstick 2: (12.0742 - 11.6658) / 11.6658 = **3.50%**, Webster ahead. Both are inside the SPEC 20% cap, and neither option is ahead on both yardsticks. (Dividing by the larger value instead gives 3.95% and 3.38%; the convention is stated once in Appendix C so that every Hero's number matches.)

---

## Twist

Hand out the 2010 column of the same Census table (S1: 2010 apportionment population and seats by state, total 309,183,463) and ask them to repeat D2 to D5. Deliver it slowly: *"The same two yardsticks, the same two methods, one census earlier."*

What they will find: in 2010 the two methods differ in two states (North Carolina 13 under current, 14 under Webster; Rhode Island 2 under current, 1 under Webster). On Yardstick 1 the current method gives 1.8847 (Montana 994,416 against Rhode Island 527,623.5) and Webster gives 1.8568 (Rhode Island 1,055,247 against Wyoming 568,300): **Webster is ahead by 1.50%.** On Yardstick 2 the current method gives 11.87 against Webster's 11.92: **Huntington-Hill is ahead by 0.44%.** The leader on each yardstick reversed.

Then: *"Sixty seconds. Are you changing your recommendation, or not?"* The twist invalidates both "HH is simply better at the worst gap" and "Webster is always closer to exact shares." It does not make either recommendation obviously correct, because the question was never which method wins in one census.

Follow-up, the whole point: **"What just broke in your original model? Were you wrong, or were you just missing information?"**

---

## Deep conflict — threads (20-30 min)

**Thread 1 — Which yardstick is the right idea of fairness?** *"One measures the two extremes. The other measures every state's rounding. When they disagree, which do you trust, and why?"* Push toward: the worst gap is about the two states furthest apart, so one state can set it; the total distance counts all 50 states but treats every state's error as equal. Do not give the answer.

**Thread 2 — Is "it's already the law" an argument?** *"Option B needs Congress to act. What would the gain have to be to justify that?"* Compare the 4.11% and 3.50% margins, the twist reversal, and the cost of asking for a change.

**5-state discussion prompt (facilitator only, optional).** Five states with populations 657, 186, 2,810, 1,146 and 567 share 8 seats. Both methods give (1, 1, 4, 1, 1) seats, whose worst-gap ratio is 6.1613. The best possible allocation of 8 seats among them is (1, 1, 3, 2, 1) with a ratio of 5.0358. Ask: *"Does that mean neither method minimises the worst gap? Then what is the worst-gap yardstick really telling us?"* This is a prompt, not a fact the Heroes must find. Do not claim either method is optimal on either yardstick.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00-3:00** | Cold-call launch. *"Thirty seconds: keep the method, or amend the law?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00-10:00** | Position defense (pre-twist). *"Convince us it's better, not just different."* · *"Which yardstick, and why that one?"* |
| **10:00-15:00** | Pressure-test the models. *"Whose recommendation is most fragile?"* · *"What single choice does your argument depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation, or not?"* |
| **15:00-20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00-30:00** | The two threads: which yardstick is the right idea of fairness · is "it's already the law" an argument. |
| **30:00-45:00** | Close, re-vote, reflection, lessons learned. |

---

## Socratic questions (each answerable only with the case's numbers)

1. Your Webster run reproduces the current seats in 46 states. Which four states differ, and what does each one's persons-per-representative do when its seat moves?
2. The two methods are separated by 4.11% on the worst gap and 3.50% on distance from exact share. At what size of margin would you stop calling the choice close?
3. New York was short by 89 residents in 2020. Is a rule that decides a seat by 89 people in 20 million a flaw in the rule, or in the count?
4. In 2010 the leader on each yardstick reversed. What does that say about recommending a change in law on the basis of one census?
5. A recommendation to amend the law has to say what it costs. What is the cost of Option B, and what would you tell the Director that cost is worth?

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: two reasonable yardsticks can rank the same two methods in opposite orders, and the order can reverse from one census to the next. In 2020 the current method is ahead on the worst gap (4.11%) and Webster ahead on distance from exact share (3.50%); in 2010 each reversed (Webster by 1.50% on the worst gap, the current method by 0.44% on distance). A recommendation must therefore say which idea of fairness it adopts and then price the change in law. All of that is true at once. The margin is stable to the 20% cap but not to the House size (see the note); the case discloses this in `case.json.sensitivity_disclosure[]`.

## Standards Touched On

**Ratio · Division · How to compare two or more values · How to subtract multi-digit numbers · How to round a number to a specified place value · How to evaluate an absolute value expression · How to convert numbers to percents.**

The square root in the priority formula is a calculator step and is not claimed as a skill. See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]` is honestly empty.

---

## Facilitator note — SPEC §6 (nonpartisan and statutory)

This case concerns how a legal formula distributes political representation. Keep it nonpartisan: do not map either method to a party, or either method to winning or losing states. Every state is a data row, and which states gain or lose a seat under a method changes from census to census (it reversed between 2010 and 2020). If a Hero argues from the state they live in, ask them to restate the argument using only the yardstick.

**Huntington-Hill is statutory.** 2 U.S.C. 2a directs the method of equal proportions (S5, S6). The Census Bureau applies it; it does not choose it. So Option B (Webster) is not something the Bureau can adopt: it requires a **change in law** by Congress. Make sure no Hero writes "the Bureau should switch to Webster" as if it were the Bureau's own decision. The memo's recommendation is advice to Congress, passed through the Director.

The scene is constructed (Wilhelmina, her memo, 1 March 2027). The 2020 and 2010 figures are the Census Bureau's own. No illness, death or family-hardship content, but keep the room civil about contested law.

## Sensitivity note (facilitator only, do not read aloud)

The Yardstick 1 comparison depends on the House size. Held at 435 the current method is ahead by 4.11%. Across House sizes from 300 to 600 in 2020 data, the current method is ahead of Webster on Yardstick 1 at 127 sizes, Webster is ahead at 6 sizes (428 to 433, by 3.99%) and they tie at 168 sizes; in 2010 data the counts are 81, 46 and 174. So the 2020 reversal sits just below the real size of 435, and at 434 the current method is ahead again. Halving the House size to about 218 ties the two methods (the same two extreme states in both); raising it by 50% to 653 keeps the current method ahead by 7.99%. The case flags this instability rather than hiding it. Cited populations are not flexed; their checking is Tier 2 probe 6.

**Source caution.** Li (2022) is cited from its Crossref record and abstract summary; the full text was not read, so the guide does not repeat her "8 of 9 apportionments" count. The Young quotation and the Ernst declaration come second-hand from the CRS report (S10), whose author judged the small-state-bias evidence the more persuasive. Present both as the contested record.
