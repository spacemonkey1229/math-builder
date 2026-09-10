# RESEARCH_LOG.md — Fizzer Order

One row per figure researched. Rejections are recorded because they stop the next person
re-running the same dead search.

## P01 — Cardstock price per square inch (Appendix D)

- Searched: "Uline chipboard cardstock sheets price per sheet 100 lb" — Uline's own chipboard
  category pages came back but no specific chipboard/cardstock sheet product with a clear
  per-sheet price at the sizes this case needs; a generic "$0.10–$0.50 per sq ft" range site
  (thepricer.org) surfaced but is an undated aggregator with no named primary source — rejected
  as LOW confidence, not used.
- Searched: "Neenah 110 lb cardstock 8.5x11 250 sheets price" — multiple retailers (Quill, Walmart,
  Office Depot, Best Buy) carry the same named product (Neenah Exact Index 110 lb., WAU40411).
- Fetched: Quill.com's own product page. Found: $20.99 for a 250-sheet, 8.5"x11" pack of 110 lb.
  index cardstock, white. **HIGH confidence** — primary retailer, current, dated by access,
  unambiguous size and weight.
- Derived: price per sheet = $20.99 / 250 = $0.08396. Sheet area = 8.5 x 11 = 93.5 sq in. Price
  per sq in = $0.08396 / 93.5 = $0.00089797. This single figure prices both container options,
  since both are cut from the same stock (SEE Appendix D).

## P02 — Mini Fizzer (mini bath bomb) diameter (Appendix B)

- Searched: "wholesale mini bath bomb diameter inches spec sheet" — finished bath bomb *products*
  (not molds) gave inconsistent, largely unsourced diameter claims in an AI-generated search
  summary (a range from "1 inch" to "2.5 inches" with no single citable product) — rejected as too
  vague to cite directly.
- The same search surfaced GumballStuff.com's own mini bath bomb *mold* product, which states an
  unambiguous finished diameter.
- Fetched: GumballStuff.com's product page directly. Found: "1-inch in diameter," SKU ECR1CLR50,
  described as "approximately the size of a quarter." **HIGH confidence** — primary retailer's own
  current listing, unambiguous diameter, real commercial mold product.
- Note: a larger "2.75 in diameter" bath bomb mold (Wholesale Supplies Plus) was also found and
  fetched during initial exploration, but at that size a single bath bomb (10.89 cu in) would not
  fit multiple-per-box inside either candidate container — using it would have broken the "gift
  sampler holding several fizzers" premise the case needs. The 1-inch mold was used instead because
  it is the real product that actually fits the scenario, not because it produced a more
  convenient number.

## P03 — Sphere loose-packing fraction (Appendix C)

- Searched: "random close packing spheres 64 percent Wikipedia" — multiple physics sources
  (Wikipedia, MathWorld, Physics World, phys.org, arXiv preprints) all converge on the same
  qualitative figure.
- Fetched: Wikipedia's "Random close pack" article directly. Found: "the most compact way to pack
  hard perfect same-size spheres randomly gives a maximum volume fraction of about 64%." **MEDIUM
  confidence** — well-established and widely cross-confirmed, but the article itself states "about
  64%" rather than one precise decimal, and notes there is no single agreed exact value across all
  experiments/methods. This is exactly a MEDIUM case per case-research's grading rubric: the figure
  is real, dated-enough (a stable physical constant, not a market price that goes stale), and
  unambiguous in units, but is itself a stated range/approximation at the source.
- This figure is applied identically to both container shapes as Modeling Assumption MA1
  (Appendix E) — no published figure exists specifically for a tapering cone shape, and inventing
  one would be exactly the kind of fabrication this pipeline forbids. The uniform-application
  caveat is disclosed openly rather than hidden.

## P04 — Shipping carton price and dimensions (Appendix F)

- Searched: "Uline standard shipping carton 12 x 12 x 12 price dimensions" — found Uline's own
  12x12x12 corrugated box product (S-4125), a common, widely-stocked cube-shaped shipping carton
  well suited to "round, cubic, or odd-shaped items" per Uline's own product description.
- Fetched: Uline's product page directly. Found: 12"x12"x12" interior dimensions, $1.16 per box at
  the bundle-of-25 price tier. **HIGH confidence** — primary retailer, current, dated by access,
  unambiguous dimensions.
- Used only for D5's shipping-footprint estimate (an illustrative, not load-bearing, secondary
  consideration per Background) — not part of the D4 primary-metric calculation.

## Summary

| Placeholder | Value | Confidence | Status |
|---|---|---|---|
| P01 cardstock price/sq in | $0.00089797/sq in (derived from $20.99/250-sheet pack) | HIGH | SOURCED |
| P02 Mini Fizzer diameter | 1.00 in | HIGH | SOURCED |
| P03 loose-packing fraction | ~64% | MEDIUM | SOURCED |
| P04 shipping carton price/dims | $1.16/carton, 12x12x12 in | HIGH | SOURCED |

**NOT FOUND count: 0.** Every figure this case needed was found and cited on the first or second
search framing; none required a Modeling Assumption in place of a real figure (MA1 and MA2 in
Appendix E are genuine scenario/business assumptions, not stand-ins for unsourceable facts).

Next step: build `sensitivity_model.py` and the `published/` packet.
