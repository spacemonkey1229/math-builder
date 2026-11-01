# RESEARCH_LOG: The Retirement State

case-research run 2026-10-28. All data retrieved live this session; `data_pull.py` reproduces every derived figure from the saved `data/` snapshots (`python3 data_pull.py`, `--tables`, `--fetch`).

## Placeholders (22 at case-write; 0 open)

| # | Placeholder | Source | Value | Grade | Notes |
|---|---|---|---|---|---|
| P01-P03 | NCHS 2017 all-cause deaths, FL / GA / US | S1 | 203,636 / 83,098 / 2,813,503 | HIGH | Socrata API on `bi63-dtpu`, `cause_name='All causes'`. Equal to NVSR 68-9 Table 12 (printed June 24, 2019). |
| P04-P06 | Census July 1, 2017 residents, FL / GA / US | S2 | 20,963,613 / 10,410,330 / 324,985,539 | HIGH | `nst-est2019-alldata.csv`, POPESTIMATE2017. |
| P07-P09 | NCHS 2017 age-adjusted rate, FL / GA / US | S1 | 672.1 / 793.7 / 731.9 | HIGH | Matches Table 12 exactly for these three. |
| P10-P12 | Residents aged 65+, July 1, 2017 | S3 | 4,209,641 / 1,406,519 / 50,793,923 | MEDIUM | Derived from `sc-est2018-alldata6.csv` (Vintage 2018), summed over SEX=0, ORIGIN=0, all six RACE codes, AGE>=65. U.S. = sum of 51 jurisdictions. |
| P13-P15 | Total residents, same series | S3 | 20,976,812 / 10,413,055 / 325,147,121 | MEDIUM | Same file, all ages. Within 0.06% of S2 for Florida. |
| P16-P18 | Share aged 65+ | S3 | 20.1% / 13.5% / 15.6% | MEDIUM | Derived: 20.07 / 13.51 / 15.62. |
| P19 | Rank of FL and GA by 65+ share among 51 | S3 | Florida 1st; Georgia 47th highest (5th lowest) | MEDIUM | Maine 20.02% is second. |
| P20 | Pair counts | S5 | 1,275 pairs; 280 reverse; 241 with both gaps under 20% (gap / higher) | MEDIUM | Derived from S1 and S2, 2017, 51 jurisdictions. |
| P21 | Appendix C table | S5 + S1 | 49 derived crude rates (1 dp) + 51 age-adjusted rates | MEDIUM | `data_pull.py --tables` writes `data/appendix_c.md`. Florida/Georgia crude cells are left for D1. |
| P22 | Appendix D table | S5 + S1 | 2010-2016 derived crude + aadr, FL and GA | MEDIUM | `data/appendix_d.md`. The 2017 row is the student's D1. |

The ten rows above are in case.md as figures with `[S#]` markers; `needs_source[]` statuses are all SOURCED. No NOT FOUND, no assumption forced by missing data, no DROPPED figure. (Assumptions MA1-MA5 are scenario choices, not substitutes for missing data.)

## What was searched and rejected

- **ACS S0101 (65+ share), the sheet's preferred source.** `api.census.gov/data/2017/acs/acs1/subject?get=...&for=state:*` returns HTTP 302 to `missing_key.html` (a key is required); the variables list loads without a key, which confirmed `S0101_C02_030E` is "Percent 65 years and over". Rejected for lack of a key; not guessed.
- **Census age files named in the concept (Vintage 2019 `asrh/` paths).** `.../2010-2019/state/asrh/sc-est2019-agesex-civ.csv`, `scprc-est2019-18+pop-res.csv`, `sc-est2019-alldata6.csv` all HTTP 404. `.../2010-2018/state/asrh/sc-est2018-alldata6.csv` and `sc-est2018-agesex-civ.csv` resolve; the first (resident basis, includes armed forces) was used so the age counts and the Appendix A denominators are both resident populations. The two files give the same 65+ counts for Florida and Georgia (4,209,641; 1,406,519). Cost: a different vintage from S2, disclosed in Appendix B.
- **CDC WONDER API** (age-specific death counts): not retried; three POSTs returned HTTP 500 at concept stage. Not needed: the case uses the all-ages rows only.
- **NCHS-published crude rates (NVSR 68-9, Table 12)** were found and parsed for all 51 jurisdictions. They are not used as the case's crude rates because the instruction is to derive them from deaths / Census July 1 estimate; they close the concept sheet's open item "agreement of derived crude rates with WONDER at the rounding level". Result: Florida 970.4 vs derived 971.4 (0.10%), Georgia 796.8 vs 798.2 (0.18%), U.S. 863.8 vs 865.7 (0.22%); across 51 jurisdictions the mean absolute difference is 0.22% and the largest is 1.35% (New Jersey), because NCHS divides by its own July 1, 2017 estimate (2010-census series as of 2017) and the case uses Census Vintage 2019. Under NCHS's printed crude rates Florida's margin is 17.9% and its crude rank 18th. Table 12's counts and age-adjusted rates equal the Socrata file for all 51 jurisdictions and the U.S. except New Hampshire (717.3 in the file, 717.2 printed) and Wyoming (714.6 vs 714.5).
- **Fixed the concept sheet's false claim.** "Florida-Georgia is the largest-population pair [that reverses with both margins under 20%]" is wrong. Among the nine states with at least 10 million residents (CA, FL, GA, IL, NY, NC, OH, PA, TX), reversing pairs with both margins under 20% include FL-GA, NY-TX (11.7 / 15.2), FL-IL (11.6 / 7.2), IL-TX (18.5 / 1.6), PA-OH (0.0 / 8.5), GA-IL (7.0 / 8.8), FL-NC (6.6 / 14.4), GA-NC (12.0 / 1.0), NC-PA (14.5 / 1.1); by combined population the first such pair is New York-Texas (47.9 million). The rule printed in Appendix E replaces it: of 280 reversing pairs, 241 have both gaps under 20% of the higher rate, and Florida-Georgia is the one whose **smaller** gap is largest (15.3%). Next on the list: Alaska-California 12.5%, Florida-Nevada 12.2%, Colorado-Hawaii 11.8%, New York-Texas 11.7%. Two pairs have a larger smaller-gap but one gap over 20% (Alaska-Hawaii 17.5%, Hawaii-Utah 16.5%). The rule was written after the pair was proposed, which FACILITATOR.md says plainly.
- **Raw counts.** Florida's deaths exceed Georgia's by 59.2% of Florida's count (203,636 vs 83,098; 2.45x). The case declares counts out of scope in Background and Appendix E, with the reason that a count tracks population (2.01x), and shows the counts in Appendix A only as the crude rate's numerator.
- **"People retire there."** Not asserted. Appendix B shows Census 65+ counts and shares (Florida 20.1%, highest of 51) and says the counts do not give reasons. The title keeps the concept's phrase; the text does not claim a cause.
- **Robustness years.** The reversal holds in every year 2010-2017. Crude margins (gap / higher) are 20.4%, 20.4%, 19.9%, 18.7%, 18.5%, 17.2%, 17.4%, 17.8%; age-adjusted 17.1%, 17.0%, 17.2%, 17.7%, 17.4%, 18.0%, 16.7%, 15.3%. 2010 and 2011 are barely over the 20% line on the crude basis; the concept's "not a one-year artifact" claim stands for the reversal, not for the margin. Recorded in FACILITATOR.md and `case.json.derived.years`.

## As-of dates and what could not be confirmed

- NCHS `bi63-dtpu`: rows updated 2019-10-24 (metadata `rowsUpdatedAt` 1571926785); licence "Public Domain U.S. Government" (usa.gov/government-works). Series ends at 2017; the 2018+ rows are not in this dataset, so no post-2017 NCHS number could appear before the Twist.
- Census `nst-est2019-alldata.csv` is the Vintage 2019 series. **UNVERIFIED:** the release month (believed December 2019). The scenario date (January 2020) was chosen to fall after it; if the release was later, MA2 should be moved. Census terms of use were not separately read; Census data are U.S. government works.
- NVSR 68-9 print date June 24, 2019, read from the PDF header.
- Twist (S9): `mpx5-t7tu`, `data_as_of` 2026-09-17, last data period ending 2026-09-12; licence Public Domain U.S. Government. Provisional; CDC's own description says counts should not be compared across states because timeliness varies. Used only as rates, only in FACILITATOR.md and case.json.
- 2010 crude rates: Census's July 1, 2010 estimate is used for the denominator; NCHS's published 2010 rate uses the April 1, 2010 census count, so students' 2010 crude rates differ slightly from NCHS's own (not shown to students).

## Confirmed this session / Unverified

CONFIRMED: every number in Appendices A-D, the five-number summaries, the pair counts and rule, the rank statements, the blended-index tie weight, and the Twist rows (all recomputed in python from the saved snapshots); 8 context and source URLs return HTTP 200 (see below). UNVERIFIED: Vintage 2019 release month; whether CDC will keep `mpx5-t7tu` rows unrevised.

URLs fetched and resolving on 2026-10-28: S1 data.cdc.gov bi63-dtpu (200, canonical `National-Center-for-Health-Statistics/NCHS-Leading-Causes-of-Death-United-States/bi63-dtpu`), S2 Census nst-est2019-alldata.csv (200), S3 sc-est2018-alldata6.csv (200), S4 nvsr68_09-508.pdf (200), S6 statnt20.pdf (200), S7 cdc.gov/nchs/about/index.htm (200), S8 census.gov/programs-surveys/popest.html (200), S9 data.cdc.gov mpx5-t7tu (200).

## Next

`case-context` pass (done in the same run): `context_glossary[]` has five terms with sourced links; case.md defines them in plain words. Run `case-readiness` Tier 1 and Tier 2.
