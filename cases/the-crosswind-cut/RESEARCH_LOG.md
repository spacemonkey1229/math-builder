# RESEARCH_LOG.md — The Crosswind Cut

One row per placeholder that was open in `case.md` at the start of `case-research`. "Rejected"
entries are the searches that did not pan out — kept so nobody re-runs the same dead search.

## Appendix A — motor/propeller combo data (12 placeholders)

| Placeholder | Searched | Found | Verdict |
|---|---|---|---|
| Motor KV rating (Sparrow, Albatross) | `T-Motor uav-en.tmotor.com Multirotor Propellers datasheet`; `T-Motor MN motor high KV small propeller thrust test data delivery drone`; then targeted fetch of T-Motor's Antigravity MN-series product pages | T-Motor's **MN5008 Antigravity** motor family is sold in three windings — KV170, KV340, KV400 — all on the same physical mount/airframe footprint, which is exactly the "same airframe, different motor/prop" premise the case needs. Picked **KV400** (Sparrow, high-KV/small-prop) and **KV340** (Albatross, low-KV/large-prop) because both are rated and tested by T-Motor at the same 6S (~23V) bus, making them the only same-battery-compatible pair in the family (KV170's own published test data is only at 12S/47V, which is not battery-compatible with the others). | SOURCED — S1, S2 |
| Propeller diameter/pitch | Read directly off the same product pages | Sparrow: T-Motor P15×5" CF. Albatross: T-Motor P18×6.1" CF (T-Motor also publishes P17×5.8" data for KV340; picked the larger P18×6.1" to make Albatross's "large propeller" framing clearly distinct from Sparrow's P15×5"). | SOURCED — S1, S2 |
| RPM / thrust / current at commanded throttle | Fetched full throttle-vs-thrust-vs-current tables for both combos (40-100% throttle, 5% steps in most of the range) | Selected **90% throttle** as the route's commanded setting. Rationale: at low throttle (40%, T-Motor's own peak-efficiency point) Albatross is clearly more current-efficient than Sparrow; T-Motor's own published curves show this gap *closes and reverses* as throttle rises — by 80% throttle Sparrow is already the more efficient combo, and the gap widens through 90-100%. Choosing a throttle in the reversed zone (90%) is what makes the case's "does the advertised ranking survive at operating conditions" question a real, sourced phenomenon rather than an invented one. | SOURCED — S1, S2 |
| Advertised calm-air thrust-per-amp | Same fetches | T-Motor publishes efficiency in **g/W**, not g/A. Derived g/A = thrust ÷ current at T-Motor's lowest published throttle row (40%, its own peak-efficiency point) for each combo, marked `derived: true`. | SOURCED (derived) — S1, S2 |
| Number of motors on Drone 114's airframe | `Zipline Wing Amazon Prime Air ... cruise speed`; `Flytrex Manna drone delivery typical range` | Drone 114 is a fictional airframe — no spec to source. No real source names a motor count for it. | **ASSUMPTION MA3** — quadcopter (4), basis = common multirotor convention + scale consistency with Flytrex-class real short-hop delivery multirotors [S6]. |
| Commanded cruise groundspeed | `Zipline Wing Amazon Prime Air delivery drone cruise speed mph published`; `DJI FlyCart 30 cruise speed max speed specifications` | Real delivery-drone cruise speeds range widely (Zipline/Wing/Amazon: 60-74 mph) but those are VTOL fixed-wing hybrids, not aerodynamically comparable to a rotor-only multirotor. DJI FlyCart 30 (a real pure-multirotor delivery drone) publishes a **15 m/s (33.5 mph) automatic-flight cruising speed**, confirmed on two DJI pages. | **ASSUMPTION MA4** — 33.5 mph, anchored to FlyCart 30 [S5]. |

## Appendix B — corridor and crosswind (1 remaining placeholder + MA1/MA2 confirmation)

| Placeholder | Searched | Found | Verdict |
|---|---|---|---|
| Crosswind speed (MA1, pre-flagged by concept sheet) | `average crosswind speed mph typical wind advisory low altitude aviation NWS climatology`; `National Weather Service "Wind Advisory" criteria`; `drone delivery maximum operating wind speed limit mph Zipline Wing` | Confirmed: no public source names a wind reading for a fictional corridor. Anchored the given 15 mph to two real thresholds: NWS Wind Advisory begins at 31-39 mph sustained [S3], and small-UAS "Level 6" wind-resistance is commonly benchmarked at ~27-31 mph [S4] — 15 mph is comfortably below both, i.e. an ordinary operating condition, not an edge case. Rejected an initial "Zipline drone rated to 14 m/s / 31 mph" claim — could not confirm this was actually a Zipline-specific spec rather than a conflation with the generic industry benchmark, so it is not used as a citation (S4 is used instead, correctly labeled as a generic benchmark, not Zipline's). | **ASSUMPTION MA1** — 15 mph (value was given; research task was to confirm/ground it). |
| Crossing angle (MA2, pre-flagged) | N/A — this is a case-design geometry choice | Confirmed still unsourceable (fictional corridor). Set to 80° (not exactly 90°) to match the Background's "close to a right angle" language while keeping the perpendicular component clearly dominant. | **ASSUMPTION MA2** — 80°. |
| Route length | `Zipline P2 Wing delivery drone typical corridor delivery distance miles`; `Flytrex Manna drone delivery typical range miles quadcopter suburban delivery radius` | Zipline's ~10-mile service radius was the first anchor found, but it is a VTOL fixed-wing platform with far lower current draw per unit thrust than the MN5008-class motors chosen for Appendix A — a 10-mile route at these current draws would need a battery far too large for this motor class (see feasibility check below). Flytrex's Sky2 (a real, comparable non-fixed-wing multirotor delivery drone) publishes a **4-mile delivery radius**, which is both a better real analog and internally consistent with the rest of the case's numbers. | **ASSUMPTION MA5** — 4 mi, anchored to Flytrex [S6]. |

## Appendix C — battery and reserve rule (3 placeholders)

| Placeholder | Searched | Found | Verdict |
|---|---|---|---|
| Battery pack capacity | `T-Motor Antigravity MN5008 recommended ESC battery cell count Lipo capacity`; `agriculture spray drone 6S battery pack capacity mAh Antigravity motor` | T-Motor does not publish a recommended pack capacity for the MN5008 (capacity is an airframe-level choice). Real 6S packs sold for this thrust class of agricultural/industrial multirotor commonly run 16,000-24,000 mAh. | **ASSUMPTION MA6** — 22,000 mAh, 6S, anchored to a representative product in that range [S7]. |
| Mandatory reserve % | `FAA battery reserve requirement small UAS BVLOS waiver minimum reserve percent landing` (three query variants) | No FAA rule specifies a battery-reserve percentage for small UAS BVLOS operations — confirmed after three search framings and review of Part 107 and BVLOS waiver-checklist documents. Rejected as NOT FOUND for a direct citation. Anchored instead to manned aviation's real VFR fuel-reserve rule (14 CFR 91.151: 30 minutes' reserve at normal cruise, day VFR) as the closest analogous real regulatory principle. | **ASSUMPTION MA7** — 25% of pack capacity, basis = 14 CFR 91.151 analogy [S8]. |
| Nominal pack voltage | Read directly off the MN5008 KV400/KV340 product pages | Both windings are rated 6S LiPo (22.2 V nominal) — this is a genuine T-Motor spec for the exact combos chosen, not a scenario detail about the fictional Drone 114. | **SOURCED** — S1, S2 (not a Modeling Assumption). |

## Appendix E — sources row (3 placeholders: which page, accessed date, confidence)

Resolved directly as part of filling Appendix A: S1 = T-Motor MN5008 KV400 product/spec page, S2 = T-Motor MN5008 KV340 product/spec page, both accessed 2026-08-30, both graded HIGH (primary manufacturer test data, unambiguous units, exactly the figures the case needs; the only soft spot is that the product pages carry no explicit revision date, noted in each source record).

## Feasibility check performed (not a placeholder, but changed a research decision)

Before finalizing MA4/MA5/MA6/MA7, ran the numbers to confirm Appendix C's battery/reserve rule is
satisfiable by both configurations at the chosen route length and groundspeed (otherwise D5 would
be unanswerable or degenerate):
- At 90% throttle, system current draw (4 motors) is 82.40 A (Sparrow) and 117.84 A (Albatross).
- At 33.5 mph over a 4 mi route, flight time is ~7.16 min.
- Energy used: Sparrow 9.84 Ah, Albatross 14.07 Ah, against a 22 Ah pack — both leave more than the
  25% mandatory reserve (55.3% and 36.1% remaining respectively), so D5 is answerable and non-trivial
  for both configurations without forcing a contrived failure.
- The original Zipline-anchored 10 mi route length was rejected at this step specifically because
  it failed this feasibility check for both configurations (would require a battery pack far larger
  than this motor class could plausibly carry) — this is the reason MA5 uses Flytrex's 4 mi figure
  instead.

## Confidence summary

| Grade | Sources |
|---|---|
| HIGH | S1, S2 (T-Motor primary datasheets), S3 (NWS), S5 (DJI), S8 (14 CFR via Cornell LII) |
| MEDIUM | S4 (aggregated industry wind-resistance benchmark), S6 (trade press reporting Flytrex spec), S7 (representative battery listing) |
| LOW | none used |

**NOT FOUND count: 2** — (1) a public wind reading for this specific fictional corridor
(pre-flagged by the concept sheet as an intended Modeling Assumption, MA1); (2) a specific FAA/UAS
battery-reserve percentage rule (became MA7, analogized to 14 CFR 91.151). Both handled as
disclosed Modeling Assumptions per SPEC §5, not invented as fact.

Next step: `case-qa` on `the-crosswind-cut`.
