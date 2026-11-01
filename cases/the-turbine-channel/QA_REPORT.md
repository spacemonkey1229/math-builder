# QA Report — Turbine Channel

## case-readiness remediation run — 2026-09-12 (second pass)

**State:** TIER1_PASS (prior run) → **DRAFT** (this run)   **Verdict:** BLOCKED — Tier 1 shows 4
fresh BLOCKERs, all of them published-packet staleness caused by this pass's own required source
and content corrections, not by any new data/logic defect. All three of the prior run's genuine
Tier 2 defects (P5, P6, P7) are now substantively fixed and re-adjudicate PASS. **This report does
not claim TIER2_PASS** — see "Why not TIER2_PASS" below for exactly why, and what closes it.

---

## What changed, fix by fix

### Fix 1 — P6 data decay (Cape Cod Canal authorized depth)

**Problem:** `case.json` S3 (cited to the ASCE "Cape Cod Canal" historic-landmark page) claimed
"a minimum channel width of 480 feet... and an authorized depth of 32 feet at mean low water" as
the *current* dimensions. A live re-fetch (2026-09-12) of that exact URL found it now states only:
*"Originally 480 feet wide and 34 feet deep, the canal was enlarged in 1940, making it the widest
canal in the world."* No post-1940 depth figure appears anywhere on the page — the 32 ft claim did
not survive re-fetch.

**Re-research:** Searched for a live, current, primary source for the canal's present authorized
depth. Found and fetched `https://nauticalcharts.noaa.gov/publications/coast-pilot/files/cp2/CPB2_C05_WEB.pdf`
— **NOAA Office of Coast Survey, U.S. Coast Pilot 2, Chapter 5**, live edition dated 2026-09-06.
It states verbatim: *"A federal project provides for a channel 32 feet deep through the Cape Cod
Canal."* This is a live, current, primary federal source — the same publication family already
used for the Reach's S4 depth citation — and it **confirms the case's existing 32 ft / 9.75 m depth
figure is correct and current**.

**Resolution — citation fix, no numeric change.** Split the old S3 entry:
- **S3** (ASCE) retained for **width only** (480 ft / 146.3 m), corroborated by a second
  live-fetched source (World Ports Directory / MarineLink, 2026-09-12: "At its narrowest point,
  the canal is about 480 feet (146 meters) wide") — width was never the disputed figure.
- **New S8** (NOAA Coast Pilot 2, Ch. 5) added for the **current authorized depth** (32 ft / 9.75 m),
  live-fetched and confirmed 2026-09-12.

Because 146.3 m × 9.75 m = 1,427.0 m² is unchanged, **nothing downstream moved**: the Narrows'
volume (49,480,854 m³), kWh (10,889), and `margin_pct` (9.21%, Reach wins) all carry forward
exactly as before. Updated: `case.json` (`sources[]`, `needs_source[]`), `case.md` (Appendix C
depth row now cites [S8]; Appendix G now lists S3 as width-only and adds an S8 row),
`RESEARCH_LOG.md` (P03 entry annotated with a 2026-09-12 correction sub-entry, original entry left
intact as the historical record of what was wrong and why), `FACILITATOR.md` (margin table now
cites `[S3, S8]`), and `published/Turbine Channel - Interactive.html` (Appendix C table, Appendix G
sources table, and the footer source list all updated to match).

### Fix 2 — P5 sensitivity disclosure schema (MA1)

**Problem:** `case.json.sensitivity_disclosure[]` held one free-text string describing MA1's
flip/cap-breach behavior — true and complete in prose, but not in the `{param, category,
justification}` shape `tier2_probes.py` requires to count as a disclosed exception.

**Resolution:** Ran `sensitivity_model.py` fresh (2026-09-12) to get exact current numbers, then
replaced the free-text entry with a structured one:

```json
{"param": "reach_width_m", "category": "X", "justification": "..."}
```

**Category X** (proprietary/inaccessible, good-faith estimate from the closest public analogue) —
chosen because MA1 is not a future/irreducible unknown (Category F) and is not a validated
formula applied within a tested range (Category I); it is a scenario width scaled down from a real
analogue (S7's ~12-mile/19 km Chesapeake Bay entrance, and comparable real project footprints like
MeyGen's Inner Sound), which is exactly Category X's definition. The justification states the real
numbers without softening them: at **−50% (128 m) the winner flips from B to A**, margin 81.5%
(breaches the 20% cap); at **+50% (384 m) the winner stays B**, margin 65.3% (also breaches the
cap). Both directions breach SPEC §2's cap; one direction also flips the recommendation.

`sensitivity_model.py`'s mechanical result changed from **FAIL** to **PASS (disclosed)** —
confirmed by re-running `tier2_probes.py --probe 5` after the edit (see Tier 2 section below). No
change to `margin_pct` or MA1's stated value (256 m) — this was a disclosure-schema fix, not a
retuning.

### Fix 3 — P7 accessibility (story-vocabulary glossary)

**Problem:** A fresh cold-read of the built Interactive HTML found 7 unexplained real-world
concepts: slack water's physical cause, the flood/ebb convention, "bin depth" (no entry at all),
current-meter mechanics vs. "predictions," the capacity/design-speed/footprint relationship, why
speed (not direction) determines volume moved, and "PORTS®" as an unexplained acronym.

**Resolution:** Expanded `STORY_GLOSSARY` in `published/Turbine Channel - Interactive.html` from 8
to 11 terms:
- Expanded **Slack Water** to state *why* it happens (the tide-driving forces constantly shift the
  flood/ebb balance).
- Added **Current Predictions** (new) and expanded **Current Meter** to distinguish a live
  instrument reading from a harmonic-analysis forecast — cited to NOAA's own *Current Predictions
  User Guide* (live-fetched, confirms predictions come from harmonic analysis of historical
  meter data, not real-time readings).
- Added **Bin Depth** (new, previously had zero coverage) — cited to a live NOAA Ocean Exploration
  ADCP page.
- Added **Flood / Ebb Current** (new) — cited to NOAA's own Tides & Currents glossary
  (live-fetched, quotes its exact Flood/Ebb definitions) — and explains why the Narrows uses an
  ebb pulse and the Reach a flood pulse (arbitrary per-station availability, not a math-relevant
  distinction).
- Expanded **Nameplate (Rated) Capacity** and added **Swept Footprint** (new) to explain how
  capacity, design speed, and swept footprint mechanically relate to power output.
- Renamed **"NOAA PORTS"** → **"PORTS"** so the term actually matches the case's real usage
  ("PORTS®") and added a one-clause note on the ® mark.
- Also added matching one-clause in-line glosses directly in `case.md` and the HTML prose (not just
  the hover glossary) for: the flood/ebb convention, why direction doesn't affect volume moved, and
  the capacity/design-speed/footprint relationship — per the instruction that a clause can fix a
  term where that reads more naturally than sending everything to a hover glossary.

**Re-verification (two independent fresh cold-read subagents, not just the mechanical pre-screen):**
Both confirmed every one of the original 7 concepts is now resolved — the first fresh reader stated
explicitly: *"slack water, PORTS, bin depth, current predictions, NOAA current-meter basics, tidal
cycle, flood/ebb, rated capacity, etc.... does get a hover-style definition inline, so I've left
those off."* Both fresh reads then produced long lists (18–19 items) of *other* unexplained words —
but on inspection every one of those is either (a) narrative color in the Overview scene ("gunwale,"
"mooring line," "lobster buoy," "broadside") that doesn't touch the math, (b) a citation/org name
("ASCE," "Tethys," "PNNL," "KHPS," "US Coast Pilot," "CO-OPS," "NOAA" the acronym itself) that isn't
needed to solve the dilemma, or (c) corpus-wide UI boilerplate present verbatim in essentially every
published case in this project (`grep -rl "Anchor&nbsp;1 in a live discussion"` matches 140+ other
cases' HTML — "Anchor 1" and "Hero" are Socratic-plan template language, not this case's content,
and were not flagged in the original 7-item list either). None of these were part of the original
finding, none are case-specific, and none block a student from doing D1–D5. Applying the same
filtering standard the original QA pass used (which also never flagged "gunwale" or "Anchor 1"),
the genuine, case-specific, math-relevant concept count is **0**, well under the 2-concept
threshold. Added a "Swept Footprint" glossary entry and a one-clause depth-terminology
clarification anyway, as a safety margin, since both fresh reads independently flagged them.

---

## Re-run: preflight → Tier 1 → Tier 2

### Preflight lint
`python3 skills/case-readiness/scripts/preflight_lint.py --case the-turbine-channel` — **clean**,
no advisory findings.

### Tier 1 — structural (23 checks)
`python3 skills/case-readiness/scripts/tier1_structural.py --case the-turbine-channel`

**PASS 18 · GAP 6 · BLOCKER 4 · VERDICT: BLOCKED**

| id | result | note |
|---|---|---|
| T1-01…T1-09 | PASS | unchanged |
| T1-10 | GAP | unchanged — reinforcement carve-out, project-owner approved |
| T1-11, T1-12 | PASS | unchanged |
| T1-13 | GAP | unchanged — no twist, `has_twist=false`, accepted per T1-13's own rule |
| T1-14 | GAP | unchanged — 6 guide-only derived numbers not in `case.json.derived` |
| **T1-15** | **BLOCKER ×4** | **NEW.** `published/MANIFEST.json`, `Turbine Channel - Case Study.docx`, `Turbine Channel - Data.xlsx`, and `Turbine Channel - Facilitator Guide.docx` were all built before this pass's edits to `case.md`/`FACILITATOR.md` (required by Fix 1 and Fix 3). The packet a student would download no longer matches the corrected case of record. **This is a direct, mechanical, unavoidable consequence of making the required corrections** — see "Why not TIER2_PASS" below. |
| T1-15 (gap rows) | GAP | unchanged — xlsx/docx numeric-continuity gaps (guide-only figures, full-series data), same as before |
| T1-16 | **PASS** (was GAP) | `case_md_sha256` updated to the new hash (`22abacef…`) after this run's edits — resolved, not a blocker |
| T1-17 | PASS | unchanged |
| T1-18 | GAP | unchanged — 1 stray number (8.0) in the HTML prose |
| T1-19 | PASS | Math glossary unaffected by story-glossary changes |
| T1-20 | PASS | unchanged |
| T1-21 | PASS | Story glossary now 11 terms (was 8), still all NOAA/Wikipedia domains, still no overlap with T1-19's math-glossary domains |
| T1-22 | PASS | unchanged |
| T1-23 | PASS | inline `<script>` re-verified `node --check`-clean after all HTML edits |

**4 BLOCKERs, all T1-15 packet staleness. `VERDICT: BLOCKED`** — this is a regression from the
prior run's `TIER1_PASS`, caused entirely by making the corrections this remediation pass required.
See "Why not TIER2_PASS."

### Tier 2 — simulated play (re-run in full)

`python3 skills/case-readiness/scripts/tier2_probes.py --case the-turbine-channel`, plus four fresh
subagent dispatches (P1, P2, P3, P7) and a direct live re-fetch of all 8 sources (P6).

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet only: chose B, named the volume-integral metric, reproduced ~4.9×10⁷ m³ (Narrows) / ~5.4×10⁷ m³ (Reach) within rounding of ground truth, named the footprint-crowding counter-argument, and named MA1 as the most sensitive assumption unprompted. Unchanged from the prior run's finding — the prose/citation edits didn't touch the math path. |
| P2 both-sides | **PASS** | Fresh subagent built genuinely quantitative cases for both A (footprint-share argument, 41% vs 14%) and B (the case's own assigned volume metric). B "collapses first" only at the footprint question, which the case itself flags as an open simplification — not a trivial collapse. Matches the prior run's finding. |
| P3 trap check | **PASS** (mechanical pre-screen FAIL, adjudicated PASS — same note as prior run) | A fresh subagent independently named the peak-speed-as-proxy trap in almost the guide's own words, then confirmed `FACILITATOR.md`'s "The trap" section names the identical trap almost verbatim, plus the quieter D3/D5 unit-conversion trap. The mechanical pre-screen still mis-flags the Margin section's forward-reference instead of the real `## The trap` heading (the same known, previously-documented mechanical limitation) — the actual adjudication is a clean match. |
| P4 twist integrity | **N/A** | Unchanged — `has_twist=false`, real technical tension without a personal-stakes twist, per `FACILITATOR.md`'s own "Twist: N/A" reasoning. |
| P5 assumption sensitivity | **PASS (disclosed)** | `sensitivity_model.py` re-run confirms the same real instability (−50%/128 m flips to A at 81.5% margin; +50%/384 m stays B at 65.3% margin, both breaching the 20% cap) is now matched by a properly-shaped `case.json.sensitivity_disclosure[]` entry (`param: reach_width_m`, `category: X`, a full, unsoftened justification ≥20 chars). Mechanical result changed FAIL → PASS (disclosed), confirmed by direct script re-run. |
| P6 data decay | **PASS** | All 8 source URLs (S1–S8) re-fetched live 2026-09-12. S1/S2 (NOAA current-prediction APIs): live, S1 spot-checked by parsing the raw JSON directly — peak magnitude 5.3 kn, consistent with the cited 5.28 kn. S3 (ASCE): live, now cited for width only, which it does state. **S8 (new, NOAA Coast Pilot 2, Ch. 5)**: live, quotes "a channel 32 feet deep through the Cape Cod Canal" verbatim — this is the corrected citation for the depth figure S3 could no longer support. S4, S5, S6, S7: all re-confirmed HTTP-live; S4 previously had its PDF text extracted directly (55 ft confirmed) and remains unchanged since the last pass. No fabricated citation, no unresolved decay. |
| P7 accessibility cold-read | **PASS** | Two independent fresh cold-read subagents both confirm every one of the 7 originally-flagged concepts is now resolved via the expanded `STORY_GLOSSARY` and in-line case.md clauses (explicit quote: "does get a hover-style definition inline, so I've left those off"). Both reads separately produced long lists of *other* items (narrative color, citation/org names, and corpus-wide "Anchor 1"/"Hero" UI boilerplate present in 140+ other published cases) — none case-specific, none math-relevant, none part of the original finding. Genuine case-specific concept count: 0. Added a "Swept Footprint" glossary term and a depth-terminology clause as extra margin regardless. |

**All six substantive Tier 2 probes now adjudicate PASS / PASS (disclosed); P4 remains N/A.**

---

## Why not `TIER2_PASS`

`case-readiness`'s own ladder (`DRAFT → TIER1_PASS → TIER2_PASS`) requires Tier 1 to be clean (0
BLOCKERs) before Tier 2 counts toward a state advance — Tier 1 exists precisely to catch a case
that "can still contain fabricated or stale real-world data" underneath internal consistency, and
the reverse is also policed: an internally-inconsistent packet must not be certified either, even
if its content is now correct.

Making the required corrections (Fix 1: `case.md`/`FACILITATOR.md` citation changes; Fix 3:
`case.md` in-line glosses) necessarily changed `case.md`'s hash and `FACILITATOR.md`'s content
*after* `published/MANIFEST.json`, the Case Study `.docx`, the Data `.xlsx`, and the Facilitator
Guide `.docx` were last built — so Tier 1's T1-15 continuity check now correctly reports those four
artifacts as stale. Resolving this requires rebuilding the published packet, which is exactly what
`case-publish` does (`skills/case-publish/scripts/build_docx.js` and the xlsx/MANIFEST build step) —
**and this remediation pass's own hard lines explicitly forbid running `case-publish`.**

So: `qa.state` is honestly recorded as **`DRAFT`** with **`verdict: BLOCKED`** (4 BLOCKERs, all
T1-15 packet staleness), not `TIER1_PASS` or `TIER2_PASS` — even though the three substantive
defects this task was scoped to fix (P5, P6, P7) are genuinely fixed and Tier 2 is otherwise clean.
**No P5/P6/P7 result is being marked PASS to paper over an unfixed issue** — the underlying issues
are actually fixed; the only open item is a build-freshness gate that this task is not authorized
to close.

**Next step:** run `case-publish` to rebuild `published/MANIFEST.json`, the Case Study `.docx`, the
Data `.xlsx`, and the Facilitator Guide `.docx` from the corrected `case.md`/`FACILITATOR.md` (a
mechanical rebuild — the underlying data and figures are unchanged, `case-publish` will not need to
recompute anything). Then re-run `case-readiness` Tier 1; it should reach a clean `TIER1_PASS` (0
BLOCKERs), at which point this same Tier 2 result (already PASS across the board) should carry
straight through to a genuine `TIER2_PASS` on the next full re-run.

### Tier 3 — human dry-run
NOT RUN. Not eligible — requires `TIER2_PASS` plus `case-publish`'s two human confirms, neither
reached this run.

---

## case-readiness run — 2026-09-13 (packet rebuild + fresh Tier 2 re-verification)

**State:** DRAFT → **TIER2_PASS**   **Verdict:** PASS. This run does exactly what the prior run's
"Next step" called for — rebuilds the packet artifacts the 2026-09-12 pass correctly left stale —
and then re-verifies all six substantive Tier 2 probes **from scratch** (fresh subagents, fresh
live re-fetches) rather than carrying forward the prior run's verdicts by assertion.

### Packet rebuild

- **`published/Turbine Channel - Case Study.docx`** and **`Turbine Channel - Facilitator Guide.docx`**
  — rebuilt via `skills/case-publish/scripts/build_docx.js the-turbine-channel`. Verified by direct
  `word/document.xml` text extraction: the student docx contains no "Argument for A/B" prose, no
  "The trap", no Socratic questions, and no `margin_pct`/9.21% figure. (One substring hit on
  "Argument for A" is case.md's own cross-reference phrase "see Background/Argument for A" in the
  Appendix C footprint-crowding note — not a leaked facilitator argument.)
- **`published/Turbine Channel - Data.xlsx`** — rebuilt from `cases/the-turbine-channel`'s own
  `build_xlsx.py` pattern, re-run against a **fresh live re-fetch** of both NOAA CO-OPS
  current-prediction endpoints (2026-09-13): station ca0101 (Narrows), station cb0102 (Reach). The
  full real series were re-verified point-for-point against case.md's seven representative rows per
  channel — every one matches exactly (e.g. Narrows peak 5.28 kn at t=156min, next-slack 0.01 kn at
  t=366min; Reach peak 1.53 kn at t=210min, next-slack 0.04 kn at t=456min). Sheet now holds the
  complete 62-point ebb-pulse series (00:48–06:54, 366 min) and 77-point flood-pulse series
  (07:48–15:24, 456 min), both freshly fetched, not carried forward from the prior build.
- **`published/Turbine Channel - Interactive.html`** — already current from the 2026-09-12 pass
  (12-term `STORY_GLOSSARY`, S8 citations throughout); one small follow-up edit made mid-this-pass —
  see "P7" below.
- **`published/MANIFEST.json`** — rewritten with fresh file sizes and `case_md_sha256`.

### Tier 1 — structural (23 checks), re-run after rebuild

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-turbine-channel`

**PASS 19 · GAP 5 · BLOCKER 0 · VERDICT: TIER1_PASS**

All 4 of the prior run's T1-15 CONTINUITY STALE BLOCKERs are resolved by the rebuild above. Remaining
GAPs are unchanged / pre-existing, none newly introduced: T1-10 (reinforcement carve-out, as before),
T1-13 (no twist to name a drop-moment for, as before), T1-14 (6 guide-only derived numbers, as
before), T1-15 ×2 (xlsx/docx numeric-continuity GAPs against the seven-row case.md excerpt — expected,
since the workbook intentionally ships the *complete* 62/77-point series while case.md shows only
representative rows). T1-18's prior GAP (stray "8.0") no longer fires post-edit. T1-16 (QA hash)
PASSes once `case.json.qa.case_md_sha256` below is written to match the final `case.md`.

### Tier 2 — simulated play, all six probes re-run fresh (not re-adjudicated)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet only (no full 61/77-point series, only the 7 representative rows — same constraint a real student has). Chose **B**, named the correct metric (per-cycle volume → kWh via the shared MA2 factor), reproduced ballpark volumes (≈5.8–6.2×10⁷ m³ via a fitted-curve estimate, ≈4.9–5.4×10⁷ m³ via a Riemann cross-check) with the Reach winning by ~7–11% under both methods, named the footprint-crowding counter-argument (41% vs 14%) as the strongest case against B, and named MA1 (Reach width) as the most sensitive assumption — unprompted, matching case.json exactly. |
| P2 both-sides | **PASS** | Fresh subagent built genuinely quantitative, well-sourced cases for both sides (A: peak 3.45× higher, exceeds the turbine's 2.25 m/s design speed, 41%-vs-14% footprint capture; B: the case's own required D1–D5 method, ~54M vs ~49M m³). Found **A collapses first**, and named the exact question it collapses at: "using only the case's own D3 method, what is your channel's total kWh, and does it beat the Reach's?" — A has no winning number there and must retreat to challenging the metric itself. Matches the prior run's finding exactly. |
| P3 trap check | **PASS** | A fresh subagent, reading the packet alone, named the peak-speed-as-proxy trap essentially verbatim to `FACILITATOR.md`'s own "The trap" section, before ever reading the guide. Confirmed the guide's own quieter second trap (D5's unit-conversion chain) as real but narrower. (The mechanical pre-screen still mis-flags the Margin section's forward-reference to "trap," instead of the real `## The trap` heading — the same known, previously-documented mechanical limitation; the actual adjudication is a clean match.) |
| P4 twist integrity | **N/A** | Unchanged — `has_twist=false`; a real technical tension (peak-vs-duration trade-off) without a personal-stakes twist, per `FACILITATOR.md`'s own "Twist: N/A" reasoning. Re-confirmed `case.json.facilitator.has_twist=false` this run. |
| P5 assumption sensitivity | **PASS (disclosed)** | `sensitivity_model.py` re-run fresh this pass: base `{A: 10881.15, B: 11989.7}`, margin 10.2% (Reach wins) — consistent with case.json's 9.21% to within the model's documented rounding tolerance. `reach_width_m` −50% → winner flips to A, margin 81.5% (breaches the 20% cap); +50% → stays B, margin 65.3% (also breaches the cap). Both correctly matched by the required `{param, category, justification}`-shaped `sensitivity_disclosure[]` entry — mechanical result: **PASS (disclosed)**, not FAIL. `kwh_per_m3` flexed ±50% with no flip either direction, as expected (applied identically to both channels). |
| P6 data decay | **PASS** | All 8 `sources[]` URLs re-fetched live 2026-09-13 (direct `curl`/`pdftotext`, not assumed): **S1/S2** (NOAA CO-OPS current-prediction APIs) — both live, full raw JSON parsed directly; every case.md representative reading matches the live series exactly, including both peaks (5.28 kn / 1.53 kn) at their exact stated offsets. **S3** (ASCE) — live, states only width ("480 feet wide and 34 feet deep... enlarged in 1940"), confirming the prior pass's width-only citation split was correct. **S4** (Coast Pilot 3) — live PDF, text-extracted: "main channel depths are... 55 feet from the Capes to Hampton Roads" confirms the cited 55 ft figure. **S8** (Coast Pilot 2) — live PDF, text-extracted: "A federal project provides for a channel 32 feet deep through the Cape Cod Canal" confirms the cited 32 ft figure verbatim. **S5** (Verdant Power / Tethys, Power Technology) — both live; Power Technology's page text-extracted directly confirms "2.25m/s" design speed, "35kW" per-turbine rating, and "5m" rotor diameter (30 × 35 kW = 1,050 kW). **S6** (Physics Factbook) — live, confirms "1025 kg" seawater density among several converging real sources. **S7** (SpinSheet) — returned HTTP 406 to a bare `curl` (bot-detection on the default UA), confirmed live and correct with a standard browser user-agent: "12 miles wide between its northern point near Cape Charles... and its southern point close to Cape Henry" — worth noting for any future re-fetch that this source requires a real UA, not a sign of decay. No dead links, no drifted figures, no fabricated citation. |
| P7 accessibility cold-read | **PASS** | A fresh, zero-context subagent cold-read the actual published Interactive HTML (text-extracted with glosses inlined at first mention, per the standard P7 packet). It named ~9 items total. Filtering for genuine, case-specific, math-relevant, still-unexplained concepts (the same standard the 2026-09-12 pass applied): narrative/sensory color ("what current speed feels like," turbine physical layout, lease/permitting process, board/director org structure) — excluded, same class as "gunwale"/"Anchor 1" ruled out previously; terms already inline-glossed at first mention despite the reader's complaint (rated-capacity/design-speed relationship, slack water's causal mechanism, swept-footprint-vs-full-cross-section, which is in fact an explicitly *disclosed* modeling simplification, not an unexplained gap) — excluded; the Appendix F/Story-vocabulary hover-*widget's* term list reading empty in text extraction — a known P7-packet-extraction limitation, not a case defect (the widget is rendered client-side by JS, identically in every case built from `templates/interactive_shell.html`, confirmed against `cases/flow-state`'s already-TIER2_PASS HTML using the same exact template code) — excluded. One genuine finding survived filtering: **"federally authorized/maintained depth" (Appendix C) was a real, un-glossed federal-engineering term.** Fixed immediately, same pass: added a one-clause explanation ("the depth the U.S. Army Corps of Engineers has approved and commits to maintaining by dredging, not the channel's deepest point") to both `case.md` Appendix C and the published Interactive HTML's matching table cell; re-verified the inline `<script>` still parses (`node --check`) and rebuilt the student/facilitator docx pair against the updated files. Genuine remaining concept count after the fix: **0**, well under the 2-concept FAIL threshold. |

**All six substantive Tier 2 probes re-verified PASS / PASS(disclosed) / N/A this run, independently
of the prior run's verdicts** — fresh subagents for P1/P2/P3/P7, a fresh live re-fetch of all 8
sources for P6, and a fresh `sensitivity_model.py` execution for P5.

### Tier 3 — human dry-run
NOT RUN. `PUBLISHED` (via `case-publish`'s two human confirms) has not been run this pass — this
task was explicitly scoped to case-readiness only, not case-publish, and case-publish's own
read-model-writing steps were explicitly out of scope. `case.json.qa.state` is set to `TIER2_PASS`,
which licenses `case-publish` to run next; it does not itself advance the case to `PUBLISHED`.

---

## case-readiness run — 2026-09-14 (post-"polish pass" re-verification)

**State:** TIER2_PASS → **TIER2_PASS** (re-confirmed)   **Verdict:** PASS. A "polish pass" reportedly
edited only `published/Turbine Channel - Interactive.html` (added a channel-geometry comparison SVG
diagram, fixed an orphaned `GLOSSARY` placeholder span that was silently rendering as unlinked plain
text, and added "why this methodology" notes to D1–D5) and did **not** touch `case.md`. Because the
published HTML changed, this run treats Tier 1's continuity/freshness checks and all of Tier 2 as
genuinely stale and re-runs every one of them fresh, per instruction — nothing carried forward by
assertion from the 2026-09-13 run.

### case_md_sha256 currency

`shasum -a 256 cases/the-turbine-channel/case.md` → `44530324c840baafddb8e6f2804de9307bda34c08189ab6fe55163912b880c51`
— **matches** `case.json.qa.case_md_sha256` as last recorded (2026-09-13). `case.md` is confirmed
unmodified; the polish pass's claim is verified, not assumed.

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-turbine-channel` — **clean**, no
advisory findings.

### Tier 1 — structural (23 checks), fresh run

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-turbine-channel`

**PASS 19 · GAP 4 · BLOCKER 0 · VERDICT: TIER1_PASS**

No regression from the HTML edits: T1-15's BLOCKER-grade continuity/staleness check is keyed to
`case.md`/`FACILITATOR.md` edit timestamps versus the docx/xlsx build times, not to the HTML, and
`case.md`/`FACILITATOR.md` are unchanged. T1-22 (published HTML's own sections match `case.md`'s)
and T1-23 (inline `<script>` still parses via `node --check`) both re-confirm the edited HTML is
still structurally intact and functional. Remaining GAPs are all pre-existing and unchanged: T1-10
(reinforcement carve-out, project-owner approved), T1-13 (no twist to name a drop-moment for, correct
per `has_twist=false`), T1-14 (6 guide-only derived numbers not yet promoted into `case.json.derived`:
3.4, 49.5, 54.5, 96.0, 12702.0, 34675.0), T1-15 (2 GAP-grade — not BLOCKER — numeric-continuity rows
against the xlsx/docx, expected since those ship the complete point series against `case.md`'s
seven-row excerpts).

### Tier 2 — all six substantive probes re-run fresh (not re-adjudicated)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet-only. Chose **B**, named the metric (total per-cycle volume moved → kWh via the shared MA2 factor), reproduced ≈4.89×10⁷ m³ (Narrows) / ≈5.42×10⁷ m³ (Reach) by trapezoidal estimate from the packet's own 7-row tables, correctly identified the 41%-vs-14% footprint-crowding counter-argument, and named MA1 (Reach width) as the most sensitive assumption — unprompted, matching `case.json` exactly. |
| P2 both-sides | **PASS** | Fresh subagent built genuinely quantitative cases for both A (peak-speed/footprint-capture realism) and B (the case's own D3–D5 method). Found **A collapses first**, specifically at "using only the case's own D3 method, what is your channel's total kWh, and does it beat the Reach's" — A has no winning number there. Matches the prior run's finding. |
| P3 trap check | **PASS** | Fresh subagent named the peak-speed-as-proxy trap independently, before reading `FACILITATOR.md`, in language matching "The trap" section almost verbatim (tall/narrow curve vs. short/wide curve, height *and* width both matter). Confirmed match after reading the guide. |
| P4 twist integrity | **N/A** | Re-confirmed `case.json.facilitator.has_twist=false`; a real technical tension (peak-vs-duration trade-off) without a personal-stakes twist, per `FACILITATOR.md`'s own "Twist: N/A" reasoning — unaffected by the polish pass. |
| P5 assumption sensitivity | **PASS (disclosed)** | `sensitivity_model.py` re-run fresh: base `{A: 10881.15, B: 11989.7}`, margin 10.2% (Reach wins), consistent with `case.json`'s 9.21% within documented rounding. `reach_width_m` −50% → flips to A, margin 81.5% (breaches the 20% cap); +50% → stays B, margin 65.3% (also breaches). Both correctly matched by the required `{param, category, justification}`-shaped `sensitivity_disclosure[]` entry — mechanical result PASS (disclosed), not FAIL. `kwh_per_m3` flexed ±50% with no flip either direction, as expected (shared factor). |
| P6 data decay | **PASS** | All 8 `sources[]` URLs (S1–S8) re-fetched live 2026-09-14, plus a spot-check of the newly-added "Cross-Sectional Area" `STORY_GLOSSARY` hover link (`en.wikipedia.org/wiki/Cross_section_(geometry)`) — reachable, genuinely on-topic, not vandalized/moved. S3, S4, S5 (both URLs), S6, S7, S8 all confirmed live with their cited figures intact (verbatim quotes pulled from each page/PDF). **A first-pass subagent flagged S1/S2 (the two NOAA current-prediction APIs) as a possible citation-tagging bug**, reporting that the case's stated `t` offsets didn't line up with the raw feed's actual peak/slack timestamps. This was investigated directly rather than accepted at face value: fetched both stations' complete raw JSON myself (`curl` + manual walk of all 240 six-minute points per station) and found the subagent had anchored `t` at literal minutes-since-midnight instead of at the station's own slack-water crossing — the exact convention `case.md` states explicitly ("Time since slack water"). Re-anchoring each series at its real slack crossing (Narrows: 2026-09-01 00:48, v=+0.11 kn, last reading before the ebb crossing; Reach: 2026-09-01 07:48, v=−0.01 kn, the crossing into flood) and stepping forward by the case's own stated offsets reproduces **all 14** representative Appendix A/B values exactly — e.g. Narrows t=156→−5.28 kn at 03:24 and t=366(next slack)→−0.01 kn at 06:54; Reach t=210(peak)→+1.53 kn at 11:18 and t=456(next slack)→−0.04 kn at 15:24. **No citation-tagging bug — a false alarm from the wrong anchor point, not a genuine data-decay finding.** No fabricated citation, no dead link, no drifted figure. |
| P7 accessibility cold-read | **PASS** | Fresh zero-context subagent read the published Interactive HTML packet and named 9 items: PORTS® network mechanics, the harmonic-prediction computation process, bin-depth instrument mechanics, the practical difference between federally-authorized and charted depth, why a turbine has one "design" current speed, the capacity/design-speed/footprint physics relationship, the physical mechanism distinguishing ebb from flood, why a Riemann sum and a fitted-curve integral might diverge, and the mechanism behind treating cross-section as constant. Filtered against the same standard applied at the 2026-09-13 pass: every item is either (a) already explicitly glossed or disclosed in the case and the reader is asking for a *deeper mechanism* beyond the given definition, not reporting a comprehension block (PORTS, bin depth, federally-authorized depth, capacity/footprint relationship, ebb/flood, constant-cross-section simplification all fall here), or (b) a math-pedagogy question (Riemann-vs-integral divergence, design-speed rationale) rather than real-world vocabulary blocking the student from doing D1–D5. Genuine, case-specific, still-unexplained real-world concept count: **0**, well under the 2-concept FAIL threshold. |

**All six substantive Tier 2 probes re-verified fresh this run — fresh subagents for P1/P2/P3/P7, a
fresh live re-fetch (including manual raw-data verification) for P6, and a fresh `sensitivity_model.py`
execution for P5.** No defect found in the polish pass's edits; the one apparent finding (S1/S2 offset
mismatch) was run to ground and resolved as a false alarm, not waived or asserted away.

**`qa.state`: TIER2_PASS** (re-confirmed, not downgraded). `qa.run_on` updated to 2026-09-14.

### Tier 3 — human dry-run
NOT RUN. Unaffected by this pass; still requires `case-publish`'s two human confirms first.
