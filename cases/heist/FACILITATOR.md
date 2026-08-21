# Guide Notes: Heist

**Case:** Heist · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (55 skills — compound/conditional
probability, decimal and percent arithmetic, unit and compound-unit conversion, elapsed time, and
two required visual displays)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y1/Session 5/Heist/Case Study_ Heist.docx` and `Guides Notes.docx`) onto the current
11-anchor ladder. The Gang Of Five, the real Zions Bank Idaho Headquarters, the 9-minute/8.5-minute/
30-second timing, the Ford Focus, and the two exit options with their exact original figures
(17 sec/94%; 29 sec/98%) are preserved verbatim from the source. The original Guide Notes' own
anchor numbering skips a number (Intro, Anchor 1, Anchor 2, Anchor 3, Anchor 5 — no "Anchor 4" in
the source docx); this conversion does not preserve that gap, it maps the source's real content
onto the current, complete 11-anchor ladder. See `case.json.legacy_conversion_note` for the full
account of what was reused verbatim vs. newly researched.

**A note on content (SPEC §6):** this case's protagonists are sympathetic bank robbers. The math
is about probability and risk, not about glorifying theft — keep the discussion on the numbers.
The original source's own "Monday Case Study Launch" material (preserved below under Lessons
Learned) explicitly raises the "heroes or villains" question as a discussion-worthy framing device,
not a resolved position; the guide should let the room sit with that ambiguity rather than settle it.

## Intro

Frame the format: this is a real building, a real destination, and a real getaway route — dressed
up as a heist, but every mile and every stated risk factor is either sourced or openly disclosed
as an assumption. Name the opener: "Two ways out of the building. One's faster to reach. One's
supposedly safer. You have to pick, and the drive afterward doesn't care which door you used."

## Launch

Read the Overview aloud. Show a map of downtown Boise centered on 800 W Main St (real address,
Appendix A). Ask: "You are Felicity 'The Viper' — Four. What's your plan?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Street level, or underground garage?" Show of hands. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'safer'?"**

Push on what "safer" means here. Safer as in the raw stated percentage (94% vs. 98%)? Safer as in
how much time cushion is left before the hard 30-second cutoff? Safer as in the *combined* odds of
making it all the way to Heroes Academy, not just out the door? Let the room sit in the ambiguity:
"Is anyone courageous enough to define 'safer' before we compute anything?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition, ask them to name the actual steps: convert every
Appendix C risk factor into a survival probability, multiply them into one route-survival number,
multiply that by each option's exit-success chance, then compare. Re-ask: "Given how we just
defined 'safer' — is that still the right process, or does the 30-second window matter on its own,
separate from the percentages?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix C's Modeling Assumptions as a group, out loud, before anyone computes anything —
especially MA1 (how the real 8.9-mile route gets split into road-type categories) and MA2 (the
stoplight/stop-sign counts). Ask which one the room thinks matters most to the final answer.
(Facilitator note: the honest answer is *none of them* — see Data Deep Dive below — but let the room
guess first.)

## Data Deep Dive

Now, and only now, the numbers. Walk D3's compound-probability chain together as a room, one
factor at a time, for one option first.

**The primary trap — additive vs. multiplicative compounding.** Appendix C hands Heroes a stack of
flat percentages ("1.2% per mile," "1.65% per stoplight," "+14% within 1 mile") that read like
things you add up. Most Heroes will compute total risk by **summing** every risk factor (or
subtracting that sum from the whole) instead of converting each one into a *survival* probability and
**multiplying** those survival probabilities together. This is the more dangerous trap because it
produces a number that looks right: for small percentages, (1-a)(1-b) is close to 1-a-b, so an
additive answer lands close enough to the real multiplicative route-survival figure (76.43%,
Appendix C) to pass a hurried sanity check without ever being caught. Watch for it directly in D3
work: ask a group to show you
the actual operation between their risk-factor rows — a plus sign there is the trap firing.

**The secondary trap — assuming the routes differ.** Because Option A and Option B share the exact
same car, the exact same getaway route, and the exact same Appendix C risk factors, some Heroes
will assume they need to build two *separate* route-risk models — one "for Option A's route" and
one "for Option B's route" — and will spend real working time trying to figure out how the choice
of exit changes the drive. It doesn't: the drive is identical either way, every stated route
assumption cancels out of the comparison algebraically, and the entire A-vs-B decision on the
graded metric is actually decided by two numbers the Heroes already have on page one: 94% and 98%.
This trap costs time and insight rather than producing a wrong final number — a Hero who computes
correctly (even redundantly, once per option) still lands on the right answer. Cold-call on it once
groups have their route-risk math done: "Which of your numbers actually changed between Option A
and Option B?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"On your way out of the building, you see a meter maid ticketing your Ford Focus — parking meter
never got paid. There's no time to argue and no time to wait: you have to abandon the car. Two
wants the corvette in the next row. Five says take the minivan instead. Everyone looks at you.
Make the call, Four."

**Facilitator-only.** Whichever vehicle the room picks, stealing it and hot-wiring it without keys
costs **3 real minutes** — the crew is now spending 24 minutes in the getaway vehicle instead of
21. Recompute live: the per-minute risk factor (0.27%/minute) now applies across 24 minutes instead
of 21, dropping the shared route-survival probability from 76.43% to 75.82%. Recomputed totals:
Option A falls to 71.27%, Option B falls to 74.30% — both options get *strictly worse*, invalidating
any room's belief that the getaway is now safer or unaffected. But the **margin between A and B is
unchanged, still 4.26%** — the twist lowers the floor under both options equally without changing
which one wins, because the added risk (like every other route risk factor) is common to both.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then the follow-up
that matters more than the vote: **"What just broke in your original model? Did the answer change —
or just get worse for everyone, in the same way, no matter which door you'd picked?"**

The corvette-vs-minivan choice itself has no case-provided numbers — that is deliberate. A Hero who
demands data before choosing has spotted something real: this is a judgment call under missing
information, not a hidden calculation, and the guide should say so if pressed rather than inventing
a number.

**Twist soundness check (SPEC §6):** checked against every stated Background/Appendix fact and
Modeling Assumption, read both sequentially and as a final combined model. The twist changes one
input (minutes in vehicle: 21 → 24) that is common to both options; it invalidates the belief some
rooms will hold after Anchor 3 that "the drive is risk-free once you're in the car," without
depending on any unstated convention. It does not flip the winner, and the case discloses that
plainly (`case.json.sensitivity_note`) rather than let a room discover a "gotcha" that isn't there.

## Immediate recommit

Re-vote immediately. "Did the twist change your hand — or just confirm it, now with worse odds for
everyone?"

## Close

Re-vote once more after full discussion. Ask: "We asked 'which exit is safer' as our key question —
did we ask the right question, or was the real question 'how much of a safety cushion do you want,
on a call the raw percentages already answered'?" And: "What math was new to you today, and how did
you attack it — did you Google it, ask a fellow Hero, or something else?"

## Lessons Learned

*(Migrated from the original Guide Notes' "Monday Case Study Launch."*) The original case opened
its week not with the heist itself but with a broader framing exercise: a hypothetical crew of
thieves who only target corrupt corporations and give away what they steal — "are these thieves
heroes or villains?" — followed by "would you keep the money, give it away, or something else,"
and "what's the easiest thing to steal and fence: jewelry, art, computer data, phones, or something
else?" This conversion preserves that framing exactly as launch-week discussion material, not as
part of the graded case itself; it is a genuinely open ethical question the original guide never
resolved, and this conversion doesn't resolve it either. The mathematical lesson this conversion
adds, which the original case's math couldn't fully deliver without a real route: **a shared
constraint cancels out of a comparison.** Every route-risk assumption in Appendix C is real, stated
work a Hero has to do correctly — but none of it, by construction, can ever change which exit is
the better choice. Recognizing which numbers are actually load-bearing to a decision, versus which
are real but decorative to *that specific decision*, is the transferable skill.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers, not general opinion.

1. Option A leaves 13 seconds of the 30-second window unused, and Option B leaves 1 — if "safer" means margin for error rather than the raw percentage, does your recommendation change?
2. Every risk factor in Appendix C applies identically to both options — what does that tell you about which numbers in this case actually decide the dilemma, versus which ones are real work that doesn't change the answer?
3. The route to Heroes Academy doesn't pass within a mile of Boise PD's real headquarters — how would your combined probability change if it did, at the half-mile penalty instead of the one-mile penalty?
4. Appendix C's speeding formula was never required for any deliverable — under what circumstance would a real getaway crew ever choose to use it anyway, even knowing the odds get worse fast?
5. After the Twist, both options get strictly worse but the gap between them stays exactly the same size — why doesn't adding a shared delay ever change which option was already ahead?

## Standards Touched On

See `case.json.standards[]` (55 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: compound, dependent, and conditional probability; percent and decimal arithmetic
(all four operations); distance, time, and compound-unit conversion (mi/min → mph); rounding; and
two required visual displays (bar graph, pie chart or histogram).

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12–20):** Anchors 2–4 run as written; the room typically splits into a "trust the higher
  percentage" faction and a "trust the bigger safety buffer" faction before the Twist forces
  everyone to recompute minutes-in-vehicle live.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; D5's two visual displays are worked as
  one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side (raw
  percentage vs. time buffer) the Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00–10:00 | Position defense: "Convince us it's safer, not just faster or higher-percentage" |
| 10:00–15:00 | Pressure-test the models: "Which of your numbers actually differ between A and B?" |
| **15:00** | **DROP THE TWIST** — the stolen-vehicle 3-minute delay, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke — the answer, or just the odds?" |
| 20:00–30:00 | Threaded deep conflict — two named threads: (1) raw percentage vs. time-window buffer as competing definitions of "safer"; (2) which of Appendix C's real, worked risk factors are actually load-bearing to the A-vs-B decision, and which are real work that doesn't move the answer |
| 30:00–45:00 | Close, re-vote, reflection, Lessons Learned |
