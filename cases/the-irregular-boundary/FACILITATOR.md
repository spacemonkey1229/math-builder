# FACILITATOR.md — The Irregular Boundary

**Facilitator-only. Never copy any of this into `case.md`.**

## Subject-matter flag (SPEC §6)

None required. This is routine agricultural land-use and property-boundary math. The neighbor
dispute is explicitly disclosed in `case.md`'s Modeling Assumptions as a fictional scenario
anchored to real, current civil/property law (Neb. Rev. Stat. §34-301; *Mueller v. Bohannon*,
Neb. Sup. Ct. 1999) — it is not a protected-subject or personal-conflict narrative, and does not
need a discussion-lead content warning beyond that disclosure students will already have read.

## Argument for A — The Squared Block

The Squared Block's cost is a straightforward opportunity cost: the corner acreage outside the
pivot's basic circle simply sits idle. Against that, it has three real advantages: (1) zero added
guidance-line or fencing cost, since its boundary is the shortest, simplest, fully-convex shape
that fits the pivot; (2) zero legal exposure, because a boundary that never touches the disputed
strip cannot be read by the neighbor as asserting — or conceding — anything about that strip this
season; (3) it can be finalized today, in time for tomorrow's bank meeting, with no negotiation
required. The strongest quantitative form of this argument: multiply the corner acreage this
option leaves unplanted by the per-acre crop margin to get the raw acreage opportunity cost, then
show that this cost is smaller than Option B's combined guidance-line/fencing cost plus turning-
margin crop loss, once both are priced from Appendix C, D, and E.

## Argument for B — The Reclaimed Line

The Reclaimed Line's argument is that idle corner acreage is real, recoverable revenue — the
cited corner-waste figure (roughly 15% of a 160-acre quarter-section, per the FCSAmerica/Edible
Geography sourcing in Appendix A) is not a rounding error, and settling the boundary now, while
the dispute is still fresh, avoids a scenario where ten more years of the neighbor's pivot-tail
crossing could ripen into a legal right to keep crossing (Neb. Rev. Stat. §34-301). The strongest
quantitative form: (reclaimed acres × per-acre crop margin) compared directly against (added
perimeter × per-foot guidance-line/fencing cost) plus (turning-margin crop loss at each reflex
vertex, from Rahman et al. 2019) — if the acreage gain clears both cost terms, B wins on the
primary metric.

## The margin

**Computed post-research (facilitator-only — never copy into case.md).** Full derivation and
every sourced/assumed input is in `case.json`'s `balance.margin_basis` and `RESEARCH_LOG.md`.

**2026-09-01 update — canonical scenario decision.** A retune pass (see `RESEARCH_LOG.md`'s
retune entry and its 2026-09-01 scenario-decision addendum) fixed a structural bug in Option B's
geometry (the original single reflex vertex was a corner chamfer, which is perimeter-neutral for
a rectilinear boundary) and rebuilt Option B as a genuine 16-vertex, 6-reflex-vertex inward-notch
polygon. Under the retuned geometry, the case's margin is genuinely fencing-choice-dependent
between two equally real, sourced fencing options (Appendix C):

- Under **woven-wire fencing** ($1.51/ft — S6): margin = **14.5%**, under SPEC.md §2's ~20% cap.
  **This is now the canonical/headline scenario** (`case.json.margin_pct` = 14.5,
  `balance.margin_basis` built around this fencing choice).
- Under **high-tensile electrified fencing** ($0.70/ft — S7, the case's original central
  assumption): margin = 45.3%, over the cap. Retained as the fully disclosed sensitivity
  alternative in `balance.margin_pct_range` and `sensitivity_note` — not the headline figure.

Verified directly via `sensitivity_model.py`'s `evaluate()`: woven-wire fencing gives acres
reclaimed = 14.45, perimeter added = 3,224 ft, revenue gain $8,485.45, fencing+guidance cost
$6,480.24, turning-margin cost $776.50, net gain $1,228.70 (~$85/acre reclaimed), margin 14.5%,
**winner = B (Reclaimed Line)**.

**Winning option: B (Reclaimed Line), under both fencing choices.**

**`margin_pct` = 14.5** (canonical, woven-wire fencing) — under the ~20% cap. The 45.3%
high-tensile figure remains disclosed as the sensitivity alternative, not silently dropped.

**Why woven-wire was chosen as canonical, not high-tensile:** both fencing costs are real,
current-best-available sourced figures from the same Iowa State Extension document (Appendix C,
S6/S7) — neither is invented or reverse-engineered to hit the cap. Woven-wire happens to be the
pricier of the two real options, and choosing it as the case's primary/headline assumption is
what brings the case under SPEC.md §2's cap without inventing any number or further distorting
the geometry. This is a scenario-selection decision (which real fencing a farm-management company
would plausibly spec for a disputed-boundary line), not a data fabrication — see
`RESEARCH_LOG.md`'s 2026-09-01 note for the record of this decision.

**Judgment call already flagged in the retune, still true:** the underlying "shape has a cost"
pitfall is real and correctly modeled; the two fencing choices simply bracket a real range of
outcomes (14.5%–45.3%) rather than the case flipping winners. Nothing here required inventing new
geometry or new prices beyond the 2026-09-01 geometry retune already on record.

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: a real recommendation memo due end of day, a bank meeting tomorrow morning, and
a testy email thread with a neighbor — not a worksheet. Name the opener: "You are Renata Suh. Two
boundary files are open side by side. One is safe and smaller. One is bigger and picks a fight.
You have until end of day."

### Launch

Show the two boundary shapes with no numbers yet — a clean rectangle next to a lumpy, notched
polygon covering the same corner of the same field. Ask: "Just looking at the shapes, which one do
you think costs more to actually build on the ground — not to plant, to *build*? What would you
need to know to check that?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with the Squared Block — the safe, smaller one?" Count hands.
"And the Reclaimed Line — bigger, but picks the fight?" Count hands. Record the split.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump to "which one has more acres" — push instead: "More
acres of what, exactly, and does 'more acres' automatically mean 'more money'? What could make a
bigger shape cost you money instead of making you money?" The room should arrive at "we need to
price the shape, not just the area" before Anchor 3.

### Anchor 3 — What is the process?

Walk the room toward: classify each boundary's vertices as convex or reflex (D1/D2), identify the
disputed strip's shape (D3), compute acreage and perimeter for both (D4), price the perimeter and
the reflex-vertex turning loss (D5), then combine into a single dollars-per-acre recommendation
(D6).

### Anchor 4 — What don't we know?

Surface honestly: the exact vertex coordinates of both boundaries are modeled figures for a
fictional parcel (MA3), not a real GIS survey; the per-foot guidance-line cost (MA4) has no public
price list and is a stated assumption; the neighbor dispute itself is fictional, anchored to real
Nebraska boundary law (MA1). Ask: "Which of these, if it moved, would actually flip your Anchor 1
vote?"

### Data Deep Dive

Walk D1 through D6 together. Reveal Appendix A/B's real geometry, then Appendix C/D/E's real cost
figures, then the D6 combination: 14.45 acres reclaimed × $587.23/ac crop margin, minus 3,224 ft
of added perimeter × the fencing/guidance rate, minus turning-margin loss at 6 reflex vertices.
Cold-call specifically for whether a Hero correctly identified all 6 reflex vertices in D2 before
trusting their D5 cost total.

### Twist

Reveal that this case's own canonical fencing choice is a real, deliberate scenario decision, not
the only real option: under woven-wire fencing ($1.51/ft), the Reclaimed Line wins by 14.5%; under
the equally real, equally sourced high-tensile electrified fencing ($0.70/ft), it wins by 45.3%.
Ask: "Does the fencing choice change *who wins* — or only *by how much*? What kind of company would
plausibly choose the pricier option here, given the live boundary dispute?" This invalidates the
idea that there is one single "the margin" for this case without making either option's win
uncertain — B wins under both real fencing choices, but the size of the win is a genuine, disclosed
range, not a single number.

### Close

Re-vote. "Did we ask the right question at Anchor 2? Was this ever really about which shape has
more area, or about which shape's *cost of shape* was smaller than the acreage it bought?"

### Lessons Learned

- Area and perimeter are independent properties of a shape — a bigger-area boundary is not
  automatically a bigger-perimeter one, and here it's a much bigger perimeter, which is what
  makes the "more land is more land" pitfall actually bite.
- A reflex (concave) vertex is not just a labeling exercise — it is exactly where a real cost
  (turning-margin crop loss) attaches, so mis-classifying a vertex has a real dollar consequence,
  not just a wrong diagram.
- Two equally real, equally sourced inputs (two fencing types) can bracket a genuine range of
  outcomes without changing which option wins — that is a disclosed range, not an unresolved case.

### Standards Touched On

Geometry — Convex, Concave, Irregular Polygon, Quadrilateral, Parallelogram (new_coverage:
geometry-parallelogram; the other four are reinforcement, see `case.json.reinforcement_note`).

---

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation yet. |
| 3:00–10:00 | Position defense: "Convince us why it's worth it, not just bigger" (Anchor 2 — define the real question). |
| 10:00–15:00 | Pressure-test: process and open assumptions (Anchors 3–4) — what's real geometry, what's modeled, what's a stated cost assumption. |
| 15:00–25:00 | Data Deep Dive — D1–D6 together; cold-call the reflex-vertex classification specifically. |
| **25:00** | **DROP THE TWIST** — the fencing-choice range (14.5% vs. 45.3%), delivered slowly. |
| 25:00–30:00 | Immediate recommit — does anyone reverse? "Did the winner change, or just the size of the win?" |
| 30:00–40:00 | Threaded deep conflict, two named threads: (1) area gained vs. shape cost; (2) legal-risk urgency (Neb. Rev. Stat. §34-301) vs. a fencing-choice-dependent dollar margin. |
| 40:00–45:00 | Close, re-vote, Lessons Learned. |

---

## Five Socratic questions

1. Your D4 table says the Reclaimed Line adds a specific number of feet of perimeter over the Squared Block — how much would the per-foot guidance-line cost have to drop before that added perimeter stopped mattering to your D6 recommendation?
2. You classified the disputed strip as a parallelogram in D3 — if it were shaped differently (say, a triangle tapering to a point instead of a constant-width strip), would that change how much acreage the Reclaimed Line actually gains, and would it change your area calculation?
3. D5 charges the Reclaimed Line for turning-margin crop loss at every reflex vertex you found in D2 — what happens to your D6 answer if Option B's real boundary has one fewer concave notch than you modeled? Does it flip the recommendation, or just narrow the margin?
4. If the reclaimed corner acres were a higher-value crop than corn or soybeans — potatoes, say — would your argument for Option B get stronger or weaker, and by roughly how much, using your own D6 formula?
5. Renata could delay this decision past tomorrow's bank meeting to negotiate directly with the neighbor first. What does your D6 number say about whether that delay is worth the legal risk named in Background?

## The trap

The plausible-but-wrong move: comparing raw acreage gained (Option B has more usable planted
acres) without pricing the *shape* of that gain. A Hero can correctly compute that the Reclaimed
Line captures more acres and stop there, concluding B obviously wins because "more land is more
land" — missing that a concave boundary carries two independent extra costs (perimeter-driven
guidance/fencing cost, and turning-margin crop loss at each reflex vertex) that scale with the
boundary's *shape*, not its area, and that neither of those costs shows up unless the student
correctly identified which vertices are reflex (concave) in D2. A student who mis-classifies
Option B as simply "bigger" rather than "bigger and more complex" will systematically overstate
its case.

## Sensitivity note (SPEC §6)

Declared post-research — see `case.json.sensitivity_note` for the full text. Updated 2026-09-01:
after the geometry retune, the margin is genuinely fencing-choice-dependent — 14.5% under
woven-wire fencing (S6, now canonical) vs. 45.3% under high-tensile electrified fencing (S7,
disclosed sensitivity alternative). Option B (Reclaimed Line) wins under both. The two
assumptions that would move the margin most are MA3 (Option B's reflex-vertex count/notch size)
and MA4 (the assumed guidance-line per-foot cost) — both are flagged as load-bearing in
`case.json.modeling_assumptions[]`.
