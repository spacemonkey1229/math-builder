# Research Log — The Multiplier Recruit

One row per figure the case needed, in the order they were tackled (load-bearing weight, not
document order).

## P01 — Is BEA RIMS II a real, currently orderable product, and at what price?

- Searched: "BEA RIMS II regional input-output multipliers 2026 how to order."
- Fetched directly: `apps.bea.gov/regional/rims/rimsii/`.
- Found: real. Current price **$520 per region** (all industries), regions are one or more
  contiguous counties or states, built on **2024 regional data + 2017 national benchmark I-O
  data**, released **May 2026**. HIGH confidence, primary federal source, fetched directly.
- Used in: Appendix C (S1), Appendix B's Modeling Assumption basis (MA1).

## P02 — Real example RIMS II final-demand multiplier values, by industry/region

- Searched multiple framings for a public table of actual RIMS II multiplier values (manufacturing
  vs. transportation/warehousing specifically). Several candidate documents were found
  (NRC filings, a California HSR EIR appendix, a WVU working paper) but none were fetchable as
  readable text — two returned HTTP 403, one returned only PDF structural metadata with no
  extractable table content.
- Success: fetched `apps.bea.gov/scb/2019/12-december/pdf/1219-rims2.pdf` — BEA's own *Survey of
  Current Business* article on the 2017 RIMS II benchmark update (Franklin, McComb, Rzeznik, Dec
  2019). This is a real, dated, primary BEA publication with actual multiplier tables.
  - **Table 7** gives real Type I final-demand multipliers for three real regions, two industries
    each. Used: Butler County, OH — miscellaneous manufacturing **1.3616**, management of
    companies (a service industry) **1.1810** (2012 national data / 2017 regional data columns).
  - **Table 1** gives real national intermediate-input shares of output: manufacturing **52.1%**,
    services **36.5%** (2012 data).
  - This article does not cover transportation/warehousing specifically — the closest real,
    fetched comparison industry in Table 7 is "management of companies," a service industry, not
    logistics. Recorded as a limitation; the case uses it only as a directional/magnitude anchor
    (manufacturing multiplier > service-sector multiplier in a county-sized region), not as
    Calder County's own transportation/warehousing figure.
- Used in: Appendix C (S2), Appendix B's Modeling Assumption basis (MA1).

## P03 — A specific, exact RIMS II multiplier or matrix for a fictional Calder County

- **NOT FOUND — cannot exist.** Calder County is fictional; BEA has no product to sell for it, and
  even a real comparable county's own table costs $520 (P01), not purchased for this exercise.
- **Exit chosen: stated Modeling Assumption (MA1)**, not a redesign — the entire pedagogical point
  of this case is a hand-built regional matrix, so redesigning away the matrix would remove the
  concept's own reason for existing. The four coefficient values were chosen so that solving the
  system reproduces output multipliers within a few hundredths of the real P02 examples, and the
  Sensitivity column in Appendix E states plainly that the exact margin depends on this choice.

## P04 — A real, published state/county per-job incentive program, to anchor the incentive-dollar figure

- Searched: state manufacturing incentive guides for 2025. Multiple real, real-dollar programs
  surfaced immediately: NC JDIG (up to $16,000/job/year, discretionary, capped), Georgia Job Tax
  Credits (up to $4,000/job/year for 5 years), Colorado ($3,000/net new job), Florida QTI ($3,000–
  $8,000/job depending on wage/sector bonuses).
- Chose Florida's QTI as the anchor for its clean, simply-stated flat base rate. Fetched directly:
  `selectflorida.org/wp-content/uploads/incentive-qualified-target-industry-tax-refund.pdf` —
  Enterprise Florida's own QTI fact sheet. Confirmed: **$3,000 per net new full-time job** (base
  rate, non-rural), **$6,000 in a rural community**, statutory reference **Section 288.106,
  Florida Statutes**. Graded MEDIUM rather than HIGH: the one-page PDF carries no visible
  publication or last-updated date, and Enterprise Florida's functions have since transferred to
  the Florida Department of Commerce, so this exact document's current status could not be
  independently confirmed within this session (the underlying statute and dollar figures are still
  the real, citable anchor).
- Used in: Appendix D, Appendix E (MA2), Appendix F (S3).

## P05 — Real County Business Patterns (CBP) baseline employment figures

- Attempted, in order: (a) the Census Bureau's own CBP API — returned an authentication error,
  requires a registered API key not available in this session; (b) `data.census.gov` CBP table
  pages — these are JavaScript-rendered single-page apps that returned no extractable tabular
  content through the fetch tool; (c) live BLS CES industry pages (`bls.gov/iag/tgs/iag48-49.htm`,
  FRED series pages for CES manufacturing/transportation-warehousing employment) — all returned
  HTTP 403; (d) a real, fetchable historical CBP national report (`cbp03-1.pdf`, "United States:
  2003," issued September 2005) was found and fetched successfully, but its detailed by-sector
  table is deep in a long PDF not practically deep-linkable within this session's tool budget, and
  2003 data would be a poor "current" baseline in any case.
- Successfully fetched a general, non-numeric description of the CBP program itself:
  `census.gov/programs-surveys/cbp.html` — confirms CBP is real, annual, county-level, and is
  exactly the tool a real analyst in Ben's role would use for baseline employment context.
- **Outcome: partial NOT FOUND.** No specific current-year CBP employment number was sourced.
  **Exit chosen: redesign, not a Modeling Assumption** — on inspection, the case's actual matrix
  math (Appendix B, D1–D5) never needed a county-wide baseline employment total as an input; it
  only needed each employer's own direct-hire count (Appendix A, MA3, already a disclosed
  scenario assumption about two fictional companies) and the technical coefficient matrix (MA1).
  A specific CBP number was never load-bearing once the case was actually built, so it was
  dropped rather than forced in. CBP's real existence and role is still cited (Appendix F, S4) as
  background context in Background, honestly scoped to "the tool Ben would use," not to a specific
  invented county figure.

## Verification pass

```
placeholders remaining: 0
citation markers with no source row: none (S1-S4 all defined; MA1-MA3 all defined and
  cross-referenced from Appendix E)
source rows never cited in text: none
LOW-confidence sources: none (S1, S2, S4 HIGH; S3 MEDIUM, none load-bearing at LOW)
```

Next step: `Run case-qa on the-multiplier-recruit.` (Not run in this session — case is left at
`status: "researched"` for a human to trigger readiness/QA next, per the task's own instruction not
to attempt publication.)
