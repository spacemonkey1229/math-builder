# Guide Notes: The Custom Die

**Case:** The Custom Die · **Tier:** T3 · **Band:** MS-stretch/HS-entry · **Studio:** Heroes Academy
**Standards:** Geometry / Visual Perceptibility (10 of 11 skills touched, 0 new — every one already
has n>=1 elsewhere in the corpus) + Geometry / Surface Area And Volume (4 skills, already covered)
+ Number Sense / Measurement And Data (`number-sense-depth`, the case's one true `new_coverage`
skill, `n=0` before this case). See `case.json.standards[]` for exact ids.

Researched and margin-resolved 2026-09-05, re-verified and re-derived 2026-09-06 after Tier 2
Probe 6 found Appendix D's Uline price had moved from $2.24 to $2.37/sheet (`margin_pct` = 6.39,
see `sensitivity_model.py`). This file is re-checked for drift at every readiness run (the
continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real tooling-commitment decision with no do-over
— once the die shop starts cutting steel, that shape is locked in for the whole production run.
Name the opener: "You have forty minutes and no second quote. Whichever box you approve is the one
they cut steel for tomorrow." Let the stakes land before moving to the Launch.

## Launch

Show both mockups side by side (the plain rectangular box and the flat, uncut die pattern for the
fitted wedge) with no numbers attached — just the shapes. Ask: "Just from looking at these, which
one do you think uses more cardboard?" Do not confirm or correct answers here. Most rooms guess
the plain rectangular box uses *less* cardboard because it looks simpler — that gut read is the
trap, and it is worth recording out loud before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Marcus on The Fitted Wedge — the pricier, harder-to-cut
box?" Show of hands, both options, no discussion. Record the count — Close will ask them to vote
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'wastes less'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which box looks
like it wastes less space," but the case grades one specific number: square inches of cardboard net
per cubic inch of Wedge shipped, tooling-amortized. Push on it: "Wasting less interior space and
using less cardboard sound like the same thing. Are they?" If the room lands on "wasted *volume*
and cardboard *cost* are two different measurements that don't have to move together" on its own,
the case is working as designed.

## Facilitator note — a live-priced source

Appendix D's material price (Source S1, Uline) is a real, live retailer SKU price, not a fixed
textbook constant — it moved from $2.24 to $2.37 per sheet between this case's initial research
(2026-09-05) and its Tier 2 re-verification (2026-09-06), a genuine one-day price change on the
supplier's own site. All figures below reflect the current $2.37 value. If re-running this case
later finds the price has moved again, re-derive with `sensitivity_model.py` before trusting any
number on this page — do not assume a live retailer price is frozen.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "wasted space" from "the graded number," ask them to name the actual steps
before touching the appendices: correctly name all six whiteboard candidates and explain why four
get rejected (D1), build a real dimensioned net for each surviving option (D2), compute net area
from the net itself — not from volume (D3), compute wasted volume separately (D4), and only then
combine net area with the amortized tooling cost (D5). Re-ask: "Is our question still the right
one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Appendix E's three Modeling Assumptions (MA1 the simple-die cost,
MA2 the complex-die cost, MA3 the expected order volume) are stated, not sourced — no public
per-company die quote exists, and MA3 is a business forecast, not a fact. Ask which one changes the
*graded* verdict if it moves. The honest answer is **all three matter, but MA3 matters the most** —
the crossover point where the two options tie is only about 16,230 units, well within range of a
number this bakery could plausibly hit. Let a sharp Hero find this themselves before confirming it
— it is a genuine, useful finding, not a gotcha.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's shape-naming, D2's net construction, D3's area-not-volume
material table, D4's wasted-space table, and D5's combined comparison together as a room,
cold-calling for D3 specifically — this is where a Hero who quietly computed material cost from
each box's *volume* instead of its *net area* will visibly struggle to explain why their ratio
doesn't match anyone else's, which is useful information for the facilitator, not a moment to
rescue.

**Facilitator-only geometry note.** Option A's net area is 102.375 sq in (rectangular prism,
2(LW+LD+WD) with L=6.25, W=3.25, D=3.25). Option B's net area is 79.914 sq in (triangular prism,
two triangular ends of 5.281 sq in each plus three lateral rectangles totaling 69.351 sq in, using
the hypotenuse 4.596 in from the two 3.25 in legs). Option B uses about 22% less cardboard by net
area — a real material win. But Option A's box wastes 39.02 of its 66.02 cubic inches (59.1%),
while Option B wastes only 6.01 of its 33.01 cubic inches (18.2%) — those two percentages (22% vs.
59.1%/18.2%) measure completely different things, which is exactly the trap: a Hero who conflates
"wastes less space" with "uses less material" will overstate how lopsided this case actually is.

**Facilitator-only cost note.** Amortized at MA3's stated 12,000 units: Option A's effective
footprint is 116.05 sq in per unit (102.375 material + 13.67 tooling-equivalent), Option B's is
123.96 sq in per unit (79.914 material + 44.05 tooling-equivalent — the pricier die dominates at
this volume). Divided by the fixed 27 cubic inches of Wedge: **A = 4.298 sq in/cu in, B = 4.591
sq in/cu in. Margin: 6.39%, Option A (the cheap-die box) wins** — the option that *feels* wasteful
in the room actually wins the graded number, at this volume.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Marcus's manager comes back from the retail buyer's office and drops a signed contract on the
table. 'It's not a trial order. They want forty thousand units a year, guaranteed.'"

"And it changes something else, too," the manager adds. "I already called the die shop. A trial
order only ever bought us until the next production run — that's why MA3 only ever counted twelve
thousand units. A signed annual contract is a different animal: they're not going to make us
re-open the tooling conversation every eight weeks anymore. The next real re-tooling decision isn't
the next production run. It's the next time this contract comes up for renewal — a full year out."

"Does that change what Marcus should approve tonight?"

**Say this reveal in full — both sentences, not just the volume.** This is not a new rule sprung on
the room; it is Appendix E's own stated definition of the re-tooling horizon ("whatever order
volume Marcus's team can actually count on with confidence at the moment of the decision"), applied
to a fact that just changed. Before tonight, the *confidently-known* volume was only the next
8-week production window (12,000 units), because there was no purchase commitment beyond that. Now
that a signed, guaranteed annual PO exists, the confidently-known volume is the full 40,000 units
the contract guarantees for the year — not a *rate* converted back down into the old 8-week window
(which would give roughly 6,154 units and NOT flip the verdict — a sharp Hero may try this reading
and should be told directly that Appendix E's horizon rule rules it out, not left to guess).

**Facilitator-only: what the numbers actually do.** Re-running the same formula at 40,000 units
instead of 12,000: Option A's tooling-equivalent per unit drops to 4.10 sq in (450/price-per-sqin/
40000), giving an effective footprint of 106.48 sq in and a metric of 3.944 sq in/cu in. Option B's
tooling-equivalent drops to 13.22 sq in, giving an effective footprint of 93.13 sq in and a metric
of 3.449 sq in/cu in. **B = 3.449, A = 3.944 — Option B now wins by 12.54%.** The twist fully
reverses the verdict, not just erodes it, because the tooling gap that favored A at low volume
shrinks faster (relative to the metric) than Option B's real material savings ever go away. Do not
hand over *why* this happens unprompted; let a Hero who took Anchor 4's finding seriously (that MA3
is the most load-bearing assumption) reason toward exactly why: a bigger order volume spreads *any*
tooling cost thinner, and once tooling stops dominating, the option with less wasted material and
less net area was always going to win. (The horizon itself — 40,000 units, not a converted rate —
is not something to make them guess at; state it, per the reveal script above.)

## Immediate recommit

Re-vote immediately. Ask by name: "Does the signed contract change your vote — or does it just tell
you the number you were graded on was never going to hold at this bakery's actual growth rate?"
That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **"Wastes less space" and "uses less material" are not the same claim.** Option B wastes far
   less interior volume (18.2% vs. 59.1%) than it saves on material (22% less net area). Why don't
   those two numbers match, and which one should actually drive a packaging decision?
2. **A forecast is doing more work than either die quote.** MA3's 12,000-unit estimate is the
   single most load-bearing number in this whole case — more than either die's price. Is it
   reasonable for a business decision to hinge harder on a volume guess than on a real quote?
3. **The trap that isn't really a trap.** Once you know material cost tracks net area, not volume,
   is Option A's win at 12,000 units actually surprising — or does it only feel surprising because
   the room's gut instinct (Launch) was never checking the right number to begin with?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both mockups, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the graded number is the number that matters"* |
| 10:00–15:00 | Pressure-test the models — *"Whose die-shape is most fragile to a bad assumption?"* |
| **15:00** | **DROP THE TWIST** — the signed 40,000-unit contract, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (waste vs. material; the forecast doing the real work; the trap revisited) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will look at Option A's box — a wedge of visibly empty air above every slice — and
conclude it must also use more cardboard, treating wasted *interior volume* as a stand-in for
*material used*, because that is the intuitive read. The actual driver of material cost is the
box's flat, unfolded **net area**, which does not move in lockstep with interior volume once the
two shapes stop being similar. Watch for a pitch that computes "material cost" from either box's
volume instead of running D3's net-area table — it has not actually done the geometry, and in this
case the two numbers tell almost opposite stories about how lopsided the comparison really is.

## Socratic questions

1. Option B wastes about a third as much interior space as Option A (18.2% vs. 59.1%) but only uses about a fifth less material (22%). Why don't a shape's wasted-space percentage and its material-savings percentage have to move together, and what does that tell you about using one as a stand-in for the other?
2. D1 asks you to reject four of six whiteboard candidates. Which property — face count, edge count, or the shape of the cross-section itself — actually does the rejecting, and would a different product shape (say, a cylindrical roll instead of a triangular wedge) reject a different four?
3. The graded metric flips entirely once the order-volume assumption (MA3) climbs high enough — a range this bakery, at its current growth rate, could plausibly reach within a year. Does that make the case's margin a real finding, or a number with an expiration date?
4. After the signed contract lands, the winner reverses to the other option by a bigger margin than the original comparison. Which of those two numbers would you want in front of you if you were the one signing the die-shop's invoice?
5. Marcus has forty minutes and no second quote. What does he actually tell the die shop, and does the contract news change the honest answer, or just how confident he should sound giving it?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
B at Anchor 1 purely on "it looks like it wastes less" and stays with B after the twist for a
*different, numbers-based* reason has genuinely moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "MA3 is the most load-bearing assumption" finding landed as a discovery or had
  to be told outright.
- Whether the "wasted space is not the same as material used" trap was the actual sticking point,
  or whether D1's shape-naming was the harder gate for most Heroes.
- Whether the twist's full flip (not just an erosion) felt earned or felt like the case moving the
  goalposts — worth listening for directly.

## Standards Touched On

Net · Face · Edge · Pyramid · Prism · Cone · Cylinder · Sphere · Surface Area · Volume · Depth ·
How to name a 3-D shape · How to draw the net of a 3-D shape · How to find the surface area of a
prism · How to find the volume of a prism

## Facilitator note — sensitivity

None required (SPEC section 6) — the stakes here are a business tooling decision and a production
deadline, not personal loss or hardship.
