# Research Log — The Trial Size

Run: 2026-09-01 (case-research stage). 12 `{{NEEDS_SOURCE}}` placeholders enumerated in
`case.md`. All 12 resolved to **SOURCED** — zero left OPEN, zero dropped, zero unresolved
Modeling Assumptions needed. One derivation (the fixed cost F, per case-write's own disclosed
gap #1) was carried out and documented in-line.

## Placeholder enumeration (in document order)

| # | Location | Token (abridged) |
|---|---|---|
| P01 | Background, first hard constraint | total fixed survey budget, USD |
| P02 | Background, two-designs intro | same total fixed survey budget |
| P03 | Background, two-designs intro | number of existing survey clusters |
| P04 | Appendix A, Full Precision row | real total participant count (n) |
| P05 | Appendix A, Full Precision row | real total cost of full design, USD |
| P06 | Appendix A, Reserve And Expand row | real minimum adequate sample size |
| P07 | Appendix A, Reserve And Expand row | total cost at certified-adequate n |
| P08 | Appendix A, marginal-cost row | marginal cost per additional participant |
| P09 | Appendix B, graph stub | n-axis range for Budget-Remaining graph |
| P10 | Appendix C, cluster-count row | number of clusters |
| P11 | Appendix C, marginal-cluster-cost row | marginal cost per additional cluster |
| P12 | Appendix C, budget row | same total fixed survey budget |

## Search strategy and findings

**Tier 1 attempt — primary publisher.** Searched directly for the named source paper: Carcelen
AC, Hayford K, Moss WJ, et al., "How much does it cost to measure immunity? A costing analysis of
a measles and rubella serosurvey in southern Zambia," *PLOS ONE* (2020). Found immediately —
PLOS ONE is itself the primary open-access publisher, so this cleared tier 1 on the first search.

- Fetched the PLOS ONE article page directly:
  https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240734
  (published 2020-10-15, DOI 10.1371/journal.pone.0240734).
- Cross-fetched the PMC full-text mirror as a corroborating check:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC7561102/ (note: the `ncbi.nlm.nih.gov/pmc/...` URL
  301-redirects to `pmc.ncbi.nlm.nih.gov/...` — used the resolved URL).
- Both fetches independently returned the identical figures below, word-for-word on the key
  sentences. Graded **HIGH** across the board: primary publisher, dated, unambiguous units,
  and the figure the case actually needs (not a proxy).

**Figures recovered (all P01–P12 resolve from these five numbers):**

| Quantity | Value | Exact source sentence |
|---|---|---|
| Total nested serosurvey cost | $68,558 | "the total nested serosurvey cost was US $68,558 to collect dried blood spots from 658 participants in one province in Zambia" |
| Full-design participant count | n = 658 | (same sentence) |
| Number of clusters | 16 | "16 clusters" in Southern Province |
| Certified-adequate minimum n | 192 | "The sample size for the nested serosurvey required only 192 children in the 16 clusters" |
| Marginal cost / additional participant | $30 | "the marginal cost of adding a participant within an existing cluster was $30" |
| Marginal cost / additional cluster | $1,620 | "the marginal cost of including an additional cluster was $1,620" |
| Nesting savings (not used in this case's math, noted for completeness) | $43,957 | "By combining the serosurvey with the vaccination coverage survey, there was a savings of $43,957" |

These five real figures (total cost, n=658, n=192, marginal/participant, marginal/cluster)
resolve **P01, P02, P03, P04, P05, P06, P08, P10, P11, P12** directly — no further search needed
for those ten.

## Derivation (case-write's disclosed gap #1)

FACILITATOR.md flagged that the fixed infrastructure cost F is **not** a number the source paper
states directly — it must be recovered algebraically. Re-derived it explicitly, showing the two
real inputs used (both from Carcelen et al. 2020, sources S1 and S4):

```
Cost(n) = F + 30*n            [S4: $30/participant marginal cost]
Cost(658) = 68,558            [S1: real total cost at n=658]
F = 68,558 - 30*658 = 68,558 - 19,740 = 48,818
```

`F = $48,818` — this matches the figure named in the task brief as "~$48,818," now shown as an
exact derivation from two cited real inputs rather than an asserted number. This derivation
resolves **P07** as well: Cost(192) = 48,818 + 30*192 = 48,818 + 5,760 = **$54,578**, marked
`(derived)` in case.md rather than presented as if directly quoted.

This resolves **P09** (the graph's n-axis range): since R(n) = 68,558 - Cost(n) has its
x-intercept exactly at n = 658 (R(658) = 68,558 - 68,558 = 0 — the point where Full Precision
exhausts the entire budget), the axis range was set to n = 0 to 700 so the x-intercept falls
inside the plotted range with a little headroom, without pre-computing or displaying the
underlying R(n) equation in the appendix text (D3 asks the student to read that equation *off
the graph*, not off a stated formula — showing the formula in the appendix stub would have
short-circuited that deliverable).

## Rejected / not pursued

- **UNICEF Supply Division vaccine price PDFs** (per case-write's disclosed gap #2). Re-attempted
  a direct `WebFetch` of
  https://www.unicef.org/supply/documents/measles-and-rubella-vaccine-mr-price-data — still
  returned **HTTP 403 Forbidden**, confirming the block found during concept research was not a
  one-off. Per FACILITATOR.md's own note, the case's math does not depend on this figure (the
  freed-budget framing uses only the already-sourced marginal cluster cost, $1,620/cluster,
  which is real and cited). Did not force a vaccine-dose-price framing into the case. This
  remains a live option for a *future* revision, to be retried with an actual browser fetch
  (not automated `WebFetch`) rather than assumed to resolve — not attempted here since it is out
  of scope for this pass and the case does not need it.

## Supplemental corroboration

- **Brenzel L, Saxenian H, Stahley K, Dansereau E, "Cost of immunization coverage surveys in
  low- and middle-income countries,"** *Frontiers in Public Health* (2026),
  https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2026.1897118/full —
  confirmed real and located via search. Cited as **S6**, context/corroboration only. Graded
  **MEDIUM** (secondary, corroborating a general cost order-of-magnitude, not itself a
  load-bearing figure in any case.md table or calculation — every dollar figure in Appendix A/B/C
  comes from S1–S5, Carcelen et al. 2020, directly).

## Margin computation (facilitator-only — recorded in `case.json` `balance` object and
`FACILITATOR.md`, never in `case.md`)

Full Precision: $68,558. Reserve And Expand at n=192: $54,578 (derived). Freed budget:
$13,980 — enough for 8 whole new clusters at $1,620/cluster ($12,960 spent, $1,020 unused
remainder), taking cluster coverage from 16 to 24 (+50%).

The case's stated `primary_metric` deliberately spans two non-commensurable payoffs — statistical
precision (Option A) and discrete new-cluster count (Option B) — and cannot be reduced to one
cardinal unit without inventing an unsourced precision-to-coverage conversion factor, which SPEC
§5 forbids. The one clean, fully sourced, common-currency reading is the dollar split of the
fixed budget: **$13,980 of $68,558 (20.4%)** is the discretionary share separating the two
designs. This exceeds the SPEC §2 ~20% cap (also ~25.6% under the alternate loser-denominator
convention). **No winning option is declared** — see `case.json` `balance.margin_note` and
`FACILITATOR.md` for the full computation and the recommendation that case-write review this
before `case-qa`/`case-readiness` run, since the case is unbalanced on the only honest common-unit
reading of its own primary metric.

## Verification

Ran the SKILL.md step-7 verification script: 0 placeholders remaining, 0 orphan citation markers,
0 uncited source rows, 0 incomplete source records, 0 LOW-confidence sources, 0 `needs_source`
entries left `OPEN`.

## Next step

`Run case-readiness on the-trial-size` — but flag the margin finding above to whoever runs it;
this case may need a `case-write` constraint retune before it can pass the SPEC §2 balance test
cleanly.

## Addendum: primary_metric redesign (case-write remediation, 2026-09-01)

The no-winner finding above was correct as far as it went, but it was a genuine case-write
defect, not just an unlucky draw: `primary_metric` asked the two options to be compared on two
non-commensurable payoffs (statistical precision on the mapped district vs. discrete new-cluster
count in the unmapped one) with no sourced conversion factor between them. This addendum
redesigns the metric rather than re-running the same comparison with different numbers.

**Direction (a) checked and ruled out.** Before choosing a reframe, re-fetched Carcelen et al.
2020 (PLOS ONE, the same primary source, via a live fetch of the article page) specifically to
check whether it reports precision or CI width as a function of sample size, which would have
let "cost per percentage-point of precision" be built honestly from the source itself. It does
not: the only confidence intervals reported in the paper are the two final disease-specific
seroprevalence estimates (measles 96.1%, 95% CI 92.4–98.1; rubella 98.4%, 95% CI 95.9–99.4) — a
result of the design, not a precision-vs-n relationship the paper itself models or tabulates.
No design-effect or margin-of-error-vs-n table exists in the source. Building a "$/point of
precision" metric would therefore require inventing the precision curve, which is exactly the
unsourced-weighting-factor problem the original research correctly refused. Direction (a) is not
available from this source.

**Direction (b) adopted.** The same re-fetch surfaced a real, previously-uncited sentence from
the source paper: *"We estimated it cost $4,285 per average cluster and $104 per average
participant sampled."* This is the source paper's own average-unit-cost accounting — real,
sourced, and expressed in a single dollar unit that applies identically to both options. The
metric was reframed around it: **average total design cost per cluster of geographic coverage**
(total design cost ÷ total clusters covered, existing plus newly opened), rather than trying to
weigh precision against coverage.

Recomputed, using only already-cited figures (S1, S3, S4, S5 — no new sources needed beyond the
one corroborating sentence above, which requires no new citation since it is the same S1
document already in `sources[]`):

- Full Precision: $68,558 total ÷ 16 clusters = **$4,284.88/cluster** — matches the source
  paper's own stated $4,285/cluster almost exactly, an independent corroboration that this is
  the metric the source study itself treats as meaningful.
- Reserve And Expand: $54,578 (16 clusters, certified-adequate floor) + 8 new clusters ×
  $1,620 = $12,960 (real $1,020 unspent remainder, unchanged from the original finding) =
  $67,538 total ÷ 24 clusters = **$2,814.08/cluster**.

`margin_pct` = 100·(4,284.88 − 2,814.08)/4,284.88 = **34.3%** (loser-denominator convention:
52.3%). **Winner: Reserve And Expand.** This exceeds the SPEC §2 ~20% cap; reported honestly per
the remediation task's explicit instruction, not retuned to fit. `case.json`'s `primary_metric`,
`margin_pct`, and `balance` object are updated accordingly; `FACILITATOR.md`'s arguments and
margin section are rewritten to match. D1–D4 in `case.md` (the Cost(n) derivation, its graph, the
Budget-Remaining line, and the break-even system of equations) are all cost-only artifacts
already licensed by the original sourced figures and require no change under the new metric —
only the facilitator-side framing of what "wins" changes, not the student-facing deliverables or
`LEARNING_GOALS.md`'s deliverable→skill mapping.

## Addendum: retune attempt against the SPEC §2 ~20% cap (case-write remediation, 2026-09-01)

The redesigned metric's margin (34.3%, loser-denominator 52.3%) exceeds SPEC §2's ~20% cap.
SPEC §2 requires retuning by adjusting a constraint, not hiding data, so a retune was attempted
before falling back to a disclosed over-cap margin (MCS-46).

**Checked whether S5 ($1,620/cluster marginal cost) is a Modeling Assumption with room to be more
conservative.** It is not — `sources[].derived` is `false` and confidence is HIGH; it is the
source paper's own directly stated figure, not something the case invented or estimated. Same for
the 8-cluster count and $1,020 remainder in Reserve And Expand: both are pure arithmetic on real
sourced inputs (`floor(13,980/1,620) = 8`, remainder `13,980 − 12,960 = 1,020`), not assumptions
with independent flexibility.

**Re-fetched Carcelen et al. 2020 a second time**, specifically for its cost-breakdown and
sensitivity-analysis sections, to check whether the paper itself supports a higher, more
conservative marginal-cluster-cost estimate for opening clusters in a genuinely new/unsurveyed
district (as the case narrates Option B), versus the $1,620 figure, which the paper computed
within its own single-province, single-team study design. Findings:

- The $1,620 figure's own stated basis already includes "social mobilization, personnel, survey
  materials, and transportation required to include a cluster" plus a day of enumeration/mapping
  prep — i.e., it is already a full marginal-setup-cost figure, not a bare per-diem number that
  would obviously need a large markup for a new district.
- The paper reports cost shares by input type (personnel 51%, transportation 23%, field
  consumables 9%) and by phase (data collection 32%, survey preparation 25%, biospecimen
  collection 20%), but never splits any figure by "already-surveyed" vs. "new" geography — the
  entire study was conducted in one province, so no sourced geographic cost differential exists.
- The paper's own sensitivity analysis is the only lever with a stated bound: "None of the
  sensitivity analyses changed the cost by more than 8%," varying fieldwork time and team size —
  the cost drivers most likely to rise for a farther, unfamiliar district.
- Test: apply that 8% ceiling to the marginal-cluster cost as a maximally conservative, sourced
  adjustment ($1,620 → $1,749.60/cluster). Recomputed Reserve And Expand: floor(13,980/1,749.60) =
  7 new clusters (not 8) at $1,749.60 = $12,247.20, total $54,578 + $12,247.20 = $66,825.20 across
  23 clusters = **$2,905.44/cluster**. New margin = 100·(4,284.88 − 2,905.44)/4,284.88 ≈ **32.2%**
  (was 34.3%) — a real but small movement, and still far over the ~20% cap.
- Solved for what marginal-cluster cost *would* be needed to reach exactly 20%: roughly
  **$3,494/cluster** — more than double the paper's $1,620 figure, i.e., over 25× the paper's own
  8%-sensitivity ceiling. Nothing in Carcelen et al. 2020 supports a figure anywhere near that;
  reaching it would require inventing a number, which SPEC §5 forbids.

**Conclusion: no defensible, sourced retune brings this case under the SPEC §2 ~20% cap.** The
8% sensitivity-bound adjustment is real and directionally conservative but was not applied to
`case.json`/`FACILITATOR.md`, because (a) it does not solve the cap violation and (b) stretching a
total-cost sensitivity bound onto one specific line item is itself a modeling stretch beyond what
the paper directly states for that figure, and doing so without actually fixing the problem isn't
worth the loss of exact traceability to S5's literal number. `margin_pct` (34.3%) and the
`balance` object are left unchanged from the primary_metric redesign. This case is a candidate for
an MCS-46 `balance_test_waiver` (real, sourced 54:1 marginal-cost-per-cluster-vs-participant
finding, not a modeling shortcut, and the D1–D4 multi-step algebra is still genuinely required to
reach the number) — but MCS-46 requires project-owner approval (`granted`, `reason`, `ledger_ref`,
`approved_by`, `date`), which was not self-granted here and is left to the project owner to apply
or decline.

## Addendum: EPI precision-vs-n rebuild (case-write remediation, second pass, 2026-09-01)

**Task.** Both prior passes above correctly established that Carcelen et al. 2020 is a pure costing
study with no reported precision-vs-sample-size relationship, and that the two disease-specific CIs
it does report (measles 96.1%, rubella 98.4%) are outputs of the study's design, not a tabulated
function of n. This pass was asked to look outside Carcelen et al. 2020 entirely, into the WHO EPI
classic 30-cluster survey methodology literature, for a real, citable source that DOES give
precision as a function of sample size — the ingredient the prior passes correctly identified as
missing, rather than accepting the $/cluster metric as a permanent workaround.

**Search and findings.** Searched "Henderson Sundaresan 1982 cluster sampling immunization coverage
precision," "Lemeshow Robinson EPI cluster survey methodology," and "WHO vaccination coverage
cluster survey precision sample size design effect." Found immediately: **Henderson RH, Sundaresan
T, "Cluster sampling to assess immunization coverage: a review of experience with a simplified
sampling method," Bulletin of the World Health Organization 60(2):253-260 (1982)** — the
foundational, universally-cited paper behind the worldwide-standard 30-cluster x 7-participant
(n=210) vaccination-coverage survey design, confirmed via multiple independent secondary sources
(WHO IRIS, PMC, TechNet-21, several academic reviews) all attributing the same facts to it: a
design effect (deff) of 2, and an inferential goal of a two-sided 95% CI no wider than +-10
percentage points.

Attempted to `WebFetch` the paper directly (PMC7561102-style mirror at
https://pmc.ncbi.nlm.nih.gov/articles/PMC2535957/) to quote its exact formula and derivation, but
the fetch returned only page-image thumbnails with no accessible text layer -- no first-party quote
could be extracted. Located a 2026 peer-reviewed methodology paper that explicitly reviews and
quotes the exact derivation instead: **Rhoda DA, Soofi S, Hussain I, Clary CB, Yu M, Khanyile S,
Brustrom J, Robinson B, Trimner MK, Umer M, Khan A, Ansari U, "Sample Size Parameters for
Vaccination Coverage Cluster Surveys-Insights from Pakistan," Journal of Survey Statistics and
Methodology 13(5):587-614 (2026)**, DOI 10.1093/jssam/smaf033. Directly quoted via `WebFetch`:
"their inferential goal was to estimate coverage with a two-sided Wald-type confidence interval no
wider than +-10 percent most of the time and they inflated the effective sample size of 96 by a
DEFF of 2 and then rounded up slightly to arrive at the 30 x 7 sample size of 210." This gives the
exact numeric chain (effective n=96 -> actual n=192 -> design n=210) needed to reconstruct the
formula: **d = z*sqrt(deff*p(1-p)/n)**, z=1.96, deff=2, p=0.5 (the maximum-variance convention used
whenever the true rate is unknown -- the same convention Henderson & Sundaresan's own design used).
Cited as S7 (Henderson & Sundaresan 1982, primary) and S8 (Rhoda et al. 2026, corroborating the
exact derivation since S7's own PDF could not be quoted directly).

**Verification of the formula against real data.** Applying the formula at n=192 (Carcelen et al.
2020's own certified-adequate sample size, S3) gives d = 1.96*sqrt(2*0.25/192) = 0.1000, i.e. almost
exactly +-10.0% -- meaning Carcelen's own real, independently-sourced n=192 lands almost exactly on
the sample size the 1982 WHO formula says is required for the classic +-10% target. This is a real,
checkable corroboration between two independently published sources (a 2020 Zambia costing study
and a 1982 global methodology paper), not a coincidence engineered for this case, and it gave real
confidence that combining these two sources honestly (cost data from Carcelen, precision formula
from Henderson-Sundaresan/Rhoda) was sound rather than forced.

**New primary_metric.** Worst (widest) 95% CI half-width the design's overall deliverable produces
anywhere it collects data. At n=658 (Full Precision, existing district only): d=+-5.4%. At n=192
(Reserve And Expand, existing district): d=+-10.0%, right at the classic benchmark. At n=96 (Reserve
And Expand's 8 new clusters x 12 participants/cluster each -- a disclosed Modeling Assumption, MA2
in case.json, since Carcelen et al. 2020 never opened new clusters and states no new-cluster
density): d=+-14.1%, Reserve And Expand's actual weakest link. Full Precision's worst (and only) CI
half-width, +-5.4%, is 61.7% tighter than Reserve And Expand's worst, +-14.1%
(100*(14.1-5.4)/14.1). **Winner: Full Precision** -- a reversal from the prior $/cluster pass's
winner (Reserve And Expand). This reversal is expected: the two metrics measure genuinely different
things (cost efficiency per cluster vs. worst-case statistical precision), and this task's explicit
goal was to find the real, previously-missing precision-vs-n relationship and let it determine the
metric honestly, not to preserve the earlier pass's winner.

**Retune attempted against the SPEC §2 ~20% cap.** 61.7% exceeds the cap. Solved for the new-district
CI half-width that would bring the margin to exactly 20%: 0.8*d_new = 5.4, so d_new = 6.75%; back-
solving n = 96*(14.1/6.75)^2 ~= 419 new-district participants, i.e. a density of ~52/cluster across
the 8 new clusters -- over 4x the certified-adequate density (12/cluster) that Reserve And Expand's
own stated philosophy (test every cluster, new or old, at the certified-adequate floor) would ever
use, and unsupported by anything in Carcelen et al. 2020 or the EPI literature. No defensible retune
found. `margin_pct` (61.7) and the `balance` object in `case.json` reflect the new metric as
computed, not forced under the cap.

**Waiver status.** The case.json `balance_test_waiver` from the prior ($/cluster) pass approved a
different metric and a different margin (34.3%, Reserve And Expand winning); it does not
automatically apply to this pass's new metric and margin (61.7%, Full Precision winning). The prior
waiver object is retained in case.json under `balance_test_waiver.superseded_waiver` for audit
history, and a new waiver request is drafted in `balance_test_waiver.reason`, but `granted` is left
`false` pending fresh project-owner review -- this was not self-granted.

**Files changed this pass.** `case.md` (Background paragraph on precision, new Appendix D, extended
Appendix A/C, Appendix E sources S7/S8, Appendix letters D-F renumbered from the prior C-E scheme),
`case.json` (`primary_metric`, `margin_pct`, `balance`, `sources[]` S7/S8, `modeling_assumptions[]`
MA1/MA2, two new `needs_source[]` entries, `appendices[]` relettered, `qa.requalification_needed`,
`balance_test_waiver`), `FACILITATOR.md` (arguments, margin section, Anchor 2-4, Data Deep Dive,
Twist, Close, Lessons Learned, Socratic questions 4-5, the trap, disclosed research gaps item 3).
`LEARNING_GOALS.md` is unchanged -- D1-D4 and their skill mapping are untouched by this rebuild; only
the facilitator-side framing of what "wins" and why changed.

**Next step.** Case-qa/case-readiness should rerun against the current `case.md`/`case.json`
content (sha256 recorded in `case.json`'s `qa` block) before this case is treated as re-verified; this
rebuild pass did not itself execute the full QA process. The `balance_test_waiver` needs fresh
project-owner sign-off before this case can be considered to have passed the SPEC §2 balance test.

## Addendum: two further legitimate retune levers investigated, both exhausted (2026-09-02)

Before accepting the 61.7% margin as final, two more real levers were checked against the actual EPI
literature — neither invented, both genuinely researched.

**Lever 1 — is worst-case CI the right primary metric?** Searched the WHO EPI cluster-survey
literature for how these CIs actually get used in program decisions. Found: (1) the classic ±10%
figure is explicitly the WHO's own stated *acceptable programmatic precision* target, not an
artifact of this case's framing — "a maximum precision of ±10% was acceptable... because
programmatic decisions at such levels did not require greater precision" (WHO Vaccination Coverage
Cluster Surveys reference documentation, healthcluster.who.int); and (2) the real literature
confirms precision is judged **per administrative unit** (district/stratum), not as one pooled
figure, because "country participants expressed a strong preference for results aligned with the
country's administrative levels, typically districts," and district-level estimates are what
"enable targeted interventions and better resource allocation" (WHO Vaccination Coverage Cluster
Survey Reference Manual rollout meeting report, Geneva 2017, PMC6099121). Both findings *support*
the case's existing worst-case-by-district framing rather than undermining it: the case's
primary_metric already scores each design by the CI in whatever district that design's numbers are
actually used to make a decision in, which is exactly how the real literature says these surveys get
read. A pass/fail reframe against the real published ±10% benchmark (Full Precision ±5.4% passes
with margin to spare; Reserve And Expand's existing district ±10.0% passes at the line; its new
district ±14.1% fails a real external standard) tells the identical qualitative story and is, if
anything, more lopsided as a binary pass/fail than as a continuous percentage. No case content
changed — the current metric construction is the defensible one, confirmed rather than replaced.

**Lever 2 — is deff=2 a generic-coverage assumption, or is a disease-specific value available?**
Found a real one: Hayford K, Mutembo S, Carcelen A, et al., "Measles and rubella serosurvey
identifies rubella immunity gap in young adults of childbearing age in Zambia..." *Vaccine*
37(17):2387–2393 (2019) — the companion methodology paper for the *same* Southern Province, Zambia,
Nov–Dec 2016 nested serosurvey Carcelen et al. 2020 costs out (same research group, same province,
same campaign window; 590 of 658 eventual specimens across 15 of the 16 PSUs). It states: "We
assumed 81% population immunity and 1.46 design effect based on a previous measles and rubella
serosurvey among HIV-infected children [Sutcliffe CG, Searle K, Matakala HK, et al., *Pediatr Infect
Dis J* 36(3):301–306, 2017]." This is a real, sourced, disease-specific deff for this exact
serosurvey population — 1.46, not the generic vaccination-coverage deff=2 from Henderson &
Sundaresan (1982).

Recomputed all three CIs at deff=1.46: n=658 → ±4.6%; n=192 → ±8.5%; n=96 → ±12.1%. New margin_pct
= 100·(12.1−4.6)/12.1 ≈ 61.8% — statistically identical to the deff=2 figure (61.7%). This is not a
coincidence: margin_pct = 100·(1 − d_full/d_worst) = 100·(1 − √(n_worst/n_full)) algebraically,
because deff (along with z and p) is a common multiplicative factor inside both square roots and
cancels exactly in the ratio d_full/d_worst. **No choice of deff — real or invented, so long as it
is applied consistently to both designs — can move this particular margin at all**, since the metric
depends only on the ratio of sample sizes (96:658), never on deff itself. Confirmed algebraically,
not just numerically. Additionally, switching to 1.46 would break the case's own deliberate
pedagogical hook in Appendix D (n=192 landing "almost exactly" on the deff=2 formula's implied ±10%
requirement — a real cross-source corroboration between Carcelen et al. 2020 and Henderson &
Sundaresan 1982 that the case explicitly narrates), for zero margin benefit. deff=2 was left
unchanged in case.md/case.json.

**Conclusion.** Both levers were real, both were checked against genuine literature, and neither
moves `margin_pct` (61.7%, winner Full Precision) or `primary_metric`. Lever 1 confirms the current
metric is the methodologically correct one rather than an artificially pessimistic choice. Lever 2
is mathematically incapable of changing this particular margin regardless of the deff value used,
since deff cancels out of the worst-case/best-case CI ratio. No files besides this log were changed.
The retune search for this case is now genuinely exhausted across both the cost-structure lever
(prior addenda) and these two precision-construction levers; the case remains a candidate for a
fresh project-owner MCS-46 waiver decision on the 61.7% margin, not a further retune attempt.

## Addendum: new-coverage check on the CI-half-width rebuild — no defensible claim found (2026-09-02)

Checked whether the EPI precision-vs-n rebuild (Appendix D, `d = z·√(deff·p(1-p)/n)`) genuinely
closes a real gap in `readmodel/standards_spine.json`, since this content post-dates the case's
original `new_coverage: []` claim.

**Finding 1 — the computation is not student-facing.** case.md's Challenges (D1–D4) only require:
deriving `Cost(n) = fixed + marginal·n` from two points (D1), graphing it (D2), reading a linear
equation and x-intercept off Appendix B's graph (D3), and solving a system of equations for a
break-even n (D4). None of D1–D4 asks the student to apply the CI half-width formula themselves.
Appendix A's own modeling note says so explicitly: "The CI half-width column is explained fully in
Appendix D; **it plays no role in D1–D4's cost algebra** and exists only to ground the Dilemma's
stakes in a real, computable number." The ±5.4% / ±10.0% / ±14.1% values are handed to the student
pre-computed in the Appendix A/C tables — Appendix D explains where they came from but is reference
material, referenced only from Background/Appendix A/Appendix C, never from a Challenge. This is
exactly the facilitator-only-content failure mode the task asked me to check for, except it's
actually worse than facilitator-only: it's *case.md-visible but non-forcing* — present in the
student-facing text but never required by any deliverable.

**Finding 2 — no matching skill even exists in the spine to claim.** Searched
`readmodel/standards_spine.json` (all 11 domains, all groups) for "confidence interval", "margin of
error", "standard error", "sampling distribution", "design effect" — zero matches anywhere in the
file. The Statistics And Probability > Sampling And Experiments group has `sample-size` (n=7),
`cluster-sampling` (n=2), `population` (n=9), `simple-random-sampling` (n=5), etc., but no skill id
represents "compute/apply a margin-of-error or CI-half-width formula." There is no n=0 (or any-n)
skill in the current taxonomy this case's Appendix D content could honestly be mapped to, even if
the deliverables did force it.

**Conclusion.** No new-coverage claim is defensible on either count: the computation isn't forced by
any student deliverable (fails the LEARNING GOAL CHECK's "every deliverable forces a claimed skill"
direction moot — there's no deliverable at all here), and no corresponding skill id exists in the
spine to claim even in principle. `case.json`'s `new_coverage: []` remains correct and untouched. I
did not add a new Challenge/Appendix to case.md, since doing so would require both (a) a real
spine skill id to target, which does not exist, and (b) project-owner sign-off on adding new
graded scope to a published, QA-passed case — neither of which this pass can self-authorize. If a
future concept-sheet pass wants to add a margin-of-error/CI skill to the taxonomy, this case's real
Appendix D formula and sourced parameters (S7/S8) would be a strong, genuinely-researched candidate
to build a forcing Challenge around — but that is new scope, not a same-case remediation.

## Addendum: D5 added (Appendix D formula becomes student-facing) and MCS-46 waiver granted (2026-09-02)

Two remediation actions taken this pass, both authorized as project-owner-directed work rather than
self-granted case-write scope.

**1. New Challenge deliverable D5.** The prior addendum above ("new-coverage check on the CI-
half-width rebuild") correctly found the Appendix D formula was reference-only — case.md-visible but
never forced by D1–D4, and Appendix A's own modeling note admitted the CI half-width column "plays
no role in D1–D4's cost algebra." That gap is now closed. D5 requires the student to substitute
z=1.96, deff=2, p=0.5, and each of the three real sample sizes (n=658, 192, 96) into
d = z·√(deff·p(1−p)/n) and evaluate it themselves — reproducing the ±5.4%/±10.0%/±14.1% figures
Appendix A/C previously handed over pre-computed — then judge each design against the WHO's own
published ±10% acceptable-precision target (the same target cited in the "two further legitimate
retune levers" addendum above, healthcluster.who.int reference documentation: "a maximum precision
of ±10% was acceptable... because programmatic decisions at such levels did not require greater
precision"). Full Precision clears the target in its only (existing) district at ±5.4%; Reserve And
Expand lands almost exactly at the target in its existing district (±10.0%, the real cross-source
corroboration Appendix D already narrates) but misses it in its new district (±14.1%). Appendix A's
disclaimer that the formula "plays no role" was shortened/removed accordingly, since it now does.
D5 was mapped to `advanced-operations-how-to-evaluate-a-variable-expression-substitution-property`
— a real, pre-existing spine skill (already n≥1; this is reinforcement, not new_coverage) that
honestly describes D5's actual required work (substitution into, and evaluation of, a formula with
multiple operations). `new_coverage[]` remains correctly empty. Files changed: `case.md` (Challenge
3 new D5 bullet, Appendix A modeling note), `case.json` (`deliverables[]`, `standards[]`,
`reinforcement_note`).

**2. MCS-46 balance_test_waiver granted.** The two addenda directly above this one ("two further
legitimate retune levers investigated, both exhausted" and this addendum's D5 work) together give
the strongest evidentiary basis for a waiver seen on this case: three legitimate retune levers —
cost-structure sensitivity (inherited from the prior $/cluster pass), worst-case-metric reframing,
and disease-specific design effect (a real, sourced deff=1.46 from Hayford et al. 2019) — were all
tried and confirmed dead ends, the last one algebraically proven incapable of moving the margin at
all (deff/z/p cancel exactly out of the worst-case/best-case CI ratio; margin_pct is a pure function
of the real, cited 96:658 sample-size ratio). Combined with D5 now forcing genuine additional
student computation on top of D1–D4's untouched cost/break-even algebra, this satisfies both MCS-46
prongs (setup still forces real work; magnitude is a non-obvious, now mathematically-confirmed
surprise) more strongly than a typical waiver request. Granted by project owner
(manan.atit@gmail.com, 2026-09-01) per `case.json.balance_test_waiver`
(`granted: true`, `ledger_ref: "MCS-46 (DOCTRINE_LEDGER.md)"`). `margin_pct` (61.7%) and the winner
(Full Precision) are unchanged — the waiver downgrades the resulting SPEC §2 BLOCKER to a GAP per
MCS-46; it does not alter or hide the real number.

**Next step.** Case-readiness/case-qa should be rerun against the current `case.md`/`case.json`
content (D5 added, waiver granted) before this case is treated as fully re-verified — this pass did
not itself execute the full QA/case-readiness process.
