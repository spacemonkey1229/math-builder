# QA Report — The Point Cloud Match

## S4 data-decay fix + re-gate — 2026-09-12 (this run)

**State:** TIER1_PASS (blocked on P6) → **TIER2_PASS**. The prior run's single open issue — S4
(a Novedge scan-to-CAD article) had rotted to different, generic live content that no longer
supported its cited 0.005mm/0.8mm tolerance figures — is fixed. `case.json.sources[]` S4 was
replaced with a real, live, directly-verified source: Kenely et al., "Large-Scale Photogrammetric
Documentation of St. John's Co-Cathedral" (arXiv:2604.24316), which reports actual measured
multi-scan photogrammetric registration point error (0.9–1.3mm mean, 3.2mm peak, 5.8mm
cross-cluster) — a better-fitting source than the original, since it measures the real quantity
MA1 approximates rather than a manufacturing-tolerance analogy. MA1's value (1.0mm) did not
change — it already sits inside this source's real measured range — so no downstream margin,
balance, or derived figure changed. `case.md` (Appendix D note, Appendix E MA1 basis, Appendix G
S4 row), `case.json.sources[]`, and the published HTML/docx/xlsx packet were all updated and
rebuilt. Full detail in `RESEARCH_LOG.md`'s 2026-09-12 addendum.

All 6 Tier 2 probes were re-run this pass, including a full re-fetch of **all 5 sources** (not
just S4) for data decay: all confirmed live and matching. Tier 1 is clean (0 BLOCKERs, same 2
pre-existing honest GAPs as before). **This case now reaches `TIER2_PASS`.**

---

## case-readiness remediation run — 2026-09-12 (prior run in this session)

**State:** DRAFT → **TIER1_PASS**   **Verdict:** Tier 1 clean (0 BLOCKERs). Tier 2: 5/6 probes
PASS, **1 FAIL (P6, data decay)** — per this skill's own rule ("never mark `TIER2_PASS` with a
probe recorded as anything but a clean verdict"), the case does **not** reach `TIER2_PASS`. This
report is honest about that; the previous run's 7 BLOCKERs / 4 GAPs are fixed, but a new, real
issue was found live during Tier 2 and is not hidden.

---

## Fixes made to clear the prior run's 7 BLOCKERs

1. **T1-10 ×4 (new_coverage claims already at n=2).** `new_coverage[]` set to `[]`.
   `case.json.reinforcement_note` added, verified live against `readmodel/standards_spine.json`
   on 2026-09-12: `geometry-congruent`/`geometry-similar`/`geometry-how-to-reflect-a-figure-
   across-the-y-axis` are covered by Company Front / The Repeat Match, and `geometry-quadrant` by
   Airstrike / Urban Planner — all n=2, none crediting this case's title. Checked every other
   skill in Geometry/Coordinate Plane and Geometry/Transformations for a genuine adjacent gap:
   none exists (every skill in both groups is already n>=2, and none of the still-thin ones are
   forced by this case's actual D1–D5 deliverables). Same precedent as `the-repeat-match` and
   `pixel-snap`. `LEARNING_GOALS.md` and `FACILITATOR.md`'s "Standards Touched On" section
   rewritten to describe this honestly as a reinforcement case, not a gap-closer.
2. **T1-02 (uncleared "100%" in Overview).** Reworded "The progress bar hits 100%" to "The
   progress bar fills all the way" — same narrative beat, no numeral. No `overview_numerals_
   cleared[]` entry needed; the Overview now carries zero suspect numerals.
3. **T1-06 ×2 (orphaned Appendix E and G).** Both appendices are genuinely used (E grounds every
   Modeling Assumption in the case; G lists every source). Added one sentence to Background,
   before the Appendix A heading: "Any figure in this case that is not a real, sourced number is
   disclosed plainly as a stated Modeling Assumption (SEE APPENDIX E), and every source used to
   ground this case is listed in full in **APPENDIX G**." Also patched into the published
   Interactive HTML and updated `case.json.appendices[].referenced_from`.
4. **T1-13 preflight leak ("for the twist").** Appendix B's methodology note in `case.md` line
   124 reworded: "a different mirror axis, deliberately inconsistent with Marker 3's, for the
   twist" → "a different mirror axis than the one applied to Marker 3." The real geometric fact
   (Marker 4 uses a different mirror axis) is preserved; the meta-textual tell is gone. (The
   published HTML/docx already had this fixed from an earlier build; only `case.md` itself still
   carried the leak, which is what the preflight linter had caught.)

## GAPs addressed

- **T1-14/T1-15 (13 FACILITATOR.md numbers with no home in case.json).** Added
  `case.json.derived` with four sub-blocks (`D1_scientific_notation`, `D2_marker_distances_cm`,
  `D4_translation_check_cm`, `D5_ratios_mm_per_min`) carrying all 13 real figures, plus a
  `reference_notes` entry for the one comparison figure (0.09%, the Robotics Engineering
  exemplar margin, cited for comparison only, not this case's own data).

## Packet rebuild

Rebuilt after all `case.md`/`case.json`/`FACILITATOR.md` edits, before re-gating (per this
session's own standing rule against re-running Tier 1 on a stale packet):
- Docx pair rebuilt via `skills/case-publish/scripts/build_docx.js` (generic converter).
- Xlsx rebuilt via `scripts/generic_publish/build_xlsx_generic.py` (generic appendix extractor).
- Interactive HTML hand-patched in place for the same two content changes (Overview wording;
  Background Appendix E/G references) — no per-case `html_config.py` exists for this case to
  regenerate it through `scripts/generic_publish/build_html.py`; everything else in the HTML
  (glossary, PARAMS/FLEX/evaluate() port, twist toggle) is unchanged from the prior build.
- `MANIFEST.json` updated with new file sizes, new `case_md_sha256`, and a build note.

sha256(case.md) = `1f4dbac962ebc8f2398ce54ac51b0c66ae475002eb0f698215bc654e3541bdde`

---

### Preflight lint (advisory)

```
python3 skills/case-readiness/scripts/preflight_lint.py --case the-point-cloud-match
```
**Clean — no advisory findings.**

### Tier 1 — structural (23 checks)

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-point-cloud-match
```

| id | result | id | result | id | result |
|---|---|---|---|---|---|
| T1-01 | PASS | T1-09 | PASS | T1-17 | PASS |
| T1-02 | PASS | T1-10 | GAP  | T1-18 | PASS |
| T1-03 | PASS | T1-11 | PASS | T1-19 | PASS |
| T1-04 | PASS | T1-12 | PASS | T1-20 | PASS |
| T1-05 | PASS | T1-13 | PASS | T1-21 | PASS |
| T1-06 | PASS | T1-14 | PASS | T1-22 | PASS |
| T1-07 | PASS | T1-15 | GAP  | T1-23 | PASS |
| T1-08 | GAP  | T1-16 | PASS |  |  |

**checks run: 23  PASS 20 · GAP 3 · FAIL 0 → VERDICT: TIER1_PASS**

Remaining GAPs (all honest, none a defect requiring a fix before TIER1_PASS):
- **T1-08** — S4 was downgraded to LOW confidence after the Tier 2 P6 data-decay finding below
  (its cited figures no longer appear on the live page). T1-08 correctly flags LOW-confidence
  sources for human confirmation that none carries a dilemma-flipping quantity — MA1's 1.0mm
  tolerance is exactly this kind of quantity, which is why P6's finding is a real blocker on
  `TIER2_PASS`, not just a T1-08 footnote.
- **T1-10** — `new_coverage[]` empty, downgraded from BLOCKER via the reinforcement carve-out
  (`case.json.reinforcement_note` on file, per doctrine amendment 2026-08-17).
- **T1-15** — 1 numeric cell in `published/…Data.xlsx` (`README!A2 = 27.0`) has no match in
  case.md/case.json. This is `scripts/generic_publish/build_xlsx_generic.py`'s own hardcoded
  README subtitle text, `"MS | Math | Case Study | 2026-27"` (a generic school-year label baked
  into the shared script, not case-specific data) — the same artifact every case built with this
  generic script carries. Not fixed here: it is a shared-script quirk outside this case's scope,
  not a case-authoring defect, and not a BLOCKER.

POLISH (2, unchanged from before): T1-07 (label-parsing note, informational), T1-20 (no chart in
the HTML — a real but non-required authoring judgment call).

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Worked the case cold from `/tmp/coldsolve-the-point-cloud-match/PACKET.md` only. All of D1–D5's numbers reproduce exactly from the given data (D1: 9.75%; D2: M1–M2 distance is invariant at 11.848 cm both sets, M1–M3 collapses 16.755→4.206, M2–M3 grows 9.995→13.825, correctly reasoned to "neither congruent nor similar"; D3: reflecting Marker 3's expected coordinate across the y-axis lands exactly on its actual (9.47, 12.42); D4: (Δx,Δy)=(+3.00,+2.00) from Markers 1–2, predicted Marker 3 at (−6.47, 14.42), 160.65 mm from its actual position; D5: face-value margin 0.61% favoring A, real ratio ~1.785 mm/min for A once corrected, ~400x worse than B). Reached a defensible position (B) via the correct arithmetic route, not a guess — the Challenge sequencing (D2–D4 before D5) structurally forces the trap-detection route. |
| P2 both-sides | **PASS** | Best sentence for A: "Ship As Converged costs 0 additional minutes and the rig converged, with 2 of 3 markers landing exactly where expected." Best sentence for B: "Marker 3's actual position is 160.65 mm from where a pure translation predicts it should be — a reflection the rig can't self-detect — so shipping risks an $8,500 re-shoot to save 33 minutes that fit comfortably in the 50-minute window." A is a real, statable position at face value, and collapses specifically at D4's translation check once the 160.65 mm gap is computed — this is intentional trap-and-reveal case design (matches the FACILITATOR's own framing), not the "concession-only" fake balance the probe is built to catch. Both `balance.argument_a`/`argument_b` were rewritten with real supporting numbers (0 mm, 0.61%, 160.65mm, $8,500, 33 min, 50 min) to fix the probe's initial "carries almost no numbers" mechanical finding. |
| P3 trap check | **PASS** | Independently named the likely wrong path before reading the Guide Notes: "2 of 3 markers check out, ship it" (a majority-vote fallacy) — and separately, "trust the naive face-value D5 ratio without doing D2–D4." FACILITATOR.md names the first explicitly as **the trap** ("Two of three markers check out, so the scan is basically fine — ship it") and the second is directly interrogated by Socratic Question 2 ("what number are you trusting that you haven't verified?"). The guide anticipates the path that will actually catch the room. |
| P4 twist integrity | **PASS** | The twist (Marker 4 reflects across the rig's x-axis, not Marker 3's y-axis) is a fixed fact of the given coordinates — verified by hand: expected (−1.75, 18.73) reflected across x-axis → (−1.75, −18.73), which is exactly Marker 4's given actual position. It does not depend on any Modeling Assumption or its reading order (unlike Cold Chain's original defect), so there is no sequential-assumption ambiguity to break it. It genuinely invalidates the "3-marker recheck is obviously sufficient" position, which FACILITATOR.md's Thread 2 explicitly discusses as live, unresolved scope creep — not silently swept under the rug. |
| P5 sensitivity (±50%) | **PASS (disclosed)** | Ran `cases/the-point-cloud-match/sensitivity_model.py --probe 5` equivalent via `tier2_probes.py`. The case's real, trap-independent recommendation (B) never changes under ±50% of MA1/MA2/MA3 — it rests on the fixed 160.65mm geometric fact from D2–D4. The *naive, pre-trap face-value* D5 ratio does flip under +50% MA2/MA3 (a real, disclosed property of the case's own mm-per-minute metric rewarding more minutes at a fixed residual). Initially FAILED mechanically because `sensitivity_disclosure[]` was free-text; fixed by restructuring it into the required `{"param","category","justification"}` schema (Category X — proprietary/inaccessible one-time estimate, grounded in S3) for `marker_time_min` and `reexport_time_min`. Now `PASS (disclosed)` per the 2026-08-13 disclosure-aware pass state. Also written into FACILITATOR.md's Sensitivity note. |
| P6 data decay | **FAIL** | All 5 sources re-fetched live on 2026-09-12. **S1** (Stanford repository page): HTTP 200, every cited figure (35,947 / 69,451 / 566,098 / 1,132,830 / 543,652 / 1,087,716 / 362,272) still present verbatim. **S1b** (`bunny.tar.gz`): downloaded and re-parsed fresh — `bun_zipper.ply` header confirms 35,947 vertices / 69,451 faces exactly; all 10 raw per-pass files (`bun000`=40,256, `bun045`=40,097, `bun090`=30,379, `bun180`=40,251, `bun270`=31,701, `top2`=38,298, `top3`=36,023, `bun315`=35,336, `chin`=37,738, `ear_back`=32,193) sum to exactly 362,272 — an exact re-verification, not a reused prior claim. **S2**: HTTP 200, both quoted phrases ("Symmetries and repetitive patterns…", "Repetitive-feature scenes can defeat dozens of markers…") present verbatim. **S3**: HTTP 200, both quoted phrases ("Place the marker across multiple photos", "adjust the marker position in several different images where the same feature is visible") present verbatim. **S4 FAILS**: the URL is reachable (HTTP 200, stable across two independent fetches), but the live page's full text (28,846 chars after stripping markup) contains **none** of the specific figures case.json/case.md attribute to it — no "0.005", no "0.0002", no "0.030", no "0.8 mm" tolerance figure, no "CMM"/"metrology"/"tolerance-critical CAD rebuild" language anywhere on the page. The live article (dated "January 02, 2026" on the page itself) is a generic scan-to-CAD pipeline piece (FPFH/SHOT features, ICP variants, pose-graph optimization, VDI/VDE 2634) that never states a numeric tolerance range at all. This is exactly the failure mode the probe warns is worse than a 404: the URL resolves, so nothing in the pipeline would notice on its own, but MA1's sourced basis for the 1.0mm registration tolerance no longer checks out against the live source. **Not fixed here** — per the hard rule against fabricating a citation, no replacement source was substituted. This is a genuine, disclosed BLOCKER for reaching `TIER2_PASS`; `case-research` needs to either find where this content moved (if the article was edited/replaced at the same URL) or find a new source for the MA1 basis, or reframe MA1 without a live citation and rely on it being fully disclosed as a Modeling Assumption per Appendix E's own already-honest framing (Appendix E already says "not sourced," and MA1's basis paragraph in Appendix E and Appendix D both already hedge this range as approximate — but `case.json.sources[]` S4 currently states these numbers as if directly attributable to that URL, which the live page does not support). |

### Tier 3 — human dry-run

NOT RUN. Not eligible — case has not reached `PUBLISHED` (and cannot, until Tier 2 is clean).

---

## What would need to happen next

1. `case-research` re-verifies or replaces S4 (Novedge scan-to-CAD article) — either locate
   updated/moved content carrying the original tolerance figures, or find a new citable source
   for MA1's 1.0mm basis, or explicitly downgrade S4/MA1's sourcing claim to match what the live
   page actually supports.
2. Re-run Tier 2 probe 6 once S4 is resolved. If it passes and nothing else has drifted, this
   case reaches `TIER2_PASS` and is eligible for human confirm → `case-publish`.

## case.json.qa written by the run above (superseded below)

```json
{
  "state": "TIER1_PASS",
  "verdict": "BLOCKED",
  "run_on": "2026-09-12",
  "blockers_open": 0,
  "gaps_open": 3,
  "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS",
            "P5": "PASS (disclosed)", "P6": "FAIL"},
  "tier3_runs": [],
  "case_md_sha256": "1f4dbac962ebc8f2398ce54ac51b0c66ae475002eb0f698215bc654e3541bdde"
}
```

---

## Re-gate after the S4 fix — 2026-09-12 (same day, this run)

S4 was replaced (see top of this report and `RESEARCH_LOG.md`'s addendum). Packet was rebuilt
(docx pair via `skills/case-publish/scripts/build_docx.js`, xlsx via
`scripts/generic_publish/build_xlsx_generic.py`, HTML hand-patched for the same 3 S4-related
spots, `MANIFEST.json` updated). All gates re-run against the new `case.md`
(sha256 `272ff520539607dd3bc5c9ccdc1f0b1e66a31ce40c0232efd89f947545c6ce91`):

**Preflight lint:** clean, no advisory findings.

**Tier 1 — structural (23 checks):** `python3 skills/case-readiness/scripts/tier1_structural.py --case the-point-cloud-match`
— **checks run: 23  PASS 21 · GAP 2 · FAIL 0 → VERDICT: TIER1_PASS.** T1-08 now PASSes (S4 is
HIGH confidence again, so no LOW-confidence-source review is outstanding). The two remaining GAPs
are the same pre-existing, honest, non-defect findings as the prior run: **T1-10** (reinforcement
carve-out, `case.json.reinforcement_note` on file) and **T1-15** (the generic xlsx-builder script's
own hardcoded `"MS | Math | Case Study | 2026-27"` README subtitle — a shared-script quirk, not a
case defect). POLISH unchanged: T1-07, T1-20.

**Tier 2 — simulated play, all 6 probes re-run:**

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Re-verified by hand against the (regenerated, content-identical for D1–D5) cold-solve packet: all arithmetic reproduces exactly as in the prior run (M1–M2 invariant at 11.848 cm; D4 translation (+3.00,+2.00) predicts Marker 3 at (−6.47, 14.42), 160.65 mm from actual; D5 face-value 0.61% margin for A, real corrected ratio ~1.785 mm/min, ~400x worse than B). Nothing in D1–D5, Appendix B/C, or the twist changed by the S4 fix — only Appendix D/E's citation text and Appendix G's S4 row changed. |
| P2 both-sides | **PASS** | `balance.argument_a`/`argument_b` and their supporting numbers (0 mm, 0.61%, 160.65mm, $8,500, 33 min, 50 min) are unchanged by this fix — still a real, numbered case for each side, not concession-only. |
| P3 trap check | **PASS** | The trap (majority-vote "2 of 3 markers check out") and FACILITATOR.md's naming of it are unchanged. |
| P4 twist integrity | **PASS** | Marker 4's reflection fact (expected (−1.75, 18.73) → actual (−1.75, −18.73) across the x-axis) is unchanged; still verified by hand. |
| P5 sensitivity (±50%) | **PASS (disclosed)** | Re-ran via `tier2_probes.py --probe 5`: identical result to the prior run — base A=225.0/B=223.64 (0.6% margin), stable under ±50% `tolerance_mm`, flips under +50% `marker_time_min`/`reexport_time_min` (both Category-X disclosed, unchanged). |
| P6 data decay | **PASS** | **All 5 sources re-fetched live on 2026-09-12** (not just S4). **S1**: HTTP 200, all 7 figures present verbatim (confirmed without thousands-separators: `35947`, `69451`, etc., exactly as the live page renders them). **S1b**: `bunny.tar.gz` re-downloaded and re-parsed fresh — `bun_zipper.ply` header confirms 35,947 vertices / 69,451 faces; all 10 raw per-pass files re-summed to exactly 362,272. **S2**: HTTP 200, both quoted phrases present verbatim. **S3**: HTTP 200, both quoted phrases present verbatim. **S4 (new source)**: `https://arxiv.org/abs/2604.24316` — PDF downloaded directly and text-extracted; confirmed verbatim on page 9 and in the results table on page 11: "mean point error reached 1.3mm with a maximum of 3.2mm at peripheral scan pairs," "registration (28 scans) achieved tighter results: 0.9mm mean point error," "mean distance error of 5.8mm" — all exactly as cited in `case.json.sources[]`/`case.md`. No source has drifted. |

**Tier 3 — human dry-run:** still NOT RUN (not eligible until `PUBLISHED`).

## case.json.qa written by this run (current)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-12",
  "blockers_open": 0,
  "gaps_open": 2,
  "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS",
            "P5": "PASS (disclosed)", "P6": "PASS"},
  "tier3_runs": [],
  "case_md_sha256": "272ff520539607dd3bc5c9ccdc1f0b1e66a31ce40c0232efd89f947545c6ce91"
}
```

---

## Real re-gate after the "polish pass" (hash self-update audit) — 2026-09-14

**Context.** This case sat at `qa.state: TIER2_PASS` (above). A subsequent "polish pass" edited both
`case.md` and the published Interactive HTML — added two diagrams (a blank quadrant reference in
Appendix B; a generic rotation-vs-reflection illustration for D3), fixed a dead glossary link
(Quadrant → cuemath.com/geometry/quadrant/), added "why this methodology" notes to D1–D5 (case.md
and HTML), and rebuilt the docx/xlsx/MANIFEST — and self-updated `case.json.qa.case_md_sha256` to
match the new `case.md` **without an actual case-readiness re-run**. This entry is that real re-run.

**Hash currency.** Recomputed `sha256(case.md)` directly: `f15383bbb8aaecdcab8ab071c3c0b171604200a8a8f1c8160c9cdb45c43b8778`.
This matches `case.json.qa.case_md_sha256` exactly — the self-updated hash is in fact current
(T1-16 would have passed on a technicality either way; the real question this run answers is
whether the *content* behind that hash is actually safe, which a hash match alone cannot prove).

**Preflight lint.** `python3 skills/case-readiness/scripts/preflight_lint.py --case the-point-cloud-match`
→ clean, no advisory findings.

**Trap-leak review of the new material (the specific risk this task was scoped to check).**
Read both new diagrams and all five new "why this methodology" blocks in both `case.md` and the
published HTML line-by-line against the twist (Marker 4 reflects across the rig's **x**-axis, a
different axis than Marker 3's y-axis reflection — FACILITATOR.md's "Twist" section, dropped at
15:00 in the Socratic plan) and against the base mystery (whether Marker 3 is genuinely mirrored).
Findings:
- The Appendix B "blank quadrant reference" SVG plots **no points at all** — axes, grid, and
  Roman-numeral quadrant labels only, explicitly captioned "no points are pre-plotted here on
  purpose." It cannot leak which marker lands where.
- The D3 rotation-vs-reflection SVG uses a **generic demo point "P"**, not any of this case's own
  marker coordinates — its own `aria-label` says so explicitly ("A generic demo point, not from
  this case's own data"). It illustrates the *concept* (rotation preserves which side of the axis
  a point is on; reflection flips it), not which of Priya's four markers is on which side.
- The five "why this methodology" notes (D1–D5, both files) explain *why each mathematical step is
  ordered the way it is* (why distance before reflection, why only two markers for the translation
  fit, why a ratio over raw numbers) — none of them names a specific marker as the mirrored one,
  states which axis a marker reflects across, or previews the Marker-4 twist. The Dilemma/D3
  Challenge text's own pre-existing phrase "the marker Priya suspects is mirrored" (naming Marker 3
  as suspect) already existed before this polish pass and is the base mystery, not the twist — it
  is not something the new text adds.
- The fixed Quadrant glossary link (→ cuemath.com) is a bare vocabulary link; no leak risk.
- Appendix B's own methodology note — which states in-fiction *how* Markers 3 and 4 were each
  built (Marker 3: reflect across y-axis; Marker 4: reflect across x-axis, "a different mirror axis
  than the one applied to Marker 3") — was already present in `case.md` at the prior `TIER2_PASS`
  gate (2026-09-12, P4 finding above cites this exact note) and is unchanged by the polish pass.
  It is the case's own designed in-fiction disclosure (data-construction methodology, standard for
  every appendix in this pipeline), not new leakage introduced here.

**Conclusion: no trap-leak.** The new diagrams and methodology notes are additive explanation of
math technique, not new disclosure of story facts. The twist (Marker 4's *different* mirror axis)
is still discoverable only by working D4's translation check and then separately checking Marker 4
against the same logic — nothing in the polish pass hands that to a reader early.

### Tier 1 — structural (23 checks), fresh run

```
python3 skills/case-readiness/scripts/tier1_structural.py --case the-point-cloud-match
```
**checks run: 23  PASS 21 · GAP 2 · FAIL 0 → VERDICT: TIER1_PASS**

| id | result | id | result | id | result |
|---|---|---|---|---|---|
| T1-01 | PASS | T1-09 | PASS | T1-17 | PASS |
| T1-02 | PASS | T1-10 | GAP  | T1-18 | PASS |
| T1-03 | PASS | T1-11 | PASS | T1-19 | PASS |
| T1-04 | PASS | T1-12 | PASS | T1-20 | PASS |
| T1-05 | PASS | T1-13 | PASS | T1-21 | PASS |
| T1-06 | PASS | T1-14 | PASS | T1-22 | PASS |
| T1-07 | PASS | T1-15 | GAP  | T1-23 | PASS |
| T1-08 | PASS | T1-16 | PASS |  |  |

BLOCKER: 0. GAPs (2, both pre-existing and honest, unchanged from the prior gate):
- **T1-10** — `new_coverage[]` empty; reinforcement carve-out on file (`case.json.reinforcement_note`).
- **T1-15** — 1 numeric cell in `published/…Data.xlsx` (`README!A2=27.0`) is the generic
  xlsx-builder script's own hardcoded school-year subtitle text, not case data — a shared-script
  quirk, not a case defect.

POLISH (1): T1-07 (label-parsing note, informational). T1-20, which previously flagged "no chart in
the HTML," now correctly finds the two new diagrams and no longer fires.

### Tier 2 — simulated play, all 6 probes re-run fresh

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Re-derived all of D1–D5 by hand from the packet/appendix data alone, independent of the prior run's numbers, and cross-checked: D1 = 35,336/362,272 = 9.75%; scientific notation 3.5947×10⁴ (Bunny vertices), 6.9451×10⁴ (Bunny triangles), 5.66098×10⁵ (Dragon vertices). D2 distances: M1–M2 invariant at 11.848 cm (expected and actual identical — confirms a true rigid translation on that pair); M1–M3 collapses 16.755→4.206 cm; M2–M3 grows 9.995→13.825 cm — correctly "neither congruent nor similar" for the full triangle. D3: reflecting expected M3 (−9.47, 12.42) across the y-axis gives exactly (9.47, 12.42), an exact match to M3's actual scanned position. D4: solving with M1/M2 gives a consistent (Δx,Δy)=(+3.00,+2.00); applying it to expected M3 predicts (−6.47, 14.42), a gap of 16.065 cm = 160.65 mm from M3's actual position. D5: face-value ratios 0.40/90=0.0044444 (A) vs 0.55/123=0.0044715 (B), a 0.61% margin favoring A; substituting A's real 160.65 mm error gives a true ratio of ~1.785 mm/min, ~400x worse than B; deadline window 4:40–5:30 PM = 50 min, Option B's 33 minutes fit with 17 to spare. All figures reproduce exactly. Reached B via the correct arithmetic route (not a guess), with the trap (naive A-wins-on-face-value ratio) genuinely present and only resolved by working D2–D4 in sequence. |
| P2 both-sides | **PASS** | A's best real sentence: "Ship As Converged costs 0 extra technician minutes, the rig reported converged (its own accepted signal), and 2 of 3 markers land exactly where expected." B's best real sentence: "Marker 3's actual position is 160.65 mm from where a pure translation predicts — consistent with an undetectable reflection — so shipping risks an $8,500 re-shoot to save 33 minutes that fit inside the 50-minute deadline with room to spare." Both sides carry real, specific numbers; A is genuinely arguable at face value and collapses specifically at the D4 translation check (160.65 mm), which is the case's designed trap-and-reveal structure, not a disguised concession. |
| P3 trap check | **PASS** | Independently named the likely wrong path before reading FACILITATOR.md: "2 of 3 markers check out / the naive ratio says A wins, so ship it" — a majority-vote / trust-the-summary-number fallacy. FACILITATOR.md's own "The trap" section names exactly this ("Two of three markers check out, so the scan is basically fine — ship it"), and Socratic Questions 1–2 interrogate it directly. The guide anticipates the path that will actually catch a room. |
| P4 twist integrity | **PASS** | Verified Marker 4's twist fact by hand, independent of MA1–MA6: expected (−1.75, 18.73) reflected across the rig's x-axis (y → −y) gives (−1.75, −18.73), an exact match to Marker 4's given actual coordinate. This is a fixed property of the given coordinate data, not contingent on any Modeling Assumption or its reading order, so there is no sequential-assumption ambiguity (the failure mode that originally broke Cold Chain's twist). It genuinely invalidates the "Option B as scoped (3 markers) is obviously sufficient" position — FACILITATOR.md's Thread 2 treats this as a live, unresolved scope-creep question, not swept under the rug. Confirmed the new D3/Appendix-B diagrams do not telegraph this twist (see trap-leak review above). |
| P5 sensitivity (±50%) | **PASS (disclosed)** | `python3 skills/case-readiness/scripts/tier2_probes.py --case the-point-cloud-match` (probe 5 section): base A=225.0/B=223.64, margin 0.6%. Stable under ±50% `tolerance_mm` (winner stays A both directions). Flips under +50% `marker_time_min` (winner→B, margin 7.9%) and +50% `reexport_time_min` (winner→B, margin 4.2%) — both are the same disclosed, Category-X face-value-only instability as every prior run (the case's own D5 metric rewards more minutes at Option B's fixed residual; the *real*, trap-independent recommendation, resting on the fixed 160.65 mm geometric fact, is unaffected by any of the three flexes throughout the sweep). `sensitivity_disclosure[]` still carries the required `{param, category, justification}` schema for both flexed dials. No change from the prior gate. |
| P6 data decay | **PASS** | **All 5 sources re-fetched live today, 2026-09-14**, independent of the prior run's cached findings. **S1** (`graphics.stanford.edu/data/3Dscanrep/`): fetched live — Bunny (10 scans, 35,947 vertices, 69,451 triangles, 362,272 raw points), Dragon (~70 scans, 566,098 vertices, 1,132,830 triangles), Happy Buddha (~60 scans, 543,652 vertices, 1,087,716 triangles) all confirmed verbatim. **S1b**: `bunny.tar.gz` freshly downloaded (4.9 MB) and unpacked; parsed every `.ply` header directly — `bun_zipper.ply` = 35,947 vertices / 69,451 faces exactly; the 10 raw per-pass files (bun000=40,256, bun045=40,097, bun090=30,379, bun180=40,251, bun270=31,701, top2=38,298, top3=36,023, bun315=35,336, chin=37,738, ear_back=32,193) sum to exactly 362,272 — an independent byte-level re-verification, not a reused claim. **S2**: fetched live — both quoted phrases ("Symmetries and repetitive patterns: building façades, tiled floors, agricultural row crops, brick walls" and "Repetitive-feature scenes can defeat dozens of markers…") present verbatim. **S3**: fetched live — "To improve accuracy, adjust the marker position in several different images where the same feature is visible" present verbatim. **S4**: `arxiv.org/pdf/2604.24316` downloaded directly (22 MB PDF) and text-extracted; confirmed verbatim — "mean point error reached 1.3mm with a maximum of 3.2mm at peripheral scan pairs," "registration (28 scans) achieved tighter results: 0.9mm mean point error," "mean distance error of 5.8mm" — exactly as cited in `case.json.sources[]`/`case.md`/Appendix D/E. No source has drifted since the prior gate; the S4 replacement made at the 2026-09-12 gate remains sound. |

### Tier 3 — human dry-run

NOT RUN. Not eligible — case has not reached `PUBLISHED`.

## Verdict

**State: TIER2_PASS** (re-confirmed). The self-updated hash was, in this instance, honest — it
matched the live `case.md` — but the underlying content it certified had never actually been
re-gated until this run. That re-gate found 0 BLOCKERs, the same 2 pre-existing honest GAPs, all
six Tier 2 probes PASS (P5 disclosed, as before), and — the specific risk this task was scoped to
check — no trap-leak in either new diagram or any of the five new "why this methodology" notes.
`case.json.qa` below is unchanged in verdict/state from the pre-polish gate, with `run_on` and
`case_md_sha256` updated to reflect this real run against the current file.

## case.json.qa written by this run (current)

```json
{
  "state": "TIER2_PASS",
  "verdict": "PASS",
  "run_on": "2026-09-14",
  "blockers_open": 0,
  "gaps_open": 2,
  "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS",
            "P5": "PASS (disclosed)", "P6": "PASS"},
  "tier3_runs": [],
  "case_md_sha256": "f15383bbb8aaecdcab8ab071c3c0b171604200a8a8f1c8160c9cdb45c43b8778"
}
```
