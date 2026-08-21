# Research Log — Carpenter

Legacy conversion. The source docx (`source/Y3/Session 4/Carpenter/Case Study_ Carpenter.docx`)
shipped its own material/maintenance cost table (tile/hardwood/carpet, material + underlayment +
installation cost/sq ft, wear life, minor/major maintenance) with **no citations at all** — every
figure in it was unverifiable and had to be treated as effectively `{{NEEDS_SOURCE}}`, even
though it arrived pre-filled. All of it was replaced with real, cited 2026 data. Room-by-room
square footage (from the source's floor-plan appendix image) had no citable real-world source
either, since the flat is fictional — declared as Modeling Assumption MA1 instead of invented as
fact.

| # | What was needed | What was searched | What was found | Outcome |
|---|---|---|---|---|
| P01 | Carpet installed cost, USD/sq ft | "2026 cost per square foot carpet installation material labor" (WebSearch); Homewyse calculator (WebFetch) | Homewyse, May 2026: $5.27-$7.72/sq ft installed | SOURCED — S1, midpoint $6.50 |
| P02 | Hardwood installed cost, USD/sq ft | "HomeAdvisor Angi 2026 hardwood flooring cost" (WebSearch, blocked by 403 on Angi); Homewyse calculator (WebFetch) | Homewyse, May 2026: $13.19-$16.72/sq ft installed | SOURCED — S2, midpoint $14.96 |
| P03 | Ceramic tile installed cost, USD/sq ft | "2026 tile flooring cost per square foot installed" (WebSearch); Homewyse calculator (WebFetch) | Homewyse, May 2026: $16.38-$20.21/sq ft installed | SOURCED — S3, midpoint $18.30 |
| P04 | Carpet material-only cost, USD/sq ft | "2026 carpet material cost only per square foot mid-grade nylon" (WebSearch) | HomeGuide 2026 compilation: $2.50-$4.00/sq ft (mid-grade nylon) | SOURCED — S4, midpoint $3.25 |
| P05 | Hardwood material-only cost, USD/sq ft | "2026 solid hardwood flooring material cost only per square foot" (WebSearch) | HomeGuide/multiple 2026 compilations: $4-$12/sq ft clustering | SOURCED — S5, midpoint $8.00 |
| P06 | Tile material-only cost, USD/sq ft | "2026 ceramic tile material cost only per square foot" (WebSearch) | Multiple 2026 compilations: glazed ceramic $4-$15/sq ft | SOURCED — S6, used $4.50 (low-to-mid of range, since Homewyse's installed figure already implies a lower material share) |
| P07 | Flooring wear-life (years), carpet/tile/hardwood | "NAHB life expectancy flooring carpet tile hardwood years" (WebSearch); direct PDF fetch + text extraction (Bash/pypdf, WebFetch failed on the PDF) | NAHB/Bank of America Home Equity "Study of Life Expectancy of Home Components," Feb 2007: carpet 8-10 yrs, tile(flooring) 75-100 yrs, all wood floors "Lifetime" | SOURCED — S7. Flagged as dated (2007); confirmed via search that current 2026 secondary sources still cite these exact figures as the industry standard. Confidence set to MEDIUM (not HIGH) for age. |
| P08 | Hardwood refinish cost, USD/sq ft | "2026 cost to refinish hardwood floors per square foot" (WebSearch) | HomeGuide/NerdWallet 2026: full sand & refinish $3.50-$6.50/sq ft; recoat-only $1-$2/sq ft (breakdown within same sources) | SOURCED — S8 (refinish, midpoint $5.00), S9 (recoat, midpoint $1.50) |
| P09 | Carpet cleaning cost, USD/sq ft | "2026 professional carpet cleaning cost per square foot" (WebSearch) | HomeGuide 2026: $0.25-$0.75/sq ft | SOURCED — S10, midpoint $0.50 |
| P10 | Tile/grout cleaning + sealing cost, USD/sq ft | "2026 grout cleaning sealing cost per square foot tile floor" (WebSearch) | HomeGuide 2026: cleaning $1.50-$3.50/sq ft + sealing $0.60-$2.50/sq ft | SOURCED — S11, combined into a single $2.50/sq ft per-service figure for tractability (derived) |
| P11 | USD/CAD exchange rate, current | "Bank of Canada daily exchange rate CAD USD August 2026" (WebSearch); direct fetch of the Bank of Canada FXUSDCAD RSS feed (WebFetch) | Bank of Canada, 2026-08-20: 1 USD = 1.3785 CAD | SOURCED — S12, HIGH confidence (primary central-bank data, same-day) |
| P12 | Room-by-room square footage of the flat | N/A — the flat and its floor plan are fictional; no real-world source exists to search for | The source docx's floor-plan appendix image (a generic stock "House Plan Europe" 3-bedroom plan, not a real property) gives meter dimensions per room, with a minor internal inconsistency between the labeled room dimensions and the overall envelope dimensions typical of reused stock plans | NOT A SOURCEABLE REAL-WORLD FACT — declared Modeling Assumption MA1 (case.md Appendix F). Room dimensions reproduced from the stock plan's labeled per-room figures, converted m² → ft² (1 m² = 10.764 ft², an exact mathematical conversion, not a research finding), and rounded for tractability. |
| P13 | Cross-border delivery fee (2.6% of material cost) | N/A — this is Newt's own stated business arrangement in the source scenario, not a general real-world fact | — | CASE-GIVEN scenario data (kept from source docx, same treatment as the Berisels' own stated CD$17,900 budget cap — a fictional protagonist's own business fact, not a claim requiring external sourcing) |
| P14 | Additional Helpful Resources articles (Appendix E) | Reused from source docx hyperlinks | angi.com pros-and-cons article; blog.hammondknoll.com cleaning-cost article — both still live URLs as of 2026-08-20 (confirmed via search results referencing current 2026-dated equivalent content on both domains) | KEPT as supplemental (non-load-bearing) reading resources, not added to sources[] since no factual claim/value is cited from them |

## Rejected / not used

- Angi.com's own hardwood/tile/carpet cost articles were found in search results with strong,
  specific 2026 figures, but every direct `WebFetch` attempt on angi.com returned HTTP 403
  (bot-blocked). Rather than cite a page this research pass could not actually verify by fetching
  it, Homewyse (which did fetch successfully, with a clear date) was used instead for the
  installed-cost figures, and Angi's own search-result summaries were used only as a
  cross-check that Homewyse's ranges are consistent with the wider market (they are).
- No attempt was made to source a "verbatim" 2026 fare/price/spec-sheet for the Berisels' actual
  flat, because the flat is fictional — see P12.

## Derived figures

Installation labor per square foot (Appendix B) is **derived**, not independently sourced: each
material's Homewyse installed-total (S1/S2/S3) minus its material-only figure (S4/S5/S6). Shown
in `case.json.sources[]` with `derived: false` on the two inputs and noted in each source's
`note` field; the arithmetic itself is shown in case.md Appendix B.

All flooring-cost/wear-life figures were re-verified as current for 2026 per SPEC §5's "still-
changing entity" rule — none is a stale legacy number carried over from the source docx.

Zero `{{NEEDS_SOURCE}}` placeholders remain. Every figure in case.md is either cited (`[S#]`
marker resolving to a `sources[]` row) or declared as a Modeling Assumption (Appendix F) or
case-given scenario data (the budget cap, the delivery-fee percentage — both direct carryovers
from the source docx's own fictional scenario, not real-world claims).
