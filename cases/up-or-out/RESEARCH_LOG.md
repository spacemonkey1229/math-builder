# Research log — Up or Out (2026-10-28)

Data pull: NYC Open Data dataset ic3t-wcy2 (DOB Job Application Filings) through the SODA API, 2026-10-28 05:24 UTC, `rowsUpdatedAt` 2026-10-27 21:56 UTC. `data_pull.py` reproduces the pull and cleaning (71,003 raw rows -> 3,474 clean; 1,424 vertical, 2,050 horizontal), matching the concept sheet's chain exactly. Date format in the API is MM/DD/YYYY (filter on the last four characters, not the first).

| Item | What was searched / fetched | Result |
|---|---|---|
| Cost and size data (S1, S6-S9) | API pull above; medians, pooled, raw values, totals, story counts recomputed in python | Reproduced the concept's 9-size medians exactly (e.g. 400: 311.2 / 364.2). New expected-cost metric computed fresh |
| Field meaning (S2) | Downloaded the dataset's attached data dictionary xlsx and read sharedStrings | Initial Cost = "Estimated Job Cost on the PW1"; Enlargement SQ Footage = "the Additional Square Footage added by the construction enlargement, if any". Closes the concept's open item 1 (sq ft is added floor area) |
| Licence / terms (S3) | API metadata `license` is null; nyc.gov/html/data/terms.html now 404; portal overview pages 403 to automated fetch; read nyc.gov Terms of Use (site-wide, no data clause); read Admin Code §23-502(d) via the NYC Laws mirror | Quoted the code. The dataset-specific portal terms were not read directly: UNVERIFIED, disclosed in S3 |
| "Enlargement" (S4) | zr.planning.nyc.gov Article I Chapter 2 | Verbatim definition found. The old nyc.gov glossary page redirects (rejected) |
| Contractor cost-per-sq-ft guides | Not fetched | Rejected: no provenance; the case uses only the filings |
| Second independent cost source | Concept sheet found none (Census permit files carry units only) | NOT FOUND; disclosed: costs are declared estimates (MA5, MEDIUM grade) |
| Why the legacy dataset stops after 2020 | Dataset description says it excludes DOB NOW jobs | Consistent with the description; DOB did not state it as the cause: stated as a caution only |

Design findings (concept 17.0% headline): only holds at 395-410 sq ft; tuning. Replaced by an unknown-size design: expected cost over the architect's 250-450 range gives a 3.2% margin; range grid, robustness rows, bootstrap and the 300 sq ft twist are in FACILITATOR.md. Stories-up check: only 28% of vertical filings of 200-299 sq ft report added stories (vs 58-60% above 300), but the small-size cost cliff persists when only story-increasing filings are used (n = 19-35), so the scope-artifact explanation is only partly supported.

Zero placeholders remain open: S1-S4 sourced, S5/S10 context, S6-S9 derived, MA1-MA5 stated assumptions.
