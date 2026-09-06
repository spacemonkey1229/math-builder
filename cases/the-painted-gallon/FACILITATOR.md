# FACILITATOR.md — The Painted Gallon

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Painted Gallon · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Geometry's Sphere, Cylinder, Radius, Volume, Surface Area, plus the sphere and
cylinder volume how-tos, the cylinder surface-area how-to, Measurement's compound-units how-to,
and Advanced Numbers' percent-of-a-number how-to (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-05); revised by a case-readiness QA pass (2026-09-06)
that fixed a real balance defect and three real citation defects — see the note below and
`case.json.readiness_revision_note`. All `{{NEEDS_SOURCE}}` placeholders are resolved: seventeen
figures are now real, cited sources (S1-S17), the town's required capacity is a disclosed Modeling
Assumption (MA2), and the gap between idealized and real geometry is a second disclosed assumption
(MA1). `case.json.balance.margin_pct` is a real, computed **14.0%** on the primary dollar metric —
but as of the 2026-09-06 revision, that dollar margin is no longer the whole balance story (see
"The margin," below).

**2026-09-06 balance fix, in brief:** independent cold-solve, both-sides, and twist QA probes found
the original case unbalanced — the Multi-Column won every dollar metric at every capacity, and the
win was mathematically invariant across a ±50% capacity flex. Argument A (future regulatory
exposure) was real but speculative, not a genuine present-day dilemma. The fix was NOT to retune
any sourced number — it was to go back to the same real Black & Veatch memo already cited for
S5-S16 and surface a second real, present-day fact it already contained: fabricator competition.
The Spheroid has 3 qualified fabricators at this capacity; the Multi-Column has exactly 1 (Caldwell
Tanks), and the memo's own Recommendations section calls this "added risk ... due to lack of
competition" (new source S17, new case.md Appendix G, new Challenge 2c). This is a real,
present-day procurement-risk axis, not a hidden or invented one — and it is what now makes both
options genuinely defensible.

**A structural redesign happened during research, and it is disclosed prominently** (see
`case.json.concept_redesign_note`): the approved concept specified Option B as a ground-standing
cylindrical "standpipe." No public, rigorously comparable cost/area dataset exists pairing a
spherical elevated tank against a ground standpipe specifically. Case-research instead found a
real, professional-engineer-sealed 2019 Black & Veatch cost study for the City of Lawrence, Kansas,
directly comparing a spheroid elevated tank against a **multi-column** elevated tank — a cylindrical
tank on multiple support legs — at the same site, capacity, and overflow height, with real
fabricator quotes for both. Every dollar and area figure in this case (S5-S16) now comes from that
one real study, rather than mixing real spheroid data with an invented standpipe cost. The
pedagogical target (sphere vs. cylinder at a fixed volume; less-area-but-costlier-to-build vs.
more-area-but-cheaper-to-build) is unchanged.

**Sensitivity note (SPEC §6):** ordinary civic/budget stress — a small town voting on a
tax-funded bond after a boil-water advisory. No illness, death, or family hardship.

## Argument for A — The Spheroid

**A's real case does not rest on the dollar metric at all — it rests on Appendix G's fabricator
competition data (S17), a real, present-day, sourced fact from the same engineering memo that
supplies every cost figure in this case.** The Spheroid has 3 qualified fabricators at this
capacity (McDermott, Caldwell Tanks, Landmark Structures); the Multi-Column has exactly 1 (Caldwell
Tanks). The real engineering firm's own memo states this means the Multi-Column has "no opportunity
for competitive bidding," and its own Recommendations section calls this "added risk ... due to
lack of competition" [S17] — the same firm whose numbers B leans on is on record flagging this as a
genuine reason to hesitate. This is NOT a "future regulation might raise costs" hedge (that was the
weaker, speculative version of this argument in the case's original draft) — sole-source risk is
already true today, at the moment Devon has to sign a recommendation. For a town six weeks into a
boil-water advisory with a hard Friday deadline, "the cheaper number on paper" and "the design least
likely to blow its price or schedule with no second bidder to check it" are genuinely different
questions, and a Hero can defend picking A on this basis without ever disputing B's cost numbers.

## Argument for B — The Multi-Column

The Multi-Column's simpler, non-specialized steel fabrication is dramatically cheaper to build per
square foot than the Spheroid's curved-knuckle single-shaft design — see "The margin" for the exact
derived rates — and that capital-cost advantage more than offsets the Multi-Column's larger area and
higher 60-year recoating bill. Under the case's own real, sourced numbers, B wins the graded dollar
comparison by a real but thin margin, and (per `sensitivity_model.py`) that win is stable across a
wide range of capacity choices — it is not a fragile, scenario-specific artifact. B's real,
quantitative case is Challenge 3 (D4)'s cost-per-square-foot work: the two designs are not built
from the same unit cost, and the gap between them is large enough to outweigh the raw area
difference in A's favor. B's honest response to Appendix G is not to deny the sole-source risk, but
to argue it is a real risk worth accepting: roughly $339,000 in documented 60-year savings (S15 vs
S9) is a concrete, quantified number, while the sole-source risk is real but unquantified — a
defensible Hero can argue a town this financially strapped should take the documented savings.

## The margin — real numbers, in full

`case.json.balance.margin_pct` = **14.0%** on the case's PRIMARY (dollar) metric only, comfortably
inside the SPEC §2 20% cap and consistent with this corpus's typical 10-15% band (e.g.
`cases/the-deferred-repair` at 13.0%). **This dollar margin is not, by itself, what makes this case
balanced** — B wins every dollar metric at every capacity (confirmed by the cold-solve, both-sides,
and twist Tier 2 probes). What makes the case balanced is that A has a genuine, real, sourced
advantage on a SECOND, non-dollar axis (Appendix G / S17) that the dollar metric does not capture.

- **Real per-square-foot build rate:** Spheroid = $2,048,000 [S7] / 16,500 sq ft [S5] =
  **$124.12/sq ft**. Multi-Column = $1,595,000 [S13] / 29,100 sq ft [S11] = **$54.81/sq ft** — the
  Spheroid costs a bit more than **2.26 times as much per square foot to build**.
- **Real per-square-foot 60-year maintenance rate:** Spheroid = $376,000 [S8] / 16,500 sq ft =
  **$22.79/sq ft**. Multi-Column = $490,000 [S14] / 29,100 sq ft = **$16.84/sq ft**.
- **Real total 60-year lifecycle cost per gallon (Table 2-5 of the source memo):** Spheroid =
  **$3.23/gal** [S10]. Multi-Column = **$2.78/gal** [S16].
- **Margin:** |3.23 − 2.78| / 3.23 = 0.45 / 3.23 = **13.9%**, rounded to **14.0%**.
- **Real fabricator count (Appendix G, S17):** Spheroid = 3 qualified fabricators. Multi-Column =
  1 qualified fabricator (sole source).

**Why this matters for the facilitator, specifically:** the concept sheet that approved this case
named a 6-10% target margin for the dollar metric. The real sourced data lands at 14.0% instead —
still well inside SPEC §2's actual 20% cap. `sensitivity_model.py` shows the recommendation (B wins
on cost) does **not** flip across a wide range of required-capacity choices (see "Twist," below) —
the 14.0% margin is a stable property of the two designs' real cost structures. The genuine
two-sidedness of this case comes from Argument A living on a different axis entirely (procurement
risk), not from the dollar margin being close.

## Five Socratic questions

1. The Spheroid has less real, sourced surface area than the Multi-Column (16,500 vs. 29,100 sq ft) — so why does it cost more per gallon over 60 years?
2. You divided each option's real capital cost by its real surface area in D4 and got two very different rates per square foot. What does that rate difference tell you about *how* each tank is actually built, that the raw dollar totals alone would not?
3. If a future regulation made recoating twice as expensive per square foot for every tank in the state, which of these two designs would that hurt more, and why — and would it be enough to flip your recommendation?
4. Appendix A requires the ballot to state one specific dollar figure, not a range. Which one number from this case would you actually put in front of voters, and is it the capital cost, the lifecycle cost, or something else?
5. `sensitivity_model.py` shows the Multi-Column keeps winning even if the required capacity were 50% larger or 50% smaller than assumed. What would have to change about the real per-square-foot rates themselves — not the capacity — for the recommendation to flip?
6. Appendix G shows the Multi-Column has exactly one qualified fabricator, and the real engineering firm itself flagged that as "added risk." Does a real number of dollars saved ever outweigh a real-but-unquantified procurement risk — and who should get to make that call, Devon or the town's elected officials?
7. Socratic Question 5 showed the dollar-cost winner doesn't change even at 50% more or less capacity. Appendix G's fabricator counts, though, are sourced specifically "at 0.5-0.75 MG capacity." If the town's real capacity turned out to be 1,125,000 gallons (the +50% case), would you still trust that the Spheroid has 3 fabricators and the Multi-Column has 1 — or is that a separate claim that would need its own new sourcing?

## The trap

**A learner who compares the two designs' raw surface areas alone — "the Spheroid has less
area, so it must be the cheaper, smarter choice" — will recommend the Spheroid, and will be
using a real, correctly computed number (Appendix B/C's real areas) to reach the wrong
recommendation on the graded metric.** This is the case's central trap: minimizing surface area
for a given volume is real, sourced, sound geometry (and is exactly what D1/D2's idealized
sphere-vs-cylinder math will independently show — the idealized sphere does come out with less
area than the idealized cylinder). But building that smaller-area shape well enough to hold water
safely at height requires far more specialized, slower, costlier fabrication per square foot, and
that fabrication-cost gap is large enough to overwhelm the area advantage on the case's actual
graded dollar metric. A pitch that never completes D4's real cost-per-square-foot division, or
that treats "less area" as automatically meaning "cheaper," has fallen into this trap even if its
area arithmetic is completely correct.

**A second, later trap (found by a Tier 2 trap-check probe, 2026-09-06): treating D6 as a
box-checking afterthought.** D1-D5 are heavily scaffolded — each sub-step forces the actual
arithmetic and makes "less area = cheaper" hard to sustain by the time a Hero reaches a
recommendation. D6 (the fabricator-competition response) has no comparable scaffolding — it is a
bare "3-5 sentences," and a hurried student who has already "solved" the case via D5's dollar
numbers can answer it with a token sentence ("sole-source is a risk, but it doesn't change my
recommendation") without ever genuinely weighing Appendix G against the savings. This is arguably
the MORE common failure in graded written pitches specifically, because D1-D5's scaffolding largely
inoculates students against the area-intuition trap by the time they write D6, while D6 itself has
no scaffolding at all. **Facilitator move:** do not accept a D6 answer that states a position
without engaging the actual trade-off — press with "you said sole-source risk doesn't change your
recommendation; what would it take for it to? Is there ANY dollar amount of savings too small to
justify sole-sourcing?" A Hero who cannot answer that question has not actually done D6, regardless
of what their 3-5 sentences say.

## Twist

Not a scripted mid-discussion reveal — the twist here is structural, and it lives in the gap
between D1/D2's idealized geometry and D4's real cost data. Facilitators should treat the moment a
student notices "wait, the shape with LESS area costs MORE per gallon" as the twist moment, and can
manufacture it directly with Socratic Question 1 if no student raises it unprompted. A second,
quieter twist is available via Question 5: cold-calling the room with "what if the town actually
needed twice the capacity?" and revealing (via `sensitivity_model.py`) that the recommendation does
not change — this is a genuine finding about *why* the margin is stable (both options' costs scale
the same way with size), not a scripted reveal of new information. A third twist, best held until
after D4/D5 have settled into a "B obviously wins" mood, is Appendix G: reveal the fabricator-count
data and Socratic Question 6 only once the room has committed to a cost-only recommendation — the
moment a purely least-cost recommendation gets genuinely contested on other real, sourced grounds.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: a boil-water advisory, a ballot deadline, and a state law that only accepts one
number. This is a real municipal engineering decision dressed as a geometry worksheet, not the
other way around.

### Launch

Read the Overview aloud. Stop at "Devon opens a blank spreadsheet and starts typing." Ask the
room: "Before you've seen a single number, which shape do you already assume is the cheaper
build — the sphere or the cylinder? Why?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "Spheroid or Multi-Column — show of hands." Record the split. Expect a strong
early lean toward the Spheroid on aesthetics/intuition ("less material, must be cheaper") — that
lean is the trap forming in real time.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which shape looks more efficient" toward "which shape is cheaper to actually
build and maintain, at this specific real-world capacity." Let the room sit with the fact that
"less surface area" and "less real cost" are not automatically the same claim.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix B/C/D's numbers, get the room to state the comparison method out loud:
solve for each shape's missing dimension (D1), compute idealized surface area (D2), convert to a
per-gallon rate (D3), then compare real dollar cost per square foot (D4) before ever comparing a
single lifecycle dollar figure (D5). Re-ask: "Now that we have a process, is 'which shape has less
area' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknown explicitly: this fictional town's exact required capacity (MA2) is
an authored scenario choice, not a number anyone measured for this specific town. "Does that
matter for which design wins? Test it." (This is where `sensitivity_model.py`'s capacity-flex
finding lands well if introduced here rather than saved for the very end.)

### Data Deep Dive

Now open Appendices A-D. Run D1-D5 as a room, or have groups report out. This is also the moment
to run Socratic Questions 1-3.

### Twist

Once D2's idealized areas are on the table and a recommendation has started to form around "the
Spheroid has less area," run Socratic Question 1 directly, then walk the room through D4's real
cost-per-square-foot division. Let the room discover that the design with less area is not the
design with the lower cost.

### Close

Reveal Appendix G (fabricator competition) before the final vote if it has not already surfaced.
VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind — a different capacity, a different cost rate, or the fabricator-competition data?"

### Lessons Learned

Two transferable ideas, not one. First: minimizing a physical quantity (surface area, for a fixed
volume) is real, sound geometry, but it is not automatically the same thing as minimizing
real-world cost — the conversion factor between "less material" and "less money" depends on how
hard that material is to work with, and that factor can be large enough to reverse the naive
conclusion. Second: the cheapest option on a single graded metric is not automatically the
objectively correct recommendation — a real decision-maker (here, the same engineering firm whose
own numbers make B look obviously cheaper) can have a real, sourced reason to weigh a second,
harder-to-quantify factor against the dollar figure, and a good pitch has to engage with that
factor rather than treat "lowest number wins" as the whole analysis.

### Standards Touched On

Sphere, Cylinder, Radius, Volume, Surface Area; How to find the volume of a sphere; How to find
the volume of a cylinder; How to find the surface area of a cylinder; How to convert an amount
with compound units; How to find the percent of a number.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00-8:00 | Position defense: "Convince us your shape is the smarter build, not just the more elegant one" |
| 8:00-20:00 | Data Deep Dive — build D1's dimension solve and D2's idealized surface-area comparison as a room |
| 20:00-30:00 | Build D3's per-gallon rate and D4's real cost-per-square-foot comparison; confirm the 14.0% margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 1: the Spheroid has less area but costs more — why? |
| 30:00-38:00 | Pressure-test the recommendation: run Socratic Question 5's capacity-flex test live, confirm it does not flip; then reveal Appendix G's fabricator-competition data and run Socratic Questions 6-7 (including the scope caveat — S17's fabricator counts are only sourced at 0.5-0.75 MG, unlike the dollar-cost invariance, which was tested to ±50%) |
| 38:00-45:00 | Close, re-vote, D5's ballot-number recommendation, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12-20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6-11)** | smaller room | Anchors 2-3 combine into one pass; D1-D2's geometry solve runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1-2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the D4 cost-per-square-foot comparison still runs in full |
