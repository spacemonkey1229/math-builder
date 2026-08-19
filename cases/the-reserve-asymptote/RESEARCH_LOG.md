# RESEARCH_LOG.md — The Reserve Asymptote

One row per placeholder: what was searched, what was found or rejected, and why.

---

## P01 — Published U.S. life table qx values, ages 90-100+, most recent year

**Searched:** "CDC National Vital Statistics Reports United States Life Tables most recent year";
followed to NVSR Vol. 74, No. 2 ("United States Life Tables, 2022," published 2025-04-08).

**Attempted:** Direct WebFetch of the CDC PDF (cdc.gov/nchs/data/nvsr/nvsr74/nvsr74-02.pdf) —
**rejected**, HTTP 403 (cdc.gov blocks the fetch tool directly).

**Attempted:** WebFetch of the NCBI Bookshelf mirror (ncbi.nlm.nih.gov/books/NBK614547/) — this
worked for narrative content (title, publication date, life-expectancy summary figures, and
methodology notes) but the summarizing model could not reliably extract the full numeric Table 1
from the rendered page; it correctly reported a "Table01.xlsx" spreadsheet link instead of
guessing at numbers.

**Resolved:** Downloaded `Table01.xlsx` directly via `curl` from
`ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/74-02/Table01.xlsx` and parsed it with
`openpyxl` — this is the report's own published data file, not a third-party mirror or a search
summary. Every value in case.md Appendix C (qx for ages 90-99, and the 100-and-over open-group
closure at qx = 1.000000) was read directly out of that spreadsheet's cells. **Confidence: HIGH.**

---

## P02 — Published SOA methodology reference for annuity reserve pricing

**Searched:** "SOA 2012 Individual Annuity Mortality IAM Basic Table select period years."

**Found:** "2012 Individual Annuity Reserving Report & Table" (SOA Payout Annuity Table Team,
2011-09-28), prepared at the request of NAIC's Life Actuarial Task Force. Confirmed via WebFetch
of the SOA resource page (soa.org/resources/experience-studies/2011/2012-ind-annuity-reserving-rpt/).
**Confidence: HIGH.** Used only for background/context (Appendix E) — no numeric figures pulled
from it.

**Also searched:** "SOA study note reserves annuity valuation methodology exam FAM ILA public
pdf" looking for a more granular methodology primer. Nothing more specific and clearly public
surfaced beyond exam-prep study guides (paywalled/commercial), which were **rejected** as not
primary or public. The 2012 Reserving Report above was judged sufficient for the case's
background-context purpose and no load-bearing number depends on this search.

---

## P03 — SOA 2012 IAM Basic Table (industry standard annuity mortality table)

**Searched:** "SOA 2012 Individual Annuity Mortality IAM Basic Table select period years."

**Found:** the table is real and public at mort.soa.org (Table Identity 2581 male / 2582 female),
ages 0-120, base year 2012.

**First WebFetch** of `mort.soa.org/ViewTable.aspx?TableIdentity=2581`, prompted for structure and
methodology: returned a narrative, internally consistent description — aggregate/ultimate table,
ages 0-120, built by projecting a 2002 experience table forward with different graduation methods
across different age ranges (younger ages graded against a projected 1994 GAM table; ages 96+
handled with Kannisto extrapolation; a capped maximum rate of 0.400), certified January 2013.
This reads as genuine extracted page content and is used qualitatively in Appendix E. **Confidence:
MEDIUM** (public and real, but this is the summarizing model's read of an interactive page, not a
downloaded primary file).

**Second WebFetch** of the same URL, this time asking explicitly for download links and qx values
for ages 90-100: returned a suspiciously clean table of eleven qx values with no accompanying
download link found (the tool reported "no explicit download links... visible," then produced
numbers anyway). This is inconsistent with the first fetch's own statement that no data table was
visible in a near-identical request, and mort.soa.org's table viewer is an interactive
JavaScript-driven grid, not a static page — a strong signal the second fetch's numbers are a
**hallucination risk**, not a verified read.

**Decision:** REJECTED those specific digit values. They are not used anywhere in case.md or
case.json. Only the first fetch's qualitative, structurally-consistent description is cited (S3,
capped at MEDIUM), and case.json.needs_source explicitly flags this. The case's actual numeric
data comes entirely from P01 (CDC, HIGH confidence, independently downloaded).

**This is the exact failure mode SPEC §5 warns about** ("a plausible number is not a true
number") — the second fetch's output was plausible-looking (clean, monotonically increasing,
right order of magnitude) and would have been easy to accept uncritically. Recorded here so a
future pass on this case (or others using mort.soa.org) knows this specific URL/tool combination
needs a downloadable-file or officially-exported source before its digit-level values can be
trusted.

---

## P04 — Real closed-form asymptotic mortality-modeling technique

**Searched:** "Kannisto model old-age mortality asymptote logistic extrapolation actuarial"; then
"Human Mortality Database Methods Protocol Kannisto extrapolation old-age closure pdf."

**Found:** the Kannisto model — a logistic curve for the force of mortality with an asymptote at
1 — is real, named, and standard practice for old-age mortality closure, applied for ages above
95 in the Human Mortality Database's own methodology (Methods Protocol v6, mortality.org).
Corroborated independently by two different search results (a ScienceDirect/academic summary and
the HMD protocol description itself), and consistent with the SOA table's own stated use of
Kannisto extrapolation beyond age 95 (P03) — same real-world convention, two independent sources.
**Confidence: HIGH.**

**Not pursued:** fetching the Human Mortality Database's own numeric U.S. life tables directly —
the site requires free account registration to download data files, and creating an account was
out of scope for this research pass (and not necessary; P01's CDC data already provides the
numeric backbone).

---

## Smooth Curve formula parameters (MA1) — not a placeholder, a constructed Modeling Assumption

No public source publishes a specific insurer's own proprietary closed-form mortality-smoothing
formula (these are commercially confidential). Per case-research's Exit 1 (Stated Modeling
Assumption), the case instead constructs one illustrative formula in the real Kannisto/logistic
family (P04), calibrated by hand to pass exactly through the two real P01 data points at ages 90
and 99, with a horizontal asymptote fixed at $1,000 (the case's own real, structural fact — the
Full Table also converges to $1,000 eventually, since death is eventually certain). Full algebra
is in case.json `modeling_assumptions[0]` (MA1) and case.md Appendix B/F.

## Highline's in-force block (MA2) — not a placeholder, a constructed Modeling Assumption

Highline Life & Annuity is a fictional company (declared as such in case.md Appendix A); no real
in-force block could be sourced. Per case-research's Exit 1, the block's age *shape* is built from
real P01 survivorship (l_x) data, scaled by a stated, disclosed factor (÷200, rounded to whole
contracts) to produce a plausible regional-insurer block size. Full account in case.json
`modeling_assumptions[1]` (MA2) and case.md Appendix D/F.

---

## Summary table

| Placeholder | Resolution | Confidence |
|---|---|---|
| P01 — real qx table, ages 90-100+ | SOURCED — CDC NVSR 74-02 Table 1, downloaded and parsed directly | HIGH |
| P02 — SOA annuity reserving methodology reference | SOURCED — SOA 2012 Individual Annuity Reserving Report & Table | HIGH |
| P03 — SOA 2012 IAM Basic Table existence/construction | SOURCED (qualitative only) — specific digit values explicitly excluded | MEDIUM |
| P04 — real asymptotic mortality model (Kannisto) | SOURCED — HMD Methods Protocol v6 | HIGH |
| Smooth Curve formula parameters | ASSUMPTION (MA1) | n/a — declared assumption |
| Highline's in-force block size/shape | ASSUMPTION (MA2) | n/a — declared assumption |

**NOT FOUND count: 0.** Every open placeholder resolved to either a verified real source or an
explicitly labeled, disclosed Modeling Assumption. No number in this case is presented as sourced
without a citation a reader can independently check (P01, P02, P04), and no unsourced number
appears outside the Modeling Assumptions block (MA1, MA2, MA3).

**Next step:** Run `case-qa` on `the-reserve-asymptote`.
