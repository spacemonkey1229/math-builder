# Facilitator Notes: The Enclosure Call

**Case:** The Enclosure Call · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Geometry/Visual Perceptibility — Cone / Sphere / 3-Dimensional / Surface Area /
Radius / Pi; Advanced Numbers — Percent (see `case.json.standards[]` for exact ids). Closes
Cone and Sphere, both previously zero-coverage.

Drafted at write time, before `case-research` fills Appendices A–C. `margin_pct` is `null` until
those figures are sourced.

## Argument for A — Project Horn (cone frustum)

The tapered mold costs more to cut than a simple mold, and a frustum does not nest for shipping as
tightly as a flat-sided box would. But the frustum's shipping penalty is modest next to a sphere's:
tapered or faceted shapes can stack close to the theoretical maximum of the container they ride in,
while a sphere is mathematically capped at roughly 74% packing density no matter how it's arranged
(the proven Kepler-conjecture ceiling). If Project Horn's shipping-cost-per-unit advantage over the
client's full target production run outweighs its higher amortized tooling cost and whatever
material-cost difference its surface area produces relative to the sphere, Project Horn wins on
total cost per unit — and it also happens to be the shape the client's own audio engineer wants for
acoustic performance, which is a real argument even before the cost model is finished.

## Argument for B — Project Orb (sphere)

The sphere's mold is simpler and cheaper to cut than a tapered mold, and a sphere may expose less
exterior surface area than a comparable-volume frustum, which would lower per-unit material cost.
Those two savings apply on every single unit in the production run, while the shipping penalty only
bites once real freight volume is involved — so at a small enough production volume, or a low
enough freight rate, Project Orb's tooling and material savings could dominate the shipping
disadvantage. It's also the shape the studio's own creative director wants for shelf appeal, which
carries real commercial weight independent of the cost model.

## The margin

`margin_basis`: once Appendix A's dimensions and Appendix B/C's cost and packing figures are
sourced, compute total cost per unit for each option as (surface area × material cost per square
inch) + (mold tooling cost ÷ target production volume) + (freight cost per container ÷ (container
volume × packing efficiency ÷ unit volume)), then express the gap between Project Horn's and
Project Orb's totals as a percentage of the lower figure. `margin_pct`: **null** — not computable
until `case-research` returns Appendix A/B/C's figures.

## Five Socratic questions

1. Project Orb's sphere can never exceed about 74% packing density in a container — a proven
   mathematical ceiling, not a market estimate. Why does that number deserve to be treated
   differently in this discussion than, say, the mold tooling cost?
2. Your total-cost-per-unit table shows one shape winning. If the client doubled their target
   production volume for next year, would you expect that same shape to still win — and why does
   the answer depend on which cost categories scale with volume and which don't?
3. The audio engineer wants Project Horn for acoustic dispersion, and the creative director wants
   Project Orb for shelf appeal. Suppose the cost model came out essentially tied. What number
   would you need that isn't in this case to break that tie?
4. You computed each shape's surface area to get its material cost. Which of the two shapes'
   surface-area calculation required more of the dimensions you marked in D1, and what would
   happen to your total-cost table if you had gotten one of those dimensions wrong?
5. Mold tooling is a one-time cost, amortized over the whole production run. What happens to each
   option's total cost per unit if the client's actual first-year volume comes in at half the
   target you used?

## The trap

A Hero compares mold tooling cost alone — Project Orb's simpler mold is cheaper, so Project Orb
looks like the obvious pick — and stops there, treating "the sphere costs less to mold" as
equivalent to "the sphere costs less to make." That comparison never reaches the shipping side of
the ledger at all: it silently assumes packing efficiency is roughly the same for any shape, when
the entire reason sphere-packing is a well-known result is that it demonstrably is not. Watch for a
pitch that cites the tooling-cost line from Appendix B and calls the decision made without ever
opening Appendix C.

## Sensitivity note (SPEC §6)

**NONE.** This case carries no SPEC §6 sensitivity — it is routine industrial-design cost modeling
(which enclosure shape a design studio recommends to a client), with no protected subject matter.
