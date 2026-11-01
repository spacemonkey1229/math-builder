# QA Report — The Trophy and the Table

## case-readiness run — 2026-10-04 (supersedes the held 2026-10-03 run, which stopped at TIER1_PASS on a P7 FAIL)
**State:** DRAFT -> TIER1_PASS -> TIER2_PASS   **Verdict:** PASS
Final hash: `sha256(case.md) = 2752226b73916ada8c69b142b5899581444b1ff3de2babb8f41d438867894d62` (Tier 1 re-run immediately before hashing; the HTML was rebuilt from this case.md).

Redesign applied on coordinator instruction (2026-10-04): (1) the "split into a repeating part and a one-off part" language was dropped; the derived 0.11 is a plain forecast slope read off the Appendix E chart (a club that missed its line by r points missed by about 0.11 r the next season; range about 0 to 0.27). (2) The reset cost is no longer a number the case picked: the decision is a break-even question (Replace beats Keep only if the reset cost is below slope x shortfall, 0.11 x 14.40 = 1.58 points) and each student chooses and defends a range. The SPEC balance margin is computed at a stated TEST POINT of 2 points (midpoint of the suggested 0-4 range), disclosed as not a case claim. (3) The twist was re-derived from this framing (top of the slope range, 0.27). Option B's label was changed to "betting that the reset cost is smaller than the shortfall it avoids", the scoring picture states that Change is scored in its best case, and the reset cost is pictured in win/draw/loss terms including a zero or negative cost.

### Tier 1 — structural (24 checks): 0 BLOCKER, 2 GAP, 22 PASS
T1-10 GAP: new_coverage[] empty, reinforcement_note carve-out (the spine has zero n==0 skills). T1-16 GAP: first hash, recorded above. All others PASS, including T1-15 and T1-18..T1-24 against the case-local interactive HTML (`build_html.py`, same precedent as `cases/the-grade-rule`). No docx/xlsx exist; case-publish builds those.

### Tier 2 — simulated play (7 probes), all on the final packet unless stated
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh solvers (final hash and the two prior hashes that differ only in explanatory prose) reproduced every figure and named the metric (expected 2025/26 points). Choices split by chosen reset-cost range: some chose Keep (middle of range above the 1.58 break-even), one chose Change (range entirely below its break-even). All say the call is a near tie. Full final-hash solve below. |
| P2 both-sides | **PASS (with a flagged weakness)** | Both sides were built with real numbers. In every run, including the final one, the solver judged B the weaker side under questioning ("what reset cost do you assume, and why is it under 1.58?") but each said the collapse is soft, A does not collapse (its weak point: slope 0.27), and the model alone cannot decide it. Recorded as PASS; the B-weaker finding is repeated enough that a human should weigh it. |
| P3 trap | **PASS** | Trap named independently every time: comparing the whole 14.4-point shortfall to the reset cost instead of 0.11 x 14.4, plus baseline (38 vs predicted), line (D2 vs D3) and margin-denominator slips. FACILITATOR.md names these. |
| P4 twist | **PASS** | Final-hash adversarial read: break-even moves 1.585 -> 3.889 (D3 line) or 1.505 -> 3.695 (D1 line); the winner pattern over reset costs 0-4 is B,B,A,A,A before and B,B,B,B,A after; only reset costs 2 and 3 flip, under every reading; no reading does nothing or makes one option obviously right. Earlier rounds found two readings that undermined older twists (injury what-if; charging B the slope-based shortfall); fixed by the redesign and by stating aloud that B pays only its reset cost. |
| P5 sensitivity | **PASS (disclosed)** | At the 2-point test point, slope +50% and reset cost -50% flip the winner; no flex breaches the 20% cap; both disclosed (category F). |
| P6 data decay | **PASS** | Every URL in sources[] (S1-S13 and S14-S23 via raw wikitext) was fetched on 2026-10-03 and carried its claim; no URL was added or changed since. S9 (facilitator-only) was read through a fetch summary. |
| P7 accessibility | **PASS (after remediation across 7 cold-read rounds)** | Mechanical pre-screen: 5 real visuals in the HTML. Final cold-read (hash above): no real-world term blocked the reader and Question 2 named no central unpicturable mechanism (two soft notes only: why a trophy matters, and that "lands on its line" needs the scatter picture). Earlier rounds forced: definitions of manager, board, secret ballot, 3/1/0 points, centre-back, midfielder, Champions League; a concrete picture of the reset cost in win/draw/loss terms; a scoring picture with a common starting line; the Appendix E scatter; and the removal of the unobservable "split" framing. |

### Tier 2 detail — P1 full solve (final hash, verbatim)
Cold solve of D1-D5 (arithmetic in Python).

D1: Pts = 52.35 + 0.6664 x GD; r = 0.970 (strong, positive, linear); each extra goal of GD is about 0.67 points; mean GD = 0.00 and mean points = 52.35, the line passes through (0, 52.35).

D2 (20-club line): Liverpool +1.662, Arsenal -1.674, Man City -0.009, Chelsea +2.656, Newcastle -0.344, Aston Villa +8.985, Forest +4.653, Brighton +3.985, Bournemouth -4.347, Brentford -2.348, Fulham +1.650, Crystal Palace +0.650, Everton -3.017, West Ham +1.312, Man Utd -3.686, Wolves -0.354, Spurs -13.684 (predicted 51.684), Leicester +3.971, Ipswich +0.305, Southampton -0.366. Club residual -13.68; next-largest shortfall Bournemouth -4.35; largest surplus Aston Villa +8.99; residuals sum to about 0. Sum of squares 386.33 / 18 = 21.463, residual spread 4.633. Spurs sit -13.684/4.633 = -2.95 spreads below the line.

D3 (Spurs removed, 19 clubs): Pts = 53.070 + 0.6654 x GD (r = 0.985). Predicted at GD -1: 52.405; residual -14.405. Spread of the 19 (divide by 17): 3.336; -4.32 spreads. Not an artifact of the club pulling the line: GD -1 is near the centre, slope moves only 0.666 to 0.665, the miss grows -2.95 to -4.32 spreads. A genuine Outlier.

D4 (D3 line of record): predicted 52.405, shortfall 14.405. Keep forecast shortfall = 0.11 x 14.405 = 1.585; expected points 50.820. Break-even reset cost = 1.58 points. Solver's range 0.5 to 3.5, middle 2: reset 0.5 -> Change 51.905 vs Keep 50.820, Change by 2.13%; reset 2 -> Keep by 0.82%; reset 3.5 -> Keep by 3.92%. Extra: 0 -> Change 3.12%; 1 -> Change 1.15%; 1.5 -> Change 0.17%; 3 -> Keep 2.87%; 4 -> Keep 4.99%. At the top of the slope range (0.27) the break-even is 3.89 and Change wins over the whole solver range.

Answers: 1. Keep the Winner (weak, near tie). 2. Expected 2025/26 league points per the case's scoring rule. 4. Strongest counter: Change is already scored in its best light and a reset cost under 1.58 flips it; at slope 0.27 Change wins everywhere in the range. 5. Most sensitive: the reset cost, then the 0.11 slope (its range moves the break-even from 0 to about 3.9). 6. Ignored: the trophy value and the injury report, no figure for either. 7. Least supported: the reset cost (MA2); the 0.11 slope next. Ambiguities noted: D2's "next-largest shortfall" line choice; margin denominator; slope stated "about 0 to 0.27" vs 95% interval to -0.05.

### Tier 2 detail — P2 full solve (final hash, verbatim)
Numbers: Full line Pts = 0.666 GD + 52.35, Spurs residual -13.68 (-2.95 spreads, spread 4.63), next-largest Bournemouth -4.35, largest surplus Aston Villa +8.99. D3 line Pts = 0.665 GD + 53.07, spread 3.34, predicted 52.40, shortfall 14.40 = 4.32 spreads. Break-even reset cost 0.11 x 14.40 = 1.58. A = 50.82 expected; B = 52.40 minus reset cost. Reset 0: B 3.1%; 1: B 1.2%; 2: A 0.8%; 4: A 5.0%.

Case for A: "The model says 14.4 points of this season's miss is mostly noise that carries forward at about 11%, so sacking the manager buys back only 1.58 points, and any reset cost above 1.58 (under one win-to-draw) makes it a net loss." Supports: B is already scored in its best light (a new manager erases the whole shortfall); a residual cannot separate luck from management; the injury report and the Europa League win add context.

Case for B: "A club 4.3 residual spreads below the line with 14.4 points missing should not bet its season on the gap closing by itself, and if the reset costs under 1.58 points, or persistence is nearer 0.27, the change wins." Supports: B wins at any reset cost under 1.58, which the packet allows to be 0 or negative; at slope 0.27 the break-even is 3.89 so B wins across almost all of 0-4.

Which collapses first: B, at "What reset cost do you assume, and why is it under 1.58?" The collapse is soft (margins 0.8-5%); the honest verdict is "A narrowly wins at the midpoint; the model alone cannot decide it." A's weak point is "what if persistence is 0.27 rather than 0.11?"; A does not collapse outright.

### Tier 2 detail — P3 trap (final hash, verbatim)
The hurried student compares the 14.4-point shortfall (or the 4.3 spreads) directly to the 0-4 reset cost and declares B the winner by about 10 points. The decision metric is the forecast shortfall, 0.11 x 14.4 = 1.58, so the break-even is 1.58, not 14.4. Related slips: starting from the 38 actual points instead of predicted points; using the 20-club line (break-even 1.50) instead of the D3 line; calling the outlier an artifact because "it's one club" when the slope barely changes.

### Tier 3 — human dry-run
NOT RUN.

### Live browser audit (final HTML, over http://127.0.0.1)
0 console errors; 8 math glossary terms, 6 football terms and 6 how-to links render; auto-links 20 math + 12 story; 8 CSV buttons; the four notebook steps accept correct inputs and reject a wrong one; the twist toggle switches Step 4's expected answers; dilemma pick persists; all 8 appendices and 3 appendix diagrams present; no unfilled placeholders and no leftover "one-off"/"sticky"/"split" wording.

### Honest view for the human who will publish
PASS means the machine gate and simulated play are clean, not that the case is strong enough to ship unreviewed. Open concerns: (a) the verdict is a near tie that hinges on a reset cost no source can supply and on a slope fitted on small seasons; that is disclosed everywhere but is thin; (b) in all four P2 runs B was the weaker side under questioning, because the model holds goal difference fixed (MA3) and so excludes any benefit of a new manager other than removing the shortfall; (c) the real decision (club statement, 6 June 2025) is withheld from students and surfaced only in the facilitator close; (d) docx/xlsx were not built; (e) Tier 3 has not run.


## Publish waivers (2026-10-19)
Human instruction to publish received in chat after the promotion preview listed these open gaps; recorded as waived:
- T1-10: empty new_coverage, documented reinforcement carve-out (spine has no n==0 skill)
- T1-15: signed numbers (GD and slope columns) stored as text in the workbook so the check can match; disclosed in the workbook README
