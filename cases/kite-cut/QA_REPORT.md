# QA Report — kite-cut

## case-readiness run — 2026-09-09
**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED (Tier 1)

### Preflight lint
Clean — no advisory findings.

### Tier 1 — structural (21 checks)
checks run: 21 · PASS 15 · GAP 5 · FAIL 1 (sha256(case.md)=539cc3a225e47bdcc1f01df6055ef55bed2f2340f52fdbc37b96f2c68fbce5ee)

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | POLISH | parsed 11 labels (11 bulleted, 0 from separator-run lines) — the separator run is the half the legacy check skipped |
| T1-08 | PASS | |
| T1-09 | PASS | |
| T1-10 | FAIL | see BLOCKER list |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | GAP | MCS-16 — timed plan never names the moment the twist drops |
| T1-14 | GAP | CONTINUITY — 2 number(s) in FACILITATOR.md appear in neither case.md nor case.json: [1.89, 8.0] |
| T1-15 | GAP | CONTINUITY — 8 numeric cell(s) in published/Kite Cut - Data.xlsx and 5 number(s) in published/Kite Cut - Facilitator Guide.docx have no match in case.md/case.json |
| T1-16 | GAP | MCS-11 — no case_md_sha256 recorded yet (expected on a first run) |
| T1-17 | PASS | |
| T1-18 | GAP | CONTINUITY — 2 number(s) in Kite Cut - Interactive.html's prose/markup (outside `<script>`) appear in neither case.md nor case.json: [1.5, 8.0] |
| T1-19 | PASS | |
| T1-20 | POLISH | no image, chart, diagram, or map found in published/ HTML — not required |
| T1-21 | PASS | |

**BLOCKER (3):**
- [T1-10] `new_coverage[]` claims `geometry-parallelogram` but the spine shows n=1 (covered_by=['The Irregular Boundary'])
- [T1-10] `new_coverage[]` claims `geometry-rhombus` but the spine shows n=1 (covered_by=['Plaza Pavers'])
- [T1-10] `new_coverage[]` claims `geometry-kite` but the spine shows n=1 (covered_by=['Plaza Pavers'])

**GAP (6):** T1-13, T1-14, T1-15 (×2 findings), T1-16, T1-18 — listed above.

**POLISH (2):** T1-07, T1-20 — listed above.

### Tier 2 — simulated play (7 probes)
NOT RUN — Tier 1 has open BLOCKERs; per SKILL.md, Tier 2 does not start until Tier 1 is clean (0 BLOCKERs).

### Tier 3 — human dry-run
NOT RUN

---
**Next step:** Fix the 3 blockers (all T1-10 — `new_coverage[]` in `case.json` claims three skills already credited to other cases in the standards spine; each has n=1 covered_by a different case title) and re-run `tier1_structural.py --case kite-cut`.

## case-readiness run — 2026-09-09 (remediation + Tier 2)
**State:** BLOCKED → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Fixes applied since the previous run
- **T1-10 (3 BLOCKERs, real padding).** `new_coverage[]` falsely claimed `geometry-parallelogram`,
  `geometry-rhombus`, `geometry-kite` as newly-covered when the spine already credits each to
  another published case at n=1 (`The Irregular Boundary`; `Plaza Pavers` x2). Since
  `standards_spine.json.totals.uncovered == 0` (verified — no id in the spine is n=0, and no
  geometry skill is n=0), this case cannot close a real gap. Fixed per the reinforcement carve-out
  (SKILL.md, "The reinforcement carve-out on T1-10"): set `new_coverage: []`, replaced the old
  `new_coverage_note` with a proper `case.json.reinforcement_note` recording the adjacent-skill
  check and why this case's real math (rhombus vs. kite diagonal-crossing geometry) is
  singleton-reinforcement, not new territory. Downgrades T1-10 to a permanent, expected GAP.
- **T1-13 (GAP).** The 45-minute timed plan never named the moment the twist-like MA3 reveal
  lands. Edited the 20:00-30:00 row in FACILITATOR.md to explicitly call out "this is where the
  case's TWIST lands: reveal MA3's near-flip (1.89x vs. the stated 2.0x)."
- **T1-14/T1-18 (GAPs, orphan numbers 1.89 / 8.0 / 1.5).** All three are real, traceable figures
  that were missing from `case.json.derived` at checkable precision: added
  `ma3_flip_point_waste_mult_rounded` (1.89), `other_standards_count` (8, the 8 standards beyond
  the 3 reinforcement skills), and `b_layout_waste_mult_twisted` (1.5, the Interactive HTML's
  "researched cutting layout" toggle value). Also fixed a stale `case.json.new_coverage_note`
  cross-reference in FACILITATOR.md's header (now points to `reinforcement_note`).
- **T1-15 (GAP, xlsx).** The 8 flagged xlsx cells were legitimate full-precision computed values
  (side lengths, roll yardage) — added matching high-precision entries to `case.json.derived`
  (`rhombus_side_in_precise`, `kite_short_side_in_precise`, `roll_yards_needed_a/b`). Separately,
  found and fixed a **real formula bug**, not a rounding artifact: `Cost Takeoff!B11` in
  `Kite Cut - Data.xlsx` computed margin as `ABS(B6-C6)/MIN(B6,C6)` = 2.207%, which disagrees with
  the project's own margin convention (`margin_pct = 100*(winner-loser)/loser`, per SKILL.md and
  this case's own `sensitivity_model.py`) and with the published 2.16% figure everywhere else in
  the case. Corrected the formula to `ABS(B6-C6)/MAX(B6,C6)` and recalculated the workbook via
  `soffice --headless` (cached value now 0.021597 = 2.16%, matching case.json/case.md/FACILITATOR).
- **T1-15 (GAP, docx).** Regenerated both published .docx files from the corrected
  case.md/FACILITATOR.md via `skills/case-publish/scripts/build_docx.js`, clearing the stale
  `new_coverage_note` reference. Three numbers remain flagged (10.0, 15.0, 45.0) — verified these
  are false positives: they're clock-time table entries (`10:00`, `15:00`, `45:00` in the timed
  Socratic plan) that the docx-continuity checker doesn't strip the way the FACILITATOR.md-prose
  checker does (which explicitly excludes `\d{1,2}:\d{2}`). Declaring this GAP as a known checker
  limitation rather than a content defect — not fixed, since it requires a script change outside
  this remediation's scope (the checker script, not the case content, is the actual defect).

### Skipped (documented, not fixed)
- The docx-checker's clock-time false positive above (T1-15) — a `tier1_structural.py` fix, not a
  case-content fix; flagging for a future script patch rather than reformatting a correct table to
  dodge a checker gap.
- No other GAP or POLISH item required rework beyond what's listed above.

### Tier 1 — structural (21 checks), re-run after fixes
checks run: 21 · PASS 19 · GAP 2 · FAIL 0

| id | result | note |
|---|---|---|
| T1-01..T1-09 | PASS | |
| T1-10 | GAP | reinforcement carve-out (expected, permanent — see above) |
| T1-11..T1-14 | PASS | |
| T1-15 | GAP | 3 clock-time false positives in the docx continuity sweep (checker limitation, declared above) |
| T1-16..T1-21 | PASS | |

**BLOCKER (0). GAP (2): T1-10, T1-15 (documented above, both accepted). POLISH (2): T1-07, T1-20 (pre-existing, non-blocking).**

**VERDICT: TIER1_PASS (0 blockers, 2 gaps)**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh read of the packet reaches Option A (True Diamond) by computing D1-D5 correctly: both raw sail areas are identical (648 sq in, diagonals formula is crossing-point-independent); Option A's zero-waste parallelogram pairing plus tail (1,224 sq in total) still undercuts Option B's individually-boxed layout (1,296 sq in) — $12.005 vs. $12.270/kite, a 2.16% margin. Metric optimized: total material cost per kite/run, the case's own stated `primary_metric`, not raw area (a deliberate red herring). Most sensitive assumption identified correctly as MA3. Weakest-supported number: S1 (general Wikipedia sizing claim, explicitly non-load-bearing) or S2's "from $3.75" unbundled rod price. |
| P2 both-sides | PASS | Both sides have a real, defensible best sentence: A — "the zero-waste parallelogram nesting is proven geometry, not an assumption, and still wins on the stated numbers." B — "Option A's cost edge depends entirely on MA3, an unsourced worst-case assumption for B that Appendix H explicitly invites you to challenge." Neither side collapses to an indefensible position; B's defense must lean on MA3's disclosed fragility rather than the stated cost table, which is the intended tension, not a broken pitch. |
| P3 trap | PASS | Most plausible wrong path — judging material cost by outline shape ("the visibly different frame must use more/different fabric") without ever running D2's diagonals-formula comparison. FACILITATOR.md's "The trap" section names this exact failure mode verbatim. A second-order trap (assuming equal area implies equal total cost, missing the tail and MA3) is also explicitly covered by Deep Conflict thread 1. |
| P4 twist | PASS, with a documentation note | FACILITATOR.md declares "Twist: N/A," but the published Interactive HTML ships a working optional toggle (MA3's waste multiplier 2.0x -> 1.5x) that DOES flip the recommendation to B ($11.075 vs. $12.005/kite) — a real, verdict-invalidating effect, not a cosmetic one. Re-derived under every reading of the stated formulas: no ambiguity, the toggle only touches Option B's sail-fabric term exactly as documented, so it survives the case's own stated assumptions cleanly (no Cold-Chain-style sequential-reading bug). Flagging for a human call, not fixing: FACILITATOR's "N/A... without needing a scripted reveal" framing is in tension with the Interactive HTML actually shipping a scripted, verdict-flipping reveal toggle. Recommend a future wording pass (e.g. "Twist: OPTIONAL interactive toggle, not a gated narrative reveal") rather than treating this as a defect — the math is sound and the instability is already fully disclosed via `sensitivity_disclosure[]`. |
| P5 sensitivity | PASS (disclosed) | Machine sweep (+/-50% on the 3 declared dials) found `tail_len_mult`, `tail_width_in`, and `b_layout_waste_mult` all flip the verdict at the extremes. Added `case.json.sensitivity_disclosure[]` with a category + justification for each (F for MA1/MA2 — no single true value exists to research; X for MA3 — a knowable-in-principle but undocumented true value, honestly estimated conservatively). Re-run confirms `PASS (disclosed)`. |
| P6 data decay | PASS | All 7 cited URLs (S1-S7) fetched live and reachable; every recorded claim/value still appears verbatim on the current page (diamond-kite sizing, rod price/length, Eddy 19% crossing point, tail-need vs. tailless framing, fabric price/width, both tail-length guidance sources). No drift, no dead links. |
| P7 accessibility | PASS | Genuine zero-context read of the published Interactive HTML packet. Only one real-world (non-math) concept was not explained anywhere in the document: "bowed spreader" (mentioned twice in Background, describing the Eddy design's curved cross-stick, never defined inline — only reachable via an optional Appendix G further-reading link to "Bowed kite — Wikipedia"). Everything else (ripstop nylon, spine, spreader, nose/tail, stock rod length) is either glossed inline via hover-definitions or clear from the scale diagram. 1 named concept is under the 2-concept FAIL threshold — PASS, with a minor future polish suggestion (gloss "bowed" inline). |

### Tier 3 — human dry-run
NOT RUN
