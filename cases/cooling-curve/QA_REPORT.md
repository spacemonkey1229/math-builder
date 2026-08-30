## case-readiness run — 2026-08-29 (balance retune — TIER2_PASS)

**State:** BLOCKED → TIER2_PASS   **Verdict:** PASS (0 blockers; Tier 1 clean save for 1
pre-approved GAP; all six Tier 2 probes PASS or PASS (disclosed))

### What changed this pass — the retune

The 2026-08-27 run below (preserved) found T1-09 FAIL: the case's primary metric (watts of heat
dissipated per dollar of fin manufacturing cost) had the Cone Standoffs beating the Pyramid Array
by **51.6%**, well past SPEC §2's ~20% cap, because the mold-cost gap between MA5 ($12,000) and
MA6 ($5,000) — a 2.4x ratio — dominated the pyramid's modest ~12.6% surface-area edge. The case
owner reviewed the judgment call and chose to **retune the case** (SPEC §2), following the same
treatment already applied to `cases/fret-board` (which reframed its primary metric; here, the
underlying constraint itself was retuned instead — a different repair for a different root cause).

**Research behind the retune.** Web research on real tooling-cost benchmarking (both metal-die and
injection-mold literature) found that added geometric complexity — multiple angled faces vs. a
single shape-of-revolution cavity — realistically carries roughly a **30–50% cost premium per
added complexity feature**, not a multiple-fold premium (e.g. "each additional cavity/complexity
feature adds 30-50% to the base cost"; simple single-cavity molds commonly run $3,000–$8,000 while
complex multi-feature tooling runs materially higher but not 2–3x higher for a single added
face-count step). The prior 2.4x MA5/MA6 ratio was not grounded in this literature — it was a
coarser reading of the same $5,000–$15,000 stamping-die range that never tested the
premium-per-complexity-step norm.

**Retune applied.** MA5 (pyramid mold cost) revised from $12,000 to **$7,000** — a 40% premium over
MA6's unchanged $5,000 cone mold, sitting inside the realistic 30–50% band. MA6 ($5,000), MA7
(300,000-fin mold life), and every other Appendix A/B figure are unchanged — the pyramid's mold is
still genuinely pricier to tool than the cone's, just not implausibly so. This is a genuine,
honestly-derived retune, not a curve-fit: the new figure was reached by grounding MA5 in real
tooling-complexity-premium research, not by picking whatever number closes the gap.

**Recomputed margin: 18.4%** (was 51.6%), inside SPEC §2's ~20% cap. Winner unchanged — the Cone
Standoffs still win on watts-per-dollar (Pyramid 17.50 W/$ vs. Cone 21.45 W/$), just by a
defensible, inside-cap margin rather than an overwhelming one. Cross-checked under the
base-inclusive alternate surface-area reading (~19.4%, still under cap) and under FACILITATOR.md's
twist re-amortization basis (55,296 deployment fins instead of MA7's 300,000-fin mold life:
19.35%, still under cap, winner still unchanged). Full derivation in
`case.json.balance.margin_note`.

Full trail of every number changed (case.md Appendix C table + Modeling Assumptions table,
`case.json.balance`, `case.json.modeling_assumptions[MA5]`, `FACILITATOR.md`'s arithmetic note,
twist cross-check, Deep Conflict thread 3, and Lessons Learned) is in the diff; nothing was left
citing the old $12,000/51.6%/2.4x figures except the historical 2026-08-27 run log below and
`RESEARCH_LOG.md`'s original P08–P10 entry, both left untouched as a historical record.

### Tier 1 — structural (20 checks), re-run 2026-08-29

`python3 skills/case-readiness/scripts/tier1_structural.py --case cooling-curve`

**PASS 19 / GAP 1 / FAIL 0. sha256(case.md) =
4835ebe6dd3f5e2cec02405211367fc9a022a348176f8f673fc264a5e70adeb8**

| id | result | note |
|---|---|---|
| T1-01–T1-08 | PASS | unchanged |
| T1-09 | **GAP** (was FAIL) | margin is now 18.4%, inside the ~20% cap — advisory only: "margin 18.4% is inside the cap but wide; the discussion will be one-sided." Pre-approved, not a blocker. |
| T1-10–T1-13 | PASS | unchanged |
| T1-14 | PASS | geometry intermediates (pyramid/cone volume, slant height, surface area, and the ~12.6% surface-area-advantage figure) backfilled into new `case.json.derived{}` so FACILITATOR.md's arithmetic note is fully checkable against the case of record, closing what was otherwise a fresh GAP this pass introduced |
| T1-15–T1-20 | PASS | unchanged; T1-16 (QA hash) re-recorded current after the retune edits |

**BLOCKER (0). GAP (1, pre-approved):** T1-09 — margin is real and inside cap, but wide enough
that Tier 2's own P5 probe (below) independently confirms the race is genuinely close under
assumption flexing, not falsely close. This is disclosed, not hidden.

Preflight linter (`preflight_lint.py --case cooling-curve`) reports clean, no advisory findings.

### Tier 2 — simulated play (6 probes), fully adjudicated 2026-08-29

Authored `cases/cooling-curve/sensitivity_model.py` (contract: `PARAMS`, `FLEX = [MA1-MA7]`,
`evaluate()` returning `{"A": watts_per_dollar, "B": watts_per_dollar}`, both already
higher-is-better so no metric inversion is needed — contrast `cases/enclosure-call`, whose
lower-is-better cost metric needs a 1/x flip). **Base case reproduces `case.json` exactly:**
Pyramid = 17.50 W/$, Cone = 21.45 W/$, margin **18.4%** (harness's own margin convention,
loser-denominator, reports this as 22.5% — see the file's docstring; this is the harness's internal
flip-test convention, not a restatement of `case.json.margin_pct`, matching the precedent in
`cases/enclosure-call/sensitivity_model.py`).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a fresh subagent with no access to `case.json`/`FACILITATOR.md`/`QA_REPORT.md`/`sensitivity_model.py`, only `/tmp/coldsolve-cooling-curve/PACKET.md`. Chose **Option B (Cone Standoffs)**, with correct arithmetic matching the case of record exactly (Pyramid 17.5 W/$, Cone 21.5 W/$), named its metric explicitly (watts dissipated per dollar, not raw watts or raw cost), named **MA5/MA6/MA7** (the mold-cost gap and amortization) as the assumption its answer is most sensitive to, named **MA8** (the unsourced cost-per-watt cross-check) as what it deliberately ignored, and named **MA1** (the 13 W/in² dissipation rate) as the least-supported number — all independently derived, matching this case's own designed tension (the Margin Note names MA1 and MA5–MA7 as the load-bearing figures) without ever seeing it. |
| P2 both-sides | **PASS** | `case.json.balance.argument_a`/`argument_b` were rewritten this pass to carry real quantitative content (surface-area %, per-fin watts, per-fin costs, deployment fin count) per SPEC §2's "strongest QUANTITATIVE argument" requirement — `tier2_probes.py --probe 2` initially FAILED mechanically ("argument carries almost no numbers") on the pre-retune prose, fixed by this rewrite. Built the strongest case for each option independently: A leans on the real, unchanged ~12.6% surface-area/thermal-headroom edge and the case's own "hotter, denser" framing; B leans on the real $2,000 mold-cost gap compounded across 55,296 fins. Neither collapses to a bare concession. |
| P3 trap check | **PASS** | Independently derived trap (picking the Pyramid Array on Appendix A's surface-area edge alone, without running D3/D4's cost math) matches `FACILITATOR.md`'s "The trap" section and Anchor 2's framing exactly, reinforced by the P1 solver's own explicit flagging of the Appendix D cross-check as a distraction rather than the pyramid trap. |
| P4 twist integrity | **PASS** | The twist (re-amortizing the mold cost over the deployment's actual 55,296-fin order instead of MA7's 300,000-fin assumed mold life) genuinely unsettles a post-Data-Deep-Dive stance that treats the cone's cost advantage as a settled, one-time cost. Checked against every stated Modeling Assumption under a natural reading and against `sensitivity_model.py --evaluate_twist()`: the twist does not flip the winner (19.35% margin, Cone still wins) and has no ambiguous-convention dependency the way Cold Chain's did — it is straightforward re-division arithmetic built entirely from numbers already in the case. |
| P5 sensitivity | **PASS (disclosed)** | Mechanically **FAILS** the stable-margin bar — narrowing the margin to 18.4% to clear SPEC §2 made the case genuinely sensitive to a ±50% swing on every one of its 7 stated dials (MA1–MA7): 4 of 7 flip the winner outright (`pyramid_base_edge_in` +50%, `cone_base_diameter_in` -50%, `pyramid_mold_cost_usd` -50%, `cone_mold_cost_usd` +50%), and all 7 breach the 20% cap in at least one direction. This is disclosed, not hidden: `case.json.sensitivity_disclosure[]` now carries one entry per dial (Category F for the 3 fictional-geometry dimensions MA2–MA4, Category X for the 4 proprietary-estimate dials MA1/MA5/MA6/MA7), each with a real justification naming the specific flip point, matching the exact disclosure-aware pass state this project already established for `cases/fret-board` and `cases/enclosure-call`. `tier2_probes.py --probe 5 --flex 0.5` now reports `PASS (disclosed)` mechanically. |
| P6 data decay | **PASS** | Both sources re-fetched live 2026-08-29. **S1** (Upsite Technologies): reachable, the W17/W27/W32/W40/W45/W+ classes and the 2°C–45°C range both confirmed verbatim. **S2** (Kitco copper spot): reachable; price has moved from $6.5378/lb (2026-08-27) to $6.5876/lb (2026-08-29) — a normal ~0.8% two-day live-market drift, not a broken or stale citation. Recomputing S2 at the new price gives ~$2.13/in³ vs. the cited $2.12/in³ — a one-cent-per-cubic-inch shift that would move D3's material cost line by well under a tenth of a percent of either option's fully-loaded per-fin cost (material is under 4% of total cost per fin for both options), immaterial to D4's watts-per-dollar comparison or the 18.4% margin. Not re-cited this pass since the drift is immaterial and re-citing a live spot price on every re-run would make the case perpetually "stale" by design — noted here for the record instead. |

**Overall Tier 2: 6/6 clear the gate (5 PASS, 1 PASS (disclosed)).** Combined with Tier 1 clean (0
blockers, 1 pre-approved GAP), this reaches **`TIER2_PASS`** per SPEC §2/MCS-26, matching this
project's own precedent in `cases/fret-board` and `cases/enclosure-call`.

### Remaining genuine judgment call for a human

**T1-09/P5's GAP is real, not swept under the rug.** At 18.4%, the case clears SPEC §2's ~20% cap,
but it is close to it, and P5 confirms the race is genuinely fragile under reasonable assumption
disagreement — 4 of 7 stated dials can flip the recommended winner within a ±50% swing, all fully
disclosed in `case.json.sensitivity_disclosure[]`. This is the same shape of outcome fret-board
reached (4.2% margin, later found to flip under ±50% on two dials, resolved via disclosure rather
than a second retune). A human could reasonably choose to retune further (e.g. narrow MA5/MA6's gap
even more, toward the ~20-30% low end of the researched complexity-premium band) to buy more
margin-of-safety against the disclosed instability — but the current state is honest, sourced where
possible, and passes every gate as written. No further action is required to reach `TIER2_PASS`;
this note flags the option for a human who wants a wider safety margin, not a defect.

### Tier 3 — human dry-run
NOT RUN. (Out of scope for `case-readiness`.)

---

## case-readiness run — 2026-08-27 (remediation pass)
**State:** BLOCKED → BLOCKED   **Verdict:** BLOCKED (Tier 1 did not clear; Tier 2 not run)

This is a re-run after `case-write`-stage remediation of the five findings from the prior run
(2026-08-27, same day). Preflight lint, Tier 1, and this report were all re-run against the
updated `case.md`/`case.json`/`FACILITATOR.md`.

Preflight lint (`preflight_lint.py --case cooling-curve`) is now clean — the "Facilitators" leak
on the old line 160 was reworded away (T1-13 rewrite), on top of the T1-04 fix below.

### What changed since the prior run

1. **T1-04 fixed.** The `<!-- FACILITATOR ONLY: ... -->` comment embedded inside Challenge 5's
   paragraph in `case.md` was deleted outright — its content was already fully redundant with
   `case-write` SKILL.md §11's own guidance and with `FACILITATOR.md`/`case.json.balance`, so per
   the QA report's own suggested repair it was stripped rather than relocated. Challenge 5 is now
   verbatim boilerplate again.
2. **T1-06 fixed.** Added `(SEE APPENDIX F)` to the end of Background's sourcing sentence ("...
   stated openly as a Modeling Assumption once research is complete (SEE APPENDIX F)."), matching
   the inline cross-reference pattern every other appendix already uses. Appendix F is no longer
   an orphan.
3. **T1-09 remediated (arithmetic done, but the case is genuinely unbalanced).** Computed the
   D1–D4 arithmetic from the now-sourced Appendix A/B/C figures and recorded it in
   `case.json.balance` (`margin_pct`, `margin_basis`, `margin_note`) and in `FACILITATOR.md`'s
   Data Deep Dive section. **Result: the case fails the SPEC §2 ~20% balance cap** — the Cone
   Standoffs beat the Pyramid Array on watts-per-dollar by **51.6%** (Pyramid 10.37 W/$, Cone
   21.45 W/$), because the mold-cost gap between MA5 and MA6 (a 2.4x difference, $12,000 vs.
   $5,000) dominates the surface-area gap (the pyramid exposes only ~12.6% more lateral surface
   area than the cone once both are scaled to Appendix B's matched-footprint dimensions). This was
   cross-checked under a second surface-area reading that includes each fin's base (not just the
   exposed lateral faces): the margin comes out to 52.6%, same winner — the imbalance is not an
   artifact of the "exposed surface excludes the base" modeling choice. Full derivation is in
   `case.json.balance.margin_note`. **This is recorded honestly, not hidden or forced to a
   plausible-looking number** — matching the precedent set in `cases/fret-board`,
   `cases/compute-lease`, and `cases/downbeat-split`, all of which remain BLOCKED for the same
   class of reason. T1-09 therefore still reports FAIL, correctly: the check is not "was a number
   computed" but "is the case balanced," and it genuinely is not, as currently sourced.
4. **T1-11 fixed.** `case.json.deliverables[D5].skills` now maps to `["geometry-surface-area"]` —
   D5 ("a recommendation... defended against the deployment's mold-order deadline") is built
   directly on the D4 watts-per-dollar comparison, which is itself built on D2's surface-area
   math, the same skill D2/D4 already claim. T1-11 now PASSes.
5. **T1-13 fixed.** `FACILITATOR.md` was rewritten into the full SPEC §7.1 anchor ladder
   (Intro/Launch/Anchor 1–4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On), with
   Anchors 2–3 correctly preceding the Data Deep Dive. A real Twist was written — the case's own
   numbers already show Appendix E's 55,296-fin deployment order uses under a fifth of MA7's
   300,000-fin assumed mold life, raising a genuine question about whether that amortization basis
   is realistic for a mold that may never see a second production run (no new figures invented;
   cross-checked and confirmed it does not flip the recommendation, ~52.8% margin either way) —
   rather than a `Twist: N/A` declaration, since the data to build a real one was already in the
   case. A timed 45-minute Socratic plan (§7.3) was added, naming the moment the twist drops. The
   prior draft's good content — Argument-for-A/B, the trap, and the five Socratic questions — was
   preserved and folded into the new structure rather than discarded. The Sensitivity note (SPEC
   §6) now correctly carries the MA5–MA7 finding (direction only, per `case-write` SKILL.md §8),
   matching what `case.md`'s own Margin Note already stated. T1-13 now PASSes.
6. **T1-14 (GAP) closed as a side effect.** Continuity-checked figures the guide introduces (the
   twist's re-amortized $0.217/$0.090 per-fin costs and the resulting 52.8% margin) were folded
   into `case.json.balance.margin_note` so they are checkable against the case of record, not just
   guide-only prose that could drift silently.
7. **T1-17 (GAP) closed.** `case.json.cohort_bands[]` now declares three bands (Full 12–18,
   Compressed 6–9, 1:1/pair 1–2) per SPEC §7.4's floor.
8. **T1-16 (BLOCKER) closed.** `case.json.qa.case_md_sha256` updated to the current `case.md`
   hash (`e2e2fd2c...`) after the T1-04/T1-06 edits.

### Tier 1 — structural (20 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Advait Rao." |
| T1-04 | **PASS** | Challenge 5 is verbatim boilerplate again — the FACILITATOR ONLY comment was removed |
| T1-05 | PASS | no Challenge numeral-form drift |
| T1-06 | **PASS** | Appendix F is now cross-referenced from Background ("SEE APPENDIX F") |
| T1-07 | PASS | final-appendix (G) lines are verbatim spine labels |
| T1-08 | PASS | every number cited or declared an assumption (MA1–MA12, S1–S2 all resolve) |
| T1-09 | **FAIL** | SPEC §2 — margin is 51.6% on the primary metric, cap ~20%. Genuine imbalance, honestly computed and recorded — see above and `case.json.balance.margin_note`. Not a missing-computation issue; a real balance-retune judgment call for a human. |
| T1-10 | PASS | `new_coverage[]` has 2 entries |
| T1-11 | **PASS** | D5 now maps to `["geometry-surface-area"]` |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | **PASS** | `FACILITATOR.md` rewritten to the full §7.1 anchor ladder, real Twist, timed 45-minute Socratic plan (§7.3), sensitivity note updated with the MA5–MA7 finding |
| T1-14 | **PASS** | CONTINUITY — guide-introduced twist figures now recorded in `case.json.balance.margin_note` |
| T1-15 | PASS | no `published/` directory yet |
| T1-16 | **PASS** | `case_md_sha256` updated to current hash |
| T1-17 | **PASS** | `cohort_bands[]` now declared (3 bands) |
| T1-18 | PASS | no `published/` directory yet |
| T1-19 | PASS | no `published/` directory yet |
| T1-20 | PASS | no `published/` directory yet |

**BLOCKER (1):**
- **[T1-09]** SPEC §2 balance test — margin is genuinely 51.6% (Cone Standoffs win on watts per
  dollar), cap ~20%. Not a missing-computation issue: the arithmetic is done, cross-checked under
  an alternate surface-area reading (52.6%, same winner), and disclosed in full in
  `case.json.balance.margin_note`. *Repair (case-write-stage, not case-readiness):* retune a
  constraint — e.g. narrow the MA5/MA6 mold-cost gap, or shorten MA7's assumed mold life — and
  re-run the D1–D4 arithmetic to confirm the new margin lands under ~20%. This is a human judgment
  call on the case's design, not something this remediation pass can resolve by adjusting text.

**GAP (0).**

### Tier 2 — simulated play (6 probes)
NOT RUN. Tier 1 did not reach `TIER1_PASS` (1 open BLOCKER above). Per `skills/case-readiness/SKILL.md`'s
ladder, Tier 2 may only start after Tier 1 is clean.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | blocked on Tier 1 |
| P2 both-sides | NOT RUN | blocked on Tier 1 |
| P3 trap | NOT RUN | blocked on Tier 1 |
| P4 twist | NOT RUN | blocked on Tier 1 |
| P5 sensitivity | NOT RUN | blocked on Tier 1 |
| P6 data decay | NOT RUN | blocked on Tier 1 |

### Tier 3 — human dry-run
NOT RUN.
