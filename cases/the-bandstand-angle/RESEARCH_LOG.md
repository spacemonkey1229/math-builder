# Research Log — The Bandstand Angle

`case-research`, 2026-09-05. This case was authored with four real, load-bearing sourcing needs
(lumber price, carpenter wage, a custom-fabrication labor premium basis, a land-grading cost basis)
and, per the approved concept sheet's own explicit guidance, one large figure set (the corner lot's
boundary geometry) that was always going to need a stated Modeling Assumption rather than a
citation, since no real address was to be used. All four sourceable figures were found and directly
fetched; the site geometry and four dollar-figure point estimates anchored inside two of the
sourced ranges were accepted as Modeling Assumptions.

## P01 — Framing lumber composite price

**Need:** a real, dated 2×6 (or general dimensional framing) lumber price to cost Appendix D's
board-foot takeoff.

- Searched: `framing lumber composite price per 1000 board feet 2026 NAHB` — surfaced NAHB's own
  "Framing Lumber Prices" page, which republishes the named, industry-standard Madison's Lumber
  Price Index weekly (the same primary source used for Roofline Call's S2, re-fetched fresh rather
  than reused, since lumber prices move weekly).
- Fetched directly: **$521.35 per 1,000 board feet, week of August 28, 2026.**
- **Outcome: SOURCED**, confidence **HIGH** (a national trade association republishing a named,
  dated index in unambiguous units — passes all four HIGH criteria).
- Recorded as **S1**, cited in Appendix C. Converts to $0.52135/board-foot.

## P02 — Carpenter labor wage (basis for Appendix E's cut-time assumptions)

**Need:** a real wage figure as the basis for the two cut-time Modeling Assumptions (MA2, MA3), so
the derived per-cut dollar costs aren't invented outright.

- Searched: `BLS median hourly wage carpenters occupational outlook handbook` — surfaced the U.S.
  Bureau of Labor Statistics' own Occupational Outlook Handbook page for Carpenters directly (a
  primary government source, more current than the May 2024 figure used in Roofline Call).
- Fetched directly: median annual wage **$60,580** and median hourly wage **$29.12**, May 2025 data.
- **Outcome: SOURCED**, confidence **HIGH** (primary U.S. government labor statistics agency,
  dated, unambiguous units).
- Recorded as **S2**, cited as the basis for MA2/MA3.

## P03 — Custom/non-repeated framing labor cost premium

**Need:** a real basis for MA3 (the time premium Option B's six non-identical hip rafters carry
over Option A's eight identical ones), since the concept sheet flagged this exact category of
figure as needing a documented, real construction-industry markup rather than an invented multiple.

- Searched: `custom cut structural member fabrication cost premium versus repeated identical framing
  member` — returned mostly metal-fabrication pricing pages (not directly on point) and one
  construction-framing-specific result.
- Fetched directly: EB3 Construction's "How To Estimate Framing Costs Per Square Foot" states that
  "angled layouts, curved walls, and specialty architectural features can add 30 to 60 percent to
  baseline framing costs compared to simple rectangular buildings," attributed to the extra
  cutting, custom fabrication, and specialized layout non-repeated members require — directly on
  point for the identical-vs-non-identical rafter distinction this case turns on.
- **Outcome: SOURCED (range), confidence MEDIUM** (a construction-industry blog, not a primary
  trade association or government document, but specific and directly on point, with a named,
  concrete mechanism, not a vague "typically more expensive" claim).
- Recorded as **S3**. The case's own MA3 premium (45%) is a point estimate the case author chose
  inside this sourced 30-60% range — not the range itself presented as a citation for a specific
  number, and not a hard timing study (none exists publicly for hip-rafter fabrication
  specifically, so a point estimate anchored to a real range is the correct exit, matching the
  Roofline Call MA2 precedent).

## P04 — Land grading / site-prep cost basis

**Need:** a real basis for MA4/MA5 (the two site-prep grading rates), since no public figure exists
for "regrading cost differential between a symmetric vs. a contour-fit small structure footprint on
this specific constructed lot."

- Searched: `site excavation grading cost per square foot small structure 2026` and `retaining wall
  cost per linear foot 2026` — the grading search returned a clean, current per-square-foot range;
  the retaining-wall search was explored as an alternative framing but not used (see below).
- Fetched directly: Lawn Love's "How Much Does Land Grading Cost?" gives an overall headline range
  of $0.08 to $2.00 per square foot, but breaks this into two more specific sub-ranges: **fine/finish
  grading, $0.40 to $1.00 per square foot** (leveling the top 1"-3" of soil), and **rough grading,
  $1.00 to $2.00 per square foot** (removing slopes or contouring for drainage).
- **Correction (2026-09-05):** an earlier pass through this case cited the page's overall headline
  as "$0.80 to $2.00/sq ft" — a transcription error introduced when an initial web-search summary
  was taken at face value instead of the page itself. A direct re-fetch of the page caught the
  error before this case reached Tier 2. Corrected to the two accurate sub-ranges above; both of
  this case's existing point estimates (MA4 $1.10, MA5 $0.95) already fell inside their respective
  correct sub-ranges (rough and fine/finish, respectively) once corrected, so only the citation
  text needed fixing, not the case's own numbers.
- **Outcome: SOURCED (two sub-ranges), confidence MEDIUM** (a home-services cost-guide aggregator,
  not a primary source, but specific, current, and directly applicable).
- Recorded as **S4**. MA4 ($1.10/sq ft, Option A — more full-envelope cut-and-fill regrading since
  its symmetric shape doesn't track the existing contour) is anchored inside the rough-grading
  sub-range; MA5 ($0.95/sq ft, Option B — lighter finish grading only, since its vertices were
  chosen to follow the existing contour) is anchored inside the fine/finish-grading sub-range. Both
  are point estimates the case author chose inside a sourced range, not independently sourced
  figures.
- **Rejected framing:** an earlier draft considered pricing Option A's site-prep as a discrete
  retaining-wall line item (retaining wall cost ranges $20-$100+/linear ft were found and are real,
  but concrete/wall-specific figures), instead of a uniform per-square-foot grading rate applied to
  each option's own footprint. Rejected because a full retaining wall is a much larger, more
  specific claim about this constructed site's actual grade break than the case needs to make, and
  a flat per-square-foot grading-rate differential tells the same real story (more regrading work
  for a shape that doesn't track the lot's own contour) without inventing a wall length/height that
  would itself need its own unsupportable Modeling Assumption on top of an already-constructed
  scenario.

## MA1 — Constructed site geometry

**Need:** the corner lot's buildable envelope, both options' side lengths and hip-rafter runs, the
covered footprint areas, and the hexagon's five known/one unknown interior angles.

- **No search performed for this figure set** — the approved concept sheet was explicit that a real
  address was out of scope ("the exact site boundary geometry itself will likely need to be a
  constructed scenario... disclose it explicitly as a Modeling Assumption, not presented as
  sourced"). This is not a NOT FOUND outcome; it was correctly identified up front as belonging to
  the Modeling Assumption exit, the same way Roofline Call's own building footprint was the
  drafter's authored design rather than a researched fact — except here, per the concept sheet's
  explicit instruction, it is disclosed under the Modeling Assumptions heading itself (Appendix E,
  MA1) rather than presented unmarked in a plain data appendix.
- **Outcome: ASSUMPTION**, disclosed as MA1. Built to be internally consistent with a real
  corner-lot infill scenario (an irregular buildable envelope, a partially completed re-survey with
  one open corner) rather than checked against any real property.

## Summary

| Figure | Outcome | Confidence | Case location |
|---|---|---|---|
| Framing lumber price | SOURCED (S1) | HIGH | Appendix C |
| Carpenter wage | SOURCED (S2) | HIGH | Appendix E basis (MA2/MA3) |
| Custom-fabrication labor premium range | SOURCED (S3) | MEDIUM | Appendix E basis (MA3) |
| Land-grading cost range | SOURCED (S4) | MEDIUM | Appendix E basis (MA4/MA5) |
| Site boundary geometry (envelope, sides, runs, footprints, 5 angles) | ASSUMPTION (MA1) | — | Appendix B / E |
| Simple/batch cut time | ASSUMPTION (MA2) | — | Appendix E |
| Custom cut-time premium (point estimate) | ASSUMPTION (MA3) | — | Appendix E |
| Site-prep rate, Option A (point estimate) | ASSUMPTION (MA4) | — | Appendix E |
| Site-prep rate, Option B (point estimate) | ASSUMPTION (MA5) | — | Appendix E |

Zero placeholders remain `OPEN`. Zero figures were invented, rounded from a remembered number, or
laundered from a contested source. The one large figure set that could not be sourced (the site's
own boundary geometry) was never treated as sourceable in the first place — the concept sheet
called this correctly before research began — and is disclosed exactly where SPEC §5 requires,
under a visible Modeling Assumptions heading, not buried in a plain data table.

Next step: run `case-readiness` on `the-bandstand-angle`.
