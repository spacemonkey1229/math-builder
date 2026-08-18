## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 0 BLOCKERs, 1 GAP (no `case_md_sha256` yet — expected on a first run). This is the
cleanest first-pass run of any case in this session, likely because the primary-metric design
(distance from a target √N) was fully verified arithmetically (base case, twist, and both flex
directions) with Python before any prose was written, rather than after. **Final run: 0 BLOCKERs,
0 GAPs.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P5 sensitivity | PASS | Base case: A=3.24, B=2.77 distance from target → margin 14.48%, Candidate B wins. Sweep of the sole FLEX dial (MA1's 0.15 calibration buffer, ±50%) shows margin 10.09%-18.68%, no flip. This design deliberately avoided the fragility found and fixed in Survey Corner's original P5 run (target too close to the midpoint between the two candidates' anchor values) by choosing candidate √N values (11.96, 17.97) far enough apart, and a target (15.2) far enough from their midpoint (14.97), that a reasonable flex range never crosses into flip territory — checked with Python before writing any case prose, not discovered after the fact. |
| P1 cold solve | PASS | Fresh agent reached Candidate B with fully correct D1-D7 arithmetic (both factorizations, both distances, 14.48% margin), independently cross-validated its own result against Appendix D's stated ±50% sensitivity band, correctly named MA1's calibration buffer as most load-bearing, and correctly identified it as the least-supported number (an admitted "soft assumption dressed up as a precise decimal," in the agent's own words) versus S1's real NIST citation. |
| P2 both-sides | PASS | Both sides built and defended with real numbers (A: 5 vs. 7 trial divisions, a real speed argument; B: 3.24 vs. 2.77 distance, the case's own stated decision criterion). The agent explicitly distinguished "defensible with real numbers" from "defensible against the case's own decision criterion" — A's speed argument is real but answers a question the case never asked, while B's argument is both real and directly responsive to the Background section's own stated rule ("whichever candidate's actual difficulty lands closer to that target..."). Confirmed the 14.48% margin is not a paper number. |
| P3 trap | PASS | Fresh agent, reading case.md only, independently predicted the exact trap the guide names (defaulting to the "easier"/faster candidate A without checking either candidate against the stated target) before reading FACILITATOR.md. Confirmed the guide reinforces this trap across four separate sections (Anchor 2, Data Deep Dive, Socratic Q1, Deep Conflict thread 1) and separately confirmed the guide also anticipates a second-order trap (failing to recompute after the twist). |
| P4 twist | **found two real, if non-blocking, gaps, fixed, re-verified** | Fresh agent independently re-derived the twist's effect from case.md's raw numbers (not trusting FACILITATOR.md): confirmed 391 = 17×23 (verified no smaller factor exists), √391≈19.77, the flip to Candidate A, and the 29.12% twist margin, exactly. Went beyond the ask and additionally verified the flip survives the same ±50% MA1 flex applied to the twisted value (margin 26.27%-31.88%, no re-flip) — a robustness check not previously run. Found two real, non-blocking documentation gaps: (1) D7's challenge text never states the margin-formula convention in student-facing prose (only in FACILITATOR.md/sensitivity_model.py) — checked that no plausible alternative formula changes the winner in either the base case or the twist, so not a correctness issue, but a reproducibility one; (2) Appendix D/MA2's original "Elena's own authored practice numbers" phrasing was a mild retcon against the Twist's later "practice key-generator with a random seed" framing. **Fixed**: D7 now states the formula explicitly (larger distance minus smaller, divided by larger); MA2 reworded to "output by Elena's practice key-generator tool," consistent with the twist from the start. |
| P6 data decay | PASS | S1 (NIST SP 800-131A Rev 2) cross-checked against a second independent NIST publication (SP 800-57) during research; both agree on the 112-bit/128-bit and 2030 figures. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. This case is **not `VERIFIED`, only
`PUBLISHED`-eligible** — should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files a
`RUN_REPORT.md` from an actual cohort.

### Minor accepted polish note

Same informal-internal-terms note carried from every prior case in this run (Appendix D's
sensitivity column references "Tier 2 probe 5" and `sensitivity_model.py` in student-facing text) —
present here too, doesn't leak any answer or twist, flagged for the same future cross-case editing
pass rather than a one-off fix.
