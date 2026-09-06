# QA Report — The Deep End

## case-readiness run — 2026-09-05
**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (21 checks)

Run 1 (initial draft): 2 BLOCKERs (T1-06 orphan Appendix D; T1-18 no interactive HTML), 4 GAPs.
All fixed (Appendix D referenced from Background; interactive HTML built from
`templates/interactive_shell.html`; Socratic questions reformatted to single lines so the
Tier 1 regex could see them; orphan facilitator numbers rephrased away; STORY_GLOSSARY added
for MCS-47/T1-21).

Final run: **0 BLOCKERs, 2 GAPs, 0 FAILs.**

| id | result | note |
|---|---|---|
| T1-01..T1-12 | PASS | structure, boilerplate, appendices, balance (8.0% margin), case.json schema, learning-goal mutual reachability, tier-vs-load all clean |
| T1-13 | GAP | Twist is explicitly N/A with a written justification (see FACILITATOR.md); GAP is the standard "confirm the justification is written out" note, not a defect |
| T1-14 | GAP | 3 numbers in FACILITATOR.md's new P5-fragility paragraph (35.0, 85.0, 1350.0 — sensitivity-sweep results) have no home in case.md/case.json; genuine, low-severity — these are Tier 2 Probe 5 outputs, not case-of-record figures, and are reproducible directly from `sensitivity_model.py` |
| T1-15..T1-21 | PASS | published-artifact continuity, QA hash current, cohort bands declared, interactive HTML leak-free and fresh, math glossary (9 terms) and story glossary (5 terms) both present with allowlisted/real links |

BLOCKER list: none.
GAP list: T1-13 (Twist N/A confirmation — see below), T1-14 (3 orphan numbers in FACILITATOR.md, see above).
POLISH list: T1-07 (appendix-label parsing note, informational only), T1-20 (no chart/diagram — optional, not required for this short elementary case).

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent (no other file read) chose B, named the metric (supervised swim-hours per sq ft), showed correct arithmetic (45/2700 vs 63/3500), named MA2 (footprint) as the most sensitive assumption, and correctly declined to use Appendix D (CDC/ADA background) as calculation input. Reached the case's intended answer for the right reasons. |
| P2 both-sides | **PASS** | Fresh subagent built real quantitative pitches for both A (63 total hrs incl. protected team time, smaller footprint, whole-foot gauge simplicity) and B (100% of hours open, 0.018 vs 0.0167 hrs/sq ft on the case's own "general-access" definition). The agent's own framing — that A's case weakens once a peer asks "should the reserved 18 hrs count as accessible to the general user base," per Appendix A's own definition — is exactly the case's designed Deep-Conflict discussion thread (see FACILITATOR.md), not a sign the dilemma is fake: A retains a genuine non-metric argument (protecting the swim team's only practice window) that the metric alone doesn't settle, which is the point of the case. |
| P3 trap | **PASS** | Fresh subagent, reading only the student packet, independently named the "compare raw hours (45 vs 63) without dividing by footprint" shortcut as the most plausible wrong path — before reading FACILITATOR.md. FACILITATOR.md's "The trap" section names that exact shortcut (plus its mirror, the footprint-only shortcut). The guide has genuinely anticipated the trap. |
| P4 twist | **PASS (N/A confirmed)** | No twist authored; FACILITATOR.md states and justifies Twist: N/A — the case's tension is a fully disclosed trade-off that resolves through the Challenge 3 division-and-comparison itself, and the D3 rate reveal (the smaller-footprint design does not win the rate) already produces the surprise-and-recompute moment a twist would provide. No `evaluate_twist()` in `sensitivity_model.py` (not needed). Mechanical screen: READY, no MCS-15 finding (Twist heading present with justification). |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` swept all 4 stated dials (`total_weekly_hours`, `reserved_hours_a`, `footprint_a`, `footprint_b`) at ±50%. The verdict is genuinely fragile — every one of the four flips the winner or breaks the SPEC §2 20% cap under some direction of flex. All four are recorded in `case.json.sensitivity_disclosure[]` as Category X (no engineering/staffing plan exists yet for either finalist design — every dial is a documented good-faith scenario estimate, not a number this specific facility has published), each with a real, non-generic justification ≥20 characters. This is the disclosure-aware PASS state per the 2026-08-13 doctrine (disclosed, not eliminated) — FACILITATOR.md's new "This margin is genuinely fragile" paragraph states this explicitly so no guide defends 8.0% as a stable fact. |
| P6 data decay | **PASS** | All 3 cited URLs (S1 CDC, S2 U.S. Access Board, S3 R&R Swimming Pools) fetched directly and confirmed live and reachable. S2 and S3's cited figures (the 300-linear-foot ADA threshold / 1-vs-2-entry rule; the ~20–25 ft / 1:7 slope-ratio zero-entry guidance) were both confirmed verbatim on the live page. **S1's original claim ("~900 children/adolescents ages 0-19 die annually") was NOT found on the current CDC page** on direct fetch — the live page states a different figure (≈4,000 deaths/year, ~11/day, all ages, plus "leading cause of death ages 1-4" verbatim). Per SPEC §5 / MCS-21 (report NOT FOUND rather than guess), S1's claim, value, and both case.md and the interactive HTML were corrected to the figure actually confirmed live on the cited URL. Re-verified after the fix: matches exactly. No load-bearing figure was affected (S1 is background-only, never used in the D3 calculation). |
| P7 accessibility | **PASS** | Mechanical pre-screen: 0 sketch/diagram-requesting deliverables in this case (D1-D3 are reading/comparison tables, not drawings), so no missing-visual finding. Model-judged cold-read (fresh subagent, zero context, reading the published Interactive HTML's text-extracted packet with inline glosses): **first pass named 6 unexplained real-world concepts** ("zero-entry ramp," "linear feet of pool wall," the MA/S tag conventions, "Anchor 1," "excellent words") — a FAIL. Remediation: (1) STORY_GLOSSARY term keys were case/phrasing-mismatched against actual prose usage ("Lifeguard"/"Diving Well"/"City Council"/"Zero-Entry Pool" vs. the lowercase/hyphenated forms actually used in the text) — relabeled to match, restoring the probe's inline-gloss mechanism for all 4 terms; (2) added one-sentence inline clarifications for "linear feet of pool wall," and for the MA/S tag conventions, directly in Appendix C/E. **Second pass (fresh subagent, same packet, regenerated): 0 genuine real-world concept gaps** — the reader flagged only that Appendix F/story-glossary's *rendered grid content* doesn't appear in the static text extraction (a known limitation of P7's text-extraction mechanism, since the glossary grids render client-side via JS — `T1-19`/`T1-21` already validate the underlying `GLOSSARY`/`STORY_GLOSSARY` data objects directly, and a real browser-rendered page does show the grids), not an unexplained real-world term. Pass criterion (0-1 named concepts) met. |

**7/7 probes recorded by name, 0 FAIL.**

### Tier 3 — human dry-run
NOT RUN. `case.json.qa.tier3_runs` is empty. Per the ladder, `TIER2_PASS` licenses `case-publish`
but not `VERIFIED` — this case has not been assigned to a real cohort yet.

## Notes on scope

Per the assignment, this case was deliberately kept short and elementary-appropriate: 3
Challenge-3 deliverables (not the usual 4-6), a T1 tier declaration, and a FACILITATOR.md that
explicitly tells the guide not to pad the discussion out to feel like a T3/T4 case. Both new-
coverage skills (`number-sense-depth`, `number-sense-digit`) are basic vocabulary terms, and the
case forces both genuinely: D1 forces a whole-number depth reading off a digital gauge, D2 forces
a tenths-precision depth reading *and* a place-value/digit-naming task — neither skill is bolted
on as decoration.

`case-publish` was intentionally NOT run for this task. `case.json.status` remains `"qa"`, and
`readmodel/cases_index.json`, `readmodel/standards_spine.json`, and `readmodel/gap_queue.json`
were not touched.
