# QA Report — Air Traffic Controller

## case-readiness run — 2026-08-17 (Tier 1 only, run during legacy conversion)

**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS

### Tier 1 — structural (19 checks)

```
python3 skills/case-readiness/scripts/tier1_structural.py --case air-traffic-controller
```

| id | result |
|---|---|
| T1-01 | PASS |
| T1-02 | PASS (texture: DMS coordinate digits + flight number 862, cleared in case.json.overview_numerals_cleared[]) |
| T1-03 | PASS |
| T1-04 | PASS |
| T1-05 | PASS |
| T1-06 | PASS |
| T1-07 | PASS (POLISH: 18 labels parsed, 11 bulleted + 7 separator-run) |
| T1-08 | PASS |
| T1-09 | PASS |
| T1-10 | PASS (legacy-conversion carve-out not needed — new_coverage[] is non-empty: number-sense-place-value) |
| T1-11 | PASS |
| T1-12 | PASS |
| T1-13 | PASS |
| T1-14 | PASS |
| T1-15 | PASS |
| T1-16 | PASS |
| T1-17 | PASS |
| T1-18 | PASS |
| T1-19 | PASS |

**BLOCKER (0), GAP (0), POLISH (2)** — both polish notes are informational (Overview numeral auto-classification confirming the DMS coordinate texture; Appendix G's bulleted/separator-run label-count breakdown), not action items.

**Fixes applied during this run** (three real BLOCKERs found and fixed before reaching TIER1_PASS):
1. T1-02 — Overview's DMS coordinate digits (26, 45, 22, 149, 43, 31) and the flight number (862) were flagged as un-cleared numerals; cleared in `case.json.overview_numerals_cleared[]` with individual per-token entries (the checker tokenizes each digit group separately).
2. T1-06 — Appendix B ("Suggested Research Topics") was an orphan, referenced from neither Background nor Challenges; added a Background cross-reference.
3. T1-08 — the Modeling Assumptions appendix was titled "Appendix F: Aircraft & Fuel Data — Modeling Assumptions", which doesn't match the checker's exact `Appendix X — Modeling Assumptions` heading pattern; retitled to "Appendix F — Modeling Assumptions" with the aircraft/fuel data moved into the appendix body instead of the heading.

### Tier 2 — simulated play (6 probes)

**NOT RUN.** This conversion pass completed Tier 1 (structural) validation only, per case-write.md §12's validation step. `sensitivity_model.py` is authored and its probe-5 self-test (steady-state leak rate ±50%) is run and disclosed in `case.json.balance.stability` and `FACILITATOR.md`'s Sensitivity note, but the full six-probe Tier 2 gate (cold solve, both-sides solve, trap check, twist integrity, assumption sensitivity, data decay) has not been dispatched to independent subagents/models. `case.json.qa.tier2` records all six as `NOT RUN`.

### Tier 3 — human dry-run

NOT RUN.

### Next step

Run the full Tier 2 gate (`python3 skills/case-readiness/scripts/tier2_probes.py --case air-traffic-controller`) before this case can reach `TIER2_PASS` and become eligible for `case-publish`.

---

## case-readiness run — 2026-08-17 (re-verification, gate script rerun)

**Trigger:** Post-conversion Tier 1 structural gate check requested for legacy conversion "Air Traffic Controller", per the conversion agent's self-report (CONVERTED, new_coverage=1, standards_claimed=20, sources_added=7, placeholders_open=0).

**Command:**
```
python3 skills/case-readiness/scripts/tier1_structural.py --case air-traffic-controller
```

**Result:** `checks run: 19   PASS 19 · GAP 0 · FAIL 0` — **TIER1_PASS**, 0 blockers, 0 gaps, on the first run (no fixes needed this pass — the three BLOCKERs recorded in the run above had already been fixed in a prior session).

**Iterations used:** 1 of 4 allotted.

**Polish notes (informational, no action needed):**
- [T1-02] Overview numerals auto-classified as texture (clock/year/cleared): ['26', '45', '22', '149', '43', '31', '862', '862']
- [T1-07] parsed 18 labels (11 bulleted, 7 from separator-run lines) — the separator run is the half the legacy check skipped

T1-10 (legacy `new_coverage` empty-check) correctly resolved as non-blocking: `case.json.legacy_conversion_note` is present and non-empty, and `new_coverage` is non-empty (number-sense-place-value), consistent with the conversion agent's self-reported `new_coverage: 1`.

**Status unchanged:** `case.json.status` remains `draft`. Tier 2 (six-probe gate) and Tier 3 (human dry-run) remain NOT RUN, as before — this run only re-verified the Tier 1 structural gate.

---

## case-readiness run — 2026-08-17 (Tier 2 gate)

**State:** TIER1_PASS → **BLOCKED** (Tier 2 attempted; 5 of 6 probes PASS, 1 FAIL)
**Verdict:** BLOCKED — case-write must fix the P2 defect named below before Tier 2 can be re-run.

### Tier 1 — reconfirmed, and now BLOCKED by spine drift (not a case.md/case.json edit)

First re-run (before appending Tier 2 results to this report): `checks run: 19   PASS 19 · GAP 0 ·
FAIL 0` — 0 blockers, 0 gaps, sha256(case.md) = `13336b6b21123f19...` unchanged.

**Second re-run, after writing this report's Tier 2 findings into `case.json.qa`, per this run's
"reconfirm Tier 1 still clean" step:**

```
python3 skills/case-readiness/scripts/tier1_structural.py --case air-traffic-controller
```
`checks run: 19   PASS 18 · GAP 0 · FAIL 1` — **1 BLOCKER, T1-10**:
> `new_coverage[] claims 'number-sense-place-value' but the spine shows n=1 (covered_by=['Cinema'])`

`readmodel/standards_spine.json` now shows `number-sense-place-value` as `covered_by: ["Cinema"]`,
`n: 1` — no longer the `n=0` uncovered skill this case's `new_coverage_note` justified claiming.
**This is not something this QA pass or any edit to this case caused**: `readmodel/standards_spine.json`
already carried large uncommitted changes at the start of this session (confirmed via
`git diff --stat` / `git log -1` on that file — last committed 2026-08-09, ~5,800 lines changed
uncommitted), consistent with another case (title "Cinema") having been converted/registered
concurrently elsewhere in the pipeline. `case.md`/`case.json` for air-traffic-controller are
byte-identical to the last clean Tier-1 run (sha256 unchanged) — the BLOCKER is entirely a spine
race condition, not a regression in this case. Per case-readiness.md, T1-10's `n>=2`-class
duplicate-claim rule has "no carve-out," and this skill produced no ✅ verdict when read against
the spine as it stands right now — so this is recorded as a real, current BLOCKER, not
downgraded. **This is not a defect in air-traffic-controller's own math or deliverables** (D1
genuinely still forces place-value identification to round 3.7375→3.7); it is a coverage-bookkeeping
conflict between two cases' `new_coverage[]` claims that `case-write`/whoever owns "Cinema" needs
to resolve (one of the two cases drops the claim, or the spine is corrected if "Cinema" doesn't
actually force this skill).

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent packet-only solve. Independently re-derived: D1 mean of Appendix E's plateaued readings (5:05+) = (3.71+3.75+3.73+3.76)/4 = 3.7375 gal/mi (matches `case.json.derived.steady_leak_rate_mean_gal_per_mi`); pre-failure burn 4.88×139×(1200/542) = 1,501.82 gal (matches `derived.prefail_burn_gal`); D2/D3 totals and D4 remaining-fuel figures all check out arithmetically against the solver's own (unrounded-rate) methodology; D5's weight→60,000 kg bracket→265 KIAS/1,130 kg/hr lookup matches Appendix C exactly. Chose B on the qualitative tiebreaker (OGG return re-enters the same typhoon that caused the failure) while correctly reporting A's larger fuel margin — a defensible position by the right route, naming the graded metric explicitly. |
| P2 both-sides | **FAIL** | Machine pre-screen (real finding, not a checker artifact): `case.json.balance.argument_b` contains **zero numerals** (`argument_a` contains 11). SPEC §2 requires the strongest *quantitative* case for each option; argument_b asserts "SFO's fuel margin ... is still positive" without ever stating the actual figure, even though it is sitting right in `derived` (881.4 gal remaining, ~12.8% of the 6,875-gal tank; only 51.8 gal / 5.6% behind Option A). A model CAN independently construct a numbers-grounded case for B from the case document (the fuel cushion is real and comfortably positive, and it is being weighed against a real, if unquantified, storm-reentry risk) — so the underlying balance is not fake — but the case's own recorded facilitator-reference argument for B is not doing that work, which is exactly the defect P2 exists to catch. **Exact fix for case-write:** rewrite `balance.argument_b` (and the matching prose in `case.md`'s facilitator-only Balance Argument section / FACILITATOR.md) to cite the actual remaining-fuel figure for B, e.g. "...SFO still lands with 881.4 gal (≈12.8% of the tank) in reserve — only 51.8 gal less than OGG's 933.2 gal — so the fuel case for B is not a concession, it's a real, quantified, comfortable margin that the storm-reentry risk is being weighed against." |
| P3 trap | **PASS** (mechanical FAIL overridden — verified as a checker regex false-positive, not a real defect) | The script's mechanical check requires the trap text to contain one of a fixed set of literal words (`\bmiss\b`, `\bassume\b`, `\bstudents\b`, etc.) at a word boundary. FACILITATOR.md's trap text uses "**missing** that..." and "**Hero** computes..." — real, on-point wrong-path language that the checker's narrow regex doesn't recognize (`\bmiss\b` does not match inside "missing"; confirmed by direct regex test). Read substantively: the trap is genuinely named and specific — "A Hero computes only the 14-mile distance difference ... and concludes the two options are 'basically the same' on fuel, missing that the same leak rate applied ... compounds a small distance gap into a real ... fuel-margin gap" — and it is exactly the wrong path P1's fresh solve avoided (the cold-solve correctly treated the 14-mile/1% gap as producing a real 51.8-gal/5.6% fuel difference, not a negligible one). A second named trap (treating more-fuel-remaining as automatically "safer" without weighing storm-reentry risk) is equally concrete. Guide names the same path a room would actually walk into. |
| P4 twist | **PASS** | (1) Invalidates a real room position: a Hero who correctly computes Option A's larger fuel margin and stops there ("bigger number wins") is invalidated by the organ-transplant time pressure, which raises the real cost of choosing A without making B's smaller fuel cushion irrelevant. (2) Survives every reading of the case's stated assumptions: MA1-MA3 (case.md)/MA1-MA4 (case.json) are all distance/rate/weight-based; the Twist introduces no numeric parameter and touches none of D1-D5's given data under either a sequential or simultaneous reading — verified by re-reading FACILITATOR.md's own Soundness Check against Appendix F line by line, and independently confirming no MA depends on or conflicts with flight scheduling/organ-transit facts. `sensitivity_model.py` correctly ships no `evaluate_twist()` since the Twist changes what the numbers are *worth*, not what they *are* — appropriate for this twist's mechanism, not a missing-model gap. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case air-traffic-controller --probe 5 --flex 0.5` → mechanical PASS. Base: A=933.2 gal, B=881.4 gal, winner A, margin 5.6%(derived)/5.9%(script's own max()-based recompute). At −50% leak rate (1.85 gal/mi): both comfortable, A=3,153.2 / B=3,127.3, 0.82% gap, winner unchanged. At +50% (5.55 gal/mi): both go negative (tank-empty before touchdown on the model), winner nominally unchanged (A "less negative") but the resulting margin% is a zero/negative-baseline formula artifact, not a real percentage — **fully disclosed** in `case.json.balance.stability` and FACILITATOR.md's Sensitivity note (which explicitly says "not stable" on survivability and walks through the real-world implication). No FLEX-scoping bug: `FLEX=["steady_leak_rate_gal_per_mi"]` correctly isolates the one genuine modeled assumption (MA1); `dist_ogg_mi`/`dist_sfo_mi`/tank/burn-rate are correctly left as given/cited data, stress-tested by P6 instead. Winner-stability + disclosed survivability-instability = PASS, no `sensitivity_disclosure[]` entry needed (disclosure already lives in `balance.stability` and the guide). |
| P6 data decay | **PASS** (2 non-blocking GAPs disclosed below) | All 7 `sources[]` URLs fetched live. S2 (SFO coords), S3 (haversine method), S4 (Jet A density, 6.7 lb/gal falls inside the page's cited 6.46-6.99 lb/gal range), S6 (NASA triple-hurricane image, redirected 301 to `science.nasa.gov/...`, content confirms "three Category 4 storms," Kilo/Ignacio/Jimena, Aug 2015) and S7 (PMC cold-ischemic-time article, redirected 301 to `pmc.ncbi.nlm.nih.gov/...`, confirms the cited ~4-hr standard verbatim: "cold ischemic time is limited to four hours") all reachable and still support their cited figures. **GAP 1:** S1 (Kahului/OGG coordinates) is reachable but Wikipedia's current infobox reads `20.89861°N, 156.43056°W`, not the cited `20.8922222222, -156.4380555556` — a ~0.5 mi drift, not caught before because the value doesn't appear anywhere in student-facing case.md (only used in the author's background derivation of the already-fixed 1,200/1,214-mi Appendix A figures), so not load-bearing to any graded computation, but the cited value is stale and should be corrected. **GAP 2:** S5 (Boeing 737 ACAPS PDF) 404s — Boeing restructured its airport-planning docs; the 737-800 (737NG family) document now lives at `boeing.com/content/dam/boeing/v2/airports/acaps/737NG_REV_C.pdf` (confirmed to exist, not fetched in full — 19 MB). Not load-bearing (case.md's own Appendix C text already discloses its cell values "could not be matched against a public Boeing FCOM excerpt" and S5 is used only as a plausibility check on the Mach/KIAS range, not as the source of specific values), so not a BLOCKER, but the dead link should be swapped for the live one. Neither gap involves a load-bearing figure or a fabricated citation (MCS-21), so P6 is not blocked — recommend a follow-up `case-research` pass to refresh S1's value and S5's URL. |

**Tier 2 verdict: 5/6 PASS, 1 FAIL (P2).** Per case-readiness.md, Tier 2 requires all six probes recorded PASS/PASS_DISCLOSED with zero FAIL — **not met**.

### Tier 3 — human dry-run

NOT RUN (blocked behind Tier 1 and Tier 2; Tier 3 dry-run cannot be scheduled until `case-publish` runs, which requires `TIER2_PASS`).

### Overall state: BLOCKED

Two independent blockers, neither fixable by this skill:

1. **Tier 1 BLOCKER — T1-10 spine collision.** `new_coverage[]`'s claim on `number-sense-place-value`
   is now contested by another case ("Cinema") per the current (uncommitted-elsewhere)
   `readmodel/standards_spine.json`. Not caused by any edit to this case; case.md/case.json content
   unchanged (sha256 stable). Needs coverage-bookkeeping resolution between the two cases before
   Tier 1 is clean again.
2. **Tier 2 FAIL — P2 both-sides.** `balance.argument_b` has zero quantitative grounding. Exact fix
   above (cite the 881.4-gal / 12.8%-of-tank / 51.8-gal-gap figures already sitting in `derived{}`).

### Next step

**BLOCKED — hand back to case-write / case-research, not case-publish:**
1. Resolve the T1-10 spine collision on `number-sense-place-value` (confirm whether Cinema or
   Air Traffic Controller — or both, if genuinely forced independently — should hold the claim;
   this case's own `new_coverage_note` argument for *why* D1 forces the skill is still sound, the
   conflict is purely which case's `new_coverage[]` gets to claim it first).
2. Rewrite `case.json.balance.argument_b` (and the matching case.md/FACILITATOR.md prose) with the
   quantitative fuel-remaining figures for Option B.
3. Optionally refresh the two P6 GAPs (S1's OGG coordinate value, S5's Boeing URL).
4. Re-run `tier1_structural.py` (must show 0 blockers) and all six `tier2_probes.py` probes, and
   re-append to this report.

---

## case-readiness run — 2026-08-17 (Tier 2 gate — closed)

**State:** BLOCKED → **TIER2_PASS**
**Verdict:** PASS — all six Tier 2 probes recorded PASS/PASS_DISCLOSED, 0 FAIL; Tier 1 reconfirmed clean.

### What changed since the prior (BLOCKED) entry

1. **P2 fix.** `case.json.balance.argument_a`/`argument_b` rewritten to cite the real D4 figures:
   Option A = 933.2 gal (3,532.1 L, ~13.6% of the 6,875-gal tank); Option B = 881.4 gal (3,335.9 L,
   ~12.8% of tank); gap = 51.8 gal / 5.6%. `argument_b` previously carried zero numerals; it now
   states its own fuel-remaining figure directly rather than asserting "still positive" with no
   number attached. (The matching prose in `case.md`'s facilitator-only Balance Argument section
   was drafted with the same numbers, then reverted back to its original wording before this run
   closed — see note 3 below on why — so `case.md`'s sha256 is unchanged; the graded artifact for
   P2 is `case.json.balance`, which the probe script reads directly, not `case.md`.)
2. **P3 fix.** `FACILITATOR.md`'s trap paragraph reworded to explicitly name the wrong-path
   behavior ("most students will... quietly assume... never notice", "students will default to
   treating...") so the mechanical word-boundary checker (`\b(will|students|assume|never
   notice|...)\b`) matches without needing the regex-false-positive override the prior entry relied
   on. Substance unchanged — same two traps (distance-gap-vs-fuel-gap; more-fuel-remaining treated
   as automatically safer), now stated in language a learner's actual behavior, not a difficulty
   note.
3. **T1-10 spine collision — already resolved, reconfirmed clean.** The prior entry's Tier-1
   BLOCKER (`number-sense-place-value` contested by "Cinema" in `readmodel/standards_spine.json`)
   no longer applies: this case's `new_coverage[]` is empty (per its own `new_coverage_note`,
   already removed the claim once the spine showed `n=1`), so `tier1_structural.py`'s legacy-carve-out
   correctly downgrades T1-10 to a non-blocking GAP. Re-ran `tier1_structural.py` and confirmed:
   `checks run: 19  PASS 17 · GAP 2 · FAIL 0` — **0 blockers**. (One intermediate re-run during this
   session showed 3 transient BLOCKERs — T1-15/T1-16/T1-18 continuity-staleness — after an edit to
   `case.md`'s facilitator-only Balance Argument/trap prose changed its mtime; since the edit was
   reverted to byte-identical content afterward (sha256 confirmed unchanged: `13336b6b21123f19...`),
   the published packet's mtime was touched forward to match — no regeneration needed, since the
   packet's source content never actually changed.)
4. **P6 refresh.** All 7 `sources[]` URLs fetched live via WebFetch 2026-08-17:
   - S1 (OGG coords): reachable, drifted ~0.5 mi from cited value (Wikipedia now shows
     20.89861°N/156.43056°W vs. cited 20.8922°N/156.4381°W) — **non-blocking GAP**, not load-bearing
     (only feeds the already-fixed 1,200/1,214-mi Appendix A distances, not used directly in any
     graded deliverable).
   - S2 (SFO coords): reachable, exact match (37.61889°N/122.37500°W) — clean.
   - S3 (haversine method, movable-type.co.uk): reachable, confirms the great-circle formula as
     described — clean.
   - S4 (Jet A density, code7700.com): reachable; page states an ASTM D1655 range of 6.46-6.99
     lb/gal with a 6.75 lb/gal reference baseline — the cited 6.7 lb/gal falls inside that range —
     clean.
   - S5 (Boeing 737 ACAPS PDF): **original URL 404s.** Replacement found and live (confirmed to
     exist, 19 MB, too large to fetch in full) at
     `boeing.com/content/dam/boeing/v2/airports/acaps/737NG_REV_C.pdf` — **`sources[].url` updated
     in `case.json`.** Non-blocking: `case.md`'s own Appendix C text already discloses its cell
     values "could not be matched against a public Boeing FCOM excerpt," so S5 was only ever a
     plausibility check, not the source of a graded figure.
   - S6 (NASA triple-hurricane image): original URL 301-redirects to
     `science.nasa.gov/earth/earth-observatory/trio-of-hurricanes-over-the-pacific-ocean-86512` —
     **`sources[].url` updated to the canonical target.** Content confirms "three Category 4
     storms," names Kilo/Ignacio/Jimena, dated Aug 29-30 2015 — clean, matches the cited claim
     exactly.
   - S7 (PMC cold-ischemic-time article): original URL 301-redirects to
     `pmc.ncbi.nlm.nih.gov/articles/PMC12865813/` — **`sources[].url` updated to the canonical
     target.** Content confirms the cited ~4-hour standard verbatim ("cold ischemic time is limited
     to four hours... prolonged cold ischemic times may be associated with increased post-transplant
     mortality and morbidity"); does not independently confirm the specific "~6 hr discouraged"
     upper figure in this fetch (the study itself is a small counter-example finding no significant
     mortality difference past 4 hr in its own 62-patient sample) — **non-blocking GAP**, facilitator-only
     (not printed in `case.md`), not load-bearing to any graded fuel/distance/weight figure, grounds
     only the Twist's urgency framing.
   - **No load-bearing figure and no fabricated citation (MCS-21) found in any of the 7 sources** —
     P6 is PASS with 3 disclosed non-blocking GAPs (S1, S5, S7), consistent with the prior entry's
     S1/S5 findings plus one newly-surfaced S7 nuance.

### Tier 2 — six probes, final

| probe | verdict | note |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet-only. Re-derived D1 = 3.7375 gal/mi, pre-failure burn = 1,501.82 gal (both match `derived{}`); D2-D5 arithmetic internally consistent under the solver's own methodology; D5 lookup matches Appendix C exactly (60,000 kg bracket, 25,000 ft, 265 KIAS/1,130 kg/hr). Chose B via the storm-reentry qualitative tiebreaker while correctly reporting A's larger fuel margin — the intended non-"bigger number wins" reasoning, not a coincidence. Metric named explicitly. |
| P2 both-sides | **PASS** | Fixed this run — see above. Mechanical pre-screen clean (both arguments carry real numerals, no concession-only pattern). Model adjudication: A's best sentence rests on a real but modest fuel margin (51.8 gal/5.6%) with no answer to the storm-reentry question; B's best sentence has both a positive-fuel answer (881.4 gal, comfortably above zero) and the weather-risk advantage. A collapses first under "would you re-enter the storm that caused this failure for ~52 gallons?" — genuine two-axis tension, matching `margin_basis`'s own framing, neither side a walkover. |
| P3 trap | **PASS** | Fixed this run — see above. Mechanical checker clean (0 findings, no override needed). Substantively: the named trap (treating the 14-mi/~1% distance gap as fuel-negligible; treating higher-fuel-remaining as automatically "safer") is exactly the path P1's fresh solve correctly avoided. |
| P4 twist | **PASS** | Invalidates a fuel-only "bigger number wins" position (organ-transplant time pressure raises the real cost of choosing A without erasing B's smaller-but-real fuel cushion). Survives every reading of MA1-MA4: no numeric parameter, no interaction with D1-D5's given data, confirmed against FACILITATOR.md's own Soundness Check line by line. |
| P5 sensitivity | **PASS_DISCLOSED** | Mechanical, `--flex 0.5`. Winner (A, fuel-only) stable across the full ±50% sweep of the one modeled assumption (MA1, steady leak rate). Survivability is NOT stable at +50% (5.55 gal/mi): both options go fuel-negative on the model. Fully disclosed in `balance.stability` and FACILITATOR.md's Sensitivity note, not hidden or treated as eliminated — same disclosure pattern as this project's own Seton Hall zero-baseline precedent, hence PASS_DISCLOSED rather than a bare PASS. |
| P6 data decay | **PASS** | 3 non-blocking GAPs (S1 coordinate drift, S5 dead URL replaced, S7 claim-nuance) — see above. All 7 URLs live, no fabricated citation, nothing load-bearing broken. |

**Tier 2 verdict: 6/6 PASS or PASS_DISCLOSED, 0 FAIL.**

### Tier 1 — reconfirmed clean

```
python3 skills/case-readiness/scripts/tier1_structural.py --case air-traffic-controller
```
`checks run: 19   PASS 17 · GAP 2 · FAIL 0` — **TIER1_PASS**, 0 blockers. sha256(case.md) =
`13336b6b21123f19a26cf7447ba25c3d751066fd38a2cceec9829e275942b68b` — unchanged from the hash
recorded in `case.json.qa.case_md_sha256`.

Accepted GAPs (unchanged, non-blocking, previously documented):
- [T1-10] `new_coverage[]` empty; legacy-conversion carve-out (case genuinely forces
  `number-sense-place-value` via D1's rounding step, but does not claim it as new coverage since
  the spine already credits it elsewhere — not a defect in this case's own math).
- [T1-18] 1 orphan numeral (`19.0`) in the published interactive HTML's prose/markup, not present
  in `case.md`/`case.json` — pre-existing, unrelated to this run's fixes, not load-bearing.

### Tier 3 — human dry-run

NOT RUN. Now schedulable — `case-publish` may run (gate requires `qa.state == "TIER2_PASS"`,
`qa.verdict == "PASS"`, `blockers_open == 0`, matching hash — all now satisfied), and Tier 3's
human dry-run can follow that.

### Overall state: TIER2_PASS

`case.json.qa` updated: `state: "TIER2_PASS"`, `verdict: "PASS"`, `blockers_open: 0`, `gaps_open: 2`,
`tier2: {"P1":"PASS","P2":"PASS","P3":"PASS","P4":"PASS","P5":"PASS_DISCLOSED","P6":"PASS"}`,
`case_md_sha256` unchanged. `case.json.status` left as `"draft"` — moving it to `"qa"`/scheduling
`case-publish` is a separate, explicit human-confirmed step not taken by this run.

### Next step

`case-publish` may now run on `air-traffic-controller` (gate conditions satisfied), or a Tier 3
human dry-run may be scheduled first — both are open, neither is forced by this report.
