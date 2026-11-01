# FACILITATOR.md: The Last Bench

**Status:** written with the case (stage 2), numbers filled after case-research (stage 3). This file and `case.json`'s `balance` object are the only places the balance argument, the margin, the break-even and the Twist may live. None of it appears in `case.md`.

**Sensitivity note (SPEC section 6, read before the room).** This case is about whether a mine closes and a crew of 180 loses its work in a town of 2,100. Some students may have a family member in mining, energy or another industry that has closed. The crew and town figures are a **scenario** the class may change, not a prediction. Invite the room to ask who bears the cost of each option without assigning blame to a person (Corwin, the board, the drivers). Do not let the cash margin alone end the debate: the stake is a legitimate argument, but the math must show it, not assume it.

**Conventions.** Margin = (winner - loser) / winner. Undiscounted unless stated. Planning price = USGS 2024 annual average (2,388 USD per troy ounce), from USGS Mineral Commodity Summaries 2026 (February 2026). Case cutoff 2026-10-28. Tonnes are metric.

---

## Argument for A: Close at the Floor

At the planning price the pushback does not pay for itself. Every tonne of ore recovered is worth 67.56 USD (1.0 g/t x 88% / 31.1035 g per oz x 2,388) against 22 USD to process, a net of 45.56 USD. But the pushback moves 146.6 Mt of rock to reach 9.61 Mt of ore: 137.0 Mt of waste, a stripping ratio of 14.26. Mining that rock costs 439.7 USD million, while the ore it uncovers nets only 437.7 USD million, so the pushback loses 1.9 USD million before the 60 USD million of capital, and 62.0 USD million after it. Option A earns 914.1 USD million; Option B earns 852.1 USD million. A is ahead by 62.0 USD million, a margin of 6.8%, with no capital at risk, no extra waste to move and no dependence on a price that has to keep rising.

## Argument for B: The Sixty-Meter Pushback

The price is the decision, and the price is moving. Break-even gold price (where A and B tie) is about 2,616 USD per troy ounce, only 9.6% above the 2,388 planning price, and the same USGS series rose from 1,801 in 2021 to 2,388 in 2024 (+32.6%). The pushback adds 271.8 thousand ounces of recoverable gold that A walks away from for good, and it extends mine life from 3.75 to 11.08 years: 1,994 crew-years against 675, an extra 1,319 crew-years of work for a crew of 180 (8.6% of the town's population). The 62.0 USD million that B gives up buys those years at about 47,000 USD per crew-year. If a Hero can defend that price per job-year as worth paying, B wins on the stake even while A wins on cash.

## The margin

**Anchor (2024 planning price): A wins by 6.8%** (A 914.1, B 852.1, gap 62.0 USD million; computed as gap / winner = 62.0 / 914.1 = 6.78%). Inside the SPEC 20% cap. Case-record value: `margin_pct` 6.78.

| Year | Price | A | B | Winner | Gap | Margin (gap / winner) |
|---|---|---|---|---|---|---|
| 2021 | 1,801 | 498.9 | 277.3 | A | 221.5 | 44.4% |
| 2022 | 1,802 | 499.6 | 278.3 | A | 221.3 | 44.3% |
| 2023 | 1,945 | 600.7 | 418.3 | A | 182.4 | 30.4% |
| **2024 (anchor)** | **2,388** | **914.1** | **852.1** | **A** | **62.0** | **6.8%** |

The 2021 to 2023 rows are outside the 20% cap on purpose: they are history the Hero plots in D5 (they show how fast the gap closes as price rises), not the decision. The decision is the 2024 row. The Hero's graph should show the two lines crossing at the break-even price, between 2024 and any later year.

**The ledger of the pushback alone (per D2/D3), 2024 price:** 9.606 Mt ore x 45.56 = +437.7; 146.55 Mt moved x 3.00 = -439.6; capital -60; total -62.0. Capital is not the lever: even with zero capital A still leads by 2.0 USD million. The live lever is price.

**Stripping ratio vs break-even stripping ratio (extension E1).** Break-even SR = (recovered value per ore tonne - processing) / mining - 1 - capital / (pushback ore x mining). 2021: 6.57; 2022: 6.58; 2023: 7.93; 2024: 12.11, against the pushback SR 14.26. Rule: pay for the pushback only if its stripping ratio is below the break-even. At 2024 the pushback fails the rule.

**Discounting (extension E3, MA7 convention: 8% a year, 20 Mt/yr, cash at the middle of each year, part-years prorated, capital paid when the pushback begins).** 2024: A 793.8, B 747.7, A ahead by 5.8%. Under end-of-year discounting the same winners hold (A 765.2, B 719.1). Discounting does not flip the anchor.

**Stake (D4).** Mine life: A 75 / 20 = 3.75 years, B 221.55 / 20 = 11.08 years. Crew-years: A 675, B 1,994, so B adds 7.33 years and 1,319 crew-years. Forgone cash per extra crew-year: 62.0 / 1,319 = 0.047 USD million, about 47,000 USD. Crew as a share of the town: 180 / 2,100 = 8.6%.

### Stability under plus or minus 50% (probe 5, disclosed)

The verdict is **not** stable under a 50% swing in many assumptions; the case says so here so the guide does not defend a margin that is thinner than it looks. Flip points (percent change in one assumption, others held, that makes B win at the 2024 price): head grade or recovery +9.6%; mining cost -14.1%; processing cost -29.3%; floor radius -22.2%; current depth -12.0%; wall angle +7.9%; ore-pipe radius +6.9%. Pushback capital never flips the winner (even at zero). The gold price flips it at 2,616. This fragility is the lesson, not a defect: a 6.8% margin on scenario inputs is a coin-flip on geology and cost, and the stake argument is what a Hero can add that the arithmetic cannot.

---

## Intro

Frame the format: this is a decision, not a worksheet. Name the opener: a cold call asking one student to describe, in one sentence, what Corwin is looking at from the last bench. Read the sensitivity note aloud in your own words.

## Launch

Show a photo or short video of a working open-pit mine with haul trucks on the ramp, or the USGS gold page headline. Ask only: what is the pit for, and who works in it?

## Anchor 1: Take a stand and vote

No reasoning yet, just commit. "Is anyone courageous enough to stand with closing the pit? With the pushback?" Record the split.

## Anchor 2: What is the problem we are solving?

"Is the question 'which option makes more money', or 'which option is worth what it costs'?" "What do you mean by 'worth it'?" Let confusion grow: cash, jobs, risk, the price. "Wow, this is a challenging problem."

## Anchor 3: What is the process?

"If we find the numbers, how will we decide?" Draw out: tonnes of rock moved, tonnes of ore, ounces, dollars per tonne, the tie price. Re-ask: "Is our question still the right question?"

## Anchor 4: What don't we know?

"Which numbers in this case are facts and which are choices?" Point students to Appendix C. "Which assumption, if wrong, would change your vote?" Do not reveal the flip points yet.

## Data Deep Dive

Now, and only now, the numbers: D1 volumes, D2 pipe and stripping ratio, D3 margins and break-even, D4 stake, D5 graph. Have two students put their D1 shell and their D3 break-even on the board and compare (they should agree to within rounding).

## Twist

Delivered slowly, with pauses, at about 15:00. **Say:** "The USGS later publishes its estimate for the 2025 average gold price, based on January through November data: 3,300 USD per troy ounce. That is 38% above the 2024 figure you used." Then: "You have 60 seconds. Are you changing your vote?"

What the twist does (facilitator only): at 3,300, A earns 1,559.1 and B earns 1,745.0. **B now wins by 10.7%** (gap 185.9 / winner 1,745.0). The price has crossed the 2,616 break-even, the pushback SR (14.26) is now below the break-even SR (20.71), and the two cash arguments reverse. Discounted at 8% (MA7 convention): A 1,354.0, B 1,449.8, B ahead by 6.6%. The stake argument did not change at all; only the cash argument moved.

This breaks the "A on cash, therefore A" position and also breaks the "B because the price keeps rising" position's certainty, because 2025 is a part-year estimate, the pushback capital is committed at one price, and a price falling back below 2,616 reverses it again. The follow-up is the whole point: **"What just broke in your original model? Were you wrong, or just missing information?"** And then: "Why should the answer not simply track the latest number?"

## Close

Vote again. "Did we ask the right question?" "What math was new to you, and how did you attack it?"

## Lessons Learned

A decision can be right on the information at hand and still be reversed by new information. The price, not the capital, was the lever. A cash margin and a stake are different currencies; the math can price one in the other (47,000 USD per crew-year) but cannot say whether the price is worth paying.

## Standards Touched On

Cone and cylinder volume, compound-unit conversion (grams per tonne to ounces), percent of a number and conversion to a percent, solving a linear equation with the unknown on both sides, graphing points and drawing lines from equations.

---

## Five Socratic questions

1. Your D1 shell is 146.6 Mt but your D2 ore pipe is only 9.6 Mt. What does that ratio tell Corwin about each tonne of gold-bearing rock he uncovers, and what would the pipe radius have to be for the stripping ratio to equal the break-even at the 2024 price?
2. Your D3 break-even price is about 2,616 USD per troy ounce and the 2024 price is 2,388. The price rose 32.6% from 2021 to 2024. Does that history make B more defensible or just make you feel better about B?
3. Capital is 60 USD million, but A still leads by 2.0 USD million with zero capital. Why is the capital not the thing to negotiate, and what would a mining cost of 2.50 or 3.50 USD per tonne do to your break-even?
4. Option B costs 62.0 USD million of cash for 1,319 extra crew-years, about 47,000 USD each. Is that a fair price for a job-year, and who decides?
5. Your crew number is a scenario input. If the crew were 60 or 400, would the stake argument for B get stronger or weaker, and does the answer to question 4 change?

## The trap

**Ore-only accounting.** The confident wrong path: "The pushback uncovers 9.6 Mt of ore and each ore tonne nets 45.56 USD, so B adds 437.7 USD million and clearly wins." It ignores that reaching the ore means moving 146.6 Mt of rock at 3.00 USD per tonne, which cancels the ore's value at the 2024 price. A second form: forgetting the waste in Option A's reserve, or mixing Mm³ with Mt (skipping the density), or comparing 914.1 against 852.1 and calling the 62.0 gap "huge" without dividing by the winner. A third: treating the stake as a number that settles the question, instead of a different currency to be priced and argued.

**Traps a room that does the full work will actually hit (found by the Tier 2 cold reads).** (1) Using the depths (300 m, 360 m) as cone heights instead of the given apex-to-rim heights, or forgetting the small floor cone. (2) Double-counting the pipe: reporting the whole shell as waste and then adding the ore on top, which overstates mining cost and the stripping ratio. (3) Omitting the capital, which makes A lead by only 2.0 USD million and moves the break-even to within a few dollars of the planning price, so the student concludes the options are tied. (4) Picking the 50-degree wall design from Appendix B: the pushback then costs far less to uncover and B wins, so a Hero can win the case by changing the problem. Treat it as a good thread (what does a steeper wall cost in safety, and who decides?), not an error. (5) Looking up today's gold price instead of the planning deck: answer that the board's deck is the 2024 average and that this is exactly the lesson of the Twist. (6) B defers the closure, it does not prevent it: the crew still leaves at the end of the longer mine life; and under B the first years are pure stripping (about 439.6 USD million of mining cost before the pipe ore arrives), which the undiscounted metric hides.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (what is Corwin looking at?), 30-second commitments, stand/sit vote. No explanation. |
| 3:00-10:00 | Position defense: "Convince us why it is better, not just cheaper." Pull one cash argument and one stake argument. |
| 10:00-15:00 | Pressure-test the models: "Whose plan is most fragile?" Ask for the assumption each Hero would most want to check (grade, mining cost, wall angle, crew). |
| **15:00** | **DROP THE TWIST**: the 3,300 USD per troy ounce estimate, delivered slowly, with pauses. |
| 15:00-20:00 | Immediate recommit: who reverses? "What just broke?" "Were you wrong, or just missing information?" |
| 20:00-30:00 | Threaded deep conflict (2-3 named threads): cash margin vs crew-years; a one-year price estimate vs an irreversible commitment; who bears the cost of each option. |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned, "what math was new to you?" |
