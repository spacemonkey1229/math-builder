## case-readiness run — 2026-08-19
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint
1 advisory finding (the standard `<!-- FACILITATOR ONLY -->` marker comment in `case.md` matched
the "names facilitator/twist/trap" heuristic — this is the documented, intended pattern from
`skills/case-write/SKILL.md` §11 for signaling facilitator content lives elsewhere; not a real
leak). No action taken.

### Tier 1 — structural (19 checks)
First pass: 17 PASS, 2 GAP (T1-07 — three already-covered arithmetic skills claimed in
`standards[]` were missing from Appendix H's "how to…" list; T1-14 — five numbers in
`FACILITATOR.md` had no home in `case.json`/`case.md`). Both fixed: added the three how-to labels
to Appendix H, and added `level_cut_angle_deg`, `ridge_interior_angle_deg`,
`hip_bisect_half_angle_deg`, `complementary_full_angle_deg`, `hip_plus_jack_members_count`,
`new_coverage_skill_count` to `case.json.derived`. `case_md_sha256` refreshed after the Appendix H
edit.

Second pass:

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 218 words, no load-bearing numerals; "six months"/"ninety minutes" cleared as texture |
| T1-03 | PASS | Dilemma binary, opens "You are Colton Marsh." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form `N.)` consistent |
| T1-06 | PASS | appendices A–H, lettered, ordered, no orphans |
| T1-07 | PASS | all 11 final-appendix lines verbatim spine labels (8 vocabulary + 3 how-to) |
| T1-08 | PASS | every number cited (S1–S3) or a declared Modeling Assumption (MA1–MA2) |
| T1-09 | PASS | both arguments written, margin 14.81% ≤ 20% |
| T1-10 | PASS | `case.json` schema clean, standards resolve in spine, `new_coverage[]` non-empty (7 skills) |
| T1-11 | PASS | mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T2 tier matches numeric load (multi-step angle arithmetic + ratio + area normalization, two competing variables) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | continuity — FACILITATOR.md numbers all traced to case.json.derived |
| T1-15 | PASS | no published/ yet, nothing stale |
| T1-16 | PASS | hash current |
| T1-17 | PASS | cohort_bands[] declared, 3 bands |
| T1-18 | PASS | no published/ yet (nothing to check) |
| T1-19 | PASS | no published/ yet (nothing to check) |

BLOCKER (0). GAP (0). POLISH (4): T1-07 label-parsing note (informational); T1-15/18/19 "no
published/ directory yet" (expected pre-publish).

**VERDICT: TIER1_PASS**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh, unbriefed subagent given only the leak-checked student packet reached Option B, correctly named the graded metric (board-feet per sq ft), reproduced the 1.20 vs 1.02 BF/sq ft arithmetic independently, correctly flagged MA2 (the 3× compound-cut multiplier) as the least-supported figure and the assumption its own counter-argument depended on, and correctly identified Appendix A's span table as safety margin it could ignore. Reached the intended answer for the intended reason. |
| P2 both-sides | PASS | Mechanical screen initially FAILED twice (numeric density and a false "concession" match on "grades worse on paper"); both fixed by rewriting `balance.argument_a`/`argument_b` with real figures phrased as affirmative wins for each side, not admissions. Adjudicated: Option A's real floor is the total-cost win ($956.50 vs $997.02, sourced price + stated labor assumptions); Option B's real floor is the material win (14.81%, pure sourced/authored geometry, no assumption dependency). Neither side collapses to zero under pressure — they are defensible on two different real numbers, which is the design intent, not a paper margin. |
| P3 trap | PASS | Read from the case document alone, the most plausible wrong path is: more framing planes and 40 extra individual members (4 hips + 36 jacks) "must" mean more lumber, so Option A "obviously" wins on material without running the D5 takeoff. `FACILITATOR.md`'s "The trap" section names this exact path verbatim ("Most Heroes will look at 'four roof planes and forty extra pieces' and conclude the hip roof must use more lumber"). Guide anticipates the real trap. |
| P4 twist | PASS | (1) The twist invalidates the position "B wins the graded metric, therefore it's the obvious pick" — a real position Anchor 1's vote would produce. (2) Re-derived under the case's own stated Appendix E assumptions exactly as written (one labor charge per rafter for a simple cut, one per hip/jack member for a compound cut, no ambiguous convention) and cross-checked against `sensitivity_model.py evaluate_twist()`'s output: total cost A=$956.50, B=$997.02, matching `FACILITATOR.md` exactly. No unstated convention the twist depends on. The twist fully reverses the winner (not merely erodes the margin), verified mechanically by the P5 script's `evaluate`/`evaluate_twist` divergence. |
| P5 sensitivity | PASS | `sensitivity_model.py` flexes both declared assumptions (`simple_cut_min`, `compound_mult`) ±50%. Neither moves the graded primary metric at all — board-feet-per-square-foot is pure geometry, independent of both assumptions by construction (`case.json.sensitivity_note` states this explicitly, and it is not a leaked answer since it does not disclose the margin or winner value, only that it is invariant to these two dials). No flip, no 20%-cap breach at any flex level. |
| P6 data decay | PASS | S1 (mycarpentry.com) — reachable, value confirmed verbatim ("16-0" for 2×8 DF#2 @16"oc, matching load combination). S2 (NAHB Framing Lumber Prices) — reachable, value confirmed verbatim ($536.15/1,000 BF, August 14, 2026, Madison's Lumber Price Index). S3 (BLS OOH Carpenters) — direct fetch returned HTTP 403 (bot-protection on bls.gov, not a dead link); figure independently confirmed live via web search against the same URL and BLS's own OEWS release data ($28.51/hr median, May 2024). No URL dead, no figure drifted, all sources under 1 year old. |

**VERDICT: TIER2_PASS**

### Tier 3 — human dry-run
NOT RUN. `PUBLISHED` is reachable without it; `VERIFIED` is not. No `runs/` directory yet.

### Corrections made during this run
- Fixed `case.json.balance.margin_pct` (and `case.json.derived.margin_pct`) from an initially
  miscalculated 17.39% to the correct 14.81% — the project's `(loser − winner) / loser × 100`
  margin convention (matching the Vent Cap precedent) divides by the *losing* option's raw value,
  not the winning option's. Recomputed and verified against `sensitivity_model.py`'s own output.
  Also corrected the supplementary total-cost margin from 4.24% to 4.06% under the same convention.
- Added Appendix H how-to labels and `case.json.derived` angle/count fields to clear two Tier 1
  GAPs (see above).
- Rewrote `case.json.balance.argument_a`/`argument_b` to carry real figures and avoid a
  concession-pattern false read, clearing a Tier 2 P2 mechanical FAIL.

**Next step:** human review, then `case-publish` on `roofline-call` (not run by this agent per
instruction — stopping here at `TIER2_PASS` for review).
