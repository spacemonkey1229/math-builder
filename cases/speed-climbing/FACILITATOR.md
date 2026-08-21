# Guide Notes: Speed Climbing

**Case:** Speed Climbing · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for exact ids (14 skills — mean, median, range,
outlier, percent-of-a-number, decimal arithmetic, ranking/comparison, bar graph, scatter plot)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 1/Speed Climbing/Case Study_ Speed Climbing.docx` and `Guide Notes.docx`) onto
the current 11-step anchor ladder. The twelve climbers, their timed data, and Coach's Notes are
preserved verbatim from the source; the open six-option philosophy prompt is locked to the two
real camps per `cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md`. See
`case.json.legacy_conversion_note` for the full account.

**A note on sensitive content (SPEC §6):** this case touches a learner's family hardship (Kylie's
parents' divorce) and a veteran athlete's declining performance (Ava). Keep the discussion on the
disclosed numbers and Coach's Notes as written — do not invite Heroes to speculate about the
climbers' real lives beyond what's on the page, and do not let "Kylie's focus problems" become a
stand-in for a Hero's own family situation in discussion.

## Balance Argument (facilitator-only — never in case.md)

**Argument for A (pure speed):** Selecting the eight fastest official times produces a combined
team-composite score of **30.82** (units: seconds) across both teams — the mathematically lowest
score this pool of twelve can produce, full stop. Every other roster is slower by construction. If
the goal really is maximizing the odds of a podium finish, this is not a close call mathematically;
it's the optimum.

**Argument for B (character/leadership):** A reference character-and-leadership roster (built from
Appendix C's coaching notes using the rubric below) lands at **32.03** combined (also seconds) —
only 3.9% slower than the mathematical optimum. Six of the twelve athletes make the team under *either*
philosophy. The entire dilemma comes down to two swing seats: Option A replaces both team
co-captains' presumed continuity with Rebecca and Jane (Rebecca has real ceiling and zero team
friction concerns baked into the metric; Jane is unproven but fast); Option B keeps Ava and
Victoria over Rebecca and Jane. For roughly one second of combined team time, Option B keeps both
co-captains on the roster and rewards the two climbers on the steepest *upward* trend
(Gertrude +23.3%, Jane +21.8% over six months) that Option A's snapshot-in-time metric doesn't
weight at all.

**The margin: 3.9%**, Option A faster. This is close enough that a genuinely defensible pitch can
be built for either side — see SPEC §2's 20% cap; this case sits comfortably inside it, and the
smallness of the gap is itself the point of the discussion.

## Facilitator's reference character/leadership rubric (NOT published to students)

This is the facilitator's own worked model for Option B, used only to verify the balance test and
to run Tier 2 probe 5 (`sensitivity_model.py`). Students are asked to build their *own* rubric from
Appendix C (Appendix F, MA3) — do not hand this table to a Hero.

Points, from Coach's Notes only: **captain/leadership role** +2 · **explicit mentor of younger
climbers** +1 · **selected by teammates as most trusted (survey)** +2 · **perfect practice
attendance / discipline** +1 · **3+ years experience** +1 · **has competed at Nationals (team or
individual)** +1 · **explicit team-morale-booster note** +1 · **explicit team-friction note
("difficult to work with," "creates tension")** −1. Personal hardship (Kylie's family situation) is
never scored, in either direction — deliberately, per SPEC §6.

| Climber | Score | Climber | Score |
|---|---|---|---|
| Ava | 6 | Gertrude | 1 |
| Kylie | 5 | Emily | 1 |
| Leslie | 4 | Sky | 1 |
| Jesse | 2 | Amara | 1 |
| Victoria | 2 | Jane | 0 |
| — | — | Gigi | 0 |
| — | — | Rebecca | −1 |

Top 8 by score, ties broken by faster official time: Ava, Kylie, Leslie, Jesse, Victoria, Emily,
Sky, Gertrude.

## Five Socratic Questions

1. Six of the twelve athletes make the national team no matter which philosophy you use — the whole argument comes down to two seats. Which two, and what does each philosophy actually buy you for giving those seats to a different pair of climbers?
2. Your combined team-composite score under Option B is only about 3.9% slower than the mathematical optimum — is a 3.9% chance-of-winning cost worth what Option B claims it buys?
3. Appendix A ("today's selection trial") and Appendix B ("Best Practice Climb Time") don't rank the twelve athletes the same way. Which one did you use to build your roster, and why is that the right one under Appendix D's rule?
4. Gertrude and Jane are trending faster than anyone else on the team (roughly +23.3% and +21.8% over six months) but neither has ever competed, while Ava is a four-year veteran whose times are trending the opposite direction. What does "long-term development" actually mean if it doesn't account for direction of travel, not just current speed?
5. If you'd used each climber's single fastest time ever recorded, instead of her most recent month, would your roster change — whose spot would move, and does that change which philosophy you'd defend?

## Intro

Print and post the twelve athlete names on the whiteboard (Appendix C). Frame the format: this is a
real selection dilemma, not a worksheet with a story stapled on. Name the opener — "Twelve real
climbers. Eight roster spots. You're the coach, and you have to decide what 'best' even means before
you can pick anyone."

## Launch

Read the Overview aloud. Optionally show a short real speed-climbing clip so the room has seen the
15-meter wall before discussing it (Appendix E has the real-world grounding — wall height, current
world records — if anyone asks "how fast is actually fast?"). Ask: "If you were Coach Chen, what
would you want to know before picking anyone?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Pure speed, or character and development?" Show of hands, no discussion yet. Record the count —
Close asks again. "Is anyone courageous enough to stand alone on this?"

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'best'?"**

Push on what "best roster" even means. Fastest right now? Most likely to still be fast in three
years? Best for the twelve individuals, or best for the two teams as scored? Let the room sit in the
ambiguity: "Wow, this is a harder question than 'who's fastest' sounded a minute ago."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "best," ask them to name the actual steps: rank by
what time, using what data, split into teams how? Re-ask: "Given how we just defined 'best' — is
that still the right process?" (Facilitator note: this is exactly the anchor the original guide's
own Lessons Learned wished they'd spent more time on — don't rush past it.)

## Anchor 4 — What don't we know?

**"Do we need to make any assumptions? Which ones are critical?"**

Surface Appendix F's three Modeling Assumptions as a group, out loud, before anyone computes
anything — especially MA1 (which time counts as "official"). Ask which one the room thinks matters
most before they've done any math. That's exactly what the Trap below is built to test.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's roster-building process together as a room, using
Appendix D's stated rules.

## The Trap

**Appendix A vs. Appendix B.** The case's own Appendix D states clearly that the *official*
selection time is Appendix B's "Best Practice Climb Time" (most recent month), not Appendix A's
"today's selection trial." But Appendix A is titled "Today's Selection Trial Results" and sits
first in the document, right where a skimming Hero expects to find "the" data — and it produces a
dramatically different, wrong ranking. Under Appendix A alone, Kylie (a single lucky 6.89s among
two runs over 13 seconds) and Jesse (a similarly wild 6.99s) look like the two fastest climbers in
the gym; under the correct Appendix B metric, they rank 5th and 6th. A Hero who builds D1's roster
from Appendix A instead of Appendix B has built a roster driven by two outlier flukes rather than
sustained performance — and it happens to be the exact scenario D3 (the consistency/range
deliverable) is designed to catch, if they do that work honestly. Cold-call on this directly: "Which
table did you rank by — and what does Appendix D actually say to use?"

## Twist — drop this at roughly the 15-minute mark, mid-Data-Deep-Dive

Deliver slowly:

"One more thing. During a practice run this week, Kylie slipped and bruised her knee hard enough
that she can't compete at Nationals. She's off the roster. Who takes her place — and does the rest
of your roster change with her?"

**Facilitator-only.** Recompute live with the room, under whichever philosophy the room chose:

- **Under Option A**, Kylie was Team 1's third competitor (8.22). Team 1's own alternate, Jane
  (8.47), moves up. New Team 1 composite: 15.18 (up from 15.10). New combined total: **30.91**
  (barely moved, +0.27 percent).
- **Under Option B**, Kylie was Team 2's second competitor (8.22). Team 2's own alternate,
  Victoria (8.70), moves up. New Team 2 composite: 16.78 (up from 16.31). New combined total:
  **32.50** (+1.47 percent).
- **New margin: 5.16%**, Option A still faster, but the gap widened.

Neither roster flips winner — but the *finding* is real and worth naming: **the pure-speed roster's
bench is deeper.** Its alternate (Jane, 8.47) is much closer in time to its departed starter than
Option B's alternate (Victoria, 8.70) is to hers. This is a legitimate quantitative point *against*
one popular Option-B claim ("character-based teams handle adversity better") — the twist shows the
opposite, on this specific metric, for this specific injury. It does not resolve which philosophy
is "right"; it complicates whichever one the room committed to.

**Twist soundness check (SPEC §6):** re-derived under every stated Modeling Assumption
(MA1's official-time definition, MA2's seeding rule) read both sequentially and all-at-once — holds
under both; no unstated convention is required for the recompute, since Appendix D's alternate rule
was already fixed before the Twist lands.

Ask: "Sixty seconds. Does this change your roster, or not?" Then: **"What just broke in your model
— was your alternate a real backup plan, or a name you never expected to actually need?"**

## Immediate Recommit

Re-vote immediately after the recompute. "Did the injury change your pick of philosophy — or just
force you to actually use the alternate you'd already written down?"

## Close

Vote again after full discussion. Ask: "We started by asking 'who's fastest' — was that ever really
the right question?" And: "What math was new to you today, and how did you attack it?"

## Lessons Learned

*(Migrated and extended from the original Guide Notes.)* The original guide's own reflection was
that "the math for this case study was not complicated, but how to use it and what the right
question to ask were the key" — that observation drives this conversion's entire structure: the
math (mean, median, range, percent change) is genuinely MS-level, but which table you rank by,
which time window you trust, and how you turn qualitative coaching notes into a defensible number
are the actual skill being taught. The original guide also noted wishing they'd asked more
process-reflection questions ("is that the right process?") before results landed — the Anchor 3
question below is built directly from that gap.

## Standards Touched On

See `case.json.standards[]` (14 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: mean, median, range, and outlier (team scoring and consistency analysis);
percent-of-a-number (six-month trend); decimal arithmetic (every climb time); ranking/comparison
(roster selection); bar graph and scatter plot (the two required visual displays).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–3 run as written; the room splits into a "pure speed" faction and a
  "character and development" faction before the Twist forces both to recompute live.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D5's two visual displays are worked as
  one shared example (one philosophy) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever philosophy
  the Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just faster" |
| 10:00–15:00 | Pressure-test the models: "Which table did you rank by — and is that the right one?" |
| **15:00** | **DROP THE TWIST** — Kylie's injury, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) current speed vs. trend direction as competing definitions of "who's actually faster"; (2) team score (mean+median) vs. individual fastest climber as competing definitions of "good roster" |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
