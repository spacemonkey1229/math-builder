# Facilitator Guide — Cinema

MS | Heroes Academy | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric:** opening-weekend (Thu-Sun) net profit from the two major releases combined ·
**Margin:** 2.86% (Option B, The Revengers House, wins) — **STABLE** under a ±50% flex of the
case's one genuine assumption (see the Sensitivity note before Lessons Learned).

Legacy source: `source/Y2/Session 7/Cinema/Guide Notes.docx`. The original Guide Notes' twist (a
burst pipe damaging "two entire theaters") was written against an earlier draft of the case with
a different theater count than the one this conversion ships — the guide's own Lessons Learned
says the dilemma and stats were revised afterward without going back to reconcile the twist, so it
is not reusable as-is (see case.json's `legacy_conversion_note`). This guide migrates the
original's real Open/Anchor1-4/Data-Deep-Dive/Close shape into the current 11-anchor ladder and
authors a new twist, checked for soundness against this conversion's own numbers below.

---

## Intro

Frame the format: Emily has one big room and two movies that both deserve it. Don't open with the
spreadsheet. Open with the moment — the blinking cursor on an empty showtime grid, an email she's
already read twice.

## Launch

Read the Overview aloud. Stop exactly where the case does — Emily staring at two folders, no
decision made yet. Don't hand out Appendix A/B until Anchor 4.

## Anchor 1 — TAKE A STAND AND VOTE

"Is anyone courageous enough to stand with The Unicorn House — give the big room to Lizzie?" Cold
call for a show of hands, no reasoning allowed yet. Write the split on the board.

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to find out here?" Let it get messy. A likely wrong first framing:
"which movie is more popular" (pulling on review score, which never enters Majesty Cinemas' own
attendance data — see Modeling Assumption D-3). Let that sit uncorrected for now; Anchor 3 and the
Data Deep Dive will surface it. If the room converges on something like "which plan makes Majesty
Cinemas more money this weekend," name it and move on.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had the numbers, how would we actually decide?" Push for a concrete comparison — revenue
per showing? Cost per showing? Total for the weekend? Re-ask Anchor 2 once a process is named: "Is
our question still the right one, now that we have a process?"

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming?" Surface without confirming: does a movie always fill the theater the same
percentage regardless of which movie it is? Does Majesty Cinemas run extra showings if a slot
looks profitable, or only the contractual minimum? Bank these — Appendix D's stated assumptions
answer exactly these questions once the Data Deep Dive begins.

## Data Deep Dive

Now hand out Appendix A (contracts), Appendix B (operating data), and Appendix C (the complex).
Let Heroes work D1-D2 (the master schedule and daily showing counts) before anyone starts D3's
revenue math — building the actual schedule is where the "Revengers needs 5 showings but can't
fit all 5 in one theater" discovery lives, and it should land before the money conversation, not
after.

## Twist

**Drop this at roughly the 15-minute mark**, slowly, after the room has committed to a read of the
D3-D5 revenue numbers but before anyone has finished a full recommendation.

> "One more thing. A follow-up email just came in from the distributor. Turns out the contract for
> both major releases includes a 'flagship placement' marketing co-op clause: whichever release
> gets the big 150-seat room satisfies that clause automatically. Whichever one gets confined to
> the smaller theaters instead — Majesty Cinemas owes the distributor a **$50 co-op fee on every
> one of that movie's small-theater showings**, all weekend."

**What this changes:** the fee lands on whichever movie is confined to small theaters, in either
plan — it doesn't structurally favor one plan over the other by design. But the two confined
movies aren't symmetric: The Revengers needs 5 daily showings against Lizzie's 4, so if Revengers
is the one confined (Option A), it's exposed to more fee-bearing showings all weekend than Lizzie
would be if the roles were reversed (Option B). Recomputed with the fee applied
(`sensitivity_model.py evaluate_twist()`), the margin moves from 2.86% to a wider 3.21%, still in
favor of Option B — the fee makes Option A's cost side worse than Option B's, on top of Option
B's already-existing edge.

**The follow-up (the whole point):** *"What just broke in your model? Was your D5 answer wrong —
or was it right given what you knew, and now you know more?"* The winner doesn't flip here — push
the room to notice that instead: *"If new information showed up and your answer didn't change,
was your original reasoning already accounting for something like this, or did you just get
lucky?"* A room that argued for B purely on cost-per-showing should recognize the twist as their
own argument getting a second, independent confirmation from a completely different angle.

**Twist Soundness Check (SPEC.md §6 / case-write §11).** Read **sequentially** against Appendix
D's Assumptions D-1 through D-5 and case.json's MA1-MA5, in order: the twist adds a new cost term
on top of D-5's "run at contractual minimum" schedule — it does not touch D-1 through D-4 at all
(the five-slot revenue model, matinee/standard pricing, uniform capacity, and the concession
estimate are all unaffected), and it composes cleanly with D-5's showing counts (which is exactly
what "5 daily showings" and "4 daily showings" are used for in `evaluate_twist()`). Read
**simultaneously** — holding all five assumptions and the twist at once — nothing contradicts:
D-1's five-slot model still determines how many small-theater showings each confined movie runs
per day, D-5 still fixes those counts at the contractual minimum, and the twist's fee is a flat
per-showing cost added afterward, not a recomputation of revenue. There is no reading, sequential
or simultaneous, under which the twist produces an undefined or contradictory result — verified by
running `evaluate()` then `evaluate_twist()` on the same `PARAMS` dict and confirming both return
well-formed `{"A":.., "B":..}` dicts with the same relative ordering of terms.

## Close (10 minutes left)

VOTE AGAIN. "Did we ask the right question? Who's changing their answer, and why?" Ask
specifically who moved because the D3-D5 arithmetic surprised them versus who moved because of
the twist. Different kinds of "wrong," worth naming out loud.

## Lessons Learned

*(New for this conversion — the legacy Guide Notes' own Lessons Learned describe a case that
never resolved its dilemma/stats revision, so nothing from the original carries forward here
directly.)* This case's real lesson is about what data a decision actually depends on. Majesty
Cinemas' own attendance-capacity numbers (Appendix B) don't care which movie is playing — only
seats, time slot, and day of week move the needle. A Hero who reaches for review score or runtime
as "obviously" the deciding factor is reaching for real, printed numbers that are nonetheless
irrelevant to this specific decision. Noticing that a real number doesn't belong in a calculation
is exactly as much a math skill as computing correctly with the numbers that do.

## Standards Touched On

See `case.json.standards[]` and `case.md` Appendix E's "How To…" list — generated mechanically
from `readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. The Revengers costs $220 per showing and Lizzie costs $325 — a real gap on every single showing, all weekend. Why doesn't that gap alone settle the decision?
2. Lizzie needs only 4 daily showings against The Revengers' 5. Walk through which single slot Lizzie skips each day, and why skipping it, rather than any other slot, is the right call?
3. The Revengers has the higher review score (9.6/10) and the longer runtime. Does either fact appear anywhere in your D3-D5 arithmetic, and if not, why does it feel like it should?
4. You built a full weekend schedule in D1. Is there a single theater, on a single day, where The Revengers' own 5-showing requirement fits without help from a second theater, and what does that tell you about "The Revengers House" as a plan, beyond the money?
5. The twist added a $50-per-small-theater-showing fee to whichever movie is confined. Recompute both plans' weekend totals with that fee applied — did the winner change, and should that surprise you given what you already knew about the two movies' showing counts?

## The trap, named explicitly

Most Heroes will lean on The Revengers' higher review score (9.6/10 vs. 8.4/10) and longer runtime
and quietly assume it obviously "deserves" the big room — without ever running the actual cost-per-showing
and slot-count arithmetic Appendix B's attendance data forces. Review score never enters Majesty
Cinemas' own attendance-capacity table at all (Modeling Assumption D-3) — it's real, printed data,
and it's irrelevant to this specific decision, which is exactly why it's tempting to reach for.
The second half of the trap is D1's own discovery: a Hero who doesn't check the cleaning-turnaround
math will build a schedule that looks fine on paper and is not actually physically buildable — The
Revengers' long runtime means it structurally cannot fit all 5 of its required daily showings
inside a single theater, of either size.

## Sensitivity note

A scheduling-and-revenue case with no illness/death/money-stress/family-hardship content — entire
scenario is fictional (Majesty Cinemas, Emily Carlin, and all six films are invented; see
case.json's `legacy_conversion_note`). No SPEC.md §6 flag required.

**Assumption-sensitivity disclosure:** the case's graded primary metric (opening-weekend net
profit, Option A vs. Option B) is **stable** under a ±50% flex of the case's one genuine, stated
assumption — the representative dollar value assumed for the open-ended "more than $40" concession
band (Modeling Assumption D-4, `sensitivity_model.py FLEX`). Flexing that estimate from $50.00
down to $25.00 or up to $75.00 changes both plans' totals but leaves the margin at 2.86% and the
winner (Option B) unchanged in both directions (`cases/cinema/sensitivity_model.py`, Tier 2 probe
5). Every other number this case's arithmetic depends on is Appendix A/B/C given data, not an
author-stated assumption, so it is not swept by probe 5 by design (only assumptions are, per
house doctrine) — but a facilitator should be ready for a room that asks "what if attendance were
different" or "what if the cost per showing changed," which is a legitimate question about *cited*
data robustness, better answered by pointing at Appendix A/B directly than by re-running the
sensitivity model.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read aloud), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchors 2-3, define the real question and a process) |
| 10:00-15:00 | Pressure-test the models: hand out Appendix A/B/C, let D1-D2 develop (the master schedule and showing counts) |
| **15:00** | **DROP THE TWIST** — delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: does anyone reverse? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict: (1) the review-score/runtime trap (D3-D5's real arithmetic vs. the tempting-but-irrelevant numbers), (2) the D1 scheduling discovery (Revengers can't fit in one theater), (3) whether the twist's confirmation of Option B should make anyone MORE confident, or whether that's a trap of its own |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands
declared per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
