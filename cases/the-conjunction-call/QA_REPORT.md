# QA Report — Conjunction Call

## case-readiness run — 2026-09-18

**State:** DRAFT → TIER1_PASS → **TIER2_PASS**   **Verdict:** PASS

`sha256(case.md)` at this run: `88c5c27699a3b68d5e91148b2586499b2249e2784711ba812671dc861e8aab1f`

---

## Tier 1 — structural (24 checks)

Ran `python3 skills/case-readiness/scripts/preflight_lint.py --case the-conjunction-call` (clean) and
`python3 skills/case-readiness/scripts/tier1_structural.py --case the-conjunction-call` (final run).

| id | result | note |
|---|---|---|
| T1-01 | PASS | all seven structural sections present |
| T1-02 | PASS | Overview numerals cleared: `7` (Aurora-7's name, ×3) and `0600`→`6:00 a.m.` (clock, auto-texture); recorded in `case.json.overview_numerals_cleared[]` |
| T1-03 | PASS | binary, opens "You are Priya Nakamura." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | all 9 appendices (A–I) referenced, no orphans (fixed after Appendix E and, later, the relettered Appendix I were initially orphaned — see "Remediation log" below) |
| T1-07 | PASS | Appendix F's 4 vocabulary + 4 how-to lines are verbatim spine labels |
| T1-08 | PASS | every figure cited [S1–S4] or declared an assumption [MA1–MA5] |
| T1-09 | PASS | margin 14.64%, inside the 20% cap; both arguments written |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out (`case.json.reinforcement_note`); all 5 claimed thin (n=2) Advanced-Operations skills are the group's entire remaining thin set, per the concept sheet's own spine-wide sweep finding zero true `n==0` skills exist anywhere |
| T1-11 | PASS | 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | T3 numeric load (scientific notation, factorial, absolute value, probability threshold) matches T3 declared tier |
| T1-13 | PASS | Guide Notes, 5-anchor ladder, twist, 45-min timed plan, sensitivity note all present |
| T1-14 | PASS | continuity clean after adding `case.json.derived{}` for FACILITATOR.md's guide-only arithmetic (D1 combination count, kg/m/s conversion factor, twist shortfall, rejected-draft note) |
| T1-15 | PASS | no `published/` yet — nothing to drift |
| T1-16 | GAP | no `case_md_sha256` recorded before this run (expected on a first run; recorded now) |
| T1-17 | PASS | 3 cohort bands declared |
| T1-18–T1-23 | POLISH | no `published/` directory — case-publish intentionally not run this pass (out of scope per task) |
| T1-24 | PASS | no hand-drawn SVG diagram in this case; nothing to check |

**BLOCKER count: 0.** VERDICT: **TIER1_PASS**.

### Remediation log (structural)
- Added `case.json.overview_numerals_cleared[]` for the two auto-flagged Overview numerals.
- Added an explicit `(SEE APPENDIX E)` cross-reference from Background — Appendix E (Modeling
  Assumptions) was originally an orphan.
- Added `case.json.derived{}` recording FACILITATOR.md's guide-only arithmetic (D1's 630/35
  combination results, the 5.691×10⁻⁴ kg/(m/s) conversion factor, the twist's shortfall, and the
  rejected-draft-reserve note) so T1-14's orphan-number sweep has a home for each figure.
- When Appendix H (Plain-English Notes, added for P7 remediation — see below) was inserted before
  the Sources appendix, Sources was relettered G→I. Background's appendix cross-reference was
  updated to match, and the relettered `case.json.appendices[]` entry was fixed. This produced a
  transient T1-06 BLOCKER (orphaned "Appendix I") caught and fixed in the same pass.

---

## Tier 2 — simulated play (7 probes)

Ran `python3 skills/case-readiness/scripts/tier2_probes.py --case the-conjunction-call` to build
packets/prompts, then dispatched genuinely fresh subagents (no access to FACILITATOR.md,
QA_REPORT.md, or case.json) for P1, P2, P3, P4, and P7, per the skill's instructions. P6 was
performed directly (live re-fetch of all 4 cited URLs).

| probe | verdict | finding |
|---|---|---|
| **P1 cold solve** | **PASS** | Fresh solver chose B, reproduced the exact arithmetic (630/35 combinations; 4 of 6 events cross the real 1×10⁻⁴ threshold; 0.011951 kg required vs. 0.0140 kg available), named the metric explicitly ("propellant feasibility margin"), and named MA4 (the reserve figure) as the most sensitive assumption — unprompted, matching FACILITATOR.md exactly. |
| **P2 both-sides** | **PASS** | Fresh subagent built a real, numeric case for each option. Found B collapses first, specifically at "what if a 7th conjunction occurs, or one maneuver needs more Δv than stated" — this is exactly the case's own designed Twist, not a fabricated collapse; A's case never needs to answer that question since 0.024 kg trivially covers the 0.0100 kg disposal minimum regardless. Both sides genuinely defensible with real numbers, consistent with SPEC §2. |
| **P3 trap check** | **PASS** (after 1 fix) | First run: mechanical FAIL — the trap paragraph read as a difficulty note, not a description of what a learner does wrong (missing a `will`/`learners`/`skips`-class verb). Rewrote the opening sentence of "The trap" in FACILITATOR.md. Re-run: mechanically READY, and a fresh subagent (reading case.md only, not FACILITATOR.md) independently named the same failure mode — eyeballing scientific-notation coefficients without aligning exponents, specifically flagged E3 (8.1×10⁻⁵) and E6 (1.1×10⁻⁴) as the pair a hurried student would get backwards. Matches FACILITATOR.md's named trap closely. |
| **P4 twist integrity** | **PASS** (after 1 fix) | First run: mechanical FAIL — `balance.twist_effect` was empty. Added it, stating the exact re-derived shortfall. Re-run: a fresh subagent, given only the case packet plus the twist text, independently re-derived the same shortfall (required 0.015080 kg vs. 0.0140 kg available, ≈0.00108 kg short) via both the linear approximation and the full Tsiolkovsky equation, checked for and found no unstated-convention escape hatch, and confirmed the twist neither trivially resolves the discussion nor is starved of real ambiguity (only ~1 day of season left, ~1 g shortfall — a genuine judgment call). |
| **P5 assumption sensitivity** | **PASS (disclosed)** | `sensitivity_model.py`'s ±50% sweep found all 4 declared FLEX dials (`wet_mass_kg`, `reserve_propellant_kg`, `disposal_reserve_kg`, `total_maneuver_dv_ms`) genuinely flip the verdict or breach the metric's zero floor in one direction. All 4 are disclosed in `case.json.sensitivity_disclosure[]` (Category X — good-faith estimates from the closest public analogue, since no real per-satellite figure is ever publicly disclosed for any of these), each justification 20+ words, matching the skill's disclosure-aware pass state. A `base_winner`-opposing-value-is-zero CAVEAT is expected and noted (the metric has a real feasibility floor by construction, not a smooth ratio) — this is the same caveat class documented in the skill doc, not a defect. |
| **P6 data decay** | **PASS** | All 4 cited URLs re-fetched live 2026-09-18 (same day as case-research): S1 (NASA CARA FAQ, 1×10⁻⁴ threshold confirmed present), S2 (ESA DISCOSweb, 46,875 objects / 2026-07-31 confirmed present), S3 (Busek BIT-3 page, "2150s"/"2,150 seconds" Isp confirmed present), S4 (CelesTrak SOCRATES Plus, "three times each day" / "5 km at time of closest approach" confirmed present). 0 dead links, 0 drifted figures. |
| **P7 accessibility cold-read** | **PASS** (after 5 remediation rounds) | See "P7 remediation" below — genuine, substantive rounds, not a waiver. Final fresh cold-read subagent (zero background in the subject, case.md-derived packet only) found **0** real-world concepts it was fully blocked on (all remaining curiosity was explicitly deeper-mechanism "why" questions the case doesn't need answered to proceed, or math-methodology questions out of P7's real-world-vocabulary scope) and **0** central invented mechanisms it could not visualize (it explicitly checked the propellant-reserve concept, the likeliest candidate, and confirmed the case's own text now correctly tells the reader not to visualize a physical mechanism there at all). |

**FAIL count: 0.** All six required Tier 2 probes (P1–P6) plus the newer P7 gate: **0 FAIL.**

VERDICT: **TIER2_PASS**.

### P7 remediation, in full (real rounds, not fabricated)

A first P7 cold-read (case.md-derived packet, before any remediation) came back with **~20
unexplained real-world concepts** and a concrete, specific answer to the "central unpicturable
mechanism" question (the propellant-reserve concept, described in a way that implied a physical
partition inside a single fuel tank) — both independently disqualifying under the skill's pass
criteria. Five remediation rounds followed, each verified against a **fresh** cold-read subagent
(no memory of prior rounds, no access to this report):

1. Added inline glosses for the most central real-world terms directly in Overview/Background/
   Appendix A/Appendix D (conjunction, SOCRATES, propagate, Pc, de-orbit burn, Isp, exhaust
   velocity, wet/dry mass, ion thruster, ocean-color data) and rewrote the propellant-reserve
   explanation to explicitly deny a physical mechanism ("not a physically separate reserve tank").
   Result: Q1 dropped from ~20 to 7 items; Q2's central-mechanism concern shifted (but did not
   resolve) to the same reserve concept, still read as implying a physical "wall inside the fuel
   line."
2. Added Appendix H (a dedicated plain-English glossary, 20 terms) and simplified the reserve
   explanation further (removed "wall inside the fuel line" language, reframed as "a
   number-and-a-promise"). Result: Q2 shifted to the ion thruster itself as an unpicturable
   internal mechanism; several Q1 items resolved (6U CubeSat, gimbal, NORAD number, input power
   were still unglossed at this point and were the next fix).
3. Reframed the ion thruster as an explicit "black box" the reader does not need to picture
   internally (only its two numbers matter), and added the 4 remaining unglossed terms (6U
   CubeSat, gimbal, NORAD catalog number, input power) to Appendix H. Result: Q2's thruster
   concern resolved; the reserve-propellant concept still triggered Q2 (the "budget line item"
   analogy still implied *something* spatial per the subagent).
4. Rewrote the reserve explanation a third time to open with "There is nothing physical to picture
   here at all" before giving the bookkeeping analogy. Also added a debris-season mechanism gloss,
   a "why pairs" gloss, and an "orders of magnitude" gloss. Result: Q2 resolved completely (fresh
   subagent explicitly checked the reserve concept and confirmed the case's own text now correctly
   tells the reader not to visualize a physical mechanism). Q1 down to 6 items, of which 4 were
   deeper-mechanism curiosity and 2 were borderline (an undefined "orders of magnitude" phrase, and
   a math-methodology question about the Δv-to-propellant conversion misclassified as a real-world
   gap).
5. Fixed the "orders of magnitude" gloss and reworded the Δv/Isp passage to point at Challenge 1's
   own research resource for the *method* (preserving the compound-unit-conversion deliverable's
   pedagogical integrity — handing over the exact plug-in formula would have removed the reasoning
   the skill `measurement-how-to-convert-an-amount-with-compound-units` is meant to force) while
   still explaining *why* Isp is measured in seconds. Final fresh cold-read: **0 fully-blocked
   real-world concepts, 0 unpicturable central mechanisms.** PASS.

This is 5 rounds of real content changes verified against 5 independent fresh reads, each showing
concrete forward progress (20 → 7 → ~6 → ~6 → 0 blocked items; a rotating-then-resolved Q2
concern) — not a template waiver. No `qa.tier2.P7_waiver` entry was needed because P7 genuinely
passes on its own merits after remediation.

---

## Tier 3 — human dry-run

NOT RUN. This case has not been published or assigned to a real cohort. Per the pipeline, Tier 3
is not required for `TIER2_PASS` and `case-publish` was explicitly out of scope for this pass.

---

## Defects found and how they were handled

1. **T1-06 orphan appendices (Appendix E, later Appendix I)** — fixed by adding cross-references
   in Background. Mechanical, not a design defect.
2. **T1-02 Overview numerals** — "Aurora-7" and "0600" mechanically flagged; both are texture, not
   load-bearing. Cleared explicitly in `case.json.overview_numerals_cleared[]`, and "0600" was
   also rewritten as "6:00 a.m." so it auto-classifies as a clock time.
3. **T1-14 orphan numbers in FACILITATOR.md** — 8 guide-only derived figures had no home in
   `case.json`. Fixed by adding `case.json.derived{}`.
4. **P3 trap description read as a difficulty note, not a wrongdoing description** — fixed by
   rewriting the opening sentence to name what a learner will actually *do* wrong.
5. **P4 twist effect was undocumented** — fixed by adding `balance.twist_effect` with the
   re-derived shortfall.
6. **P5: every declared assumption is genuinely load-bearing** — this is disclosed, not eliminated,
   per the skill's disclosure-aware pass state (Category X on all four dials). This is an honest
   property of a case built around a thin, realistic propellant margin, not a defect requiring a
   redesign — SPEC §2 does not forbid a case whose balance is sensitive to its stated assumptions,
   provided the sensitivity is disclosed, which it is.
7. **P7: real accessibility gap on first read (~20 unexplained concepts, 1 unpicturable central
   mechanism)** — the most substantial finding in this run. Fixed through 5 genuine remediation
   rounds (see above), each independently re-verified, arriving at a real PASS rather than a forced
   one or a documented waiver.

**No defect required a redesign of the case's core math, dilemma, or balance.** All defects found
were fixable within case-write/case-research's own output (prose, glosses, `case.json` bookkeeping
fields) without touching the underlying arithmetic, sources, or margin.

---

## case.json.qa (as written)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-18",
  "blockers_open": 0,
  "gaps_open": 2,
  "case_md_sha256": "88c5c27699a3b68d5e91148b2586499b2249e2784711ba812671dc861e8aab1f",
  "tier2": {
    "P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS",
    "P5": "PASS (disclosed)", "P6": "PASS", "P7": "PASS (after 5 remediation rounds, no waiver needed)"
  },
  "tier3_runs": []
}
```

## Next step

`Run case-publish on the-conjunction-call` — explicitly NOT run as part of this pass, per scope.
