# QA Report — Medical Statistician

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case medical-statician`
19 checks: 17 PASS, 2 GAP, 0 FAIL.

**GAP (2):** T1-09 — margin 15.5% inside the SPEC §2 20% cap but wide, expected/disclosed.
T1-10 — `new_coverage[]` empty, expected legacy-conversion carve-out.

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose Option B, reached it via schedule feasibility as the binding constraint (dosing alone consumes ~6 of the 7-month window) with cost/MOE as secondary. Reproduced all arithmetic exactly ($640/subject A, $480/subject B, n=770/1,027, MOE 3.53%/3.06%). Self-identified the MA1 all-in-vs-screening-cost ambiguity as a soft spot in its own analysis — the same issue P2/P3 independently found as a defect. |
| P2 both-sides-solve | **PASS** (after a real fix) | A fresh subagent found that Option A's own numbers were internally inconsistent: Appendix B states a pure random draw needs ~300 contacts per diabetic dog found (the stated reason A is slower/more expensive), but MA1's $250/subject figure never stated whether that screening cost was already included — a Hero taking MA1 literally gets a clean budget fit; a Hero taking Appendix B's 300:1 ratio seriously and stacking it gets a budget blown by ~100x. **Fixed**: MA1/MA2's basis text in both `case.md` and `case.json` now explicitly states the figure is an all-in per-enrolled-subject cost, not stacked with the 300:1 ratio, with reasoning for why that's the correct reading. |
| P3 trap-check | **PASS** (after a real fix) | A fresh subagent independently found the identical ambiguity as an undocumented trap: a Hero could literally multiply Appendix B's 300:1 ratio into MA1's $250 during D1's sample-size arithmetic and get a nonsensical result, with no facilitator scaffolding to catch it (the Data Deep Dive script only walked "budget ÷ cost-per-subject," treating that as settled). **Fixed**: added as a second named trap in `FACILITATOR.md`'s Data Deep Dive section, with a redirect instruction pointing to MA1's now-clarified basis note. |
| P4 twist-integrity | **PASS** | Independently re-derived both MOE figures from the case's own numbers (matched exactly), confirmed the GFI #266 twist doesn't contradict Appendix F's 21 CFR 514.117 quote or any Appendix G assumption, and confirmed the one genuine open regulatory ambiguity (how GFI #266 relates procedurally to 514.117) is honestly flagged as unresolved in `FACILITATOR.md` rather than quietly resolved either way. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run, clean. |
| P6 data-decay | **PASS** (after two real fixes) | S4 originally cited a fabricated article ID (`S1067-991X(07)00230-5`, zero web hits) — **fixed** to the correct, independently-verified DOI-matching ID (`S1067-991X(07)00002-8`, confirmed via PubMed ID 17346642 and multiple academic listings) during an earlier pass this session. This re-run's fetch confirmed the corrected ID is real, not a repeat of the original fabrication. Separately, S5 was found to bundle three distinct cost figures ($277 mean, $10-$1,300+ range, $72/$199 online-offline) under one URL that only substantiates the first — **fixed** by narrowing S5's `value`/`claim` in `case.md` Appendix D and `case.json` to only the figure the cited URL actually contains, removing the two mis-attributed figures rather than leaving them wrongly sourced. All other sources (S1, S2, S3, S6, S7, S8) confirmed live and accurate; S2/S8 return empty/blocked content to automated fetch tools but are independently corroborated as correct via search-indexed snippets (bot-gating, not real dead links). |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Three real defects
were found and fixed during this run (P2/P3's shared MA1 ambiguity, P6's fabricated S4 citation
fixed earlier this session, P6's S5 mis-attribution).

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 2`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
