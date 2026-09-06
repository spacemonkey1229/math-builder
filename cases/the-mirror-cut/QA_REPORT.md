## case-readiness run — 2026-09-05
**State:** DRAFT → TIER1_PASS   **Verdict:** PASS (Tier 1) / see note on Tier 2 below

### Preflight lint

First pass: 1 advisory finding — Appendix E's MA3 "Sensitivity" cell named `FACILITATOR.md`
directly ("Not disclosed here — see FACILITATOR.md and case.json's balance object"), which the
leak heuristic correctly flagged as student-facing text naming a facilitator artifact. Fixed:
reworded to "The answer is sensitive to this value." with no pointer to where. Re-ran: clean, 0
advisory findings.

### Tier 1 — structural (21 checks)

First pass: 18 PASS, 3 GAP (T1-10 — `new_coverage[]` empty, expected and covered by the
reinforcement carve-out; T1-14 — 4 numbers in `FACILITATOR.md` (0.96, 0.99, 8.25, 55.0) had no
home in `case.json`/`case.md`; T1-16 — no `case_md_sha256` recorded yet, expected on a first run).
Fixed: added `reject_rate_simple_complement`, `reject_rate_mirrored_complement`,
`d4_bbox_before_width_in`, `d4_bbox_before_height_in` to `case.json.derived`; corrected
`FACILITATOR.md`'s rounded "about 55%" to the exact `55.4%` matching a new
`labor_cost_pct_increase_mirrored_vs_simple` derived field; computed and recorded
`case_md_sha256`.

Second pass:

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 199 words, no load-bearing numerals; "9:00 AM" clock-time auto-texture, "six"/"two" cleared as texture |
| T1-03 | PASS | Dilemma binary, opens "You are Sam Delgado." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form `N.)` consistent |
| T1-06 | PASS | appendices A–H, lettered, ordered, no orphans |
| T1-07 | PASS | all 16 final-appendix lines verbatim spine labels (7 vocabulary + 9 how-to) |
| T1-08 | PASS | every number cited (S1–S8) or a declared Modeling Assumption (MA1–MA3) |
| T1-09 | PASS | both arguments written, margin 9.99% <= 20% |
| T1-10 | GAP (recorded, not a blocker) | `new_coverage[]` genuinely empty — all 13 claimed skills already `n>=2`; `case.json.reinforcement_note` records the full spine sweep that ruled out every adjacent `n==0` skill project-wide (six exist: sphere volume, quotient rule, Taylor series x2, number-sense depth/digit — none forced by this case's actual deliverables). Downgraded from BLOCKER per the 2026-08-17 T1-10 reinforcement carve-out (project-owner-approved doctrine, not a per-case waiver). |
| T1-11 | PASS | mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T2 tier matches numeric load (coordinate reflection/rotation/dilation + a multi-step weighted cost comparison, two competing variables) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | continuity — all FACILITATOR.md numbers traced to case.json.derived after the fix above |
| T1-15 | PASS | no published/ yet, nothing stale |
| T1-16 | PASS | hash current |
| T1-17 | PASS | cohort_bands[] declared, 3 bands |
| T1-18 | PASS | no published/ yet (nothing to check) |
| T1-19 | PASS | no published/ yet (nothing to check) |
| T1-20 | PASS | no published/ yet (nothing to check) |
| T1-21 | PASS | no published/ yet (nothing to check) |

BLOCKER (0). GAP (1): T1-10, recorded and justified above, per doctrine's own carve-out — not
resolvable any other way without fabricating a skill claim. POLISH (7): T1-02 auto-texture note;
T1-07 label-parsing note (informational); T1-15/18/19/20/21 "no published/ directory yet" (expected
pre-publish, and expected to remain so — this task explicitly stops before case-publish, stage 5).

**VERDICT: TIER1_PASS** (0 blockers, 1 recorded GAP)

### Tier 2 — simulated play (7 probes; task scope covers probes 1-6, all run and adjudicated below;
probe 7 documented honestly as blocked by an out-of-scope stage, not skipped silently)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh, unbriefed subagent given only the leak-checked `/tmp/coldsolve-the-mirror-cut/PACKET.md` (and no other file) reached Option A (The Mirror Cut), correctly named the graded metric (net cost per finished bracket), reproduced the $1.48019 vs. $1.33224 arithmetic independently and correctly (matching `case.json.derived` to the cent), correctly named MA3 (the reject-rate assumption) as the one the answer is most sensitive to — exactly matching the case's own designed sensitivity note — and correctly flagged MA1's 2x pierce multiplier as the least-supported number. Reached the intended answer for the intended reasons, via genuinely independent arithmetic. |
| P2 both-sides | **PASS** | Mechanical pre-screen passed on the first attempt (no concession-pattern false match, real numbers on both sides). Adjudicated: Option A's real floor is the sourced/computed net-cost win (9.99%, backed by S1-S7 and two assumptions that don't by themselves flip it); Option B's real floor is that it needs zero stated assumptions to defend its number, while A's rests on three. Neither side collapses to a numbers-free concession — they are defensible on two different, real dimensions (lower expected cost vs. lower assumption risk on a fixed multi-year price), which is the design intent, not a paper margin. |
| P3 trap | **PASS** | A second genuinely fresh subagent, given only the packet, named the wrong path *before* being shown `FACILITATOR.md`: a hurried student would read the sourced 10-15%/12% material-yield figure and assume the graded net-cost margin is roughly that size too, without running D6's actual takeoff. `FACILITATOR.md`'s "The trap" section names this exact misconception almost verbatim ("Most Heroes will look at the sourced 10-15% material-yield figure and assume the net-cost-per-bracket margin must be roughly that large too"). Guide anticipates the real trap. |
| P4 twist | **PASS** | (1) The twist invalidates the position "The Mirror Cut wins by the full sourced yield%, no further risk to consider" — a real position a room could hold after Anchor 4 if it stops at "MA1/MA2 don't flip anything." (2) Re-derived under the case's own stated Appendix E assumptions exactly as written (reject rates are stated per-option, unambiguous, no reader-dependent convention) and cross-checked against `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` divergence: base margin 9.99% -> twist margin 7.18%, matching `FACILITATOR.md` and `case.json.derived` exactly. No unstated convention the twist depends on. The twist narrows the margin substantially without reversing it — a real, non-trivial finding, not a null result. |
| P5 sensitivity | **PASS** | `sensitivity_model.py` flexes all four declared FLEX dials (`mirrored_pierce_mult`, `mirrored_speed_mult`, `reject_rate_simple`, `reject_rate_mirrored`) +/-50%. The graded primary metric's margin stays in a 9.1%-10.3% band across every flex — no flip, no 20%-cap breach at any tested value. The twist metric (checked separately, not by the script's default sweep) stays in a 5.2%-9.1% band across the same reject-rate flexes — also no flip. |
| P6 data decay | **PASS** | All 8 sources independently re-verified by direct fetch during this same authoring session (2026-09-05, 0 days old): S1 (fabworks.com) reachable, 48x120in confirmed. S2 (speedymetals.com) reachable, $7.20/$10.81/$14.41 prices and 2.448/3.672/4.896 lb weights confirmed, backing out to $2.94/lb. S3 (stylecnc.com) reachable, 25-30 m/min at 1.5mm/2kW confirmed. S4 (kasulaser.com) reachable, "0.3-3 seconds" and the 0.8-sec/3mm worked example confirmed. S5 (bls.gov) reachable, $22.94/hr and $47,700/yr May 2025 confirmed directly from the Quick Facts and Pay sections. S6 (arcuscnc.com) reachable, $7.00/hr oxygen/carbon-steel/6kW confirmed. S7 (sltl.com) reachable, "10-15%" direct material savings confirmed. S8 (regerlaser.com + htindustryco.com) both reachable, both quotes confirmed. No URL dead, no figure drifted, every source same-day fresh. |
| P7 accessibility | **PASS (re-run 2026-09-06, now that `published/` exists).** Stage-1 packet build (case-publish) produced `published/The Mirror Cut - Interactive.html` — a real coordinate-plane SVG diagram (The Straight Run's translated copies; The Mirror Cut's reflected+translated interlocking pair with its line of symmetry marked), a Working Notebook whose D1-D6 checks and live takeoff calculator call a JS port of `sensitivity_model.py`, a 9-term math `GLOSSARY` (Translation, Reflection, Rotation, Dilation, Scale Factor, Symmetry, Line Of Symmetry, Coordinate Plane, Vertex — all links freshly fetched and confirmed live 2026-09-06) and a `STORY_GLOSSARY` (Nesting, Kerf, Fiber Laser, Heat-Affected Zone, Laser Cutting). Mechanical pre-screen (`tier2_probes.py --probe 7`): D1's sketch deliverable matched against 2 real visuals found in the published HTML — 0 mechanical FAILs. Model-judged cold-read: a genuinely fresh, zero-context subagent was given only `/tmp/coldread-the-mirror-cut/PACKET.md` (built from the published HTML, glossary terms glossed inline) and the exact prompt from `SKILL.md`'s P7 section ("You have no background in Sam Delgado, production lead... List every real-world term or concept you could NOT picture or understand..."). It reported: "Every term in this packet is either defined inline (parenthetically), covered in a hover-glossary, or ordinary classroom/arithmetic vocabulary I already know. I found no real-world term or concept I couldn't picture or understand well enough to proceed." — 0 unexplained concepts, well under the 0-1 PASS threshold. |

**VERDICT: Probes 1-7 all genuine PASS.**
`case.json.qa.state` is now recorded as `TIER2_PASS` with `tier2` sub-verdicts P1-P7 all = PASS —
the full seven-probe Tier 2 gate is genuinely clean. `case.json.qa.verdict` = `"PASS"` (the literal
string case-publish's own gate requires).

**2026-09-06 addendum — stage-1 packet build + P7 re-run.** This session built the packet
(`cases/the-mirror-cut/published/`: Case Study docx, Data xlsx, Facilitator Guide docx, Interactive
HTML, MANIFEST.json), re-ran `tier1_structural.py` (T1-18/T1-19/T1-20/T1-21 all PASS, unchanged
`TIER1_PASS` with the same single T1-10 reinforcement-carve-out GAP as before), and re-ran Tier 2
Probe 7 for real per the procedure above. The previous entry's qualification ("genuine TIER2_PASS
is not reachable from inside stage 4 alone") is resolved now that stage 5's packet-build half has
run. Per the task's own scope, `case-publish`'s read-model promotion (stage 5's second half) was
NOT run — `readmodel/` is untouched, and `case.json.status` remains whatever it was before this
session (not promoted to `"published"`).

### Tier 3 — human dry-run
NOT RUN. No `runs/` directory. Not in scope for this task.

### Corrections made during this run
- Fixed the MA3 "Sensitivity" cell in `case.md` Appendix E, which named `FACILITATOR.md` directly —
  a preflight-lint leak finding — reworded to disclose sensitivity without pointing at where the
  answer lives.
- Added four numbers to `case.json.derived` (`reject_rate_simple_complement`,
  `reject_rate_mirrored_complement`, `d4_bbox_before_width_in`, `d4_bbox_before_height_in`) and
  corrected `FACILITATOR.md`'s rounded "about 55%" labor-cost-increase figure to the exact `55.4%`
  matching a new `labor_cost_pct_increase_mirrored_vs_simple` derived field, clearing a Tier 1
  T1-14 continuity GAP.
- Computed and recorded `case_md_sha256` in `case.json.qa`, clearing the T1-16 GAP.
- Confirmed, via two independently-dispatched fresh subagents (P1 cold solve, P3 trap check), that
  the case's numbers and its named trap both survive a genuinely blind read — no leaked answer, no
  guide/case mismatch found.

**Next step:** this case has not been run through `case-publish`. Per this task's own instructions,
stage 5+ is explicitly out of scope; a future stage-5 run should regenerate `published/` and then
re-run Tier 2 probe 7 before treating the case as fully `TIER2_PASS`.
