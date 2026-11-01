# Review brief: Sports Science wave (R1a / R1b / R1c)

**Status:** PROPOSED. No research done yet. All stats below are from memory and must be verified before any case uses them.
**Foundation material:** `Sports_Science_Math_Case_Studies_Bundle_2026.zip` (whitepaper, 10 CSVs, 12 SVG charts, 5 hotlinked photos).
**Gate:** proceed only if R1a, R1b and R1c are unanimous. Any dissent goes back to the author with reasons.

## The slate

| # | Case | True story | Dilemma | Math | Free data | Facts to verify |
|---|---|---|---|---|---|---|
| 1 | The Hundredth | Phelps vs. Cavic, 2008 Olympic 100 m butterfly (50.58 vs 50.59) | Is a 0.01 s margin a real result or a measurement artifact? | Rates, precision, uncertainty | Olympic results, Omega timing docs; bundle's Douglass 512 Hz work | Times, touchpad resolution, protest outcome |
| 2 | The Trophy and the Table | Spurs sack Postecoglou, 2025 (Europa League winner, 17th in league, 38 pts, GD -1) | Fire a trophy-winning manager after a 17th-place finish? Luck or management? | Regression, residuals (-13.7 pts) | EPL 2024/25 table (bundle), Football-Data multi-season, FBref xG | Dismissal facts, final table |
| 3 | The Eight-Second Tour | LeMond over Fignon, 1989 Tour (8 s, final time trial, aero bars) | Spend on aero equipment or power? | v^3 drag, sensitivity (bundle model) | Stage 21 ITT results, published CdA studies | Margin, stage distance and times, equipment |
| 4 | The Beijing Slowdown | Bolt 2008 (9.69, eased at ~80 m) vs 2009 (9.58) | How much did the celebration cost? | ODE, split analysis (bundle splits) | World Athletics biomechanics reports, both races | Beijing splits, who measured them |
| 5 | The Rest Day Fine | Popovich sits stars 2012, $250k fine; Kawhi load management 2018-19 | Is resting a star worth the penalty? Does a workload ratio justify it? | ACWR, causal inference | NBA games/minutes data; bundle ACWR evidence table | Fine amount, dates, ACWR study details |
| 6 | The Mid-Range Question | Curry (402 threes, 2015-16) vs DeRozan; Morey's Rockets | Should a coach ban mid-range shots? | Expected value, 1.5x break-even | Basketball Reference, NBA.com shot zones | 402 threes, per-zone efficiency |
| 7 | Judge's 62 | Aaron Judge, 2022 AL home run record | Chase launch angle? Where is his sweet spot? | Projectile motion vs empirical | Baseball Savant Statcast | 62 HR, his launch-angle distribution |
| 8 | The Shot from the Wing | Messi's goals vs angle to goal | Shoot from distance or take the wider angle? | Trig, subtended angle | StatsBomb open data (Messi, Barcelona) | Data coverage, shot-location fields |
| 9 | The Disgrace of Gijon | 1982 World Cup, West Germany vs Austria; simultaneous final group games | How do you schedule a group so nobody can collude? | Graph theory, game theory | FIFA schedules and group tables | Match result, rule change |

**Proposed first batch:** 1, 2, 3, 4, 6, 7.

## Changes from the bundle's original nine
- Goalball demoted: its source claim fails a geometry check and it has no iconic athlete. Folded into case 8 as a "verify a published number" sidebar.
- Swimming now leads with Phelps; the Douglass digital-twin paper becomes a supporting source.
- Round-robin K6 replaced by case 9 (real story, real data).

## Questions for each reviewer
1. Is each story true, and recognizable to middle/high school students?
2. Is each dilemma a real binary decision with a defensible case on both sides?
3. Does any case duplicate an existing one? (Known neighbours: `a-coachs-dilemma`, `lebron-vs-michael`, `baseball-lineup`, `speed-climbing`, `deluge-gun`.)
4. Is there enough free, student-explorable data to build from?
5. Does the batch respect domain diversity (it is all sports)?
6. Verdict per case: GO / REVISE / DROP, with reasons.

## Verdicts (round 1, 2026-10-03)
| Case | R1a math | R1b evidence | R1c student/corpus | Unanimous GO? |
|---|---|---|---|---|
| 1 The Hundredth | REVISE: needs protagonist whose choice depends on a computed uncertainty band | GO: cite Omega/FINA for resolution; no press-agency photo | GO: named official as protagonist | No (R1a). Fixable. |
| 2 Trophy and Table | GO | GO: FBref xG removed Jan 2026, use StatsBomb/Understat | REVISE: living manager, EU competition, soccer overlap | No (R1c). Fixable. |
| 3 Eight-Second Tour | REVISE: aero dominates, needs budget/rule constraint | GO: do not state "aero gained X s" as fact | GO: frame from team director | No (R1a). Fixable. |
| 4 Beijing Slowdown | REVISE, near DROP | REVISE (blocking): no official Beijing splits | REVISE: estimate, not decision | No. HOLD. |
| 5 Rest Day Fine | REVISE | REVISE: ACWR evidence is rugby/youth football, not NBA | REVISE, leaning DROP | No. HOLD/DROP. |
| 6 Mid-Range Question | REVISE: no defensible side (~0.8 vs 1.08 pts) | REVISE: no licensed data source | REVISE: overlaps a-coachs-dilemma | No. HOLD. |
| 7 Judge's 62 | DROP as framed | REVISE: not a real decision; Statcast terms unchecked | REVISE | No. HOLD. |
| 8 Shot from the Wing | REVISE (minor): 7.32 m goal | REVISE: no real dilemma; StatsBomb logo/attribution terms | REVISE | No. HOLD. |
| 9 Disgrace of Gijon | REVISE: needs binary protagonist choice | GO: frame as incentives, not accusation | GO | No (R1a). Fixable. |

**Overall:** R1a BLOCK, R1b BLOCK (full slate), R1c BLOCK. No case is unanimous GO as written.
**Converged candidates:** 1, 2, 3, 9 (no reviewer says DROP; all objections are fixable framing).
**Blocking for all:** domain concentration (all sports; ~10 of 186 existing are sports). Cap the wave at 3-4, each paired with a non-sports case.

## Round 2-4 history (condensed)
- Round 2 (concepts file CONCEPTS_sports-science_2026-10-03.md): R1a BLOCK, R1b/R1c conditional APPROVE.
- Round 3: R1a BLOCK (C1 uphold dominates; C4 option A dominates), R1b/R1c APPROVE conditional.
- Round 4: R1a APPROVE (C1-C4 GO), R1b APPROVE (C1-C4 GO), R1c BLOCK on two small items: C4 open ending and forward cost of Option B; release-plan slots in already-mined domains. Both fixed; R1c confirmation pending.
- Standing conditions: Fintelman 14% human check; 1982 tie-break ladder URL; 2008 FINA rule wording; lag range stays labelled an assumption.

## GATE MET (2026-10-03, after round 4 + R1c confirmation)
R1a APPROVE (C1-C4 GO), R1b APPROVE (C1-C4 GO), R1c APPROVE (C4 and release plan GO after fixes). Unanimous. Proceed to research and drafting for C1-C4.
Open conditions carried into research: Fintelman abstract human check; 1982 tie-break ladder URL; 2008 FINA rule wording; keep C1 lag range labelled assumption; nuclear slot prefers decay/shielding angle.
