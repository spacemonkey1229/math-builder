# QA Report: The Sixteenth Land

## case-readiness run, 2026-10-28
**State:** DRAFT -> TIER1_PASS (Tier 2 incomplete)   **Verdict:** BLOCKED (not TIER2_PASS; P7 FAIL)
sha256(case.md) is recorded in case.json.qa.case_md_sha256.

### Tier 1: structural
24 checks, 0 BLOCKERs. GAPs: T1-10 (new_coverage[] empty, reinforcement carve-out: no spine skill has n=0, reinforcement_note recorded), T1-16 (hash recorded by this run), T1-14 cleared after moving guide-only figures into case.json.derived. Preflight lint clean. No published/ directory yet (T1-15, 18-24 had nothing to check).

### Tier 2: simulated play
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Three fresh solvers (and a final re-run on the final text) chose B on the locked metric, with exact arithmetic matching the model (0.8446 vs 0.8510, 0.75%), named the metric, flagged the window/turn as the sensitive dial. Ambiguity found and fixed: D4 "how many windows" -> "nine windows (at turn 4)". |
| P2 both-sides | PASS | Neither side collapses. A is the more exposed side (loses the primary by 0.75% and the no-play hand by 21.54%) but has the draw (+0.61%), 3 of 9 windows, turn 5, flood (P(>=7 lands) 3.2% vs 4.9% in 10 cards) and an unpriced 24th spell. |
| P3 trap | PASS | Cold reviewer named (1) stopping at the opening-hand 21.5% number, (2) play-only / 10-vs-11 card miscount, (3) binomial with replacement or wrong window. Guide originally lacked (1); added as trap form (0). Others already named. |
| P4 twist | PASS | Free redraw of 0/1/6/7-land openers flips the winner to 16 under all five readings (0.545% to 1.729%). Conventions the packet never states (discard shuffled back; discards not counted as seen; twist overrides "no redraws") added to FACILITATOR.md. |
| P5 sensitivity | PASS (disclosed) | Verdict flips under lo -50% (A), hi -50% (A), turn +50% (A); not under play share. Disclosed in sensitivity_disclosure[] and FACILITATOR.md. |
| P6 data decay | PASS | S1 reachable, PMF and with/without-replacement contrast present. No other sources. |
| P7 accessibility | FAIL | Mechanical: D5 requests a chart; no published/ HTML exists, so the pre-screen cannot find a visual (case.md carries an illustrative inline SVG that renders only at publish). Cold-read: Q1 0-1 unexplained terms; Q2 a mild answer on the final run (why a land count among cards seen stands in for lands in play). Re-run on published HTML. |

### Tier 2 detail: P1 full solve (final run, condensed to the numbers)
D1: C(40,7)=18,643,560; 16L: 0 lands C(24,7)=346,104, 1 land 16xC(24,6)=16x134,596=2,153,536; 17L: C(23,7)=245,157, 17xC(23,6)=17x100,947=1,716,099.
D2: 16L 2,499,640/18,643,560=13.41%; 17L 1,961,256/18,643,560=10.52%; 17 has 21.54% fewer.
D3: C(40,10)=847,660,528; C(40,11)=2,311,801,440. Play 16L 0.8370, 17L 0.8550; draw 16L 0.8522, 17L 0.8470; averaged 0.8446 vs 0.8510; margin 0.75% for 17.
D4 (turn 4, averaged): 2-5 16 by 5.84%; 2-6 16 by 1.75%; 2-7 17 by 0.14%; 3-5 16 by 3.40%; 3-6 17 by 0.75%; 3-7 17 by 2.64%; 4-5 17 by 1.60%; 4-6 17 by 5.78%; 4-7 17 by 7.72%. 16 wins 3 of 9. 3-6: turn 3 17 by 3.27%, turn 5 16 by 2.13%.
D5: play 14-19 = .7627 .8061 .8370 .8550 .8599 .8518; draw = .8156 .8418 .8522 .8470 .8266 .7920.
D6: adopted 3-6 at turn 4 because fixed in advance; six notebook games cannot separate a 0.6-point difference.
Strongest counter: margin under 1%, flips with window and turn count; A leads on the draw. Most sensitive: window (then turn, play share). Least supported: the upper bound 6.

### Tier 2 detail: P2 full solve
A: draw 0.8522 vs 0.8470; windows 2-5, 2-6, 3-5; turn 5 (0.8432 vs 0.8252); flood P(>=7 lands in first 10) 3.18% vs 4.86%, in first 11 6.53% vs 9.60%; one more spell. B: play 0.8550 vs 0.8370; primary 0.8510 vs 0.8446; no-play 10.52% vs 13.41%; 6 of 9 windows; turn 3; P(0-2 lands in 10 cards) 9.64% vs 13.11%.

### Tier 3: not run.

### Remaining
BLOCKER: none (Tier 1). Open for TIER2_PASS: P7 re-run after case-publish. GAP: T1-10 reinforcement carve-out; the 17Lands real-data Twist is a plan only (licence unverified, no file downloaded, not analysed).
