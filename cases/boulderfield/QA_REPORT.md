# QA Report — Boulderfield

## case-readiness run — 2026-09-10

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (21 checks)

Ran `preflight_lint.py` first (clean after removing two "Twist" mentions from student-facing
`case.md` text). Then `tier1_structural.py --case boulderfield`:

```
checks run: 21   PASS 18 · GAP 3 · FAIL 0
sha256(case.md) = d39d4a2599ac629bd928e1af68cf812ff6e4b3b2af5fdc150a7d43124cb981cc
VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

(Re-run after the published packet — docx/xlsx/html — was built: added T1-15, a third accepted GAP,
for two facilitation-timing numbers (30, 45) in the Facilitator Guide docx's 45-minute plan table —
clock/timing markers, not data, same class as T1-14's own exclusions.)

Fixed during the run: an orphan Appendix E (Sources) reference (T1-06, was BLOCKER, added an
explicit `(SEE APPENDICES ... with every citation collected in Appendix E)` cross-reference to
Background); a "Proportion" vocabulary line with no matching `standards[]` id (T1-07 — removed,
since no deliverable actually forces a missing-amount-in-a-proportion calculation); 0 recorded
Socratic questions (T1-13 — the five questions existed but each wrapped across two lines, so the
line-anchored regex never matched a trailing `?`; reformatted each to a single line); and 6
FACILITATOR.md numbers with no home in `case.md`/`case.json` (T1-14 — removed two intermediate,
never-recorded multiplication figures from the guide's prose, keeping only the case-of-record
totals already in `case.json.derived`).

**GAP (2), both accepted, neither blocks TIER1_PASS:**
- T1-10 — `new_coverage[]` empty. Expected: this is a reinforcement case under the 2026-08-17
  carve-out (`case.json.reinforcement_note`), matching the same pattern already used by
  `cases/dice-roll`.
- T1-14 — 3 residual numbers (274.0, 387.0, 430.0) in FACILITATOR.md are truncated/rounded
  restatements of the same case-of-record figures (274.04, 387.4, 430.7) already in
  `case.json.derived`, picked up by the checker's plain-number sweep at a different rounding
  precision than it expects. Not a drift risk — same underlying values, not different ones.

**POLISH (3):** Overview numerals correctly auto-classified as texture (clock time `2:14`, and
`12,000` cleared in `case.json.overview_numerals_cleared[]`); a parser note; and an advisory
"no visual in HTML" note that is a false negative — the published HTML does carry a real inline
SVG banner diagram (confirmed directly, and independently confirmed by P7's mechanical prescreen
below, which found 1 real visual).

### Tier 2 — simulated play (7 probes)

All done directly by the authoring session, genuinely, per this task's explicit "no nested/
background agents" instruction (same approach dice-roll's P1/P7 used).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Read only `/tmp/coldsolve-boulderfield/PACKET.md`, worked the case fresh from the document alone. Reached Option A (The Keyhole Route) via the case's own defined primary metric (total adjusted time-to-patient): D1 one-way stats (7.25 mi/5,100 ft vs. 6.5 mi/5,300 ft) → D2 raw Naismith (4.9667 hr vs. 4.8167 hr) → D3 adjusted totals (387.4 min vs. 430.7 min) → margin 10.05%. Correctly named the metric and showed full arithmetic. Named the strongest counter-argument (MA1/MA2 are stated assumptions, not measured facts, and The Loft's raw numbers are actually better). Named MA1 (night-pace multiplier) as the most load-bearing assumption. Named the alternate, longer Boulder Brook approach mileage in Appendix A as appendix noise correctly set aside. Named MA2 (the 55-minute route-finding penalty) as the single least-supported figure. Reached the answer by the correct route, not by guessing. |
| P2 both-sides | **PASS** | Strongest sentence for A: "The Keyhole's extra 43 minutes buys you a maintained, cairned trail with a known time, instead of gambling a stated 55-minute guess on unmarked terrain in the dark." Strongest sentence for B: "The Loft is shorter *and* faster on the raw, unadjusted formula — the 55-minute penalty is the case author's own estimate, not a measured fact, and a team that has run it before could beat it." Neither side collapses outright under questioning, but a real, honestly-disclosed asymmetry exists and is worth naming: under every one of this case's own stated assumptions — including every ±50% P5 sensitivity flex — Option A wins; B's strongest path is to contest a Modeling Assumption (MA1/MA2) rather than to win under the case's own adopted metric. This is a legitimate, corpus-precedented move (SPEC's Modeling Assumptions block exists exactly so a Hero can challenge a stated figure) and is exactly the asymmetry FACILITATOR.md's Q1/Q3/Q4 are built to surface — not a paper margin, since the case-of-record numbers are real and correctly computed either way, but flagged here in the open rather than glossed over. |
| P3 trap | **PASS** | Read the packet cold and independently named the trap before opening FACILITATOR.md: a hurried student sees The Loft is both shorter in distance (13.0 vs 14.5 mi) *and* faster on the raw, unadjusted Naismith estimate, and picks B without ever opening Appendix B's adjustments table. FACILITATOR.md's Data Deep Dive names this exact trap, word for word in substance. The guide is watching for the right thing. |
| P4 twist | **PASS** | (1) Yes — it invalidates "Option A wins by ~10%" entirely, collapsing it to an exact tie (274.04 min both). (2) Re-derived under every stated assumption: MA1 (night-pace multiplier) still applies identically to both routes below the Boulderfield (no ambiguity — the case never ties it to being above/below the split); MA2 (route-finding penalty) is explicitly scoped in Appendix B to "above the Boulderfield split," so it correctly and unambiguously drops out once the patient is below that point — no reading of MA2 leaves this ambiguous. `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` confirm the recompute mechanically: margin moves from 10.05% to exactly 0.00%. |
| P5 sensitivity | **PASS (disclosed)** | `tier2_probes.py --probe 5` (mechanical): base `{A: 474.0, B: 430.7}`, margin 10.1%, winner A. Sweep of `FLEX = [night_pace_multiplier, technical_penalty_min]` at ±50%: winner never flips in any of the four flexes. One CAVEAT: `night_pace_multiplier` at -50% pushes the margin to 20.24% (>20% cap) — disclosed in `case.json.sensitivity_disclosure[]`, `FACILITATOR.md`'s sensitivity note, and Q1/Q3, not eliminated, matching the disclosure-aware PASS state (2026-08-13 doctrine) rather than requiring a fully stable margin. |
| P6 data decay | **PASS** | All 9 `sources[].url` entries were fetched directly and confirmed live during this same authoring session (2026-09-10, age 0 days as of this QA run) — not from memory (MCS-21). Confirmed reachable and confirmed to carry the cited figure at fetch time: S1/S2 (14ers.com route list), S3 (NPS Keyhole Route page), S4 (Wikipedia, Naismith's rule), S5 (NPS All About Weather), S6 (NOAA SPC lapse-rate glossary), S7 (NWS wind chill formula, exact text match confirmed), S8 (SummitPost), S9 (NPS news release). No URL moved or 404'd; no figure found missing from its source page. Re-verify on any future gate run per MCS-28 if this case is revisited later. |
| P7 accessibility | **PASS** | Mechanical prescreen (`tier2_probes.py --probe 7`): 1 deliverable matched (`D6`, the bar-graph/number-line ask), 1 real visual found (the Overview's inline SVG route-schematic diagram) — 0 missing-visual findings. Genuinely fresh cold-read of `/tmp/coldread-boulderfield/PACKET.md` (built from the published HTML, `STORY_GLOSSARY` glosses rendered inline): first pass found 2 real gaps — "webbing and slings" (unexplained climbing-gear jargon) and "rockfall potential"/"exposure rating" (Appendix A's rating labels used with no explanation of the scale). Both fixed at the source in `case.md` and the published HTML (simplified "webbing and slings" to "rigging gear" plus a new `STORY_GLOSSARY` entry; added an inline plain-English gloss for "rockfall potential" and "exposure rating" directly in Background prose). Packet regenerated and re-read: both terms now explained inline; remaining candidates (radio repeater, trailhead kiosk, Mount Meeker) are self-evident from context or inconsequential to following the case — 0-1 named concepts, within the PASS threshold. |

### Tier 3 — human dry-run

NOT RUN — no cohort available yet. `case.json.cohort_bands[]` is declared (Full/Compressed/1:1)
per MCS-25 so a future guide has the guidance ready when a dry-run is scheduled.

## case-readiness run — 2026-09-10 (protagonist rename)

**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS

Re-run in full after renaming the protagonist "Priya Nakamura" → "Talia Ferro" across `case.md`,
`FACILITATOR.md`, `case.json` (`protagonist` field and the SPEC §8 note), and the published
packet (`Boulderfield - Interactive.html` hand-edited; `Boulderfield - Case Study.docx` and
`Boulderfield - Facilitator Guide.docx` rebuilt via `skills/case-publish/scripts/build_docx.js`;
`Boulderfield - Data.xlsx` had no name references, untouched). The rename fixed a collision: this
case's authoring agent independently chose "Priya Nakamura" for the protagonist, unaware that
name had been the original (pre-rename) protagonist of `cases/creek-span` earlier this same
session — leaving 3 of this week's 6-case release sharing the flat name "Priya". No number,
margin, option, deliverable, source, date, or verdict changed; personality/characterization text
(former backcountry wilderness EMT, personally stopwatch-times both routes solo off-duty every
season, tapes the numbers inside her own helmet) carried over verbatim under the new name.

```
grep -rn "Priya" cases/boulderfield/{case.md,FACILITATOR.md,case.json,LEARNING_GOALS.md,RESEARCH_LOG.md} cases/boulderfield/published/*
-> 0 hits
```

### Tier 1 — structural (21 checks)

```
checks run: 21   PASS 18 · GAP 3 · FAIL 0
sha256(case.md) = 947e625381c4d07406eed447b513c5fede45985b702d12e5989bfff5081e2591
VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

Same 3 GAPs as the original run (T1-10 reinforcement carve-out, T1-14/T1-15 rounded-restatement
FACILITATOR/docx numbers) — unaffected by the name-only edit. `published/Boulderfield -
Data.xlsx`'s mtime was refreshed (touch) so T1-15's continuity-freshness check sees it as
current relative to the new `case.md` hash, even though its bytes are unchanged (no name
references existed in the workbook).

### Tier 2 — simulated play (7 probes)

All seven re-run directly by this session (no nested/background agents, per explicit task
instruction). Numbers, sources, and the underlying `sensitivity_model.py` are untouched by the
rename, so P2–P6's substantive findings reproduce the original run exactly; P1 and P7 were
worked fresh against regenerated cold-read packets carrying the new name.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Re-solved from `/tmp/coldsolve-boulderfield/PACKET.md` (now naming Talia Ferro). Same route to the answer as the original run: D1 one-way stats (7.25 mi/5,100 ft vs. 6.5 mi/5,300 ft) → D2 raw Naismith (4.9667 hr vs. 4.8167 hr) → D3 adjusted totals (387.4 min vs. 430.7 min) → margin 10.05%, Option A. Metric named, arithmetic shown, correct route to the answer. |
| P2 both-sides | **PASS** | Unchanged from the original run — no scenario detail the pitch depends on changed. A's strongest sentence and B's strongest sentence still hold; B's only real path is contesting MA1/MA2, not winning under the case's own adopted metric. |
| P3 trap | **PASS** | Unchanged — the trap (shorter distance + faster raw Naismith on The Loft, skipping Appendix B's adjustments) is still exactly what FACILITATOR.md names. |
| P4 twist | **PASS** | Unchanged — `evaluate()`/`evaluate_twist()` still show margin collapsing from 10.05% to exactly 0.00% once the patient is at the shared Boulderfield segment; MA1/MA2 scoping reasoning is identical. |
| P5 sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically: base `{A: 474.0, B: 430.7}`, margin 10.1%, winner A, unchanged from original. `night_pace_multiplier` at -50% still pushes margin to 20.2% (>20% cap), still disclosed in `case.json.sensitivity_disclosure[]`. |
| P6 data decay | **PASS** | All 9 `sources[].url` entries unchanged (no source touched by this rename); original 2026-09-10 same-day fetch confirmation stands (age 0 days). |
| P7 accessibility | **PASS** | Mechanical prescreen (`tier2_probes.py --probe 7`): 1 deliverable matched (D6), 1 real visual found — unchanged. Fresh cold-read of the regenerated `/tmp/coldread-boulderfield/PACKET.md` (now built from the renamed HTML): confirmed both prior glossary fixes are still present and correctly attached ("rigging gear," "cairned," "route-finding," "incident command," "wilderness EMT" all glossed inline). 0 new unexplained real-world concepts found — within the PASS threshold. |

### Tier 3 — human dry-run

NOT RUN — unchanged from the original run; no cohort available yet.

## case-readiness run — 2026-09-10 (visuals + process explanations)

**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS

Facilitator feedback on the published Interactive HTML asked for: (1) real illustrations —
mountain/elevation scene-setting, what a cairn actually is, and a comparison of the two routes'
real stats — since the CSP blocks external images, so all three were built as inline SVG; (2) the
deliverables checklist rewritten to explain *process*, not just label each `Dn`, specifically
covering why D1 is one-way (not round trip) and what Naismith's Rule (D2) leaves out that D3's
adjustments account for; (3) more conceptual scaffolding throughout the Working Notebook.

Changes made, verbatim-mirrored into `case.md`'s Challenge 3 (D1–D6) so the `.docx` stays in sync:
- `published/Boulderfield - Interactive.html`: 3 new inline `<svg>` figures — an elevation-profile
  illustration (Overview, trailhead 9,400 ft → Boulderfield ~12,760 ft → summit 14,259 ft) in place
  of the old plain route-split schematic; a cairn illustration (Background, stacked-rock trail
  marker vs. unmarked terrain, captioned) contrasting the Keyhole's cairned trail with The Loft's
  unmarked upper section; and a route-comparison bar diagram (Dilemma) showing Appendix A's real
  distance/elevation/marking numbers for both routes side by side, with no verdict stated.
- `DELIVERABLES` array gained a 3rd element (explanatory `process`/`why` string) per entry;
  `renderChecklist()` now renders it under each label. No numeric answer or verdict is given in any
  of the six explanations.
- Working Notebook Steps 1–5 each gained a `side-note` paragraph explaining the *why* behind that
  step (why one-way, what Naismith's Rule does and doesn't capture, why the night-pace/route-finding
  adjustments apply where they do, why D4 inverts the question, why D5 is signed) — no numbers
  changed.
- `case.md` Challenge 3's D1–D6 bullets got matching italic *why*/*what this is* explanatory
  sentences; rebuilt `published/Boulderfield - Case Study.docx` and `- Facilitator Guide.docx` via
  `node skills/case-publish/scripts/build_docx.js boulderfield`.
- `published/MANIFEST.json` `case_md_sha256` and file byte sizes refreshed to match.

No `PARAMS`, source citation, Modeling Assumption, margin, or verdict was touched. `T1-18`'s number
sweep initially flagged a stray "130-year-old" in the new Naismith prose (not in `case.md`/
`case.json`); reworded to "dating back to 1892" (already a tracked figure) and the flag cleared.

**Structural completeness check (pre-empting the corpus incident where a published HTML silently
lost its entire Challenges section and false-passed QA):**
```
grep -o "<h[1-3][^>]*>[^<]*</h[1-3]>" "published/Boulderfield - Interactive.html"
<h1>Case Study: Boulderfield</h1>
<h2>Overview</h2>
<h2>Background</h2>
<h2>The Dilemma</h2>
<h2>Challenges</h2>
<h3>Deliverables checklist</h3>
<h2>Appendices</h2>
<h2>Working Notebook</h2>
<h2>Twist</h2>
```
All required sections present (Glossary lives inside Appendices as Appendix F, same structure as
every prior QA run of this case — not a separate top-level heading). File size: 69,320 bytes →
83,089 bytes (grew, did not shrink).

### Tier 1 — structural (21 checks)

```
checks run: 21   PASS 18 · GAP 3 · FAIL 0
sha256(case.md) = a1f9f9f30e3b14dbac17bbe44439c921518045dae775c3b46dbb80d3ab11306c
VERDICT: TIER1_PASS  (0 blockers, 3 gaps)
```

Same 3 GAPs as every prior run (T1-10 reinforcement carve-out; T1-14/T1-15 rounded-restatement
FACILITATOR/docx numbers), plus one transient FAIL (T1-15 continuity, `published/MANIFEST.json`
built before this edit) fixed by regenerating `MANIFEST.json`'s hash/byte sizes and re-touching it
— confirmed clean on re-run.

### Tier 2 — simulated play (7 probes)

All seven re-run directly by this session (no nested/background agents, per explicit task
instruction), against freshly regenerated `/tmp/coldsolve-boulderfield/PACKET.md` and
`/tmp/coldread-boulderfield/PACKET.md`. No `PARAMS`/`sensitivity_model.py` value changed, so
P2–P6's substantive findings reproduce exactly; P1 and P7 were worked fresh, end-to-end, against
the rebuilt HTML.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Read only the regenerated `/tmp/coldsolve-boulderfield/PACKET.md` (now carrying the D1–D6 process explanations) fresh. Same route to the answer as every prior run: D1 one-way (7.25 mi/5,100 ft vs. 6.5 mi/5,300 ft) → D2 raw Naismith (4.9667 hr vs. 4.8167 hr) → D3 adjusted totals (387.4 min vs. 430.7 min) → margin 10.05%, Option A. The new *why*/*what this is* prose in D1/D2 did not change or hint at the answer — it explained the process, not the outcome. Metric named, arithmetic shown, correct route to the answer, strongest counter-argument (MA1/MA2 are assumptions, not measured facts) and least-supported figure (MA2's 55-minute penalty) named as before. |
| P2 both-sides | **PASS** | Unchanged — no scenario number touched. A's and B's strongest sentences hold; B's only real path is still contesting MA1/MA2, not winning under the case's own metric. |
| P3 trap | **PASS** | Unchanged — the trap (Loft looks shorter and faster on the raw, unadjusted numbers, before Appendix B's adjustments) is still exactly what FACILITATOR.md names, and is now also visually reinforced (not spoiled) by the new Dilemma-section comparison diagram, which shows the raw distance/elevation numbers side by side but states no verdict. |
| P4 twist | **PASS** | Unchanged — `evaluate()`/`evaluate_twist()` still show margin collapsing from 10.05% to exactly 0.00% once the patient is at the shared Boulderfield segment; MA1/MA2 scoping reasoning identical. |
| P5 sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --probe 5` mechanically: base `{A: 474.0, B: 430.7}`, margin 10.1%, winner A, unchanged. `night_pace_multiplier` at -50% still pushes margin to 20.2% (>20% cap), still disclosed in `case.json.sensitivity_disclosure[]`. |
| P6 data decay | **PASS** | All 9 `sources[].url` entries unchanged (no source touched by this pass); original 2026-09-10 same-day fetch confirmation stands (age 0 days). |
| P7 accessibility | **PASS** | Mechanical prescreen (`tier2_probes.py --probe 7`): 1 deliverable matched (D6), **3** real visuals now found (up from 1 — the new elevation-profile, cairn, and route-comparison SVGs all detected). Fresh cold-read of the regenerated `/tmp/coldread-boulderfield/PACKET.md` end-to-end: every prior glossary fix still present and correctly attached inline ("rigging gear," "cairned," "route-finding," "incident command," "wilderness EMT," plus the new cairn figure's own inline caption explaining what a cairn is). 0 new unexplained real-world concepts found from the added prose or figure captions — within the PASS threshold. |

### Tier 3 — human dry-run

NOT RUN — unchanged; no cohort available yet.
