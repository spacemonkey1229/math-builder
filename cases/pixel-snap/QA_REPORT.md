# QA Report — Pixel Snap

## case-readiness run — 2026-09-12
**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case pixel-snap` — found 2 real advisory
leaks on the first run: Appendix E's MA2 row named "the Twist" by name in student-facing text
(`case.md` line 147), and MA4's row referenced "facilitator materials" (line 149) — both fixed by
rewording (removing the literal words "Twist"/"facilitator" from the student-facing table cells
without changing either row's actual content or figures). Re-run: clean, 0 findings.

### Artifacts built this pass

- `cases/pixel-snap/sensitivity_model.py` — new. `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()`
  contract per `skills/case-readiness/scripts/example_sensitivity_model.py`. Reproduces
  `case.json.balance.margin_basis`'s whole-month, shared-budget computation exactly: base
  ratio_A=4.80, ratio_B=4.08 ha/analyst-hour, winner=True Lock (B), margin=15.0% (matches
  `case.json`/`FACILITATOR.md` to the stated precision). `FLEX` sweeps exactly the three dials
  this task named: `tree_edge_m` (MA1), `true_lock_rmse_m` (MA3), and `n_concessions` (MA4/MA7
  combined, per MA4's own definition that the monthly budget equals
  `n_concessions x fast_lock_hours_per_scene`). `evaluate()` returns the NEGATIVE of the real
  ratios (documented in the module docstring) so the generic Tier 2 harness's higher-is-better
  `max()` convention correctly recovers True Lock as the winner, matching the case's own
  lower-ratio-wins metric.
- `cases/pixel-snap/published/Pixel Snap - Interactive.html` — new, built from
  `templates/interactive_shell.html` per `templates/INTERACTIVE_HTML_CONTRACT.md`. 12-term math
  `GLOSSARY` (Congruent, Similar, Transformation, Translation, Dilation, Scale Factor, Coordinate
  Plane, Origin, Quadrant, and the three How-To skills) — all `mathsisfun.com` links freshly
  fetched and confirmed on-topic this session (2026-09-12). A separate 5-term `STORY_GLOSSARY`
  (Image Registration, Ground Control Point, Sentinel-2, Geolocation Accuracy, Ascending/
  Descending Orbital Pass) using `class="sterm"`/`{desc, link}`, linking to the case's own
  already-verified real sources (Copernicus, NOAA CORS, eoPortal) rather than the math allowlist
  domains. A Working Notebook with 5 stepboxes (D1 translation vector, D2 dilation scale factor,
  D3 y-axis reflection, D4 GCP quadrant, D5 per-scene ratio) whose check functions call a JS port
  of `sensitivity_model.py`'s `evaluate()`/`naiveRatios()`, never a hardcoded literal. `node
  --check` confirms the inline `<script>` block parses with no syntax errors (`tier1_structural.py`
  T1-23 also confirms this mechanically).
- `cases/pixel-snap/build_xlsx.py` and `cases/pixel-snap/published/Pixel Snap - Data.xlsx` — new
  (openpyxl). Appendices B/C/D/Modeling-Assumptions as data sheets, plus a blank D1-D5 work area.
  Raw values only — the ratio comparison is left for the student.
- `cases/pixel-snap/published/Pixel Snap - Case Study.docx` and
  `cases/pixel-snap/published/Pixel Snap - Facilitator Guide.docx` — new, via
  `skills/case-publish/scripts/build_docx.js` (ran cleanly, not skipped).
- `cases/pixel-snap/published/MANIFEST.json` — new.
- `cases/pixel-snap/FACILITATOR.md` — rewritten to the mechanical anchor-ladder shape
  `tier1_structural.py` T1-13 requires (Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/Lessons
  Learned/Standards Touched On, a timed 45-minute Socratic table, 5 named Socratic questions). All
  of the ORIGINAL content (both arguments, the margin, the trap, the twist, the five Socratic
  questions, the cohort bands) was preserved and reorganized, not replaced — this is a structural
  conformance fix, not a content change to the balance/margin/trap.
- `cases/pixel-snap/case.json` — added `deliverables[D5].skills` (was `[]`, which is a T1-11
  BLOCKER; added `geometry-coordinate-plane`, already a claimed standard, so this adds no new
  `new_coverage[]` claim), `derived{}` (the Data-Deep-Dive intermediate m²/ha figures),
  `cohort_bands[]` (T1-17), `sensitivity_disclosure[]` (one Category-F entry for `n_concessions`,
  closing a genuine P5 FAIL — see below), strengthened `balance.argument_a`/`argument_b` with real
  quantitative figures (20 min, 4 hr, 100 min, <5 m, <12 m, 3 m, $180 — closing a genuine P2 FAIL,
  see below; no verdict/margin/winner language was added), and the `qa` block below. No
  `readmodel/*.json` file touched, per this task's explicit scope limit.

### Tier 1 — structural (23 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case pixel-snap` → **0 BLOCKERs, 4
GAPs, 2 POLISH** (after the fixes above; the first run found 2 BLOCKERs — T1-11 D5-skills-empty and
T1-13 anchor-ladder-incomplete — both fixed as described above).

| id | result | note |
|---|---|---|
| T1-01..T1-07, T1-09, T1-11..T1-14, T1-17..T1-23 | PASS | structural sections, boilerplate, appendices, citations, balance test, learning-goal reachability, facilitator artifacts, continuity, cohort bands, interactive HTML present/fresh/leak-free, 12-term math glossary on allowlisted domains, 5-term story glossary, visual-asset polish note only, published HTML section parity, inline `<script>` parses |
| T1-08 | GAP | LOW-confidence source present (S11, the conservation-cost overview page) — confirmed: S11 informs MA8 only, and `case.json` already states MA8 "does not enter the D5 hectares-per-analyst-hour calculation; narrative and Appendix D context only." No constraint or dilemma-flipping quantity traces to S11. |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out (`case.json.reinforcement_note`), same precedent as `the-repeat-match`, project-owner approved 2026-08-17 amendment, correctly downgraded from BLOCKER, not silently resolved. |
| T1-15 | GAP | 1 number (45.0) in the Facilitator Guide docx (the "45-minute Socratic plan" heading itself) has no literal match in case.md/case.json — a section-title numeral, not a data figure; harmless. |
| T1-16 | GAP | no `case_md_sha256` recorded yet — expected on a first run, closed below by this run's own `qa` block. |

**VERDICT: TIER1_PASS (0 blockers, 4 gaps).**

### Tier 2 — simulated play (6 probes, per this task's explicit scope)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS (with a flagged finding)** | Read only `/tmp/coldsolve-pixel-snap/PACKET.md` (case.md's student-facing content) as a fresh solver. Reached a defensible position (True Lock, using the case's own hectares-per-analyst-hour metric) but the exercise surfaced the exact risk this task asked to check: **D5's own instruction text ("divided by the analyst-hours each method costs (Appendix D)") and Appendix D's own PER-SCENE hours (20 min / 4 hr) most naturally produce the NAIVE ratio — Fast Lock 4.8 ha/hr vs. True Lock 0.24 ha/hr, a ~95% gap — not the whole-month, shared-budget ratio (4.8 vs. 4.08, 15.0%) that `case.json.balance.margin_basis` actually records.** The only textual signal in case.md pointing a solver toward the whole-month reframing is Appendix E's "Sensitivity note (MA4/MA5/MA6/MA7 together)" paragraph, which explicitly says: *"How much that matters depends on what you assume happens to the other 4 concessions' scenes that month — and that is exactly the kind of judgment call Challenge D5 asks you to make explicit, not one this appendix makes for you."* This sentence IS present in `case.md` (not facilitator-only), so a diligent solver who reads Appendix E in full before writing D5 has everything needed to derive the whole-month framing independently — but a hurried solver who works Appendix C/D's numbers directly into D5 without cross-reading Appendix E's assumption note will land on the naive ~95% figure and never know a different, case-of-record answer exists. **This matches `FACILITATOR.md`'s own documented "trap" exactly** ("Students compute D5's per-scene ratio... without noticing the ratio is per scene, while True Lock's real cost is hours taken from a shared, fixed monthly budget") — i.e., this is not a broken case, it is the case's intended teaching mechanism working as designed. Recording as PASS rather than FAIL because the reframing IS derivable from `case.md` alone by a careful reader, per this task's explicit instruction to report (not silently patch) ambiguity — but flagging clearly that this is a real, load-bearing ambiguity a facilitator must be ready to resolve, not a hypothetical one. |
| P2 both-sides | **PASS** (mechanical FAIL fixed — see Artifacts above) | First run: `probe_both_sides` mechanically FAILED both `argument_a`/`argument_b` for carrying "almost no numbers" — true on inspection; both arguments cited Appendix letters but no actual figures. Fixed by adding real quantities (20 min, 4 hr, 100 min, 5 m, 12 m, 3 m, $180, 2.4x) to both arguments without adding any verdict/margin/winner language. Re-run: mechanically READY. Adjudication: Option A's case (stays inside the fixed 100-minute monthly budget with room to spare, bounded whole-pixel worst-case error under Sentinel-2's own published spec) and Option B's case (removes most of a real, already-costly smear; a defensible single-highest-priority-concession argument) are both genuinely defensible from the case's own numbers alone. Neither collapses to a bare concession. |
| P3 trap check | **PASS** (mechanical FAIL fixed — see Artifacts above) | First run: `probe_trap`'s regex captured the wrong text (the top-of-file "Do not distribute... trap may live" disclaimer, matched as the "named trap" before the real trap paragraph, because the disclaimer's own use of the word "trap" came first in the file). Fixed by rewording the disclaimer to "wrong-path analysis" without touching the actual trap paragraph. Re-run: mechanically READY, correctly extracting `FACILITATOR.md`'s real trap text ("students compute D5's per-scene ratio... and declare True Lock the unconditional right answer — without noticing the ratio is per scene..."). Adjudication: this is exactly the wrong path a competent, hurried solver produces (confirmed directly by this session's own P1 cold-solve run, above) — the guide names the trap that will actually catch the room. |
| P4 twist integrity | **PASS (finding disclosed)** | `evaluate_twist()` resets True Lock's achieved RMSE on Kutai to the native/unregistered 12 m figure (modeling "the flagged ribbon sits in a cloud-covered quadrant this month"). Result: Policy B's ratio rises from 4.08 to exactly 4.80 ha/hr — **the margin collapses to ~0% (a near-tie), it does not flip outright to Fast Lock.** This does invalidate a real position a room would hold ("True Lock is worth the hours, full stop") — the twist shows that advantage is entirely contingent on the flagged ribbon sitting in the one GCP-covered quadrant. The twist's exact numeric effect depends on the modeling choice "assume the worst case, the ribbon IS in a cloud-covered quadrant" — the case's own narrative frames this as a conditional ("if this month's flagged ribbon sits in one of the cloud-covered quadrants"), not a certainty, so this is a disclosed convention (recorded in `sensitivity_model.py`'s `evaluate_twist()` docstring), not an unstated one masquerading as fact. |
| P5 sensitivity | **PASS (disclosed)** | First run: mechanical FAIL — `n_concessions` at +50% (7.5) flips the winner from True Lock to Fast Lock (margin -31.0%, i.e. Fast Lock now ahead), with no matching `sensitivity_disclosure[]` entry. Fixed by adding a Category-F entry (irreducible scenario-count assumption, cannot be pinned down by more research) with a real, specific justification naming both the flip direction and magnitude. Re-run: PASS (disclosed). Full sweep: `tree_edge_m` ±50% — no flip, margin unchanged at 15.0% (both options' areas scale together). `true_lock_rmse_m` ±50% — no flip; margin ranges 12.5%-17.5%. `n_concessions` ±50% — **FLIPS** at +50% (winner becomes Fast Lock, margin 31.0%); at -50% margin widens to 75.0% (toward the naive per-scene figure) without flipping. `n_concessions` is confirmed the single most load-bearing, and only genuinely unstable, dial in this case, exactly matching `case.json.sensitivity_note`'s own prose. |
| P6 data decay | **PASS** | All 11 `sources[]` URLs (S1-S11) individually re-fetched this session (2026-09-12) via WebFetch (S8 additionally confirmed via the Semantic Scholar API, since the paper's own page is JS-rendered and returns no static text to a scraping fetch). All 11 reachable and each cited figure/claim confirmed still present, matching `case.json` exactly. Zero dead links, zero drifted figures. Per-URL summary: S1 (Copernicus dataspace docs, 10/20/60 m bands, 110x110 km tiles) ✓; S2 (USGS EarthExplorer, login-required-to-download) ✓; S3 (AWS Open Data, `s3://sentinel-cogs`, `--no-sign-request`, no account) ✓; S4 (Copernicus Data Space Ecosystem, free instant access) ✓; S5 (eoPortal, 786 km / 98.6° / 10:30 LTDN) ✓; S6 (same Copernicus dataspace docs page as S1, 110x110 km tiles) ✓; S7 (Copernicus Sentinel-2 L2A product page, <12 m / <5 m at 95.5%) ✓; S8 (Dai & Khorram 1998, IEEE TGRS — title/authors/venue/year confirmed via Semantic Scholar's API) ✓; S9 (Brinck et al. 2017, PMC, ~50 million km edge / 295 million ha within 100 m) ✓; S10 (NOAA CORS Network, real public GNSS reference network) ✓; S11 (Donate to Wildlife Conservation, $150-300/scout/month, $25,000-30,000/14-scout unit) ✓. |

**VERDICT: TIER2_PASS** — all six in-scope probes recorded by name, 0 unresolved FAIL. Two
mechanical FAILs (P2, P5) were closed by strengthening `case.json`'s own disclosed content (real
numbers in the balance arguments; a Category-F sensitivity disclosure), never by touching
`case.md`'s student-facing text or by inventing a result. One structural FAIL surfaced by the
readiness pass itself (P3's trap-extraction regex hitting boilerplate text) was closed by a wording
fix that changed no content. The P1 finding about the month-scale framing's derivability is
recorded as a genuine, load-bearing observation, not silently resolved — see the note above and
the flag in the closing summary.

### `sensitivity_model.py` full sweep output (2026-09-12)

```
Base: A=4.8000 ha/hr  B=4.0800 ha/hr  winner=B  margin=15.00%
Twist (cloud-covered quadrant -> True Lock loses its edge on Kutai): A=4.8000 ha/hr  B=4.8000 ha/hr  winner=B  margin=0.00%

tree_edge_m          +50%   A=  7.2000  B=  6.1200  winner=B  margin= 15.00%
tree_edge_m          -50%   A=  2.4000  B=  2.0400  winner=B  margin= 15.00%
true_lock_rmse_m     +50%   A=  4.8000  B=  4.2000  winner=B  margin= 12.50%
true_lock_rmse_m     -50%   A=  4.8000  B=  3.9600  winner=B  margin= 17.50%
n_concessions        +50%   A=  4.8000  B=  6.9600  winner=A  margin= 45.00% <-- FLIPS, CAP-BREACH(>20%)
n_concessions        -50%   A=  4.8000  B=  1.2000  winner=B  margin= 75.00% <-- CAP-BREACH(>20%)
```
(The +/-31.0%/45.0% figures quoted in the P5 table above are `tier2_probes.py`'s own recomputation
using its `winner/loser` margin convention, which differs slightly in which value is the
denominator from `sensitivity_model.py`'s `__main__` report above, which always divides by Option
A's value per `case.json.balance.margin_basis`'s own stated convention. Both are the same
underlying arithmetic; see each script's own comments for the convention it uses.)

### Tier 3 — human dry-run

NOT RUN. No `cases/pixel-snap/runs/` directory exists yet. Required before `VERIFIED`, not before
this `TIER2_PASS`.

### Next step

`case-publish` may run once a human reviews this report, in particular the P1 finding above (the
month-scale framing is derivable from `case.md` alone but only via a careful cross-read of
Appendix E — a facilitator should be briefed to expect the naive ~95% answer from most solvers, not
surprised by it). `readmodel/cases_index.json`, `readmodel/standards_spine.json`, and
`readmodel/gap_queue.json` were **not** touched by this run, per this task's explicit instruction —
those remain `case-publish`'s responsibility.

## case-readiness run — 2026-09-14 (re-verification after the "polish pass")

**Context.** `case.md` and the published Interactive HTML were edited by a "polish pass" since the
last run above: a whole-pixel-vs-sub-pixel comparison diagram was added to the HTML, "why this
methodology" notes were added under D1–D5 in both `case.md` and the HTML, and `.docx`/`.xlsx` were
rebuilt. That pass self-updated `case.json.qa.case_md_sha256` to match the new `case.md` content
**without an actual re-run of the gate**. This entry is that real re-run — full fresh Tier 1 +
Tier 2, not a rubber-stamp of the self-certified hash.

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Hash check

`shasum -a 256 cases/pixel-snap/case.md` → `90adda1844b9123956b0639cfba1da1a6ddaf306541f0576f1fee70ceec78d24`
— matches `case.json.qa.case_md_sha256` exactly. The self-certified hash was in fact accurate to
the current file content (it just wasn't backed by a real Tier 1/Tier 2 run at the time it was
written — that gap is what this entry closes).

### Preflight lint

`python3 skills/case-readiness/scripts/preflight_lint.py --case pixel-snap` → **clean, 0 advisory
findings.** In particular, the new D1–D5 "why this methodology" prose in `case.md` (added by the
polish pass) does **not** leak any margin/winner/threshold content — confirmed both by the linter
and by manual read: the D5 "why" paragraph discusses *why* the ratio's denominator is a judgment
call and points to Appendix E, but never states the 15.0% margin, the winner, or the whole-month
numbers themselves.

### Tier 1 — structural (23 checks), fresh run

`python3 skills/case-readiness/scripts/tier1_structural.py --case pixel-snap` → **0 BLOCKERs, 3
GAPs, 2 POLISH.** `case.md` genuinely changed since the last run, so this was not assumed to still
pass — it was re-run in full.

| id | result | note |
|---|---|---|
| T1-01..T1-07, T1-09, T1-11..T1-14, T1-16..T1-23 | PASS | all structural sections, boilerplate, appendices/citations, balance test, learning-goal reachability, facilitator artifacts, cohort bands, continuity (`FACILITATOR.md`/case.json agree with the new case.md), interactive HTML present/fresh/leak-free (including the new diagram section), math + story glossaries, published HTML section parity, inline `<script>` parses |
| T1-08 | GAP | unchanged from prior run — S11 (LOW confidence) informs MA8 narrative context only, does not enter the D5 calculation |
| T1-10 | GAP | unchanged — `new_coverage[]` empty, reinforcement carve-out per `case.json.reinforcement_note`, still valid |
| T1-15 | GAP | unchanged — the "45.0" section-title numeral in the rebuilt Facilitator Guide docx, harmless |

**VERDICT: TIER1_PASS (0 blockers, 3 gaps)** — same gap profile as the prior run; nothing new
introduced by the polish pass.

**Note (non-blocking):** T1-20 mechanically reports "no image, chart, diagram, or map found," but
the polish pass's new whole-pixel-vs-sub-pixel `<svg>` diagram (with real `<rect>`/`<path>`
content, `role="img"` + `aria-label`) is visibly present in the published HTML around line 335.
T1-20 is advisory/POLISH-only and never blocks, so this doesn't affect the verdict, but it's worth
flagging as a checker false-negative for whoever next touches `tier1_structural.py`'s T1-20 visual
detector — it appears not to recognize a `<div class="card" role="img">`-wrapped SVG the way it
recognizes other visual containers.

### Tier 2 — simulated play, all 6 in-scope probes fresh

| probe | verdict | finding |
|---|---|---|
| **P1 cold solve** | **PASS** | Dispatched a genuinely fresh subagent with zero prior context, given only `/tmp/coldsolve-pixel-snap/PACKET.md` (this pass's own re-generated, leak-free copy of the current `case.md`). **Direct test of this task's central question: does the new D5 "why" note make the month-scale reframing reliably findable now?** Result: **yes, materially improved.** The solver still computed D5's primary ratio using **per-scene** hours (reaching True Lock by an even larger, ~20x naive margin) — but unlike the pre-polish-pass finding, it explicitly surfaced the shared-monthly-budget collision unprompted, in response to "what's the strongest argument against your choice," citing MA4/MA6/MA7 by name and echoing the case's own language ("case-defining assumption"). It made an examined, stated choice about the ratio's denominator ("I used per-scene hours... because the monthly-budget collision is a separate capacity problem, not a property of the registration method itself"), exactly matching what D5's own instruction text now explicitly permits ("decide deliberately... and say which you chose and why"). This is a real improvement over the prior run's finding that a hurried solver "will land on the naive ~95% figure and never know a different, case-of-record answer exists" — this solver knew, named it accurately, and made a defensible, disclosed choice not to fold it into the D5 ratio itself. Passing per the probe's own criterion (a defensible position, correct-for-its-own-premises arithmetic, a named metric) — not a silent miss of the reframing. **Facilitator implication, unchanged from before:** a room will likely still open on the naive ~95% number; the guide's Anchor 2/3 Socratic questions and the Data Deep Dive's explicit whole-month table remain necessary to land the case's actual 15% margin, but a diligent solver is now demonstrably more likely to flag the ambiguity themselves before the facilitator has to raise it. |
| **P2 both-sides** | **PASS** | `case.json.balance.argument_a`/`argument_b` (unchanged content from prior run — the polish pass touched `case.md`'s D-note prose, not the balance block) both carry real figures (20 min, 4 hr, 100 min, <5 m, <12 m, 3 m, $180, 2.4x) and neither collapses to a bare concession. Re-confirmed by direct read this session. |
| **P3 trap check** | **PASS** | `FACILITATOR.md`'s named trap ("students compute D5's per-scene ratio... and declare True Lock the unconditional right answer — without noticing the ratio is per scene...") is exactly the wrong path this session's fresh P1 cold-solve run actually took (per-scene ratio, ~20x margin) before self-correcting via Q4. The guide names the trap that will actually catch the room, confirmed directly against this session's own live cold-solve, not just by inspection. |
| **P4 twist integrity** | **PASS (disclosed)** | Re-ran `sensitivity_model.py`'s `evaluate_twist()` fresh: base A=4.8000, B=4.0800, margin 15.00%, winner B; twist (cloud-covered quadrant) A=4.8000, B=4.8000, margin 0.00%. Matches `FACILITATOR.md`'s twist section exactly. The twist collapses True Lock's edge to a near-tie, it does not flip to Fast Lock outright — consistent with the case's own conditional framing ("if this month's flagged ribbon sits in one of the cloud-covered quadrants"), a disclosed convention, not an unstated one. |
| **P5 sensitivity (±50%)** | **PASS (disclosed)** | Fresh run of `sensitivity_model.py`'s full sweep via `tier2_probes.py --case pixel-snap`. `tree_edge_m` ±50%: no flip, margin stays 15.0%/12.5%-17.5% range as area scales symmetrically. `true_lock_rmse_m` ±50%: no flip, margin ranges 12.5%–17.5%. `n_concessions` ±50%: **flips** at +50% (winner → Fast Lock/A, margin -31.0% per `tier2_probes.py`'s winner/loser convention), and widens to -75.0% (toward the naive figure) at -50% without flipping. This exact instability is disclosed in `case.json.sensitivity_disclosure[]` (Category F, irreducible scenario-count assumption) — PASS per the disclosure-aware pass state, not a silently-stable claim. |
| **P6 data decay** | **PASS** | All 11 `sources[]` URLs re-fetched fresh this session (2026-09-14) via WebFetch (S8 and S9 additionally verified via the CrossRef and Europe PMC REST APIs respectively, since their own pages are JS-rendered/reCAPTCHA-gated to a plain fetch — same workaround the prior run used). All 11 reachable, zero dead links, zero drifted figures: S1 (Copernicus dataspace docs — 4/6/3 bands at 10/20/60m confirmed, though the page text doesn't spell out individual band letters or the exact 10,980×10,980 pixel count — those are a correct derivation from the page's stated 110×110km tile size, not independently printed on the page) ✓; S2 (EarthExplorer — login required to download, confirmed) ✓; S3 (AWS Open Data, `s3://sentinel-cogs`, `--no-sign-request`, no account, confirmed) ✓; S4 (Copernicus Data Space Ecosystem, free instant access, confirmed) ✓; S5 (eoPortal, 786km/98.6°/10:30 LTDN, confirmed) ✓; S6 (same Copernicus dataspace page, 110×110km tiles, confirmed) ✓; S7 (Copernicus Sentinel-2 L2A page, "< 12 m at 95.5% confidence of Absolute Geolocation" and "< 5 m at 95.5% confidence of Multitemporal Registration," confirmed verbatim) ✓; S8 (Dai & Khorram 1998 IEEE TGRS 36(5):1566-1577 — title/authors/venue/year/pages confirmed via CrossRef API since the Semantic Scholar page itself returned empty/rate-limited to WebFetch) ✓; S9 (Brinck et al. 2017 Nat Commun — confirmed via Europe PMC full-text API with exact quotes: "the length of the world's tropical forest edges sums to nearly 50 million km" and "295 million ha (19%) of tropical forest area is <100 m from the forest edge," matching `case.json` exactly) ✓; S10 (NOAA CORS Network, confirmed) ✓; S11 (donatetowildlifeconservation.com, $150-300/scout/month and $25,000-30,000/14-scout/year, confirmed verbatim) ✓. |

**VERDICT: TIER2_PASS** — all six in-scope probes independently re-verified this session, 0
unresolved FAIL, 0 silent gate-through. The self-certified hash update from the polish pass held up
under genuine re-verification: no new BLOCKER, no new mechanical FAIL, and the one open pedagogical
question this task specifically asked about (does the new D5 "why" note make the month-scale
finding more findable?) resolved favorably — a fresh solver now surfaces the reframing explicitly,
though the case's own design still permits a defensible per-scene reading, so the facilitator
should not expect the room to arrive at the 15% figure unprompted.

### Tier 3 — human dry-run

NOT RUN (unchanged). No `cases/pixel-snap/runs/` directory exists.

### Next step

`case.json.qa` updated below with today's date. No change to `readmodel/*.json` — out of scope for
this run, per instruction.
