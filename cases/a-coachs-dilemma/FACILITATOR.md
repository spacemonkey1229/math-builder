# Facilitator Guide — A Coach's Dilemma

MS | Heroes Academy | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric:** corrected expected points conceded by Houston per defensive possession
(Hack-a-Jordan vs. Play It Straight) · **Margin:** 9.7% in favor of Hack-a-Jordan — inside SPEC's
20% cap and load-bearing on the disclosed transition-suppression assumption (see the Sensitivity
note before Lessons Learned).

This is a full content replacement of the previous "A Coach's Dilemma" (a fictionalized 2008 NCAA
Championship scenario, BLOCKED at Tier 2 QA 2026-08-18 — see `case.json.replacement_note` and git
history for the retired content). This guide is written fresh for the new, real-2015-NBA-anchored
content; nothing below carries over from the old guide.

---

## Intro

Frame the format: this is a real coaching decision from a real, documented NBA playoff series, not
a story pasted on top of made-up numbers. Don't open with the math — open with the stakes: down
2-1 in a second-round playoff series, two hours before Game 4 tips off.

## Launch

Read the Overview aloud. Pause where the case does — Priya Shah with two folders squared on the
table, waiting for the knock. Do not reveal which folder she's about to hand over, and do not show
Appendix B/C's numbers yet.

## Anchor 1 — TAKE A STAND AND VOTE

"Is anyone courageous enough to stand with Option A — Hack-a-Jordan?" Cold-call for a vote, no
reasoning allowed yet. Write the split on the board (e.g., "10 hack / 5 straight / 3 unsure").

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to find out here?" Let it get messy before steering. A room that lands
on something like *"is fouling actually worth more points than letting them play?"* is close to the
real question, but push further: the real question is *"worth more points than what, exactly — and
what are we not counting yet?"* That second half is what D2 vs. D3 exists to expose.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had the data, how would we actually decide?" Push for a concrete comparison, not a vibe: two
free throws at some percentage, versus... what, exactly, for the other option? Re-ask Anchor 2's
question once a process is on the board: "Given this process, is our question still the right one?"

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming? Which assumptions are load-bearing?" Surface, without confirming or denying
yet: does a missed second free throw definitely end the possession? Does fouling cost Houston
anything on their OWN next possession? Does the fouling player have unlimited fouls to give? Bank
these — Anchor 4's questions are exactly what Appendix D's four stated Modeling Assumptions (MA1-4)
and Appendix C's foul rule answer.

## Data Deep Dive

Now, and only now, hand out Appendix B (Jordan's real shooting splits, Clippers' real offense) and
Appendix C (the real foul-out rule and the D4 scenario). Let Heroes work D1 and D2 — the raw,
uncorrected "gut check" — before revealing anything about D3's two cost adjustments.

Expect D2 to land somewhere near a ~29% margin favoring Hack-a-Jordan (2 x 39.7% = 0.794 points,
versus the Clippers' real 1.124 points per possession). Let the room sit with that number before
Appendix D comes out.

## Twist

**Drop this at roughly the 15-minute mark**, slowly, with pauses — after the room has worked
through D2/D3's corrected ~9.7% margin and started discussing D4's foul-budget scenario, but
before the room has voted a second time.

> "One more thing. This case is set before Game 4 actually tips off — but Game 4 already happened,
> in real life, on May 10, 2015. Here's the real box score. Houston ran Hack-a-Jordan hard.
> DeAndre Jordan went to the free-throw line 34 times in that one game — 28 of those attempts came
> in the FIRST HALF ALONE, a real NBA playoff record — and made 14 of them. Houston's primary
> center, the one doing most of the fouling, picked up personal foul after personal foul and fouled
> out with 18 minutes and 22 seconds played — barely more than a third of the game — and drew a
> technical foul on the same play, ejecting him. The Clippers won 128-95. Houston lost by 33."

**What this invalidates:** the comfortable read that D3's ~9.7% modeled edge for Hack-a-Jordan
means the strategy "worked" that night. It did not — but that does not mean D3's math was wrong.
A real, defensible ~9.7% expected-value edge is still just an edge, not a guarantee, and one real
game is a tiny sample. The foul-out risk D4 asked students to quantify in the abstract (a stated
scenario, "4 fouls already, entering the fourth") happened for real, faster and worse than the
case's own stated scenario — Houston's primary center didn't even make it out of the first three
quarters.

**The follow-up (the whole point):** *"Was the recommendation wrong, or did the dice just land
badly? What's the difference between those two things, and how would you even tell?"* Push the
room to separate **process** (was ~9.7% a real, honestly-computed edge, given what was knowable
before Game 4?) from **outcome** (Houston got blown out anyway). This is the transferable skill:
a good process can still produce a bad single-game outcome, and a bad process can still get lucky
once. Real NBA history did not need to spoil in Houston's favor for the case's own math to have
been done honestly.

**Bonus real color, if the room wants more:** Houston lost Game 4 by 33 but came back to win the
series 4-3 anyway (Games 5, 6, and 7 all went to Houston). That fact is not needed for any of this
case's math — it's real, and it's a good way to close the loop that one bad night, even a blowout,
doesn't retroactively make a defensible pre-game process wrong.

**Soundness check (SPEC.md §6 / case-write §11):** read sequentially against Appendix D's MA1-MA4
and case.json's `modeling_assumptions[]`, in order — the Twist doesn't contradict any of them. MA1
already flags that season percentages don't predict single-game variance; the Twist is that
disclosed limitation showing up for real, not a new fact fighting an old one. MA4's backup-center
cost is the same real mechanism the Twist's foul-out fact demonstrates, just with the real numbers
in place of the stated scenario's assumed ones. No assumption is invalidated; the Twist is additive
real-world confirmation, not a contradiction — and none of this real Game 4 detail appears anywhere
in case.md itself, so it is not pre-leaked.

## Close (10 minutes left)

VOTE AGAIN. "Did we ask the right question? Who's changing their answer, and why?" Ask specifically
who moved *because of D3's corrected math* versus who moved *because of the Twist's real outcome*.
Push back on anyone who says the Twist alone proves Option A was the wrong call — ask them to
separate the real, computed ~9.7% edge from the one real game's result.

## Lessons Learned

This case's own math is a clean, real example of a recurring trap: the "obvious" comparison (D2's
2 x 39.7% vs. 1.124, a lopsided ~29% margin) and the *corrected* comparison (D3's ~9.7% margin,
after two real, disclosed costs are added back in) point in the same direction here, but by very
different amounts — and D4's roster-exhaustion risk is a real, separate lever that doesn't show up
in either per-possession number at all. Real decisions are rarely as clean as a single ratio; a
careful analyst asks "what does this number leave out?" before trusting it. The Twist adds a second,
harder lesson: even a fully honest, well-sourced process can still lose on a given night. That is
not a flaw in the math — it's what "expected value" actually means, and it's worth sitting with
before Lessons Learned wraps.

## Standards Touched On

See `case.json.standards[]` and case.md Appendix F "How To…" list — generated mechanically from
`readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. D2's "gut check" says fouling Jordan concedes 0.794 expected points, against the Clippers' real 1.124 points per possession — a real, computed ~29% margin. D3's corrected number narrows that to ~9.7%. What two real costs did D3 add back in, and why does adding costs to Option A *narrow* the gap instead of widening it?
2. Walk through the arithmetic behind MA2's ~0.07-point rebound-risk adjustment. What three numbers did you multiply together, and why is multiplying — not adding — the right operation for "Jordan misses the second free throw AND the Clippers grab the rebound"?
3. Appendix C's D4 scenario says Houston's center enters the fourth quarter with 4 personal fouls. Using the real 6-foul rule, how many more intentional fouls can Houston call through him before he's disqualified — and what happens to the Clippers' points-per-possession for the rest of the stretch once he's gone?
4. The Twist tells you Houston's real center in the real Game 4 fouled out with 18:22 played, faster than D4's own stated scenario predicted. Does that change your D3 answer? If not, what exactly *does* it change about how much you'd trust Option A going into a real Game 5?
5. Suppose the Clippers' real season points-per-possession had been 1.05 instead of 1.124 — a weaker offense. Recompute D3's margin with that one number changed, using this case's other real figures unchanged. Does Option A still win, and by how much?

## The trap, named explicitly

A Hero computes D2's raw, uncorrected comparison — 2 x 39.7% = 0.794 expected points from fouling,
against the Clippers' real 1.124 points per possession — and concludes Hack-a-Jordan is an
overwhelming, nearly-30%-margin no-brainer. This is the trap: D2 leaves out two real, disclosed
costs (Appendix D's MA2 live-ball-rebound risk and MA3 transition-offense forfeit) that narrow the
true, defensible margin to roughly 9.7% once D3 is worked correctly — still real, still favoring
the foul, but nowhere near as lopsided as the naive number suggests. A second, quieter trap: a Hero
who *does* work D3 correctly can still wrongly treat ~9.7% as "basically decided," missing that
D4's real foul-budget risk is a separate, uncaptured axis that gives Option B genuine, independent
footing — not just a smaller number on the same scale.

## Sensitivity note

Sports-strategy expected-value case, no illness/death/money-stress/family-hardship content — no
SPEC.md §6 flag required on that front. One disclosure facilitators should be ready for: this case
uses a real, named, publicly documented head coach (Kevin McHale) and a real, named player (DeAndre
Jordan) purely as real historical figures in a real, already-completed, publicly reported game — it
does not invent dialogue, quotes, or decisions for either of them. The protagonist who actually
makes the case's choice, Priya Shah, is an explicitly fictional stand-in (see case.md Appendix A
and `case.json.protagonist`), the same convention this project's `LeBron vs. Michael` case uses for
its own real-named subjects.

**Assumption-sensitivity disclosure (required reading before you defend the 9.7% margin):** The
case's graded primary metric depends on two Modeling Assumptions that are NOT derived from a
precisely dated, primary, 2014-15-specific source (MA2's rebound-risk anchor is a 2015-16 season
figure from a secondary blog; MA3's transition-suppression cost is the low end of a range found
across several non-primary analyses — see RESEARCH_LOG.md for the full research trail). A hand
check run during authoring (not yet a formal Tier 2 probe 5): removing MA3 entirely widens the
margin to 23.1%, which **breaks** the SPEC Section 2 20% cap — meaning MA3 is load-bearing for
this case's balance, not decorative color, and any future Tier 2 probe 5 run should flex it first.
`sensitivity_model.py` implements a runnable version of this arithmetic for that future run. Per
this project's own doctrine (`DOCTRINE_LEDGER.md` MCS-26/MCS-41), a disclosed dependency on a
stated assumption is not automatically disqualifying — disclosure is the requirement, not perfect
robustness — but a facilitator should be ready for a room to push on exactly this point, and that
pressure is legitimate.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read aloud), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just fair" (Anchors 2-3, define the real question and a process) |
| 10:00-15:00 | Pressure-test the models: hand out Appendix B/C, let D1-D2's "gut check" develop, then start D3's corrected math |
| **15:00** | **DROP THE TWIST** — the real Game 4 box score, delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? "Was the recommendation wrong, or did the dice just land badly?" |
| 20:00-30:00 | Threaded deep conflict: (1) the naive-vs-corrected trap (D2/D3), (2) D4's real foul-budget risk as a separate axis from the per-possession metric, (3) process vs. outcome after the Twist |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands declared
per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
