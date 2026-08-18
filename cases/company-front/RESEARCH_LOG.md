# Research Log — Company Front

`case-research`, 2026-08-12.

| # | What was needed | Searched | Found | Outcome |
|---|---|---|---|---|
| 1 | Real high school football field dimensions | "football field yard lines hash marks dimensions feet high school NFHS" | CoverSports, NFHS specs: 160ft wide, 300ft goal-to-goal, yard lines every 5yd, hashes 53ft4in from sidelines | SOURCED — S1 (HIGH) |
| 2 | Real marching-band step-size standard | "marching band 8 to 5 step size 22.5 inches standard drill design" | Wikibooks "Corps-Style Marching/Technique/Step Sizes": 8-to-5 = 22.5 in/step (heel to heel), 6-to-5 = 30.0 in/step (5 yd / 6 steps) | SOURCED — S2 (HIGH). Cross-checked against search snippets from FloMarching and the OSU Marching Band manual (not independently fetched, not cited) — all agree on 22.5 in. |
| 3 | The Block's own starting formation coordinates | N/A — proprietary/copyrighted drill-chart software output does not exist publicly for a fictional show | N/A | Authored directly (Appendix B), declared as such — same convention as Cold Chain's box-route plan and Plaza Pavers' border-cut piece |
| 4 | The Expand's scale factor (MA1) | N/A — no public drill chart for this fictional show | N/A | Set directly as a Modeling Assumption, chosen so the resulting step size sits between the two real cited ceilings (22.5in / 30in) — a genuine, realistic design choice, not derived from a specific real show |
| 5 | Counts available for the transition (MA2) | N/A | N/A | Set as a round, common phrase length (16 counts = two 8-counts); Modeling Assumption |
| 6 | Reason the 180° pivot was rejected (MA3) | N/A — internal design-team judgment call, not a claimed external fact | N/A | Realistic narrative reasoning (sightline/staging), matching the same "real or realistic" convention used for Plaza Pavers' rhombus/kite rejection |

## Margin resolution

Computed directly from real field/step-size sources and the stated scale factor (no rework cycle
needed this time — the Plaza Pavers lesson about disclosing every formula input up front was
applied from the first draft): Option A's required step size, 27.05 in/step, sits at **9.84%
headroom** under the real 30 in/step ceiling. This is a genuine threshold-vs-ceiling shape, not a
direct A-vs-B ratio (rotating a compact formation about its own center is structurally always
cheaper than a large dilation — confirmed by an independent adversarial pass, which additionally
proved Option A can never beat *any* rotation about the same center on raw travel, since this
case's (S−1)=3.4 exceeds a rotation's maximum possible travel multiplier of 2). The dilemma stays
genuine because the two options are not competing on the same axis: The Mirror Turn structurally
cannot deliver a full-field visual spread, which is the entire reason The Expand exists.

## Next step

Run `case-readiness` Tier 2 (six simulated-play probes) on `company-front`.
