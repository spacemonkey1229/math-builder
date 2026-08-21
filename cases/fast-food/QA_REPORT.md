# QA Report — Fast Food

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
19 checks: 18 PASS, 1 GAP, 0 FAIL (T1-10, expected legacy carve-out).

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose Subway via a legitimate capital-fit screen (top of Papa John's investment range, $890,267, exceeds the group's $806,000 total available capital by $84,267; Subway's top of range fits with room to spare). Correctly noted Papa John's wins on raw ROI (26.2% vs 23.2%) and break-even speed, but fails the affordability screen the case's own D1 poses. Reproduced all D1-D6 arithmetic exactly. |
| P2 both-sides-solve | **PASS** | Fresh subagent confirmed both sides have real, defensible numbers. Papa John's "collapses first" specifically at the question of why MA3's bottom-quartile AUV choice was used instead of the system median — but that choice is already disclosed as the case's own load-bearing modeling assumption in `modeling_assumptions`/`sensitivity_disclosure`, not hidden, so this is the intended discussion tension, not an undisclosed weakness. |
| P3 trap-check | **PASS** | Fresh subagent, packet-only, independently named the identical trap `FACILITATOR.md` describes: stopping after D1's raw investment-cost comparison ("Subway is cheaper, therefore better") without running the ROI/break-even math in D2-D6 that says something more nuanced. |
| P4 twist-integrity | **PASS** | Independently reproduced all twist arithmetic exactly (labor cost 30%→34% shared across both options). Confirmed the shared-percentage-point framing is consistent with S11's own disclosed shared-benchmark sourcing note, and that MA1's explicit "headcount is informational only, does not feed any dollar calculation" disclaimer forecloses the one plausible unstated-convention objection (that differing Day-1 headcounts should make the same wage hike hit the options differently). |
| P5 assumption-sensitivity | **PASS** | Mechanical script run, clean. |
| P6 data-decay | **PASS** (after a real fix) | S11 was found to imply its cited source directly states a QSR-specific 30% labor-cost figure; the live page in fact only reports aggregate, all-restaurant-segment distribution buckets (no quick-service-specific number). **Fixed**: reworded S11 in `case.md` and `case.json` to accurately describe 30% as this case's own derived estimate from the aggregate data, not a value quoted verbatim from the source. All other load-bearing sources (S1-S10, S13) confirmed exact and live. S12 has a minor, non-blocking characterization nuance (cited value comes from a secondary "good range" callout, not the page's primary range). S14b shows trivial price drift (~$1/sq ft, non-load-bearing supplemental figure). S15 is blocked to automated fetch (403) but plausibility-corroborated via search snippets. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. One real defect
(P6's S11 mischaracterization) was found and fixed during this run.

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
