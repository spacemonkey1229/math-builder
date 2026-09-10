# Research Log — The Weekly Rate

This case was authored with sourced figures gathered inline (WebSearch + WebFetch) rather than
staged through placeholder tokens, because a genuine, checkable real-world dataset was identified
and fetched before the spine of the document was drafted. Every figure below still follows the
same discipline SPEC §5 requires: cited to a real, fetched source, or explicitly disclosed as a
Modeling Assumption. Nothing was invented quietly.

| # | What was needed | What was searched | What was found | Outcome |
|---|---|---|---|---|
| 1 | A real weekly e-bike rental subscription price for gig delivery riders | "Zoomo e-bike weekly rental subscription price delivery riders 2026"; then a direct fetch of ridezoomo.com/us/home | Zoomo Standard Plan, "From $39/week," full maintenance/wear-and-tear/battery/U-lock/GPS included | SOURCED — S1 |
| 2 | A real weekly e-bike subscription price from a second company, for comparison/distractor use | "Whizz e-bike subscription weekly price delivery riders"; direct fetch of getwhizz.com/uber-eats and a Philadelphia-market blog post | Whizz Storm-1 $69/week, Thunder $79/week, mandatory $99 deposit on weekly plans (Philadelphia market); separate monthly rent-to-own tiers $129-$279/month | SOURCED — S5b. Deliberately kept as Appendix B distractor data, not folded into the primary A-vs-B comparison. |
| 3 | A real, purchasable delivery-grade e-bike with a published price and battery spec | "RadRunner 3 Plus price battery capacity range specs 2026"; direct fetch of electricbikereview.com's review | $2,299 MSRP (one earlier aggregator search returned $2,229, an apparently outdated or promotional figure — not used); 672 Wh (48V, 14Ah) battery; 25-45 mile real-world range | SOURCED — S2. Manufacturer's own radpowerbikes.com product page returned HTTP 404 at fetch time (twice, different URL forms); electricbikereview.com's review, cross-confirmed for price by two other independent search results, was used instead and graded MEDIUM rather than HIGH for that reason. |
| 4 | A real electricity price to convert battery Wh into a dollar charging cost | "EIA average residential electricity price per kWh 2026"; direct fetch of eia.gov's Electric Power Monthly Table 5.6.A | $0.1834/kWh, U.S. average residential, June 2026 (preliminary) | SOURCED — S3, HIGH (primary federal statistical source). |
| 5 | A real figure for e-bike maintenance/repair cost, to build Dara's self-maintenance line if she owns | "average annual e-bike maintenance cost commuter bike shop tune-up"; direct fetch of hovsco.com's breakdown | Casual rider <$200/yr; regular commuter $400+/yr; component breakdown (tune-ups $200-400/yr, tires $30-70/yr, brakes $30-100/yr, chain $30-100/2yr); electricity $10-30/yr at 2,000-5,000 mi/yr | SOURCED — S4, but NOT directly usable as Dara's own maintenance figure — her mileage (≈10,400 mi/yr under MA1) is 2-5x the source's "regular commuter" range. See rejection note below. |
| 6 | Dara's own actual annual maintenance cost at full-time delivery mileage | Searched specifically for "e-bike delivery courier maintenance cost per mile" and similar — no published figure exists for maintenance cost at commercial/delivery-intensity mileage specifically | NOT FOUND | Recorded as Modeling Assumption MA3 ($900/yr), an explicit upward extrapolation from S4's commuter figure, with the scaling logic stated in the assumption's basis. This is the textbook "assumption, not a fabricated number" case: a real source exists for a *different* rider profile, and the case says so rather than passing S4's figure off as Dara's own. |
| 7 | Dara's actual weekly mileage as a full-time courier | "e-bike delivery courier average miles per week full-time gig worker" | Search returned per-shift ranges (25-50 mi/shift, "40-80 km per shift") from secondary blog sources, and one claim about a DoorDash mileage bonus threshold ("$5-$15/week for riding at least 125 miles a week") that could not be traced to a specific, datable DoorDash source in a follow-up search — the claim appeared only inside aggregated AI-search summaries, never inside a single fetchable document. | REJECTED as a citable source (no traceable primary document — MCS-21's "report NOT FOUND rather than guessing" applies) and NOT used anywhere in the case, including as color. Weekly mileage recorded as Modeling Assumption MA1 (200 mi/week) instead, with an independently articulable basis (6 shifts/week x ~33 mi/shift). |
| 8 | Real-world grounding for a Twist that changes Option B's price mid-horizon | Following up on the Zoomo pricing page, checked Zoomo's own blog for pricing history | "Old vs New: Understanding our updated US Price Plans" — Zoomo's own account of raising its Flex Plan from $39/week to $49/week (~26%) in exchange for expanded coverage | SOURCED — S5a, HIGH (primary, the company's own statement about its own past pricing). Used only in the Twist (facilitator-only), not in the base A-vs-B comparison, and not claimed as evidence the Standard Plan specifically has already changed. |
| 9 | Real-world color establishing the situation as genuine and current | "New York City e-bike delivery workers app-based couriers article 2026" | NYC Mayor's Office press release: ~80,000 app-based delivery workers citywide; UL-certification requirement for delivery e-bikes/batteries effective 2026-01-26; NYC's Deliverista Hub | SOURCED — S6, HIGH (primary government press release). Used as Background color and Appendix D context; not load-bearing to any calculation. |

## Rejected or excluded figures

- The $2,229 RadRunner 3 Plus price from one earlier search snippet was not used — two independent
  later sources (electricbikereview.com's own fetched page, and a separate aggregator search)
  converged on $2,299, and $2,229 looked like a stale or promotional figure. Noted, not silently
  dropped.
- The "DoorDash pays a mileage bonus at 125 mi/week" claim was never traced to a single fetchable,
  datable source and is not used anywhere in this case, per item 7 above.
- Whizz's Philadelphia-market weekly pricing ($69/$79/week, $99 deposit) is used as-is for Appendix
  B's distractor data without adjustment for NYC — flagged in S5b's note, and harmless because
  Appendix B is explicitly not part of the graded A-vs-B comparison.

## Status

All figures needed for the primary balance test are SOURCED or explicitly disclosed as Modeling
Assumptions. Zero placeholders remain in `case.md`. `status` → `"researched"`.

Next step: `Run case-readiness on the-weekly-rate.`
