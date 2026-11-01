# Concept sheet v2 — The Gap Between Fifth and Sixth (`drill-choreography`) — 2026-10-28

Revision of C1 from `CONCEPTS_drill-choreography_2026-10-27.md` after R1 round 1. Single concept. Tier T3. All numbers recomputed in Python this session (scratchpad g.py / h.py).

**Margin convention (stated once, applied everywhere):** margin = (winner's value - loser's value) / winner's value, on the primary metric.

## Sources actually fetched this session (LIVE, 2026-10-28)
- DCI 2026 World Championship Finals recap: https://www.dci.org/scores/recap/2026-dci-world-championship-finals/ . Caption totals and sub-caption (judge-level) table for ranks 4-8 were readable. Checked: Visual = (Visual Proficiency + Visual Analysis + Color Guard)/2; Music = (Brass + mean of the two Music Analysis scores + Percussion)/2; GE = (sum of four GE judge scores)/2. The 6th-place row's components sum to 94.1375 (DCI prints 94.137).
- DCI 2025 World Championship Finals recap: https://www.dci.org/scores/recap/2025-dci-world-championship-finals/ . Caption totals and sub-captions for ranks 5-9 readable; GE+Visual+Music = Total for ranks 5-9.
- DCI 2026 final-scores page: https://www.dci.org/scores/final-scores/2026-dci-world-championship-finals/ . Shows ranks 4-8 totals only (no captions this fetch).
- Rights note: dci.org content is all-rights-reserved. This case therefore does NOT reproduce any recap table, does NOT name corps or judges, and does NOT quote judge sheets. The scenario scores are labeled Modeling Assumption composites (below). The DCI URL is cited only as the place students go to find real recaps.

---

### C1-v2 — The Gap Between Fifth and Sixth · tier T3 · data grade MEDIUM-HIGH (structure real, yield rates assumed and disclosed)

**Protagonist.** Constructed (disclosed): Tomasz Veldkamp, caption head for a fictional World Class corps, "Corps 6". Name not found anywhere under `cases/` (grep: 0 hits for Veldkamp and Tomasz). No real corps, person or judge is named; no invented quotes about real people.

**Story.** It is finals week. Corps 6 sits 0.900 behind Corps 5 and the director has fixed one thing: the corps has six 10-hour rehearsal blocks left (60 hours), and only one caption family gets the "emphasis" blocks (Visual or Music) because the members can only absorb one new-cleaning push before the last performance. Tomasz must choose, and defend it to a staff that is split. Ending (not a phone buzz): he writes the choice on the whiteboard in the rehearsal hall, and then writes the one number he cannot know, the yield ratio k, beneath it.

**Dilemma (binary, with a proven twist).** Option A, Visual emphasis (all six blocks across Visual Proficiency, Visual Analysis, Color Guard). Option B, Music emphasis (all six blocks across Brass, Music Analysis, Percussion). GE is excluded by rule: GE is the sum of four judge scores of the whole show's impact, it is not a caption a rehearsal block targets, and neither emphasis option can move it in a way the case can model (the case states this; it is not "ignored"). Corps 6 actually has the LOWER GE gap in the second season (see Twist), which students may notice.

**Modeling Assumptions block (every non-sourced number).**
- MA-1 Scenario scores. "Season X" and "Season Y" are composite scenarios patterned on the 5th/6th-place finals pair of two recent seasons (as of 2026-10-28), rounded and labeled as assumed values, not quoted rows. Students find real recaps at https://www.dci.org/scores/ and learn how to read one (GE, Visual, Music, and sub-captions; Visual and Music are each out of 30, built from three sub-scores out of 20 divided by 2).
- MA-2 Budget: 6 blocks of 10 hours.
- MA-3 Recovery per block: one block on a sub-caption recovers a fraction phi of that sub-caption's REMAINING headroom (20 minus current), so returns diminish. Baseline phi_V = 0.30 for Visual sub-captions (plausible range 0.20 to 0.40).
- MA-4 Yield ratio k = phi_V / phi_M, so phi_M = 0.30 / k. Baseline k = 1.00; plausible range 0.80 to 1.30. Where students source or estimate it: their own band's or team's before/after sectional data (points or rubric levels gained per hour, Visual drill cleaning vs Music ensemble work), or the earlier-season to finals score gains for any corps in the public recaps divided by the number of rehearsal days they estimate. No source is claimed for k; the case reports the break-even k instead.
- MA-5 Corps 5 does not improve during the week (frozen at the scenario scores).

**Scenario scores (all MA-1).**

| | GE | Visual | Music | Total | Gap |
|---|---|---|---|---|---|
| Season X, Corps 5 | 38.050 | 28.300 | 28.700 | 95.050 | |
| Season X, Corps 6 | 37.800 | 28.250 | 28.100 | 94.150 | 0.900 |
| Season Y, Corps 5 | 37.600 | 28.150 | 29.050 | 94.800 | |
| Season Y, Corps 6 | 37.950 | 28.050 | 28.300 | 94.300 | 0.500 |

Corps 6 sub-captions (out of 20), Season X: Visual Proficiency 18.9, Visual Analysis 18.8, Color Guard 18.8; Brass 19.0, Percussion 18.5; Music Analysis shown only as judge 1 = 18.6 (the second judge's sheet is "lost"; see the forced skill). Season Y (Corps 6): VP 18.7, VA 19.0, CG 18.4; Brass 18.7, Music Analysis mean 18.95, Percussion 18.95.

**Forced skill: missing data element given the mean.** In Season X the staff has the Music caption total (28.100) and the other Music sub-scores, but not the second Music Analysis judge. Music = (Brass + MA mean + Percussion)/2, so 56.2 = 19.0 + MAmean + 18.5, MAmean = 18.7, and MA2 = 2(18.7) - 18.6 = 18.8. Without it the student cannot build Music headroom (sub-score headroom needs the MA mean: 20 - 18.7 = 1.3). This is genuinely forced: the headroom list cannot be built otherwise.

**Primary metric.** Caption points recovered by the six-block plan = (sum of sub-caption gains)/2, where each block's gain on a sub-caption is phi x its current headroom. Secondary pass line: recovered points >= the gap.

**The arithmetic is not just two headrooms.** The best plan inside an emphasis puts each block on the sub-caption with the largest remaining headroom (greedy, diminishing returns). Season X Visual: headrooms 1.1, 1.2, 1.2; blocks go VA 0.360, CG 0.360, VP 0.330, VA 0.252, CG 0.252, VP 0.231, raw 1.785, so 0.8925 points. Students must discover that spreading beats stacking, and that the six blocks interact with phi.

**Computed (baseline phi_V 0.30, k 1.00).**

| Season | Gap | A Visual pts | B Music pts | Winner | Margin | Clears gap |
|---|---|---|---|---|---|---|
| X | 0.900 | 0.8925 | 0.9743 | B Music | 8.4% (0.0818/0.9743) | Music yes; Visual misses by 0.0075 |
| Y | 0.500 | 1.0071 | 0.8670 | A Visual | 13.9% | both clear |

Headline margin 8.4% (inside the 20% cap).

**Break-even k (Visual gain fixed, Music gain shrinks as k grows), phi_V = 0.30, 6 blocks:**
- Season X: Music wins for k < 1.118; Visual wins for k > 1.118. (Music also stops clearing the gap at k = 1.106, so for k between 1.106 and 1.118 Music is "better but still short".)
- Season Y: Visual wins for k > 0.830; Music wins for k < 0.830.
- Therefore for k in (0.830, 1.118) the correct emphasis is Music in X and Visual in Y: the choice depends on the corps' own headrooms, not the caption. Outside that band one caption wins both. This is the honest statement of what the data can and cannot decide. The old shortcut k* = Music headroom / Visual headroom = 1.9125/1.75 = 1.0926 is the single-pass (no diminishing returns, no sub-caption structure) limit; students can compare it with 1.118 and explain the difference.
- phi_V sensitivity (k = 1): at phi_V 0.20 and 0.25 neither emphasis clears 0.900 in X; at 0.30 only Music; at 0.35 and 0.40 both clear. Winner (Music in X, Visual in Y) does not change across 0.20 to 0.40; k* barely moves (X: 1.130 / 1.118 / 1.113 for phi_V 0.20 / 0.30 / 0.40; Y: 0.825 / 0.830 / 0.826).

**Twist / sensitivity.** (1) Season Y (same placement, other year, anonymized) flips the answer to Visual at k = 1. (2) Relax the director's one-emphasis rule: a mixed greedy plan over all six sub-captions recovers 1.1025 in X (k = 1) and 1.113 in Y, beating the best single emphasis by 11.6% (1.1025 vs 0.9743) and 9.5% (1.113 vs 1.0071) on the margin convention; students must ask what the single-emphasis rule is protecting (member fatigue, assumed) and whether it is worth that. (3) Let students choose k from their own data and see which side of 1.118 / 0.830 they land on.

**Thin spine skills it forces (verified to exist in `readmodel/standards_spine.json`).**
- `statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-` (n=1): back out the missing judge's score (forced, above).
- `advanced-numbers-how-to-find-the-percent-of-a-number`: phi = 30% of remaining headroom per block; k conversion to phi_M (covered elsewhere, not thin).
- Dropped: `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data`. No deliverable forces it honestly (twelve corps are not in the case; plotting would be decorative), so it is not claimed.

**Deliverables sketch.** (1) Read a recap: where do Visual, Music, GE come from (use the cited DCI URL). (2) Recover MA2. (3) Build headroom lists for both emphases. (4) Run the six-block greedy plan for A and B; state points and margin. (5) Compute break-even k in each season and state a plausible range for k with a reason. (6) Write a recommendation with the single assumption that would change it.

**Facilitator note (SPEC 6).** No illness, death, money or family-hardship stakes. Judges and real corps are not named; the real recaps are for the student's own reading.

**Data feasibility.** Structure and scale are real and student-checkable at the public DCI recaps (free, multi-season). Numbers in the case are Modeling Assumption composites. phi_V and k are not sourced anywhere; the case says so openly and reports break-even instead.

#### Footnote (item d): 98.750 vs 99.100
The 2026 final-scores page shows 98.750 for 1st place in a summary block (appearing three times) and 99.100 in the full World Class table. Not used in this case (no 1st-place data); the 99.100 value could NOT be cross-checked against the 2026 recap this session (that fetch covered ranks 4-8 only), so it is UNVERIFIED. Students who check the top of the table should expect the discrepancy and use the recap. The 6th-place total prints as 94.137 while the components sum to 94.1375 (truncation); the case uses composite totals so this does not appear.

## Fixes applied

| Review item | Fix |
|---|---|
| R1b DCI rights, real corps names | Anonymized as Corps 5 / Corps 6; composite scenario labeled Modeling Assumption; no recap table reproduced; judges unnamed; DCI URL cited as where to find recaps; recap-reading step added |
| R1a metric reduces to headroom ratio on unsourced k | k stated as a Modeling Assumption with range 0.80-1.30 and how to estimate it; metric is now points recovered over 6 blocks with diminishing returns and sub-caption allocation; break-even k 1.118 (X) and 0.830 (Y) reported; old 1.0926 explained as the single-pass limit |
| GE handling | Excluded by stated rule with reason |
| "Missing data element" not forced | Forced: back out the second Music Analysis score from the Music caption total (MA2 = 18.8) |
| Box-and-whisker | Dropped, not claimed |
| 94.138 vs 94.137 | Components sum 94.1375; DCI prints 94.137; explained in footnote |
| 98.750 vs 99.100 | Footnote above; marked UNVERIFIED |
| Real seasons' contrast | Kept as anonymized Season X (favors Music) vs Season Y (favors Visual) |
| Margin convention | Gap / winner's value; headline 8.4% |
| Protagonist name | Tomasz Veldkamp, 0 grep hits in `cases/` |
| Decision shape variety | Allocation with diminishing returns plus a relaxed-rule mixed plan, not a single break-even |

## Still open
- UNVERIFIED: 99.100 (1st place) vs 98.750; the 2025 Season Y composite is built from 2025 recap rows (Phantom/Crown pattern) read this session but should be spot-rechecked; 2026 Visual/Music/GE sub-scores read once via WebFetch summarizer.
- phi_V = 0.30, k, the 6-block budget, and the one-emphasis rule are assumptions with no source (flagged, not hidden).
- R1b to decide whether even rounded composite sub-captions patterned on a real 5th/6th pair are acceptable under the rights notice, or whether Season Y should use hand-chosen numbers.
- R1c: confirm "pass the corps ahead" stake is enough (no people stake) and that the whiteboard ending is distinct from the phone-buzz endings.
