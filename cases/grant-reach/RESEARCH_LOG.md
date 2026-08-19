# Research Log — Grant Reach

One row per figure needed. This case was authored and researched in a single combined pass
(case-write + case-research), so placeholders were resolved directly into `case.md` rather than
staged as `{{NEEDS_SOURCE}}` tokens first; this log reconstructs what was searched, found, and
rejected for each.

| # | Needed figure | Searched | Found | Outcome |
|---|---|---|---|---|
| P01/P02 | National Pell Grant recipient rate and average award | "Federal Pell Grant End-of-Year Report 2023-2024 percent of undergraduates" (WebSearch); attempted direct fetch of studentaid.gov/data-center/student/title-iv for the primary EOY XLS — **timed out** after 60s and was not retried a third time. | EducationData.org's synthesis of Dept. of Education / NCES / Federal Student Aid data: 32.4% of undergraduates awarded Pell in AY2023-24, average award $5,300. | SOURCED, confidence MEDIUM (aggregator, not the primary EOY report itself — flagged in case.json note for future upgrade to HIGH if the primary XLS is fetched later). |
| P03 | State grant agency's published income eligibility table | Searched and confirmed California as the chosen real state; tried direct WebFetch of the CSAC PDF (405 error), then successfully retrieved full table text via an r.jina.ai reader-proxy fetch of the same PDF. | 2025-26 Cal Grant A/C and B income ceilings by household size (Table A-1). | SOURCED, confidence HIGH — content matches the primary CSAC document; two independent search-synthesis passes agreed with the proxy-fetched table before it was used. |
| P04/P05 | Statewide state-grant recipient count and total state undergraduate enrollment (used to build Modeling Assumption MA2's ratio) | "California Student Aid Commission Cal Grant number of recipients 2024-25"; "California total undergraduate enrollment 2024 total students". | LAO: 453,000 Cal Grant recipients, AY2024-25 (HIGH — CA Legislative Analyst's Office, a primary state fiscal body). Total CA undergrad enrollment 2,440,631 (MEDIUM — aggregator page summing NCES/state segment data; individual segment figures it cited — 1,101,584 CCC / 339,946 CSU / 206,588 UC FTE plus private-sector estimates — are internally consistent with the total, which is why it was accepted at MEDIUM rather than rejected). | Both SOURCED; used only inside Modeling Assumption MA2's stated basis, not presented as a per-university figure. |
| P06 | Cal Grant B Access Award amount | "Cal Grant B award amount 2025-26 access award tuition award dollar amount CSAC"; direct WebFetch of csac.ca.gov/post/what-are-cal-grant-award-amounts returned 405/403 both directly and via the r.jina.ai proxy (the proxy returned a login-wall page, not the article). | $1,648 first-year Access Award, 2025-26, from a search-engine synthesis of the CSAC page. | SOURCED, confidence MEDIUM only, and flagged in case.json as needing direct re-verification against csac.ca.gov before being treated as fully confirmed — this figure is used only in Appendix E (context), never in a load-bearing calculation, so it was accepted at MEDIUM rather than blocking the case. |
| P07 | USPS commercial mail per-piece rate | "USPS commercial Marketing Mail letter price per piece 2025 2026"; then a direct WebFetch of the primary USPS page pe.usps.com/text/dmm300/notice123.htm (the PDF version at pe.usps.com/resources/PriceChange/... returned binary/unparseable content on first attempt). | 5-Digit $0.395 / 3-Digit-SCF $0.435 / Mixed AADC $0.467, commercial automation Letters, effective 2026-07-12 — confirmed as the currently-effective price list given the case's 2026-08-18 authoring date. | SOURCED, confidence HIGH — primary USPS source, directly fetched and readable. |
| P08 | Renewal-rate-by-outreach-method (the figure the concept sheet flagged in advance as likely needing a Modeling Assumption) | "FAFSA renewal reminder mailer postcard effect on renewal rate study higher education"; found and fetched the GSA Office of Evaluation Sciences project page directly. | Real 2017 RCT: emailed FAFSA reminders raised submission-within-20-days from 4.34% to 7.77% (79% relative increase); Pell-specific messaging was the most effective variant tested. | **NOT transferable as a direct figure** — different channel (email vs. this case's physical mail) and different outcome window (20-day submission vs. full-cycle renewal). Per case-research's NOT FOUND protocol, this became exit 1: a **stated Modeling Assumption** (MA4 baseline 55%, MA5 with-reminder 70%), anchored to the study's direction and rough scale rather than its literal numbers, with the mismatch explicitly disclosed in Appendix D of case.md. |
| MA1, MA2 (population share), MA3, MA6 | Cascade State's own aid-renewal population size, the exact share of it that is state-eligible, the Pell/state overlap fraction, and the office's discretionary mailing budget | Searched for any public per-institution dual-eligibility roster or overlap statistic — none exists, as expected (no real university publishes a Pell/state-grant overlap count, and Cascade State is itself a fictional university, per this case's design). | No public figure exists at this granularity for any real, named institution. | Exit 1 (stated Modeling Assumption) for all four, each anchored to a real statewide/national rate where one was available (MA2 to the real CA statewide Cal Grant ratio) and to qualitative real-world reasoning where no rate exists (MA1, MA3, MA6) — see case.json's `modeling_assumptions[]` and case.md's Modeling Assumptions block for the full basis of each. |

## Rejections worth recording (so nobody re-runs these searches)

- The primary Federal Pell Grant Program End-of-Year Report (the exact document named in the
  concept sheet) was never directly retrieved this session — `studentaid.gov/data-center/student`
  and `studentaid.gov/data-center/student/title-iv` were searched and one fetch attempt timed out.
  A future pass should retry that fetch (or search `data.ed.gov` directly for the dataset) to
  upgrade S1/S2 from MEDIUM to HIGH.
- A secondary financial-aid blog (collegeaidguide.com) reported Cal Grant A family-of-four income
  ceiling as $72,100 and Cal Grant B as $37,100 — roughly half the real CSAC figures ($135,900 and
  $71,500). This was caught by cross-checking against a direct proxy-fetch of the primary CSAC PDF
  and was **rejected** rather than used. Treat any Cal Grant income figure from a financial-aid
  blog as unverified until checked against csac.ca.gov directly.
- Direct WebFetch of multiple csac.ca.gov pages returned HTTP 405 (and once 403 via a reader
  proxy). The PDF documents were successfully retrieved through an r.jina.ai reader-proxy fetch of
  the same URL; the "post"-type CSAC articles (not PDFs) were not successfully retrieved by any
  method tried this session.

## Next step

Run `case-qa` on `grant-reach`.
