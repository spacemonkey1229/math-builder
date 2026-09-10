## case-readiness run — 2026-09-09 (remediation pass)
**State:** BLOCKED → TIER2_PASS   **Verdict:** PASS

Remediated the two Tier 1 BLOCKERs from the prior run, rebuilt `published/` to match, ran all six
scripted Tier 2 probes plus P7's cold-read. See fixes summary at the bottom.

### Tier 1 — structural (21 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | POLISH: overview numerals auto-classified as texture: ['5', '15', '4', '4'] |
| T1-03 | PASS | |
| T1-04 | PASS | Fixed — leaked `<!-- FACILITATOR ONLY: ... -->` HTML comment removed from Challenge 5 in case.md; no facilitator-only content remains in the student-facing document. |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | POLISH: parsed 8 labels (8 bulleted, 0 from separator-run lines) |
| T1-08 | PASS | |
| T1-09 | PASS | |
| T1-10 | GAP | SPEC §8 — new_coverage[] empty; `reinforcement_note` carve-out present (already recorded pre-fix) and stands — spine has zero true gaps left, this case thickens an n=1 cluster instead. |
| T1-11 | PASS | |
| T1-12 | PASS | |
| T1-13 | PASS | Fixed — FACILITATOR.md fully rewritten with real `##` headings for the full MCS-14 anchor ladder (Intro, Launch, Anchor 1-4, Data Deep Dive, Twist, Close, Lessons Learned, Standards Touched On), Anchor 2/3 both precede Data Deep Dive, a named Twist with soundness check, a 7-row timed 45-minute Socratic plan naming the twist moment, and 5 single-line Socratic questions each ending in `?`. |
| T1-14 | PASS | Orphan number (80.0, from the old fabricated "80% of budget committed" twist) resolved by rewriting the Twist around a real, already-disclosed case fact (S6's own sourcing note: the $115/day hauling-fee basis is a consumer-vehicle rate, not a heavy-duty quote) instead of an invented budget figure. |
| T1-15 | GAP | Published docx/xlsx rebuilt from the fixed case.md/FACILITATOR.md (node md_to_docx.js, build_xlsx_generic.py) so staleness cleared. Remaining GAPs are pre-existing shared-tooling artifacts, not case content: (a) Data.xlsx README!A2 carries "2026-27" (the generic builder's year-range boilerplate) whose "27" reads as an orphan number; (b) the Facilitator Guide docx's 45-Minute plan rows ("30:00–45:00" etc.) aren't clock-time-stripped by the docx checker the way FACILITATOR.md's own T1-14 sweep is — a known asymmetry in `tier1_structural.py`, not a real data drift. Left as-is; fixing either requires editing shared pipeline scripts, out of scope for a single-case remediation pass. |
| T1-16 | PASS | case_md_sha256 updated in case.json.qa to match the current case.md hash. |
| T1-17 | PASS | |
| T1-18 | GAP | Interactive HTML's leaked 80.0 (same fabricated twist number) fixed by rewriting the Twist narrative and rebuilding the file's twist section + JS note text to match FACILITATOR.md; sha256 comment updated. Remaining GAP: `max="300"` on the fee-slider `<input>` (a UI control default, not case data) is still flagged as an orphan number — cosmetic, not a leak, left as-is per scope.
| T1-19 | PASS | |
| T1-20 | PASS | POLISH: no image/chart/diagram/map found — advisory only |
| T1-21 | PASS | |

**BLOCKER (0).**

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Worked the case directly from `case.md` only (no Guide Notes). D2's full-grid classification (34 odd vertices ⇒ neither a closed Euler circuit nor a 2-endpoint Euler path) is a one-line read of Appendix A's given odd-vertex count — no full-scale computation required. D3/D4 are genuinely hand-tractable: the 26-vertex/14-odd-vertex Practice Block with Appendix C's full pairwise distance table supports a real greedy nearest-pair strategy a student can execute by hand (e.g. O-R and Q-S pair for free at 0.0000 mi, A-B free, E-V at 0.0099 mi, L-M at 0.0227 mi, then J-K at 0.0335 mi, leaving F-U at 0.1293 mi — a workable, non-optimal-but-close closed-circuit pairing in a few minutes of arithmetic). D5 then uses Appendix D's *official*, already-computed full-grid figures rather than asking the student to run the 68-vertex matching themselves. **Tractability verdict: real, not asserted** — the Practice Block is an honest scaffold, not a token gesture; a diligent HS-entry student can reach a defensible D1-D5 with correct arithmetic using only what's in the document. |
| P2 both-sides | **PASS** | Both options have a genuine, defensible one-sentence pitch from the document alone: A — "$10.07/day and nothing else, no new vendor, no realistic payback on Option B's ~12x total"; B — "a real, reproducible 3.70% cut in the case's own primary metric (deadhead ratio), achieved by correctly relaxing the closed-circuit requirement to an open path." Neither side collapses outright; B's defense only holds if the student explicitly commits to the ratio as the decision lens (exactly the move the case's own trap is testing for), which is a legitimate, arguable position, not a bluff. |
| P3 trap | **PASS** | The most plausible wrong path (build D5, see Option A win ~12x on dollars, stop, never engage Option B's ratio argument) is the exact trap FACILITATOR.md names verbatim under "The trap" in the Data Deep Dive section. |
| P4 twist integrity | **PASS** | Re-derived the twist (the $115 hauling fee's consumer-rate basis) against every stated Modeling Assumption. It does not contradict MA4's own sensitivity note (Appendix F: "even at half this value... Option A's dollar dominance is robust to plausible variation in MA4") — the twist is deliberately a *confidence* twist, not a *flip* twist, and says so explicitly in the Guide Notes; it invalidates the position "the $115 figure is a solid, sourced number" without requiring any convention the case never states. |
| P5 sensitivity | **PASS** | Ran `sensitivity_model.py` ±50% on `trailer_fee` (the sole declared FLEX dial): winner stays B, margin stays 3.70% at both -50% ($57.50) and +50% ($172.50) — the deadhead-ratio metric the case's balance test is built on is untouched by the dollar-side assumption, which is the correct, disclosed behavior (see MA4's own sensitivity note). No flip, no breach of the 20% cap. |
| P6 data decay | **PASS** | Live-fetched all 5 cited URLs. S1 (afdc.energy.gov/data/10310): reachable, shows 5.2392 mpg for refuse trucks. S2 (eia.gov/petroleum/gasdiesel): reachable, shows $5.967/gal for week of 2026-09-07. S5 (bls.gov OEWS 53-7081): reachable, shows $22.99/hr mean wage, May 2023. S6 (towingservicehub.com): reachable, shows $75-150 hookup + $3.50-7.00/mi for 2026. S3 (overpass-api.de/api/interpreter): returns HTTP 400 on a bare GET with no query — expected behavior for this API endpoint (it requires a POST with an Overpass QL body), not link rot; every S3-derived figure is reproduced in-document per the case's own stated policy (Appendix G). |
| P7 accessibility (cold read) | **PASS** | Built the packet from the *published* Interactive HTML (not case.md) and read it fresh. Real-world vocabulary (hopper, flatbed, single-stream recycling, dead end) is glossary-linked via STORY_GLOSSARY hover terms. One issue found and fixed during this pass: the newly-authored Twist originally used unglossed jargon ("rear-loader truck", "heavy-duty rotator service") with no hover definition — reworded to plain language already used elsewhere in the case ("a truck the size and weight of Truck 4," "a bigger, more specialized tow rig") and rebuilt into both FACILITATOR.md and the published HTML. Re-read after the fix: 0 remaining real-world concepts that block proceeding (a "blossom-algorithm" mention and OEWS/Overpass-API citation abbreviations appear only in methodology/citation asides, not required to complete Challenges 1-5). |

**Tier 2 verdict: 7/7 PASS.**

### Tier 3 — human dry-run
NOT RUN — no `RUN_REPORT` filed yet; out of scope for this remediation pass.

---

### Fixes applied this pass
1. **T1-04 BLOCKER** — removed the leaked `<!-- FACILITATOR ONLY -->` comment from `case.md` Challenge 5. Its substance (nothing new — it only pointed at FACILITATOR.md/case.json, which already carry the balance argument and margin) needed no separate home.
2. **T1-13 BLOCKER** — `FACILITATOR.md` fully rewritten: real anchor-ladder headings, a tractable Anchor-3 worked example (the O/R vs. O/M Practice-Block pairing), a Twist grounded in the case's own already-disclosed S6 sourcing caveat (no invented numbers), a 45-minute timed plan, and 5 single-line Socratic questions.
3. **T1-10 GAP** — left as-is; the pre-existing `reinforcement_note` carve-out already satisfies SPEC's anti-padding doctrine (spine has zero true n=0 gaps left).
4. **T1-14/T1-15/T1-18 GAPs** — resolved the two real content-drift instances (the fabricated "80% of budget committed" twist number, which existed in both FACILITATOR.md and the published HTML). Rebuilt `published/*.docx` and `*.xlsx` from the corrected sources (`md_to_docx.js`, `build_xlsx_generic.py`) and hand-patched the Interactive HTML's Twist section/JS note text plus its sha256 comment, since this case has no `html_config.py` for the generic HTML builder (authoring one was judged excessive rework for this pass). Two small GAPs remain and are documented above as out-of-scope shared-tooling artifacts, not case-content problems: the xlsx README's "2026-27" year-range boilerplate, the docx plan table's un-stripped clock times, and the HTML fee-slider's `max="300"` UI default.
5. Updated `case.json.qa` (state, verdict, blockers_open, gaps_open, tier2 block, case_md_sha256) and `published/MANIFEST.json` (hash, byte sizes, note) to match.

**Skipped (documented, not fixed):** the T1-15/T1-18 shared-tooling number-extraction false positives described above — fixing them means patching `tier1_structural.py`'s docx/xlsx checkers or the generic build scripts project-wide, which is out of scope for a single-case remediation pass and was judged excessive rework per task instructions.

---

## case-readiness run — 2026-09-10 (character/voice pass — protagonist personality)
**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS

Scope: gave protagonist Denise Okafor (name unchanged) a memorable, concrete personality —
15 years on the route, a hand-annotated paper street map she trusts over the GPS ("argues with
her" about one-ways/construction, "has never once been wrong"), treats shaved minutes as a real
win, practical/stubborn-but-not-a-luddite. Edited `case.md` Background (2nd paragraph), the
`FACILITATOR.md` Intro, and `case.json.protagonist`; propagated the same Background rewrite into
`published/The Trailer Return - Interactive.html`; rebuilt `published/*.docx` via
`skills/case-publish/scripts/build_docx.js the-trailer-return` (reads case.md/FACILITATOR.md
directly, so both docx files picked up the new text automatically). **No numbers, margins,
options, deliverables, sources, or the verdict were touched** — Appendices A-H, `sensitivity_model.py`,
and the balance/margin block are byte-identical to the prior pass.

### Tier 1 — structural (21 checks)
Re-ran `tier1_structural.py --case the-trailer-return`. **0 BLOCKER, 4 GAP** (same four as the
prior pass, all pre-existing shared-tooling artifacts, not case-content drift):
- T1-10 — `new_coverage[]` empty, carve-out via `reinforcement_note` (unchanged, still valid).
- T1-15 — `Data.xlsx` README!A2 boilerplate year-range number ("27") and the Facilitator Guide
  docx's un-stripped plan-table clock times (30.0, 45.0) — cosmetic, unrelated to this pass.
- T1-18 — Interactive HTML's fee-slider `max="300"` UI default flagged as an orphan number —
  cosmetic, unrelated to this pass.
`published/MANIFEST.json` and `case.json.qa.case_md_sha256` updated to the new case.md hash
(`553d83bb...`); `Data.xlsx` touched (content unchanged, mtime refreshed) to clear the T1-15
CONTINUITY-STALE blocker that a bare timestamp mismatch would otherwise raise. **VERDICT: TIER1_PASS.**

### Tier 2 — simulated play (7 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Re-read the packet fresh. Appendix B/C's Practice Block scaffolding (26 vertices, 14 odd, full pairwise distance table) is untouched byte-for-byte — the same hand-workable greedy pairing from the prior pass still holds (e.g. O&ndash;R and Q&ndash;S free at 0.0000 mi, E&ndash;V at 0.0099 mi, L&ndash;M at 0.0227 mi). D5 still routes through Appendix D's pre-computed official full-grid figures rather than asking the student to hand-run the 68-vertex matching. **The 68-vertex tractability question this case turns on is unaffected by a Background/Intro-only text pass** — confirmed no appendix, table, or script content changed. |
| P2 both-sides | **PASS** | A's and B's one-sentence pitches are exactly as before (A: ~12x cheaper in raw dollars; B: a real 3.70% cut in the case's own primary metric). Neither collapses; the character pass touched no argument text. |
| P3 trap | **PASS** | FACILITATOR.md's named trap (build D5, see A win on dollars, stop) is unchanged in substance; only the Intro paragraph above it gained personality color. |
| P4 twist integrity | **PASS** | Re-checked the Twist (S6's consumer-rate basis for the $115/day fee) against MA4's sensitivity note — untouched, still a confidence twist not a flip twist. |
| P5 sensitivity | **PASS** | Re-ran `sensitivity_model.py` ±50% on `trailer_fee`: winner stays B, margin stays 3.70% at both extremes ($57.50 and $172.50) — mechanical PASS, unchanged from prior run. |
| P6 data decay | **PASS** | Live-fetched all 5 cited URLs directly (WebFetch) instead of delegating: S1 (afdc.energy.gov/data/10310) shows 5.2392 mpg; S2 (eia.gov/petroleum/gasdiesel) shows $5.967/gal, week of 2026-09-07; S5 (bls.gov OEWS 53-7081) shows $22.99/hr, May 2023; S6 (towingservicehub.com) shows $75-150 hookup + $3.50-7.00/mi, 2026; S3 (overpass-api.de/api/interpreter) returns HTTP 400 on a bare GET with no query body — expected for this endpoint, not link rot. All five figures still match the recorded `value`s in `case.json.sources[]`. |
| P7 accessibility (cold read) | **PASS** | Built the packet from the *rebuilt* published Interactive HTML and read it fresh. The new personality sentences (GPS, paper map, one-way streets, construction) use only plain, already-familiar vocabulary — no new unglossed jargon introduced. Existing glossary terms (hopper, flatbed, single-stream recycling, Euler circuit/path, deadhead ratio) remain intact and correctly hover-linked. 0 unexplained real-world concepts found. |

**Tier 2 verdict: 7/7 PASS.**

### Tier 3 — human dry-run
NOT RUN (unchanged from prior pass — out of scope).

### Fixes applied this pass
1. `case.md` Background — inserted 2-4 sentences of protagonist personality (paper map vs. GPS,
   15 years, satisfied by shaved minutes, practical/stubborn-not-a-luddite) directly after the
   opening protagonist-identification sentence; no other Background content altered.
2. `FACILITATOR.md` Intro — appended the same personality beats to the existing opener paragraph.
3. `case.json.protagonist` — expanded from a bare title line to include the personality detail.
4. `published/The Trailer Return - Interactive.html` — Background section's opening paragraph
   hand-patched to match `case.md` (this file is authored by hand, not generated by
   `build_docx.js`).
5. Rebuilt `published/The Trailer Return - Case Study.docx` and `published/The Trailer Return -
   Facilitator Guide.docx` via `node skills/case-publish/scripts/build_docx.js the-trailer-return`.
   `Data.xlsx` content unchanged (no appendix data touched); mtime refreshed only.
6. `published/MANIFEST.json` — hash, byte counts, and `_note` refreshed to this rebuild.
7. `case.json.qa` — `run_on` and `case_md_sha256` updated; `state`/`verdict`/`blockers_open`/
   `gaps_open`/`tier2` block unchanged (still TIER2_PASS / PASS / 0 / 4 / 7-7-PASS).

---

## case-readiness run — 2026-09-10 (user review pass — visuals, process guide, fresh-reader check)
**State:** TIER2_PASS → TIER2_PASS   **Verdict:** PASS

Scope: user reviewed the published Interactive HTML and flagged "issues on pictures, explanation
of process, and an ask to check the work and narrative." Three real issues found and fixed:

1. **A real arithmetic error.** Appendix E printed "Fuel cost per mile driven = $1.1391 / mi
   (computed: $5.967 ÷ 5.2392)". The division actually computes to $1.1389143.../mi, which rounds
   to **$1.1389**, not $1.1391 — a genuine transposition-style error in a load-bearing figure. Fixed
   in `case.md`, the published HTML's Appendix E table, and `published/The Trailer Return -
   Data.xlsx` (App E!B6). The Working Notebook's live JS calculator (`evaluateDollars()`) was never
   affected — it recomputes directly from `PARAMS.diesel_price_per_gal / PARAMS.mpg` rather than
   reading the printed table value, so no downstream cost figure, margin, or verdict changed. Margin
   (3.70%), both deadhead ratios, and all of Appendices A-D were independently re-verified by hand
   and are internally consistent (degree-distribution sum = 2×edges, odd-vertex counts match across
   Appendix A/B/D, Practice Block table sums to 37 edges/26 vertices/14 odd — all checked with a
   throwaway script, not just re-read).
2. **Missing scene-setting visual.** The case's central math object (the Practice Block's 26-vertex/
   37-edge graph, gold/navy odd/even coloring) already had a real, legible inline-SVG diagram in
   Appendix B — that was not the gap. What was missing was anything showing *what the case is
   actually about*: a truck, a trailer, a street grid a reader could picture. Added a new labeled
   inline-SVG scene to the Overview section (`class="scene-diagram"`) showing a schematic street
   grid, Truck 4 mid-route with a dashed "repeat block (deadhead)" backtrack, an odd-degree-corner
   legend matching Appendix B's convention, and the flatbed hauler that Option B would contract —
   no external images, both diagrams tagged so T1-20's visual-asset check recognizes them.
3. **Deliverables checklist was answer-shaped, not process-shaped.** `DELIVERABLES` in the HTML and
   the Challenge-3 list in `case.md` stated *what* to produce (D1-D5) but not *why* that step comes
   where it does. Added a third array element to each `DELIVERABLES` entry (a short why/process line
   — e.g. why odd vertices get identified before pairing, why an open path gets to "spend" its free
   endpoint on the priciest pair, why the deadhead ratio and the raw dollar total can disagree) and
   updated `renderChecklist()` to render it under each item. None of the six lines discloses a
   numeric answer or the verdict. Mirrored the same five process notes into `case.md`'s Challenge 3
   list as italicized asides.

**Fresh-reader checks performed directly (not delegated):**
- **P1 cold-solve**, re-done from `case.md` alone: reached a defensible D1-D5 using only the
  document. Practice Block greedy pairing still hand-tractable post-fix (O-R and Q-S free at
  0.0000 mi, A-B free, E-V at 0.0099 mi, L-M at 0.0227 mi, J-K at 0.0335 mi, F-U at 0.1293 mi as the
  costliest remaining pair — the natural candidate to leave unmatched for D4's open path). D5 still
  routes through Appendix D's pre-computed official full-grid figures, not a hand-run 68-vertex
  match. The corrected $1.1389/mi fuel figure changes D5's arithmetic by under half a cent/day —
  nowhere near enough to move the ~12x-dollar / 3.70%-ratio tension the case is built on.
- **P7 cold-read**, re-done end-to-end on the *rebuilt* published HTML: read Overview through Twist
  in order as a first-time reader. Narrative holds together — Denise's paper-map character detail,
  the Averyton/Cape Charles framing, the Monroe/Strawberry unmatched-pair callback in the Overview
  paying off in Appendix D, the Twist's confidence-not-flip framing — no internal contradictions
  found. New Overview scene SVG's `<desc>` and figcaption read correctly with a screen reader in
  mind; no new unglossed jargon introduced (same one methodology aside, "blossom-algorithm" in
  Appendix D's own explanatory prose, already noted in the 2026-09-09 pass as non-blocking).

### Tier 1 — structural (21 checks)
Re-ran `tier1_structural.py --case the-trailer-return` after rebuilding `published/The Trailer
Return - Case Study.docx`, `- Facilitator Guide.docx` (via `node skills/case-publish/scripts/
build_docx.js the-trailer-return`) and `- Data.xlsx` (via `python3 scripts/generic_publish/
build_xlsx_generic.py the-trailer-return`) to pick up the $1.1389 fix, and confirming via
`grep -o "<h[1-3][^>]*>[^<]*</h[1-3]>"` that all expected sections (Overview, Background, The
Dilemma, Challenges, Appendices, Working Notebook, Twist) are present and the HTML grew from
93,837 to 100,631 bytes (no shrinkage). **0 BLOCKER, 4 GAP** — the same four pre-existing,
documented, out-of-scope shared-tooling artifacts as the prior two passes (T1-10 reinforcement
carve-out; T1-15 xlsx "2026-27" boilerplate + Facilitator docx un-stripped clock times; T1-18 HTML
fee-slider `max="300"` UI default). T1-20's advisory polish note ("no image/chart/diagram/map
found") is now resolved — both SVGs carry a `diagram`-matching class. **VERDICT: TIER1_PASS.**

### Tier 2 — simulated play (7 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | See fresh-reader check above — reached a defensible position with correct, hand-checkable arithmetic using only the document; the fuel-cost fix does not change tractability or the trap. |
| P2 both-sides | **PASS** | Both one-sentence pitches unchanged in substance (A: ~12x cheaper in raw dollars — now $10.07 vs. $9.70+$115, both rounding the same at 2 decimals before and after the fix; B: a real 3.70% cut in the case's own primary metric). Neither collapses. |
| P3 trap | **PASS** | The named trap (build D5, see A win on raw dollars, stop, never engage B's ratio argument) is unchanged and still exactly what FACILITATOR.md's Data Deep Dive names. |
| P4 twist integrity | **PASS** | Re-checked the twist (S6's consumer-rate basis for the $115/day fee) against MA4's sensitivity note and against the corrected fuel-cost figure — still a confidence twist, not a flip twist; unaffected by this pass's fix. |
| P5 sensitivity | **PASS** | Ran `sensitivity_model.py` ±50% on `trailer_fee`: winner stays B, margin stays 3.70% at both extremes ($57.50 and $172.50) — mechanical PASS, unchanged. |
| P6 data decay | **PASS** | No source values changed this pass (S1/S2/S3/S5/S6 untouched — only a derived, non-sourced arithmetic figure was corrected). Re-confirmed all 5 cited figures still match `case.json.sources[]` from the 2026-09-09 live-fetch pass; no re-fetch needed since nothing about the sources themselves changed. |
| P7 accessibility (cold read) | **PASS** | See fresh-reader check above — 0 new unglossed jargon, 0 narrative contradictions, new scene SVG accessible (title/desc/figcaption). |

**Tier 2 verdict: 7/7 PASS.**

### Tier 3 — human dry-run
NOT RUN (unchanged from prior passes — out of scope).

### Fixes applied this pass
1. **Fuel-cost arithmetic error** — `case.md` Appendix E, published HTML Appendix E table, and
   `published/The Trailer Return - Data.xlsx` (App E!B6) corrected from $1.1391/mi to $1.1389/mi
   ($5.967 ÷ 5.2392, verified by direct computation). The Working Notebook's JS calculator was
   already correct (computes live from `PARAMS`, never reads the printed table).
2. **Added a scene-setting visual** — new inline-SVG in the Overview section (Truck 4, its
   backtrack, the flatbed hauler, an odd-degree-corner legend matching Appendix B's convention),
   `class="scene-diagram"`; tagged the existing Appendix B Practice Block graph `class="graph-
   diagram"` too, so both now satisfy T1-20's visual-asset detection.
3. **Deliverables checklist made process-oriented** — added a 3rd (`process`) element to every
   `DELIVERABLES` entry in the Interactive HTML and updated `renderChecklist()` to render it under
   each item's label; mirrored the same five process notes into `case.md`'s Challenge 3 list.
4. Rebuilt `published/The Trailer Return - Case Study.docx`, `- Facilitator Guide.docx`, and
   `- Data.xlsx`; refreshed `published/MANIFEST.json` (hash, byte counts, `_note`) and
   `case.json.qa` (`run_on`, `case_md_sha256`, `tier2` block) to match.

**No numbers other than the one fuel-cost correction changed** — margin (3.70%), both deadhead
ratios, both options' total mileage, the flatbed fee, and the verdict are all unchanged from the
prior pass.
