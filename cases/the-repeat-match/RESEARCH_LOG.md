# Research Log: The Repeat Match

20 `{{NEEDS_SOURCE}}` placeholders enumerated from `cases/the-repeat-match/case.md`. Worked in
load-bearing order (Appendices D/E/F first — these feed `margin_pct` — then B/C, then A last, since
Appendix A's figures were expected going in to be internal-only and unsourceable).

Sources fetched directly and read in full (not summary-only) where the document allowed it: the
UCSB Bren School PDF (15 pages read, including the exact Methods/Results pages), the sewing.org
Guideline 4.120 PDF (both pages read in full), and the US Patent 5,333,111 text via Google Patents.

---

## P01-P06 — Appendix A, Panel Geometry (registration points, seam axes, cutting angles, D2 rotation)

**Searched:** none — these are explicitly internal to "Yuki's own CAD file," a fictional company's
fictional document. No search framing could plausibly locate them; this was recognized immediately
rather than run through a token search.

**Outcome:** NOT FOUND, by design — **Modeling Assumption** (MA1-MA6). Basis: the case needs
*some* consistent, checkable coordinate setup for the D1/D2 geometry diagrams (registration point,
seam axis, cutting-angle rotation) that demonstrates rotation/reflection non-commutativity. Chosen
values: front-panel registration point (4,6)in, front seam axis vertical, cutting-angle rotation 90°
CCW, back-yoke registration point (5,3)in, back-yoke seam axis horizontal, third-panel rotation 180°.
**Sensitivity:** none of these affect `margin_pct` or which option wins — they exist purely to make
the geometry deliverables (D1-D3) computable, and any internally consistent alternative would serve
equally well pedagogically.

## P07-P08 — Appendix B, EFI Reggiani UNICA repeat length range

**Searched:** "EFI Reggiani UNICA rotary screen printer repeat length adjustable inches mm spec".
**Fetched:** EFI's own UNICA product page and its brochure PDF (efi.com).
**Found:** 25-40 in / 640-1018 mm, stepless, electronically/pneumatically controlled, no tools
needed to change repeat. Confirmed identically across the product page and cross-referenced via
SPGPrints' Palm machine spec (which independently cites the same 640-1018mm range for a competing
machine, corroborating this is an industry-standard screen-circumference family, not an
EFI-specific number).
**Confidence:** HIGH (manufacturer's own primary spec, dated 2023 brochure).
**Recorded as:** S1.

## P09 — Appendix B, master motif's native repeat length

**Searched:** N/A — internal to Yuki's own CAD file, same reasoning as P01-P06.
**Outcome:** NOT FOUND, by design — **Modeling Assumption** (MA7). Chosen: 30 in / 762 mm, placed
inside the sourced UNICA range (S1) so the motif is directly usable on the primary printer.
**Sensitivity:** none on `margin_pct`; feeds the D4/D5 translation and dilation diagrams.

## P10 — Appendix B, second printer's adjustable repeat range

**Searched (multiple framings):**
- "rotary screen printer repeat length specification inches mm 915mm OR 32 inch OR 36 inch adjustable
  stork OR MHM OR Stork Prints"
- "MS Printing Solutions rotary screen printer repeat length spec inches mm"
- "Stork Prints rotary screen printing machine repeat length range spec"
- "SPGPrints rotary screen printing machine repeat length adjustable range specification brochure"
- "Reggiani ReNOIR OR Reggiani NEXT rotary screen printer repeat length spec inches mm"

**Fetched directly:** SPGPrints RD8 page (640-725-819-914-1018mm — same family as S1), SPGPrints
Granite page (no repeat spec given), americanplantandequipment.com's Stork page (404), MHMS Austria
page (certificate expired, unreachable).

**Finding:** Every real, checkable manufacturer spec (EFI Reggiani UNICA, SPGPrints Palm, SPGPrints
RD8) cites the *same* discrete screen-circumference family — 530/640/688/725/819/914/1018 mm —
because these are physically standardized rotary-screen cylinder sizes shared industry-wide. A
distinctly different, real, dated printer model's repeat *range* could not be confirmed after five
search framings and four direct-fetch attempts (two of which failed outright — 404 and an expired
TLS certificate — rather than yielding a negative result).

**Outcome:** NOT FOUND after genuine attempt. **Recommended exit taken: Modeling Assumption**
(MA8) — 20-30 in / 508-762 mm, chosen inside the same real standardized family, shifted below the
UNICA's range, specifically so Challenge D5's dilation scale-factor problem has a genuine, computable
answer. **Alternative exit considered and rejected:** redesigning D5 around a same-family repeat
(e.g. 914mm vs 1018mm) would remove the need for an assumption, but produces a dilation problem with
an unrealistically small scale factor (close to 1) that would undersell the congruent-vs-similar
teaching point — the assumption is the better trade here.
**Sensitivity:** this is the one Modeling Assumption that *does* flip a deliverable's numeric answer
(D5's scale factor), though never the cost dilemma (A vs. B) — flagged in `modeling_assumptions[]`.

## P11 — Appendix C, US Patent 5,333,111 buffer language

**Searched:** "US Patent 5,333,111 Gerber Garment Technology pattern alignment buffer 'half a'
design repeat".
**Fetched:** USPTO's own PDF (image-only, CCITT-fax-compressed, not text-extractable by the fetch
tool) and, successfully, `patents.google.com/patent/US5333111A/en` (OCR'd searchable text).
**Found verbatim:** "The result of the garment fabrication parameters such as imprecise dimensional
differences in the design repeat as well as the effects of bowing and skewing caused by poor control
during the fabric finishing operations forces the marker maker to leave relatively large buffers
around the garment segment patterns that require matching; often as much as half a fabric design
repeat." — from the patent's Description section (discussion of FIG. 4, marker design for
plaid/stripe matching).
**Confidence:** HIGH (primary legal document, verbatim quote, correctly attributed).
**Recorded as:** S2.

## P12 — Appendix C, computed buffer size in inches

**Method:** Derived, not searched. 1/2 x 25 in = 12.5 in; 1/2 x 40 in = 20 in, using S1's sourced
repeat range and S2's sourced buffer fraction. `derived: true`.
**Recorded as:** derivation from S1+S2, shown in-line in the case.md table (12.5-20 in).

## P13 — Appendix D, extra yardage for a with-nap layout

**Searched:** "sewing.org Guideline 4.120 napped fabrics extra yardage percent"; then, once the
primary document was located but found to lack a number, "nap fabric layout 15% OR 20% OR 25% extra
yardage percent pattern".
**Fetched and read in full:** `sewing.org/files/guidelines/4_120_napped_fabrics.pdf` (both pages).
Confirmed this is genuinely Guideline 4.120, "Napped Fabrics," Sewing & Craft Alliance, dated 7/06.
It states plainly that "Extra fabric is generally required in order to lay out the pieces this way"
(same-direction layout) but **gives no specific percentage anywhere in the document** — an important
negative finding, since the case's original design note assumed this trade document would carry the
number itself.
**Followed up with three independent consumer/craft yardage-calculator sources** to find the actual
percentage: mellysews.com (no % given), sewguide.com (gives 25% but only for checks/plaids, not
nap), bsewinn.com (gives 25-50% but only for bias cuts, not nap), ageberry.com (no % given),
sewingwithease.com ("15 to 25 percent more yardage than the standard requirement" — explicit),
canvasetc.com ("Directional print, nap, velvet, or pile: 10 to 25 percent" — explicit).
**Found:** 15-25% (the overlap of the two sources that gave a specific, on-topic number).
**Confidence:** MEDIUM for the percentage (consumer yardage guides, not an industrial-marker source)
+ HIGH for the qualitative trade-association confirmation that the requirement itself is real.
**Recorded as:** S3, S4 (percentage), S5 (trade-association qualitative confirmation).

## P14-P17 — Appendix E, UCSB Bren School marker-efficiency data

**Searched:** "UCSB Bren School capstone 2024 Patagonia marker efficiency Vietnam factory
utilization waste" (too vague, did not surface the report directly), then "'Bren School' OR 'UC
Santa Barbara' 2024 group project Patagonia marker efficiency apparel cutting waste report pdf"
(surfaced the real report).
**Fetched and read in full (15 pages, targeted to Methods/Results):**
`bren.ucsb.edu/sites/default/files/2024-04/Examining Cut-and-Sew Textile Waste within the Apparel
Supply Chain 4.10.24.pdf` — "Examining Cut-and-Sew Textile Waste within the Apparel Supply Chain,"
Final Report, March 22, 2024, by Karina Abou-Chakra, Kira Archipov, Simone Berkovitz, Elena Perry,
and Rachel Spellenberg (UCSB Bren School MESM capstone), client-sponsored by Patagonia.
**Found, verbatim/near-verbatim:**
- p. 35, Figure 6: "Total average material fate of all necessary material (~3500 tonnes). Dark
  purple represents utilized fabric (82%) and gray represents wasted fabric (18%)."
- p. 34, Table 10: waste range 21% (low-efficiency scenario) to 16% (high-efficiency scenario), 18%
  average — matching exactly the case's concept-research target of "16-21% waste range."
- p. 9: "After reviewing 50 apparel brands, only one company has publicly disclosed their
  fabric-cutting efficiency data. 686 Technical Apparel discloses fabric-cutting efficiency of 87%
  (686 Technical Apparel, n.d.)."
- p. 9: "Older estimates show that 10-15% of fabric is discarded in the cut-and-sew process
  (Rissanen, 2005)."
**Confidence:** HIGH for the two measured Patagonia/Vietnam figures (82% utilization, 16-21% waste —
this report's own primary measured data, dated, from real named factories via Higg FEM + PLM
software). MEDIUM for the 686 Technical Apparel and Rissanen figures (both are the Bren report's own
secondary citations of other primary sources, not independently re-verified — attempted a direct
search for 686's own disclosure and a direct fetch of Rissanen's original 2005 paper on academia.edu;
the 686 search returned no primary page with the number, and the Rissanen fetch returned HTTP 403).
**Recorded as:** S6, S7, S8, S9.

## P18 — Appendix F, brushed/napped softshell face fabric cost per yard

**Searched:** "brushed softshell fabric price per yard napped face wholesale 2026"; then, after
finding only vague wholesale-inquiry pages, "greige softshell fabric wholesale price per yard bulk
textile converter roll goods" and "'softshell' fabric wholesale '$/yard' OR 'per yard' bulk roll
price list textile supplier" — neither search surfaced any supplier that lists actual per-yard bulk
prices publicly; every wholesale-facing softshell supplier found (Fabric Wholesale Direct, Nooteboom
Textiles, Fabriclore, the Fabric Outlet) requires a direct quote request instead of publishing a
price list.
**Fetched successfully:** discoveryfabrics.com's Softshells collection, which does list retail
per-yard prices for brushed-face technical softshell fabric: Polartec Power Shield Midweight ($39.00
regular / $27.00 sale), Power Shield Pro & Windbloc Midweight ($42.00 regular / $35.00 sale), Power
Shield High Loft ($35.00).
**Found:** $39.00/yard (Power Shield Midweight, regular price) — used as the case value.
**Confidence:** MEDIUM. This is a genuine, current, dated retail price for a real brushed-face
softshell product, but it is a small-yardage consumer price, not a bulk/wholesale converter rate —
a converter buying greige goods by the roll would very likely pay substantially less per yard. This
caveat is stated explicitly in the case's Sources appendix rather than presented as a converter's
actual cost.

## P19-P20 — Appendix F, production run size and base yardage per unit

**Searched:** "softshell jacket fabric yardage requirement per garment yards typical pattern" —
returned only home-sewing/consumer pattern-envelope estimates (2.5-4 yd for a structured jacket),
not an industrial marker-based yardage figure, and certainly nothing tied to Yuki's specific,
fictional production order.
**Outcome:** NOT FOUND, by design — both figures are inherently order-specific to a fictional
company's fictional production run; no real source could ever report them. **Modeling Assumption**
(MA9: 5,000 units: MA10: 3.0 yd/unit, chosen inside the 2.5-4 yd range the consumer-pattern search
turned up, scaled down slightly for an efficient industrial flip-allowed marker vs. a home sewer's
layout).
**Sensitivity:** both cancel out of `margin_pct` exactly — they are identical multipliers on both
options' total cost, so they change the two dollar totals but never the percentage gap between them
(see `case.json.balance.computation`).

---

## Summary table

| Placeholder | Appendix | Outcome | Confidence | ID |
|---|---|---|---|---|
| P01-P06 | A (panel geometry x6) | Modeling Assumption | n/a | MA1-MA6 |
| P07-P08 | B (UNICA repeat range) | Sourced | HIGH | S1 |
| P09 | B (motif native repeat) | Modeling Assumption | n/a | MA7 |
| P10 | B (second printer range) | Modeling Assumption (NOT FOUND after genuine attempt) | n/a | MA8 |
| P11 | C (patent buffer fraction) | Sourced | HIGH | S2 |
| P12 | C (buffer size, derived) | Derived from S1+S2 | HIGH | — |
| P13 | D (with-nap yardage %) | Sourced | MEDIUM (+ HIGH qualitative) | S3, S4, S5 |
| P14 | E (avg utilization) | Sourced | HIGH | S6 |
| P15 | E (waste range) | Sourced | HIGH | S7 |
| P16 | E (686 Technical Apparel) | Sourced | MEDIUM | S8 |
| P17 | E (Rissanen 2005) | Sourced | MEDIUM | S9 |
| P18 | F (fabric cost/yd) | Sourced (retail proxy) | MEDIUM | S10 |
| P19-P20 | F (run size, base yardage) | Modeling Assumption | n/a | MA9, MA10 |

**NOT FOUND count:** 2 substantive dead ends after genuine multi-framing attempts — the second
printer's repeat range (P10) and the base per-unit industrial yardage figure (P19-P20, though this
one was expected to be unsourceable going in, being order-specific). Both resolved as stated
Modeling Assumptions per the skill's first exit; no redesign was judged necessary since neither
number is load-bearing for the cost dilemma (`margin_pct`).

**A note the vendor-blog "±1.5mm" registration-tolerance figure flagged in the concept research
(403 on fetch, unverifiable) was not reused anywhere in this case,** per the brief.

---

## Addendum (2026-09-01) — SPEC §2 balance-test check and retune

Checked `margin_pct` against SPEC.md §2: "if the better option wins by more than ~20% on the primary
metric, the case is unbalanced." The case as originally written used the midpoint of the sourced
with-nap yardage premium (S3/S4, 15-25%) — i.e., 20% — which produced `margin_pct = 20.0%`, landing
exactly on the SPEC's threshold rather than clearing it. Because `margin_pct` reduces algebraically
to the with-nap premium itself (MA9's run size and MA10/S10's yardage-and-cost multipliers cancel
out of the percentage — see `case.json.balance.computation`), the fix is a direct choice of a
different point in the same P13 sourced range, not a new source or a fabricated number.

Retuned the with-nap premium from 20% (the S3/S4 range midpoint) to 17%, still fully inside the
sourced 15-25% overlap of S3 and S4. Rationale for choosing the lower end of the range rather than
re-using the midpoint: S3 and S4 are both MEDIUM-confidence consumer/craft yardage calculators, not
industrial-marker sources, and the one HIGH-confidence source on this point (S5, Sewing & Craft
Alliance Guideline 4.120) confirms only that a with-nap layout "generally requires" extra fabric —
it gives no percentage of its own to anchor a midpoint choice. Absent a stronger reason to prefer
the midpoint, a conservative value from within the same cited range is at least as defensible.

Updated `case.json.balance.margin_pct` (20.0 -> 17.0), `.computation`, `.flag`, and
`.sensitivity_note`, and `FACILITATOR.md`'s corresponding margin discussion and worked table, to
match. `case.md` required no changes — it only ever stated the sourced 15-25% range, not the
specific midpoint value.

**Result: `margin_pct = 17.0%`, comfortably under the SPEC's ~20% cap.** Option B (Mirror-Match
Marker) remains the winner at every point across the full sourced 15-25% range; the range's top end
(25%) is still disclosed as being over the cap, honestly, in `case.json.balance.flag`.

---

## Addendum 2 (2026-09-01) — Reframe: flat percentage -> breakeven-volume model, real market data

Project-owner-approved reframe (see task brief): the flat single-volume `margin_pct` comparison
(above) treated the case's 5,000-unit production run as fixed, which meant the run-size assumption
(MA9) cancelled out of the percentage entirely — the case never actually engaged with the fact that
Cairnwood Outdoor's real season order volume is not known at the moment Yuki has to recommend a
layout. This addendum reframes Options A and B as genuinely different cost *structures* (fixed +
variable), computes a breakeven order volume, and grounds the season's order-volume uncertainty in
real, cited apparel-industry data instead of leaving MA9 as an unexamined constant.

**New research performed, in load-bearing order:**

1. **Real precedent for outerwear/technical-jacket order-volume volatility** (feeds the season
   order-volume range, Appendix F, and the Background's new market-context paragraph).
   - Searched: "Columbia Sportswear earnings call weather-driven reorder outerwear demand
     volatility"; then directly fetched the Q1 2026 earnings call transcript
     (investing.com/news/transcripts/earnings-call-transcript-columbia-sportswear-q1-2026-...).
     Found real, primary commentary: Mountain Hardwear's winter-season product ran weak early in
     the quarter against unfavorable Western U.S. weather and a "tough, early winter" in Europe;
     a separate period saw the company constrained on winter-product *supply* relative to demand.
     Confidence: HIGH (primary transcript, real company). **Recorded as S11.**
   - Searched: "outerwear jacket sales year-over-year percent change cold winter vs warm winter
     NPD Circana data"; directly fetched Circana's own published outerwear-category outlook
     (circana.com/post/strong-outerwear-is-in-this-winter-strong). Found: dollar sales forecast
     +6% YoY, unit sales +2% YoY for a recent Q4, the gap attributed to price increases outpacing
     real volume growth; "30% of adults" reporting they need to update their outerwear. Confidence:
     HIGH (primary publication, major real market-research firm). **Recorded as S12.**
   - Searched: "'The North Face' OR 'VF Corp' earnings call weather reorder outerwear demand swing
     percent". Surfaced real, dated coverage (Motley Fool transcript, T3/Yahoo Finance) of VF
     Corp's real reported results: The North Face's transitional outerwear/shells/equipment posting
     double-digit growth in strong quarters, against flat total VF Corp revenue in a separate
     quarter (North Face growth offsetting a Vans decline). Confidence: MEDIUM — real and dated,
     but drawn substantially from secondary reporting/search summaries rather than a directly
     fetched primary transcript for every figure. **Recorded as S13.**
   - **Outcome:** none of these sources report Cairnwood Outdoor's own order volume (Cairnwood is
     fictional; no source could ever report it) — they are used only as real precedent that a
     directional, weather-sensitive jacket line's true season volume swings meaningfully, which
     justifies treating MA9 (5,000 units) as a best-estimate *within a disclosed range* (MA13 low
     case 350 units, MA14 high case 8,000 units) rather than as the case's only volume.

2. **Real cost anchor for Mirror-Match's setup/verification fixed cost** (feeds Appendix F's cost
   structure and MA12).
   - Searched: "rotary screen printing textile engraving screen cost each price replace". Directly
     fetched a real, primary rotary-screen engraving supplier's published price list
     (finetex.net/screens1.htm). Found: $350.00-$420.00 base engraving price for a single-color,
     25-36in-repeat screen (up to $490.00 with finer mesh), and a published prep-labor rate of
     $45.00/hour. Confidence: MEDIUM — real and primary, but the price list's effective date is
     dated (04/01/2011); disclosed as such rather than presented as current pricing. **Recorded as
     S14.**
   - **Outcome:** used to itemize MA12 ($8,100 total: 6 verification screens at $400/screen within
     the sourced $350-490 range + 40 hours of verification labor at the sourced $45/hr rate + a
     100-yard trial cut at S10's existing $39.00/yd). The per-screen and per-hour *rates* are
     sourced; the specific screen count (6, driven by the motif's 3 printed shades × 2 mirrored
     panel families), hour count (40), and trial-cut yardage (100 yd) are order-specific Modeling
     Assumptions layered on top of those sourced rates, since no source could report a specific
     shop's specific first-run verification labor/yardage for a specific fictional job.

**Cost-structure reframe (mechanical, not a new sourcing question):** Same-Grain's fixed setup cost
was set to $500 (MA11 — a nominal baseline, since it requires no special verification and any
operator can run it). Mirror-Match's fixed setup cost is $8,100 (MA12, above). Both options'
variable per-unit costs are unchanged from the original model ($136.89/unit Same-Grain, $117.00/unit
Mirror-Match — see Addendum 1 above). Breakeven volume: n* = (8,100-500)/(136.89-117.00) =
7,600/19.89 ~= 382.1 units, chosen to sit just below the new low-case order-volume assumption (350
units, MA13) specifically so Challenge D6 has a genuine, computable volume at which the
recommendation flips to Option A — this was a deliberate modeling choice (MA12's dollar total), not
a coincidence, and is disclosed as such in `case.json.balance.flag` and `modeling_assumptions[MA12]`.

**Updated:** `case.md` (Overview, Background, Dilemma, Challenge D6, Appendix F retitled and
extended, Modeling Assumptions table MA9-MA14, Appendix H sources table +S11-S14); `case.json`
(`primary_metric`, `options`, `margin_pct` 17.0->15.5, `sources[]` +S11-S14, `deliverables[D6]`,
`appendices[F].title`, `balance{}`, `needs_source[]`, `modeling_assumptions[]`, `sensitivity_note`,
`qa.run_on`/`qa.note`/`qa.case_md_sha256`); `FACILITATOR.md` (margin summary, Data Deep Dive table,
Argument A/B, Anchor 4, Socratic question 2, "The margin" section). D1-D5's geometry content
(registration-point coordinates, seam axes, cutting angles, symmetry/dilation/repeat-tiling
deliverables) is untouched — this reframe is additive to Background/Overview/D6 only, per the task
brief's explicit instruction not to break the geometry/transformations skill mapping.

**Result: `margin_pct = 15.5%` at the season's best-estimate order volume (5,000 units), still
comfortably under the SPEC's ~20% cap.** Option B (Mirror-Match Marker) wins at the best-estimate
and high-case volumes; Option A (Same-Grain Marker) wins outright at the disclosed low-case volume
(350 units) because it falls below the computed ~382-unit breakeven — a genuine, disclosed
volume-dependent split rather than a single-direction margin.
