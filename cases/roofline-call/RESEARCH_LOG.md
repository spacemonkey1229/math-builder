# Research Log — Roofline Call

`case-research`, 2026-08-19. This case was authored with three real, load-bearing figures needed
and two figures identified up front as needing a stated Modeling Assumption (per the approved
concept sheet's own MEDIUM-feasibility note). All three sourceable figures were found on the first
or second search attempt; no figure returned NOT FOUND.

## P01 — 2×8 rafter maximum span, DF-Larch No. 2, 16" o.c.

**Need:** confirm the 2×8 lumber size Colton specifies for every member (rafters, hips, jacks,
ridge boards) actually clears this job's 12 ft rafter run at 16" spacing, so the lumber-size choice
isn't an unstated liberty.

- Searched: `APA span tables rafters 2x8 24 inch on center span` — surfaced the Southern Pine
  Council's own MAXIMUM SPANS PDF, a primary trade-association document. Attempted `WebFetch`
  directly on the PDF; the tool could not extract readable table text from the PDF's internal
  image/stream encoding. Recorded as **attempted, not usable** rather than silently skipped.
- Searched again: `APA span tables rafters 2x8 24 inch on center span` (general), then fetched
  mycarpentry.com's "Rafter Span Tables" page directly, which reproduces the standard IRC/AWC
  table in plain HTML. Found: 2×8, Douglas Fir #2, 16" o.c., live load 20 psf / dead load 20 psf,
  no ceiling attached to rafters → maximum span **16 ft – 0 in**.
- **Outcome: SOURCED**, confidence **MEDIUM** (a construction-education site reproducing a standard
  code table, not the primary AWC/IRC document itself, since the primary PDF did not extract
  cleanly). This job's actual 12 ft run has a 4 ft margin either way — it is a safety-margin check
  for the lumber-size choice, not a figure the dilemma turns on, so MEDIUM is an acceptable grade
  here per the case-research skill's own "not load-bearing" allowance.
- Recorded as **S1** in `case.json.sources[]`, cited in Appendix A.

## P02 — Framing lumber composite price

**Need:** a real, dated 2×8 (or general dimensional framing) lumber price to cost Appendix D's
board-foot takeoff.

- Searched: `2x8 SPF framing lumber price per board foot 2026` — returned mostly low-quality
  aggregator/calculator sites (calcsummit.com, buildestimatory.com, etc.) with inconsistent,
  undated per-board-foot ranges ($0.50–$2.50/BF). **Rejected as load-bearing** — no clear primary
  attribution, several are AI-generated cost-guide pages with no visible sourcing of their own.
- Searched again: `NAHB eye on housing framing lumber price per thousand board feet 2026 Random
  Lengths` — surfaced NAHB's own "Framing Lumber Prices" page, which republishes the named,
  industry-standard Madison's Lumber Price Index weekly. Fetched directly: **$536.15 per 1,000
  board feet, dated August 14, 2026.**
- **Outcome: SOURCED**, confidence **HIGH** (a national trade association republishing a named,
  dated index with unambiguous units — passes all four HIGH criteria).
- Recorded as **S2**, cited in Appendix C. Converts to $0.53615/board-foot, used directly in
  Appendix D's material cost line (shown in `FACILITATOR.md` and `case.json.derived`, not in
  `case.md`, per the no-answer-key-in-case.md rule).

## P03 — Carpenter labor wage (basis for Appendix E's cut-time assumptions)

**Need:** the concept sheet flagged the labor-cost differential between gable and hip framing as
"likely needing a stated Modeling Assumption rather than a hard citation." A real wage figure was
still needed as the *basis* for that assumption, so the derived per-cut dollar costs aren't
invented outright (same pattern as the Vent Cap precedent, MA1).

- Searched: `BLS occupational employment statistics carpenters median hourly wage 2024` —
  surfaced the U.S. Bureau of Labor Statistics' own Occupational Outlook Handbook page for
  Carpenters directly (a primary government source). Found: median hourly wage **$28.51/hr**, May
  2024 data.
- **Outcome: SOURCED**, confidence **HIGH** (primary U.S. government labor statistics agency,
  dated, unambiguous units).
- Recorded as **S3**, cited as the basis for both Appendix E assumptions.

## MA1 — Simple-cut time per common rafter

**Need:** minutes to mark and cut one common rafter's birdsmouth + ridge plumb cut.

- Searched for a published per-cut timing study (`carpenter rafter cut time minutes per rafter
  production framing`) and found nothing citable — no public source times this specific operation
  in a way that would transfer cleanly to this job's spacing/pitch/lumber size.
- **Outcome: NOT FOUND → Modeling Assumption.** Exit taken: **stated Modeling Assumption** (exit 1
  of the three allowed exits), not redesign or drop, because the concept sheet's own feasibility
  note anticipated exactly this and the figure is genuinely needed for the case's Twist. Recorded
  as **MA1** in Appendix E: 4 minutes/rafter, basis stated, sensitivity noted (does not touch the
  graded primary metric — see `case.json.sensitivity_note`).

## MA2 — Compound-cut time multiplier (hip/jack rafters)

**Need:** minutes to mark and cut one hip or jack rafter's compound-angle cut, relative to MA1.

- Searched: `hip roof vs gable roof framing lumber cost percentage more material` — returned a wide,
  inconsistent, low-quality range (5% to 40% "more material" or "more cost" across contractor
  marketing blogs, no primary methodology disclosed by any of them, several contradicting each
  other on the same claim). **Rejected as a citation** — this is exactly the SPEC §5 "contested,
  poorly sourced, conflates categories" case (material % vs. total cost % vs. labor % are all
  blended together across these pages with no consistent definition).
- **Outcome: NOT FOUND (as a hard percentage) → Modeling Assumption**, built as a *reasoned
  multiple* instead of adopting any of the contested percentages directly: a compound cut lays out
  two bevels instead of one, plus a test-fit, which is a real, describable difference in operation
  even without a timed study backing the exact multiple. Recorded as **MA2** in Appendix E: 3× MA1
  (12 minutes/member), basis stated, flagged for Tier 2 probe 5 flexing.
- The rejected 5–40% range was **not** reproduced anywhere in `case.md` — per SPEC §5's contested-
  figure rule, the dispute is named here in the research log, not laundered into the case as if it
  were a real citation.

## Summary

| Placeholder | Outcome | Confidence | Case location |
|---|---|---|---|
| 2×8 span, 16" o.c. | SOURCED (S1) | MEDIUM | Appendix A |
| Framing lumber price | SOURCED (S2) | HIGH | Appendix C |
| Carpenter wage | SOURCED (S3) | HIGH | Appendix E basis |
| Simple-cut time (MA1) | ASSUMPTION | — | Appendix E |
| Compound-cut multiplier (MA2) | ASSUMPTION | — | Appendix E |

Zero placeholders remain `OPEN`. Zero figures were invented, rounded from a remembered number, or
laundered from a contested source. All footprint/pitch/geometry figures in Appendix B are Colton's
own stated design (not public data), consistent with the Vent Cap precedent for an authored part
design.

Next step: run `case-readiness` on `roofline-call`.
