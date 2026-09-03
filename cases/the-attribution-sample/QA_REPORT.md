## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: removed `statistics-and-probability-multistage-sampling` from
`standards[]` and Appendix H after T1-11 correctly flagged it — case.md itself states explicitly
that neither option is a multistage design (line 35), so no deliverable ever forced that skill;
this was a labeling error, now corrected. Added `(SEE APPENDIX H)` reference to Background (T1-06
GAP). Added `reinforcement_note` after checking the full Statistics And Probability domain for
`n==0` skills — none exist. Recorded `qa.case_md_sha256` (T1-16).

`VERDICT: TIER1_PASS (0 blockers, 3 gaps: T1-09 margin 19.83% wide-but-in-cap, T1-10 reinforcement
carve-out, T1-14 8 guide-only derived numbers not moved to case.json.derived)`.

### Tier 2 — simulated play (6 probes)

Added `case.json.sensitivity_disclosure[]` (7 entries: `share_affiliate`, `n_total_a`,
`setup_hours_a`, `floor_affiliate_b`, `setup_hours_b`, `time_affiliate`, `p_affiliate`) — a manual
recomputation of `sensitivity_model.py`'s sweep (the generic Tier-2 harness's margin formula
divides by the *winning* side's value, which is negative in this model's cost-convention `evaluate()`,
so its own "breaks_20pct_cap" flag never fires; recomputed properly using `abs()` of the losing
side) found the true base margin is 19.68-19.83% (both readings agree, inside cap but the closest
case in this batch to it) and that all 7 declared dials swing the true margin past 20% at ±50% —
every one of the 7 is a stated scenario Modeling Assumption (MA4-MA8, MA12) already flagged HIGH
sensitivity in case.md's own table, not new information.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | The packet alone gets a solver to: D1's pooled-sample per-channel SEs (Affiliate 12.62pp, worst), D2's stratified SEs (Affiliate 5.65pp, much tighter), D3's hours totals (10.1 hr A vs 12.95 hr B, both under the 13-hr budget), D4's primary metric (pooled SE per analyst-hour). The metric is explicitly named by D4's wording; arithmetic is traceable from Appendix B/C/E's stated figures. |
| P2 both-sides | **PASS** | A's best sentence: "Pooled is faster to set up and both options verify the same 400 clicks, so on raw analyst-hours efficiency it's the cheaper option." B's best sentence: "The pooled sample draws almost nothing from the Influencer/Affiliate channel Driftline's own marketing lead has flagged for board-deck scrutiny (SE 12.62pp, barely better than a coin flip) — Stratified's guaranteed floor fixes exactly that channel (SE 5.65pp) at a real but bounded hours cost that still fits the weekend budget." Neither side concedes outright; B's argument survives even if a reader is unmoved by D4's aggregate number, because it targets the specific channel Background names as high-stakes. |
| P3 trap | **PASS** | The stated trap (reading D4's *pooled* SEs as "basically equivalent" and missing the *channel-level* story for exactly the flagged Affiliate channel) is the single most plausible failure mode, since D4 is deliberately close (1.369pp vs 1.407pp) while the channel-level gap is stark (12.62 vs 5.65). FACILITATOR.md names this trap explicitly. |
| P4 twist | **PASS** | (case.md/FACILITATOR.md's twist mechanism reviewed; not reproduced here per SPEC's facilitator-only content rule.) It introduces real information that changes the room's confidence without pre-declaring a winner, and holds under every stated reading of the Modeling Assumptions — none of MA1-MA12 contradicts it. |
| P5 sensitivity | **PASS (disclosed)** | Base margin 19.68-19.83% depending on rounding, inside the ~20% cap. All 7 swept dials (MA4-MA8, MA12) push the true margin over the cap at some ±50% extreme — every one is a stated, already-HIGH-flagged scenario assumption in case.md's own table, now also recorded machine-checkably in `case.json.sensitivity_disclosure[]` (mix of category F/X per param, each justification quoting the case's own basis). No undisclosed instability. |
| P6 data decay | **PASS (live fetch)** | S1 (AppsFlyer global fraud rate) — live, confirmed verbatim: "13.2% in H1 2020." S2 (RocketshipHQ channel breakdown) — live, confirmed: SAN 1-8%, Tier-1 DSP 12-20%, Influencer/CPI 15-30% (all match case's stated ranges exactly). S3-S5 (all same AppsFlyer domain as S1) not independently re-fetched this session; RESEARCH_LOG.md records same-day confirmation. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Margin 19.68-19.83%, inside the ~20% cap (closest case in this batch to the
line, but not over it), both live-fetch spot checks confirm accurate current data, and every
genuinely unstable sensitivity dial is now machine-disclosed.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-attribution-sample/runs/RUN_*.md` filed.
