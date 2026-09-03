# FACILITATOR.md — The Plaza Bid

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Plaza Bid · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Geometry/Quadrilaterals And Polygons (Hexagon, Octagon, Regular Polygon, Sum of the
Interior Angles of a Polygon Theorem, and the matching how-to) + Basic Operations/Factoring
(Greatest Common Factor family) + Advanced Numbers/Percents (Percent, how to find the percent of a
number) — see `case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-01) — all 11 `{{NEEDS_SOURCE}}` tokens closed (6
SOURCED, 5 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `9.9` (see Balance section below), well inside SPEC §2's ~20% cap.
Not yet run through `case-qa`; treat the numbers as sourced-and-computed but not yet
QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **Stone & Tile Shoppe, Inc.** (stoneandtileshoppe.com) — a real online tile retailer. Both
  Appendix C's hexagon tile (Daltile Color Wheel Mosaic, Arctic White) and Appendix D's
  octagon-and-dot tile (Daltile Octagon & Dot 6501) are real, currently-listed products from the
  same retailer and the same manufacturer (Daltile), fetched live on 2026-09-01. This is the
  cleanest possible same-supplier price comparison the case could ask for.
- **A real, load-bearing geometric fact discovered during research, not assumed going in:** the
  hexagon tile's manufactured sheet is 11⅝″ × 10¼″ — an irregular rectangle that does NOT divide
  the plaza's whole-foot dimensions evenly. The octagon-and-dot tile's manufactured sheet is
  exactly 12″ × 12″ (1 sq ft) — a perfect square that divides any whole-foot plaza dimension with
  zero remainder. This is the real mechanism behind the case's D3 waste computation, and it is the
  opposite of the naive intuition a Hero is likely to bring in from D1 (see the wrong-path discussion later in this guide).
- **makecalcs.net / Angi / HomeGuide / EstimationPro** — real, independently operated tile-cost
  and installation-cost guidance sites. None of them publish an exact numeric premium for
  hexagon-vs-square-grid mosaic labor, but all confirm the same qualitative direction (small,
  intricate tile takes longer to install) — this qualitative-only evidence is exactly why MA4 (the
  numeric premium itself) is a disclosed Modeling Assumption, not a citation.

## Intro

Frame the format: this is a real fixed-price bid decision, due at the end of the week, where
guessing wrong either loses the contract or loses the firm money on every job it wins. Name the
opener — "You are the estimator whose number goes on the bid. Get it too high, you lose the job to
a competitor. Get it too low, your firm eats the difference for six months." Mention, once, that
this is exactly the math professional tile estimators, contractors, and quantity surveyors do
before every real bid — not an invented classroom exercise.

## Launch

Show the two tile samples and the two patterns exactly as the Overview describes them — hexagon
vs. octagon-and-square — with no prices or waste numbers yet. Ask: "Just from looking at these two
patterns, which one do you think wastes more material once you have to cut it to fit a rectangular
plaza?" Do not confirm or correct. Most rooms will guess the octagon-and-square needs more cuts
(more shapes, more seams) — record the guess; the Data Deep Dive will test it directly.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the client's preferred octagon-and-square pattern, even
though Marcus's boss wants the hexagon?" Show of hands, both options, no discussion yet. Record the
count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'wastes material'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which shape tessellates,"
but push on what "tessellates with zero gaps" (D1) actually buys you in a REAL, finite, rectangular
plaza: "A hexagon tessellates the infinite plane perfectly. Does that mean it wastes zero material
when you tile an actual 45-by-30 rectangle with real manufactured tile sheets? What's different
between the infinite-plane math and the real bounded job?" If the room lands on "the plane math
tells you about the *interior*, not what happens at the *edges*, and real tile ships in
pre-manufactured sheets of a fixed size that may or may not fit those edges cleanly," the case is
working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which pattern is the mathematically 'purer' tessellation" from "which
pattern actually costs less to install on this specific plaza," ask them to name the actual steps
before touching the appendices: prove both patterns' vertex geometry (D1); find the largest
staging block using GCF (D2); compute real cut-waste for both options against the plaza's actual
sheet sizes (D3); build the total installed cost table, materials and labor both (D4); and decide,
using all of that, which pattern to bid (D5). Re-ask: "Is our question still the right one, now
that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: the exact numeric labor premium for installing a hexagon mosaic
pattern versus a clean square-grid pattern is NOT published anywhere as a specific percentage —
every real source found (Appendix F) only confirms the *direction* (mosaic/small tile takes
longer), not a number. Ask which of the case's open figures is actually load-bearing for the
recommendation. The honest answer: MA4 (the 15% hexagon labor premium) is the single most
load-bearing assumption in the whole case — it is the one number that, if it moved far enough
(see the sensitivity section below), would flip which option wins.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's tessellation proof, D2's GCF staging-block computation,
D3's cut-waste table, and D4's cost table together as a room, cold-calling for D3 specifically —
this is where a Hero who assumed the hexagon (the "purer" tessellation) automatically wastes less
material will have to reckon with Appendix E's real numbers: Option A's real computed waste (10.5%)
is actually *higher* than Option B's (9.1%), because the octagon-and-square's manufactured sheet
is a perfect 1-sq-ft square that fits the plaza's whole-foot dimensions with zero rounding waste,
while the hexagon's real manufactured sheet size does not.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, once Appendix F is walked: "Marcus's boss picked the hexagon because it's 'one
shape, simpler to install.' The real numbers say the hexagon pattern is actually MORE
material-wasteful than the client's two-shape pattern — the octagon-and-square's manufactured tile
sheet happens to be a perfect square that fits the plaza's dimensions with zero leftover, while the
hexagon's sheet doesn't. But Marcus's boss's intuition about *labor* turns out to be right: the
one-shape hexagon pattern is still the cheaper bid overall, not because it wastes less material —
it doesn't — but because it's real, sourced dollars-per-square-foot difference (32% cheaper tile,
Appendix C vs. D) survives even after both its higher waste percentage and its labor premium are
counted against it."

"If your first intuition about which shape 'wastes more' was backwards, what does that tell you
about which of the two variables — material waste, or price-and-labor — was actually doing the
work in this decision the whole time?"

**Facilitator-only: what this does and doesn't change.** This does not change D4's totals — it
reframes WHY Option A wins. A Hero whose D5 memo argues "hexagon wins because it wastes less
material" has gotten the right answer for the wrong reason and should be pushed to correct the
memo's own logic, not just its conclusion.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just fair" (Anchor 2 — what does "tessellates with zero gaps" actually buy you in a bounded, real plaza?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface MA4 as the load-bearing open figure. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call D3's waste table specifically. |
| **25:00** | **DROP THE TWIST** — the hexagon actually wastes more material, not less; labor and price are what actually decide it. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — your geometry intuition, or your bid recommendation?" |
| 30:00–40:00 | Threaded deep conflict — see the two named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **"Tessellates with zero gaps" is a fact about the infinite plane, not about Marcus's plaza.**
   D1's proof is airtight for the idealized, unbounded tessellation — but Appendix E shows the real
   waste comes from the plaza's *finite rectangular edges*, where the manufactured sheet's actual
   size (not the idealized hexagon shape) is what matters. Push: "Could a case exist where the
   hexagon really does waste less? What would have to be true about the sheet size or the plaza's
   dimensions for that to happen?" (Answer: yes — if the hexagon sheet's dimensions divided the
   plaza's dimensions evenly the way the octagon sheet's do, D1's zero-gap fact and D3's real waste
   fact would point the same direction instead of opposite ones.)
2. **A close margin is still a real decision, not a coin flip.** 9.9% is not a landslide — Marcus
   is choosing to bid a number that beats the alternative by less than $2/sq ft on a plaza where
   getting the number wrong either loses the contract or costs the firm money. Push: "If you were
   Marcus, would a 9.9% margin feel comfortable enough to bid with confidence, or would you want to
   double-check MA4 (the one number that could flip it) before signing off?"

## The trap

Heroes will treat D1's "hexagon tessellates the plane with zero gaps" as automatically meaning
"the hexagon wastes the least material on this job" — without checking Appendix E's actual sheet
sizes against the plaza's actual dimensions. The real numbers say the opposite: Option A's real
computed waste (10.5%) is higher than Option B's (9.1%), because the octagon-and-square's
manufactured sheet is a perfect 1-sq-ft square that fits any whole-foot plaza dimension with zero
rounding waste, and the hexagon's isn't. A Hero who never separates "which pattern is the
mathematically purer tessellation" from "which pattern's *specific manufactured product* wastes
less material on *this* plaza" will get D3 backwards.

## Socratic questions

1. Your D1 proof shows a regular hexagon tessellates the plane with zero gaps. Does that proof, by itself, tell you anything about how much material gets wasted cutting tile to fit a real, finite, rectangular plaza? Why or why not?
2. Appendix E shows the hexagon pattern actually has a *higher* real waste percentage than the octagon-and-square pattern. What specific fact about the two products' manufactured sheet sizes explains that, and why doesn't D1's tessellation math predict it?
3. MA4 (the 15% hexagon labor premium) is the only number in this case that isn't backed by a specific published figure. If MA4 turned out to be 0% instead of 15%, would your D5 recommendation change? What if it turned out to be 40%?
4. The margin between the two options is 9.9% — real, but not huge. What would you need to see to feel confident enough in that number to actually sign a fixed-price bid based on it?
5. Marcus's boss favors the hexagon for a reason that turns out to be only half right (it wastes more, not less, but it's still cheaper overall). Has that ever happened to you — being right about the conclusion but wrong about the reason? Why does it matter, for a bid Marcus has to defend later if the client's committee pushes back?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the twist
should be pressed to explain the move using D3/D4, not just the twist's reveal.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Hexagon · Octagon · Regular Polygon · Sum of the Interior Angles of a Polygon Theorem · How to
find the measure of an interior angle of a polygon given the other angles · Greatest Common Factor
· How to find the greatest common factor of a set of numbers · Percent · How to find the percent of
a number

## Balance argument (SPEC §2)

**Argument for A (The Regular Hexagon Pattern).** Its total installed cost, $17.71/sq ft, is real
and computed from a real, live, same-supplier tile price (32% cheaper per sq ft than Option B, S1
vs. S2) — and that price advantage survives even though Option A's *own* computed waste percentage
(10.5%) is higher than Option B's (9.1%), and even after a 15% mosaic-installation labor premium
(MA4) is applied on top of it. A single repeating shape is also simpler for the crew to lay out and
for Marcus to defend to the client's committee if questions come up later.

**Argument for B (The Octagon-and-Square Combination Pattern).** It is the client's stated design
preference, its manufactured sheet is a perfect 12″×12″ square that fits the plaza's dimensions
with genuinely less structural waste than Option A's irregular hexagon sheet (9.1% vs. 10.5%,
Appendix E — a real, computed, sourced fact), and it needs no labor-premium assumption at all
(Appendix F) — its cost estimate rests on fewer stated assumptions than Option A's does.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 9.9`. **Winner: Option A, The
Regular Hexagon Pattern.** Option A totals $23,911.67 ($17.71/sq ft); Option B totals $26,539.65
($19.66/sq ft). margin_pct = (19.66-17.71)/19.66 × 100 = 9.9%. Well inside SPEC §2's ~20% cap — no
retune needed. Full arithmetic trail: `case.json.balance.margin_note`, reproduced and sweepable in
`sensitivity_model.py`.

**What this means for facilitation.** The case's genuine tension is real on two separate axes that
point in *opposite* directions from what a Hero's first intuition predicts: the "purer"
tessellation (hexagon, D1) turns out to have the *higher* real cut-waste (D3), and the option with
the numerically higher tile price and higher waste (hexagon) still wins on total cost, because its
real, sourced price-per-square-foot advantage is large enough to absorb both. The room's real work
is untangling which of D1, D3, and D4 is actually driving the D5 recommendation — not assuming any
one of them settles it alone.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine small-business bid-estimating math — no subject-matter sensitivity flag
applies. The case does carry real financial stakes for the fictional protagonist (his firm's
contract and six months of margin), which is exactly the kind of grounded, real-world stake SPEC §0
calls for, not a flag-worthy sensitivity.

## Sensitivity model — quick reference (see sensitivity_model.py for the full sweep)

MA4 (hexagon labor premium) is the case's real fulcrum: at 0% premium, Option A's margin widens to
~16.8%; the winner does not flip until the premium rises to roughly 37% — more than double the 15%
value actually used, so the stated recommendation is fairly robust to reasonable disagreement about
the exact premium, but a Hero who wants to argue MA4 should be pushed to name a real number and
defend it, not just gesture at "it feels like it should be higher." MA3 (base labor rate) does not
flip the winner across its full published range ($3–$15/sq ft) — it scales both options' labor cost
together without changing their fixed 15% relative gap.
