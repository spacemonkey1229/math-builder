# QA Report — The Eight-Second Tour

## case-readiness run — 2026-10-03
**State:** DRAFT -> TIER1_PASS (Tier 2 NOT clean: P2 FAIL)   **Verdict:** BLOCKED (1 open Tier 2 finding)

### Tier 1 — structural (24 checks)
`sha256(case.md) = 5ddb2c19c0bfc8cab6db14022d369593c722c3ae5255f12ff9544315344c570c`

0 BLOCKER. 2 GAP: T1-10 (reinforcement carve-out: live spine had zero n==0 skills; `reinforcement_note` on file) and T1-16 (resolved by this report's hash record). T1-15, T1-18..T1-24 are POLISH "no published/ directory yet": case-publish has not been run (out of scope for this authoring pass), so interactive-HTML, glossary-rendering and live-browser checks have NOT been exercised.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver did D1-D5 with correct arithmetic, chose B, named the metric (speed against the 54.277 km/h break-even), the assumptions MA3/MA2, and the least-supported number (the 3% floor on y). Caveat: it chose B on the ground that aero fails the 50 s target at its believed point, although under MA1 B cannot reach the target either (see P2). |
| P2 both-sides | **FAIL** | Both fresh arguments were built with correct numbers, but B collapses at the first question, "How does B win the Tour?": under MA1 (equal conventional speed) B is a certain 50 s loss, so B is defensible only as risk-management or by attacking MA1/MA2/MA3, while A has a winning region (about 13% of the Appendix D box under the cube law, about 9% under the full model). The recorded 1.50% margin is a speed margin (A faster than B in about 86% of the box) and is therefore a paper number against the Tour criterion. Routes back: case-write (see below). |
| P3 trap | PASS | Fresh solver's trap (stop at "aero is faster", never test the 50 s bar) matches the guide's named trap; the guide's second trap (reading the two 14% figures as a matched pair) is also present. |
| P4 twist | PASS | Twist (x 12.5%, y 14%, supplied together) flips A to B on speed by 0.58% under cube law and 0.94% under the full model, and worsens every A position in the box. One non-blocking weakness (a student could keep A because B cannot win): fixed by adding "they replace your own x and y" and a recommit probe to FACILITATOR.md. |
| P5 sensitivity | PASS (disclosed) | cda_cut -50% (6.25%) and power_loss +50% (12.75%) flip the winner to B; the other two flexes widen A's lead to 4.04% and 3.05%; no breach of the 20% cap. Both dials disclosed (category F) in sensitivity_disclosure[]. |
| P6 data decay | PASS | All four URLs fetched: S1 (stage facts and equipment sentence present), S2 (Benjamin Werner, CC BY 2.0, Flickr bw94), S3 (14% drag), S4 (46 km/h; no 14% power figure). Note: the S1 page also carries a sentence citing a 1989 magazine estimate of about a minute gained from aero bars; the case deliberately does not use it. |
| P7 accessibility | PASS (after 2 remediation rounds) | Round 1 named about 9 unexplained setting terms; round 2 (after glosses for the hoods, follow car, stage-race standings, disc wheel, sustainable power, drafting, drag area, torso angle) still returned a Q2 finding on the hindsight scenario; an "In plain terms" paragraph was added; round 3 named 0 central unpicturable constructs. Residual gaps: no feel for watt scale (D5 now tells the student to find and cite a reference), a vague picture of "the hoods". Caveat: read from case.md, not published HTML. |

### Tier 2 detail — P1 full solve
D1: 1617 s / 1675 s / needed 1625 s; speeds 54.5455 / 52.6567 / 54.2769 km/h = 15.1515 / 14.6269 / 15.0769 m/s; needed ratio 1675/1625 = 1.0308. D2: 1.0308^3 = 1.0952 (+9.52%). D3 aero-only y = 1 - 1.09518(1 - x): 1.43 / 5.81 / 6.91 / 12.39 percent at x = 10 / 14 / 15 / 20; full model (P_conv 658.1 W at 14.6269 m/s; rolling 46.14 W at the needed speed): 1.13% at x = 10, 6.23% at x = 15 (rolling-resistance block does not shrink, so the full model tolerates less). D4: points (10, 1.43), (14, 5.81), (15, 6.91), (20, 12.39); y = 1.0952x - 0.0952, slope 1.0952, zero crossing x about 8.7%; believed pair x 12.5%, y 8.5% sits above the 4.17% break-even. D5: 681.7 W aero + 46.4 W rolling = about 728 W at 26:57; judged not sustainable; ratios only. Choice B; metric speed against the break-even; strongest counter: the literature leans aero above 46 km/h; most sensitive to MA3; ignored the 15-25% figures; least supported: the 3% floor on y.

### Tier 2 detail — P2 full solve
Shared: needed ratio 1.0308, power factor 1.0952. A (best case): only option with a winning region: x 14% tolerates y 5.8%, at y 3% and x 14% about 66 s saved, at x 15% and y 3% about 72 s; "Conventional riding can only tie Fignon's 27:55, which still loses the Tour by 50 s, so the only way to win is to bet that the aero position's drag cut outruns its power loss." B (best case): inputs unsourced (MA3, the 3% floor is the author's); about 87% of the box fails the target (91% under the full model); A is slower than B wherever y > x (about 14% of the box); variance; "The literature never measured the power cost of aero bars, so the 50-second target rests on an unsourced y." Collapse: B, at "How does B win the Tour?" (needs +9.5% power, B ratio 1.0000 vs 1.0308); A's weak point: "What is your y, and where does it come from?" Solver verdict: not a fair coin flip under its own numbers.

### Tier 3 — human dry-run
NOT RUN.

### Unresolved before TIER2_PASS
P2 FAIL needs a case-write decision (not a research fix). Options: (a) replace MA1's exact equality with a stated range or give B a legitimate route to the target; (b) reframe the dilemma so the decision criterion is explicitly the faster ride (A faster in about 86% of the box, B faster where y > x) and the 50 s bar becomes a graded follow-on; (c) accept the asymmetry, tell the room (already in FACILITATOR.md), and obtain a recorded human waiver. This pass did not choose, because the concept specified MA1 and the reviewers approved it.


## case-readiness run 2 — 2026-10-03 (after the MA1 redesign)
**State:** TIER1_PASS (Tier 2 NOT clean: P2 FAIL)   **Verdict:** BLOCKED (1 open Tier 2 finding)
`sha256(case.md) = c3c4a27a74349c68c0c2a5071318e992da046bd2837ca7d0cca5638965a08e5a` (Tier 1: 0 BLOCKER, 2 GAP: T1-10 carve-out, T1-16 resolved by this hash; no published/ yet so T1-15, T1-18..T1-24 are POLISH.)

Change under test: MA1 now uses a sourced baseline b (1.0000 to 1.0109, from the prologue, stage 5 and stage 15 ITTs, S5/S6) instead of exact equality, and the primary criterion is the faster ride with the 50 s bar as a graded follow-on (route b, because the real baseline still cannot close 50 s). The run-1 results above are superseded by this table.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver reproduced every D1-D5 number (ratios 1.0000/1.0095/1.0109, needed 1.0308, power factors 1.0952 and 1.0600, break-even tables, shares 12.7%/38.6%/85%, 728 W), chose A on best expected speed, named MA3 as most sensitive and the 3% floor as least supported. |
| P2 both-sides | **FAIL** | A is not a strawman. B is defensible on the primary metric only as a risk argument (best worst case; faster than A in about 14% of the box), and collapses at "how does Full Power get LeMond 50 seconds?": at the best baseline B gains about 18 s. The solver judged the "honest tension" framing overstated. Same underlying cause as run 1: the sourced prior is too small (at most 1.1% against 3.1% needed) to give B a route to the bar. |
| P3 trap | PASS | Fresh solver's trap matches the guide's, including the triathlon-bars caveat on stage 5 and the 14%/14% pair. |
| P4 twist | PASS | Flips A to B on speed at every b in the range (b cancels), by 0.58% cube law and 0.94% full model; no unstated convention. One delivery risk (the facilitator must say the twist's x and y replace the student's own) is in the script, and a wording fix was applied. |
| P5 sensitivity | PASS (disclosed) | Unchanged: cda_cut -50% and power_loss +50% flip the winner; both disclosed (category F). |
| P6 data decay | PASS | All six URLs (S1-S6) re-fetched; every value present. Note: the main Wikipedia page also carries a Texas A&M finding and a magazine "about a minute" estimate for the aero gain; neither is used. |
| P7 accessibility | PASS (after fixes) | Cold-read of the revised packet: no blocker; fixes applied for "prologue", triathlon bars = aero bars, and how b and the aero ratio combine. Residual: no sense of watt scale; "hoods". Read from case.md, not published HTML. |

### Tier 2 detail — P1 full solve (run 2, key numbers)
D1: prologue 600/600 s (1.0000); stage 5 5892/5948 s, 44.60/44.18 km/h (1.0095); stage 15 4299/4346 s, 32.66/32.31 km/h (1.0109); stage 21 1617/1675 s (1.0359, not a baseline); needed 1625 s, 54.277 km/h, total ratio 1.0308. D2: aero must supply 1.0308 (power factor 1.0952, +9.5%) at b = 1.0000 and 1.0196 (1.0600, +6.0%) at b = 1.0109. D3 aero-only y max at x = 10/14/15/20: 1.43/5.81/6.91/12.39 percent (b low), 4.60/8.84/9.90/15.20 percent (b high); full model b low 1.13 / 6.23 percent at x = 10 / 15. D4: y = 1.0952x - 0.0952 (slope 1.0952); upper line y = 1.0600x - 0.0600; shares of the box 12.7% / 38.6% / 85% (merely faster). D5: about 728 W (681.7 aero + 46.4 rolling); judged not sustainable; ratios only. Choice A at (14%, 8.5%), metric speed; strongest counter: at b low aero gains about 34 s, short of 50.

### Tier 2 detail — P2 full solve (run 2, key numbers)
Best for A: only option that can reach the bar (B ceiling about 18 s of 50); A faster in about 85% of the box. Best for B: y unmeasured, aero slower where y > x (worst about 26 s slower), best-worst-case rule picks B, upper baseline comes from a mountain ITT where the cube law fits poorly. B collapses at "How does Full Power get LeMond 50 seconds?"; A's weak point is "What is y?".

### Unresolved before TIER2_PASS
P2 FAIL needs a human case-write decision. Sourcing the baseline did not make Full Power competitive against the 50 s bar. Options: (1) accept and record a waiver (A is the better bet on both criteria; the case's honest tension is a decision-rule and evidence one, already stated in FACILITATOR.md); (2) drop the 50 s bar from the decision entirely and make the case purely "A vs B on predicted speed" with y as the tension (then the Background must stop saying the Tour is won only by 50 s); (3) widen the sourced baseline with a stated rival-time uncertainty so B has a non-zero route (needs a source for how well Fignon's stage 21 time could have been predicted; none found); (4) replace the story with a concept where the conventional choice has a real upside. This pass has not chosen.


## case-readiness run 3 — 2026-10-04 (final; published HTML built case-locally, live-browser audited)
**State:** TIER1_PASS (Tier 2 NOT clean: P2 FAIL)   **Verdict:** BLOCKED
`sha256(case.md) = 95dc194c3635b5e30082f5df1d3fe48998d521ae36f91ad6f11e8d448e87e8db` (Tier 1 re-run immediately before hashing: 0 BLOCKER; 1 GAP, T1-10 reinforcement carve-out; 1 POLISH.)
Interactive HTML built by the case-local script `build_html.py` (same precedent as the-grade-rule and the-trophy-and-the-table) plus `skills/case-publish/scripts/render_context.py` for the story glossary; no case-publish was run. T1-15 and T1-18 to T1-24 now run against `published/` and pass.

**Live browser audit (served over http://127.0.0.1, then stopped):** console clean (no errors). All seven sections present; tab navigation worked by real clicks; the Figure B1 SVG (21 points) renders with its points inside the plot area and axes aligned; the stage 21 photo loads (1024 px) with its CC BY 2.0 credit caption; the glossary shows 21 math terms and 12 story terms with tooltips. **Defect found and fixed:** the story-glossary tooltips rendered as visible inline text because the builder's own partial `.sterm` CSS stopped `render_context.py` from adding the tooltip rules; the builder's rule was removed and the tooltips now hide and show on hover. Notebook checks driven with correct and incorrect values: all five steps and the twist toggle behave (correct inputs show a tick, wrong ones "try again"). Placeholders contain no digits. Minor polish: input boxes are narrow, so placeholders were shortened. Not tested: mobile width, print/PDF export.

### Tier 2 — simulated play (7 probes; fresh solvers/cold readers on this build)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh solver reproduced every D1-D5 number (b 1.0000-1.0109, needed ratio 1.0308, power factors 1.0952/1.0600, break-even tables, shares 12.7%/38.6%/86%, 728 W), chose A on best-expected speed checked against best worst case, named MA3 as most sensitive and the 3% floor as least supported. Full solve below. |
| P2 both-sides | **FAIL** | A is not a strawman. B is defensible only as a risk or maximin argument and collapses at "does Full Power reach 50 s?" (it gains at most about 18 s). The solver expects nearly all students to choose A: the case is lopsided toward A, balanced only in how confident A deserves to be. Full solve below. |
| P3 trap | PASS | Fresh solver's trap matched the guide's, including secondary traps. |
| P4 twist | PASS | Twist flips A to B at every b in range (b cancels); no unstated convention; "replace your own x and y" is scripted. Caveat: a student who judges on the 50 s bar alone sees no change (both fail it before and after). |
| P5 sensitivity | PASS (disclosed) | cda_cut -50% and power_loss +50% flip the winner; both disclosed (F); no cap breach. |
| P6 data decay | PASS | All six data URLs and all 15 glossary links resolve; values present. Notes: Aero_bars redirects to the Bicycle handlebar page; time.html is about clock reading. |
| P7 accessibility | PASS (borderline) | Run 3 and run 4 each returned a concrete Q2 answer (how the baseline b multiplies with the aero ratio); after a worked made-up example and the total-ratio sentence were added, run 5 named no wholly unpicturable object (nearest: the b-times-aero comparison against the 50 s bar) and no blocking term. Residual: stage structure and the leader are explained after the Overview; watt scale; "hoods". |

Probes P1-P4 and P6 ran on the build before the Appendix A "how to use the table" sentence and the b-multiplication illustration were added to case.md (text-only clarifications, no number changed); P7 re-ran on the final text.

### Tier 2 detail — P1 full solve (verbatim, run on this design)
> # Cold-solve: The Eight-Second Tour
> 
> I read only PACKET.md and used Python as a calculator.
> 
> ## 1. Choice
> **A, Aero Bars.**
> 
> - It is faster than Full Power in most of the plausible range (about 86% of the shaded box).
> - Full Power alone can never win the Tour. Its best case is a gain of about 18 s, and the target is 50 s.
> - Aero Bars is the only option that can reach the target. I put that chance at roughly 13% to 39% of the box. I do not claim it is likely.
> 
> ## 2. Metric and why
> I optimised the predicted average speed over 24.5 km (equivalently, the finish time) under the scenario model. This is the case's stated primary metric, and the 50 s bar is a second test of how far each option gets.
> 
> Speed is the right metric because the winner is whoever finishes fastest. Raw power is not the goal: Full Power names a posture, not extra effort.
> 
> Decision rule: I use "best expected result, checked against best worst case".
> - Expected: Aero Bars is faster at the believed point and over about 86% of the box.
> - Worst case: Aero Bars is up to 26 s slower at the corner (x = 10%, y = 14%, b = 1.0000), while Full Power is never more than 18 s ahead. I accept that downside because Full Power cannot win the Tour in any scenario.
> 
> ## 3. Arithmetic
> 
> ### D1. Times and speeds
> Winner's time plus gap, in seconds. Speed is km/h = distance / seconds × 3600. Ratio is Fignon's time divided by LeMond's time.
> 
> | Time trial | km | LeMond (s) | Fignon (s) | LeMond km/h | Fignon km/h | Ratio L/F |
> |---|---|---|---|---|---|---|
> | Prologue | 7.8 | 9:54 + 6 = 594 + 6 = 600 | 600 | 46.800 | 46.800 | 1.00000 |
> | Stage 5 | 73 | 1:38:12 = 5892 | 5892 + 56 = 5948 | 44.603 | 44.183 | 1.00950 |
> | Stage 15 | 39 | 1:10:42 + 57 = 4242 + 57 = 4299 | 4242 + 104 = 4346 | 32.659 | 32.306 | 1.01093 |
> | Stage 21 (real) | 24.5 | 26:57 = 1617 | 27:55 = 1675 | 54.545 | 52.657 | 1.03587 |
> 
> Stage 21 is not used as a baseline.
> 
> - Baseline range: **b from 1.0000 to 1.0109**.
> - Needed finish time: 27:55 − 50 s = 1675 − 50 = **1625 s = 27:05**.
> - That speed is 24.5 / 1625 × 3600 = 54.277 km/h.
> - Needed total speed ratio over Fignon: 1675 / 1625 = **1.03077**.
> 
> ### D2. Needed power factor
> The aero position must supply R/b, where R = 1.03077.
> 
> | Baseline | Aero ratio needed | Power factor (ratio³) | Percent increase |
> |---|---|---|---|
> | b = 1.0000 | 1.03077 | 1.03077³ = 1.0952 | **+9.52%** |
> | b = 1.0109 | 1.03077 / 1.01093 = 1.01962 | 1.01962³ = 1.0600 | **+6.00%** |
> 
> ### D3. Break-even table
> The aero-only break-even condition is ((1−y)/(1−x))^(1/3) = a, so y = 1 − a³(1−x). The values are a³ = 1.0952 (b = 1.0000) and a³ = 1.0600 (b = 1.0109).
> 
> | x | Largest y, b = 1.0000 | Largest y, b = 1.0109 |
> |---|---|---|
> | 10% | 1 − 1.0952 × 0.90 = 1.43% | 1 − 1.0600 × 0.90 = 4.60% |
> | 14% | 5.81% | 8.84% |
> | 15% | 6.91% | 9.90% |
> | 20% | 12.39% | 15.20% |
> 
> **Full two-term model, b = 1.0000.** Parameters: ρ = 1.225, CdA = 0.32, Crr = 0.004, m = 78, g = 9.81.
> - Conventional speed = 52.657 km/h = 14.627 m/s. Total power = 0.5 × 1.225 × 0.32 × 14.627³ + 0.004 × 78 × 9.81 × 14.627 = 658.1 W.
> - Aero must reach 54.277 km/h = 15.077 m/s.
> - At x = 10%, the aero position's power is 0.5 × 1.225 × 0.288 × v³ + rolling = 650.7 W. So 1 − 650.7/658.1 = **y = 1.13%** (aero-only gave 1.43%).
> - At x = 15%, the aero position's power is 617.1 W. So **y = 6.23%** (aero-only gave 6.91%).
> 
> The full model tolerates less power loss. Rolling resistance (about 46 W at the target speed) is not reduced by the drag cut. The extra speed also adds rolling power. So the drag saving is a smaller share of the total.
> 
> ### D4. Chart
> I did not render the picture. The plot would be:
> - x-axis: drag cut, 8% to 22%.
> - y-axis: power loss, 0% to 16%.
> - Line 1 (b = 1.0000): through (10%, 1.43%), (14%, 5.81%), (15%, 6.91%), (20%, 12.39%).
> - Line 2 (b = 1.0109): through (10%, 4.60%), (14%, 8.84%), (15%, 9.90%), (20%, 15.20%).
> - Shaded box: x 10 to 15%, y 3 to 14%.
> - Marked "believed" point: (12.5%, 8.5%), the midpoint of both ranges.
> 
> **Lower-baseline line:** y = 1.0952x − 0.0952.
> - The slope is 1.0952.
> - Plain meaning: every extra percentage point of drag the aero position removes lets the rider give up about 1.1 points more power and still reach the goal. Drag cuts and power loss trade almost one for one, with a bit extra because of the cube law.
> - Upper-baseline line: y = 1.0600x − 0.0600.
> 
> **Share of the box on the winning side** (y at or below the line, by numerical area):
> - Lower baseline: about 12.7%.
> - Upper baseline: about 38.6%.
> - Aero faster than Full Power at all (y < x): 0.00475 / 0.0055 = 86.4%.
> 
> **The believed point (12.5%, 8.5%) fails both lines.** The lines at x = 12.5% sit at y = 4.17% and 7.25%, below 8.5%. Aero speed ratio ((0.915/0.875)^(1/3)) = 1.0150.
> 
> | Baseline | Aero speed | Aero finish | Time gain vs Fignon | Full Power finish | Full Power gain |
> |---|---|---|---|---|---|
> | b = 1.0000 | 53.45 km/h | 1650 s | 24.8 s | 1675 s | 0 s |
> | b = 1.0109 | 54.03 km/h | 1632 s | 42.6 s | 1657 s | 18.1 s |
> 
> Aero does not reach 50 s at the believed point, but it beats Full Power by 25 s at both baselines.
> 
> Box corners (aero gain, b = 1.0000 / 1.0109):
> 
> | x, y | Gain at b = 1.0000 | Gain at b = 1.0109 |
> |---|---|---|
> | 10%, 3% | +41.3 s | +59.0 s |
> | 15%, 3% | +72.1 s | +89.5 s |
> | 15%, 14% | +6.5 s | +24.6 s |
> | 10%, 14% | −25.6 s | −7.2 s |
> 
> ### D5. Model limits
> At 54.545 km/h = 15.152 m/s, the full model gives:
> - Aero term: 0.5 × 1.225 × 0.32 × 15.152³ = 681.7 W.
> - Rolling term: 0.004 × 78 × 9.81 × 15.152 = 46.4 W.
> - Total: about **728 W**, or 9.3 W/kg for a 78 kg rider and bike.
> 
> I find that not sustainable for 27 minutes. Sustained power for a good professional over about 30 minutes is, from my general memory, in the 400 to 450 W range. I could not look up a citation, so I give this reference low weight and it is unverified.
> 
> The 728 W implies that the Appendix B parameters are wrong for LeMond, most likely CdA = 0.32 being too high for a tucked time-trial rider. That is why the case uses ratios only: absolute watts would be false, but ratios mostly cancel the scale error.
> 
> What the literature supports:
> - García-López [S3] gives about 14% drag change from position changes. It measures drag only, not aero bars against a conventional position.
> - Fintelman [S4] says aero losses outweigh power losses above 46 km/h. It gives no power-loss figure.
> - Neither study measures y, and the two cannot be combined. So the x and y ranges are a sensitivity range, not data.
> 
> Two things the model leaves out: wind, course profile and cornering; and drafting, helmet and wheels (also pacing, rolling-resistance changes with speed, and a rider's variable effort).
> 
> ### Pitch
> Aero Bars is faster than Full Power across about 86% of the plausible range, and it is the only option that can win. The conventional position cannot beat a 50 s deficit even in the best case. The tuck plus triathlon-bars position pays at the roughly 54 km/h race speed, well above Fintelman's 46 km/h crossover. I rate it a high-variance bet: it wins the Tour in about 13% to 39% of the box. Full Power is a certain loss. The pitch used unit conversion, ratios, exponents and linear equations ("How to write a linear equation from data" was the Challenge 1 skill, a resource I did not research here).
> 
> ## 4. Strongest argument against A
> At the believed point, Aero does not reach the 50 s bar at either baseline (24.8 s and 42.6 s). Only 13% to 39% of the box wins the Tour. The power-loss lower bound (3%) is the author's own invention, and if y is near 14% Aero is slower than conventional by up to about 26 s. Also, y is a fatigue effect that grows over 27 minutes, which a steady-state model hides. A director could reasonably prefer the known position.
> 
> ## 5. Most sensitive assumption
> **MA3, the power loss y (3% to 14%).** The lower bound of 3% is the author's guess. The break-even for y at x = 10% is only 1.4% to 4.6%, so the outcome flips across the range. MA1 (the baseline b, 1.0000 vs 1.0109) comes second: it moves the winning share from about 13% to about 39%.
> 
> ## 6. Ignored in the appendices
> I ignored the stage 21 real-time ratio (1.0359) as a baseline, since the case says not to use it and it would smuggle in hindsight. I also set aside the "15-25% popular aero drag figures" in Appendix C, which are not peer reviewed. Separately, I did not use the real equipment differences (helmet and wheels), because MA6 holds them equal.
> 
> ## 7. Least supported number
> **The 3% lower bound for y**, which the case itself admits is its own assumption. Close behind is b: the prologue's 1.0000 comes from a 7.8 km short effort with a different course and equipment, and Wikipedia is the only source.

### Tier 2 detail — P2 full solve (verbatim)
> # Report on "The Eight-Second Tour"
> 
> I used only PACKET.md and Python as a calculator.
> 
> ## Shared numbers (D1 and D2)
> 
> | Time trial | LeMond | Fignon | LeMond/Fignon speed ratio |
> |---|---|---|---|
> | Prologue, 7.8 km | 600 s | 600 s | 1.0000 |
> | Stage 5, 73 km | 5892 s | 5948 s | 1.0095 |
> | Stage 15, 39 km | 4299 s | 4346 s | 1.0109 |
> 
> - **Baseline range:** b runs from 1.0000 to 1.0109.
> - **Stage 21 target:** Fignon rode 27:55 = 1675 s. LeMond needs 1625 s (27:05) or better. The total speed ratio he needs is 1675/1625 = 1.0308.
> - **Ratio the aero position must supply (D2):** 1.0308 at b = 1.0000, and 1.0196 at b = 1.0109.
> - **Power factor for those ratios (cube law):** 1.0952, a 9.5% increase, at b = 1.0000, and 1.0600, a 6.0% increase, at b = 1.0109.
> - **Conventional position (B), model speed:** about 52.66 km/h at b = 1.0000, which needs about 658 W in the full model.
> - **Break-even condition (aero-only):** y ≤ 1 − r³(1−x), where r is the ratio D2 requires.
> 
> Break-even y (D3):
> 
> | x | b = 1.0000 (aero-only) | b = 1.0109 (aero-only) |
> |---|---|---|
> | 10% | 1.4% | 4.6% |
> | 14% | 5.8% | 8.8% |
> | 15% | 6.9% | 9.9% |
> | 20% | 12.4% | 15.2% |
> 
> The full two-term model, at b = 1.0000, tolerates less loss, because rolling resistance does not shrink when drag does:
> 
> | x | y, full model |
> |---|---|
> | 10% | 1.13% |
> | 15% | 6.23% |
> 
> At b = 1.0109 the full-model figures are 4.16% for x = 10% and 9.11% for x = 15%.
> 
> Break-even line at b = 1.0000: y = 1.0952x − 0.0952. The slope is about 1.1, so each extra point of drag cut buys about 1.1 points of tolerable power loss. That is close to one-for-one trading, which is the director's rule of thumb.
> 
> ## Option B, Full Power: the strongest case
> 
> **The argument.** The one number B controls is how fast LeMond rides in the conventional position. Under the packet's own baseline that is Fignon's speed times b, where b is between 1.0000 and 1.0109.
> 
> - At b = 1.0109 he finishes in 1675/1.0109 = 1657 s. That is 18 s gained and the Tour lost by 32 s.
> - At b = 1.0000 he finishes in 1675 s. That is no gain and the Tour lost by 50 s.
> 
> So the 50-second test is failed everywhere, and B has no route to the win inside the model. B's defence therefore cannot be "B wins." It has to be a risk-and-honesty argument.
> 
> - **Aero Bars is only faster than B when y < x.** (The cube-law form is speed ratio ((1−y)/(1−x))^(1/3).) The packet's range is x from 10% to 15% and y from 3% to 14%. About 86% of that rectangle has y < x, so about 14% of it has the aero position slower than B.
> - **The packet admits y is unmeasured.** MA3 says no source measures it, and the 3% lower bound is the author's own assumption. At the worst corner (x = 10%, y = 14%) A is about 25 s slower than B, at b = 1.0000.
> - **The literature is thin.** García-López [S3] measured position changes, not aero bars against a conventional position. Fintelman [S4] gives only a speed crossover and no power-loss figure.
> - **The model is not LeMond.** It implies about 728 W for his real 54.5 km/h average, which D5 prompts you to doubt. "I choose the posture whose speed I can bound" is a defensible maximin-on-speed rule.
> - **Supporting point against the baseline.** LeMond used triathlon bars in stage 5 [S5], so b is contaminated by aero effects. The true conventional ratio may be lower, and that makes B look no better.
> 
> **Single best sentence for B:** "We cannot measure how much power the tuck costs him, and the only variable we know how to bound is the conventional position, so I minimise the chance of riding slower than baseline even though I accept it will not close the 50 seconds."
> 
> **Can a competent student defend B?** Only narrowly, and only by changing the question to "least downside." The argument has to concede up front that B never reaches the target.
> 
> ## Option A, Aero Bars: the strongest case
> 
> **The argument.** The aero position is the only option that can win the Tour at all. The question is how much power loss the tuck can tolerate.
> 
> - **Speed.** A is faster than B whenever y < x. That covers about 86% of the sensitivity rectangle.
> - **Reaching 50 seconds.**
>   - At b = 1.0000, A reaches the target when y ≤ 1.1% at x = 10%, 5.8% at x = 14%, and 6.9% at x = 15%. Only about 13% of the rectangle meets it.
>   - At b = 1.0109, A reaches it when y ≤ 4.6% at x = 10%, 8.8% at x = 14%, and 9.9% at x = 15%. About 39% of the rectangle meets it.
> - **Specific winning points.**
>   - At (x = 15%, y = 3%), A wins by 22 s at b = 1.0000 and by 40 s at b = 1.0109.
>   - At (x = 14%, y = 5%), A wins by 5 s at b = 1.0000 and by 22 s at b = 1.0109.
>   - Using the heaviest drag-cut point from the literature, x = 14% [S3], at y = 5% the tuck wins.
> - **The literature leans toward A.** LeMond's 54.5 km/h is well above Fintelman's 46 km/h crossover [S4].
> - **The decision rule (D4).** A has a non-zero chance of winning and B has none. If the question is "which option can win the Tour," A dominates.
> 
> **Single best sentence for A:** "At 54 km/h the literature says drag beats power loss, B cannot close the 50 seconds even at its best, and A closes it whenever the tuck costs him less power than about 1–10% depending on how much drag it saves, so A is the only option with a winning region."
> 
> **Can a competent student defend A?** Yes. The honest version is "A wins in a minority of plausible worlds, B in none."
> 
> ## Which side collapses first, and where
> 
> B collapses at the first question: "Does Full Power reach 50 seconds?" It does not, at either end of b.
> 
> - **Why a rescue fails.** The packet says Full Power names a posture, not extra effort, so a B advocate cannot rescue it by saying LeMond would push harder.
> - **What B's only rescue costs.** The only way out is to attack the stand-in (Fignon's 27:55 as a fixed time). That is outside the model, and it would also gut A's argument.
> 
> A collapses later and more softly, at the question: "What is your y, and why?" A has no measured y, so it has no source.
> 
> - At the range midpoint (x = 12.5%, y = 8.5%), A misses the target at both baselines: by 25 s at b = 1.0000 and by 7 s at b = 1.0109.
> - So an honest A advocate must say "I think A probably misses unless x is at the high end or y at the low end."
> - That is a calibrated gamble, not a collapse. It collapses outright only if the room insists on a win-probability above 50%.
> 
> ## Is either side a strawman? Could the room split evenly?
> 
> B is close to a strawman on the 50-second test. It is not one on the packet's stated primary metric, since that metric is average speed. On the primary metric B's only edge is the roughly 14% corner where y ≥ x. The argument B can make is risk-averse speed, and it is not compelling.
> 
> A is not a strawman. But it is also not strong: it wins the Tour in only about 13–39% of the range.
> 
> I expect nearly all students to land on A. The exception is a minority who adopt a worst-case-speed rule or distrust the model, and they may split off a few. A roughly even split is unlikely unless the facilitator forces maximin as the decision rule (D4 invites this).
> 
> The packet claims "the honest tension is how much power loss the position can tolerate, not a coin flip." That is true of A's internal question, but it does not make the case balanced between A and B.
> 
> **Bottom line:** the case is lopsided toward A in the choice between options. It is balanced only in the sense of how confident A deserves to be.

### Tier 3 — human dry-run
NOT RUN.

### Is the case genuinely two-sided?
No, not on the 50-second criterion, and only narrowly on speed. The sourced baseline (b 1.0000-1.0109) leaves Full Power at most about 18 s of the 50 s needed, so only Aero Bars can win the Tour. On the speed criterion the aero position is faster in about 86% of the Appendix D box (Full Power in about 14%). The tension that remains is real but lopsided: how much power loss the tuck tolerates (unmeasured), and which decision rule the room uses (best worst case favours B; best expected result and minimax regret favour A). Share of the box where each option reaches the 50 s bar: Full Power 0% at any b in range; Aero Bars 12.7% (cube law) / 9.3% (full model) at b = 1.0000 and 38.6% / 33.0% at b = 1.0109.

### Decision needed
P2 cannot be cleared by research or editing within the approved concept. Options: (1) record a human waiver and run the case as an honest "one clear favourite, how sure should you be" case (the guide already says so); (2) redesign so the conventional option has a real upside; (3) replace the concept. qa is therefore NOT set to a passing state and status stays "researched".
