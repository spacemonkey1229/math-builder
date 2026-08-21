## case-readiness run — 2026-08-20
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Two real defects were found by independent Tier 2 probes during QA (original run), fixed, and
re-verified by fresh independent sub-agents before this verdict was recorded.

### Defect 1 — P4 twist-integrity, originally FAIL

The Twist claimed coordination calls "actually take TWICE as long as assumed" — 30 minutes instead
of MA1's chosen 15. Appendix A ("The Survey Rules") and Background both explicitly and repeatedly
state, as a hard given fact of the survey (not a challengeable assumption): "Every call — guide
coordination or learner interview — runs 15–20 minutes." Doubling to 30 minutes put the twist's
coordination-call length 10 minutes past the case's own explicitly declared upper bound for ANY
call in this survey, directly contradicting a stated fact rather than flexing a genuine assumption.

**Fix:** the twist now pushes coordination calls to the TOP of the case's own already-stated
15–20 minute range (20 min, not a fabricated 30 min) instead of doubling past it. Changed in
`sensitivity_model.py` (`evaluate_twist()` now sets `coordination_call_min` to 20.0, docstring
rewritten to explain the in-range framing), `FACILITATOR.md` (twist delivery text and the
45-minute-plan twist row), `case.json.modeling_assumptions[MA1].sensitivity`, and `RESEARCH_LOG.md`.
Twist numbers recomputed: base A=51.23h / B=53.92h (5.25% margin, unchanged) → twist A=54.50h /
B=58.08h (6.58% margin). Option A still wins both times — the twist widens rather than narrows A's
margin (B pays the extra 5 min/call across all 50 campuses it always reaches; A pays it only across
the expected 39.235 campuses it reaches), which is itself the pedagogically interesting result: a
naive room expects the twist to hurt A, and it doesn't.

### Defect 2 — P2 both-sides-solve, concerning finding (not a hard FAIL)

Two independent fresh probes (P1 cold-solve and P2 both-sides-solve) both found that Option A's
framing ("fitting Jeff's tight 3-month timeline") oversold its real advantage. The actual math:
Option A saves only ~2.7 hours of call time (5.25% margin) against a 3-month runway with enormous
slack — a peer question ("would B have blown your deadline?") deflates that framing instantly, since
the answer is clearly no. Meanwhile Option B's real benefit (avoiding ~10.8 of 50 campuses, ~21.5%
of the network, getting zero survey representation) is large and concrete, making Option A read as
weaker than it should for a genuinely balanced case.

**Fix:** reframed Argument A in `case.json.balance.argument_a` and `FACILITATOR.md`'s "Argument for
A" section to explicitly kill the "tight timeline" framing (naming the deflating peer question
directly) and instead lean on a real, defensible, previously-unused advantage: administrative
simplicity as a genuine operational cost distinct from the hours already counted in the primary
metric — Jeff runs the whole survey alone, one call at a time, with no team to divide the
bookkeeping; SRS needs one flat draw of 1,420 IDs, while Stratified requires him to carry 50
separate running quotas simultaneously (Appendix C's largest-remainder table) with real risk of
over/under-shooting a campus along the way. Also reworded the Option A label itself in `case.json`
(`options.A`) and `case.md`'s Dilemma section to match (dropped "tight timeline," kept "simplest to
administer" grounded in the no-quota-tracking fact), since the same misleading framing originated
there. Margin (5.25%) and winner (A) unchanged — well under SPEC §2's 20% balance cap, so no
retuning was needed, only honest rewording.

`case.md`'s sha256 changed as a result (`0e62f64d69f321ebe8617f16e9bb31061dbc103d50056af95fc61fb3f1ea7517`)
and is recorded in `case.json.qa.case_md_sha256`.

### Tier 1 — structural (19 checks)
Re-run after both fixes (`tier1_structural.py --case acton-survey`): 17 PASS, 2 GAP, 0 BLOCKER.

| id | result | note |
|---|---|---|
| T1-01..T1-09, T1-11..T1-13, T1-15..T1-19 | PASS | 17/19 clean |
| T1-10 | GAP | `new_coverage[]` empty — legacy-conversion carve-out, pre-existing, project-owner approved, not caused by this fix |
| T1-14 | (was GAP, now resolved) | initially flagged a new derived number (`2.7`) introduced in the FACILITATOR.md reframe of Argument A; fixed by citing the already-recorded 51.23h/53.92h figures instead of a new unchecked derived number |

BLOCKER (0) / GAP (1, T1-10, pre-existing carve-out) / POLISH (5, cosmetic, unrelated to these fixes).

### Tier 2 — simulated play (6 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Original run: fresh solver reached a defensible position (Option A, total-call-time metric) with correct arithmetic. Unaffected by the two fixes (neither changed the base numbers or the primary metric). |
| P2 both-sides-solve | **PASS (re-verified)** | Fresh sub-agent, no knowledge of the fix, independently attacked Argument A with the "would B have blown your deadline?" question. Confirmed the "tight timeline" framing is now explicitly and preemptively killed in `FACILITATOR.md`, and Argument A instead rests on two verified-legitimate claims: per-campus-quota coordination overhead (50 simultaneous quotas vs. one flat draw) and individual-learner fairness. Argument B's 21.5%-of-network shutout claim independently reconfirmed exact. Verdict: genuinely balanced, neither side collapses under pressure, no concerning findings remain. |
| P3 trap check | PASS | Original run: the trap the case contains (stopping at a scary per-campus shutout percent without tallying the call-time cost of fixing it) matches the trap `FACILITATOR.md` names. Unaffected by the fixes. |
| P4 twist-integrity | **PASS (re-verified)** | Fresh sub-agent, no knowledge of the fix, independently confirmed Q1 (the twist still forces real recomputation — base 5.25% margin → twist 6.58% margin, without flipping the winner, so it is not a no-op) and Q2 (the twist now stays inside Appendix A's own explicitly stated 15–20 minute bracket rather than contradicting it — coordination calls move to 20 min, the top of the stated range, not a fabricated 30 min past it). `sensitivity_model.py`'s `evaluate_twist()` output (A=54.50h, B=58.08h) confirmed correct by direct execution. |
| P5 assumption-sensitivity | PASS | Machine-run via `tier2_probes.py`. Swept all 3 declared assumption dials (`coordination_call_min`, `learner_call_min`, `sample_fraction`) at ±50%: winner never flips (A wins every scenario when read for the correct "lower is better" direction), margins range ~1.8%–19.3%, never breaching the 20% balance cap. Unaffected by the fixes — `PARAMS`/`FLEX`/`evaluate()` were not changed, only `evaluate_twist()`. |
| P6 data decay | PASS | Original run: all 3 cited sources (S1 internal roster export, S2 hypergeometric-distribution LibreTexts page, S3 Hamilton's-method LibreTexts page) reachable with figures intact, no drift. Unaffected by the fixes. |

### Tier 3 — human dry-run
NOT RUN
