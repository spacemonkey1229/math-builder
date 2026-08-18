# FACILITATOR.md — Casino Owner

Authored new for this legacy conversion (no `Guide Notes.docx` accompanied the source file — see
`case.json.legacy_conversion_note`). Written to SPEC.md's eleven-anchor ladder (Facilitator
Artifacts section).

---

## Argument for A (Indigo card tables)

Under Appendix E's peak-hours assumption (MA1), the four Indigo tables' high-dollar pots
produce a substantially larger weighted-average rake per game (case.json.derived:
$137.76–$211.01 per game across the three tiers) than any single video machine's blended
profit per play, even after Indigo's slower pace (case.json.derived: 2.59–3.99 games per hour
per table, vs. over 200 plays per hour per machine) and its per-table dealer wage are subtracted
out. The dollars moving through a single Indigo hand simply dwarf a $0.50–$2.50 machine bet —
D1/D2 make this comparison concrete tier by tier.

## Argument for B (Video machines)

Video machines need no specialized staff to open at all — no dealer to hire, certify, or
schedule — and 25 of them can run at once against only 4 Indigo tables, with volume (200+ plays
per hour per active machine) partly closing the per-unit gap. Fixed labor cost is also much lower:
2 security staff cover the *entire* room regardless of machine count, versus one paid dealer for
*every* Indigo table. D3/D4 force this side to be worked with the same rigor as A, not asserted.

## The margin

Computed from D4 under Appendix E MA1–MA3, using `sensitivity_model.py`'s `evaluate(PARAMS)`:
Option A (Indigo) projects a peak-hours weekly profit of $190,472.64; Option B (Video) projects
$162,372.05 — Option A wins by **17.31%** (`case.json.balance.margin_pct`). Close enough, on the
peak-hours-only reading, to be genuinely worth a room's debate — and, per the Twist below, fragile
enough that a single real-world staffing fact reverses it. Do not print this number to students
before the discussion.

---

## Intro

Frame the format for the room: Emilia has two days to recommend one game for a brand-new room,
and the room will decide the same way she has to — with a firm pitch, defended live. Name the
opener: "You have a two-day deadline and no historical revenue for either game. What do you do
first?"

## Launch

Read the Overview aloud (or project it) through the moment Emilia opens a blank note — stop
there, before any appendix is shown. Ask for a first reaction: "Which game does your gut say,
before you've seen a single number?"

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.** "Is anyone courageous enough to stand
with Indigo? With the video machines?" Record the room's initial split — you will return to it
at the Close.

## Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?** "Is 'which game earns more in a week' really the whole
question, or is it 'which game earns more, under what assumptions about when the room is open and
how it's staffed'?" Let confusion grow here rather than resolving it — "Wow, this is a harder
question than it looked."

## Anchor 3

**WHAT IS THE PROCESS?** "If we work out Appendix A–D and find real numbers, how exactly will we
decide?" Re-ask Anchor 2's question once the room has an answer: "Is 'which earns more in a week'
still the right question, now that you've said out loud how you'd compute it?"

## Anchor 4

**WHAT DON'T WE KNOW?** "Appendix C tells you how busy the room gets by hour — does it tell you
which hours the room is even *open*? Do we need to assume that? Is it a critical assumption?" This
is where MA1 (the peak-hours assumption) should surface from the room itself, before you confirm
it's the one the case uses.

## Data Deep Dive

Now, and only now, the numbers: work D1–D4 together or in small groups, using Appendix A–E. This
is where the Working Notebook in the published interactive case earns its keep — Steps 1–3 there
walk the same arithmetic this deliverable set requires.

## Twist

**What breaks:** Appendix A states plainly that "the casino does not have any Indigo tables
currently" and that "each Indigo table requires a trained dealer." Indigo is an entirely new game
to The Landmark — it has never run a single table before. At the moment of the drop, the
facilitator reveals: *The Landmark currently has exactly two dealers certified to run Indigo — the
other two tables would sit empty, unstaffed, until new hires are trained and certified, which will
not happen before opening night.*

Recomputed with `indigo_tables_staffed = 2` instead of 4 (`sensitivity_model.py`'s
`evaluate_twist()`), Indigo's peak-hours weekly profit is cut roughly in half while the video
machines' number is completely unaffected — flipping the recommendation to Option B. "What just
broke in your original model? Were you wrong, or just missing information?" is the follow-up —
the Hero's Appendix A→D4 arithmetic was correct; a real-world staffing constraint the case never
hid, just never called out as load-bearing, changes which option that arithmetic favors.

**Soundness check — does the twist survive every stated reading of the assumptions?**

- *Sequential reading* (a reader works Appendix E in order, MA1 → MA2 → MA3, before reaching the
  Twist): MA3 states the room is modeled at its "full stated maximum build-out (4 Indigo tables...
  since no other capacity figure is given in Appendix A or B)." The Twist does not contradict
  MA3 — it *installs* 4 tables (the room is still built to capacity) but only *staffs* 2 of them
  at launch, a distinct fact MA3 never addresses (MA3 is about how many units are **built**, not
  how many are **staffed**). No conflict.
- *Simultaneous reading* (a reader treats MA1–MA3 as one combined constraint set, applied all at
  once): the same distinction holds — MA1 (hours open) and MA3 (units built) say nothing about
  dealer staffing levels, so a reader who applies all three assumptions at once still has no basis
  to assume all 4 tables are staffed; the base case (`indigo_tables_staffed = 4`) is itself an
  additional, separate assumption the case makes only implicitly until the Twist names it. This is
  intentional: the Twist's whole pedagogical point is that "built" and "staffed" quietly got
  conflated in the base model, and Appendix A's own words were the tell all along.
- Checked against `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()`: with every other
  `PARAMS` value held at its stated base, `indigo_tables_staffed = 2` is the *only* change the
  Twist makes, and it flips the winner from A to B (case.json.balance.margin_pct = +17.31% for A
  in the base case; case.json.derived.twist_margin_pct_video_over_indigo = +70.49% for B once the
  twist is applied) — a genuine flip, not a magnitude change in the same direction.

## Close

**VOTE AGAIN.** Who reversed from Anchor 1? "Did we ask the right question at the start, or did
it change along the way?" Ask directly: "What math was new to you today, and how did you attack
it?"

## Lessons Learned

The recurring lesson in this case is that "built" and "staffed" are not the same claim, and a
model can be arithmetically perfect while quietly assuming the friendlier of two readings without
saying so. A second, smaller lesson: unit count (4 tables vs. 25 machines) is not the same
quantity as dollars per unit, and confusing the two is the case's other named trap.

## Standards Touched On

Percent · Decimal · Multiplication · Division · Mean (weighted average) · Ratio · Bar Graph ·
Probability (odds-to-probability conversion) · unit and compound-unit rate conversion · comparing
two or more values. See `cases/casino-owner/case.json.standards[]` and Appendix F of `case.md` for
the full verbatim spine list.

---

## Five Socratic questions

1. Your D1/D2 numbers say a single Indigo table brings in real money at a fairly slow pace, and your D3 number says a single video machine brings in almost nothing per play but very fast — which of those two facts matters more once you multiply out to a full room?
2. Appendix E's MA1 assumes the new room only opens 16:00–04:00 — what does your D4 total look like if Mr. Paseronopolis insists the room run 24 hours a day instead, and does the winner change, or just the size of the gap?
3. Every dealer wage and pot-rake figure in Appendix A is given data, not something you chose, but MA1 — which hours the room is open — is something the case asked you to assume — what happens to your recommendation if that one assumption turns out to be wrong?
4. Appendix D gives you beverage revenue per player for both games, and it isn't required by any deliverable — did you use it, and would including it change which option you'd pitch?
5. Appendix A says "the casino does not have any Indigo tables currently" — what does that sentence imply about who's available to deal cards at 4 tables on opening night, and have you assumed an answer to that without noticing you assumed it?

## The trap

A Hero who reasons "25 machines will obviously out-earn 4 tables — there are more than six times
as many of them" is comparing **unit counts**, not **dollars per unit**. Indigo's weighted-average
rake per table-hour (case.json.derived: $525.54–$600.92, D2) is high enough that even a 4-to-25
unit disadvantage doesn't decide the case on its own — D3's video profit-per-play (well under $1)
has to be multiplied out across the full room and the full week before either side has a real
number. The opposite trap exists too: a Hero who assumes card tables obviously win "because the
pots are huge" without ever computing D3 is skipping the same required arithmetic from the other
direction. D1–D4 exist specifically so both sides get computed, not assumed, before Emilia picks a
side.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on A vs. B — no explanation yet |
| 3:00–10:00 | Position defense: "Convince us why it's the better business, not just the bigger room" |
| 10:00–15:00 | Pressure-test the models: "Whose D1–D4 numbers are most likely to be wrong, and where?" |
| **15:00** | **DROP THE TWIST** — the dealer-staffing reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) unit-count intuition vs. per-unit-dollars math (the trap); (2) "built" vs. "staffed" as two different claims Appendix A never separated for you |
| 30:00–45:00 | Close, re-vote, reflection: "What math was new to you, and how did you attack it?" — Lessons Learned |

## Cohort bands

| Band | Typical size | What changes |
|---|---|---|
| Full (12–20) | the size this case is authored for | Anchors 2–3 run as written; expect real debate over whether MA1's peak-hours assumption is fair before the room settles on D4's numbers, and an audible reaction when the Twist reveals the dealer-staffing constraint |
| Compressed (6–11) | roughly half | Anchors 2–3 combine into one pass; D1's three-tier weighted-average table is worked as a shared example for one tier before pairs finish the other two independently |
| 1:1 / pair (1–2) | one or two learners | No vote to take — Anchor 1 becomes a stated initial position instead of a cold-call; the guide plays devil's advocate directly, specifically pushing the "more units must mean more money" framing to see if the Hero catches the per-unit-dollars error unprompted |

## Sensitivity note

Not stable under every stated assumption at ±50% (see `sensitivity_model.py`, `FLEX =
["peak_hours_per_day", "indigo_tables_staffed"]`): flexing `peak_hours_per_day` to 18 hours/day
(+50%) keeps Option A winning but pushes the margin well past SPEC §2's 20% cap; flexing
`indigo_tables_staffed` down to 2 (-50%, the Twist's own scenario) flips the winner to Option B
outright. Both are disclosed here and in `case.json.balance.stability` rather than hidden — this
case's real teaching point is precisely that the base recommendation depends on an assumption
(dealer staffing) the original docx never called out as load-bearing.

## Content sensitivity

A business-profit-projection case (gambling economics) with no illness/death/money-stress/
family-hardship content per SPEC §6. Indigo, The Landmark Hotel And Casino, and every person in
this case are fictional (see `case.json.legacy_conversion_note`) — no real casino, game, or person
is being described.
