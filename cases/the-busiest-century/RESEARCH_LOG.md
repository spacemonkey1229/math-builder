# Research Log — The Busiest Century

Stage 3 (case-research), 2026-10-28. Every figure in `case.md` Appendices B–D is **derived** (not quoted) from S1 and S2 by the case author; there were no `{{NEEDS_SOURCE}}` placeholders left to fill after case-write, because the numbers are computed, not looked up. This log records what was fetched, what was recomputed, and what could not be verified.

## Fetches and checks

| Item | What was done | Result |
|---|---|---|
| p3k14c release 2025.07 (S1) | Zenodo API `records/16394072` read; zip (35,892,370 bytes) downloaded fresh; md5 compared with the record (5f6a7fba5e1999e68fa8871211a42452) | match; version 2025.07, published 2025-07-24; newest of 5 versions on the concept record |
| Licence of the data | README.md in the zip, "Licenses" section | "Data: CC-0 ... attribution requested in reuse"; code GPLv3; text CC-BY-4.0. The Zenodo record's own `license` field was empty (API); the README is the authority used |
| IntCal20 curve (S2) | `https://intcal.org/curves/intcal20.14c` downloaded (9,512 lines, md5 39ee5217bd24b67badefe1622a4a7cab); header cites Reimer et al. 2020 | Crossref confirms Radiocarbon 62(4):725–757, doi 10.1017/RDC.2020.41, licence CC BY 4.0 for the paper. **No licence statement on intcal.org/curves.html or intcal.org/.** Case reproduces no curve values |
| Bird et al. 2022 (S3), Crema and Bevan 2021 (S4) | Crossref metadata and abstracts read | volume/issue/pages confirmed; both CC BY 4.0 |
| Crema and Bevan claim | Abstract only | Supports "SPD is a standard method for large date sets with stated assumptions and limitations"; the full paper was not read |
| Chaco NPS page (S6) | Fetched; quoted sentences confirmed | "Their descendants are the modern Southwest Indians"; "Pueblo descendants say that Chaco was a special gathering place...". Mesa Verde NPS People page also fetched (Pueblo and Hopi people are the direct descendants of those who built and lived in the communities at Mesa Verde and surrounding sites). Used only for the living-communities sentence |
| 54 U.S.C. § 307103 (S7) | Cornell LII text fetched | Subsection (a) confirmed: withhold information about location, character or ownership of a historic property if the Secretary and the agency determine disclosure may cause invasion of privacy, risk harm, or impede traditional religious use. The statute binds federal agencies and grantee officials; the case follows its spirit voluntarily and says "federal law lets agencies withhold" |
| Glossary links (S8–S11) | HTTP status checked | all 200 (Wikipedia pages); Britannica returned 403 and is not used |

## Recompute (independent of the concept sheet)

The concept sheet's NM numbers (3,678 dates; 870 sites) reproduced exactly with the same numeric rules (NM rows with SiteID; 100 < age < 8000; 0 < error < 300). Differences from the concept sheet, all deliberate: (1) bone and teeth rows left out (62 samples: 61 bone, 1 teeth; the brief's 86 BONE rows is the count across ALL New Mexico rows, 25 of which fall outside the numeric rules), leaving 3,616 dates and 863 sites; (2) the primary convention is the summed probability on a 1-calendar-year grid, not the per-date median; (3) the sites reading is the expected number of sites with at least one date in the century.

Convention results (all computed on the 3,616 dates; centuries from 0 unless stated):

| Cut | Dates winner | Sites winner |
|---|---|---|
| Summed probability, from 0 | 700–799 (272.0) | 1200–1299 (152.5) |
| Summed probability, shifted 50 | 650–749 (272.0) | 1150–1249 (147.4) |
| Median year | 700–799 (286) | 1200–1299 (154) |
| Mean year | 800–899 (274) | 1100–1199 (156) |
| Mode year | 1100–1199 (353) | 1100–1199 (198) |

Per-reading margins with the 62 bone/teeth samples kept: Dates 280.0 vs 246.1 (12.1%); Sites 153.1 vs 129.2 (15.6%) — the brief's 12.1% reproduces in this variant. 2-year grid check on the summed probability: Dates winner 700–799 (272.5) unchanged, so the SPD split does not depend on the 1-year grid (the median convention on a 2-year grid does, per the review).

Other checks run (see `data/check_figures.py`): heaviest-site and 5-heaviest-site removal; sites with 5+ and 10+ dates; cluster bootstrap over sites (2,000 resamples, seed 20261028): P(Dates 700–799 > 1200–1299) = 0.710, P(Sites 1200–1299 > 700–799) = 0.978. The extract `data/derived_dates_by_century.csv` reproduces Appendix B to within 0.001.

## NOT FOUND / UNVERIFIED

- **IntCal20 licence text** — not on the intcal.org pages. Exit chosen: reproduce no curve values; cite the paper; flagged for the owner.
- **Whether any specific New Mexico Pueblo or Native organization will review** — nobody has been approached. FACILITATOR.md and `case.json.community_review` record the review as NOT DONE.
- **Site delineation in the database** — the `SiteID` is the database's, not independently verified; whether some "sites" are lumps of several places or one place split into several IDs is unknown. This affects the Sites reading only; flagged in the Sites argument as M4 and in Socratic question 2.
- **Whether the lead of one site (137 dates) reflects an intensively excavated place** — not investigated on purpose (identity withheld, NHPA 304 spirit).
- **Full text of Crema and Bevan 2021 and Bird et al. 2022** — abstracts only.

## Rejected

- Using the per-date median calibration as the primary convention (reviewers: reproduces the split only on a 1-year grid).
- Mode as the primary convention (kills the split; shown in Appendix D instead).
- Britannica as a glossary link (HTTP 403).
- Publishing site IDs, names or coordinates, even the fuzzed ones.
