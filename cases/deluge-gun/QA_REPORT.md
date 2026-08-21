# QA_REPORT.md — Deluge Gun

## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

1 advisory finding (not blocking): the standard `<!-- FACILITATOR ONLY -->` guard-comment line at
the bottom of `case.md` trips the "names twist/trap/facilitator in student-facing text" heuristic.
This is the exact boilerplate pattern `case-write` SKILL.md §11 mandates (verified identical in
`cases/the-reserve-asymptote/case.md`) — a single self-contained comment line naming where
facilitator content lives, with no content following it. Reviewed and kept as-is.

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 236 words, present tense, no load-bearing numbers |
| T1-03 | PASS | binary dilemma, opens "You are Danny Ruiz." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form consistent |
| T1-06 | PASS | 8 appendices (A–H), no orphans |
| T1-07 | PASS | final appendix is 11 verbatim spine labels (6 vocab, 5 how-to) |
| T1-08 | PASS | every number cited [S1]–[S6] or in the visible Modeling Assumptions block |
| T1-09 | PASS | both arguments written, margin 9.45% ≤ 20% cap |
| T1-10 | PASS | case.json schema valid; all 11 standards ids resolve in the spine |
| T1-11 | PASS | learning-goal mutual reachability (LEARNING_GOALS.md) |
| T1-12 | PASS | T4 numeric load matches declared tier; MA2 is the required T4 stated assumption |
| T1-13 | PASS | FACILITATOR.md: 5 Socratic questions, trap named, anchor ladder complete and correctly ordered, twist present, timed 45-min plan, sensitivity note present |
| T1-14 | PASS | FACILITATOR.md numbers all trace to case.md/case.json (via `case.json.derived` + `balance.computed_values`); balance margin_pct (9.45) appears in FACILITATOR.md |
| T1-15 | PASS | no `published/` dir yet — nothing to check |
| T1-16 | PASS | `case.json.qa.case_md_sha256` matches current `case.md` |
| T1-17 | PASS | 3 cohort bands declared |
| T1-18 | PASS | no `published/` dir — nothing to check |
| T1-19 | PASS | no `published/` dir — nothing to check |

**BLOCKER:** none. **GAP:** none (all resolved iteratively during this run — see "Findings and
fixes" below). **VERDICT: TIER1_PASS.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Two independent fresh subagents (pre- and post-MA3-fix) cold-solved from the leak-free packet alone. Both reached the same defensible position (Option B, High Arc), correctly reproduced all core arithmetic (θ=19.20°/70.79°, apex/time-of-flight, effective GPM, and — post-fix — the y(200) parapet-clearance check), explicitly named the metric they optimized (target-reachability, not raw GPM), named the correct most-sensitive assumption (MA3, then MA1), and named the correct least-supported number (MA2's 2%/s loss rate). Right answer, right route, both times. |
| P2 both-sides | **PASS** | Two independent fresh subagents built genuinely quantitative cases for both A and B (both arguments carry ≥3 numbers; neither is a bare concession). Both times, the subagent identified the same collapse point: A's flow-efficiency argument has no answer to the direct clearance question ("does the Low Arc's trajectory clear the 12 ft parapet at x=200 ft?" — answer: no, 7.7–7.8 ft < 12 ft), while B's case rests on the same physics without needing to dispute any assumption. |
| P3 trap | **PASS** | A fresh subagent, reading case.md only, independently predicted the case's real trap (D4-margin tunnel vision, ignoring D3's clearance finding) before opening FACILITATOR.md, and it matched the guide's named trap closely. A second fresh subagent on the final version surfaced a real secondary, worksheet-level trap (apex-height vs. height-at-the-obstruction confusion) that the guide had not explicitly called out as "a trap to watch for" — FACILITATOR.md's "## The trap" section was extended with a third, worksheet-level trap naming this exact confusion, closing the gap. |
| P4 twist | **PASS** (after 1 fix cycle) | **Finding 1 (real defect, fixed):** initial adversarial check found the twist's clearance claim rested on apex-height comparisons (19.6 ft / 161.5 ft) rather than height at the parapet's actual location — since a trajectory returns to height 0 exactly at its own range, apex height does not describe the obstruction's location. Fixed by adding MA3 (a stated parapet height/distance) and a new required D3 sub-step computing trajectory height via $y(x)=x\tan\theta-gx^2/(2v^2\cos^2\theta)$ at the parapet's actual location; re-verified independently, both arcs' clearance/blocked verdicts confirmed correct at the case's stated numbers. **Finding 2 (real fragility, disclosed):** a second adversarial check found the resulting clearance verdict flips under a small MA1 flex (≈+9 ft / 6% on the stated 150 ft structure height, holding MA3's distance fixed as the stated convention requires) — a first facilitator note claiming otherwise was mathematically wrong and was corrected. `FACILITATOR.md` and `case.json.modeling_assumptions[MA3].sensitivity` now state the exact, verified crossover (~159 ft) as an honest, disclosed fragility, explicitly distinguished from the primary metric's confirmed ±50%-robust margin. A third fresh subagent independently re-verified the corrected numbers and returned PASS. |
| P5 sensitivity | **PASS** | `sensitivity_model.py` ships `PARAMS`/`FLEX`/`evaluate()`. Both stated assumptions (`structure_height_ft` = MA1, `wind_loss_rate_pct_per_s` = MA2) swept ±50%: winner stays A (Low Arc) in all four flexes; margin stays inside the SPEC §2 20% cap in all four (4.0%–15.3%). No flip, no cap breach — the *primary metric* is robust. (The separate, disclosed D3/MA3 clearance fragility found under P4 is not a P5 finding — P5 only sweeps the two declared `FLEX[]` assumptions against the primary A/B metric, which stayed stable throughout.) |
| P6 data decay | **PASS** | All 6 `sources[]` URLs were fetched live during `case-research` earlier this session (2026-08-19/20) via `WebFetch`, with the exact cited text quoted and confirmed present on each page at fetch time: S1 (firehouse.com, Naum), S2 (cdc.gov — returned HTTP 403 to automated fetch; downgraded to MEDIUM and used only for general supporting context, not for any cited number), S3 and S4 (fireengineering.com, Polenzani and Shapiro), S5 (openstax.org), S6 (tft.com). Zero decay risk given same-session sourcing; no dead links, no drifted figures. S2's 403 is a pre-existing, disclosed access limitation (see `sources[].note`), not a decay finding — nothing about it changed during this QA run. |

**VERDICT: TIER2_PASS — 0 FAIL, 6/6 probes recorded by name, 0 NOT RUN.**

### Findings and fixes applied this run (chronological)

1. T1-14 BLOCKER (margin_pct not in FACILITATOR.md) — fixed by writing the exact `9.45` figure
   into FACILITATOR.md's arithmetic note (margin corrected from an initially-mis-keyed 8.64% —
   see item 3).
2. T1-13/T1-07/T1-14 GAPs (Socratic questions not machine-parseable due to line-wrapping; final
   appendix missing 6 already-covered skill labels; several rounded numbers in FACILITATOR.md not
   traceable to case.json) — all fixed: Socratic questions rewritten as single lines; Appendix H
   extended to all 11 claimed labels; a `case.json.derived` object added to carry every
   intermediate figure FACILITATOR.md states.
3. **Margin-convention bug, self-caught while wiring P5:** `case.json.margin_pct` was originally
   computed as (winner−loser)/**winner** = 8.64%, inconsistent with this project's own convention
   (confirmed against `tier2_probes.py`'s `probe_sensitivity` and against
   `the-reserve-asymptote`'s worked margin) of (winner−loser)/**loser** = 9.45%. Corrected
   throughout case.md-adjacent files (case.json, FACILITATOR.md, sensitivity_model.py docstring).
4. `sensitivity_model.py` v1 returned extra debug keys alongside `A`/`B`, which broke
   `tier2_probes.py`'s implicit "exactly two keys" contract and produced a nonsensical ~21,000%
   "margin" by picking a stray key as the loser. Fixed by narrowing `evaluate()`'s return to
   `{"A":..., "B":...}` only and moving debug fields to a separate `evaluate_debug()`.
5. P4 twist-integrity found a real defect (apex-height-only clearance claim) and, after a first
   fix, a real residual fragility (mis-stated in the first correction attempt) — both described in
   the Tier 2 P4 row above. This is the only probe that took more than one adjudication cycle.

### Tier 3 — human dry-run

NOT RUN. `PUBLISHED` is reachable without Tier 3; `VERIFIED` is not. No RUN_REPORT has been filed
because this case has not been published or assigned to a real cohort.

---

**Hash of record:** `sha256(case.md)` = `105802ead69634d03cb3d58cdb2162f416ccf1347372515d26360d4eac6f8f40`
(matches `case.json.qa.case_md_sha256` as of this report).
