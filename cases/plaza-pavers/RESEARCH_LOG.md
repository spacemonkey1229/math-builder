# RESEARCH_LOG — Plaza Pavers

Every `{{NEEDS_SOURCE}}` placeholder from `case-write`, what was searched, and how it resolved.
28 placeholders total. 4 real distinct claims verified live 2026-08-12 (spot-check re-fetch after
initial search) — see `case.json.sources[]` for full citation records.

| # | Placeholder (Appendix) | Search framing(s) tried | Resolution |
|---|---|---|---|
| 1 | Cost cap, $/sq ft (Background/D) | municipal capital-improvement bid documents for a real public plaza cost cap | NOT FOUND (no such document exists for a fictional plaza) → **MA3**: $30.00/sq ft, set just above S6's real 2026 national basic-pattern high end ($28.49) |
| 2 | Plaza footprint, ft × ft (Background/C) | real public plaza renovation project footprints, as a scale anchor | NOT FOUND (fictional plaza has no real plan) → **MA2**: 200×150 ft (30,000 sq ft), area matched to S5 (a real, different, comparable-scale civic paver job) as a scale anchor only |
| 3–9 | Interior angle, pentagon–dodecagon (Appendix A) | none needed — pure arithmetic from `(n-2)×180/n`, the formula already stated in the case | Derived, not sourced. Confirmed by hand and by `sensitivity_model.py._hex_area_sqft`/`_octagon_area_sqft` at research time; final values folded into `case.json.derived.interior_angles_deg` |
| 10 | Rhombus/kite rejection reason (Appendix A) | real trade-press reasons a hardscape firm would reject a valid tessellating paver shape | Genuine trade reasoning exists (acute-corner spalling under snowplow blades is a real, well-known paver durability issue) but no single citable source ties it to *this* fictional rejection → written directly as case narrative (`needs_source[]` status `DROPPED`), same convention as a fictional protagonist's backstory — not a claimed external fact |
| 11 | Hexagon paver module size (Appendix B) | "hexagon concrete paver dimensions price manufacturer spec sheet" (WebSearch) → Belgard, Stepstone, Super Arbor listings found | **S1** — Super Arbor, 10.25"×10.25" hexagonal concrete paver product listing. Re-fetched live 2026-08-12, confirmed. |
| 12 | Hexagon paver price (Appendix B) | same listing | **S2** — same Super Arbor page, $1,162.00/112-pc pallet → derived $10.36/paver |
| 13 | Octagon paver module size (Appendix B) | "octagon and square paver combination module price manufacturer spec" (WebSearch) → Hanover, Western Interlock, Cement Products Mfg found | **S3** — Hanover Architectural Products "Multisided Paver System," 15⅞" across flats. Fetched live directly, confirmed. |
| 14 | Square paver module size (Appendix B) | same page | **S4** — same Hanover page, 6 9/16" |
| 15 | Octagon+square set price (Appendix B) | Hanover and Western Interlock product pages checked directly; both say "contact sales," no public list price | NOT FOUND (confirmed — matches `domains.json`'s own `tiling-pattern-art.data_availability.note`: "Tile prices... are not published centrally") → **MA1**: +25% material premium over the hex paver's real per-sq-ft cost, basis stated in `case.json.modeling_assumptions[]` |
| 16 | Pavers per sq ft, both options (Appendix B) | none needed — derived from sourced module dimensions via regular-polygon area formulas | Derived (`derived: true`), not fabricated — real hexagon/octagon/square area math from S1/S3/S4's real dimensions |
| 17 | Installed-cost benchmarks, material & labor (Appendix D) | "Angi HomeGuide paver patio installation cost per square foot intricate pattern vs simple pattern"; "paver installation waste factor percentage cut pattern industry standard" (WebSearch) | **S7** — StoneCenters, material $2–$8/sq ft, installation $7–$15/sq ft. Re-fetched live 2026-08-12, confirmed. MEDIUM confidence (aggregator blog, on-page date only in title). |
| 18 | Intricate-pattern labor premium (Appendix D) | same StoneCenters page | **S8** — "intricate patterns...can add 15%-25% to labor costs." Case uses the 20% midpoint. Confirmed live 2026-08-12. |
| 19 | Waste factor, simple vs. cut pattern (Appendix D) | "paver installation waste factor percentage cut pattern industry standard" (WebSearch) → pavercalculator.net blog: stack/running bond 2–10%, diagonal/herringbone ~15%, circular 20–25% | Real range found, but no single citable figure for *this* case's specific simple-vs-cut split → **MA4**: 3% simple / 12% cut, order-of-magnitude cross-checked against S8's real 15–25% (labor) / 20–40% (total-cost) bands, not directly cited from the waste-specific source (kept as an assumption, not mislabeled as sourced) |
| 20 | National-average cross-check total (Appendix D) | "Homewyse paver installation cost 2026" | **S6** — Homewyse, $21.74–$28.49/sq ft, national average, May 2026, basic/mid-range work. Re-fetched live 2026-08-12, confirmed. |
| 21 | Historic pavement document + commission quote (Appendix E) | "'octagon and dot' concrete sidewalk pavement historic pattern early 20th century"; TCLF "Neglected Heritage Beneath Our Feet" article fetched directly | TCLF's real historic-pavement article does **not** mention octagon-and-square patterns by name — checked, not found. Kessler Plaza's own 1962 pavement and the commission's quoted preference are fictional case narrative (status `DROPPED`, not a claimed real citation), consistent with how every case invents its own protagonist/company/site. The real-world grounding that *does* exist — multiple manufacturers (Hanover, Western Interlock, Cement Products Mfg.) market the octagon+square combination today as a "classic and timeless" pattern — is noted in Appendix E as qualitative color, not a numeric or dated claim. |

## Supplemental verification (beyond the original 28 placeholders)

- Confirmed geometrically: Hanover's real octagon (15⅞" across flats) and square (6 9/16" side)
  dimensions are consistent with a genuine semi-regular 4.8.8 tessellation (theoretical square
  side implied by the octagon's across-flats measurement: 15.875 / (1+√2) ≈ 6.575", within
  manufacturing tolerance of the real 6.5625" square) — a real product validating the case's own
  geometric premise, surfaced as a "Facilitator-only geometry note" opportunity.
- All four HIGH/MEDIUM-confidence source URLs (S1, S3, S6, S7/S8) re-fetched live 2026-08-12 and
  confirmed to still carry the cited figures — Tier 2 probe 6 (dead-link/data-decay check) should
  re-verify at QA time regardless, since sources rot.

## Not attempted

None. All 28 original placeholders reached a terminal status (SOURCED / ASSUMPTION / DROPPED) —
see `case.json.needs_source[]`.

**Next step:** Run `case-readiness` on `plaza-pavers`.
