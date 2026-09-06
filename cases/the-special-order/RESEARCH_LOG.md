# Research Log — The Special Order

Stage 3 (`case-research`) run on `cases/the-special-order/`. 6 `{{NEEDS_SOURCE}}` placeholders
enumerated from `case.md`. Worked in load-bearing order: Appendix B's milling allowances first
(these drive D2's core fraction arithmetic), then Appendix B's lumber price, then Appendix C's
Special Order figures (price premium, minimum order quantity, lead time).

## P01 — Jointing allowance (Appendix B)

**Searched:** "jointing allowance inch rough lumber before ripping to width woodworking",
"how much extra width to buy rough lumber jointer", "sizing rough lumber to finished dimension
allowance."

**Fetched directly:** `https://www.wwgoa.com/post/9-steps-to-sizing-rough-lumber` (WoodWorkers
Guild of America) — states directly: "Rip the rough width 1/4 in. wider than the finished width"
as the first-pass rip allowance before a final jointing pass. Cross-checked against
`finewoodworking.com/forum/rough-wood-milling-philosophy` and `workshopcompanion.com`'s truing
lumber guide, both of which describe the same general practice (rough-cut oversize before
jointing/planing to finished dimension) without giving as precise a number.

**Outcome:** SOURCED as [S1], value 1/4 in, MEDIUM confidence (trade-education guidance, not a
single manufacturer's dated spec — the WWGOA article carries no explicit publish date).

## P02 — Saw-kerf allowance (Appendix B)

**Searched:** "table saw rip blade kerf width standard 1/8 inch spec", "full kerf vs thin kerf
blade width."

**Fetched directly:**
`https://www.woodworkerssource.com/blog/woodworking-101/tips-tricks/woodworking-101-the-3-table-saw-blades-woodworkers-should-have/`
— states directly: "A full kerf is 1/8-inch, whereas thin kerf is just 3/32-inch." Cross-checked
against `flowyline.com`'s blade-thickness article (full kerf ≈0.110–0.125 in) and
`woodworkingtalk.com`'s kerf/blade-body-thickness thread, both consistent with 1/8 in as the
standard full-kerf figure.

**Outcome:** SOURCED as [S2], value 1/8 in, MEDIUM confidence (no explicit publish date on the
blog post; figure is, however, consistent across every independent source checked).

## P03 — Hard maple 4/4 price per board foot (Appendix B)

**Searched:** "Woodworkers Source hard maple 4/4 price per board foot."

**Fetched directly:** `https://www.woodworkerssource.com/hard-white-maple/maple-hard-white-44-lumber.html`
— live retailer product page states "$8.99 /Board Feet" for random-width selection (additional
upcharges apply for specified widths or straight-line ripping, not used here since this figure
feeds the *rough random-width* Standard Stock option).

**Outcome:** SOURCED as [S3], value $8.99/board foot, MEDIUM confidence (a live current price
with no explicit "last updated" timestamp on the page itself — only a copyright year — and retail
lumber prices fluctuate with market conditions).

## P04 — Special Order price per board foot (Appendix C)

**Searched:** "custom width milling S4S dimension lumber price per board foot hardwood mill
service", "Woodworkers Source straightline ripping surfacing price per board foot custom width."

**Fetched directly:**
- `https://help.woodworkerssource.com/support/solutions/articles/9000115990-how-do-i-buy-the-sizes-i-want-`
  — confirms selection/straight-line-rip fees apply but states no specific dollar amount; directs
  customers to call or email for a quote.
- `https://www.woodworkerssource.com/help/straight_line.html` — same outcome: no published price,
  "call or email for a quote."
- `https://pro.csclumber.com/blog/s4s-lumber-guide` — states surfacing/S4S milling "is a service,
  not a discount" but gives no specific per-board-foot rate.
- `https://www.woodweb.com/knowledge_base/Rates_for_custom_milling.html` — a real, named-contributor
  industry trade forum thread with reported hardwood custom-milling rates: "$0.25–$0.35/bdft" to
  "$0.40–$0.45/bdft" depending on the job, plus separate hourly/setup-fee models.

**Outcome:** No single retailer or mill publishes a specific per-board-foot rate for exact-width
custom milling of hard maple — every retail source that mentions the service directs the customer
to call for a quote rather than publishing one. **SOURCED as [S4]** using the WoodWeb trade
forum's reported $0.25–$0.45/board-foot range, midpoint $0.35/board foot, MEDIUM confidence (a
wide range picked down to a midpoint from forum-reported figures, not one supplier's published
price list — meets the case-research skill's MEDIUM criterion exactly: "a wide range you had to
pick a midpoint from"). Combined with [S3]'s $8.99 base price to produce Appendix C's derived
$9.34/board-foot rate (`derived: true` on the needs_source resolution).

## P05 — Minimum order quantity for a custom width run (Appendix C)

**Searched:** "hardwood mill minimum order quantity custom milling board feet", "custom width
dimensioning minimum board footage."

**Fetched directly:**
- `https://www.estatemillwork.com/hardwood-boards.html` — "There is no minimum — order one
  board... There is no minimum quantity and no cut fee," but this applies to individually
  cut-to-size boards, not a custom *width* dimensioning run across an entire order.
- `https://www.woodweb.com/knowledge_base/Rates_for_custom_milling.html` — one contributor reports
  "$50, 100 board foot minimum for sawing logs"; another describes a hybrid hourly/per-bd-ft model
  with no stated floor; a third (Florida Woodsmith, via search summary) states a "$50 minimum for
  logs yielding less than 40 linear feet." Estate Millwork's separate wholesale page states a
  500-board-foot minimum for bulk hardwood — a different service tier entirely (bulk purchase, not
  custom milling).

**Outcome:** **NOT FOUND** as a figure specific to this exact scenario — no source publishes a
minimum-order-quantity figure for a small custom exact-width dimensioning run specifically (as
opposed to log sawing, individual cut-to-size boards, or bulk wholesale purchasing, all of which
are adjacent but different services with their own, very different, minimums ranging from none to
500 board feet). Redesign (Exit 2) was considered and rejected: the batch-size-dependent
economics of a minimum order quantity is the reason this concept exists (per the approved concept
sheet's framing — "a bet she has to place today... only pencils out if the batch is big enough"),
so removing the constraint would gut the case rather than repair it. **Exit chosen: Modeling
Assumption (MA1)**, value 30 board feet, stated openly with a sensitivity note — see `case.md`
Appendix E and `case.json.modeling_assumptions[MA1]`. The value was chosen within the low end of
the real range found (above Estate Millwork's "no minimum" for single boards, well below the
100–500 board-foot minimums found for log-sawing and bulk wholesale), appropriate for a
specialized small-shop custom-width run.

## P06 — Lead time for a custom hardwood milling order (Appendix C)

**Searched:** same searches as P05 surfaced this figure directly.

**Fetched directly:** `https://www.estatemillwork.com/hardwood-boards.html` — direct quote:
"Boards are milled to order at our Meyersdale, Pennsylvania shop and ship nationwide in one to two
weeks."

**Outcome:** SOURCED as [S5], value 1–2 weeks, MEDIUM confidence (one named company's stated
turnaround, offered as representative of the trade rather than a universal figure — custom-mill
lead times vary by shop and by season).

## Verification pass

```
placeholders remaining: 0
citation markers with no source row: {}
source rows never cited in text: {}
LOW-confidence sources: []
```

All 6 placeholders resolved: 5 SOURCED (S1–S5), 1 ASSUMPTION (MA1, Appendix C's minimum order
quantity — the case's core sourcing risk, flagged as such at concept approval). No figure was
invented, rounded from memory, or presented as sourced without a fetched, checkable URL. The
5 sourced figures are all graded MEDIUM rather than HIGH — none carries an explicit, dated
publish timestamp on its own page, and the custom-milling premium and the minimum-order figure
both required synthesizing across multiple imperfect real-world sources rather than reading a
single authoritative number off one page. This is disclosed rather than upgraded artificially.

Next step: `Run case-readiness on the-special-order.`
