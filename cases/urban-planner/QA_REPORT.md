# QA Report — Urban Planner / City Planner

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
19 checks: 18 PASS, 1 GAP, 0 FAIL (T1-10, expected legacy carve-out).

**VERDICT: TIER1_PASS (0 blockers, 1 gap)**

### Tier 2 — simulated play (6 probes)

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Chose Site B via a justified weighted-criteria composite (Capacity 40/Accessibility 35/Cost-efficiency 25), reproduced all D1-D4 arithmetic exactly, cross-checked against the case's own example weighting, correctly identified MA3 (Hayden Island's 50%-of-total-acreage split) as the most sensitive assumption. |
| P2 both-sides-solve | **PASS** (after a real fix) | Fresh subagent found the Dilemma text asserted Option B draws "the least neighborhood opposition" with zero supporting data anywhere in Appendices B-H — an unsupported claim presented as a selling point. **Fixed**: reworded to a claim the case's own data actually supports (largest usable acreage of the two sites), in both `case.md`'s Dilemma line and `case.json.options.B`, rather than inventing a source for the original claim. Both sides' real quantitative arguments (A on accessibility, B on capacity) hold up independently; cost-efficiency is confirmed a near-total wash (<0.1% difference). |
| P3 trap-check | **PASS** | Fresh subagent, packet-only, independently named the same trap FACILITATOR.md describes: students correctly compute D1-D3 but then treat D4's weight-selection step as a formality (copying the example weights or splitting evenly) instead of the actual analytical decision the case is testing. |
| P4 twist-integrity | **PASS** | Mechanically verified via `sensitivity_model.py`: the twist (developed-footprint assumption halved for Site B) genuinely reverses the recommendation under the case's own example weighting (7.68→8.85 for A vs. constant 8.16 for B). One disclosable caveat noted: a sharp student could raise a magnitude-based objection (the case's site only ever needed ~1% of its acreage, so why would losing unused land shrink that) — this is a legitimate discussion thread already covered by Appendix F's standing invitation to challenge any assumption, not a hidden dependency that neutralizes the twist. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run, clean. |
| P6 data-decay | **PASS** (after two real fixes) | S12 claimed a fabricated mid-year IRS mileage-rate increase to $0.76/mile (IRS standard mileage rates are set once annually, not revised mid-year) — the live IRS page confirms only $0.725/mile effective January 1, 2026. **Fixed**: corrected in `case.md`, `case.json`, and `sensitivity_model.py`; recomputed via the model — margin_pct unchanged at reported precision (6.3%) since shuttle cost is a small fraction of total cost either way. S2's degree-length conversion constants (69.0 mi/deg lat, etc.) are correct standard geodetic values — the cited page just presents the same figures in km, not an actual error, left as-is. S5 (a non-load-bearing sanity-check link) is dead (expired SSL) and S10 is bot-blocked/unconfirmable automatically — both flagged for awareness, neither load-bearing nor blocking. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Two real defects
were found and fixed during this run (P2's unsupported "least opposition" claim, P6's fabricated
mid-year mileage-rate figure).

**Tier 1 clean (0 blockers) AND all six Tier 2 probes PASS → state promoted to `TIER2_PASS`.**
`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `run_on: "2026-08-20"`,
`blockers_open: 0`, `gaps_open: 1`, `case_md_sha256` recorded. Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`. **Note on subject matter:** this case touches homeless-encampment siting, a genuinely
sensitive real-world topic — the conversion kept a factual, matter-of-fact tone throughout and
neither option is editorialized; worth a human read before publishing given the topic.
