## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: downgraded source S3's confidence from the invalid label
`"MEDIUM-HIGH"` to `"MEDIUM"` (this project's convention allows only HIGH/MEDIUM/LOW) — the
primary paper 403'd on direct fetch and the figure was confirmed via a secondary page instead
(not load-bearing on the D1-D4 math, Background stakes-framing only), so MEDIUM is the honest
tier (fixed T1-08 BLOCKER). Reformatted the 5 Socratic questions onto single lines so the
mechanical parser can see the trailing `?` (was T1-13 GAP — content was already there, wrapped
across lines). Added `(SEE APPENDIX G)` reference (T1-06 GAP). Added `reinforcement_note` after
checking the full Pre-Calculus domain — no `n==0` skills exist. Recorded `qa.case_md_sha256`.

`VERDICT: TIER1_PASS (0 blockers, 2 gaps: T1-10 reinforcement carve-out, T1-14 1 guide-only
derived number)`.

### Tier 2 — simulated play (6 probes)

Added `case.json.sensitivity_disclosure[]` (3 entries: `ctr_a`, `dropout_b`, `ctr_b_completer`) —
`tier2_probes.py`'s own mechanical sweep correctly found these 3 params both FLIP the verdict and
push the margin past the 20% cap at ±50%. All three are stated scenario assumptions already
flagged HIGH in case.md's own table (MA2 explicitly: "the most narratively-invented number in the
case"; MA3 explicitly: "the single most dilemma-relevant modeling choice in the case," with the
literal MovieLens-2002 counterfactual already computed in Appendix D's own bottom row).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A solver builds Appendix B/C's item-similarity/completer matrices, computes D1's sparsity, D2's identity-matrix framing for Option A, D3's completers-only vs. Appendix D's per-100-starters scoring, and D4's clicks-per-100 comparison. The metric (recommendation clicks per 100 users exposed, at the platform's actual funnel stage) is named by D4's wording and Appendix D's own "per 100 starters, not per 100 completers" framing, which is deliberately the case's real content (see P3). |
| P2 both-sides | **PASS** | A's best sentence: "The Popularity Path reaches every user immediately, with zero cold-start dropout, at a real published median dropout figure this platform can't yet beat with day-one personalization." B's best sentence: "The Ratings Gate's completer-only CTR (35%) is real evidence personalization works once it has data — the real question is whether it's worth the dropout, and Appendix D's own per-100-starters framing (not per-100-completers) is what makes that honest." Neither collapses; B's argument survives scrutiny because the case forces the *funnel-wide* metric, not the completer-only one a naive read would reach for. |
| P3 trap | **PASS** | The stated trap (scoring Option B on its 35% completer-only CTR instead of the analytics team's mandated per-100-starters metric) is the most plausible failure mode, since the completer number looks better in isolation and a rushed student may not notice the denominator switch. FACILITATOR.md names this trap explicitly. |
| P4 twist | **PASS** | (twist reviewed in FACILITATOR.md, not reproduced here.) It introduces a real, disclosed data point that changes the room's read on the dropout assumption without pre-declaring a winner, consistent with Appendix D's own documented literal-MovieLens-figure counterfactual. Holds under every stated reading of MA1-MA5. |
| P5 sensitivity | **PASS (disclosed)** | Base margin 4.76% (well inside cap — the tightest-margin case in this batch after The Rig Split). `ctr_a`, `dropout_b`, `ctr_b_completer` genuinely flip the verdict and cross the cap at ±50% — each is a stated scenario assumption already HIGH-flagged in case.md's table (the literal MovieLens counterfactual is even pre-computed in Appendix D), now also recorded in `sensitivity_disclosure[]`. No undisclosed instability. |
| P6 data decay | **PASS (live fetch)** | S1 (MovieLens 25M) — live, confirmed verbatim: "25 million ratings," "162,000 users," "62,000 movies." S2 (Rashid et al. 2002 IUI paper, PDF), S3 (New America/Netflix secondary), S4 (Baymard) not independently re-fetched this session — RESEARCH_LOG.md records S2/S4 fetched and confirmed at research time same day; S3 is already downgraded to MEDIUM (see Tier 1) and is Background color only, not load-bearing on the D1-D4 metric. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Base margin 4.76%, comfortably inside the ~20% cap and among the tightest
races in this batch, live-fetch spot check confirms the load-bearing dataset citation, and all
genuinely unstable sensitivity dials are machine-disclosed.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-cold-start/runs/RUN_*.md` filed.
