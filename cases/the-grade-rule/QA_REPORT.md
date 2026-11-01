# QA Report — Grade Rule

## case-readiness run — 2026-09-18

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (24 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 156 words; "size 16" removed after T1-02 correctly flagged it as a load-bearing numeral (it names the exact size that fails under Option A) — reworded to "a size" |
| T1-03 | PASS | Dilemma binary, opens "You are Devon Okafor." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form consistent |
| T1-06 | PASS | 7 appendices, all referenced (fixed after Appendix G was initially an orphan — added a Background cross-reference), no orphans |
| T1-07 | PASS | 7 final-appendix lines all verbatim spine labels |
| T1-08 | PASS | every number cited (S1–S2) or a declared Modeling Assumption (MA1–MA2) |
| T1-09 | PASS | margin 10.77%, well inside the 20% cap |
| T1-10 | GAP | `new_coverage[]` empty; `reinforcement_note` carve-out applies (live spine sweep found zero true `n==0` skills anywhere) |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T2 numeric load matches multi-step ratio/scale-factor comparison |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | derived figures cross-check clean |
| T1-15 | PASS | (a transient GAP on first run — "15.0"/"45.0" from the Socratic-plan timing labels — resolved by recording them in `case.json.derived`) |
| T1-16 | PASS | hash current after final edit round: `21480d68020e3d1719f83f65c9d2411f6814e76e782fd624c6178de08ed72ab4` |
| T1-17 | PASS | 3 cohort bands declared |
| T1-18 | PASS | interactive HTML present, fresh, leak-free |
| T1-19 | PASS | 8 math-glossary terms, allowlisted domains |
| T1-20 | POLISH | no diagram/chart in the published HTML — advisory only, never blocks |
| T1-21 | PASS | 9 STORY_GLOSSARY real-world terms, real https URLs |
| T1-22 | PASS | published HTML's sections match case.md's |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | connector-line check (no diagram connectors in this case) |

**BLOCKER (0)** · **GAP (1, accepted — reinforcement carve-out)**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh subagent, given only the leak-free packet, reproduced the case's own arithmetic exactly (point-specific factors, the shared 1.0417 dilation factor, the D3 predictions, the D4 fit-check misses at sizes 8/16, $3.91 vs. $7.21 labor costs) and correctly identified MA1 (fit tolerance) as most sensitive and MA2's 3:1 time ratio as least-supported. It recommended **B**, reasoning about the marginal cost of buying full coverage rather than the case's own literal D5 metric — a defensible position via correct arithmetic with a clearly named (if reframed) metric, and itself evidence the balance test is real. |
| P2 both-sides solve | **PASS** | Argument for A: the case's own primary metric, 10.77% edge, real numbers. Argument for B: guaranteed full-run fit, zero out-of-tolerance risk. Neither collapses — the P1 transcript independently built a strong case for both, including naming A's own genuine cost advantage on the literal metric even while recommending B on different grounds. |
| P3 trap check | **PASS** | A fresh subagent named the trap as: trusting D2's scale factor because it reproduces the run's endpoints almost exactly, without running D4's full point-by-point check on the middle sizes and non-bust landmarks. `FACILITATOR.md`'s trap section is updated to name this exact mechanical path explicitly, alongside the original conceptual trap (mistaking mathematical dilation validity for real-world fit). |
| P4 twist integrity | **PASS** | `sensitivity_model.py`'s `evaluate_twist()` confirms the tolerance-tightening twist (±0.5in → ±0.42in) flips the winner from A (10.77%) to B (35.42%) — a genuine, mechanically verified flip. The twist is a direct substitution into the same fit-check formula every option already uses; no ambiguous reading of any Modeling Assumption is involved. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py --probe 5`: all four FLEX parameters (tolerance, setup time, and both per-point time rates) flip the winner in at least one direction within ±50%. All disclosed in full, with real, verified numbers, in `case.json.sensitivity_disclosure[]` — disclosure-aware PASS per the 2026-08-13 standing rule, not a stable-margin PASS. This is a genuinely fragile case, and both `FACILITATOR.md` and `case.json` say so plainly. |
| P6 data decay | **PASS** | Both sources re-fetched live 2026-09-18: S1 (en.wikipedia.org/wiki/U.S._standard_clothing_size, ASTM D5585-11e1 table values for sizes 8/10/12/14/16 confirmed verbatim), S2 (bls.gov/oes/2023/may/oes516092.htm, $30.05/hr median confirmed). Both reachable, both values present, neither moved nor dead. |
| P7 accessibility cold-read | **FAIL (waived — see `qa.tier2.P7_waiver`)** | See below. |

**P7 remediation detail.** Round 1: a fresh cold-read named 6 unexplained real-world concepts (grading room, light table, pulling fabric, cutting/blade process, grade rule document format) and a concrete Q2 FAIL (could not visualize the grade rule as a physical/operational artifact). Remediation: added `case.md` Appendix G's "Picturing the grade rule" note plus 5 glossary terms. Round 2: Q1 dropped to 4 borderline items; Q2 FAIL persisted, now specifically about whether Devon ships numbers or redrawn patterns. Remediation: clarified explicitly that the numeric table alone is the shipped deliverable; added ASTM/die-press/occupation glosses. Round 3: Q1 remained at ~5 items (ASTM's internal methodology, grading software's interface, die-press mechanics beyond the analogy, the BLS occupation's day-to-day scope); Q2 FAIL persisted with a deeper, legitimate finding — the case never explains how a body *circumference* measurement converts into a specific pattern *point's* directional displacement. Remediation: added an explicit "From a body measurement to a moved point" disclosure naming the case's own width-only simplification and its real patternmaking basis (halving circumference for a mirrored flat pattern). **Genuine assessment after 3 real remediation rounds: full 2-D pattern-point grading is a genuinely complex real-world mechanism this case deliberately does not model, and no amount of text alone fully substitutes for an actual pattern diagram here** — the same class of honest, disclosed limitation as `the-constellation-bid`'s own P7 waiver (a single orbital burn re-tilting an entire plane) and `the-fold-line`'s disclosed real-nesting limitation. Waived per MCS-49, not silently passed — see `case.json.qa.tier2.P7_waiver` for the full disclosure.

### Tier 3 — human dry-run

NOT RUN. No real cohort has used this case yet. `cohort_bands[]` is declared for when one does.
