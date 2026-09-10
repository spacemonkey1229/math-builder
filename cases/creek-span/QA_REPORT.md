# QA Report — creek-span

## case-readiness run — 2026-09-09
**State:** DRAFT → BLOCKED   **Verdict:** BLOCKED (Tier 1)

### Tier 1 — structural (21 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | FAIL (BLOCKER) | Overview contains numerals ['24'] that are neither clock times nor years — needs read + clearance in `case.json.overview_numerals_cleared[]` or remains BLOCKER |
| T1-03 | GAP | Option B may not be named in Background (fuzzy match; read and clear or keep deliberately) |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | GAP | standards[] claims skills absent from the final appendix: ['Triangle'] |
| T1-08 | PASS | |
| T1-09 | PASS | |
| T1-10 | GAP | new_coverage[] empty; reinforcement carve-out available if `reinforcement_note` added |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | FAIL (BLOCKER) | anchor ladder incomplete, missing headings: ['Intro','Launch','Anchor 1','Anchor 2','Anchor 3','Anchor 4','Data Deep Dive','Close','Lessons Learned','Standards Touched On']; no timed 45-minute Socratic plan (SPEC §7.3); facilitator guide has 0 Socratic questions (spec asks for 5) |
| T1-14 | PASS | |
| T1-15 | GAP | CONTINUITY — 1 number(s) in published/Creek Span - Facilitator Guide.docx appear in neither case.md nor case.json: [60.0] |
| T1-16 | GAP | no case_md_sha256 recorded yet (expected on a first run) |
| T1-17 | PASS | |
| T1-18 | PASS | |
| T1-19 | PASS | |
| T1-20 | POLISH | no image/chart/diagram/map found in published/ HTML — not required |
| T1-21 | PASS | |

**BLOCKER (3):**
1. [T1-02] SPEC §1.2 — Overview contains numeral '24', not a clock time or year. Must be read and either cleared as texture in `case.json.overview_numerals_cleared[]` or, if a student could use it in a calculation, it stays a BLOCKER.
2. [T1-13] MCS-14 — anchor ladder incomplete, missing headings: Intro, Launch, Anchor 1, Anchor 2, Anchor 3, Anchor 4, Data Deep Dive, Close, Lessons Learned, Standards Touched On.
3. [T1-13] MCS-16 — no timed 45-minute Socratic plan (SPEC §7.3); facilitator guide has 0 Socratic questions, spec asks for 5.

**GAP (6):**
- [T1-03] Option B may not be named in Background (fuzzy match; read it and clear or keep deliberately)
- [T1-07] standards[] claims skill 'Triangle' absent from the final appendix
- [T1-10] new_coverage[] is empty — no reinforcement_note recorded yet
- [T1-13] facilitator guide has 0 Socratic questions, spec asks for 5
- [T1-15] CONTINUITY — number 60.0 in published Facilitator Guide docx appears in neither case.md nor case.json
- [T1-16] no case_md_sha256 recorded yet (expected on first run)

**POLISH (2):**
- [T1-07] parsed 9 labels (9 bulleted, 0 from separator-run lines)
- [T1-20] no image/chart/diagram/map found in published/ HTML — not required, but consider adding one

### Tier 2 — simulated play (7 probes)
NOT RUN — Tier 1 has open BLOCKERs; per skill doctrine, Tier 2 does not start until Tier 1 is clean (0 BLOCKERs).

### Tier 3 — human dry-run
NOT RUN

## Next step
Fix the 3 blockers (T1-02 overview numeral clearance/removal, T1-13 anchor-ladder headings + timed 45-minute Socratic plan with 5 questions in FACILITATOR.md) and re-run case-readiness.

## case-readiness run — 2026-09-09 (remediation)
**State:** BLOCKED → TIER1_PASS   **Verdict:** TIER2_FAIL (P7)

### What changed
- **T1-02 (BLOCKER, fixed):** Overview's stray numeral '24' ("a 24-foot footbridge") was not
  flavor text — it is the same load-bearing span figure used in D5's cost-per-foot calculation —
  so per SPEC §1.2 it was rephrased out of the Overview rather than cleared as texture: "a 24-foot
  footbridge" → "a short footbridge". No `overview_numerals_cleared[]` entry needed since the
  numeral no longer appears there.
- **T1-13 / MCS-14 (BLOCKER, fixed):** `FACILITATOR.md` was rewritten with the full anchor-ladder
  structure (Intro, Launch, Anchor 1-4, Data Deep Dive, Twist, Immediate recommit, Close, Lessons
  Learned, Five Socratic Questions, Standards Touched On, Cohort Bands), grounded in creek-span's
  actual content (truss geometry, the Triangle Inequality gate, the fabrication-sub joint-combining
  twist, margin 14.81% → 7.84%).
- **T1-13 / MCS-16 (BLOCKER, fixed):** Added a timed 45-minute Socratic plan table and 5 Socratic
  questions (reformatted one-per-line so the mechanical scanner recognizes them) grounded in the
  case's real numbers.
- **T1-07 GAP (fixed):** Appendix I's vocabulary list was missing "Triangle" itself (the term
  behind the `geometry-triangle` skill used by D1). Added.
- **T1-10 GAP:** left as a recorded GAP, not fixed — `case.json.reinforcement_note` already
  documents the reinforcement carve-out per 2026-08-17 doctrine (all six Triangles skills already
  at spine n=1; no genuine n=0 zero exists for this case to claim). This is correct as-is, not a
  defect.
- **T1-03 GAP:** read Background directly — "The Low Line" (Option B) is in fact named and
  described at length in Background (paragraphs on its panel count, depth, floodway-driven
  geometry, and chord-weight tradeoff). This is a fuzzy-match false positive (the checker looks
  for literal "Option B," not the option's story name) — kept deliberately, not fixed.
- **T1-15 docx continuity drift ("60.0"):** the Twist's "You have 60 seconds" line in
  `FACILITATOR.md`/the Facilitator Guide docx had no home in `case.json.derived`. Added
  `derived.twist_response_window_sec: 60.0` so it no longer drifts silently.
- **Published artifacts:** re-rendered `Creek Span - Case Study.docx` and
  `Creek Span - Facilitator Guide.docx` from the edited sources
  (`skills/case-publish/scripts/build_docx.js`), then resynced remaining artifact mtimes and the
  QA hash (`skills/case-readiness/scripts/resync_artifacts.py`). Per this task's explicit
  instruction, `Creek Span - Interactive.html`'s glossary/JS content was **not** touched — it was
  independently rebuilt and verified earlier this session.
- **Skipped:** nothing else was skipped as "excessive rework" — all listed items above were
  addressed.

### Tier 1 — structural (21 checks), re-run
PASS 19 · GAP 2 · FAIL 0. **0 BLOCKERs.** Remaining GAPs: T1-03 (fuzzy-match false positive, Option
B genuinely named in Background), T1-10 (reinforcement carve-out, already documented). Verdict:
**TIER1_PASS**.

### Tier 2 — simulated play (7 probes)
Run directly (no nested/background agents), per this task's instruction.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Worked the packet (`/tmp/coldsolve-creek-span/PACKET.md`) as a fresh solver. Chose A ($21.22/ft vs. $24.91/ft, 14.81% margin), reproduced the full D5 arithmetic (chord + new-diagonal weight × $0.55/lb + joints × 1.5 hr × $30.18/hr, ÷ 24 ft), named the optimized metric (total fabricated cost per foot of span), named MA1 (joint labor hours) as the most sensitive assumption, and named S4 (steel $/lb, derived from an industry blog's range midpoint) as the least-supported figure. Reached the intended, defensible position for the right reasons. |
| P2 both-sides solve | **PASS** | A's best case: fewer joints (7 vs. 9) and lighter chord steel win on both labor and material despite buying all-new diagonal steel. B's best case: material cost is actually lower than A's ($190.34 vs. $192.32) thanks to zero-cost salvage reuse, and the Triangle Inequality check has a real 1-ft margin (3.5+3.5=7>6). B collapses first, at the full D5 joint-labor tally — its "free steel" narrative is real but is outweighed by two extra gusset joints ($90.54 more labor). Neither side is a bare concession; the 14.81% margin is not a paper number. |
| P3 trap check | **PASS** | From `case.md` alone, the most plausible wrong path is exactly the one named in `FACILITATOR.md`: seeing "free steel is free steel" and stopping at B's zero-cost salvage reuse without running the full takeoff, missing that B's shallower depth also forces heavier chord steel and two extra joints. The guide names both the shortcut and its subtler variant. |
| P4 twist integrity | **PASS** | (1) The twist invalidates a room's confident "A wins clearly" position — the margin nearly halves (14.81% → 7.84%). (2) Re-derived under the case's own stated facts: combining 2 of B's 9 joints into one field connection changes only the joint count (9→8), leaving all other Appendix E/F quantities untouched; recomputed labor = 8 × 1.5 hr × $30.18/hr = $362.16, total = $552.50, $23.02/ft — matches `case.json.derived.twist_cost_per_ft_b_usd` (23.02) and `twist_margin_pct` (7.84) exactly. No unstated convention required; the winner does not flip. |
| P5 assumption sensitivity | **PASS** | `sensitivity_model.py`, `FLEX = ['gusset_hours_per_joint']`. ±50% on MA1: -50% (0.75 hr/joint) → margin 11.0%, A still wins; +50% (2.25 hr/joint) → margin 16.7%, A still wins. No flip, no SPEC §2 cap breach. |
| P6 data decay | **PASS** | Fetched all 5 sourced URLs directly (WebFetch; raw curl hit bot-detection 403s on 2 of them, consistent with `case.json`'s own S4 note about this site class). All 3 Engineers Edge figures (3.21/4.89/7.17 lb/ft) confirmed verbatim. BLS's $62,780/yr May-2025 median wage confirmed verbatim (case's derived $30.18/hr is unchanged arithmetic). SteelFlo's $950-$1,250/ton range confirmed verbatim. No dead links, no drifted figures. |
| P7 accessibility cold-read | **FAIL** | Built the packet from the already-published `Creek Span - Interactive.html` and read it cold, as a zero-context reader. Found a real defect the mechanical T1-21 hover-glossary check cannot see: the phrase "salvaged steel **angle**" in the Overview/Background is hover-defined with the *math* glossary's definition of "angle" ("a measure of the amount of turn between two rays...") — wrong in context; "steel angle" here means L-shaped angle-iron stock, not a geometric angle, and the mismatched definition actively misleads rather than helps. Beyond that one wrong definition, at least two more real-world (non-math) terms go unexplained anywhere in the packet: the "L2×2×1/4" angle-size notation (leg × leg × thickness in inches) and "AISC"/"A36" (the steel-shapes standard and grade the sourcing table cites), plus "P.E." / "seal on her own stamp" (professional-engineer licensing) on first use. That is 3+ genuinely unexplained/mis-explained concepts, over the probe's 2-concept pass threshold. **Not fixed** — this task's instructions explicitly excluded editing the Interactive HTML's glossary/JS content; the fix (correct the "angle" hover-definition to a structural-steel-specific one, and add STORY_GLOSSARY entries for the angle-size notation, AISC/A36, and P.E.) is named here for a follow-up pass, not applied. |

**6 of 7 probes PASS; P7 FAILs on a real, previously-uncaught glossary-correctness defect in the
published Interactive HTML.** Per SPEC, `qa.state` stays at `TIER1_PASS` (not `TIER2_PASS`) until
P7 is re-run clean after that HTML fix — Tier 2 is not clean with a recorded FAIL.

### Tier 3 — human dry-run
NOT RUN.

## Next step (superseded — see the 2026-09-09 P7-fix run below)
Fix the P7 defect in `published/Creek Span - Interactive.html` (mismatched "angle" hover-definition
in Overview/Background; missing glossary entries for the L2×2×1/4 angle-size notation, AISC/A36,
and P.E./"seal on her own stamp") without touching anything else in that file, then re-run
`tier2_probes.py --case creek-span --probe 7`. Once clean, `case.json.qa.state` can move to
`TIER2_PASS` and `case-publish` can run.

## case-readiness run — 2026-09-09 (P7 fix)
**State:** TIER1_PASS → TIER1_PASS   **Verdict:** TIER2_FAIL (P7) → TIER2_PASS

### What changed in `published/Creek Span - Interactive.html`
Only the glossary-linking JS and the `STORY_GLOSSARY` data object were touched — `evaluate()`,
`evaluate_twist()`, and every previously-verified glossary entry are untouched.

- **Term-collision fix (the wrong "angle" hover-def):** `autoLinkStoryGlossaryTerms()` now runs
  *before* `autoLinkGlossaryTerms()` (the math linker already skips anything inside a `.sterm`
  span), so once "steel angle" is claimed by the new STORY_GLOSSARY entry, the math linker never
  sees that text. As a second, independent guard (for the bare "…angle" that follows the
  `L2×2×1/4` shorthand with no literal word "steel" in front of it), `autoLinkGlossaryTerms()`
  now skips any "Angle" match whose preceding ~40 characters end in `steel`, `structural`, or an
  `L#x#x#/#` size code, so a math-Angle link can no longer land on a structural-steel mention.
- **New STORY_GLOSSARY entries (`{desc, link}`, `.sterm` class — verified-live URLs, 2026-09-09):**
  "Steel Angle" (engineersedge.com/angle_steel.htm — reused, already cited in Appendix G), "L2×2×1/4"
  (same source), "AISC" (aisc.org), "A36" (en.wikipedia.org/wiki/A36_steel), "P.E."
  (nspe.org/resources/licensure/what-pe).
- **Two small correctness fixes needed to make the above safe:** (1) both linkers now skip text
  already inside an `<a>` tag (`AISC`/`A36` only ever appear inside the Appendix G/H citation
  links' own text — without this they'd have nested a second `<a>` inside the citation's `<a>`,
  invalid HTML and its own accessibility problem); (2) the story linker's word-boundary regex was
  switched from `\b…\b` to lookaround (`(?<!\w)…(?!\w)`) because `\b` silently fails to match a term
  that ends in punctuation followed by non-word text — exactly "P.E." followed by a space, which
  never would have matched under the old regex.
- Verified by inspection of the JS (parses cleanly with `new Function()`) and by loading the file
  in a live browser (local HTTP server, not `file://`, so the script actually executes): confirmed
  in the rendered DOM that "steel angle" now carries a single `.sterm` link to the correct
  definition, the math `.gterm` "Angle" link only ever lands on the genuine Notebook-math uses
  (Step 3/4 interior-angle work, Challenge D3's "classify… by angle"), all 5 new STORY_GLOSSARY
  entries render in the on-page glossary grid with live `https://` links, and there are 0 nested
  `<a>` tags anywhere in the page.
- Grepped the file for literal `{{` placeholders and verdict-leak text: none found.

### P7 re-run
`tier2_probes.py --case creek-span --probe 7` mechanical pre-screen: 0 probes failed mechanically
(unchanged — P7 was never mechanically failing; it fails/passes on the model-judged cold-read).
Regenerated `/tmp/coldread-creek-span/PACKET.md` from the fixed HTML and read it cold myself (no
nested/background agent, per this task's instruction), as a reader with no background in Priya
Nakamura reading the case for the first time.

Note on the packet itself: `build_html_cold_read_packet()` is a static text-substitution script,
not a DOM/JS-aware renderer — it inserts every `GLOSSARY` gloss before every `STORY_GLOSSARY` gloss
by construction, so "steel angle"'s first mention in the packet still shows *both* the (correct)
Steel Angle gloss and, appended after it, the math Angle gloss it would have received under the old
code. That is a packaging artifact of the probe script (out of scope for this fix — the task
scoped changes to the Interactive HTML only), not a live-page defect: the actual rendered page,
confirmed above, only ever attaches the one correct definition. Read as a student, the term is now
*explained* (correctly, if redundantly) rather than *actively misled*, which is what P7 tests for.

**Cold-read finding:** every term named in the original FAIL is now explained on first use —
"steel angle" (correct material definition, not the math one), "P.E.", "AISC", "A36", and
"L2×2×1/4" (the last via context — "L2×2×1/4 structural steel angle" — plus its own glossary entry
at second mention). The only borderline item is "floodway ordinance" (Background/Appendix B),
which has no dedicated hover-def but is explained functionally in the same sentence ("required to
clear the county's floodway ordinance for the walkway underside during high water"). That is 1
soft/borderline concept, at or under the probe's 0-1 pass threshold, with none of the original
mis-explained or fully-unexplained concepts remaining.

**Verdict: PASS.**

### Tier 2 — final
7 of 7 probes PASS. `case.json.qa.state` → `TIER2_PASS`, `qa.verdict` → `TIER2_PASS`.

### Tier 3 — human dry-run
NOT RUN.

## Next step
Tier 2 is clean. `case-publish` / Tier 3 human dry-run can proceed when scheduled.
