## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

**Verdict-leak fix found and fixed during packet-build (post-Tier2, pre-publish):** Appendix E's
worked cost table stated the literal computed margin ("Margin: ... ≈ 17.0%") directly in
student-facing `case.md` — this is D4's own graded deliverable, given away before the student
computes it. Removed the sentence, replaced with a pointer back to D4. The Modeling Assumptions
MA5 sensitivity note also restated the same base-case value ("raise the margin from ≈17.0% to
≈55.9%") — reworded to describe the counterfactual model's effect without repeating the base
number. Re-hashed `case.md` after the fix; Tier 1 re-verified clean (0 blockers, 3 gaps,
unchanged). No other case in this batch was found to leak its base margin/winner in `case.md`
(checked all 8 for the same pattern).

Remediation this session: added `(SEE APPENDIX G)` reference to Background so the final standards
appendix is named by letter (was T1-06 GAP). Added `reinforcement_note` to `case.json` after
checking the full Advanced Operations domain for `n==0` adjacent skills — none exist as of
2026-09-01, so `new_coverage[]` empty is a genuine reinforcement, not padding (T1-10 downgraded to
GAP per the documented carve-out). Recorded `qa.case_md_sha256` (T1-16).

| id | result |
|---|---|
| T1-01..T1-08 | PASS |
| T1-09 | GAP — margin 16.98%, inside the ~20% cap but wide; discussion will lean one way |
| T1-10 | GAP — `new_coverage[]` empty, reinforcement carve-out (`reinforcement_note` present) |
| T1-11..T1-13 | PASS |
| T1-14 | GAP — 1 orphan number in FACILITATOR.md (56.0); guide-only derived figure, not moved into `case.json.derived` |
| T1-15..T1-20 | PASS |

`VERDICT: TIER1_PASS (0 blockers, 3 gaps, all accepted — none touch the numbers a student sees)`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading the packet alone: 2²⁰=1,048,576, 2²⁴=16,777,216, ratio=2⁴=16×. Appendix D's calibrated linear gate-count model gives 200/240 two-qubit gates. Success probabilities (1−0.00464)^200≈0.3945 and (1−0.00464)^240≈0.3275 are unambiguous arithmetic. Cost-per-successful-shot: $0.2028 (A) vs $0.2443 (B), margin ≈17.0% — matches `case.json.margin_pct` (16.98%) to rounding. The metric (dollars per successfully-completed shot) is explicitly named by D4's own wording, so a solver reaches Option A with correct, traceable arithmetic and no ambiguity about which number is the answer. |
| P2 both-sides | **PASS** | A's best sentence: "17% cheaper per successful shot, real published hardware numbers, fits this quarter's budget." B's best sentence: "the only option that represents all 24 of the client's variables exactly — A's savings come from quietly punting 4 lanes to an un-costed classical fallback (MA3), a real qualitative risk D4's dollar figure never captures." Neither side collapses to a concession — B's argument survives even after conceding the 17% cost gap, because it targets a different axis (solution completeness vs. cost), which is the real tension SPEC §2 wants. |
| P3 trap | **PASS** | The stated trap ("24 qubits is exact settles it" vs. "Option A is cheaper settles it," each ignoring the other axis) is the single most plausible failure mode given the deliverable order (D1 proves exactness, D4 proves cost) — a rushed student stops at whichever they reach first. FACILITATOR.md names this exact trap. |
| P4 twist | **PASS** | The twist (recompute gate counts using IonQ's own n² #AQ worst-case formula instead of the case's calibrated linear model) is a real, disclosed second reading of the *same* source (S2), not new data. Under it, Option A still wins but the margin jumps from ≈17.0% to ≈55.9% — this invalidates the "nail-biter, either pick is fine" reading a room would likely take from a 17% margin, without making Option B correct. Survives every legitimate reading of MA5 (both models are anchored to the same real S2 anchor point at width≈20). |
| P5 sensitivity | **PASS** | `sensitivity_model.py` reproduces the base case: A=−0.2, B=−0.24 (arbitrary sign convention), margin ≈17.0%, matching `case.json.margin_pct` (16.98%) to rounding. Flexing both declared dials (`gate_error_rate`, `gates_per_qubit`) ±50% never flips the winner and never breaks the 20% cap (max swing to −24.4%, still under cap, still Option A). |
| P6 data decay | **PASS (live fetch)** | S1 (AWS Braket pricing) — live, both figures confirmed verbatim: $0.30/task, $0.08/shot for IonQ Forte. S2 (arXiv:2308.05071) — live (HTML mirror), both load-bearing figures confirmed verbatim: median two-qubit gate error "46.4×10⁻⁴", and "widths up to ≈20 qubits and depths up to ≈200 two-qubit gates" before the 1/e threshold. S3 (IBM pricing, background color only) and S4 (Rigetti device, background color only) not re-fetched this session — RESEARCH_LOG.md records both fetched and confirmed at research time same day; neither is load-bearing on the margin arithmetic. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Margin 16.98%, inside the ~20% cap, and both live-fetch spot checks confirm
the two load-bearing sources are accurate and current.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-qubit-budget/runs/RUN_*.md` filed. Required before VERIFIED/✅ in
`DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.
