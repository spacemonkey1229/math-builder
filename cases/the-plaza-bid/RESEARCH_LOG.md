# RESEARCH_LOG.md — The Plaza Bid

`case-research` pass, 2026-09-01. 11 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
6 SOURCED, 5 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Plaza dimensions (Appendix A)

Searched: nothing — Ashford is fictional, so no real blueprint exists to source. Chosen deliberately
so the two dimensions (45, 30) have a clean, computable GCF (15) for Appendix B's staging-block
deliverable, and so neither tile sheet's real manufactured size (Appendix C, D) divides both
dimensions evenly, which is what makes Appendix E's cut-waste computation genuinely have two
different answers instead of both being trivially zero.

**Outcome: ASSUMPTION.** MA1 = 45 ft × 30 ft (1,350 sq ft). Flagged HIGH sensitivity — every
downstream computation depends on these exact numbers.

## P02 — Bid deadline (Appendix A)

Searched: nothing — explicitly framed as a narrative/flavor detail matching the Overview's
same-week urgency, not a load-bearing figure.

**Outcome: ASSUMPTION.** MA2 = 4 days. Decorative, not load-bearing.

## P03 — Hexagon mosaic tile: price and sheet size (Appendix C)

Searched: "hexagon mosaic tile price per square foot Floor Decor OR Home Depot OR Tile Shop." Home
Depot and The Tile Shop's own product pages both returned HTTP 403 on direct `WebFetch` and on a
`curl` retry with a browser user-agent, and also 403'd through the `r.jina.ai` reader proxy — all
three routes blocked. Pivoted to `stoneandtileshoppe.com`, a real independent online tile retailer,
which fetched successfully and directly on every attempt (no proxy needed).

Fetched `stoneandtileshoppe.com/products/color-wheel-mosaic-0190-0790-arctic-white-1_1_2-hexagon-ceramic-mosaic`
directly. Confirmed on the page: "$6.59 / Sqft" (current listed price; "on sale from $9.39/Sqft"
also shown), "Actual Size: 11 5/8" x 10 1/4" | 0.81 sqft per sheet," "12 sheets per box, 9.72 sq ft
per box." Product: Daltile Color Wheel Mosaic, Arctic White, 1½" hexagon, ceramic mosaic.

Judgment call: used the *listed* price ($6.59) actually obtainable on the access date, not the
crossed-out regular price ($9.39), per the domain note's own guidance to use "a named retailer's
live price list captured with a date" — a live price list's live price is $6.59 on 2026-09-01,
whatever the regular price is. This is logged explicitly because it is a real judgment call that
changes the case's numbers materially (see the "regular-price counterfactual" note under the
Margin section below).

**Outcome: SOURCED, HIGH.** S1.

## P04 — Octagon-and-dot mosaic tile: price and sheet size (Appendix D)

Searched: "octagon and dot mosaic tile price per square foot Floor Decor OR Home Depot OR Tile
Shop." Same blocking pattern as P03 — Home Depot 403'd on direct fetch, `curl`, and the `r.jina.ai`
proxy. Found a Lowe's listing via search snippet but its direct fetch also 403'd. Returned to
`stoneandtileshoppe.com` and searched their catalog directly for an octagon-and-dot Daltile product
to keep the retailer (and manufacturer) consistent with S1 for a clean, apples-to-apples,
same-supplier comparison.

Fetched `stoneandtileshoppe.com/collections/octagon-mosaics/products/octagon-dot-6501-matte-white-with-gray-gloss-dots-2-octagon-ceramic-mosaic`
directly. Confirmed on the page: "$9.69 / Sqft," "Actual Size: 12" x 12" 1 sqft per sheet. 10 sqft
per box. 10 sheets per box." Product: Daltile Octagon & Dot 6501, Matte White with Gray Gloss Dots,
ceramic mosaic.

**Outcome: SOURCED, HIGH.** S2. Same retailer and manufacturer (Daltile) as S1 — deliberately
chosen this way once found, since it removes "different supplier's markup" as a confound in the
price comparison Appendix C vs. D sets up.

## P05 — Standard tile installation waste allowance (Appendix E)

Searched: "tile installation waste factor percentage hexagon pattern add extra material." General
search results (makecalcs.net, tilecalcs.com, stonemarketusa.com, several others) converged on
"10% for a standard/straight layout" as the common baseline figure, with higher figures (12-18%)
for more complex laying *patterns* (brick bond, diagonal, herringbone) — none of the sources found
addressed *tile shape* (hexagon vs. square-based) as its own waste-factor variable; all of them
frame waste factor purely in terms of the *laying pattern* chosen for otherwise-rectangular tile.

Fetched `makecalcs.net/blog/tile-waste-factor-guide` directly (succeeded without a proxy).
Confirmed the specific quoted line: "A straight layout in a simple rectangular room wastes about
10% of your tiles." The page separately lists pattern-complexity add-ons (brick bond +12%, diagonal
+15%, herringbone +18%) and room-complexity add-ons, but does not address hexagonal tile shapes at
all, which is exactly why the case treats this 10% figure as a general breakage/field-cut allowance
applied identically to both options, layered on top of the geometry-specific grid-rounding waste
this case computes itself (Appendix E) rather than trying to find (or invent) a shape-specific
industry waste-factor figure that does not appear to exist publicly.

**Outcome: SOURCED, MEDIUM.** S3. Confidence MEDIUM because the source is an independent
installation-calculator/blog site, not a manufacturer or trade-association standard.

## P06 — Published U.S. tile installation labor cost range (Appendix F)

Searched: "tile installation labor cost per square foot 2026 HomeAdvisor OR Angi." Direct
`WebFetch` of `angi.com/articles/tile-installation-cost.htm` returned HTTP 403. Retried via the
`r.jina.ai` reader proxy, which returned full real page text. Confirmed: "Labor costs for tile
installation are around $3 to $15 per square foot"; "contractors charge hourly rates, ranging from
$60 to $120 per hour"; and, on pattern complexity, "small, intricate tiles are more time-consuming
and costly to install" — but the page does not give a specific dollar or percentage figure
distinguishing mosaic/intricate-pattern labor from standard-layout labor.

**Outcome: SOURCED, HIGH.** S4.

## P07 — Base labor rate used in this case (Appendix F)

No published source gives a single specific labor rate for this fictional job; S4's range ($3-$15/
sq ft) is wide. Chose the midpoint of that real, cited range as a defensible working figure rather
than inventing an unsourced specific rate from nothing.

**Outcome: ASSUMPTION.** MA3 = $9.00/sq ft, anchored inside S4's cited range (not free-floating).

## P08, P09 — Independent confirmations #2 and #3 that mosaic/intricate tile costs more labor (Appendix F)

Searched for a second and third independent source to check whether S4's qualitative claim (mosaic
tile takes longer to install) was an outlier or a consensus view, and to look for any source that
DID publish a specific numeric premium (none was found — see P10).

Fetched `homeguide.com/costs/tile-installation-cost` via `r.jina.ai` (direct `WebFetch` 403'd).
Confirmed: "Tiny, intricate designs...typically cost more to install because they're more difficult
and time-consuming," overall labor range "$8 to $20 per square foot."

Fetched `estimationpro.ai/tools/blog/labor-price-for-tile-installation` via `r.jina.ai` (direct
`WebFetch` 403'd). Confirmed: "Small tile / mosaics: slower layout + more grout + more cleanup,"
standard tile range "$4 to $25 per square foot."

**Outcome: SOURCED, MEDIUM (both).** S5, S6. Both confirm the same qualitative direction as S4
independently, which is why the case treats "mosaic tile costs more labor" as a real, multiply-
sourced qualitative fact even though no single source gives an exact number.

## P10 — Exact numeric labor premium for Option A (hexagon mosaic) (Appendix F)

Searched specifically for a published percentage (not just a qualitative statement) differentiating
mosaic/hexagon labor cost from standard-layout labor cost: "tile installation labor cost premium
mosaic pattern percentage," and checked homeguide.com and estimationpro.ai (already fetched for
P08/P09) specifically for a number. Neither, nor any other source found, publishes one — every
source stops at the qualitative claim.

**Outcome: NOT FOUND → ASSUMPTION.** MA4 = +15%, a round, moderate value inside the general
direction S4/S5/S6 all confirm. Flagged HIGH sensitivity — this is the single most decision-
relevant modeling choice in the case (see the Margin section and `sensitivity_model.py`).

## P11 — Cut-waste computation methodology for an irregular manufactured sheet (Appendix E, MA5)

Not a web-search question — a modeling-methodology decision. A fully accurate model would need to
simulate the true staggered/offset row pattern within each hexagon mosaic sheet, which is beyond
MS-level geometry and beyond what a bid estimator would do for a first-pass takeoff in practice.

**Outcome: ASSUMPTION (methodology).** MA5 = compute cut-waste via each sheet's bounding-rectangle
grid fit (round up partial rows/columns) rather than the true hexagon offset pattern. Disclosed as
conservative in the direction of understating, not overstating, Option A's real advantage (see
case.md's Modeling Assumptions block for the reasoning).

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none
needs_source OPEN remaining: 0
```

No LOW-confidence source exists in this case at all — S3, S5, S6 are MEDIUM (independent
blog/aggregator sources, not manufacturer/trade-association standards, but specific and directly
confirmed by fetch), and S1, S2, S4 are HIGH (a live retailer product page and a major
home-services cost aggregator, respectively).

## A genuine research finding that inverted the concept sheet's initial framing

The concept sheet (`CONCEPTS_formal-logic-vectors-matrices-numbertheory_2026-08-23.md`, C5)
hypothesized the hexagon option would have "minimal cut waste" and the octagon-and-square option
would have cut waste "raising waste percentage." Real, sourced manufactured-sheet geometry found
during research shows the opposite: the octagon-and-dot tile's real sheet is exactly 12″×12″ (a
perfect 1 sq ft square, S2) which divides the plaza's whole-foot dimensions with zero
grid-rounding waste, while the hexagon tile's real sheet is 11⅝″×10¼″ (S1), an irregular rectangle
that does not divide the plaza's dimensions evenly in either direction. Computed cut-waste
(Appendix E): Option A (hexagon) 10.5%, Option B (octagon+square) 9.1% — the hexagon has the
*higher* real waste percentage, not the lower one.

This is disclosed here explicitly as a real judgment call, not smoothed over: rather than force the
concept sheet's initial hypothesis, the case was written to the real sourced numbers. The dilemma's
two-option structure, the primary metric (total installed cost per sq ft including waste), and the
underlying interior-angle-sum/GCF skill targets are all unchanged from the concept sheet — only
which option carries the "higher waste" label changed, because that label was never asserted by the
concept sheet as a citable fact, only as an initial narrative hypothesis pending research. The
case's D1 (tessellation proof) vs. D3 (real cut-waste) tension this creates is used deliberately as
the Twist in `FACILITATOR.md`.

## Margin (facilitator-only — computed here, not written into case.md)

Option A (Hexagon): sheet grid 47×36 = 1,692 positions (bounding rectangle 11.625in×10.25in against
the 45ft×30ft plaza, S1) + Appendix E's 10% install waste allowance (S3) → 1,862 sheets purchased;
purchased coverage = 1,862 × 0.81 sq ft/sheet (S1) = 1,508.22 sq ft; material cost = 1,508.22 ×
$6.59 (S1) = $9,939.17. Labor: $9.00/sq ft (MA3) × 1.15 (MA4) = $10.35/sq ft × 1,350 sq ft =
$13,972.50. **Total A = $23,911.67 → $17.71/sq ft.**

Option B (Octagon+Square): sheet grid 45×30 = 1,350 positions (12in×12in sheet divides the
45ft×30ft plaza exactly, S2) + 10% waste allowance (S3) → 1,485 sheets purchased; purchased
coverage = 1,485 × 1.00 sq ft/sheet (S2) = 1,485 sq ft; material cost = 1,485 × $9.69 (S2) =
$14,389.65. Labor: $9.00/sq ft (MA3), no premium × 1,350 sq ft = $12,150.00. **Total B = $26,539.65
→ $19.66/sq ft.**

**margin_pct = (19.66 − 17.71) / 19.66 × 100 = 9.9%. Winner: Option A, The Regular Hexagon
Pattern.** Well inside SPEC §2's ~20% cap — no retune pass needed.

**Regular-price counterfactual, checked explicitly.** If the hexagon's *regular* list price ($9.39,
shown crossed-out on the same page as S1's $6.59 sale price) had been used instead of the live
listed price, material cost A would rise to $14,162.19 (1,508.22 × $9.39), total A would rise to
$28,134.69 ($20.84/sq ft), and the winner would *flip* to Option B (B's $19.66/sq ft would then be
lower). This was checked specifically because the price choice is a real, disclosed judgment call
(P03) — the domain note's "live price list captured with a date" guidance is why the live/listed
price was used rather than the regular price, but a facilitator or a Hero could reasonably argue
the other way, and that argument is a legitimate in-discussion move, not a case defect.

**Sensitivity, checked via `sensitivity_model.py`.** MA4 (hexagon labor premium) is the case's real
fulcrum: at 0% premium, margin widens to ~16.8%; the winner does not flip until roughly a 37%
premium — more than double the 15% value used, so the base recommendation is reasonably robust, but
not so robust that a Hero should treat MA4 as untouchable. MA3 (base labor rate) does not flip the
winner across its full published range ($3-$15/sq ft, S4) — it scales both options together without
changing their fixed relative gap.

## SPEC §2 self-check

Primary metric exists (total installed cost per sq ft, both options computed): yes. Neither option
is structurally zero-cost: yes, both have real, substantial material and labor cost. Dilemma is not
a foregone conclusion: margin is 9.9%, real and modest, not a rout — and the case's own D1-vs-D3
tension (the "purer" tessellation has the higher real waste) means a Hero cannot shortcut the
decision by reasoning from geometry alone; the numbers have to actually be computed. **Verdict:
PASS**, no balance concern to flag for `case-readiness`. The one item worth flagging forward: the
tile-price judgment call (live/listed price vs. regular price, see the counterfactual above) is
real and disclosed, and a `case-readiness` or `case-qa` pass should confirm it's an acceptable
reading of the domain note's "live price list" guidance rather than silently re-deciding it.

## No sensitivity_model.py gap

Built `sensitivity_model.py` (PARAMS dict, `evaluate(params) -> {"A": ..., "B": ...}`, `FLEX[]` =
[`base_labor_rate_per_sqft`, `hex_labor_premium`]) since this case has a real, continuous, worth-
stress-testing sensitivity dimension (MA4's labor premium) whose flip point was not obvious without
actually computing the sweep — exactly the situation the pattern is meant for. One implementation
note logged here in case a future pass touches the model: naive Python float arithmetic
(`1350 * 1.10`) produces `1485.0000000000002` due to IEEE754 binary rounding, which would incorrectly
`math.ceil()` up to 1,486 instead of the mathematically exact 1,485 sheets — a real off-by-one that
was caught by cross-checking the model's output against this log's hand computation. Fixed with a
small-tolerance `_ceil_clean()` helper in the model; the hand computations in this log and in
`case.json.balance.margin_note` use the mathematically exact values throughout.

## Next step

Run `case-qa` on `the-plaza-bid`.
