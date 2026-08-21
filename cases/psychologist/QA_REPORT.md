# QA Report — Psychologist

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
19 checks: 17 PASS, 2 GAP, 0 FAIL (T1-10 expected legacy carve-out; T1-14 a benign continuity
false-positive — the flagged "26" is a plain applicant count in a facilitator-only aside, not a
computed derived value).

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

### Tier 2 — simulated play (6 probes)

Two real defects found and fixed during this run — a mislabeled data figure and an unstated
normalization convention in the Twist — plus one source-attribution overstatement corrected.
Neither fix changed which slates win either ranking.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Independently recomputed all 27 rows of the normalization table and both D3 rankings, landing on Standout Slate = Sophia/Spencer/Riley and Balanced Slate = Sophia/Tyler/Brigitte — an exact match to `case.json`'s recorded `standout_slate`/`balanced_slate`. Chose the Balanced Slate, correctly flagged Spencer's 100%-typing/weak-composite tension as the strongest counter-argument, and correctly named MA1 (pool-relative normalization) as the most sensitive assumption and its own mechanism (Spencer's "100%" typing score is only 56 of a real-world 225 WPM certification bar) as the most assumption-driven number in the case. |
| P2 both-sides-solve | **PASS** | Fresh subagent confirmed both slates are genuinely defensible on the case's own two metrics (single-best vs. composite); Option A's fragility centers on Spencer's Test-3 weakness, a real but non-fatal tension, not a collapse. Intentional case design. |
| P3 trap-check | **PASS** | Fresh subagent's cold-read prediction (students misapplying MA1's normalization rule to typing speed, or comparing raw scores instead of normalized ones) diverges from `FACILITATOR.md`'s named trap (assuming single-best and composite rankings must agree, and skipping building both). Both are real, well-reasoned failure modes tied to the case's actual mechanics — the guide's trap is directly anchored to D3's explicit dual-ranking requirement, so it is not replaced, but facilitators should also watch for the normalization-mechanics slip the probe surfaced. Not a blocking defect. |
| P4 twist-integrity | **PASS** (after a real fix) | Original defect: the Twist's "share 2 of 3 names" result depends on an unstated convention — that Appendix B's category-max denominators (MA1's normalization basis) stay frozen at the original 27-applicant field even after Sophia withdraws. Under the more literal reading (recompute maximums from the remaining 26 applicants), the result changes materially: a six-way tie for the Standout Slate's single-best ranking, and the Balanced Slate's third seat shifts from Riley to Allissa. **Fixed**: added an explicit sentence to Appendix C's MA1 row in `case.md` stating the basis is fixed once at the start and not recomputed on withdrawal, plus a facilitator-only note in `FACILITATOR.md`'s Twist section pre-empting the question if a Hero raises it. Also fixed a real, independently-caught data error: `case.json`'s `argument_b` cited "Spencer (56.2 in Test 3)" — 56.2 is actually Ellie's composite score, not Spencer's Test 3 percentage (which is 33.3). Corrected to the right figure. |
| P5 assumption-sensitivity | **PASS** | Mechanical script run (`--flex 0.5`), clean. Sweeping the typing-weight dial ±50% moves the margin between 7.7% and 11.3% but never flips the winner or breaches the 20% cap. |
| P6 data-decay | **PASS** (after a real fix) | S1 (LegalClarity RPR certification structure) confirmed exact and live — no changes. S2 (Individual Psychometrics composite-scoring coursebook) was reachable and on-topic, but the case's phrasing ("simplest/most transparent approach," "reasonable neutral default") oversold the source, which actually says only that equal weighting is "the most common" approach in clinical practice and does not use that normative language. **Fixed**: reworded MA2's basis text and the S2 sources-table row in `case.md` to attribute only the "most common practice" fact to the source, with the "defensible default" judgment correctly framed as the case's own modeling choice (MA2), not the source's claim. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Two real defects
(P4's undisclosed twist normalization convention plus a mislabeled data figure, P6's source
overstatement) were found and fixed during this run, independently re-verified against the
corrected text (P1's fresh cold-solve, run after the fixes, reproduces the case's own recorded
D3 rankings exactly).

**Tier 1 clean (0 blockers, 2 gaps) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 2`, `case_md_sha256` recorded (re-hashed
after the case.md/case.json/FACILITATOR.md fixes above). Per SKILL.md's ladder, `case-publish` may
now run — Tier 3 (a filed human `RUN_REPORT`) remains required before `VERIFIED`.
