## case-readiness run — 2026-08-31

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Before Tier 1: `preflight_lint.py --case the-transfer-window` → clean, no advisory findings.

### Background — why this case was re-opened

`RESEARCH_LOG.md`'s "RETUNE PASS — 2026-08-31" left this case researched, structurally sound, and
untouched: `margin_pct = 15,940.5%` (Option A, the Direct Burn, wins by roughly two orders of
magnitude), confirmed structural (not a modeling artifact — chemical vs. electric propulsion
inherently differ by ~800x in transit time due to real thrust-technology physics, only ~5x in
payload-mass advantage) and left shelved pending a human decision, since at the time no
BLOCKER-level-safe path existed to ship a case this far outside SPEC §2's ~20% balance cap.

The project has since adopted **MCS-46** (`DOCTRINE_LEDGER.md`), a narrow, per-case,
project-owner-approved exception letting a real, honestly-researched landslide margin ship if (1)
the problem setup still forces genuine multi-step analytical work and (2) the *size* of the gap is
a real surprise a student can only discover by computing it, not something guessable from the
premise alone — first applied to the sibling case The Phasing Call. Judgment call made this
session: The Transfer Window meets both prongs. D1–D6 require real parametric-equation setup,
rectangular-equation elimination with a solved intercept check, rocket-equation propellant-mass-
fraction arithmetic, a kg/day ratio, and a radiation-dose unit-conversion check — not a plug-and-
chug exercise. And while the premise supports the well-known qualitative fact that chemical
propulsion is faster and electric propulsion is more propellant-efficient, it does not support the
specific magnitudes: a plausible naive intuition ("a much-more-efficient electric engine should
bank enough extra payload to be worth its extra months in transit") is actively wrong, and only
computing the real ~815x transit-time asymmetry against the real ~5x payload-mass asymmetry reveals
that the two are nowhere near the same order of magnitude — which is itself the pedagogical payoff.

Applied: `case.json.balance_test_waiver` added (ledger_ref MCS-46, approved_by "project owner,
2026-08-31 session"). `FACILITATOR.md` rewritten from scratch on the `cooling-curve`/`the-phasing-
call` structural template — full anchor ladder (Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/
Immediate recommit/Deep conflict/45-minute plan/The trap/Socratic questions/Close/Lessons Learned/
Standards Touched On), with 5 Socratic questions and a Twist probing *why* the two propulsion
technologies differ by such different orders of magnitude on mass vs. time, what the rocket
equation actually predicts, and what a real mission planner would weigh — not "which side wins."
Authored `sensitivity_model.py` (rocket-equation-based, reproduces the case's own 133.0/63.7 kg
propellant figures exactly). Added `case.json.reinforcement_note` (empty `new_coverage[]` carve-
out — every claimed Pre-Calc/Parametric skill is already `n=1`/`covered_by=['Feedback']`, and every
other Pre-Calc group is already `n>=1`, so no adjacent skill this case's real deliverables could
claim exists) and `case.json.cohort_bands[]` (3 bands).

### Tier 1 — structural (20 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview, no load-bearing numerals |
| T1-03 | PASS | binary dilemma, opens "You are Talia Brooks." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-G, no orphans |
| T1-07 | PASS | Appendix G labels parsed (7 bulleted) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | GAP | margin 15,940.5% — MCS-46 waiver on file, four required keys present, downgraded per doctrine |
| T1-10 | GAP | new_coverage[] empty — reinforcement carve-out, `reinforcement_note` present and checked |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier/numeric load consistent |
| T1-13 | PASS | facilitator guide, anchor ladder, 5 Socratic questions, Twist, timed plan |
| T1-14 | GAP | continuity — 2 guide-only rounded figures (100, 160) with no exact-form home in case.json; both are restatements of `case.json.balance.margin_basis`/`derived.facilitator_ratio_terms_note`, not stale values (see note below) |
| T1-15 | PASS | no published/ artifacts yet, nothing to drift |
| T1-16 | PASS | `case_md_sha256` recorded and current (this run) |
| T1-17 | PASS | cohort_bands[] declared |
| T1-18 | PASS | no published/ dir, nothing to check |
| T1-19 | PASS | no published/ dir, nothing to check |
| T1-20 | PASS | advisory, never blocks |

**BLOCKER (0).**

**GAP (3, all accepted/expected):**
* T1-09 — margin 15,940.5% waived under MCS-46 (`case.json.balance_test_waiver`, `DOCTRINE_LEDGER.md`).
* T1-10 — empty `new_coverage[]`, reinforcement carve-out per `case.json.reinforcement_note` (every
  Pre-Calc skill in the spine is already `n>=1`; nothing adjacent for this case's real deliverables
  to legitimately claim).
* T1-14 — orphan-number sweep flags `100` (a `×100` in a percent formula, not a substantive figure)
  and `160` (the rounded ~160x headline ratio, whose exact form 160.5x/76.9÷0.479 already lives in
  `case.json.balance.margin_basis` and `derived.facilitator_ratio_terms_note`). Cosmetic; no drift.

**POLISH (5):** T1-07 (separator-run parsing note), T1-15/T1-18/T1-19/T1-20 (no `published/`
directory yet — expected pre-publish).

`VERDICT: TIER1_PASS (0 blockers, 3 gaps)`. `case_md_sha256` recorded and current (below).

`case_md_sha256` (this run): `58cc1619eea33d7cb09a78249152a335fb0891a10db1f7b711124308b742e325`

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen: 2 probes FAILED mechanically on first pass, both fixed this session —
`case.json.balance.argument_a`/`argument_b` were rewritten with real digits (were prose with fewer
than 3 numerals each, tripping P2's "almost no numbers" screen), and `case.json.sensitivity_
disclosure[]` was added for the four genuine stated Modeling Assumptions the sensitivity model
flexes (MA1 delivery window, MA3 Patient Drift transit time, MA4 dry mass, MA5 dose rate),
resolving P5's mechanical FAIL to `PASS (disclosed)`. Re-run after fixes: 0 probes failed
mechanically.

Two further real findings surfaced by the adjudication subagents and fixed this session:
`case.md`'s D4 deliverable pointed to "your D2 transit-time figures," but D1/D2 (parametric setup
and parameter elimination) never produce a transit-time figure — corrected to point to "each
option's stated transit time in Appendix B." And Tier 2 probe 6 found the previously-cited NAIF
`geophysical.ker` kernel file does not literally contain the cited GM value 398,600.4418 km³/s²
(it lists 398600.8 for WGS72 and 398600.5 for WGS84 instead) — a live-but-drifted citation, fixed
by re-sourcing S6 (and S12/S13's derived-from-S6 url) to a live Wikipedia page confirmed to state
the WGS84-adopted value verbatim.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh, genuinely blind subagent (packet-only, no FACILITATOR.md/case.json/RESEARCH_LOG.md access) independently derived its own parametric equations (x(E), y(E) with b=17,030 km, ae=17,642.9 km), eliminated the parameter to the rectangular form, solved the apoapsis/periapsis intercept checks against both the 42,164 km and 6,878 km real radii, ran the rocket equation for both options (reproducing 133.0/63.7 kg propellant, 17.0/86.3 kg deliverable payload), computed D4 (76.9 vs 0.479 kg/day, a ~160x gap it flagged as "matches Appendix E's own stated '~160x gap,' a nice internal consistency check") and D5's radiation dose, chose Option A, named kg/day as the optimized metric, correctly identified MA3 as the assumption its answer is most sensitive to (and confirmed by its own arithmetic that even halving MA3 leaves the gap two orders of magnitude wide), and named MA4 (dry mass) as the least-supported figure. Reached the right answer by the right route, with its own work shown. |
| P2 both-sides | **PASS** | Both `case.json.balance.argument_a`/`argument_b` are real, independently quantitative arguments built from the case's own appendix figures (A: 0.221 vs 180 days, ~815x, 76.9 kg/day, comfortably inside the 240-day window; B: 6.0 vs 3.82 km/s delta-v, 1,400 vs 290 s Isp, 63.7 vs 133.0 kg propellant, 86.3 vs 17.0 kg payload, a real ~5.1x mass advantage). Argument B does not collapse into a bare concession — it has real numbers and a real, defensible partial case (more payload, still comfortably inside the contract window and radiation tolerance) right up until D4's own division is actually performed, at which point the ratio construction (not a hand-wave) is what decides it. This is the expected shape for an MCS-46-waived landslide case, not evidence of fake balance. |
| P3 trap | **PASS** | Independent subagent, reading `case.md` only, named the trap as: students correctly compute D2 (fast transit) and D3 (more payload for B) but treat them as two separate, additive-feeling "wins" instead of completing D4's required division — "a category error: conflating a quantity advantage with a rate advantage." Compared against `FACILITATOR.md`'s "The trap" section afterward: found the guide names essentially the same failure, split into the same two framings (the equal-weighting intuition, and stopping before actually running D4's division) the subagent had already folded into one description. Assessed the guide's two-tier structure as better suited to catching students at whichever stage they stall, not a different or missed trap. |
| P4 twist | **PASS (after remediation)** | Independent adversarial subagent confirmed the twist's core claim (a ~5x term and an ~815x term compound to ~160x rather than partially canceling) survives every natural reading of MA1, MA3, MA4, and MA5 it could construct — including hand-extending the sensitivity model to a halved MA3 (90 days), which still leaves an ~80x gap. It also stress-tested MA2 (same shared transfer ellipse) by asking whether a rigorous Kepler's-third-law reading would force both options to the *same* transit time (erasing the twist entirely) — confirmed numerically that a literal Kepler reading would indeed do exactly that, but found `case.md`'s own Appendix B footnote already forecloses this reading in writing ("a real continuous low-thrust transfer does not actually trace a single Keplerian ellipse at all... a stated simplification (MA2)... not a literal description of low-thrust orbital dynamics"). **Real finding, fixed this session:** the same subagent found D4's own instruction text pointed to "D2 transit-time figures," a genuine wording bug since D1/D2 never produce a transit-time figure at all — fixed in `case.md` (see above). Not a live threat to the twist itself once the wording is corrected, since Appendix B's prose (not the broken D4 cross-reference) is what actually forecloses the Kepler-equal-times reading. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` reproduces the base case closely (A=76.84 kg/day, B=0.479 kg/day, margin ≈15,931.5%, matching `case.json.balance.margin_pct`=15,940.5 to within the rounding the case's own published figures carry). Flexing the four genuine stated assumptions (MA1 delivery window, MA3 transit time, MA4 dry mass, MA5 dose rate) ±50% never flips the winner in any direction tested. The only real effects: MA1 at -50% (120 days) and MA3 at +50% (270 days) both disqualify the Patient Drift outright on the delivery-window gate (already disclosed in Appendix E's own MA1 sensitivity note); MA3 at -50% (90 days) narrows the margin to ~7,916% (still ~80x); MA4 flexed either direction shrinks or grows the margin but never closes it (already Appendix E's own documented "major lever" finding); MA5 never moves the primary metric at all, by construction (it feeds only the separate D5 pass/fail dose check). Every flexed dial "breaks the 20% cap" only because the MCS-46-waived baseline margin itself already does — disclosed via `case.json.sensitivity_disclosure[]` (Category F for MA1, Category X for MA3/MA4, Category I for MA5) per the 2026-08-13 disclosure-aware pass state, consistent with the case's own retune-pass diagnosis that no real value of any Modeling Assumption brings the margin near SPEC's ~20% cap. |
| P6 data decay | **PASS (2 findings, both fixed this session)** | Independent subagent fetched all 11 distinct source URLs. 9/11 confirmed reachable with the cited figure verbatim on the page (S1, S3, S4, S5, S7, S8, S9, S10, S11). **Two real findings, both remediated:** (1) S6's cited NAIF `geophysical.ker` kernel file does not literally contain 398,600.4418 km³/s² (it lists 398600.8 WGS72 / 398600.5 WGS84 instead) — a live-but-drifted citation, fixed by re-sourcing S6 (and S12/S13's shared url) to a live Wikipedia page confirmed (via a follow-up direct fetch) to state the WGS84-adopted 3.986004418×10¹⁴ m³/s² value verbatim in its Earth-row summary table. (2) S2's cited 180 kg wet mass and 500 km SSO parking orbit are both real, on-page figures but belong to two distinct flown Sherpa-LTC units rather than one unified spec sheet — not a fabrication (case.md never claims a single-unit configuration; it models the product line generically per Appendix A/G), but flagged with a clarifying note added to `case.json`'s S2 entry. No dead links; no BLOCKER-level failures. |

`MECHANICAL RESULT: 0 probes FAILED mechanically (after fixes).` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-transfer-window/runs/RUN_*.md` filed. Required before this case may be
marked ✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).
Schedule a Tier 3 human dry-run before any `VERIFIED` claim in the doctrine ledger.
