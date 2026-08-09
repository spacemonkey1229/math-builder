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
direct A-B distance (21.587 m) by only 1.271 m. Hold onto that number — it resurfaces almost
immediately.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Ultron has just started moving. A secondary explosion sends debris flying across the site — the
direct path between Sites A and B is now blocked. Whichever order you chose, that leg of the trip
just got longer. Ultron has to route back through Site C's position to get around it."

**Facilitator-only: what the numbers actually do (`case.json.derived`).** The direct A-to-B leg
(21.587 m) becomes a detour through C (22.858 m) — a real, computed 1.271 m longer, for *either*
route order equally. That 1.271 m is the exact same number D6's triangle-inequality margin already
surfaced — ask the room to notice this if they don't on their own: "the detour distance isn't a new
number, it's one you already found." Recomputed: C→A→B rises to 21.686 minutes, C→B→A rises to 20.925 minutes.
**The twist does not flip the verdict — C→B→A is still faster, and the margin barely moves (3.78%
to 3.64%).** This was computed honestly from the real detour distance, not picked to force a
reversal. The room's real argument should be whether a twist that doesn't change the answer was
still worth dropping — ask directly: "if the order didn't change, what was the point of that twist?"
(A good answer: it tests whether a Hero's model was built to *recompute*, not just to state a
one-time answer — the same distinction Anchor 3's "if we go through this process" is testing for.)

## Immediate recommit

Re-vote immediately. Ask by name: "Did anyone's answer actually change? If not, why not — was your
original reasoning already robust to this, or did you just get lucky?"

## Deep conflict — three threads (20-30 min)

1. **Known-small risk vs. unknown risk.** Container B's number is real and falling; Container A's
   number doesn't exist. Is "we can't measure it" a reason to prioritize A, or a reason it can't
   actually drive the decision at all?
2. **Whose call is this?** Spencer isn't DOD — he doesn't know why Container A's feed cut out, or
   what's actually inside either container. Should a missing data point from an agency that won't
   explain itself carry real weight in his decision?
3. **What the twist actually tested.** If a Hero's route order survived the explosion unchanged,
   was their original analysis right, or just not sensitive enough to notice a real change?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show the unlabeled map, cold-call for a gut read, no distances yet |
| 3:00–10:00 | Position defense — *"Convince us your order is faster, not just different"* |
| 10:00–15:00 | Pressure-test the models — *"Whose total-time number is doing the most work?"* |
| **15:00** | **DROP THE TWIST** — the explosion and the blocked A-B path, delivered slowly |
| 15:00–20:00 | Immediate recommit — did anyone's answer actually change, and why |
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
4. The explosion twist made both routes slower by close to the same amount — what would a twist have to do differently to actually flip your recommendation?
5. Spencer trusts DOD's integrity readings for B and C but has no way to verify them — should a number you can't independently check carry the same weight as one you can?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't move at
all after the twist is worth asking about directly: did the twist not land, or did the room already
understand it wouldn't change the order?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the distance-formula step (D2) or the unit-conversion step (D3) was the place most Heroes
  actually got stuck.
- Whether Heroes engaged with Container A's missing-data argument on their own, or needed Anchor 2's
  prompt to surface it.
- Whether the explosion twist's "doesn't flip the verdict" result felt like a letdown or a genuine
  lesson about model robustness.

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
