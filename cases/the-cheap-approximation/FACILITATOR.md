# FACILITATOR.md — The Cheap Approximation

*Facilitator-only. Do not paste any of this into `case.md`'s student-facing appendices — the
balance argument, margin, and the plausible wrong path this case sets up live only here and in
`case.json`'s `balance` object.*

**Case:** The Cheap Approximation · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Calculus/Series — Series, Taylor Series, How to determine whether a series
converges or diverges, How to find the Taylor series of a function at a point (see
`case.json.standards[]` for exact ids).

**Status:** RESEARCHED, then REVISED (case-fix pass, 2026-08-31). All 14 `{{NEEDS_SOURCE}}` tokens
are resolved — 10 sourced (Omega Engineering 44000 Series thermistor datasheet for Appendix A;
STMicroelectronics STM32L011F4 and the Arm Cortex-M0+ Technical Reference Manual for Appendix B's
clock speed and add-cycle cost) plus a new S11 confirming the datasheet's own stated
accuracy-guarantee range, and 4 as disclosed Modeling Assumptions (MA1–MA4, covering multiply
cycles and flash-read cycles for the specific MCU, and the fictional project's own flash budget
and entry width, none of which have a public source to find). See RESEARCH_LOG.md for the full
trail, including the original research pass and the subsequent case-fix pass that produced the
numbers below.

**Balance flag, read before you facilitate:** on the primary metric (degrees of error at the
sensor's calibration-curve extremes, per microsecond of on-chip compute time), the Table Path beats
the Series Path by `margin_pct` = 13.97% (`case.json.balance_test`) — inside SPEC §2's ~20% cap.
**This case was retuned 2026-08-31** (see RESEARCH_LOG.md's case-fix pass for the full derivation):
the case originally came back from `case-research` at `margin_pct` = 99.86% (Table Path winning by
roughly 730x), which was not a genuine dilemma. Two things were revised together: (1) Appendix A's
operating range was corrected from a spliced −80°C/150°C figure (which combined two different
datasheet spec lines the datasheet itself never states as one) to the datasheet's own explicitly
stated 0–70°C accuracy-guarantee window; (2) Appendix C's flash budget (MA3, always a disclosed,
unsourced Modeling Assumption) was tightened from 64 bytes to 6 bytes, reflecting a genuinely
flash-starved coin-cell part. Neither change alone closes the gap — see `case.json.derived` and
RESEARCH_LOG.md for the sensitivity sweep across intermediate flash-budget values. The discussion
below is built so the room's real tension is *how much you should trust a stated Modeling
Assumption that the whole recommendation turns on* — the flash budget is the most load-bearing
figure in the case, and defending it (or attacking it) is the transferable skill, not the vote
itself.

## Intro

Frame the format before anything else: this is a real firmware release-train decision with a
locking deadline, not a worksheet. Name the opener — "You are Naomi Kessler, cursor hovering over
the merge button, two firmware branches open side by side, and a release train that locks at the
end of the week." Let the stakes land — a coin-cell part with no wall power, flash memory shared
across features, and a pilot customer whose units sit in unconditioned attics and equipment
enclosures — before moving to the Launch.

## Launch

Show the Dilemma's two branches side by side — the Series Path's on-chip math, the Table Path's
flash-memory lookup — with no numbers beyond what the Overview already says (Series Path: cheap in
cycles, no flash spent; Table Path: no math, but flash-hungry and slower per reading). Ask: "Just
from that description, which one do you think wins, and on what?" Do not confirm or correct answers
here. Most rooms will jump to "the Series Path, because it's basically free in cycles" — that
instinct is worth recording out loud before anyone touches Appendix A's accuracy numbers, because it
is exactly the plausible wrong path this case is built to expose (named further down, after the
Data Deep Dive).

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Table Path — the option that spends more cycles and
more flash?" Show of hands, both options, no discussion. Record the count — Close will ask them to
vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which option is
more accurate" or "which option is faster," but push on what Naomi's release train actually needs:
"The Overview says outright that Naomi doesn't want the branch with the least error, full stop, and
doesn't want the branch that runs fastest, full stop — so what *is* she actually optimizing for, and
why does that make this harder than picking the bigger or smaller number in Appendix A or Appendix
B?" If the room lands on "we need accuracy per microsecond of compute time, not accuracy alone and
not speed alone" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which option is more accurate" from "which option buys the most accuracy
per microsecond," ask them to name the actual steps before touching the appendices: derive the
Series Path's 2nd-order Taylor expansion at the calibration center point (D1, from Appendix A),
check the interval over which the full series is guaranteed to converge (D2), compute each option's
error at the operating-range extremes (D3, Appendix A), compute each option's on-chip evaluation
time using Appendix B's cycle-timing spec and Appendix C's flash-budget-derived table resolution
(D4), then combine error and time into the primary metric and recommend (D5). Re-ask: "Is our
question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix B's multiply-cycle and flash-read-cycle figures (MA1, MA2)
and Appendix C's flash budget and entry width (MA3, MA4) are all stated Modeling Assumptions, not
sourced figures — no fetchable public document pins down STMicroelectronics' specific silicon
choices here. Ask which ones actually change the *graded* D5 result if they move. MA1 and MA4 narrow
or widen gaps without flipping anything by themselves. The honest answer for what *does* matter is
MA3 — the flash budget is the figure the whole dilemma turns on (see case.md's own Modeling
Assumptions table, MA3's Sensitivity column). Let a sharp Hero find this themselves before
confirming it.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's derivation, D2's convergence interval, D3's two error
figures, D4's two compute-time figures, and D5's comparison together as a room, cold-calling for D5
specifically — this is where a Hero who correctly found the Series Path cheaper in cycles (D4) but
never carried D3's error figures through to the ratio will visibly struggle to explain why the Table
Path still wins. That struggle is useful information for the facilitator, not a moment to rescue.

**Facilitator-only arithmetic note.** Using the sourced Steinhart-Hart coefficients (Model 44004:
A=1.468e-3, B=2.383e-4, C=1.007e-7) and the response function T(u) = 1/(A+Bu+Cu³) − 273.15,
u=ln(resistance), expanded to 2nd order about u0=ln(R at 25°C): D3 — the Series Path is off by
**+0.17°C** at 0°C and **−0.67°C** at 70°C (worst case 0.67°C); the Table Path's worst-case
linear-interpolation error, at a 3-entry table (MA3=6 bytes, MA4=2 bytes/entry), is **≈1.03°C**,
occurring near the interval's midpoint (~50°C) rather than at either endpoint, since the endpoints
are themselves exact table nodes. D4 — Series Path = 5 cycles = **0.156 µs**; Table Path = 9 cycles
(2 flash reads + 1 multiply + 2 adds) = **0.281 µs**, about 1.8x slower in raw time, exactly as the
Overview predicts ("never the faster option in absolute terms"). D5 — Series metric ≈ **4.27°C/µs**
(0.67 ÷ 0.156, rounding); Table metric ≈ **3.68°C/µs** (1.03 ÷ 0.281, rounding). The primary metric
rewards the *smaller* error-per-microsecond figure — a Hero who gets this backwards will confidently
recommend the Series Path because it has fewer cycles, without noticing that its own error figure,
divided by its own (smaller) compute time, is actually the *larger* ratio. The full method is in
`case.json.balance_test.margin_basis`; a Hero reproducing this arithmetic from Appendix A/B/C alone
should land on the same numbers. All values above are recorded in `case.json.derived` for
continuity checking.

**Root cause, for your own understanding (do not over-explain unprompted).** The 2nd-order Taylor
truncation's error grows roughly with the cube of (u−u0), not with distance-in-degrees-C — which is
why the *original* −80°C/150°C scoping was so lopsided (u is far more compressed on the hot side and
far more stretched on the cold side of this NTC thermistor's log-resistance curve; the original
range alone produced a ~21.4°C error at its cold extreme). The full, non-truncated series converges
everywhere in the operating range regardless of scoping — convergence was never the problem; a
low-order truncation's accuracy near the range edges was. This is exactly the distinction D2 (do we
converge?) versus D3 (how much error at this order, at this range?) is built to surface.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Someone on the review points out something everyone in the room already had in front of them: the
target microcontroller's total flash is 16 Kbytes — 16,384 bytes. Appendix C reserves 6 bytes of
that for calibration data. That's a little over three-hundredths of one percent of the part's total
flash — a genuinely tiny sliver, even for a coin-cell part."

"If 6 bytes is really what's left once the wireless stack, drivers, and bootloader take their share,
that's a real and defensible number. But if it isn't — if it was chosen specifically because it
produces a close, interesting margin rather than because it reflects what this firmware project
would actually reserve — then the whole recommendation rests on a number nobody in the room has
independently verified. Does knowing it's under a tenth of a percent of total flash make you more
confident in that number, or less?"

**Facilitator-only: what this actually does, and does not, change.** The 16 Kbyte total-flash figure
(sourced to the STM32L011F4, S8) and the 6-byte MA3 reservation were both already in the case —
this twist is not a new sourced number, it is a ratio computed from two figures Heroes already had
that most will not have connected on their own. Walk a Hero through the arithmetic (6 ÷ 16384 ≈
0.037%) and note that **the recommendation does not automatically flip** — MA3 is still the number
of record until a Hero makes and defends a specific, reasoned alternative. What the twist *does* do
is surface a real modeling question the D3/D4/D5 chain doesn't ask on its own: is "genuinely
flash-starved" a fact about this fictional firmware project, or a framing choice that happens to
produce a 13.97% margin instead of a 99.86% one? The case has no sourced answer for what this
specific project's real memory map looks like — inventing one here would be exactly the fabrication
SPEC §5 forbids. **The twist reframes, it doesn't resolve:** "which option wins under the stated
6-byte budget" is a different question from "is 6 bytes the right number to trust," and a Hero who
only answers the first hasn't interrogated the assumption the whole D4/D5 chain is built on. Do not
hand a specific answer to the second question — it is genuinely open given what this case can
honestly source, and that openness is the point.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the flash-budget question change your vote — or does it
just tell you that '6 bytes' was an assumption worth pressure-testing, not a fact?" That distinction
is the transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **Fewer cycles is not the same as more accuracy per microsecond.** The Series Path wins D4 every
   time, by construction — yet it loses D5. Why does looking only at Appendix B's cycle-timing table
   mislead here, and what does the primary metric's structure (error divided by time, not either
   alone) actually protect against?
2. **A flash budget chosen to produce "a genuine dilemma" is not the same as a flash budget grounded
   in this project's real memory map.** The twist shows the 6-byte reservation is well under a tenth
   of a percent of the part's total flash. Does that change how confident the room should be in
   Argument B's framing — even though the recommendation itself doesn't flip without a specific,
   defended alternative number?
3. **What the flash-budget gap can and can't tell you.** MA3 is the load-bearing, unsourced figure
   the whole 13.97% margin turns on. Is a margin this close, built on an assumption this contested, a
   decision worth defending with real confidence — or does the closeness itself argue for hedging the
   recommendation rather than stating it flatly?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both branches side by side, cold-call for a gut read, no accuracy or timing numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your option actually wins on accuracy per microsecond, not just on cycles or on error alone"* |
| 10:00–15:00 | Pressure-test the models — *"Which of MA1, MA2, MA3, or MA4 would have to change, and by how much, for your answer to flip?"* |
| **15:00** | **DROP THE TWIST** — the 6-byte flash reservation vs. the part's 16 Kbyte total flash, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (cycles vs. accuracy-per-microsecond; is "flash-starved" a fact or a framing choice; is a narrow, assumption-driven margin still worth defending) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most learners will pick the Series Path purely because "Taylor series math is only a handful of
cycles, so it must win" — they assume the low compute-time cost is the whole story and skip D3's
error-at-the-extremes figure entirely, never checking whether the accuracy loss is small enough to
justify it. The mirror-image mistake: a student assumes a lookup table "can be made arbitrarily
accurate" — true in principle — and misses that the case forces a *specific* table resolution, set
by Appendix C's flash budget, not an unlimited one. A Hero who defaults to that assumption and never
checks D4's compute-time cost against that resolution will end up defending a table that is either
not accurate enough to justify its cost, or accurate enough but slower than the metric can tolerate.
The case forces D1 through D4, in that order, specifically so no one can jump from "one option feels
obviously cheaper" or "one option feels obviously more accurate" straight to a recommendation
without ever computing the ratio the primary metric actually asks for.

## Socratic questions

1. Your D1 Taylor series is exact at the calibration center point by construction. Your D3 table measures its error at the operating-range extremes instead. Why does the case ask you to check the extremes rather than trusting the center-point accuracy you already know is perfect?
2. Your D2 convergence check tells you the interval over which the full, non-truncated Taylor series is guaranteed to converge. If that interval is narrower than Appendix A's full rated operating range, what does that tell you about how much you should trust a 2nd-order truncation near the edges of that range — even before you've computed D3's actual error numbers?
3. Appendix C's flash budget sets a specific table resolution for the Table Path — not an unlimited one. If that budget were cut in half, what would you expect to happen to the Table Path's D3 error figure, and would that change which option wins D5?
4. Your D4 compute-time table should show the Series Path finishing in far fewer microseconds than the Table Path, every time. Does that automatically make the Series Path the better choice on this case's primary metric — or does "fewer microseconds" only matter in relation to something else?
5. Naomi's part runs on a coin cell, not a wall outlet. If this were instead a wall-powered device with generous flash memory and no battery constraint at all, would you expect the same option to win D5 — and what part of your D4 table would that change?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for the
Table Path at Anchor 1 purely on "more accuracy sounds safer" and stays with the Table Path after the
twist for a *different, ratio-and-assumption-based* reason has genuinely moved, even if the vote
count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "MA3 is the load-bearing figure, not MA1/MA2/MA4" finding landed as a discovery
  or had to be told outright.
- Whether the "fewer cycles vs. accuracy per microsecond" trap was the actual sticking point, or
  whether D3's error arithmetic itself was the harder gate for most Heroes.
- Whether the flash-budget twist felt like a genuine new constraint or felt like the case dodging a
  clean numeric answer — worth listening for directly, since this case's own balance note records a
  13.97% margin (inside SPEC §2's cap, but genuinely close) that the twist does not paper over.

## Standards Touched On

Series · Taylor Series · How to determine whether a series converges or diverges · How to find the
Taylor series of a function at a point

## Facilitator note — sensitivity (SPEC §6)

None declared by the concept sheet — routine embedded-systems/firmware engineering math, no
contested or emotionally weighted subject matter. `case.json.sensitivity_note` is `null`.
Now that `case-research` and the subsequent case-fix pass have both run, the confirmed
load-bearing lever is Appendix C's flash-memory budget (MA3) — it directly sets the Table Path's
achievable resolution and therefore its D3 error figure, and at the current 6-byte assumption the
case sits close enough to a flip that even modest, defensible changes to MA3 move the winner.
Appendix B's cycle-timing figures (MA1, MA2) matter less — they narrow or widen the compute-time
gap but do not flip the winner at any tested value. Direction only, per `case-write` SKILL.md's
Modeling-Assumptions-leak rule: this note states the direction of that sensitivity only — never its
size — even though the actual computed numbers are recorded in `case.json.derived` and
RESEARCH_LOG.md for facilitator reference.
