# Research Log — Protein Per Dollar (case-research, 2026-10-28)

Fetched 2026-10-28. Margin convention: gap divided by the winner's value. The order is placed in mid-September 2024 (changed from the concept sheet's "August", see Decision-date fix).

| P | Placeholder | Searched / fetched | Found | Status |
|---|---|---|---|---|
| P01 | Monthly budget, USD | n/a (constructed pantry) | $12,000 | ASSUMPTION MA1 |
| P02 | Quarterly budget, USD | derived | $36,000 (3 x MA1) | ASSUMPTION (derived) |
| P03 | Egg price Aug 2024 | curl `https://fred.stlouisfed.org/graph/fredgraph.csv?id=APU0000708111` (HTTP 200, 9,563 bytes); WebFetch of the FRED series page for title and notes | $3.204 per dozen | SOURCED S1, HIGH |
| P04 | Chicken price Aug 2024 | same method, `APU0000FF1101` (HTTP 200, 4,259 bytes) | $3.952 per pound | SOURCED S2, HIGH |
| P05 | Dry-bean price Aug 2024 | same method, `APU0000714233` (HTTP 200, 6,391 bytes) | $1.711 per pound | SOURCED S3, HIGH |
| P06 | Grams per pound | FRED series title for APU0000FF1101 ("Cost per Pound/453.6 Grams") | 453.6 | SOURCED S2 |
| P07 | Egg edible weight | USDA FoodData Central: `fdc.nal.usda.gov` did not resolve (WebFetch ENOTFOUND; curl "could not resolve host"); API `api.nal.usda.gov` returned HTTP 429 OVER_RATE_LIMIT (DEMO_KEY, Retry-After about 66,895 s) | 50 g (earlier read, not re-confirmed) | ASSUMPTION MA3, UNVERIFIED |
| P08 | Egg protein per 100 g | same; a web search found third-party mirrors (getfoodfacts.com, fitnessvolt.com) listing 12.56 for FDC id 171287. Not the primary record, not cited | 12.56 | ASSUMPTION MA4, UNVERIFIED |
| P09 | Chicken protein per 100 g | same; no mirror consulted | 22.5 (FDC id unconfirmed; one reviewer pointed to 2646170) | ASSUMPTION MA5, UNVERIFIED |
| P10 | Dry-bean protein per 100 g | same | 21.6 (FDC 173734 raw black beans; 173735 is cooked and wrong) | ASSUMPTION MA6, UNVERIFIED (used only in D6) |
| P11 | Egg monthly history | parsed from the S1 CSV; 224 values Jan 2006 to Aug 2024 | complete, no blanks | SOURCED S1 |
| P12 | Chicken monthly history | parsed from the S2 CSV; 224 values in the window | complete in window (the series has 248 observations Jan 2006 to Sep 2026 because Oct 2025 is blank) | SOURCED S2 |

## Rejected or not used
- BLS direct fetch: `https://www.bls.gov/cpi/factsheets/average-prices.htm` returns HTTP 403 to curl but loaded in WebFetch; used as S4 (MEDIUM, no figure).
- FRED series pages timed out under curl but loaded in WebFetch; the CSV endpoint is the cited data URL.
- Third-party nutrition mirrors: not cited (not primary, one site had implausible metadata).
- Khan Academy links: return a bot "Client Challenge" page to curl, so their content could not be confirmed; the math glossary uses mathsisfun.com pages whose titles were confirmed (HTTP 200).

## Decision-date fix
The concept sheet placed the order on a Friday in August 2024 yet planned with the August 2024 average, which BLS has not published in August. The case places the order in mid-September 2024 for an October-December quarter, so August 2024 is the latest published month. The post-decision twist therefore covers Oct-Dec 2024 (and Jan-Mar 2025 as an extension), not Sep-Nov.

## Contested / flagged
BLS says average prices are for the price level, not price change over time, and are retail rather than supplier prices. The case declares this as MA2 and S4.

## Recomputation (python, derive.py)
Aug 2024: eggs 23.52 g/$ (75.36 g per dozen / $3.204), chicken 25.82 g/$ (102.06 g per lb / $3.952). Margin (25.82 - 23.52) / 25.82 = 8.92%; gap/loser 9.80%. Break-evens: eggs $2.918 (-8.92%), chicken $4.339 (+9.80%). Quarter on $36,000: 846,742 g vs 929,696 g, diff 82,955 g. History: 224 months, eggs lead 209, chicken 15 (Jun-Dec 2015 = 7, Nov 2022-Apr 2023 = 6, Jul-Aug 2024 = 2). Chicken price range Jun 2023-Aug 2024: $3.946 (Jul 2024) to $4.229 (Sep 2023). June 2024 eggs ahead by 9.12% (gap/winner). Twist quarter: eggs 734,290 g, chicken 907,135 g.

## Remaining
Re-confirm MA3 to MA6 against USDA FoodData Central with a registered api.data.gov key (and fix the chicken FDC id); then remove the UNVERIFIED labels or update the values.
