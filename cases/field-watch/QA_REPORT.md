## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 2 BLOCKERs (Appendix F/Modeling Assumptions never referenced by letter from Background —
a genuine mislabel, Background's closing paragraph said "APPENDIX D" where it meant "APPENDIX F";
SPEC §6 triggered by "dying wheat" in the Overview, a crop-stress metaphor, not personal
hardship — required an explicit sensitivity note rather than being auto-cleared) plus 3 GAPs
(standards[] claimed 2 already-covered reinforcement skills — percent, subtract-with-negative-numbers
— absent from the final appendix's spine-label list; FACILITATOR.md contained 2 numbers (0.06, 0.176,
the intermediate distribution constants) absent from case.json's number universe; no
`case_md_sha256` yet). All resolved: the Appendix D→F mislabel fixed; a one-line sensitivity note
added (professional/economic stakes, not personal hardship); Appendix G expanded to the full
two-part list; the 2 missing numbers added to `case.json.derived`. **Final run: 0 BLOCKERs, 0
GAPs**, held clean through two further rounds of content strengthening (the balance-argument fix,
the P4/P2 bonus-insight additions).

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P5 sensitivity | PASS | Base case: A=7.0, B=8.0 days buffer → margin 14.29%, Model B wins. Sweep of the sole FLEX dial (`calib_margin`, MA1's ±50%) shows margin 12.02%-17.09%, no flip — the ceiling-collapse transform used in every prior case wasn't even needed here, since "days of buffer" is naturally higher-is-better. |
| P1 cold solve | PASS | Fresh agent reached Model B with fully correct D1-D7 algebra (distribute, combine, solve, both crossing days, both buffers, 14.29% margin), independently cross-validated its own base-case result against Appendix F's stated ±50% sensitivity band, correctly named MA1 as most load-bearing, and correctly identified the 0.03 calibration allowance as the least-supported number. |
| P2 both-sides | **found a real defensive-vs-affirmative gap, fixed, re-verified twice** | First pass: fresh agent confirmed the case technically passes a basic balance test (both options quantifiable) but characterized Option A's original argument as purely defensive ("we still clear the deadline") rather than affirmative, and surfaced a genuinely new, real fact the case hadn't used: plugging day 13 into Model A's own equation predicts NDVI 0.52, only 0.01 off Pass 3's real measured 0.51 — a legitimate out-of-sample residual check in Model A's favor. **Fixed**: rewrote Argument A around this real, quantified point (both in case.md's FACILITATOR ONLY section and case.json's `balance.argument_a`), added it as a new Socratic question, and updated FACILITATOR.md's margin note. Re-verified with a second fresh agent, which independently re-derived the arithmetic, confirmed Option A's case is now genuinely affirmative in form, and — going further than asked — found a legitimate deeper reading: reframed as a *rate* rather than an absolute NDVI gap, the 0.01 residual is actually a 9.09% underestimate of the true Pass2→Pass3 decline rate, which (given the case's own documented acceleration) would plausibly grow rather than shrink by day 19. This doesn't undermine the case's balance — it's a genuine, correct, deeper layer of the same real numbers — so it was added as a facilitator-only "sharpest possible follow-up" note rather than treated as a defect requiring further redesign. |
| P3 trap | **mechanical FAIL from an edit side-effect, fixed** | The P2 fix's added text used the word "extrapolation" before the "## The trap" heading in FACILITATOR.md; the mechanical trap-check's regex matches the bare substring "trap" (not word-bounded), so it grabbed "...ex-**trap**olation..." instead of the real trap section. **Fixed**: reworded to "a shorter forward reach past its own last data point," avoiding the substring collision. Re-ran clean; a fresh agent then independently predicted the exact same trap the guide names (defaulting to Model A on a "more data = more trustworthy" heuristic, missing the case's own documented acceleration) and confirmed the guide's secondary trap (stopping at D3/D4, skipping the D6/D7 buffer comparison) as a real, separately-anticipated risk. |
| P4 twist | PASS | Fresh agent independently re-derived the twist's effect from case.md's raw numbers (not trusting FACILITATOR.md): confirmed the corrected Pass 3 NDVI (0.54), Model B's new slope (-0.016), new crossing day (21.75), new buffer (4.25), and the flip to Model A at a 64.71% margin, exactly. Confirmed the twist's asymmetry (only Model B is affected, since Model A's raw form has no Pass-3 term) is forced by the models' own stated construction, not an unstated convention — no BLOCKER. Bonus finding, added to FACILITATOR.md: the twist also quietly reverses Appendix C's own "accelerating decline" story (post-correction, Model B's slope becomes shallower than Model A's, i.e. decelerating) — a second, independent reason Model B's original justification weakens, on top of the raw buffer numbers. |
| P6 data decay | PASS | S1 (ESA Sentinel-2 revisit) and S2 (USGS Burn Severity Portal) both fetched live 2026-08-12, same day as authoring. S1: confirmed "Sentinel-2 images the globe every 5 days," cross-checked against a second independent source. S2: confirmed NDVI/dNBR thresholding is discussed without a stated universal threshold value, consistent with the claim. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. This case is **not `VERIFIED`, only
`PUBLISHED`-eligible** — should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files a
`RUN_REPORT.md` from an actual cohort.

### Minor accepted polish note

Same informal-internal-terms note carried from every prior case in this run (Appendix F's
sensitivity column references "Tier 2 probe 5" and `sensitivity_model.py` in student-facing text) —
present here too, doesn't leak any answer or twist, flagged for the same future cross-case editing
pass rather than a one-off fix.
