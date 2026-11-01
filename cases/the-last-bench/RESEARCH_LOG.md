# RESEARCH LOG: The Last Bench

Researched 2026-10-28. 52 placeholders (36 distinct tokens): 5 SOURCED (USGS), 47 ASSUMPTION (scenario, in Appendix C or the Appendix B/D tables), 0 DROPPED, 0 NOT FOUND left open.

| Placeholder group | Searched / fetched | Result |
|---|---|---|
| Gold price 2021-2024 (4) | Fetched https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-gold.pdf with curl (HTTP 200, 138,864 bytes, sha256 c2fef62f...) and parsed with pdftotext. Salient Statistics row "Price, dollars per troy ounce": 1,801 / 1,802 / 1,945 / 2,388 / 3,300 (2021-2025e). Footnote 5: Engelhard's average quotation for the year; the 2025 value was estimated by USGS from January-November data. Publication page https://pubs.usgs.gov/publication/mcs2026 (HTTP 200): published February 06, 2026; versions 1.0 Feb, 1.1 Mar, 1.2 Apr, 1.3 May 2026. PDF footer: "February 2026". | SOURCED, HIGH (S1). Only 2021-2024 used in case.md; the 2025e value (3,300) is the Twist, FACILITATOR.md only. NOTE: the concept sheet said January 2026; the review brief corrected it to February 2026, which matches. The footnote that the fetched PDF may differ from v1.0 is recorded; values were identical to those the concept sheet logged on 2026-10-28. |
| Troy ounces per tonne (1) | Same PDF, footnote 1: "One metric ton (1,000 kilograms) = 32,150.7 troy ounces." Cross-check: Wikipedia Troy weight, troy ounce = 31.1034768 g; 1e6 g / 32,150.7 = 31.1035 g. | SOURCED, HIGH (S1), cross-checked MEDIUM (S6). |
| Geometry, density, pipe (17) | No real mine is represented; searched for nothing to cite. Rim radii and cone heights are derived from the assumed depths, floor radius and 42-degree wall by right-triangle trigonometry (recomputed in python, `sensitivity_model.py`). | ASSUMPTION (MA1), visible block, all labelled. |
| Reserve, grade, recovery, costs, capital, throughput, discount (12) | Considered citing real mine technical reports (NI 43-101 / S-K 1300): not fetched; any single real mine would turn the scenario into a claim about that mine. Considered BLS mining wages for the stake: not used (wage is not needed; Hero may research it). | ASSUMPTION (MA2-MA5, MA7). Not sourced, not presented as sourced. |
| Crew, town (2) | No real employment data used on purpose; a real town would make the stake a claim about real people. | ASSUMPTION (Appendix D, loudly labelled scenario input). |
| Context terms (6) | Fetched Wikipedia (Open-pit mining, Strip ratio, Ore grade, Troy weight): all HTTP 200, text confirms definitions. Fetched Hacettepe MAD455 notes (HTTP 200, 11 MB PDF): defines bench, stripping ratio, cutoff stripping ratio. Fetched Datamine Studio NPVS "About Pushbacks" (HTTP 200): "a 'pushback' refers to a designated zone representing an area to be mined as a single operation". | SOURCED, MEDIUM (S2-S6). |

## Rejected
- dataminesoftware.com/?p=45837 (404 on fetch), k-mine.com page (no pushback definition found on fetch), srk.com event page (HTTP 403): not cited.
- NIST Handbook 44 appendix URL (404): not cited.
- Search-result summaries about pushback vs cutback differ by source; recorded as a caveat in S3.

## Recomputation
All numbers recomputed in `sensitivity_model.py` (python): shell 146.55 Mt (exact) / 146.56 Mt using the rounded givens in Appendix B; pipe 9.606 Mt; stripping ratio 14.26; A 914.1, B 852.1 (2024); break-even 2,616.1 USD/oz; mid-period discounted 793.8 / 747.7 (2024) and 1,354.0 / 1,449.8 (2025e). The concept sheet's discounted values (794.0 / 747.9 and 1,354.3 / 1,450.2) differ by 0.2-0.4 because of a slightly different part-year treatment; winners and margins agree (A 5.8%, B 6.6%).
