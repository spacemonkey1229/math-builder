# QA Report — Navigation

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case navigation`
19 checks: 17 PASS, 2 GAP, 0 FAIL.

**GAP (2):** T1-09 — margin 18.15% inside the SPEC §2 20% cap but wide; disclosed and expected
(the case's own `sensitivity_note` already flags this). T1-10 — `new_coverage[]` empty; expected
legacy-conversion carve-out (this title was already credited in `standards_spine.json`'s
`covered_by[]` from the pre-pipeline corpus scan, per `case.json.legacy_conversion_note`).

`sha256(case.md) = 6537f63d7165a65c52dab806bedf86a32451645bdc44948a6583fdd87a2d40d4`

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose **A (The Clean Run)**. Independently built the segment-by-segment drive-time table (own mph-over choice of +10, a legitimate free choice per D3's own design), computed total risk exposure ($10,000 fine + $42,100 one-year-income proxy = $52,100) divided by time actually saved, named the metric explicitly, gave a real counter-argument (a faster second labor could make the marginal minute matter more than the average dollar rate suggests), and correctly flagged the uncited "$10,000+" fine as the least-supported number in the case. |
| P2 both-sides-solve | **PASS** | Both options have real, non-concession arguments. Option A: ~$31,000+ of risk exposure per minute saved is lopsided against a 1.5-hour labor window. Option B: in a true medical emergency, the marginal minute could outweigh any dollar figure. B's case collapses specifically at D4 — the packet supplies no detection-probability data and no stated medical deadline, so B can assert the minutes "could matter" but can't show it, while A can point to the exact computed rate. |
| P3 trap-check | **PASS** (after one fix) | The case's existing trap (scaling the whole trip by the speed ratio instead of recomputing each segment, missing that stop-sign delay is fixed-cost regardless of speed) was independently reproduced. A second, previously undocumented trap was also independently found by a fresh subagent: dividing total dollar exposure by an option's *total trip time* instead of by the time *actually saved* (the D4 denominator), producing a misleadingly tame rate (~$8,700/min instead of the correct ~$31,000+/min). **Fixed this session**: added as a second named trap in `FACILITATOR.md`, directly below the existing one, matching D4's exact wording ("actually saved"). Re-verified via Tier 1 (clean, no new continuity issues). |
| P4 twist-integrity | **PASS** | Independently recomputed both pre- and post-twist drive times from Appendix B/C's own stated rules (Route 9 closure forces a detour via Fifth Ave + Ridge Rd). Confirmed Option B stays faster and the practical verdict (time saved dwarfed by risk exposure) is unchanged under every defensible reading of the mph-over ambiguity in Challenge D3's phrasing — that ambiguity is an intentional, disclosed design choice (the case explicitly leaves "how much faster" to the student), not a defect. |
| P5 assumption-sensitivity | **PASS (disclosed)** | Mechanical (`sensitivity_model.py` / `tier2_probes.py`): `speeding_mph_over` is disclosed in `sensitivity_disclosure[]` — at +50% flex (6→9 mph), the margin rises to 26.9%, breaking the 20% cap (winner never flips; B stays faster at every tested value). `license_loss_years` has zero effect on the graded primary metric (drive time) — it only scales the supplemental, non-graded D4 dollar-risk rate. Both disclosures already present in `case.json.sensitivity_note` before this session; re-verified accurate. |
| P6 data-decay | **PASS** | Both `sources[]` URLs (S1 O*NET taxi driver median wage $42,100, S2 SpeedingCost.com $150-300 ticket range) fetched live and independently reconfirmed exact on two separate passes this session. No source 404s, no drifted figures. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real defect
(P3's undocumented second trap) was found and fixed in `FACILITATOR.md` during this run, then
re-verified via Tier 1 (0 blockers, 2 gaps after the fix — both pre-existing, expected classes).

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 2`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
