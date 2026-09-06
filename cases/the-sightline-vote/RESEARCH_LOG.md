# Research Log — The Sightline Vote

`case-research`, 2026-09-05. Four placeholders needed. Two returned SOURCED on the first or second
search framing; two returned NOT FOUND and became stated Modeling Assumptions with a real, named
basis.

## P01 — State minimum sightline-safety / interior intersection angle standard

**Need:** a real, citable state or federal standard for the minimum acceptable interior angle at
an at-grade public roadway intersection, since the case's Background states both contractors claim
to clear this standard and neither number has been checked.

- Searched: `state DOT minimum intersection angle skew standard degrees design manual` — surfaced
  several real state DOT figures: Washington State DOT (90° desirable, 60°-120° allowed), Georgia
  DOT (changed from 70° to 75° to match the current AASHTO Green Book), Illinois DOT (within 15° of
  perpendicular preferred, up to 30° from perpendicular under restricted conditions), and
  California DOT (75° minimum).
- Attempted a direct fetch of the primary Caltrans Highway Design Manual PDF
  (`dot.ca.gov/.../chp0400-a11y.pdf`) — the tool could not extract readable text from the PDF's
  internal encoding. Recorded as **attempted, not usable**, same failure mode as roofline-call's
  S1 precedent.
- Searched again for a clean HTML reproduction: found `up.codes/s/angle-of-intersection`, a
  code-reference site that quotes the Caltrans HDM Chapter 400, Topic 403.3 "Angle of Intersection"
  directly: *"the interior angle should be designed as close to 90 degrees as is practical, but
  should not be less than 75 degrees. A 75 degree angle does not unreasonably increase the crossing
  distance or generally decrease visibility."*
- **Outcome: SOURCED**, confidence **MEDIUM** (a code-reference site reproducing a real, dated
  state design manual's own numbered topic, not the primary PDF itself, matching the same
  precedent and grade as roofline-call's S1). Recorded as **S1**, cited in Appendix B and Appendix
  E, and used directly as the case's stated 75-degree minimum.

## P02 — Real quantitative backing for "intersection angle affects safety"

**Need:** the case's own safety-score formula (Appendix B, MA3) needed a real research basis, not
just an invented curve, for why intersection angle should affect a safety score at all.

- Searched: `FHWA Highway Safety Improvement Program typical project cost "intersection skew" OR
  "realignment" versus "channelization" low cost countermeasure` — surfaced FHWA's own
  `FHWA-HRT-20-067`, *Impact of Intersection Angle on Highway Safety* (January 2021), a primary
  federal research report whose stated objective is "to derive quantitative relationships between
  intersection angle and safety." A follow-up search confirmed the report used real Minnesota and
  Ohio crash data and recommends agencies reconsider their "critical minimum angle" design
  policies.
- Attempted a direct fetch of the full PDF — same PDF-encoding failure as P01. Fetched the report's
  own HTML index/abstract page instead (`fhwa.dot.gov/publications/research/safety/20067/index.cfm`),
  which confirmed the publication number, date, and abstract text directly.
- **Outcome: SOURCED**, confidence **HIGH** (primary U.S. federal research agency, a report
  directly on this case's exact topic, confirmed via its own index page). Recorded as **S2**. This
  case does **not** reproduce the report's own crash-modification formula (not extractable from the
  PDF in this session, and not something this case can verify precisely) — Appendix B's
  `sin(angle)` scoring is explicitly disclosed as this case's own simplification (MA3), not a
  restatement of FHWA's formula.

## P03 — Shared base intersection reconstruction cost

**Need:** a real total-dollar cost for the base reconstruction work (signal loop, drainage,
ADA ramps, base course paving) common to both redesign options.

- Searched: `small town capital improvement plan "intersection" "safety improvement" project cost
  estimate` and `municipal capital improvement plan intersection realignment project cost budget`
  — surfaced a wide range of real project costs, none matching this exact fictional intersection
  (expected — no public record exists for a fictional site): a Waller County, TX capital-bond
  project ("curb radii improvements and lighting," signage/striping only) at **$42,000**; a Texas
  intersection realignment at **$9,374,000**; a Pennsylvania DOT skew-correction realignment
  (Route 8 / Route 77, Bloomfield Township) at **$4,000,000**.
- None of these is a clean match for a modest local two-lane/four-lane intersection's full base
  reconstruction (signal + drainage + ADA + paving, but not a state-highway-scale rebuild) — the
  found figures bracket a very wide range ($42K minor fix to multi-million state-highway projects)
  without a matching midpoint.
- **Outcome: NOT FOUND (as an exact match) → Modeling Assumption.** Exit taken: **stated Modeling
  Assumption** (exit 1 of the three allowed exits), because the case's own project scope
  (rebuilding drainage, a signal loop, and pavement at a genuinely local intersection) is real and
  necessary regardless of which option wins, and the found comparables — while not an exact match
  — establish it sits well above a minor fix and well below a state-highway project. Recorded as
  **MA1** in Appendix D: $400,000, basis stated, flagged for Tier 2 probe 5 flexing.

## P04 — Land acquisition cost, two corner-lot slivers

**Need:** a real-basis dollar figure for acquiring the two narrow corner-lot slivers Option A
requires.

- Searched: `right of way acquisition cost per square foot small residential corner lot state DOT
  2025` — surfaced VDOT's and WSDOT's own Right-of-Way manuals (methodology documents, no specific
  small-town per-square-foot figure), and an academic transportation-research paper (Kockelman et
  al., cost-of-right-of-way-acquisition literature) whose search-result summary states corner lots
  at signalized intersections carry a real, documented acquisition premium over otherwise-similar
  parcels.
- Attempted a direct fetch of the academic paper's PDF for the exact premium figure — same
  PDF-encoding failure as P01/P02. The underlying finding (corner parcels near intersections carry
  a real acquisition premium) is well-established in the transportation-economics literature
  generally, but no clean, quotable per-square-foot figure for a small residential/commercial
  corner slice was found in this session.
- **Outcome: NOT FOUND (as a hard dollar figure) → Modeling Assumption.** Exit taken: **stated
  Modeling Assumption**, built as a reasoned dollar figure for two *narrow slivers* (not full
  lots — Option A only needs enough land to widen the curb-return radius, per Appendix A's 25 ft
  radius, not the whole parcel) rather than adopting the academic paper's per-acre elasticity
  figure directly, since that figure measures a different quantity (a statistical premium, not a
  transaction price) and applying it as if it were this case's real number would be exactly the
  kind of contested-figure laundering SPEC §5 prohibits. Recorded as **MA2** in Appendix D:
  $80,000 total, basis stated, flagged for Tier 2 probe 5 flexing.
- The academic paper's specific per-acre figure was **not** reproduced anywhere in `case.md` —
  only the qualitative finding (a real acquisition premium exists) is cited as the assumption's
  basis, per SPEC §5's contested/proxy-figure rule.

## P05 — Municipal curb-and-gutter construction unit cost

**Need:** a real, dated per-linear-foot construction cost to price each option's own new
curb-and-gutter footage.

- Searched: `city public works cost per linear foot curb and gutter pavement reconstruction 2025
  2026 estimate` — returned a wide range of contractor-marketing and cost-calculator sites
  ($12-$78/linear foot, inconsistent scope definitions, no clear primary attribution for most).
  **Rejected as load-bearing** — same pattern as roofline-call's rejected P02 attempt, several
  pages are AI-generated cost-guide content with no visible sourcing.
- One result stood out: the City of Idaho Falls, Idaho, Public Works Department's own page,
  "Curbs, Gutters and Sidewalks," stating a dated **2026 reimbursement amount of $21.00 per linear
  foot for qualifying curb and gutter.** Fetched directly and confirmed the exact quote.
- **Outcome: SOURCED**, confidence **HIGH** (primary municipal government page, dated, unambiguous
  units). Recorded as **S3**, applied to both options' own curb-and-gutter footage in Appendix C.
  Disclosed in `case.json.sources[].note` as a modeling simplification: a real municipal rate
  standing in for this fictional town's own rate, the same pattern roofline-call used for its
  national composite lumber price.

## Summary

| Placeholder | Outcome | Confidence | Case location |
|---|---|---|---|
| State minimum intersection angle | SOURCED (S1) | MEDIUM | Appendix B, Appendix E |
| Intersection-angle/safety research basis | SOURCED (S2) | HIGH | Appendix B, Appendix E |
| Shared base reconstruction cost | ASSUMPTION (MA1) | — | Appendix C, Appendix D |
| Land acquisition cost | ASSUMPTION (MA2) | — | Appendix C, Appendix D |
| Curb-and-gutter unit cost | SOURCED (S3) | HIGH | Appendix C, Appendix E |

Zero placeholders remain `OPEN`. Zero figures were invented, rounded from a remembered number, or
laundered from a contested source — the one contested/proxy figure encountered (the academic ROW
premium paper's per-acre elasticity number) was deliberately **not** used as if it were this case's
own number; only its qualitative finding backs MA2's basis. All site-specific geometry in Appendix
A (the 50°/130° current skew, the 75° platted lot-line angle, the 35° ADA ramp angle, street
widths, curb-return radius) is Dana's own site design, consistent with the roofline-call precedent
for an authored, one-of-a-kind site's own stated design figures.

Next step: run `case-readiness` on `the-sightline-vote`.
