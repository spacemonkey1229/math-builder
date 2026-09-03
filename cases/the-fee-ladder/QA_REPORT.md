## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: added `(SEE APPENDIX H)` reference to Background (T1-06 GAP). Added
`reinforcement_note` after checking the full Discrete Mathematics domain for `n==0` skills — none
exist. Recorded `qa.case_md_sha256` (T1-16).

`VERDICT: TIER1_PASS (0 blockers, 2 gaps: T1-10 reinforcement carve-out, T1-14 5 guide-only
derived numbers)`.

### Tier 2 — simulated play (6 probes)

Added `case.json.sensitivity_disclosure[]` (3 entries: `quick_quote_rate_bp`, `tier1_bp`,
`tier2_bp`) after running `sensitivity_model.py` directly (its own `__main__` self-test block
already computes the true `margin_pct`, since the generic Tier-2 harness's `evaluate()` contract
returns a raw dollar gap for A and a fixed 0.0 for B by design, which produces a degenerate -100%
reading through the harness's own margin formula) — the true base margin is 13.32%, well inside
the cap, but `quick_quote_rate_bp` (MA5, "the case's real fulcrum") pushes the true margin to
56.66%/30.02% at ±50%, and `tier1_bp`/`tier2_bp` (MA6) push it to ~29%/~24% at +50%. All three are
scenario-chosen rates already flagged HIGH-sensitivity in case.md's own Modeling Assumptions table.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A solver walks Appendix C's recursion tier-by-tier (2.00/1.25/0.75/0.50 bp on the successively-shrinking balance) to get the Full Ladder's true fee ($382,441.03 on $850M AUC), compares to the Quick-Quote flat 3.90bp fee ($331,500), and computes the 13.32% gap as a percentage of the true fee — D4's own wording names this exact metric. The recursion (not a naive marginal-bracket sum) is the case's real math content, and it's unambiguous once Appendix C's table is read literally. |
| P2 both-sides | **PASS** | A's best sentence: "The Quick-Quote card is Meridian's own real published reference rate for this exact AUC band, and it can be quoted to the client today, days before Full Ladder-quality pricing would be ready." B's best sentence: "The Full Ladder is provably exact by construction (D1's recursion), and the 13.32% gap is a real, scale-invariant dollar error the Quick-Quote card doesn't know it's making — for a multi-year relationship, that's a real number to walk back later." Neither concedes; B's argument survives even after granting A's speed advantage, since it targets accuracy, not speed. |
| P3 trap | **PASS** | The stated trap ("recursive is exact, so always pick B" without ever running D4 to check whether 13.32% is an acceptable, bounded cost of speed) is the most plausible failure mode, since D1-D3 are pure recursion/algebra and D4 is where the actual decision-relevant number appears. FACILITATOR.md names this trap explicitly. |
| P4 twist | **PASS** | The twist (case.md/FACILITATOR.md's real cited State Street overcharge enforcement action, S3) introduces a real consequence for undisclosed fee errors without pre-declaring a winner — it sharpens the stakes of B's 13.32%-error argument without making A wrong outright (Quick-Quote's error is disclosed and bounded, not hidden and compounding like the S3 case). Holds under every reading of MA1-MA6. |
| P5 sensitivity | **PASS (disclosed)** | True base margin 13.32%, well inside the ~20% cap and scale-invariant across AUC (verified: identical margin at $300M/$850M/$1.2B AUC, confirming D4's own scale-invariance finding). `quick_quote_rate_bp`, `tier1_bp`, `tier2_bp` push the margin over cap at some ±50% extreme — all three are stated scenario rates already HIGH-flagged in case.md's table, now recorded machine-checkably in `sensitivity_disclosure[]`. No undisclosed instability. |
| P6 data decay | **PASS (live fetch)** | All three sources are real SEC EDGAR filings/press releases; WebFetch's default fetch got HTTP 403 from sec.gov (bot-detection on default UA), so re-fetched via `curl` with a compliant identifying User-Agent per SEC's fair-access policy — all three confirmed live and verbatim: S1 "First $500 Million .50 Basis Points, Remainder .3875 Basis Points" (State Street/Gabelli filing); S2 "First $150mm ... 7.0 bps Assets in excess of $150mm ... 4.0 bps ... $3,826.67" (State Street/Green Century filing); S3 "$170 million from the overcharges, with $110 million coming from the hidden SWIFT markup" and "$48.78 million ... civil penalty of $40 million" (SEC 2019-114 press release). |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** True margin 13.32%, comfortably inside the ~20% cap, scale-invariant by
design, all three real SEC sources confirmed live and exact.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-fee-ladder/runs/RUN_*.md` filed.
