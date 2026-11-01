## case-readiness run - 2026-10-28
**State:** DRAFT -> TIER1_PASS (Tier 2 NOT complete)   **Verdict:** TIER1_PASS; not TIER2_PASS. sha256(case.md)=d9ac72ada08389b35723035807eafbf1fd71e74339309fee02c28afd89e46a3c

### Tier 1 - structural
Script verdict TIER1_PASS: 0 BLOCKERs, 2 GAPs.
- GAP T1-10: new_coverage[] empty. Reinforcement carve-out via case.json.reinforcement_note (the live spine has no skill at n=0).
- GAP T1-16: hash recorded by this run.
- POLISH: T1-15/18-24 have no published/ directory (case-publish not run, by instruction). Hover/hyperlink glossary (case.json.context_glossary[], T1-19/21) and the interactive HTML are therefore NOT built; context_glossary[] is not yet written.

### Tier 2 - simulated play
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh agent, packet only: chose B with rho_F 0.90, rho_D 0.85, w 1.20 (margin 5.7%); D1-D5 arithmetic correct, named metric. Ran before the final clarifications to case.md. |
| P2 both-sides | PASS | Both sides defensible inside stated ranges. B collapses first at "is anyone waiting for a van hour" (rho_D has no data); A is the easier default. No side needs out-of-range values for a narrow win. |
| P3 trap | PASS | Cold reader named "averages as verdict, vans half price" and the two-point D4 trend; the guide names both. |
| P4 twist | FAIL | Fresh reviewer run 2 (after run 1 fixes): arithmetic reproduces; M0 holds; but the staff note misstated M2 (cost per hour is not constant in RY2025) and per-hour vs per-dollar rho was unstated. Fixes applied to FACILITATOR.md and case.json (both rho forms, compare earlier increments, S5 provenance). Final re-run NOT RUN (concurrent-subagent limit). |
| P5 sensitivity | PASS (disclosed) | Model flips under +/-50% on rho_F, rho_D and w; all disclosed in sensitivity_disclosure[]. Script margin uses gap/loser (base 6.9%); the case convention is gap/winner (6.48%). |
| P6 data decay | PASS | Fresh agent fetched all 4 URLs live: HTTP 200, all 36 RY2022-24 cells and the RY2025 expense/hours/trips cells match. |
| P7 accessibility | FAIL | Run 1 listed ~15 minor terms and named the weighted-trip yardstick unpicturable; run 2 (after Appendix E additions) named only the access weight w as under-anchored. Added a plain statement of what w measures and a worked example; final re-run NOT RUN. Mechanical visual pre-screen needs the published HTML. |

### Tier 2 detail - P1 full solve (summary of recorded response)
D1: fixed $174.09/h, 4.698 trips/h, 574.4 h, 2,698.4 trips/$100k, 5.19 riders; vans $87.89/h, 2.218, 1,137.8 h, 2,523.7, 4.85; gap 6.5% of the larger. D2: rho_F*=0.935; break-even trips/h 4.39 fixed, 2.37 vans. D3: w*=1.069 (1.132 at the solver's own rhos). D4: D=+462.8,+160.3,-174.7; slope -318.8; RY2025 -493.5. D5: passenger-miles 34,344 vs 28,952 (A by 15.7%). Choice B at (0.90, 0.85, 1.20), tie at rho_D 0.80. Ambiguities the solver flagged (now fixed): "percent of the larger", D2 wording, how to compute passenger-miles per $100k, boardings vs rider trips.

### Tier 2 detail - P2 full solve (summary)
A: starting values, A by 4-7% with rho_D<=1, w<=1.05; passenger-miles lens 15.7%. B: rho_F 0.90, rho_D 1.0, w 1.0 gives B by 4%; or rho_F 0.85, w 1.2 gives B by 32%. B needs rho_D near 1.0.

### Tier 3 - human dry-run
NOT RUN.

### Remaining
P4 and P7 need a fresh re-run on the current files; case-context glossary and published HTML (case-publish) are not done; TIER2_PASS not reached.
