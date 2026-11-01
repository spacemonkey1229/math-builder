# QA_REPORT.md — The Culling Volume

## case-readiness run — 2026-09-18

**State reached:** DRAFT → TIER1_PASS → TIER2_PASS
**Verdict:** PASS

### Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-culling-volume`,
iterated several times as real defects were found and fixed (see "Real defects found and fixed"
below). Final run:

```
checks run: 24   PASS 20 · GAP 4 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 4 gaps)
```

| id | result | note |
|---|---|---|
| T1-01–T1-09 | PASS | structural sections, boilerplate, appendix referencing, Appendix F verbatim spine labels, sourcing discipline, Overview clean of load-bearing numerals, balance test |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out applies (`case.json.reinforcement_note`: all 6 claimed skills checked, all at n=2, no genuinely uncovered skill elsewhere in Geometry reachable from this case's real deliverables) |
| T1-11 | PASS | LEARNING GOAL CHECK — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | tier (T2) matches numeric load |
| T1-13 | PASS | 5 Socratic questions, trap(s) named, full anchor ladder (Anchor 1 initially missing — see fixes below), 45-minute timed plan, sensitivity note present |
| T1-14 | GAP | 1 confirmed false positive: "SPEC Section 7" in a heading parses as literal `7.0` — same precedented class as `the-approval-gate`/`the-marginal-detection` |
| T1-15 | GAP | 4 confirmed false positives in the Facilitator Guide docx: `7.0`/`7.3` (SPEC section references), `38.0` (a `38:00` clock-time-range boundary the checker's exclusion doesn't recognize past 23:59), `8.0` (see T1-18) |
| T1-16 | PASS | hash matches |
| T1-17 | PASS | `cohort_bands[]` declared, 3 bands |
| T1-18 | GAP | 1 confirmed false positive: every HTML document's own `<meta charset="utf-8">` tag contains the digit 8 ("utf-8"), universal to any HTML file, not case data |
| T1-19 | PASS | 8-term hover+hyperlink math glossary, all links allowlisted and verified live |
| T1-20 | PASS | real SVG visual present (prop-silhouette comparison chart) |
| T1-21 | PASS | 5→9-term `STORY_GLOSSARY` (domain vocabulary, expanded during P7 remediation — see below), all Wikipedia links verified live |
| T1-22–T1-24 | PASS | published HTML section parity, inline `<script>` parses clean, no hand-drawn SVG connectors to check |

**VERDICT: TIER1_PASS (0 blockers, 4 gaps, all 4 confirmed accepted/false-positive, none a real
defect).**

### Real defects found and fixed during this run

1. **T1-13 BLOCKER (first run): missing "Anchor 1" heading.** `FACILITATOR.md`'s anchor ladder
   jumped straight from "Launch" to "Anchor 2," omitting the required Anchor 1 (take a stand and
   vote) section. Fixed: added the Anchor 1 section.
2. **T1-14/T1-15/T1-18 GAPs (several rounds): orphan derived numbers.** Figures referenced in
   `FACILITATOR.md` (the 1.8 ms CPU-cost gap, the lamppost's exact 137,143.4 L waste, the sign
   post's 0.1414 m capsule radius) were not recorded in `case.json.derived`, so the continuity
   sweep correctly flagged them as unverifiable. Fixed by adding each to `case.json.derived`.
3. **T1-02 BLOCKER (introduced during P7 remediation, caught immediately on re-run): a P7 fix
   accidentally added a load-bearing-looking digit ("3-D") to the Overview**, and pushed the
   Overview to 310 words (over SPEC's 300-word cap). Fixed by trimming the Overview back to a
   leaner 238 words with no stray digits, moving the fuller "mesh"/"profiler" plain-English
   definitions to Background (which has no numeral restriction) and the `STORY_GLOSSARY`.

---

# TIER 2 — SIMULATED PLAY (seven probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **Initially FAIL (arithmetic error) → remediated → PASS** | See "Real defect found and fixed (P1)" below. |
| P2 both-sides solve | **PASS** | Fresh subagent. Built genuine, numbers-grounded cases for both A ("the sphere's 0.9ms cost is fixed and simple; B's entire 0.357ms advantage rides on an unsourced MA9 that only needs a ~17% haircut to flip") and B ("even paying 3x more per test, the capsule eliminates 352x more wasted volume, netting a real 2.706ms vs 3.063ms"). Found A collapses first under a "if overdraw cost is real at all, why ignore a 352x geometric waste gap" cross-examination — a real, case-grounded critique. Margin is not a paper number. |
| P3 trap check | **Initially found a 3rd, unanticipated trap → remediated → PASS** | See "Real defect found and fixed (P3)" below. |
| P4 twist integrity | **PASS** | Fresh subagent independently re-derived every D1–D4 figure from Appendix B/D from scratch (matched the packet almost exactly), confirmed the base case (A=3.063ms, B=2.706ms, 13.2% margin) and the twist's flip (halving MA9 → A=1.982ms, B=2.703ms, A wins) are both arithmetically sound. Checked one candidate alternate reading of the capsule construction rule (standard physics-engine "cylinder length = H−2r" convention) and found it is not just a different-but-reasonable reading — it's geometrically invalid here (fails to contain the pipe's flat end), and the case's own Appendix B text already forecloses it explicitly. No unstated-convention BLOCKER. |
| P5 assumption sensitivity | **PASS (disclosed)** | Mechanical (`sensitivity_model.py`). Base: A=3.063ms, B=2.706ms (winner), margin 13.2%. All three FLEX[] params (`sphere_cost_per_test`, `capsule_cost_per_test`, `render_cost_per_liter`) genuinely unstable under ±50% — each has a real flip direction. Disclosed as Category X in `case.json.sensitivity_disclosure[]`. Note: the raw harness prints a differently-signed margin (−11.7%) due to its generic negative-cost convention interacting with a metric where both values are negative — the correct, verified positive-cost margin (13.2%) is what `sensitivity_model.py`'s own `__main__`/`costs()` and `case.json.derived` report; this is the same documented "CAVEAT"-class harness quirk noted in `tier2_probes.py`'s own comments for negative/zero-baseline metrics, not a case defect. |
| P6 data decay | **PASS** | All 4 `sources[]` URLs fetched and confirmed live and figure-bearing this session (age 0 days): S1 (LED Lighting Supply, MEDIUM), S2 (Engineering ToolBox/ASME B36.10, HIGH), S3 (Epic Games/Unreal Engine docs, HIGH — the case's strongest single citation), S4 (Unity docs, HIGH, supplemental). No dead links, no drifted figures. |
| P7 accessibility cold-read | **FAIL (waived, MCS-49)** | 2 genuine remediation rounds (see below), narrowed from comprehension-blocking gaps to non-blocking "flavor" items plus one deliberately-disclosed non-mechanistic figure. Waived, not eliminated — see `case.json.qa.tier2.P7_waiver`. |

### Tier 2 — Real defect found and fixed (P1)

A fresh subagent dispatched against the cold-solve packet correctly **chose Option B** (matching
the case's own designed outcome) but made a **genuine 1000× arithmetic error**: it computed
`render_A = 108,172,400 L × 0.00000002 ms/L` as **2,163.4 ms** (should be **2.163 ms**) and
consequently reported a wildly wrong total (`A = 2,164.3 ms`, `B = 8.83 ms`) — a decimal-place slip
on a constant with seven leading zeros. Per P1's own pass criteria, reaching the "right" answer
(B) by **wrong arithmetic** is a FAIL, not a pass — and the fact that a competent solver made
*this specific* error is real evidence that Appendix D's `0.00000002 ms/L` figure is a genuine
usability hazard, not just one solver's carelessness.

**Fix applied directly to `case.md` and the interactive HTML** (not just noted): Appendix D now
states the same rate in a friendlier equivalent form — "0.02 ms per 1,000,000 liters" — alongside
the original `0.00000002 ms/L`, plus an explicit decimal-point warning with a worked example using
a **placeholder number that is not one of this case's own totals** (so the fix teaches the
technique without leaking a graded intermediate value). No underlying numeric value changed;
`sensitivity_model.py`'s own `costs()` function already used full floating-point precision
throughout (the bug was purely in the fresh human-style hand-calculation this fix targets).

**Re-run (fresh subagent, after remediation): PASS.** Correct arithmetic throughout: sphere render
cost = 108,172,519 L = 108.1725 million L × 0.02 ms = 2.1635 ms; capsule render cost = 306,515 L ×
0.02 ms/million = 0.00613 ms; totals A = 3.0635 ms, B = 2.7061 ms. Chose B, named the metric,
correct order of magnitude throughout — the decimal-point fix closed the gap.

### Tier 2 — Real defect found and fixed (P3)

The machine pre-screen confirmed `FACILITATOR.md` names a trap; the fresh subagent, reading the
packet alone, independently named a **different, additional, genuinely plausible trap** the guide
had not anticipated: building the bounding capsule from a prop's *component* height/radius (e.g.
the lamppost pole's 6.1m/0.075m) instead of its *full total* height/widest radius (6.4m/0.15m) —
"the capsule hugs the pole; the pointy cap sticks out past the rounded caps." This produces an
undersized, non-containing capsule that makes Option B look artificially cheap, which is exactly
the kind of error that would go undetected because it doesn't obviously break the story. Per
doctrine, an unanticipated trap the guide isn't watching for is a Tier 2 FAIL even if the case is
otherwise sound.

**Fix applied directly to `FACILITATOR.md`:** added this as a named "third trap," with explicit
guidance to watch for it "when a group's Option B numbers look suspiciously good." No change to
`case.md` — the student-facing construction rules in Appendix B were already unambiguous (P4
independently confirmed this); only the guide's own anticipation was incomplete, and that gap is
now closed.

### Tier 2 — Real defect found and fixed (P7)

**First run: FAIL.** A fresh, zero-context subagent named 7 unexplained real-world concepts (frame
budget, profiler, mesh, draw calls, shading work, the GPU/CPU split, wireframe view) and, on Q2,
identified a genuine mechanism gap: MA9's liters-to-milliseconds conversion has no stated physical
mechanism connecting 3-D wasted volume to 2-D overdraw/pixels, and the Twist section's own framing
("a bare constructed modeling device") confirmed there isn't one to find — a legitimate finding,
not a missed explanation.

**Remediated:**
- Added inline plain-English definitions for frame budget, profiler, mesh, draw call, shading, and
  the GPU/CPU split directly in Overview/Background prose (see the T1-02 fix above for the
  numeral-safety correction this required on a second pass).
- Expanded `STORY_GLOSSARY` from 5 to 9 terms: added Profiler, Mesh, GPU, and Shading (all
  Wikipedia, verified live), alongside the existing Occlusion Culling, Bounding Volume, Overdraw,
  Capsule, and Frame Budget.
- The MA9-mechanism concern (Q2) is inherent to the case's own honest disclosure that MA9 is an
  unmechanistic constructed conversion (this is a *feature*, not a bug, per the Twist's whole
  point) — not remediated further, since manufacturing a fake mechanism would violate the
  never-fabricate-a-number rule worse than leaving the gap honestly disclosed.

**Second run (fresh subagent, after remediation): still technically FAIL, but materially
narrower.** 7 items were still named, but the solver itself explicitly qualified them as
"flavor/justification details" that "didn't block me" from following the case's real geometry and
arithmetic (frame-budget spreadsheet contents, content-patch specifics, shader internals, GPU
parallelism mechanics, NPS/Schedule-40 pipe-standard meaning, per-pixel lighting math) — a
materially different finding from round 1's comprehension-blocking gaps. The one Q2 item (MA9's
mechanism) was independently confirmed by the solver as the case's own deliberate, disclosed
non-mechanistic device ("there's nothing further to picture, only a formula to apply"), not a
missed explanation. Per MCS-49 and the precedent set on `the-marginal-detection` (2–3 genuine
remediation rounds, then a disclosed-partial waiver rather than open-ended iteration chasing an
irreducible tail of "why is this physically true" depth questions), this is waived — see
`case.json.qa.tier2.P7_waiver` for the full required fields and the verbatim remaining-gaps list.

---

## Tier 3 — human dry-run

NOT RUN. This case is being taken to `PUBLISHED`, not `VERIFIED`, in this pipeline pass — Tier 3
requires a real cohort and is out of scope here. `cases/the-culling-volume/runs/` does not yet
exist.

---

## Live browser audit (2026-09-18)

Opened `published/The Culling Volume - Interactive.html` in a real Chromium browser (served over a
local HTTP server; `file://` access was unavailable in this environment). This session's Browser
pane is shared across multiple concurrent agents publishing other cases in the same batch — tabs
for other cases (`The Missing Hub`, `The Absorption Call`, and others) were repeatedly observed
taking over the fronted tab and even overwriting `tabId` assignments mid-session, which made
click-based navigation and screenshot timing unreliable. Where screenshots were unreliable,
verification was done via direct JS evaluation against the live page (`javascript_tool`) and
`get_page_text` instead, which are unaffected by which tab happens to be visually fronted, and a
handful of screenshots did succeed and are reported below.

- **Zero console errors, zero failed network requests** for this case's own HTML across the
  session (confirmed via `read_console_messages`/`read_network_requests`; other agents' concurrent
  requests to their own local ports appeared in the same shared network log, unrelated to this
  case).
- **Initial page load (screenshot-confirmed):** header, pillbar, Overview render correctly;
  `wireframe`, `mesh`, `profiler`, `sphere`, `capsule` all auto-link correctly on first mention.
- **Appendix A prop-silhouette chart:** confirmed rendering via `propChart.innerHTML.length > 0`.
- **Working Notebook, all 4 steps (JS-evaluated directly against the live page, not simulated):**
  - Step 1 (lamppost real volume, computed from `propStats('lamppost')`): ✓ — matches
    `case.json.derived` exactly.
  - Step 2 (sphere volume + wasted liters): ✓ / ✓ — matches.
  - Step 3 (capsule volume + wasted liters): ✓ / ✓ — matches.
  - Step 4 (total cost A/B, computed from `totalsAt(RENDER_COST_PER_L)`): ✓ / ✓ — **A = 3.0634 ms,
    B = 2.7061 ms**, matching `case.json.derived.cost_a_ms`/`cost_b_ms` (3.063/2.706) exactly.
  - Wrong-value rejection tested directly (Step 1 with an incorrect volume): correctly returned
    "try again."
- **Dilemma pick:** setting Option B and calling `updatePick()` correctly updated the header pill
  to "Current pick: B" (the same mechanism the UI's own click handler calls).
- **Twist:** applying the twist checkbox correctly live-computed the halved-MA9 scenario —
  **A = 1.982 ms, B = 2.703 ms** — exactly matching the disclosed sensitivity finding
  (`sensitivity_disclosure[]`'s `render_cost_per_liter` −50% flip to A, margin 36.4%).

**No rendering or computation bugs found.** The only friction was environmental (a shared,
concurrently-used Browser pane), not a defect in this case's artifact — the JS-evaluation
fallback confirmed every interactive computation is correct and consistent with the case's
recorded values.

---

## Final state

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 4,
  "tier2": {"P1": "PASS (remediated)", "P2": "PASS", "P3": "PASS (remediated)", "P4": "PASS",
            "P5": "PASS (disclosed)", "P6": "PASS", "P7": "FAIL (waived -- see qa.tier2.P7_waiver)"}
}
```

Next step: `case-publish` may run (packet already built into `published/`; the read-model write
[`cases_index.json`/`standards_spine.json`/`gap_queue.json`] is explicitly deferred per this
batch's own instructions, to avoid a write conflict with other agents publishing other cases in
the same batch concurrently).
