# Concept sheet — Textiles, Pattern & Garment Design (`textiles-pattern`)

**Target and why (one line).** `readmodel/domains.json`'s `textiles-pattern` entry is HIGH
authoring priority, MEDIUM data grade, **0 existing cases** — the domain itself names its
signature skills as Geometry/Transformations (reflection, dilation, translation, similarity) plus
two thin Fractions groups and one Measurement how-to, so it was checked directly against those
groups rather than against the generic Geometry gap list.

**A scoring note that changes how this reads.** This session's spine-wide sweep already found
zero true `n==0` skills anywhere in the 437-skill spine, and Geometry/Transformations in
particular has *already* been thinned hard this session: of its 20 skills, only 3 are still
`n<=2` (`geometry-congruent`=2, `geometry-similar`=2,
`geometry-how-to-reflect-a-figure-across-the-y-axis`=2) — the rest sit at n=3-5. I pulled every
id below live from `readmodel/standards_spine.json` on 2026-09-12; none of the "would close"
tables claim a false zero, and I flag n=3 skills as *not* thin rather than round them down.
Fractions/Addition-And-Subtraction (4/4 at n=2) and most of Fractions/Multiplication (3/4 at
n=2) are still genuinely thin and are the domain's best remaining lever. Because the easy
Transformations wins are mostly gone, none of the four concepts below clear the Cold Chain
4.2 calibration anchor — that is an honest consequence of the group already being worked this
session, not concept weakness, and I say so rather than inflate a score or an availability grade.

| # | Concept | Score | Tier | Skills (how-to/term) |
|---|---|---|---|---|
| C1 | Fold Or Open | **2.88** | T2 | 6 (3 how-to / 3 term) |
| C2 | The Grade Rule | **2.64** | T2 | 6 (2 how-to / 4 term) |
| C3 | The Repeat Match | **1.56** | T2 | 3 (2 how-to / 1 term) |
| C4 | The Nesting Cut | **1.44** | T2 | 4 (0 how-to / 4 term) |

**Recommendation.** Write **C1, Fold Or Open** first — it has the best raw skill count (it is the
only concept that reaches a genuine 3 how-to skills, including the one truly thin how-to left in
Transformations, `geometry-how-to-reflect-a-figure-across-the-y-axis`) and it matches
`domains.json`'s own decision archetype #2 verbatim. **C2, The Grade Rule** is the domain's
headline archetype (uniform dilation vs. graded increments) and is worth writing as the *second*
case even though it scores slightly lower — it is the concept a reader would expect this domain
to lead with, and it closes both remaining thin Transformations terms (`congruent`, `similar`).
Treat C1 and C2 as a pair the way SPEC's calibration note allows: together they close 4 of the 5
thin-or-borderline Transformations skills without overlap. **Kill C4** for this round — its 4
skills are all Quadrilaterals-And-Polygons terms with no how-to, its cost data (fabric price,
labor rate) is not sourced anywhere in `domains.json`, and at score 1.44 it is vocabulary-adjacent.
**C3** is a fine fourth idea to keep on file but needs a real yardage-loss number before
`case-research` should touch it — flagged LOW-leaning-MEDIUM below, not MEDIUM outright.

---

### C1 — Fold Or Open   ·   score 2.88   ·   tier T2

**Protagonist.** Priya Nakamura, cutting-room lead at a small-batch garment manufacturer (12
cutters, one 44-in bolt line), who signs off on every day's cutting layout and eats the fabric
overage out of the shop's own margin if she guesses wrong.

**The dilemma.** A.) Cut every bodice panel on the fold — half the pattern pieces, half the
marking and tracing time, but the fold forces extra fabric to be left un-nested on both sides of
the fold line OR B.) cut every panel open (full pattern piece, no fold) so the pieces can be
flipped and nested edge-to-edge across the full 44-in bolt width, saving fabric but doubling
marking and cutting time per panel.

**Primary metric.** Total dollars (fabric cost + cutting/marking labor) per finished garment —
a ratio, not a total, because the fold option's labor savings and the open option's fabric
savings pull in opposite directions and neither total alone settles it.

**Why it's close.** Cutting on the fold produces the mirror half of a pattern piece by reflecting
it across the fold line — mathematically identical to reflecting a figure across an axis on a
coordinate grid, and the two halves are congruent by construction. That symmetry is what halves
the marking work, but it also locks the piece's placement relative to the fold, which wastes the
sliver of fabric on either side that a freely-rotated open piece could use. Cutting open lets
Priya nest two panels together like matching congruent shapes head-to-tail, closing that gap — at
the cost of tracing and cutting twice as many distinct pieces. Whether the labor savings or the
fabric savings wins per garment is genuinely not obvious until both are priced out.

**Would close (6 skills, 3 how-to / 3 term):**

| id | kind | label | n |
|---|---|---|---|
| geometry-how-to-reflect-a-figure-across-the-y-axis | how-to | How to reflect a figure across the Y-Axis | 2 |
| geometry-line-of-symmetry | term | Line Of Symmetry | 3 |
| geometry-symmetry | term | Symmetry | 3 |
| geometry-congruent | term | Congruent | 2 |
| fractions-how-to-add-with-mixed-numbers | how-to | How to add with mixed numbers | 2 |
| fractions-how-to-multiply-a-fraction-and-a-mixed-number | how-to | How to multiply a fraction and a mixed number | 3 |

**Already-covered skills it also exercises.** `geometry-reflection` (n=4, the fold line itself);
`measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` (n=17, inches ↔ yards on the
bolt); `measurement-distance` (n=14, bolt width and panel widths).

**Data feasibility: MEDIUM.** Named sources I can point to:
- FreeSewing (`https://freesewing.eu/designs/`) — confirmed LIVE this session; its parametric
  pattern drafts expose real panel dimensions and fold-line placement I can pull specific pieces
  from instead of inventing panel sizes.
- Standard bolt widths (44/45-in and 58/60-in) — near-universal trade convention, citable to a
  named fabric retailer's own published width spec, but explicitly **not** a standards-body figure
  (per `domains.json`'s own note) — must be disclosed as trade convention, not "the standard."

Not confident about: any real published cutting-labor rate (dollars per minute of marking/cutting)
or fabric cost per yard for a specific fabric — these would need a stated Modeling Assumption or a
separately-verified fabric-price source `case-research` has not yet checked.

**Sensitivity (SPEC §6).** None — a shop-cost decision, no personal stakes.

**Split risk.** None — 6 skills, one deliverable arc (lay out both cutting plans, price both).

---

### C2 — The Grade Rule   ·   score 2.64   ·   tier T2

**Protagonist.** Devon Okafor, pattern grader for a mid-size apparel company, whose grade rule
ships to the factory this week and whose name is on the tech pack if size 16 doesn't fit.

**The dilemma.** A.) Grade the whole size run by one uniform dilation — scale every pattern point
by the same factor per size step, fast to produce and cheap to program OR B.) grade by point-
specific increments — move the bust point 1 inch per step while the shoulder point moves only
3/8 inch, matching how bodies actually grow across sizes, but requiring a separate scale
calculation at every pattern point.

**Primary metric.** Dollars of grading and marking labor per size in the run that fits within a
stated tolerance band across the body — because uniform dilation is cheaper to produce but "fits"
fewer of the sizes it claims to cover, while graded increments cost more per size but fit more of
them; raw labor cost alone favors A, raw fit count alone favors B.

**Why it's close.** A uniform dilation is a single scale factor applied to every point of a
similar figure — cheap to compute, and mathematically clean, but real bodies do not scale
uniformly (a bust grows faster than a shoulder across sizes), so at the small and large ends of
the run the uniformly-graded pattern stops being a genuinely similar copy of the base size and the
garment measurably misfits. Point-specific grading treats each landmark as its own scale-factor
problem, so it can hold every point within tolerance, but Devon has to justify why the extra
per-point labor is worth it in a run that may only sell a handful of the extreme sizes anyway.

**Would close (6 skills, 2 how-to / 4 term):**

| id | kind | label | n |
|---|---|---|---|
| geometry-dilation | term | Dilation | 3 |
| geometry-scale-factor | term | Scale Factor | 3 |
| geometry-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor | how-to | How to dilate a figure on the coordinate plane given a scale factor | 3 |
| geometry-how-to-find-the-scale-factor-of-a-dilation | how-to | How to find the scale factor of a dilation | 3 |
| geometry-similar | term | Similar | 2 |
| geometry-congruent | term | Congruent | 2 |

**Already-covered skills it also exercises.** `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit`
(n=17, inches/cm on a size chart).

**Data feasibility: MEDIUM.** Named sources:
- FreeSewing (`https://freesewing.eu/designs/`) — confirmed LIVE; its parametric formulas show
  exactly how a draft point's position is a function of a body measurement, which is the real
  math behind "why grading isn't uniform," and can source the base-size pattern coordinates.
- A single named brand's published size chart (per `domains.json`'s own note: brand charts differ,
  so the case must cite one specific brand's chart, not a generic industry table).

Not confident about: a real published *grade rule* table (the industry's actual per-point
increment values, e.g. ASTM D6960) — these are typically sold, not free; `case-research` will
likely need to construct a plausible, disclosed grade-rule table as a Modeling Assumption rather
than cite a paywalled one as real.

**Sensitivity (SPEC §6).** None.

**Split risk.** None — 6 skills, one arc (grade the run both ways, price and fit-check both).

---

### C3 — The Repeat Match   ·   score 1.56   ·   tier T2

**Protagonist.** Lena Vasquez, textile print designer at a small print house, pitching two ways to
lay a floral repeat onto a garment's center-front seam before the sample run is cut.

**The dilemma.** A.) Register the print so the repeat matches exactly across the center seam —
requires buying extra fabric to allow the pattern to be shifted (translated) into alignment at
every seam OR B.) accept a visible mismatch at the seam and buy only the fabric the pattern pieces
strictly require.

**Primary metric.** Extra dollars of fabric per garment required to guarantee a matched repeat —
a ratio against the base (mismatched) yardage, since the raw yardage difference alone doesn't say
whether the visual upgrade is worth the added cost per unit.

**Why it's close.** A matched repeat is a translation problem: the print motif has to land at the
same phase on both sides of the seam, which means the fabric has to be cut so the repeat's
translation vector lines up across the seam line — and because the repeat length rarely divides
evenly into a panel's height, matching almost always "wastes" a partial repeat's worth of fabric
per panel. Whether that partial-repeat waste, multiplied across an order, is worth the visual
upgrade over a cheap mismatch is the case.

**Would close (3 skills, 2 how-to / 1 term):**

| id | kind | label | n |
|---|---|---|---|
| geometry-translation | term | Translation | 3 |
| geometry-how-to-translate-a-figure-on-the-coordinate-plane | how-to | How to translate a figure on the coordinate plane | 3 |
| fractions-how-to-multiply-two-mixed-numbers | how-to | How to multiply two mixed numbers | 2 |

**Already-covered skills it also exercises.** None claimed beyond the table above — this is a
deliberately small, tightly-scoped set to avoid claiming skills the print-matching task doesn't
force.

**Data feasibility: MEDIUM leaning LOW.** Named sources:
- The Met Collection Open Access (`https://www.metmuseum.org/art/collection`) and Rijksstudio
  (`https://www.rijksmuseum.nl/en/rijksstudio`) — both confirmed LIVE; both give real repeat-print
  textile images with dimensions, useful for a real repeat length to work from.

Not confident about: any real, sourced number for how much *extra* fabric a matched repeat costs
in practice (this is normally a shop's internal costing rule, not published) — this is the
concept's weak point, and `case-research` should expect to flag it NOT FOUND and fall back to a
disclosed assumption, which is why this concept is graded down from the domain's overall MEDIUM.

**Sensitivity (SPEC §6).** None.

**Split risk.** None.

---

### C4 — The Nesting Cut   ·   score 1.44   ·   tier T2

**Protagonist.** Marcus Webb, marker maker (the person who lays out pattern pieces on the bolt
before cutting) at a costume shop, cutting fabric for a run of stage costumes on a fixed budget.

**The dilemma.** A.) Use simple rectangular panels for the skirt gores and yoke — easy to nest,
but the straight-edged panels don't follow the body, so more panels are needed to fake the shape
OR B.) use true trapezoid gores and a parallelogram yoke that follow the body's taper directly —
fewer, better-fitting panels, but their slanted edges leave triangular gaps when nested on the
bolt that a rectangle wouldn't.

**Primary metric.** Square inches of fabric waste per finished costume — a ratio against total
fabric purchased, since a wasteful layout on a small run costs little in absolute dollars but a
lot as a fraction of the (small) costume-shop budget.

**Why it's close.** A trapezoid or parallelogram panel matches the body's real taper with fewer
seams, so it needs less total pattern area than a rectangle-based fake — but its non-parallel
edges don't tile a rectangular bolt as cleanly, so more of the bolt is wasted around each piece.
The rectangle wins on nesting efficiency and loses on pattern area; which one wastes less fabric
overall depends on how tightly the shapes can actually be interlocked, which is the case.

**Would close (4 skills, 0 how-to / 4 term):**

| id | kind | label | n |
|---|---|---|---|
| geometry-trapezoid | term | Trapezoid | 2 |
| geometry-parallelogram | term | Parallelogram | 2 |
| geometry-rhombus | term | Rhombus | 2 |
| geometry-kite | term | Kite | 2 |

**Already-covered skills it also exercises.** `geometry-quadrilateral` (n=4, the umbrella term for
all four shapes above).

**Data feasibility: MEDIUM.** Named sources:
- The sheet-metal gauge chart (`https://sheetmetal.me/sheet-metal-gauge-chart/`) — confirmed LIVE
  per `domains.json`'s own note, usable only as the *parallel* nesting-on-standard-stock analogue,
  not as a garment source.
- Standard bolt widths, same trade-convention caveat as C1.

Not confident about: any real fabric-waste or panel-area data for costume-shop patterns — no
source in `domains.json` covers this, so the panel dimensions and waste figures would be entirely
constructed, not sourced. Combined with zero how-to skills closed, this is the weakest concept
here and is why the recommendation kills it for this round.

**Sensitivity (SPEC §6).** None.

**Split risk.** None.
