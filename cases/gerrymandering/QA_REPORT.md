# QA Report — Gerrymandering

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
19 checks: 19 PASS, 0 GAP, 0 FAIL.

**VERDICT: TIER1_PASS (0 blockers, 0 gaps)**

### Tier 2 — simulated play (6 probes)

A cleanly designed case — most probes passed without needing a fix, one real data-citation defect
found and fixed.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose Option B via population-deviation math and the *Karcher v. Daggett* precedent; independently caught the S8 arithmetic inconsistency described below before it was flagged by any other probe. |
| P2 both-sides-solve | **PASS** | Confirmed Option B wins decisively on population equality (0.011% deviation vs. Option A's 18.44%), matching the case's own disclosed `argument_a`/`argument_b`. This is intentional case design, not a defect: the graded primary metric is the statewide efficiency gap, a mathematically necessary tie between the two plans (see P4) — population deviation is a separately-disclosed consideration with a genuine county-integrity legal counter-argument for Option A, not the graded metric. |
| P3 trap-check | **PASS** | Fresh subagent independently identified the compactness-vs-population-equality trap that FACILITATOR.md names as its primary trap; the probe's own predicted trap (the efficiency-gap tie being an artifact of Modeling Assumption MA2) turned out to already be the case's own Twist, not a gap in the guide. Both are real, guide-covered failure modes. |
| P4 twist-integrity | **PASS** | Independently and rigorously re-derived the "efficiency gap is identical under both plans" claim from first principles (not just trusting the script) — confirmed it's a mathematically necessary consequence of Modeling Assumption MA2's uniform vote-share assumption (the population/district-count terms cancel algebraically), not a coincidence specific to these numbers. Robust to the one ambiguity found (third-party-vote treatment), since that convention applies symmetrically to both plans. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run, clean. |
| P6 data-decay | **PASS** (after a real fix) | All load-bearing figures (Census population totals, election vote totals, statutory text, efficiency-gap methodology) confirmed exact. One real defect found independently by two probes (P1 and P6): S8's Ada County under-18 figure paired "21.1%" with a raw count of "112,900 residents" that does not reconcile against the 2020 Census population (494,967) used everywhere else in the case (21.1% × 494,967 = 104,438, not 112,900) — the raw count evidently came from a different, later population vintage than the rest of the case. **Fixed**: removed the mismatched raw count from `case.md` and `case.json`, keeping only the percentage, which is the figure actually used in Challenge D4. Two minor, non-blocking items also noted (a 2-sq-mi drift in Ada County's land area, a supplementary media citation that doesn't resolve to the exact claimed episode) — neither load-bearing. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real defect
(S8's internally inconsistent Census figure) was found — independently, by two separate probes —
and fixed during this run.

**Tier 1 clean (0 blockers, 0 gaps) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 0`, `case_md_sha256` recorded. Per
SKILL.md's ladder, `case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains
required before `VERIFIED`. **Note on subject matter:** per the locked dilemma file, all
partisan/party-specific framing was kept out of the case throughout this conversion — confirmed
by P2/P3's independent reads finding no partisan lean anywhere in the materials.
