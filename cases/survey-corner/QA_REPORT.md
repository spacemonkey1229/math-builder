## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 2 BLOCKERs (Appendix A orphan — never referenced by letter from Background; source S1
missing required `org`/`title` fields) plus 3 GAPs (standards[] claimed 3 already-covered
reinforcement skills — percent, absolute value, interior-angle-of-a-polygon — absent from the final
appendix's spine-label list; FACILITATOR.md contained 3 numbers (88.3, 90.0, 91.7) absent from
case.json's number universe; no `case_md_sha256` yet — expected on a first run). All resolved:
Appendix A referenced from Background; S1 given `org`/`title`; Appendix G expanded to a full
two-part list including all 9 claimed standards (not just the 6 new ones); the 3 missing numbers
added to `case.json.derived`. **Final run: 0 BLOCKERs, 0 GAPs**, and held clean through two later
rounds of content edits (the balance-test fix, the source-coordinate correction).

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P5 sensitivity | **mechanical FAIL, then fixed** | The mechanical probe's generic ±50% sweep on the raw `nw_angle` PARAM (93° → 46.5°-139.5°) is not a physically plausible test of real plat-recording uncertainty, and correctly caught that a naive ±50% sweep at that scale flips the winner. **Fixed**: reparametrized the model to `right_angle_deg` (90°, fixed) + `nw_excess_deg` (3°, the FLEX target) — a real deed-angle recording error plausibly scales with the *excess past square*, not the whole angle. Re-verified: ±50% on the 3° excess (effective NW angle 91.5°-94.5°) holds the winner (Pin 2) across the whole range, margin 8.33%-16.67%. `case.json`/`FACILITATOR.md` updated to match. |
| P1 cold solve | PASS | Fresh agent reached the case's own intended answer (Pin 2, 11.11% margin) with fully correct D1-D7 arithmetic, correctly named the primary metric (minimum angular deviation, quoting the case's own stated decision rule), and correctly identified MA1 as the most load-bearing assumption. Its own free-text answer referenced a stale "±1°" sensitivity figure that had been superseded by the P5 fix above — not an error in its reasoning, just evidence the cold-solve packet was built before that fix; no case defect. |
| P2 both-sides | **FAIL, then fixed** | First pass found a real, serious defect: Option A (Pin 1) had **zero genuine quantitative argument** — every number in the original case (angle deviation, triangle shape) favored Pin 2, leaving Pin 1's only "case" a non-quantified appeal to the pin's age, which the case's own text explicitly labels as the flawed reasoning path. The agent stated plainly: "the balance test has not actually been passed... a paper number." **Fixed**: added a genuine, conflicting distance check to Appendix C (the plat's recorded boundary length vs. each pin's measured distance from the NW corner) that favors Pin 1 by a real, quantified margin — the two independent checks (angle vs. distance) now genuinely disagree, and Priya's choice to weight angle over distance is a stated, arguable professional judgment rather than a hidden thumb on the scale. Re-verified with a fresh agent: confirmed both options are now defensible with real case numbers in front of peers, calling the fix "a real, substantive improvement... not the same paper-margin problem in a new coat of paint." That re-verification also noted an honest residual: the case asserts, but doesn't numerically quantify, why the angle check should outweigh the distance check — accepted as a legitimate feature of real professional judgment (see waived-note below), not a defect requiring a fabricated precision figure. |
| P3 trap | **PASS, then a real guide gap found and fixed** | First pass (before the P2 fix): fresh agent independently predicted the same appearance-over-math trap the guide names, near-verbatim — PASS. After the P2 distance-check fix, a second fresh agent re-checked the revised case and found a real, unanticipated gap: **after the Twist, the angle and distance checks converge** (both come to favor Pin 1), but the guide's Deep Conflict thread 4 was written in the present tense as if they still disagree, and is scheduled to run *after* the twist in the 45-minute plan — a facilitator running the script as written would be caught flat-footed. The same agent surfaced a sharper, genuinely interesting point the guide hadn't drawn out: the twist's actual content (a transcription error in the angle reading) undercuts Priya's own stated reason for trusting angle over distance in the first place. **Fixed**: added an explicit facilitator-only note in the Twist section flagging the post-twist convergence and the self-undercutting argument, reworded thread 4 to be time-aware, and corrected the 45-minute plan's summary row (it had silently dropped thread 4). |
| P4 twist | PASS | Fresh agent independently re-derived D1-D7 and the twist's effect from case.md's raw numbers alone (not trusting FACILITATOR.md), confirmed all four twist figures (88.3°, 91.7°, 4.7°, 4.26%) exactly, confirmed the verdict genuinely flips (Pin 2 → Pin 1), and confirmed no BLOCKER-level convention ambiguity — the supplementary-angle rule applies identically and unambiguously to both pins, and the twist's own model function documents touching only `pin2_raw`. Bonus finding: the post-twist verdict is itself robust to the MA1 flex (3.5%-5.4% range, no re-flip). |
| P6 data decay | PASS, with a correction | S1 fetched live 2026-08-12. Station designation, PID, and elevation (5,318.45 ft NAVD 88) confirmed exact. Coordinates had drifted slightly from an earlier 2018 archival copy (45°01'46.29"N/110°42'30.03"W → live 45°01'46.22"N/110°42'30.10"W) — a routine NGS position readjustment, not a data-quality problem. **Corrected the case to the live, current value** rather than ship a technically-stale figure (SEE RESEARCH_LOG.md). |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. This case is **not `VERIFIED`, only
`PUBLISHED`-eligible** — should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files a
`RUN_REPORT.md` from an actual cohort.

### Waived note (not a defect)

P2's re-verification agent noted that the case asserts, rather than numerically quantifies, *why*
the angle check should outweigh the distance check when the two disagree (Priya's stated reason —
a clean angle shot is less exposed to field error than a distance shot over rough terrain — is a
real, plausible professional judgment call, not a fabricated number). The agent itself characterized
this as "a legitimate, arguably realistic feature of real-world professional judgment... rather than
a flaw to be embarrassed about." Not fixed as a numeric precision figure, since inventing an
"error-budget" number with no real basis would itself violate SPEC §5 (no fabricated numbers) —
instead, this exact tension is now the explicit subject of Socratic Question 6 and Deep Conflict
thread 4, turning the open question into the discussion rather than pretending it's resolved.
