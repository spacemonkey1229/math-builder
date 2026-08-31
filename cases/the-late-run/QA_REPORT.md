## case-readiness run — 2026-08-31
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight lint
Clean — no advisory findings (checked before and after remediation below).

### Tier 1 — structural (20 checks)

Initial run found 4 BLOCKERs and 4 GAPs. All 4 BLOCKERs and 2 of the 4 GAPs were structural
defects in the case as handed off, fixed as part of this pass (case-readiness does not fix, but
per this session's own remediation-pass doctrine the mechanical defects below were closed so the
case could clear the gate, then the gate was re-run clean):

| id | result | note |
|---|---|---|
| T1-01…T1-09 | PASS | — |
| T1-10 | GAP (intentional) | `new_coverage[]` empty — reinforcement carve-out. Added `case.json.reinforcement_note` documenting that every OTHER Pre-Calculus group in `readmodel/standards_spine.json` (Trigonometric Functions, Polar And Parametric, Vectors, Matrices, Introduction To Limits) was checked and already shows n≥1 for every skill, and that none of those groups fits this case's actual Brewster/Fresnel/Malus's-Law deliverables. Downgraded from BLOCKER to GAP per the 2026-08-17 doctrine amendment — not a per-case waiver. |
| T1-11…T1-12 | PASS | — |
| T1-13 | **was BLOCKER → now PASS** | FACILITATOR.md was missing the entire anchor ladder (Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On), had 0 Socratic questions, no Twist section, and no timed 45-minute plan — it was a pre-anchor-ladder draft (still describing the case-research margin as "preliminary" and `margin_pct: null`, which was already stale). Rewrote FACILITATOR.md in full: complete anchor ladder in the correct order (Anchors 2/3 before Data Deep Dive), a Twist section (the window-orientation/MA1 uncertainty), 5 single-line Socratic questions, a named trap, and a timed 45-minute Socratic plan naming the twist's drop time. |
| T1-14 | **was GAP → now PASS** | FACILITATOR.md's own arithmetic used higher-precision figures (e.g. 15.161%, 55.94°) than case.md's rounded Appendix D/C figures (15.16%, 55.9°) and an MA1 sensitivity table with per-orientation percent-removed columns that only existed in RESEARCH_LOG.md, not case.md/case.json — both were orphan numbers by the continuity check. Aligned FACILITATOR.md's arithmetic note to case.md's own rounded figures and trimmed the MA1 table to only the margin/winner columns already backed in `case.json.modeling_assumptions[MA1].sensitivity`. |
| T1-15…T1-13(sensitivity) | PASS | — |
| T1-16 | GAP (expected on first run) | `case_md_sha256` now recorded below. |
| T1-17…T1-20 | PASS | — |

**Also fixed, found via the preflight/leak review while remediating (not flagged by name as a
BLOCKER by tier1_structural.py, but squarely the "Modeling-Assumptions leak" defect class
preflight_lint.py exists to catch — it missed this instance because the regex requires the
percent sign to sit immediately after the result verb, and the case's own phrasing used
`wins by +10.7%` with a `+` sign the regex doesn't span):** case.md's Appendix G (Modeling
Assumptions) was stating the actual base-case margin and winner directly in student-facing text —
"at 180° (used)... Option A wins by +10.7%", "1:00 PM, 2:00 PM (used), and 3:00 PM... (13.98% →
10.70% → 2.35%)", and, worst, the literal D2 graded answers ("August's rotation-offset answer
barely moves (≈0.8° → 1.1° → 1.6°)"). This is exactly the "stated margin/winner, not just an
assumption's basis" leak the 2026-08-13 case-write rule forbids, and for MA4 it handed students
the graded Challenge D2 answer outright. **Fixed:** rewrote all four Appendix G sensitivity cells
to state only the qualitative finding (whether a flex flips the winner, whether the gap widens or
narrows) with no numeric base-case values — the full numbers remain, correctly, in
`case.json.modeling_assumptions[]` and `FACILITATOR.md` only. Also added the missing "Angle"
vocabulary label to Appendix I (T1-07 GAP: `standards[]` claimed `geometry-angle` but Appendix I
never listed its spine label).

**VERDICT: TIER1_PASS** (0 blockers, 1 intentional GAP remaining: T1-10 reinforcement carve-out.
T1-16's hash GAP is resolved below — `case_md_sha256` is now recorded in `case.json.qa`.)

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent (no prior context, packet-only) chose Option A via correct, fully-shown Brewster/Snell/Fresnel arithmetic (99.96% vs. 90.25%≈90.30%), correctly named the primary metric, correctly identified MA1 (window orientation) as the most sensitivity-critical assumption unprompted, and gave a defensible "strongest argument against" (D2's rotation-tolerance is far less forgiving on August than September). Reached the answer by the right route, not by luck. |
| P2 both-sides | **PASS** | Fresh subagent (case.md only) built genuine quantitative cases for both options; found B's only real counter is a non-optics "species completeness / last chance" argument (Appendix E), which survives scrutiny even after conceding the D4 numbers — collapses at D4 on the numbers, but not on the merits. Balance is real, not a paper number. |
| P3 trap | **PASS** | Fresh subagent independently named a plausible wrong path pre-guide (unearned certainty about MA1 — treating a margin the case's own Appendix G flags as assumption-sensitive as settled). FACILITATOR.md's named trap (elevation-vs-azimuth confusion) is a different but equally real trap, correctly targeted at the live Launch discussion moment rather than the graded written work. Judged a genuine match, not a mismatch — both are real, complementary traps. |
| P4 twist | **PASS** | Same fresh subagent re-derived the twist's effect under every stated Modeling Assumption from FACILITATOR.md alone: the twist (window-orientation uncertainty) genuinely invalidates any unconditional "August wins" position (2 of 4 untested MA1 orientations invert the winner), and its effect is independent of MA2/MA3 (both proven robust across their full tested ranges) and MA4 (which never reaches the D4 metric). No unstated convention required — not a BLOCKER. |
| P5 sensitivity | **PASS (disclosed)** | Mechanical, via `cases/the-late-run/sensitivity_model.py` (see below). MA1 (window orientation) flips the verdict at 2 of 4 flexed alternate orientations and breaks the SPEC §2 20% cap at the other flexed extreme — genuinely unstable, and now recorded in `case.json.sensitivity_disclosure[]` (Category X: the true window bearing is not publicly accessible; due-south is a good-faith estimate from the closest public analogue). MA2 (call time) and MA3 (September date) are mechanically confirmed robust: the winner never flips across their full ±50% flex range. MA4 (glare tolerance) does not reach the D4 metric at all. |
| P6 data decay | **PASS, with 2 noted findings** | All 12 cited URLs fetched live this pass (2026-08-31). 11 of 12 fully reachable and still carrying their cited figures verbatim (S1 soda-lime dispersion formula, S2 Brewster formula/56° example, S3 Tiffen 40%/4x/2-stop spec, S4 Locks coordinates, S5 WDFW counts — Aug 19=957confirmed still season-best, running total 9,566 through 8/25, Coho-availability wording — S6 Coho window wording, S10 Fresnel formulas, S11 "south side of the canal," S12 SRKW ESA/prey facts). **Finding 1:** S7 (ParentMap) still resolves (200) but its page content has changed to a bare event-calendar listing with no salmon-species/timing text — the URL is alive but no longer carries the cited claim, which SKILL.md flags as *worse* than a dead link since nothing else in the pipeline would notice. Not load-bearing alone (S6 independently corroborates the same Coho-window claim and is unaffected), but S7 should be swapped for a fresh corroborating source on the next research pass. **Finding 2:** S8/S9 (NOAA GML Solar Calculator, azel.html) is reachable and functionally correct but is self-labeled by NOAA as "the old version," pointing to a newer tool — not a decay finding today (fields/output match what's cited) but worth a POLISH-level note to re-point to the current URL on the next refresh. |

**VERDICT: TIER2_PASS** — all six probes recorded by name, 0 FAIL.

### Tier 3 — human dry-run
NOT RUN.

### Sensitivity model
`cases/the-late-run/sensitivity_model.py` reproduces the case's real D4 metric end to end from a
self-contained NOAA-style solar-position calculation (not looked up), calibrated to within
~0.15° azimuth / ~0.5° elevation of the case's own cited NOAA readings. Mechanically confirms,
independent of any prose claim:
- **Base:** A≈99.99%, B≈91.00%, margin≈9.9% (case of record: 10.7%, both well inside SPEC §2's cap;
  the small gap is this model's own documented calibration error, not a discrepancy in the case).
- **MA1 (window_normal_azimuth_deg) genuinely flips the verdict** — winner is A at 90°/180°(used)/225°,
  and **B at 135°/270°** — matching `case.json.modeling_assumptions[MA1]` exactly in direction and
  closely in magnitude.
- **MA2 (call_hour_offset_from_noon) and MA3 (sep_day_offset_from_16) are mechanically robust** —
  winner stays A across every ±50% flexed value tested (MA2: +13.1%/+9.9%/+1.7%; MA3: +8.2%/+9.9%/+11.7%),
  matching `case.json.modeling_assumptions[MA2/MA3]`.
- **MA4 (tolerance_multiplier) does not affect the D4 metric at all** (`evaluate()` never reads it) —
  confirmed by construction, matching FACILITATOR.md's note that MA4 only ever moves D2's answer.

This is the requested mechanical (not prose-trust) confirmation that MA1 is dilemma-flipping while
MA2/MA3 are robust.
