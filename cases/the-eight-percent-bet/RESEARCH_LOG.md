# Research Log — The Eight-Percent Bet

Researched 2026-10-27. 17 placeholder occurrences (11 unique). **Result: 1 figure SOURCED (league minimum), the two return series SOURCED (Damodaran), 8 unique figures resolved as stated Modeling Assumptions (the fictional club's deal terms and policy mix), 0 NOT FOUND.**

| Placeholder | What was searched / fetched | Found | Outcome |
|---|---|---|---|
| Salary still owed (x2) | Fetched CBS Sports 2026 (Axisa) and CBS 2013 (Heyman); ESPN 2024 (fetched in review) | $5.9 million, 2000 season | Real-deal figure found (MEDIUM, secondary press). **Resolved as MA1**: the club is fictional and the review decided no real names appear in student text; the real source is in `real_world_basis` and FACILITATOR.md |
| Deferral interest rate (x2) | same | 8% ('precisely 8 percent', Heyman 2013; CBS 2026) | MA2 |
| Number of equal yearly payments (x2) | same | 25 years, 2011-35 | MA3 |
| Years from signing to first payment (x2) | derived: signing 2000, first payment 2011 (all-January clock) | 11 | MA4 |
| Signing year | CBS 2026 (released January 2000); ESPN ('In 2000'); sources differ on release timing | 2000 | MA4 (fixed so D5's real run lies in the Appendix B record) |
| Yearly payment in contract | CBS 2026 | $1,193,248.20 each July 1; reproduces exactly as an 8% annuity due on $5.9M grown 11 years (checked in review) | MA5 |
| Policy share in stocks (x2) / in bonds | no public source (a fictional club's policy) | NOT FOUND by construction | MA6, exit 1 (stated Modeling Assumption); a concept-stage design constant reviewed by R1a/R1b/R1c |
| League minimum in the first payment year (x2) | Fetched Baseball Prospectus (Maury Brown, 2012) | $414,000 for 2011 (table cites MLBPA annual report) | **S1, MEDIUM** |
| S&P 500 annual returns | Fetched Damodaran page and downloaded histretSP.xls (md5 unchanged since 2026-10-23); read the workbook's explanation sheet | 98 annual values 1928-2025 | **S2, HIGH** (spliced before 1957, noted) |
| 10-year Treasury bond annual returns | same | 98 annual values | **S3, HIGH** (constructed constant-maturity return, noted) |

## Rejected / not used
- The 2000 minimum salary ($200,000) is not used (payments run from 2011); the Baseball Prospectus table covers 2007-2016 only and does not show 2000. Earlier attempts to confirm 2000 via Baseball Almanac (404), FanGraphs (no such article) and Baseball-Reference (403) failed.
- Conflicts left in FACILITATOR.md: who proposed the deferral; release timing; ESPN says 'buy out', CBS says 'defer'. No primary contract text exists in the sources found.
- A second reported deferral (2004-2028) is not used.

## Structural note handed back to case-write
The Sources appendix is inserted as Appendix F, so the mandatory final "How To…" appendix moves from F to G (letter only; its content is unchanged). Background's appendix pointers were updated to match.

## Not done here (belongs to later stages)
`margin_pct` and `sensitivity_disclosure[]` (Tier 2), the facilitator anchor ladder, and `case-context` (glossary, visual).
