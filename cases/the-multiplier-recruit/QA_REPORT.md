# QA Report — The Multiplier Recruit

## case-readiness run — 2026-08-19

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case the-multiplier-recruit`
19 checks: 18 PASS, 1 GAP, 0 FAIL.

**GAP (1):** T1-13 — MCS-15, Twist is N/A (mathematical surprise, not narrative); justification is
written out in `FACILITATOR.md`'s Twist section. Expected GAP class for an N/A twist, same
precedent as `the-one-pass-route`.

`sha256(case.md) = ec9eab1b52d1e58782bda25f185782fc668bb4a0ad62a7ddacbb469e192656ed`

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only (`/tmp/coldsolve-the-multiplier-recruit/PACKET.md`), no other project file read. Reached **A (Anvil/Meridian)** via the required matrix pipeline (built A, computed I−A, det=0.716, solved x=(I−A)⁻¹d for both employers, normalized by incentive dollars into jobs-per-$10,000) — not by eyeballing. Independently reproduced det=0.716, x_meridian total 191.6, x_cascade total 368.0, 4.56 vs 3.96 jobs/$10k. Named the metric and why, named the strongest counter-argument, named MA1 as the most sensitive assumption, correctly identified Appendix C's national figures as intentionally not load-bearing. |
| P2 both-sides-solve | **PASS** | Independently reproduced the full matrix arithmetic and the 13.3% margin. Both options have real, non-concession sentences: A wins on jobs-per-dollar efficiency; B wins on absolute scale and lower per-employer risk. Neither collapses to a bare concession — B's collapse point is specifically the case's own stated decision metric (total regional jobs per $10,000), not a weaker argument overall. |
| P3 trap-check | **PASS** (after one fix) | Primary trap (naive 310>140 direct-job comparison, never opening Appendix B) confirmed present and correctly named in `FACILITATOR.md`. The probe additionally surfaced a real secondary trap not originally documented: a Hero can correctly solve the matrix, reach D4's totals (Cascade 368.02 vs Meridian 191.62), and still pick Cascade by stopping before D5's per-incentive-dollar normalization — this survives real linear-algebra work and is more dangerous than the headcount trap. **Fixed this session**: added a paragraph to `FACILITATOR.md`'s "The trap" section naming this D4-without-D5 failure mode explicitly, with the exact derived figures (191.62 / 368.02) matching `case.json.derived`. Re-verified via Tier 1 re-run (T1-14 continuity check confirms the new numbers resolve against `case.json.derived`, no orphans). |
| P4 twist-integrity | **PASS** | Twist is N/A by design (mathematical surprise: identical $3,000/job rate produces meaningfully different regional return once the matrix is solved). Confirmed the twist survives every stated Modeling Assumption (MA1-MA3) under a natural reading — the guide's own P5 sensitivity note already confirms the winner never flips under ±50% flex on any single coefficient. |
| P5 assumption-sensitivity | **PASS (disclosed)** | `tier2_probes.py --case the-multiplier-recruit --probe 5 --flex 0.5`: swept all 7 declared dials. Winner (A) never flips under any flex. Margin does breach the SPEC §2 20% cap under 3 individual flexes (a11 +50% → 30.7%; a21 +50% → 20.0%; a22 -50% → 21.2%), but all three are disclosed in `case.json.sensitivity_disclosure[]` with a recorded category and justification (Category-X proprietary-estimate exception — the four matrix entries are a stated Modeling Assumption calibrated to real Butler County, OH analogues, not a purchased regional table, since Calder County is fictional). Passes per the disclosure-aware pass state, not the stable-margin state — the instability is real but honestly flagged, not hidden. |
| P6 data-decay | **PASS** | All 4 `sources[]` URLs fetched live 2026-08-19. S1 (BEA RIMS II pricing page): reachable, $520/region confirmed exact. S2 (BEA SCB Dec 2019 PDF, Butler County multipliers): reachable, Table 7 and Table 1 values confirmed exact (1.3616, 1.1810, 52.1%, 36.5%). S3 (SelectFlorida QTI tax refund PDF): reachable, $3,000/$6,000 figures confirmed exact (note: PDF hosted at selectflorida.org but branded "Enterprise Florida" — same org lineage, not a mismatch). S4 (Census CBP program page): reachable, 2023-vintage framing confirmed accurate as originally accessed. No source 404s, no moved URLs, no drifted figures. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict (P1-P4 by
independently-dispatched subagents this session, P5 by the script, P6 by a fetch-delegated
subagent). One real defect (P3's secondary trap) was found and fixed in `FACILITATOR.md` during
this run, then re-verified via Tier 1.

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-19"`,
`blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
