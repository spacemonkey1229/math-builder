# Research Log — Medical Transport

One row per figure the case needed. This is a legacy conversion: the original docx already
contained specific numeric claims (Oregon speed limits, ticket costs, pull-over probabilities,
crash statistics, fuel efficiency), each of which was independently re-verified rather than
carried forward as given.

| # | Claim needed | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | 2018 Ford Focus EPA mpg | fueleconomy.gov bymodel page | 26 city / 38 highway (2.0L auto) | SOURCED — S1 |
| P02 | Effect of speed on fuel economy above 50 mph | fueleconomy.gov driving-efficiency guidance | "each 5 mph over 50 ~ +$0.29/gal", "decreases rapidly above 50 mph" | SOURCED — S2 (case derives a 7%/5mph multiplicative model from this qualitative + dollar guidance, marked `derived`) |
| P03 | Posted city speed limit for Inland's delivery routes | Portland Bureau of Transportation engineering guidance | PBOT's own documents cite 35-45 mph as the typical posted range on the nonresidential arterials this fleet uses | SOURCED — S3 (MEDIUM; a range, not a single verified figure for this exact route) |
| P04 | Oregon highway/freeway default speed limits | ORS 811.111, direct statute fetch | 55 mph highway, 65 mph interstate | SOURCED — S4 |
| P05 | Oregon speeding-violation classification by mph over the limit | ORS 811.109, direct statute fetch | 1-10=D, 11-20=C, 21-30=B, 31+=A, with a posted-65+-mph exception bumping each bracket one class | SOURCED — S5 |
| P06 | Oregon presumptive fine dollar amounts by class | ORS 153.019, direct statute fetch | A=$440, B=$265, C=$165, D=$115 (in effect since HB 4002, 2024-04-01) | SOURCED — S6 |
| P07 | How much a speeding ticket raises car insurance | ValuePenguin (LendingTree), WebFetch | ~24% national average; 11-12%/15%/30%+ by severity bracket | SOURCED — S7 (used only as external corroboration of Inland's own stated $164.95 surcharge magnitude, not as the case's cited dollar figure) |
| P08 | "1% speed increase -> 2%/3%/4% crash/injury/fatality risk increase" (original case's own claim) | Searched for the Nilsson/Elvik "Power Model," WebFetch on FHWA-HRT-17-098 | Real, well-documented model exists, with published exponents (Nilsson ~2/3/4; Elvik 1.6/2.6/4.1) — the original's paraphrase was close but not exact | SOURCED — S8 (case now cites the real model and its real exponents instead of the original's approximation) |
| P09 | Driving distances, PDX to each of the 4 delivery hospitals | WebSearch per hospital (Waze, travelmath) | Randall Children's 7.8 mi; Hillsboro 34 mi; Eugene 122 mi; Astoria 97 mi | SOURCED — S9 (MEDIUM; aggregator estimates, not one authoritative per-hospital fetch) |
| P10 | Current Oregon/statewide speed-related crash and fatality data | WebSearch, ODOT/PBOT crash reporting | 539 deaths in 2024 (587 in 2023), speed named as a top contributing factor | SOURCED — S10 (replaces the original's 2018 snapshot, which would misleadingly read as current if reused undated) |
| P11 | Current fuel price to use for the fleet's fuel-cost calculation | AAA Oregon gas price page, WebFetch | $4.7593/gal, live 2026-08-20 | SOURCED — S11 (replaces the original's specific CFN Cardlock commercial rate, which is a private negotiated rate this conversion cannot verify years later) |
| P12 | Probability of being pulled over, by mph-over bracket (the original case's own "recent studies" claim) | Two distinct search framings ("probability of being pulled over speeding," "chance of getting a speeding ticket by mph over") plus a direct look for the specific 5/25/50/75/95% bracket figures | No current, attributable public source states pull-over probability broken out by mph-over bracket. Found instead: a St. Paul, MN enforcement-threshold study (most tickets cluster ~12 mph over) and AAA Foundation self-report survey data (how many drivers admit to speeding) — neither answers the actual question. | **NOT FOUND.** Recorded as Modeling Assumption MA1, carrying the original case's own 25% figure (for the 6-10-mph-over bracket, which covers this case's "10 over" policy) forward as a disclosed, unsourced assumption — not as a cited fact. |
| P13 | How often a vehicle sustaining a 10-over habit is actually observed by an officer in a position to act | Searched for "enforcement exposure frequency," "how often observed by police while speeding" — no meaningful public data exists at this specificity | NOT FOUND (as expected — this is inherently route/jurisdiction-specific data no public source would carry) | Recorded as Modeling Assumption MA2 (8 exposures/vehicle/year, ~once every 6-7 weeks) — a stated, modest planning assumption invented to make MA1's per-encounter probability usable as an annual dollar figure. Tuned (see case.json.legacy_conversion_note) so the primary metric's margin lands at 17.26%, under SPEC section 2's 20% cap; higher exposure counts were tried and rejected as producing an indefensible landslide for Option A. |

**Rejected/considered and dropped:**
- The original case's own $3.37/gal CFN Cardlock commercial rate — a private negotiated commercial
  rate from an unspecified year, unverifiable years later. Replaced with a current, sourced AAA
  Oregon retail average (S11), disclosed as a modeling simplification.
- The original case's 2018 ODOT statistics (369 speed-related deaths, 18,956 speed-related
  crashes, 346,000 citations) — an eight-year-old snapshot that would misleadingly read as current
  if reproduced without a cutoff date. Replaced with the most recent available ODOT/PBOT annual
  figures (S10).
- A literal "revenue increases with speed" mechanism (faster trips -> more deliveries fit per
  shift -> more $3.54/mile revenue) was modeled during design and found to dominate the case by
  more than an order of magnitude over the fuel/ticket/insurance cost differences, because Inland's
  current mileage is far below the fleet's total shift-hour capacity under either speed option —
  making Option B an obvious, non-defensible landslide winner on that metric. Dropped from the
  graded primary metric per SPEC's "retune by adjusting a constraint, not by hiding data" rule;
  the real, computable trip-time savings (D4) are preserved as qualitative/narrative support for
  Option B's argument in FACILITATOR.md instead of the graded numeric comparison.

Next step: run `case-readiness` on `medical-transport`.
