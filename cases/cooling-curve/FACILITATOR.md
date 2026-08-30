# FACILITATOR.md — The Cooling Curve

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no marker comment for this by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object.*

**Case:** The Cooling Curve · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Geometry — How to find the volume of a pyramid, How to find the volume of a cone,
Surface Area (see `case.json.standards[]` for exact ids).

**Status:** Researched and computed 2026-08-27. All 12 `{{NEEDS_SOURCE}}` tokens in `case.md` are
closed (`RESEARCH_LOG.md`). The D1–D4 arithmetic is done and recorded below and in
`case.json.balance`.

**Balance flag, read before you facilitate:** on the primary metric (watts dissipated per dollar
of fin manufacturing cost), the Cone Standoffs beat the Pyramid Array by **18.4%** — inside SPEC
§2's ~20% cap. **This case was retuned 2026-08-29** (see `case.json.balance.margin_note` for the
full derivation): MA5 (pyramid mold cost) was revised from $12,000 to $7,000, grounded in real
tooling-cost-complexity benchmarking research showing a 30–50% cost premium per added mold
complexity feature is realistic, versus the original untested 2.4x ratio against MA6's $5,000 cone
mold. The retune narrows the margin honestly — it does not flip the winner (the Cone Standoffs
still win) and does not erase the real cost story (a 40% pyramid-mold premium over the cone mold
still remains, reflecting that a four-face mold really is harder to tool than a shape-of-revolution
mold). The mold-cost gap (MA5 vs. MA6, now $2,000 rather than $7,000) still outweighs the
surface-area gap (the pyramid only exposes ~12.6% more surface than the cone), just by a
defensible, inside-cap margin rather than an overwhelming one. The discussion below is built so the
room's real tension is the *mold-reuse* twist and the *what would have to be true to flip it*
framing — with the primary-metric race now genuinely closer, that framing is even more load-bearing
than before.

## Intro

Frame the format before anything else: this is a real tooling sign-off with a hard deadline, not a
worksheet. Name the opener — "You are Advait Rao, standing on the mezzanine with two cold-plate
samples in your hands, a chiller loop humming behind you, and a mold order that locks in whatever
you spec next for the life of this hardware generation." Let the stakes land before moving to the
Launch.

## Launch

Show Appendix B's two fin geometries side by side — the Pyramid Array's four flat faces, the Cone
Standoff's single curved surface — with no numbers beyond the dimensions yet. Ask: "Just looking at
these two shapes, which one do you think wins? On what?" Do not confirm or correct answers here.
Most rooms will jump to "the pyramid, because it has more surface area" — that instinct is worth
recording out loud before anyone touches Appendix C's cost figures, because it is exactly the trap
(see below).

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Cone Standoffs — the option with *less* surface
area?" Show of hands, both options, no discussion. Record the count — Close will ask them to vote
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better cooling'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which fin
dissipates more heat," but push on what the deployment actually needs: "The Background says
outright that the answer isn't the fin that dissipates the most heat, and it isn't the fin that
costs the least — so what *is* the deployment actually optimizing for, and why does that make this
harder than just picking the bigger number in Appendix A?" If the room lands on "we need heat
dissipated per dollar spent, not heat alone and not dollars alone" on its own, the case is working
as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which fin moves more heat" from "which fin moves more heat per dollar,"
ask them to name the actual steps before touching the appendices: find each fin's volume (D1, from
Appendix B's dimensions), find each fin's exposed surface area (D2, same dimensions), turn D1 into
a material cost and add Appendix C's mold amortization for a fully-loaded cost per fin (D3),
combine D2 with Appendix A's dissipation rate for watts per fin and divide by D3 for watts per
dollar, scaled to Appendix E's deployment size (D4), then recommend (D5). Re-ask: "Is our question
still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix A's dissipation rate (MA1), Appendix B's fin dimensions
(MA2–MA4), and Appendix C's mold costs and mold life (MA5–MA7) are all stated Modeling
Assumptions, not sourced figures — no public datasheet publishes a "pyramid fin" or "cone
standoff" spec under those names. Ask which ones actually change the *graded* D4 result if they
move. MA1 and MA4 scale both designs' numbers together and don't flip anything by themselves. The
honest answer for what *does* matter is MA5–MA7 — the mold-cost gap and the mold-life amortization
are the figures the whole dilemma turns on (see case.md's own Margin Note, MA5–MA7). Let a sharp
Hero find this themselves before confirming it.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's two volumes, D2's two surface areas, D3's two
fully-loaded costs, and D4's watts-per-dollar comparison together as a room, cold-calling for D4
specifically — this is where a Hero who correctly found the pyramid has more surface area (D2) but
never carried the mold-cost gap through D3 will visibly struggle to explain why the cone still
wins. That struggle is useful information for the facilitator, not a moment to rescue.

**Facilitator-only arithmetic note.** Pyramid (base edge 0.08 in, height 0.2 in): volume
(1/3 × 0.08² × 0.2) = 0.0004267 in³; slant height √(0.2² + 0.04²) = 0.20396 in; exposed lateral
surface area (four triangular faces — the square base is bonded to the cold plate, not exposed to
coolant) 2 × 0.08 × 0.20396 = 0.032634 in². Cone (base diameter 0.09 in, height 0.2 in): volume
(1/3 × π × 0.045² × 0.2) = 0.0004241 in³; slant height √(0.045² + 0.2²) = 0.205 in; exposed lateral
surface area π × 0.045 × 0.205 = 0.028981 in². D3: material cost = volume × $2.12/in³ (Pyramid
$0.000905, Cone $0.000899); mold amortization = mold cost ÷ 300,000 fins (Pyramid, **retuned**
$7,000/300,000 = $0.023333/fin, Cone $5,000/300,000 = $0.016667/fin); fully-loaded cost per fin:
Pyramid $0.024238, Cone $0.017566. D4: watts per fin = exposed area × 13 W/in² (Pyramid 0.4242 W,
Cone 0.3768 W, unchanged); watts per dollar = watts/fin ÷ cost/fin — Pyramid 17.50 W/$, Cone
21.45 W/$. The Cone Standoffs win by (21.45 − 17.50) / 21.45 = **18.4%**. Full derivation, and the
alternate base-inclusive surface-area cross-check (~19.4%, same winner), in
`case.json.balance.margin_note`.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Someone on the procurement team points out that Appendix E's entire deployment — 16 racks × 72
cold plates × 48 fins — needs exactly 55,296 fins. Appendix C's mold-life figure assumes a mold
produces 300,000 fins before it's replaced. This one deployment doesn't even use up a fifth of a
single mold's assumed lifetime — and the Overview says the tooling doesn't change until the *next*
hardware refresh, which is rated for a different, hotter rack profile than this fin geometry was
sized for."

"If this mold might never get a second production run, is spreading its cost over 300,000 fins
still the right way to price it into your recommendation?"

**Facilitator-only: what this actually does, and does not, change.** The 55,296-fin deployment
total (Appendix E) and the 300,000-fin mold-life assumption (MA7) are both already in the case —
this twist is not a new sourced number, it is a consequence of two numbers Heroes already had that
most will not have connected on their own. Walk a Hero through re-amortizing both mold costs over
55,296 fins instead of 300,000 (Pyramid, retuned: $7,000/55,296 = $0.1266/fin; Cone: $5,000/55,296 =
$0.0904/fin) and the *recommendation does not flip* — the margin under this basis is **19.35%**,
essentially the same as the 18.4% headline figure, because the MA5/MA6 mold-cost ratio (1.4x) stays
fixed regardless of which fin count the mold cost is divided by. What the twist *does* do is surface a real modeling
question the D4 table alone doesn't ask: MA7's "amortization" framing implicitly assumes the mold
gets reused across many future orders, and Appendix E's own numbers suggest this specific order
might not generate anywhere near that reuse. The case has no sourced answer for whether the mold
will be reused — inventing one here would be exactly the fabrication SPEC §5 forbids.
**The twist reframes, it doesn't resolve:** "which fin wins per dollar under the stated
assumptions" is a different question from "is 300,000 fins the right amortization basis for a mold
that might only ever produce this one order," and a Hero who only answers the first hasn't
interrogated the assumption the whole D3/D4 chain is built on. Do not hand a specific answer to the
second question — it is genuinely open given what this case can honestly source, and that openness
is the point.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the mold-reuse question change your vote — or does it just
tell you that '300,000 fins' was an assumption worth pressure-testing, not a fact?" That
distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **More surface area is not the same as more watts per dollar.** The pyramid wins D2 every time,
   by construction — yet it loses D4 badly. Why does looking only at the surface-area appendix
   mislead here, and what does the primary metric's denominator (cost, not watts alone) actually
   protect against?
2. **A "one-time" mold cost is only really one-time if the mold gets reused.** The twist shows this
   deployment alone uses under a fifth of MA7's assumed mold life. Does that change how confident
   the room should be in Argument A's framing that mold cost "pays back" over many cooling cycles —
   even though the recommendation itself doesn't flip?
3. **What the mold-cost gap can and can't tell you.** MA5–MA7 are the load-bearing, unsourced
   figures the whole 18.4% margin turns on. Is a margin this close, built on assumptions this
   contested, a decision worth defending with real confidence — or does the closeness itself argue
   for hedging the recommendation rather than stating it flatly?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both fin geometries side by side, cold-call for a gut read, no cost numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your fin actually wins on watts per dollar, not just watts per fin"* |
| 10:00–15:00 | Pressure-test the models — *"Which of MA5, MA6, or MA7 would have to change, and by how much, for your answer to flip?"* |
| **15:00** | **DROP THE TWIST** — the 55,296-fin order vs. the 300,000-fin mold-life assumption, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (surface area vs. watts per dollar; is "one-time" mold cost really one-time; is a wide, assumption-driven margin still worth defending) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The plausible wrong answer is picking the Pyramid Array on the strength of Appendix A alone —
"more surface area always means better cooling" — without ever running D3's cost math or D4's
per-dollar comparison. More surface area is real, but the case's primary metric is watts per
*dollar*, not watts per fin, and a design can dissipate more heat per fin while still losing badly
on cost once mold complexity and deployment scale (Appendix E) are priced in. The reverse trap is
symmetric: picking the Cone Standoffs purely because the mold is cheaper, without checking whether
the surface-area deficit costs the deployment more in under-dissipated heat than the mold savings
are worth. The case forces D1 through D4, in that order, specifically so no one can jump from "one
number looks better" straight to a recommendation. In this case that discipline still lands on the
Cone Standoffs — but a Hero who reasons straight from Appendix A without doing D3/D4 gets there by
luck, not by the math, and won't be able to defend the number when pressed.

## Socratic questions

1. Your D4 watts-per-dollar figures — which design wins, and by how much? Now imagine the deployment were ten times smaller — does your D3 cost-per-fin math tell you that answer would change, and why?
2. The Pyramid Array wins on D2 surface area every time, by construction. So why isn't the answer to this case just "always build the pyramid"?
3. Your D3 table treats the mold cost as a cost per fin, spread across the number of fins one mold produces (Appendix C). What happens to your D4 result if that mold only ever produces this one deployment's fins, instead of the full 300,000 Appendix C assumes — and which option's cost changes more?
4. Appendix D gives an industry cost-per-watt benchmark as a cross-check. If your D4 figure for the option you'd recommend comes out much better than that industry benchmark, does that mean your recommendation is right, or does it mean something else is worth double-checking?
5. A pyramid has more surface area than a cone of the same base and height — but "more" is not a number. What would have to be true about the size of that surface-area gap, relative to the mold-cost gap, for your recommendation to flip?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
the Cone Standoffs at Anchor 1 purely on "the mold feels cheaper" and stays with the Cone
Standoffs after the twist for a *different, numbers-and-amortization-based* reason has genuinely
moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "MA5–MA7 are the load-bearing figures, not MA1/MA4" finding landed as a
  discovery or had to be told outright.
- Whether the "more surface area vs. more watts per dollar" trap was the actual sticking point, or
  whether D3's amortized-cost math itself was the harder gate for most Heroes.
- Whether the mold-reuse twist felt like a genuine new constraint or felt like the case dodging a
  clean numeric answer — worth listening for directly, since this case's own balance note records
  an 18.4% margin (inside SPEC §2's cap, but genuinely close) that the twist does not paper over.

## Standards Touched On

How to find the volume of a pyramid · How to find the volume of a cone · Surface Area

## Facilitator note — sensitivity (SPEC §6)

None declared by the concept sheet — routine facilities-engineering math, no contested or
emotionally weighted subject matter. `case.json.sensitivity_note` and case.md's own Margin Note
(MA5–MA7) record the load-bearing modeling-assumption finding instead, which is a different
(non-§6) kind of note: the mold-cost-gap and mold-life assumptions (MA5–MA7) are the figures most
likely to flip D5's recommendation — if the pyramid-mold premium over the cone mold (MA5 − MA6) is
smaller than assumed, or the assumed mold life (MA7) is longer than 300,000 fins, the per-fin cost
gap narrows and the Pyramid Array's real surface-area advantage can outweigh it on watts-per-dollar.
Per `case-write` SKILL.md §8, this note states the *direction* of that sensitivity only — never its
size — even though the actual computed numbers are recorded elsewhere in this file and in
`case.json.balance.margin_note` for facilitator reference.
