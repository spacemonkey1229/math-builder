Case Study: The Repeat Match
MS | Math | Case Study | 2026 | Adventure

## Overview

Yuki Alvarez has the CAD file open on two monitors, and neither version agrees with the other. On
the left screen sits the master chevron motif — the client calls it "the arrow," and it does point
one way, printed in three shades of blue across a brushed softshell that has real nap, the raised
fiber running downhill toward the hem. On the right screen sits the same motif, twice: once rotated
ninety degrees and then mirrored, once mirrored and then rotated the same ninety degrees. Same
starting shape. Same two moves. Two different files.

She drags the little green crosshair — the registration point, the exact pixel the rotary screen
locks the print to the cut line by — and watches it land in two different places depending on which
order she built the transformation in. One version puts that crosshair exactly where the
center-front zipper seam's chevron-match line actually sits. The other puts it somewhere the seam
will never touch.

Down the hall, the engraving room is waiting on her final file before they cut screens that can't
be uncut. Two doors past that, the cutting-room foreman has a marker layout pulled up on his own
screen — one version lets pieces flip freely across the fabric to save yardage, the other locks
every piece facing the same way so the nap never runs backward on a finished sleeve. He's asked her
twice already this morning which layout to load.

Yuki minimizes the CAD window, opens the layout-comparison spreadsheet her ops lead sent over, and
lines both decisions up side by side on her screen.

## Background

Yuki Alvarez is the print-repeat engineer at a mid-size garment-print converter — a company that
prints and finishes greige (undyed) fabric to order for apparel brands — and she owns the CAD file
that a rotary-screen print run and the downstream cutting marker both depend on. Once the engraving
room cuts screens from her file, the motif's position on the fabric is fixed for the entire yardage
run; once the cutting room cuts fabric from a marker layout, that fabric cannot be uncut. Both
decisions are hers to make and hers to defend.

The current job is a directional chevron border print for a softshell jacket line, printed on a
brushed ("napped") softshell face fabric whose raised fiber surface runs in one direction. The
chevron motif itself is not symmetric under reflection — it points one way, like an arrow — which
means every mirrored copy of it is a genuinely different-looking image from the original, not an
identical twin (SEE APPENDIX A). The jacket's front is two mirror-image panels that must meet at a
center-front zipper seam with the chevron matching exactly; a separate back-yoke seam mirrors the
same family of motif across a horizontal seam instead of a vertical one (SEE APPENDIX A). To build
the mirrored panel's CAD artwork from the master motif, Yuki applies a rotation (to align the motif
to the marker's cutting angle) and a reflection (to produce the mirror image) — and the order she
applies them in is not interchangeable, because rotation and reflection do not commute in general
(SEE APPENDIX A).

That geometric fact collides with a second, independent constraint. Reflecting the motif to build a
mirrored panel also reverses which way the fabric's nap runs on that panel — a defect the trade's
own napped-fabric guidance warns against by name (SEE APPENDIX D). The only way to guarantee every
panel's nap runs the same direction is to forbid reflection across the whole marker and cut every
piece facing the same way, which costs real, sourced extra yardage over a layout that is free to
flip pieces (SEE APPENDICES D and E). The print house's rotary screen printer can also adjust its
repeat length within a documented range, which matters once this same motif gets reused on a second
printer that has a different adjustable range of its own — resizing the motif there means dilating
it by a scale factor, not just moving it into place (SEE APPENDIX B). A separate, real patent on
marker-alignment buffers for pattern-matched fabrics shows this is not a novelty problem unique to
Yuki's shop — the same registration challenge has a documented industrial history (SEE APPENDIX C).

Yuki's recommendation must be defended on one number: total fabric cost for this production run
under whichever marker layout policy she recommends (SEE APPENDICES D, E and F). Every sourced and
assumed figure in this case is listed in the appendices and the Modeling Assumptions section — full
source citations for every sourced figure are in **APPENDIX H** — and
the vocabulary and "how to…" skills this case will ask of you are listed in **APPENDIX G** — that
is where Challenge 1 sends you.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->

## Dilemma

You are Yuki Alvarez.
Do you:
A.) Recommend the Same-Grain Marker — lock every piece to face the same direction so the nap never
reverses, and pay the real yardage premium that requires OR
B.) Recommend the Mirror-Match Marker — allow the mirrored front and back-yoke panels to save
yardage, provided your CAD file's rotate/reflect composition order puts the registration point
exactly where the seam's match line actually sits

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A coordinate-plane diagram tracing the front panel's registration point through both
    candidate composition orders (rotate-then-reflect and reflect-then-rotate), with the motif's
    position and the registration point's coordinates labeled at every intermediate step.
    D2. A second coordinate-plane diagram applying the equivalent build to the back-yoke panel,
    which mirrors across a horizontal seam instead of a vertical one, plus a 180-degree-rotation
    check confirming whether the yoke's motif lands in matching orientation against a third,
    separate panel elsewhere in the same marker that is only rotated, never reflected.
    D3. A symmetry analysis of the master chevron motif: a diagram testing every candidate axis
    for a line of symmetry, with a written explanation of why none exists and how that absence is
    exactly what makes the composition order in D1 non-interchangeable.
    D4. A repeat-tiling diagram showing the motif translated at fixed intervals across the
    printable fabric width, drawn once at the printer's minimum adjustable repeat setting and once
    at its maximum, with every translation vector labeled.
    D5. A congruent-vs-similar comparison: a diagram and written argument showing that the
    rotated/reflected/translated copies used on this printer are congruent to the master motif and
    to each other, versus a rescaled copy dilated to fit an integer number of repeats on a second
    printer with a different adjustable repeat range, with that dilation's scale factor computed
    and shown.
    D6. A marker-layout cost comparison and final recommendation: a table showing total fabric
    cost for the production run under the Same-Grain Marker versus the Mirror-Match Marker,
    stating in writing which composition order from D1 the Mirror-Match recommendation depends on
    getting exactly right.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

### Appendix A — Panel Geometry & the Registration Point

The registration point is the exact pixel the rotary screen locks the print to the cut line by. A
rotation applied before a reflection and a reflection applied before that same rotation do not, in
general, send the registration point to the same place — this appendix supplies the coordinate
setup a diagram needs to check that directly for this motif and these panels.

| Quantity | Value |
|---|---|
| Front-panel registration point coordinates (local CAD panel coordinate system) | (4, 6), in inches, origin at the panel's bottom-left corner [MA1] |
| Front seam axis (center-front zipper seam) orientation | Vertical — coincides with the panel's local y-axis [MA2] |
| Marker cutting-angle rotation applied to the front panel | 90° counterclockwise [MA3] |
| Back-yoke registration point coordinates | (5, 3), in inches, origin at the panel's bottom-left corner [MA4] |
| Back-yoke seam axis orientation | Horizontal — coincides with the panel's local x-axis [MA5] |
| Rotation applied to the third, non-mirrored marker panel referenced in D2 | 180° [MA6] |

*Every value in this appendix is a stated Modeling Assumption (SEE Modeling Assumptions block below)
— these figures live only inside Yuki's own CAD file, and no outside source could ever report them.*

### Appendix B — EFI Reggiani UNICA Rotary Screen Printer & a Second Printer's Repeat Range

The primary printer's repeat length is electronically adjustable, which is exactly what makes the
motif reusable across more than one machine — provided it is resized correctly.

| Quantity | Value |
|---|---|
| Primary printer (EFI Reggiani UNICA) minimum adjustable print repeat length | 25 in / 640 mm [S1] |
| Primary printer (EFI Reggiani UNICA) maximum adjustable print repeat length | 40 in / 1018 mm [S1] |
| Master motif's native repeat length, as designed | 30 in / 762 mm [MA7] |
| Second printer's electronically adjustable repeat length range | 20-30 in / 508-762 mm [MA8] |

*A genuine attempt to source a second, real rotary-screen printer model with an electronically
adjustable repeat range meaningfully different from the UNICA's could not confirm one — every
manufacturer spec sheet found (SPGPrints Palm and RD8, Stork, MHM) cites the same
530/640/688/725/819/914/1018 mm family of standardized screen circumferences the whole industry
shares, because these machines mount physically interchangeable screen cylinders (SEE
RESEARCH_LOG.md). [MA8] is a stated Modeling Assumption for a hypothetical second machine, chosen
to sit inside that same real standardized family while still differing from the UNICA's range, so
Challenge D5's dilation problem has a genuine, computable scale factor.*

### Appendix C — US Patent 5,333,111, Marker-Alignment Buffer Language

US Patent 5,333,111, "Garment cutting system having computer assisted pattern alignment," describes
why plaid- and stripe-matching fabrics historically required a skilled worker to align patterns by
hand, and states that a marker must leave a buffer around any garment segment that requires
matching "often as much as half a fabric design repeat."

| Quantity | Value |
|---|---|
| Patent's stated maximum pattern-alignment buffer, as a fraction of one design repeat | One-half (1/2) of one fabric design repeat [S2] |
| Buffer size in inches, using Appendix B's repeat-length range | 12.5-20 in *(derived: 1/2 x 25 in and 1/2 x 40 in, from [S1] and [S2])* |

### Appendix D — Sewing & Craft Alliance Guideline 4.120, Napped Fabrics

The Sewing & Craft Alliance's own guideline on napped/directional fabrics states that pattern
pieces must be laid out so the nap runs the same direction on every piece, or the finished garment
shows visibly uneven color shading, and that this same-direction requirement costs extra fabric.

| Quantity | Value |
|---|---|
| Extra yardage required for a with-nap (same-direction-only) layout vs. a without-nap (flip-allowed) layout | 15-25% [S3][S4], consistent with Guideline 4.120's own qualitative confirmation that a with-nap layout "generally requires" extra fabric [S5] |

### Appendix E — UCSB Bren School Marker-Efficiency Data

Real measured factory data on marker material utilization, from a 2024 university capstone report
on cut-and-sew apparel supply-chain waste, gives this case a real baseline efficiency band to
compare the same-grain layout's yardage penalty against.

| Quantity | Value |
|---|---|
| Average marker material utilization, measured Vietnam-factory data (Patagonia 2022 seasons) | 82% [S6] |
| Measured marker waste range, same report | 16-21% [S7] |
| 686 Technical Apparel's own publicly disclosed cutting efficiency | 87% [S8] |
| Broader literature baseline, pre-consumer cutting waste | 10-15% [S9] |

### Appendix F — Production Run & Fabric Cost

| Quantity | Value |
|---|---|
| Brushed/napped softshell face fabric cost | $39.00 / yard [S10] |
| Jacket line total production run size | 5,000 units [MA9] |
| Base fabric yardage required per finished unit (flip-allowed baseline, before any nap penalty) | 3.0 yd / unit [MA10] |

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Front-panel registration point coordinates | (4, 6) in | Internal to Yuki's own CAD file; no outside source can ever report a fictional company's registration-point pixel. Chosen as a simple, checkable coordinate for the D1 diagram. | Does not affect the cost dilemma or `margin_pct`. Affects only the geometry diagrams (D1-D3): any consistent coordinate that keeps the panel's shape intact works equally well for testing composition-order non-commutativity. |
| MA2 | Front seam axis orientation | Vertical (y-axis) | Matches the case's description of a center-front zipper seam running the length of the garment. | Same as MA1 — no effect on cost or margin. |
| MA3 | Marker cutting-angle rotation, front panel | 90° CCW | A round, teachable rotation that makes D1's rotate-then-reflect vs. reflect-then-rotate comparison land on clearly different, non-overlapping coordinates. | Same as MA1 — no effect on cost or margin. A rotation other than a multiple of 90° would still work but would not commute either; 90° is chosen for MS-level coordinate arithmetic. |
| MA4 | Back-yoke registration point coordinates | (5, 3) in | Same basis as MA1, for the back-yoke panel of D2. | No effect on cost or margin. |
| MA5 | Back-yoke seam axis orientation | Horizontal (x-axis) | Matches the case's description of a back-yoke seam that mirrors across a horizontal seam instead of the front's vertical one. | No effect on cost or margin. |
| MA6 | Rotation on the third, non-mirrored panel (D2) | 180° | Gives D2's "matching orientation" check a clean, computable comparison against the yoke panel. | No effect on cost or margin. |
| MA7 | Master motif's native repeat length | 30 in / 762 mm | No outside source reports the repeat length Yuki originally designed into her own CAD file. Chosen to sit inside the sourced UNICA range (25-40 in, [S1]) so the motif is usable on the primary printer without modification. | No effect on cost or margin; sets up the D4/D5 translation and dilation diagrams. |
| MA8 | Second printer's adjustable repeat range | 20-30 in / 508-762 mm | A genuine attempt to source a real second machine with a meaningfully different range failed — every manufacturer spec found shares the industry's standardized 530-1018 mm screen-circumference family (SEE Appendix B note and RESEARCH_LOG.md). Chosen within that same real family, shifted down from the UNICA's range. | **Flips D5's answer directly.** The dilation scale factor Challenge D5 asks for is computed from this range against MA7's native repeat length; a different assumed range changes that scale factor, though it never changes which marker-layout policy (A or B) is cheaper — D5 is a geometry deliverable, not a cost input. |
| MA9 | Jacket line total production run size | 5,000 units | Order-specific to Yuki's fictional employer; no run size for a specific fictional production order can be sourced. A representative mid-size converter run. | **Cancels out of `margin_pct`.** Because it multiplies both options' total cost identically, it changes the two options' dollar totals but not the percentage gap between them. |
| MA10 | Base fabric yardage required per finished unit (flip-allowed baseline) | 3.0 yd / unit | Order-specific; chosen within the range consumer/home-sewing yardage guides give for a structured jacket (2.5-4 yd, per the sources checked in RESEARCH_LOG.md), scaled down slightly for an efficient flip-allowed industrial marker. | **Cancels out of `margin_pct`** for the same reason as MA9 — it is a common multiplier on both options' cost. |

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Congruent
- Similar
- Translation
- Symmetry
- Line Of Symmetry
- Dilation
- Scale Factor
- Transformation
- Reflection
- Rotation
- Clockwise
- Counter-Clockwise

**"How to…" questions**

- How to translate a figure on the coordinate plane
- How to reflect a figure across the X-Axis
- How to reflect a figure across the Y-Axis
- How to rotate a figure on the coordinate plane 90 degrees counterclockwise
- How to rotate a figure on the coordinate plane 180 degrees
- How to dilate a figure on the coordinate plane given a scale factor
- How to find the scale factor of a dilation
- How to rotate a figure on the coordinate plane 90 degrees clockwise

### Appendix H — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | EFI Reggiani UNICA rotary screen printer, adjustable print repeat length | 25-40 in / 640-1018 mm, stepless, electronically controlled | EFI — [Reggiani UNICA product page](https://www.efi.com/products/textile/efi-reggiani-analog-printers/efi-reggiani-unica-rotary-screen-printer/) and [brochure](https://www.efi.com/wp-content/uploads/sites/2/2023/10/EFI-Reggiani-UNICA-Brochure-US.pdf) | 2023 | HIGH |
| S2 | US Patent 5,333,111 ("Garment cutting system having computer assisted pattern alignment"), stated maximum plaid/stripe marker-alignment buffer | "often as much as half a fabric design repeat" | USPTO / [Google Patents, US5333111A](https://patents.google.com/patent/US5333111A/en) | 1994 (patent grant) | HIGH |
| S3 | Extra yardage for nap/directional fabric layouts | 15-25% | [Sewing With Ease, Fabric Yardage Calculator](https://sewingwithease.com/fabrics/fabric-yardage-calculator/) | 2026 | MEDIUM — a craft/consumer yardage guide, not an industrial-marker source; used because it is one of the few sources that states a concrete percentage. |
| S4 | Extra yardage for directional print, nap, velvet, or pile layouts | 10-25% | [Canvas Etc., Fabric Yardage Calculator](https://www.canvasetc.com/fabric-yardage-calculator/) | 2026 | MEDIUM — same caveat as S3; the two sources' ranges overlap at 15-25%, which is the value used in Appendix D. |
| S5 | Trade-association confirmation that a with-nap layout requires extra fabric and must run all pieces the same direction | Qualitative confirmation; no specific percentage stated in the primary document itself | Sewing & Craft Alliance, [Guideline 4.120, "Napped Fabrics"](https://www.sewing.org/files/guidelines/4_120_napped_fabrics.pdf) | 2006 (7/06) | HIGH for the qualitative claim; the guideline itself carries no percentage, so S3/S4 supply the number used in Appendix D. |
| S6 | Average marker material utilization, Patagonia's Vietnam Tier-1 factories, Fall/Spring 2022 seasons | 82.0% ("Used") | UC Santa Barbara Bren School of Environmental Science & Management, [*Examining Cut-and-Sew Textile Waste within the Apparel Supply Chain*](https://bren.ucsb.edu/sites/default/files/2024-04/Examining%20Cut-and-Sew%20Textile%20Waste%20within%20the%20Apparel%20Supply%20Chain%204.10.24.pdf) (Final Report, March 22, 2024), Figure 6, p. 35 | 2024-03-22 | HIGH |
| S7 | Measured marker waste range, same report | 16-21% (Table 10: 16% high-efficiency scenario, 21% low-efficiency scenario, 18% average) | Same report, Table 10, p. 34 | 2024-03-22 | HIGH |
| S8 | 686 Technical Apparel's own publicly disclosed fabric-cutting efficiency | 87% | Cited in the same Bren School report, p. 9, attributing "686 Technical Apparel, n.d." | 2024-03-22 (as cited; 686's own disclosure is undated) | MEDIUM — secondary citation of an undated primary disclosure. |
| S9 | Rissanen (2005) baseline pre-consumer cutting-room fabric waste | 10-15% | Cited in the same Bren School report, p. 9: "Older estimates show that 10-15% of fabric is discarded in the cut-and-sew process (Rissanen, 2005)" | 2024-03-22 (as cited; original Rissanen paper is 2005) | MEDIUM — secondary citation; Rissanen's original paper (*From 15% to 0*) was not independently fetchable (403 on direct access). |
| S10 | Brushed-face technical softshell fabric, current retail price | $39.00 / yard (Polartec Power Shield Midweight, regular price) | [Discovery Fabrics, Softshells collection](https://discoveryfabrics.com/collections/softshells) | 2026 | MEDIUM — a retail, small-yardage consumer price, used as a proxy for a converter's bulk per-yard cost; the actual bulk/wholesale rate a converter pays is not publicly listed by any supplier checked (SEE RESEARCH_LOG.md). |
