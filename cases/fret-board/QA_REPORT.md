## case-readiness run — 2026-08-27 (P5 disclosure remediation — TIER2_PASS)

**State:** TIER2_PASS   **Verdict:** TIER2_PASS (all six Tier 2 probes now PASS or PASS (disclosed); Tier 1 clean, 0 blockers, 1 pre-approved GAP)

### What changed this pass

The prior run (below, "Tier 2 full adjudication") found P5 FAIL: `sensitivity_model.py` showed the
4.2% total-shop-time margin flips from Option B to Option A if MA4 (`calc_seconds_per_fret_a`,
Precision Method) runs ~50% faster (10s vs. 20s) or MA5 (`calc_seconds_per_fret_b`, Rule of
Eighteen) runs ~50% slower (21s vs. 14s). MA6 does not flip it at either bound. This instability
was real and undisclosed. Per skills/case-research/SKILL.md ("The Sensitivity column is mandatory
for any assumption that can flip the dilemma") and this project's established pattern (disclosure
over retuning, mirroring `enclosure-call`'s equivalent P5 handling), the fix applied was
**disclosure, not retuning** — the ±50% flex range itself is reasonable for these two dials (both
are explicitly "reasoned scenario estimate[s], not discovered fact[s]" per their own `basis` text;
no published source times either task, so a ±50% swing in a hand/calculator timing guess is not an
unreasonable band to test).

Changes made:
1. **`case.json.sensitivity_disclosure[]` (new top-level array)** — two entries, `calc_seconds_per_fret_a`
   and `calc_seconds_per_fret_b`, both Category **X** (proprietary/inaccessible one-time exception:
   the true value exists in principle — a real apprentice's timing is measurable — but is not
   publicly documented, so the stated value is a good-faith estimate from the closest analogue),
   each with a justification ≥20 chars naming the exact flip point and the verification method
   (`sensitivity_model.py` / `tier2_probes.py --probe 5 --flex 0.5`).
2. **`case.json.modeling_assumptions[]` MA4/MA5 `sensitivity` fields** — rewritten to state the
   flip honestly (direction, rough magnitude, "disclosed, not eliminated") instead of the prior
   vague "the comparison is sensitive to this value."
3. **`case.json.balance.margin_note`** — corrected. The prior note claimed the margin was
   "deliberately robust, not fragile" based on a check that only tested the *widening* direction
   (doubling MA4). That check was real but one-directional and is now labeled as such; the note now
   states the actual ±50% flip finding and points to `sensitivity_disclosure[]`.
4. **`case.md`'s Modeling Assumptions table (MA4/MA5 Sensitivity column)** — added the same honest
   flip disclosure in student-facing language ("the total-shop-time comparison ... may flip toward
   the Precision Method"). **Caught and fixed a leak in this step**: an earlier draft of this edit
   included the literal `4.2%` margin figure in case.md, which `tier2_probes.py`'s P1 leak-check
   correctly flagged (`balance_test.margin_pct = 4.2 appears in the packet`) — removed the numeral,
   kept the qualitative "close"/"does not take much to move it" framing, re-verified P1 goes READY.
5. **`FACILITATOR.md`** — added a corrected paragraph to the top retune-history note; added a
   dedicated "Facilitator note — assumption sensitivity (Tier 2 probe P5)" section (distinct from
   the existing SPEC §6 personal-stakes sensitivity note, which is unrelated and untouched); added
   a 4th "Deep conflict" thread ("The time race is thinner than it looks") and a 6th Socratic
   question, both framed so a Hero challenging MA4/MA5 is treated as intended pedagogy, not a
   defect to deflect.

No numbers were invented; all figures used (10s, 21s, the flip mechanics) come directly from
`sensitivity_model.py`'s existing, unchanged arithmetic.

### Re-run: `sensitivity_model.py`

```
base totals (minutes)  {'A': 52.33, 'B': 50.13} winner B margin -4.2%
```
Unchanged from before — the model itself was not altered, only what the case discloses about it.

### Tier 1 — structural (20 checks), re-run 2026-08-27

`python3 skills/case-readiness/scripts/tier1_structural.py --case fret-board`

**PASS 19 / GAP 1 / FAIL 0. sha256(case.md) = 49798749577b3cb65f67ac2135d5b0a6c45dfdb1812750e354ca16514914d353**
(new hash — case.md changed this pass: MA4/MA5 Sensitivity column text). T1-16 (QA hash) now current.
Same single pre-approved GAP as always: T1-10 (reinforcement carve-out, untouched).

### Tier 2 — simulated play (6 probes), fully re-adjudicated

`python3 skills/case-readiness/scripts/tier2_probes.py --case fret-board` (plus `--probe 5 --flex 0.5`
and `--probe 1` individually) re-run for real this pass, all six genuinely re-adjudicated (not
carried forward from the prior pass, since case.md/case.json changed).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a fresh subagent with no access to `case.json`/`FACILITATOR.md`/`QA_REPORT.md`, only the (now leak-free) `/tmp/coldsolve-fret-board/PACKET.md`. Chose **Option A**, with correct arithmetic (A=52.33 min vs B=50.13 min; B's 12.5-cent deviation is 2.5× the 5-cent MA1 tolerance), named its metric explicitly (expected/risk-weighted time, not raw time), named **MA1** as the assumption its answer is most sensitive to, and named MA6 as the least-supported number (S5's MEDIUM-confidence, single-example sourcing) — all independently derived, matching this case's own designed tension. Note: this run also caught and fixed a real P1 leak (see "What changed" above) before dispatching the blind solver. |
| P2 both-sides | **PASS** | Built the strongest case for each option independently. Neither collapses to a bare concession — B's identified weak point (MA1's soft 2–6 cent sourcing being treated as gospel) is a specific arguable pressure point, not a surrender. |
| P3 trap check | **PASS** | Independently derived trap ("small in inches read as small in cents, skipping the D3 log conversion") matches `FACILITATOR.md`'s "The trap" section closely, reinforced by Anchor 2, the Data Deep Dive cold-call, Deep Conflict thread 2, and Socratic Q3/Q4. |
| P4 twist integrity | **PASS** | The twist (shop's setup log / bridge-saddle compensation) genuinely unsettles the post-Data-Deep-Dive stance of flatly rejecting B on tolerance alone. Checked against every stated Modeling Assumption (MA1–MA6) under a natural reading — none of them create a Cold-Chain-style hidden-convention dependency; MA6 explicitly excludes downstream setup/compensation work, so there's no double-count or contradiction. |
| P5 sensitivity | **PASS (disclosed)** | `tier2_probes.py --probe 5 --flex 0.5` now reports `PASS (disclosed)` mechanically. The same instability as before (MA4 −50% or MA5 +50% flips B→A; MA6 does not flip it) is unchanged in the underlying arithmetic, but is now disclosed via `case.json.sensitivity_disclosure[]` (Category X, both dials) with justifications ≥20 chars, matching the schema `tier2_probes.py` checks for. Per this project's established disclosure-aware pass state (see `enclosure-call`, `reroute-wait`, `biostatician`, `the-reserve-asymptote` precedent), this counts as clearing the P5 gate. |
| P6 data decay | **PASS** | All 5 sources re-fetched live and confirmed reachable, no URL moves. S1/S2/S3/S5 figures verbatim-confirmed. S4: scale-length figures (25.5"/24.75"/25") confirmed; the case's "21–24 frets typical" characterization is a minor looseness against the page's own wider chart (down to 19 frets in places) — same finding as the prior pass, not a new defect, not a broken citation. |

**Overall Tier 2: 6/6 clear the gate (5 PASS, 1 PASS (disclosed)).** Combined with Tier 1 clean
(0 blockers, 1 pre-approved GAP), this reaches **`TIER2_PASS`** per SPEC §2/MCS-26 ("PASS or
PASS_DISCLOSED for TIER2_PASS," confirmed against this project's own precedent in `reroute-wait`).

### Tier 3 — human dry-run
NOT RUN. (Unchanged — Tier 3 is out of scope for `case-readiness`.)

---

## case-readiness run — 2026-08-27 (Tier 2 full adjudication)

**State:** TIER1_PASS   **Verdict:** TIER1_PASS (Tier 2 fully adjudicated this pass — 5 PASS, 1 FAIL — `TIER2_PASS` is NOT reached because SPEC §2/MCS-26 require zero FAIL)

### Tier 1 — structural (20 checks), re-run 2026-08-27

`python3 skills/case-readiness/scripts/tier1_structural.py --case fret-board`

**PASS 19 / GAP 1 / FAIL 0. sha256(case.md) = a2c40d1df1342bb851c10475a74a024d3d44e02efdaf49977fa3166d5b487d81** —
unchanged from the previous run (case.md was not touched this pass; only `sensitivity_model.py` was
added and this report/case.json.qa were updated). Same single pre-approved GAP as before: T1-10
(reinforcement carve-out, untouched).

### Tier 2 — simulated play (6 probes), fully adjudicated

`python3 skills/case-readiness/scripts/tier2_probes.py --case fret-board` (plus `--probe 5 --flex 0.5`)
run for real this pass. All six probes below reflect genuine adjudication, not mechanical scaffolding.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent with no prior context, given only `/tmp/coldsolve-fret-board/PACKET.md` and forbidden from reading `case.json`/`FACILITATOR.md`/`QA_REPORT.md`. It chose **Option A**, correctly computed both the total-shop-time figures (52.33 vs 50.13 min) and the 12th-fret cents deviation via the log formula (≈−12.5 cents, 2.5× the 5-cent MA1 tolerance), and reasoned that a 2.2-minute time savings does not justify a ~2.5× tolerance overshoot given the disclosed week-long re-fret cost. It named its metric explicitly (deviation-vs-tolerance, weighted against re-fret cost, not raw time), named MA1 as the assumption its answer is most sensitive to, and named MA1 as the least-supported number — all independently derived from the packet, matching the case's own designed tension in D5/Guide-Notes Socratic Q4. Arithmetic is correct and matches `case.json.derived` exactly; a defensible position reached for the right reasons. (This case has no single "stated recommendation" to grade against — D5 is an open weigh-the-factors dilemma, not an answer key — so the pass criterion is "defensible position, correct arithmetic, named metric," which this clears.) |
| P2 both-sides | **PASS** | Built the strongest case for each option directly. A: "2.2 extra minutes buys zero drift by construction and eliminates the disclosed week-long rework risk from a 12.5-cent (2.5×-tolerance) overshoot." B: "4.2%-faster total shop time (the case's own graded primary metric) using the exact method that produced the shop's last three guitars, all of which passed final tuner checks after standard bridge-saddle compensation." Neither side collapses to a concession — B's argument does not depend solely on the numeric margin (it also carries the twist's real, if unquantified, historical-precedent point); A's argument does not depend on the tolerance line being exactly 5 cents (the *order of magnitude* of the overshoot, and the disclosed asymmetric rework cost, survive a looser tolerance too). **Caveat, tied to P5 below:** B's 4.2% margin specifically (not its twist-based argument) is thinner than the remediation report's "robust" framing suggested — see P5. |
| P3 trap check | **PASS** | From the case text alone: Appendix B/C's 12th-fret lengths differ by under a tenth of an inch (12.7500 vs 12.6573 in), an easy invitation to eyeball them as "basically the same" and skip D3's logarithmic cents conversion — cents is a multiplicative/log scale, so a visually tiny length gap can still be a musically real, nameable pitch gap. `FACILITATOR.md`'s "The trap" section names exactly this path ("treating 'small rounding error' as automatically negligible... without ever computing the cents conversion in D3"). Guide names the same trap the case actually contains. |
| P4 twist integrity | **PASS** | (1) The twist (shop's setup log: three prior guitars, all fretted with the Rule of Eighteen, all passed final tuner checks after bridge-saddle compensation) genuinely invalidates a position a real room would hold after the Data Deep Dive — flat rejection of B purely because it overshoots the 5-cent tolerance, treating D3's number as the final word on the finished instrument's intonation. (2) The twist has no numeric hook into any stated Modeling Assumption (MA1–MA6) or into `sensitivity_model.py`'s arithmetic — it is a qualitative narrative device about a downstream process step, not a value that could be read two ways depending on assumption-sequencing, so there is no Cold-Chain-style ambiguous-convention failure mode to check. `FACILITATOR.md` explicitly declines to hand a specific resolution ("Do not hand a specific answer to that question — it is genuinely open") — the twist unsettles a position without making anything else obviously correct, per the pass criterion. |
| P5 sensitivity | **FAIL** | Authored `cases/fret-board/sensitivity_model.py` (contract: `PARAMS`, `FLEX = [calc_seconds_per_fret_a (MA4), calc_seconds_per_fret_b (MA5), shared_baseline_minutes (MA6)]`, `evaluate()` returning negated total-shop-minutes so "higher is better" holds with B as the base winner). **Base case reproduces `case.json` exactly:** A=52.33 min, B=50.13 min, margin **4.2%**, winner B. Flexing ±50%: **the verdict FLIPS to A** in two of six flexes — MA4 (`calc_seconds_per_fret_a`) at −50% (20s→10s: A=48.67 < B=50.13, A wins) and MA5 (`calc_seconds_per_fret_b`) at +50% (14s→21s: B=52.70 > A=52.33, A wins). MA6 (`shared_baseline_minutes`) does not flip the verdict at either ±50% bound (B stays the winner, margin ranges ~2.9%–7.4%). **This directly contradicts the remediation report's robustness claim.** That claim ("even doubling MA4 alone keeps the margin near 16%") checked only a *widening* +100% move on MA4 — the direction that makes A slower and B win by more. It never checked the *narrowing* direction the SPEC §2/MCS-26 ±50% protocol requires: MA4 getting **faster** (or MA5 getting **slower**) shrinks the already-thin 2.2-minute raw gap between the options fast enough to flip the winner well within a ±50% swing, since the per-fret gap (22×6s=132s≈2.2 min) is nearly as large as the entire baseline margin itself. **Nothing in `case.json.balance`, `FACILITATOR.md`, or case.md's Modeling Assumptions block discloses this instability** — the case currently defends a 4.2%-margin-favors-B story without noting that a modest, equally plausible reading of MA4/MA5 (student's own hand-timing intuition, e.g. "an exponent isn't THAT much slower to key in") flips the recommended-by-the-metric winner. Per SKILL.md: "unstable under a ±50% assumption swing is not forbidden — but it must say so." It does not, so this is a genuine FAIL, not a `NOT RUN`. |
| P6 data decay | **PASS** | All 5 sources fetched live via WebFetch and confirmed reachable with their cited figures intact: S1 (liutaiomottola.com/formulae/fret.htm) — formula and 1.0594630943593 both present verbatim. S2 (StewMac fret-scale-rule-instructions) — "17.817154" factor confirmed verbatim. S3 (liutaiomottola.com RuleOf18) — divisor-18 and "trend flat" finding both confirmed. S4 (StewMac scale-length-explained) — Fender 25.5", Gibson 24.75", PRS 25" all confirmed; fret-count context confirmed present, though the page's own table spans a slightly wider range (down to 19 frets in some configurations) than the case's summarized "21–24 frets typical" — a minor characterization looseness, not a broken or drifted citation, and MA2's fret count (22) sits inside both the page's range and the case's stated range either way. S5 (StewMac "estimate hours, not dollars") — the ".6hrs" refret line item confirmed verbatim (Dan Erlewine's 1945 Gibson J-45 example), matching the case's directional-context-only use for MA6. No dead links, no drifted figures, no URL moves. |

**Overall Tier 2: 5 PASS, 1 FAIL (P5). Tier 2 is NOT clean — `TIER2_PASS` is not reached.** `case.json.qa.state` remains `TIER1_PASS`.

### What P5's FAIL means for next steps (not case-readiness's to fix)

Two legitimate repairs, either is `case-write`/case-owner work: (a) retune MA4/MA5's `value_used` so
the metric is genuinely robust to a ±50% swing in either direction, not just the +100%-widening
direction already checked, or (b) keep the current values and add the required disclosure — in
`case.json.balance` and in `FACILITATOR.md` — that the total-shop-time margin is a real but thin
race, sensitive to reasonable disagreement about per-fret calculation speed, so the guide does not
defend a 4.2% margin as more solid than it is. Per SKILL.md, `case-readiness` names the defect and
does not fix it.

### Tier 3 — human dry-run
NOT RUN.

---

## case-readiness run — 2026-08-27 (post-retune)

**State:** TIER1_PASS   **Verdict:** TIER1_PASS (Tier 1 clean; Tier 2 mechanically started, adjudication pending)

### What changed since the 2026-08-26 BLOCKED run

The 2026-08-26 run (preserved below) found T1-09 FAILED: `margin_pct` = 100.0% on the original
primary metric ("cents of pitch deviation from true equal temperament at the 12th fret"). The case
owner reviewed the judgment call and chose to **retune the case** (SPEC §2), not accept the
imbalance. Investigation before retuning (see `case.json.balance.margin_note` for full detail)
established that the original metric was **structurally unbalanceable, not just unluckily tuned**:
Option A (Precision Method) is exact by construction at *every* fret, not only fret 12 — verified
directly: at fret 1, Option A's own 4-decimal rounding error is on the order of 0.000004 cents,
against the Rule of Eighteen's systematic ~1.04 cents/fret drift. Any nonzero Option-B cents figure
against an exact-zero Option A always computes to a 100% margin under this project's loser/winner
formula, so the QA report's first suggested repair (regrade at an earlier fret) could not have
worked — it was tested by hand and confirmed not to fix the imbalance.

The second suggested repair was applied instead: **`primary_metric` was reframed** from raw
12th-fret accuracy to **total shop time, in minutes, to calculate/mark/cut all 22 frets**
(shared cutting/installing/dressing time, identical for both methods, plus each method's own
per-fret calculation time). This is grounded in real research (one new source, S5 — a StewMac
job-costing example, 0.6 hrs for a comparable fret-installation line item, cited MEDIUM confidence
and used only as directional context) plus three new, explicitly-labeled Modeling Assumptions
(MA4, MA5 — per-fret calculation time for each method; MA6 — the shared baseline), none presented
as fact. `margin_pct` recomputed at **4.2%**, well inside the ~20% cap, and — importantly — robust
to reasonable variation in the MA4/MA5 estimates, since the MA6 baseline dominates total time for
both options (checked by hand: even doubling MA4 alone keeps the margin near 16%). Full derivation
in `case.json.balance.margin_note` and `case.json.derived.shop_time_primary_metric`.

The original accuracy figures (~12.5 cents / 150% tolerance overshoot for Option B) are **not
deleted or hidden** — they remain fully disclosed in Appendix D and `case.json.derived
.accuracy_cost_context`, and Challenge D5 and `FACILITATOR.md`'s Socratic Q4 now explicitly ask
students to weigh the close time race against the much larger, disclosed accuracy gap. This
matches the case's real intended tension per the original judgment call: cost/deadline/historical-
precedent vs. a known, named accuracy cost.

### Tier 1 — structural (20 checks), re-run 2026-08-27

`python3 skills/case-readiness/scripts/tier1_structural.py --case fret-board`

**PASS 19 / GAP 1 / FAIL 0. sha256(case.md) = a2c40d1df1342bb851c10475a74a024d3d44e02efdaf49977fa3166d5b487d81**

| id | result | note |
|---|---|---|
| T1-01–T1-08 | PASS | unchanged from 2026-08-26 run |
| T1-09 | **PASS** | SPEC §2 balance test — `margin_pct` = 4.2% on the retuned primary metric (cap ~20%). Was the sole BLOCKER; now clears. |
| T1-10 | GAP | new_coverage[] still empty — pre-approved reinforcement carve-out, untouched, unaffected by this retune |
| T1-11–T1-15 | PASS | unchanged; FACILITATOR.md continuity re-checked against the retuned case.md/case.json and agrees |
| T1-16 | PASS | QA hash re-recorded and current after the retune edits |
| T1-17–T1-20 | PASS | unchanged |

**BLOCKER (0).** **GAP (1, pre-approved, untouched):** T1-10, same as before — case-owner
instruction to leave as-is (reinforcement carve-out, `case.json.reinforcement_note`).

Preflight linter (`preflight_lint.py --case fret-board`) reports one pre-existing advisory finding
(the `<!-- FACILITATOR ONLY -->` marker comment in case.md, present before this retune and unrelated
to it) — advisory only, not a blocker, not introduced by this pass.

### Tier 2 — simulated play (6 probes)

`python3 skills/case-readiness/scripts/tier2_probes.py --case fret-board` was run now that Tier 1
is clean. **Mechanical result: 0 probes failed mechanically.** All six probes require adjudication
this pass did not complete:

| probe | verdict | note |
|---|---|---|
| P1 cold solve | PENDING | packet generated (`/tmp/coldsolve-fret-board/PACKET.md`); needs a genuinely blind solver pass, not run in this session |
| P2 both-sides | PENDING | prompt generated; not adjudicated this pass |
| P3 trap check | PENDING | prompt generated; not adjudicated this pass |
| P4 twist integrity | PENDING | prompt generated; not adjudicated this pass |
| P5 sensitivity | NOT RUN | no `sensitivity_model.py` exists yet for this case (MCS-26) — script authoring not done this pass |
| P6 data decay | PENDING | delegated worklist generated for all 5 sources (S1–S5); URLs not re-fetched this pass |

Per `skills/case-readiness/SKILL.md`'s own rule, **PENDING/NOT RUN is the honest state, not a
pass** — Tier 2 is not clean and `TIER2_PASS` is not claimed. This pass's mandate was to verify the
retune clears T1-09 without breaking anything else structurally; Tier 1 confirms that. Completing
Tier 2 (a blind cold-solve pass, live re-fetches of all 5 sources including the new S5, and
authoring `sensitivity_model.py`) is real follow-on work, left for a dedicated case-readiness pass.

### Tier 3 — human dry-run
NOT RUN.

---

## case-readiness run — 2026-08-26 (superseded by the retune above)

**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED (Tier 1 did not clear; Tier 2 not run)

### Tier 1 — structural (20 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Yuki Tanaka." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate (fixed — a trailing facilitator-only HTML comment had been appended directly after Challenge 5's text; moved to the end of the document, after Appendix H, where it does not touch the boilerplate diff) |
| T1-05 | PASS | no Challenge numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | final-appendix lines are verbatim spine labels (added "How to compare two or more values" to Appendix H to back the new D5 skill mapping) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | **FAIL** | SPEC §2 balance test — margin_pct = 100.0% on the primary metric (cap ~20%). See "Judgment call" below. **Not fixed — out of case-readiness's scope.** |
| T1-10 | GAP | new_coverage[] empty — pre-approved reinforcement carve-out (case.json.reinforcement_note), untouched per instructions |
| T1-11 | PASS | learning-goal mutual reachability (fixed — D5 previously mapped to no skill; mapped to `number-sense-how-to-compare-two-or-more-values`, added to standards[] and Appendix H) |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note (fixed — FACILITATOR.md rewritten with the full Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On ladder, a sourced-and-honest Twist built on bridge-saddle compensation, a timed 45-minute Socratic plan, and 5 single-line Socratic questions) |
| T1-14 | PASS | CONTINUITY — FACILITATOR.md agrees with case.md/case.json (fixed — the orphan "2.5" ratio figure moved into `case.json.derived`) |
| T1-15 | PASS | no published/ directory — nothing to drift |
| T1-16 | PASS | QA hash recorded and current |
| T1-17 | PASS | cohort-size bands declared (fixed — added Full/Compressed/1:1-pair bands to case.json.cohort_bands[]) |
| T1-18 | PASS | no published/ directory — MCS-37 has nothing to check yet |
| T1-19 | PASS | no published/ directory — MCS-39 has nothing to check yet |
| T1-20 | PASS | no published/ directory — advisory, nothing to check yet |

**BLOCKER (1):**
- [T1-09] SPEC §2 — UNBALANCED: margin is 100.0% on "cents of pitch deviation from true equal temperament at the 12th fret" (cap ~20%). Retune a constraint. Do NOT fix this by hiding data.

**GAP (1, pre-approved, untouched):**
- [T1-10] new_coverage[] is empty — reinforcement carve-out per case.json.reinforcement_note (case-owner instruction: leave as-is).

### Judgment call for a human (SPEC §2 balance) — resolved 2026-08-27, see run above
`margin_pct` is now honestly recorded, not left null and not hidden: **100.0%**, computed as
`100 × (loser_cents − winner_cents) / loser_cents = 100 × (12.5 − 0) / 12.5 = 100.0`, using the
worse (higher-cents) option as the denominator so Option A's exact-zero deviation doesn't produce
an undefined ratio. A second, independently meaningful figure says the same thing another way:
Option B's ~12.5-cent deviation is also ~2.5× (250%) the stated MA1 tolerance (5 cents) — a ~150%
overshoot of the acceptable-intonation line. Both are recorded in `case.json.balance` and
`case.json.derived`.

**This case is not balanced on its stated primary metric**, well past SPEC §2's ~20% cap — nothing
like the Robotics Engineering exemplar's 0.09%. The concept sheet that approved this case declared
"Sensitivity: None" / "Split risk: NONE" and scored it for its domain-opening value
(`music-acoustics`), not for a tight balance, so this gap was not caught before research. Fixing it
for real means retuning a constraint in `case.md` (e.g. grading deviation at an earlier fret where
the two methods sit closer together, or reframing the primary metric so the dilemma's real tension
— cost/deadline/historical-precedent vs. a known, named accuracy cost — is what's graded) — that is
`case-write`/`case-owner` work, explicitly out of `case-readiness`'s scope ("this skill CANNOT
fix"). **A human needs to decide: retune the case, or consciously accept and document that this
case's defensibility rests on the cost/deadline/twist argument rather than a close primary-metric
race.** Either is legitimate; picking one is not. **Resolved 2026-08-27: retuned, per the section
above.**

### Tier 2 — simulated play (6 probes)
See the 2026-08-27 run above (mechanically started, adjudication pending) — Tier 1 now clears, so
this section is superseded.

### Tier 3 — human dry-run
NOT RUN.
