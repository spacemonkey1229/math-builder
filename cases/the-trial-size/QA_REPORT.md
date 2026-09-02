## case-readiness run — 2026-09-01

**State:** researched → structurally clean, **BLOCKED on SPEC §2 balance test**   **Verdict:** BLOCKED

### Tier 1 — structural (20 checks)

Remediation this session: removed a stray `## Appendices` wrapper heading that was tripping T1-04's
Challenge-5 boilerplate diff (same root cause as `the-repeat-match`: "Appendices" does not start
with the literal substring "Appendix" the T1-06 boundary regex requires, singular vs. plural
spelling). Added an `(SEE APPENDIX E)` reference from Background (was a GAP). Rewrote
`FACILITATOR.md`'s anchor ladder into real markdown headings (Intro/Launch/Anchor 1-4/Data Deep
Dive/Twist/Close/Lessons Learned/Standards Touched On), added a concrete Twist (the $1,620
marginal-cluster-cost figure's single-province basis, stress-tested against the source paper's own
8% sensitivity ceiling), added a 45-minute Socratic plan, and added `case.json.cohort_bands[]` (3
bands). Joined the 5 Socratic questions onto single physical lines so the mechanical count parser
can see them.

After these fixes, **every Tier 1 check passes except T1-09 (the balance test)**, which is a real,
substantive finding, not a formatting gap:

| id | result | note |
|---|---|---|
| T1-01 through T1-08 | PASS | structure, boilerplate, appendices, citations all clean |
| **T1-09** | **BLOCKER** | margin **34.3%** (loser-denominator convention: 52.3%), real and sourced, far over the SPEC §2 ~20% cap |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, accepted |
| T1-11 through T1-13 | PASS | learning-goal reachability, tier load, facilitator artifacts (anchor ladder, Twist, timed plan, 5 Socratic questions, trap) all clean |
| T1-14 | GAP | 3-4 residual "orphan" numbers are guide-only pedagogical figures (participant counts named in Socratic questions) or SPEC section references, not case data drift |
| T1-16 | GAP | hash not yet recorded — this case is not being promoted, so intentionally left unset |
| T1-17 through T1-20 | PASS | cohort bands, no published/ yet |

`VERDICT: BLOCKED (1 blocker, 3 gaps)` — the blocker is T1-09 alone.

### Why this is not a formatting problem: the real math

Primary metric: average total design cost per cluster of geographic coverage delivered, computed
identically for both options from real, directly-sourced figures (Carcelen et al. 2020, *PLOS ONE*,
a real published costing analysis of a measles-rubella serosurvey in Zambia — S1-S5, all HIGH
confidence, none derived/estimated):

- **Full Precision:** $68,558 total ÷ 16 clusters = **$4,284.88/cluster** (independently confirmed
  by the source paper's own stated average, "$4,285 per average cluster" — matches almost exactly).
- **Reserve And Expand:** $54,578 (16 clusters at the certified-adequate floor, S3) + floor($13,980
  ÷ $1,620) = 8 new clusters × $1,620 = $12,960 (a real $1,020 unspent remainder), for $67,538 total
  ÷ 24 clusters = **$2,814.08/cluster**.
- **margin_pct = 100·(4,284.88 − 2,814.08)/4,284.88 = 34.3%.**

This is the *second* metric this case has used. The original metric (statistical precision for A
vs. discrete new-cluster count for B) was already found by a prior remediation pass to be
uncomparable — the source paper never reports CI width as a function of sample size, so no honest
conversion factor exists between the two units. That pass correctly redesigned the metric around a
single real dollar unit the source paper itself computes (RESEARCH_LOG.md, "REDESIGNED 2026-09-01"
entry) rather than inventing a conversion.

### Retune attempted, and genuinely exhausted (RESEARCH_LOG.md, verified this session)

A prior session already ran a real retune attempt against this exact 34.3% finding before I began
work on this case, and I re-verified its reasoning and its two load-bearing citations (S1, S5) this
session rather than taking it on faith:

1. Checked whether $1,620/cluster (S5) is a Modeling Assumption with room to move. It is not — the
   source paper states it directly (not derived, not estimated); confidence HIGH.
2. Re-fetched Carcelen et al. 2020's cost-breakdown and sensitivity sections for a defensible,
   sourced basis to use a higher marginal-cluster cost for a genuinely new/unsurveyed district (the
   case's own narrative). The paper's $1,620 figure already includes social mobilization,
   personnel, materials and transport for a new cluster — not a bare per-diem that would obviously
   need a geography markup — and the paper was conducted entirely within one province, so no
   sourced geographic cost differential exists to apply.
3. The paper's own sensitivity analysis is the only lever with a stated, sourced bound: no cost
   driver moves the total by more than 8%. Applying that ceiling to the marginal-cluster cost
   ($1,620 → $1,749.60) drops the new-cluster count from 8 to 7 and moves the margin only to
   **~32.2%** — still far over the cap.
4. Solving for the marginal-cluster cost that *would* close the gap to exactly 20% gives
   **~$3,494/cluster** — more than double the sourced figure, over 25x the paper's own sensitivity
   ceiling. Nothing in the source supports a number anywhere near that; using it would be
   fabrication, which SPEC §5 forbids outright.

**No defensible, sourced retune brings this case under the SPEC §2 ~20% cap.** The lopsidedness is
structural to the real cited data (a genuine 54:1 ratio between the source paper's own
per-participant and per-cluster marginal costs), not an artifact of a modeling shortcut this
session could fix by adjusting a constraint.

### Disposition — left BLOCKED, not published, no waiver self-granted

Per this project's own hard line ("If a case's premise turns out to be un-fixable within the SPEC,
do not force a fake pass — leave it at its current stage, document why, and move to the next
case") and per MCS-46's own text ("requires project-owner approval... not self-granted"), **this
case is left at `status: researched`, `qa.state` unset, not promoted to `published`.** It is not
BLOCKED because it is unsound — the math, the sourcing, and every structural check are clean — it
is blocked because SPEC §2's ~20% balance cap is a real, substantive rule this case's real, honestly
researched numbers do not clear, and closing that gap would require either inventing a number this
session has no license to invent, or the project owner explicitly granting the same kind of
per-case MCS-46 waiver already recorded for `the-phasing-call` (a landslide margin driven by real,
sourced data, with genuinely required multi-step work to reach the number) and `prove-it-scales`.

**Recommendation for the project owner:** this case is a strong MCS-46 candidate on the same
reasoning already accepted for those two cases — (1) the D1-D4 algebra (deriving the fixed cost,
graphing it, reading the Budget-Remaining x-intercept, solving the break-even system of equations)
is genuinely hard, multi-step work regardless of which option wins, and (2) the size of the
54:1 marginal-cost ratio, and therefore the size of the margin, is not guessable from the premise —
a student has to actually compute it. If approved, `case.json.balance_test_waiver` should be added
(`granted: true`, `reason`, `ledger_ref: "MCS-46 (DOCTRINE_LEDGER.md)"`, `approved_by`, `date`) and
this case re-run through `case-readiness` — Tier 1 will then pass cleanly on the record already
established here, and Tier 2 (untouched this session) still needs to run before `TIER2_PASS`.

### Next step

Held at `researched`, structurally clean, one substantive BLOCKER (T1-09) pending an explicit
project-owner MCS-46 decision. Tier 2 probes were not run — Tier 1 must clear first.

---

## case-readiness continuation — 2026-09-01 (waiver grant + Tier 2)

**MCS-46 waiver GRANTED.** The project owner (manan.atit@gmail.com) explicitly approved a
per-case `balance_test_waiver` for this case's 34.3% margin, on the same reasoning already
accepted for `the-phasing-call` and `prove-it-scales` (real, honestly researched figures; a
genuinely exhausted retune; a magnitude that is not guessable without computing it; genuinely
hard multi-step algebra regardless of winner). `case.json.balance_test_waiver` added
(`granted: true`, `approved_by: "manan.atit@gmail.com"`, `date: "2026-09-01"`,
`ledger_ref: "MCS-46 (DOCTRINE_LEDGER.md)"`).

**Tier 1 re-run** (`tier1_structural.py --case the-trial-size`): **TIER1_PASS**, 0 blockers, 4
gaps. T1-09 now downgrades from BLOCKER to GAP — the waiver is on file and recognized by the
checker. Remaining GAPs: T1-10 (empty `new_coverage[]`, reinforcement carve-out, already
accepted), T1-14 (3 guide-only orphan numbers — pedagogical figures, not case-data drift), T1-16
(hash not yet recorded, expected pre-publish).

**Authored `cases/the-trial-size/sensitivity_model.py`** (did not exist before this session) —
models Cost(n) = F + 30n, the certified-adequate floor, and the floor()'d new-cluster count
exactly as D1/D4 and the balance object specify. `PARAMS`/`FLEX` cover the case's 6 real sourced
dollar/count dials (this case has no `modeling_assumptions[]` — every figure is sourced, S1-S5).
Verified against case.json: base A=$4,284.88/cluster, B=$2,814.08/cluster, margin 34.3% (primary
convention) / 52.3% (loser-denominator convention) — both match case.json/FACILITATOR.md exactly.

### Tier 2 — six probes, all recorded

| Probe | Verdict | Note |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent with no access to this file, FACILITATOR.md, or case.json — only `/tmp/coldsolve-the-trial-size/PACKET.md`. It independently re-derived F=$48,818, the $13,980 freed budget, floored to 8 new clusters (not 8.63), and chose B with correct arithmetic and a named metric ("incremental geographic coverage per dollar, subject to a precision floor"). It also independently flagged S5 ($1,620/cluster) as the least-supported, most load-bearing figure in the case — matching this project's own Twist and retune-attempt finding exactly, without having read either. |
| P2 both-sides solve | **PASS** | Mechanical pre-screen clean (argument_a and argument_b both carry real numbers, neither is a bare concession). Argument A (tightest read on a mapped district, matches the source paper's own stated $4,285/cluster average almost to the dollar, zero unspent budget) is genuinely defensible and does not collapse under the obvious pressure question ("why does reach matter more than precision in a district we're already committed to?") — it has a real qualitative answer even though it loses on the quantified metric. Argument B (34.3% cheaper per cluster of real coverage, 8 new clusters funded) does not collapse either. Neither side is a paper tiger. |
| P3 trap check | **PASS** | The most plausible wrong path a hurried student produces — treating the freed $13,980 as buying proportional coverage instead of flooring by the real $1,620/cluster marginal cost (8.63 clusters vs. the real 8) — is exactly the trap FACILITATOR.md names. The independently-dispatched P1 cold-solve subagent did the flooring correctly on its own, but flagged the same $1,620 figure as the case's weakest point, confirming the guide is watching the right number. |
| P4 twist integrity | **PASS** | The twist (the $1,620 marginal-cluster cost's single-province basis, stress-tested against the source paper's own 8% sensitivity ceiling) is a straightforward, mechanically checkable sensitivity result, not dependent on an ambiguous reading of a stated convention — re-verified this session: applying the 8% ceiling moves the margin from 34.3% to ~32.2%, matching FACILITATOR.md exactly. It genuinely invalidates the naive "so it's basically free money" read of Option B without making Option A the obvious winner. |
| P5 assumption sensitivity | **PASS** | `tier2_probes.py --probe 5 --flex 0.5`: 0 flips, 0 cap breaches across all 4 declared FLEX dials (`total_budget`, `marginal_participant_cost`, `cert_min_n`, `marginal_cluster_cost`) at ±50%. Reserve And Expand (B) remains the winner under every swing tested; the margin moves (widens to ~52% under a -50% marginal_cluster_cost swing, narrows to ~26% under +50%) but never flips. Stable. |
| P6 data decay | **PASS** | All 6 source URLs fetched live this session. S1-S5 (all the same PLOS ONE article, Carcelen et al. 2020) are reachable and every load-bearing value ($68,558/n=658; 16 clusters; 192 children certified-adequate; $30/participant marginal; $1,620/cluster marginal) is confirmed still present verbatim on the live page, quoted directly. S6 (Frontiers in Public Health, context-only, not load-bearing) is reachable and on-topic. 0 dead links, 0 stale values. |

**VERDICT: TIER2_PASS.** All six probes recorded, 0 FAIL. `case.json.qa.state` set to `TIER2_PASS`.
Ready for `case-publish`.

---

## case-readiness run — 2026-09-02 (requalification after EPI precision-vs-n rebuild)

Re-gating after the case was rebuilt around real WHO EPI 30-cluster survey methodology (Henderson
& Sundaresan 1982, Rhoda et al. 2026) combined with Carcelen et al. 2020 cost data, with a new D5
deliverable requiring students to compute the CI half-width themselves, and a fresh, superseding
MCS-46 waiver for the new 61.7% margin.

`preflight_lint.py`: clean, no advisory findings.

### Tier 1 — structural (20 checks)

| id | result | note |
|---|---|---|
| T1-01 – T1-06 | PASS | |
| T1-07 | GAP | `standards[]` claims a skill absent from the final appendix: "How to evaluate a variable expression (Substitution Property)" |
| **T1-08** | **BLOCKER** | SPEC §5 — `case.json` declares assumptions but `case.md` has no visible 'Modeling Assumptions' block |
| **T1-09** | **GAP (correctly downgraded)** | margin 61.7% on the new CI-half-width metric, cap ~20%, but the fresh MCS-46 waiver (granted 2026-09-02, `approved_by: manan.atit@gmail.com`, `ledger_ref: MCS-46`) is on file and complete, and the checker recognized it — **not** left as BLOCKER |
| T1-10 | GAP | empty `new_coverage[]`, reinforcement carve-out already accepted |
| T1-11 – T1-13 | PASS | |
| T1-14 | GAP | 2 numbers in FACILITATOR.md (7.1, 403.0) have no home in case.md/case.json |
| **T1-15** | **BLOCKER ×5** | every published artifact (MANIFEST.json, Case Study.docx, Data.xlsx, Facilitator Guide.docx, Interactive.html) was built before the last edit to its source (case.md / FACILITATOR.md) — the rebuild's D5 content is not in the packet students would download. Also a GAP: 12 numbers in the published Facilitator Guide.docx orphaned from case.md/case.json. |
| **T1-16** | **BLOCKER** | MCS-11 QA hash stale — recorded hash is from the pre-rebuild pass, actual hash reflects the rebuilt case.md |
| T1-17 | PASS | |
| **T1-18** | **BLOCKER** | published Interactive.html is stale relative to case.md (same rebuild, not yet rebuilt) |
| T1-19, T1-20 | PASS | |

**VERDICT: BLOCKED — 8 blockers, 5 gaps.** Confirmed: T1-09 correctly downgraded to GAP (waiver
present and complete) — the fresh MCS-46 waiver is doing its job. But 7 *other* BLOCKERs exist
(T1-08 ×1, T1-15 ×5, T1-16 ×1, plus T1-18 restates one of the T1-15 staleness findings), all
independent of the waiver and all caused by the rebuild landing in case.md/FACILITATOR.md without
a corresponding `case-publish` rebuild and without the QA hash being refreshed.

Per SKILL.md: **Tier 2 does not start until Tier 1 is otherwise clean.** Not run this pass.

### Tier 2 — six probes
NOT RUN. Tier 1 is not otherwise clean (7 non-waived BLOCKERs).

### Tier 3 — human dry-run
NOT RUN.

### Disposition
`case.json.qa.state` set to `DRAFT` (regressed from the prior `TIER2_PASS`, which described the
pre-rebuild content — see that state's own `requalification_needed` flag, now realized). Hand back
for remediation, not for `case-readiness` itself to fix:

1. **T1-08** — add a visible `## Modeling Assumptions` section to case.md.
2. **T1-15 / T1-16 / T1-18** — re-run `case-publish` to regenerate all 5 published artifacts from
   the current case.md/FACILITATOR.md, and refresh the MCS-11 QA hash.
3. **T1-14 / T1-15 GAP** — trace FACILITATOR.md's/the published guide's orphan numbers (7.1, 7.3,
   25.0, 40.0, 96.1, 98.4, 403.0, 2814.08, 4284.88, 4285.0, 12960.0, 67538.0) back to case.json —
   several (4284.88, 4285.0, 12960.0, 67538.0) look like stale pre-rebuild cost-per-cluster figures
   left over from the metric this case no longer uses; confirm and remove or relocate into
   `case.json.derived`.
4. **T1-07** — either add the Substitution Property skill's appendix reference or drop it from
   `standards[]`.

**Next step:** Fix the BLOCKERs above (case-publish rebuild covers most of them), then re-run
`case-readiness` from Tier 1.

---

## case-readiness run — 2026-09-02 (Tier 1 reconfirm + full Tier 2, first run)

Tier 1 reconfirmed clean after the prior pass's remediation (case-publish rebuild, hash refresh).
All six Tier 2 probes run for the first time against the current content: WHO EPI precision
framing, the new D5 CI-computation deliverable, and the MCS-46 waiver on the 61.7% margin.

`preflight_lint.py`: not re-run this pass (no content changes since last clean run).

### Tier 1 — structural (20 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-trial-size`
sha256(case.md) = `1e51691d38...` (matches `case.json.qa.case_md_sha256` — hash current)

| id | result | note |
|---|---|---|
| T1-01 – T1-08 | PASS | |
| T1-09 | GAP | margin 61.7% (cap ~20%), fresh MCS-46 waiver on file and complete (`ledger_ref: MCS-46`, `approved_by: manan.atit@gmail.com`, `date: 2026-09-01`) — correctly downgraded, not a BLOCKER |
| T1-10 | GAP | empty `new_coverage[]`; reinforcement carve-out (`case.json.reinforcement_note`) accepted |
| T1-11 – T1-13 | PASS | |
| T1-14 | GAP | 2 numbers in FACILITATOR.md (7.1, 403.0) have no home in case.md/case.json — guide-only derived figures, should move into `case.json.derived` |
| T1-15 | GAP | 5 numbers in published Facilitator Guide.docx (7.1, 7.3, 25.0, 40.0, 403.0) same orphan-number class as T1-14, not a staleness finding this pass — all published artifacts are current |
| T1-16 – T1-19 | PASS | |
| T1-20 | POLISH | no image/chart/map in published HTML; not required |

**VERDICT: TIER1_PASS — 0 blockers, 4 gaps** (all four pre-existing/carried forward, none new).

### Tier 2 — six probes (all run for the first time on this content)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Blind solve from `/tmp/coldsolve-the-trial-size/PACKET.md` alone reached: F=$48,818 (D1, from the two real data points), Cost(n)=48,818+30n; R(n)=19,740-30n with x-intercept n=658 (D3 — the point Full Precision's own sample size exhausts the budget); break-even system (D4) also resolves to n=658, confirming D3/D4 are internally consistent restatements, not contradictory; D5 computed d=1.96·sqrt(2·0.25/n) for n=658/192/96 giving **±5.40%/±10.00%/±14.1%**, matching the case's stated figures exactly. Correctly named the metric as worst-case (weakest-link) CI half-width across whichever district(s) a design actually samples, and correctly concluded Full Precision wins (5.4% < WHO's own ~10% target vs. Reserve And Expand's worst reading at 14.1%, which misses it). Strongest counter-argument identified: Reserve And Expand is the only option returning any data at all from an entirely unsurveyed district. Most sensitive assumption named: MA2 (12 participants/cluster new-district density, which sets n=96). Reached the intended answer by the intended route, not by shortcut. |
| P2 both-sides | **PASS** | Neither side collapses. Best case for A: the existing district gets an interval nearly twice as tight as the WHO benchmark, at zero risk of unspendable/unusable data. Best case for B: its existing-district reading (±10.0%) still clears the classic WHO benchmark, and it is the only option returning any real evidence at all from a district with zero prior coverage — for campaign dose-allocation decisions, "some data" can outweigh "no data" even at a wider interval. B's real weakness is narrow and specific (the new district's ±14.1% misses the target), not a wholesale concession — the packet genuinely supports both pitches. |
| P3 trap | **PASS** | Blind guess (before reading FACILITATOR.md): a hurried solver treats the $13,980 freed by Reserve And Expand as buying *proportional* new-district precision/coverage, not recognizing clusters and participants sit on different cost and precision curves (precision scales as sqrt(n), not linearly with dollars). FACILITATOR.md's trap section names this exact mistake as its primary trap, plus two others (treating the shared fixed cost as "wasted" money; assuming more clusters = better *overall* precision when precision is per-district, not averaged). The primary trap is a direct match. |
| P4 twist | **PASS**, with one caveat flagged for authors | Twist (cluster-split invariance: 4 clusters × 24 participants vs. 8 × 12 give the *identical* ±14.1%, since the formula depends only on total n) invalidates the naive room-position that "more, smaller clusters must mean worse precision." The core mathematical claim is sound and survives every reading of the stated CI formula. Caveat, not a BLOCKER: the twist's hypothetical (reallocating the same freed $13,980 across fewer/bigger new clusters) is never reconciled against Appendix C's stated cost structure, where the $1,620 marginal cost is per-*cluster*-opened with no stated per-participant cost inside a new cluster — under a literal reading, 4 clusters would cost only $6,480, not consume the same $13,980, so the "same budget, different split" framing in the twist's own hypothetical is under-specified. This doesn't undermine the twist's actual mathematical point (which needs no budget arithmetic to be true) and the twist is discussion-only, not a graded deliverable, so this is a POLISH-level note for a future revision, not a P4 FAIL. |
| P5 sensitivity | **FAIL (stale artifact)** | `cases/the-trial-size/sensitivity_model.py` still implements the **superseded** $/cluster metric (its own docstring says so): base result `{A: -4284.88, B: -2814.08}`, winner **B**, margin **-34.3%** — this is the pre-2026-09-01-rebuild metric and directly contradicts `case.json.balance_test`'s current primary metric (worst-case CI half-width, winner **A**, margin **61.7%**). The mechanical script reported this as a PASS; that PASS is not trustworthy because it validates a metric the case no longer uses. Manual re-derivation of the *actual* current metric's only genuine flexible assumption (MA2's 12/cluster new-district density) at ±50% (6 and 18 participants/cluster → n_new = 48 and 144) gives margins of 73.0% and 53.2% respectively — winner stays Full Precision in both directions, consistent with the case's own "exhaustively tested, invariant" claim in the T1-09 waiver text — but this had to be done by hand. `sensitivity_model.py` must be rebuilt against the current `evaluate()` contract (worst CI half-width per design, FLEX=["ma2_new_cluster_density"]) before this probe can be trusted mechanically again. |
| P6 data decay | **PASS** | All 8 `sources[].url` entries fetched live and reachable, none moved, all cited values confirmed still present verbatim: S1-S5 (Carcelen et al. 2020, PLOS ONE) — cost $68,558/n=658, 16 clusters, cert-min n=192, $30/participant, $1,620/cluster all quoted directly on the page. S6 (Brenzel et al. 2026, Frontiers in Public Health, context-only) reachable, topic matches. S7 (Henderson & Sundaresan 1982, Bull WHO) reachable; full text is page-image-only (matches the case's own disclosed limitation in FACILITATOR.md — not a fresh finding). S8 (Rhoda et al. 2026, J Survey Stat Methodol) reachable, open access, quotes the exact effective-n=96→actual-n=192→design-n=210/deff=2 derivation verbatim. |

**MECHANICAL RESULT (script):** 0 probes failed mechanically. **ADJUDICATED RESULT: 5 PASS, 1 FAIL (P5)** — Tier 2 is not clean.

### Tier 3 — human dry-run
NOT RUN.

### Disposition

`case.json.qa.state` stays `TIER1_PASS` (not `TIER2_PASS` — P5 is a genuine FAIL, not a formality).

**Next step:** Rebuild `cases/the-trial-size/sensitivity_model.py` against the current CI-precision
`primary_metric` (contract: `evaluate(params) -> {"A": -worst_CI_halfwidth_A, "B":
-worst_CI_halfwidth_B}`, `FLEX = ["ma2_new_cluster_density"]` — MA1's p=0.5 is provably
non-load-bearing since it cancels out of the A/B ratio, per the algebraic proof already in
`case.json`'s T1-09 waiver text), then re-run `tier2_probes.py --probe 5` and re-append its verdict.
Once that single rebuild is done, all six probes are genuinely PASS and `TIER2_PASS` can be set.

## P5 finalization — 2026-09-02

`sensitivity_model.py` was rebuilt to model the case's current WHO-EPI CI-precision `primary_metric` (the prior version tested the superseded $/cluster metric and its "PASS" was not trustworthy). Rebuilt script's base case reproduces the case's own margin (61.8% vs. case.json's 61.7%, rounding only) and winner (Full Precision). `tier2_probes.py --probe 5 --flex 0.5` now confirms: MA1 (p) ±50% never flips the winner (p cancels algebraically out of the ratio); MA2 (density_per_cluster) ±50% gives margin range 53.2%–73.0%, no flip — matching the manual hand-check from the prior QA pass exactly.

**Final state: TIER2_PASS.** All 6 Tier 2 probes PASS. `case.json.qa` updated accordingly (state/verdict/tier2.P5). Case is ready for `case-publish`.
