# Guide Notes: Plaza Pavers

**Case:** Plaza Pavers · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Heroes Academy
**Standards:** Geometry / Transformations (partial) + Geometry / Quadrilaterals And Polygons
(partial) + Basic Operations / Factoring (GCF pair) — all `new_coverage` (see `case.json.standards[]`
for the exact ids)

Researched and margin-resolved 2026-08-12, **revised same day** after Tier 2 adversarial QA found
the base cost model used an undisclosed interior/border blend and a per-paver retail price instead
of Appendix D's real market range — both fixed; see the Revision note in case.md's balance-argument
block. Current `margin_pct` = 16.07 (see `sensitivity_model.py`, `case.json.derived`). This file is
re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real bid, not a worksheet. Name the opener — "You
are the senior designer of record. Your boss just told you it's your name on this one, not his.
The portal closes at five." Let the stakes land before moving to the Launch.

## Launch

Show both elevation boards side by side (the same pair described in the Overview) with no prices
labeled — just the two patterns. Ask: "Which one do you think costs more to build, just from
looking at it?" Do not confirm or correct answers here. The point is a gut read before anyone
touches a formula.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Priya on the Weave Pattern — the expensive-looking one?"
Show of hands, both options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'costs more'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which pattern
is cheaper," but D5 has three separate legs that don't move together: material, cutting labor, and
waste. Push on it: "Priya isn't pricing one number. She's pricing three, and they don't move
together. What are they?" If the room lands on "material vs. labor vs. waste" on its own, the case
is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has split "cost" into its legs, ask them to name the actual steps before touching
the appendices: check which candidate shapes can even tile alone (D1), prove the chosen pattern's
layout is genuinely repeatable (D2), work the border-cut angle math (D3), fit the real modules to
the real plaza footprint via GCF (D4), price both out against the target (D5). Re-ask: "Is our
question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix G's five Modeling Assumptions (MA1a/MA1b the Weave
Pattern's material rate and premium, MA2 the plaza's exact footprint, MA3 the cost target, MA4 the
waste factors, MA5 the twist's curved-edge cutting growth) are all
stated, not sourced — no manufacturer publishes a public price for the octagon+square combination,
and Kessler Plaza itself is fictional. Ask which one actually changes the recommendation if it
moves (MA1b — see Data Deep Dive), and which ones don't move it much (MA2, MA4 — the sensitivity
sweep in `sensitivity_model.py` keeps the margin in a 14.8%-17.3% band across every flex).

## Data Deep Dive

Now, and only now, the numbers. Walk D1's tessellation check, D2's transformation proof, D3's
border-cut angle work, D4's GCF-based module fit, and D5's cost comparison together as a room,
cold-calling for the border-cut missing-angle step specifically (D3) — this is where a Hero who
treated "sum of interior angles" as a formula to memorize rather than a tool to apply will visibly
struggle, which is useful information for the facilitator, not a moment to rescue.

**Facilitator-only geometry note.** D1 has a genuine "aha" hiding in it: regular pentagons,
heptagons, nonagons, decagons and dodecagons all fail the alone-tiling test (their single interior
angle never divides 360° evenly — 108°, ≈128.57°, 140°, 144°, 150°), but the rhombus and the kite —
neither one regular, neither one with equal angles — always pass, because *any* quadrilateral's
four interior angles sum to exactly 360° by the same theorem, which is exactly the angle total
needed at one point. If a Hero notices this and asks "wait, so any four-sided shape works?", that
is the case rewarding real curiosity, not a tangent to shut down.

**Facilitator-only cost note.** Option A: $16.66/sq ft, clears the $18.50 target. Option B: $19.86/sq
ft, **over target by about $1.36/sq ft**. The single biggest lever is MA1b (a 10% material premium on
the octagon+square set, retuned down from an initial 20% after that value pushed the +50%-flex
margin over SPEC's own 20% instability threshold). Flexed +/-50% at its current 10% value, the
margin holds in a 14.8%-17.3% band, Option A cheaper throughout. This is a genuinely stable result,
not a coin flip dressed up as a dilemma — and because the target is explicitly not a hard
disqualifier, the real tension is not "which number wins" but "is historic match worth defending
anyway, on a bid that costs more than the published target."

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. Priya's phone buzzes. The city just approved restoring
Kessler Plaza's original center fountain — the one the 1962 photo shows, half-buried under asphalt
this whole time. It's round, and it sits dead center in the plaza."

"Both patterns now need extra cut pavers ringing a circle they weren't built to fit. Priya has
about sixty seconds before the print shop closes to decide whether this changes her bid."

"Does it change your recommendation — and can you say, in general terms, which pattern's cutting
cost is likely to grow *faster* as the amount of curved edge to fit grows, without doing the full
arithmetic over again?"

**Facilitator-only: what the numbers actually do.** `sensitivity_model.py`'s `evaluate_twist()`
models the Hex Grid's more-numerous-but-smaller cut pieces growing cost more slowly than the Weave
Pattern's fewer-but-larger cut pieces (MA5, a stated assumption — the case gives no fountain radius):
Option A moves from $16.66 to $16.83/sq ft (+1.0%), Option B from $19.86 to $20.25/sq ft (+2.0%) —
the gap widens slightly under this stated assumption, it does not close. **The twist does not flip
the verdict; it mildly reinforces it**, which is itself worth surfacing: not every
twist needs to threaten the leading option to be a real test — a twist that makes Heroes re-justify
a position that turns out to still hold is testing whether they can tell the difference between "I
was right" and "I got lucky." Do not hand this reasoning over unprompted; let a Hero who did D3/D4
carefully reason toward it, and treat one who says "I'd need the curve's actual length to be sure"
as the strongest possible answer.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the fountain change your vote, or just your confidence?"
That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **Three cost legs, one number.** Material, labor, and waste don't move together, and D5 asks
   for all three broken out before totaling. Is it fair to compress them into a single "$/sq ft"
   figure for a bid decision, or does that hide information the commission would want to see
   separately?
2. **Whose preference, whose target.** The commission's memo asks bidders to honor history
   "responsibly, within the published target cost" — and Option B doesn't stay within it. Who decides
   whether "responsibly" ever licenses going over — the firm submitting the number, or the
   commission reading it?
3. **The pentagon that almost worked.** Several candidate shapes failed the tiling test by a
   little, and some (rhombus, kite) passed it by construction but were rejected anyway, for a
   completely different reason. Is "the math says no" ever different from "the math says not with
   this one shape alone" — and did D1 actually force that distinction, or let a Hero blur it?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both boards, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us it's worth going over target, not just prettier"* |
| 10:00–15:00 | Pressure-test the models — *"Whose cost number is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the fountain restoration, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (three cost legs; whose target; the pentagon that almost worked) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will notice the hexagon tiles a flat surface perfectly, assume Option A needs *zero*
cut pavers, full stop, and skip the border-cutting analysis in D3/D4 entirely. It is true for an
*infinite* plane. It is not true for a *finite rectangular plaza*: a straight border still slices
through hexagons at the edge, exactly as it does the Weave Pattern's border. Watch for a pitch that
reports one $/sq ft number with no material/labor/waste breakdown and calls the case closed.

## Socratic questions

1. Option B costs about $3.20 more per square foot than Option A. Why does that number matter enough to lose a bid over?
2. Option B comes in about $1.36/sq ft over the commission's own published target — is that the same kind of problem as "we don't like the pattern," or a different, harder one to defend, given the target isn't a hard disqualifier?
3. D1 proves the hexagon is one of only three regular polygons that tile a flat surface with zero gap — why does Option A still need any cut pavers at all once Kessler Plaza's actual rectangular border enters the picture?
4. Appendix G's MA1b (a 10% material premium for the octagon+square set) is the single biggest lever in this whole case, and it's an assumption, not a citation — what would you want to see before you trusted it, and what happens to your recommendation if the real premium is much higher?
5. The rival firm's cheap bid already clears the target — would a compliant-but-plain bid beat a historic-but-over-target one automatically, or is there a number the historic bid could still win at?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the room
already have the right structure built in?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the border-cut missing-angle problem (D3) was where most Heroes actually got stuck,
  versus the more mechanical per-shape divisibility checks in D1.
- Whether the rhombus/kite "any quadrilateral works" discovery landed as a genuine surprise or felt
  like a rules exception nobody explained.
- Whether the twist's "the gap widens, it doesn't close" framing produced real reasoning about
  what a stable result means, or just relief that the vote didn't have to change.

## Standards Touched On

Pentagon · Hexagon · Heptagon · Octagon · Nonagon · Decagon · Dodecagon · Rhombus · Kite · N-gon ·
Sum of the interior angles of a polygon theorem · Transformation · Translation · Symmetry · Line Of
Symmetry · Clockwise · Counter-Clockwise · Vertical Angles · Supplementary Angles · Greatest Common
Factor · How to translate a figure on the coordinate plane · How to reflect a figure across the
X-Axis · How to rotate a figure on the coordinate plane 90 degrees clockwise · How to find the
greatest common factor of a set of numbers · How to find the measure of an interior angle of a
polygon given the other angles

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are commercial and professional (a firm's bid, a junior
designer's first solo lead), not personal loss or hardship.
