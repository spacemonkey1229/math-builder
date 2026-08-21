# QA Report — Insurance Actuary

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case insurance-actuary`
19 checks: 18 PASS, 1 GAP, 0 FAIL.

**GAP (1):** T1-10 — `new_coverage[]` empty, expected legacy-conversion carve-out.

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose **Option A** — the opposite of the case's own recorded winner (B, by 2.19%) — via a legitimate alternate metric: exposure-retained (car-years) as a proxy for revenue, since the packet gives no premium data and the case's stated mandate is revenue growth, not cost reduction. Reproduced the D2 blended-rate arithmetic exactly (A: ₡1,952/vehicle, B: ₡1,910/vehicle, matching the case's 2.19% margin). A genuinely close, well-balanced case producing a defensible split across independent solvers is a healthy signal, not a defect. |
| P2 both-sides-solve | **PASS** | Fresh subagent independently reproduced all D1/D2 figures. Confirmed neither side collapses under cross-examination: Option A's hardest question (does the severity trend concern overturn today's data?) is answered by the current book already showing Young out-costing Senior per-vehicle and skewing more High-risk; Option B's hardest question (does a cost win serve a revenue mandate?) is answered via a legitimate loss-ratio/pricing-headroom reframe. The 2.19% margin is real, not a paper number. |
| P3 trap-check | **PASS** | Fresh subagent, packet-only, independently predicted the exact trap named in `FACILITATOR.md`: computing each class's own per-vehicle claims rate in isolation, seeing Young's is highest, and stopping there — without running D2's blended-remaining-book comparison, which flips the answer because Senior's much larger exposure drags its own blended contribution down further. |
| P4 twist-integrity | **PASS** (after a real fix) | Independently verified the twist gives real, non-decorative ammunition against both positions (Senior's Low-risk sub-segment is nearly as large as Young's entire book; Young's High-risk tier share is the largest of any class). Found a real documentation defect: `FACILITATOR.md`'s "no escape hatch" justification cited Carbosian law's five-coverage bundling requirement, which governs coverage *types* within a policy, not age-class risk-tier selectivity — a non-sequitur as written, even though the twist's actual effect holds. **Fixed**: `FACILITATOR.md` now correctly cites Background's own "discontinued entirely — no new policies, no renewals" framing as the operative constraint, and explains why the law citation doesn't itself do that work. Outcome unaffected. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run; the one stated assumption (2016-2018 trend continuing into 2019) flexed ±50%, winner stays B, margin stays in a 2.1-2.3% band throughout. |
| P6 data-decay | **PASS** (after a real fix) | S2 (IIHS older-driver fatality-rate data) was found to inaccurately aggregate: the case cited "40-64: 1.6" as a single band, but the live IIHS page breaks that range into five sub-bands ranging 1.4-2.2, only some of which equal 1.6. **Fixed**: corrected to "60-64: 1.6," a real single band that matches the source exactly, in both `case.md` and `case.json`. All other cited figures (85+: 7.9, 70-74: 2.1, the injury-susceptibility explanation) confirmed exact. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Two real defects
were found and fixed during this run (P4's mis-cited constraint, P6's aggregated IIHS figure).

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
