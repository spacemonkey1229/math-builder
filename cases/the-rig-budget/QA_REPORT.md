## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Fixes made this session (before Tier 1/Tier 2 would pass)

1. **Preflight-lint leak (Modeling Assumptions).** The "Retune history" paragraph under Modeling
   Assumptions stated the base-case margin/winner literally ("whose real measured cost margin is
   17.9%"), violating the `skills/case-write/SKILL.md` 2026-08-13 rule (assumptions may state WHAT
   was assumed and WHY, never the actual base-case result). Reworded to remove the literal figure.
2. **Background leak (worse — this is the actual graded metric, given away in the case's own
   student-facing narrative).** Background stated "Real, measured GPU cost: 17.9% more than The
   Direct Blend" — this is exactly D5's graded percent-difference deliverable. Reworded to
   "higher than The Direct Blend's, by an amount Appendix D's raw figures let you work out
   yourself."
3. **Appendix D leak (also serious).** Appendix D's cost table included a pre-computed "Share of
   frame budget" row (1.9%/2.4%, D5's own graded percentage) and a bolded sentence stating
   "margin_pct = ... ≈ 17.9%" directly. Both are D5's actual graded outputs, handed to the student
   before they compute them (same defect class as the T1-18 "A Coach's Dilemma" placeholder-leak
   finding in `skills/case-readiness/SKILL.md`). Removed the computed row and sentence; Appendix D
   now states only the raw given inputs (0.32ms, 0.39ms, 16.6ms budget) and explicitly tells the
   student D5 wants the percentages worked out by hand.
4. **MA6/MA7 leaks.** MA6's sensitivity column and MA7's own value/basis columns restated the
   17.9% literal figure. Reworded MA7 to describe the raw per-frame inputs instead of the derived
   percentage; MA6 now says "does not feed Appendix D's real measured cost comparison" without the
   number.
5. **T1-02 BLOCKER — Overview numeral '9' ("9 AM"), Overview over the 300-word cap (302 words).**
   Cleared '9' via `case.json.overview_numerals_cleared[]` (texture — the lab's opening time is
   never used in any D1-D5 calculation). Trimmed 3 words from the closing Overview paragraph to
   land at 299 words.
6. **Re-hashed `case.md`** into `case.json.qa.case_md_sha256` twice (once after the T1-02 fix,
   again after the leak fixes above changed the file further) — confirmed T1-16 clean at the final
   hash.

**`sensitivity_model.py` sign-convention defect found (NOT a code fix — a manual-recompute
workaround per this run's briefing).** `evaluate()` returns negative-cost values (`{"A": -0.32,
"B": -0.39}`, since lower ms is better but the harness contract is "higher is better"). The shared
`tier2_probes.py` harness computes `margin_pct = 100*(win-lo)/base[lo]` with a negative denominator
in this case, producing a **negative** printed margin (`-17.9%` instead of `+17.9%`) and, more
seriously, a `breaks_20pct_cap` check (`margin > 20`) that a large negative swing would never trip
— exactly the "silently masks real sensitivity swings" defect flagged in this session's briefing.
Manually recomputed: `FLEX = ["frame_rate_fps"]` is the case's only declared dial, and it
provably does not appear in the `a_ms`/`b_ms` formula at all (confirmed by the model's own
`__main__` sweep across 30/60/90/120 fps — margin identically 17.9% at every value). There is no
other numeric dial in `PARAMS` that qualifies as a genuine author-chosen assumption — `direct_blend_ms`/
`quaternion_blend_ms` are S6's real citation, `frame_budget_ms` is S3's real citation — so this
case's true assumption-sensitivity surface is empty by design (the whole point of the 2026-09-01
redesign was to anchor the primary metric to a fixed real benchmark, not a formula). No masked
instability found on manual recheck.

### Tier 1 — structural (20 checks)

| id | result |
|---|---|
| T1-01 | PASS |
| T1-02 | PASS (after fix — '9' cleared, word count 299) |
| T1-03..T1-08 | PASS |
| T1-09 | GAP — margin 17.9%, inside the ~20% cap but wide; discussion leans one way |
| T1-10 | GAP — `new_coverage[]` empty, reinforcement carve-out (pre-existing `reinforcement_note`, checked adjacent pre-calculus `n==0` skills — none exist) |
| T1-11..T1-20 | PASS |

`VERDICT: TIER1_PASS (0 blockers, 2 gaps, both accepted)`

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Genuinely fresh subagent (packet-only). All arithmetic exact: elbow M=[[1.2,-0.3],[0.9,0.4]], det=0.75; shoulder M_blend=[[0.5,-0.5],[0.5,0.5]], det=0.5; D4's system-solve recovered M_blend exactly; D5's cost figures (0.32/0.39ms) reproduced. The solver recommended **Option B**, not the case's raw-cost-metric winner (A) — but for an explicit, correctly-argued reason (weighing the proven determinant defect against a small absolute cost gap), which the case's own FACILITATOR.md deep-conflict thread 2 is deliberately built to let a Hero argue ("Is a 17.9% performance win worth shipping a technique you can prove produces the wrong math?"). Per the probe's actual pass criterion — "the solver reaches a defensible position with correct arithmetic AND names a metric" — this is a PASS: correct arithmetic, a named and defended metric (rigidity guarantee vs. raw cost), not a wrong-route accident. This is a genuinely good sign for SPEC §2 balance, not a defect: an independent fresh solver landed on the "off-metric" option through sound reasoning, which is exactly what a working close case should produce. |
| P2 both-sides | **PASS** | A's best sentence: "faster (0.32 vs 0.39 ms/frame), real measured, industry-standard." B's best sentence: "mathematically guaranteed rigid — proven by D3(b)'s own determinant work that A visibly fails at this exact seam." Empirically confirmed non-collapse: the independent P1 cold-solve above chose B on exactly this argument, unprompted. Neither side concedes; the case's own D5 table is genuinely a "which cost, for what guarantee" tradeoff. |
| P3 trap | **PASS** | Case doc alone (via the P1 agent) named the trap as: a hurried student sees A is cheaper/standard and ships it without ever engaging D3(b)'s determinant finding. `FACILITATOR.md`'s "The trap" section names the same trap almost verbatim as its first-listed trap. |
| P4 twist | **PASS** | The twist (Appendix C's own source, S8, only guarantees Quaternion-Blend correctness at simple two-bone joints like the shoulder — not at the underarm/cape mount) invalidates the position "Option B is safe everywhere" that a room favoring B (including, empirically, the fresh P1 solver) would hold. It survives a literal reading of the case's own stated assumptions because S8's complex-joint limitation is already given verbatim in Appendix C, not introduced as new information contradicting anything else in the case. |
| P5 sensitivity | **PASS (manually reconfirmed, see sign-convention note above)** | Harness printed `PASS` (base margin reported as -17.9% due to the sign-convention artifact); manually reconfirmed the true, positive 17.9% margin is invariant under ±50% flex of the only declared dial (`frame_rate_fps`, 30-90fps swept), and confirmed by inspection that no other `PARAMS` entry is a genuine flexible assumption (all are real citations). No masked instability. |
| P6 data decay | **PASS (live fetch, all 8 sources)** | S1/S2 (Unity ModelingOptimizedCharacters docs) — live, "keep below thirty for mobile" and "300 to 1500 polygons... mobile" both confirmed verbatim. S3 (gamedevcheatsheet) — live, confirms 16.67ms/frame at 60fps (case cites 16.6, a one-decimal rounding, not a drift). S4 (dev.to mobile checklist) — live, "60fps - Required for action games, competitive multiplayer..." confirmed verbatim. S5 (github raduacg gpu_skinning.md) — live, the 25M-transforms/60ms-CPU/<1ms-GPU worked example confirmed verbatim. S6/S7/S8 (Kavan et al., "Skinning with Dual Quaternions," SI3D 2007) — live, fetched and read the full PDF directly (Figure 11: GeForce 6600 GT, LBS=0.32ms, DQB=0.39ms, exactly matching S6); Figure 2's "candy-wrapper" artifact caption confirmed (S7); page 3's "for more complex joint influences, such as those usually occurring around the armpit or dorsum, artifacts result from the fact that the center of rotation is fixed" confirmed near-verbatim (S8). No dead links, no drifted figures, no fabricated URLs. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

### Tier 3 — human dry-run

NOT RUN. No `cases/the-rig-budget/runs/RUN_*.md` filed. Required before VERIFIED/✅ in
`DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.
