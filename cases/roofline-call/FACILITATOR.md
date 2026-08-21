# Guide Notes: Roofline Call

**Case:** Roofline Call · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Geometry / Fundamentals Of Geometry (5 new_coverage + 6 already-covered — see
`case.json.standards[]` for the exact ids; `geometry-parallel-lines`/`geometry-perpendicular-lines`
moved from new_coverage to already-covered on 2026-08-20 when Urban Planner, published the same
day, claimed both first)

Researched and margin-resolved 2026-08-19 (`margin_pct` = 14.81, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real construction-cost decision with a deadline,
not a worksheet. Name the opener — "You are a drafter with a truss-shop cutoff in ninety minutes.
Your supervisor wants the number, not the vibe." Let the stakes land before moving to the Launch.

## Launch

Show both roof plans side by side (the same pair described in the Overview) with no numbers
labeled — just the shapes. Ask: "Which one do you think uses more lumber, just from looking at
it?" Do not confirm or correct answers here. Most rooms will guess the hip roof uses more — that
gut read is the trap, and it is worth recording out loud before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Colton on The Hip Wrap — the one everyone assumes costs
more?" Show of hands, both options, no discussion. Record the count — Close will ask them to vote
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which roof
looks nicer" or "which one is cheaper," but the case only grades one specific number: board-feet
of lumber per square foot of attic space. Push on it: "The client cares about wind performance and
looks. Colton's boss asked for a number. Are those even the same question?" If the room lands on
"the graded metric and the 'is it worth it' question are two different things" on its own, the case
is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "looks/performance" from "the graded number," ask them to name the actual
steps before touching the appendices: correctly identify vertex/ray/parallel/perpendicular on each
framing plan (D1), verify the birdsmouth cut angles are complementary (D2), find one acute and one
obtuse angle in the actual framing (D3), verify the hip's corner bisection (D4), and only then run
the full lumber takeoff (D5). Re-ask: "Is our question still the right one, now that we can see the
steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Appendix E's two Modeling Assumptions (MA1 the simple-cut time, MA2
the compound-cut multiplier) are stated, not sourced — no public per-cut timing study exists for
either. Ask which one changes the *graded* number if it moves. The honest answer is **neither** —
the graded board-feet-per-square-foot metric is pure geometry (footprint, pitch, lumber size,
spacing), and MA1/MA2 don't enter that calculation at all. Let a sharp Hero find this themselves
before confirming it — it is a genuine, useful finding, not a gotcha.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's vocabulary labels, D2's complementary-angle check, D3's
acute/obtuse identification, D4's hip-bisection check, and D5's takeoff together as a room,
cold-calling for D2 and D4 specifically — these are where a Hero who never actually computed the
pitch angle (arctan of rise over run) or never worked out that a hip bisects a 90° corner into two
45s will visibly struggle, which is useful information for the facilitator, not a moment to rescue.

**Facilitator-only geometry note.** Pitch angle = arctan(6/12) = 26.57°. Birdsmouth plumb cut =
26.57° (acute), level cut = 90° − 26.57° = 63.43° — complementary (D2). The ridge's interior roof
angle = 180° − 2(26.57°) = 126.87° (obtuse) — pairs with the plumb-cut angle as D3's acute/obtuse
example. The hip rafter bisects the building's 90° plan corner into two 45° angles that share the
hip's ray as a common side (adjacent) and sum to 90° (also complementary) — D4.

**Facilitator-only cost note.** Option A (Gable): 1,500.42 board-feet ÷ 1,248 sq ft = **1.20
BF/sq ft**. Option B (Hip): 1,278.20 board-feet ÷ 1,248 sq ft = **1.02 BF/sq ft**. Margin:
**14.81%**, Option B uses less lumber. This is decided entirely by geometry — the tapering jack
rafters and the shorter hip-side ridge genuinely cost less total lumber than running full-length
common rafters the entire 52 ft, even though Option B has four extra hip members and thirty-six
jack members the Gable Line never needs. The single biggest lever on this number, if a Hero wants
to argue with it, is the footprint's aspect ratio (a near-square building narrows the gap further
in B's favor; a very long, narrow building narrows it toward A) — not either Modeling Assumption.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Colton sends his board-feet numbers to his supervisor. She nods, then hands him something else:
the shop's labor log from the last hip-roof job they framed, next to the log from the last
gable-roof job. 'Board-feet is what the lumber yard bills you. This is what the crew bills you.'"

"Does the labor number change what Colton should actually recommend?"

**Facilitator-only: what the numbers actually do.** Using Appendix E's stated cut-time assumptions
(MA1 4 min/simple cut, MA2 3× that for a compound cut) at the real BLS carpenter wage ($28.51/hr):
material cost A = $804.45, material cost B = $685.31 (B still cheaper on material, tracking the
board-feet result). Labor cost A = $152.05 (80 simple cuts only), labor cost B = $311.71 (44 simple
+ 40 compound-cut members). **Total cost: A = $956.50, B = $997.02 — Option A is now cheaper by
4.06%.** **The twist flips the verdict, not just erodes it** — the option that wins on the graded
board-feet metric loses once labor is priced in. Do not hand this reasoning over unprompted; let a
Hero who took Anchor 4's finding seriously (that MA1/MA2 don't touch the graded metric) reason
toward exactly why: those assumptions were always about a *different* number than the one they were
graded on.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the labor log change your vote — or does it just tell you
the number you were graded on was never the whole story?" That distinction is the transferable
skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **The metric you're graded on isn't the metric that decides the job.** Board-feet-per-square-foot
   is real, sourced-adjacent geometry — and it is *not* what the shop actually bills the client for.
   Is that a flaw in the case, or a real lesson about which number a professional should actually be
   watching?
2. **Fewer members, more lumber — vs. — more members, less lumber.** The Hip Wrap needs 40 more
   individual pieces (4 hips + 36 jacks) than the Gable Line needs extra pieces, and still uses
   *less* total lumber. Why does member count and material quantity move in opposite directions
   here?
3. **Whose 3×.** MA2's compound-cut multiplier is the case author's own estimate, not a timed study.
   Is a stated, reasoned multiplier trustworthy enough to flip a real recommendation — and what
   would you want to see before you trusted it more, or less?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both roof plans, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the graded number is the number that matters"* |
| 10:00–15:00 | Pressure-test the models — *"Whose framing plan is most fragile to a bad assumption?"* |
| **15:00** | **DROP THE TWIST** — the labor log, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (graded metric vs. real cost; members vs. material; whose 3×) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will look at "four roof planes and forty extra pieces" and conclude the hip roof must
use more lumber — treating member *count* as a proxy for material *quantity* because that is the
intuitive read. Watch for a pitch that asserts the hip roof "obviously" costs more material without
ever actually running D5's takeoff — it has not actually done the geometry, and the geometry says
the opposite.

## Socratic questions

1. The Hip Wrap needs 40 more individual framing members than the Gable Line, and still uses less total lumber. How can more pieces add up to less material — and what does that tell you about trusting a piece count as a stand-in for a board-feet count?
2. D4 asks you to verify the hip rafter bisects the building's 90° corner into two adjacent, complementary 45° angles. Why does a framer in the field actually need that fact to be true, not just interesting?
3. The graded metric (board-feet per square foot) never uses either Modeling Assumption in Appendix E. Does that make MA1/MA2 pointless to the case, or does it tell you something about the difference between "what you're graded on" and "what the client actually pays for"?
4. After the labor log lands, Option A is cheaper by 4.06% on total cost — a much thinner margin than the 14.81% material result. Which of those two numbers would you want in front of you if you were Colton's supervisor signing the check?
5. Colton has ninety minutes. What does he actually tell his supervisor — and does the labor log change the answer, or just how confident he should sound giving it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
B at Anchor 1 purely on "it looks nicer" and stays with B after the twist for a *different,
numbers-based* reason has genuinely moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "the assumptions don't touch the graded metric" finding landed as a discovery
  or had to be told outright.
- Whether the "more pieces, less material" trap was the actual sticking point, or whether D2/D4's
  angle arithmetic was the harder gate for most Heroes.
- Whether the twist's full flip (not just an erosion) felt earned or felt like the case moving the
  goalposts — worth listening for directly.

## Standards Touched On

Ray · Vertex · Acute Angle · Obtuse Angle · Parallel Lines · Perpendicular Lines · Complementary
Angles · Adjacent Angles

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a project deadline and a construction cost/labor
decision, not personal loss or hardship.
