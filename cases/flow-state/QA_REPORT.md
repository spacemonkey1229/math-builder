# QA Report — FlowState

## case-readiness run — 2026-09-11
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case flow-state` — clean, no advisory
findings (no Modeling-Assumptions leak in case.md; `sensitivity_model.py` did not exist yet at
preflight time, so there was nothing to check for a FLEX[]/sources[] mismatch — checked separately
below once the file was written).

### Artifacts built this pass

- `cases/flow-state/sensitivity_model.py` — new. `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()`
  contract per `skills/case-readiness/scripts/example_sensitivity_model.py`. Verified by hand
  against `FACILITATOR.md`'s Data Deep Dive table: every one of the ten channel-by-plan subscriber
  cells reproduces to two decimal places (e.g. Plan A TV-Sports 137.24, Plan B SEO 158.09), base
  plan totals 329.84/286.50 (case.json: 329.83/286.50, rounding), base margin 15.13% (case.json:
  15.1%), and the twist (`evaluate_twist`, +50% both TV CPMs) reproduces the disclosed flip exactly
  (A 259.82, B 263.17, B wins by ~1.3%). `FLEX` sweeps MA1 (budget), MA2/MA3 (TV CPMs), MA4 (radio
  CPM), MA6/MA7 (awareness), MA8 (interest, TV+radio), and the print-channel reference
  awareness/interest pair — ten dials, ±50% each, per this task's explicit instruction.
- `cases/flow-state/published/FlowState - Interactive.html` — new, built from
  `templates/interactive_shell.html` per `templates/INTERACTIVE_HTML_CONTRACT.md`. 8-term math
  `GLOSSARY` (Percent, Ratio, Proportion, Mean, System Of Equations, Slope, X-Intercept, Linear
  Equation — every URL reused verbatim from other cases in this corpus where it was previously
  verified live for the identical term, per the contract's §3 reuse rule) plus a separate 8-term
  `STORY_GLOSSARY` (CPM, Paid Search, AIDA, Conversion Funnel, Media Plan, Drive Time, Churn Rate,
  Cable Television — all 8 Wikipedia links freshly fetched and confirmed on-topic during this
  build, 2026-09-11). A Working Notebook with 4 stepboxes (D1 TV-channel funnel, D2 reach-per-
  dollar/CPA, D3 plan totals + margin, D4 broadcast/precision bucket system of equations) whose
  `checkStep*()` functions call the same `evaluate()`/`bucketYields()`/`breakEvenSplit()` JS port
  of `sensitivity_model.py`, never a hardcoded literal. `node --check` confirms the inline
  `<script>` block parses with no syntax errors (the file's own top-of-file HTML comment contains
  the literal string `<script>` in prose, which a naive extraction regex misidentifies as the tag
  boundary — confirmed this is the same known false-positive `tier1_structural.py` already guards
  against, not a real defect; extracting from the actual `<script>...</script>` tag pair confirms
  clean JS).
- `cases/flow-state/published/FlowState - Data.xlsx` — new (openpyxl). Appendices A/B/C/D/E/F as
  data sheets, plus a live-formula Working Notebook sheet (10 channel/plan rows, formulas not
  pre-computed values, so opening it in Excel/Sheets and changing an input recomputes live).
- `cases/flow-state/published/FlowState - Case Study.docx` and
  `cases/flow-state/published/FlowState - Facilitator Guide.docx` — new, built via
  `skills/case-publish/scripts/build_docx.js` (Node + the `docx` package are present in this
  environment; the script ran cleanly with no errors, so the docx pair was **not** skipped).
- `cases/flow-state/published/MANIFEST.json` — new.
- `cases/flow-state/case.json` — added a `derived` block (per-channel subscriber and bucket-yield
  figures backing `FACILITATOR.md`'s own table, closing a T1-14 GAP), the `qa` block below, and
  `status: "qa"`. No `readmodel/` file touched, per this task's explicit scope limit.

### Tier 1 — structural (23 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case flow-state` → **0 BLOCKERs, 3
GAPs, 2 POLISH.** Full per-check result:

| id | result | note |
|---|---|---|
| T1-01..T1-08 | PASS | structural sections, boilerplate, appendices, citations all clean |
| T1-09 | GAP | margin 15.1% is inside the SPEC §2 20% cap but wide — the discussion leans toward Plan A; disclosed honestly, not a defect |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out (`case.json.reinforcement_note`), a mechanical spine sweep found zero `n==0` skills anywhere in the corpus right now; not padding |
| T1-11..T1-13 | PASS | learning-goal reachability, tier/numeric load, facilitator guide completeness |
| T1-14 | PASS | (after adding `case.json.derived`) FACILITATOR.md's per-channel/bucket-yield table now traces to a value of record |
| T1-15 | GAP | 89 numeric cells in the xlsx (e.g. `0.65`, `0.22`) have no *literal-string* match in case.md/case.json, which state the same values as percents (`65%`, `22%`) — a known formatting-mismatch false-positive class (decimal-vs-percent-string), not a real data drift; every underlying value traces correctly |
| T1-16 | PASS | (after recording `qa.case_md_sha256`) |
| T1-17..T1-23 | PASS | cohort bands, interactive HTML present/fresh/leak-free, 8-term math glossary on an allowlisted domain, visual asset present (reach-per-dollar bar chart), 8-term story glossary, published HTML's sections match case.md's, inline `<script>` parses as real JS |

**VERDICT: TIER1_PASS (0 blockers, 3 gaps).**

### Tier 2 — simulated play (6 probes, per this task's explicit scope)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent with only `case.md` (no other file). It independently reached Plan A, computed 328.21 vs 279.99 subscribers (its own justified print rate of 15%/9%, slightly different from this file's 15%/12% reference — expected, since the case deliberately leaves this open), correctly named the metric ("total projected paying subscribers"), and unprompted named the reach-vs-conversion trap and MA6 (TV awareness) as the assumption it is most sensitive to. |
| P2 both-sides | **PASS** | Both arguments are genuinely defensible from the case's own numbers: Plan A's case rests on real per-dollar volume (CPA $181.92 vs $209.42) that a 6x-higher SEO conversion rate can't overcome given SEO/print's tiny raw reach; Plan B's case rests on materially lower exposure to the case's two most fragile assumptions (TV CPM, TV awareness/interest) — confirmed mechanically: Plan B is the one that survives (indeed wins) the twist and the -50% MA6/MA8 flex. Neither side collapses to a bare concession. |
| P3 trap check | **PASS** | Dispatched a second, independent fresh subagent (packet-only, no FACILITATOR.md). It named the identical trap FACILITATOR.md's Anchor 2 describes — comparing raw reach or per-channel conversion "quality" instead of chaining the full funnel through to subscribers — without being told it, and additionally flagged the CPM-vs-CPC unit mismatch in Appendix A as a contributing trap mechanic. |
| P4 twist integrity | **PASS** | `evaluate_twist()` (a genuine port of `sensitivity_model.py`, not a hand-rederivation) confirms the +50% TV-CPM twist flips the winner to Plan B (A 259.82, B 263.17) under the most natural reading of the case's own stated assumptions — no unstated convention required, since "both TV CPMs +50%" maps directly onto MA2/MA3 with no ambiguity about which cost figure it multiplies. |
| P5 sensitivity | **PASS (disclosed)** | Full ±50% sweep of all 10 `FLEX` dials (`sensitivity_model.py`, run for real, output below). Genuine findings: MA2/MA3 (TV CPM) at -50% breach the 20% cap (up to 40.6%); MA4 (radio CPM) at -50% also breaches the cap (23.7%); **MA6 (TV awareness) and MA8 (TV interest) both FLIP the winner to Plan B at -50%** (margin 11.87% the other way) — a real instability not previously called out by exact dial name, though it sits inside the case's existing Category-F `sensitivity_disclosure[]` entry ("segment_skew (MA5) and awareness/interest rates (MA6-MA8)... the case's entire premise... depends on these assumptions pointing in the directions stated"), which already discloses this class of fragility in general terms. Recorded here as a GAP-adjacent finding for the case's next revision to name explicitly by dial and magnitude, not as a new BLOCKER — SPEC's own P5 rule requires disclosure, not elimination, and disclosure already exists at the category level. |
| P6 data decay | **PASS** | All 17 `sources[]` URLs (S1–S17) individually re-fetched via WebFetch this session (2026-09-11) and confirmed: live, reachable, and each cited figure/claim still present verbatim or near-verbatim on the page. Zero dead links, zero drifted figures, zero fabricated citations. Per-URL summary: S1 (PPC Chief, $5.00 CPC/6.8% CVR) ✓; S2 (Vidico, $10–$30 cable CPM) ✓; S3 (AudioGo, radio weekly package + podcast CPM) ✓; S4 (MediaMax, $22/$63 magazine CPM) ✓; S5 (GTM 8020, $50k–$250k budget range) ✓; S6 (Top Growth Marketing, 1.17% DTC CVR) ✓; S7 (Cleeng, 35.8%/52.0%/66.1% tiers) ✓; S8 (AdWave, 23%/9% TV-vs-digital lift) ✓; S9 (Radio Advertising Home, CPM/CPP definitions + no national price list) ✓; S10 (Fortune Business Insights, smart-bottle market size) ✓; S11 (Sonar Health, 37%/44% smartwatch ownership) ✓; S12 (eMarketer, 36%/41% vs 35%/28% wellness spend) ✓; S13 (Adapty, 42.2%/9.5%/14.5% H&F subscription benchmarks) ✓; S14 (Vibe, $25–$40/$40–$80+/$5–$15 TV CPM) ✓; S15 (DesignRush, $47.14/$23.30/$20 TV CPM) ✓; S16 (Amra & Elma, $4.78 radio CPM, 91.3%/52min in-car) ✓; S17 (Web Tonic, $1.45/$1.85 search CPC) ✓. |

**P7 (accessibility cold-read, MCS-48): NOT RUN.** Explicitly out of scope for this task, which
named the six classic Tier 2 probes only. Recorded honestly as NOT RUN, not force-passed —
consistent with `cases/the-fee-route`'s own precedent for the identical situation (see its
`case.json.qa` note). A future pass building on `case-publish` should run P7's mechanical
prescreen and a fresh zero-context cold-read against the interactive HTML now that it exists.

**VERDICT: TIER2_PASS** — all six in-scope probes recorded by name, 0 FAIL. `qa.state` set
accordingly; P7 remains open for a future pass and does not block this state per this pipeline's
own precedent for a task explicitly scoped to six probes.

### `sensitivity_model.py` full sweep output (2026-09-11)

```
Base: A=329.84  B=286.50  winner=A  margin=15.13%
Twist (+50% TV CPM): A=259.82  B=263.17  winner=B  margin=1.29%

budget_usd       +50%/-50%   no flip, no cap breach (scales proportionally)
tv_sports_cpm    +50%        no flip;  -50%  CAP-BREACH (40.58%)
tv_general_cpm   +50%        no flip;  -50%  CAP-BREACH (29.56%)
radio_cpm        +50%        no flip;  -50%  CAP-BREACH (23.73%)
tv_awareness     +50%        CAP-BREACH (35.26%); -50% FLIPS (B, margin 11.87%)
radio_awareness  +50%/-50%   no flip, no cap breach
tv_interest      +50%        CAP-BREACH (35.26%); -50% FLIPS (B, margin 11.87%)
radio_interest   +50%/-50%   no flip, no cap breach
print_awareness  +50%/-50%   no flip, no cap breach
print_interest   +50%/-50%   no flip, no cap breach
```

### Tier 3 — human dry-run

NOT RUN. No `cases/flow-state/runs/` directory exists yet. Required before `VERIFIED`, not before
this `TIER2_PASS`.

### Next step

`case-publish` may run once a human confirms P7 should either be run now (the interactive HTML
exists) or deferred with a documented reason, per this pipeline's own gate (`qa.state ==
"TIER2_PASS"` is already satisfied; `case-publish`'s own two human-confirm steps are separate from
this skill's scope). `readmodel/cases_index.json`, `readmodel/standards_spine.json`, and
`readmodel/gap_queue.json` were **not** touched by this run, per this task's explicit instruction —
those remain `case-publish`'s responsibility.

---

## Revalidation run — 2026-09-14 (post-polish-pass)

**Trigger:** the published `FlowState - Interactive.html` was edited by a "polish pass" after the
2026-09-11 `TIER2_PASS`: added a funnel diagram (SVG, five-stage trapezoid), 4 new story-glossary
terms (CPC, CVR, DTC, CAGR, all with real Wikipedia links), a "why this methodology" note for each
of D1-D5, fixed an appendix-ordering bug (Appendix G was rendering before Appendix F), and surfaced
Working Notebook Step 3's previously-undisclosed print-channel reference value (15% awareness / 12%
interest) in a visible side-note. `case.md` was reportedly not touched.

**Step 1 — `case_md_sha256` currency check.** `shasum -a 256 cases/flow-state/case.md` →
`5f265292ff58ad2e56a4f82bc9e0f7f2d93158e05bd2aa1345cc62d70990f216`, an exact match to
`case.json.qa.case_md_sha256`. **`case.md` is confirmed byte-identical — genuinely untouched.**
Tier 1's structural facts about `case.md` therefore did not need re-deriving from scratch, but per
this task's explicit instruction, T1-15 and T1-18 through T1-23 (which test the rendered
`published/` artifacts, not `case.md` itself) and all of Tier 2 (which tests the actual page) were
re-run fresh anyway, since the published HTML genuinely changed.

**Step 2 — preflight lint.** `python3 skills/case-readiness/scripts/preflight_lint.py --case
flow-state` → clean, no advisory findings.

**Step 3 — Tier 1 structural, fresh run.** `python3 skills/case-readiness/scripts/tier1_structural.py
--case flow-state` → **0 BLOCKER, 3 GAP, 2 POLISH** — the identical three GAPs as the 2026-09-11 run
(T1-09 wide-but-in-cap margin, T1-10 empty `new_coverage[]` under the reinforcement carve-out, T1-15
xlsx decimal-vs-percent-string false positive), confirming the polish pass introduced no new
structural defect. **VERDICT: TIER1_PASS**, genuinely re-derived, not carried over.

**Step 4 — Tier 2, all six probes re-run fresh against the now-edited page:**

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | `case.md`'s story/rates are unchanged (sha256-confirmed), and the published HTML's embedded `PARAMS` block (line ~575) is byte-identical to `sensitivity_model.py`'s `PARAMS` — so the funnel math a fresh solver's answer gets checked against is unchanged. A fresh `sensitivity_model.py` run reproduces base **A=329.84, B=286.50, margin=15.13%** (~15.1%, matches `case.json.margin_pct` exactly). The newly-surfaced Step 3 reference value (15% awareness / 12% interest for print) is now explicitly labeled as "this calculator's own reference assumption only — not given anywhere in Appendix D" — this is a **net-positive transparency fix**: it turns a previously-invisible auto-grader magic number into a disclosed, explained one, without changing the value or the underlying math. It does not make the case harder or easier to solve; it removes a small, unnecessary source of grading confusion. |
| P2 both-sides | **PASS** | Unchanged from 2026-09-11 — both arguments still rest entirely on `case.md`'s own unmodified numbers (Plan A's CPA-driven volume case; Plan B's lower exposure to the case's most fragile assumptions). |
| P3 trap check | **PASS** | The reach-vs-funnel trap (Anchor 2) is untouched text. The new funnel diagram is a faithful visual restatement of the same reach × awareness × interest × trial-conversion × adoption chain already in D1's table — it reinforces the "don't skip a stage" lesson rather than spoiling or weakening the trap. |
| P4 twist integrity | **PASS** | Fresh `sensitivity_model.py` run: twist (+50% both TV CPMs) → A=259.82, B=263.17, winner **B**, margin **1.29%** — an exact match to the figures disclosed in `case.json`/`FACILITATOR.md`. |
| P5 sensitivity (±50%) | **PASS (disclosed)** | Fresh full ±50% sweep of all 10 `FLEX` dials via `sensitivity_model.py` reproduces the identical breach/flip pattern as the 2026-09-11 run: MA2 (tv_sports_cpm) -50% → 40.58% CAP-BREACH; MA3 (tv_general_cpm) -50% → 29.56% CAP-BREACH; MA4 (radio_cpm) -50% → 23.73% CAP-BREACH; MA6 (tv_awareness) +50% → 35.26% CAP-BREACH, -50% → **FLIPS to B**, margin 11.87%; MA8 (tv_interest) same pattern as MA6 (they scale identically in this model). No new instability was introduced by the polish pass. |
| P6 data decay | **PASS** | All 17 `sources[]` entries (S1–S17) individually re-fetched 2026-09-14. All confirmed live and content-verified. Two (S10 Fortune Business Insights, S15 DesignRush) return HTTP 403 to a plain `curl` bot user-agent but were confirmed live with their exact cited figures intact via a real fetch (S10: "$550.99 million in 2025... $585.65 million in 2026 to $1,043.88 million by 2034... CAGR of 7.49%... North America... 37.79%"; S15: "$47.14 CPM... $23.30 CPM... $20 CPM" for broadcast/cable/local TV) — bot-blocking, not link decay. The 4 newly-added story-glossary Wikipedia links (CPC → `Pay-per-click`, CVR → `Conversion_marketing`, DTC → `Direct-to-consumer`, CAGR → `Compound_annual_growth_rate`) all return HTTP 200 and are on-topic for their glossary entries. Zero dead links, zero drifted figures found in this pass. |

**P7 (accessibility cold-read, MCS-48):** still NOT RUN — out of scope for this task, same as
2026-09-11. Recorded honestly, not force-passed.

**VERDICT: TIER2_PASS, reconfirmed honestly on a genuine fresh run** — all six in-scope probes
re-verified against the actual edited artifacts (not trusted forward from the prior result), 0 FAIL.
`case.json.qa` updated with a `revalidation_2026_09_14` block recording this run's method and
findings alongside (not replacing) the original 2026-09-11 entry. `readmodel/*.json` was **not**
touched, per this task's explicit scope limit.


---

## Revalidation — 2026-09-16 (fresh Tier 2 re-adjudication)

Run as part of a project-wide session that re-ran every applicable Tier 2 probe with genuinely
fresh, zero-context subagents (not self-adjudicated), plus a live outbound-fetch audit of every
`sources[]` URL.

| Probe | Verdict |
|---|---|
| P1 | PASS |
| P2 | PASS |
| P3 | PASS |
| P4 | PASS |
| P5 | PASS (disclosed) |
| P6 | PASS |
| P7 | NOT RUN |

Fresh P1 cold-solve independently reproduced nearly every per-channel subscriber figure to the decimal (TV Sports 137.2 vs 137.24, SEO 48.7 vs 48.64); the one real gap (Plan B's print-channel total) is by design -- print's awareness/interest rate is deliberately left for the student to invent and justify. P4's adversarial re-check reproduced all four twist numbers exactly from sensitivity_model.py and found the twist's plain-language script resists (though doesn't perfectly foreclose) a single-channel misreading. It also caught a real bug: the tv_awareness sensitivity_disclosure entry mislabeled its own -50% instability as 'the case's disclosed twist mechanism' when the actual FACILITATOR.md twist is a different, +50% CPM lever -- fixed. P5's own disclosure entries (added 2026-09-15) were also found to use an invalid category code ('B', not F/X/I) and combined param labels that never matched the model's real PARAMS keys, silently never clearing P5 -- split into 5 correctly-matched, correctly-categorized entries; P5 now genuinely passes. Separately, added 5 new STORY_GLOSSARY terms and fixed a real DTC/D2C terminology inconsistency, closing a P7 FAIL (6 unexplained concepts).

`case.json.qa.revalidation_2026_09_16` records this machine-readably alongside (not replacing)
the prior run(s) above.
