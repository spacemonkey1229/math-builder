# QA Report — college-admissions

## Tier 1 Structural Gate — 2026-08-17

**Command:** `python3 skills/case-readiness/scripts/tier1_structural.py --case college-admissions`

**Result:** `VERDICT: TIER1_PASS  (0 blockers, 1 gaps)`

- Checks run: 19 — PASS 18 · GAP 1 · FAIL 0
- Iterations used: 1 (no fixes required)

### Detail

| Check | Result |
|---|---|
| T1-01 | PASS |
| T1-02 | PASS |
| T1-03 | PASS |
| T1-04 | PASS |
| T1-05 | PASS |
| T1-06 | PASS |
| T1-07 | PASS (POLISH note: parsed 15 labels — 15 bulleted, 0 from separator-run lines; separator run is the half the legacy check skipped) |
| T1-08 | PASS |
| T1-09 | PASS |
| T1-10 | GAP — `new_coverage[]` is empty; the case closes no NEW gap. Legacy-conversion carve-out applies: this title is already credited in `standards_spine.json`'s `covered_by[]` from the pre-pipeline corpus scan, so no uncovered skill remains for it to honestly claim. Downgraded from BLOCKER per the 2026-08-13 doctrine amendment (project-owner approved, not a per-case waiver). `case.json.legacy_conversion_note` is present and non-empty, which is why this correctly showed as GAP rather than BLOCKER. |
| T1-11 | PASS |
| T1-12 | PASS |
| T1-13 | PASS |
| T1-14 | PASS |
| T1-15 | PASS |
| T1-16 | PASS |
| T1-17 | PASS |
| T1-18 | PASS |
| T1-19 | PASS |

### Notes

No blockers surfaced, so no case-file fixes were needed this run. The single GAP (T1-10) is the expected, permanent legacy-conversion carve-out, not an issue requiring remediation.

Per the self-report, the case sits at TIER1_PASS / `status: "qa"` and is **not yet eligible for `case-publish`** — Tier 2 (simulated-play probes) has not been run in this session. Open human-review items carried over from the self-report:

1. Sanity-check the Common Data Set figures' secondary sourcing (S1–S3, confidence MEDIUM) — the primary `irds.stanford.edu` PDF returned HTTP 403 to automated fetch this session.
2. Decide whether Tier 2's six simulated-play probes should be run before this case is considered publish-eligible.

## case-readiness run — 2026-08-17 (Tier 2)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (19 checks, re-confirmed)

Re-ran `python3 skills/case-readiness/scripts/tier1_structural.py --case college-admissions` before
starting Tier 2. Result unchanged: `VERDICT: TIER1_PASS (0 blockers, 1 gaps)`. 18 PASS, 1 GAP
(T1-10, the standing legacy-conversion carve-out — see Tier 1 section above), 0 FAIL, 0 BLOCKER.
`sha256(case.md) = 28cee4b5e75acf2d55b0036dec36f1ec7ec20610b5009820eda95eb0a88382d8` — matches
`case.json.qa.case_md_sha256`, so T1-16 is current and every other finding in this report describes
the file actually on disk.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent cold-solve (packet-only, no `FACILITATOR.md`/`QA_REPORT.md`/`case.json`) chose **B — Admit Harrison Carter**, named its metric explicitly (position within Stanford's own published SAT/ACT Composite IQR, Appendix A — justified as "the yardstick the committee uses"), and showed correct arithmetic: SAT gap 1520−1480=40 → 40/1480=2.7%; D5 headcount Tisha 0.03×3200=96, Harrison 0.07×649≈45. Named the strongest counterargument (Tisha's better in-school percentile, GPA, and holistic hooks), the most sensitive assumption (MA2's 649-student national-average proxy), an appendix item correctly ignored (ACT-submission-rate %, a reporting-behavior stat not a competitiveness benchmark), and the least-supported number (the 649 national-average enrollment). Reached the intended route (D4/D5 as designed) by the right reasoning, not by luck — passes the "right answer for the right reasons" bar. |
| P2 both-sides | **PASS** | Strongest case built for each option independently, both numerically grounded. **A:** "Tisha out-ranks Harrison within her own school (3rd vs. 7th percentile) and holds the higher unweighted GPA (3.73 vs 3.69), plus is a first-generation, lower-income applicant whose profile Stanford's own admit data (Appendix A) signals the committee values beyond a raw test-score comparison." **B:** "Harrison's SAT (1520) and ACT (34) both land inside Stanford's own published middle-50% admitted range (Appendix A) while Tisha's fall below it on both tests, and his broader, higher-scoring AP record (6 exams, 4.83 avg, three 5s) plus a concrete Intel technical credential give the committee the most externally verifiable evidence of Stanford-level readiness." Neither side collapses outright: A's weakest joint (the percentile-rank comparison) is complicated, not destroyed, by D5's headcount conversion — Harrison's raw headcount-above (≈45) is in fact lower than Tisha's (96), which tempers but does not reverse the case for A, since A's GPA/first-gen/income arguments stand independent of rank. B's weakest joint (near-tied GPA, 3.69 vs 3.73) is a real but minor concession that doesn't touch its core evidence (test-score IQR position, AP record, résumé credential). Neither argument is a bare concession ("B is cheaper but worse in every other way") — both carry real, load-bearing numbers throughout. The recorded 2.7% margin is not a paper number: it is the graded metric (D4), stable by construction, and both sides remain genuinely arguable on the case's other deliverables. |
| P3 trap | **PASS** (mechanical pre-screen false-flagged, overridden on independent read — see note) | The tier2_probes.py machine screen returned FAIL: its regex captures only the first 400 characters after the literal word "trap" in `FACILITATOR.md`, which truncates mid-sentence before any of its required action-verb keywords (`will/students/assume/...`) appear — a scoping artifact of the screen's fixed-length capture window, not a defect in the actual trap. Independent cold read of `case.md` alone (before opening `FACILITATOR.md`) named the same wrong path an unbriefed solver would take: a hurried student sees "Tisha: 3rd percentile" vs. "Harrison: 7th percentile" and concludes Tisha's class rank is unambiguously stronger, because a smaller percentile number reads as "closer to the top" — silently assuming the two high schools are comparably sized. `FACILITATOR.md`'s "The trap, named explicitly" section (and its Socratic Q1/Q2) names this exact path, describes what a Hero will concretely *do* (commit to "3rd beats 7th, obviously" in Anchor 4 before the Twist), and the case's own Background paragraph plants the setup ("Appendix A also does not... tell Jack how many classmates rank above a given applicant... that takes combining a rank percentile with a school's actual size"). Guide and independently-derived trap match exactly — real PASS. |
| P4 twist | **PASS** | (1) The twist invalidates the position a real room would hold after Anchor 4: that Tisha's 3rd-percentile rank is unambiguously the stronger credential. Converting both percentiles to raw headcounts (D5) shows Harrison's estimated headcount-above (≈45, using the MA2 national-average stand-in) is *lower* than Tisha's fixed 96, complicating the naive smaller-number-wins read. (2) Re-derived under every stated modeling assumption: MA1 (fictional committee frame, real CDS data) is orthogonal to the twist. MA2 (Harrison's national-average school-size substitution) is exactly the twist's mechanism, not a threat to it. MA3 (unstated, possibly-differing ranking methodology between the two schools) does not neutralize the twist — it adds a second, disclosed layer of uncertainty on top of it, but does not make the headcount conversion vacuous the way Cold Chain's sequential-reading bug once did. MA4 (SAT box-plot median-as-midpoint estimate) is unrelated to class rank/D5 entirely. Checked an alternate reading of "class-rank percentile" (bottom-percentile vs. top-percentile convention) against Appendix A's own framing ("97.8% of admits ranked in the top tenth of their class") — the case's convention (smaller percentile = closer to the top) is the only reading consistent with both applicants' files and Appendix A, so no undocumented convention is silently required. No capacity limit is stated for this case (unlike Cold Chain's cold-chain capacity), so there is no analogous constraint to re-check. Twist survives every defensible reading. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case college-admissions --probe 5 --flex 0.5`. Base: A=1480, B=1520, winner B, margin 2.7%. Scope: swept the one declared FLEX[] dial, `harrison_hs_enrollment_assumed` (the MA2 national-average school-size stand-in, ≈649). At −50% (324.5) and +50% (973.5): winner stays **B**, margin stays **2.7%** in both directions — `flips: false`, `breaks_20pct_cap: false` at both ends. Machine status: `PASS` (not `PASS_DISCLOSED`) — the graded `primary_metric`/`evaluate()` is the SAT-Composite-gap-percent, which is given verbatim in both applicants' files and is untouched by the enrollment assumption by construction, so there is no unstable param requiring a `sensitivity_disclosure[]` entry. (The genuinely enrollment-sensitive quantity — D5's raw-headcount-above estimate — is a disclosed *secondary* comparison, not the graded metric; its own ~3x sensitivity is already written up in `FACILITATOR.md`'s "Assumption-sensitivity disclosure" section and `case.json.balance.stability`, which is the correct treatment per SPEC §2/§5 for a non-graded finding, not a P5 FLEX-scoping requirement.) |
| P6 data decay | **PASS** | Fetched all 6 `sources[].url` entries (all `accessed: 2026-08-17`, age 0d). **S1** `cosmic.nyc` — reachable, figure confirmed verbatim: "Total applicants: 57,326", "Admitted students: 2,067", "Acceptance rate: Approximately 3.6%". **S2** `blog.collegevine.com` — reachable, confirmed: "middle 50%... scored between 1510 and 1570 on the SAT... composite ACT score between 34 and 35", "50.3% submitted an SAT score, and 19% submitted an ACT score". **S3** `koppelmangroup.com` — reachable, confirmed: admit rate 3.61%, SAT 25th/75th 1510/1570, ACT 25th/75th 34/35, avg GPA 3.94, 73.30% at 4.0 GPA, 97.80% top-tenth rank. **S4** `irds.stanford.edu` — HTTP 403 (unreachable to automated fetch), same failure mode already disclosed in the source's own `claim` text at conversion time ("direct PDF fetch blocked (403)"); this source backs only the institutional-provenance claim ("Stanford publishes a CDS annually"), not any of the load-bearing numeric figures, which are independently corroborated by the reachable S1–S3. Not a new decay finding, not a BLOCKER — a pre-existing, already-disclosed access limitation, unchanged since conversion. **S5** `nutmegeducation.com` — reachable, confirmed: "total number of high school enrollment for public high schools was 15,492,000 for the year 2022", "around 23,872 public high schools". **S6** `publicschoolreview.com` — reachable, confirmed: "national average public school student size is approximately 511 students (2026)" — matches the case's stated "≈511-514" range used as corroboration, not as the primary derived figure (S5's 15,492,000/23,872=648.96 is the actual Appendix B figure). No dead links among load-bearing sources, no drifted figures, all sources under 365 days old. |

### Tier 3 — human dry-run

NOT RUN. `PUBLISHED` may proceed on Tier 1 + Tier 2 clean (per the ladder); `VERIFIED` still
requires a filed `cases/college-admissions/runs/RUN_<date>.md` before this case can be marked ✅ in
`DOCTRINE_LEDGER.md`.

### Next step

`case.json.qa.state` set to `TIER2_PASS`. Case is now eligible for `case-publish`. Schedule the
Tier 3 human dry-run before any `DOCTRINE_LEDGER.md` ✅ claim.
