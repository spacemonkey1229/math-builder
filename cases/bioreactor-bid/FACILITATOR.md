# FACILITATOR.md — The Bioreactor Bid

**Facilitator-only. Do not distribute to students.** Balance argument, margin, and the trap live
here and in `case.json`'s `balance` object — never in `case.md`.

## Argument for A — The Column Bid (stirred-tank bioreactor)

The Column Bid's working volume is not in question — a right circular cylinder at a stated fill
level is exact arithmetic, no integral needed, and it is typically the cheaper vessel to buy and
to validate. Because its volume is fully usable and predictable, its yield-per-dollar denominator
(total vessel cost) is small and its usable-volume numerator carries no penalty for wasted
headspace shape. If the Wave Bid's mixing advantage is not large enough to overcome its higher
purchase-plus-validation cost and its volume penalty from the curved bag profile (the disk-method
integral will always return less usable volume than the bag's stated nominal capacity, since the
bag doesn't fill as a perfect cylinder), the Column Bid wins on dollars per liter even though its
raw density ceiling is lower.

## Argument for B — The Wave Bid (wave/rocking bioreactor)

The Wave Bid's superior mixing lifts the achievable cell density, which raises the net cumulative
yield per liter of working volume — the area between the feed-rate and uptake-rate curves is
larger for a better-mixed batch, because more of the fed nutrient converts to viable product
before it goes uneaten or the culture stalls. If that per-liter yield advantage is large enough,
it can outrun both the Wave Bid's higher cost and its smaller-than-nominal working volume once the
disk-method integral is applied — because the metric is yield per dollar, not yield per liter, and
a vessel that turns fewer liters into more product per liter can still win on the ratio that
actually matters to the client's budget.

## Margin

`margin_basis` (see `case.json.balance.margin_basis`): compare total liters of viable product
yielded per dollar of total vessel cost (net cumulative yield per liter × working volume, divided
by vessel-plus-validation cost) for Option A versus Option B, once Appendices A–D are filled by
`case-research`. `margin_pct` is `null` until then — this case was designed so the Wave Bid's
mixing/yield advantage and its cost/volume penalty pull against each other on the same ratio; the
actual margin is not yet known and must not be guessed at write time.

## Five Socratic questions

1. Your yield-per-dollar table gives one option the edge — what would the Wave Bid's validation
   cost have to drop to for that ranking to flip?
2. You integrated the bag's radius profile to get the Wave Bid's working volume instead of using
   its nominal capacity — how many liters did that integral cost you compared to just using the
   sticker number, and why does that gap matter to your final ratio?
3. If the client's minimum required total yield rules out one vessel entirely, does that vessel's
   yield-per-dollar number even matter anymore — and which of your two options is more exposed to
   that risk?
4. Your net-cumulative-yield figure came from the area between two curves — what part of the
   batch (which days) contributed the most to that area, and would a shorter batch duration have
   changed which option you'd recommend?
5. Two teams could compute the same disk-method integral and land on different working volumes
   for the Wave Bid — what's the most likely place a small measurement or rounding choice in
   Appendix C would change your final recommendation?

## The trap

The plausible reasoning that produces a confident wrong answer: a Hero compares the two vessels'
nominal capacities directly — reading the Wave Bid's bigger sticker-capacity number and its
higher mixing-driven per-liter yield and concluding it must win on total output — without ever
running the disk-method integral to find out how much of that nominal capacity is actually usable
at the target fill level. The bag's curved profile means its true working volume is smaller than
its nominal capacity in a way the cylinder's working volume is not; skipping that integral and
using the nominal number for Option B systematically overstates its yield and can flip the
yield-per-dollar recommendation.

## Sensitivity note

NONE. This case does not touch illness, death, financial hardship, or family stress — it is a
production-engineering budget decision. No sensitivity flag applies (SPEC §6).
