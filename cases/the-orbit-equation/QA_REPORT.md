# QA Report — The Orbit Equation

## case-readiness run — 2026-09-18
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Ran `python3 skills/case-readiness/scripts/preflight_lint.py --case the-orbit-equation` first: clean,
no advisory findings.

### Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-orbit-equation`:

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | no load-bearing Overview numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Devon Achebe." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices A-G lettered, ordered, no orphans |
| T1-07 | PASS | 6 final-appendix labels, all verbatim spine labels (POLISH: all bulleted, none from a separator-run line) |
| T1-08 | PASS | every number cited (S1-S3) or a declared Modeling Assumption (MA1-MA6) |
| T1-09 | PASS | balance test: both arguments written, margin 3.71% (well under the 20% cap, genuinely thin) |
| T1-10 | **GAP** | `new_coverage[]` empty — reinforcement carve-out (see below), not a padding attempt |
| T1-11 | PASS | learning-goal mutual reachability (see LEARNING_GOALS.md) |
| T1-12 | PASS | T3 tier vs. numeric load (polar equations, unit-circle exact values, multi-variable ratio metric, one deliberately non-load-bearing source (S3/FOV)) |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, cohort bands, sensitivity note |
| T1-14 | PASS | FACILITATOR.md numbers all traced into case.json.derived |
| T1-15 | PASS | published HTML built after case.md/FACILITATOR.md, no staleness |
| T1-16 | PASS | case_md_sha256 current |
| T1-17 | PASS | cohort bands declared (3 bands, band+note both present) |
| T1-18 | PASS | Interactive HTML present, fresh, leak-free (no margin_pct/winner literal outside `<script>`) |
| T1-19 | PASS | math GLOSSARY: 8 terms, all mathsisfun.com, verified live this session |
| T1-20 | PASS | visual asset present (worked-example polar graph + top-down orbit-comparison diagram), sourced |
| T1-21 | PASS | STORY_GLOSSARY (`.sterm` anchors): 9 real-world terms, each a real https:// link outside the math allowlist (Wikipedia) |
| T1-22 | PASS | published HTML's sections match case.md's |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | no dangling SVG connector lines (MCS-52) |

**BLOCKER (0).**

**GAP (1):** T1-10 — `new_coverage[]` is empty under the reinforcement carve-out
(`skills/case-readiness/SKILL.md`, "The reinforcement carve-out on T1-10," 2026-08-17). At case-write
time, a fresh read of `readmodel/standards_spine.json` found all 6 targeted Pre-Calculus skills
(Polar And Parametric ×3, Trigonometric Functions ×3) already at `n=2` — matching the concept sheet's
own "remaining thin" framing (`CONCEPTS_computer-graphics_2026-09-12.md`, C2), not a claim that they
were ever at `n=0`. Every adjacent skill in both target groups, and in the related Vectors group this
case's D4 also touches, was checked and found already thicker (`n>=3`) — see
`case.json.reinforcement_note` for the full accounting. All 6 claimed skills are still genuinely
forced by a deliverable (`LEARNING_GOALS.md`). `case-readiness` never edits `readmodel/`; the live
count should be re-verified at `case-publish` time before promotion.

**POLISH (1):** T1-07 (all 6 labels are bulleted, none came from a separator-run line — informational
only).

### Tier 2 — simulated play (7 probes)

Ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-orbit-equation`. Probes P1-P4 and
P7 were each dispatched to a genuinely fresh, zero-context subagent per this project's own doctrine
(the way sibling cases in this batch did); P5 ran fully mechanically; P6 (data-decay) was performed
directly against live-fetched pages in this same session (the sources were fetched and confirmed
during `case-research`, not from memory).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, given only the student packet, chose A, named the primary metric (avg %-frame per ms of compute) as required by D3, and reproduced the case's own arithmetic almost exactly (833.33 vs ~803.6, ~3.6-3.7% margin). Reached the recorded position by the intended route, not a shortcut. |
| P2 both-sides | **PASS** | Fresh subagent built genuine, non-concession arguments for both options: A's structural robustness (833.3 vs 803.6 on the case's own required metric, plus a 112%-oversized clip margin) and B's real framing win (17.68% avg, 25% at the telegraph moment, and a still-comfortable 41% clip margin). Neither side collapses to "worse but simpler" — the subagent explicitly noted this is a genuine, well-balanced trade-off. |
| P3 trap | **PASS** | Fresh subagent independently named a different (more sophisticated, "average-radius-before-inverting") trap before reading the guide, then read FACILITATOR.md's stated trap ("fixate on the one dramatic telegraph frame") and judged the guide's trap the one that will actually catch a real classroom — a lower-effort, more natural shortcut for a hurried student. This satisfies the probe: the guide's trap is real, anticipated, and judged effective. |
| P4 twist | **PASS** | Fresh subagent re-derived the twist (push-in amplitude 6→9) independently, confirmed it flips a real, thin, calculation-backed margin (3.71%→4.98%, A→B), tested the most plausible adversarial reading of "amplitude" against Appendix E's explicit definition (the coefficient itself, not the peak-to-trough swing) and found the case forecloses that ambiguity, verified the numbers match FACILITATOR.md/sensitivity_model.py exactly, and confirmed the guide correctly also flags the clipping-clearance side effect (3.5→0.5 game-units). |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py`'s ±50% sweep: `cost_A`, `cost_B`, and `amplitude_B` each flip the winner or breach the SPEC 20% cap; `framing_k` is a verified structural invariant (any flex leaves the margin exactly unchanged, confirmed to 4 decimal places). All three unstable dials have a Category-F (irreducible forecast/production-unknown) entry in `case.json.sensitivity_disclosure[]` with a real justification. `tier2_probes.py` reports `PASS (disclosed)` mechanically. MA1 (clipping radius) and MA2 (framing constant) are correctly out of scope for the continuous-metric FLEX sweep (a pass/fail gate and a verified invariant respectively) per `sensitivity_model.py`'s own docstring. |
| P6 data decay | **PASS** | All 3 cited URLs were fetched live during `case-research` this session (2026-09-18) and their claimed content directly confirmed by quote: S1 (Unity Orbital Follow docs) — "3 axis values: horizontal, vertical, and radius" confirmed verbatim; S2 (Unity Rotation Composer docs) — "rotates the camera to face the Look At target" confirmed verbatim; S3 (Unity Camera manual) — 60-degree default vertical FOV confirmed. Zero dead links, zero drifted figures. (A fourth candidate source, an Unreal Engine Camera Rig Rail page, was fetched, found not to actually support the specific claim it would have been cited for, and correctly rejected rather than misused — see RESEARCH_LOG.md.) |
| P7 accessibility | **PASS** (after 2 remediation rounds) | **Round 1** (original HTML): fresh cold-read subagent named 5 unexplained real-world concepts (Cinemachine "components," frame-time-budget scale, "blocking review" procedure, FOV-to-framing-formula connection, keyframe timeline) — a mechanical FAIL (>1 concept) — **and** gave a concrete, disqualifying answer to the MCS-51 question: it could not picture the Variable-Radius Push-In's actual camera motion in 3D space, despite the equation and the abstract worked example. **Remediation:** added a concrete, case-specific top-down diagram (Appendix B) showing both rigs' real orbital paths (drawn to the case's own r(θ) equation, not the illustrative example), glossed "component" with a plain-English analogy, clarified the FOV mention does not feed the framing formula, and strengthened the frame-budget-scale sentence. **Round 2**: fresh cold-read still named 6 concepts (still >1) and a softer but still-concrete "can't picture the concrete camera motion/cinematic effect" finding. **Further remediation:** glossed "blocking locks," "playtest," and "collision mesh" with real Wikipedia links, added a concrete FOV comparison ("roughly what a human eye takes in without turning the head"), and extended the diagram's caption to describe what a player would actually see on screen (boss growing larger during the push-in, like a camera dollying in for a close-up). **Round 3** (final): fresh cold-read named 0 blocking concepts (explicitly: "none of these block me from doing the actual math... texture/justification, not required inputs") and gave no concrete disqualifying answer to the MCS-51 question (explicitly: "I don't think this is a flaw in the packet" regarding the one residual, self-acknowledged-as-intentional abstraction, `percent of frame ≈ 300/r`'s unitless "game-units"). This is a genuine PASS reached through real remediation, not a forced pass and not an MCS-49 disclosure waiver — no waiver was needed or self-granted. |

**MECHANICAL RESULT (script):** P5 passed mechanically after `sensitivity_disclosure[]` was corrected to
the schema `tier2_probes.py` actually checks (`{"param","category","justification"}`, not the author's
first-draft `{"dial","finding"}` shape — a real authoring mistake caught and fixed during this run, not
a script defect). All other qualitative verdicts above are fresh-subagent judgments, per this project's
own dispatch doctrine, not the operator's own reasoning.

**A second real defect found and fixed during this run:** `sensitivity_model.py`'s `evaluate()`/
`evaluate_twist()` originally returned extra diagnostic keys (`frame_pct_A`, `min_r_B`,
`clip_clearance_B`, etc.) alongside `{"A","B"}`. `tier2_probes.py`'s `probe_sensitivity` computes
`min(base, key=base.get)` / `max(base, key=base.get)` over the *entire* dict returned by `evaluate()`,
on the documented assumption that the shape is exactly `{"A","B"}` — the extra keys were picked up as
fake "options" (e.g. `clip_clearance_B` = 3.5, smaller than either real metric), producing nonsense
margins in the tens of thousands of percent. Fixed by splitting the model into a private `_diagnostics()`
helper (used by the JS port and this report's own arithmetic) and a public `evaluate()`/`evaluate_twist()`
that return only `{"A","B"}`, per the documented Tier-2 contract in
`templates/INTERACTIVE_HTML_CONTRACT.md` §2. Re-ran and confirmed sane output (base margin 3.71%, not
23709.5%).

### Tier 3 — human dry-run

NOT RUN. `cohort_bands[]` is declared (3 bands) for whenever a facilitator schedules a live session; no
`cases/the-orbit-equation/runs/RUN_*.md` exists yet. This does not block `TIER2_PASS` per the ladder in
`skills/case-readiness/SKILL.md` — it blocks `VERIFIED` only.

## case.json.qa (written by this report)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 1,
  "case_md_sha256": "18c1f06120142c1f7bf3a7da23dc379f4f67f5367534a0295a65540df0e4cce2",
  "tier2": {
    "P1": "PASS",
    "P2": "PASS",
    "P3": "PASS",
    "P4": "PASS",
    "P5": "PASS (disclosed)",
    "P6": "PASS",
    "P7": "PASS"
  },
  "tier3_runs": []
}
```

## Next step

`Run case-publish on the-orbit-equation` — out of scope for this pipeline pass per the operator's
instructions (case-publish, and any write to `readmodel/`, is deliberately left to a later, centralized
pass given concurrent sibling agents authoring other cases against the same spine right now). Before
that publish runs, re-verify `readmodel/standards_spine.json`'s live `n` for the 6 claimed Pre-Calculus
skills — it was `n=2` at this report's time and may have moved again.
