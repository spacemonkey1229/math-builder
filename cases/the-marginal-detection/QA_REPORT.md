# QA_REPORT.md — The Marginal Detection

## case-readiness run — 2026-09-18

**State reached:** DRAFT → TIER1_PASS → TIER2_PASS
**Verdict:** PASS

### Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/tier1_structural.py --case the-marginal-detection`,
iterated three times as real defects were found and fixed (see "Real defects found and fixed"
below), final run:

```
checks run: 24   PASS 21 · GAP 3 · FAIL 0
VERDICT: TIER1_PASS  (0 blockers, 4 gaps)
```

| id | result | note |
|---|---|---|
| T1-01–T1-08 | PASS | structural sections, Overview/Dilemma/Challenge boilerplate verbatim, appendix referencing (no orphans), Appendix E verbatim spine labels, every figure cited or a stated assumption |
| T1-09 | GAP | margin 19.2% is inside the SPEC §2 20% cap but wide — flagged as a GAP ("the discussion will be one-sided"), not a blocker. Accepted: the margin is deliberately close to the cap because the case's real tension is that the two methods land on *opposite sides* of the 3.0 decision threshold, not a close dollar-cost race — see `case.json.balance.margin_basis` |
| T1-10 | GAP | `new_coverage[]` is empty — reinforcement carve-out applies. `case.json.reinforcement_note` records that all 9 claimed skills were checked against the spine before writing: none is `n=0` (non-linear, line-of-best-fit how-to, box-and-whisker how-to are the 3 THIN target skills at n≤2; outlier/scatter-plot/correlation/quartiles are reinforced adjacent skills), and no genuinely uncovered (`n=0`) skill elsewhere in Statistics And Probability fits this case's actual deliverables without padding |
| T1-11 | PASS | LEARNING GOAL CHECK — 0 unmapped deliverables, 0 unreachable skills (see `LEARNING_GOALS.md`) |
| T1-12 | PASS | tier (T2) matches numeric load — multi-step line-fit + box-and-whisker comparison, two competing variables (which method to trust) that trade off |
| T1-13 | PASS | 5 Socratic questions, trap named, full anchor ladder, 45-minute timed plan, sensitivity note present |
| T1-14 | PASS | `FACILITATOR.md` agrees with `case.json.derived`/`balance` |
| T1-15 | GAP | two sub-findings, both confirmed false positives from checker limitations, not real drift: (a) 12 negative xlsx cells (e.g. `Appendix A — Light Curve!C4=-12.0`) flagged as "no match in case.md" — `tier1_structural.py`'s `NUM_RE` regex does not parse a leading minus sign, so case.md's own `-12` is indexed into the checker's "number universe" as unsigned `12.0`, not `-12.0`; xlsx correctly stores the real negative value `-12.0`, which is why it doesn't match. Confirmed by direct inspection: case.md and the xlsx agree on every one of the 20 flux values. (b) `FACILITATOR.md`'s own `§7.3` (a SPEC section reference) and `38:00` (a clock time > 23, so the checker's clock-time exclusion doesn't recognize it) both get parsed as literal numbers `7.3`/`38.0` — the same precedented false-positive class already on file for `cases/the-approval-gate/QA_REPORT.md` ("SPEC Section 7"/"SPEC section 7.3") |
| T1-16 | PASS | `case.json.qa.case_md_sha256` matches `sha256(case.md)` |
| T1-17 | PASS | `cohort_bands[]` declared, 3 bands |
| T1-18 | PASS | Interactive HTML present, fresh (mtime ≥ case.md's), no `balance_test` literal leak, no numeric Working Notebook placeholder |
| T1-19 | PASS | 9-term hover+hyperlink math glossary (≥8 required), all links allowlisted (khanacademy.org ×6, mathsisfun.com ×0 — corrected: cuemath.com ×1, khanacademy.org rest), all verified live |
| T1-20 | PASS | 3 real SVG visuals present (light-curve scatter + fitted line, box-and-whisker plot, linear-vs-non-linear illustrative diagram); real data sourced/cited |
| T1-21 | PASS | 7-term `STORY_GLOSSARY` (domain vocabulary: Transit, Light Curve, Exoplanet, Photometric, Pipeline, Kepler Mission, Signal-to-Noise, Stellar Magnitude, Statistical Trials — 9 total after remediation), all Wikipedia links verified live |
| T1-22 | PASS | published HTML's own section headings match case.md's |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | (advisory, no hand-drawn SVG connector lines in this case) |

**VERDICT: TIER1_PASS (0 blockers, 4 gaps, all 4 gaps confirmed accepted/false-positive, none a
real defect).**

### Real defects found and fixed during this run

1. **T1-18 BLOCKER (first run): Working Notebook numeric placeholder.** Step 3's `sig_robust`
   input field originally had `placeholder="dip ÷ (0.7413×IQR)"` — the `0.7413` constant inside a
   placeholder reads as a worked numeric example per the MCS-37 rule (`skills/case-readiness/SKILL.md`,
   "A third defect found in later use"). Fixed: placeholder changed to `"dip ÷ robust noise unit"`
   (format only, no digit).
2. **T1-15/T1-21 (first run): the published HTML's Appendix A data table was JS-rendered into an
   empty `<tbody>`, not static markup.** This didn't trip any Tier 1 check directly, but it broke
   Tier 2 P7's text-extraction packet (see "Tier 2 — Real defect found and fixed" below) — the
   interactive-shell contract (`templates/INTERACTIVE_HTML_CONTRACT.md`) explicitly says appendix
   tables should be authored as normal static `<table>` markup, and this case's first draft
   violated that. Fixed: all 20 rows are now literal, static HTML; the JS chart-drawing functions
   read the same `FLUX` array to draw the scatter/line/box-and-whisker visuals but no longer
   overwrite the table body.
3. **T1-21 GAP (first run): no `STORY_GLOSSARY` at all.** Fixed by adding the full `STORY_GLOSSARY`/
   `.sterm` mechanism (CSS, container, object, render/auto-link functions) per the same pattern
   `cases/the-approval-gate` used, with domain terms verified live this session (Wikipedia ×6).

---

# TIER 2 — SIMULATED PLAY (seven probes, all fresh-subagent-adjudicated except P5/P6)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet only. Independently re-derived both significance ratios to the same precision as `case.json.derived` (3.006σ naive, 2.521σ robust), correctly identified the naive method's r≈−0.03 (essentially no real linear trend, i.e. it's fitting noise) as the reason to distrust it, chose **B**, named the metric, showed full arithmetic, correctly flagged MA2 (the 3.0 threshold)/MA1 (the light curve itself) as most sensitive, and named the light curve's constructed-scenario status as the least-supported figure — all unprompted. |
| P2 both-sides solve | **PASS** | Fresh subagent. Built genuine, numbers-grounded cases for both A (procedural: "the survey's own policy is met by its own stated method, 3.006 clears 3.0") and B (substantive: "the one method immune to the night's proven curved drift puts this candidate under the bar"). Found A's defense collapses under direct questioning about whether its razor-thin 0.006 margin is itself an artifact of the very curvature bias Appendix B warns about — a real, sourced-from-the-case-text critique, not a manufactured concession. Both sides genuinely defensible before that pressure point; margin is not a paper number. |
| P3 trap check | **PASS** | Fresh subagent, packet only, before reading `FACILITATOR.md`. Independently named the exact trap the guide names: "compute Method 1's 3.006, see it clears 3.0, stop there because it's the more work-showing/rigorous-looking calculation, without asking whether a straight-line fit is even the right tool for a visibly curved night." This matches `FACILITATOR.md`'s trap verbatim in substance. |
| P4 twist integrity | **Initially FAIL → remediated → PASS** | See "Real defect found and fixed" below — a genuine unstated-convention ambiguity (which standard-deviation denominator; which quartile method) was found, fixed by stating both conventions explicitly in `case.md` and the interactive HTML, verified the case's own numbers (3.006 / 2.521 / 19.2%) are unchanged and now the *only* value reproducible under the stated conventions. |
| P5 assumption sensitivity | **PASS (disclosed)** | Mechanical (`sensitivity_model.py`). Base: sig_naive(A)=3.006, sig_robust(B)=2.521, margin 19.2%. `transit_dip_ppm` (the only FLEX[] param — `followup_threshold_sigma` is held fixed per the same "structural, not a dial" precedent as `the-approval-gate`'s gate thresholds): the naive/robust *order* never flips under ±50%, but −50% breaches the 20% cap (24.5%). Disclosed as Category X in `case.json.sensitivity_disclosure[]`, together with a qualitative (non-FLEX) threshold-crossing check showing both MA1 and MA2 are genuinely load-bearing to the case's central "the two methods disagree" tension. |
| P6 data decay | **PASS** | All 5 `sources[]` URLs fetched and confirmed live and figure-bearing this session (age 0 days): S1 (TESS precision, IOPscience), S2 (Kepler 7.1σ, arXiv), S3 (AAVSO, Wikipedia), S4/S5 (NASA Exoplanet Archive, including the HD 189733 b overview page's real 2.4% transit depth). No dead links, no drifted figures. |
| P7 accessibility cold-read | **FAIL (waived, MCS-49)** | 3 genuine remediation rounds (see below), still FAIL on a narrowed set of "why is this true" depth questions. Waived, not eliminated — see `case.json.qa.tier2.P7_waiver` for the full record. |

### Tier 2 — Real defect found and fixed (P4)

A fresh subagent dispatched against `FACILITATOR.md` + the student packet independently re-derived
both significance ratios by hand and found **two unstated-convention ambiguities** in Appendix B's
method descriptions:

1. **Residual standard-deviation denominator.** "Take the standard deviation of those residuals"
   does not say whether to divide by n (population), n−1 (sample), or n−2 (regression standard
   error, correcting for the two fitted line parameters). Under n−2, the naive ratio falls to
   **2.904 — below the 3.0 threshold**, which would put *both* methods on the same side of the
   line and collapse the entire "the two methods disagree" premise the Twist depends on.
2. **Quartile method.** The case's Q1/Q3 (−42.5, 71.75) match the linear-interpolation convention
   (the same one spreadsheet `PERCENTILE.INC` and NumPy's default use) but not the "split the data
   in half, take the median of each half" convention more commonly taught at the MS level — which
   gives Q1=−45, Q3=75.5, and a different (though still sub-3.0) robust ratio of 2.390.

**Fix applied directly to `case.md` and the published Interactive HTML** (not just noted): Appendix
B's Method 1 paragraph now states explicitly "sample standard deviation... divide the sum of squared
residuals by (16 − 1) = 15... not the population or regression-standard-error version," and Method
2 now states explicitly "using the linear-interpolation method for Q1 and Q3... not the split-the-
data-in-half method." Verified: `sensitivity_model.py`'s own `_stdev()` (÷(n−1)) and `_percentile()`
(linear interpolation) already implemented exactly these conventions — only the case's prose was
ambiguous, not the actual arithmetic or `case.json`'s recorded numbers. No numbers changed; the
case's stated 3.006σ/2.521σ/19.2% margin are now the unique, reproducible result under the stated
rules, closing the ambiguity P4 exists to catch.

### Tier 2 — P7 accessibility cold-read: three real remediation rounds, then a disclosed waiver

**Round 1 (before the table-static-markup fix): FAIL.** A fresh, zero-context subagent named 5
unexplained real-world concepts (IQR/0.7413 constant, "residual," Kepler's "combined detection
statistic"/statistical-trials logic, "normalized" flux/ppm, the stellar-magnitude scale) and,
separately, said it could not picture the light curve's actual shape/data at all — because the
packet-building text extraction read an *empty* `<tbody>` (the table was JS-rendered, not static
markup, violating `templates/INTERACTIVE_HTML_CONTRACT.md`'s own "write appendix tables as normal
`<table>` markup" rule), so the cold-reader never saw a single one of the 20 real data points, only
the chart captions describing them.

**Remediation 1:**
- Made Appendix A's data table static HTML (Tier 1 fix #2 above) so a text-extraction packet now
  contains every real value.
- Added `GLOSSARY["Residual"]` (Khan Academy, verified live) and inline plain-English glosses for
  "normalized"/ppm (a thermometer analogy) directly in Appendix A's prose.
- Added `STORY_GLOSSARY["Stellar Magnitude"]` and `STORY_GLOSSARY["Statistical Trials"]` (Wikipedia,
  both verified live) for the two Appendix C domain concepts.

**Round 2 (fresh subagent, after remediation 1): still FAIL.** "Residual" and "normalized"/ppm were
resolved, but 6 new/remaining items surfaced: the 0.7413 constant's derivation, the unshown
linear-interpolation formula, an ambiguous "how exactly is dip depth computed from 4 points" rule,
magnitude-scale depth, Kepler-statistic mechanics, and the statistical-trials causal link — plus
(MCS-51) an unpicturable central mechanism: the scheduling-field/queue-default system in the
Overview.

**Remediation 2:**
- Renamed `STORY_GLOSSARY["Stellar Magnitude"]` → `["Magnitude"]` so the literal text "TESS
  magnitude 10" actually triggers the auto-linker (the two-word key never matched the prose).
- Added an explicit dip-depth computation rule to both Method 1 and Method 2 in Appendix B ("the
  dip depth is the line's/median's value minus the average of the four in-transit flux values").
- Added a one-clause derivation for 0.7413 (≈ 1 ÷ 1.349, the normal-distribution IQR-to-SD ratio).
- Added an apposition clarifying Kepler's "combined detection statistic" is the same kind of ratio
  this case computes, and a parenthetical on what one "statistical trial" means operationally.
- Rewrote the Overview's opening and closing paragraphs with more concrete (still non-numeric)
  staging of the dashboard/scheduling mechanism (a spreadsheet-like flagged-candidate table; a
  named scheduling field; an explicit "types a target name in, or the default fills it" mechanic).

**Round 3 (fresh subagent, after remediation 2): still FAIL**, but on a materially narrower set —
5 items, all now "why is this physically/statistically true" depth questions rather than "what does
this term mean" comprehension gaps (why air-thickness drift curves rather than just knowing it
does; what a magnitude *unit* represents; the multi-night statistic's operational mechanics; one
"trial"'s operational definition; the 1.349 constant's own derivation), plus the same Q2 finding on
the scheduling-field mechanism, softened but not eliminated by remediation 2's concreteness.

**Disposition: waived per MCS-49**, mirroring the Cardiology precedent (3 genuine remediation
rounds, then a disclosed-partial waiver rather than open-ended iteration). Full required fields —
`granted`, `reason`, `remediation_rounds: 3`, `terms_added_total: 3`, `remaining_gaps[]` (the
verbatim round-3 list), `approved_by`, `date` — are recorded in `case.json.qa.tier2.P7_waiver`.
`tier2_probes.py`'s own convention records this as `"P7": "FAIL (waived — see
qa.tier2.P7_waiver)"` in the machine-readable table; the underlying FAIL and every round's
transcript is preserved above, not hidden.

---

## Tier 3 — human dry-run

NOT RUN. This case is being taken to `PUBLISHED`, not `VERIFIED`, in this pipeline pass — Tier 3
requires a real cohort and is out of scope here. `cases/the-marginal-detection/runs/` does not yet
exist.

---

## Live browser audit (2026-09-18)

Per this project's own doctrine (text-based checks miss real rendering/behavior bugs), opened
`published/The Marginal Detection - Interactive.html` in a real Chromium browser (served over a
local HTTP server, since `file://` access was unavailable in this environment) and clicked through
every interactive surface:

- **Zero console errors, zero failed network requests** across the full session.
- **Tab navigation** (Overview/Background/Dilemma/Challenges/Appendices/Working Notebook/Twist) —
  all 7 tabs load and scroll correctly.
- **Appendix A scatter chart** — renders all 20 points, transit window in red, gold fitted line
  overlaid correctly.
- **Linear-vs-non-linear illustrative diagram** — renders correctly.
- **Appendix A data table** — all 20 rows present and correct (confirmed the earlier JS-render bug
  is fully fixed).
- **Appendix B box-and-whisker chart** — renders a correct five-number-summary box.
- **Math glossary (9 terms) and Story glossary (9 terms)** — both render as expected chip grids.
- **Dilemma pick** — clicking Option B updates the header pill to "Current pick: B" live, confirmed
  via `localStorage` persistence mechanism.
- **Working Notebook Steps 1–3** — tested with both correct and incorrect values:
  - Step 1 (slope/intercept -0.345/18.84): green check, computed residual SD = 76.71 ppm — matches
    `case.json.derived.resid_sd_ppm` exactly.
  - Step 2 (sig_naive = 3.006): green check. Also tested a wrong value (5.5): correctly showed "try
    again" in red.
  - Step 3 (Q1=-42.5, Q3=71.75, sig_robust=2.521): green check, computed IQR=114.3 ppm and
    0.7413×IQR=84.69 ppm — matches `case.json.derived` exactly.
  - Step 4 dropdown (3 options: both-clear/both-miss/disagree) — present and functional, correctly
    un-graded (judgment call, as designed).
- **Twist reveal** — "I've been told to reveal it" button correctly reveals the narrative and
  disables itself (text changes to "Revealed"); the "show both ratios" checkbox correctly computes
  and displays **3.006** and **2.521** live from Appendix A's embedded data, matching the case's
  recorded values to 3 decimal places.

**No rendering or behavior bugs found.** One environment note, not a case defect: this session's
Browser pane is shared across multiple concurrent agents publishing other cases in the same batch
(tabs for `the-mooring-choice`, `the-absorption-call`, `the-constellation-bid`, `the-hub-choice`,
etc. were observed sharing the same pane) — every action was re-targeted at this case's explicit
`tabId` after confirming tab identity via `tabs_context`, since an un-scoped action would otherwise
land on whichever tab another concurrent agent had just fronted.

---

## Final state

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 4,
  "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS (remediated)",
            "P5": "PASS (disclosed)", "P6": "PASS", "P7": "FAIL (waived -- see qa.tier2.P7_waiver)"}
}
```

Next step: `case-publish` may run (packet already built into `published/`; the read-model write
[`cases_index.json`/`standards_spine.json`/`gap_queue.json`] is explicitly deferred per this
batch's own instructions, to avoid a write conflict with parallel agents doing the same batch).
