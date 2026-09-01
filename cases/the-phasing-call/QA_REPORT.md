## case-readiness run — 2026-08-31

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Before Tier 1: `preflight_lint.py --case the-phasing-call` → clean, no advisory findings.

### Tier 1 — structural (20 checks)

Remediation this session: rewrote `FACILITATOR.md` from scratch on the `cooling-curve` structural
template (full anchor ladder: Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Immediate
recommit/Deep conflict/45-minute plan/The trap/Socratic questions/Close/Lessons Learned/Standards
Touched On), with 5 Socratic questions probing the analysis process (ratio setup, phase-angle-to-days
conversion, why the two terms compound instead of partially cancel, what would have to change to flip
it, whether an additive construction tells a different story) instead of "argue for A vs argue for
B." Trimmed `case.md`'s Overview from 309 to 287 words. Added `case.json.cohort_bands[]` (3 bands).
Removed the orphan `7.4` (was a stray "SPEC §7.4" heading reference). Verified `reinforcement_note`
was already present and valid. Authored `sensitivity_model.py`, reproducing the documented 1991.18%
margin exactly. Recorded `case_md_sha256` after the case.md edit settled.

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 287 words (was 309, GAP; fixed) |
| T1-03 | PASS | binary dilemma, opens "You are Talia Brooks." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-G, no orphans |
| T1-07 | PASS | Appendix G labels parsed (9 bulleted) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | GAP | margin 1991.18% — MCS-46 waiver on file, four required keys present, downgraded per doctrine |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, `reinforcement_note` present and checked |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier/numeric load consistent |
| T1-13 | PASS | facilitator guide, anchor ladder, 5 Socratic questions, Twist, timed plan (was BLOCKER x2, GAP x1; fixed by the FACILITATOR.md rewrite) |
| T1-14 | PASS | continuity — no orphan numbers (was GAP for stray `7.4`; fixed) |
| T1-15 | PASS | no published/ artifacts yet, nothing to drift |
| T1-16 | PASS | case_md_sha256 recorded and current |
| T1-17 | PASS | cohort_bands[] declared (was GAP; fixed) |
| T1-18 | PASS | no published/ dir, nothing to check |
| T1-19 | PASS | no published/ dir, nothing to check |
| T1-20 | PASS | advisory, never blocks |

**BLOCKER (0).**

**GAP (2, both accepted/expected):**
* T1-09 — margin 1991.18% waived under MCS-46 (`case.json.balance_test_waiver`, `DOCTRINE_LEDGER.md`).
* T1-10 — empty `new_coverage[]`, reinforcement carve-out per `case.json.reinforcement_note` (this case
  replaces `the-transfer-window` and reuses its full skill group by design).

**POLISH (5):** T1-07 (separator-run parsing note), T1-15/T1-18/T1-19/T1-20 (no `published/` directory
yet — expected pre-publish).

`VERDICT: TIER1_PASS (0 blockers, 2 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen: 0 probes failed mechanically after two real fixes made this session —
`case.json.balance.argument_b` was rewritten with real digits (was all spelled-out numbers, tripping
P2's "almost no numbers" screen), and `case.json.sensitivity_disclosure[]` was added for the two
genuine stated Modeling Assumptions the sensitivity model flexes (MA2 docking deadline, MA3 minimum
reserve fraction), both Category X (proprietary/inaccessible, anchored to a real analogue), resolving
P5's mechanical FAIL to `PASS (disclosed)`.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh, genuinely blind subagent (packet-only, no FACILITATOR/case.json access) independently reached Option A with correct D1-D7 arithmetic (own polar conversion, parametric setup, parameter elimination, percent-of-reserve, phase-angle-to-days conversion, final ~20.9x ratio), named the D7 ratio as the optimized metric, and — **unprompted**, before being told the framing — explained the compounding mechanism in its own words: "these two moderate effects multiply rather than add... stacking a numerator advantage on top of a denominator advantage compounds them... an artifact of the metric's shape (a compounding ratio), not evidence that one option is overwhelmingly better in every dimension." This directly answers whether a fresh solver can articulate the insight: yes, spontaneously. |
| P2 both-sides | **PASS** | Independent subagent built real, quantitative arguments for both options from the packet alone (A: 94.8h/100.8h reserve, 94.0%; B: 270°/360° tolerance, 22.5 of 30 workable days, a real 9x launch-window advantage). Verdict: genuine two-sided case, not fake balance — B does not collapse until the case's own D7 ratio construction is applied; both sides have real numbers up to that point. |
| P3 trap | **PASS** | Independent subagent, reading the packet only, named the trap as students correctly computing D4/D6 but never actually performing D7's division, mistaking two separately-favorable facts for a wash. Confirmed against `FACILITATOR.md`'s "The trap" section afterward: substantially the same trap (ratio-vs-sum weighting-equivalence mistake), assessed by the reviewer as the guide's framing being the sharper, more classroom-relevant version of the same underlying error. |
| P4 twist | **PASS (after remediation)** | Independent adversarial subagent verified the Twist's core insight (ratio vs. sum compounding) is sound, and independently reproduced the additive-score arithmetic (0.512 vs 0.577) as correct. **Real finding, fixed this session:** the additive-score flip is a knife-edge result (~12.7% apart) fragile to the exact 50/50 weighting (ties at w≈0.554; flips back to A at w=0.60), unlike D7's own result (robust across the full ~11x-21x researched range) — and `FACILITATOR.md` originally stated the flip as flatly "mechanically verified" without disclosing this fragility. Fixed: added an explicit facilitator-only disclosure paragraph in the Twist section and `case.json.derived.twist_additive_score_fragility_note`, instructing facilitators not to present the flip as equally robust to D7's real result. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` reproduces the base case exactly (A=37.92 h/day, B=1.81 h/day, margin 1991.18%, matching `case.json.balance.margin_pct`). Flexing the two genuine stated assumptions (MA2 docking deadline, MA3 minimum reserve fraction) ±50% never flips the winner; the only real effect is MA2 at -50% (48h) disqualifying the Phasing Climb outright on the deadline floor, already disclosed in Appendix E's own MA2 sensitivity note. Both flexed dials trivially "break the 20% cap" only because the baseline margin itself already does (the MCS-46-waived finding recurring, not a new instability) — disclosed via `case.json.sensitivity_disclosure[]` (Category X, both dials) per the 2026-08-13 disclosure-aware pass state. Consistent with the case's own diagnosis that none of MA1-MA4 is where the real margin comes from. |
| P6 data decay | **PASS (1 non-blocking finding, disclosed)** | Live fetch/search this session (not delegated — this session has outbound network) against all 11 distinct source URLs. 10/11 confirmed reachable with the cited figure still present and verbatim-matching (S1, S2, S3, S5, S6, S7, S8/S10 — S8/S10's primary Soyuz Crew Operations Manual PDF fetched and `pdftotext`-extracted directly, confirming 4.2 days/88.62 min/240 km/202 km/the "240-30 degrees" note verbatim — S9, S11). **Real finding:** S4's cited SpaceRef URL now resolves but serves an unrelated, apparently regenerated generic article — the "resolves but no longer carries the figure" case this skill calls worse than a 404. Not a BLOCKER: the 34-orbit/2-day figure S4/attests is corroborating context in Appendix B, not itself a load-bearing input to D4-D7 (the actual Phasing Climb transit time used, 60h, comes from S5), and the claim is independently corroborated by S4's co-cited AmericaSpace reporting and by the already-recorded internal cross-check (88.62 min × 34 orbits ≈ 50.2h ≈ 2.09 days). Recorded in `RESEARCH_LOG.md` per MCS-21 rather than silently left stale. |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-phasing-call/runs/RUN_*.md` filed. Required before this case may be marked
✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).
Schedule a Tier 3 human dry-run before any `VERIFIED` claim in the doctrine ledger.
