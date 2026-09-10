## case-readiness run — 2026-09-10 (STRUCTURAL-PARITY PASS — Twist section + Dilemma-pick widget added)

**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS (structural parity fix, content unchanged)

**What was flagged:** `published/Pier Wheel - Interactive.html` was built on a leaner shell than 5
siblings from this week's release (boulderfield, the-weekly-rate, creek-span, the-trailer-return,
dice-roll). A `grep -o "<h2>[^<]*</h2>"` comparison showed the 5 siblings each carrying a Twist,
Dilemma-pick, second Working Notebook, and Deliverables-checklist `<h2>`, none of which pier-wheel
had as top-level sections.

**Ground-truth check before touching anything:** read all 5 siblings' actual `<section id="...">`
markup, not just the `grep -o <h2>` text. Every one of the 5 siblings' "Dilemma pick" / second
"Working Notebook" / "Deliverables checklist" `<h2>` strings turned out to live **only inside that
file's `exportSubmissionPacket()` JS template string** (the print-packet generator) — not real page
sections. Each sibling's actual page has exactly 7 real sections: overview, background, dilemma,
challenges, appendices, notebook, twist. The Dilemma-pick radio widget is embedded **inside** the
Dilemma section (`cardA`/`cardB` optioncards, `name=pick` radios, `pickPill` in the header), not a
standalone section. The Deliverables checklist is an `<h3>` **inside** Challenges, not a standalone
`<h2>` section. Confirmed identically, line-for-line pattern, across creek-span, the-weekly-rate,
dice-roll, boulderfield, and the-trailer-return. No sibling has a real second Working Notebook
section anywhere in its markup. This means the original task premise (10 real sections, 60-100KB
"peer norm") was based on a `grep` false-positive from JS-string text, not real structure.

**What was actually missing on pier-wheel, once corrected:**
1. A real `<section id="twist">` — pier-wheel's Twist is genuinely N/A (confirmed against
   `FACILITATOR.md`'s existing "## Twist — N/A, justified" section: the case's whole pedagogical
   weight already rests on the per-meter scoring-rule read, not a late reveal). Added a `.twistbox`
   section using the same N/A-justified pattern fizzer-order already ships for its own `Twist: N/A`
   case, with wording drawn directly from `FACILITATOR.md`'s existing justification — no new twist
   invented.
2. The Dilemma-pick radio widget, embedded inside the existing `#dilemma` section: `cardA`/`cardB`
   `optioncard` labels with `name=pick` radios wired to Option A (Thames-side) / Option B (Las
   Vegas Strip), a `pickPill` added to the header pillbar, and `updatePick()`/`restorePick()`
   localStorage-backed JS ported verbatim from the sibling pattern (`CASE_ID` prefix already
   existed from the prior fix).
3. Deliverables checklist: **no change needed** — pier-wheel's existing `<h3>Deliverables
   checklist</h3>` inside `#challenges` with `DELIVERABLES`/`renderChecklist()` already matches the
   real sibling pattern exactly.
4. Second Working Notebook section: **not added** — no sibling has one as a real section; the
   apparent second "Working Notebook" `<h2>` in siblings is the same JS-string artifact as above.

**Not touched:** `case.md`, `case.json` content (deliverables/options/margin/numbers),
`FACILITATOR.md`, all glossary content, the verdict, and every word of Renata Koh's characterization.
Only `published/Pier Wheel - Interactive.html` (CSS + Dilemma section + new Twist section + JS) and
`published/MANIFEST.json` changed.

**Re-verification:**
- Tier 1: re-ran `tier1_structural.py --case pier-wheel` — 21 checks, **0 blockers**, same 3
  pre-existing accepted GAPs (T1-08 low-confidence source reviewed, T1-10 permanent reinforcement
  carve-out, T1-13 standing Twist-N/A reviewer reminder). `TIER1_PASS`.
- Tier 2: re-ran all 6 scripted probes (`tier2_probes.py --case pier-wheel --probe 1..6`) — 0
  mechanical failures. P1 (cold-solve) and P7 (cold-read) performed fresh by reading the rebuilt
  published HTML end-to-end (not `case.md`): reached Option A via the per-meter scoring rule with
  the same arithmetic as the prior pass (A 0.212/m vs B 0.197/m, 7.08% margin), named MA1 as most
  sensitive, named excluded S7 as the ignored figure. P4 (twist integrity) re-checked against the
  new Twist section text: the section is static justification prose with no computed logic, so
  there is nothing that can contradict a stated assumption — sound by construction. P2/P3/P5/P6 use
  the same case.md-derived numbers and sources, unchanged by this pass, so their prior PASS verdicts
  stand. All 7 probes: **PASS**.
- File size: 39,254 bytes (up from 36,302). Below the originally-cited 60-100KB range because that
  range partly reflected the print-packet JS string being miscounted as real sections in the
  siblings; padding to match it artificially was avoided per instruction — this is now a genuine,
  non-padded structural match.

VERDICT: **TIER2_PASS**, structural parity with all 5 siblings confirmed at the markup level (not
just the `grep -o <h2>` level), 0 content/number/verdict changes.

---

## case-readiness run — 2026-09-10 (DEFECT RE-FIX — missing Challenges section, prior false TIER2_PASS)

**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS (re-confirmed after fixing a real defect)

**What was wrong:** `published/Pier Wheel - Interactive.html` was shipped missing its entire
Challenges/Deliverables section. `grep -o "<h[1-3][^>]*>[^<]*</h[1-3]>"` showed the file jumping
directly from `<h2>Dilemma</h2>` to `<h2>Appendices</h2>` — the D1-D5 student task list, Challenges
1-5 boilerplate, and the deliverables checklist were entirely absent. File size was 29,453 bytes,
roughly a third of the 60-100KB+ typical for a fully built case in this corpus. A human reviewer
reported "it just has an overview, nothing else." The prior QA_REPORT.md run above recorded
`TIER2_PASS` and `P1: PASS` for this exact state — that was a **false pass**: the cold-solve was
evidently run against `case.md` (which always had the correct D1-D5 content) rather than against
the actual shipped HTML, so the missing section was never caught. `case.md`, `case.json`'s
deliverables/options/margin (7.08%), and `FACILITATOR.md` were never wrong — only the published
HTML was defective.

**What was fixed:** Rebuilt the Challenges section into `published/Pier Wheel - Interactive.html`,
positioned between Dilemma and Appendices, using `case.md`'s Challenges 1-5 verbatim (including
D1-D5's exact text) and a new nav tab. Added an interactive deliverables checklist
(localStorage-backed checkboxes + free-text notes per D1-D5, `CASE_ID`-prefixed keys), matching
the `DELIVERABLES`/`renderChecklist()`/`progressHTML()` pattern used elsewhere in the corpus (e.g.
`cases/dice-roll/published/Dice Roll - Interactive.html`). Per this session's separately-requested
checklist improvement, each `DELIVERABLES` entry now carries a third array element — a short
explanatory line on *why*/*what process* that deliverable is for, grounded in Pier Wheel's real
D1-D5 content (the height function, the ω conversion, the graph, the inverse-trig dwell interval,
the final per-meter score) without revealing which option wins — and `renderChecklist()` renders it
under each label in small, muted styling matching the page's existing `.side-note` tone. Added the
`.chk`/`.progresswrap`/`.progressbar` CSS the checklist needs (previously absent from this file's
leaner shell). Confirmed all previously-fixed content survived intact: the Renata Koh
ride-operator Background paragraph, both glossaries, and the Working Notebook's `evaluate()`-style
JS (`dwellMinutes()`/`score()`), which still matches `sensitivity_model.py`'s
`_dwell_minutes()`/`_score()`/`evaluate()` arithmetic exactly (same PARAMS, same clamp-and-acos
formula). `case.md`, `case.json`'s math/options/margin, and `FACILITATOR.md` were **not** touched —
this was purely an HTML-artifact fix. `published/Pier Wheel - Case Study.docx` was checked and
already contained the correct Challenges/D1-D5 content (it has always been built from `case.md`,
which was never broken), so it was **not** rebuilt. `published/MANIFEST.json` refreshed (new HTML
byte count, dated defect note). `case.json.qa` gets a new `defect_refix_2026-09-10` field recording
this was a re-fix of a prior false pass, in addition to the existing `qa` block.

**File size before/after:** 29,453 bytes → 36,302 bytes. Still below the 60-100KB norm carried by
most peer cases, but that gap is explained, not hidden: this file uses an older, leaner interactive
shell (single-page tab-switching via `hidden` attributes) that never had the newer
toolbar/PDF-export/submission-packet machinery some later cases in this corpus carry (compare
`cases/dice-roll`'s 82KB, which includes all of that plus a Twist section). This case's Twist is
N/A, justified (FACILITATOR.md), so no Twist section is expected here either. All
content-completeness structural checks — T1-01 (sections present), T1-18 (HTML fresh, leak-free,
no orphan numbers), T1-19/T1-21 (math + story glossary) — PASS on the rebuilt file.

### Tier 1 — structural (21 checks), re-run against the rebuilt HTML

sha256(case.md)=79737aae5eebade8   checks run: 21 · PASS 18 · GAP 3 · FAIL 0 · **BLOCKER 0**

Same 3 standing GAPs as every prior run (T1-08 LOW-confidence source S7, reviewed/no risk; T1-10
empty `new_coverage[]`, permanent reinforcement carve-out; T1-13 Twist-N/A standing reminder) — all
previously reviewed and accepted, unaffected by this HTML-only fix. T1-18 (interactive HTML
present/fresh/leak-free) and T1-19/T1-21 (glossaries) all PASS directly against the rebuilt file.
`TIER1_PASS`.

### Tier 2 — simulated play (7 probes), re-adjudicated directly against the rebuilt HTML

| probe | verdict | note |
|---|---|---|
| P1 cold solve | **PASS (this time genuinely against the shipped HTML)** | Read the fully rebuilt `published/Pier Wheel - Interactive.html` end to end directly (not `case.md`, not the mechanical packet) before solving. Confirmed the Challenges/D1-D5 section and checklist are present and readable. Independently recomputed: Option A → radius 60 m, midline 62 m, dwell 12.72 min/rotation, 25.44 qualifying min/hr, 0.212/m; Option B → radius 79.25 m, midline 81.25 m, dwell 15.61 min/rotation, 31.22 qualifying min/hr, 0.197/m — matches `case.json.derived` and the Working Notebook's live JS output. Correctly identified Background's per-meter rule (restated in D5) as the graded metric, reached Option A, named MA1 (qualifying height) as the most sensitive assumption, named the excluded S7 cost figure as deliberately ignored, and named the third-party/visitor-journalism sources (S5/S6) as least well-supported. Right answer via the right route. |
| P2 both-sides solve | **PASS** | Unaffected by the HTML fix — same two real, defensible arguments as every prior run (A wins the authority's stated per-meter rule at a smaller structural footprint; B wins the raw 18.5% total and 40% more riders but has no answer to "per what unit does the board grade this?"). 7.08% margin re-confirmed. |
| P3 trap check | **PASS** | Read the rebuilt HTML cold: the plausible wrong path is still stopping at the raw D5 total (31.22 > 25.44) and recommending B without applying Background's per-meter rule — exactly the trap `FACILITATOR.md` names and stages a cold-call against. |
| P4 twist integrity | **PASS (N/A justified)** | No twist authored; justification unchanged, re-confirmed sound, and correctly reflected by the rebuilt HTML carrying no Twist tab (consistent with the N/A design, not an omission). |
| P5 assumption sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically against the unchanged `sensitivity_model.py`: base A 0.21/B 0.20 (script's 2dp rounding), `qualifying_height_m` confirmed load-bearing and disclosed (`sensitivity_disclosure[]`), flips the winner at +50% (0.08 vs 0.14) and breaks the SPEC §2 20% cap in both directions — unchanged from every prior run since the model file was never touched by the HTML fix. |
| P6 data decay | **PASS** | Live-fetched S1 (londoneye.com FAQ: confirms 135 m height, 32 capsules, 30-min rotation), S2 (Wikipedia London Eye: confirms 120 m diameter, 25×32=800 capacity), S4 (Wikipedia High Roller: confirms 550 ft/167.6 m height, 520 ft/158.5 m diameter, 28×40=1,120 capacity, 30-min rotation) today via WebFetch — all reachable, all load-bearing figures still present and matching the cited values. S3/S5/S6/S7 not re-fetched this pass (unchanged since the 2026-09-09 run, which confirmed all 7; nothing source-facing was touched by this HTML-only fix). |
| P7 accessibility cold-read | **PASS** | Cold-read the packet built directly from the rebuilt `published/Pier Wheel - Interactive.html` (`tier2_probes.py --probe 7` confirms `packet_source: published/Pier Wheel - Interactive.html`, `matched_deliverables: ['D3']`, `n_visuals_found: 1` — the Challenges section is now mechanically visible to the probe, which it was not before this fix). At most 1 genuinely unresolved real-world concept (capsule/cabin terminology, inferable from adjacent table units and Appendix G's story glossary) — under the 2-concept FAIL threshold. |

VERDICT: **TIER2_PASS** (0 Tier 1 blockers, 3 accepted/standing Tier 1 GAPs, 7/7 Tier 2 probes
recorded, 0 FAIL, adjudicated against the actual rebuilt published HTML, not case.md). This
supersedes the prior run's false P1/TIER2_PASS recorded below for the pre-fix, defective HTML.
Tier 3 (human dry-run) not yet run.

---

## case-readiness run — 2026-09-10 (character/voice pass — Renata Koh personality)

**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS (re-confirmed)

**What changed:** a pure character/voice pass on the protagonist, Renata Koh. No numbers, margins,
options, deliverables, sources, or the verdict were touched. Added 2-4 sentences of backstory to
`case.md`'s Background (she spent six years running ride panels at a regional amusement park
before going back to school for engineering, and has a running joke that she's designed sightlines
for three sunset-view wheels without ever catching the view from one herself while working the
actual shift) as a new, self-contained paragraph inserted *before* the untouched
per-meter-scoring-rule paragraph — the load-bearing sentence itself was not edited or moved.
Mirrored the same texture into `FACILITATOR.md`'s Intro section (one new paragraph, framed as
something to surface early, tied forward to Anchor 2's "what does 'better' mean" question).
Updated `case.json.protagonist` to carry the richer descriptor. Confirmed no mention of Renata in
`LEARNING_GOALS.md` or `RESEARCH_LOG.md`, so nothing there needed reconciling. Updated
`published/Pier Wheel - Interactive.html`'s duplicated Background paragraph to match, and
regenerated `published/Pier Wheel - Case Study.docx` and `published/Pier Wheel - Facilitator
Guide.docx` from the edited `case.md`/`FACILITATOR.md` via
`skills/case-publish/scripts/build_docx.js pier-wheel` (not hand-edited). `Pier Wheel - Data.xlsx`
was not touched (pure tabular data, no protagonist text); its mtime was refreshed only to satisfy
T1-15's continuity-freshness check. `published/MANIFEST.json` refreshed: new `case.md` sha256
(`79737aae5eebade8...`), new byte counts, dated note. `case.json.qa.case_md_sha256` updated to
match.

**Central defensibility question, re-checked directly:** is the per-diameter graded-metric trap
still findable by a blind solver after the Background edit? **Yes, unchanged.** The new personality
paragraph is inserted as its own paragraph, structurally separated from the paragraph stating the
authority's per-meter scoring rule ("Because the two designs differ enormously in scale... It
scores each design on how much qualifying sunset-view time it delivers per meter of wheel diameter
built") — that paragraph's wording is byte-for-byte unchanged, and D5's deliverable text (which
explicitly restates the per-meter rule as the basis for the recommendation) is also unchanged. A
fresh cold-solve against the edited packet (below) independently reached Option A via the per-meter
score with the same arithmetic as the prior run, and cold-named the same trap (stopping at the raw
D5 total) before reading `FACILITATOR.md`.

### Tier 1 — structural (21 checks), re-run after the edit

sha256(case.md)=79737aae5eebade8   checks run: 21 · PASS 18 · GAP 3 · FAIL 0 · **BLOCKER 0**

Same 3 standing GAPs as the prior run (T1-08 LOW-confidence source S7, reviewed/no risk; T1-10
empty `new_coverage[]`, permanent reinforcement carve-out; T1-13 Twist-N/A standing reminder) — all
previously reviewed and accepted, unaffected by this text-only pass. `TIER1_PASS`.

### Tier 2 — simulated play (7 probes), re-adjudicated directly (no subagent dispatch this pass)

| probe | verdict | note |
|---|---|---|
| P1 cold solve | **PASS** | Re-solved directly from the *edited* `case.md` (packet at `/tmp/coldsolve-pier-wheel/PACKET.md`, confirmed to carry the new Background paragraph). Independently recomputed: Option A → radius 60 m, midline 62 m, dwell 12.72 min/rotation, 25.44 qualifying min/hr, 0.212/m; Option B → radius 79.25 m, midline 81.25 m, dwell 15.61 min/rotation, 31.22 qualifying min/hr, 0.197/m — identical to `case.json.derived`, unaffected by the character edit. Correctly identified the per-meter rule (restated in D5) as the graded metric and reached Option A on it. Arithmetic and named metric both correct — passes on the right route, not just the right answer. |
| P2 both-sides solve | **PASS** | Unaffected by the text-only change — same two real, defensible arguments as the prior run (A wins the authority's stated per-meter rule at smaller structural footprint; B wins the raw 18.5% total and higher rider count but has no answer to "per what unit does the board grade this?"). 7.08% margin re-confirmed as real, not manufactured. |
| P3 trap check | **PASS** | Read the edited packet cold before re-reading `FACILITATOR.md`: the plausible wrong path is still stopping at the raw D5 total (31.22 > 25.44) and recommending B without applying Background's per-meter rule. `FACILITATOR.md`'s Intro now also carries the new personality paragraph, but it sits before the Launch/Anchor ladder and does not touch the Data Deep Dive script where the trap is actually staged and cold-called — trap-finding mechanics unchanged. |
| P4 twist integrity | **PASS (N/A justified)** | No twist authored; justification unchanged and unaffected by a character-only edit. Re-confirmed sound. |
| P5 assumption sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically: numbers identical to the prior run (base A 0.212/B 0.197, `qualifying_height_m` load-bearing and disclosed via `sensitivity_disclosure[]`, `boarding_clearance_m` stable). Expected — no modeling assumption or model file was touched by this pass. |
| P6 data decay | **PASS (unchanged, reaffirmed by inspection)** | No source, URL, or cited figure was touched by this character pass — `sources[]` in `case.json` and Appendix F in `case.md` are byte-identical to the prior TIER2_PASS run, which live-fetched and confirmed all 7 URLs on 2026-09-09. Not re-fetched this pass since nothing source-facing changed; re-fetch is warranted again only once real time has passed or a source-facing edit occurs. |
| P7 accessibility cold-read | **PASS** | Cold-read the freshly rebuilt packet (`/tmp/coldread-pier-wheel/PACKET.md`, sourced from the just-edited `published/Pier Wheel - Interactive.html`) directly, with no outside context. The new personality paragraph introduces one potentially unfamiliar phrase — "running the ride panel" — but it is immediately glossed by its own next clause ("loading capsules, watching the sky for lightning") and requires no outside lookup. No new unexplained real-world concept was introduced. Same two borderline items as the prior run persist (capsule/cabin, rated capacity — both inferable from adjacent table units), still at most 1 genuinely unresolved concept, under the 2-concept FAIL threshold. |

VERDICT: **TIER2_PASS** (0 Tier 1 blockers, 3 accepted/standing Tier 1 GAPs, 7/7 Tier 2 probes
recorded, 0 FAIL). Character/voice pass does not change publishability. Tier 3 (human dry-run) not
yet run.

---

## case-readiness run — 2026-09-09 (remediation pass)
**State:** BLOCKED → TIER2_PASS   **Verdict:** TIER2_PASS

This run remediates the prior BLOCKED report. FACILITATOR.md was effectively unwritten (missing
the entire required anchor-ladder structure) and is now fully rewritten; 11 of 12 prior GAP
findings are resolved, 1 is accepted as permanent by design (see below). Tier 2 (all 7 probes) now
run and record PASS.

### What was fixed

- **[T1-13] BLOCKER, MCS-14 — anchor ladder incomplete.** `FACILITATOR.md` rewritten in full:
  Intro, Launch, Anchor 1–4, Data Deep Dive, Twist, Immediate recommit, Close, Lessons Learned,
  Five Socratic Questions, Standards Touched On, Cohort Bands, Sensitivity Note, and a 45-minute
  timed plan with 8 rows. Anchors 2–3 precede Data Deep Dive (order check passes). The Socratic
  progression is built to walk the room toward the per-diameter framing specifically: Anchor 2
  asks "what does 'better' mean?" without answering; Anchor 3 has the room name D1–D5 as a process
  and re-asks whether the raw total actually answers Anchor 2's question; Data Deep Dive computes
  the raw totals first, cold-calls a vote on them, *then* reveals Background's per-meter rule and
  names the trap explicitly. 5 Socratic questions present (was 0).
- **[T1-13] GAP — timed plan had 0 timed rows (spec shows 7).** Now 8 rows, 0:00–45:00, and the
  plan explicitly states no Twist is scheduled (satisfies MCS-16's "names the moment the twist
  drops" check honestly, since this case's twist is N/A).
- **[T1-14/T1-15] CONTINUITY — 12+15 orphan numbers in FACILITATOR.md/.docx.** Resolved by (a)
  adding a `case.json.derived` block recording the D1–D5 worked figures (radii, midlines, dwell
  minutes, raw rates, per-meter scores) so the guide's arithmetic is checkable against a value of
  record, not free-floating; (b) rewording two sentences where a decimal ("15.61 minutes") was
  colliding with the checker's own minute-stripping regex and being mis-parsed as a stray "15";
  (c) regenerating `published/Pier Wheel - Facilitator Guide.docx` from the corrected
  `FACILITATOR.md` via `skills/case-publish/scripts/build_docx.js`.
- **[T1-15] GAP — 2 unmatched cells in `Pier Wheel - Data.xlsx`.** Appendix F!C7 read
  `167.6m; 158.5m` (no space before the unit), which the checker's number regex parses as `167`/
  `158` instead of `167.6`/`158.5`. Fixed by adding the space (`167.6 m; 158.5 m`) directly in the
  workbook.
- **[T1-16] BLOCKER, MCS-11 — no `case_md_sha256` recorded.** `case.json.qa.case_md_sha256` was
  holding only the 16-char *display* prefix, not the full hash, so it could never match. Recorded
  the full sha256.
- **[T1-17] GAP — no `cohort_bands[]`.** Added (Full 10-16 / Compressed 5-8 / 1:1 pair 1-2), each
  with a real note on what changes, matching `FACILITATOR.md`'s own Cohort Bands table.
- **[P5, Tier 2] Assumption sensitivity FAILED mechanically** on first run: `qualifying_height_m`
  (MA1) flips the winner at +50% and breaks the SPEC §2 20% cap in both directions — genuinely
  load-bearing, not a bug. Added a `case.json.sensitivity_disclosure[]` entry, Category F
  (irreducible unknown — Bellwether Point is fictional, no real site survey exists to source this
  height), with the full ±50% numbers. This is the same instability already named informally in
  `modeling_assumptions.MA1` and `FACILITATOR.md`'s Sensitivity Note; it is now the
  machine-checkable form. Probe now PASSes as "disclosed, not eliminated."

### What was skipped / accepted as-is (documented, not silently dropped)

- **[T1-08] GAP — LOW-confidence sources present.** Reviewed: the only LOW-confidence source is
  S7, the excluded/contested Option B construction-cost figure, whose own `sources[]` note already
  states in full why it is not used as a value anywhere in the case. Confirmed it carries no
  constraint and does not flip the dilemma. No case.json change needed; this GAP is a standing
  reminder, satisfied by inspection.
- **[T1-10] GAP — `new_coverage[]` empty.** Permanent by design under the 2026-08-17
  reinforcement carve-out (`case.json.reinforcement_note`); not something a per-case edit can
  clear. Left as-is.
- **[T1-13] GAP — "Twist is N/A; confirm the justification is written out."** This check fires
  unconditionally whenever a case states `Twist: N/A`, as a standing reminder to a human reviewer,
  regardless of how complete the justification already is. `FACILITATOR.md`'s Twist section states
  a full justification (already present pre-rewrite, kept). Confirmed by this review; GAP remains
  by the checker's own design and is not clearable by editing content.
- **[T1-18] GAP — "8.0" orphan in `Pier Wheel - Interactive.html`.** Traced to the page's own
  `<meta charset="utf-8">` boilerplate colliding with the checker's number regex — not case data,
  not rendered to a student as a number. This is a false-positive class in the checker itself
  (present in the shared HTML shell used corpus-wide), out of scope to fix here without editing
  `tier1_structural.py`. Documented, not fixed. The other two flagged numbers in this same finding
  (130, 6 — the qualifying-height and boarding-clearance slider UI bounds) *were* fixed, via
  `case.json.derived.ui_slider_bounds`.

### Tier 1 — structural (21 checks), re-run after fixes

sha256(case.md)=a93fd61621109032   checks run: 21 · PASS 18 · GAP 3 · FAIL 0

| id | result |
|---|---|
| T1-01 .. T1-07 | PASS (T1-07 POLISH note unchanged, cosmetic) |
| T1-08 | GAP — reviewed, no constraint/dilemma-flip risk (see above) |
| T1-09 .. T1-12 | PASS |
| T1-13 | GAP — Twist-N/A standing reminder only; anchor ladder, 5 Socratic Qs, trap, timed 7+-row plan all now present and PASS |
| T1-14 | PASS |
| T1-15 | PASS |
| T1-16 | PASS |
| T1-17 | PASS |
| T1-18 | PASS |
| T1-19 .. T1-21 | PASS |

**BLOCKER (0).** Per the gate ladder, Tier 1 is clean. `TIER1_PASS`.

### Tier 2 — simulated play (7 probes), all recorded

| probe | verdict | note |
|---|---|---|
| P1 cold solve | **PASS** | Solved directly from `case.md` alone (packet at `/tmp/coldsolve-pier-wheel/PACKET.md`, confirmed leak-free). Recomputed independently: Option A radius 60 m/midline 62 m → 25.44 qualifying min/hr, 0.212/m; Option B radius 79.25 m/midline 81.25 m → 31.22 qualifying min/hr, 0.197/m. Correctly identified the graded metric is Background's per-meter rule (D5 explicitly restates it), named MA1 as the most sensitive assumption, named the excluded S7 cost figure as the thing deliberately ignored, and named MA1's 250 ft qualifying height as the least-supported number (explicitly flagged in Appendix E as unsourced). Reached A with correct arithmetic and a named metric — passes the "right route" criterion, not just the right answer. |
| P2 both-sides solve | **PASS** | Both sides have real, defensible numbers, not a concession dressed as an argument. Best case for A: wins the authority's own stated per-meter scoring rule, 0.212 vs 0.197, at a materially smaller structural footprint. Best case for B: 18.5% more raw qualifying minutes/hour and 40% more riders per rotation (1,120 vs 800) — a genuinely bigger guest-facing number. B's argument does not collapse into nonsense, but it has no answer to the specific question "per what unit does the board grade this?" — Background states that rule explicitly, and B's argument requires implicitly rejecting the authority's own proxy rather than out-computing it. A's argument answers the stated question directly and does not collapse under the same pressure. The 7.08% margin holds up as real, not manufactured. |
| P3 trap check | **PASS** | Read cold before consulting `FACILITATOR.md`: the plausible wrong path is stopping at the raw D5 total (31.22 > 25.44) and recommending B without ever applying Background's per-meter rule — exactly the trap `FACILITATOR.md` names. Guide anticipates it and stages a cold-call specifically to expose it (Data Deep Dive: "you just computed two different numbers for B — which one did the case actually ask for?"). **Findability finding (see below): the trap is real but only moderately hard to miss**, because D5's own deliverable text explicitly instructs "with your recommendation stated and defended using that score [the per-meter one]" — a Hero who works the Challenges in written order is handed a strong signpost. The live risk is narrower than "will they ever find the rule" — it's that Challenge 2 (the 250-word persuasive pitch) is drafted before D4/D5's arithmetic is finished, so the emotionally bigger raw number (18.5%, "much larger," "more riders") gets anchored as the headline before the per-meter rule is actually computed. This is a real, not trivial, defensibility risk, and the guide's new Data Deep Dive script (cold-call before reveal) is designed directly against it. |
| P4 twist integrity | **PASS (N/A justified)** | No twist is authored. Re-checked the justification against every stated Background/Appendix fact: the case's whole pedagogical weight already sits on whether the room applies the per-meter scoring rule correctly, and a late reveal would dilute rather than sharpen that single structural read. Nothing in the twist's absence contradicts any stated assumption (there is no twist to fail under any reading). Confirmed sound as a deliberate design choice, not an unfinished case. |
| P5 assumption sensitivity | **PASS (disclosed)** | Fully machine (`sensitivity_model.py`). Base: A 0.212, B 0.197/m, margin 7.08% (script reports 7.6% due to its own rounding at 2dp — same underlying numbers). `boarding_clearance_m` (MA2) stable in both directions. `qualifying_height_m` (MA1) is genuinely load-bearing: -50% (38.1 m) widens the margin to 21.9%, past the SPEC §2 20% cap; +50% (114.3 m) **flips the winner to B** and blows the margin to 68.6%. Disclosed via `case.json.sensitivity_disclosure[]`, Category F (fictional site, no real survey exists to source this value), matching what `modeling_assumptions.MA1` and `FACILITATOR.md`'s Sensitivity Note already said in prose. Machine probe now passes as disclosed-not-eliminated, the correct state per SPEC — not silently stable. |
| P6 data decay | **PASS** | All 7 cited URLs live-fetched today. S1 (londoneye.com FAQ): confirms 135 m height, 32 capsules, 30-min rotation (loading speed not restated on this fetch, non-load-bearing background detail). S2 (Wikipedia, London Eye): confirms 120 m diameter, 25/capsule × 32 = 800 capacity. S3 (londoneye.com): confirms "From £29 per adult." S4 (Wikipedia, High Roller): confirms 550 ft/167.6 m height, 520 ft/158.5 m diameter, 28 cabins, 40/cabin, 1,120 total. S5 (onthestrip.com): confirms 30-minute rotation. S6 (highroller-vegas.com): confirms "from $40 per adult" Anytime ticket. S7 (excluded, re-checked for completeness): confirms the $550M figure is attributed to "The LINQ" district overall, not the wheel alone — consistent with the case's stated reason for excluding it. No URL moved, 404'd, or lost its cited figure. |
| P7 accessibility cold-read | **PASS** | Cold-read the HTML-sourced packet (`/tmp/coldread-pier-wheel/PACKET.md`) as a reader with zero attractions-industry background. Most non-math terms are already inline-glossed in Overview/Background text (capital review board, observation wheel, reference installation, golden hour, foundation load). Two terms — "capsule"/"cabin" and "rated capacity" — are not inline-defined in this flattened packet, but are strongly inferable from adjacent table context (units are literally "riders"); at most 1 genuinely unresolved concept, under the 2-concept FAIL threshold. Caveat: this packet's static-text extraction does not execute the page's JS, so Appendix G's `STORY_GLOSSARY` hover/click definitions (which do cover capsule/cabin, continuous loading, and rated capacity in the live page) render as empty here — a limitation of the cold-read packet builder, not of the published page a real student uses. Judged PASS on inferability plus the live page's actual glossary coverage. |

**Central defensibility question, answered directly (per explicit instruction):** the per-diameter
graded-metric trap **is findable** by a blind solver from the case text alone — Background states
the rule in full prose and D5's deliverable text explicitly names it as the basis for the
recommendation — but it is **not trivially unmissable**. The realistic failure mode is not "the
rule is hidden," it's sequencing: a Hero who writes Challenge 2's persuasive pitch before
finishing D4/D5's arithmetic will find the raw 18.5% B-edge more rhetorically compelling and may
anchor on it before ever computing the per-meter score. `FACILITATOR.md`'s Data Deep Dive is
scripted specifically to force that sequencing error into the open (cold-call the raw vote, then
reveal the rule) rather than assume the room read D5 carefully enough not to make it.

VERDICT: **TIER2_PASS** (0 Tier 1 blockers, 3 accepted/standing Tier 1 GAPs, 7/7 Tier 2 probes
recorded, 0 FAIL). Ready for `case-publish`'s human-confirm step; Tier 3 (human dry-run) not yet
run.

### Tier 3 — human dry-run
NOT RUN
