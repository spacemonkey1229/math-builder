# Guide Notes: The Average Lies

MS/HS | Guide Notes | Adventure | 2026-27
**Tier:** T4 (HS-entry) · **Primary metric:** share of historical windows in which all four tuition bills are paid in full at the gift's size (second axis: share of windows that also leave at least the student's chosen leftover) · **Margin:** computed at case-research (see "The margin") · **SPEC Section 6:** does not apply as a death/illness stake; one facilitator note on family money stress (below).

**Status: DRAFT from case-write.** Every figure marked "concept stage" was computed from the Damodaran historical-returns file (1928-2025) and the College Board's published tuition series during concept review and has NOT yet been research-sourced or re-verified. Do not quote it to students until `case-research` confirms it.

---

## Argument for A — The Growth Mix

The family is not trying to maximize wealth; the grandmother has said she wants leftover for graduate school, and only a stock-heavy mix produces much leftover. At the concept-stage gift of $50,000 and 3.5% tuition growth, the Growth Mix (70% stocks / 30% bonds) pays all four bills in 92.2% of 90 historical windows and leaves at least $20,000 in 64.4% of them, against 34.4% for the Steady Mix; the median leftover is $36.7K against $15.5K (failures counted as $0). For any student who values leftover, B gives up two dollars in three of what A would have produced. The failures are real but bounded in size relative to the upside.

## Argument for B — The Steady Mix

The first four bills are the promise; leftover is a hope. At the concept-stage gift the Steady Mix (30% stocks / 70% bonds) pays all four bills in 96.7% of windows against 92.2% for A (87 of 90 against 83 of 90, a gap of about 4.8%), and its worst window leaves the family about $4,900 short against about $21,100 for A (concept stage). For a family that cannot make up a shortfall, a mix that fails about half as often and a quarter as badly when it does is the responsible choice. **A student who cares only about paying the bills chooses B on the primary metric with no leftover threshold at all, and that is a legitimate answer.**

## The margin

**Primary metric:** share of windows in which all four bills are paid in full, at the gift's size. **Margin (to be computed at case-research):** B's share minus A's share, as a percent of A's, from sourced inputs. Concept stage: about 4.8% (87 of 90 against 83 of 90), well inside the SPEC §2 cap of about 20%. **Second axis, declared (so neither option dominates):** share of windows with all bills paid and at least $20,000 left; concept stage A 64.4% against B 34.4%, A ahead by about 87% relative. **Thresholds:** for a leftover threshold from $15,000 to $30,000, A leads the second axis at every tuition growth rate in the measured band (concept stage); below a crossover that depends on the growth rate (about $13,000 at 2.40%, about $8,500 at 3.5%, about $6,400 at 3.97%), B leads both axes, so a bills-only student is correct to choose B. `case.json.margin_pct` stays null until research recomputes it.

## Five Socratic questions

1. D2's calculator says one mix is cheaper and D3's history says the other is. By how many dollars and what percent does each method say the family needs, and what is it about a steady average that makes the two ranks disagree?
2. In D3 the Growth Mix pays all four bills in a smaller share of windows than the Steady Mix but leaves much more when it works. At the leftover amount you chose, how many more windows does the Growth Mix need to leave that amount before you would call it the better choice, and why that number?
3. D4's planning gap is larger for one mix. If the family funded exactly the calculator's lump sum, in what share of windows would all four bills be paid, and would you tell Mara that plan is "on track"?
4. D5 reverses the order of the same yearly returns. Of the windows that failed, how many now pay, and what does that tell you about what the average return can and cannot predict for one family?
5. In D4 you found the smallest lump sum each mix needs at the reliability you chose. How far above or below each of those is the gift, and what happens to your recommendation if the gift were a few thousand dollars smaller, or a few thousand larger?

## The trap

The confident wrong answer is **"the calculator says the stock-heavy mix needs less, so use it."** A steady-return calculator reports one number and no probability: at the average rate each mix has historically earned, the lump sum it names pays all four bills in only about half of the historical windows for the Growth Mix and about a third for the Steady Mix (concept stage: 54.4% and 36.7%). Second-level traps: (1) using the arithmetic average instead of the compound average as the steady rate (the arithmetic average is higher and flatters the stock-heavy mix); (2) forgetting that **the order of returns matters once money is being withdrawn** (D5: the same returns in reverse order rescue most failing windows; concept stage: 6 of 7 for A, 3 of 3 for B); (3) treating 90 overlapping windows as 90 independent stretches (they are about ten independent blocks, and on non-overlapping blocks the Steady Mix is ahead by at most one block).

## Independence caveat (facilitator note, plus one student question)

The 90 windows overlap. On non-overlapping nine-year blocks, B pays all four bills in at least as many blocks as A but only by zero or one block, depending on the starting year (concept stage: across nine starting years, A pays in 7 to 10 of its 10 blocks and B in 8 to 10); five of A's seven failures start in 1928-1937. So "B is safer" is suggestive, not proven. Ask students: *how many independent nine-year stretches does the record really contain?*

## Facilitator-only legal and tax note (not student text)

The case models a gift, not tax advice. A $50,000 gift exceeds the 2026 annual gift-tax exclusion of $19,000 per recipient (IRS, "What's New - Estate and Gift Tax"); tuition is excluded only if it is paid directly to the school (26 CFR 25.2503-6), which a lump sum to a family is not; the FAFSA's treatment of grandparent-owned 529 plans changed (secondary sources say they are not reported for 2024-25; verify on studentaid.gov before stating it).

## Sensitivity note (SPEC §6)

Family money stress: some students' families carry college debt or have no college fund. Students may opt out of the family-money framing and work from the numbers alone. The case frames the risk as a borrowing consequence (the unpaid part of a bill is borrowed), not as a family losing a college place.

## Facilitator guide notes (batch)

- **Contrast with its companion, The Eight-Percent Bet:** there, stocks help a pool *reach a target while saving*; here, bonds help a fund *pay bills while withdrawing*. Both use the same Damodaran historical-returns table (also cited by the published case `the-quiet-thief`; three corpus items use it). Name the contrast aloud when teaching both, or a teacher will hear a contradiction.
- **The calculator is a model, not a strawman.** The case models a calculator's assumed rate with each mix's compound average, a typical single-number input; real calculators vary. Do not tell students "all calculators lie."
- **The geometric mean is not a spine skill** (logged as a spine gap with present value and compound interest). Teach it as the compound average and have students check it by growing one dollar through every year and taking the root.

## Standards touched on

Sequences and series (D1, D2), recursive formulas and explicit forms (D2, D3), exponential expressions (D1, D2), mean (D2), percent and conversion to percent (D3, D4, D5). New coverage: none (every spine skill is already at n>0); the case carries a `reinforcement_note`.
