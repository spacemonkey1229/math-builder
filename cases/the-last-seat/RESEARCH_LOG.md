# Research log: The Last Seat (2026-10-28)

Note: case.md was drafted with the figures already filled from fetched files (stages 2 and 3 run in one pass), so `needs_source[]` was written retrospectively with status SOURCED. No number was taken from memory; every figure was recomputed in `sensitivity_model.py`.

| Item | Searched / fetched | Result |
|---|---|---|
| Populations, seats (2020, 2010), totals | Downloaded Table C2 xlsx, parsed | S1 HIGH. 50 states + Total row; HH reproduces published seats for both censuses |
| Priority values | Downloaded 2020PriorityValues.xlsx | S2 HIGH. Rank 435 Minnesota 8th 762997.705266; rank 436 New York 27th 762994.3528429 (recomputed identically) |
| Table 1 | Downloaded; footnotes read | S3 HIGH. Apportionment population definition, 435, 2 U.S.C. 2a/2b |
| Landing page | WebFetch | S4 HIGH. April 2021, revised 2024-06-07 |
| Statute | LII 2 U.S.C. 2a | S5 HIGH. Phrase confirmed; no currency date on page |
| 435 / 1941 act | Census legislation page | S6 HIGH |
| Constitution | LII Art. I | S7 HIGH |
| 503 U.S. 442 | Justia 403; LII fetched | S8 HIGH. 9-0, 1992-03-31, Stevens; Dean-method argument |
| Li 2022 | Crossref API + doi.org | S9 MEDIUM. PS 55(4) 647-654, DOI verified. Abstract paraphrase only; full text not read; "8 of 9" NOT used. arXiv 2201.11787 removed (different paper) |
| Ernst claim | CRS R41382 PDF (congress.gov HTML 403; PDF fetched and pdftotext) | S10 MEDIUM. Footnote 44 and 37: "Lawrence R. Ernst" declaration, Massachusetts v. Mosbacher (1991); CRS author found bias evidence more persuasive. Declaration itself not read. "Laurence" corrected |
| Rejected | Search-result summaries (NAS 1929 committee, 1941 partisan motive) | Not fetched from a primary; not used |
| Context terms | Census apportionment page; Wikipedia HH and Webster pages | S11-S13; links return 200. Wikipedia HH writes n as seats already held (n(n+1)); case defines n as the seat being awarded (n(n-1)); same formula |
| Committees with census jurisdiction | not searched | Left generic ("committees with census jurisdiction") |
