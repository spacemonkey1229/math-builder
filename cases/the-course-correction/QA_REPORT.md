## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: cleared the T1-02 BLOCKER — "0400" in the Overview is a 24-hour nautical
clock time (4:00 a.m.), texture establishing watch duration, not a value used in any calculation;
recorded the clearance in `case.json.overview_numerals_cleared[]`. Recorded `qa.case_md_sha256`.

`VERDICT: TIER1_PASS (0 blockers, 3 gaps: T1-09 margin 16.88% wide-but-in-cap, T1-10 reinforcement
carve-out, T1-14 10 guide-only derived numbers — mostly Excel-serial-style dates, not moved to
case.json.derived)`.

### Tier 2 — simulated play (6 probes)

Added `case.json.sensitivity_disclosure[]` (3 entries: `distance_nm`, `course_deg`, `window_hr`) —
`tier2_probes.py`'s own sweep correctly found `distance_nm` and `window_hr` flip the verdict at
±50%; all three are explicitly named in case.md's own Modeling Assumptions table (MA1/MA2), which
documents the near-identical flip behavior in prose already ("the 3.0 hr base case sits close to
the flip boundary on the loosening side — a genuinely sensitive constraint, disclosed rather than
hidden").

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A solver computes Option A's required speed-over-ground (27.0 nm ÷ 3.0 hr = 9.000 kt), resolves the real NOAA current vector (S1) into along-track/cross-track components relative to the stated bearing, looks up Appendix C's fuel-cost curve at the resulting required boat speed, and compares against Option B's stated fixed speed on the same curve — the primary metric ($/nm of net progress) is named explicitly. |
| P2 both-sides | **PASS** | A's best sentence: "The True Line accounts for the real, live-measured current (S1) and gets the vessel to the buoy inside the weather window at the true minimum required speed — burning exactly what's needed, no more." B's best sentence: "The Steady Burn holds the cheapest point on the real fuel curve (Appendix C) and accepts a schedule risk instead of a certain fuel-cost premium — a defensible tradeoff when the closing window (MA2) is itself only a stated estimate, not a hard deadline." Neither concedes; the tension is a real cost-vs-schedule-risk tradeoff, not a one-sided arithmetic fact. |
| P3 trap | **PASS** | The stated trap (picking whichever speed sits at the fuel table's cheapest point without completing D3's vector decomposition or D5's actual $/nm computation) is the most plausible failure mode, since the case's primary metric is deliberately a ratio (cost per net mile of progress), not a flat hourly burn rate. FACILITATOR.md names this trap explicitly. |
| P4 twist | **PASS** | (twist reviewed in FACILITATOR.md.) Holds under every stated reading of MA1-MA4; does not depend on an unstated convention — the case's own S4 citation resolves the one genuine ambiguity (NOAA's current-direction convention, "toward" vs. "from") explicitly. |
| P5 sensitivity | **PASS (disclosed)** | Base margin 16.88%, inside cap but the second-widest in this batch. `distance_nm` and `window_hr` (MA1/MA2) flip the verdict at some ±50% extreme, and `course_deg` pushes past the cap without flipping — all three are explicitly HIGH/MODERATE-flagged in case.md's own table with the *exact same flip description* already in prose, now also machine-recorded in `sensitivity_disclosure[]`. No undisclosed instability. |
| P6 data decay | **PASS (live fetch)** | S3 (EIA weekly diesel retail price) — live, confirmed verbatim: "week ending August 31, 2026, at $5.599 per gallon," exactly matching the case's cited figure and cutoff date. S1 (NDBC live buoy feed) is by nature a live real-time feed that has moved on since the case's stated observation timestamp — this is expected and disclosed in the case's own "as-of" framing (SPEC §5's fixed-cutoff rule), not a decay failure. S2 (ADFG, background color) and S4 (NDBC direction-convention FAQ) not independently re-fetched this session; RESEARCH_LOG.md records same-day confirmation. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Base margin 16.88%, inside the ~20% cap, live-fetch spot check confirms the
load-bearing fuel-price citation, and the case's genuine sensitivity to its own stated distance/
window assumptions is disclosed in both case.md prose and now machine-recorded.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-course-correction/runs/RUN_*.md` filed.
