# Guide Notes: Robotics Engineer

**Case:** Robotics Engineer · **Tier:** T2 · **Band:** MS · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (13 skills — coordinate geometry,
the distance formula, the triangle inequality theorem, unit conversion, percent, and comparison)

Legacy conversion, 2026-08-01, reformatted from the original 2021 Guide Notes
(`source/Y2/Session 2/Robotics Engineer/Guides Notes.docx`) onto the current 11-anchor ladder.
This case is SPEC.md's own cited exemplar ("Route 1 beat Route 2 by 0.09%") — this conversion
computes its own honest coordinates and distances from the source map rather than replicating that
exact historical number (see `case.json.legacy_conversion_note`), and lands on a comparably tight,
independently-derived 3.78% margin.

## Intro

Frame the format: this is a real decision Spencer has to defend, not a worksheet. Name the opener
— "It's 3 AM, a robot the size of a small car is standing in a debris field, and you have thirty
seconds to give it its next order."

## Launch

Show Appendix A's map with the three sites marked, no distances or times labeled yet. Ask: "Just
looking at the map, which order looks faster to you?" Do not confirm or correct answers — the
point is a gut read before anyone touches the distance formula.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who sends Ultron to A first? Who sends it to B first?" Show of hands, no discussion. Record the
count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "Is it just as simple as which path is fastest, or is there
something else we need to consider?"**

Let confusion grow here, deliberately — this is the original Guide Notes' own move, preserved. Push
on Container A's missing data: "Is 'which path is fastest' really the only thing Spencer has to
weigh, or is there a second kind of risk here that a stopwatch can't measure?" If the room lands on
"we have a known-and-falling number for B and an unknown for A" on its own, that's the case working
as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of the tradeoff, ask them to name the actual steps: plot the
three sites, compute the three pairwise distances with the distance formula, convert Ultron's speed
to match, total the time for both orders. Re-ask: "Do we agree on that process? Is our question
still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix C's three real conventions: rough terrain everywhere (no shortcut modeled),
straight-line travel (no mid-route climbing in the time calculation), and Container A's total data
absence — not an assumption to fill in, a real fact to sit with.

## Data Deep Dive

Now, and only now, the numbers. Walk D2's three distances and D3's time totals together as a room,
cold-calling for the unit-conversion step specifically — this is where a Hero who mixed mph and
meters without converting will visibly disagree with everyone else's answer.

**D6, right after D2's three distances are on the board.** Before anyone commits to a route, ask
the room to check the three distances against the Triangle Inequality Theorem: does any one side
come out longer than the sum of the other two? It shouldn't — real coordinates always form a valid
triangle unless the points are collinear — but this is a real, disclosed sanity check a robotics
engineer would actually run before trusting a drone survey enough to route a valuable robot through
a hazardous debris field. The margin is real and worth naming: C-A plus C-B (22.858 m) beats the
direct A-B distance (21.587 m) by only 1.271 m — a real margin, though it's this case's C-B leg
specifically, not this triangle-inequality gap, that the Twist below actually turns on.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Ultron has just started moving. A secondary explosion sends debris flying across the site — the
direct path between Site C and Site B is now blocked. A drone resurvey finds a real detour route
around the debris field: 15 extra meters, whenever that leg is used."

**Facilitator-only: what the numbers actually do (`case.json.derived`).** This is deliberately a
*different* leg from the case's own triangle-inequality moment (D6 cold-calls the C-A/C-B/A-B
triangle; the twist blocks C-B specifically, not A-B) — and that choice matters mechanically, not
just narratively. Route C→A→B never travels the C-B leg at all; it goes C→A→B directly, so it is
completely unaffected by a C-B blockage. Route C→B→A travels C-B directly, so its C-B leg goes
from 10.817 m to 25.817 m (+15 m), and its total time rises from 20.135 to 29.456 minutes.
**The twist flips the verdict — C→A→B (unchanged at 20.896 minutes) is now faster than C→B→A
(29.456 minutes), a reversal from B to A, margin swinging from 3.78% to 40.96%.** Ask the room
directly, before revealing which order flips: "does blocking a road that only ONE of your two
route orders actually uses affect both orders equally, or could it matter which order you picked
after all?" A Hero who assumed (from the A-B version of this kind of twist, or from Anchor 3's
"whichever order you chose" framing) that any blocked leg affects both orders the same way has a
real, concrete moment to be wrong here — the C-B leg is not symmetric between the two orders the
way the shared A-B leg is.

## Immediate recommit

Re-vote immediately. Ask by name: "Did the C-B detour change your recommended order? If you chose
C-B-A originally, does a 15-meter detour on just that leg actually flip your vote, or do you want
to see the exact numbers first?"

## Deep conflict — three threads (20-30 min)

1. **Known-small risk vs. unknown risk.** Container B's number is real and falling; Container A's
   number doesn't exist. Is "we can't measure it" a reason to prioritize A, or a reason it can't
   actually drive the decision at all?
2. **Whose call is this?** Spencer isn't DOD — he doesn't know why Container A's feed cut out, or
   what's actually inside either container. Should a missing data point from an agency that won't
   explain itself carry real weight in his decision?
3. **What the twist actually tested.** The C-B detour flips the faster order from C-B-A to C-A-B —
   a real reversal, not a wash. Does a Hero whose recommendation flips on a single blocked road have
   a fragile original analysis, or is correctly recomputing when new information arrives exactly
   what a robotics engineer's model is supposed to do?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show the unlabeled map, cold-call for a gut read, no distances yet |
| 3:00–10:00 | Position defense — *"Convince us your order is faster, not just different"* |
| 10:00–15:00 | Pressure-test the models — *"Whose total-time number is doing the most work?"* |
| **15:00** | **DROP THE TWIST** — the explosion and the blocked C-B path, delivered slowly |
| 15:00–20:00 | Immediate recommit — did the C-B detour flip anyone's order, and why |
| 20:00–30:00 | Threaded deep conflict (known-small vs. unknown risk; whose call; what the twist tested) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes the total-time comparison, finds C→B→A faster, and stops — treating "faster" as the
whole answer. The case's real tension is that the numbers point one way and the *unmeasured* risk
(Container A's missing feed) points the other, and Spencer's actual job is to decide how much
weight an unknown deserves against a known, falling number. Watch for a pitch that reports one
number and calls the case closed without ever mentioning Container A's missing data at all.

## Socratic questions

1. Your total-time numbers say C-B-A is 3.78% faster — how would you explain to Spencer's boss why a 3.78% edge is worth building a whole recommendation on?
2. Container A has no integrity reading at all — is "we don't know" a reason to go there first, or a reason it's impossible to justify going there first?
3. If Ultron's rough-terrain speed were actually twice as fast as stated, would the margin between the two orders grow, shrink, or stay the same percentage — and why?
4. The explosion twist only slowed down ONE of the two route orders (C-B-A), not both — why does blocking a single leg affect the two orders so differently, and would a twist on the A-B leg instead have done the same thing?
5. Spencer trusts DOD's integrity readings for B and C but has no way to verify them — should a number you can't independently check carry the same weight as one you can?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — the correct order genuinely
flips after the twist (C-B-A to C-A-B), so a room that didn't move is worth asking about directly:
did they not trust the new numbers, or did they miss that the detour only hits one of the two orders?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the distance-formula step (D2) or the unit-conversion step (D3) was the place most Heroes
  actually got stuck.
- Whether Heroes engaged with Container A's missing-data argument on their own, or needed Anchor 2's
  prompt to surface it.
- Whether Heroes correctly recomputed and voted C-A-B after the twist, or defended their original
  C-B-A pick out of anchoring rather than recomputed arithmetic.

## Standards Touched On

Coordinate Plane · Coordinate Pair (also Ordered Pair) · Right Triangle · Hypotenuse · Pythagorean
Theorem · Triangle Inequality Theorem · Unit · Percent · How to graph a coordinate pair on the
coordinate plane · How to find the distance between two coordinate pairs on a coordinate plane ·
How to convert an amount from one unit to another unit · How to find the percent of a number · How
to compare two or more values

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes are a disaster-recovery logistics decision, not personal
illness, death, or hardship. The train-crash/classified-cargo framing is scene-setting, not the
graded content.
