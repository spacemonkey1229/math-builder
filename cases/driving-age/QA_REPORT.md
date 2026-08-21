# QA Report — Driving Age

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case driving-age`
19 checks: 18 PASS, 1 GAP, 0 FAIL.

**GAP (1):** T1-10 — `new_coverage[]` empty; expected legacy-conversion carve-out (this title was
already credited in `standards_spine.json`'s `covered_by[]` from the pre-pipeline corpus scan).

`sha256(case.md) = ce1f78d581f0bd33...` (full hash in `case.json.qa.case_md_sha256`)

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose **B (NAY, keep 15½)**. Built two independent best-fit lines through Appendix B's crash-rate data points, correctly completed the D4 chauffeuring-vs-insurance cost comparison ($7,964.40 vs $8,100 — options only ~$135.60 apart over two years, essentially a wash), named the net two-year family cost as the metric, correctly identified MA1 (the unsourced 6,000 mi/yr chauffeuring estimate) as both the most sensitive assumption and the least-supported number, and correctly set aside Appendix D's constituent poll as non-load-bearing. |
| P2 both-sides-solve | **PASS** | Neither option is a pure concession. Option A's cost pillar collapses first once the D4 arithmetic is completed in full (the naive "$8,100 savings" claim is wrong; the real net difference is ~$135.60). Option B's safety pillar is more resilient — its toughest counter (per-mile vs. per-population framing) is a genuinely disclosed ambiguity, not a clean contradiction. |
| P3 trap-check | **PASS** | Fresh subagent, packet-only, independently predicted the exact trap `FACILITATOR.md` names: reading Appendix B's per-100,000-*population* fatality-rate table (which rises with age) as if it were a per-mile risk rate, and using that rise to argue "raising the age is safer" — the opposite of what the case's own per-mile citation (S8) supports. |
| P4 twist-integrity | **PASS** (after a real fix) | Original defect: the twist's decisive claim (per-mile teen crash rate) had **no citation** anywhere in `case.md`/`case.json.sources[]`, despite every other factual claim in the case carrying an S-number, and `FACILITATOR.md`'s Lessons Learned incorrectly called it "correctly-sourced." There was also a granularity mismatch (the case's actual comparison is 16-vs-18; the uncited claim only supported a coarser teens-vs-adults read) and an internal inconsistency (`case.json.balance.argument_a` cited the same population table the Trap section calls an invalid basis for a safety claim). **Fixed this session**: sourced a real citation (S8 — AAA Foundation for Traffic Safety, 16-17 vs. 18-19 age-band per-mile crash rates, the closest published breakdown to the case's actual comparison), disclosed the granularity gap explicitly everywhere the stat is used (case.md, FACILITATOR.md's Arguments for A/B and Lessons Learned, case.json's balance fields), and rewrote Argument for A to ground its safety claim in S8 rather than the population table the Trap correctly flags as invalid for that purpose. Independently re-verified clean by a second fresh subagent — confirmed the citation resolves end-to-end, the granularity caveat is stated consistently everywhere the stat appears, Argument for A no longer contradicts the Trap, and the twist is now a genuine, honestly-sourced discussion device. |
| P5 assumption-sensitivity | **PASS (disclosed)** | Mechanical script run; disclosed in `sensitivity_disclosure[]` per the case's own documentation. |
| P6 data-decay | **PASS** | All 7 `sources[]` URLs fetched live and confirmed exact (AZ DOT permit ages, IIHS 2024 fatality-by-age stats matching exactly, carinsurance.com's $4,050 teen premium increase, AAA's 2025 per-mile cost table, NJ DMV teen permit age, Germany's BF17 accompanied-driving program). One non-blocking note: S5's linked FHWA PDF is the 2023 edition of Highway Statistics even though cited as "Highway Statistics 2024, Table VM-1" — the citation label matches the source page's own text exactly, so this reads as an upstream naming quirk (the government page itself uses that label for the linked file) rather than a real staleness defect; not fixed, flagged for awareness only. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real defect
(P4's uncited, mischaracterized twist claim) was found and fixed during this run — a real source
added, the granularity gap disclosed consistently, and an internal contradiction between Argument
A and the Trap section resolved — then independently re-verified clean by a second fresh subagent.

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
