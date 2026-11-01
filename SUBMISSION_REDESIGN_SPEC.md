# Submission & Workbook Redesign — Spec (DRAFT)

**Date:** 2026-10-29 · **Status:** draft for owner R2; not yet through unanimous R1 approval
**Origin:** two real submissions (LeBron vs. Michael — Nishchay S., 2026-10-23; Gerrymandering — Moksh A., 2026-10-28) reviewed by R1a, R1b, R1c. Verdicts: R1a BLOCK, R1b BLOCK, R1c CONCERNS — all agree the mechanism needs redesign and that the two cases must be fixed separately, not encoded as-is.

Related: `templates/INTERACTIVE_HTML_CONTRACT.md` §6, `RUBRIC.md` (C2/C4/C5/C7), `PRD.md` R3, `sql/schema.sql` (`class_submissions`).

---

## 1. Problems (observed)

| # | Problem | Evidence |
|---|---|---|
| P1 | No single submit path. Toolbar has "Export PDF" (whole case) beside "Submit" (2-page packet that only downloads). Students hand in whichever looks like "the PDF". | Nishchay sent the packet; Moksh sent the 15-page case print. |
| P2 | Nowhere to write the pitch/justification. Challenge 2 is not a `deliverables` entry, so the checklist cannot see C2 (weight 20). | Gerrymandering: no pitch, 0/4 checklist, no appendix. |
| P3 | Workbook is not structured per option/player. Packet rows are unlabeled or all read "lebron". | LeBron packet: four rows "lebron — not checked yet". |
| P4 | Checkbox is self-report, wrong evidence. Page says "track your own progress". | Checklist all "not marked done" while values show "checks out". |
| P5 | Green = "input was valid", not "answer accepted". `checkD4` is always green; `checkD1` only tests the sum; Step 2 accepted Idaho's total area. | 18+ shares entered as under-18 → 77.34% (correct 22.66%) with green ✓. |
| P6 | Static HTML exposes reference values in view-source (PARAMS, LEBRON_SEASON_ASSISTS). Per-field "checks out" lets students search to green. | R1b (c); `interactive_shell.html:589`. |
| P7 | Guide has no view of status per deliverable. | Owner R2. |

## 2. Design principles

1. **One submission, one button, one file.** Everything a guide needs is in it.
2. **Justify at the decision points, not everywhere.** Every deliverable has an Answer; a **Why** is required only at 2–3 designated points per case (the Pitch plus at most two judgment deliverables). Context is critical: reasoning is asked for where a choice was made, which avoids fatigue and keeps the Whys meaningful.
3. **Evidence, not ticks.** No self-marked checkboxes feed any status.
4. **Both options visible.** Numbers for every option/player side by side, labeled.
5. **Guide-side verdicts only.** The student never sees a verdict (MCS-37 hard line holds). Verdicts are machine first-pass; the guide confirms.
6. **Honest about what machines can't check.** Reasoning and open-ended items get rubric tags, never green.

## 3. Student flow

1. Student works the case and Working Notebook as today.
2. Each deliverable card (D1…Dn, plus **Pitch** as a final row) has an **Answer** box. Cards the author flags `why: required` (max 2 per case, plus the Pitch = max 3 Whys total) also show a required **Why** box with a word floor by tier (Pitch uses Challenge 2's 250 words). All other cards show an optional one-line note. A "Why" card states what decision it asks about (e.g. "What threshold did you use for a meaningful deviation, and why?").
3. Notebook steps are labeled by option/player and source appendix. Where a case compares options, the notebook holds one block per option; the packet prints them side by side.
4. Toolbar: replace "Submit" with **Build my submission**. "Export PDF" is renamed **Print case (reference only)** and visually demoted. Page text states: "Your submission is the file from *Build my submission*."
5. Build step shows a completeness list (what's missing), not a verdict, and builds the PDF anyway.
6. Self-review (3 RUBRIC questions) is part of the packet. Student's name is in the filename.
7. **Twist.** The pick is **frozen and timestamped at the first Build**; later rebuilds may add work but show the original pick and mark any change. The Twist reveal is unlocked by the facilitator in class; for self-paced use it unlocks only after the first Build. The Twist text is not present in the page source, "Print case (reference only)" or the packet until unlocked (print styles exclude it), so view-source and print cannot bypass the gate. The checkbox label no longer asserts a claim for the student.

## 4. Submission packet contents (single PDF)

1. Header: case, student, date, case version/freeze date.
2. Pick + reasoning paragraph.
3. Per deliverable: Answer, the notebook values it rests on (labeled by option), and the Why for designated decision points (optional note elsewhere).
4. Side-by-side option table (all inputs and results, units, rounding as entered).
5. Original visual (student-built) and appendix of working.
6. Self-review answers.
7. Machine-readable block (JSON, embedded and also POSTed when R3 lands): field id, option, value, unit, Why text.

No "checks out" strings anywhere in the student's file.

## 5. Guide view

Computed server-side from a **versioned reference** generated from each case's `sensitivity_model.py` at build time, carrying `frozen_on` and data vintage (never checked against live sources, which drift).

| Status | Meaning |
|---|---|
| GREEN ("matches reference") | Numeric value matches the **versioned reference** within a propagated tolerance (§7). Self-consistency alone is never green: wrong inputs with consistent arithmetic must not pass. A decision-point card is green on its number only; its Why is judged by the guide, never greened by presence. |
| AMBER | Value matches but the unit is missing or wrong, or the value is right for a different convention than the case states. |
| RED | Missing, or violates a hard set constraint (e.g. a district not in the case's region set), or contradicts the student's own appendix. |
| CHECK THIS | Out of tolerance, or fails a plausibility guard (e.g. under-18 share outside 10–35%; implausible is not the same as wrong) — guide decides. |
| RUBRIC | Not machine-checkable (see below). Shows tag checklist, never green. |

Every status cites its evidence ("recomputed 22.66, student 77.34").

**Not machine-checkable → RUBRIC tags:** weighted algorithm (≥3 case inputs, stated weights, same inputs for both options, recommendation consistent with own scores), convex/concave call, string-measured perimeter (±10% band), scenario-only metrics, Pitch (claim; both options computed; rejected option's strongest number; threshold stated before computing; limitation + flip test).

Guide view always labeled "machine first pass — not confirmed". Guide confirms or overrides, as in `submission-score`; each override records `guide_id`, reason and timestamp.

**Class triage:** a roster-by-deliverable grid (rows = students, columns = deliverables, cells = status) sortable by RED / CHECK THIS, so a guide with ~20 submissions opens only the ones that need a look. Every row also shows its count of unconfirmed RUBRIC cards (Pitch, algorithm, convex call), so a submission with green numbers and a weak Pitch is never skipped. In-line Why text appears when a card is opened.

## 6. Data model

`class_submissions` today has `answer_text` and `pdf_path` only. Add `submission_fields` (jsonb or child table): `field_id, option, value, unit, why_text, notebook_refs`, plus `reference_version` and `pick_frozen_at`. Guide statuses stored separately from student data with `computed_on`. Overrides are rows with `guide_id`, `reason`, `overridden_at`, `previous_status`.

## 7. Check semantics (replaces per-case ad-hoc checks)

- Tolerance = the student's input rounding error **propagated through the formula** by worst-case interval (each entry ± half its last displayed digit; e.g. a margin of two percentage shares entered to 2 dp carries ±0.01 percentage points), not a flat ±0.1. Reference drift (source vintage) is a separate, disclosed allowance recorded in the reference, never folded into the student tolerance.
- Plausibility guards and their ranges are **guide-only**: they are never printed in the page, the Build step or the student's file, since a range leaks the expected answer.
- Quartile/percentile method named in the case and in the reference.
- Plausibility guards defined per field in the case's reference file.
- Reference carries tolerance, convention (e.g. efficiency gap: all-votes vs two-party), and source vintage.

## 8. Case-authoring contract changes

- `deliverables` includes the Pitch row. **The Pitch is always a required Why** (250 words, C2 — the explicit exception to the tier floors) and counts as one of the max 3. At most 2 further deliverables carry `why: required`, with a `why_prompt` and tier-based `why_min_words`. Readiness check fails a case with more than 3 required Whys; it does not require extra ones (a pure-calculation case's Pitch is its decision point).
- **Rubric coverage rule:** every deliverable with `check_type: rubric` (weighted algorithm, convex/concave, string-measured perimeter) is **always shown to the guide with its rubric-tag checklist and an "unconfirmed" status**, whether or not it is a designated Why. It is never greened and never hidden by triage sorting. Why boxes stay capped at 3 (Pitch + 2); a rubric card without a Why must have an Answer that evidences itself (e.g. the algorithm's weights table, the measured perimeter with scale). A case may carry any number of rubric cards.
- A required Why's `why_prompt` asks for: the threshold stated before computing, the rejected option's strongest number, and what input change would flip the call. Word floors are completeness hints and never set a status on their own.
- Each deliverable declares `check_type`: `numeric | set | rubric`, with its guards.
- Notebook fields declare `option`/`player` and `source_appendix`.
- `case.json` and published HTML must agree (add a Tier-1 case-readiness check; currently Gerrymandering D2/D4 drift).
- Packet must not contain Twist text (add check).
- Readiness check: no always-green check functions.
- Readiness check (P6): the published HTML must not embed reference values or answer-bearing parameters (e.g. PARAMS, season totals) beyond what the case's own appendices print; the reference lives only server-side.
- `case.json` is the single source for deliverables, options and prompts; the published HTML is generated from it, so drift (e.g. Gerrymandering D2/D4) cannot occur. `case.json` fields are split into **publishable** (prompts, options, appendices, sources, deliverable text) and **reference-only** (expected values, tolerances, guards, Twist text until unlocked); the generator emits only the former, and the P6 check enforces it. Until generation lands, the §8 drift check applies.
- Sensitivity check: cases on live political disputes or naming living people carry a **student-visible** neutrality frame plus a teacher note (Gerrymandering, LeBron vs. Michael). The frame states that the rubric grades the quality of reasoning, not which conclusion the student reaches.

## 9. Out of scope / open questions

- Server-side POST and auth belong to PRD R3; this spec defines the payload so R3 can adopt it.
- **Decided (owner R2, 2026-10-29):** Why text shows **in-line** in the guide view. Why is required at 2–3 decision points per case (Pitch + at most two), not every deliverable. Word floors by tier (complexity of the question) confirmed in principle; R1a suggests T1 40, T2 50 (a trade-off to argue), T3 60, T4 80 per required Why, Pitch 250. Owner to confirm the T2 change.
- **Confirmed:** the two PDFs received are the only submissions; no separate write-ups exist. This is why the Pitch row and a single packet are needed.
- Open: which deliverables are the designated decision points for each case (author picks; default = the deliverable where a threshold, assumption or convention is chosen).

## 10. Case fixes (separate track — do not encode current dilemmas)

**Gerrymandering (R1a/R1b: BLOCK)**
- Background claims Idaho gains a third seat; the 2020 apportionment left it at 2 (next chance after 2030). Reframe as a hypothetical/after-2030 scenario or re-source.
- Plan A is +18.4% / −7.2% / −11.3% vs the case's own 5% rule. R1a reads this as Plan B dominating the ordered criteria; R1b notes `case.json:450-452` says Plan A wins on county integrity. Authors must reconcile: the dilemma is only genuine if both plans are legally viable, so either redraw Plan A within tolerance or reframe the trade-off.
- Efficiency gap is identical under both plans by MA2; choose a discriminating primary metric or add sourced county-level shares. Convention (R1a and R1b agree on recomputation): the case's stated two-party convention (MA2) gives **12.56%** (signed, favors R; statewide two-party share 561,405/816,936 = 68.72%), for baseline and projection alike. Alternates reproduce from the same totals but are off-convention: 17.89% (all votes, minor votes counted as wasted, literal Appendix E) and 14.01% (hybrid, drop). Decide: keep Appendix E as printed and grade 17.89%, or rewrite it as two-party and grade 12.56%; record the convention in the reference. Also bound the FLEX sweep: `statewide_r_share` ×1.5 yields an impossible 1.03 share and the script returns −56.2.
- Step 3: the published HTML (≈ line 941) computes total/2+1 = 229,285.5 and displays "229,286", while the surplus shown (81,451) uses 229,285 (half of 458,569 is 229,284.5). Make the threshold and label consistent at 229,285 with surplus 81,451. (R1a's "81,450" was wrong; the string "229,286" is not in `case.md`/`case.json`, only produced by the HTML code.)
- Background "on track to gain a third seat" appears in `case.md:25` and the published HTML overview, not only the background; fix all instances. Also fix `case.json` NEEDS_SOURCE tokens (≈ lines 462–538) and replace Neilsberg (secondary) as the statewide under-18 source.
- Step 2/D2: only region areas accepted; D2 region and D4 scope must match `case.json`.
- Remove Twist spoiler from printed text; fix "both maps satisfy the letter of the law" vs Appendix C.
- S19 "16% competitive" unsupported (also in `case.json:734` glossary and HTML:448). Drop, or replace with a dated, verified figure; R1b found 43 competitive, 22 toss-ups (NPR/KUNC, 2026-10-08), but 43/435 ≈ 10% is not a substitute for the unverified 16%, and Kettering (the S19 source) returned 403. An earlier "≈7%, 32 of 435" figure could not be re-supported and is withdrawn.
- Source hygiene: the case sums Ada 1,053 + Canyon 590 (S6/S7, Wikipedia's NACo "Area" column shows 1,055 / 590, not a land/total split). Census QuickFacts 2020 land area is Ada 1,052.01 / Canyon 587.05 (totals 1,060 / 604 unverified). Pick one basis (land or total) from a primary Census source and record its vintage. Statewide under-18 and age vintage differ from the 2020 counts; record the vintage allowance in the reference.

**LeBron vs. Michael (R1a/R1b)**
- Twist is within noise (one Jordan make flips it) and the Jordan playoff 150/444 conflicts with Basketball-Reference 148/446; resolve reconstruction or use a band.
- `FLEX = []` makes the sensitivity check vacuous.
- D2 recovery is copying (Appendix C prints all 18 totals); hide or replace.
- Name the quartile method (Tukey 25.3/27.5 vs QUARTILE.INC 25.58/27.48).
- Option B rests on FT% and ungraded rings; rebalance or disclose.
- Freeze/vintage key for career stats (live BBRef has drifted).
- Fix packet's Player labels; margin 5.54 vs 5.55 rounding.
- Teacher note: living athletes (Gerrymandering: neutrality note).

**Corpus**
- Add Pitch deliverable to all cases' `deliverables`; 4 of 16 sampled cases lack a recommendation row.
- Elections/apportionment overlap (Gerrymandering, Redrawing Lines, Electoral College); Phone Plan vs Phone Plans.
- 169 of 200 cases lack catalog metadata.

## 11. Rollout

1. Owner R2 on this spec → R1a/b/c re-review (unanimous approval gate).
2. Shell + contract change; migrate LeBron and Gerrymandering as pilots after case fixes.
3. Add case-readiness checks (§8), live-browser audit per memory, UAT as each persona, automated tests.
4. Migrate remaining cases in batches; R3 server POST adopts §4 payload.

**Effort and policy (open):** each migrated case needs notebook refactoring (option/player/source_appendix labels), per-field guards and a versioned reference; estimate per case to be set after the two pilots, with ~200 cases migrated by priority (active cohort first). **In-flight policy:** students mid-case keep the HTML version they started (version pinned in the packet); submissions are scored against the `reference_version` stamped in their packet, and a guide may rescore against a newer version only by explicit override, with notice to the student. **Factual-errata exception:** a case with a known factual error (e.g. Gerrymandering's third-seat premise) is reissued to in-flight students with a visible errata notice rather than left pinned. Both pilots still carry open case-fix BLOCK items, so they do not yet prove the contract; fix them first.
