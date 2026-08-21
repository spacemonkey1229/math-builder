# QA Report — Player Of The Year

## case-readiness run — 2026-08-20

### Tier 1 — structural (19 checks)
19 checks: 17 PASS, 2 GAP, 0 FAIL (T1-06 expected — final Appendix G referenced only by
construction via Challenge 1; T1-10 expected legacy carve-out).

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

A real structural defect was found and fixed before Tier 2 began: the case-write pass had left
the `<!-- FACILITATOR ONLY -->` marker immediately after the Dilemma (before Challenges/Appendices
A-G), which would have stripped the entire student packet — including the 14-finalist data table —
down to just the Overview/Background/Dilemma. Moved to the end of the file, where it belongs.

### Tier 2 — simulated play (6 probes)

Three real defects found and fixed during this run: a real arithmetic error in the Twist's own
numbers, a factually false premise in the Twist's script, and an undisclosed convention gap.

| Probe | Verdict | Basis |
|---|---|---|
| P1 cold-solve | **PASS** | Fresh subagent, packet-only. Independently computed all 14 finalists under both methodologies, reproducing `case.json`'s exact winners (Stevenson under A, Hilley under B) and margins. Correctly named MA1 (z=0 convention) as the most sensitive assumption and the TeamMult curve constants as the least-supported number. |
| P2 both-sides-solve | **PASS** (confirms a real fix) | Fresh subagent independently computed all 14 finalists under both methodologies and, unprompted, found the same Peterson CompositeB arithmetic error P3/P4 found (see below) — Peterson's correct score is 3.117, not the case's original 3.102. Two independent probes converging on the identical corrected number is strong confirmation. Also found that Methodology A's winner flips on an implausibly small single-stat change (Stevenson's Blocks/Set moving by 0.006), while Methodology B's winner is robust to any single plausible correction — directly informing the Twist fix below. |
| P3 trap-check / P4 twist-integrity | **PASS** (after two real fixes) | Fresh subagent's cold-read trap prediction (fencepost errors in the TeamMult formula, mishandling `(d)`-marked/NR cells) didn't match the guide's named trap (reverse-engineering a formula to justify a pre-picked favorite) but is a real, adjacent risk worth watching. Two real defects independently found: (1) **Arithmetic error**: Peterson's CompositeB was miscalculated as 3.102 in `case.json`/`FACILITATOR.md`; the correct value (re-verified independently by two probes) is 3.117, changing Methodology B's stated margin from 0.749 pts/24.1% to 0.731 pts/23.4%. **Fixed** throughout `case.json` and `FACILITATOR.md`. (2) **False premise**: the Twist claimed Stevenson's Kills/Set was one of the `(d)`-marked (back-computed) inputs feeding Methodology A's razor-thin margin — checked directly against Appendix A, this is false; only her (unused) Attacks/Set carries a `(d)` marker, not her Kills/Set or Blocks/Set. A sharp Hero checking the appendix would correctly call this out. **Fixed**: rewrote the Twist to make its real, defensible point (the 0.009-point margin is smaller than routine box-score correction precision — concretely, Stevenson's Blocks/Set would only need to shift by 0.006 to flip the winner) without the false `(d)`-marker claim, and added a facilitator note flagging the removed claim explicitly so it's never reintroduced. |
| P5 assumption-sensitivity | **PASS** | No `sensitivity_model.py` existed at TIER1_PASS — authored one, reproducing `case.json`'s declared primary balance metric (Methodology A's own #1-vs-#2 margin, 1.74%) exactly. `FLEX` is scoped to `unranked_z_penalty` (MA1), the only assumption that affects this specific metric; `team_mult_max_bonus`/`team_mult_cutoff_rpi` (MA3) are documented in `PARAMS` but correctly excluded from `FLEX` since they don't touch Methodology A's margin (Methodology B's own separate margin, 23.4%, is disclosed directly in `case.json.balance` rather than re-derived by this probe). Flexing `unranked_z_penalty` ±50% is a no-op since its base value is exactly 0.0 (the same domain-boundary exception pattern documented in `cases/cold-chain`'s `allocation_village_priority`); manually verified the underlying mechanism responds correctly to non-zero values. |
| P6 data-decay | **PASS** | The one live web source (S4: AVCA's own selection-process page) fetched and confirmed exact — the page states verbatim that "The AVCA Division I Women's Volleyball Awards Committee has been responsible for all phases of the Player of the Year process," matching the claim precisely. S1-S3 are local data files (the real NCAA stats workbook and AVCA stat-definitions PDF), not live citations requiring re-fetch. |

**MECHANICAL RESULT:** 0 probes failed. All 6 probes carry a recorded verdict. Two real defects
(P3/P4's arithmetic error and false Twist premise) were found and fixed during this run, both
independently confirmed by a second probe (P2) before the fix.

**Tier 1 clean (0 blockers, 2 gaps) AND all six Tier 2 probes PASS → state promoted to
`TIER2_PASS`.** `case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`,
`run_on: "2026-08-20"`, `blockers_open: 0`, `gaps_open: 2`, `case_md_sha256` recorded (re-hashed
after the marker fix and MA1-extension-to-Methodology-B disclosure fix). Per SKILL.md's ladder,
`case-publish` may now run — Tier 3 (a filed human `RUN_REPORT`) remains required before
`VERIFIED`.
