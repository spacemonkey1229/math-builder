# QA_REPORT.md — Casino Owner

## case-readiness run — 2026-08-17
**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS

### Tier 1 — structural (19 checks)

Command: `python3 skills/case-readiness/scripts/tier1_structural.py --case casino-owner`

Result: **17 PASS · 2 GAP · 0 BLOCKER** — `VERDICT: TIER1_PASS`

| id | result | note |
|---|---|---|
| T1-01 | PASS | all seven structural sections present |
| T1-02 | PASS | Overview length in range, no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Emilia Carlon." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | appendices lettered A–F, ordered, no orphans (Appendix E now cross-referenced from Background) |
| T1-07 | PASS | final appendix labels match standards[] exactly (mechanically regenerated) |
| T1-08 | PASS | every figure cited or a declared Modeling Assumption; legacy_conversion_note reworded to avoid an unbacked "verbatim"/real-world-claim trigger it did not actually intend |
| T1-09 | GAP | margin 17.31% is inside SPEC §2's 20% cap but wide — disclosed honestly (case.json.balance.stability), not narrowed by inventing data |
| T1-10 | GAP | new_coverage[] empty — legacy-conversion carve-out applies (case.json.new_coverage_note documents the n==0 spine check) |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | tier T3 matches numeric load (weighted averages, odds-to-probability, multi-block rate stacking, a stated assumption) |
| T1-13 | PASS | FACILITATOR.md has the full 11-anchor ladder, 5 Socratic questions (one per line), a named trap, a Twist section with soundness check, and a 7-row timed 45-minute plan naming the twist drop |
| T1-14 | PASS | every number in FACILITATOR.md's balance/twist prose resolves to case.json.derived or case.json.balance |
| T1-15 | PASS | published artifact built after case.md/FACILITATOR.md's last edit |
| T1-16 | PASS | case_md_sha256 current |
| T1-17 | PASS | cohort_bands[] declared, 3 bands |
| T1-18 | PASS | interactive HTML present, fresh, no balance/margin literal leaked outside `<script>` |
| T1-19 | PASS | 8 glossary terms with real, fetched, allowlisted (khanacademy.org / mathsisfun.com) URLs |

BLOCKER list: **none.**

GAP list:
- T1-09 — margin 17.31% inside cap but wide (disclosed in `case.json.balance.stability`, `sensitivity_model.py`, and FACILITATOR.md's Sensitivity note).
- T1-10 — `new_coverage[]` empty (legacy-conversion carve-out; see `case.json.new_coverage_note`).

POLISH: T1-07 parsed 18 labels via the separator-run half of the check (7 of them), confirming the fix that catches labels the legacy script used to skip.

### Tier 2 — simulated play (6 probes)

**NOT RUN.** This conversion pass completed Tier 1 only. Next step:
`python3 skills/case-readiness/scripts/tier2_probes.py --case casino-owner`, dispatching a fresh
cold-solve subagent for P1 and a web-connected subagent for P6 (this case has an empty `sources[]`
by design — a fully fictional dataset per `legacy_conversion_note` — so P6's fetch worklist is
empty and that probe should report accordingly, not NOT RUN). P5 (assumption sensitivity) can run
immediately against `sensitivity_model.py`; a preliminary hand-check (see FACILITATOR.md's
Sensitivity note) already shows `peak_hours_per_day` at +50% breaks the SPEC §2 cap and
`indigo_tables_staffed` at -50% flips the winner (this is the Twist itself, so an expected,
disclosed finding, not a surprise).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | — |
| P2 both-sides | NOT RUN | — |
| P3 trap | NOT RUN | — |
| P4 twist | NOT RUN | — |
| P5 sensitivity | NOT RUN | preliminary hand-check only (see above) — needs the actual script run for a recorded verdict |
| P6 data decay | NOT RUN | `sources[]` is intentionally empty (fully fictional dataset); worklist is empty |

### Tier 3 — human dry-run

NOT RUN.

## Next step

Run Tier 2 (`tier2_probes.py`) before this case may reach `TIER2_PASS`/publish-eligible. This
conversion is `TIER1_PASS`, not yet `PUBLISHED`.

## Gate re-run — 2026-08-17 (post-conversion verification)

Command: `python3 skills/case-readiness/scripts/tier1_structural.py --case casino-owner`

Result: **17 PASS · 2 GAP · 0 BLOCKER** — `VERDICT: TIER1_PASS`, 1 iteration, no fixes required.

GAPs matched the self-report exactly:
- T1-09 — margin 17.31% inside the 20% cap but wide.
- T1-10 — `new_coverage[]` empty under the legacy-conversion carve-out.

No BLOCKERs were present, so the T1-10-BLOCKER re-check-against-live-spine contingency did not
apply. Case remains `TIER1_PASS`; Tier 2/3 still not run (see above).

## case-readiness run — 2026-08-17 (Tier 2 gate)

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — re-confirmed clean

`python3 skills/case-readiness/scripts/tier1_structural.py --case casino-owner` — **17 PASS · 2
GAP · 0 BLOCKER**, identical to the prior run (T1-09 margin-width GAP, T1-10 legacy-carve-out
GAP). No regression.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh subagent solve, packet-only, no FACILITATOR.md/case.json access. Chose **A (Indigo)**, correctly named the metric ("Projected weekly profit (D4)... net of staffing cost, under MA1–MA3"), and produced the full D1→D5 route with the right structure (weighted-average rake/length by tier, games/hr, odds→probability conversion for D3, hours-stacked D4 build-up, D5 comparison). Reached the case's intended winner and margin direction. **One minor arithmetic slip found on independent re-check**: the solver's 6–7-player-tier weighted-average rake came out $212.01/game vs. the correct $211.01/game (case.json.derived.indigo_tier_6_7_avg_rake_per_game) — re-derived by hand from Appendix A's 6–7-player table (`0.078·24.60 + 0.215·48.75 + 0.373·126.00 + 0.204·307.50 + 0.072·543.75 + 0.058·857.50 = 211.01`), confirming the case's own figure is right and the solver's is a ~$1 slip. Propagated forward this shifts the solver's final Indigo weekly profit by ~0.4% ($191,171 vs. the correct $190,472.64) — it does not change the tier's games/hr, does not change D2's per-hour figure direction, and does not come close to moving the 17.31% margin or flipping the winner. Scored PASS: the route is correct, the metric is correctly named, arithmetic is correct everywhere else verified, and this single small slip has no effect on the defensibility of the chosen position — but it is worth a facilitator's eye if this exact solve is ever reused as a worked-answer key. |
| P2 both-sides | PASS | Machine pre-screen: both `case.json.balance.argument_a`/`argument_b` and FACILITATOR.md's "Argument for A/B" contain real numbers (rake $137.76–$211.01/game, 2.59–3.99 games/hr per table for A; 200+ plays/hr/machine, 2 fixed security staff vs. 1 dealer/table for B) — neither is a numberless or concessive argument. Independently built the strongest case for each side from case.md alone: **A's best sentence** — "a single Indigo table's per-hour dollar rate ($525–$601, D2) is roughly 5–6x a video machine's, so a 4-to-25 unit disadvantage doesn't decide the case on its own." **B's best sentence** — "video machines scale to 25 simultaneous units against a hard 4-table cap, at a flat $15/hr total security cost regardless of headcount, versus a dealer wage that scales linearly with every table Indigo adds." Neither side collapses on inspection — both survive to the point where D4's actual hours-stacked arithmetic has to be run, and only then does A pull ahead by 17.31%, a real (not paper) margin consistent with `case.json.balance.margin_pct`. |
| P3 trap | PASS | Mechanical pre-screen in `tier2_probes.py` reported FAIL, but this is a script extraction bug, not a case defect: the regex `(the )?trap[^.\n]*[:.\n](.{0,400})` matches the *first* occurrence of the word "trap" in FACILITATOR.md, which is an incidental mention at line 131 ("...confusing the two is the case's other named trap.") — the captured 400 chars then land in the unrelated "## Standards Touched On" section below it, not the real "## The trap" heading at line 150. Read directly: FACILITATOR.md's actual "## The trap" section names exactly the wrong path a hurried student would take — reasoning from unit count ("25 machines will obviously out-earn 4 tables") instead of dollars-per-unit — and names the mirror-image trap too (assuming Indigo wins on pot size alone without computing D3). Independently naming the trap from case.md alone (25 machines vs. 4 tables, no dealer needed for machines) reaches the same unit-count-vs-per-unit-dollars trap the guide names. Scored PASS on the actual content; the mechanical FAIL is a known extraction-order bug in the probe script (worth fixing: anchor the regex to the `## The trap` heading specifically, not the first case-insensitive occurrence of the word). |
| P4 twist | PASS | (1) The twist invalidates the Anchor-1 "pitch Indigo" position a real room would hold under the base numbers — flipping the recommendation to B once only 2 of 4 tables are staffed. (2) Re-derived under every stated reading of Appendix E: under a *sequential* reading (MA1→MA2→MA3 in order) MA3 only speaks to units **built** ("full stated maximum build-out"), never to units **staffed**, so the Twist's `indigo_tables_staffed=2` does not contradict it. Under a *simultaneous* reading (all three assumptions applied at once) the same gap holds — nothing in MA1–MA3 asserts a staffing level, so the base case's implicit `indigo_tables_staffed=4` is itself an unstated assumption the Twist is entitled to correct. FACILITATOR.md's own "Soundness check" subsection already runs this exact adversarial check. Mechanically confirmed via `sensitivity_model.py`: `evaluate(PARAMS)` → A wins by 17.3%; `evaluate_twist(PARAMS)` → B wins by 70.5% — winner AND margin both move, not a same-direction magnitude shift. |
| P5 sensitivity | PASS (disclosed) | `python3 skills/case-readiness/scripts/tier2_probes.py --case casino-owner --probe 5 --flex 0.5`. Mechanical result: `peak_hours_per_day` +50% keeps A winning but pushes margin to 31.7% (breaks the 20% cap); `indigo_tables_staffed` −50% flips the winner to B at margin 70.5% (breaks the cap in the other direction) — this is exactly the case's own Twist scenario, not a hidden instability. Checked both dials are genuine Appendix E modeling assumptions, not cited/given data (no FLEX-scoping bug: `dealer_wage_per_hr`, `security_wage_per_hr`, `security_staff_count`, and the pot/bet tables are correctly excluded from `FLEX[]`). Both instabilities were already narratively disclosed in FACILITATOR.md's Sensitivity note and `case.json.balance.stability`, but `case.json.sensitivity_disclosure[]` (the structured, machine-checked form) was missing — added two entries (`peak_hours_per_day`, `indigo_tables_staffed`, both category **F**: the true value is a future operating/staffing decision that does not exist yet and cannot be researched in advance, per Appendix A's own "no current Indigo dealers" statement and the room having no operating history) with 20+ character justifications. Re-run after the edit: `PASS (disclosed)`. |
| P6 data decay | PASS | `case.json.sources[]` is empty by design — `legacy_conversion_note` documents every number in Appendix A–D as the legacy authors' own invented, internally self-consistent fictional dataset (Indigo, The Landmark, and all named people are fictional), not a real-world claim requiring external sourcing; T1-08 already enforces that an unbacked "verbatim"/"publicly verifiable" real-data claim would be a BLOCKER, and this case makes no such claim. Fetch worklist is therefore empty — nothing to check for reachability, drift, or staleness. Vacuously clean, scored PASS rather than NOT RUN per the same logic already recorded in this file's prior Tier 2 planning note. |

### Tier 3 — human dry-run

NOT RUN (not required for TIER2_PASS; blocking only for VERIFIED).

### Verdict

All six Tier 2 probes: **PASS** (P5: PASS, disclosed). Tier 1 re-confirmed clean, 0 BLOCKERs.
**State: TIER2_PASS.** `case-publish` may now run.
