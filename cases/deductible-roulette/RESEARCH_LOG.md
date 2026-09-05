# Research Log — Deductible Roulette

Stage 3 (`case-research`) run on `cases/deductible-roulette/`. 10 `{{NEEDS_SOURCE}}` placeholders
enumerated (across Appendix A, B, C). Worked in load-bearing order: Appendix B's baseline claim
frequency first (flagged HIGHEST priority — the case's central number), then Appendix A's
premiums, then Appendix C's repeat-claim probability.

## Appendix B — baseline collision/comprehensive claim frequency and severity (worked first)

**Searched:**
- "III.org auto insurance claim frequency collision comprehensive percentage of insured vehicles"
- direct fetch of III.org's own facts-and-statistics page

**Fetched directly:**
- `https://www.iii.org/fact-statistic/facts-statistics-auto-insurance` — Insurance Information
  Institute (Triple-I)'s own facts-and-statistics page. Confirmed directly: "4.9 percent of
  collision insurance policyholders had a claim" and "3.3 percent of people with comprehensive
  coverage had a claim" (2022 data, sourced by III to ISO/Verisk), with average claim severities
  of $5,992 (collision) and $2,738 (comprehensive). The page does not carry an explicit
  "last updated" stamp but its surrounding claims data is dated 2022-2024 throughout.

**Outcome:** SOURCED as [S2], HIGH confidence — a primary trade-association page, directly
fetched, dated, unambiguous units, and exactly the figure the case needs (not a proxy). This is
the case's core load-bearing probability figure (Appendix B's baseline rate feeds directly into
D1/D2/D3).

## Appendix A — the two renewal quotes (premiums by deductible level)

**Searched:**
- "NAIC average auto insurance premium by deductible $500 vs $1000 savings percent"
- "III.org 'raise your deductible' save money auto insurance premium percent"
- "Bankrate car insurance deductible $500 vs $1000 study average premium difference by state 2026"
- "bankrate.com 'average car insurance rates' deductible table site:bankrate.com"
- direct WebFetch attempts on `iii.org/article/understanding-your-insurance-deductibles`,
  `bankrate.com/insurance/car/car-insurance-deductible/`,
  `bankrate.com/insurance/car/auto-insurance-guide/`,
  `bankrate.com/insurance/car/how-does-a-deductible-affect-insurance`

**Rejected / investigated and excluded:**
- III.org's own deductible-guidance article ("Understanding your insurance deductibles"),
  directly fetched, states only that raising a deductible "can reduce" premium costs with **no
  percentage or dollar figure at all** — an earlier WebSearch summary had attributed a "15 to 30
  percent... 40 percent or more" figure to this III.org page, but the directly fetched primary
  page does not contain that language. Per the skill's "never cite a URL you did not verify"
  rule, that figure is **not used anywhere in this case**, despite being repeated by several
  secondary sites that (incorrectly) attribute it to III.org.
- WalletHub's "$1,000 deductible could save you up to 28%" figure — directly fetched, but the
  page cites no source or methodology for the 28% figure and gives no underlying dollar amounts.
  Rejected as LOW confidence (undated methodology, no attribution) per the skill's tier-4 rule.
- A MoneyGeek same-family pair of pages (`car-insurance-with-500-deductible`,
  `car-insurance-with-1000-deductible`), each directly fetched and each individually well-dated
  (Aug 14 and Aug 17, 2026 respectively) and well-attributed (14 major insurers, a stated driver
  profile) — but the two pages, updated on different days with what is presumably independently
  re-sampled data, show the $1,000-deductible policy costing $1,631/yr versus the $500-deductible
  policy's $1,616/yr — the **higher deductible costing slightly more**, the opposite direction
  from every other source found and economically implausible as a real, causal $500-vs-$1,000
  comparison (more likely week-to-week rate-table noise between two separately-refreshed pages
  than a genuine finding). This is a **contested figure** in the SPEC §5 sense (the "50% of
  vaccines wasted" precedent) — investigated and explicitly excluded from the case rather than
  used, and noted in Appendix E so a future reader does not independently re-discover it and
  wonder why it wasn't used.
- Multiple direct WebFetch attempts on specific bankrate.com insurance-deductible URLs
  (`/insurance/car/car-insurance-deductible/`, `/insurance/car/auto-insurance-guide/`,
  `/insurance/car/how-does-a-deductible-affect-insurance`) each returned generic
  homepage/navigation boilerplate rather than the underlying article content — most likely a
  JS-rendered page or a geo/bot gate the fetch tool could not get past. This means the specific
  Bankrate table used below (S1) could **not** be independently verified by direct primary fetch
  in this research pass.

**Found (via WebSearch, corroborated across multiple independent secondary pages):** "Bankrate's
January 2025 rate analysis with Quadrant Information Services" reporting a matched, same-day,
same-driver-profile comparison: $500/$500 comprehensive/collision deductible averages $2,638/yr;
$1,000/$1,000 averages $2,336/yr (a $302/yr, ~11.4% reduction). This exact pairing recurs
identically across at least three independent aggregator pages (moneygeek.com's search-surfaced
summary, an AOL Finance syndication, and a Medium comparison piece), all attributing it to the
same named study — the kind of consistent, specific, dated attribution the skill's tier-3 rule
treats as MEDIUM-confidence "reputable coverage citing a named tier-1 source," even without an
independently rendered primary page.

**Outcome:** SOURCED as [S1], **MEDIUM** confidence (not HIGH) specifically because the primary
Bankrate page could not be independently fetched and rendered in this research pass, despite
multiple attempts and URL variations. Chosen over the MoneyGeek pair specifically because it is
same-day/same-methodology (a genuine controlled A/B comparison) rather than two independently
drifting snapshots.

## Appendix C — repeat-claim probability (the case's one Modeling Assumption)

**Searched:**
- "study drivers with one at-fault accident more likely second accident within following years
  probability"
- traffic-safety and actuarial literature searches (ScienceDirect, ResearchGate)

**Found:** Real, peer-reviewed literature confirms the underlying phenomenon — crash-prone driver
clustering is a documented, studied effect (e.g. a cited Louisiana crash-data finding that at-fault
crash-prone drivers, ~5% of licensed drivers, account for ~34% of at-fault crashes; a cited study
finding a 4.53x elevated subsequent-crash risk for a specific subgroup — older female at-fault
drivers). None of this literature reports a single general-population "probability a driver with
one at-fault claim files a second one within 1-3 years" — the studies found report relative-risk
ratios for narrow demographic subgroups, or population-concentration shares, neither of which
converts cleanly into the single applicable annual percentage this case's Appendix C needs.

**Outcome:** NOT FOUND as a directly citable general-population figure. **Exit chosen: Modeling
Assumption (MA1)**, value 20% (roughly 4x Appendix B's 4.9% baseline) — a deliberately moderate
reading of "meaningfully elevated" given the literature confirms the direction and general
magnitude of the effect (several-fold elevation for some subgroups) without providing a single
number this case could cite directly. Redesign (dropping the repeat-claim mechanic entirely) was
considered and rejected: it is exactly the mechanic that forces genuine conditional/dependent
probability reasoning across the three-year window, per the concept brief's explicit design goal
("frame the case over a multi-year window so compound/conditional probability is genuinely
forced") — an honest, sensitivity-labeled assumption is the correct exit, not a redesign that
would flatten the case back to a single-year expected-value plug-in.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01-P04 | Appendix A premiums (monthly/annual x 2 options) | SOURCED (S1) | $219.83/mo, $194.67/mo ($2,638/$2,336 annual) | MEDIUM |
| P05-P06 | Appendix A three-year premium totals (derived) | SOURCED (S1, derived) | $7,914 / $7,008 | MEDIUM |
| P07 | Collision claim frequency | SOURCED (S2) | 4.9%/yr | HIGH |
| P08 | Collision claim severity | SOURCED (S2) | $5,992 | HIGH |
| P09 | Comprehensive claim frequency | SOURCED (S2) | 3.3%/yr | HIGH |
| P10 | Comprehensive claim severity | SOURCED (S2) | $2,738 | HIGH |
| P11 | Repeat-claim probability given a prior claim | ASSUMPTION (MA1) | 20% | n/a (assumption) |

Sourced: 10 placeholders resolved by 2 source records (S1 covers the 6 premium-related
placeholders; S2 covers the 4 claim-frequency/severity placeholders). Assumption: 1 (MA1).
Dropped: 0. Open: 0.

## Next step

Run `case-readiness` (Tier 1 structural, then Tier 2 simulated play) on `deductible-roulette`.
