# QA Report — The Weekly Rate

## case-readiness run — 2026-09-10
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight lint
Clean — no advisory findings (Modeling-Assumptions leak check, FLEX/sources overlap check).

### Tier 1 — structural (21 checks)
20 PASS, 1 GAP-carveout (T1-10, reinforcement), 1 GAP (T1-16, pre-QA-hash — expected on a
first run, resolved below by this report). 0 BLOCKERs.

| id | result | note |
|---|---|---|
| T1-01..T1-09 | PASS | structural sections, boilerplate, appendices, balance test, case.json schema all clean |
| T1-10 | GAP (carve-out) | `new_coverage[]` empty by design — see `case.json.reinforcement_note`. Reinforces 5 genuine n=2 singletons (Like Terms, Distributive Property, both multi-step-equation how-tos, X-Intercept, "how to write a linear equation given a graph") from a distinct real-world grounding (NYC gig-delivery e-bike buy-vs-subscribe) than any other case this session. |
| T1-11..T1-15 | PASS | learning-goal mutual reachability, tier check, facilitator artifacts, continuity (guide ↔ case, published artifacts ↔ sources) all clean after fixing: Overview load-bearing numerals (21-month horizon, battery %), a Socratic-questions line-wrap regex miss, and orphan derived numbers (charging/maintenance precision, twist week split) moved into `case.json.derived` |
| T1-16 | GAP | resolved by this report's `qa` block below (hash now recorded) |
| T1-17..T1-21 | PASS | cohort bands, interactive HTML fresh/leak-free, math glossary (11 terms, allowlisted), visual asset present, STORY_GLOSSARY (7 terms: Zoomo, Whizz, RadRunner 3 Plus, UL Certification, Independent Contractor, Deliverista, Dashing — all real fetched sources, non-math domains) |

Fixes applied during this run: Overview rewritten to remove the load-bearing "21 months" figure
and the decorative "61 percent" battery numeral (kept "9:00 p.m." as auto-classified clock
texture); Five Socratic Questions reformatted onto single lines (the line-wrap in the original
draft made every question invisible to the regex); `case.json.derived.cost_breakdown` extended
with full-precision charging/maintenance figures, the twist's week-40/41/51 split, and the timed
Socratic plan's minute markers so FACILITATOR.md and the published docx no longer read as having
orphan numbers; a "single weeky term" typo fixed in case.md D3; "UL safety certification" reworded
to "UL Certification" so it matches the STORY_GLOSSARY key and gets auto-glossed at first mention;
build helper scripts moved out of `published/` (they aren't part of the shipped packet and were
tripping the artifact-staleness check).

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Worked the packet cold: derived C_A(w)=2299+18.2937w, C_B(w)=39.986w; break-even ≈105.98 wk; at w=91, A=$3963.72, B=$3638.72, margin 8.20%, B (Subscription) wins. Reached the recorded answer by the intended route (derive → solve system → evaluate at horizon → convert to percent), not by guessing. Named the metric (total cost at Dara's 91-week horizon), the strongest counter-argument (break-even is only ~15 weeks past her horizon — a small mileage/maintenance swing could flip it), the most sensitive assumption (MA4, decision horizon), an appendix item correctly ignored (Appendix B's Whizz plan — a real distractor), and the least-supported figure (MA3's $900/yr maintenance estimate, an author extrapolation beyond the cited commuter range). |
| P2 both-sides | **PASS** | A's best sentence: "Ownership's weekly rate is under half Subscription's, so every week ridden past the ~106-week break-even point is money saved with no ceiling." B's best sentence: "Over the actual 91 weeks Dara is committed to — 15 weeks short of break-even — Subscription is $325.00 (8.2%) cheaper and carries zero repair risk." Neither side collapses into a concession; both survive first-pressure questioning by engaging the horizon assumption directly (which is the case's intended tension, not a design flaw), consistent with `sensitivity_disclosure[]`. |
| P3 trap | **PASS** | Cold read of the packet alone named the same wrong path the guide anticipates: computing the ~106-week break-even, seeing Ownership win "eventually," and recommending it without checking that Dara's own 91-week horizon falls short of that break-even. `FACILITATOR.md`'s named trap matches exactly. |
| P4 twist | **PASS** | (1) The twist invalidates a room's confident "Subscription is just cheaper" position by showing that premise depends on Zoomo's rate staying flat for all 91 weeks. (2) Re-derived under every reading of Appendix C's four assumptions: the twist changes only `subscription_weekly_rate` for weeks 41-91 and touches none of MA1-MA4, so there is no ambiguous convention for it to depend on. `sensitivity_model.py.evaluate_twist()` confirms the recompute mechanically: base margin 8.20% (B wins) → twist margin 4.62% (A wins) — a genuine winner flip grounded in a real, cited precedent (S5a, Zoomo's own documented past 26% rate increase on an equivalent plan), not an invented number. |
| P5 sensitivity | **PASS (disclosed)** | Machine-run: sweeping `FLEX = [decision_horizon_weeks, annual_maintenance_cost, charging_range_low_mi]` at ±50% finds `decision_horizon_weeks` (+50% flips to A at 12.13%; -50% breaks the 20% cap at 41.90%) and `annual_maintenance_cost` (-50% flips to A at 12.71%; +50% breaks the cap at 23.42%) genuinely unstable — both are disclosed, with basis and category, in `case.json.sensitivity_disclosure[]`, `FACILITATOR.md`'s sensitivity note, and Socratic Questions 1/2. `charging_range_low_mi` is stable (margin moves under 0.3 points either direction). Per the 2026-08-13 disclosure-aware pass rule, disclosed-not-eliminated instability is a PASS, not a FAIL. |
| P6 data decay | **PASS** | All 7 cited URLs were fetched live during this session's research pass (2026-09-10, same day as this QA run — age 0d): S1 (ridezoomo.com/us/home, Standard Plan $39/week confirmed present), S2 (electricbikereview.com RadRunner 3 Plus review, $2,299/672Wh/25-45mi confirmed), S3 (eia.gov Table 5.6.A, $0.1834/kWh June 2026 confirmed, primary), S4 (hovsco.com maintenance breakdown confirmed), S5a (ridezoomo.com blog, $39→$49 Flex Plan history confirmed), S5b (getwhizz.com Philadelphia pricing, $69/week + $99 deposit confirmed), S6 (nyc.gov Mayor's Office Deliverista Hub release confirmed). Zero 404s, zero moved URLs, zero figures that resolved but no longer matched. |
| P7 accessibility | **PASS** | Mechanical pre-screen: matched deliverable D5 (graph language), 4 genuine visuals found in the published HTML (Appendix B's real Whizz-plan SVG line chart, the D5 worked-example SVG, plus the shell's standard iconography) — 0 missing-visual findings. Qualitative cold-read of the built packet (`/tmp/coldread-the-weekly-rate/PACKET.md`, sourced from the published Interactive HTML with GLOSSARY/STORY_GLOSSARY terms inlined at first mention): read the full packet with zero assumed background. Every real-world domain term (Zoomo, Whizz, RadRunner 3 Plus, UL Certification, Independent Contractor, Deliverista, Dashing) is auto-glossed inline at its first mention. Two minor un-glossed flavor details remain ("48V, 14Ah" battery notation, "U-lock") but neither is needed to solve the case and both are clear enough from context — 0 concepts named as genuinely blocking, comfortably within the 0-1 PASS threshold. |

**Tier 2 result: 7/7 probes recorded, 0 FAIL. TIER2_PASS.**

### Tier 3 — human dry-run
NOT RUN — no cohort has run this case yet. `PUBLISHED` does not require Tier 3; `VERIFIED` does.

---

## Remediation pass — 2026-09-10 (later same day) — reviewer feedback: "has no pictures," graph/section correctness check

**Trigger:** direct reviewer feedback on the published Interactive HTML — no e-bike picture; the deliverables checklist reads as an answer key with no process explanation; needs more hover/hyperlink context; explicit request to verify individual sections and graphs are actually correct rather than assumed correct.

**Changes made:**
1. **Visuals.** Added a labeled, not-to-scale inline-SVG illustration of a step-through delivery e-bike (battery, rear cargo rack, callouts to both real prices) in Background, right after the option-comparison card. Verified both existing cost-function graphs by hand:
   - **Bug found and fixed:** Appendix B's Whizz distractor SVG drew its cost line flat (`y1=195` to `y2=195`) instead of sloping from the $99 deposit point to the $69/week-rate point at `(390,35)` — the marked (4, 375) dot was floating disconnected above a horizontal line. Fixed to `y2=35` so the line actually connects both marked points.
   - **Bug found and fixed:** the D5 "worked example" (fictional Mercury/Vesta lines, used to teach the graphing technique without leaking Dara's real numbers) had its "intersection" marker at a pixel position that was mathematically off both drawn lines by ~8-48px. Recomputed the true line-line intersection and moved the marker/label to the correct pixel.
   - Relabeled the worked-example card "Step 5" and renumbered the old Step 5 (D6, total-cost-at-horizon) to Step 6, closing a numbering gap that made D5 look skipped.
2. **Checklist as process guide.** `DELIVERABLES` gained a 3rd array element per item — a "Why" line explaining the *reasoning* for that step (e.g. why a break-even point matters, why the Whizz graph is a distractor) without stating any numeric answer or the verdict. `renderChecklist()` updated to render it under each label.
3. **Glossary.** Added "Linear Equation" (mathsisfun.com, fetched and confirmed) to `GLOSSARY` and "Watt-Hour (Wh)" (eia.gov, fetched and confirmed) to `STORY_GLOSSARY`; Challenge 3's D1 text reworded so "linear equation" appears in prose and gets auto-linked, not just listed in Appendix E.
4. **Correctness verification (not just re-asserted).** Ran `sensitivity_model.py` and a hand-written Node port of the HTML's `evaluate()`/`costBreakdown()` side by side: `A_cost=$3963.7222144`, `B_cost=$3638.7222144`, `breakeven=105.982...wk`, `margin=8.19936...%` — bit-for-bit identical between Python and the shipped JS. The JS port has not drifted.
5. **P6 data-decay re-check turned up two real findings**, both on non-critical figures: S2 (RadRunner 3 Plus price) now shows $2,229 on a fresh fetch vs. the $2,299 cited (a $70/~3% drift — does not flip the winner or breach the 20% margin cap even worst-case); S5b (Whizz) no longer shows the $99 deposit at all, and the $69/week plan is now labeled "Storm-2," not "Storm-1" as originally cited. Fixed the plan-name label everywhere (case.md, case.json, HTML, build scripts) since it's a clean correction. Left the $2,299 and $99 figures as originally cited (MCS-21 — don't silently swap in a new number from a single fetch that could be a momentary promo) and added a dated re-verification disclosure to Appendix D in both case.md and the HTML, plus a `note` field update on `case.json.sources` S2/S5b, flagging both for re-verification before the next reprint.

### Tier 2 — re-adjudication (all 7 probes)

| probe | verdict | note |
|---|---|---|
| P1 cold solve | **PASS** | Re-worked cold from the rebuilt packet; arithmetic unchanged (A=$3963.72, B=$3638.72, margin 8.2%, B wins) — none of this pass's changes touch `PARAMS` or the model. |
| P2 both-sides | **PASS** | Unaffected by this pass — no change to either side's supporting figures. |
| P3 trap | **PASS** | Trap (mistaking "eventually cheaper" for "cheaper on Dara's actual horizon") is unaffected; still named correctly in `FACILITATOR.md`. |
| P4 twist | **PASS** | `evaluateTwist()` re-verified against `sensitivity_model.py.evaluate_twist()` numerically — matches (base margin 8.2% B wins → twist margin 4.62% A wins). |
| P5 sensitivity | **PASS (disclosed)** | Re-run mechanically; unchanged from the original pass (no PARAMS touched this cycle). |
| P6 data decay | **PASS (2 drifts disclosed)** | Re-fetched all 7 sources live this pass. 5 of 7 (S1, S3, S4, S5a, S6) confirmed unchanged. S2 and S5b show drift (see above) — neither is a 404/dead link, neither changes the balance-test verdict, both are now disclosed in Appendix D and `case.json.sources[].note` rather than silently left stale. This is the "resolves but no longer matches" failure mode P6 exists to catch, and it did. |
| P7 accessibility | **PASS** | Illustration and both graph fixes make the packet stronger, not weaker, on this axis. Cold-read of the rebuilt packet end-to-end: every real-world term including the two new glossary additions is glossed at first mention; the same two flavor details as before ("48V, 14Ah", "U-lock") remain un-glossed but non-blocking — still comfortably within threshold. |

**Tier 2 result: 7/7 probes recorded, 0 FAIL, 2 disclosed data-decay findings (non-blocking). TIER2_PASS.**
