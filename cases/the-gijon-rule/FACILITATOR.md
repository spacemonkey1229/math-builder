# Guide Notes: The Gijon Rule

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 (MS-core) · **Primary metric:** the ceiling, the larger of two safe-cell percents (1-0 and 6-5) over the 49 Algeria-Chile cells, lower is better · **Margin:** 7.14% relative, i.e. B's ceiling is 7.14% higher than A's (about 6.1 percentage points); Option A's ceiling is lower; read the sensitivity note before Lessons Learned

---

## Intro

Heroes, a committee has to replace a rule before the next World Cup. One camp wants to change only the clock. The other wants to change the clock and the way ties are broken. I'm not going to tell you which is better. One thing before we start: nobody in this case is accused of anything. FIFA ruled that no rule was broken. We are studying what a rule rewards, not who is a good or bad person.

## Launch

Show the one-line fact on the board: *In 1982, two teams played a match in which, for most of the second half, neither side tried very hard to score. Both got what they needed. A third team, which had finished a day earlier, went home.* Ask: *"If you were one of the two teams, what would you do? If you were the team that went home, what would you want changed?"*

Let them argue about fairness for two minutes. Then: *"Marguerite has to turn that argument into a rule. She can't ask anyone to behave better. She can only change the rules."*

> **Hero name: Same-Clock Only, or Same-Clock, Goals First? Commit out loud.**

Teach-from-scratch note: many Heroes will not know how a World Cup group works. Draw the four-team round-robin on the board (six matches), the two-points-per-win table and the tie-break ladder before the vote (Appendix A). Do not skip this.

---

## Anchor 1 — Take a stand and vote

Option A (Same-Clock Only) or Option B (Same-Clock, Goals First). No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start counting grids yet.

- What's the actual question, in one sentence? "Which rule is fairer?" "Which rule stops what happened?" "Which rule leaves two teams with the smallest guaranteed deal?" Those sound similar and are not the same question. The case's number measures the last one.
- Someone will say "obviously add the goals rule, it punishes the 1-0 coasting." Push: *"Punishes it for which teams, in which tournaments? Does it only change 1982?"*
- Someone will say "three points for a win fixes it." Do not correct. Let D2 do it.
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh. 'Fix the match that happened' and 'fix the rule for every match to come' might not be the same job."* Do not rescue them.

**The trap to let them walk into (two forms).** (1) Most Heroes will count the 1-0 grid, see that Option B shrinks the safe cells from 39 of 49 (79.6%) to 29 of 49 (59.2%), and stop: *B shrinks the coasting gamble, B wins.* They miss the second benchmark: under B, 6-5 is safe in 45 of 49 cells (91.8%), higher than Option A's 42 of 49 (85.7%), so the ceiling rises. Goals-first does not remove the cooperative scoreline; it moves it up the scoreboard. (2) A subtler trap: treating the 49 cells as probabilities ("A is safe most of the time"). The cells are a counting device; no cell is more likely than another. Catch it every time it is said aloud.

## Anchor 3 — What is the process?

- If we mark every cell for every scoreline, how many cells is that? (By the Fundamental Counting Principle: 49 cells per grid.)
- What does "safe" mean precisely, and what do we do with a tie that only a lot can break? (MA2: unresolved is never safe.)
- If we get a percent for 1-0 and a percent for 6-5, how do we decide which one the committee should care about, before we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What does the grid assume that real teams might not do? (MA4: steering to a scoreline.)
- Why 0-6 goals? What if it were 0-3 or 0-9? **Have them actually try the smaller and larger window and see how much the comparison moves.** (Sensitivity: see the note below. Do not read the numbers aloud.)
- Appendix F says A's own cost (a broadcast slot, fan access) is unsourced. Do you believe the case is complete? What would you need to know?
- What are we assuming about what the teams can see while the matches are on? (This is the case's built-in opening for the twist; don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1: the standings (D1).** Before West Germany-Austria (after matches 1-5):

| Team | P | Pts | GF | GA | GD |
|---|---|---|---|---|---|
| Austria | 2 | 4 | 3 | 0 | +3 |
| Algeria | 3 | 4 | 5 | 5 | 0 |
| West Germany | 2 | 2 | 5 | 3 | +2 |
| Chile | 3 | 0 | 3 | 8 | -5 |

West Germany's 1-0 win gives: West Germany 4 pts, GF 6, GA 3, GD +3; Austria 4 pts, GF 3, GA 1, GD +2 (the signed addition: +3 plus -1 = +2); Algeria 4 pts, GD 0. Goal difference separated Algeria from Austria: +2 against 0.

**Step 2: the three-point test (D2).** With Algeria-Chile at its as-played 3-2 and any West Germany win from 1-0 to 6-5, the advancing pair under three points per win is the same as under two points per win. A case-wide recount (every Algeria-Chile cell, every West Germany-Austria scoreline, both ladders, 7 x 7 x 7 x 7 = 2,401 combinations per ladder) finds **0** differences. The reason to draw out, with Algeria-Chile as played: in every West Germany win, West Germany, Austria and Algeria each finish with two wins and one loss, so three points per win just rescales three equal totals (4 becomes 6) and the tie that goal difference had to break is still there. (That is the as-played reason (with an Austria win or a draw, Austria finishes ahead of West Germany and Algeria and keeps its place whatever the points rule; West Germany needs a win to pass anyone); the exhaustive recount, which includes every cell with a draw, is what supports the broader claim, and a draw in either match is the only way a different points value could matter at all.) As played, under 1982's ladder, the West Germany wins that send West Germany and Austria through are 1-0, 2-0, 2-1, 3-1, 3-2, 4-2, 4-3, 5-3, 5-4, 6-3, 6-4, 6-5. 5-2 is an unresolved tie (Austria and Algeria level on points, goal difference and goals scored) and 6-3 does send Austria through (it is in the list above, not an exception to it). The wins that send West Germany and Algeria through instead are 3-0, 4-0, 4-1, 5-0, 5-1, 6-0, 6-1 and 6-2.

**Step 3: Option A grids (D3).** 49 cells per grid (7 x 7 by the Fundamental Counting Principle).

| Scoreline | Safe | Percent | Algeria wins (21 cells) | Algeria draws (7) | Algeria loses (21) |
|---|---|---|---|---|---|
| 1-0 | 39 | 79.6% | 11 | 7 | 21 |
| 6-5 | 42 | 85.7% | 14 | 7 | 21 |

(6-5 under A also has 1 unresolved cell.) The ceiling for Option A is 42 of 49, **85.7%**.

**Step 4: Option B grids (D4).**

| Scoreline | Safe | Percent | Algeria wins (21 cells) | Algeria draws (7) | Algeria loses (21) |
|---|---|---|---|---|---|
| 1-0 | 29 | 59.2% | 1 | 7 | 21 |
| 6-5 | 45 | 91.8% | 17 | 7 | 21 |

The ceiling for Option B is 45 of 49, **91.8%**. For 1-0 the Venn diagram has three regions: only under A = 10, under both = 29, only under B = 0, and B's safe set is a subset of A's. For 6-5 it runs the other way: A's safe set is a subset of B's (only under B = 3 cells: Algeria 4-0, 5-0 and 5-1). The best scoreline over the whole 0-6 window is 6-5 under both options.

**Step 5: the ceiling, the average and the margin (D6).** Ceiling: A 85.7%, B 91.8%. B's ceiling is higher by 6.1 percentage points, which is 7.14% of A's (45/42), so on the primary number Option A wins. **Average of the two benchmark percents:** A (39+42)/98 = 82.7%, B (29+45)/98 = 75.5%; now B is lower by 7.1 points, and A's average is 9.46% higher than B's. So which summary the committee adopts decides the winner. That is the case's real tension and B's strongest quantitative argument: it is not that B wins on the ceiling (it does not), it is that the ceiling lets one extreme scoreline (a 11-goal match) outvote the scoreline that was actually played. Say plainly to the room: the primary metric as defined favors A; the average favors B; neither is the 'true' one. Do not let the room treat that as the end: the 1-0 share falls by 10 cells, 20.4 points, under B, and that is exactly the scoreline played in 1982.

**Step 6: the cost to history (D5).** Under Option B's ladder, Group 6: Scotland (GF 8) replaces the Soviet Union (GF 6, who advanced on goal difference). Groups 1, 3, 4 and 5 are unchanged. Group 2 as actually played: under B's ladder, West Germany (GF 6) and Algeria (GF 5) advance and Austria (GF 3) does not.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"The two matches kick off at the same moment, as both options require."*
>
> (pause)
>
> *"Late in both matches, word reaches the benches. The Algeria-Chile match is over. It ended as a narrow Algeria win: by one goal or by two. Like the 3-2 that was actually played."*
>
> (pause)
>
> *"Treat that as settled for the other match. Cross out every cell that is not a one-goal or two-goal Algeria win; the grid is now those cells only, and your percents are out of those cells. Rerun your ceiling and your average."*

**Facilitator only: read before you drop this, do not read aloud.** The surviving grid is 11 cells (6 one-goal and 5 two-goal Algeria wins). Percents re-based on 11 (Appendix C): Option A: 1-0 safe in 11 of 11 and 6-5 in 11 of 11, so ceiling 100% and average 100%. Option B: 1-0 safe in 1 of 11 (9.1%) and 6-5 in 11 of 11, so ceiling 100% and average (1/11 + 1)/2 = 54.5%. So the ceilings **tie** (A's 7.14% lead vanishes) and the averages **split wide open** in B's favour (100% against 54.5%). A student who keeps 49 as the denominator gets 22.4% for both ceilings (11/49) and averages of 22.4% (A) against 12.2% (B); the tie and the split are unchanged. This breaks both comfortable positions: "A is better because its ceiling is lower" (the ceiling now ties) and "the average gap is small, so B hardly matters" (B's cut to the coasting scoreline is now the whole story). It makes neither option obviously correct: the choice between rules now turns entirely on which summary the committee adopts, and on D5, where B's costs are unchanged (B rewrites Group 6, would have sent Algeria not Austria through in Group 2, and changes every future group). The twist keeps the as-played 3-2 inside the surviving grid, so no convention is contradicted. State aloud: the 0-6 window still applies to both matches (so 'by one or two goals' leaves 11 cells), the benchmarks stay 1-0 and 6-5, and Option A's premise is not being argued here: the news is assumed to reach the benches although the kickoffs are simultaneous (simultaneity delays information, it does not remove it). Warn yourself that the tilt is real: with the ceilings tied and the averages 100% against 54.5%, B looks strong if the average is allowed to break ties; the counter is D5's unchanged costs and the point that a 100% ceiling under either option means the ceiling has stopped telling the options apart. D3's draw/loss split is empty after the twist (0 draw and 0 loss cells); do not ask for it. Ask: **"Sixty seconds. Are you changing your recommendation, or not?"**

**Follow-ups, only if the room has time.** (1) *Algeria did not win* (a draw or a Chile win, 28 cells): 1-0 and 6-5 are each safe in all 28 under both options, so ceiling and average are 100% under both and the options are identical. Percents kept on 49 give 57.14% for both; the tie is unchanged. Lesson: simultaneous kickoffs delay information; they do not remove it, and some news makes the tie-break order irrelevant. (2) *Algeria won by any margin* (21 cells): 1-0 safe in 11 (A, 52.4%) against 1 (B, 4.8%); 6-5 in 14 (A, 66.7%) against 17 (B, 81.0%); ceiling A 66.7%, B 81.0%; average A 59.5%, B 42.9%. (Wikipedia's account of the Disgrace of Gijón also records a 2018 World Cup match in which one team, watching the other match played at the same time, changed its play: Japan-Poland. If you use it, tell the room the 2018 tie-breaks differed and this case does not analyze them.)

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong, or were you just missing information?** (Sit on this one.)
- Who built their case on "simultaneous kickoffs fix it" or on "the 1-0 gamble is shrunk by B" without ever asking what a team can learn mid-match?

---

## Deep conflict — threads (20-30 min)

**Thread 1 — Moving the safe scoreline.** *"If B takes 1-0 off the table, why does the ceiling go up?"* Push toward: a rule cannot remove a team's incentive to find a mutually good scoreline, it can only move where that scoreline sits. Goals-first moves the safest scoreline to a high-scoring win; now two teams that both profit could cooperate on a goal-fest. B also changes every future group for every team: a side protecting a lead gains nothing from goal difference under B, and attacking play is rewarded whether or not it wins the game. Ask whether a 6-5 deal is more or less plausible than a 1-0 deal. The case has no data on that. Say so.

**Thread 2 — Better rule, or just the one history picked?** *"Option A is what FIFA actually did. Does that make it the better rule, or only the one history picked?"* Do not give the answer. Push: what would you have to see to call the actual choice good? Option A costs no 1982 result. Option B rewrites a real result in one of five other groups and, as played, would have put Algeria through in place of Austria. That cuts both ways, so ask whose result you would be willing to rewrite, and why.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00-3:00** | Cold-call launch. *"Thirty seconds: change only the clock, or change the clock and the ladder?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00-10:00** | Position defense (pre-twist). *"Convince us it's better, not just different."* · *"What's your actual ceiling, not a guess?"* |
| **10:00-15:00** | Pressure-test the models. *"Whose grid is most fragile?"* · *"What single choice does your count depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your recommendation, or not?"* |
| **15:00-20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00-30:00** | The two threads: moving the safe scoreline · the better rule, or the one history picked. |
| **30:00-45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: a rule that changes the tie-break ladder does not remove the incentive for two teams to find a mutually good scoreline; it moves it. Option B cuts the 1-0 gamble from 39 of 49 cells to 29 of 49 and raises the highest-scoring benchmark from 42 of 49 to 45 of 49. The 7.14% (a relative margin: 6.1 percentage points) favors Option A on the ceiling, and that margin is itself fragile: it depends on the 0-6 window and on which scorelines are benchmarks, and under the twist it disappears (ceilings tie) while the averages split. All of that is true at once. Option A is what FIFA actually did; the debrief's open question is whether that makes it the better rule or only the one history picked, and the case does not answer it.

Say plainly what the case says: the case does not claim Option A's own cost (a broadcast slot, fan access) because no source was found, and the tension rests on B's computed side effects and on A leaving a gamble open.

---

## Standards Touched On

**Fundamental Counting Principle · Outcome · Event · Set · Subset · Negative Number · Percent · How to apply the Fundamental Counting Principle to count outcomes · How to find the union and intersection of two sets · How to represent a set relationship using a Venn diagram · How to add with negative numbers · How to convert numbers to percents · How to compare two or more values.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]` is honestly empty.

---

## Facilitator note — sensitivity

This case concerns a real, famous match and real national teams. Keep to the incentive framing: FIFA ruled that no rule was broken, and the case never alleges match-fixing, so do not let the room settle on "they cheated." Algeria's complaint and its elimination are facts; discuss them as the cost of a rule, not as a verdict on any player. The committee scene is constructed (no source documents how the real rule was decided), and the three-point rule came later, in 1994, for other reasons.

**Sensitivity of the margin (facilitator only, do not read aloud).** The ceiling comparison depends on the goal window (MA1). With the window at 0-3 goals per side the two ceilings tie (15 of 16 cells each); at 0-6 Option A's ceiling is lower by 7.14%; at 0-9 it is lower by 19.23%, still inside the 20% cap. With the twist's narrow-Algeria-win fact, the two ceilings tie at 100%. The case discloses this instability in `case.json.sensitivity_disclosure[]` rather than hiding it.
