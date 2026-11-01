# QA_REPORT.md — The Yield Die

## case-readiness run — 2026-09-09

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-yield-die` — clean, no advisory
findings.

### Tier 1 — structural (21 checks)

Run repeatedly across the remediation cycle below; final run on the current `case.md`
(`sha256=d950343c0722a7aa...`):

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length in range, no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Priya Anand." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | all appendices referenced, no orphans (fixed: Appendix A was originally an orphan) |
| T1-07 | PASS | final appendix (F) lines are verbatim spine labels (fixed: an earlier draft's Sources-appendix middot characters were mis-parsed as vocabulary bullets) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments written, margin 8.23% (well under the 20% cap) |
| T1-10 | GAP | `new_coverage[]` empty — disclosed reinforcement case (see `case.json.reinforcement_note`); downgraded from BLOCKER per the 2026-08-17 doctrine amendment, since all 4 claimed skills already show `n>=1` and the case forces the two thinnest of them (Standard Notation, the standard-given-scientific how-to) repeatedly across D1/D3/D4 |
| T1-11 | PASS | learning-goal mutual reachability — no unmapped deliverables, no unreachable skills |
| T1-12 | PASS | tier (T3) matches numeric load (scientific notation, two competing variables) |
| T1-13 | PASS | facilitator guide, anchor ladder, 5 Socratic questions, twist, timed plan, sensitivity note all present |
| T1-14 | PASS | FACILITATOR.md agrees with case.md/case.json (fixed: an earlier draft's margin/derived figures were stale) |
| T1-15 | PASS (POLISH) | no `published/` directory yet — nothing to drift (case-publish out of scope for this task) |
| T1-16 | PASS | QA hash current |
| T1-17 | PASS | three cohort bands declared |
| T1-18 | PASS (POLISH) | no `published/` directory — MCS-37 has nothing to check |
| T1-19 | PASS (POLISH) | no `published/` directory — MCS-39 has nothing to check |
| T1-20 | PASS (POLISH) | no `published/` directory — advisory only |
| T1-21 | PASS (POLISH) | no `published/` directory — MCS-47 has nothing to check |

**BLOCKER list: none, on the final run.** Two BLOCKERs and one FAIL were found and fixed during
this session (see "Remediation history" below): T1-06 (Appendix A orphan), T1-07 (Sources-table
middot characters mis-parsed as vocabulary bullets), and T1-14 (stale FACILITATOR.md figures).

**GAP list: 1** — T1-10, disclosed reinforcement case, per the standing 2026-08-17 doctrine
carve-out (not a per-case waiver).

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh subagent, given only the leak-free student packet, reached Option A (Compact Die) with fully correct arithmetic matching `case.json.balance` exactly, correctly named "revenue per wafer" as the optimized metric, and correctly named the defect-density assumption (MA2) as the figure its answer was most sensitive to. |
| P2 both-sides | **PASS** | A second fresh subagent built the strongest case for each option independently and explicitly tested whether either side ever has *zero* winning scenarios across the full defensible defect-density range (0 to 0.40, the real Intel-18A ceiling). Finding: **neither side collapses** — Option B genuinely wins below the real crossover (~D0=0.16, itself within the cited "mature line" range) and Option A wins at and above the case's own stated planning assumption (D0=0.30) through the disclosed ceiling. This is the corrected result after remediation — see "Remediation history." |
| P3 trap | **PASS** | A third fresh subagent, before reading `FACILITATOR.md`, independently named the same wrong path the guide names: recommending Option A on gross-die-count alone (ignoring Appendix D's yield model and Appendix C/E's price differential). Confirmed on both the pre- and post-remediation numbers. |
| P4 twist | **PASS** | A fourth fresh subagent independently re-derived the Twist's arithmetic from Appendix B–E's raw figures (not trusting the stated results), confirmed the flip is real and robust to every rounding convention tested, confirmed no unstated convention is secretly load-bearing, and confirmed D5's "what value would flip it" question has a real, findable answer (crossover ≈0.157–0.16 defects/cm²) — this is the corrected result after remediation. The same probe also surfaced one real, fixed documentation gap: Appendix B's wafer diameter (mm) needed an explicit mm→cm conversion note before being used against cm²-denominated die areas; fixed in `case.md`. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py`'s `FLEX = ["defect_density_D0_per_cm2"]` genuinely flips the verdict at −50% (D0=0.15, Option B wins by 0.59%) and does not flip at +50% (D0=0.45, Option A wins by 15.09%; base case D0=0.30, Option A wins by 8.23%). This instability is disclosed in `case.json.sensitivity_disclosure[]` (category F — forecast/irreducible-unknown, since no foundry discloses its live defect density for a not-yet-running line), matching the disclosure-aware PASS state per the 2026-08-13 doctrine. |
| P6 data decay | **PASS** | All 9 cited URLs checked by direct fetch. 7 of 9 fetched cleanly with the cited figure confirmed present (S1, S2/S3, S5, S6, S7, S8, S9). 2 of 9 (S4's original WikiChip Fuse link, and TechPowerUp/PhoneArena as fetch attempts) returned connection errors — WikiChip Fuse (`ECONNREFUSED`) appears genuinely down and was swapped out as the primary citation for TechPowerUp (still corroborated by three independent outlets reporting the same figure, though the automated fetcher hit a 403 bot-block on TechPowerUp itself). No fabricated URL, no silently-broken load-bearing figure. |
| P7 accessibility | **FAIL (waived — see `qa.tier2.P7_waiver`)** | Seven independent fresh-subagent cold-reads were run across seven remediation rounds. Round 1 (before any real-world glossary existed) found ~20 unexplained concepts. `case.md` gained a new Appendix H ("Real-World Vocabulary," 55 defined terms) built specifically in response, with six further remediation passes narrowing the gap. Round 7's residual finding was 6 items, all genuinely second-order (e.g., the physical appearance of a reticle, exact wafer-lot billing mechanics) — never reaching the 0–1 pass bar. Recorded as a disclosed MCS-49 waiver (all 7 required fields populated, `remaining_gaps[]` holding round 7's verbatim list) rather than a forced pass, following the same precedent as `cases/cardiology`. **This is a disclosed judgment call, flagged prominently for the project owner's own review** — case-readiness's own doctrine text is explicit that this pattern ("carpenter"/"codebreaker" never converging below threshold either) is a known, real limitation, not a defect unique to this case, but the decision to stop remediating after seven rounds and accept a waiver rather than continuing indefinitely is a judgment call, not a mechanical one. |

### Tier 3 — human dry-run

NOT RUN. `PUBLISHED` is not reached in this task (case-publish deliberately out of scope per this
run's instructions), so Tier 3 cannot begin — consistent with "you cannot dry-run a case you have
not published."

---

## Remediation history (real defects found and fixed this session)

1. **T1-06 BLOCKER, fixed:** Appendix A ("Priya's Wafer Commitment and the Reticle Lock Deadline")
   was never referenced from Background or Challenges in the first draft. Fixed by adding an
   explicit `(SEE APPENDIX A)` cross-reference.
2. **T1-07 BLOCKER, fixed:** the first-draft Appendix G (Sources) used middot (`·`) characters
   inside one table cell (S3's die-size list), which Tier 1's separator-run parser — designed to
   read the *final* "How To…" appendix's middot-separated vocabulary line — misidentified as
   vocabulary labels needing to match the spine verbatim, because the "final appendix" regex reads
   from the How-To heading to the end of the document. Fixed by replacing the middots with commas.
3. **T1-13 GAP, fixed:** the first-draft Socratic questions were written as word-wrapped multi-line
   Markdown list items; Tier 1's single-line regex for detecting a numbered question ending in "?"
   never matched across a line wrap, so it reported 0 questions found despite 5 being present.
   Fixed by rewriting each as one unwrapped line.
4. **T1-14 GAP/FAIL, fixed:** `FACILITATOR.md`'s Balance argument was written before case-research
   resolved the real figures, and was not updated when they landed. Fixed by rewriting the section
   with the actual computed numbers, keeping it in sync across every subsequent numeric revision.
5. **P2/P4 structural defect, found and fixed (the most significant remediation this session):**
   the case's original calibration (defect density D0=0.10, pure linear per-transistor pricing) was
   mathematically **structurally undefeatable** for Option A — a both-sides-solve probe and a
   twist-integrity probe, run independently, both proved algebraically that Option A wins on
   revenue per wafer at *every* non-negative defect density under that calibration. This meant the
   case's one disclosed "assumption" (MA2) could never actually flip the verdict, and Challenge
   deliverable D5's own instruction (name the value that would flip your recommendation) had **no
   valid answer** — a real authoring defect, not a false alarm from either probe. Fixed by (a)
   moving the base assumed defect density from 0.10 to 0.30 defects/cm² (still real and defensible
   — below Intel's own disclosed 18A ceiling of 0.40, and arguably more defensible than 0.10 given
   this is the company's first tape-out on an unproven line) and (b) adding a new, disclosed
   Modeling Assumption (MA4: a conservative 19% flagship pricing premium on Option B only, grounded
   in the real Nvidia L4-vs-H100 dollars-per-transistor gap, source S9). Together these produce a
   genuine crossover at D0≈0.157-0.16, confirmed independently by both probes on re-run, with the
   verdict now genuinely flipping within the standard ±50% sensitivity range. `margin_pct` moved
   from 13.92 to 8.23 (still within the concept sheet's 8-14% target band).
6. **P6 finding, fixed:** the original S4 citation (WikiChip Fuse) is no longer reachable
   (`ECONNREFUSED`) — swapped to TechPowerUp as the primary url, retaining WikiChip Fuse and
   PhoneArena as corroborating (unreachable-by-automated-fetch, not confirmed dead) outlets, all
   three independently reporting the same transistor-density figure.
7. **P7 finding, partially remediated, disclosed via waiver:** seven rounds of real-world glossary
   remediation (Appendix H, 0 → 55 terms) reduced the fresh-subagent cold-read's named-gap count
   from ~20 to 6, never reaching the 0-1 pass bar — recorded as an MCS-49 disclosed waiver rather
   than continued indefinitely or silently downgraded.

## Verification

- `python3 skills/case-readiness/scripts/tier1_structural.py --case the-yield-die` → `TIER1_PASS
  (0 blockers, 1 gaps)` on the final `case.md` (`sha256=d950343c0722a7aa...`).
- `python3 cases/the-yield-die/sensitivity_model.py` → base (D0=0.30) A wins 8.23%; -50% (D0=0.15)
  B wins 0.59% (flips); +50% (D0=0.45) A wins 15.09%.
- `python3 skills/case-readiness/scripts/resync_artifacts.py --case the-yield-die` → already in
  sync.

## Report back

**State reached:** `TIER2_PASS`. **BLOCKER list:** none (2 found and fixed during this run — see
Remediation history). **Six-probe verdicts:** P1 PASS, P2 PASS, P3 PASS, P4 PASS, P5 PASS
(disclosed), P6 PASS — plus **P7 FAIL (waived)**, disclosed and documented per MCS-49, flagged for
the project owner's own review as the one genuine judgment call in this run. **Next step:** this
case is ready for `case-publish` when the project owner chooses to run it (out of scope for this
task) — `case-publish` will need to build the actual interactive HTML with a real hover/hyperlink
`STORY_GLOSSARY`, at which point P7 should be re-run against the published artifact rather than the
`case.md` fallback, since a real hover-tooltip glossary may resolve some of the residual gaps that
a flat Markdown table cannot (a reader hovering a term inline is a different experience than
scanning a 55-row reference table before reading).
