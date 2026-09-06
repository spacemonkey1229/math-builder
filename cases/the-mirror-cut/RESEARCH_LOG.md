# Research Log — The Mirror Cut

`case-research`, 2026-09-05. This case was authored with seven real, load-bearing figures needed
(sheet size, steel price/weight, cutting speed, pierce time, machine wage, machine operating cost,
mirrored-nesting yield improvement) and one general, real, cross-corroborated phenomenon needed as
the basis for three stated Modeling Assumptions (heat-affected-zone buildup in tightly nested laser
cuts). All eight were found; no figure returned a hard NOT FOUND that forced a redesign, though two
searches were rejected as too low-quality to cite before better sources were found (see P02 and
P05 below).

## P01 — Standard stocked steel sheet size for laser cutting

**Need:** a real, commercially standard sheet size to nest brackets against.

- Searched: `standard steel sheet size 4x10 feet laser cutting stock size` — surfaced several job
  shops' own capability pages (Fabworks, Xometry) and a forum thread (WeldingWeb) converging on
  48 in × 120 in (4 ft × 10 ft) as a common stocked size, alongside 4×8 ft as also common.
- Fetched Fabworks' own "Max Cuttable Size" FAQ page directly: confirms 48 in × 120 in as their
  standard stocked size, with up to 60 in × 120 in cuttable on request.
- **Outcome: SOURCED**, confidence **MEDIUM** (one shop's own stocked-inventory size, generalized;
  not a national standards-body figure, but corroborated as a common commercial size by the
  broader search).
- Recorded as **S1**, cited in Appendix B.

## P02 — 16-gauge steel sheet price and weight

**Need:** a real, dated price per pound for the case's chosen gauge, plus a real weight-per-area
figure to compute full-sheet weight.

- Searched: `hot rolled steel sheet price per pound 2026` and `cold rolled steel sheet price per
  pound 16 gauge supplier price list 2026` — returned mostly commodity-index pricing quoted per
  net ton or per metric tonne (Nucor, Cleveland-Cliffs, FRED PPI series), which does not resolve
  to a specific gauge, specific sheet, or a price a small shop would actually pay. **Rejected as
  the primary figure** — a bulk mill index price doesn't reflect what a six-person shop buying
  modest quantities of cut-to-size sheet would pay, and doesn't give a weight-per-sheet figure
  directly.
- Searched again, more specifically: the same query surfaced SpeedyMetals' own product page for
  16-gauge (0.060 in) cold-rolled steel sheet, listing exact prices and weights for several cut
  sizes (12×12 in: $7.20 / 2.448 lb; 12×18 in: $10.81 / 3.672 lb; 12×24 in: $14.41 / 4.896 lb — all
  three back out to the same $2.94/lb). Fetched directly.
- **Outcome: SOURCED**, confidence **MEDIUM** (small-quantity, cut-to-size retail pricing from a
  named metals retailer — a shop buying full 48×120 sheets in volume for a 3-year, 120,000-part
  contract would likely negotiate a lower bulk rate than this retail price; the case states this
  caveat explicitly rather than presenting the retail price as a mill contract price).
- Recorded as **S2**, cited in Appendix B. The $2.94/lb figure and the 2.448 lb / 144 sq in
  weight-per-area figure are both used directly; sheet weight (97.92 lb for 48×120 in) and material
  cost per sheet ($287.88) are this case's own arithmetic, shown in `case.json.derived`.

## P03 — Fiber-laser cutting speed, 16-gauge mild steel

**Need:** a real cutting-speed figure for the case's gauge and a plausible small-shop laser power.

- Searched: `fiber laser cutting speed inches per minute mild steel 14 gauge spec sheet` — returned
  several vendor speed-chart pages (MachineMFG, RapidDirect, GYC Laser, StyleCNC, LaserSpecHub).
  MachineMFG's own chart page returned HTTP 403 on direct fetch — recorded as **attempted, not
  usable**, not silently skipped.
- Fetched StyleCNC's chart directly: a table of cutting speed vs. thickness across laser power
  levels. At 1.5 mm carbon steel (close to 16-gauge's 0.060 in ≈ 1.52 mm) with a 2 kW fiber laser,
  air/oxygen assist: 25–30 m/min.
- **Outcome: SOURCED**, confidence **MEDIUM** (a manufacturer-facing reference chart giving a
  range, not a single-machine spec sheet for one named shop's actual laser). Case adopts 25 m/min,
  the conservative (slower) end of the range, and states this choice explicitly rather than
  averaging or picking the faster end.
- Recorded as **S3**, cited in Appendix C.

## P04 — Laser pierce time, thin-gauge steel

**Need:** a real per-pierce time figure to cost the pierce-count difference between the two
layouts.

- Searched: `laser cutting pierce time seconds per pierce sheet metal cutting cost calculator` —
  returned several vendor/blog pages. Paramount Machinery's piercing-time article was fetched
  directly but its actual numeric data lived only in embedded chart images, not extractable text —
  recorded as **attempted, not usable**.
- Fetched Kasu Laser's "How Long Does Laser Cutting Take?" page directly: states "each pierce takes
  0.3–3 seconds, depending on thickness and power level," with an explicit worked example of 0.8
  seconds for 3 mm carbon steel.
- **Outcome: SOURCED**, confidence **MEDIUM** (a job shop's general guidance page giving a range
  across thicknesses, not a single-thickness spec). Case adopts 0.3 seconds, the low end of the
  range, appropriate for the case's thinner 16-gauge (1.5 mm) stock relative to the page's 3 mm
  worked example.
- Recorded as **S4**, cited in Appendix C.

## P05 — Machine-and-labor rate for costing machine time

**Need:** a real hourly rate to convert cut/pierce seconds into a dollar cost.

- Searched first: `fiber laser cutting machine shop rate per hour cost fabrication 2026` — returned
  mostly vague, unsourced "$75-150/hour" claims repeated across marketing pages with no primary
  attribution, and one page (LaserCalcPro) that explicitly states it provides a *methodology*, not
  a real number ("this guide intentionally treats example numbers as planning placeholders, not
  universal rates"). **Rejected as a citation** — this is exactly the SPEC §5 "plausible is not the
  same as true" case; several of these pages likely inflate the figure with machine depreciation
  assumptions inappropriate for a six-person shop's actual fixed laser.
- Instead built the rate from two real, narrower, better-attributed figures:
  - Searched `BLS occupational outlook handbook computer numerically controlled machine tool
    operators median wage`, then fetched the BLS OOH page for "Metal and Plastic Machine Workers"
    directly (a primary U.S. government source): median hourly wage **$22.94/hr**, May 2025 data.
    **Outcome: SOURCED**, confidence **HIGH**. Recorded as **S5**.
  - Searched `fiber laser cutting machine shop rate per hour cost fabrication 2026` again with a
    narrower operating-cost framing, and fetched Arcus CNC's "Laser Cutter Cost Breakdown" page
    directly: a worked hourly operating-cost breakdown for a 6 kW fiber laser cutting carbon steel
    with oxygen assist — electricity + assist gas + consumables = **$7.00/hr**, explicitly
    excluding labor and depreciation. **Outcome: SOURCED**, confidence **MEDIUM** (a single
    vendor's worked example for one machine class, not a survey). Recorded as **S6**.
  - Combined S5 + S6 into a blended **$29.94/hr** machine-and-labor rate. This combination is the
    case's own derivation (`derived: true` reasoning), not a single sourced figure — logged here so
    the arithmetic is traceable back to its two real inputs.

## P06 — Real-world material-yield improvement, mirrored vs. simple nesting

**Need:** a real, vendor-published comparison of material utilization between mirrored/advanced
nesting and basic/simple nesting, per the approved concept's own sourcing guidance.

- Searched: `nesting software mirrored vs simple layout material yield percentage sheet metal laser
  cutting` — surfaced several nesting-software vendor pages (SigmaNEST, Autodesk, Ponoko, SLTL
  Group, Canadian Fabricating & Welding, The Fabricator). Search-result summaries mentioned "most
  customers saving more than 4%... advanced nesting can reach 10 to 15 percent" and a worked
  example of "82% utilization → 87% utilization" with rotation/mirroring.
- Fetched SLTL Group's article directly for exact wording: **"10–15%" direct material savings
  "through tighter part clustering"** from smart/advanced nesting (which the article explicitly
  attributes in part to rotation and mirroring features), separate from a "5%" programming-time
  savings figure and a blended "up to 20 percent" total-cost claim.
- **Outcome: SOURCED**, confidence **MEDIUM** (a nesting-software vendor's own published figure;
  directionally consistent with the search-summary figures from other vendor pages, but no
  independent third-party audit was found for either the 10–15% range or the specific 82%→87%
  example).
- Recorded as **S7**, cited in Appendix C. Case adopts 12%, a value picked within the sourced
  10–15% range (per the "wide range, picked a value" MEDIUM-confidence pattern), applied directly
  to Straight-Run parts-per-sheet (196 → 219, floor of 196 × 1.12) rather than re-deriving an exact
  2-D packing solution by hand, which is out of scope for a MS-band case and would not itself be
  more defensible than a real vendor-published industry figure.

## P07 — Basis for the machine-time and reject-rate Modeling Assumptions (MA1/MA2/MA3)

**Need:** the concept sheet flagged "more transformations does not always mean more savings" as the
required rubric trap — a real mechanism was needed for why a tighter mirrored nest costs the shop
*more* machine time and carries *more* risk, not just less material.

- Searched: `laser cutting nesting heat distortion closely spaced parts slower speed thermal
  buildup` — surfaced several fabrication-industry pages (The Fabricator, Reger Laser, Hightech
  Industry Group, ADH Machine Tool). The Fabricator's own "Nesting fundamentals for laser cutting
  stability" article returned HTTP 403 on direct fetch — recorded as **attempted, not usable**.
- Fetched Reger Laser's thermal-stress article directly: **"tight clusters of cuts concentrate heat
  in one area"**; **"sequence cuts so heat is spread across the sheet instead of stacked in one
  spot, and let an area cool before cutting next to it."**
- Fetched Hightech Industry Group's warping-prevention article directly: corroborates the same
  general phenomenon (managing cut density and sequencing to avoid concentrated heat).
- **Outcome: SOURCED (as a general, qualitative phenomenon)**, confidence **MEDIUM**, cross-
  corroborated by two independent fabrication-industry sources. Recorded as **S8**.
- **The specific multipliers are NOT sourced from S8 or anywhere else — no public per-shop study
  times this exact pierce-count multiplier, speed penalty, or reject-rate pair for this exact part
  and nest.** Per SPEC §5's three-exit rule, exit taken: **stated Modeling Assumption** for the
  numeric values, built on S8's real mechanism as basis. Recorded as **MA1** (2× pierces),
  **MA2** (70% cutting speed), and **MA3** (1% / 4% reject rates) in Appendix E. MA1/MA2 are
  flagged for Tier 2 probe 5 flexing; MA3 is disclosed as sensitive without stating the direction
  or size of that sensitivity in `case.md`, per `skills/case-write/SKILL.md`'s no-answer-key rule.

## Summary

| Placeholder | Outcome | Confidence | Case location |
|---|---|---|---|
| Standard sheet size | SOURCED (S1) | MEDIUM | Appendix B |
| Steel price + weight/area, 16ga | SOURCED (S2) | MEDIUM | Appendix B |
| Laser cutting speed, 16ga | SOURCED (S3) | MEDIUM | Appendix C |
| Pierce time, thin gauge | SOURCED (S4) | MEDIUM | Appendix C |
| Machine-worker wage | SOURCED (S5) | HIGH | Appendix C |
| Laser operating cost/hr | SOURCED (S6) | MEDIUM | Appendix C |
| Mirrored-nesting yield gain | SOURCED (S7) | MEDIUM | Appendix C |
| HAZ/heat-distortion phenomenon (basis for MA1-MA3) | SOURCED (S8, qualitative) | MEDIUM | Appendix E basis |
| Pierce-count multiplier (MA1) | ASSUMPTION | — | Appendix E |
| Cutting-speed penalty (MA2) | ASSUMPTION | — | Appendix E |
| Reject rates (MA3) | ASSUMPTION | — | Appendix E |

Zero placeholders remain `OPEN`. Zero figures were invented, rounded from a remembered number, or
laundered from a contested source. The bracket's own coordinate geometry in Appendix A is Sam's own
stated part design (not public data), consistent with the Roofline Call precedent for an authored
part design. Two searches (a bulk mill-index steel price, and vague unsourced "$75-150/hr shop
rate" marketing claims) were explicitly rejected as too low-quality or mismatched to this shop's
actual scale to cite, and better, narrower sources were found instead — the rejections are recorded
above so the next person doesn't re-run the same searches expecting a different result.

Next step: run `case-readiness` on `the-mirror-cut`.
