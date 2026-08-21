## case-readiness run — 2026-08-20
**State:** TIER1_PASS → TIER2 run (clean)   **Verdict:** TIER2_PASS — 6 of 6 probes PASS

### Context: the fix this run verifies
An independent Tier 2 P2 (both-sides-solve) probe found a real structural bug: `case.json.derived`
computed different round-trip travel TIMES for Option A vs Option B (e.g. Eugene round trip 3.91 hr
vs 3.36 hr), but `avg_long_distance_deliveries_day` (4.5) and `avg_total_deliveries_day` (20.5) were
stored as fixed values that did not vary by option — making Option B a pure concession (higher fuel/
ticket/insurance cost, zero quantified capacity/bonus benefit). Fixed by building an honest
delivery-capacity model from Appendix C's own shift/break rules (5 vehicles x 2 shifts x 7.5 hr
available driving/shift = 75 vehicle-hr/day fleet capacity) and checking it against Appendix A's
route data across four independent allocation methods (fleet-pooled hours, weighted throughput,
per-route dedicated-vehicle ceiling, remaining-capacity-after-short-routes). All four honestly show
fleet capacity is never the binding constraint under either option (only 35-42% utilized) — so the
4.5/20.5 averages are correctly demand-bound, not speed-bound, and Josie's bonus stays genuinely out
of reach either way (not hidden, not fabricated around). The one real, quantified exception the same
math surfaces: a single vehicle dedicated only to the Eugene route clears 2 round trips/day under
Option A (short of Eugene's own 2.7/day demand — Option A needs a second, partially-dedicated
vehicle) vs. 4/day under Option B (covers Eugene alone). This is now Option B's genuine quantitative
counter in `balance.argument_b`, replacing the prior vague "speed has value" framing. See
`case.json.derived` (new shift/capacity fields), `case.md` Appendix A/C, `sensitivity_model.py`'s new
`capacity_check()`, and `case.json.legacy_conversion_note`/`sensitivity_note` for the full account.

Also fixed in this run: **S10** (Oregon traffic-fatality context) was cited to a Portland Bureau of
Transportation press release showing city-only figures (58/69), while the case's own value field
(539/587) is statewide — a genuine citation mismatch. Replaced with ODOT's own statewide safety page
(oregon.gov/odot/state-of-the-system/pages/safety.aspx), re-fetched 2026-08-20, which directly
confirms 539 (2024) / 587 (2023) statewide plus "speeding is a factor in 25% of fatal and serious-
injury crashes." **S7** (insurance-premium research) previously claimed an mph-bracket percentage
severity breakdown (11-12%/15%/30%+) that the live ValuePenguin page no longer supports — re-fetched
2026-08-20, the page now shows a near-flat rate table by mph bracket (<1.5% spread) and a much larger
ticket-COUNT-driven jump (24%/45%/60% for 1st/2nd/3rd ticket), which is what `case.json.derived` and
FACILITATOR.md's Twist already correctly used. `case.md`, `case.json.sources[]`, and FACILITATOR.md's
Twist text are now all consistent with the live sources.

### Tier 1 — structural
Re-run after the fixes above: `python3 skills/case-readiness/scripts/tier1_structural.py --case
medical-transport` -> **TIER1_PASS, 0 blockers, 2 gaps** (both pre-existing/accepted: T1-09 margin
17.26% inside the 20% cap but wide; T1-10 legacy-conversion new_coverage[] carve-out, doctrine-
approved). `case_md_sha256` in `case.json.qa` is current: `cc89b3432783817c...`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | A genuinely fresh subagent (leak-free packet only, no FACILITATOR.md/case.json) chose Option A, correctly named the primary metric (total annual operating cost/vehicle, reasoning that revenue and bonus-eligibility are identical across options per Appendix A's capacity check), and reproduced the fuel-penalty arithmetic correctly (mpg_hwy_A=35.34, mpg_fwy_A=30.57, matching `derived`). It used D1's literal deliverable scope (fuel + fines + surcharge, omitting the $1,453 fixed insurance base that both options share equally) rather than case.json's full "total" figure — a defensible reading of D1's own wording, not an arithmetic error; the margin still lands close to the recorded 17.26% once the shared base is added back symmetrically. Notably, **without any prompting**, it independently surfaced the new Eugene single-vehicle-dedication capacity argument as "the strongest argument against my choice" — real evidence the new Appendix A capacity-check paragraph is discoverable by a cold reader, not just asserted in facilitator material. |
| P2 both-sides | PASS (marginal) | Independent fresh subagent, case.md only: strongest A = ~$8,321 vs ~$9,772/vehicle/year (~17.4%), plus a real secondary safety argument (Power Model risk). Strongest B = the Eugene-capacity argument (2 round trips/day under A, short of demand, vs. 4/day under B) — assessed as "genuinely quantified, not hand-wavy," but narrow in scope (one route/vehicle) and not translated into the same dollar units as the cost table. Verdict: "B is no longer a pure concession... but this reads as a case that technically clears the bar rather than one where B is robustly, comparably defensible." Recorded as a PASS, not a robust one — flagged honestly rather than oversold. |
| P3 trap | PASS (after fix) | First pass: FAIL. A fresh subagent found a real, previously unanticipated trap: Appendix B's mpg penalty is keyed to *speed over 50 mph*, not to which option is "legal" — Option A's own highway (55mph, one 7% mpg cut) and freeway (65mph, three compounding cuts, ~19.6% loss) already pay a real fuel penalty, which a hurried student is likely to assume only applies to Option B given the A="legal"/B="speeding" framing. This would corrupt D1/D2's headline dollar figures, and FACILITATOR.md's existing two traps (freeway ticket misclassification, raw-mph-vs-relative-percent risk) never anticipated it. **Fixed**: added this as trap #3 in FACILITATOR.md's "The trap" section, with the exact mechanism, numbers, and a direct cold-call line for the facilitator. A second fresh subagent re-verified the updated text: PASS — the guide now names the error precisely enough for a facilitator to catch it live. |
| P4 twist | PASS | Independent fresh subagent, case.md + FACILITATOR.md: the ticket-count-variance twist genuinely invalidates the "compare two averages" framing a room defending B would hold (fleet-wide policy vs. per-vehicle average is a materially different question), and survives the case's own stated facts under the natural student reading — D1 asks for a per-vehicle average table with no prompt toward per-vehicle variance, so the twist isn't pre-empted, and it recombines only facts already stated in Appendix E (ticket-count-driven premium escalation, 4-ticket cap) rather than introducing anything unstated. One noted soft spot (the "roughly half the fleet" line leans on an unstated median≈mean assumption) doesn't undermine the twist since it's delivered as an open provocation, not a graded calculation. |
| P5 sensitivity | PASS (disclosed) | `python3 skills/case-readiness/scripts/tier2_probes.py --case medical-transport --probe 5` — unaffected by this run's fixes (capacity math and S7/S10 don't feed the cost metric or FLEX[] dials). Base: A=$8,319.97, B=$9,756.24, margin 17.3%. Sweeping the 2 declared dials (MA1 pullover_probability, MA2 annual_exposures_per_vehicle) at +/-50%: no winner flip at any flex; +50% on either dial pushes the margin to 20.8%, just over the 20% cap — disclosed in `sensitivity_disclosure[]` as a Category-X best-effort estimate, not eliminated. Same result as this case's prior (undocumented) internal check; nothing about this run's fixes touched MA1/MA2 or the cost-metric arithmetic. |
| P6 data decay | PASS | All 11 `sources[]` URLs checked live 2026-08-20. **S1** (fueleconomy.gov Focus page): reachable, confirms 26 city/38 highway mpg exactly. **S2** (fueleconomy.gov driving-habits): reachable, confirms both quoted claims verbatim ("decreases rapidly above 50 mph"; "$0.29/gal per 5 mph over 50"). **S4** (ORS 811.111): reachable, confirms 55/65 mph defaults. **S5** (ORS 811.109): reachable, confirms the D/C/B/A bracket structure and the posted-65+ exception exactly as cited. **S6** (ORS 153.019): reachable, confirms $440/$265/$165/$115 exactly. **S7** (ValuePenguin): reachable — re-fetch triggered the fix above; case.md/case.json now match the live page. **S8** (FHWA-HRT-17-098): reachable, confirms Nilsson/Elvik Power Model with matching exponent ranges (fatal ~4.1, serious-injury ~2.6-3.5, injury ~1.6-2.2). **S10** (now ODOT statewide safety page): reachable — re-fetch triggered the fix above; now matches the cited 539/587 statewide figures. **S11** (AAA Oregon gas price): reachable, confirms $4.7593/gal live snapshot, exact match. **S3** (PBOT PDF): reachable (200), but the fetch tool's text extraction from the 902KB PDF did not surface the 35-45 mph arterial figure in "visible content" — inconclusive rather than a confirmed drift; pre-existing MEDIUM confidence, unaffected by this run's fixes, not independently re-verified further given scope. **S9** (Waze live-map): a dynamic map URL, not independently re-verified this pass (pre-existing MEDIUM confidence aggregator estimate, unaffected by this run's fixes). Neither S3 nor S9 is a new finding — both were already flagged MEDIUM confidence before this run. |

### Tier 3 — human dry-run
NOT RUN.

### Final state
`case.json.qa.state` set to **TIER2_PASS**. `case-publish` may run when a human confirms. Tier 3
(a real cohort dry-run, filed as `runs/RUN_*.md`) remains required before `VERIFIED`.

### Honest caveats carried forward (not blockers, but real)
- P2's margin is a genuine but *marginal* pass — Option B's real counter-argument (Eugene capacity)
  is narrower in scope and not denominated in the same dollar units as Option A's cost advantage.
  A future pass could strengthen this further, but per SPEC section 2 it does not need to be equally
  weighted, only genuinely non-zero and quantified — which it now is.
- P5's sensitivity sweep shows the 17.26% margin breaches the 20% cap at +50% on either MA1 or MA2
  — both disclosed, unsourced, Category-X assumptions. This was true before this run and is
  unchanged by it; recorded here for visibility, not re-litigated.
- S3 (Portland arterial posted-speed range) and S9 (PDX-hospital distances) remain MEDIUM
  confidence; not re-verified beyond their pre-existing state in this pass.
