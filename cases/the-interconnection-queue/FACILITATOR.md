# FACILITATOR.md — The Interconnection Queue

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Interconnection Queue · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Fractions/Addition and Subtraction of Fractions — How to add fractions, How to add
with mixed numbers, How to subtract fractions, How to subtract with mixed numbers (see
`case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-09). All `{{NEEDS_SOURCE}}` placeholders in `case.md`
are resolved — four real figures are sourced (Appendix F: LBNL's queue wait-time and total-capacity
statistics, DOE's transmission-planning threshold, and FERC Order No. 2023's cluster-study reform),
and Appendix C/D's capacity-block MW size is a disclosed Modeling Assumption (MA1 = 24 MW),
because no source publishes Fenwick Creek's own block size. `case.json.balance.margin_pct` is a
real, computed **8.33%**. Everything below is the case of record, not a placeholder. **The A-vs-B
win arithmetic does not depend on MA1's 24 MW figure at all** — the comparison is a pure
same-units fraction comparison in blocks; the MW figure only translates the answer into a
real-world quantity for narrative color (per this fact, MA1 is disclosed as `sensitivity_disclosure`
Category F but is *not* expected to flip the verdict, unlike a typical load-bearing assumption).

## Argument for A — Approve Aurora Ridge now

A's case is **certainty**: Aurora Ridge is engineering-cleared and ready to sign today, with no
dependency on anyone else's bid confirming. Its request (2-7/8 blocks) very nearly fills the
substation's remaining capacity (3-3/8 blocks after subtracting the 1-1/4 blocks already
committed from the 4-5/8-block total) — the leftover under this option is **1/2 block** of
stranded capacity, found by subtracting 2-7/8 from 3-3/8 with a regrouping step (3-3/8 = 2-11/8,
since 3/8 is less than 7/8). A's real weakness is that this 1/2-block leftover is an odd, specific
size — it is smaller than every other single bid Meridian Valley Power has on this queue, so it
may sit stranded indefinitely once committed.

## Argument for B — Hold the slot for the combined bid

B's case is that the two smaller bids, added together (1-1/4 + 1-2/3, converted to twelfths, =
2-11/12 blocks), fit inside the same 3-3/8-block remaining capacity and leave only **11/24
block** stranded — genuinely less than A's 1/2 block (12/24), a real, computed advantage. B's real
weakness is structural, not arithmetic: it requires *both* Cobalt Peak and Fenwick Yards to
actually confirm before Meridian Valley Power's queue deadline, and neither is engineering-cleared
the way Aurora Ridge already is. Choosing B is a bet that a smaller total stranded-capacity number
on paper is worth the risk that one or both smaller bids fall through and the slot sits idle
while Aurora Ridge — a bid that was ready today — goes elsewhere.

## The margin — real numbers, and how thin they are

`case.json.balance.margin_pct` = **8.33%**, inside the project's 8–15% target band. The
arithmetic, in full:

- **Remaining capacity:** 4-5/8 − 1-1/4 = 4-5/8 − 1-2/8 = **3-3/8 blocks**.
- **Option A (Aurora Ridge):** 3-3/8 − 2-7/8 = (borrow) 2-11/8 − 2-7/8 = **1/2 block stranded**.
- **Option B (Cobalt Peak + Fenwick Yards):** 1-1/4 + 1-2/3 = 1-3/12 + 1-8/12 = **2-11/12 blocks
  combined**; 3-3/8 − 2-11/12 = (LCD 24: 3-9/24 − 2-22/24, borrow) 2-33/24 − 2-22/24 = **11/24
  block stranded**.
- **Margin:** |1/2 − 11/24| / (1/2) = (12/24 − 11/24) / (12/24) = (1/24)/(12/24) = **1/12 ≈
  8.33%**. B leaves less stranded capacity under this case's own fixed numbers.

**Why this matters for the facilitator, specifically:** the gap between the two options is exactly
**1/24 of a block** — a single, small unit. A student who makes any of the three regrouping
subtractions in this case even slightly wrong (in either direction) can flip which option looks
better, because the true margin is this thin. Do not let a room believe B is an obviously superior
choice; it wins by a real but narrow amount, and it carries real confirmation risk A does not.

## Five Socratic questions

1. Appendix B lists Aurora Ridge's request as 2-7/8 blocks and the remaining capacity as 3-3/8 blocks — why can't you just subtract 7 from 3 and 8 from 3 and call it done?
2. Your D2 subtraction of 3-3/8 minus 2-7/8 requires "borrowing" a whole block — walk us through exactly what that means and why the answer would be wrong without it?
3. Cobalt Peak and Fenwick Yards are each too small alone to be worth holding the slot for — what has to be true about their combined size, arithmetically, before Option B is even worth comparing to Option A?
4. Your D4 answer says Option B strands less capacity than Option A — is that difference large enough that you would still trust it if you'd made a small arithmetic error somewhere upstream?
5. Option B depends on two separate bids both confirming before the deadline — if you knew only one of the two would actually confirm, would you still recommend B?

## The trap

**A learner who adds or subtracts the whole-number parts and the fraction-numerator parts of these
mixed numbers separately, without first converting every fraction to a common denominator, will
compute a plausible-looking but wrong total at almost every step of this case** — this is the
concept sheet's own named trap, and it appears at least three times: D1's four-bid sum (eighths,
quarters, thirds, sixths), D2's borrow-required subtraction (3-3/8 − 2-7/8), and D3/D4's
quarters-and-thirds addition followed by an eighths-and-twelfths subtraction. Because every one of
these mixed numbers has a *different* denominator from the next, a student can get lucky and add
two same-denominator numbers correctly early on and falsely conclude their method (add/subtract
numerators directly) generalizes — and then get every later step wrong. **Watch specifically for a
D2 answer of "3/8 − 7/8 = can't do it, so I'll just subtract the smaller from the larger and get
1/2" without ever regrouping the whole block** — this produces the *same numeric answer* (1/2) as
the correct method here by coincidence, so a facilitator cannot tell from D2's final number alone
whether the student actually understands borrowing; ask them to show the regrouping step
explicitly (Socratic Question 2).

## Twist

Structural, not a dropped mid-discussion fact: **the real margin between Option A and Option B is
exactly 1/24 of a block — the smallest fractional unit that appears anywhere in this case's own
arithmetic.** A student who makes a single regrouping error in either D2 or D4 (for example,
forgetting to borrow, or borrowing incorrectly and writing 2-11/8 as 2-10/8) will compute a
stranded-capacity figure that is off by exactly the size of this margin or larger, and will not
be able to tell, from their own wrong number, that anything went wrong — the wrong answer looks
just as plausible as the right one. Facilitators should treat the moment two students compare
D2/D4 answers and get different results as the natural twist moment, and can manufacture it
directly with Socratic Question 4: "Is that difference large enough that you would still trust it
if you'd made a small arithmetic error somewhere upstream?"

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro
Frame the format: a queue board, a supervisor's five o'clock deadline, a developer's counsel on
hold. This is a real grid-capacity allocation decision wearing a fractions worksheet, not the
other way around.

### Launch
Read the Overview aloud. Stop at "she mutes the line." Ask the room: "Before you've seen a single
number, does 'take the sure thing now' or 'hold out for a better fit' sound like the safer call?"

### Anchor 1 — TAKE A STAND AND VOTE
No reasoning yet. "Approve Aurora Ridge now, or hold the slot for the combined bid — show of
hands." Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?
Push the room past "which developer seems more reliable" toward "which option leaves less of the
substation's real, physical capacity stranded, once the fraction arithmetic is done honestly."
Surface that "nearly fills the remaining capacity" (Aurora Ridge) is not the same as "fills it
best."

### Anchor 3 — WHAT IS THE PROCESS?
Before touching Appendix A/B's numbers, get the room to state the process out loud: find the
remaining capacity (subtract committed from total), find each option's stranded leftover
(subtract the request(s) from what remains), then compare the two leftover amounts directly.
Re-ask: "Now that we have a process, is 'which developer seems more reliable' still the right
first question?"

### Anchor 4 — WHAT DON'T WE KNOW?
Name the load-bearing unknown explicitly: Option B requires *both* Cobalt Peak and Fenwick Yards
to confirm before the queue deadline, and neither is engineering-cleared the way Aurora Ridge
already is. "Is 'B wins by 1/24 of a block' still true if one of the two bids doesn't show up?"

### Data Deep Dive
Open Appendices A–D. Run D1–D5 as a room, or have groups report out. This is also the moment to
run Socratic Questions 1 and 2 (common denominators, and the regrouping/borrow step).

### Twist
Once D2 and D4 are on the table, run Socratic Questions 4 and 5: "How much headroom does Option B
actually have over Option A?" (Answer: exactly 1/24 of a block.) Then: "If you'd made a small
arithmetic error upstream, would you even know?" Let the room discover how thin the margin (8.33%)
and the confirmation risk actually are.

### Close
VOTE AGAIN. "Did the vote move? For anyone who didn't move, what would it take to change your
mind — a different number, or a different priority (efficiency vs. certainty) entirely?"

### Lessons Learned
The core transferable idea: when every quantity in a comparison has a different denominator, you
cannot shortcut the common-denominator step anywhere in the chain — get away with it once by luck
and the next step will be wrong, and a wrong answer from skipped regrouping can look exactly as
plausible as a right one.

### Standards Touched On
How to add fractions; How to add with mixed numbers; How to subtract fractions; How to subtract
with mixed numbers.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00–8:00 | Position defense: "Convince us your pick actually uses the substation's capacity better" |
| 8:00–20:00 | Data Deep Dive — build D1's total-demand table and D2's remaining-capacity/stranded-A figures as a room |
| 20:00–30:00 | Build D3's combined-bid sum and D4's head-to-head comparison |
| **30:00** | **DROP THE TWIST** — "The real margin between the two options is 1/24 of a block. If you'd made one small arithmetic error upstream, would you even know?" |
| 30:00–38:00 | Pressure-test the regrouping steps directly: re-derive D2 and D4 as a room, checking every borrow step |
| 38:00–45:00 | Close, re-vote, D5's visual walkthrough, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the Data Deep Dive runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly; the D2/D4 arithmetic pressure-test (30:00–38:00) still runs in full |
