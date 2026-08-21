# QA Report — AirBnb Or Landlord

## case-readiness run — 2026-08-20
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 190 words, present tense, no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Dwayne and Wendy Dalton." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form consistent (`N.)`) |
| T1-06 | PASS | all 8 appendices referenced, no orphans (fixed: Appendix G originally orphaned, added a Background cross-reference) |
| T1-07 | PASS | final appendix (Appendix H) lines are verbatim spine labels |
| T1-08 | PASS | every number cited [S1]-[S6] or declared a Modeling Assumption (Appendix F) |
| T1-09 | GAP | margin 18.5% is inside SPEC §2's 20% cap but wide; the discussion will lean toward B without the Twist |
| T1-10 | GAP | `new_coverage[]` honestly empty; downgraded from BLOCKER under the 2026-08-13 legacy-conversion carve-out (`legacy_conversion_note` present) |
| T1-11 | PASS | mutual learning-goal reachability, 0 unmapped deliverables, 0 unreachable skills (fixed: `advanced-numbers-how-to-divide-decimal-numbers` was originally unreachable, mapped into D3) |
| T1-12 | PASS | T2 tier matches numeric load (5 deliverables, percent/decimal/ratio, two competing variables) |
| T1-13 | PASS | FACILITATOR.md has full 11-anchor ladder, Twist, 5 Socratic questions (one per line, fixed from an earlier multi-line format the question-counter missed), timed 45-minute Socratic plan (fixed: added) |
| T1-14 | GAP | 2 benign numbers in FACILITATOR.md prose ("11-anchor ladder", "40-hour work week") have no case.md/case.json home — not case data, not moved |
| T1-15 | PASS | no published/ directory yet — nothing to drift |
| T1-16 | GAP | sha256 recorded on this run (expected note on a first run) |
| T1-17 | PASS | `cohort_bands[]` declared, 3 bands with size range + note each |
| T1-18 | PASS | no published/ directory yet — nothing to check |
| T1-19 | PASS | no published/ directory yet — nothing to check |

**BLOCKER (0):** none.

**GAP (4):** T1-09 (margin width, informational), T1-10 (expected legacy carve-out), T1-14 (2 benign non-data numbers in guide prose), T1-16 (expected pre-run note).

**POLISH (4):** T1-07 (all labels parsed as bullets, none needed the separator-run parser), T1-15/T1-18/T1-19 (no `published/` directory exists yet — this conversion stops at TIER2_PASS per instructions, before `case-publish`).

Two real defects were found and fixed during this run:
1. **T1-06 BLOCKER (fixed):** Appendix G (Sources) was never cross-referenced from Background — added `(SEE APPENDIX G)` to the sentence about cited figures.
2. **T1-11 GAP (fixed):** `advanced-numbers-how-to-divide-decimal-numbers` was claimed in `standards[]` but no deliverable forced it — mapped into D3 (dividing a decimal annual total by 12 to get a monthly figure).
3. **T1-13 BLOCKER x2 (fixed):** FACILITATOR.md's five Socratic questions were written across multiple lines each, which the question-counter's single-line regex missed entirely (reported as 0 questions) — reformatted to one line each. The mandatory 45-minute timed Socratic plan (SPEC §7.3) was missing entirely — added.
4. **T1-14 BLOCKER (fixed):** `balance_test.margin_pct` (18.5) did not appear anywhere in FACILITATOR.md — added to the Twist section.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh subagent, packet only, no FACILITATOR.md/case.json/QA_REPORT.md access. Chose B, arithmetic matched `sensitivity_model.py`'s `evaluate()` exactly to the cent ($14,112.50 / $16,724.60 / 18.5%), correctly named annual net profit (converted to monthly) as its optimized metric, and independently surfaced the contested-occupancy counter-argument as its strongest objection — a defensible position reached for the right reasons. |
| P2 both-sides | PASS | Worked directly. Neither option reads as pure concession: A's real net profit ($14,112.50) is a substantial, legitimate number even under the case's own default (uncontested-favoring) data — a competent Hero can defend it without resorting only to "A is worse but has other virtues." B does not collapse either — its lead survives every ±50% flex of its own assumption without ever losing to A. |
| P3 trap | PASS | Fresh subagent, packet-only prediction (before reading FACILITATOR.md) independently named the same trap the guide names: computing Airbnb's gross revenue correctly, then stopping before subtracting the 15.5% host fee and the extra utilities cost, and wrongly declaring Airbnb the landslide winner on a gross-vs-net mismatch. The subagent judged the guide's trap the one most likely to actually catch a room. |
| P4 twist | PASS | Worked directly, cross-checked against `sensitivity_model.py`'s `evaluate_twist()`. The 116-hour (58 bookings x 2 hrs) self-cleaning labor reveal invalidates a naive "Airbnb profit is directly comparable to traditional profit" position without flipping either D1/D2 dollar total. The figure follows directly from Background's stated 2-hour cleaning time and Appendix F/MA2's stay-length assumption — no unstated convention required, holds under every defensible reading. |
| P5 sensitivity | PASS_DISCLOSED | Mechanical run via `tier2_probes.py --probe 5`. Both declared `FLEX[]` assumptions are genuinely unstable under a +50% flex (`avg_stay_nights` -> 23.8% margin; `furnished_premium_pct` -> 32.5% margin, both breaking SPEC §2's 20% cap; neither ever flips the winner from B). Both disclosed with Category-F justifications in `case.json.sensitivity_disclosure[]` — machine-verified `PASS (disclosed)`, not a stable-margin pass. |
| P6 data decay | PASS | Fresh fetch-capable subagent. All 4 live sources (S1 AirROI, S2 Zumper, S3 furnishedunfurnished.com, S4 Airbnb Help Center) reachable, cited values confirmed present and unchanged. One real nuance found and fixed: S4's page describes two live Airbnb fee structures (an older ~3% split-fee model still active for some hosts, and the newer 15.5% single host-only fee this case uses) — case.md/case.json did not originally make explicit which structure the case models. Fixed in case.md Appendix D and case.json S4's note. S5/S6 are non-fetchable local source-folder image/PDF references (historical color only, not load-bearing to D1/D2), not re-checked. |

**0 FAIL. 6/6 probes recorded by name. TIER2_PASS.**

### Tier 3 — human dry-run

NOT RUN. No `cases/airbnb-or-landlord/runs/` directory. Per instructions, this conversion stops at
`TIER2_PASS` — `case-publish` was not run.

---

**Next step:** `case-publish` may run whenever a human wants to promote this case (two confirms,
per the pipeline gate) — not run as part of this conversion per explicit instruction to stop at
`TIER2_PASS` and report back.
