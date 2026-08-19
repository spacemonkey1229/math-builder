# Guide Notes: Airplane Manufacturer

**Case:** Airplane Manufacturer · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (35 skills — polygon/circle
perimeter-area-circumference, decimal arithmetic, percent, elapsed time, comparison)

Legacy conversion, 2026-08-13, built from the original case study docx
(`source/Y2/Session 7/Airplane Manufacturer/Case Study_ Airplane Manufacturer.docx` +
`Guide Notes.docx`) onto the current 11-anchor ladder. Stout Aviation and its numbers are the
original case's own fictional scenario data, not a real external dataset — see
`case.json.legacy_conversion_note` for exactly what carried over verbatim versus what this
conversion had to add (turbine disk hole diameter, tooth-geometry reconciliation, nesting
convention).

## Intro

Frame the format: this is a real production-line decision with real dollars on the table, not a
worksheet. Broadcast the Stout Aviation logo if you have it. Name the opener — "One new machine.
Two parts it could make. You have until Friday to tell the CFO which one."

## Launch

Read the Background aloud through "Drew has seen an increased demand for inlet O-rings and
turbine disks" — stop there, before any Appendix numbers. Ask: "Just from the sale prices alone
— $5,498 for an O-ring, $657 for a turbine disk — does this feel like an easy call?" Do not
confirm or correct answers here. (This is the trap being set on purpose — let it sit.)

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who pitches turbine disks? Who pitches O-rings?" Show of hands, no discussion. Record the count
— Close will ask them to vote again. Expect most first votes to favor the O-ring on sale-price
alone; that is the trap working as intended.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "Is it just as simple as which part sells for more, or is
there something else we need to consider?"**

Push past "which one costs more to make" toward "which one makes Stout Aviation more money, at
the volume this one machine can actually produce in a week." Ask what "more profitable" would
even mean here — per part? Per week? Per sheet of aluminum?

## Anchor 3 — What is the process?

**"If we just go look at sale price and nothing else, we'll know the answer — is that the right
process?"**

Walk toward Challenge 3's actual sequence: net → cut length → cut time → parts per sheet → parts
per week → cost per part → profit per part → weekly profit → breakeven. Ask: "If we end up with a
higher sale price for one and a higher weekly volume for the other, how do we decide?"

## Anchor 4 — What don't we know?

**"Is there anything we don't know that's critical here? Do we need to assume anything?"**

Surface Appendix C's ambiguity directly: the turbine disk's source sketch calls its teeth
"equilateral triangles" but its own two labeled dimensions (28 in square, 36 in overall height)
don't actually produce equilateral teeth. Also surface that the center hole's diameter is never
labeled at all. Both are resolved in Modeling Assumptions (MA1, MA2) — but let the room notice
the gap before you point to the fix.

## Data Deep Dive

Work Appendix A (machine), B (O-ring), and C (turbine disk) together. Have Heroes physically sketch
each net before calculating anything. Flag the two decorative rows in Appendix A (maximum cutting
size 10m x 10m, laser power/type) — the machine's own ceiling is bigger than the sheets Stout
Aviation actually buys, and laser power/type never enters a Challenge-3 calculation. A Hero who
uses either in a formula has taken the bait on irrelevant data, which is itself worth naming.

## Twist — drop this at ~15 minutes into the discussion

Do not hand out or paraphrase in advance — deliver verbally, slowly: a parts-manufacturing
facility in China that Boeing sourced this component from has just burned to the ground. A Boeing
representative calls: can Stout Aviation start production immediately on the component Drew's
pitch chose? Boeing will pay **$114.00 per part**, plus a **$200,000 bonus** if Stout Aviation
delivers **more than 5,000 units within 10 days**. The machine can run up to 20 hours a day during
the sprint (not limited to 5 days a week, given the urgency) — but every load time and cut time
from Challenge 3 still applies. Ask: "Can you actually hit 5,000? Do you take the deal?"

The real, computed answer (see `sensitivity_model.py`) is that **neither option clears 5,000 units
in 10 days** — O-rings reach only 1,302 (26% of target), and turbine disks reach 4,760 (95% of
target, tantalizingly short). This is the twist's real teeth: even the *better* production option
falls just short of the bonus threshold, forcing a genuinely open question (take the guaranteed
$114/part revenue anyway? try to negotiate the 10-day window? decline?) rather than a clean yes/no.

**Soundness check (done during authoring, not just claimed here):** the twist's 5,000-unit
shortfall holds under both a *sequential* reading of Modeling Assumptions MA1–MA4 (apply tooth
geometry, then hole size, then nesting, then wage, one at a time, recomputing after each) and a
*simultaneous* reading (apply all four at once from the stated case.json values). At their stated
values, MA1/MA2 change the turbine disk's cut time and material cost by single-digit percentages
and do not touch parts-per-sheet (set by the 36in x 36in bounding box, not by tooth/hole
precision), and MA3/MA4 scale both options' capacity roughly proportionally — so no ordering of
these four assumptions *at their stated values* moves either option's 10-day unit count across the
5,000 threshold. Verified directly in `sensitivity_model.py`'s `evaluate_twist()`.

`sensitivity_model.py`'s own `FLEX` sweep (Tier 2 probe 5, +-50% stress test, a different and
harder check than the soundness check above) finds **two** dials, out of the three currently in
scope (`disk_hole_d_in`, `wage_per_hr_per_employee`, `twist_sprint_days`), where an arbitrary
+-50% perturbation crosses the 5,000-unit threshold (corrected 2026-08-18 -- `disk_overall_h_in`
was removed from probe 5's scope on 2026-08-18, since it is Appendix C's own cited sketch
dimension, not a stated modeling assumption; an earlier draft of this note listed it as a third
flip dial before that rescoping):

1. `disk_hole_d_in` at -50% (9in -> 4.5in, current base): a smaller hole raises turbine-disk
   throughput to 5,040 units -- just over the 5,000 threshold (bonus met).
2. `twist_sprint_days` at +50% (10 days -> 15 days): a longer sprint window alone pushes turbine
   disks to 7,210 units (bonus met); this one isn't a Modeling Assumption at all, it's a flex of
   the Twist's own stated sprint length.
3. `wage_per_hr_per_employee` at either +-50% does not move either option's unit count at all --
   wage affects cost/profit, not physical throughput.

Both real findings are legitimate, expected Tier 2 findings about the *model's* sensitivity to
these stated dials, not a contradiction of the soundness check above — the case's actual stated
values (28in square / 36in overall height / 9in hole / 10-day sprint) are the ones that matter
for running this case with students, and none of MA1-MA4 at their *stated* values (not flexed)
moves either option's 10-day unit count across the 5,000 threshold, which is what the soundness
check verifies.

## Immediate recommit

Quick re-vote right after the twist, no discussion yet: does the twist change your Challenge 3
pick? (For most Heroes it shouldn't — the twist applies to whichever component they already
chose — but it's a good gut-check moment before the deep dive.)

## Deep conflict — three threads (20–30 min)

1. **Volume thread.** 6 O-rings/sheet vs. 35 turbine disks/sheet (Modeling Assumption MA3). Have
   Heroes physically draw the grid nesting on grid paper for both parts before trusting the
   division.
2. **Margin thread.** The O-ring's $4,870 bending/shaping cost against its $5,498 sale price —
   what fraction of the sale price does that eat? (Answer: 88.6%.) Compare against the
   turbine disk, which has no bending cost at all.
3. **Breakeven thread.** Both options pay off the $136,500 machine in under a week under this
   case's numbers — ask what that implies about how load-bearing the *choice* between them really
   is for Stout Aviation's survival, versus how load-bearing it is for how much money the company
   makes on top of survival.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–0:03 | Intro — frame the format, broadcast the Stout Aviation logo |
| 0:03–0:07 | Launch — read the Background aloud, cold-call for a gut read on sale price alone, Anchor 1 vote |
| 0:07–0:15 | Anchors 2–4 — is sale price the right question, what's the process, what don't we know (tooth geometry, hole diameter) |
| **0:15** | **DROP THE TWIST** — the Boeing emergency order, delivered slowly |
| 0:15–0:20 | Immediate recommit — does the Twist change anyone's Challenge 3 pick |
| 0:20–0:40 | Threaded deep conflict — volume thread, margin thread, breakeven thread |
| 0:40–0:45 | Close, re-vote, reflection, Lessons Learned |

## The trap

**Heroes who stop the math at sale price ($5,498 vs. $657) will confidently pitch O-rings and be
blindsided twice** — once when D5's weekly-capacity numbers show the machine turns out roughly 6x
more turbine disks per sheet, and again when D6's profit numbers show the O-ring's $4,870 bending
cost eats nearly all of its price advantage per unit. The name for this trap: *mistaking price for
profit, and profit-per-unit for profit-per-week.* The case's own graded metric (D8, cutting
efficiency) already tips slightly toward turbine disks — a real but modest 15.4% edge — and a Hero
who carries the same math through to weekly gross profit finds the real gap is far larger (turbine
disks roughly 679% ahead), driven almost entirely by the bending cost and sale-price gap, not by
cutting efficiency at all. Stopping at any earlier step produces a confident, wrong-shaped answer.

## Socratic questions

1. "Your net for the O-ring shows a 72-inch outer diameter and a 54-inch inner diameter — if Stout Aviation could somehow fit 8 O-rings on a sheet instead of 6, would that alone flip your recommendation?"
2. "You computed the O-ring's $4,870 bending cost against its $5,498 sale price — if that bending cost were cut in half, does your recommendation change, and by how much does the weekly profit gap close?"
3. "The turbine disk falls just short of the 5,000-unit bonus target in the Twist's 10-day sprint — what single change to the case (more machine hours per day, a faster cutting speed, a different sheet size) would close that gap?"
4. "Both options pay back the $136,500 machine in under a week under this case's numbers — given that, why does the choice between turbine disks and O-rings still matter to Stout Aviation at all?"
5. "If Boeing's contract required Stout Aviation to deliver both an O-ring per airplane and a turbine disk per airplane, how would you use this case's numbers to figure out how many airplanes' worth of parts the company can supply in a week?"

## Close

Vote again. Ask: "We asked 'which part sells for more' at the start — was that the right
question?" "Was this case study challenging? Why?" "What math concepts were new to you, and how
did you take on that challenge?" "If you got a similar case next time, what would you do
differently?"

## Lessons Learned

*(Migrated from the original Guide Notes, 4/9/2021 discussion — preserved verbatim in spirit.)*
The original discussion was described as "a really advanced case study, mathematics-wise" that
produced strong high-level Hero questions, an improvement over prior case studies. The discussion
wasn't evenly split for-vs-against, but was still a strong session; the room worked through the
right question and the right process before the Twist (the Boeing emergency order) became the
bulk of the discussion — "should Drew say yes to Boeing's new order or not." That session also ran
with a shortened window (30 minutes lost to internet issues, discussion moved into Hero's Choice
time) — a useful data point for facilitators planning time for this case: the twist genuinely
carries the back half of the room's energy, so protect that time first if the session runs short.

## Standards Touched On

See `case.json.standards[]` for the exact spine ids (35 total). In plain language: polygon
perimeter and circle circumference (the cut path), polygon and circle area (material and scrap),
elapsed time (cut time, load time, breakeven time), the full decimal arithmetic chain (cost,
profit), percent (profit margin), comparing multiple values (the final recommendation) — plus four
skills genuinely new to the spine, forced by the turbine disk's own real shape: quadrilateral (its
square core), vertex (each tooth tip), concave (each inward notch between teeth), and irregular
polygon (the disk's full 12-pointed outline, which is not a regular polygon).

## Facilitator note — sensitivity

This case's graded primary metric is D8's cutting efficiency (minutes of laser time per square
meter of finished part): turbine disks come in at roughly 2.44 min/m^2 against the O-ring's
roughly 2.92 min/m^2, a real, honestly-close margin_pct of 19.4%. A much larger, separately
disclosed gap sits off that primary metric — real, computed weekly gross profit is roughly 679%
higher for turbine disks, well outside SPEC's usual ~20% balance target on any profitability
metric, driven almost entirely by two disclosed given inputs (the O-ring's $4,870 bending cost and
the ~8x sale-price gap), not by anything adjustable. Do not present the profit gap as a "close
call" going in; the discussion's value is in the trap (Anchor 1's vote almost always favors the
higher-sale-price O-ring before the room does the volume/margin math), not in a nail-biter margin
on profit. The 19.4% cutting-efficiency margin, by contrast, genuinely is close, and is the number
the balance test is graded on. See `case.json.sensitivity_note` and `legacy_conversion_note` for
the full disclosure, and SPEC.md §6 for the general sensitivity framing this note follows.

**Correction, 2026-08-13 (Tier 2 probe 5, re-run after FLEX rescoping and the MA2 re-estimate).**
`sensitivity_model.py`'s `evaluate()` previously modeled weekly gross profit, not D8 -- corrected
to compute D8 directly. MA1's `disk_overall_h_in` (36in) is the source sketch's own labeled
dimension, a cited measurement rather than an assumption, so it is no longer flexed by probe 5 (P5
tests stated assumptions, not cited data — see `sensitivity_model.py`'s inline note). MA2's
`disk_hole_d_in` was never labeled in the source and real turbine-disk bore sizing depends on
proprietary engineering analysis with no public standard to cite — it has been re-estimated from
10in to **9in**, the closest defensible public analogue (a general hole-in-plate stress-concentration
formula whose stated validity range tops out at a hole-to-width ratio of 0.3; 9/28 = 0.32, versus
the original 10/28 = 0.36), disclosed in MA2 as a **PROPRIETARY — ESTIMATED, one-time exception**,
not presented as equivalent to this case's actually-cited figures. The re-estimate raises the base
D8 margin from 15.4% to 19.4% — still inside SPEC's 20% cap, still genuinely close.

**Correction, 2026-08-18 (fresh P5 re-run against the current 9in base).** The prior note above
(and MA1/MA2's `case.json` sensitivity fields) claimed a +50% flex of the 9in hole still flips the
D8 winner to the O-ring. Re-running `sensitivity_model.py`'s FLEX sweep directly against the
current `PARAMS` (base D8: A=0.4094, B=0.3429, margin 19.4%) shows this is **no longer true** at
the current 9in base — that flip finding was carried forward from when the base was still 10in and
never re-verified after the re-estimate to 9in:
- `disk_hole_d_in` **+50%** (13.5in) → A=0.35, B=0.34, margin **1.2%**, disk still wins (no flip).
- `disk_hole_d_in` **-50%** (4.5in) → A=0.47, B=0.34, margin **36.4%**, disk still wins, but the
  margin now exceeds SPEC's 20% cap — a wide-margin finding, not a flip, but still disclosure-worthy.

So the honest, current P5 finding for MA2 is: **no winner flip in either direction** at the current
9in base, but the -50% direction breaches the balance cap. This is disclosed as a **Category X**
instability (a real, proprietary quantity that cannot be publicly sourced, best-effort estimated
from the closest public analogue) in `sensitivity_disclosure[]`, not silently dropped — a Hero
should be pushed to defend *why* 9in is a reasonable engineering estimate (citing the general
stress-concentration formula's boundary, S6), not just told "the real number is unknown."
Facilitators running this case should know the 19.4% D8 margin, while real and currently stable
under a +50% flex, does narrow to 1.2% at the top of that band — close enough that a sharp Hero
pressing on MA2 can make the disk's win feel much less comfortable, even though it never actually
flips.
