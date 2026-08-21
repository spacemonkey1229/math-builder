# QA Report — Movie Producer

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
19 checks: 17 PASS, 2 GAP, 0 FAIL (T1-10 expected legacy carve-out; T1-14 a guide-only derived
figure now recorded in `case.json.derived`, see below).

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

### Tier 2 — simulated play (6 probes)

Three real, non-trivial defects found and fixed during this run — two source-citation errors and
one undisclosed modeling convention in the Twist — none of which changed which film wins.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Reproduced all D1-D6 arithmetic exactly (Waves: 0.954x-1.15, r=0.97; Flower's Ice: 0.634x+2.63, r=0.80), chose Waves via revenue-per-production-dollar (0.265 vs 0.233), correctly named Appendix E's addressable-audience figure as the least-supported number and Appendix C (Rebecca's prior slate) as the deliberately-irrelevant appendix. |
| P2 both-sides-solve | **PASS** | Fresh subagent confirmed Flower's Ice's raw-revenue pitch collapses first, at the case's own stated judging rule (own-budget ratio, not rival comparison, per Background) — 0.233 &lt; 0.265 — with no fallback number once that framing is challenged. Waves' weaker point (only a 13-30 age stratum of the full 87-person sample shown) is real but survivable. This is the case's intended tension, not a defect. |
| P3 trap-check | **PASS** | Fresh subagent's cold-read prediction of the trap (raw bigger-sample/bigger-revenue reasoning, ignoring per-budget normalization) matched FACILITATOR.md's named trap closely, including both contributing mistakes ("more data" bias and unnormalized dollar comparison). |
| P4 twist-integrity | **PASS** (after a real fix) | Original defect: the Twist's specific post-correction margin (36.0%) rests on an unstated convention — pegging Flower's Ice's bias-corrected rate to Waves' own observed rate as the implicit "true" reference point — that isn't forced by the cited Pew finding, and a different, equally defensible convention (applying the 30% retention to the dollar gap directly) yields a different magnitude (42.6%). Independently re-verified: under every convention tried, Waves still wins, so the twist's *direction* is robust even though its *exact size* is not. **Fixed**: added an explicit disclosure paragraph to `FACILITATOR.md`'s Twist section naming the convention, the alternate reading, and the correct facilitator answer if a Hero pushes on it; recorded the alternate figure in `case.json.derived.twist.margin_pct_after_twist_alt_convention` so it's checkable rather than a silent guide-only number. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run (`--flex 0.5`), clean. Neither addressable-audience nor twist-retained-fraction swept ±50% flips the winner or the 13.8% base margin outside the 20% cap. |
| P6 data-decay | **PASS** (after real fixes) | Two real citation defects found: (1) S3 (Pew Research) was cited to the wrong report — the 8.4-to-6.0-point/24-benchmark bias figure actually comes from Pew's January 2018 "Reducing Bias on Benchmarks" report, not the May 2016 "Evaluating Online Nonprobability Surveys" report, which studies different benchmarks entirely and does not contain this figure. **Fixed**: re-sourced S3 in `case.json` to the correct 2018 report/URL. (2) S2 (Thoolie P&A guide) was cited to support a "20-30% of production budget" marketing-share rule of thumb that does not appear anywhere on the live page — the page instead gives named examples (1.1x-4x production cost) and a "roughly twice production budget" breakeven rule. **Fixed**: reworded S2's claim/value in both `case.md` Appendix D and `case.json` to accurately describe what the source states, and reframed the case's own 20-30% planning figure (used in Challenge D6) as a separate, author-stated modeling estimate rather than a number taken directly from S2. S1 (NATO/Cinema United ticket price) confirmed exact and live, no changes needed. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Three real defects
(P4's undisclosed twist convention, P6's two source-citation errors) were found and fixed during
this run, all independently re-verified against the corrected text.

**Tier 1 clean (0 blockers, 2 gaps) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 2`, `case_md_sha256` recorded (re-hashed
after the case.md/case.json/FACILITATOR.md fixes above). Per SKILL.md's ladder, `case-publish` may
now run — Tier 3 (a filed human `RUN_REPORT`) remains required before `VERIFIED`.
