# RESEARCH LOG — The Curve's Turn (`curves-turn`)

Stage 3, `case-research`, run 2026-08-12. Fifteen placeholders opened by `case-write`; fifteen
closed. **Zero `{{NEEDS_SOURCE}}` remain.** Every URL in `case.json.sources[]` was fetched in this
session and confirmed to carry the figure cited from it (MCS-21). Nothing was filled from memory,
and the rejections below are the part worth reading — they stop the next person re-running dead
searches.

## Outcome table

| # | Placeholder | Exit | Value | Source / assumption |
|---|---|---|---|---|
| P01 | Appendix A weekly series (previous wave) | SOURCED | 19 weeks of real county counts | S1 |
| P02 | Appendix A fitted cubic P(t) | SOURCED (derived) | −0.3348, 8.9975, −42.0177, 38.2994 | S7 (OLS on S1) |
| P03 | Appendix B weekly series (current wave) | SOURCED | 12 weeks of real county counts | S1 |
| P04 | Appendix B fitted cubic D(t) | SOURCED (derived) | 0.2174, −1.8006, 25.3255, 247.9597 | S8 (OLS on S1) |
| P05 | Instructional days per horizon week | ASSUMPTION | 5, every week | MA5 |
| P06 | County population denominator | SOURCED | 163,774 (2019 Census estimate) | S2 + S3 |
| P07 | Reference case-rate tiers | SOURCED | <10 / 10–49 / 50–99 / ≥100 per 100k per 7 days | S4 |
| P08 | Board's written closure level | ASSUMPTION | 500 per 100,000 per week | MA2 |
| P09 | Closure budget | ASSUMPTION | two weeks, once per term | MA3 |
| P10 | Evaluation horizon | ASSUMPTION | six weeks (t = 12…17) | MA4 |
| P11 | In-school transmission coefficient `k` | ASSUMPTION | 0.5 | MA6, reasoned down from S6 |
| P12 | Rapid antigen test performance | SOURCED | 55.0% sensitivity (95% CI 50.9–59.0), 99.5% specificity | S5 |
| P13 | Screening programme effectiveness `e` | ASSUMPTION | 0.10 | MA7, built down from S5 |
| P14 | Appendix E sources table | SOURCED (composed) | S1–S8 | — |
| P15 | Appendix F assumptions table | ASSUMPTION (composed) | MA1–MA8 | — |

**NOT FOUND count: 0 figures were abandoned.** Five figures were returned as NOT FOUND *as citable
public numbers* and each took exit 1 (a stated Modeling Assumption in a visible block) — MA2, MA3,
MA4, MA5 and MA6/MA7. No figure was dropped and no case redesign was needed. Nothing was quietly
filled.

---

## What was searched, fetched, and rejected

### The case series (P01, P03) — the load-bearing find

The case needed a **real, noisy, frozen** weekly count series for one jurisdiction, long enough to
carry a completed wave (for the critical-point and optimisation work) and a partial rising wave
(for the concavity work), with data *after* the decision week available to the guide but not to the
student packet.

- **Rejected: the NYT COVID-19 county archive** (`github.com/nytimes/covid-19-data`, named in the
  concept sheet). Correct shape, but the county files are of the order of a hundred megabytes; a
  fetch tool cannot return them and cherry-picking rows out of a file this session never actually
  read would be exactly the failure MCS-21 exists to prevent.
- **Rejected: CDC NSSP ED-visit trajectories** (`data.cdc.gov` `rdmq-nq56`, fetched). This one *did*
  fetch cleanly, but its per-county columns are categorical — `"Data Unavailable"`, "Increasing",
  "Decreasing" — not numeric. You cannot differentiate a word.
- **Rejected: CDC WONDER.** Query-form interface, not fetchable as a document.
- **Accepted: CDC `yviw-z6j5`, "Weekly United States COVID-19 Cases and Deaths by County —
  ARCHIVED."** Found via the Socrata catalog API, then fetched twice: once for the dataset metadata
  (`/api/views/yviw-z6j5.json`, giving the exact title, the CDC COVID-19 Response attribution and
  the 2023-05-11 discontinuation) and once as a filtered data query for FIPS 50007 across
  2021-05-29 → 2021-12-26, which returned the exact rows printed in Appendices A and B, plus the
  `cumulative_cases`, `cumulative_deaths` and `new_deaths` columns the case deliberately keeps as
  data a Hero must decide to ignore (SPEC §1.6).

Why Chittenden County, Vermont: a mid-size county whose weekly counts are large enough to be
meaningful and small enough to be legible, with a completed Delta wave (June–October 2021) that
contains **both** a local minimum and a local maximum inside one window — which is what makes D3's
first-derivative-test table have two rows instead of one — immediately followed by a rising wave.

**Frozen-entity check (SPEC §5).** The series is archived; CDC stopped updating it on 2023-05-11.
It cannot drift after the case is written. The case still states its window explicitly on both
appendix tables.

### The fitted models (P02, P04)

Not published anywhere; derived here by ordinary least squares on the two New-cases columns, and
published in the case to four decimal places so a Hero reproduces them with any regression tool.
The sensitivity model uses the **rounded** coefficients, not the full-precision fit, so every number
the case asserts is reachable by hand from the case document. `g = D'(11)/D(11) = 0.108070` follows
from the rounded coefficients and is asserted at import time in `sensitivity_model.py`.

One property was checked and kept on purpose: `P(t)` returns **−16.17** at its own local minimum.
A cubic fitted to a real epidemic trough does that. The case does not hide it — D3 asks the Hero to
find it and say what it means.

### The population denominator (P06)

- **Rejected: `api.census.gov/data/2020/dec/pl`** — returns "A valid key must be included with each
  data API request." No key available in this session, and inventing one is not an option.
- **Rejected: `census.gov/quickfacts/…`** — HTTP 403 to this sandbox.
- **Accepted: CDC `3nnm-4jni`, column `county_population` = 163,774**, with the column's own metadata
  fetched separately to establish the vintage: *"County population (2019 Census estimate)."*

This is arguably the better citation regardless of the 403s: it is the denominator CDC itself uses
for its own county case rates, so the case's rates and CDC's rates are on the same base.

### The reference tier scale (P07)

- **Rejected: `stacks.cdc.gov/view/cdc/108529` and `stacks.cdc.gov/view/cdc/106255`** (CDC's K-12
  operational-strategy PDFs) — HTTP 403.
- **Rejected: `cdc.gov/mmwr/…`** — HTTP 403 across the board for this sandbox.
- **Accepted: CDC dataset metadata for `nra9-vzzn`**, which states all four cut-offs verbatim: low
  fewer than 10, moderate 10–49, substantial 50–99, high 100 or more, per 100,000 in the past
  7 days.

The scale is used only as the reference a health officer would recognise. The board's own level is
**not** sourced to it and does not pretend to be — see MA2.

### Rapid antigen test performance (P12)

- **Rejected: `cochranelibrary.com/cdsr/doi/10.1002/14651858.CD013705.pub3/full`** — HTTP 403.
- **Rejected: `pubmed.ncbi.nlm.nih.gov/37540523/`** — cookie wall; the fetch returned a consent
  banner and no abstract.
- **Accepted: `cochrane.org/evidence/CD013705_…`**, Cochrane's own plain-language page for the same
  review (Dinnes, Berhane, Walsh et al., 28 November 2025), which carries the figures directly:
  asymptomatic sensitivity **55.0% (95% CI 50.9%–59.0%)**, specificity **99.5%**.

Note the trap avoided: this is **test sensitivity**, not programme effectiveness. The case never
uses 55% as the screening programme's removal rate. MA7 reasons down from it and says so.

### School transmission (P11)

- **Rejected: `medrxiv.org/…2021.09.22.21263900.full.pdf`** (Massachusetts in-school transmission
  study) — HTTP 403.
- **Rejected: the underlying MMWR articles** (Salt Lake County, St. Louis, Marin County) — all on
  `cdc.gov/mmwr` or `stacks.cdc.gov`, all 403.
- **Accepted: CDC's own Science Brief on K-12 transmission**, mirrored on NCBI Bookshelf
  (`NBK570438`, last updated 17 December 2021), which fetched cleanly and carries five real
  school-associated secondary attack rates in one place: 0.38% and 6.46% (Italian primary and
  middle/high), 0.7% (Utah elementary), 1.5% among 1,035 students (Lake County, Illinois), and 2%
  of school contacts (St. Louis).

**A contested figure this case refuses to print (SPEC §5).** There is no defensible single number
for "what share of transmission happens in schools." The same CDC brief that reports a 6.46%
attack rate in Italian middle and high schools also states that *"Neither increases in case
incidence among school-aged children nor school reopenings for in-person learning appear to
pre-date increases in community transmission."* Rather than launder that spread into one
authoritative-looking constant, the case states a coefficient in the open (MA6), names the range it
came from, and — this is the honest part — shows that the coefficient **cancels out of the
comparison entirely**, so the recommendation never depended on it.

---

## One structural change research forced back into stage 2

`case-research` may not rewrite deliverables, so this was handed back and re-entered at
`case-write`, and the LEARNING GOAL CHECK was re-run afterwards (unchanged: 6 deliverables,
13 claimed skills, 0 unmapped, 0 unreachable, 0 phantom).

**D5 as drafted was unanswerable.** It asked for the closure start week maximising *chain-weighted*
transmissions prevented on the **previous** wave — but the chain multiplier `w(t)` is defined only
against the current wave's horizon and planning growth rate, neither of which exists for the
previous wave. D5 now maximises `G(w) = P(w) + P(w+1)`, the reported cases the closure would have
covered, which is the question a retrospective look-back actually asks and which still forces the
full optimisation-with-derivatives skill. It also gained a second clause once the data landed,
because the data handed the case a gift: **the previous wave never crossed the board's written level
at all** (it peaked at a fitted 302.67 cases against a level of 818.87), which is a real, computed
argument for Option B that no author invented.

## Supplemental material considered and not shipped

A Desmos graph of the two cubics would help D2 and D4. None was shipped: a Desmos permalink cannot
be verified as loading from this sandbox, and MCS-21 does not make an exception for a link that
would merely be convenient. Both models are printed in full in the case, so a Hero builds the graph
in whatever tool they already use — which is Challenge 1's job anyway.

## Handoff

`Run case-readiness on curves-turn.` Zero placeholders open. `case.json.status` is `researched`.
The sensitivity model is written and runs, so Tier 2 probe 5 will not return NOT RUN.
