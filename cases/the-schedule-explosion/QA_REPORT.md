# QA_REPORT.md — The Schedule Explosion

## case-readiness run — 2026-09-09

**State:** `TIER2_PASS`   **Verdict:** PASS   **Tier 1:** 0 BLOCKERs, 1 GAP (T1-10 reinforcement carve-out)
**Tier 2:** 6/6 required probes recorded, 0 FAIL; P7 (accessibility cold-read) also now run for real against the published Interactive HTML and PASSED after 2 remediation rounds — see below

### Preflight lint (advisory, non-blocking)

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-schedule-explosion` → clean, no
advisory findings. No Modeling-Assumptions leak (MA1/MA2/MA3's Sensitivity columns state direction
of *what is affected*, never the size/direction/threshold of the graded margin itself) and no
`sensitivity_model.py` `FLEX[]`/`sources[]` collision (the one swept dial, `switchover_scale`, ties
back to MA1, a stated assumption, not a cited source).

### Tier 1 — structural (21 checks)

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-schedule-explosion
```
sha256(case.md) = `9b8cbb04268b85384dc9c084026c6138819c82424dac2cbf0a7d49a6e0d4f219`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | one Overview numeral ("10", a ten-minute meeting countdown) cleared as texture in `case.json.overview_numerals_cleared[]` |
| T1-03 | PASS | dilemma binary, opens "You are Dara Osei."; both option labels ("The Full Sweep", "The Greedy Queue") named explicitly in Background (fixed during this pass — see below) |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | all six appendices referenced by letter, including the final standards Appendix F (fixed during this pass — see below) |
| T1-07 | PASS | Appendix F's 2 labels parsed (both bulleted) |
| T1-08 | PASS | every number cited or declared a Modeling Assumption |
| T1-09 | PASS | balance test: both arguments written with real numbers, margin 13.9% ≤ 20%, inside the 8-15% target band |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out applies (see `reinforcement_note`) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs. numeric load (T3: optimization over a set, 3+ effective variables — job count, switchover cost, evaluation rate) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, cohort bands, sensitivity note |
| T1-14 | PASS | CONTINUITY — `FACILITATOR.md` agrees with `case.md`/`case.json` (fixed during this pass — see below) |
| T1-15 | PASS | no `published/` dir yet — nothing to drift |
| T1-16 | PASS | QA hash current (resynced twice during this pass, after each content fix) |
| T1-17 | PASS | `cohort_bands[]` declared (Full/Compressed/1:1) |
| T1-18 | PASS | no `published/` dir yet — nothing to check |
| T1-19 | PASS | no `published/` dir yet — nothing to check |
| T1-20 | PASS | no `published/` dir yet — nothing to check |
| T1-21 | PASS | no `published/` dir yet — nothing to check |

**VERDICT: TIER1_PASS — 0 BLOCKERS, 1 GAP.**

The one remaining GAP (T1-10) is the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`,
2026-08-17): `case.json.reinforcement_note` records both claimed skills' exact `n` values in the spine
(`advanced-operations-factorial` n=1, `advanced-operations-how-to-evaluate-a-factorial-expression`
n=1 — neither is 0) and the full search for a genuine `n=0` skill this case could close instead
(checked the complete current n=0 list: place-value Depth/Digit, sphere volume, the quotient rule,
Taylor series and its how-to — none fits a factorial-driven job-scheduling case without padding).
This matches the identical pattern in `cases/the-minimum-payment-trap/case.json`,
`cases/the-deferred-repair/case.json`, and `cases/the-two-offers/case.json`.

### Defects found and fixed during this pass

**1 · T1-02 BLOCKER, first run (mechanical, immediately fixed).** The Overview's "10 min" (a VP
meeting countdown) tripped the numeral-clearance check. Read it: pure scene-setting texture, never
used in any calculation. Cleared in `case.json.overview_numerals_cleared[]` with a stated reason.

**2 · T1-03/T1-06 GAPs, first run (mechanical, immediately fixed).** The initial `case.md` draft
never named "The Full Sweep" / "The Greedy Queue" by their memorable labels inside Background (only
in the Dilemma) — fixed by naming both labels explicitly in Background's second paragraph. The
initial draft also never cross-referenced the final standards Appendix F from Background — fixed by
adding a "(SEE APPENDIX F)" sentence.

**3 · T1-14 CONTINUITY GAPs, found across two sub-passes (fixed).** First pass: three numbers in
`FACILITATOR.md` (a 25% job-count increase, a hypothesized 1,000x speedup, and a stated factorial
time-ratio) had no home in `case.json`. Fixed by adding `job_count_pct_increase_12_to_15`,
`hypothetical_speedup_factor_socratic_q3`, and `search_time_ratio_15_over_12` (plus its three
multiplicative factors, 15/14/13) to `case.json.derived`. Second sub-pass, while adding those
factors: caught that `FACILITATOR.md` had **incorrectly stated the 12-to-15-job time-ratio as
"2,725,000x"** — a real arithmetic error, not a typo of formatting. The true ratio is exactly
15!/12! = 15 × 14 × 13 = **2,730x** (verified independently by the P4 twist-integrity subagent below,
which recomputed the same figures from scratch and matched them to `case.json.derived` exactly).
Corrected in `FACILITATOR.md`'s trap section and recorded correctly in `case.json.derived` this time
— this is the kind of arithmetic-direction defect Tier 2 subagents exist to catch, caught here during
Tier 1 continuity work instead, before ever reaching Tier 2.

**4 · P2 mechanical pre-screen FAIL, first run (fixed).** `case.json.balance.argument_b` originally
described Vantage's batch-size growth only in words ("twice the size... heading toward triple") with
no actual digits, tripping the "argument carries almost no numbers" pre-screen (SPEC §2 requires a
*quantitative* argument for each side). Fixed by restating the same argument with its real numbers
(12 jobs, 6-job pilot, 18-20 jobs, 48 seconds, 36.3 hours, the 8-hour window, 20-7,709 years).

**5 · P3 mechanical pre-screen FAIL, first run (fixed) — a genuine trap-extraction bug this case's
own text triggered.** `tier2_probes.py`'s trap-check regex finds the *first* occurrence of the word
"trap" in `FACILITATOR.md` and reads forward from there. The first draft's "The margin" section
referenced a sibling case by its literal folder name, `cases/the-minimum-payment-trap`, which
contains the substring "trap" with word boundaries (hyphens count) — so the script extracted text
from the middle of an unrelated cross-reference sentence instead of the actual "## The trap" section
below it, and flagged that extracted (garbled) text as not describing a real wrong path. **Fixed** by
rewording the cross-reference to "a sibling case in this corpus" (removing the literal folder name),
which lets the script's first "trap" match land on the real "## The trap" heading, where the actual
trap text correctly matches the "learner"/wrong-path pattern the check looks for. This is a real,
if narrow, finding: any case referencing `the-minimum-payment-trap` by name anywhere in
`FACILITATOR.md` *before* its own "## The trap" heading will trip this same false pre-screen FAIL —
worth a note for future authors, though not a `tier2_probes.py` bug to fix in the script itself (the
regex is doing what it says: finding the first "trap").

### Tier 2 — simulated play (6 required probes, all recorded; P7 now run for real post-publish)

```
python3 skills/case-readiness/scripts/tier2_probes.py --case the-schedule-explosion
```

| Probe | Verdict | Finding |
|---|---|---|
| **P1 — Cold solve** | **PASS** | A genuinely fresh, unbriefed subagent was dispatched with only the leak-free packet path and the 7 printed questions, no access to `FACILITATOR.md`/`case.json`/`QA_REPORT.md`. It independently re-derived the full D1-D3 arithmetic exactly matching `case.json.derived` (factorial table; 47.9s at n=12, 36.3 hours at n=15, etc.; Full Sweep 62 minutes / Greedy Queue 72 minutes on the six-job pilot). It chose **B (The Greedy Queue)** — the option that *loses* the graded six-job margin — explicitly naming its optimized metric as "sustained feasibility of the scheduling approach... as job count grows" rather than raw one-night idle-time minimization, and explicitly cited D2's feasibility-crossing finding as its reason. This is exactly the case's designed twist working as intended on a reader who has never seen the guide: reaching a defensible position with correct arithmetic and a named metric, even though it doesn't match the graded metric's own six-job winner — meeting the P1 pass criterion precisely (reaching a defensible position for the right reasons, not necessarily "the" graded winner). It also independently flagged MA2 (the assumed evaluation rate) as the least-supported number and MA1 as the most sensitive assumption — both match `case.json`'s own disclosures, not new defects. It additionally noted the Greedy Queue's total varies by starting job (72-82 minutes across all six possible starts) — see finding #6 below, which led to a real fix in Appendix D/A. |
| **P2 — Both-sides solve** | **PASS** | A fresh subagent built the strongest quantitative case for each option independently from `case.md` alone. Both are genuinely defensible with real numbers (A: 16.1%-worded margin — see note below on margin convention — at near-zero computational cost on the six-job batch; B: the D2 feasibility-crossing arithmetic against the fixed 8-hour window). The subagent identified A's collapse point precisely as "does the Full Sweep still finish inside the fixed 8-hour window once the batch reaches n=15?" — confirming the case's twist targets exactly the right pressure point. Neither argument is a bare concession. *Note on margin convention:* the subagent computed (72-62)/62 = 16.1% (denominator = winner); `case.json.balance.margin_basis` uses (72-62)/72 = 13.9% (denominator = loser/Greedy Queue), matching this corpus's established convention (see `cases/the-minimum-payment-trap`). Both are correct arithmetic under their own stated convention — not a discrepancy, just two valid ways to express the same 10-minute gap. |
| **P3 — Trap check** | **PASS (after remediation)** | See "Defects found and fixed" #5 above for the mechanical pre-screen fix. After the fix, a fresh subagent reading `case.md` alone (before opening `FACILITATOR.md`) independently named, as its own Step-1 answer, the exact same core trap later confirmed in `FACILITATOR.md`: a student generalizing the six-job D3 margin into a company-wide recommendation without running D2's feasibility-crossing arithmetic. It also independently anticipated the guide's named "milder" secondary trap (misjudging factorial growth as roughly proportional). No mismatch to reconcile. |
| **P4 — Twist integrity** | **PASS** | A fresh subagent independently recomputed all of D2's headline figures from Appendix B/C data (n=12: 47.9s; n=15: 36.32 hours; n=18: 20.28 years; n=20: 7,708.6 years) and confirmed they match `case.json.derived` exactly. It confirmed (1) the twist genuinely invalidates a "vote Full Sweep on the 13.9% margin alone" position, since 15 jobs — one step past Vantage's *current* typical batch (12) — already blows the 8-hour window by 4.5x. It also stress-tested (2) the twist's survival under the case's own stated MA2 (evaluation-rate) assumption at a defensible, case-prompted 1,000x-faster reading (exactly Socratic Question 3's own scenario): even then, n=18-20 (Vantage's stated one-year target) remains catastrophically infeasible (days to years, not hours) — the twist survives. It further computed that only an ~8.45-million-times-faster rate would rescue Option A at n=20, which it correctly judged to contradict MA2's own stated basis (a simple single-machine loop) rather than merely stretch it — so the twist does not depend on an unstated convention. One minor, non-blocking looseness noted: FACILITATOR.md's twist description says the infeasibility crossing falls "somewhere between 12 and 15 jobs," which is true but imprecise (the subagent's own finer-grained check found the true crossing is between n=14, ~2.42 hours, and n=15) — not a defect, since the case only ever asks students to test the specific n values Appendix B lists (which do not include 13 or 14), but recorded here for completeness. |
| **P5 — Assumption sensitivity (±50%)** | **PASS** | `sensitivity_model.py` created. `FLEX = ["switchover_scale"]`, the one dial tied to the graded six-job margin (MA1's switchover-cost matrix). Sweep result: base `A=-62, B=-72` (margin -13.9%); at -50% (`switchover_scale=0.5`): `A=-31, B=-36`, margin still -13.9%, no flip; at +50% (`switchover_scale=1.5`): `A=-93, B=-108`, margin still -13.9%, no flip. This is a genuine, provable invariance (uniformly rescaling a cost matrix scales both the optimal and the nearest-neighbor totals by the same factor, which cannot change either strategy's chosen ordering or their ratio) — documented in `sensitivity_model.py`'s own module docstring, not a script artifact. MA2 (evaluation rate) and MA3 (batch window) are correctly excluded from `FLEX`, since neither affects the graded six-job margin at all — both are exposed as separate PARAMS/helper functions instead (`search_time_seconds`, `feasibility_crossing`), matching the treatment `cases/the-minimum-payment-trap`'s model gives its own non-margin dial. |
| **P6 — Data decay** | **PASS** | All 4 `sources[]` URLs (S1-S4) live-fetched directly by this session (WebFetch) on 2026-09-09, 0 days old. S1 (Cornell Optimization Wiki): reachable, exact quote re-confirmed verbatim ("There are n! feasible solutions for a job shop scheduling problem..."). S2 (NVIDIA investor relations): reachable, exact "2 million additional NVIDIA GPUs... 2027-2028" figure re-confirmed, dated 2026-08-26. S3 (AWS containers blog): reachable, exact 82s/457s baseline figures re-confirmed verbatim in the results tables. S4 (Wikipedia): reachable, confirms the nearest-neighbour algorithm's use for TSP-style routing/scheduling problems, matching the case's non-load-bearing definitional claim. No drift, no dead links, no figure moved. |
| **P7 — Accessibility cold-read** | **PASS (after 2 remediation rounds)** | `published/` now exists. Mechanical pre-screen: D5 (the visual-display deliverable) matched against 2 real visuals found in the Interactive HTML (the Overview's schematic bar-chart SVG and the twist/notebook's live-calculator output regions) — READY, 0 mechanical FAIL. Model-judged cold-read: `skills/case-readiness/scripts/tier2_probes.py --case the-schedule-explosion --probe 7` built the packet from the actual published `The Schedule Explosion - Interactive.html` (glossary glosses rendered inline, per the script's `build_html_cold_read_packet()`). **Round 1:** a genuinely fresh, zero-context subagent named 11 real-world concepts it could not picture (NP-hard, container, shared pipeline stage, utilization review, GPU fleet, AI accelerator, plus several meta/pedagogy labels) — well over the 2-concept FAIL threshold. **Fix:** added 4 new `STORY_GLOSSARY` entries (Container, Pipeline, NP-Hard, AI Accelerator — each URL freshly fetched and confirmed live 2026-09-09 on Wikipedia) and hand-wrapped their first mentions in Background/Appendix E, plus a light inline clarification of "fleet" in prose. **Round 2:** a second fresh subagent still named 2 genuinely unglossed real-world concepts ("utilization review" and the terminal/command-line notation in the Overview). **Fix:** added 2 more `STORY_GLOSSARY` entries (Utilization, Command Line — Wikipedia "CPU time" and "Command-line interface," fetched and confirmed live 2026-09-09) and wrapped their Overview mentions. **Round 3 (final):** a third fresh subagent's findings were entirely either (a) terms that already carry an inline gloss in the packet (the subagent's own text acknowledges the gloss exists and asks for deeper mechanistic intuition beyond it — e.g. "given only a one-line gloss... without worked intuition for why") or (b) math/procedural mechanism questions (the percent-margin formula, how to hand-enumerate 6! permutations, nearest-neighbor tie-breaking) rather than unexplained real-world vocabulary — 0 genuinely unglossed real-world concepts, meeting the PASS criterion (0-1 named concepts). `case.json.qa.tier2.P7` updated to PASS. Re-ran `tier1_structural.py` after each round: `TIER1_PASS` held throughout (0 BLOCKER, same 2 accepted GAPs) and T1-19/T1-21 both stayed PASS (11 STORY_GLOSSARY terms, 8 math GLOSSARY terms, all URLs allowlisted/Wikipedia). |

**MECHANICAL RESULT: 0 of the 6 required probes FAILED.** All six are recorded by name in
`case.json.qa.tier2` and above. Tier 2 is clean on the required six-probe ladder: `qa.state =
TIER2_PASS`.

### Tier 3 — human dry-run

NOT RUN (not reachable — case is not `PUBLISHED`; `case-publish` was intentionally **not** run this
pass, per instruction).

### Margin

`case.json.balance.margin_pct` = **13.9%** on the primary metric (six-job pilot batch idle time,
Full Sweep vs. Greedy Queue), inside the SPEC §2 target 8-15% band (the concept sheet's stated
margin target for this case) and well inside the 20% hard cap. This is a genuinely computed figure,
verified independently by two separate fresh Tier 2 subagents (P1, P2) via full exhaustive search and
nearest-neighbor simulation over Appendix A's switchover-cost matrix — not a tuned or hidden number.
The six-job pilot batch is a disclosed, stated design choice (the largest batch size where a true
head-to-head comparison is even computable), not an empirical figure or a shrink-to-fit window: at
realistic Vantage batch sizes (12-20 jobs), no comparable "true optimal" figure can be computed at
all within the case's own stated constraints, which is the entire point of the twist.
`FACILITATOR.md`'s "The margin" section explains this explicitly.

### Skill-claim confirmation

This case claims exactly `advanced-operations-factorial` and
`advanced-operations-how-to-evaluate-a-factorial-expression` — the Factorial half of the "Scientific
Notation, Factorial, Absolute Value" Advanced Operations group — and explicitly does **not** claim
any Scientific Notation, Standard Notation, or Absolute Value skill in that same group.
`cases/the-yield-die/` (the sibling case targeting the Scientific Notation half, per the approved
concept sheet) does not exist yet anywhere in this corpus as of 2026-09-09 — checked directly before
writing `case.json.standards[]` and again during this QA pass — so there is no live duplicate claim
to reconcile. This is recorded in `case.json.reinforcement_note` and `LEARNING_GOALS.md` for
whichever author writes `the-yield-die` next.
