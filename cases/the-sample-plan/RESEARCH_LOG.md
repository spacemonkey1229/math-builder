# Research Log — The Sample Plan

Stage 3 (`case-research`) run on `cases/the-sample-plan/`. 15 `{{NEEDS_SOURCE}}` placeholders
enumerated (Appendix A, B, C intro figures). Worked in load-bearing order: the ANSI/ASQ Z1.4
sample-size table first (the case's core mechanical numbers), then the real-world contamination
data, then the unit-level defect fraction (expected, going in, to be the hardest to source).

## Appendix A/B — ANSI/ASQ Z1.4-2003 sample size code letters and sample sizes (worked first)

**Searched:**
- "ANSI ASQ Z1.4 sample size code letter table general inspection level II III lot size 3201 to
  10000" — search-summary results pointed at several AQL-calculator vendor sites and one
  downloadable chart PDF, but summaries alone do not carry citable table cells.
- Direct WebFetch of `https://www.intouch-quality.com/blog/anatomy-of-the-ansi-asq-z1.4-industry-standard-aql-table`
  — explains how to read the table but does not reproduce it (rejected as a citation source for
  this reason — it does not contain the figures needed).
- Direct WebFetch (as a PDF, read via the Read tool since text extraction alone did not render
  cleanly) of `https://www.intouch-quality.com/hubfs/pdf/AQLChart.pdf` — an "AQL Chart" reproducing
  the actual ANSI/ASQ Standard Z1.4-2003 tables (explicitly labeled "SINGLE SAMPLING PLAN FOR
  NORMAL INSPECTION, ANSI/ASQ STANDARD Z1.4-2003" on the second page).
- Also attempted `https://www.gqc.io/quality-resources/ansi-sampling-tables` for a cross-check —
  the page references the standard conceptually but does not reproduce exact Ac/Re or sample-size
  cells, so it was not used as a citation.

**Found (directly read from the fetched PDF, both pages):**
- Page 2 ("Sample Size Code Letters" table, by lot size range and General Inspection Level):
  for lot size range **281 to 500**, Level I = **F**, Level II = **H**, Level III = **J**.
- Page 1 (Master Table, sample size by code letter): code letter **H = 50** units;
  code letter **J = 80** units.

**Design decision:** the case needed a lot-size band with a real, moderate-magnitude sample-size
gap between Level II and Level III (a larger band like 3,201–10,000 gives Level II=200/Level
III=315, which produces an inspection-cost gap so large it swamps any realistic risk-cost
difference and makes the case unbalanced — checked by hand-computing both bands' totals before
committing). The 281–500 band's H(50)/J(80) pair was chosen specifically because it produces a
genuinely close (8–12%) margin once combined with the other sourced/assumed figures below — this
is the SPEC §2 "retune a constraint, don't hide data" move, applied to the *lot-size-band choice*
(itself a Modeling Assumption, MA3), not to any sourced figure.

**Outcome:** SOURCED as [S1], HIGH confidence — a primary-standard reproduction, directly fetched
and read in full (not summarized secondhand), unambiguous units, and exactly the figures the case
needs.

## Appendix A — the c=0 (zero acceptance number) sampling rule

**Searched:**
- "zero acceptance number sampling plan c=0 critical defect pharmaceutical NIST OC curve binomial
  approximation AQL" — confirmed this is a real, standard, named methodology (Nicholas L.
  Squeglia's "Zero Acceptance Number Sampling Plans," ASQ Press, is the standard reference work;
  multiple independent quality-engineering sites — Quality Digest, IPQC, Minitab's own support
  documentation — describe c=0 plans and the P(accept) = (1-p)^n relationship consistently).
- Direct WebFetch attempt of `https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc27.htm` —
  this specific NIST Engineering Statistics Handbook page turned out to cover **skip-lot**
  sampling, not c=0/OC-curve theory — a wrong page for this exact URL guess. Not used, and not
  cited, since it does not contain the claimed content (this rejection is recorded so a future
  pass does not re-fetch the same wrong URL expecting c=0 content).
- Direct WebFetch of `https://www.qualitydigest.com/inside/operations-article/when-and-how-use-zero-acceptance-number-sampling-041119.html`
  — confirmed publication date (2018-04-04), author (William A. Levinson), and the specific claim
  that c=0 plans "require far less inspection than the corresponding ANSI/ASQ Z1.4" for a
  comparable assurance level. The full article sits behind a login wall; the (1-p)^n formula
  itself was corroborated via the search-summary's discussion of Squeglia's methodology rather
  than a single fully-rendered primary derivation, hence MEDIUM rather than HIGH confidence.

**Outcome:** SOURCED as [S2], MEDIUM confidence — real, named, dated, and the underlying mechanism
independently corroborated across multiple quality-engineering sources, but the exact formula
derivation was not read on one fully-open primary page.

## Appendix C — real lot-contamination-occurrence rate and cost of a failed batch

**Searched:**
- "single-use bioprocess bag leak integrity failure rate percent BPOG survey" — found real
  discussion of single-use system integrity testing (helium leak detection, maximum allowable
  leak limits) but **no public, company-specific or BPOG-published unit-level defect/leak rate**
  for single-use consumables. This negative result is itself load-bearing: it is why MA1 (the
  unit-level defect fraction) had to become a Modeling Assumption rather than a citation.
- "cost of a lost or contaminated biologics manufacturing batch dollars industry estimate" and
  "'cost of a failed batch' biopharmaceutical manufacturing dollar figure per batch citation" —
  surfaced two closely related trade-press articles citing the same underlying BioPlan Associates
  survey.
- Direct WebFetch of `https://www.genengnews.com/insights/batch-failure-rates-in-biomanufacturing/`
  — confirmed a 7% overall / 7.6% large-facility (1,000L+) / 6.6% small-facility total batch
  failure rate, a 2.3% large-facility contamination sub-rate, and a cost figure attributed to Beth
  Junker (Merck) — but this fetch's automated text extraction rendered the cost figure as
  "$1–2 billion," which is not economically plausible for a single batch.
- Direct WebFetch of `https://www.bioprocessintl.com/bioanalytical-methods/biotech-facilities-average-a-batch-failure-every-40-6-weeks`
  — a companion article citing the same survey and the same Beth Junker attribution, but this
  fetch's text unambiguously reads **"greater than $1–2 million"** — a per-batch magnitude that
  matches known biologics batch scale. Both articles are dated **2008-09-01**, both cite the "5th
  Annual Report and Survey of Biopharmaceutical Manufacturing Capacity and Production" (BioPlan
  Associates, 145 organizations surveyed worldwide).
- **Discrepancy investigated, not silently resolved:** the GEN fetch's "$1–2 billion" and the BPI
  fetch's "$1–2 million" cannot both be the intended quote from what is presented as the same
  Beth Junker statement. BioProcess International's directly-fetched text is unambiguous
  (no OCR/markdown artifacts around the figure); the GenEngNews figure is treated as a likely
  extraction error (a stray "billion" substituted for "million," or a scale confusion with an
  unrelated statistic elsewhere on that page) and is **not used**. "$1–2 million" (BPI) is the
  value cited in this case, and the discrepancy is recorded in `case.json.sources[S3].note` and
  in `case.md` Appendix E rather than picking a number and hiding the conflict.
- Attempted a third, more recent source for a fresher figure (queries for "cost of a failed batch"
  generally, and single-use consumable pricing to inform the unit-test-cost assumption) — did not
  surface a more recent, equally specific, equally well-attributed figure. The 2008 figure is the
  best available public data for this exact claim; its age is disclosed explicitly in both
  `case.md` (Appendix E note) and `case.json.sources[S3]`, consistent with SPEC's "still-changing
  entity" cutoff-disclosure principle applied here to an aging industry benchmark rather than a
  literally still-changing individual entity.

**Outcome:** SOURCED as [S3], MEDIUM confidence (not HIGH, specifically because of the 18-year age
and the cross-source cost-figure discrepancy just described, both disclosed rather than hidden).

## Appendix C — MA1 (unit-level defect fraction) and MA2 (supplier-deviation-notice elevated risk)

**Searched:** (see Appendix C section above for the single-use-consumable-specific search; no
manufacturer or industry group publishes a unit-level defect fraction). A further targeted search
for single-use bioreactor/consumable per-unit pricing ("single-use bioreactor bag price cost per
unit 2026 Sartorius Thermo Fisher Cytiva") surfaced only **modeled/aggregated** price-corridor
estimates (e.g., an IntuitionLabs industry analysis citing a "$800–$5,000 per bag" corridor
"modeled from Sartorius and Thermo Fisher catalog prices") rather than a directly-quotable primary
vendor price list — this modeled, non-primary character is why the case's per-unit
destructive-testing cost ($250) is presented as a Modeling Assumption (MA-cost) rather than a
sourced figure, informed by but not equal to that broader corridor (a full assembled bioreactor
bag and a smaller tested consumable component are not the same product).

**Outcome:** NOT FOUND as directly citable figures for either MA1 or MA2. **Exit chosen: Modeling
Assumption**, for both:
- MA1 (2.5%) — set within the range of Acceptable Quality Levels the ANSI/ASQ Z1.4 standard's own
  AQL columns are built to test critical/major characteristics against.
- MA2 (6%) — a deliberately moderate (~2.6x) multiple of the sourced 2.3% baseline, chosen the
  same way `cases/deductible-roulette`'s MA1 was chosen (a stated, disclosed multiple of a real
  baseline, not an arbitrary round number).

Redesign (dropping the unit-level defect-fraction mechanic entirely, e.g. by using only the
sourced batch-level rate) was considered and rejected: collapsing the model to a single sourced
probability would remove the case's genuine compound/independent-event mechanic (D2's repeated
multiplication) and its real, checkable sensitivity finding (MA1 is robust; MA2 is fragile) —
exactly the kind of pedagogically load-bearing structure an honest, sensitivity-labeled assumption
is meant to preserve, per the same reasoning `cases/deductible-roulette`'s own research log used
for its MA1.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01 | Lot 4471 size | ASSUMPTION (MA3) | 500 units | n/a (assumption) |
| P02–P05 | Z1.4 code letters and sample sizes, Options A/B | SOURCED (S1) | H=50, J=80 | HIGH |
| P06 | Per-unit destructive test cost | ASSUMPTION (MA-cost) | $250 | n/a (assumption) |
| P07–P08 | Total destructive-testing cost, Options A/B (derived) | SOURCED (S1, derived) | $12,500 / $20,000 | HIGH |
| P09–P12 | Z1.4 lot-size-band row and code letters (Appendix B) | SOURCED (S1) | 281-500: F/H/J | HIGH |
| P13 | Large-facility batch contamination rate | SOURCED (S3) | 2.3% | MEDIUM |
| P14 | Cost of an undetected escape | SOURCED (S3) | $1M-$2M range, $1.4M used | MEDIUM |
| P15 | Unit-level defect fraction | ASSUMPTION (MA1) | 2.5% | n/a (assumption) |
| — | Supplier-deviation-notice elevated lot risk | ASSUMPTION (MA2) | 6% | n/a (assumption) |

Sourced: 9 placeholders resolved by 3 source records (S1 covers the Z1.4-table placeholders; S3
covers the contamination-rate/escape-cost placeholders). Assumption: 4 (MA1, MA2, MA3, MA-cost).
Dropped: 0. Open: 0.

## SPEC §2 balance-test self-check (post-research pass, 2026-09-09)

Independently re-verified before flipping `status` to `researched` (re-ran `sensitivity_model.py`
fresh and re-fetched two of the three sources rather than trusting the prior write):

- **Primary metric exists and is well-defined:** yes — expected total cost per production lot
  (certain destructive-testing cost + probability-weighted expected cost of an undetected
  out-of-spec escape), computed identically for both options. Confirmed by re-running
  `sensitivity_model.py`, which reproduces `case.json.derived` exactly: A = $21,580.02,
  B = $24,248.40, margin = 11.00%.
- **No structurally-zero-cost option:** both options carry a real, non-zero certain cost
  (inspection: $12,500 for A, $20,000 for B) and a real, non-zero probability-weighted risk cost
  (A = $9,080.02, B = $4,248.40) — neither term collapses to zero for either option.
- **Margin under the ~20% cap:** 11.0% margin on the primary metric, comfortably inside SPEC §2's
  ~20% ceiling and within the concept brief's 8-12% target band. Not near the cap edge.
- **Source spot-check (independent re-fetch, this pass):** re-fetched
  `bioprocessintl.com/.../biotech-facilities-average-a-batch-failure-every-40-6-weeks` directly —
  confirms the Beth Junker (Merck) quote, the "greater than $1-2 million" figure, and the BioPlan
  Associates 2008 "5th Annual Report and Survey" attribution exactly as recorded for [S3]. Also
  re-fetched `intouch-quality.com/hubfs/pdf/AQLChart.pdf` as a PDF (via the Read tool, since
  WebFetch's own text extraction still garbles this specific PDF, consistent with the original
  research note) — confirms lot size 281-500 -> Level I=F, Level II=H, Level III=J on page 2, and
  code letter H=50 / J=80 on page 1, exactly as recorded for [S1]. No discrepancy found on
  re-check.
- **No badly-off balance to flag:** the primary-metric margin (11.0%) is solid and not
  borderline. The one thing worth flagging forward to `case-readiness`: the primary metric's
  winner (A) is *fully* robust to MA1 across its entire [0,1] range (never flips), which is a
  clean result, not a problem — but it does mean the case's actual pedagogical tension lives in
  the D4/Twist scenario (MA2), where the winner flips to B at a lot-occurrence probability of only
  ~3.57%, far below the case's own stated MA2 (6%). This is already disclosed in
  `case.json.modeling_assumptions`, `sensitivity_disclosure`, and `derived.twist_flip_threshold` —
  noted here again so Tier 1/2 readiness checks do not treat the primary-metric robustness finding
  as a balance-test failure; the balance test is passed on the primary metric as scored, and the
  Twist is a separate, intentionally fragile secondary mechanic.

**Verdict: balance test passes, nothing to flag as badly off.**

## Next step

Run `case-readiness` (Tier 1 structural, then Tier 2 simulated play) on `the-sample-plan`.
