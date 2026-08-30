# Facilitator Notes: The Enclosure Call

**Case:** The Enclosure Call · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Geometry — Cone / Sphere / 3-Dimensional / Surface Area / Radius / Pi;
Advanced Numbers — Percent (see `case.json.standards[]` for exact ids). Closes Cone and Sphere,
both previously zero-coverage.

`margin_pct` is now computed and recorded: **8.85%**, Project Orb (B) wins. See "Data Deep Dive"
below for the full arithmetic; every figure there is also recorded in `case.json.derived` so this
guide and the case of record cannot silently drift apart. (Updated 2026-08-27: recomputed from
9.11% after re-sourcing the ABS resin-price and density citations for P6; the winner and the shape
of the case are unchanged.)

---

## Intro

Frame the format before anything else: this is a case study, not a worksheet. Nina Odom has to
walk into Friday's client review with one recommendation, and the room is about to split the same
way her studio has — the client's engineer wants acoustic performance, the creative director wants
shelf appeal, and Nina's own job is to be the one who actually runs the numbers. Name the opener:
"Two foam shapes are on the table. One of you is about to be Nina. What do you recommend, and why,
before you've seen a single number?"

## Launch

Show the two shapes. A photo or two physical props (a paper cone-frustum net folded from Appendix
A's dimensions, a ball) land better than description alone — the class should be able to physically
turn each one over the way Nina does in the Overview. Read the Overview aloud, stop at "she picks up
the tapered shell first, turns it once in her hand, and sets it back down next to the sphere," and
go straight into Anchor 1 without commentary.

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Project Horn — the tapered shape, the one the audio
engineer wants?" Count hands. "And Project Orb — the sphere, the one the creative director wants?"
Count hands. Write the split on the board and leave it there for the whole session; it's the number
the Close comes back to.

## Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?**

"Is this actually a question about which shape sounds better, or looks better on a shelf?" Let
students say yes — then push: "Nina's own boss told her this gets judged on one number. What number?"
Make them find it in Background themselves: total cost per unit at the client's target first-year
production volume. "Is that the right question? What do you mean by 'cost'? Does that include
shipping, or just the mold?" Deliberately let the confusion grow here — a group that thinks "cost"
means only the sticker price on the mold quote has not yet found the real problem, and that's fine.
"Wow, this is a harder problem than it looked."

## Anchor 3

**WHAT IS THE PROCESS?**

"If we go through this — measure both shapes, price both shapes, ship both shapes — how do we
actually decide?" Walk the room toward: compute total cost per unit for each option (materials +
amortized mold tooling + shipping), then compare. "Is our question still the right one, now that we
can see the process? What would make this process fail?" (A good answer: if the production volume
assumption is wrong, since it changes how much the tooling cost matters per unit — hold onto that
thread, it resurfaces in Anchor 4 and again in the Twist.)

## Anchor 4

**WHAT DON'T WE KNOW?**

"Do we need to make assumptions? Which ones are load-bearing?" Walk the Modeling Assumptions table
in `case.md` as a group: MA1 (both shapes' exact dimensions), MA2 (target production volume — no
real client exists to source this from), MA3 (shell material, cancels out — same for both), MA4
(Project Horn's packing efficiency, the single most dilemma-sensitive number in the case), MA5
(wall thickness, low-stakes), MA6 (the tooling-cost gap between a tapered and a spherical mold).
"Which of these, if it moved, would flip your Anchor 1 vote?" Good answers: MA4 and MA2×MA6 — both
are named explicitly in `case.json.sensitivity_note` and both resurface below.

## Data Deep Dive

Now, and only now, the numbers. Walk the class through the arithmetic `case.json.margin_basis`
describes — total cost per unit = (surface area x material cost per sq in) + (mold tooling cost /
target production volume) + (freight cost per container / (container volume x packing efficiency /
unit volume)) — for each option, using Appendices A, B and C.

| | Project Horn (frustum) | Project Orb (sphere) |
|---|---|---|
| Surface area (sq in) | 157.90 | 153.94 |
| Material cost/unit | $0.4895 | $0.4772 |
| Tooling cost/unit (at 250,000 units) | $0.2320 | $0.1280 |
| Unit volume (cu ft) | 0.0845 | 0.1039 |
| Units per 2,683-cu-ft container | 25,391 | 19,117 |
| Shipping cost/unit | $0.1406 | $0.1868 |
| **Total cost per unit** | **$0.8621** | **$0.7920** |

Project Orb wins on total cost per unit, by **8.85%** — comfortably inside SPEC §2's ~20% balance
cap, so this is a genuine, defensible split, not a runaway. Notice out loud what a room that
stops at the tooling line alone would miss: a room that only compared the $32,000-vs-$58,000 mold
quote would have picked Orb for the wrong reason, never noticing that Orb's *shipping* cost per
unit is actually the *higher* of the two — its cost advantage survives only because tooling and
materials outweigh that shipping penalty, not because shipping favors it too.

**Disclosed sensitivity (added 2026-08-27, P5 remediation):** a mechanical ±50% flex of every
stated assumption (`cases/enclosure-call/sensitivity_model.py`) found that MA1's four geometry
dimensions and MA6's Horn-side tooling cost can each, individually, flip this recommendation to
Project Horn — this is real, disclosed fragility (see `case.json.sensitivity_disclosure[]`), not
a reason to distrust the base numbers above. If a Hero pushes on "what if the dimensions were
different," that is the case's own most legitimate move, not a gotcha.

## Twist

At roughly the 15-minute mark, drop this: *"New information just came in from the client's
engineering team. The acoustic dispersion certification the client requires — the one the audio
engineer has been talking about — is not just a preference. It's contractual. And it turns out
Project Orb's spherical shell has never been certified for that specific dispersion pattern. If
Nina recommends Project Orb, the studio needs a one-time redesign-and-retest pass to get it
certified — call it $45,000, amortized over the same 250,000-unit production run."*

That is **$0.18/unit** added to Project Orb's total cost — pushing Orb from $0.7920/unit to
roughly **$0.9720/unit**, which now *loses* to Project Horn's $0.8621/unit by about **12.75%**.
(This $45,000 figure is illustrative for the discussion only — it is not a `sources[]`-backed
number or part of the case's balance test of record; it lives only here, in `case.json.derived`,
for facilitators to use consistently if they choose to run this twist.)

*"You now have 60 seconds. Are you changing your plan — or not?"*

The follow-up is the whole point: **"What just broke in your original model? Were you comparing the
right two numbers, or did you assume the two shapes were equally free to choose, with cost as the
only variable?"** A model that only ever priced materials, tooling, and shipping was implicitly
assuming the two options were otherwise interchangeable — the twist shows that assumption was never
stated, let alone tested.

## Close

**VOTE AGAIN.** Compare the new count against the Anchor 1 tally still on the board. "Did we ask the
right question at Anchor 2? What math was new to you today, and how did you attack it?" Surface
that the *base* case (no twist) genuinely favors Project Orb by 8.85%, and that the twist is a
deliberately introduced complication, not a hidden "real" answer — the point is that both numbers
are honest, and a good recommendation names which one it's using and why.

## Lessons Learned

- Total cost per unit is not the mold quote. A model that stops at "which mold costs less" misses
  the shipping line entirely — and in this case, the cheaper-to-mold shape is also the *worse*
  shipper, so those two effects partially cancel rather than reinforce each other.
- A mathematically proven ceiling (Kepler's ~74.05% sphere-packing limit) behaves differently in an
  argument than a market estimate — it cannot be contested the way a freight rate or a tooling quote
  can, and naming that distinction is itself a mathematical-reasoning skill.
- Amortization means the same fixed cost (mold tooling) means a different amount per unit depending
  on volume — a plan that looks decisive at 250,000 units/year can look very different at 50,000.
- "Cost" is not a fixed, closed set of line items. A contractual requirement (the twist) can add a
  real cost category that the original model never priced in at all.

## Standards Touched On

Geometry — Cone, Sphere, 3-Dimensional, Surface Area, Radius, Pi (naming and measuring two 3-D
solids and computing their surface area and volume). Advanced Numbers — Percent, How to find the
percent of a number (computing the cost margin and the twist's cost swing as percentages). See
`case.json.standards[]` for the exact spine ids; `new_coverage[]` = Cone and Sphere, both
previously zero-coverage.

---

## Argument for A — Project Horn (cone frustum)

The tapered mold costs more to cut than a simple mold, and a frustum does not nest for shipping as
tightly as a flat-sided box would. But the frustum's shipping penalty is modest next to a sphere's:
tapered or faceted shapes can stack close to the theoretical maximum of the container they ride in,
while a sphere is mathematically capped at roughly 74% packing density no matter how it's arranged
(the proven Kepler-conjecture ceiling). Run the actual numbers (see Data Deep Dive) and Project
Horn's shipping-cost-per-unit advantage over Project Orb ($0.1406 vs. $0.1868/unit) is real — it
just isn't quite large enough on its own to overcome Project Orb's lower tooling and material cost
at the case's 250,000-unit target volume. Horn also happens to be the shape the client's own audio
engineer wants for acoustic performance, which is a real argument even before the cost model closes
the gap — and the Twist shows a scenario where that qualitative argument turns out to have real
dollar consequences.

## Argument for B — Project Orb (sphere)

The sphere's mold is simpler and cheaper to cut ($32,000 vs. $58,000), and the sphere's exterior
surface area (153.94 sq in) is genuinely smaller than the frustum's (157.90 sq in), so material cost
is lower too. Those two savings apply on every single unit in the production run, while the shipping
penalty is real but not large enough at this volume to erase them: at the client's 250,000-unit
target, Project Orb wins on total cost per unit, $0.7920 vs. $0.8621, an 8.85% margin. It's also the
shape the studio's own creative director wants for shelf appeal, which carries real commercial
weight independent of the cost model — though the Twist shows that "cheaper to make" is not the same
as "cheaper, full stop," if a contractual requirement the base model never priced turns out to bind.

## The margin

`margin_basis`: total cost per unit for each option = (surface area x material cost per sq in) +
(mold tooling cost / target production volume) + (freight cost per container / (container volume x
packing efficiency / unit volume)). Computed from the on-file MA1/MA2/MA4/MA6 assumptions and
S1/S2/S6 sourced figures (see Data Deep Dive for the full walkthrough): Project Horn = $0.8621/unit,
Project Orb = $0.7920/unit. **`margin_pct` = 8.85%**, Project Orb (B) wins, comfortably inside SPEC
§2's ~20% cap — a genuinely close, defensible case.

## Five Socratic questions

1. Project Orb's sphere can never exceed about 74% packing density in a container, a proven mathematical ceiling, not a market estimate — why does that number deserve to be treated differently in this discussion than, say, the mold tooling cost?
2. Your total-cost-per-unit table shows Project Orb winning by about 8.85%. If the client doubled their target production volume for next year, would you expect that same shape to still win, and why does the answer depend on which cost categories scale with volume and which don't?
3. The audio engineer wants Project Horn for acoustic dispersion, and the creative director wants Project Orb for shelf appeal, but your cost model favors Orb by 8.85% — what number would need to change, and by how much, to make Horn win on cost instead?
4. You computed each shape's surface area to get its material cost — which of the two shapes' surface-area calculation required more of the dimensions you marked in D1, and what would happen to your total-cost table if you had gotten one of those dimensions wrong?
5. Mold tooling is a one-time cost, amortized over the whole production run — what happens to each option's total cost per unit if the client's actual first-year volume comes in at half the 250,000-unit target you used?

## The trap

A Hero compares mold tooling cost alone — Project Orb's simpler mold is cheaper, so Project Orb
looks like the obvious pick — and stops there, treating "the sphere costs less to mold" as
equivalent to "the sphere costs less to make." That comparison never reaches the shipping side of
the ledger at all: it silently assumes packing efficiency is roughly the same for any shape, when
the entire reason sphere-packing is a well-known result is that it demonstrably is not — and in
this case Project Orb's shipping cost per unit ($0.1868) is actually *higher* than Project Horn's
($0.1406). Orb still wins overall, but only because its tooling and material savings outweigh that
shipping penalty, not because shipping favors it too. Watch for a pitch that cites the tooling-cost
line from Appendix B and calls the decision made without ever opening Appendix C.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "Convince us why it's better, not just fair" (Anchor 2 — define the real question) |
| 10:00-15:00 | Pressure-test the models: "Whose plan is most fragile?" (Anchor 3 and 4 — process and assumptions) |
| **15:00** | **DROP THE TWIST** — the acoustic-certification requirement, delivered slowly, with pauses |
| 15:00-20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00-30:00 | Threaded deep conflict — two named threads: (1) cost-optimization vs. qualitative/contractual requirements, (2) a mathematically proven ceiling (Kepler) vs. a negotiable market estimate (tooling, freight) |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Sensitivity note (SPEC §6)

**NONE.** This case carries no SPEC §6 sensitivity — it is routine industrial-design cost modeling
(which enclosure shape a design studio recommends to a client), with no protected subject matter.
