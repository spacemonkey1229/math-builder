## case-readiness run — 2026-08-19
**State:** DRAFT → TIER1_PASS → TIER2 attempted (1 probe FAIL, does not reach TIER2_PASS)
**Verdict:** TIER1_PASS (Tier 2 blocked by P4)

### Tier 1 — structural (19 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case robotics-engineer`
sha256(case.md) = `57c6f9ead4cb8e81f9221c70583a43f1559641907275694e9c9d01adafc242d0` (unchanged from the
2026-08-05 pass recorded in `case.json.qa`)

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | POLISH: parsed 13 Appendix E labels (5 bulleted, 8 separator-run) |
| T1-08 | PASS | |
| T1-09 | PASS | |
| T1-10 | PASS | |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | PASS | |
| T1-14 | GAP | 1 number in FACILITATOR.md (`21.0`) appears in neither case.md nor case.json — a guide-only derived figure (looks like a rounded twist-route minute value); should move into `case.json.derived` so it stays checkable, not a blocker |
| T1-15 | PASS | |
| T1-16 | PASS | |
| T1-17 | PASS | |
| T1-18 | GAP | 35 numbers in the interactive HTML's prose/markup (outside `<script>`) don't resolve against case.md/case.json — pre-existing, not introduced by this run |
| T1-19 | PASS | |

**BLOCKER (0)** — none.
**GAP (2)** — T1-14, T1-18 as above (both pre-existing, carried from the 2026-08-05 pass; not
re-caused by anything in this Tier 2 run).
**POLISH (1)** — T1-07 Appendix E label-count note.

VERDICT: TIER1_PASS (0 blockers, 2 gaps) — unchanged from before this run.

### Tier 2 — simulated play (6 probes)
`sensitivity_model.py` authored this run (`cases/robotics-engineer/sensitivity_model.py`) —
`evaluate()` reproduces `case.json.derived`'s base route times exactly (C-A-B = 20.896 min,
C-B-A = 20.135 min, winner C-B-A, margin 3.78%) and `evaluate_twist()` reproduces the twist's
detour numbers exactly (21.686 / 20.925 min, margin 3.64%). `FLEX = []` by design — see finding
under P5.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Genuinely fresh subagent, given only `/tmp/coldsolve-robotics-engineer/PACKET.md`, chose Option B, reproduced every one of the case's own derived numbers exactly (distances 12.042/10.817/21.587 m; route times 20.899/20.138 min; Container B integrity 92.58%/92.87%; correct triangle-inequality check), correctly named "total travel time" as the optimized metric, and — critically — when asked for the strongest argument against its own choice, independently surfaced Container A's total data absence as a real, unresolved risk ("purchased for a 46-second time savings"). Correct answer reached for the right reasons, with the case's central tension explicitly engaged, not glossed over. |
| P2 both-sides | **PASS** | Built independently from the packet: Argument A (reach the unmonitored Container A ~12.65 min sooner, hedging an unquantified risk) and Argument B (measurably faster total time, 3.78% margin, and better-preserved Container B integrity, the one container with a real decay number) both carry genuine numbers and neither reads as a concession. Argument A's quantitative core is real (the exposure-window minutes) but its link to actual risk-to-A is inherently unquantifiable — by the case's own design (`modeling_assumptions` MA3: "no number is invented for Container A"), not a defect; this is the deliberate known-vs-unknown-risk tension the case is built around, not a collapse. Margin is not a paper number. |
| P3 trap | **PASS** (qualified) | FACILITATOR.md names: a Hero computes total time, finds C→B→A faster, and stops there without ever weighing Container A's missing data. A second fresh subagent, given only the packet and asked to name the wrong path *before* seeing the guide, proposed a different candidate trap (conflating "faster overall" with "better for Container B specifically") — but that proposed trap does not actually hold up: in this case's real numbers the faster route (C-B-A) is *also* the route that best preserves Container B, so there is no real tradeoff there to fall into. It is not evidence of a second, unanticipated trap. Independently, P1's solver's own first-pass reasoning (Q1–3, before being asked for a counter-argument) stopped exactly where the guide predicts — at total time plus Container B's integrity — and only surfaced Container A when explicitly prompted for a counter-argument. That is strong direct evidence the guide's named trap is the real one a default solve falls into. |
| P4 twist | **FAIL** | The twist (secondary explosion blocks the direct A–B leg; Ultron detours via C's position) adds an identical extra distance to the A–B leg for *both* route orders, because both route orders traverse the A–B leg exactly once. This is a structural property of the case's own geometry, not an estimation artifact: algebraically, adding a constant to one shared leg shifts both routes' total time by the same amount, so the absolute gap between the two routes is invariant and the winner cannot change under any detour distance. Recomputed mechanically with `evaluate_twist()`: winner is unchanged (C-B-A both before and after) and the absolute time gap is exactly unchanged (0.7611 min before, 0.7611 min after, to 4+ decimal places — not "roughly stable," algebraically identical). Per this skill's own P4 criterion, this fails "does the twist invalidate at least one position a real room would hold?" — no position becomes indefensible; nobody who held either view before the twist is wrong afterward. FACILITATOR.md is self-aware of the surface symptom ("if the order didn't change, what was the point of that twist?") and frames it as an intentional lesson about model robustness — a legitimate discussion move, but it does not satisfy the mechanical P4 bar this skill sets, which explicitly treats "winner and margin both unmoved" as a fail condition. This is a real defect to report, not fixed here per "Never fix the case." |
| P5 sensitivity | **PASS** (trivial — see finding) | `sensitivity_model.py` declares `FLEX = []`. This is deliberate, not an omission: every numeric quantity in this case's arithmetic is either (a) real/given case data the author cites or measures directly (the three site coordinates read off Appendix A's map; Ultron's 0.06 mph rough-terrain speed, a stated Background design spec; Container B's 93%/−1.2%-per-hour integrity reading, Appendix B) — P6's territory, not P5's — or (b) a purely binary modeling convention with no continuous numeric dial to flex ±50% (Appendix C Assumption 1: uniform-terrain, no locally-faster shortcut modeled; Assumption 2: straight-line legs, no mid-route climb pause). Unlike Cold Chain's `opening_cost_h` or `allocation_village_priority`, there is no author-chosen numeric fudge factor anywhere in this case's balance-test arithmetic. Running `tier2_probes.py --probe 5 --flex 0.5` against the model confirms: 0 dials swept, mechanical PASS by construction. This is an honest, thin result — it means P5 could not meaningfully stress-test an assumption dial because none exists, not that the case was tested and found stable. |
| P6 data decay | **PASS** | `case.json.sources[]` is empty — no cited external figure backs the balance test; every load-bearing number (site coordinates, robot speed, Container B's integrity/decay) is internal case content (Appendix A/B/Background), not sourced from an external URL, so the mechanical worklist is empty (confirmed via `tier2_probes.py --probe 6`). Additionally live-fetched, as a courtesy check, the five non-load-bearing "Learn More" links in Appendix D (explicitly marked "none of them are required to complete the Challenges"): all five reachable and topically correct as of 2026-08-19 — DARPA Robotics Challenge (Wikipedia), Robonaut (Wikipedia), Atlas (bostondynamics.com/atlas/), NTSB (ntsb.gov), NREC (nrec.ri.cmu.edu). None carries a load-bearing figure; no BLOCKER. |

**Mechanical result:** 0 probes failed the machine pre-screen; 1 probe (P4) fails on model-adjudicated
grounds. Tier 2 is not clean — `TIER2_PASS` is not reached.

### Tier 3 — human dry-run
NOT RUN. (Note: a prior real learner, ben-okafor, completed a full assign→submit→revise→resubmit→
discuss→complete cycle on this case per `student_work/ben-okafor/robotics-engineer/` — but per this
skill's own instruction that history was not used as evidence for this gate, and it is not a filed
`RUN_REPORT.md` in the required format regardless. No `cases/robotics-engineer/runs/RUN_*.md` exists.)
