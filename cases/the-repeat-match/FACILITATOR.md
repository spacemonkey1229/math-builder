# Facilitator Notes: The Repeat Match

**Case:** The Repeat Match · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Geometry/Transformations — Congruent, Similar, Translation, Symmetry, Line Of
Symmetry, Dilation, Scale Factor, Transformation, Reflection, Rotation, Clockwise,
Counter-Clockwise, and all 7 of the group's how-to skills (see `case.json.standards[]` for exact
ids). This is a **second-pass/redundancy case**: `new_coverage[]` is deliberately empty — every
skill in the group already has `n>=1` — because 14 of the group's 20 skills sit at exactly `n=1`,
a single point of failure the pipeline flags as its own priority. See `case.json.reinforcement_note`
for the verified counts.

`margin_pct` is computed: **17.0%** (Same-Grain Marker costs 17% more than Mirror-Match, using a
with-nap yardage premium of 17% chosen toward the conservative end of the sourced 15-25% range
[S3/S4]; the original draft used the range's midpoint, 20%, which sat exactly at the SPEC's ~20%
review threshold — retuned to 17%, still fully within the same sourced range, to clear the cap
cleanly rather than sit on the boundary). Winning option on pure cost: **B, the Mirror-Match
Marker**, at every point in the sourced range. See `case.json.balance` for the full computation and
`cases/the-repeat-match/RESEARCH_LOG.md` for how each figure was sourced or, where unsourceable,
adopted as a stated Modeling Assumption, and for the addendum documenting this retune.

---

## Intro

Frame the format before anything else: this is a case study, not a worksheet. Yuki Alvarez has
two decisions that are both about to become permanent — a CAD file the engraving room is waiting
on, and a marker layout the cutting room is waiting on — and neither one can be undone once it's
made. Name the opener: "Yuki has a green crosshair that lands in two different places depending on
the order she does two things in. One of you is about to be Yuki. Which order do you build it in,
and what do you do about the fabric underneath it — before you've seen a single number?"

## Launch

Show the two build orders side by side if at all possible — even a simple hand-drawn version of an
asymmetric arrow shape, rotated-then-flipped next to flipped-then-rotated, makes the "these are not
the same picture" point physically, before any coordinate math happens. Read the Overview aloud,
stop at "lines both decisions up side by side on her screen," and go straight into Anchor 1 without
commentary.

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Same-Grain Marker — the safe one, the one that costs
more?" Count hands. "And the Mirror-Match Marker — the cheaper one, the one that has to be built
exactly right?" Count hands. Write the split on the board and leave it there for the whole session;
it's the number the Close comes back to.

## Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?**

"Is this actually a question about which order you rotate and reflect something in, or is it a
question about how much extra fabric you're willing to pay for?" Let students say "both" — then
push: "Which one is Yuki actually being judged on?" Make them find it in Background themselves:
total fabric cost for the production run, under whichever layout she recommends. "Is that the
right question? If the Mirror-Match Marker is cheaper and the geometry is fully checkable, why
would anyone ever recommend Same-Grain?" Deliberately let the confusion grow — a group that thinks
"checkable" means "guaranteed correct in practice, every time, by every operator" has not yet found
the real problem. "Wow, this is a harder problem than it looked."

## Anchor 3

**WHAT IS THE PROCESS?**

"If we go through this — trace the registration point through both orders, check the symmetry of
the motif, price both layouts — how do we actually decide?" Walk the room toward: determine which
composition order is geometrically correct for this seam axis (D1/D2), understand why that
correctness is only possible because the motif has no line of symmetry (D3), then compare the two
layouts' total fabric cost (D6). "Is our question still the right one, now that we can see the
process? What would make this process fail?" (A good answer: if the seam-axis or cutting-angle
figures in Appendix A turn out different from what a student assumed — hold onto that thread, it
resurfaces in Anchor 4 and again in the Twist.)

## Anchor 4

**WHAT DON'T WE KNOW?**

"Do we need to make assumptions? Which ones are load-bearing?" Walk `case.json.needs_source[]` as
a group: the registration-point coordinates and seam-axis figures in Appendix A (internal to
Yuki's own CAD file — there is no outside source for these, so they will likely become stated
Modeling Assumptions rather than cited numbers), the Reggiani and second-printer repeat ranges in
Appendix B (real, sourceable from a manufacturer spec sheet), the patent's buffer language in
Appendix C, the nap-yardage-penalty range in Appendix D, the marker-efficiency baseline in
Appendix E, and the fabric-cost and run-size figures in Appendix F. "Which of these, if it moved,
would flip your Anchor 1 vote?" Good answers: the nap-yardage-penalty percent (Appendix D) and the
marker-efficiency baseline (Appendix E) — both directly set how large the Same-Grain premium
actually is, which is the whole cost side of the tension.

## Data Deep Dive

Now the numbers. Walk the class through `case.json.balance.margin_basis`: total fabric cost for the
production run under each layout = base yardage per unit × fabric cost per yard × production run
size, with Same-Grain adding the with-nap yardage premium (Appendix D) on top of that same base.
Have the room build this table themselves before revealing the totals.

| Quantity | Value | Source |
|---|---|---|
| Base yardage per unit (flip-allowed) | 3.0 yd | MA10 (order-specific assumption) |
| Fabric cost | $39.00/yd | S10 (Discovery Fabrics, retail proxy — MEDIUM) |
| Production run size | 5,000 units | MA9 (order-specific assumption) |
| With-nap yardage premium | 15-25% sourced, 17% used | S3/S4 (yardage-calculator sources — MEDIUM), qualitatively confirmed by S5 (Sewing & Craft Alliance Guideline 4.120 — HIGH) |
| **Mirror-Match total cost** | 3.0 × 39.00 × 5,000 = **$585,000** | derived |
| **Same-Grain total cost** | 3.0 × 1.17 × 39.00 × 5,000 = **$684,450** | derived |
| **margin_pct** | **17.0%** (range 15-25% across the sourced premium) | derived |

Push the room on why MA9 (run size) and MA10 (base yardage) never actually move the *percentage* —
they're common multipliers on both totals, so they change the dollar figures but cancel out of the
margin. What genuinely moves the margin is the with-nap premium (Appendix D) alone — a good moment
to ask "which of the numbers on this table would you have guessed didn't matter, and were you
wrong?" Appendix E's real Patagonia/Vietnam data (82% average utilization, 16-21% waste — UCSB Bren
School, 2024, HIGH confidence) is worth surfacing too, even though it's not a term in this specific
formula: it's the room's evidence that marker-efficiency variance in this range is realistic, not
invented for the case.

## Twist

At roughly the 15-minute mark, drop this: *"New information just came in from the cutting-room
foreman. He ran a test cut of the Mirror-Match layout on the older of the shop's two markers this
morning — and on that older marker, the cutting-angle rotation is not quite what Yuki's CAD file
assumed. The registration point that was supposed to land on the seam's match line landed about a
quarter-inch off it instead."*

That is the case's own real geometric point turned into a live discussion beat: the composition
order that is correct for one cutting-angle assumption is not automatically correct for a
different one. *"You now have 60 seconds. Are you changing your plan — or not?"*

The follow-up is the whole point: **"What just broke in your original model? Was the rotate/reflect
order actually wrong — or was an assumption about the cutting angle wrong, and the order that was
correct for that assumption is no longer correct for this one?"** A model that treated "the correct
order" as a fixed fact, rather than a fact that depends on the seam-axis and cutting-angle inputs in
Appendix A, was implicitly assuming those inputs would never change.

## Close

**VOTE AGAIN.** Compare the new count against the Anchor 1 tally still on the board. "Did we ask the
right question at Anchor 2? What math was new to you today, and how did you attack it?" Surface that
the *base* case (no twist) compares a guaranteed-safe, costlier layout against a cheaper layout that
depends on getting one geometric fact exactly right — and that the twist does not prove Mirror-Match
was the wrong call, only that "exactly right" depends on inputs that can themselves be wrong.

## Lessons Learned

- Rotation and reflection do not commute — order matters, and "it's just two simple moves" is
  exactly the pitfall that makes a novice CAD operator's 50/50 guess feel safe when it isn't.
- A geometric fact being *checkable* is not the same as a process being *foolproof* — the twist
  shows that the correct answer depends on real-world inputs (the cutting angle) that can
  themselves be measured wrong, which is a different failure mode than the math being wrong.
- Congruent and similar are not interchangeable words for "the same shape" — a motif that is
  rotated, reflected, or translated stays exactly the same size (congruent); a motif that is
  resized to fit a different machine's repeat range is a genuinely different size (similar), and
  mixing the two up would misprice the second printer's material needs.
- A single trade guideline's stated requirement ("nap must run the same direction") can force a
  real, quantified cost penalty on an otherwise cheaper process — "the safe option costs more" is
  not a vague intuition here, it is a specific, sourced percentage.

## Standards Touched On

Geometry/Transformations — Congruent, Similar, Translation, Symmetry, Line Of Symmetry, Dilation,
Scale Factor, Transformation, Reflection, Rotation, Clockwise, Counter-Clockwise, and all 7 how-to
skills in the group (see `case.json.standards[]` for exact ids). `new_coverage[]` is empty by
design — see the reinforcement note above and in `case.json`.

---

## Argument for A — The Same-Grain Marker

Forbidding reflection anywhere in the marker removes all risk tied to the rotate/reflect
composition-order question — there is no order to get wrong if nothing is ever mirrored — and it
guarantees the nap runs the same direction on every panel, avoiding the visible color-shading
defect the Sewing & Craft Alliance's own guideline exists to prevent. That safety is not free: it
costs a real, sourced yardage premium over a flip-allowed layout, on top of the baseline
marker-efficiency loss every layout already carries. The strongest version of this argument treats
that premium as insurance against a failure mode — a mismatched seam on cut, unrecoverable fabric —
whose cost, if it happened, would likely exceed the premium many times over.

## Argument for B — The Mirror-Match Marker

The yardage premium the Same-Grain layout requires is avoidable, and the geometry that makes it
avoidable is not a guess — it is fully determined by the seam axis and cutting angle in Appendix A,
which a competent CAD build can check directly rather than assume. The strongest version of this
argument treats the composition-order question as solved, not risky: once Yuki knows which axis the
marker's chevron-match line sits on, exactly one of the two build orders is correct, every time, for
that panel — the risk is in a careless build, not in the geometry itself.

## The margin

`margin_basis` (recorded in `case.json.balance`): total fabric cost for the production run under
each layout = base yardage per unit × fabric cost per yard × production run size, with Same-Grain
adding the with-nap yardage premium (Appendix D) on top. **Computed: margin_pct = 17.0%**
(Mirror-Match $585,000 vs. Same-Grain $684,450, using a with-nap premium of 17%, chosen toward the
conservative end of the sourced 15-25% range; sourced range 15-25%). **Winning option: B, the
Mirror-Match Marker**, cheaper at every point in that range. The range's top end (25%) still clears
the SPEC's ~20% threshold and that is disclosed rather than hidden, but the value actually used
(17%) clears the cap comfortably — the original midpoint value (20%) sat exactly on the boundary and
was retuned. See `case.json.balance.computation` for the full arithmetic and `RESEARCH_LOG.md` for
how each input was sourced or assumed, and for the addendum documenting the retune.

## Five Socratic questions

1. You've shown that rotating-then-reflecting and reflecting-then-rotating send the registration point to two different places on the panel — why does that fact alone not tell you which build order is correct, and what in Appendix A actually decides it?
2. The Same-Grain Marker guarantees a correct nap direction with no geometry to get wrong; the Mirror-Match Marker is cheaper but depends on one composition-order decision being exactly right. If you were grading Yuki's recommendation, would you weight "guaranteed safe" and "cheaper but checkable" the same way, and why or why not?
3. Your D5 diagram shows the rotated/reflected/translated copies are congruent to the master motif, but the copy resized for the second printer is only similar to it — what would go wrong with your cost or yardage calculations if you treated that resized copy as congruent instead?
4. The back-yoke panel reflects across a horizontal seam instead of the front panel's vertical one — why does that mean D2 needed a completely different reflection procedure than D1, instead of just the same one applied to a different picture?
5. If the fabric had no nap at all — a plain, non-directional face fabric — would the Same-Grain-vs-Mirror-Match dilemma still exist? What part of Yuki's decision depends specifically on the fabric being napped, and what part would remain even if it weren't?

## The trap

**Most learners will treat "rotation and reflection are both just simple moves" as meaning they
can be applied in either order with the same result** — and will pick whichever order is easier
to draw first in D1, without ever checking it against the seam axis in Appendix A. That is the exact 50/50 guess the case is
built to catch: rotation and reflection do not commute in general, and a build that gets the order
backward sends the registration point to the opposite side of the panel from where the seam's
match line actually is. A pitch that jumps straight to the cost comparison in D6 without first
showing, in D1 and D2, *why* one order is correct for these two seams has skipped the part of the
case that makes the Mirror-Match recommendation defensible at all.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just cheaper (or safer)" (Anchor 2 — define the real question) |
| 10:00-15:00 | Pressure-test the models: "Whose plan is most fragile if the cutting angle turns out different than assumed?" (Anchor 3 and 4 — process and assumptions) |
| **15:00** | **DROP THE TWIST** — the older marker's cutting-angle mismatch, delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict — two named threads: (1) composition-order precision vs. cost-avoidance, (2) a proven geometric non-commutativity fact vs. a negotiable, sourced yardage-cost estimate |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Sensitivity note (SPEC §6)

**NONE.** This case carries no SPEC §6 sensitivity — it is routine textile-manufacturing
engineering (which marker layout policy a print-repeat engineer recommends for a jacket print
run), with no protected subject matter.
