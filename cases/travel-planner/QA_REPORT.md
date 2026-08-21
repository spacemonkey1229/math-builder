# QA Report — Travel Planner

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
18 checks: 18 PASS, 1 GAP, 0 FAIL (T1-10 expected legacy carve-out). First pass surfaced 2 real
blockers (orphan Appendix E/F, per SPEC §1.6) and 3 GAPs (fuzzy-match plan-name miss, hard-wrapped
Socratic questions, 2 twist dollar figures missing from `case.json.derived`) — all fixed; see
`case.json.qa.note` for detail.

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

### Tier 2 — simulated play (6 probes)

Two real defects found and fixed during this run: an undisclosed discount-tier convention in the
Twist, and a source/room-type mismatch in one hotel citation.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose Plan A, reproduced its full D1-D4 arithmetic exactly ($1,865.66 tickets + $635.93 hotel + $100.06 fee = $2,601.65), correctly named MA1 (Henrietta's free-admission cutoff) as most sensitive for Plan A and MA4 (the Anaheim hotel rate) as the case's least-supported number. |
| P2 both-sides-solve | **PASS** | Fresh subagent computed both plans in full, matching `case.json.balance` exactly (A $2,601.65, B $2,817.36). Independently confirmed neither plan comes close to the $3,950 cap even under adverse re-readings, and correctly identified MA4 (the $210 Anaheim rate) as the single assumption that could flip the recommendation — solving the exact break-even rate (~$153.30/night), inside the disclosed $102-$210 range. This confirms `sensitivity_disclosure[]`'s existing entry rather than finding a new defect. |
| P3 trap-check / P4 twist-integrity | **PASS** (after a real fix) | Fresh subagent's cold prediction (discount-tier misapplication across ticket products) was directionally right and adjacent to the guide's actual named trap (under-applying the 6% tier to Plan A's Universal tickets). Independently re-derived the Twist's full arithmetic from raw Appendix C data — all four figures ($174.28, $2,775.93, $70.32, $2,887.68) and both margins (8.29%→4.03%) matched exactly. **Found a real gap**: the Twist's $174.28 figure depends on pricing Henrietta's new Day-3 Universal ticket at the standalone 2% tier rather than the family's existing 6% 3+-day tier — a real, defensible modeling choice, but never stated anywhere in `case.md` or `FACILITATOR.md`; using 6% instead gives $163.46, not $174.28. **Fixed**: added an explicit disclosure paragraph to `FACILITATOR.md`'s Twist section naming the convention and the alternate figure, and recorded the alternate value in `case.json.derived` so it's checkable. |
| P5 assumption-sensitivity | **PASS (disclosed)** | Authored `sensitivity_model.py` (none existed at TIER1_PASS), reproducing `case.json`'s exact base figures (A $2,601.65, B $2,817.36, margin 8.29%) and its pre-existing `sensitivity_disclosure[]` entry for `plan_b_hotel_rate` (MA4) to the decimal (-50% flips the winner to A at 7.6% margin; +50% breaks the 20% cap at 23.7%) — confirming the disclosure was already accurate, not just asserted. `FLEX` is scoped to only `plan_b_hotel_rate`, since the ticket prices and discount/fee percentages are Background's fixed, sourced deal terms, not scenario assumptions. |
| P6 data-decay | **PASS** (after a real fix) | S1-S4 and S6 fetched and confirmed exact. **S5 (Hampton Inn & Suites) had a real room-type mismatch**: the case cited $139/night specifically as the 2-queen room rate, but live data shows $139 is actually the King-room rate — the 2-queen room is currently $155/night. **Fixed**: reworded S5's claim in `case.md`'s Sources table to describe $139 as "the lowest publicly listed starting nightly rate (any room type)" rather than tying it to the specific 2-queen configuration the narrative needs, consistent with Appendix E's existing general disclaimer that hotel prices depend on exact date/room booked, which no public source fixes in advance. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Two real defects
(P3/P4's undisclosed twist convention, P6's S5 room-type mismatch) were found and fixed during
this run.

**Tier 1 clean (0 blockers, 1 gap) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded (re-hashed
after the S5 citation fix). Per SKILL.md's ladder, `case-publish` may now run — Tier 3 (a filed
human `RUN_REPORT`) remains required before `VERIFIED`.
