# Facilitator Guide — A Coach's Dilemma

MS | Heroes Academy | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric:** single-attempt make probability, fouled player's FT% vs. defended shooter's
3PT% · **Margin:** 7.3pp / 15.6% of B — **NOT stable** under a ±50% flex of either compared
percentage (see the Sensitivity note before Lessons Learned).

Legacy source: `source/Y1/Session 1/A Coach_s Dilemma/Guide Notes.docx`. The original Guide Notes
had no timed plan and no authored twist — just an Open, three discussion questions, and a closing
video. This guide preserves the original's real pedagogical finding (see **Lessons Learned**
below) and migrates its Open/Q1/Q2/Q3/Close shape into the current 11-anchor ladder, with a
genuinely new, sourced Twist (the original had none).

---

## Intro

Frame the format: this is a decision under time pressure, and the room will feel that pressure
too. Don't open with the math. Open with the moment: 25,000 people, 4 seconds, a two-point lead.

## Launch

Read the Overview aloud, or better, act it out — pause right where the case does, on Coach
Cavenaugh with his mouth open, no answer yet. Do not show the box score yet.

## Anchor 1 — TAKE A STAND AND VOTE

"Is anyone courageous enough to stand with Option A — foul them?" Cold-call for a vote, no
reasoning allowed yet. Write the split on the board (e.g., "9 foul / 6 defend / 2 unsure").

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to find out here?" Let it get messy — this legacy case's own Guide
Notes record a room spending 15 minutes before landing on the real question: *"Is it more likely
they miss a 2- or 3-point shot, or miss a one-and-one free throw?"* Treat that struggle as the
win, not a delay. If the room lands somewhere close to that framing, name it out loud and move
on; if they land somewhere else entirely (e.g., "which Kansas player is scariest"), that's fine
too — Anchor 3 will pull them back toward a process either way.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had the data, how would we actually decide?" Push for a concrete comparison, not a vibe.
Re-ask Anchor 2's question once a process is on the board: "Given this process, is our question
still the right one?"

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming? Which assumptions are load-bearing?" Surface, without confirming or
denying yet: does a missed free throw definitely end the possession? Does the season percentage
really predict this one shot? Bank these — Anchor 4's questions are exactly what the Twist and
Appendix D's stated assumptions answer.

## Data Deep Dive

Now, and only now, hand out Appendix B (box score) and Appendix C (season stats). Let Heroes work
D1-D2 (the shooting-percentage table and best/worst shooters) before revealing anything about
D3's squaring.

## Twist

**Drop this at roughly the 15-minute mark**, slowly, with pauses — after the room has committed
to a read of D1/D2's percentages but before D3's compound-probability step is worked.

> "One more thing. You've been assuming that if Memphis fouls and the front end of the free throw
> is missed, the possession is over — Memphis wins. That's not the rule. **A missed front-end
> free throw is a live ball.** Either team can rebound it. If Kansas's shooter misses the first
> free throw, Kansas can still crash the boards, grab the miss, and put it back up — no whistle,
> no new foul required, just basketball."

**What this invalidates:** the comfortable version of Option A where "miss the front end = 100%
safe for Memphis." It doesn't invalidate fouling as a strategy (the p² math still holds for the
*clean* two-shot sequence), but it means the true probability Kansas survives the possession is
*higher* than 29.3% once you account for offensive rebounds off a missed front end — a real
factor this case does not ask students to quantify (there's no real data to source a rebound-rate
number from), but one a sharp Hero should now name as a gap in their own model.

**The follow-up (the whole point):** *"What just broke in your model? Were you wrong, or just
missing information?"* Push the room to articulate that D3's 29.3% is a **lower bound on risk for
Memphis** — the true number is higher, but by an amount nobody in the room can compute from the
data they have. This is the transferable skill: recognizing when a clean number is quietly
incomplete.

**Soundness check (SPEC.md §6 / case-write §11):** read sequentially against Appendix D's
Assumptions 1-3 and case.json's MA1-MA4, in order — the Twist doesn't contradict any of them; it
adds a factual rule (sourced S2) that the base model already flags as excluded ("except for the
live-ball-rebound wrinkle in the case's Twist," Appendix D Assumption 2). Read simultaneously —
holding all four assumptions plus the Twist at once — the arithmetic in D1-D4 doesn't change; only
the interpretation of what D3's 29.3% represents (a lower bound, not an exact figure) changes. No
assumption is invalidated by another; the Twist is additive information, not a contradiction.

## Close (10 minutes left)

VOTE AGAIN. "Did we ask the right question? Who's changing their answer, and why?" Ask specifically
who moved *because of the squaring* (D3/D4's trap) versus who moved *because of the Twist*. Those
are two different kinds of "wrong" and worth distinguishing out loud.

Optional: end video, real 2008 NCAA Championship final possession (Kansas vs. Memphis) — see
Appendix A's note on the real game this case is loosely inspired by. Be explicit with students
that the case's own names, score, and stats are invented, even though the real finish is worth
watching.

## Lessons Learned

*(Preserved from the legacy Guide Notes, lightly edited for the anchor-ladder format.)* You may be
faced with a real dilemma that is equally challenging to weed through. There may not be a single
right answer, because there are many variables and the future is entirely unpredictable — but if
you use good logic and thinking, you can at least tip the scales in your favor. This case's own
math is a clean example: the "obvious" comparison (54.1% vs. 46.8%) and the *correct* comparison
(29.3% vs. 46.8%) point in opposite directions. Both numbers are real. Only one answers the
question actually being asked. One more layer for a facilitator to sit with privately: even the
"obvious" 54.1%-vs-46.8% comparison is a fragile 7.3-point margin — flex either player's season
percentage by half and it can flip outright (see the **Sensitivity note** above). Real decisions
built on real, close numbers stay real and close; that is not a flaw to paper over.

## Standards Touched On

See `case.json.standards[]` and the case.md Appendix E "How To…" list — generated mechanically
from `readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. Diego Imor's season free-throw percentage (54.1%) is *higher* than Cooper Charmers' season three-point percentage (46.8%) — a 7.3-percentage-point gap in Imor's favor. If bigger percentages mean better odds, why would fouling Imor ever be the smarter play?
2. You computed a 29.3% chance Kansas ties the game by fouling Imor. What two real numbers did you multiply to get that, and why is multiplying — not adding — the right operation here?
3. If Coach Cavenaugh fouled Fiaro Russle instead of Imor (77.9% season free-throw shooter), what would Kansas's chance of tying become, and would you still recommend Option A?
4. The Twist tells you a missed front-end free throw is a live ball. Does that change your D3 answer (29.3%)? If not, what exactly *does* it change about how much you trust that number?
5. Suppose Memphis led by 3 instead of 2. Kansas's best available shot to win outright would then be a three-pointer worth exactly enough to tie, not win. Walk through how that changes which option you'd recommend, using this case's own Kansas shooting numbers?

## The trap, named explicitly

A Hero compares Diego Imor's single free-throw percentage (54.1%) straight across to Cooper
Charmers' three-point percentage (46.8%) and concludes Option B (defense) is the better play,
since the number defense "allows" is smaller. This is the plausible reasoning that produces a
confident wrong answer: the free-throw route requires **two** successful shots, not one — the
correct comparison squares Imor's percentage first (p² = 29.3%), which flips the recommendation
hard toward fouling. Facilitators should let a room reach the wrong conclusion out loud before
D3/D4 corrects it; that reversal is the case's real payoff.

## Sensitivity note

Sports-strategy probability case, no illness/death/money-stress/family-hardship content — no
SPEC.md §6 flag required on that front. One disclosure facilitators should be ready for: this case
is fiction (see case.md Appendix A and case.json's `legacy_conversion_note`). If a student asks
"did this really happen," the honest answer is: the coaching dilemma is real and famous (2008 NCAA
Championship, Kansas over Memphis in overtime), but this case's coach, players, score, and season
are invented for the exercise.

**Assumption-sensitivity disclosure (required reading before you defend the 7.3pp margin):**
The case's graded primary metric — Diego Imor's season free-throw % (54.1%) vs. Cooper Charmers'
season three-point % (46.8%), a 7.3-point / 15.6% margin — is **not stable** under a ±50% flex of
either number (`cases/a-coachs-dilemma/sensitivity_model.py`, Tier 2 probe 5). Flexing Imor's FT%
down 50% (to 27.05%) **flips the recommendation to Option B**, by a wide 73.0% margin; flexing it
up 50% (81.15%) keeps Option A but by 73.4%, which itself breaks the SPEC §2 20% balance cap.
Flexing Charmers' 3PT% up 50% (70.185%) **also flips the recommendation to Option B** (29.7%
margin, over the cap); down 50% (23.395%) keeps Option A but by 131.2%. In short: this is a close,
debatable margin only at the case's own real, given numbers — nudge either shooter's percentage by
half and the "obvious" comparison stops being close, and can even reverse.

This is a genuine, permanent finding, not a modeling bug: both flexed values are the case's real,
internally-consistent Appendix C season stats (verified byte-identical to the original legacy
workbooks), and there is no other stated numeric assumption behind this comparison to retune
honestly — adjusting Imor's or Charmers' percentage to "fix" the sensitivity would mean inventing
data the case does not have. Per this project's own doctrine (`DOCTRINE_LEDGER.md` MCS-26/MCS-41),
a disclosed-but-unstable sensitivity does **not** earn a pass on probe 5 — disclosure is the
requirement, not elimination, and probe 5 stays a mechanical FAIL. If a room pushes hard on "what
if Coach fouled someone else, or Kansas's shooter were colder/hotter that night," that pressure is
legitimate — name it as a real, open limitation of comparing two single fixed season percentages,
the same way Cold Chain (this project's own flagship case) discloses its own unresolved P5 FAIL
rather than claiming a stability the numbers don't have.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read/acted aloud), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just fair" (Anchors 2-3, define the real question and a process) |
| 10:00-15:00 | Pressure-test the models: "Whose plan is most fragile?" — hand out Appendix B/C, let D1-D2 develop |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict: (1) the single-shot-vs-compound trap (D3/D4), (2) risk severity — a foul caps the downside at a tie, defense risks an outright loss, (3) how much the Twist's unquantified rebound risk should actually move anyone's confidence |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands
declared per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
