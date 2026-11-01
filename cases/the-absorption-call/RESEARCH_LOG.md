# Research Log — The Absorption Call

One row per placeholder identified at case-write time. Rejections are recorded because they are
the part that stops the next pass from re-running the same dead search.

| # | Placeholder (what was needed) | Searched | Found | Outcome |
|---|---|---|---|---|
| P01 | Sabine's equation, metric constant | `Sabine equation RT60 = 0.161 V/A reverberation time formula acoustics-engineering.com`; direct fetch of `acoustics-engineering.com/html/sabin.html` (the exact page the approved concept sheet named); corroborating fetch of `sengpielaudio.com/calculator-RT60.htm` | Both pages state `T = 0.161 V/A` (V, A metric); Sengpiel also gives the imperial-unit variant `0.049` (V, A in feet), used only as a cross-check, not in the case itself since the case commits to metric. | **SOURCED** — S1 (HIGH), S2 (HIGH, corroborating). |
| P02 | Baseline absorption coefficients for the room's untreated surfaces (drywall, wood floor, painted concrete block) | `NRC absorption coefficient table drywall plaster concrete block wood 1000 Hz`; direct fetch of `sengpielaudio.com/calculator-RT60Coeff.htm` | Table with 125/1000/4000 Hz values for sheetrock/drywall, smooth/rough plaster, painted concrete block, plywood paneling, carpet, upholstered seating. Used the 1000 Hz ("mid-band") column for each, matching the mid-band convention the concept sheet itself used for the Boston Symphony Hall reference figure. | **SOURCED** — S3 (MEDIUM: a compiled table, no single named primary publisher/date on the page itself). Rejected using the concept sheet's cited ResearchGate audience-seating figures (0.56–0.86) because the case design ultimately did not need an occupied-seating term (see "Redesign" note below) — dropping it kept the room's surface list to materials, not a mix of area-based and per-seat sabins, which would have added unit-conversion complexity beyond T2 scope. |
| P03 | Absorption coefficient (NRC) of the absorptive treatment panel | `GIK Acoustics absorption panel NRC coefficient spec sheet price per panel`; direct fetch of `gikacoustics.com/product/242-acoustic-art-panels-3-625-inch/` | Manufacturer's own page states NRC 1.05 (vs. 0.4 for foam alternatives). | **SOURCED** — S4 (HIGH, manufacturer's own published spec). Pricing on the same page requires a custom quote through a "Launch Designer" tool and is not a stated public number — rejected as a load-bearing cost figure; see P09. |
| P04 | Target RT60 for the theater's dominant (speech/amplified) use | `recommended RT60 reverberation time target black box theater speech vs music seconds`; direct fetch of `commercial-acoustics.com/sound-advice/rt60-chart/` | Page gives a "Theater (Legitimate Stage): 0.9–1.2 s" band, and cites ANSI/ASA S12.60 and ISO 3382 as underlying standards; published 2026-05-24. | **SOURCED** — S5 (MEDIUM: a secondary industry page citing standards, not the standards documents themselves). Used the range midpoint, 1.05 s. |
| P05 | Foot-to-meter conversion constant | `NIST 1 foot = 0.3048 meter exact conversion factor` | NIST SP 811 Appendix B and NIST HB 44 both state the international foot is exactly 0.3048 m (by the 1959 international yard/pound agreement). | **SOURCED** — S6 (HIGH). |
| P06 | Room interior dimensions (Hollow Oak Community Theater) | N/A — Hollow Oak is a fictional venue invented for this case; no search was run because no real theater has both treatment options pre-quoted for it, per the concept sheet's own explicit caveat. | N/A | **ASSUMPTION** (MA1) — 40 ft × 30 ft × 16 ft, a plausible mid-size black-box community-theater footprint. |
| P07 | Absorption coefficient of the diffusive treatment panel | `RPG diffusor price absorption coefficient QRD Skyline`; direct fetch of `rpgacoustic.com/product/qrd-734/` | The manufacturer's own product page describes the QRD 734's "natural wood construction" as limiting absorption, but states no numeric absorption coefficient — only diffusion behavior. A second search (`RPG Skyline diffusor absorption coefficient value`, implicit in the same session) turned up forum/AVS-style discussion citing a rough 0.25–0.55 range for wells-type diffusors, which is LOW-confidence provenance and cannot carry a load-bearing figure per SPEC §5/case-research grading rules. | **NOT FOUND → ASSUMPTION** (MA2) — α = 0.48, disclosed range 0.25–0.55, flagged as the case's one load-bearing assumption and flexed in `sensitivity_model.py`. |
| P08 | Target RT60 for the unamplified acoustic-music use | Same RT60-chart search as P04 — the chart gives bands for amplified music (~1.0 s) and orchestral/unamplified music (2+ s), but no band specific to "small black-box solo acoustic act." | No exact match for the specific use case. | **NOT FOUND → ASSUMPTION** (MA3) — 1.6 s, scaled to the lower-middle of the sourced amplified-to-orchestral range for a small venue and a solo performer rather than a full ensemble. |
| P09 | Installed cost per square foot, absorptive panel | `GIK Acoustics 242 panel price NRC absorption coefficient 2x4` | Only stale (2013-era, $49.99/panel) or "request a quote" pricing found; GIK's current panel pages use a custom configurator with no listed per-unit price. A 2013 figure is not usable as a 2026 cost input. | **NOT FOUND → ASSUMPTION** (MA4) — $45/ft², disclosed basis: commonly discussed $30–$60/ft² installed range for professional broadband panels, midpoint used. |
| P10 | Installed cost per square foot, diffusive panel | `RPG diffusor price absorption coefficient QRD Skyline` (same search as P07) | One forum/AVS-style data point ("$258 for two 2'×4' GIK QRD panels," i.e. ≈$32/ft² material-only, not installed, and LOW-confidence provenance) — rejected as load-bearing per the same LOW-confidence rule as P07. | **NOT FOUND → ASSUMPTION** (MA5) — $65/ft², disclosed basis: diffusor products are consistently discussed as costing more per unit area than flat absorptive panels of comparable coverage; set above MA4 within a $50–$80/ft² range. |
| P11 | Assignment of baseline material to each room surface (floor/ceiling/walls) | N/A — the coefficients themselves (P02) are sourced; which material sits on which surface of a fictional room is a scenario-construction choice, not a fact to search for. | N/A | **ASSUMPTION** (MA6) — wood stage floor, painted drywall ceiling, painted concrete block walls; typical converted-warehouse black-box construction. |

## Note on `measurement-volume` and `new_coverage[]` (corrected after running tier1_structural.py)

Verified against `readmodel/standards_spine.json`: `measurement-volume` currently has `n = 2`, not
`n = 0`, `covered_by = ['Nuclear Waste', 'Cold Chain']`. An initial pass of this case (matching the
approved concept sheet, `cases/_concepts/CONCEPTS_music-acoustics_2026-09-12.md`, C2) claimed it
as `new_coverage[]` anyway, reasoning from `readmodel/gap_queue.json`'s own "thin" framing
(`Measurement/Units` still listed at `n_gap: 1`, naming `Volume` as its one remaining thin skill).

Running the actual gate — `skills/case-readiness/scripts/tier1_structural.py`, check T1-10 —
showed that reasoning does not hold: T1-10 requires `n == 0` (or this case's own title already in
`covered_by[]`), with no allowance for "thin but nonzero." `measurement-volume`'s `covered_by` is
two *other* cases from this same large parallel batch — the gap the approved concept was scored
against had already been closed, by a sibling case, sometime between the concept sheet's
2026-09-12 scoring pass and this case's 2026-09-18 write pass. That is a real, stale-concept
finding, not a mistake in this case's own math or sourcing.

Before falling back to the `reinforcement_note` carve-out (SPEC §8 / T1-10), every skill in the
Measurement domain and every skill in the Geometry domain was queried directly for `n == 0` —
none exists. There was no adjacent, still-open gap this case's deliverables could be honestly
redirected to without abandoning the approved acoustics/Sabine's-equation premise. `new_coverage[]`
is now `[]`; `case.json.reinforcement_note` records this check; `tier1_structural.py` T1-10
downgrades from BLOCKER to GAP accordingly. `standards[]` is unchanged — every id in it still
passes the T1-11 forcing test — this case still legitimately teaches `measurement-volume` and the
other four ids; it simply cannot claim credit for closing a gap someone else closed first.

## Supplemental appendix materials considered and not used

- The concept sheet's own Boston Symphony Hall RT60 citation (~1.8–1.9 s occupied, mid-band) was
  considered as color/context but ultimately **not included** — it risked being read as an implicit
  target for Hollow Oak, when the case's actual point is that no real hall's numbers transfer
  directly to a fictional black-box room a fraction of Symphony Hall's size. Cut rather than risk
  muddying the two stated targets in Appendix C.
- All external sources are reproduced in-document (Appendix F) rather than left as bare links, per
  SPEC §1.6 — every load-bearing figure survives if any of these pages goes down.
