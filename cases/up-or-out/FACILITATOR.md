# Guide Notes: Up or Out

MS/HS | Guide Notes | Adventure | 2026-27
**Case:** Up or Out · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** MS Adventure
**Primary metric:** a plan's expected declared cost, averaged over nine equally likely job sizes (250 to 450 sq ft, 25 apart); at each size, cost = median $/sq ft of comparable filings within +/-50 sq ft x the size. Lower wins.
**Margin convention (used everywhere below):** gap divided by the winner's (lower) value, as a percent. **Margin: 3.2%** (Tall Plan $135,817 vs Wide Plan $140,206; gap $4,389).
**Status:** researched 2026-10-28. Every figure below is from the 2026-10-28 pull of NYC Open Data dataset ic3t-wcy2 (see `data_pull.py`, `RESEARCH_LOG.md`). Never state these to students before Anchor 4 / the Data Deep Dive.

---

## Why this case was restructured (read first)

The earlier concept fixed the job at 400 sq ft, where the Tall Plan won by 17.0% but only for job sizes 395-410 (390 = 22.3%, 415 = 22.5%); moving the job from 350 to 400 was tuning, which SPEC §2 forbids. This case does not tune a size. The size is the unknown: the architect's range is 250-450 sq ft and the decision is made before the size is known. The finding is the crossing: the Wide Plan is cheaper per sq ft below about 304 sq ft, the Tall Plan above it, and the two average within 3.2% over the range. **Honest limit, say it aloud if asked:** the near-balance holds when the range straddles the crossing with room on both sides. Of 81 (low, high) ranges tried (low 150-350, at least 100 wide, high up to 550), 44 have margin <= 20%. Ranges lying wholly above about 300 (e.g. 325-450, 25.3%) give the Tall Plan by more than 20%; ranges with a low end of 225 or below and a high end of 375 or below give the Wide Plan by more than 20%. The range 250-450 is a stated scenario input (MA2, centered on 350 from the concept stage, before this analysis), not a data-selected one, and the full grid is below so no one is misled.

## The real numbers (facilitator reference, never in case.md)

| Size | Tall $/sq ft (n) | Wide $/sq ft (n) | Tall cost | Wide cost | Cheaper | Margin |
|---|---|---|---|---|---|---|
| 250 | 718.8 (66) | 421.5 (194) | $179,701 | $105,366 | Wide | 70.5% |
| 275 | 667.3 (62) | 437.1 (183) | $183,500 | $120,202 | Wide | 52.7% |
| 300 | 454.5 (70) | 434.4 (178) | $136,340 | $130,322 | Wide | 4.6% |
| 325 | 312.7 (68) | 426.1 (177) | $101,625 | $138,475 | Tall | 36.3% |
| 350 | 304.9 (63) | 373.8 (180) | $106,707 | $130,847 | Tall | 22.6% |
| 375 | 300.8 (65) | 364.2 (167) | $112,799 | $136,577 | Tall | 21.1% |
| 400 | 311.2 (57) | 364.2 (171) | $124,485 | $145,682 | Tall | 17.0% |
| 425 | 314.8 (62) | 390.7 (169) | $133,796 | $166,055 | Tall | 24.1% |
| 450 | 318.7 (67) | 418.5 (167) | $143,399 | $188,326 | Tall | 31.3% |

Average over the nine sizes: Tall **$135,817**, Wide **$140,206**; gap **$4,389**, **3.2%**. Tall is cheaper at 6 of 9 sizes, Wide at 3 of 9.
Over the $150,000 savings: Tall at 250 ($179,701) and 275 ($183,500); Wide at 425 ($166,055) and 450 ($188,326). Two sizes each.
Straight-line crossing: between 300 (Tall - Wide = +$20.1/sq ft) and 325 (-$113.4/sq ft): about **304 sq ft**. State it as "roughly 300, plausibly 275-325": the step comes from windows of 57-70 Tall filings.
Slopes: Tall 250-300 = -$5.29 per sq ft per sq ft; 350-450 = +$0.14. Wide 250-300 = +$0.26; 350-450 = +$0.45. Tall is clearly non-linear (a cliff then a flat); Wide is gently rising and nearer linear, though not exactly.
Largest regret: Tall **$74,335** (at 250); Wide **$44,927** (at 450). Minimax regret favors Wide even though the expected cost favors Tall.
Pooled comparison (Appendix D): all sizes pooled, Tall $203.7 vs Wide $265.8 per sq ft, a **30.5%** gap for Tall, over the 20% cap and wrong in direction below ~304 sq ft. Size mix: Tall median job 931 sq ft vs Wide 669; under 300 sq ft 7.8% vs 20.2%; 600+ sq ft 78.7% vs 55.4%.
Box-plot summaries (median-of-halves, values rounded to $1): 250 window Tall min 58, Q1 277, med 719, Q3 1,250, max 1,935 (IQR 973, fence 2,709.5, no outliers); Wide min 24, Q1 200, med 421.5, Q3 857, max 1,911 (IQR 657, fence 1,842.5, 1 outlier: 1,911). 450 window Tall min 27, Q1 170, med 319, Q3 548, max 1,534 (IQR 378, fence 1,115, 5 outliers 1,159-1,534); Wide min 59, Q1 226, med 419, Q3 600, max 1,773 (IQR 374, fence 1,161, 13 outliers 1,162-1,773). The boxes overlap in both windows.
Uncertainty: stratified bootstrap of the filings in 200-500 sq ft (3,000 resamples, seed 20261028): Tall wins the average in 52% of resamples; the 95% interval for (Wide - Tall) is about -$31,000 to +$27,000. **The primary-metric winner is a coin flip.** At 300 sq ft alone, the Wide Plan's median is lower in 54% of resamples.

## Argument for A — The Tall Plan

Expected cost is lower ($135,817 vs $140,206, 3.2%) and the Tall Plan is cheaper at six of the nine sizes, by 17% to 36% at every size from 325 up, saving $21,000 to $45,000 against the Wide Plan there. The size that makes it expensive (under about 300 sq ft) is where the records carry a likely scope artifact: Tall filings of 200-299 sq ft have a median total declared cost of $159,190, higher than the $121,255 for 300-449 sq ft, and only 28% of them report added stories against 58-60% above 300. A smaller addition costing more overall cannot be pure building cost, so the family's addition-only job probably does not face the cliff. If so, the Tall Plan also frees the ground floor for Nonna and keeps the yard.

## Argument for B — The Wide Plan

Never very wrong: its cost per sq ft stays between about $364 and $437 across the whole range, and its largest regret is $44,927 against $74,335 for the Tall Plan; the Wide Plan's worst surprise is paying $44,927 more than the Tall Plan at 450 sq ft, while the Tall Plan's is paying $74,335 more than the Wide Plan if the survey comes back at 250. It has more evidence behind it (167-194 filings per window against 57-70), so its medians are steadier, and it is cheaper at 250, 275 and 300 by up to 70.5%. The scope-artifact argument cuts both ways: it is an inference from total costs and story counts, not a documented fact, and the Tall cliff persists even when only filings that report added stories are counted (median $/sq ft at 250 / 275 / 300 / 325 = $676 / $686 / $530 / $358, n = 19 / 22 / 34 / 35). A family that cannot absorb a $75,000 surprise should buy the narrower distribution.

## The margin

3.2% on the primary metric, well inside the SPEC §2 cap of about 20%, and the winner is statistically a toss-up. **Robustness, expected-cost metric, one change at a time (margin per the convention above):** base Tall 3.2%; keep $/sq ft outside $20-$2,000 Wide 6.2%; keep duplicate documents Wide 3.0%; filed 2008 onward Tall 7.1%; Queens only Tall 10.8%; filed 2011-2015 Tall 6.3%; filed 2016-2020 Wide 1.0%; crude year-index adjustment Tall 7.6%; Tall filings restricted to those reporting added stories Wide 0.2%. Window half-width 25 / 75 / 100: Tall 0.02% / 0.3% / 1.6%. Every variant is under 11%; five of the nine rows (base included) choose the Tall Plan and four the Wide Plan, which is itself the finding: the data cannot pick a winner on cost, so the stance has to come from risk and from the scope argument. `case.json.margin_pct` = 3.2.

**Range grid (expected cost; winner and margin):**

| low \ high | 375 | 400 | 425 | 450 | 475 | 500 | 525 | 550 |
|---|---|---|---|---|---|---|---|---|
| 200 | W 25.1 | W 19.8 | W 14.6 | W 9.6 | W 6.2 | W 3.4 | W 1.3 | W 0.1 |
| 225 | W 20.1 | W 15.1 | W 10.1 | W 5.4 | W 2.4 | T 0.1 | T 2.0 | T 3.0 |
| 250 | W 7.7 | W 4.2 | W 0.5 | T 3.2 | T 5.5 | T 7.5 | T 8.9 | T 9.4 |
| 275 | T 2.4 | T 4.8 | T 7.7 | T 10.9 | T 12.5 | T 13.9 | T 14.8 | T 14.8 |
| 300 | T 17.2 | T 17.2 | T 18.5 | T 20.6 | T 21.0 | T 21.5 | T 21.6 | T 20.8 |
| 325 | T 26.4 | T 23.8 | T 23.9 | T 25.3 | T 24.9 | T 24.9 | T 24.6 | T 23.4 |
| 350 | T 21.8 | T 20.1 | T 21.2 | T 23.6 | T 23.4 | T 23.6 | T 23.5 | T 22.3 |

(T = Tall Plan, W = Wide Plan; steps of 25 sq ft, +/-50 sq ft windows.)

## Five Socratic questions

1. In D4 the two average costs are $4,389 apart. What is that as a percent of the lower average, and how many of the nine sizes does the plan with the lower average actually win?
2. In D5 the Tall Plan's largest regret is $74,335 and the Wide Plan's is $44,927. If the survey gave you equal odds of every size, would you still accept the Tall Plan's lower average, and what odds on a small survey result would make you switch?
3. In D2 the Tall curve falls from $719 to $455 per sq ft between 250 and 300, then to $313 by 325. What is the slope of that stretch, and what would you need to know about those small Tall filings to decide whether the cliff applies to the Marchettis' addition-only job?
4. In D3 the pooled medians say the Tall Plan wins by 30.5%. Using the size mix in Appendix D, what share of Tall filings are under 300 sq ft compared with Wide filings, and how does that change what the pooled gap measures?
5. At 450 sq ft the Tall box runs from about $170 to $548 and the Wide box from about $226 to $600, with medians of $319 and $419. How much does a $100 gap between medians tell you when the boxes overlap this much, and what would more filings change?

## The trap

Most students will take the pooled medians at face value, and the confident wrong answer is **"pool everything: the Tall Plan costs 30.5% less per square foot, so file vertical."** Tall filings are mostly large jobs (median 931 sq ft vs 669) and cost per sq ft falls steeply with size for both plans, so the pooled gap mostly measures what size of job each plan is filed for. In the sizes the family might actually build, the plans trade places at about 304 sq ft. Second-level traps: (1) reading the Tall Plan's lower expected cost as a clear win when the bootstrap says it wins 52% of the time; (2) treating the 300 sq ft row as decisive (Wide by 4.6% on 70 and 178 filings, but a step in the curve, so a 25 sq ft change flips it to Tall by 36.3%); (3) forgetting that the average hides the shape: the plans have the same average but very different worst cases (D5); (4) taking the declared costs as quotes (MA5, Appendix E); (5) averaging the $/sq ft medians instead of the costs, which reverses the winner (Wide by about 2%): D4 asks for cost at each size first; (6) reading Appendix E's total-cost bins as the metric at 300 sq ft (Tall $121,255 vs Wide $140,598): those are totals over 300-449 sq ft, not the defined $/sq ft x size.

## Intro

Frame the format before anything else: this is a decision the family must make before the survey says how big the addition is. Name the opener: "You're Ilse Marchetti. The architect needs one box ticked, and nobody can tell you the size yet." Let the stakes land (a grandmother who takes the stairs with both hands) before moving to the Launch.

## Launch

Read the two plan names aloud with no numbers: the Tall Plan and the Wide Plan. Ask: "If all you knew was those two names, which one would you file, and why?" Take answers without correcting. Record the split; the case's job is to replace both gut reactions with a decision under an unknown size.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**
"Is anyone courageous enough to stand with the Wide Plan?" Show of hands, both options, no discussion. Record the count; Close will ask again.

## Anchor 2 — What is the problem we're solving?

**"Is 'which costs less per square foot' the right question?"** and "What do you mean by 'cheaper' when we do not know the size?" Let confusion grow: cheaper on average, cheaper in the worst case, cheaper at the most likely size? "Wow, this is a challenging problem."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"** Steer toward: compare like with like (similar-size jobs), cost at each possible size, then combine across sizes. Re-ask: "Is our question still the right question?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"** Surface: the size; whether declared costs are real costs; whether small Tall filings are bundled with other work; whether 2011-2020 dollars are comparable; the range itself. Ask which one would flip the stance.

## Data Deep Dive

Now the numbers. Let students build the nine-size table (Appendix B) and the cost memo (D4), then the two end-of-range box plots (D1). Hold back D3's pooled gap until the table exists, then reveal it and ask why it disagrees. Facilitator-only arithmetic: the averages and the regrets are in "The real numbers" above.

## Twist

**New information, delivered at 15:00:** "The survey is back. The rear yard and the stairs give one answer: the addition will be **exactly 300 square feet.**" Pause. Ask who changes their plan.
What it does: the average over nine sizes no longer exists; the only row that matters is 300. Tall $136,340 vs Wide $130,322: the Wide Plan wins by 4.6%, so the expected-cost winner (Tall) is reversed by one fact. But 300 is the crossing: the medians rest on 70 and 178 filings, the Wide Plan wins in only 54% of resamples there, and one step either way (25 sq ft) moves the cheaper plan. No position is obviously correct: the Tall-by-average camp is invalidated, the Wide-by-regret camp has won on a technicality, and the scope argument (D5) now decides.
Follow-up: **"What just broke in your original model? Were you wrong, or just missing information?"** The model was right for an unknown size; with the size known, it answers a question nobody is asking.
(`sensitivity_model.evaluate_twist` reproduces this: Tall loses to Wide at range 300-300.)

## Immediate recommit

15:00-20:00. "You have 60 seconds. Are you changing your plan?" Who reverses, who stays, and why. Ask the stayers: what number would make you reverse?

## Deep conflict — two threads (20-30 min)

1. **Average versus worst case.** At the unknown size, is the better plan the one with the lower average or the one with the smaller regret? Whose money is it? (The family's $150,000.)
2. **Is the cliff real?** The Tall plan's cost per sq ft jumps below ~300 sq ft. Is that building cost or other work bundled into small filings (Appendix E)? Both are inferences; what evidence would settle it? (A contractor quote for the actual scope.)

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00-3:00 | Launch: read both plan names with no numbers, cold-call a gut read, stand/sit vote (Anchor 1) |
| 3:00-10:00 | Position defense: *"Convince us why your plan is better when nobody knows the size."* |
| 10:00-15:00 | Pressure-test: *"Whose plan is most fragile if the survey comes back small? If it comes back large?"* |
| **15:00** | **DROP THE TWIST** (the addition is exactly 300 sq ft): slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? *"What just broke?"* |
| 20:00-30:00 | Threaded deep conflict (average vs worst case; is the cliff real) |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Close

**VOTE AGAIN.** "Did we ask the right question?" and "What math was new to you, and how did you attack it?" Ask whether anyone changed their vote because of the twist or because of the pooled comparison.

## Lessons Learned

- A big pooled gap can be a mix effect: compare like with like before trusting a gap.
- An average hides shape: two options can average the same and carry very different worst cases.
- When the data cannot pick a winner, the decision shifts to risk and to what the numbers leave out.
- A declared estimate is not a price.

## Standards Touched On

Box-and-whisker plot construction (D1), quartiles, outliers, median (D1, D3), scatter plot (D2), slope and linear versus non-linear (D2), mean (D4), compound units (D4), percents (D3, D4), comparing values (D4, D5). New coverage: none, since no spine skill is at n=0; the box-and-whisker how-to (n=1) is forced by D1 and non-linear (n=2) by D2. The case carries a `reinforcement_note`.

## Cohort bands (MCS-25)

- **Full (12-20):** anchors and the 45-minute plan as written.
- **Compressed (6-11):** Anchors 2-3 combine into one pass; the deep-conflict section runs one thread (average versus worst case); total runtime shortens proportionally.
- **1:1 / pair (1-2):** no vote; a stated initial position instead; the guide plays devil's advocate directly; the twist still lands, and "who reverses" becomes "would you reverse, and why".

## Facilitator note — sensitivity (SPEC §6)

Family finances and housing for an aging relative are the stake. Keep the discussion on the numbers and the decision, not on what families "should" be able to afford. Some students' families rent or live in crowded housing; do not ask anyone to disclose their home situation. No real filing, owner, address or applicant is shown; if students browse the dataset themselves, tell them it contains real owners' names and addresses and they should not search for or post identifiable people. The savings figure and the family are invented. Nothing here is construction, permit or legal advice: zoning, structural limits and permits are not modeled.

## Sensitivity (P5) and disclosed instabilities

Flexing the stated assumptions by +/-50%: window half-width (25 / 75): Tall by 0.0% / 0.3%, stable. Range low end 125: Wide by 18.7% (flips); 375: Tall by 23.7% (breaks the 20% cap). Range high end 225 (a single-size range at 250): Wide by 70.5% (flips and breaks the cap); 675: Tall by 13.2%. These are disclosed in `case.json.sensitivity_disclosure[]` as category F: the final size is a future survey result. The verdict depends on where the range sits relative to the crossing; that is the case's point.

## Grading note

Students working from Appendix B's rounded medians get slightly different dollars than the guide (for example $136,350 and $130,320 at 300 sq ft, averages $135,821 and $140,204, regrets $74,325 and $44,910). Differences are under $20 per figure; accept either.
