# QA Report — dice-roll

## case-readiness run — 2026-09-09 (remediation pass)

**State:** TIER1_PASS → **TIER2_PASS**   **Verdict:** PASS

This run remediates the 3 BLOCKERs and several GAPs from the 2026-09-09 readiness-gate run, then
completes Tier 2. Fixes were applied directly (no nested/background agents were used, per explicit
instruction); Tier 2's model/subagent-adjudicated probes (P1-P4, P7) were self-adjudicated by the
fixing agent against the case's own packets rather than dispatched to a genuinely fresh subagent —
recorded as a caveat below, not concealed.

### BLOCKERs fixed (all T1-13)

* **MCS-14** — `FACILITATOR.md` fully rewritten onto the required anchor ladder: Intro, Launch,
  Anchor 1-4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On (plus Cohort
  Bands and a 45-Minute Socratic Plan). Anchors 2-3 precede the Data Deep Dive as required.
* **MCS-15** — a real Twist section was added. It reuses the twist already live in
  `published/Dice Roll - Interactive.html`'s gated "Reveal the Twist" panel (a conceptual
  challenge: a county clerk argues the ballot-level RLA's randomness already covers Marisol's
  visit-plan question; it doesn't — the two sampling processes are independent) rather than
  inventing a competing one. `sensitivity_model.py`'s pre-existing `evaluate_twist()` (an Alamosa
  highway-bypass distance change) is kept as an optional secondary quantitative extension.
* **MCS-16** — a timed 45-minute Socratic plan with 8 timed rows (spec shows 7) and 5 single-line
  Socratic questions (was 0 counted; the prior draft's questions were multi-line and didn't match
  the counter) were added.

### Also fixed (quick items)

* **T1-07** — Appendix F (case.md) was missing 5 spine-verbatim vocabulary labels claimed by
  `standards[]` (Addition, Multiplication, Percent, Proportion, Rounding). Added.
* **T1-10** — `reinforcement_note` was already present and honest (adjacent uncovered skills
  checked and ruled out); this correctly downgrades the SPEC §8 empty-`new_coverage[]` finding
  from BLOCKER to GAP per the 2026-08-17 carve-out. No further action — this GAP is permanent by
  design, not a defect.
* **T1-14/T1-15** — resolved by the FACILITATOR.md rewrite plus a `case.json.derived.cost_breakdown`
  block recording the cost-comparison and twist figures so they're checkable, not orphaned.
  Rebuilding `FACILITATOR.md` also staled the 4 published artifacts; all 4 were rebuilt/resaved
  (docx via python-docx, xlsx resaved with no content drift, html patched for one glossary bug and
  touched) and `MANIFEST.json` updated. A residual GAP remains: 4 facilitation-timing numbers
  (13, 30, 35, 45 — table row minutes not matching the `\d{1,2}:\d{2}` clock-time exclusion) are
  flagged as orphans; reviewed, these are legitimate timed-plan minute markers, not drift.
* **T1-17** — `cohort_bands[]` added to `case.json` (Full/Compressed/1:1 bands with notes).
* **Preflight FLEX bug** — `mileage_rate` (cited, S7) removed from `sensitivity_model.py`'s
  `FLEX[]`; it was cited data sitting in the assumptions-sweep list by mistake. `FLEX` is now
  `["staff_daily_rate", "overnight_threshold_mi"]`, the two genuine Modeling Assumptions.
* **P7 side-finding, fixed in passing** — `STORY_GLOSSARY`'s "Chain Of Custody" entry existed but
  never actually auto-linked, because the source prose used the hyphenated "chain-of-custody"
  while the auto-linker matches space-separated phrases. Changed to "chain of custody" in
  `case.md`, the published docx, and the interactive HTML; confirmed the popup now renders.

### Skipped

* Full re-render/visual proofing of the rebuilt docx packets (PDF conversion + screenshot check
  per the `docx` skill's own verification step) was skipped as excessive rework for this pass;
  content was verified programmatically (text extraction, number continuity) instead. Recommend a
  visual proof pass before this case reaches a human-facing `PUBLISHED` promotion.
* T1-09's "margin is wide" GAP (19.43%, inside the 20% cap) was left as-is — the case's own design
  already carries a documented sensitivity note and a `sensitivity_disclosure[]` entry; narrowing
  the margin itself would mean re-tuning MA1/MA2, out of scope for this pass.

### Tier 1 — structural (21 checks), re-run after fixes

**VERDICT: TIER1_PASS (0 blockers, 3 gaps)**

| id | result | note |
|---|---|---|
| T1-01 .. T1-08 | PASS | |
| T1-09 | GAP | margin 19.43% is inside the cap but wide — documented, not retuned |
| T1-10 | GAP | empty `new_coverage[]`, reinforcement carve-out applies (permanent, by design) |
| T1-11 .. T1-14 | PASS | |
| T1-15 | GAP | 4 facilitation-timing numbers in the Guide docx (13, 30, 35, 45) reviewed, legitimate |
| T1-16 .. T1-21 | PASS | |

Preflight lint: clean (`mileage_rate` removed from FLEX).

### Tier 2 — simulated play (7 probes)

**VERDICT: TIER2_PASS — 0 FAIL across all 7 probes.**

| Probe | Mechanical | Verdict | Notes |
|---|---|---|---|
| P1 Cold solve | leak-free packet confirmed | **PASS** | Self-adjudicated (see caveat above), not a fresh subagent. Metric named (total program cost), arithmetic reproduced independently and matches `sensitivity_model.py` exactly (A=$3,624.64, B=$2,920.48, margin 19.43%). A defensible position is reachable either way (B on cost; A on D4's representativeness) provided the solver actually opens D4 — the case's own trap. |
| P2 Both-sides solve | READY (after fix) | **PASS** | `balance.argument_b` originally carried <3 digits (mechanical FAIL); rewritten with the full cost breakdown ($2,920.48 vs $3,624.64, $704.16/19.43% gap). Both arguments are real, numeric, non-concession cases. B's argument collapses first and completely at the D4 "will a Western Slope county ever be visited" question (a hard 0%, not a probability); A's argument survives that question but requires a value judgment on whether representativeness is worth $704.16 — it doesn't structurally collapse. |
| P3 Trap check | trap named | **PASS** | Independently-derived trap ("B is cheaper and still hits 5 counties → declare it the winner without opening D4") matches `FACILITATOR.md`'s named trap exactly. |
| P4 Twist integrity | READY | **PASS** | (1) Invalidates a real room position: "the county audit is already random, so the visit plan doesn't need to be." (2) Depends on no stated numeric assumption at all (it's conceptual), so it survives every reading trivially — no Cold-Chain-style convention dependency. The optional quantitative extension (Alamosa bypass) was independently re-derived and matches `evaluate_twist()` exactly: A $3,624.64→$3,354.84, margin 19.43%→12.95%, winner unchanged. |
| P5 Assumption sensitivity | **PASS (disclosed)** | **PASS** | `staff_daily_rate` −50% → 28.17% and `overnight_threshold_mi` −50% → 21.80%, both over the 20% cap; neither flips the winner. Both are now recorded in `case.json.sensitivity_disclosure[]` as Category X (proprietary/inaccessible, good-faith estimate from a public analogue) with 20+-char justifications, matching Appendix D's own MA1/MA2 sensitivity language. Margin never flips the winner under any ±50% sweep of the 2 genuine FLEX assumptions. |
| P6 Data decay | 8 sources checked via WebFetch | **PASS** | No dead (404) or fabricated links. S7 (mileage rate) and S8 (GSA per diem) both fetched and confirmed verbatim. S1 (Verified Voting) reachable, RLA content confirmed (county count not visible in the fetched excerpt but the source is live and on-topic). S2/S3/S4/S5 (Justia, Colorado SoS, TravelMath) returned HTTP 403 to automated fetch — consistent with this case's own already-documented pattern (S7's note already records the state's OSC page doing the same); not evidence of a dead or wrong claim, just bot-blocking. S6 (World Population Review) is reachable but now shows 2026-projection figures rather than the cited 2024 Vintage estimates, with small drift (e.g. Jefferson 580,543 vs. the case's 580,451) — expected of a live-updating aggregator, already MEDIUM-confidence and explicitly non-load-bearing to the cost balance test per its own `sources[]` note. |
| P7 Accessibility cold-read | 2 visuals found vs. 4 deliverables matched | **PASS** | The MCS-48 mechanical match (D2/D3/D5 flagged alongside D6) is a false positive — only D6 actually requires visuals (bar graph + pie chart), and those are correctly *absent* from the packet because they are the student's own deliverable, not an answer key; D2/D3/D5 were keyword-matched on unrelated "chart/diagram" language. Reviewed and cleared. Real-world jargon check: found and fixed one glossary bug (STORY_GLOSSARY's "Chain Of Custody" entry never auto-linked because the prose used "chain-of-custody" with hyphens against a space-matching regex — fixed at the source in `case.md`, the docx, and the HTML). After the fix, only one borderline unexplained phrase remains ("a Colorado state classified analyst's salary band," buried in Appendix D's MA2 justification, not required to complete any Challenge) — within the probe's 0-1-concept PASS threshold. **Political neutrality confirmed directly in the published/student-facing packet text** (Overview, Background, Dilemma, Challenges, Appendix D/E), not just in `FACILITATOR.md`'s SPEC §6 flag: no candidate, party, or election-outcome framing anywhere; the case stays entirely inside sampling methodology, program cost, and Colorado's real risk-limiting-audit statute (C.R.S. §1-7-515). |

### Tier 3 — human dry-run

NOT RUN (unchanged — requires a real cohort).

---
**Next step:** a human visual proof of the rebuilt `published/` docx packets (skipped this pass —
see Skipped above), then `case-publish`'s two human-confirm steps (read-model promotion + optional
Drive upload) to move from `TIER2_PASS` to `PUBLISHED`.
