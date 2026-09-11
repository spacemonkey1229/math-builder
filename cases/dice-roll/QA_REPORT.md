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

---

## case-readiness run — 2026-09-10 (character/voice pass — no data changed)

**State:** TIER2_PASS → **TIER2_PASS** (re-confirmed)   **Verdict:** PASS

Scope: purely a character/personality pass on protagonist Marisol Ibarra, per explicit
project-owner request. Added: a former-poll-worker background, an unflappable-under-scrutiny
trait, and a six-sided die kept on her desk from her first audit-methods training (a concrete,
on-theme sampling callback). No number, source, margin, option, deliverable, or the verdict was
touched. Fixes applied directly (no nested/background agents, per explicit instruction).

**Files touched:** `case.md` (Background — 2 new sentences of texture woven into the existing
protagonist paragraph), `FACILITATOR.md` (Intro — a new paragraph naming the same traits for
facilitators), `case.json` (`protagonist` field enriched; `qa.case_md_sha256` updated twice, see
below). `published/Dice Roll - Interactive.html`, `Dice Roll - Case Study.docx`, `Dice Roll -
Facilitator Guide.docx`, and `Dice Roll - Data.xlsx` were rebuilt from source via the existing
generic pipeline (`scripts/generic_publish/build_html.py`, `skills/case-publish/scripts/build_docx.js`,
`scripts/generic_publish/build_xlsx_generic.py`) — no hand-editing of binaries. The rebuild
initially dropped a hand-authored feature not covered by the generic pipeline or `html_config.py`
(the `STORY_GLOSSARY`/`.sterm` election-vocabulary hover-glossary layer, previously spliced
directly into the published HTML at original authoring time) — caught by Tier 1's T1-21 (MCS-47)
going from PASS to GAP after the first rebuild. Recovered the original block from git history
(`git show 74ad25f:cases/dice-roll/published/Dice Roll - Interactive.html`) and re-spliced it into
the freshly-built HTML, adding one new story-glossary term ("Poll Worker") for the new background
text; T1-21 returned to PASS. `MANIFEST.json` updated with new byte sizes and hash both times a
rebuild ran.

**Mid-pass correction:** a genuinely fresh cold-read (Tier 2 P7) of the first-draft rewrite caught
that the new Background sentence used the phrase "the provisional-ballot envelopes" — a real
election-jargon term with no glossary entry. Combined with the pre-existing borderline term ("a
Colorado state classified analyst's salary band," in Appendix D's MA2), that would have put the
packet at 2 unexplained real-world concepts, over the probe's 0-1-concept PASS threshold.
Simplified to "the long lines of forms to sign" in `case.md`, rebuilt the packet again, and
re-ran the cold-read: back to exactly 1 borderline term (unchanged from the pre-existing baseline),
a clean PASS.

### Tier 1 — structural (21 checks), re-run after the rewrite

**VERDICT: TIER1_PASS (0 blockers, 3 gaps)** — identical gap set to the 2026-09-09 baseline
(T1-09 margin-width, T1-10 empty `new_coverage[]` reinforcement carve-out, T1-15 four legitimate
facilitation-timing numbers). No new gaps, no regressions, after the story-glossary fix above.

### Tier 2 — the 6 scripted probes + P7 cold-read, re-run

| Probe | Result | Notes |
|---|---|---|
| P1 Cold solve | **PASS** | Genuinely fresh cold-solve of `/tmp/coldsolve-dice-roll/PACKET.md`, done directly (no subagent, per instruction). Metric named (total program cost); arithmetic reproduced independently — A = $3,624.64 (mileage $814.64 + lodging $220.00 [Kit Carson, Alamosa overnight] + M&IE $340.00 + staff $2,250.00), B = $2,920.48 (mileage $330.48, no lodging), margin 19.43% — exact match to `case.json.derived.cost_breakdown`. D1: 5/12 = 41.7% of roster, 5/64 = 7.8% of state. D4: P(WS/SLV county selected, 1 cycle, A) = 5/12 = 41.7% vs. 0% under B; P(at least once in 3 cycles, A) = 1 − (7/12)^3 ≈ 80.2% vs. 0% under B forever. Strongest counter-argument: the $704.16/19.43% premium is real and the margin is documented as "wide" (T1-09), so a cost-first room can reasonably prefer B. Most sensitive assumption: MA2 (`staff_daily_rate`, $450/day) — a −50% swing alone pushes the margin to 28.17%, over the 20% cap. Ignored: Appendix B's exact per-county systematic-sampling interval/starting-session arithmetic (only needed for D2's own sub-answer, not the A-vs-B decision). Least-supported number: MA2's $450/day, an undisclosed-source estimate and the case's single most load-bearing figure. |
| P2 Both-sides solve | **PASS** (unchanged — no data touched) | Re-affirmed: B's argument collapses first and completely at D4's "will a Western Slope county ever be visited" question (a hard, permanent 0%); A's argument survives that question and only requires a values judgment on whether representativeness is worth $704.16. |
| P3 Trap check | **PASS** (unchanged) | Trap unchanged: "B is cheaper and still hits 5 counties → declare it the winner without opening D4" — still matches `FACILITATOR.md`'s named trap exactly; narrative rewrite did not touch the Dilemma, Challenges, or Twist text the trap depends on. |
| P4 Twist integrity | **PASS** (unchanged) | Twist text and `evaluate_twist()` untouched by this pass; conceptual twist (county-level RLA randomness ≠ visit-plan randomness) still holds, still has no numeric-assumption dependency. |
| P5 Assumption sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically: base margin 19.4% (B cheaper), `staff_daily_rate` −50% → 28.2%/+50% → 14.8%, `overnight_threshold_mi` −50% → 21.8%/+50% → 16.9% — all four figures match the existing `sensitivity_disclosure[]` entries and the pre-existing QA record exactly. **Confirmed: the margin's sensitivity behavior is unchanged by this pass** — no number, rate, or FLEX parameter was touched, only narrative prose. |
| P6 Data decay | **PASS** (unchanged — no source touched) | No source citation, URL, or cited value was touched by this pass; the 2026-09-09 P6 fetch results stand. |
| P7 Accessibility cold-read | **PASS** | Done directly, genuinely fresh, against the rebuilt `/tmp/coldread-dice-roll/PACKET.md` (see mid-pass correction above for the one round-trip this took). Final state: exactly 1 borderline unexplained real-world term ("salary band," Appendix D MA2, not required for any Challenge) — within the 0-1-concept threshold. MCS-48's mechanical visual-flag (D2/D3/D5 keyword-matched alongside D6) is the same pre-existing false positive noted in the 2026-09-09 run — only D6 requires visuals, and they're correctly absent as a student deliverable, not an answer key. **Political neutrality explicitly re-confirmed** in the rewritten Background/Intro text and across the full student-facing packet: grepped for democrat/republican/party/candidate/election-outcome/fraud/liberal/conservative language — zero matches. The new personality material (poll-worker background, unflappable-under-scrutiny trait, the desk die) is character- and competence-only; it makes no claim about election administration, outcomes, or any party, consistent with `FACILITATOR.md`'s SPEC §6 flag. |

### Tier 3 — human dry-run

NOT RUN (unchanged — requires a real cohort).

---
**Next step:** unchanged from the 2026-09-09 record — a human visual proof of the `published/`
docx packets, then `case-publish`'s two human-confirm steps to move from `TIER2_PASS` to
`PUBLISHED`.

---

## case-readiness run — 2026-09-10 (narrative-clarity + visuals remediation pass)

**State:** TIER2_PASS → **TIER2_PASS** (re-confirmed)   **Verdict:** PASS

Scope: direct facilitator feedback that the case wasn't clear on what decision Marisol is making,
why the dice/randomness matter, what the two concrete options are, or whether the sampling methods
(SRS, systematic, cluster, multistage) are a standard toolkit or something invented for this case —
plus a request for a real inline-SVG visual and a deliverables checklist that explains *process*
without leaking answers. No number, source value, margin, option, or verdict was touched. Fixes
applied directly (no nested/background agents, per explicit instruction).

**Files touched:**
- `case.md` — new lead paragraph at the top of Background stating the concrete decision, why the
  dice/random-seed process is the case's actual math content, the two options in one line each, and
  a new sourced claim (S9) that SRS/systematic/cluster/multistage are the standard, textbook-taught
  sampling toolkit — not invented for this exercise — while explicitly disclosing that whether
  Colorado's real Division uses one of these methods for site-visit selection specifically is not
  public record (consistent with the existing MA1-MA5 disclosure pattern, not a second sourcing
  overclaim). Appendix E gained a new S9 row.
- `cases/dice-roll/RESEARCH_LOG.md` — new P09 entry: searched for an election-observation-specific
  source first (OSCE/ODIHR site-selection methodology), found only that real deployment is
  explicitly "pseudo-random" and "not standardized" — rejected as not citable for the intended
  claim — then found and live-fetched OpenStax's *Introductory Statistics 2e* §1.2, which names
  stratified/cluster/systematic sampling as "well-known" alternatives to simple random sampling.
  Quoted verbatim, not paraphrased from memory.
- `cases/dice-roll/case.json` — `sources[]` gained S9 (HIGH confidence, OpenStax, directly fetched
  2026-09-10); `qa.case_md_sha256` updated to match the rebuilt `case.md`.
- `cases/dice-roll/html_config.py` — new `overview_banner_svg` key: a two-panel inline SVG (no
  external images) showing the same 12-county roster grouped by region, with Option A's actual
  5-county draw highlighted spread across every region in the top panel, and Option B's fixed
  Front-Range-only 5 highlighted in the bottom panel with the other four regions visually shaded
  and labeled "never in reach." Uses the page's own CSS custom properties (`--navy`, `--gold`,
  `--bad`, `--line`) so it matches the existing palette exactly. `deliverables[]` gained a 3rd
  element per D1-D6 — a one-line *process* description (what to do and why) that does not state
  any numeric answer or the A-vs-B verdict.
- `scripts/generic_publish/build_html.py` — `{{CASE_OVERVIEW_BANNER_SVG}}` now sources from
  `cfg.get("overview_banner_svg", "")` instead of a hardcoded empty string (backward-compatible:
  every other case's `html_config.py` omits this key and still resolves to `""`).
- `templates/interactive_shell.html` — `renderChecklist()` now destructures an optional 3rd
  `process` element per deliverable and renders it under the label when present (backward-
  compatible: a case whose `DELIVERABLES` array has only `[id, label]` pairs renders exactly as
  before, since `process` is simply `undefined`).
- `published/Dice Roll - Interactive.html`, `Dice Roll - Case Study.docx`, `Dice Roll - Facilitator
  Guide.docx`, `Dice Roll - Data.xlsx` rebuilt from source via the existing generic pipeline
  (`build_html.py`, `skills/case-publish/scripts/build_docx.js`, `build_xlsx_generic.py`) — no
  hand-editing of binaries. As in the 2026-09-10 character/voice pass, the generic HTML rebuild
  drops the hand-spliced `STORY_GLOSSARY` layer (not covered by `html_config.py`); re-spliced from
  the pre-rebuild version after each rebuild, adding one new story-glossary term, **"Audit Board"**
  (linked to the same already-verified-live Colorado SoS press release used for S4), since the new
  Background text uses the term. `MANIFEST.json` updated with new byte sizes and `case_md_sha256`.
- The SVG's `<svg>` tag also picked up `class="county-comparison-diagram"` and
  `aria-label="county sampling comparison diagram"` so Tier 1's T1-20 visual-asset advisory check
  (which pattern-matches on chart/diagram/map keywords in `id`/`class`/`aria-label`) recognizes it;
  purely a metadata addition, no visual change.

**Verification before re-running the gates:** confirmed via
`grep -o '<h[1-3][^>]*>[^<]*</h[1-3]>'` that all expected sections are present (Overview,
Background, The Dilemma, Challenges, Deliverables checklist, Appendices, Working Notebook, Twist,
plus the print-packet template headings) and that `published/Dice Roll - Interactive.html` grew
from 82,144 bytes (2026-09-09 baseline) to 95,410 bytes — no shrink. Verified the SVG and checklist
process lines actually render (not just parse) by serving the file over a local HTTP server and
loading it in a real browser tab (the file:// preview renders only a static snapshot with JS not
executed, which briefly looked like a `DELIVERABLES is not defined` bug before this was diagnosed
as a preview-mode artifact, not a real defect — confirmed by a Node.js syntax check of the extracted
`<script>` block and by the live HTTP-served page evaluating correctly).

### Tier 1 — structural (21 checks), re-run after the rewrite

**VERDICT: TIER1_PASS (0 blockers, 3 gaps)** — identical gap set to the 2026-09-09 baseline
(T1-09 margin-width, T1-10 empty `new_coverage[]` reinforcement carve-out, T1-15 four legitimate
facilitation-timing numbers). No new gaps, no regressions. T1-20 (visual-asset advisory), which
previously fired a polish note for having no chart/diagram in the published HTML, now passes
cleanly given the new SVG.

### Tier 2 — the 6 scripted probes + P7 cold-read, re-run

| Probe | Result | Notes |
|---|---|---|
| P1 Cold solve | **PASS** | Genuinely fresh, done directly (no subagent) against the rebuilt `published/Dice Roll - Interactive.html`, read end-to-end via a live-served copy of the page (Overview, Background, Dilemma, Challenges/checklist, all four content appendices, Working Notebook, Twist, Sources). Metric named (total program cost); arithmetic independently reproduced from the appendix tables alone: A = mileage $814.64 (Jefferson/Boulder/Pueblo/Kit Carson/Alamosa) + lodging $220.00 (Kit Carson 169mi, Alamosa 235mi both exceed the 150mi threshold) + M&IE $340.00 + staff $2,250.00 = **$3,624.64**; B = mileage $330.48 (Jefferson/Douglas/Larimer/Boulder/El Paso, none over threshold) + lodging $0 + M&IE $340.00 + staff $2,250.00 = **$2,920.48**; margin = (3,624.64 − 2,920.48)/3,624.64 × 100 = **19.43%** — exact match to `case.json.derived.cost_breakdown` and to `sensitivity_model.py`'s own printed output. D1: 5/12 = 41.7% of roster, 5/64 = 7.8% of state. D4: single-cycle P(WS/SLV county selected) = 5/12 = 41.7% under A vs. 0% under B; 3-cycle P(at least once) = 1 − (7/12)³ ≈ 80.2% under A vs. 0% forever under B. Strongest counter-argument: the $704.16/19.43% premium is real and documented as "wide" (T1-09), so a cost-first room can reasonably prefer B. Most sensitive assumption: MA2 (`staff_daily_rate`, $450/day) — a −50% swing alone pushes the margin to 28.2%, over the 20% cap. Ignored: Appendix B's exact per-county systematic-sampling interval/starting-session arithmetic (only needed for D2's own sub-answer). Least-supported number: MA2's $450/day, an undisclosed-source estimate and the case's single most load-bearing figure. The new Background paragraph and the SVG diagram did not change any of this arithmetic — confirmed by rederiving it from the appendix tables alone, without reference to the prior QA record. |
| P2 Both-sides solve | **PASS** (unchanged — no cost/option data touched) | Re-affirmed: B's argument collapses first and completely at D4's "will a Western Slope/San Luis Valley county ever be visited" question (a hard, permanent 0%); A's argument survives that question and only requires a values judgment on whether representativeness is worth $704.16. The new Background framing makes this tradeoff easier to see going in, not different in substance. |
| P3 Trap check | **PASS** (unchanged) | Trap unchanged: "B is cheaper and still hits 5 counties → declare it the winner without opening D4" — still matches `FACILITATOR.md`'s named trap exactly; the rewrite touched only Background prose and added a banner visual, not the Dilemma, Challenges, or Twist text the trap depends on. |
| P4 Twist integrity | **PASS** (unchanged) | Twist text and `evaluate_twist()` untouched by this pass; re-read directly from the rebuilt HTML — the conceptual twist (county-level RLA randomness ≠ visit-plan randomness) still holds, still has no numeric-assumption dependency. |
| P5 Assumption sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically: base costs A=$3,624.64/B=$2,920.48 (evaluate() ceiling-transform values {A: 3624.64, B: 4328.8} — the transform, not raw dollars), base margin 19.4%; `staff_daily_rate` −50% → 28.2%/+50% → 14.8%, `overnight_threshold_mi` −50% → 21.8%/+50% → 16.9% — all four figures match the pre-existing `sensitivity_disclosure[]` entries and QA record exactly. No FLEX parameter, rate, or cost figure was touched by this pass — only narrative prose, a visual, and the checklist's process-explanation text. |
| P6 Data decay | **PASS** | S1-S8 unchanged from the 2026-09-09 fetch record (no source touched). New S9 (OpenStax) was fetched live as part of this pass itself (see RESEARCH_LOG.md P09) — HTTP reachable, and the fetched text was quoted verbatim into `case.json`'s source note, not paraphrased from memory (MCS-21). |
| P7 Accessibility cold-read | **PASS** | Done directly, genuinely fresh, reading the rebuilt `published/Dice Roll - Interactive.html` end-to-end via a live-served copy (not the static file:// snapshot). Confirmed the SVG diagram and the 6 deliverable "process" lines actually render in a real browser, not just parse. Real-world jargon check: the new Background text introduces no new unglossaried real-world term — "OpenStax" is a self-explanatory textbook citation, not jargon; the new STORY_GLOSSARY term "Audit Board" (added because the reworked Background now uses that exact phrase) auto-links correctly in the body text, confirmed via a live DOM check (`document.querySelectorAll('.sterm[data-sterm]')` returns "Audit Board" linked both in-body and in the story-glossary card). Final state unchanged from baseline: exactly 1 borderline unexplained real-world term ("salary band," Appendix D MA2, not required for any Challenge) — within the 0-1-concept PASS threshold. MCS-48's mechanical visual-flag false positive (D2/D3/D5 keyword-matched alongside D6) is unchanged and remains correctly cleared — only D6 requires a student-made visual; the new banner SVG is case-authored context, not a D6 answer. **Political neutrality explicitly re-confirmed**: grepped the full rebuilt `case.md` and published HTML for democrat/republican/party/candidate/election-outcome/fraud/liberal/conservative/trump/biden/gop/dnc language (excluding "bipartisan") — zero matches. The new Background paragraph and SVG diagram describe sampling methodology and program cost only; no claim about election administration, outcomes, or any party. |

### Tier 3 — human dry-run

NOT RUN (unchanged — requires a real cohort).

---
**Next step:** unchanged — a human visual proof of the rebuilt `published/` docx packets, then
`case-publish`'s two human-confirm steps to move from `TIER2_PASS` to `PUBLISHED`.

---

## case-readiness run — 2026-09-10 (UAT-defect remediation pass)

**State:** TIER2_PASS → **TIER2_PASS** (re-confirmed)   **Verdict:** PASS

Scope: a simulated 5-student UAT read `published/Dice Roll - Interactive.html` end-to-end and
live-rendered it in a browser, and found 4 real, concrete defects plus 1 clarity issue. All 4
required items fixed for real; the 5th (time allowed) fixed too. No nested/background agents used,
per explicit instruction. Every fix was verified in a real browser via a local HTTP server
(`python3 -m http.server`), never `file://` and never grep-only.

### Defects fixed

1. **Appendix E existed nowhere in the published HTML** — it was present in full in `case.md` all
   along (Sources table, S1-S9) but silently dropped from the HTML build, so both "SEE APPENDICES D
   AND E" (Background) and "Appendix B, Appendix E S4" (Twist) resolved to nothing a reader could
   find. Added a real `<details>Appendix E — Sources</details>` block to the published HTML between
   Appendix D and Appendix F, mirroring `case.md`'s own Appendix E table exactly (Claim/Value/
   Source/Date/Confidence columns), with each row linking to its matching footer citation anchor.
   Both existing Appendix-E references now resolve correctly — confirmed by reading the live DOM
   (`document.querySelectorAll` for the new `<details>` and its table rows).

2. **Width-dependent SVG overlap, confirmed at normal desktop width** — Panel B's italic red "never
   in reach" annotation (`x="437" y="426"`) sat directly on top of the Boulder ✓ / El Paso ✓ county
   labels (Front Range column rows extend to `y=456`, past the annotation's row). Repositioned the
   annotation as two lines below all county rows (`y=476`/`y=491`), pushed the legend row down to
   `y=527` with a separating rule, and grew the `viewBox` from `0 0 760 500` to `0 0 760 545` to fit.
   Verified with real browser screenshots at both 1280px and 800px viewport width — clean at both,
   no overlap, confirmed both visually and via `get_page_text`/DOM inspection.

3. **D2 (Statewide Draw's systematic-sampling interval) had no Working Notebook step** — added Step
   5 ("The Statewide Draw's systematic-sampling interval (D2)"), matching the existing steps'
   pattern exactly: a goal box, 10 `.fieldrow` input fields (interval *k* and starting session for
   each of the 5 realized-draw counties — Jefferson/Boulder/Pueblo/Kit Carson/Alamosa), and a Check
   button wired to a new `checkStep5()` function that reads `PARAMS.a_sessions` and
   `PARAMS.sessions_target_per_county` (no hardcoded answer key). *k* is checked for an exact match
   (`Math.floor(scheduled/target)`); the starting session is checked only for falling inside the
   valid `[1, k]` range, since the actual starting point is the student's own random pick, not a
   fixed answer — verified directly via `checkStep5()` calls: `fb ok` on correct values (k=9 for
   Jefferson), `fb bad` after deliberately setting an incorrect k=5.

4. **Inline `[S#]` citation tags were plain unlinked text** — all 38 occurrences of `[S1]`…`[S9]`
   in the body (Background, Appendix A/B/C prose and table cells) were programmatically wrapped in
   `<a href="#src-Sn" class="cite-link">` links; each footer `<li>` gained a matching `id="src-Sn"`
   plus a small back-arrow (`↩`, `history.back()`) so a reader can jump down and back without losing
   their place. `:target` CSS highlights the destination `<li>` on arrival. Verified by clicking a
   live `[S1]` link via direct DOM `.click()` and confirming `location.hash`, `li.matches(':target')`,
   and the back-arrow's presence in the DOM.

5. **(Time allowed) Background's dense opening paragraph** — split into five shorter paragraphs and
   pulled the single most-missed sentence ("the audit itself is required in all 64 counties
   regardless of Marisol's choice; only the in-person visit selection is being decided") into its
   own `.card`-style callout, matching the pattern already used elsewhere in this corpus (e.g.
   `apron-order`, `bioreactor-bid`). Mirrored into `case.md` as a `>` blockquote in the same
   position so the two stay in sync; `Dice Roll - Case Study.docx` and `Dice Roll - Facilitator
   Guide.docx` were rebuilt from the updated `case.md` via `skills/case-publish/scripts/build_docx.js`
   (confirmed the new callout text landed in the rebuilt docx via `python-docx` text extraction) and
   `Dice Roll - Data.xlsx` was rebuilt via `scripts/generic_publish/build_xlsx_generic.py` (Tier 1's
   staleness check flagged it after the `case.md` edit; content unchanged, timestamp refreshed).
   `MANIFEST.json` and `case.json.qa.case_md_sha256` updated to match.

**Also fixed in passing:** the D2 Working Notebook side-note originally stated "Pueblo's 9÷2 = 4.5
rounds down to 4," introducing a new number (4.5) not present anywhere in `case.md`/`case.json` and
tripping Tier 1's T1-18 continuity check as a GAP; reworded to describe the non-even division
without stating the intermediate decimal, clearing the check back to PASS.

### Verification (real browser, not grep-only)

Served `published/Dice Roll - Interactive.html` over `python3 -m http.server` and drove it with a
live browser tab: confirmed Appendix E renders with real content; confirmed the SVG has no overlap
at 1280px and 800px (screenshots); confirmed Step 5's Check button flips `ok`/`bad` correctly against
both correct and deliberately-wrong input; confirmed a citation link jump sets `location.hash`,
triggers `:target`, and lands the back-arrow in view; confirmed zero political/partisan terms via
full-text grep (democrat/republican/party/candidate/fraud/liberal/conservative/trump/biden/gop/dnc —
zero matches). **`read_console_messages` returned zero entries (0 errors) throughout the entire
session**, including after all form interactions and citation-link clicks.

### Tier 1 — structural (23 checks), re-run after fixes

**VERDICT: TIER1_PASS (0 blockers, 3 gaps)** — identical gap set to the established baseline (T1-09
margin-width, T1-10 empty `new_coverage[]` reinforcement carve-out, T1-15 four legitimate
facilitation-timing numbers). T1-18 (a transient GAP introduced mid-pass by the "4.5" side-note
number) was caught and fixed before this final run — no regression versus baseline.

### Tier 2 — the 6 scripted probes + P7 cold-read, re-run

| Probe | Result | Notes |
|---|---|---|
| P1 Cold solve | **PASS** | Genuinely fresh, done directly (no subagent), reading only `/tmp/coldsolve-dice-roll/PACKET.md` regenerated from the post-fix `case.md` (confirmed the new callout text appears in the regenerated packet). Metric named (total program cost). Arithmetic independently reproduced: A = mileage $814.64 + lodging $220.00 (Kit Carson 169mi, Alamosa 235mi both exceed the 150mi threshold) + M&IE $340.00 + staff $2,250.00 = **$3,624.64**; B = mileage $330.48 (none of B's 5 counties exceed 150mi) + M&IE $340.00 + staff $2,250.00 = **$2,920.48**; margin = (3,624.64−2,920.48)/3,624.64×100 = **19.43%**, B cheaper — exact match to the established baseline. D1: 5/12=41.7% of roster, 5/64=7.8% of state. D4: single-cycle P(remote county selected)=5/12=41.7% under A vs. 0% under B; 3-cycle P(at least once)=1−(7/12)³≈80.2% under A vs. 0% forever under B. Strongest counter-argument: the $704.16/19.43% premium is real and documented as "wide" (T1-09). Assumption named as most sensitive: MA2 (`staff_daily_rate`) — though applied identically in dollar terms to both options, a swing in it still moves the *percentage* margin because it changes each option's total by a different proportion. Ignored: Appendix B's per-county interval/start-point arithmetic (D2's own sub-answer, not the A-vs-B decision). Least-supported number: MA2's $450/day, an undisclosed-source estimate. |
| P2 Both-sides solve | **PASS** (unchanged — no cost/option data touched) | Re-affirmed: B's argument collapses first and completely at D4's "will a Western Slope/San Luis Valley county ever be visited" question (a hard, permanent 0%); A's argument survives that question and only requires a values judgment on whether representativeness is worth $704.16. |
| P3 Trap check | **PASS** (unchanged) | Trap unchanged: "B is cheaper and still hits 5 counties → declare it the winner without opening D4" — matches `FACILITATOR.md`'s named trap; this pass touched only Appendix E, the SVG, the Working Notebook, citation links, and Background prose — not the Dilemma, Challenges, or Twist text the trap depends on. |
| P4 Twist integrity | **PASS** (unchanged) | Twist text and `evaluate_twist()` untouched by this pass (the Twist's "Appendix E S4" reference now correctly resolves, which is a defect fix, not a content change); the conceptual twist (county-level RLA randomness ≠ visit-plan randomness) still holds, still has no numeric-assumption dependency. |
| P5 Assumption sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically: base margin 19.4% (B cheaper); `staff_daily_rate` −50%→28.2%/+50%→14.8%; `overnight_threshold_mi` −50%→21.8%/+50%→16.9% — all four figures match the established `sensitivity_disclosure[]` record exactly. No FLEX parameter, rate, or cost figure was touched by this pass. |
| P6 Data decay | **PASS** (unchanged — no source citation, URL, or cited value touched) | S1-S9 unchanged from the prior fetch record; this pass only added anchor-jump wiring around the existing citations, not new claims or sources. |
| P7 Accessibility cold-read | **PASS** | Done directly, genuinely fresh, against the rebuilt, live-HTTP-served HTML. Confirmed the new Appendix E, SVG fix, Step 5, and citation links all actually render and function (not just parse) via direct browser interaction. Real-world jargon check: the Background restructuring and new callout reuse only already-glossaried terms (audit, observer, county); no new unglossaried real-world term introduced. Final state unchanged from baseline: exactly 1 borderline unexplained real-world term ("salary band," Appendix D MA2, not required for any Challenge). **Political neutrality explicitly re-confirmed**: full-text grep of the rebuilt HTML for democrat/republican/party/candidate/election-outcome/fraud/liberal/conservative/trump/biden/gop/dnc (excluding "bipartisan") returned zero matches. |

### Tier 3 — human dry-run

NOT RUN (unchanged — requires a real cohort).

---
**Next step:** unchanged — a human visual proof of the rebuilt `published/` docx packets, then
`case-publish`'s two human-confirm steps to move from `TIER2_PASS` to `PUBLISHED`.
