# Guide Notes: The Bandstand Angle

**Case:** The Bandstand Angle · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Geometry / Quadrilaterals And Polygons (10 skills, all reinforcement of a thin
group — see `case.json.reinforcement_note`; 0 new_coverage, honestly, per the 2026-08-17 T1-10
reinforcement carve-out) + 3 already-covered Advanced Numbers how-tos.

Researched and margin-resolved 2026-09-05 (`margin_pct` = 11.35, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real permit deadline with real money attached,
not a worksheet. Name the opener — "You are a volunteer engineer with a stamped drawing due
tomorrow morning and a $40,000 grant riding on it." Let the stakes land before moving to the
Launch.

## Launch

Show both frame plans side by side (the two shapes described in the Overview) with no numbers
labeled — just the polygons. Ask: "Which one do you think covers more of the lot?" Do not confirm
or correct answers here. Most rooms will guess by eye and get it roughly right (The Site Six is
bigger) — the real trap isn't about area, it's about the angle math, and it's coming.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Tomas on The Even Eight — the simple, symmetric one?"
Show of hands, both options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which one looks
nicer" or "which one is bigger." Push on it: "The case grades one specific number: covered square
feet per dollar of frame-plus-site-prep cost. Is 'more space' the same as 'more space per dollar'?"
If the room lands on "the graded metric and the 'is it worth it' question are two different things"
on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which looks bigger" from "the graded number," ask them to name the actual
steps before touching Appendix D: correctly classify each option's polygon and mark its vertices
(D1), find every interior angle using the sum theorem — the regular way for Option A, the
given-five-find-the-sixth way for Option B (D2), compute every hip rafter's run/rise/length with
the Pythagorean theorem (D3), classify one roof panel's quadrilateral shape in each option (D4),
and only then run the full cost takeoff (D5). Re-ask: "Is our question still the right one, now
that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Appendix E's five Modeling Assumptions are stated, not sourced (MA1
the constructed site geometry itself; MA2/MA3 the two cut-time figures; MA4/MA5 the two site-prep
rates). Ask which ones actually move the *graded* number if they change. The honest answer is
**MA2 through MA5 all do, to varying degrees — MA1 does not**, because MA1 defines the two shapes
being compared rather than a dollar figure layered on top of them. Let a sharp Hero find this
themselves before confirming it.

**Facilitator-only, recorded per Tier 2 Probe 5 (`case.json.sensitivity_disclosure[]`).** MA2/MA3
(the cut-time figures) do not flip the verdict or breach the 20% balance cap at any ±50% flex.
MA4/MA5 (the two site-prep rates) genuinely do — flexing either one far enough reverses the winner
and pushes the margin well past 20%. This is disclosed as a real, evidenced instability (Category
X: no real site-prep quote can exist for this constructed, non-real lot; both rates are good-faith
estimates anchored to the same sourced land-grading range, not eliminated by retuning), not hidden.
If a Hero pushes hard on "how sure are we about the site-prep numbers," that pressure is earned.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's polygon classification, D2's interior-angle theorem work,
D3's Pythagorean rafter-length work, D4's quadrilateral classification, and D5's takeoff together as
a room, cold-calling for D2 and D4 specifically — these are where a Hero who assumed the hexagon's
angles must all be equal (because a regular octagon's are) or who called both roof panels the same
kind of trapezoid without checking will visibly struggle. That is useful information for the
facilitator, not a moment to rescue.

**Facilitator-only geometry note.** Option A (regular octagon): interior angle sum = 1080°
(`180(8-2)`), each angle = 135° by regularity. Option B (irregular hexagon): interior angle sum =
720° (`180(6-2)`); five corners are given (108°, 132°, 121°, 143°, 116°, summing to 620°), so the
sixth, not-yet-resurveyed corner = 720 − 620 = **100°**. All six angles (108, 132, 121, 143, 116,
100) are under 180°, so Option B is convex — same as Option A. **The trap is assuming a shortcut
exists for Option B**: `180(n-2)/n` only works because Option A's angles are congruent by
regularity; Option B's are not, and dividing 720 by 6 to get "120° each" is simply wrong for an
irregular hexagon, even though 120° happens to be the *average*.

**Facilitator-only rafter-geometry note.** Option A: all 8 hip rafters share run = 12.988 ft, rise
= 6.494 ft (half the run, from the 6-in-12 pitch), length = √(12.988² + 6.494²) = **14.521 ft**,
identical every time. Option B: the six hip-rafter runs (14.0, 16.5, 12.0, 15.5, 13.0, 17.0 ft) each
give a different rise and a different length (15.6525, 18.4476, 13.4164, 17.3295, 14.5344, 19.0066
ft) — no two alike, because no two vertices sit the same distance from the frame's center.

**Facilitator-only quadrilateral note.** Both roofs rise to a small flat deck, so every roof panel
is a trapezoid: one polygon side at the bottom, the corresponding (shorter) deck edge at the top —
parallel because both run at the same constant pitch — and two hip-rafter segments as the legs.
Option A's panel legs are two of its eight *identical* hip-rafter segments, so by the octagon's own
symmetry the legs are congruent: an **isosceles trapezoid**. Option B's panel legs are two
*different* adjacent hip rafters (established in D3) — the legs are not congruent, so it is a
trapezoid but **not** isosceles. A Hero who assumes Option B's panel must also be isosceles because
"they're both trapezoids" has made exactly the same regular-vs-irregular mistake as the angle trap,
one level up.

**Facilitator-only cost note.** Option A: 195.70 total lumber ft = 195.70 board-feet (2×6 stock) →
material $102.03; labor (8 × 10 min simple cuts, MA2) → $38.83; site-prep (477.17 sq ft × $1.10/sq
ft, MA4) → $524.89; **total $665.74**; 477.17 sq ft ÷ $665.74 = **0.7168 sq ft/$**. Option B: 215.39
board-feet → material $112.29; labor (6 × 14.5 min custom cuts, MA3) → $42.22; site-prep (510.00 sq
ft × $0.95/sq ft, MA5) → $484.50; **total $639.02**; 510.00 sq ft ÷ $639.02 = **0.7981 sq ft/$**.
Margin: **11.35%**, Option B wins on the graded metric.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Tomas emails both drawings to the truss shop. The shop calls back: they have exactly one open slot
before the permit deadline, and it's sized for a single half-day batch-cut run. The Even Eight's
eight identical hips fit that slot easily. The Site Six's six unique hips — no shared pattern, each
one needing its own template and test-fit — don't."

"Does the shop's calendar change what Tomas should actually recommend?"

**Facilitator-only: what the numbers actually do.** Using Appendix E's cut-time assumptions plus
one-time setup overhead (pattern setup for A, a per-piece template-and-test-fit for B — these setup
minutes are facilitator-only, not printed in `case.md`): Option A's total shop time = 15 min setup +
8 × 10 min = 95 min = **1.5833 hr**. Option B's total shop time = 6 × 20 min template setup + 6 ×
14.5 min cutting = 207 min = **3.45 hr** — more than double. **The twist does not touch the graded
dollar metric at all** (it's a different metric, shop hours, not dollars-per-square-foot) — it
reveals that the option that wins on value doesn't necessarily win on time, and time is the one
resource the grant deadline doesn't forgive.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the shop's calendar change your vote — or does it just tell
you which risk you're accepting?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **The metric you're graded on isn't the only metric that matters.** Covered-square-feet-per-
   dollar is real, and Option B wins it by a real 11.35% — but the twist's shop-hours metric belongs
   to a professional Tomas can't ignore. Is that a flaw in the case, or a real lesson about which
   number a professional should be watching, and when?
2. **A bigger footprint bought with a fabrication premium.** Option B captures 6.9% more covered
   space and *still* wins on cost-per-square-foot, even after its non-identical rafters cost more
   to cut. Why doesn't the fabrication premium erase the space advantage here?
3. **Whose 45%, whose $1.10 and $0.95.** MA3's custom-cut premium and MA4/MA5's site-prep rates are
   all point estimates the case author chose inside a real sourced range, not the range itself. How
   much would you want to see change before you stopped trusting this recommendation?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both frame plans, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the graded number is the number that matters"* |
| 10:00–15:00 | Pressure-test the models — *"Whose angle math is most fragile to a bad shortcut?"* |
| **15:00** | **DROP THE TWIST** — the truss shop's calendar, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (graded value vs. shop time; space vs. premium; whose point estimates) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will try to shortcut Option B's interior angles the same way they found Option A's —
dividing 720° by 6 to get "120° each" — because that is exactly how the regular octagon's angles
work, and it feels like the same problem. It is not: the sum-of-interior-angles theorem gives the
*total*, and only a *regular* polygon's own definition (all sides and angles congruent) lets you
divide that total evenly. An irregular hexagon's angles must each be found from what's actually
given — here, the five surveyed corners and the theorem, not the average.

## Socratic questions

1. The sum of Option B's interior angles is 720°, the same theorem gives Option A's sum as 1080°. Why can you divide 1080° by 8 to get every one of Option A's angles, but you can't divide 720° by 6 to get every one of Option B's?
2. D4 asks you to classify one roof panel from each option as specifically as you can. What single fact from D3 tells you Option A's panel is an isosceles trapezoid and Option B's is not?
3. Option B captures 6.9% more covered square footage than Option A and still wins on the graded cost-per-square-foot metric by 11.35%, even after its fabrication premium is priced in. What would MA3's premium have to look like for that not to be true — and does knowing that change how much you trust the 11.35%?
4. After the twist, Option B needs more than double Option A's total shop time before the truss-shop cutoff. Does that change which option Tomas should recommend, or does it just change how he explains the risk?
5. Tomas has one night and a stamped-drawing deadline tomorrow morning. What does he actually tell the committee — and does the shop's calendar change the answer, or just how confident he sounds giving it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
The Site Six at Anchor 1 purely on "it looks bigger" and stays with it after the twist for a
*different, numbers-based* reason has genuinely moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the "you can't average an irregular polygon's angles" finding landed as a discovery or
  had to be told outright.
- Whether the isosceles-vs-plain-trapezoid distinction in D4 was a genuine "aha" or the harder gate
  for most Heroes, compared to D2's angle trap.
- Whether the twist's shop-hours reversal felt like a fair complication or like the case moving the
  goalposts — worth listening for directly.

## Standards Touched On

Octagon · Hexagon · Regular Polygon · Irregular Polygon · Convex · Quadrilateral · Trapezoid · Sum
of the interior angles of a polygon theorem · Pythagorean Theorem

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a volunteer project deadline and a construction
cost/timeline decision, not personal loss or hardship.
