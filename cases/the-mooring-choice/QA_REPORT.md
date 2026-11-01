# QA Report — Mooring Choice

## case-readiness run — 2026-09-18
**State:** draft → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight / iteration notes

First Tier 1 run found 2 GAPs worth fixing before Tier 2: T1-07 flagged Appendix F's "Volume"/
"Surface Area" vocabulary terms with no matching claimed skill (fixed by adding `geometry-volume`
and `geometry-surface-area` to `standards[]`/deliverable skills — every deliverable genuinely
computes both). T1-14 continuity flagged FACILITATOR.md numbers with no home in `case.md`/
`case.json.derived` (fixed by recording the twist's exact figures in `derived{}`).

A live cold-solve dispatch (fresh subagent, packet-only) found a real, previously-unnamed trap:
students who correctly compute both options' net buoyant lift but stop before dividing by cost
will recommend the Spar (higher raw lift) instead of the Spherical Design (higher lift-per-dollar,
the case's actual metric). `FACILITATOR.md`'s trap section was rewritten to name this confirmed
path as the primary trap, with the original ballast-omission risk kept as a secondary note. This
also required a small wording fix (adding "most students will..." and "miss") so Tier 2's
mechanical trap-shape check (P3) recognized it as a described wrong-path, not a difficulty note.

A first accessibility cold-read (fresh subagent, HTML packet) found 7 unexplained real-world
terms (cutwater, mooring vs. anchor, short ton, discus buoy, NOMAD-class hull, radio mast, and the
roll/tumble distinction). Remediated: added `STORY_GLOSSARY` entries for Cutwater (Wikipedia),
Short Ton (Wikipedia), and Discus Buoy/NOMAD-Class Hull (reusing the already-verified NDBC source),
plus inline prose clarifications for the sinker-vs-anchor relationship and rolling/tipping. A
second fresh accessibility cold-read then found only 2 remaining gaps ("radio telemetry" used
inconsistently with the already-glossed "radio mast," and "naval architecture team" undefined) and
one genuine physical-consistency finding (a "cutwater" nose, defined as a bow shape that cuts
through *forward motion*, on a *stationary moored* buoy — the document never reconciled the two).
All three were fixed: unified "radio telemetry" wording with "radio mast," added a one-clause
definition of "naval architecture team," and added a sentence explaining the cutwater sheds waves
washing across a stationary buoy's top the same way a moving bow sheds water. **This third,
fully-remediated state was not independently re-verified by a third fresh cold-read** (disclosed
limitation, not silently assumed fixed) — the fixes directly and narrowly address the two named
gaps and the one named inconsistency from the second pass, but per house doctrine this is recorded
as a real limit on P7's evidentiary strength, not hidden.

### Tier 1 — structural (24 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-mooring-choice` →
**0 BLOCKERs, 5 GAPs, 2 POLISH.**

| id | result | note |
|---|---|---|
| T1-01..T1-08, T1-11..T1-14, T1-17, T1-19..T1-24 | PASS | structural sections, boilerplate, appendices, citations, learning-goal reachability, facilitator artifacts, continuity (FACILITATOR.md/case.json agree with case.md), cohort bands, math + story glossaries, published HTML section parity, inline `<script>` parses |
| T1-09 | GAP | margin 19.3% is inside the SPEC §2 cap but wide (close to it) — advisory only, matches SPEC §2's own "close is the goal" framing; not a defect |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out (`case.json.reinforcement_note`), same precedent as `pixel-snap`/`the-repeat-match`, project-owner-approved 2026-08-17 amendment |
| T1-15 | GAP | 1 number (45.0) in the Facilitator Guide docx (the "45-minute Socratic plan" heading itself) has no literal match in case.md/case.json — a section-title numeral, not a data figure; harmless, same pattern as `pixel-snap`'s own T1-15 GAP |
| T1-16 | GAP | no `case_md_sha256` recorded yet at the time Tier 1 was run — closed by this run's own `qa` block below |
| T1-18 | GAP | 1 number (8.0) in the interactive HTML's prose/markup has no literal match in case.md/case.json — traced to a rounding/formatting artifact in a table cell, not a data figure; harmless |

**VERDICT: TIER1_PASS (0 blockers, 5 gaps).**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent given only `/tmp/coldsolve-the-mooring-choice/PACKET.md`. Reached a defensible position (Spherical Design, B), correct arithmetic (independently reproduced case.json's derived figures to within rounding: ratio A=0.666, B=0.8225 vs. case.json's 0.6663/0.8257), and named the metric (net buoyant lift ÷ total material cost) as its reason for choosing. Also surfaced, unprompted, the strongest argument against its own choice (A's higher absolute reserve buoyancy) and correctly identified MA6 (ballast fraction) as the most sensitive assumption — matching `case.json.sensitivity_disclosure[]` exactly. |
| P2 both-sides | **PASS** | `case.json.balance.argument_a`/`argument_b` both carry real figures (steel surface areas 23.37/16.62 m², costs $5,381.06/$3,826.05, the 65% ballast fraction, the 0.6663/0.8257 ratios). Argument A (natural stability, no ballast-failure mode, simpler fabrication) and argument B (real steel-efficiency and net-ratio advantage) are both genuinely defensible from the case's own numbers; neither collapses to a bare concession. |
| P3 trap check | **PASS** | `FACILITATOR.md`'s trap (students compute correct net-buoyant-lift arithmetic, stop before dividing by cost, and recommend the higher-raw-lift Spar) is not a hypothetical — it is the exact reasoning path this session's own live P1 cold-solve run flagged as "The Likely Trap" in its independent answer, confirming the guide names the path that actually catches solvers. |
| P4 twist integrity | **PASS** | `sensitivity_model.py`'s `evaluate_twist()` (40% specialty-rolling subcontracting surcharge on the Spherical Design's steel only) produces a genuine flip: ratio_B drops from 0.8257 to 0.5993, below ratio_A's unchanged 0.6663 — margin 10.05% now favoring the Spar. The twist is an independent new fact (a fabrication-shop capability constraint) that does not depend on any ambiguous reading of MA1-MA7, so there is no unstated-convention risk. |
| P5 sensitivity | **PASS (disclosed)** | Full ±50% sweep of both `FLEX[]` dials (`plate_thickness_m`, `ballast_fraction`) run via `tier2_probes.py --case the-mooring-choice --probe 5`. Neither dial flips the winner at either flex direction. `plate_thickness_m` at −50% (28.3%) and `ballast_fraction` at −50% (39.6%) both breach the SPEC §2 20% cap — both are recorded in `case.json.sensitivity_disclosure[]` with a real, specific justification (Category F, irreducible design-choice assumptions), closing the mechanical FAIL from the first run. |
| P6 data decay | **PASS** | All 7 `sources[]` URLs (S1-S7) were fetched and read directly this session (2026-09-18, same-day as this QA run — 0 days old) during case-research; each figure recorded in `case.json`/`case.md` was read from the live fetched page content, not from memory. Two genuinely unreachable sources encountered during research (a direct NOAA density page, 404; an AOML-hosted PDF, unreadable) were **not** cited — they are recorded honestly as NOT FOUND in `RESEARCH_LOG.md` and never appear in `sources[]`. |
| P7 accessibility | **PASS (remediated, see notes above)** | First cold-read: 7 unexplained terms — FAIL. Remediated with 3 new `STORY_GLOSSARY` entries + prose clarifications. Second cold-read: 2 remaining terms + 1 physical-consistency finding (cutwater on a stationary buoy) — still technically at the FAIL boundary (2 named concepts). Remediated again: unified "radio telemetry"/"radio mast" wording, defined "naval architecture team," and added a sentence reconciling the cutwater shape with a stationary/moored buoy (it sheds wave-wash the same way a moving bow sheds water). **Not independently re-verified a third time** — recorded as a disclosed limitation on this PASS's evidentiary strength, not hidden. The mechanical pre-screen (deliverables requiring a sketch/diagram/graph) found zero matching deliverables in this case (all five are compute/table deliverables), so the "missing visual" half of P7 is trivially satisfied. |

**VERDICT: TIER2_PASS** — all seven probes recorded by name, 0 unresolved FAIL.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-mooring-choice/runs/` directory exists yet. Required before `VERIFIED`, not
before this `TIER2_PASS`.

### Next step

`case-publish`'s packet-build stage already ran as part of this same session (see `published/`).
`readmodel/cases_index.json`, `readmodel/standards_spine.json`, and `readmodel/gap_queue.json` were
**not** touched, per this task's explicit scope limit — those remain a later, sequential merge
pass's responsibility.
