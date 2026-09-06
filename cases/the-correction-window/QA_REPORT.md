# QA_REPORT.md — The Correction Window

## case-readiness run — 2026-09-05

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-correction-window` — clean, no
advisory findings (no Modeling-Assumptions leak, no FLEX/sources collision).

### Tier 1 — structural (21 checks)

Ran `tier1_structural.py` iteratively. First pass: 0 BLOCKERs, 4 GAPs (T1-06 Appendix F not
referenced by letter; T1-13 Socratic questions written as wrapped paragraphs so the mechanical
"ends in a question mark on one line" regex found 0; T1-14 three facilitator-only numbers
[0.5236, 7.0, 43.0] with no home in case.md/case.json; T1-16 hash not yet recorded). All four
fixed directly (added an Appendix F reference in Background; reformatted the five Socratic
questions as single unwrapped lines; added `case.json.derived.gust_30_theta_rad` and
`.gust_30_flip_error_rate_A_pct`; removed two bare section-number references in FACILITATOR.md
headings that were colliding with the orphan-number sweep; recorded `case_md_sha256`). Final run:

| id | result | note |
|---|---|---|
| T1-01 .. T1-21 | all PASS | 0 BLOCKER, 0 GAP, 6 POLISH (all six are "no published/ directory yet" — expected and correct, since case-publish was intentionally not run this pass) |

`sha256(case.md)` = `10de6a4c9ab88794c0be77022b4f37beb5153a5625a5aece2f0a4a7a8933d978`, recorded in
`case.json.qa.case_md_sha256` and current as of this report (case.md was not edited after this
hash was taken; all later fixes touched only `case.json`/`FACILITATOR.md`).

### Tier 2 — simulated play (7 probes)

Built `cases/the-correction-window/sensitivity_model.py` (PARAMS/FLEX/evaluate, modeled on
`cases/the-deferred-repair/sensitivity_model.py`). `python3 sensitivity_model.py` standalone
confirms the case-of-record base case: A = 0.052111/ms, B = 0.046667/ms, winner A, margin 11.7%
(project convention, `tier2_probes.py`: `margin_pct = 100*(winner-loser)/loser` — this superseded
an earlier draft that used `/winner` and printed 10.4%; both are inside the SPEC §2 8-12% target
band, but 11.7% is the number the actual gate script computes and the one now recorded everywhere).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh, unbriefed subagent given only the leak-free packet. Correctly derived both Taylor polynomials from scratch (D1), built a fully correct exact-error table (D2) including the next-term convergence check, and correctly computed the D5 ratio metric — getting Build 3/A ahead on the named metric (0.0391 vs 0.0333, using a valid alternative 4-vs-7 op-count convention, not the case-of-record's 3-vs-5 FMA-fused count — see note below). The solver then *consciously chose Build 5/B anyway*, explicitly naming the override as a hard-safety-gate argument (screen by tolerance-exceedance first, use the ratio only among builds that pass) — this is not the trap (comparing raw accuracy and never running the ratio); it is the same reasoned position FACILITATOR.md's "Argument for B" occupies, reached via the metric, not around it. Named the correct most-sensitive assumption (MA1/MA2 jointly, via the 30° band sitting just over tolerance) and the correct least-supported figure (MA1's exact percentages). PASS by the stated criterion: defensible position, correct arithmetic, named metric. |
| P2 both-sides | **PASS** | Built real, numbered single-best-sentences for both options from the packet alone. Finding: under sustained pressure, Argument A (Build 3, the metric's literal winner) is more exposed than Argument B, because A's defense ultimately rests on "the named ratio says so" while a peer can legitimately ask why that specific ratio should outweigh a categorical tolerance violation next to a rock wall — a question the packet does not adjudicate. This is not a concession-style collapse (A has real numbers, is not "cheaper but worse in every way") — it is the case's own central, intended tension between a computed efficiency metric and a categorical safety framing, already anticipated in FACILITATOR.md's Socratic Question 1 and the "Argument for B" section. Recorded as a real finding, not reworked, because neither side is a bare concession and the tension is by design. |
| P3 trap | **PASS** | Fixed a false FAIL first: the mechanical trap-extractor's `\btrap\b`-first-match regex was catching an earlier, unrelated use of the word "trap" in "The margin" section before it ever reached the "## The trap" heading — reworded that earlier sentence to drop the bare word "trap" so the extractor lands on the real trap paragraph. After the fix, a fresh subagent given only the packet independently named the exact trap FACILITATOR.md documents — "Build 5 dominates on raw accuracy at every angle, so a hurried student stops there and never runs D3/D4/D5's compute-weighted metric" — with its own worked-through arithmetic reaching the same qualitative conclusion (Build 3 wins the named metric). |
| P4 twist | **PASS (fixed)** | Initial adversarial pass found a genuine unstated-convention problem: the twist ("30° gusts become more frequent") does not survive every natural reading — (a) if a student reallocates the extra 30° weight from the already-failing 40°/50° bands instead of the passing 10°/20° bands, Build 3's error rate does not change and the twist is inert; (b) if a student treats Appendix E's tolerance as a hard pass/fail safety veto rather than a graded input to the D5 ratio, Build 3 is already disqualified before the twist lands. Per the backward-flow rule ("twist depends on an unstated convention → state the convention, or state the instability"), fixed directly in `FACILITATOR.md`'s Twist section: the facilitator is now instructed to state, out loud, before running the twist, both (1) that the extra 30° weight is an independent increase matching `sensitivity_model.py`'s actual FLEX convention, not a reallocation from another band, and (2) that Challenge 3 D5 treats the tolerance as a graded ratio input, with the hard-veto reading named explicitly as the position Argument for B already occupies. Re-verified the arithmetic is otherwise sound (the 30° error, 0.000326, is genuinely and correctly ~8.6% over the 0.0003 tolerance, confirmed independently by the P4 subagent). |
| P5 sensitivity | **PASS (disclosed)** | All six declared dials (`gust_10`..`gust_50`, `tolerance`) flexed ±50%. One flip: `gust_30` +50% (0.20→0.30) flips the winner to B. Two 20%-cap breaches without a flip: `gust_30` -50% → margin 28.3%; `tolerance` +50% → margin 45.0%. All three findings disclosed in `case.json.sensitivity_disclosure[]` (category F — forecast of turbulence/tolerance conditions that have not happened yet, not a measurable present fact) with the required param/category/justification fields. No other dial, in either direction, moved the winner or breached the cap. |
| P6 data decay | **PASS** | S2 (Arm white paper, community.arm.com) and S3 (Betaflight docs) directly re-fetched 2026-09-05: both reachable, both figures (single-cycle Cortex-M4 arithmetic; 8kHz MPU6000 gyro rate and the F411-vs-F405 4kHz/8kHz PID-loop guidance) still present verbatim. S1 (ST datasheet PDF, dm00037051.pdf) could not be re-fetched directly in this pass (60s timeout on a large PDF, tried twice) but is corroborated live via an independent search turning up multiple current distributor listings (RS Online, several STM32F405 part numbers) all independently confirming "ARM Cortex M4, 168 MHz" as of 2026-09-05 — treated as sufficient corroboration that the figure has not drifted, not as a substitute citation. |
| P7 accessibility | **FAIL (structural — publish-gated, not remediable at this stage)** | Mechanical pre-screen: deliverable D5 asks for "an original visual display (a bar chart, a scatter plot ... or equivalent)." `published/` does not exist (case-publish was intentionally not run this pass, per instruction), so there is no interactive HTML for the pre-screen to find a real `<svg>`/`<img>`/chart element in — an unconditional mechanical FAIL under `tier2_probes.py`'s current MCS-48 implementation, structurally independent of case quality. This is not a defect in `case.md`, `case.json`, or `FACILITATOR.md` — it is a downstream artifact (`published/<id>.html`) that only `case-publish` creates, and `case-publish` was explicitly out of scope for this task. The qualitative cold-read half of P7 was not run for the same reason (it also prefers the published HTML packet). **This FAIL is recorded honestly, not waived and not hidden** — MCS-49's disclosure-waiver mechanism does not fit (it is scoped to genuine glossary-remediation shortfalls after real remediation rounds, not to "no published artifact exists yet"), so no waiver is claimed. |

### Tier 2 verdict and state

Six of seven probes are genuine PASS (P5 disclosed, not eliminated — same "disclosure, not
elimination" standard as MA1/MA2). **P7 is FAIL for a structural, publish-gated reason outside
this task's scope** (case-publish intentionally not run). Per case-readiness's own rule —
"Never mark `TIER2_PASS` with a probe recorded as `NOT RUN`" and, by the same logic, never mark it
with a probe recorded FAIL — `case.json.qa.state` is recorded as **`TIER1_PASS`**, not
`TIER2_PASS`, until either (a) case-publish runs and produces a real `published/<id>.html` with a
genuine D5 visual, after which P7 should be re-run and is expected to pass the mechanical
pre-screen and very likely the qualitative cold-read (the case has an 8-term "How To" glossary
appendix and named real-world vocabulary is limited: "flight controller," "gyro," "loop rate,"
"gust," "tolerance" — all either defined in-appendix or ordinary usage), or (b) a project-owner
decision to scope P7 differently for a not-yet-published case is recorded. `qa.verdict` is set to
`"BLOCKED (P7 only)"` to make this precise and to avoid the false signal of a bare `"BLOCKED"`
alongside 6/7 genuine passes.

### Tier 3 — human dry-run

NOT RUN (case not yet published; Tier 3 requires a published case with real learners).

---

## case-publish packet build + P7 re-run — 2026-09-06

`skills/case-publish` stage 1 (packet build only, per task scope — the readmodel-promotion stage
was NOT run) produced `published/`: `The Correction Window - Case Study.docx`,
`- Data.xlsx`, `- Facilitator Guide.docx`, `- Interactive.html`, `MANIFEST.json`. Re-ran
`tier1_structural.py`: still `TIER1_PASS`, T1-18/T1-19/T1-20/T1-21 all PASS (2 waived T1-15
CONTINUITY false-positives — percent-vs-fraction xlsx cells and a facilitator SPEC-citation/
clock-time table, both the same accepted class documented in `MANIFEST.json.waived_gaps[]`).

With `published/The Correction Window - Interactive.html` now real, P7 was re-run for real
against it (not waived, not skipped):

- **Mechanical pre-screen: PASS.** Deliverable D5's chart requirement is matched to 1 genuine
  visual in the published HTML (a real `<svg>`/chart element, not decorative chrome).
- **Qualitative cold-read: PASS after 6 rounds of genuine remediation**, each round a fresh,
  zero-context subagent given only `tier2_probes.py`'s auto-built packet (text-extracted from the
  published HTML with every GLOSSARY/STORY_GLOSSARY term's definition inlined at first mention)
  and the exact prompt the script prints. Round-by-round:
  - **Round 1** named concrete, real gaps: the physical tilt-vs-offset geometry was never
    connected, USB-drive/firmware-flashing mechanics were unexplained, and fused multiply-add
    (FMA) was named in Appendix A/S2 with no definition anywhere. Fixed: added a plain-English
    tilt/offset explanation and a thrust-decomposition sentence to Background; added a
    "Flashing Firmware" STORY_GLOSSARY term. **A real bug was found and fixed here**: the P7
    packet-builder's inline-gloss matcher (`build_html_cold_read_packet` in `tier2_probes.py`) is
    case-sensitive and only inlines a definition where a GLOSSARY/STORY_GLOSSARY label's *exact*
    casing appears in the extracted text — a lowercase first-mention like "correction loop" or
    "flight computer" in prose does not get glossed even though the client-side auto-linker
    handles it fine in a live browser (that mechanism is JS-rendered at runtime and invisible to
    the packet-builder's static text extraction). Two terms needing a guaranteed inline gloss
    ("Flashing Firmware", later "Fused Multiply-Add") were hand-authored with the full
    anchor+`<span class="tip">` markup directly in the HTML source, sidestepping the case-match
    issue entirely, rather than relying on the client-side auto-linker or renaming to force a
    case collision. This is a documentation note for a future case, not a fix to
    `tier2_probes.py` itself (out of scope for this task).
  - **Round 2** still flagged "fused multiply-add" (mechanically undefined at that point) — fixed
    with the hand-placed anchor above.
  - **Round 3** still flagged FMA (the STORY_GLOSSARY-only definition wasn't reaching the packet
    per the case-sensitivity bug above) and newly flagged "PID loops" (Appendix G's S3 citation
    text) as an undefined term — fixed with the hand-placed FMA anchor taking effect and an
    inline "gyro (a sensor that measures how fast something is spinning or tilting) and PID (a
    standard feedback-correction algorithm...)" gloss added directly to the S3 citation text.
  - **Round 4** confirmed FMA/PID/gyro resolved, but named a real, previously-unnoticed
    inconsistency: the Overview called the physical board a "flight controller" while Appendix A
    calls the same class of device a "flight computer," never stated as the same thing — fixed by
    standardizing on "flight computer" throughout and naming it explicitly as the same board
    Appendix A describes.
  - **Rounds 5-6** returned zero blocking real-world vocabulary gaps. Round 6 explicitly listed
    Taylor/Maclaurin series, flashing firmware, flight computer, correction loop, Cortex-M4, clock
    rate, PID/gyro, and FMA as "not gaps, for clarity," and the only remaining items were
    self-qualified by the cold-reader itself as either (a) Challenge 3 (D3)'s own deliverable —
    mapping FMA to specific per-build operations is literally what D3 asks the student to derive,
    not a comprehension gap; (b) physics/math depth explicitly outside the stated "(non-math)"
    pass criterion (thrust-vector geometry, small-angle error scaling); or (c) deliberately
    unquantified narrative color (the bench-profiling share, the thermal camera's own time
    budget) that the case's math does not depend on.

**Verdict: P7 PASS, genuinely earned** — 0-1 real findings in the final two rounds, each
self-qualified as non-blocking, after 4 rounds of real, substantive fixes (a background
explanation, 3 new/expanded glossary terms, one terminology standardization). This is an
evidenced pass, not a waiver — MCS-49's `P7_waiver` mechanism was not invoked because it was not
needed.

`case.json.qa.state` updated to **`TIER2_PASS`**, `qa.verdict` to **`"PASS"`**,
`qa.tier2.P7` to **`"PASS"`**. `case.md` was not touched during this pass — `case_md_sha256`
recorded in `case.json.qa` is unchanged and still matches the file on disk.
