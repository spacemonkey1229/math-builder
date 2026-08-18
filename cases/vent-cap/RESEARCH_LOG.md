# Research Log — Vent Cap

`case-research`, 2026-08-12.

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| 1 | Real steel sheet gauge/thickness reference | "steel sheet metal price per square foot 16 gauge 2026" (led to sheetmetal.me) | sheetmetal.me gauge chart: 16ga = 0.0598in, standard 36in/48in widths | SOURCED — S1 (HIGH) |
| 2 | Real 16-gauge, 4x8 sheet price | "16 gauge steel sheet 4x8 price per sheet metal supplier" | Several suppliers listed ($60-$100 range in search snippets, not independently fetched); direct-fetched M&K Metal Co. product page: $68.39/sheet | SOURCED — S3 (MEDIUM, page itself says "sample pricing... call to confirm"). Rejected using the unfetched search-snippet range per the never-cite-an-unfetched-URL rule. |
| 3 | Real welding/seam labor cost | "sheet metal welding labor cost per linear foot or per seam" | tzrmetal.com (direct-fetched): "$20 to $50" for a simple tack weld/short seam (retail service-call price) | SOURCED as context — S4 (HIGH). NOT used directly as the per-seam production cost -- see #4. |
| 4 | A defensible production-scale (not retail) per-seam labor cost | "sheet metal fabrication shop labor rate per hour production 2026" | PayScale (direct-fetched): $26.28/hr average direct wage for a sheet metal worker (distinct from $50-130/hr fully-loaded shop billing rates, which include overhead/profit inappropriate for a marginal-cost estimate) | SOURCED — S5 (HIGH). Derived MA1 ($3.00/seam) from S5's wage x an estimated ~6.85 min/seam production time (no public source for this specific time; stated as the assumption's basis). |
| 5 | Whether a public database of real factory nesting results exists | Domain data (`domains.json`) already notes none does | ESICUP cutting & packing datasets confirmed live (direct-fetched context, not part-specific data) | S6 (HIGH, cited only to establish irregular nesting is a real, studied problem class). Caps-per-sheet figures (MA2) declared as case-authored, per the domain's own explicit guidance. |

## Margin resolution

First design attempt used a flat retail weld cost ($20-50/seam per S4) directly, which made labor
so dominant that Option A (more panels, more seams) could never be cost-competitive at any
realistic batch size — the material-nesting story the domain is actually about became irrelevant.
Redesigned the labor cost as a genuine production-marginal-cost derivation (wage x time, not a
retail quote) at $3.00/seam, and picked a batch size (70 units) where both the material line
(driven by sheets-needed rounding) and the labor line move by comparable dollar amounts. Final
margin: 11.98%, confirmed stable under a ±50% flex of the one FLEX-eligible dial (weld_cost_per_
seam: 4.80%-15.39%, Option B cheaper throughout).

## Next step

Run `case-readiness` Tier 2 (six simulated-play probes) on `vent-cap`.
