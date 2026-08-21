# QA Report — Catering

## case-readiness run — 2026-08-19
**State:** DRAFT → TIER1_PASS (Tier 2 run, 1 probe FAIL)   **Verdict:** TIER1_PASS (Tier 2 blocked; TIER2_PASS not reached)

### Tier 1 — structural (19 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS (POLISH) | 11 labels parsed (6 bulleted, 5 separator-run) |
| T1-08 | PASS | |
| T1-09 | GAP | margin 17.99% inside SPEC §2's 20% cap but wide — discussion risks being one-sided |
| T1-10 | GAP | `new_coverage[]` empty; legacy-conversion carve-out applies (title already credited in `standards_spine.json.covered_by[]`) |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | PASS | |
| T1-14 | GAP | 2 numbers in FACILITATOR.md (15.0, 200.0 — the twist's "+15 guests" and "grew by over $200") have no `case.json.derived` home; guide-only derived phrasing, not stale, but not machine-checkable as written |
| T1-15 | PASS | |
| T1-16 | PASS | |
| T1-17 | PASS | |
| T1-18 | GAP | 33 numbers in the interactive HTML's prose (outside `<script>`) not traceable to case.md/case.json — CSS/SVG/decorative decimal sweep, previously accepted class |
| T1-19 | PASS | |

BLOCKER (0): none.
GAP (4): T1-09, T1-10, T1-14, T1-18 — all pre-existing, accepted classes per this case's prior TIER1_PASS run (2026-08-04); re-verified unchanged on this pass.

### Tier 2 — simulated play (6 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh subagent, given only the leak-free packet (`/tmp/coldsolve-catering/PACKET.md`) and the 7 questions, chose **B (Adobitron)**. Its arithmetic reproduced every one of the case's derived figures exactly (servings 118/107, revenue $3,186.00/$3,135.10, net profit $897.42/$760.62, D5 thresholds 123/122 servings) and its reasoning explicitly rested on the Background's own stated recurring-client signal, not a guess — it also independently surfaced that neither event's net profit alone covers the $950 loan. This is a defensible position reached for the right reasons with correct arithmetic (this case has no single "correct" side — it's a balance case — so the pass criterion is defensible-reasoning-plus-correct-math, which it met). |
| P2 both-sides | **PASS** | Argument A (wedding): $897.42 net profit, the highest real number, consistent per-serving margins, closest to covering the $950 loan (short by only 5 servings / $52.58). Argument B (corporate): $760.62 net profit — lower but real — on a smaller order, with the Background's own stated fact that corporate clients recur while wedding clients are one-off; the trade is "$137 less today for the client type the business needs to survive year two." Neither side collapses: both carry genuine numbers and neither reduces to a bare concession. Machine pre-screen also reported `READY` (no fabricated-support or concession-pattern flags). |
| P3 trap | **PASS** | Machine pre-screen mechanically **FAILED** — its verb-form regex (`assumes|forgets|misses|skips|defaults...`) did not match FACILITATOR.md's actual trap phrasing ("...finds the wedding ahead, and stops — never engaging with the Background's own signal..."), a false negative in the script, not a defect in the case (the trap does describe a concrete wrong action: compute net profit, stop, never engage with the recurring-client signal). A second genuinely fresh subagent, given only the packet, named the trap *before* seeing the guide as: "picking the higher one-time net profit (Beal wedding) while ignoring the recurring-revenue signal the case is actually testing" — plus, unprompted, the same D5 loan-shortfall angle FACILITATOR.md flags. This matches FACILITATOR.md's trap closely. **Finding (script, not case): `probe_trap`'s verb-form regex in `tier2_probes.py` needs `engag(e|es|ed|ing)` (or similar) added — it currently misses a legitimate trap phrased as "stops...never engaging" because none of its listed verb forms occur in that sentence.** |
| P4 twist | **PASS** | Mechanically recomputed via `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()`: base A=$897.42/B=$760.62 (A ahead 17.99%/18.0%); twist (wedding +15 guests → 134 buffered servings) → A=$1,098.86/B=$760.62 (A ahead ~44.5%). The twist does not flip the winner, but it does invalidate the specific real-room position "the wedding's lead is thin enough that the recurring-client trade tips it" — the gap it has to argue against grows by over $200, exactly as FACILITATOR.md's Deep Conflict thread 1 anticipates. Re-derived under the case's own stated conventions (7% buffer rounds up, same menu/fees, event length unchanged, delivery mileage unchanged) — the twist's effect does not depend on any convention the case leaves unstated; only guest count changes, per its own text ("Fifteen more guests are coming to the Beal wedding"). |
| P5 sensitivity | **FAIL** | `sensitivity_model.py` ships `PARAMS`/`FLEX = [buffer_pct, wedding_miles, corporate_miles]` (the case's own two named `modeling_assumptions`, MA1/MA2) and reproduces every base and twist figure exactly. Flexed ±50%: `buffer_pct` and `wedding_miles` stay stable (margin moves within 16.8%–18.9%, verdict never flips). **`corporate_miles` +50% (18mi → 27mi) pushes the margin to 20.3%, breaking SPEC §2's 20% cap** — a real, reproducible instability, not a script artifact. `case.json` has no `sensitivity_disclosure[]` entry for `corporate_miles`, so this does not qualify for a disclosed pass. This is a genuine, undisclosed finding to hand back to case-write/case-research, not something fixed here. |
| P6 data decay | **PASS** | `case.json.sources[]` is empty — by design: `legacy_conversion_note` discloses all menu/fee/loan data as invented fictional scenario data, not sourced from or representing any real external entity, so there is nothing load-bearing to fetch. As due diligence, the four supplementary Appendix E "Learn More" links (not `sources[]`, not load-bearing to any case figure) were fetched live: Lightspeed's food-cost-percentage article (reachable, states the formula as claimed), Fooda's corporate-catering blog (reachable, confirms the "repeatable process" claim), the SBA loans page (reachable, official SBA content as claimed), and the Khan Academy multi-step-ratio-and-proportion article (reachable/200, but content could not be extracted through this fetch tool — it is a JS-rendered SPA; URL path is a standard, plausible KA slug for the claimed topic, not independently content-verified). None are dead; none are misrepresented where verifiable. |

### Tier 3 — human dry-run
NOT RUN.

---

### Overall
**TIER2_PASS not reached.** 5 of 6 probes PASS; P5 (assumption sensitivity) genuinely FAILs on an undisclosed instability (`corporate_miles` +50% breaks the SPEC §2 20% margin cap). Per doctrine ("Never fix the case"), this QA run does not add a `sensitivity_disclosure[]` entry or otherwise touch the case content — that is case-write/case-research's call: either disclose `corporate_miles` in `case.json.sensitivity_disclosure[]` with a real category (F/X/I) and justification, or retune the corporate delivery-mileage estimate/fee structure so the margin no longer breaches the cap at +50%.

Also flagged, not fixed: `skills/case-readiness/scripts/tier2_probes.py`'s `probe_trap` verb-form regex produced a false-negative mechanical FAIL on this case's (real, well-written) trap — worth a script fix, filed separately, not a case defect.

**Next step:** Resolve the P5 finding (disclose or retune `corporate_miles`), then re-run `tier2_probes.py --case catering --probe 5 --flex 0.5`. Once P5 records PASS or PASS (disclosed), all six Tier 2 verdicts will be clean and `case.json.qa.state` can move to `TIER2_PASS`.

---

## P5 remediation — 2026-08-20

Resolved the P5 finding from the 2026-08-19 run above by disclosure (Option A), not retuning.
`corporate_miles` (18 miles round trip to Adobitron HQ, Appendix C Assumption 2) is already stated
in `case.md` itself as "a reasonable estimate for the area, not a routed, sourced figure" for a
fictional company with no real address to route a distance against — there is no more-precise real
mileage to look up, so retuning the number would just be picking a different unsourced value
rather than fixing anything. Disclosure is the honest fix, matching this project's own pattern on
Cold Chain (`in_spec_fraction`) and Family Trip (`fare_per_leg_usd`, `hotel_rate_per_night_usd`).

Added a top-level `case.json.sensitivity_disclosure[]` entry:
```json
{
  "param": "corporate_miles",
  "category": "F",
  "justification": "... (see case.json for full text) ..."
}
```
Category F (forecast/irreducible-unknown): Adobitron is an invented company for this case, so
`corporate_miles` cannot be tightened by further research the way a real business's routed
distance could be. Also added a paragraph to `FACILITATOR.md`'s Lessons Learned section so a
facilitator who gets pushed on "what if the mileage estimate is off" has the honest answer on
hand (the instability is real, specific to `corporate_miles`, and does not touch `wedding_miles`
or `buffer_pct`, both of which stay stable across the full ±50% range).

Re-ran `python3 skills/case-readiness/scripts/tier2_probes.py --case catering --probe 5 --flex 0.5`:
`machine_status` now reports **`PASS (disclosed)`** — `corporate_miles +50%` still breaks the
SPEC §2 20% cap (margin 20.3%) exactly as before (the underlying instability is disclosed, not
eliminated, matching the project's disclosure-aware pass state), but the run now finds a matching
`sensitivity_disclosure[]` entry for every unstable param, so it is no longer an undisclosed FAIL.
`buffer_pct` and `wedding_miles` remain stable across the same ±50% sweep, unchanged from the prior
run.

Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case catering`: unchanged from
the last Tier 1 run — `TIER1_PASS`, 0 blockers, 4 GAP (same accepted classes as before: T1-09
margin-width, T1-10 legacy-conversion new_coverage carve-out, T1-14/T1-18 continuity). The two new
`FACILITATOR.md` numbers this edit introduced (17.99%/20.3%, 18/27 miles) are already traceable to
`case.json` (the new `sensitivity_disclosure[]` entry and existing `derived`/`modeling_assumptions`
fields), so T1-14's orphan-number count did not increase.

P1-P4 and P6 were not re-run — this remediation touched only P5's disclosure and did not change
any menu/fee/loan/mileage figure, D1-D6 arithmetic, the trap, the twist, or any cited source, so
the 2026-08-19 verdicts for those five probes stand unchanged.

**Overall: all 6 Tier 2 probes now clean** (P1 PASS, P2 PASS, P3 PASS, P4 PASS, P5 PASS (disclosed),
P6 PASS). `case.json.qa.state` moved to `TIER2_PASS`.
