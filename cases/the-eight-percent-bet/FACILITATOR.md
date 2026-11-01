# Guide Notes: The Eight-Percent Bet

MS/HS | Guide Notes | Adventure | 2026-27
**Tier:** T4 (HS-entry) · **Primary metric:** pool-to-debt ratio on the first payment date (The Long Bet beats The Clean Check when the ratio is at least one; The Clean Check has no pool and no debt, so the comparison is the sign of the net position) · **Margin:** computed at case-research (see "The margin") · **SPEC Section 6:** does not apply to students; one facilitator-only note on financial fraud (below).

**Status: DRAFT from case-write.** Every figure in this guide marked "concept stage" was computed from the Damodaran historical-returns file during concept review and has NOT yet been research-sourced or re-verified. Do not quote it to students until `case-research` confirms it.

---

## Argument for A — The Clean Check

Certainty has a price the owner can see. Paying today makes the club's obligation exactly zero; there is no pool to track, no snapshot to dread, and no roster spot to cut years from now. The strongest quantitative case: the deferral costs a fixed, known rate on the unpaid salary, while the pool must beat that rate **after** rebalancing, **every year, for as long as the wait lasts**, using a mix capped by policy at a share of stocks. Appendix B shows that a policy-mix pool beats the grown debt only in roughly half of the historical runs (concept stage: 52.3% of 88 overlapping runs; median ratio about 1.05; 10th percentile about 0.68), and in the real run that began in the signing year the pool fell well short (concept stage: 60/40 returned about 3.75% a year; the pool was about $8.85M against a debt of about $13.76M, roughly $4.9M short). A bet that wins about half the time and loses by a third of the debt when it loses is not an obviously good use of an owner's trust.

## Argument for B — The Long Bet

The deferral's price is an interest rate; the pool's return is whatever the markets deliver. Over the long record, the median run clears the grown debt slightly (concept stage: median ratio about 1.05), and the upside is much larger than the downside is deep in dollars the club can actually keep (concept stage: 90th percentile about 1.70, with the 10th percentile about 0.68). The club does not have to pay the player today, keeps the cash working, and keeps any surplus. The shortfall, when it comes, is spread over the repayment years and covered from a roster budget, not paid in one lump. A finance director who refuses every bet whose odds are about even will be unable to run a club.

## The margin

On the primary metric the comparison is a sign test, not a ratio of two totals: the pool-to-debt ratio is compared to one. **Margin (to be computed at case-research):** the median pool-to-debt ratio at the club's policy mix minus one, as a percent of the debt. Concept stage: about 5%, well inside the SPEC §2 cap of about 20%. With a stocks-only pool the median is about 28.5% above one, outside the cap, which is why the allocation is fixed as club policy and not a student choice. `case.json.margin_pct` stays null until research recomputes it from sourced inputs.

## Five Socratic questions

1. Your D1 figure is the debt on the first payment date. By what percent did the unpaid salary grow, and why is comparing the pool with the original salary the wrong test?
2. D3's median ratio is close to one. What does a median near one tell you about the chance The Long Bet works, and what does the width of the box tell you that the median does not?
3. D4 counts successful blocks, and the count changes when you move the starting year. How many of the independent blocks would you want to see succeed before you told the owner "yes," and why?
4. D5 shows the real run. If the club had held only bonds, or only stocks, how would D3's median and its share of runs at or above one change, and would that have been a better decision or only a luckier one?
5. In D6, how does the yearly gap change when you lower the funding rate, who benefits from your choice, and how many roster spots does your yearly gap cost?

## The trap

The confident wrong answer has three forms, and good students will find at least one:
1. **Comparing the pool with the salary instead of the grown debt.** The unpaid salary compounds; the right yardstick is the debt on the first payment date, not the number in the contract's first line.
2. **"Stocks average more than the deferral rate, so defer."** An average return is not the compound return a pool actually earns, and an average hides the runs where the pool is a third short. (This is the seed of the sequel case, The Average Lies.)
3. **Treating 88 overlapping runs as 88 pieces of evidence.** They are about eight independent blocks; the count of successful blocks moves with the starting year (concept stage: 3 to 5 of 8 at 60/40).

## Optional teacher-read reveal (after the vote is closed)

*"The numbers in this case come from a real deal. In 2000 a New York baseball club still owed one of its former All-Stars $5.9 million of salary for that season. The two sides agreed to defer the money at 8% interest. Starting July 1, 2011, and every July 1 through 2035, the club pays him $1,193,248.20. Check your answer to D2 against that number. (This case moved the first payment to January 1 to keep the clock simple.)"*

**Optional teacher sentence (public record; the user has not yet ruled on whether it may appear): "The player is Bobby Bonilla, and the media call July 1 'Bobby Bonilla Day.'"** The reveal itself names no player and no owner.

## Facilitator-only background on the real deal (never in student text or any student export)

Reporting says the real club's ownership was invested in a Bernard Madoff account that promised double-digit returns (ESPN, 2024). Madoff pleaded guilty on March 12, 2009 and was sentenced on June 29, 2009 to 150 years. In 2012 the owners agreed to pay $162 million in settlement with the trustee (NBC News) and their lawyers said they had no idea the investments were fraudulent (JTA). Reports differ on who proposed the deferral (a 2013 report says the club; the player's agent says the club) and on the exact release date; no primary contract text was found. A second reported deferral exists with a different counterparty and is not used. **This material is facilitator-only context for the question "what happens when the 'safe' bet is itself a fraud?"; do not use it to shame a student's choice, and do not name any living owner.**

## Sensitivity note (SPEC §6)

None for students. The real-deal backstory involves a large financial fraud and real victims; keep it out of student text and out of any student export. The case is about arithmetic and uncertainty, not about blame.

## Standards touched on

Recursive formulas and explicit forms (D2), sequences and series (D2), exponential expressions (D1), percent (D3, D6), quartiles, box-and-whisker plots and median (D3), mean (D4). New coverage: none (every spine skill is already at n>0); the case carries a `reinforcement_note`.

## Facilitator guide notes (batch)

- **Contrast with its companion, The Average Lies:** here, stocks help a pool *reach a target while saving*; there, bonds help a fund *pay bills while withdrawing*. Both use the same Damodaran historical-returns table (also cited by the published case `the-quiet-thief`). Name the contrast aloud when the two cases are taught in one unit, or a teacher will hear a contradiction.
- **Roster stake wording (student text, for D6):** "Every season for the repayment years, the club must cut about one minimum-salary player to cover the gap." Compute the player count from Appendix C's sourced league minimum; do not use a remembered figure.
