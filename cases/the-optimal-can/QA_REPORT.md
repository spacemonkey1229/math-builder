# QA Report — The Optimal Can

## case-readiness run — 2026-08-15
**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS

This is a fresh-authored case (no `legacy_conversion_note`) closing a genuine spine gap: the
entire Calculus/Applications Of Derivatives group (7 skills) plus three Calculus/Derivatives
skills were at `n=0` before this case. The T1-10 legacy carve-out does not apply here and was not
invoked; `new_coverage[]` (10 ids) is a real, non-padded subset of `standards[]`, verified to
resolve in `readmodel/standards_spine.json` at `n=0` for every claimed new-coverage id.

### Session actions, in order

1. **Placeholder audit.** Grepped `case.md` for `{{NEEDS_SOURCE}}` — zero remain. Cross-checked
   `case.json.needs_source[]`: every token is `SOURCED` (backed by S1/S2/S3 in `sources[]`) or
   `ASSUMPTION` (backed by MA1–MA4 in `modeling_assumptions[]`). No fabrication needed.
2. **Standards/new_coverage audit.** Verified all 12 `standards[]` ids resolve in the spine; the
   10 `new_coverage[]` ids are exactly the ids at `n=0` before this case (the 7-skill
   Applications-Of-Derivatives group plus `calculus-derivative`,
   `calculus-instantaneous-rate-of-change`, `calculus-how-to-find-a-derivative-using-the-power-rule`).
   The two remaining `standards[]` ids (compound-unit conversion, percent-of-a-number) are
   correctly *not* claimed in `new_coverage[]` — both already have prior coverage (`n=6`, `n=24`).
3. **Built `cases/the-optimal-can/sensitivity_model.py` from scratch.** Contract:
   `PARAMS`/`FLEX`/`evaluate()` (no twist, so no `evaluate_twist()`). `FLEX` contains only the
   four genuine stated Modeling Assumptions (MA1 sheet thickness, MA2 retooling cost, MA3 annual
   volume, MA4 payback ceiling) — never the three sourced figures (CMI diameter [S1], 3104-H19
   density [S2], aluminum price [S3]), per the FLEX-scoping doctrine note (P6 stress-tests cited
   data instead). Verified the model reproduces `case.json.derived` exactly: `S_std=43.9266 in²`,
   `S_opt=43.0101 in²`, `annual_savings_usd=281268.82`, `payback_months=25.598`,
   `shortfall_pct=6.244`, `breakeven_annual_cans=319978587` — all bit-for-bit matches.
4. **Built `cases/the-optimal-can/published/The Optimal Can - Interactive.html`** from
   `templates/interactive_shell.html`. JS port of `PARAMS`/`FLEX`/`evaluate()` verified to match
   the Python model exactly under Node (`evaluate({}) → {A: 0, B: -18731.178...}` both sides).
   Glossary: 10 terms (7 fetched and confirmed live on mathsisfun.com 2026-08-15 this session —
   Critical Point, Local Maximum, Local Minimum, Concavity, Derivative, Instantaneous Rate Of
   Change, Power Rule — plus 3 reused verbatim from the contract doc's already-verified
   `STARTER_GLOSSARY`: Percent, Unit, Measurement). No balance-test literal (margin_pct=6.24, or
   the verdict itself) appears anywhere outside the calculator's own live computation — the
   Working Notebook's Step 4 explicitly does not tell the student whether the payback period
   clears the ceiling.
5. **Two case-content gaps found and fixed during this session** (not placeholder/fabrication
   issues — genuine doctrine gaps in an otherwise-researched case):
   - `FACILITATOR.md`'s Twist section was an unfilled "(to be authored...)" stub, not a real
     twist and not an explicit `Twist: N/A` justification. Investigated the one candidate twist
     research had flagged (a Ridgeline volume-doubling scenario) and confirmed it only restates
     the case's own D4 break-even calculation — recorded `Twist: N/A` with the reasoning written
     out, per MCS-15.
   - `FACILITATOR.md` was missing the mandatory 45-minute timed Socratic plan (MCS-16, SPEC §7.3)
     and had only 3 of the required 5 Socratic questions machine-detectable (the other 2 existed
     but were line-wrapped, which the checker's per-line regex can't see across a wrap). Added
     the timed plan table and reflowed the 5 questions to single lines. Added a named "trap"
     subsection (the guide previously never used the word).
6. **Two orphan-number findings fixed** (T1-14c): the Overview's "Line 3" numeral was cleared in
   `case.json.overview_numerals_cleared[]` (texture only, never used in a calculation); five
   guide-only sensitivity figures (51.2/17.1/12.8/38.4 months) were recomputed from
   `sensitivity_model.py` at each assumption's ±50% bound and moved into
   `case.json.derived.sensitivity{}` so they're checkable, not silently guide-only.
7. **Appendix F gap fixed**: `standards[]` claimed the compound-unit-conversion and
   percent-of-a-number "how to" skills but Appendix F's vocabulary bridge never listed them —
   added both lines to `case.md` Appendix F and to the interactive HTML's `HOWTO` array.
8. **Declared `case.json.cohort_bands[]`** (MCS-25; previously undeclared) for 8-12 / 13-20 / 21+
   Heroes, each noting what changes about how Anchor 4 and the Data Deep Dive run.

### Tier 1 — structural (19 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | 'Line 3' cleared in `overview_numerals_cleared[]` |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | Appendix F now lists all 12 standards-mapped labels |
| T1-08 | PASS | |
| T1-09 | PASS | margin_pct 6.24, within the 20% cap |
| T1-10 | PASS | standards resolve; new_coverage genuinely closes the gap (no carve-out invoked, this is fresh-authored) |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | GAP | MCS-15 — Twist is N/A; the checker flags this state for a human to confirm the justification is written out (it is, see FACILITATOR.md) |
| T1-14 | PASS | FACILITATOR.md ↔ case.md/case.json continuity clean after moving sensitivity figures into `derived` |
| T1-15 | PASS | |
| T1-16 | PASS | `case_md_sha256` recorded |
| T1-17 | PASS | `cohort_bands[]` declared |
| T1-18 | GAP | 39 orphan numbers, all SVG path/stroke decimals outside `<script>` — the documented accepted false-positive class (Cold Chain's own baseline is 110 of the same kind); zero balance-test leak |
| T1-19 | PASS | glossary: 10 terms, all on allowlisted domains, live-verified |

**BLOCKER (0). GAP (2), both accepted/expected. POLISH (2).**

### Tier 2 — simulated play (6 probes)
NOT RUN this session — case-readiness's own gate requires Tier 1 clean first, which is now true.
Tier 2 (cold solve, both-sides solve, trap check, twist integrity [N/A here], assumption
sensitivity, data decay) was out of scope for this authoring/gating pass; `sensitivity_model.py`
is in place and ready for probe 5 (`FLEX` = MA1–MA4) when Tier 2 runs.

### Tier 3 — human dry-run
NOT RUN.

## case.json.qa (written by this run)
```json
{"state": "TIER1_PASS", "verdict": "PASS", "run_on": "2026-08-15", "blockers_open": 0,
 "gaps_open": 2, "case_md_sha256": "27078268cb909225dd689124b5f6885603835b6e454ab0e5e73822e8c29db49d"}
```

**Next step:** Run `case-readiness` Tier 2 probes on `the-optimal-can`, or hand to a human for the
Tier 2 P1/P2/P3 model dispatch this skill delegates.

---

## case-readiness run — 2026-08-17 (Tier 2)

Re-ran Tier 1 first (`tier1_structural.py --case the-optimal-can`): still clean, **0 BLOCKERs, 3
GAPs** (T1-10 reinforcement carve-out — see `case.json.reinforcement_note`, added 2026-08-17 after
Curves Turn published first and claimed the same skill set; T1-13 twist-N/A confirmation; T1-18 39
orphan numbers, all SVG path/stroke decimals in the interactive HTML outside `<script>`, the same
accepted false-positive class as Cold Chain's baseline — zero balance-test leak). `case_md_sha256`
unchanged (`27078268...`), so this report and `case.json` describe the same `case.md` throughout.

`sensitivity_model.py` and `tier2_probes.py --case the-optimal-can --probe 5 --flex 0.5` both ran
mechanically; P1–P4 were adjudicated (P1 by a genuinely fresh cold-solve subagent, per the skill's
own dispatch instruction; P2–P4 by direct re-derivation from `case.md`/`FACILITATOR.md`); P6 was
delegated to a live WebFetch pass against all three cited URLs.

| probe | verdict | finding |
|---|---|---|
| **P1 cold solve** | **PASS** | Fresh subagent given only the leak-free packet chose **A — Hold The Line**, named the correct metric (payback period in months against MA4's 24-month capital-approval ceiling — explicitly *not* the surface-area-minimization the case sets up as the "obvious" pitch), and reproduced the case's own arithmetic essentially exactly: S(r)=2πr²+2V/r, r*=1.51055 in, h*=3.02110 in (h*/r*=2, second-derivative test confirms minimum), S_std≈43.9268 in² vs S_opt≈43.0101 in² (2.0867% reduction), savings ≈$0.000938/can, ≈$281,400/yr, payback ≈25.6 months (misses the 24-month ceiling), break-even ≈319.9M cans/yr. Correctly named MA1 (sheet thickness) as the most sensitive assumption and MA2 (retooling cost) as the least-supported number, and named the published 4.812 in flanged height as the deliberately-ignored appendix figure. Reached the case's own intended answer **by the intended route** — the metric-identification step (payback, not surface area) is exactly the trap this case's D1–D4 sequencing is built to test, and the solver did not skip it. |
| **P2 both-sides solve** | **PASS** | **A's best sentence:** at the case's own stated numbers, the optimal shape's savings pay back in ≈25.6 months against a 24-month ceiling — a real, computed miss, not an opinion, and it costs nothing to keep running today's tooling while waiting for a future contract that might change the math. **B's best sentence:** the shape genuinely uses less aluminum on every single can forever, and the case's own break-even shows Ridgeline needs only ≈6.7% more annual volume than its stated 300M cans/yr to clear the ceiling on the same formula — a thin, specific, quantitative gap, not a vague "worth it long-term" claim. Neither side collapses into a concession pattern (no "B is better but not worth it" hand-wave); both arguments are numbers-first and independently defensible, which is exactly what the disclosed 6.24% margin and the P5 instability below predict. B's argument does lean on the fact that MA1–MA3 are all Category-X estimates rather than hard citations — real leverage for B, but not a collapse, since A's own case rests on those same three assumptions and doesn't get to keep them while denying B the same challenge. |
| **P3 trap check** | **PASS** | Reading `case.md` alone, the most plausible wrong path a hurried student produces is exactly the one `FACILITATOR.md`'s "The trap" section names: compute the 2.09% surface-area reduction (D1–D2), treat "smaller shape → less material → retool" as self-evident, and never reach D3's per-can dollar conversion or D4's payback/break-even math where the actual capital-approval decision lives. The guide also anticipates the mirror-image trap (treating 25.6 > 24 months as a clean, decisive "no" without registering how thin the 6.24% margin is against three unsourced assumptions) — both directions of the same shortcut, named before a room would hit either one. |
| **P4 twist integrity** | **PASS (N/A)** | This case ships with no twist. `FACILITATOR.md`'s Twist section states `Twist: N/A` and writes out the reasoning: the one candidate twist research considered (a Ridgeline volume-increase scenario, e.g. a new client contract) was rejected because every mechanically clean version of it only restates the break-even calculation D4 already asks the Hero to compute, and forcing a distinct twist would require a fifth unsourced modeling dial this case's research found no defensible basis for. This is a written, reasoned N/A per MCS-15, not a silently-skipped section (confirms T1-13's GAP — the checker correctly flags twist-N/A for human confirmation, and this is that confirmation). |
| **P5 assumption sensitivity** | **PASS (disclosed)** | `tier2_probes.py --probe 5 --flex 0.5` (mechanical): base case A wins. Sweeping the 4 declared `FLEX` dials (`sheet_thickness_in`, `retool_cost_usd`, `annual_can_volume`, `ceiling_months`) at ±50% flips the winner to B on `sheet_thickness_in` +50%, `retool_cost_usd` −50%, `annual_can_volume` +50%, and `ceiling_months` +50% — i.e. the verdict is genuinely unstable under a ±50% swing on any of the four stated assumptions, matching `FACILITATOR.md`'s own "all four are load-bearing" framing and Appendix D's per-assumption sensitivity notes exactly (payback range 17.1–51.2 months across MA1/MA3, 12.8–38.4 months across MA2, verdict flip at 30-month ceiling for MA4). All four flexed params have a recorded `sensitivity_disclosure[]` entry with category **X** (proprietary/no-public-figure-exists estimate — MA1 no exact datasheet gauge found, MA2 no public one-off die-changeover price, MA3 Ridgeline is fictional so no real production record can exist, MA4 Ridgeline's internal finance policy is not public) and a written justification for each. Per the disclosure-aware pass state (2026-08-13 doctrine), instability that is disclosed in both `case.json` and the Guide Notes — not silently hidden — passes as **PASS (disclosed)** rather than a mechanical FAIL. The margin-formula artifact (huge nominal % swings when `B`'s base value straddles a near-zero net-benefit function) is a known formula-shape quirk at this base, not an independent finding — the real, substantiated instability is the flip itself, already disclosed. |
| **P6 data decay** | **PASS** | All three `sources[].url` fetched live 2026-08-17: **S1** (Can Manufacturers Institute, cancentral.com) reachable, states "Body Outside Diameter 2.602 ± .007" with "ANC 2.600 Nominal" and "Flange Can Height 4.812 ± .015" — both cited figures still present verbatim. **S2** (MatWeb 3104-H19 datasheet, university mirror) reachable, states "Density 2.72 g/cc / 0.0983 lb/in³ / AA; Typical" — cited figure still present verbatim. **S3** (USGS *Mineral Industry Surveys: Aluminum in January 2026*, S3-hosted PDF) reachable, states "The January 2026 average U.S. spot market price of primary aluminum ingot was $2.42 per pound, 10 percent more than that in December 2025 and 71 percent more than that in January 2025" — cited figure still present verbatim. No URL moved, no URL 404'd, no cited figure decayed. All three sources are 4 days old at accessed date, well under the 365-day staleness flag. |

**Net effect of this pass:** no defect found or fixed. The case's headline finding — a narrow,
disclosed 6.24% margin that genuinely flips under any single stated assumption's ±50% swing — was
already fully disclosed in `case.json.sensitivity_disclosure[]` and `FACILITATOR.md` before this
run; P1–P6 independently re-derive and confirm it rather than surface anything new.

## case.json.qa (written by this run)
```json
{"state": "TIER2_PASS", "verdict": "PASS", "run_on": "2026-08-17", "blockers_open": 0,
 "gaps_open": 3, "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS (N/A)",
 "P5": "PASS (disclosed)", "P6": "PASS"},
 "case_md_sha256": "27078268cb909225dd689124b5f6885603835b6e454ab0e5e73822e8c29db49d"}
```

**Next step:** `case-publish` may run (Tier 1 clean, Tier 2 all-PASS). Tier 3 (human dry-run) is
still required for `VERIFIED` and has not been attempted.
