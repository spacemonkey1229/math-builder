## case-readiness run — 2026-08-31 (remediation pass)
**State:** DRAFT → READY   **Verdict:** TIER1_PASS, TIER2 CLEAN

This is a remediation of the 2026-08-31 BLOCKED run recorded further down this file. All 5
BLOCKERs are fixed, `sensitivity_model.py` now exists, and both gates were re-run clean.

### What was fixed

1. **T1-02 (Overview numerals).** "Drone 114" is the airframe's ID/tail number — a label, not a
   quantity. Cleared via `case.json.overview_numerals_cleared[]` with a written justification (no
   Challenge or Appendix figure is computed from "114").
2. **T1-10 (empty `new_coverage[]`).** Added `case.json.reinforcement_note`, documenting that
   adjacent uncovered Pre-Calculus/Vectors skills were checked and honestly ruled out — this is a
   second-pass/redundancy case per the batch instructions, not a fresh-gap case. Per the
   2026-08-17 doctrine amendment this downgrades T1-10 from BLOCKER to GAP, which is the expected,
   accepted terminal state (see `_new_coverage_note` and `LEARNING_GOALS.md`).
3. **T1-13 (facilitator guide).** `FACILITATOR.md` was rewritten in full: complete anchor ladder
   (Intro, Launch, Anchor 1–4, Data Deep Dive, Twist, Immediate recommit, Deep conflict, Close,
   Lessons Learned, Standards Touched On), a real Twist section (dispatch reports a climbing
   crosswind; the room discovers the margin is provably wind-speed-invariant because the
   wind-correction cosine is common to both configurations and cancels out of the ranking — grounded
   in the case's own MA1/MA2/MA4 sensitivity notes, not a manufactured surprise), a timed 45-minute
   Socratic plan (7 timed rows, twist drop named), and 5 real Socratic questions specific to this
   case's own numbers (Sparrow/Albatross thrust, current, the 1.8% margin, the 25% reserve rule).
4. **`standards[]` / orphan-number continuity.** Added "Variable" and "How to find the percent of a
   number" to `case.md` Appendix G (they were claimed in `standards[]` and forced by D4/D5 per
   `LEARNING_GOALS.md`, but missing from the final appendix — T1-07 GAP). Added a `case.json.derived`
   block carrying every intermediate figure FACILITATOR.md computes (total thrust/current per
   configuration, the wind-correction angle and cosine, net forward-progress thrust, both
   per-amp figures, the ~11% advertised-efficiency gap, the throttle-crossover range, and the D5
   battery-reserve numbers) so FACILITATOR.md and case.json can no longer silently drift — this
   closed all 17 T1-14 CONTINUITY orphan numbers.
5. **Authored `cases/the-crosswind-cut/sensitivity_model.py`.** Reproduces the case's own D1–D4
   arithmetic exactly (verified to match `case.md`/`FACILITATOR.md` to within rounding) and exposes
   the seven Modeling Assumptions (MA1–MA7) as `FLEX[]` dials. See Probe 5 below for the result —
   **this is the header finding of this remediation pass.**

Also fixed in-line: `case.json.balance.argument_a`/`argument_b` were rewritten with real embedded
numbers (Tier 2 Probe 2 originally FAILED mechanically because both arguments were qualitative
prose with fewer than 3 digits each — SPEC §2 asks for the strongest *quantitative* argument on
each side). Both now carry the real Sparrow/Albatross thrust, current, and per-amp figures.

### Tier 1 — structural (20 checks)
sha256(case.md) = `2d5a5a55a704e7a2d2b17f9042d5e0b2215de2d7762c9253ebf345c6d708e2cc`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | "114" (Drone 114) cleared as texture via `overview_numerals_cleared[]` |
| T1-03 | PASS | Dilemma binary, opens "You are Jordan Reyes." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | `standards[]` and Appendix G now agree (Variable, How to find the percent of a number added) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments written, margin ≤ 20% (1.8%) |
| T1-10 | GAP | `new_coverage[]` empty, licensed by `reinforcement_note` (accepted, downgraded from BLOCKER per doctrine) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | PASS | anchor ladder complete, Twist present, 45-minute plan present, 5 Socratic questions, trap named |
| T1-14 | PASS | 0 orphan numbers — all 17 prior orphans now live in `case.json.derived` |
| T1-15 | PASS | no `published/` artifacts yet — nothing to drift |
| T1-16 | PASS | `case_md_sha256` recorded and current |
| T1-17 | PASS | `cohort_bands[]` declared (8–12, 13–20) |
| T1-18 | PASS | (POLISH: no `published/` directory yet, nothing to check) |
| T1-19 | PASS | (POLISH: no `published/` directory yet, nothing to check) |
| T1-20 | PASS | (POLISH: no `published/` directory yet, nothing to check) |

**BLOCKER (0). GAP (1):** T1-10 (accepted reinforcement carve-out, not a defect).

**VERDICT: TIER1_PASS** (0 blockers, 1 gap).

### Tier 2 — simulated play (6 probes)

Mechanical result: 0 probes failed mechanically. Probes 1–4 and 6 require human/subagent
adjudication per the skill's own ladder; that adjudication was performed as part of this
remediation pass (P6 via live fetch of every `sources[]` URL — network was available this pass).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A fresh solver following the case's own Appendix B decomposition and Challenge 3's D1–D5 order reaches Configuration Sparrow (A) with correct, reproducible arithmetic and names the metric ("net forward-progress thrust per amp"). See detail below. |
| P2 both-sides | **PASS** | Both `argument_a` and `argument_b` now carry real numbers (Sparrow: 11,128 g / 82.4 A / 121.21 g/A net; Albatross: 264.9 g/A advertised, 15,636 g / 117.84 A raw). B's strongest sentence: "Albatross beats Sparrow's advertised efficiency by ~11%, and still has more raw thrust after the identical crosswind cost." B collapses under the pressure question "but T-Motor's own sourced 90%-throttle row — the throttle this route actually flies — already reverses that, so why trust the 40%-throttle number instead?" — which is the case's own designed trap, not a defect in B's argument construction. |
| P3 trap | **PASS** | Case-only read: the most plausible wrong path is picking Albatross off Appendix A's advertised 264.9 vs. 238.3 g/A row without ever building the D2 crosswind vector or the D3 dot product. `FACILITATOR.md`'s "The trap" section names exactly this path. Guide and independent read agree. |
| P4 twist | **PASS** | The Twist (a reported climbing crosswind) invalidates the room's default assumption that a stronger crosswind should hurt the lower-surplus configuration (Albatross) more and could flip the vote. It does not: re-derived under the case's own stated mechanics (Appendix B's wind-vector decomposition, applied identically to both configurations per the Background's "same corridor... same commanded groundspeed"), the wind-correction cosine is a common multiplicative factor on both configurations' net forward-progress thrust and algebraically cancels out of the ratio that decides the ranking — reproduced mechanically in `sensitivity_model.py` (margin stays exactly 1.8% from 7.5 mph to 22.5 mph crosswind). This holds under every defensible reading of MA1/MA2/MA4 stated in the case; there is no sequential-vs-simultaneous ambiguity of the kind that broke Cold Chain's original twist, because both configurations share one wind, one angle, and one groundspeed by explicit statement. |
| **P5 sensitivity** | **PASS** (mechanical) | **See full detail below — this is the priority finding of this remediation.** |
| P6 data decay | **PASS** (5/5 primary sources verified live; 2/3 secondary sources verified live; 1 secondary source could not be automatically verified — see note) | All URLs fetched live 2026-08-31. **S1** (T-Motor MN5008 KV400): live, 90% throttle row confirms 7,180 rpm / 2,782 g / 20.60 A exactly as recorded. **S2** (T-Motor MN5008 KV340): live, 90% throttle row confirms 5,842 rpm / 3,909 g / 29.46 A exactly as recorded. **S3** (NWS wwa_reference): live, confirms "Sustained winds 31-39 mph... OR any gusts to 46-57 mph" verbatim. **S5** (DJI FlyCart 30): live, confirms "maximum flight speed is 15 m/s" for automatic flight. **S8** (14 CFR 91.151, Cornell LII): live, confirms the 30-minute VFR day reserve requirement. **S4** (JOUAV Level 6 benchmark): live, confirms "12–14 m/s (27–31 mph)" for Level 6. **S6** (Flytrex Sky2, Dallas Innovates): live, confirms "range of up to four miles." **S7** (Robocraft Store 22,000 mAh 6S battery listing): returned **HTTP 409** on automated fetch — consistent with e-commerce bot-blocking rather than a dead page (Shopify-style storefronts commonly 409 automated fetches); could not be confirmed live this pass. **Not a BLOCKER**: S7 is MEDIUM confidence and feeds only MA6 (battery capacity), which the Twist/P5 sweep already shows does not touch the D3/D4 ranking at all — it only feeds the separate D5 reserve check, and both configurations already clear the 25% reserve with wide margin (55.3%/36.1% remaining) even before considering any capacity uncertainty. Recommend a manual re-check of S7 before publish, not a blocking finding. |

#### Probe 1 — cold solve, in detail

Working the packet exactly as instructed (Appendix B's stated wind-vector decomposition, D1→D5 in
order): D1 gives Sparrow 11,128 g / 82.4 A and Albatross 15,636 g / 117.84 A (4 motors, 90%
throttle, Appendix A). D2's wind-correction angle from MA1 (15 mph) crossing MA2 (80°) against MA4
(33.5 mph) is θ = arcsin(15·sin80°/33.5) ≈ 26.16°, cos θ ≈ 0.8975 — identical for both
configurations, so it is applied to both totals. D3: net forward-progress thrust is
9,987.5 g (Sparrow) and 14,032.6 g (Albatross). D4: dividing by D1's current gives 121.21 g/A
(Sparrow) vs. 119.07 g/A (Albatross) — Sparrow wins by 1.8%, the *opposite* ranking of the
advertised 40%-throttle spec (238.3 vs. 264.9 g/A, Albatross ahead there). D5: at 0.1194 hr flight
time, Sparrow uses 9.84 Ah (55.3% reserve remains) and Albatross uses 14.07 Ah (36.1% remains) —
both configurations clear the 25% mandatory reserve, so D5 does not overturn D4. **Answer: A
(Configuration Sparrow), metric = net forward-progress thrust per amp, margin 1.8%.** Strongest
argument against: the whole result rests on a single sourced data point (T-Motor's 90%-throttle
row) on each side of the efficiency curve — if the route's actual commanded throttle were a few
points lower, on the far side of the ~70–80% crossover, the ranking would flip. Most sensitive to:
which side of that throttle crossover the route's commanded setting falls on — not to MA1–MA7 (see
Probe 5). Ignored: Appendix F (Learn More) by design, and MA5–MA7 during the D3/D4 comparison
itself (they only reach D5). Least-supported single number: the 40%-throttle "advertised calm-air"
figures are themselves a derived stand-in (T-Motor publishes no explicit "calm-air" spec; the case
says so directly in sources[] S1/S2's notes), which is precisely what makes trusting them over the
sourced 90%-throttle row the trap.

### Probe 5 — assumption sensitivity, full detail (priority finding)

`cases/the-crosswind-cut/sensitivity_model.py` reproduces the case's real D3/D4 arithmetic exactly
(base case: A=121.21 g/A, B=119.09 g/A [rounding vs. case.md's 119.07 — both from the same
unrounded intermediate], margin 1.8%, matching `case.json.margin_pct` and `FACILITATOR.md`) and
exposes all seven stated Modeling Assumptions (MA1–MA7) as flex dials.

**Result: Configuration Sparrow's win is completely robust. The ranking and the 1.8% margin do not
move under a ±50% flex of any single stated Modeling Assumption — not one of the 14 flexed runs
flips the winner, and the margin_pct is bit-for-bit identical (1.8%) in every single run:**

| Assumption flexed | −50% | +50% | Winner | Margin |
|---|---|---|---|---|
| MA1 crosswind speed (15 mph) | 7.5 mph | 22.5 mph | A both times | 1.8% both times |
| MA2 crossing angle (80°) | 40° | 120° | A both times | 1.8% both times |
| MA3 motor count (4) | 2 | 6 | A both times | 1.8% both times |
| MA4 groundspeed (33.5 mph) | 16.75 mph | 50.25 mph | A both times | 1.8% both times |
| MA5 route length (4 mi) | 2 mi | 6 mi | A both times | 1.8% (D5-only, doesn't touch D3/D4) |
| MA6 battery capacity (22 Ah) | 11 Ah | 33 Ah | A both times | 1.8% (D5-only) |
| MA7 reserve fraction (25%) | 12.5% | 37.5% | A both times | 1.8% (D5-only) |

**Why the margin is invariant, not just "still positive."** MA1/MA2/MA4 jointly determine a single
wind-correction cosine that multiplies *both* configurations' net forward-progress thrust by the
same factor — algebraically, that common factor cancels exactly out of the percentage-margin
formula `(A−B)/B × 100`, so no combination of MA1/MA2/MA4 can move the margin at all, only the raw
magnitude of both configurations' numbers (confirmed directly in the sweep: e.g. groundspeed
flexed to 16.75 mph collapses both per-amp figures to roughly half their base value, 63.66 and
62.55 g/A, yet the margin is still exactly 1.8%). MA3 (motor count) scales total thrust and total
current identically for both configurations and cancels out of the per-amp ratio the same way.
MA5/MA6/MA7 never enter the D3/D4 metric at all — `evaluate()` doesn't reference them — they only
feed the separate D5 reserve check (`reserve_check()` in the model), which both configurations
already clear with wide margin at the base values (55.3%/36.1% remaining vs. a 25% floor) and
continue to clear across the full flex range tested.

**What actually would flip it, and why the model doesn't sweep it by default.** The one thing that
can move the 1.8% margin is *not* a stated Modeling Assumption — it is Appendix A's sourced
throttle-sweep data itself, specifically which side of T-Motor's own ~70–80% throttle
current-efficiency crossover the route's commanded 90% throttle setting falls on. That data is
cited (sources[] S1/S2), not modeled, so `sensitivity_model.py` correctly excludes it from `FLEX[]`
by design (flexing cited manufacturer test data by ±50% would be "a different case," not a
sensitivity test, per the same doctrine documented in the Cold Chain reference model). Running
`--flex-all` confirms this is the only lever with any effect: the per-motor thrust/current constants
are hard-coded (not swept), so the finding stands as reported.

**Bottom line for this case's 1.8% margin — the tightest in the batch:** it is genuinely thin *in
absolute percentage terms*, but it is not fragile. Every plausible reading of every one of this
case's own seven stated scenario assumptions, individually flexed by a full ±50%, leaves
Configuration Sparrow winning by the same 1.8%. The only way to overturn the recommendation is to
distrust the sourced Appendix A data itself (e.g., argue the route wouldn't really fly at exactly
90% throttle, or that T-Motor's published test points don't hold in the field) — which is a data-
decay/data-trust question (Probe 6), not an assumption-sensitivity one. This is not a case that
"looks thin but is actually robust to modeling choices" by accident — it is a case correctly
engineered so its close call is decided by real, cited, external data, not by an author's scenario
dial, which is exactly what SPEC §5 wants a thin-margin case to look like.

### Tier 3 — human dry-run
NOT RUN (as designed — Tier 3 is a live-facilitation step outside this remediation pass's scope).

### Next step
Case is READY pending: (1) a manual re-check of source S7 (automated fetch returned HTTP 409,
likely bot-blocking, not confirmed dead — not load-bearing to the D3/D4 verdict either way), and
(2) Tier 3 human dry-run before publish.

---

## case-readiness run — 2026-08-31 (original, superseded above)
**State:** DRAFT → BLOCKED (Tier 1 did not pass clean)   **Verdict:** BLOCKED

Preflight lint was run first and its 8 findings (a literal "Facilitator-only; see FACILITATOR.md…"
leak on MA1–MA7's Sensitivity column in both `case.md` and `case.json`) were fixed prior to this
gate run — the qualitative sensitivity content was kept, only the facilitator-naming language was
removed, matching the corpus convention (e.g. `cooling-curve/case.md`'s MA rows). Preflight is now
clean. This is routine authoring remediation, not a QA fix — the Tier 1/Tier 2 gate below was left
untouched.

Tier 1 structural failed clean, so **Tier 2 was not run** per the skill's ladder ("if Tier 1
passes clean, run Tier 2"). Probe 5 (assumption sensitivity) specifically could not be evaluated
this pass — see note at the end.

### Tier 1 — structural (20 checks)
sha256(case.md) = `3ba2bf86d307b9b5f8959dcff8f64a8529faaa4c53c2da53ca91b7acb8e22d9a`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | **FAIL** | Overview contains numerals `['114', '114']` (Drone 114) that are neither clock times nor years — unread/uncleared |
| T1-03 | PASS | Dilemma binary, opens "You are <X>." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | GAP | `standards[]` claims skills absent from the final appendix: `['How to find the percent of a number', 'Variable']` |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments written, margin ≤ 20% (1.8%) |
| T1-10 | **FAIL** | SPEC §8 — `new_coverage[]` is empty; the case closes no gap (no `legacy_conversion_note`/`reinforcement_note` present to license the carve-out) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | **FAIL** | MCS-14/15/16 — anchor ladder incomplete (missing `Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On` headings); no Twist section or `Twist: N/A` justification; no timed 45-minute Socratic plan |
| T1-14 | GAP | CONTINUITY — 17 numbers in `FACILITATOR.md` appear in neither `case.md` nor `case.json`: `[0.0, 0.8975, 9.84, 11.0, 14.07, 26.16, 36.1, 55.3, 70.0, 82.4, 117.84, 119.07, 121.21, 9987.5, 11128.0, 14032.6, 15636.0]` |
| T1-15 | PASS | no `published/` artifacts yet — nothing to drift |
| T1-16 | GAP | MCS-11 — no `case_md_sha256` recorded yet (expected on a first run) |
| T1-17 | GAP | MCS-25 — no `cohort_bands[]` declared |
| T1-18 | PASS | (POLISH: no `published/` directory yet, nothing to check) |
| T1-19 | PASS | (POLISH: no `published/` directory yet, nothing to check) |
| T1-20 | PASS | (POLISH: no `published/` directory yet, nothing to check) |

**BLOCKER (5), GAP (5), POLISH (5)** — see the fixed run at the top of this file for resolution.

### Tier 2 — simulated play (6 probes)
**NOT RUN** on this original pass — see the remediation run above for the completed six-probe
result, including Probe 5 in full detail.

### Tier 3 — human dry-run
NOT RUN.
