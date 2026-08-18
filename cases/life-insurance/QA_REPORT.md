# QA Report — Life Insurance

## case-readiness run — 2026-08-17

**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS

### Tier 1 — structural (19 checks)

Run via `python3 skills/case-readiness/scripts/tier1_structural.py --case life-insurance`.

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview numerals cleared (see `overview_numerals_cleared[]`); one load-bearing "20" (a specific term length) was removed from the Overview during this run rather than cleared, since a student could otherwise read it as the D2 answer |
| T1-03 | PASS | Dilemma binary, opens "You are Jake Johnson." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | 5 appendices (A–E), no orphans |
| T1-07 | PASS (POLISH noted) | 18 verbatim spine labels parsed in Appendix E; POLISH: all 18 came from bulleted lines, none from a separator-run line — not a defect, just noting the parser's other code path went unexercised here |
| T1-08 | PASS | every number cited (sources[] S1–S5) or a declared Modeling Assumption (MA1–MA5); legacy `verbatim`/`publicly verifiable` claim check n/a — this case does not claim its figures are a real company's actual product data, only real published market averages |
| T1-09 | PASS | balance test: both arguments written, margin 3.3% (≤ 20% cap) |
| T1-10 | PASS | `case.json` schema valid; all 18 standards[] ids resolve in the spine; `new_coverage[]` non-empty (4 ids, all live n=0 as of this run) — no legacy-conversion carve-out needed |
| T1-11 | PASS | learning-goal mutual reachability: 0 unmapped deliverables, 0 unreachable skills (see LEARNING_GOALS.md) |
| T1-12 | PASS | tier T4 vs. numeric load: Modeling Assumptions block present (5 assumptions), consistent with T4 |
| T1-13 | PASS | full 11-anchor ladder present in order, Twist section present (not N/A), 5 Socratic questions (one-line, question-mark-terminated), trap named, 45-minute timed plan with 7 rows and the twist-drop moment named |
| T1-14 | GAP | CONTINUITY: 1 orphan number in FACILITATOR.md ([7.0]) — false-positive from "Section 7" (a SPEC.md cross-reference), not a drifted figure. No action needed; matches the same benign pattern seen on other converted cases (e.g. a-coachs-dilemma's "MCS-37" false positive) |
| T1-15 | PASS | published HTML built after case.md's/FACILITATOR.md's latest edits |
| T1-16 | PASS | QA hash current: `f7a1d4be85116af53c47ca97235ad36c2d585b3fdcc6762836cc828731f9b2f5` |
| T1-17 | PASS | 3 cohort_bands[] declared (Full/Compressed/1:1-pair) |
| T1-18 | GAP | CONTINUITY: 1 orphan number in the interactive HTML's markup ([37.0]) — false-positive from a code-comment cross-reference to "MCS-37" (the doctrine id for the leak-check rule itself), same benign pattern as T1-14's finding. Leak-check itself: PASS — no `balance_test`/`margin_pct` literal printed outside a `<script>` computation |
| T1-19 | PASS | 9 glossary terms (≥8 required), all allowlisted domains (mathsisfun.com, khanacademy.org, ck12.org), hover+hyperlink wired, Appendix E cross-checked |

**BLOCKER (0):** none.
**GAP (2):** T1-14, T1-18 — both benign cross-reference-number false positives (SPEC.md "Section 7", "MCS-37"), not drifted figures. No fix required; documented here for the record per T1-14/T1-18's own intent (make orphan numbers visible, not necessarily wrong).
**POLISH (1):** T1-07 — noted above.

### Tier 2 — simulated play (6 probes)

**NOT RUN.** This case has not yet been through Tier 2. `case.json.qa.tier2` records all six
probes as `NOT RUN`, which is a real, honest state, not a pass. Next step for whoever picks this
case up: run `python3 skills/case-readiness/scripts/tier2_probes.py --case life-insurance` and
dispatch the cold-solve/both-sides/trap-check subagents per SKILL.md.

### Tier 3 — human dry-run

NOT RUN.

---

## Regression self-test

Not re-run in this session (no edits to `tier1_structural.py` itself). See
`skills/case-readiness/scripts/selftest_tier1.py` for the standing regression suite.

---

## Independent Tier 1 gate re-run — 2026-08-17 (post-conversion verification)

Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case life-insurance` from the
repo root to independently verify the converter's self-reported TIER1_PASS.

Result: **TIER1_PASS** — 19 checks run, 17 PASS, 2 GAP, 0 FAIL, 0 BLOCKER. 1 iteration used (no
fixes required).

- T1-14 GAP: orphan number `7.0` in FACILITATOR.md — confirmed the same benign "Section 7"
  cross-reference false positive already documented above. No change needed.
- T1-18 GAP: orphan number `37.0` in the interactive HTML's prose/markup — confirmed the same
  benign "MCS-37" cross-reference false positive already documented above. No change needed.
- T1-10 (new_coverage vs. live spine): re-checked `new_coverage[]` (calculus-sequence,
  discrete-mathematics-recursive-formula,
  discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence,
  discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula) against the live
  `readmodel/standards_spine.json` at gate time — PASS, all 4 still uncovered, no collision from
  concurrent batch runs.
- T1-07 POLISH: unchanged — 18/18 spine labels parsed from bulleted lines.

No BLOCKERs at any point; no case files were modified by this verification pass. Matches the
self-reported outcome exactly. Next step remains Tier 2:
`python3 skills/case-readiness/scripts/tier2_probes.py --case life-insurance`.

---

## case-readiness run — 2026-08-17 (Tier 2)

**State:** TIER1_PASS → Tier 2 attempted   **Verdict:** BLOCKED (Tier 1 clean; Tier 2 finds 1 real
BLOCKER on P6)

### Tier 1 — reconfirmed clean this run

Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case life-insurance`: 19
checks, 17 PASS, 2 GAP (T1-14, T1-18 — same benign "Section 7"/"MCS-37" cross-reference
false-positives already documented above, unchanged), 0 FAIL, 0 BLOCKER. `VERDICT: TIER1_PASS`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve chose B (term), correct arithmetic (17yr window x $55,000 + $374,000 = $1,309,000 → rounds to $1,300,000; scale 2.6; term $93.60/mo x 240mo = $22,464; whole life $1,154.40/mo ≈ 12x term), named its metric (cost-efficiency of meeting the stated 17-year coverage need). Reached the position via the case's own required D1→D2 route, not a lucky guess. |
| P2 both-sides | **PASS** | Both options have real, independent numeric arguments. A: whole life's dividend-inclusive rate (4.65%) beats the best CD (4.50%), plus a $1.3M permanent death benefit vs. term's 20-year-only benefit, plus a 3% guaranteed floor. B: term is ~12x cheaper in annual premium ($93.60/mo vs. $1,154.40/mo), matches the family's stated 17-year time-bound need exactly, and against whole life's *own guaranteed* 3% floor the CD's guaranteed 4.50% wins outright. Neither argument reads as a concession. A's case does collapse — at the specific "guaranteed vs. dividend" question — but that collapse is the twist's designed job, not a sign the pre-twist balance was fake; both sides had real content to argue up to that point. |
| P3 trap check | **PASS** (mechanical pre-screen FAIL is a script false-negative, see below) | Read case.md cold, independent of FACILITATOR.md: the most plausible wrong path is exactly the one the guide names — a hurried student takes D4's rate comparison (4.65% vs 4.50%) at face value and concludes whole life is "basically tied, not a bad deal," without connecting it back to the ~12x premium-pool-size gap D2/D3 already computed. This matches FACILITATOR.md's named trap verbatim. **Script defect found:** `tier2_probes.py`'s trap-screen regex `\b(will|most|learners|students|never notice|quietly|assume|optimi[sz]e|forget|miss|skip|default)\b` requires the exact word "assume"; the guide's trap text uses "silently **assumes**" (conjugated), so the word-boundary match fails and the probe mechanically FAILs on a real, present, on-point behavioral clause. This is a `tier2_probes.py` regex bug (missing conjugated forms of "assume"), not a case defect or a FLEX-scoping issue — recommend widening the regex to `assum\w*` in a future script fix. Recorded here per SKILL.md so the false-fail is visible, not silently overridden. |
| P4 twist | **PASS** | (1) The twist invalidates the real, room-plausible "whole life's rate is basically as good as a safe CD" position. (2) It survives the case's own stated assumptions under both a sequential and simultaneous reading: `case.md` never states the dividend is guaranteed, only that it is "declared by the insurer" (Appendix D) — consistent with, not contradicted by, the twist's "not guaranteed" framing; MA5's 3% guaranteed rate is already given in the case (used by D3), so the twist introduces a new *comparison*, not a new *number* or an unstated convention. No BLOCKER. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case life-insurance --probe 5 --flex 0.5`: base A=4.65%, B=4.50%, winner A, margin 3.3%. All 4 flexed runs (`guaranteed_growth_rate` ±50%, `cv0_multiple_of_premium` ±50%) leave winner and margin completely unmoved — no flip, no 20%-cap breach. This is structurally correct, not a scoping bug: D4's graded metric (`dividend_inclusive_rate` vs `cd_rate`) is cited data, correctly excluded from `FLEX[]` per SKILL.md's "only FLEX[] is swept" rule, and is mathematically independent of both genuine stated assumptions (which only feed D3's cash-value projection). Already disclosed in FACILITATOR.md's "Assumption-sensitivity disclosure" note, now updated with the actual (not predicted) result. |
| P6 data decay | **FAIL** | Fetched all 5 `sources[].url` (WebFetch + browser fallback for S4). **S1** (MoneyGeek): reachable, $36/mo term & $444/mo whole life at $500k/age~30 confirmed verbatim. PASS. **S2** (Ritter): reachable, multiple-of-income + DIME method (debt/mortgage + income×years) confirmed. PASS. **S3** (InsuranceGeek): reachable, but **does not carry the cited figure**. The live page (updated 2026-07-03) states the guaranteed 2–4% range correctly, but lists individual 2026 carrier *dividend* rates of 5.75%–6.60% (Northwestern Mutual 5.75%, Guardian 6.25%, Penn Mutual 6.00%, New York Life 6.40%, MassMutual 6.60%) and explicitly does not compute or state any combined "4.65% average" — the case's cited figure appears nowhere on its own source, and the real data on that page is dramatically higher than what was cited. This is the exact "resolves but no longer carries the figure" case SKILL.md calls worse than a dead link, and it is the case's **graded D4 primary-metric number** — not a peripheral fact. **BLOCKER.** **S4** (CNBC Select): HTTP 403 (Access Denied) via both WebFetch and a rendered browser fetch — cannot independently confirm or refute the cited 4.50% CD figure. Per MCS-21, reported as NOT VERIFIABLE (bot-blocked), not guessed at; flagged as a GAP needing re-verification via a different access path, not treated as a confirmed BLOCKER since the block is consistent with anti-bot behavior rather than evidence the page or figure changed. **S5** (Baily Insurance Agency): reachable, all 8 riders confirmed with matching cost figures (Return of Premium ~+30%; Waiver of Premium $2.50–$10/mo per $100k). PASS. |

**MECHANICAL RESULT (script):** 1 probe FAILED mechanically at pre-screen (P3, script regex bug —
overridden above after manual verification). P6 is a substantive FAIL found only by the fetch,
not by the mechanical pre-screen (P6 has no mechanical pre-screen; it is fully delegated).

**BLOCKER (1):** P6 — `sources[]` S3's cited "4.65% average dividend-inclusive crediting rate"
is not supported by, and is directly contradicted by, its own cited URL's live content (which
shows 5.75%–6.60% across named carriers, no stated average). This number drives the case's graded
D4 primary metric and the entire `balance_test`/twist framing (the "close 3.3% margin vs. a safe
CD" premise). **Exact fix needed (for `case-research`/`case-write`, not this skill):** either (a)
find a real, current source that actually states an aggregate dividend-inclusive average across
major mutual carriers and re-cite it, or (b) recompute the case's own average from the 5 real
carrier rates S3 does provide (5.75%, 6.00%, 6.25%, 6.40%, 6.60% → avg 6.20%) and propagate that
new number through `case.json.derived`, `balance_test`, `sensitivity_model.py`, `case.md` Appendix
D, and `FACILITATOR.md` — which would also materially change the balance-test margin (6.20% vs.
4.50% is a much larger, likely >20%-cap gap) and may require re-deriving the whole balance
argument from scratch, not just swapping one number in place.

**GAP (1 new, Tier 2):** P6 — S4 (CNBC Select) returned HTTP 403 on every fetch attempt; the
4.50% CD figure could not be independently reconfirmed or refuted. Recommend a follow-up fetch
from a different network/tool before the next gate run; not escalated to BLOCKER because the
failure mode (bot-block) does not itself indicate the source or figure changed.

### Tier 3 — human dry-run

NOT RUN. Blocked upstream by the Tier 2 P6 BLOCKER — `case-publish` cannot run until Tier 2 is
clean, per `qa.state == "TIER2_PASS"` gate (SKILL.md, "Two more defects found in later use," #5).

### Next step

Hand the P6 BLOCKER back to `case-research`/`case-write` per the exact fix above. Once S3 (and,
if needed, the balance test / sensitivity model / D4 text) is corrected, re-run
`python3 skills/case-readiness/scripts/tier2_probes.py --case life-insurance --probe 6` (and a
full Tier 2 re-run if the margin recompute changes any other probe's inputs) before `TIER2_PASS`
can be recorded. Separately, `skills/case-readiness/scripts/tier2_probes.py`'s P3 trap-screen
regex should be widened (`assum\w*`) so a future run doesn't need this manual override again.

---

## case-readiness run — 2026-08-17 (Tier 2 completion, post-S3-fix)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

The S3/balance retune recorded in `case.json.qa.tier2_fixed_2026_08_17` (dividend-inclusive rate
corrected from an unsupported 4.65% to a case-computed 6.20%; graded primary metric moved to
`guaranteed_rate_ceiling` (4.0%) vs. `cd_rate` (4.5%), margin 12.5%) is confirmed still current in
`case.json`/`case.md`/`FACILITATOR.md`/`sensitivity_model.py`. This run reconfirms Tier 1 and
closes out all six Tier 2 probes.

### Tier 1 — reconfirmed clean this run

`python3 skills/case-readiness/scripts/tier1_structural.py --case life-insurance`: 19 checks, 17
PASS, 2 GAP, 0 FAIL, 0 BLOCKER.

- T1-14 GAP: orphan number `7.0` in FACILITATOR.md — same benign "Section 7" cross-reference
  false positive documented in every prior run. No action needed.
- T1-18 GAP: orphan number `37.0` in the interactive HTML's markup — same benign "MCS-37"
  cross-reference false positive documented in every prior run. No action needed.

`VERDICT: TIER1_PASS` (0 blockers, 2 pre-existing benign gaps).

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh cold-solve (dispatched independently of this gate run, packet-only, no `FACILITATOR.md`/`QA_REPORT.md`/`case.json` access) chose **B (term)**. Arithmetic verified against `case.json.derived`: coverage need $374,000 + ($55,000 x 17) = $1,309,000 → rounds to $1,300,000 (exact match); scale factor 2.6; term $93.60/mo → $22,464 over 20 years (exact match); whole life $1,154.40/mo → $277,056 over 20 years (exact match, `whole_life_annual_premium` x 20). Named its metric explicitly ("20-year total premium cost to fully satisfy the stated coverage need... weighed against the family's disposable monthly cash flow") and named the correct strongest counter-argument (Neil outliving the 20-year term) and correct least-supported number (the 6.20% dividend-inclusive rate, unprompted — the solver independently flagged the same fragility the case's own Twist and `sensitivity_disclosure[]` name). One arithmetic imprecision: the solver computed cash value at age 65 as `13,852.80 x 1.03^38` (≈$42,589) where the case's own convention (`sensitivity_model.py:_cash_value`, matching `derived.cash_value_at_65_age39yrs`) computes `13,852.80 x 1.03^39` (≈$43,872) — an off-by-one in the recursive-index convention (whether CV\_0 or CV\_1 is the funded starting value). This affects a secondary D3 figure by ~3%, not the D1/D2 primary-metric arithmetic that drove the chosen option, and does not change the verdict or the route taken to it. Reached the position via the case's own required D1→D2 route (not a lucky guess), with correct arithmetic on the load-bearing numbers and a correctly named metric — meets the P1 pass criterion. |
| P2 both-sides | **PASS** | `case.json.balance.argument_a`/`argument_b` (and `case.md`'s "Balance Argument" section, identical text) both carry real, independent, current figures: A cites the real 2%–4% guaranteed range (top 4.0%) plus the real 5-carrier dividend data (5.75%–6.60%, avg 6.20%) plus the permanent-coverage/forced-savings case; B cites the CD's federally-guaranteed 4.50%, the real guaranteed-vs-dividend distinction, and the real ~12x annual-premium-dollar gap. Neither argument reads as a concession — both are built to be argued by a competent student in front of peers. A's case does collapse, but only at the specific guaranteed-vs-dividend question the Twist is designed to raise, and the graded margin (12.5%, guaranteed-vs-guaranteed) stays a real, defensible near-tie under the 20% cap up to that point — not a paper number. |
| P3 trap | **PASS** | `FACILITATOR.md`'s "The trap, named explicitly" section states the concrete wrong-path behavior: "Most students will only compare the two headline rates in D4 (6.20% vs. 4.50%) and conclude whole life is the clear winner," and explains why it's wrong (treating a non-guaranteed year-to-year dividend as equivalent to a federally-insured guarantee). This is a real, plausible action a hurried student takes, not merely a hard bit of math. Independent corroboration: the fresh P1 cold-solve, working from the packet alone, spontaneously flagged this exact fragility ("Least-supported number: the 6.20%... dividends can be changed or eliminated at insurer discretion") without having read the guide — direct evidence the trap is real and reachable from the case text, and that the guide's named trap is the one that will actually surface in a room. |
| P4 twist | **PASS** | (1) The twist invalidates the real, room-plausible "whole life's headline rate makes it the clear winner" position — the 45-Minute Plan and Twist section both describe the room reaching exactly this position (via D4's raw 6.20% vs. 4.50% comparison) before the twist drops at the 15-minute mark. (2) `FACILITATOR.md`'s own "Soundness check" explicitly re-derives the twist's effect under both a sequential reading (room works D1→D4 in order, twist lands directly against the number just used) and a simultaneous reading (a Hero who reads every appendix at once first) — under both, `case.md` never states anywhere that whole-life dividends are non-guaranteed, so the twist supplies genuinely new information under either reading and does not depend on an unstated convention. No BLOCKER. |
| P5 sensitivity | **PASS (disclosed)** | `python3 skills/case-readiness/scripts/tier2_probes.py --case life-insurance --probe 5 --flex 0.5`: base A=4.0%, B=4.5%, winner B, margin 12.5% (under the 20% cap). `guaranteed_growth_rate` and `cv0_multiple_of_premium` flexed ±50%: winner/margin completely unmoved (correct — neither dial feeds the graded D4 rate comparison, only D3's cash-value dollars). `guaranteed_rate_ceiling` flexed ±50%: **+50%** (6.0%) flips the winner to A (margin 33.3%, breaks the 20% cap); **-50%** (2.0%) keeps winner B but margin balloons to 125% (also breaks the cap). Both instabilities are recorded in `case.json.sensitivity_disclosure[]` (param `guaranteed_rate_ceiling`, category I) with a justification tying the flip directly to the case's own designed Twist mechanic (the +50% direction is structurally the same real number as the Twist's 6.20% dividend rate) — disclosed, not eliminated, matching the disclosure-aware PASS state (SKILL.md, 2026-08-13). Script confirms mechanically: `PASS (disclosed)`. |
| P6 data decay | **PASS** | Fetched all 5 `sources[].url` live via WebFetch (S4 additionally attempted via a rendered browser, see below). **S1** (MoneyGeek): reachable; confirms $36/mo term and $444/mo whole life at $500k coverage, age 30, verbatim. **S2** (Ritter): reachable; confirms the multiple-of-income and DIME methods (income x years + debts/mortgage), matching the cited method description. **S3** (InsuranceGeek): reachable; confirms the real 2%–4% guaranteed range and all 5 real 2026 carrier dividend rates (MassMutual 6.60%, New York Life 6.40%, Guardian 6.25%, Penn Mutual 6.00%, Northwestern Mutual 5.75%) verbatim, and confirms the page still states **no** combined/average dividend-inclusive rate — matching the case's own disclosure that 6.20% is a case-computed average of these 5 real rates, not a source-stated figure. The prior BLOCKER (an unsupported "4.65%" claim) remains fixed; today's figure is fully consistent with the live source. **S4** (CNBC Select): direct fetch (`WebFetch` and a rendered-browser fetch) both returned HTTP 403 (bot-protection, `errors.edgesuite.net`), consistent with the prior gate run's finding and not evidence of a changed page. Corroborated instead via search: the page's own indexed title is `"The best 5-year CD rates of August 2026: Up to 4.50%"`, and a search snippet independently states "CNBC Select's top picks range from 4.50% APY at Popular Direct... for August 2026" — matching the cited $4.50%$ APY figure and August-2026 date exactly. Reported per MCS-21 as reachable-but-bot-blocked with independent corroboration, not guessed at. **S5** (Baily Insurance Agency): reachable; confirms all 8 riders by name, the Return of Premium "~+30%" figure, and the Waiver of Premium "$2.50–$10.00/month per $100k" figure verbatim. No figure drift found on any of the 5 sources. |

**MECHANICAL RESULT (script):** P5 mechanically confirmed `PASS (disclosed)`. P6 has no mechanical
pre-screen (fully network-delegated); this run's fetch found 0 dead links and 0 figure drift.

**BLOCKER (0). GAP (0) new this run.**

### Tier 3 — human dry-run

NOT RUN. Tier 3 is not required for `TIER2_PASS` and is not blocking here — see SKILL.md's ladder
(`PUBLISHED` is reachable on Tier 1 + Tier 2 alone; `VERIFIED` requires a filed `RUN_REPORT`).

### Next step

Run `case-publish` on `life-insurance` — `qa.state == "TIER2_PASS"` is now satisfied. Schedule the
Tier 3 human dry-run separately once the case is published and assigned to a cohort.
