# Guide Notes: LeBron vs. Michael

**Case:** LeBron vs. Michael · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (8 skills — percent, mean, box-and-
whisker/quartiles, and comparison)

Legacy conversion, 2026-08-02, built from the original case study docx and its real career-log
workbook (`source/Y3/Session 7/LeBron Vs. Michael/`). Every number in this case is a real,
publicly verifiable NBA statistic — no cost data or disclosed modeling convention had to be
invented, only a stated methodology for how "career average" is calculated (Appendix E).

**Correction, 2026-08-04:** LeBron James's "Year 18" data (originally 25.6 ppg, 246 assists) was
an undisclosed partial-season snapshot, not his real completed 2020-21 season — see
`case.json.correction_2026_08_04` for the full account and sources. Every LeBron number in
Appendix A, B, C, and D has been corrected and is now frozen at the real end of his 18th season
(Appendix E, Assumption 6), since he is still an active player. One consequence worth knowing
before you run this: the playoffs-only Twist below no longer flips the leader on the graded
3-point metric — with real data, LeBron leads it both before and after the twist. The twist
section below has been rewritten to reflect that honestly.

## Intro

Frame the format: this is a real, ongoing sports debate with real numbers behind it, not a
worksheet. Name the opener — "Two of the greatest careers basketball has ever seen. One magazine
cover. Your editor already thinks he knows the answer."

## Launch

Read both players' real championship counts aloud (4 for LeBron, 6 for Jordan) with no other
numbers yet. Ask: "Just from that, does this look like a settled question to you?" Do not confirm
or correct answers here.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who puts LeBron on the cover? Who puts Jordan?" Show of hands, no discussion. Record the count —
Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do we need to consider in order to decide?"**

Push on what "greatest" even means: efficiency, longevity, team success, all-around production,
dominance relative to era — these are all real, different, defensible lenses. A room that jumps
straight to "just add up championships" hasn't actually decided what it's measuring yet.

## Anchor 3 — What is the process?

**"Do we consider all of these factors, focus on 2-3, or focus on only one? Which one(s)?"**

Once the room has picked its deciding factor(s), ask them to name the actual steps: career
shooting percentages from real makes/attempts, games-weighted means for assists and rebounds, the
same five stats for the playoffs, and a box-and-whisker plot of one player's points-per-game across
his whole career. Re-ask: "Do we agree that's the right process for the factor(s) we picked?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the two real conventions: career percentages/means are computed career-wide (total
makes/total attempts, total stat/total games), not by averaging each season's own number, and
Appendix C lines the two careers up by career year instead of calendar year so Jordan's real
mid-career retirement doesn't misalign the comparison. Ask which one actually matters more to the
final numbers.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's career-wide percentage calculation and D2's
games-weighted mean together as a room, cold-calling for the "why not just average the season
percentages" question specifically — this is where a Hero who averages season-by-season numbers
instead of career totals will get a real, subtly wrong answer that still looks plausible.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Robert calls again. 'One more thing — I want the cover to reflect who was better in the games that
actually mattered. Playoffs only.'"

**Facilitator-only.** This is a genuine recompute using Appendix B's real playoff data instead of
Appendix A's regular-season data (D3), not a new invented number. Ask: "Does switching to playoff
numbers change your recommendation, or does it mostly change which argument feels stronger?" A Hero
who anchored on regular-season 3-point percentage has a real, harder question: Jordan's playoff
free-throw percentage stays dominant, and LeBron's playoff rebounding stays far ahead — do the same
stats that mattered in the regular season still matter the same way in the playoffs?

**The graded 3-point metric itself does not flip here** — LeBron leads it both before the twist
(34.49% vs. 32.68%) and after (33.88% vs. 33.78%). That is itself worth putting to the room: "The
twist changes the numbers but not the winner on this one metric — does a twist have to flip an
answer to be worth taking seriously, or is confirming a real conclusion under new data still a real
result?" Don't manufacture drama the real numbers don't support; the honest tension here is in the
*other* stats the twist touches (free-throw%, rebounding), not in a reversal that isn't there.

Do not hand over a "correct" answer — this is a real, ongoing debate with reasonable people landing
on both sides.

## Immediate recommit

Re-vote immediately. Ask by name: "Did the playoff numbers change your recommendation, or did they
just change what argument you'd lead with?"

## Deep conflict — three threads (20-30 min)

1. **Efficiency vs. volume vs. team success.** LeBron edges Jordan in 3-point percentage and both
   per-game means; Jordan edges LeBron in free-throw percentage, scoring titles, and real
   championships. Does any one of these get to be "the" deciding stat, or does the answer depend on
   what a GOAT debate is actually supposed to measure?
2. **Different eras, different games.** LeBron played his whole career in an era that shoots far
   more 3-pointers league-wide than Jordan's era ever did. Does that make LeBron's 3-point edge more
   impressive, less impressive, or just not comparable at all?
3. **What a self-designed algorithm can and can't settle.** Every Hero's D5 algorithm is real math
   applied to real data — but the choice of which 3+ stats to weight, and how heavily, is a real
   value judgment. Does that make the algorithm more persuasive than a gut opinion, or just a more
   precise-looking version of the same opinion?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read both championship counts aloud, cold-call for a gut read, no other numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your player is the GOAT using more than just a highlight reel memory"* |
| 10:00–15:00 | Pressure-test the models — *"Which stat is actually deciding your vote, and why that one?"* |
| **15:00** | **DROP THE TWIST** — playoffs-only, delivered slowly |
| 15:00–20:00 | Immediate recommit — did playoff numbers change anyone's answer |
| 20:00–30:00 | Threaded deep conflict (efficiency vs. volume vs. team success; different eras; what an algorithm can settle) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes one or two favorable stats for their preferred player, builds an algorithm that
happens to weight exactly those stats most heavily, and never engages with the real numbers that
cut the other way. The case's actual tension is that BOTH players have real, genuine statistical
advantages depending on what you choose to measure — a persuasive pitch has to acknowledge the
stats that don't favor its own conclusion, not just the ones that do.

## Socratic questions

1. LeBron's career 3-point percentage is a real 5.54% higher than Jordan's — how much should that matter for a player whose era barely attempted 3-pointers at all?
2. Jordan won every Finals he ever reached — does a perfect Finals record matter more than a larger sample of near-misses across a longer career?
3. Your own algorithm is real math, but you chose which stats to include and how to weight them — what would have to change about your algorithm to make it favor the other player?
4. LeBron's real games-weighted rebound average is about 20% higher than Jordan's — for a debate about "greatest," does a rebounding gap matter as much as a scoring or efficiency gap?
5. If Jordan's real career had also lasted 18 seasons instead of 15, do you think his career percentages would have gone up, down, or stayed about the same — and why?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't move at
all after the twist is worth asking about directly: did playoffs-only not feel like a real factor,
or did the room already treat the regular season as the fairer, larger sample?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the career-wide percentage calculation (D1) or the box-and-whisker plot (D4) was the
  place most Heroes actually got stuck.
- Whether Heroes anchored on efficiency stats or counting/team-success stats as their real deciding
  factor, and whether that split along any pattern.
- Whether the playoffs-only twist changed votes or just changed the stated reasoning behind an
  unchanged vote.

## Standards Touched On

Percent · Mean · Box And Whisker Plot · Quartiles · How to convert numbers to percents · How to
find the mean of a set of data · How to create a box and whisker plot given a set of data · How to
compare two or more values
