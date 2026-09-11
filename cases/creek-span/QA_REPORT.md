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

## case-readiness run — 2026-09-10 (protagonist rename)
**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS

### What changed
Protagonist renamed "Priya Nakamura, P.E." → "Suri Nakamura, P.E." across `case.md`,
`FACILITATOR.md`, `case.json.protagonist`, and `published/Creek Span - Interactive.html`
(prose only — no numbers, margins, options, deliverables, sources, or the verdict touched).
Added character texture to `case.md`'s Background (and a matching one-sentence beat in
`FACILITATOR.md`'s Intro): Suri grew up in this town and crossed the old footbridge over Miller's
Creek every school morning as a kid, and still carries a tape measure in her bag out of habit even
to meetings where she won't use it. `LEARNING_GOALS.md` and `RESEARCH_LOG.md` contained no
protagonist name (checked — neither names Priya), so neither needed edits.
Published packet rebuilt: `Creek Span - Case Study.docx` and `Creek Span - Facilitator Guide.docx`
regenerated via `skills/case-publish/scripts/build_docx.js creek-span`; `Creek Span - Data.xlsx`'s
one "Priya" cell (Appendix B side-note, `A2`) updated via openpyxl and verified cell-for-cell
identical to the prior workbook except that one string. `Creek Span - Interactive.html` had only
its 7 protagonist-name/Background-prose lines edited (`git diff` confirms no other line changed) —
its independently-verified glossary/JS logic (`evaluate()`/`evaluate_twist()`, `STORY_GLOSSARY`,
the steel-angle/math-Angle term-collision fix) is byte-for-byte untouched.
`published/MANIFEST.json` resynced (`case_md_sha256`, `built_on`, file byte counts) via
`skills/case-readiness/scripts/resync_artifacts.py --case creek-span` plus a manual MANIFEST note,
since that script only touches HTML/docx/xlsx mtimes, not MANIFEST.json content.

### Tier 1 — structural (21 checks), re-run
PASS 18 · GAP 2 · FAIL 0. **0 BLOCKERs.** Same two pre-existing, already-documented GAPs as every
prior run (T1-03 Option B fuzzy-match false positive; T1-10 reinforcement carve-out). Verdict:
**TIER1_PASS**.

### Tier 2 — simulated play (7 probes), re-run
No case math, sources, or the FACILITATOR twist logic changed — only protagonist name and prose
texture — so every probe was re-verified against the rebuilt packet rather than assumed.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Re-read the regenerated cold-solve packet (`/tmp/coldsolve-creek-span/PACKET.md`, now naming Suri). Reproduced the full D5 arithmetic unchanged: chord + new-diagonal weight × $0.55/lb + joints × 1.5 hr × $30.18/hr, ÷ 24 ft → A $21.22/ft vs. B $24.91/ft, 14.81% margin. Metric named (total fabricated cost per foot of span), MA1 named as most sensitive assumption, S4 named as least-supported figure. |
| P2 both-sides solve | **PASS** | A's case (fewer joints, lighter chord) and B's case (zero-cost salvage, cheaper raw material at $190.34 vs $192.32) both still stand on their own; B still collapses first at the full D5 joint-labor tally, unchanged from the prior run — none of this turns on the protagonist's name. |
| P3 trap check | **PASS** | The "free steel is free steel" trap named in `FACILITATOR.md`'s Data Deep Dive is unchanged and still the most plausible wrong path from `case.md` alone. |
| P4 twist integrity | **PASS** | Re-derived the twist under the case's own stated facts: jointsB 9→8, labor = 8 × 1.5 hr × $30.18/hr = $362.16, total = $552.50, $23.02/ft — matches `case.json.derived.twist_cost_per_ft_b_usd`/`twist_margin_pct` (23.02 / 7.84%) exactly. No unstated convention required; winner unchanged. |
| P5 assumption sensitivity | **PASS** | `sensitivity_model.py` mechanical sweep of MA1 ±50%: margin ranges 11.0%–16.7%, A wins throughout, no SPEC §2 cap breach. |
| P6 data decay | **PASS** | Fetched all 3 distinct sourced URLs directly (WebFetch): Engineers Edge (S1/S2/S3, all three weights 3.21/4.89/7.17 lb/ft confirmed verbatim), SteelFlo (S4, $950–$1,250/ton range confirmed verbatim), BLS OOH (S5, $62,780/yr May-2025 median confirmed verbatim). No dead links, no drifted figures. |
| P7 accessibility cold-read | **PASS** | Regenerated `/tmp/coldread-creek-span/PACKET.md` from the rebuilt Interactive HTML and read it cold myself (no nested/background agent). Confirmed the P7-fix from the prior run is still intact: "steel angle" carries the correct structural-steel definition (the packet still shows the known, previously-documented packaging artifact of the math Angle gloss appended after it — a cold-read packet construction quirk, not a live-page defect, per the prior run's note and reconfirmed by `git diff` showing the linker JS untouched), P.E./AISC/A36/L2×2×1/4 are all explained on first use, and "floodway ordinance" remains the sole borderline/soft item — 1 concept, at/under the probe's 0–1 pass threshold. No new unexplained concepts introduced by the rename or the added Background texture. |

**7 of 7 probes PASS.** `case.json.qa.state` stays `TIER2_PASS`, `qa.verdict` stays `PASS`.

### Tier 3 — human dry-run
NOT RUN.

## Next step
Tier 2 remains clean after the protagonist rename. No further action required for this pass.

## case-readiness run — 2026-09-10 (user review remediation)
**State:** TIER2_PASS   **Verdict:** PASS

### What changed
User review of the published Interactive HTML asked for three things, none touching
`evaluate()`/`evaluate_twist()` or the `STORY_GLOSSARY` steel-angle/math-Angle term-collision fix
(both confirmed byte-for-byte untouched via `git diff`):

1. **Bridge visuals.** Appendix B already carried real, carefully-verified inline SVG technical
   elevation diagrams (panel points, chord/diagonal lengths, triangle labels) for both options —
   confirmed present and left untouched. What was missing was a picture of what each design
   actually *looks like as a structure*, not just a line diagram of lengths and angles. Replaced
   the Overview's two small abstract silhouette SVGs with two larger, labeled inline SVG
   illustrations showing each truss as a real pony-truss footbridge over Miller's Creek — deck,
   railing posts, banks, water — with The Warren Line's tall/deep 3-panel truss and The Low Line's
   low/shallow 4-panel truss visually distinct at a glance, each clearly labeled and captioned.
   `tier2_probes.py --probe 7`'s visual counter went from 2 → 4, confirming both are detected.
2. **Suri's story.** Added a specific, vivid childhood memory (the third board past the north
   bank that always gave underfoot and never broke) tied directly to how she separates
   sentimentality from engineering rigor, in `case.md`'s Background, the Interactive HTML's
   matching paragraph, and `FACILITATOR.md`'s Intro (plus one added facilitator prompt tying the
   memory to D2's Triangle Inequality check). No plot, options, numbers, or deliverables changed.
3. **Deliverables checklist as process guide.** Added a third array element to each
   `DELIVERABLES` entry in the Interactive HTML (`D1`–`D5`) — a short "why this step" line
   explaining the process/reasoning (e.g., why the Triangle Inequality Theorem gates
   buildability before cost, why cost-per-linear-foot rather than raw totals is the fair
   comparison) without stating any numeric answer or verdict. `renderChecklist()` updated to
   render this line under each label.

`published/Creek Span - Case Study.docx` and `Creek Span - Facilitator Guide.docx` rebuilt via
`skills/case-publish/scripts/build_docx.js creek-span`; `Creek Span - Data.xlsx` unaffected in
content (no case data changed) and resynced via `resync_artifacts.py --case creek-span`.
`published/MANIFEST.json` updated by hand (`case_md_sha256`, file byte counts, note) since
`resync_artifacts.py` only touches file mtimes, not MANIFEST content.

### Structural completeness check (before Tier 1/2)
`grep -o "<h[1-3][^>]*>[^<]*</h[1-3]>"` on the rebuilt Interactive HTML shows all expected
sections present and unchanged: Overview, Background, Bridge & Truss Vocabulary, The Dilemma,
Challenges, Deliverables checklist, Appendices, Working Notebook, Twist (plus the
submission-packet template headings). File size grew 92,882 → 98,253 bytes (net addition, no
truncation). `sensitivity_model.py` re-run standalone reproduces base margin 14.81% (A −21.2172
vs. B −24.9073) and twist margin 7.84% (A −21.2172 vs. B −23.0210) exactly matching the
Interactive HTML's ported `evaluate()`/`evaluate_twist()` JS and every figure already on record —
confirms the JS was not touched or regressed.

### Tier 1 — structural (21 checks), re-run
PASS 19 · GAP 2 · FAIL 0. **0 BLOCKERs.** Same two pre-existing, already-documented GAPs as every
prior run (T1-03 Option B fuzzy-match false positive; T1-10 reinforcement carve-out). T1-15/T1-16
(continuity/hash staleness) cleared after the docx rebuild + MANIFEST/`case.json` resync. Verdict:
**TIER1_PASS**.

### Tier 2 — simulated play (7 probes), re-run
No case math, sources, options, or twist logic changed — only visuals, character prose, and
checklist process explanations — so every probe was re-verified against the rebuilt packet.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Read `/tmp/coldsolve-creek-span/PACKET.md` (regenerated from the current `case.md`) cold and worked it by hand: A = (195.60+154.08)×$0.55 + 7×1.5×$30.18 = $509.21 → $21.22/ft; B = (301.14+44.94)×$0.55 + 9×1.5×$30.18 = $597.77 → $24.91/ft; margin 14.81%, A wins. Metric named (total fabricated cost per foot of span), MA1 named as most sensitive assumption, S4 named as least-supported figure — all unchanged from the case of record. |
| P2 both-sides solve | **PASS** | A's best sentence: fewer joints (7 vs. 9), standard textbook geometry, wins the case's own metric by 14.81%. B's best sentence: zero-cost salvage honors the county's own "free steel is free steel" directive and actually beats A on raw material cost ($190.34 vs. $192.32). B collapses first, at the full D5 joint-labor tally (2 extra joints × 1.5 hr × $30.18/hr = $45.27, more than double B's material-cost edge). |
| P3 trap check | **PASS** | Read `case.md` cold: the most plausible wrong path is reading "free salvage steel" and totaling B's material savings without first checking whether A could use the same salvage (it can't — 3.5+3.5=7<8, a hard geometric wall) — and, for Heroes who do catch that, stopping there and declaring B the winner on "free steel" alone without running the full D5 takeoff. `FACILITATOR.md`'s Data Deep Dive names exactly this two-layer trap. |
| P4 twist integrity | **PASS** | Re-derived under the case's own stated facts: jointsB 9→8, labor = 8×1.5×$30.18 = $362.16, total = $552.50, $23.02/ft, margin 7.84% — matches `case.json.derived` exactly. No unstated convention required; winner unchanged. |
| P5 assumption sensitivity | **PASS** | `sensitivity_model.py` mechanical sweep of MA1 ±50%: margin ranges 10.99%–16.70%, A wins throughout, no SPEC §2 cap breach. |
| P6 data decay | **PASS** | Fetched all 3 distinct sourced URLs directly (WebFetch, this run): Engineers Edge (S1/S2/S3 — 3.21/4.89/7.17 lb/ft, all confirmed verbatim), SteelFlo (S4 — "$950–$1,250/ton" confirmed verbatim), BLS OOH (S5 — "$62,780" May 2025 confirmed verbatim). No dead links, no drifted figures. |
| P7 accessibility cold-read | **PASS** | Regenerated `/tmp/coldread-creek-span/PACKET.md` from the rebuilt Interactive HTML (`n_visuals_found: 4`, up from 2 before the new Overview illustrations) and read it cold myself end-to-end. The known pre-existing packaging artifact (the math-Angle gloss trailing the correct "steel angle" structural gloss in the flattened cold-read text) is still present and still confirmed a packet-construction quirk, not a live-page defect — `autoLinkStoryGlossaryTerms`/term-collision fix untouched per `git diff`. P.E./AISC/A36/L2×2×1/4/Gusset Plate/Chord/Panel Point/Pony Truss all explained on first use. "Floodway ordinance" remains the sole borderline/soft real-world concept — 1 item, at/under the probe's 0–1 pass threshold — unchanged by the new visuals, story texture, or checklist explanations, none of which introduced new unexplained real-world jargon. |

**7 of 7 probes PASS.** `case.json.qa.state` → `TIER2_PASS`, `qa.verdict` → `PASS`.

### Tier 3 — human dry-run
NOT RUN.

## Next step
Clean after this remediation pass. No further action required.

## case-readiness run — 2026-09-10 (live-browser mechanical audit, Pier Wheel bug class)

**State:** TIER2_PASS   **Verdict:** PASS (no defects found; nothing changed in the published HTML or the model)

### Why this run
Pier Wheel's published Interactive.html was found to carry two real, user-caught bugs (a doubled-backslash
JS syntax error that silently broke the entire script, and a Working Notebook slider whose `max` sat below
one option's real computed ceiling) that every prior "verified" pass missed because those passes only read
source/grepped text and never actually drove the live page. This run repeats that same mechanical audit on
`published/Creek Span - Interactive.html`, live, over local HTTP (not `file://`), to check whether the same
bug class is present here. `evaluate()`/`evaluate_twist()` and the `STORY_GLOSSARY` steel-angle/math-Angle
term-collision fix were carefully verified earlier today's runs above — this pass RE-verified them live
rather than assuming, per instruction, but did not touch them since they checked out correct again.

### Method and findings
1. **Served over local HTTP** (`python3 -m http.server`, not `file://`) and loaded in a real browser.
   Console: 0 errors on load, and 0 errors thrown across every subsequent DOM-driven interaction below.
2. **Extracted the one inline `<script>` block** (HTML comments stripped first) and ran it through
   `node --check`: syntactically valid. No Pier-Wheel-class doubled-backslash or similar break.
3. **Searched the Working Notebook / calculator section for every `<input type="range">` or numeric input
   with `min`/`max`.** Result: `grep -n 'type="range"\|min="\|max="'` over the full published HTML returns
   **zero matches**. This case's Working Notebook (Steps 1-6) uses free-form `<input type="number">` fields
   with no `min`/`max` clamp at all — so the specific bug class that hit Pier Wheel (a slider `max` cutting
   off part of the real exploration space) **cannot occur here by construction**: there is no bound to be
   wrong. Confirmed this is a genuine design difference, not an oversight — every Step 1-6 field accepts any
   typed value and is graded by tolerance-based comparison (`near()`), not range-restricted.
4. **Drove the calculator via real DOM events** (`el.value = X; el.dispatchEvent(new Event('input'))`) for
   all of Steps 1-6, matching Appendix B/C/D/E/F's real numbers: `checkGeometry`, `checkInequality`,
   `checkWarrenTriangle`, `checkLowLineTriangle`, `checkTakeoff`, and `checkTwist` (after clicking the real
   `#twistBtn` reveal button and toggling `#applyTwist`) all returned "✓" live, and `checkTakeoff`'s live
   output read *"Option A (The Warren Line)... margin: 14.81%..."*, `checkTwist`'s live output read
   *"...margin moved from 14.81% to 7.84%..."* — both exact matches to `sensitivity_model.py`'s
   `evaluate()`/`evaluate_twist()`, confirming the ported JS is still byte-for-byte consistent with the
   Python model.
5. **Swept `gusset_hours_per_joint` from 0 to 10** (far wider than the case's own ±50% flex range of
   0.75-2.25) through the live page's `evaluate()`/`evaluate_twist()`: no `NaN`, no console error, at any
   point. Noted (not a defect) that at `h=0` the winner flips to B on material cost alone — expected and
   consistent with the case's own "material cost is close to a wash" narrative and `checkTakeoff`'s own
   prompt ("does the winner ever flip?"); the case's stated flex range (0.75-2.25) never reaches that flip
   point, matching `case.json`'s recorded sensitivity note (10.99%-16.70%).
6. **Exercised every other interactive element live**: the Dilemma pick radios (`#pickA`/`#pickB`, real
   `.click()`, `localStorage` persists correctly, pill text updates correctly both directions); the
   deliverables checklist (`#chk_D1` toggle persists to `localStorage` and back); the Twist reveal button
   and `#applyTwist` toggle (Step 6 fields correctly hidden until both are triggered, in that order); both
   glossaries live in the rendered DOM — confirmed 2 `.sterm[data-sterm="Steel Angle"]` spans (correct
   structural definition) and the math `.gterm[data-term="Angle"]` links only ever landing on genuine
   math uses (D1, the Appendix I vocabulary list, the "How to multiply decimals" HOWTO entry) — zero
   collisions, the P7-fix documented in the 2026-09-09 entries above is still intact.
7. **Fresh full-page read** (`get_page_text`, end to end) and a **fresh P1 cold-solve + fresh P7 cold-read**
   (regenerated packets, read personally, no nested/background agent): both reproduce the same PASS
   findings already on record (A wins at $21.22/ft vs. B's $24.91/ft, 14.81% margin; "floodway ordinance"
   remains the sole borderline unexplained real-world term, at/under P7's 0-1 threshold; the math-Angle
   packaging artifact in the flattened cold-read packet text is confirmed once more to be a packet-builder
   quirk, not a live-page defect, since the live DOM check in step 6 shows no such collision).

**Verdict: no real defect of the Pier Wheel bug class (or any other) found.** Nothing in
`published/Creek Span - Interactive.html` or `sensitivity_model.py` was changed by this pass.

### Tier 1 — structural (23 checks), re-run
PASS 21 · GAP 2 · FAIL 0. **0 BLOCKERs.** Same two pre-existing, already-documented GAPs (T1-03 Option B
fuzzy-match false positive; T1-10 reinforcement carve-out). Verdict: **TIER1_PASS**.

### Tier 2 — simulated play (7 probes), re-run
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh packet, fresh read: A $21.22/ft vs. B $24.91/ft, margin 14.81%, metric named, MA1 named as most sensitive, S4 (steel $/lb, blog-midpoint-derived) named as least-supported figure. |
| P2 both-sides solve | **PASS** | Unchanged from the 2026-09-10 run above — not re-litigated since no math/prose affecting either side's argument changed in this pass. |
| P3 trap check | **PASS** | Unchanged — the free-steel/geometry-fit trap is still exactly what `FACILITATOR.md` names. |
| P4 twist integrity | **PASS** | Re-confirmed live in-browser this run (see Method §4/§6): `checkTwist()`'s live output reproduces 23.02/ft and 7.84% margin exactly; winner unchanged. |
| P5 assumption sensitivity | **PASS** | Mechanical rerun: -50% -> 10.99% margin, +50% -> 16.70% margin, A wins throughout; also swept live in-browser 0-10 hr/joint (Method §5) with no NaN/errors across the full range. |
| P6 data decay | **PASS** | Not re-fetched this pass (no source claims touched); stands on the 2026-09-10 WebFetch verification above. |
| P7 accessibility cold-read | **PASS** | Fresh packet, fresh cold read (see Method §7): same 1 borderline item ("floodway ordinance"), same confirmed-harmless packaging artifact, 0 new unexplained concepts. |

**7 of 7 probes PASS.** `case.json.qa.state` stays `TIER2_PASS`, `qa.verdict` stays `PASS`.

### Tier 3 — human dry-run
NOT RUN.

## Next step
Clean. No defects found by this mechanical live-browser audit; no further action required.
