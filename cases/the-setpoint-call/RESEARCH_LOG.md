# Research Log — The Setpoint Call

One row per placeholder from `case-write`'s handoff (8 total). Searched via WebSearch/WebFetch,
2026-09-09. Rejections are recorded because they are the valuable part — they stop the next person
re-running the same dead search.

## P01 — Base cost rate to operate a rotary bottle labeler, USD/min, independent of speed

- Searched: "BLS median wage Packaging and Filling Machine Operators and Tenders 2025", then
  fetched `bls.gov/oes/current/oes519111.htm` directly.
- Found: the primary BLS OEWS page is an index of downloadable data-table files, not an
  occupation-level figure page — could not extract the number directly from it.
- Fallback: fetched O*NET OnLine's summary for SOC 51-9111.00, which republishes BLS 2025 wage
  data with attribution: median $20.78/hour ($43,220/year). Cited as **S1**, MEDIUM (secondary
  republication of a primary government source).
- No public source publishes a per-minute *operating cost rate* for a specific labeler (this
  needs labor burden + baseline utilities, neither of which any manufacturer or trade source
  prices for a generic machine). Searched "typical labor burden rate multiplier manufacturing" and
  found convergent trade/HR-industry figures (1.25×–1.4× base wage) — cited as **S2**, MEDIUM.
- Disposition: **SOURCED (partial) + ASSUMPTION**. [S1]×MA2's 1.3× burden multiplier gives the
  labor+burden component ($0.45/min); MA1 adds a stated $0.45/min baseline utility-draw assumption
  (no public source) to reach the case value, $0.90/min.

## P02 — Incremental operating cost per bottle-per-minute of speed, USD per (bottle/min)

- Searched: "electric motor power draw scaling with machine speed packaging line", "packaging
  line defect rate versus machine speed", "cost of running a labeler faster energy".
- Found: no source publishes a per-speed-unit dollar coefficient for a specific machine — this is
  a genuinely proprietary, machine-specific engineering quantity. The underlying phenomena
  (motor power scales with speed; defect/jam rate rises with speed) are real and well-documented
  in general industrial-engineering/manufacturing literature, but not as a numeric coefficient.
- Found real order-of-magnitude context instead: EIA's industrial electricity price, 9.17
  cents/kWh (June 2026) — cited as **S3**, HIGH.
- Disposition: **NOT FOUND → ASSUMPTION (MA3)**. $0.0004/(bottle/min), informed by [S3] for the
  power-cost order of magnitude and stated explicitly as a scenario simplification for the
  combined power+wear+defect effect.

## P03 — Fixed downstream case-packing/palletizing handling time, min/bottle

- Searched: "case packer cycle time per unit beverage line", "palletizing time per bottle
  co-packing line".
- Found: manufacturer case-packer spec sheets publish throughput in units/minute, but no source
  ties a specific downstream time-per-bottle figure to an upstream labeler's speed decision for a
  generic line.
- Disposition: **NOT FOUND → ASSUMPTION (MA4)**. 0.02 min/bottle (a 50 bottle/min-equivalent
  downstream station), a representative order of magnitude, not tied to any specific source.

## P04 — Manufacturer-rated maximum safe operating speed for a rotary bottle labeler, bpm

- Searched: "rotary bottle labeler rated speed bottles per minute manufacturer spec sheet".
- Found: multiple manufacturer pages (Quadrel, Maharshi, ZONESUN, Parthec) publish speed ranges;
  Quadrel's own page states "speed capabilities from 100–500 bottles per minute" across its
  rotary labeling machine line. Cited as **S4**, MEDIUM (general manufacturer capability
  statement, not one machine's dated spec sheet).
- Disposition: **SOURCED (range) + ASSUMPTION**. Line 3's own specific rated speed is
  protagonist-specific and not independently found — MA5 sets it at 150 bpm, the conservative end
  of [S4]'s documented range, consistent with Line 3 being an older, existing installation rather
  than a new high-speed line.

## P05 — Name, publisher, and scope of the real machinery-safety standard governing packaging-machinery guarding/speed

- Searched: "ANSI PMMI B155.1 safety requirements packaging machinery guarding speed", then
  fetched `blog.ansi.org`'s summary and `pmmi.org/standards-and-regulations`.
- Found: ANSI/PMMI B155.1 (current edition B155.1-2023) is real, confirmed by both ANSI's own
  blog and PMMI's own standards page — a risk-assessment-based standard for packaging machinery
  safety, requiring hazard identification and risk reduction across the machine's life cycle.
  Cited as **S6**, MEDIUM.
- Attempted but could not confirm: the exact clause language tying a specific guarding
  configuration to a specific numeric operating-speed threshold — that text sits behind ANSI's
  paywall (a purchased standard document), and no free secondary source quotes it. Searched "OSHA
  machine guarding risk assessment required when increasing operating speed" and found only the
  general, real principle (a risk assessment is warranted when operating parameters change) —
  not a numeric threshold.
- Disposition: **SOURCED (existence/scope) + case does not claim beyond what is public**. The
  case cites the standard's real existence and general methodology, and treats "how much guarding
  a speed increase requires for Line 3 specifically" as MA6's own disclosed assumption rather than
  a quoted clause — avoiding the overclaiming this project's own doctrine warns against (SPEC §5).

## P06 — Capital cost of a guarding/interlock retrofit for higher-speed operation, USD

- Searched: "cost of machine guarding retrofit interlock upgrade industrial equipment price
  range".
- Found: a safety-equipment blog (The Safety Geek) states a safety-rated interlock door (switch,
  controller, wiring) runs $1,500–$5,000. Cited as **S5**, LOW (a blog/consultant page, not a
  manufacturer price list or standards body — graded per case-research's tier-4 rule).
- No public source prices a full-line, multi-zone retrofit (which is what this case actually
  needs — turret access panels, infeed/outfeed conveyor guarding, an updated safety PLC, not one
  door).
- Disposition: **NOT FOUND (at the needed scope) → ASSUMPTION (MA6)**. $44,000, disclosed as
  extending [S5]'s per-door range to a comprehensive multi-zone scope — [S5] is explicitly not
  presented as the retrofit's own literal cost.

## P07 — Total production volume of the co-packing contract, bottles

- Searched: "beverage co-packing contract volume typical exclusive agreement".
- Found: co-packing contract volumes are commercially confidential; no public source publishes a
  representative figure for "a multi-month exclusive contract on one line."
- Disposition: **NOT FOUND → ASSUMPTION (MA7)**. 10,000,000 bottles, protagonist-specific, set at
  a realistic fraction of Line 3's theoretical full-time capacity over a multi-month contract
  (well under running 24/7 at r*'s ~335 bpm for the whole period).

## P08 — Guarding-retrofit contractor's install lead time relative to the production start date

- Searched: "machinery guarding retrofit installation lead time".
- Found: general industrial-automation retrofit sources describe lead times varying widely by
  scope and are not standardized publicly; nothing ties a lead time to this specific scenario.
- Disposition: **NOT FOUND → ASSUMPTION (MA8)**, and not load-bearing to any deliverable's
  arithmetic (same role as `cases/the-marginal-call`'s ship-deadline MA7) — kept as narrative
  urgency only, matching the Background's own stated timeline.

---

## Summary

| Placeholder | Disposition | Resolved by |
|---|---|---|
| P01 base cost rate | SOURCED (partial) + ASSUMPTION | S1, S2, MA1, MA2 |
| P02 incremental cost rate | ASSUMPTION | MA3 (informed by S3) |
| P03 downstream handling time | ASSUMPTION | MA4 |
| P04 rated max speed | SOURCED (range) + ASSUMPTION | S4, MA5 |
| P05 safety standard | SOURCED | S6 |
| P06 retrofit cost | ASSUMPTION | MA6 (informed by S5) |
| P07 contract volume | ASSUMPTION | MA7 |
| P08 install lead time | ASSUMPTION | MA8 |

**NOT FOUND count: 6** (P02, P03, P06, P07, P08 fully; P01 and P04 partially). All six became
disclosed Modeling Assumptions with a stated basis and range — none were silently filled. Zero
figures were invented and presented as sourced.

Next step: `Run case-readiness on the-setpoint-call.`
