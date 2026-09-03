## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: reformatted the 5 Socratic questions onto single lines so the mechanical
parser can see the trailing `?` (was T1-13 GAP). Added `(SEE APPENDIX H)` reference. Added
`reinforcement_note` after checking the full Pre-Calculus domain — no `n==0` skills exist.
Recorded `qa.case_md_sha256`.

`VERDICT: TIER1_PASS (0 blockers, 2 gaps: T1-10 reinforcement carve-out, T1-14 3 guide-only
derived numbers)`.

### Tier 2 — simulated play (6 probes)

Added `case.json.sensitivity_disclosure[]` (2 entries: `fpr_a`, `fpr_b`) — `tier2_probes.py`'s own
sweep correctly found these flip the verdict at ±50%. This is the case's own designed mechanism:
MA7 (Wave Nine's surge-scaled false-positive rate) is explicitly named "the single most
dilemma-relevant modeling choice in the case" in case.md, which states outright that at the real
unscaled baseline (15%, no surge premium) the recommendation flips to Option B — this is also the
case's Twist.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A solver reads Appendix A's cluster sizes and connection-matrix density, Appendix D's real published detection-accuracy ranges (S1), and Appendix E's modeled false-positive rates, then computes each cluster's confirmed-bots-per-false-positive ratio (Ring Alpha 4.0, Wave Nine 3.44) — the metric is named explicitly by the case's own framing. |
| P2 both-sides | **PASS** | A's best sentence: "Ring Alpha's connection matrix is real, dense, and the modeled false-positive rate is grounded in a real published academic baseline (S1) — its ratio (4.0) is higher, meaning fewer innocent accounts get caught per confirmed bot suspended." B's best sentence: "Wave Nine is the platform's highest-traffic weekend, and volume-based detection is a real, documented weak point during traffic surges — under the real unscaled baseline rate with no surge premium, Wave Nine actually wins by ~29%, which is exactly the twist a room needs to reckon with." Neither collapses; the case's Twist exists specifically because B's argument strengthens once the surge-premium assumption is questioned. |
| P3 trap | **PASS** | The stated trap ("denser matrix = more suspicious = suspend it," skipping Appendix D's real accuracy comparison and treating Appendix E's modeled rates as measured) is the most plausible failure mode for a rushed read. FACILITATOR.md names this trap explicitly. |
| P4 twist | **PASS** | The twist (recompute under the real unscaled 15% baseline, no surge premium) is real, disclosed, and explicitly documented in case.md's own MA7 sensitivity note — it flips the recommendation to Option B under ordinary conditions without making Option A's real modeled reasoning wrong, since the surge condition is itself real and stated (Verve's "highest-traffic weekend"). Holds under every stated reading of MA6/MA7. |
| P5 sensitivity | **PASS (disclosed)** | Base margin 13.89% (winner: Ring Alpha/A), inside cap. `fpr_a` and `fpr_b` flip the verdict at some ±50% extreme — both are explicitly HIGH-flagged in case.md's own table (MA7 pre-computes the exact flip: "0.85/0.15 ≈ 5.67, beating Ring Alpha's 4.00 by ~29%"), now also recorded in `sensitivity_disclosure[]`. This is the case's designed Twist mechanism, not a hidden defect. |
| P6 data decay | **PASS (live fetch)** | S1 (Varol et al., arXiv:1703.03107, bot-detection accuracy ranges) not independently re-fetched (PDF; RESEARCH_LOG.md records same-day confirmation of the AUC/FP/FN figures). S2 (X API rate limits) not re-fetched this session. S3 (Stanford SNAP ego-Facebook dataset) — live, confirmed verbatim: "4,039" nodes, "88,234" edges, "0.6055" average clustering coefficient, exactly matching the case's cited figures. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Base margin 13.89%, inside the ~20% cap; the case's genuine flip-sensitivity
on the false-positive-rate assumptions is the deliberate Twist mechanism, fully disclosed in
case.md and now machine-recorded.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-bot-farm/runs/RUN_*.md` filed.
