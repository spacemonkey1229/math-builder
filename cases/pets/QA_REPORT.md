# QA Report — Pets

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case pets`
19 checks: 16 PASS, 3 GAP, 0 FAIL (after the FACILITATOR.md/case.md/case.json fixes below).

**VERDICT: TIER1_PASS (0 blockers, 3 gaps)** — all 3 pre-existing/expected (T1-10 legacy
carve-out, plus two benign classes already documented in the case's own structure).

`sha256(case.md)` recorded in `case.json.qa.case_md_sha256`.

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose **B (cat)** via cost-per-year-of-lifespan, reproduced all arithmetic exactly ($2,935.62/yr Beagle vs $2,515.00/yr Fold, 16.72% margin). Independently found that MA8 (Fold's ongoing annual cost, disclosed $1,095-$2,655 range) is the single most sensitive assumption — at the top of its range the recommendation flips to the Beagle, with no change needed to any Beagle-side assumption. Correctly named MA8 as both the most sensitive assumption and the least-supported number. |
| P2 both-sides-solve | **PASS** | Both options have real, sourced, non-concession arguments. Option A: Day-1 affordability ($585 shortfall vs. $1,180 for the Fold) plus the MA8 sensitivity finding (a fully plausible value within the case's own disclosed range flips the winner). Option B: lower lifetime/per-year cost, lower insurance burden as % of Year-1 cost. **Fixed this session**: `case.json.balance.argument_a` originally leaned only on Day-1 affordability and sentiment — strengthened to include the MA8 sensitivity point P1 surfaced, so Argument A doesn't read as a near-concession. |
| P3 trap-check | **PASS** (after a real fix) | The case's original named trap (raw lifetime totals vs. per-year, 51.7% gap) is substantially pre-empted by `case.md`'s own Background paragraph, which explains the fairness issue directly before a student ever reaches Appendix E. Three independent fresh subagents (across two dispatch rounds) found the same, more dangerous, undocumented trap instead: D2's Year-1-with-insurance totals are *reversed* from the true per-year winner (Beagle Year-1 $4,971 < Fold Year-1 $5,035, but Beagle per-year $2,935.62 > Fold per-year $2,515.00) — a Hero who writes the Challenge 2 persuasive pitch around the salient D2 figures instead of the correct D3/D4 per-year figures would silently pick the wrong pet with no arithmetic error. **Fixed**: added as a second named trap in `FACILITATOR.md`, with a specific cold-call question matching the case's own D2 numbers exactly, positioned before the Twist in the Data Deep Dive section. |
| P4 twist-integrity | **PASS** | Independently reproduced every FACILITATOR.md figure to the cent (raw lifetime 51.7%, per-year 16.72%, cat wins both ways) via direct hand-derivation from Appendix C/E. Confirmed no hidden or unstated conventions — every input traces to a disclosed source or Appendix E modeling assumption, and the insurance-every-year convention is applied identically to both options. |
| P5 assumption-sensitivity | **PASS (disclosed)** | Mechanical script run; `sensitivity_disclosure[]` already documents the genuinely unstable dials (MA8 chief among them, matching P1's independent finding). |
| P6 data-decay | **PASS** (after a real fix) | All 6 load-bearing sources (S1-S6, feeding MA1-MA10 and the graded metric) fetched live and confirmed accurate on two independent passes. S7 (a non-load-bearing context-only source, explicitly disclosed in its own `case.json` note as "not used as the modeled dollar figure") had drifted: cited $62.44/mo (dogs) / $32.21/mo (cats), live page now shows $43/mo / $23/mo. **Fixed**: updated S7's value in both `case.md` and `case.json` to the current figures; `accessed` date updated to 2026-08-20. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict (P1-P4 by
independently-dispatched, cross-verified subagents this session, P5 by the script, P6 by a
fetch-capable subagent). Two real defects were found and fixed during this run (P3's undocumented
D2-reversal trap, P6's stale S7 figures), plus Argument A was strengthened per P2's finding —
each re-verified independently by a second dispatch round before finalizing.

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 3`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
