# RESEARCH_LOG.md — The Painted Gallon

One row per original placeholder: what was searched, what was found, what was rejected, and the
disposition. Ordered by load-bearing weight, not document order.

## The core sourcing problem, stated up front

The approved concept named Option B as a ground-standing cylindrical **standpipe**. A genuine,
multi-tier search (see below) found no publicly available, rigorously comparable cost/area dataset
pairing a spherical elevated tank against a ground standpipe specifically — real standpipe cost
data exists (see the rejected searches below) but nowhere alongside a matched, same-methodology
spheroid comparison. The search DID surface something better: a real, professional-engineer-sealed
2019 Black & Veatch memorandum for the City of Lawrence, Kansas, directly comparing a spheroid
elevated tank against a **multi-column** elevated tank (a cylindrical reservoir on multiple support
legs) — same site, same required capacity, same overflow height, real fabricator budgetary quotes
for both. This is the REDESIGN exit under `skills/case-research/SKILL.md` Section 5's NOT-FOUND
procedure, applied at the pairing level rather than to a single figure: swap the unsourceable
standpipe pairing for a real, comparably rigorous one that preserves the same pedagogical target
(sphere vs. cylinder at fixed volume; less-area-but-costlier-to-build vs. more-area-but-cheaper).
Recorded prominently in `case.json.concept_redesign_note` for the project owner.

## P01/MA2 — Required elevated storage capacity

- Searched: "AWWA M42 elevated steel water tank sizing rule of thumb gallons per capita small
  town" — AWWA's M42 manual exists but its full sizing tables are paywalled; public previews did
  not surface a specific gpcd-based sizing worksheet.
- Searched: "recommended standards for water works Ten States Standards minimum elevated storage
  volume average daily demand" — found a real, dated secondary source (One Source Plastics blog,
  2026) stating the Ten States Standards / AWWA D100 convention that elevated storage should equal
  average daily demand for systems under 3,300 connections [S2].
- Searched: "AWWA average per capita water demand gallons per day residential design standard" —
  found a real 2011 municipal design-criteria document citing a 200 gpcd average-day design
  standard [S1].
- Disposition: no source publishes a required capacity for this fictional town specifically —
  combining a per-capita rate with an assumed town population is itself an authored scenario
  choice. **ASSUMPTION (MA2)**: fixed at 750,000 gallons, chosen to match the exact capacity (0.75
  MG) evaluated in the real Lawrence, Kansas study used for every other figure in this case, so
  every subsequent number could be real rather than invented.

## P03 — Ballot must state one dollar figure, not a range

- Searched: "state law municipal bond ballot measure must state specific dollar amount not a range
  election code" — found the general real convention (bond resolutions state a "maximum principal
  amount") via Ballotpedia and a real 2026 district bond example quoting "$300,000,000" as a
  specific stated amount, and located California Elections Code Division 9, Chapter 5 ("Bond
  Issues") as the relevant statutory chapter.
- Attempted to fetch the full statute text (Justia, Section 9401) directly for a precise quote —
  the fetch returned HTTP 403 (blocked), so only the search-snippet evidence could be used.
- Disposition: **SOURCED at MEDIUM confidence (S3)** — the underlying convention is real and
  well-evidenced (a real ballot example quoting a specific principal amount, a real statutory
  chapter title), but the precise statute text could not be directly verified, so this is graded
  MEDIUM rather than HIGH. This claim is scenario/background support, not a number entering any
  calculation.

## P04 — Gallons-to-cubic-feet conversion

- Standard US customary unit definition (1 US gallon = 231 in³; 1 ft³ = 1728 in³), not a
  measured or contested quantity. **SOURCED (S4)**, HIGH confidence, cited to USGS's water-units
  reference page.

## P05/P06/P07/P08/P09/P10 — Spheroid design: real area, dimensions, and cost

- Searched: "steel standpipe water tank typical height diameter feet design range" and
  "spheroid elevated water tank support tower cost more than standpipe foundation" while still
  pursuing the original standpipe framing — found real qualitative evidence (a 2022 Tuscaloosa, AL
  bid where a spheroid tank was selected at a stated 25% premium over other elevated styles;
  general trade commentary that "a tall elevated tank ... will push costs higher than a compact
  standpipe with basic controls") but no rigorously matched, same-methodology cost comparison
  against a ground standpipe specifically.
- Fetched: `lawrenceks.gov/wp-content/uploads/2020/07/Tank-Alternatives-Memorandum.pdf` — a real,
  professional-engineer-sealed 2019 Black & Veatch memorandum for the City of Lawrence, Kansas,
  evaluating four real elevated-tank alternatives (composite, spheroid, hydropillar, multi-column)
  at two capacities (0.5 MG and 0.75 MG), with real fabricator budgetary quotes (McDermott,
  Caldwell Tanks, Landmark Structures) and a life-cycle cost analysis (LCCA) using a 1.5% discount
  rate over a 60-year horizon with recoats at years 20 and 40.
- This memo's own Appendix B reproduces Tnemec Company, Inc.'s published "Estimating Guide for
  Surface Areas of Water Tanks" (real, industry-standard, dated 2009) — the real source of the
  outside-area figures used throughout this case.
- Disposition: all six figures **SOURCED (S5-S10)** directly from Table 2-1 (dimensions), Table
  2-4 (capital/maintenance/total cost), Table 2-5 (cost per gallon), and the Tnemec guide, all at
  the 0.75 MG row. HIGH confidence — real, dated, professional-engineering-firm-produced figures
  from an actual named municipal project.
- Caveat recorded: the Tnemec guide's areas are stated as approximations for a 100 ft head-to-base
  tank height; the real Lawrence project used a 132 ft overflow height, so the true area at that
  exact height could differ slightly from the generic guide figure. Not treated as disqualifying —
  the same guide, and the same caveat, applies equally to both options being compared, and it is
  the exact table the real engineering firm itself used for this exact project (memo Section
  2.1.2.3: "Tank surface area estimations can be found in Appendix B").

## P11/P12/P13/P14/P15/P16 — Multi-Column design: real area, dimensions, and cost

- Same source as above (Black & Veatch memorandum + Tnemec guide), 0.75 MG row, Multi-Column
  column. All six figures **SOURCED (S11-S16)**, HIGH confidence.
- Caveat recorded: the memo notes that only Caldwell Tanks is a qualified multi-column fabricator
  at this capacity, so the $1,595,000 capital-cost figure [S13] lacks the multi-quote averaging
  the memo applied to the other three (multi-fabricator) designs. This is a real, disclosed
  single-source-bid limitation in the underlying real study, not a defect introduced by this case
  — noted in `case.json.sources[S13].note` rather than smoothed over.

## 2026-09-06 — Case-readiness QA revision: balance fix + three citation corrections

A Tier 2 QA pass (cold-solve, both-sides, and twist probes, run independently) found the case's
original balance defective and three citation defects. This section documents the fix trail.

### Balance defect and fix (S17 / Appendix G)

The probes found the Multi-Column wins every dollar metric (capital cost, 60-year lifecycle cost,
cost/gallon) at every capacity, and that this win is mathematically invariant across a ±50%
capacity flex (both designs scale by the same capacity^(2/3) law — confirmed independently by
`sensitivity_model.py`). The original Argument A (future, stricter environmental regulation raising
recoating costs in proportion to coated area) was real but speculative, not a present-day dilemma —
insufficient to make the case a genuine two-sided balance test per SPEC §2.

Per PIPELINE.md's "QA BLOCKER on structure/balance → re-enter at case-write" and "retune a
constraint, never fix a margin by hiding data" — the fix was not to alter any sourced dollar figure.
Instead, the same real Black & Veatch memorandum already cited for S5-S16 was re-read in full
(pages 4, 6, 9 of the PDF) for any other real, present-day, quantifiable factor. It contained one
already, unused: Section 2.1.2.4 ("Bidding Competitiveness of Alternatives") states "Because the
multi-column tank is only fabricated by one company, selecting this alternative would effectively
sole source the tank with no opportunity for competitive bidding. Selecting the spheroid,
hydropillar, or composite alternative includes multiple manufacturers, which should result in a
competitive bidding environment for the City." Table 2-1 confirms three qualified spheroid
fabricators (McDermott, Caldwell Tanks, Landmark Structures) versus one qualified multi-column
fabricator (Caldwell Tanks only). The memo's own Section 3.1 Recommendations repeats this as a
reason for caution: "Because Caldwell is the only manufacturer that is qualified to manufacture
this style of tank, there is added risk in choosing this tank alternative due to lack of
competition." Table 2-6/2-7's own Tank Alternative Selection Matrix independently scores "Bidding
Competition" as 1 (most desirable) for the Spheroid and 4 (least desirable) for the Multi-Column.

Disposition: **SOURCED (S17)**, HIGH confidence, same memo as S5-S16. Added to case.md as new
Appendix G and Challenge 2c; added to case.json as `balance.argument_a`'s primary basis, replacing
the weaker future-regulation framing. This is a real, present-day, structural procurement-risk fact
documented by the same engineering firm whose cost numbers make B look cheaper — not a fabricated
balancing factor, and not dependent on the case's capacity choice (fabricator qualification at this
capacity range is a manufacturing-capability fact, not a cost-scaling one, so it survives the same
±50% capacity flex that the dollar metric was twist-tested against).

### Citation fix: S2 (dropped an unsupported "3,300 connections" claim)

A Tier 2 data-decay probe live-refetched the original S2 source (onesourceplastics.com) and found
it does NOT contain "3,300 connections," or any connection-count threshold, anywhere on the page —
the claim was overstated relative to that source. The page in fact argues AGAINST sizing storage to
average daily demand alone (it argues for adding fire-flow and emergency-reserve components on top).
Re-searched and found a real, HIGH-confidence replacement that supports exactly the narrower claim
this case needs: PDH Academy's "Water Storage Tanks" continuing-education course (Mark Ludwigson,
P.E., Course 378, 2022), page 15: "The Ten States Standards specifies that the required storage
capacity (volume) to be equal or greater than the average daily consumption (demand)." The
"3,300 connections" qualifier has been dropped entirely rather than re-sourced, since no source in
this case's trail supports that specific number. **Fixed: S2 replaced, claim narrowed to what is
actually supportable.**

### Citation fix: S3 (mis-cited California Elections Code §9401)

A Tier 2 probe fetched the actual text of California Elections Code §9401 (via search-engine
summary and cross-check against Ballotpedia's own summary of §§9400-9405) and confirmed it governs
the tax-rate DISCLOSURE STATEMENT mailed with the sample ballot (average and highest annual tax
rate, filed 88 days before the election) — not the format (single figure vs. range) of the bond
amount itself. This was a real mis-citation. Re-searched for the actual California statute
governing bond-ordinance content and found California Government Code §43610 (General Bond Law for
cities, Title 4, Division 4, Chapter 4, Article 1), confirmed via FindLaw's full text: "The
ordinance shall recite: (a) The object and purpose... (b) The estimated cost... (c) The amount of
the principal of the indebtedness. (d) The rate or maximum rate of interest... (e) The date of the
election. (f) The manner of holding the election..." — this is the correct, real, verified statute:
it requires a single stated principal amount, not a range, as one of six required recitals.
**Fixed: S3 replaced with Cal. Gov. Code §43610, HIGH confidence (up from MEDIUM).**

### Citation fix: S4 (dead USGS link)

A Tier 2 probe live-fetched the original S4 URL (usgs.gov water-units-and-conversions page) and
confirmed a genuine HTTP 404 (not a bot-block — checked via `curl -I`). Re-searched for a live,
authoritative replacement and found NIST Handbook 133 (2026 edition), Appendix E — "General Tables
of Units of Measurement" — confirmed live via `curl -I` (HTTP 200) at
`https://www.nist.gov/system/files/documents/2025/12/23/2026_NIST_HB133_AppendixE-20251222.pdf` on
2026-09-06, and confirmed via `pdftotext` extraction to state "1 gallon (gal) = 231 cubic inches"
and "1 cubic foot (ft3) = 7.481 gallons" (1/7.481 = 0.133679..., consistent with the case's stated
0.133681 = 231/1728 exactly). **Fixed: S4 replaced with a live NIST citation.**

## 2026-09-06 — Tier 2 probe findings on the new balance axis, and their fixes

Two independent, fresh-subagent Tier 2 probes (trap-check and twist-integrity), run against the
revised case, surfaced two real, non-trivial findings on top of the balance fix above. Both were
fixed in the same pass rather than deferred, since both are genuine defects the probes are designed
to catch, not stylistic nits.

- **Trap-check (P3) finding:** the case's scaffolded D1-D5 steps largely inoculate a Hero against
  the "less area = cheaper" intuition trap by the time they write a recommendation, but the new D6
  (fabricator-competition response) has no comparable scaffolding and can be answered with a token,
  unengaged sentence. **Fix:** added a second, explicit trap to `FACILITATOR.md`'s "The trap"
  section describing this exact failure mode, plus a named facilitator follow-up question to press
  on a superficial D6 answer.
- **Twist-integrity (P4) finding:** `sensitivity_model.py`'s capacity sweep (+/-50%) validates only
  the dollar cost-per-gallon metric's invariance; the new S17 fabricator-count claim is sourced by
  the real memo specifically "at 0.5-0.75 MG capacity" and was never claimed, by this case or the
  source memo, to hold at capacities materially outside that band (e.g. the sweep's +50% case,
  1.125 MG). Nothing in the case previously disclosed this scope mismatch. **Fix:** added an
  explicit "Scope note" to `case.md` Appendix G, a matching caveat to `case.json.balance.margin_basis`
  and `sources[S17].note`, a scope-note paragraph to `sensitivity_model.py`'s docstring, and a new
  Socratic Question 7 in `FACILITATOR.md` that puts this exact scope distinction in front of
  students rather than leaving it implicit.

## Rejected sources (for the record, so nobody re-runs the same dead search)

- Generic water-tank retail cost pages (Angi, Tank Depot, LatestCost, Design Transition Studio,
  etc.) — undated or vaguely dated consumer-facing "2026 pricing guide" content with no named
  primary source; rejected as LOW confidence, never used for a load-bearing figure.
- A 1.5-million-gallon elevated tank budget for Abilene, TX ($4,430,000, ≈$2.95/gallon, a real
  2025 municipal budget line) — real and HIGH-confidence on its own terms, but a single aggregate
  figure with no shape-vs-shape comparison and no area breakdown, so it could not support the
  case's actual required comparison and was not used.
- A generic AWWA/steel-tank cost range ("$1.00-$4.50 per gallon for steel tanks") — too broad to
  distinguish the two designs from each other; rejected in favor of the Lawrence, KS memo's real,
  apples-to-apples, same-project comparison.
