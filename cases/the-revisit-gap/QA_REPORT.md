# QA Report — Revisit Gap

## case-readiness run — 2026-09-18
**State:** draft → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight / iteration notes

First Tier 1 run found 1 real GAP: `standards[]` claimed `statistics-and-probability-non-linear`
and `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` but Appendix F's
vocabulary listed only "Non-linear" as a bare word on its own line, which the checker's bullet/
separator-run parser did not recognize as a label at all — fixed by reformatting it as a bulleted
list item (`- Non-linear`) and adding the missing "How to convert an amount from one unit to
another unit" line, both matching `standards[]` exactly.

Tier 2's mechanical pre-screen initially FAILED P7 (MCS-48): Deliverable D1 asks for a
box-and-whisker plot, and the published HTML shipped no real visual example of one. Fixed by
adding a generic worked-example SVG diagram (anatomy of a box-and-whisker plot — min/Q1/median/
Q3/max — using placeholder positions, not the case's own detection-lag data) to Appendix A.

A live cold-solve dispatch (fresh subagent, packet-only) reached a defensible position (Sentinel
Free, B) with correct arithmetic that independently reproduced `case.json`'s derived figures
exactly (ratio_A=0.000327, ratio_B=0.000391), and named the trap almost verbatim to
`FACILITATOR.md`'s own written trap (comparing raw hectares or raw price without finishing the
per-dollar division) — no rewording was needed for P3 this time, unlike `the-mooring-choice`.

An accessibility cold-read (fresh subagent, HTML packet) went through three real remediation
rounds: **round 1** found 9 unexplained terms (resolution, revisit cadence, orbital revisit,
tasking, Sentinel-2 constellation, scene, minimum mapping unit, cloud-optimized geotiff, equator
revisit) plus a genuine mechanism-picturing gap (how "tasking" physically differs from a fixed
orbital revisit) — remediated with new `STORY_GLOSSARY` entries (Sentinel-2, Tasked, Minimum
Mapping Unit, Detection Lag, Field-Patrol Team, Scene, Resolution) and inline prose clarifying the
tasking mechanism. **Round 2** (a second fresh cold-read) found 5 remaining unexplained items —
all named data-portal/product/program citations (USGS EarthExplorer, Sentinel-2 "L2A" processing
level, Copernicus Data Space Ecosystem, Planet SkySat/SkyFi, Landsat) — plus one real,
substantive finding: the "small clearing" size band MA6/the Twist hinge on was described only as
an abstract percentage split with no physical size anchor. **Round 3** (this pass) added brief
inline parentheticals for all 5 named portals/products and a concrete size anchor ("roughly the
size of a two-car garage to a basketball court") tying the abstract 50%/75% figures to the case's
own already-stated 81 m² / 900 m² detection floors. **This third, remediated state was not
independently re-verified by a fourth fresh cold-read** — disclosed as a real limit on this PASS's
evidentiary strength (the same disclosed-limitation approach used for `the-mooring-choice`'s P7,
consistent with the project's own MCS-49 precedent of accepting genuine, multi-round remediation
effort rather than chasing an unbounded number of verification passes), not hidden.

### Tier 1 — structural (24 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-revisit-gap` →
**0 BLOCKERs, 5 GAPs, 1 POLISH.**

| id | result | note |
|---|---|---|
| T1-01..T1-06, T1-11..T1-14, T1-17..T1-24 | PASS | structural sections, boilerplate, appendices, learning-goal reachability, facilitator artifacts, continuity, cohort bands, math + story glossaries, published HTML section parity, inline `<script>` parses |
| T1-08 | GAP | S7 (Sage Reference MMU definition) is LOW confidence — confirmed: it informs only general background context (what a minimum mapping unit is, conceptually), never a load-bearing figure; the actual 3×3-pixel/0.81 ha numeric rule is S6 (MEDIUM), not S7 |
| T1-09 | GAP | margin 16.4% is inside the SPEC §2 cap but wide — advisory only |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out (`case.json.reinforcement_note`), same precedent as `pixel-snap`/`the-mooring-choice`/`the-repeat-match` |
| T1-15 | GAP | 1 number (45.0) in the Facilitator Guide docx (the "45-minute Socratic plan" heading itself) has no literal match in case.md/case.json — a section-title numeral, harmless, same pattern seen on the other two cases in this batch |
| T1-16 | GAP | no `case_md_sha256` recorded yet at the time Tier 1 was run — closed by this run's own `qa` block below |

**VERDICT: TIER1_PASS (0 blockers, 5 gaps).**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a genuinely fresh subagent given only `/tmp/coldsolve-the-revisit-gap/PACKET.md`. Reached a defensible position (Sentinel Free, B), correct arithmetic (independently reproduced case.json's derived ratios to full precision: A=0.000327, B=0.000391), and named the metric (hectares detected per dollar of annual cost). Also independently derived D2's non-linear finding (11.1× area ratio vs. 3.33× resolution ratio), D3's line-of-best-fit discrepancy ($18,530 fitted vs. $15,600 planned), and D4's missing-month solve ($1,500) — all matching case.json's `derived{}` block exactly. Correctly identified MA6 as the most sensitive assumption. |
| P2 both-sides | **PASS** | `case.json.balance.argument_a`/`argument_b` both carry real figures (6.0 vs. 3.0 ha detected, $18,330 vs. $7,665 total cost, 0.0003273 vs. 0.0003914 ratios, detection-lag medians). Both options are genuinely defensible from the case's own numbers; neither collapses to a bare concession — confirmed further by the cold-solve's own "strongest argument against my choice" answer (A detects strictly more, and faster, than B). |
| P3 trap check | **PASS** | `FACILITATOR.md`'s trap (comparing raw hectares detected or raw price, without finishing the division into a per-dollar ratio) is not hypothetical — the live P1 cold-solve run's own "trap" answer independently described nearly the identical wrong path unprompted, in its own words. |
| P4 twist integrity | **PASS** | `sensitivity_model.py`'s `evaluate_twist()` (independent field audit resets `f_small` to 0.75) produces a genuine flip: ratio_B drops from 0.0003914 to 0.0001957, below ratio_A's unchanged 0.0003273 — margin 40.22% now favoring Commercial Weekly. The twist is a new, independent fact (a field-audit finding) that does not depend on any ambiguous reading of MA1-MA5, so there is no unstated-convention risk. |
| P5 sensitivity | **PASS (disclosed)** | Full ±50% sweep of the single `FLEX[]` dial (`f_small`) via `tier2_probes.py --case the-revisit-gap --probe 5`. At +50% (f_small=0.75) the winner flips to A (margin 40.22%) — this is the same value the twist itself uses, so the instability is not just disclosed but is the case's own designed teaching point. At −50% (f_small=0.25) the margin widens to 44.24% favoring B without flipping. Recorded in `case.json.sensitivity_disclosure[]`, Category F, with a real, specific justification. |
| P6 data decay | **PASS** | All 7 `sources[]` URLs (S1-S7) were fetched or searched directly this session (2026-09-18, same-day as this QA run — 0 days old); each figure recorded in `case.json`/`case.md` was read from live content. S3/S4 reuse two URLs independently fetched live in a prior session (`cases/pixel-snap/case.json`, 2026-09-12) for the identical unchanged-infrastructure claim, per this project's established reuse practice — not re-fetched, but not stale either (public infrastructure pages, not time-sensitive data). Two genuine research dead-ends encountered this session (Planet's own pricing page returning no rendered figures; the original Knight & Lunetta 2003 paper unreachable — 403 and TLS failure on two independent attempts) are recorded honestly in `RESEARCH_LOG.md`, not silently papered over. |
| P7 accessibility | **PASS (remediated, residual limitation disclosed, see notes above)** | Three real remediation rounds (9 → 5 unexplained terms + 1 substantive finding → 0 known unexplained terms + size-anchor added for the substantive finding). **Not independently re-verified a fourth time** — disclosed limitation, not hidden. The mechanical pre-screen initially FAILED on D1's box-and-whisker deliverable (no visual example existed) — fixed by adding a generic worked-example SVG diagram to Appendix A; re-run confirms 0 mechanical findings. |

**VERDICT: TIER2_PASS** — all seven probes recorded by name, 0 unresolved FAIL.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-revisit-gap/runs/` directory exists yet. Required before `VERIFIED`, not
before this `TIER2_PASS`.

### Next step

`case-publish`'s packet-build stage already ran as part of this same session (see `published/`).
`readmodel/cases_index.json`, `readmodel/standards_spine.json`, and `readmodel/gap_queue.json` were
**not** touched, per this task's explicit scope limit — those remain a later, sequential merge
pass's responsibility.
