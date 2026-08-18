# QA_REPORT — Pattern Rights

## case-readiness run — 2026-08-15
**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS

### Placeholder / source audit (pre-gate)
`grep -c NEEDS_SOURCE cases/pattern-rights/case.md` → 0 unresolved tokens. `RESEARCH_LOG.md`
records 11/11 placeholders closed (P01-P11), with its own verification block confirming
`placeholders remaining: 0`, no orphan citation markers, no INCOMPLETE or LOW-confidence
sources. `case.json.standards[]`/`new_coverage[]` re-checked against `readmodel/standards_spine.json`
by the script itself (T1-10, T1-11 below) — both resolve cleanly; `new_coverage[]` is a genuine
subset (`discrete-mathematics-binomial-coefficient` and its how-to sibling, both n=0 at authoring
time, per `LEARNING_GOALS.md`'s coverage-overlap note explaining why Pigeonhole is claimed in
`standards[]` but deliberately left out of `new_coverage[]`).

### Artifacts built this run
- `cases/pattern-rights/sensitivity_model.py` — new. Contract: `PARAMS`, `FLEX`, `evaluate()`,
  plus helper functions `config_counts()`/`capsule_counts()`/`pigeonhole_thresholds()`/`yardage()`
  reproducing D1-D4 exactly. No `evaluate_twist()` — this case's Twist is a sequencing move (D1/D2
  computed before D4, not a changed assumption), documented in the file's own docstring. Verified
  by the script's own `__main__` self-check: reproduces every figure in `case.json.derived`
  (config counts 4/8, capsule counts 15/66, pigeonhole thresholds 5/9, repeat geometry 3×43744=131232,
  yards/$ 50.47/43.74, margin 13.3%) to the recorded precision, asserted, exits clean.
- `cases/pattern-rights/published/Pattern Rights - Interactive.html` — new, built from
  `templates/interactive_shell.html` per `templates/INTERACTIVE_HTML_CONTRACT.md`. JS port of
  `sensitivity_model.py` (`configCounts`/`capsuleCounts`/`pigeonholeThresholds`/`yardage`/
  `evaluate`/`evaluateCapsulePerDollar`) verified against the Python model with Node (both emit
  identical A/B figures to full float precision — see this run's transcript). 9-term glossary
  (`Fundamental Counting Principle`, `Combination`, `Permutation`, `Binomial Coefficient`,
  `Pigeonhole Principle`, `Factorial`, `Set`, `Subset`, `Configuration`), every URL fetched and
  confirmed live this session (mathsisfun.com, cuemath.com; the ck12.org Pigeonhole PLIX page
  blocks the fetch tool with a 403 bot-block but was confirmed by an exact title-and-content match
  in live search results — ck12.org is already an allowlisted, previously-vetted domain). Four
  Working Notebook steps (D1-D4) call the live JS functions; nothing pre-computes or prints
  `balance_test.margin_pct` (13.3) as a static literal anywhere outside `<script>` — verified by
  T1-18's leak scan (PASS).

### Fixes applied to clear BLOCKERs found by this run
- `FACILITATOR.md`: Socratic questions 1-5 were each wrapped across two source lines, so the
  `T1-13` regex (which requires the trailing `?` on the same physical line as the numbered marker)
  matched 0 of them. Un-wrapped each onto a single line — no wording changed.
- `FACILITATOR.md`: no "45-minute Socratic plan" section existed (`MCS-16`, `SPEC §7.3`, BLOCKER).
  Added a 9-row timed table (0:00-0:45) naming the TWIST's drop time explicitly at 0:38.
- `case.json`: no `cohort_bands[]` (`MCS-25`, GAP). Added three bands (8-12 / 13-18 / 19-24) each
  with a note on what changes in facilitation at that size.
- Interactive HTML: initial draft used `class="gterm"` on the Appendix A/B/D inline source-citation
  brackets (`[S1]`...`[S5]`), which is reserved for the glossary hover/hyperlink contract. Not a
  gate failure (the JS `GLOSSARY` data object is the sole source of truth T1-19 counts against,
  per the contract doc's own gotcha note), but corrected to plain `<a href>` citations before
  shipping so the `.gterm` class stays exclusively the glossary's own vocabulary.

### Tier 1 — structural (19 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | all seven structural sections present |
| T1-02 | PASS | Overview word count and numeral texture both clean |
| T1-03 | PASS | binary dilemma, opens "You are Priya Deshmukh" |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-F lettered, ordered, no orphans |
| T1-07 | PASS (1 POLISH) | final appendix's 5 labels are verbatim spine labels |
| T1-08 | PASS | 0 unresolved `{{NEEDS_SOURCE}}`; all 5 sources complete with valid confidence grades |
| T1-09 | PASS | both balance arguments written; margin 13.3% (under the 20% cap, inside the 15% one-sidedness watch but not over it) |
| T1-10 | PASS | standards/new_coverage resolve in the spine; new_coverage is a genuine subset |
| T1-11 | PASS | every deliverable maps to a claimed skill and vice versa (mutual reachability) |
| T1-12 | PASS | T3 tier matches numeric/deliverable load |
| T1-13 | PASS (after fix) | anchor ladder complete, Twist named, timed plan added, 5 Socratic questions now regex-visible |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json numbers |
| T1-15 | PASS | no staleness/drift in published artifacts |
| T1-16 | PASS | `case_md_sha256` recorded and current |
| T1-17 | PASS (after fix) | 3 cohort bands declared |
| T1-18 | GAP (not blocking) | 2 orphan numbers (37, 39) — both from the shell's own boilerplate header comment citing "MCS-37"/"MCS-39" doctrine codes, not case data; same accepted false-positive class as CSS/SVG decimals. No leak of `balance_test.margin_pct` or any verdict. |
| T1-19 | PASS | 9 glossary terms, all `https://` to allowlisted domains |

**BLOCKER (0)** · **GAP (1, non-blocking, see T1-18 above)** · **POLISH (1, T1-07's parse-count note)**

### Tier 2 — simulated play (6 probes)
NOT RUN this session (out of scope for this task — Tier 1 gate only, per the task instructions).

### Tier 3 — human dry-run
NOT RUN.

`case.json.qa` set to `{"state": "TIER1_PASS", "verdict": "PASS", "run_on": "2026-08-15",
"blockers_open": 0, "gaps_open": 1 (post-fix), "case_md_sha256": "5fae96b738a3bf83..."}`.
`status: "qa"`.

**Next step:** Run Tier 2 (`skills/case-readiness/scripts/tier2_probes.py --case pattern-rights`)
before `case-publish`.

---

## case-readiness run — 2026-08-17 (Tier 2)
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 reconfirmation
`python3 skills/case-readiness/scripts/tier1_structural.py --case pattern-rights` re-run this
session: 17 PASS / 2 GAP / 0 FAIL, same two non-blocking GAPs as the 2026-08-15 run (T1-14's lone
`20.0` orphan number — the "SPEC §2 20%" cap referenced in prose, not case data; T1-18's `37.0`/
`39.0` orphans — the interactive shell's own boilerplate header citing MCS-37/MCS-39 doctrine
codes). `case_md_sha256` unchanged (`dc1e4fe0c8...`) — `case.md` has not drifted since Tier 1
cleared. VERDICT: TIER1_PASS, 0 blockers.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent (dispatched by the orchestrating task, not this session) chose A (The Straight Set), correctly named the case's own labeled primary metric (yards/$ of engraving setup cost, D4a), and reproduced the arithmetic (32,808 yd ÷ $650 = 50.47 yd/$ vs. ÷$750 = 43.74 yd/$, ~15.4% margin) plus the supporting D1–D3 figures. Named the strongest counter-argument (Half-Drop dominates D4b/D1/D2), the most sensitive assumption (MA2's $100 engraving premium), the deliberately-ignored aside (Appendix A's 17-wallpaper-groups note, correctly identified as explicitly non-load-bearing), and the least-supported number ($750 Half-Drop cost). Reached the intended answer by the intended route — the primary-metric route, not a guess. |
| P2 both-sides | **PASS** | Argument for A is fully quantitative and grounded directly in the case's own labeled primary metric (D4a): identical total yardage per engraving (32,808.4 yd, both schemes share cylinder circumference and screen life) ÷ setup cost, A wins 50.47 vs 43.74 yd/$. Argument for B is independently quantitative, not a concession: 8 configs vs 4 (D1), 66 capsule subsets vs 15 (D2, >4x), for only a 15% cost premium — a genuine "design variety per dollar" case the primary metric doesn't capture. Neither argument is numberless or a throwaway concession. B's argument collapses specifically at the question "what does the case's own designated primary metric say, given both schemes print identical total yardage?" — i.e., at D4, which is the case's built-in Twist question, not an artifact of a weak B argument. Margin (13.3% per case.md's stated basis / 15.4% per the yd/$ delta itself — both under the 20% SPEC §2 cap) is a real number, not a paper one. |
| P3 trap check | **PASS** | Machine screen: `FACILITATOR.md` names an explicit trap ("A Hero who finishes D1 and D2 will stop there and recommend The Half-Drop... they will never divide either scheme's output by its setup cost") describing a concrete learner *action* (stopping after D1/D2, never reaching D4), not merely a hard step. Independent read of `case.md` alone: Challenge 3's D1→D4 ordering puts the two figures that favor B (configs, capsule subsets) before the primary-metric step D4 that favors A, so a hurried, competent reader naturally forms a B-leaning impression before reaching the deciding calculation — the same trap the guide names. Guide anticipates the actual trap. |
| P4 twist integrity | **PASS** | (1) Twist invalidates a real room position: a room that has voted/leaned B on D1+D2's configuration/capsule counts is shown its basis doesn't measure the case's own primary metric, and D4 reverses the recommendation to A. (2) Twist survives every defensible reading of the stated assumptions: the "identical total yardage per engraving" claim rests on Appendix A's licensing-terms table, which states the 27" repeat height and thus the cylinder circumference as *shared, fixed* between schemes (not ambiguous), and on Appendix B's single sourced screen-life figure (30,000 m) applied identically to both under MA1 — MA1's own stated Sensitivity note confirms it scales both schemes proportionally and cannot change the winner. The D1/D2-vs-D3 width-fitting ambiguity noted by the P1 cold-solve (3 columns across 54" width for Straight vs. 1 true tile for Half-Drop) affects D3's actual-units-printed figure, not D4's yardage-from-rated-run figure, so it does not touch the twist's mechanism. No unstated convention is load-bearing for the twist itself. |
| P5 sensitivity | **PASS_DISCLOSED** | `tier2_probes.py --probe 5 --flex 0.5`: base state A wins 50.47 vs 43.74 yd/$ (15.4% margin by the yd/$ delta). `screen_life_m` (MA1) does not flip the verdict at ±50% (scales both schemes identically, margin unmoved at 15.4%) — matches the case's own MA1 Sensitivity note. `setup_cost_straight_usd` (+50%) and `setup_cost_half_drop_usd` (-50%) DO flip the winner to B, and multiple flex directions blow through the SPEC §2 20% balance cap (margins from 30% to 130.8%). Both unstable params are recorded in `case.json.sensitivity_disclosure[]` with category **F** ("no current, scheme-specific engraving quote is publicly available — the real figure is a future vendor quote, not a research gap") and appear, matching that same disclosure, in `FACILITATOR.md`'s "Facilitator-only numbers → Sensitivity" section. Per the disclosure-aware pass state (2026-08-13 SKILL.md addendum), an instability that is disclosed with a recorded category and justification is PASS_DISCLOSED, not FAIL. |
| P6 data decay | **PASS** | All 5 `sources[]` URLs fetched live this session, all reachable, all still carry their cited figure: S1 (indigoandluxe.com) — "Most decorator fabrics are 54 inches wide per industry standards," confirms 54". S2 (finetex.net) — 27"/688mm, 1-color pricing $410.00–$470.00 across mesh grades, confirms the $410–$470 range. S3 (hanzeltd.com) — "screens used with water-based pastes may last for 30,000–50,000 meters," confirms the range. S4 (mathworld.wolfram.com) — "The wallpaper groups are the 17 possible plane symmetry groups," confirms 17 (supplemental, not load-bearing). S5 (linda-matthews.com) — "Resize the canvas to twice the width... The canvas size now becomes 400px wide by 200px high," confirms the doubling-of-width construction. All 5 accessed 2026-08-13 per case.json, re-verified live 2026-08-17 (4 days old) — well under the 365-day staleness flag. No BLOCKER, no silently-decayed figure.

**BLOCKER (0) · GAP (0 new — the 2 pre-existing Tier 1 GAPs above remain open, non-blocking) · FAIL (0)**

`case.json.qa` set to `{"state": "TIER2_PASS", "verdict": "PASS", "run_on": "2026-08-17",
"blockers_open": 0, "gaps_open": 2, "tier2": {"P1_cold_solve": "PASS", "P2_both_sides": "PASS",
"P3_trap_check": "PASS", "P4_twist_integrity": "PASS", "P5_sensitivity": "PASS_DISCLOSED",
"P6_data_decay": "PASS"}, "case_md_sha256": "dc1e4fe0c85c3293662141f9b847d7d897e666af379a46ec25351e40ccd1413f"}`.

**Next step:** `case-publish` may run — Tier 1 clean (0 blockers) and all six Tier 2 probes recorded
PASS or PASS_DISCLOSED, per this skill's `TIER2_PASS` gate.
