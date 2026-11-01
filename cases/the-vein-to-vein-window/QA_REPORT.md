# QA Report — The Vein-to-Vein Window

## case-readiness run — 2026-09-09

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

First pass found one advisory finding: Challenge 3's D5 was originally titled "Writing the trap
into the pitch," leaking the word "trap" into student-facing text (SPEC intends the trap to
surface only through the facilitator during play). Fixed: retitled to "Writing the cutoff argument
into the pitch," text otherwise unchanged. Re-run: clean, 0 advisory findings.

### Tier 1 — structural (21 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 150-300 words, no load-bearing numerals (6, 52 auto-classified as clock-time texture) |
| T1-03 | PASS | Dilemma binary, opens "You are Dana Whitfield." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-G lettered, ordered, no orphans |
| T1-07 | PASS | final appendix lines are verbatim spine labels (6 parsed) |
| T1-08 | PASS | every number cited [S1-S3] or a disclosed Modeling Assumption [MA1-MA5] |
| T1-09 | PASS | both arguments written, margin 9.89% <= 20% cap |
| T1-10 | **GAP** (not blocker) | `new_coverage[]` empty by design -- all 6 claimed skills already n=2 in the spine (thin, not zero); `reinforcement_note` records the live spine check and the full-group-thickening rationale. Downgraded from BLOCKER per the 2026-08-17 reinforcement carve-out (case.json carries a `reinforcement_note`, not a fabricated new-coverage claim). |
| T1-11 | PASS | learning-goal mutual reachability -- 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T4 tier justified: Modeling Assumptions block present (MA1-MA5), 5 deliverables, probability content |
| T1-13 | PASS | FACILITATOR.md: 5 single-line Socratic questions, names "the trap," full anchor ladder (Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On) in order, Anchors 2-3 precede Data Deep Dive, Twist authored (not N/A), 45-minute timed plan with 7 rows naming the twist moment, case.json.sensitivity_note present for the illness/hardship content |
| T1-14 | **GAP** | 2 numbers in FACILITATOR.md (from "SPEC §7" heading references and one hypothetical Anchor-4 discussion prompt) have no home in case.md/case.json -- reviewed, both are conversational/hypothetical, not stale derived figures; no fix needed beyond this note |
| T1-15 | PASS | no published/ directory yet -- nothing to drift (by design; case-publish not run) |
| T1-16 | **GAP** | case_md_sha256 now recorded (33cf976fe7a7d194463dd80e470a157e62a81b999ad8999a4b95524d3c0ff556) as of this report; was open before this run completed |
| T1-17 | PASS | cohort_bands[] declared (Full/Compressed/1:1) |
| T1-18 | PASS | no published/ directory yet |
| T1-19 | PASS | no published/ directory yet |
| T1-20 | PASS | no published/ directory yet |
| T1-21 | PASS | no published/ directory yet |

**BLOCKER (0).** **GAP (3):** T1-10 (disclosed reinforcement, not a defect), T1-14 (harmless
orphan numbers, reviewed), T1-16 (resolved by this report's own sha256 write). **VERDICT:
TIER1_PASS.**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent (packet-only, no FACILITATOR.md/case.json/QA_REPORT.md access) chose Option A, named the correct metric (probability of viability), showed correct D1-D4 arithmetic (100% vs. 91%, margin 9 points), named the strongest counterargument, correctly identified MA2 as the most sensitive assumption, correctly treated Appendix A as background-only, and named MA4 as the least-supported number. Reached the intended answer for the intended reasons -- not a lucky guess. First run caught a real leak (`balance_test.margin_pct=10.0` collided with Appendix C's literal "10%" major-delay-probability text); fixed by retuning MA4 to 71/20/9% (margin recomputed to 9.89% under the house winner-loser-as-%-of-loser convention), re-verified leak-free, re-solved clean. |
| P2 both-sides solve | **PASS** | First run found Option B's argument had no dollar figure at all -- it collapsed to a values-only claim ("meaningfully lower cost") the moment a peer asked for a number, which is a real P2 fail mode per skills/case-readiness/SKILL.md ("an argument with almost no numbers... fails before a model sees it"). Fixed: added a disclosed Modeling Assumption (MA5, $500/dose incremental standby-staffing cost) grounded in real, general hospital shift-differential/on-call pay practices (searched; no institution-specific per-dose figure is public, so disclosed as an assumption, not a citation). Re-run: both sides now argue with real numbers (100% viability + $500 cost for A; $0 cost + 91% viability for B); the case now collapses only at the genuine, intended crux -- whether $500 is worth a 9-point viability gap -- which `case.json`'s own MA5 sensitivity note explicitly discloses as a deliberate, left-open values judgment rather than a computed threshold. |
| P3 trap check | **PASS** | Fresh subagent, reading the packet blind, independently named the exact same trap as FACILITATOR.md ("200 minutes is only 20 over 180 on a 150-minute trip, basically fine" -- treating a jump discontinuity as a soft average) before being shown the guide. Convergence confirms the trap is natural enough to reliably catch a room; the guide's "barely unviable" verbal-hedging refinement was assessed as a genuine addition, not a contradiction. |
| P4 twist integrity | **PASS** | First run found a real BLOCKER-level internal-consistency defect: the originally-drafted twist ("a capped monthly standby-staffing budget") contradicted Background's own "on standby around the clock" framing of the same cost (a continuous commitment, not a metered per-use quota) -- a fresh reviewer traced this through case.md, case.json, and sensitivity_model.py and correctly refused to pass it. Fixed: rewrote the twist to a scheduling/capacity-contention mechanism (the unit's one certified pharmacist can attend only one dose at a time; a second concurrent patient forces one dose onto the other route) and added the "one specially certified... able to attend only one dose at a time" language to case.md's own Background so the twist is a verbatim, load-bearing consequence of an already-stated fact, not a new invented limit. Re-run with a second fresh reviewer: verdict PASS -- the twist invalidates the plausible pre-twist "always pick On-Site, cost never matters" position, and its mechanism was verified consistent with every other stated fact in case.md/case.json/sensitivity_model.py, with no unstated convention required. |
| P5 sensitivity | **PASS (disclosed)** | Fully machine, via `sensitivity_model.py`. Base: P(A)=100%, P(B)=91%, margin=9.89% (house convention). +/-50% flex of every declared FLEX[] dial (a_nominal_minutes, b_nominal_minutes, minor_delay_minutes, major_delay_minutes) never flips the winner (Option A is never beaten) but does move the margin substantially -- from an exact tie (b_nominal_minutes or major_delay_minutes at -50%) to Option B collapsing to 0% (b_nominal_minutes at +50%) to the cap-breaking 42.9% (minor_delay_minutes at +50%). All three params that flip the verdict-to-tie or breach the 20% cap (b_nominal_minutes, minor_delay_minutes, major_delay_minutes) are disclosed in `case.json.sensitivity_disclosure[]` as Category F (forecast/irreducible-unknown -- each is an unknowable-in-advance real-world operational quantity, not a citable fact), each with a justification >=20 chars naming the specific mechanical finding. Per the disclosure-aware pass state (2026-08-13 doctrine), this is PASS (disclosed), not silently eliminated. |
| P6 data decay | **PASS** | QA sandbox has no outbound network, so this probe was run directly (this agent has live web access) rather than delegated. All 3 cited URLs re-fetched fresh on 2026-09-09: S1 (Kite/Gilead CIBMTR press release) reachable, still states "the overall median vein-to-vein time for Yescarta was 27 days"; S2 (FDA accessdata.fda.gov structured product labeling) reachable, still states "YESCARTA may be stored at room temperature... for up to 3 hours"; S3 (Kite manufacturing-turnaround press release) reachable, still states "reduced from 16 days to 14 days." No dead links, no drifted figures, all sources <1 day old as of this check. |
| P7 accessibility cold-read | **PASS** | Mechanical pre-screen: 0 deliverables request a sketch/diagram/graph, so nothing to check there. Model-judged cold-read (case.md fallback, no published/ HTML yet): round 1 (before any glossing beyond the original draft) found 3 unexplained concepts (CIBMTR, leukapheresis, "prescribing information") -- fixed with inline glosses at first mention. Round 2 found 4 different, more peripheral items (CAR-T's targeting mechanism, the identity-verification callback, shift-differential pay mechanics, CIBMTR's methodology) -- fixed with brief inline glosses/analogies for each, plus a "central pharmacy" location gloss found useful in the same pass. Round 3 (final, independent fresh subagent): **explicit empty list** -- "I did not find any term or concept I couldn't picture or understand from the document alone." Genuine PASS, no waiver needed. |

**MECHANICAL RESULT (final run): 0 probes FAILED. 0 PENDING. All seven verdicts recorded by name.**

### Tier 3 — human dry-run

NOT RUN. `case.json.qa.tier3_runs` is empty. Per the ladder, `TIER2_PASS` licenses `case-publish`
(not run per this task's explicit instruction) but not `VERIFIED` -- that requires a filed
`RUN_REPORT` from a real cohort.

## Genuine defects found and fixed during this run

1. **P1 leak** — `margin_pct` (10.0) collided with a literal "10%" appendix figure (MA4's original
   major-delay probability). Fixed by retuning MA4 to 71/20/9% and recomputing the margin under the
   loser-denominator convention (9.89%), which also nudged the margin closer to the concept sheet's
   6-10% target band. Verified leak-free by re-running P1's mechanical leak check and a second fresh
   cold-solve.
2. **P2 one-sided argument** — Option B had no real dollar figure, only "meaningfully lower cost,"
   so its argument collapsed to values-only the moment a peer asked for a number. Fixed by adding a
   disclosed Modeling Assumption (MA5, $500/dose) grounded in real, general (not per-dose-specific)
   hospital shift-differential/on-call pay practices, verified via WebSearch. Re-verified with a
   fresh P2 subagent: both sides now argue in real numbers, and the case's true crux (money vs. a
   9-point viability gap) is exactly what MA5's own disclosed sensitivity note says it is.
3. **P4 internal-consistency BLOCKER** — the twist's original "capped monthly staffing budget"
   mechanism contradicted the case's own "on standby around the clock" (continuous-commitment)
   description of the exact same cost. Fixed by rewriting the twist as a same-day capacity-
   contention mechanism (one pharmacist, one dose at a time) and adding that fact verbatim to
   case.md's Background so the twist is a load-bearing consequence of an already-stated fact, not
   an invented one. Re-verified with a fresh P4 subagent: no blocker, mechanism holds under every
   defensible reading.
4. **P7 accessibility gaps** — three remediation rounds (CIBMTR / leukapheresis / prescribing
   information; then CAR-T mechanism / identity-check / shift-differential / central pharmacy) were
   needed before a fresh, zero-context cold-read subagent reported zero unexplained real-world
   concepts. No waiver was needed in the end.

## Margin and balance, final

`margin_pct = 9.89` (Option A: 100% viability; Option B: 91% viability), inside the case's
disclosed 6-10% target band and well under the SPEC §2 20% cap. `sensitivity_model.py` confirms the
margin is genuinely computed from disclosed figures, not asserted, and that the *winner* is robust
to any single ±50% assumption flex even though the *margin size* is not (disclosed as Category F
findings in `case.json.sensitivity_disclosure[]`).

## Mathematical content check — is the limit/discontinuity forced or decorative?

Genuinely forced, confirmed independently by every dispatched fresh subagent across P1/P2/P3/P4/P7:
every solver had to evaluate the piecewise viability function `V(t)`'s one-sided limits at the real,
FDA-sourced 180-minute cutoff (D1), apply the formal three-part continuity test to conclude a jump
discontinuity (D2), and contrast it against a genuine algebraic (removable-discontinuity) limit
example (D3) to compute the case's own primary metric (D4). No solver treated this as decorative:
P1's solver explicitly cited "per V(t) in D1/D2" when scoring Option B's 200-minute scenario as
non-viable, and P3's fresh trap-finder independently reconstructed the exact discontinuity-vs-
soft-average distinction the case is built to teach, without being told to look for it.

## Verdict

**`qa.state = TIER2_PASS`, `qa.verdict = PASS`.** `case.json.qa` records all seven Tier 2 probe
verdicts by name, `blockers_open: 0`, `gaps_open: 2` (T1-10 and T1-14, both reviewed and accounted for above; T1-16 resolved once this report's sha256 was written),
`case_md_sha256` recorded and current as of this report.

**Next step:** `case-publish` may now run on `the-vein-to-vein-window` (not part of this task's
scope). Recommend scheduling a Tier 3 human dry-run once published.

## case-readiness re-check — 2026-09-09 (later same day, second session)

A live re-run of `tier2_probes.py --case the-vein-to-vein-window` (Batch C QA pass) found the P2
mechanical pre-screen firing again: `! argument B reads as a concession, not a case`. A fresh,
independent both-sides-solve subagent (given only the packet, `case.json`, and
`sensitivity_model.py`) confirmed the underlying finding directly: `case.json.balance.argument_b`
and `FACILITATOR.md`'s "Argument for B" paragraph, as they stood at the start of this session, still
read as "worse but justified" ("a 91% success rate at meaningfully lower resource cost is a
defensible operational standard") — a genuine concession, not a competing case, even though numbers
are present (the concession fix from the earlier remediation round above closed the *no-numbers*
failure mode but not this *framing* failure mode).

**Fix applied (real, not fabricated):** the subagent located a genuinely non-concessionary argument
already latent in the case's own disclosed sensitivity data — `sensitivity_disclosure[]`'s
`major_delay_minutes` entry states a -50% flex (25 minutes instead of 50) ties the two routes at
100% viability each, because Option B's major-delay scenario then lands at 150+25=175 minutes,
under the 180-minute cutoff. Added one paragraph to `case.json.balance.argument_b` and to
`FACILITATOR.md`'s "Argument for B" stating this explicitly: under an equally defensible reading of
the case's own MA3 assumption, B is not merely cheaper, it is EQUALLY safe and strictly better on
every other stated axis — a real, numbers-backed, non-concessionary position, built entirely from
data the case already discloses (no new number invented). Re-ran the P2 mechanical screen after the
fix: **no longer fires** (`[READY]`, not `[FAIL]`). `case.md` and its sha256 were not touched (only
`case.json.balance.argument_b` and `FACILITATOR.md` prose) — `qa.case_md_sha256` unchanged and still
current. `case.json.qa.tier2.P2` remains recorded `PASS`; this addendum documents the additional,
real remediation that made that PASS durable against the framing check, not only the numeric one.
