# QA Report — the-search-box

## case-readiness run — 2026-09-18 (Tier 1 re-verify + genuine Tier 2 completion, incl. new P7)

**State:** TIER1_PASS (2026-08-31, unrelabeled) → **TIER2_PASS**. This run brings the case's `qa.state` in line with
its actual, current standard: re-ran Tier 1 against today's grown check set (T1-22–T1-24, added by MCS-50/52 after
2026-08-31), built the case's first `published/` interactive HTML (none existed before), ran P7 (added 2026-09-03,
never checked against this case before today) for real, and re-verified P1–P6 rather than carrying the 2026-08-31
record forward unearned. `case.md` and `case.json`'s sourced/assumed figures, `balance` object, and
`sensitivity_disclosure[]` are **unchanged** from 2026-08-31 — this run is a genuine current QA pass, not a rewrite
of the case's content, and the framing-discipline register (SPEC §6, person-overboard scenario) was preserved
throughout (verified again at the end of this section).

### Tier 1 — structural (24 checks, up from 20 at the 2026-08-31 run)

Ran `skills/case-readiness/scripts/tier1_structural.py --case the-search-box` against the unmodified `case.md` plus
the newly-built `published/The Search Box - Interactive.html`. sha256(case.md) = `be42e562c1c0eba8...` — unchanged,
matches `case.json.qa.case_md_sha256`, so nothing described below is stale.

**PASS 23 · GAP 1 · FAIL 0 — VERDICT: TIER1_PASS**

| id | result | note |
|---|---|---|
| T1-01 – T1-09 | PASS | unchanged from 2026-08-31 |
| T1-10 | GAP | unchanged carve-out (`reinforcement_note`), doctrine-approved, not a per-case waiver |
| T1-11 – T1-17 | PASS | unchanged |
| T1-18 | PASS | new `published/` HTML: no `balance.margin_pct` leak, no Working Notebook numeric-example placeholder leak (2 real bugs found and fixed during authoring — see "What was built and fixed" below), 0 orphan numbers outside `<script>` |
| T1-19 | PASS | 9 real math-vocabulary terms (`GLOSSARY`), all `https://mathsisfun.com`/`khanacademy.org`, verified live 2026-09-18 |
| T1-20 | PASS | 1 real diagram (drift-vector/search-box figure, inline SVG, real shape content) |
| T1-21 | PASS | 17 real story-vocabulary terms (`STORY_GLOSSARY`), real non-math domains (`wikipedia.org`, `rdept.cgaux.org`), verified live |
| T1-22 | PASS | published HTML's own `<h2>` headings match every section T1-01 finds in `case.md` (Overview/Background/Dilemma/Challenges/Appendices) |
| T1-23 | PASS | inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | the hand-drawn SVG diagram's 3 connector `<path>` endpoints all land exactly on their anchor shapes' centers (vessel/radar-fix circles, each datum's box) — verified both mechanically and by eye in a live browser |

**0 BLOCKERs, 1 GAP (pre-existing carve-out), 1 POLISH** (T1-07, unchanged pre-existing note about the separator-run
parser; harmless, not a defect in this case).

### What was built and fixed

1. **Built `published/The Search Box - Interactive.html`** (none existed before this run) from
   `templates/interactive_shell.html`'s pattern, following `cases/the-manifest-split/published/The Manifest Split -
   Interactive.html` as the reference. Includes: all 7 `case.md` sections plus a Working Notebook (D1–D5, each
   self-checking against a live JS port of `sensitivity_model.py`'s own arithmetic — never printing the
   `balance`/recommendation as a static literal), a Twist section (the same MA12-doubling twist as
   `FACILITATOR.md`, gated behind an explicit "ask your facilitator" reveal), a math `GLOSSARY` (9 terms) and a
   `STORY_GLOSSARY` (17 terms), and an inline-SVG diagram plotting tonight's actual D1–D3 figures (vessel position,
   converted radar fix, both drift vectors, both search boxes) to scale.
2. **Two real authoring bugs found and fixed before this ever reached Tier 1** (found by opening the actual page in
   a live browser and reading the console/DOM, not by trusting the text-based checks alone, per this project's own
   standing instruction that case-readiness's checks miss real rendering bugs):
   - **T1-18 BLOCKER (self-inflicted, fixed same session):** every Working Notebook `<input type="number">`
     placeholder originally read like `"nautical miles, 3 decimals"` / `"knots, 4 decimals"` — a bare digit in a
     placeholder is the exact MCS-37 defect class (a placeholder that states or implies the graded value). Reworded
     every one to a digit-free format hint (`"nautical miles, several decimal places"`, etc.). Re-ran T1-18 clean.
   - **Live-browser-only defect, not caught by any Tier 1 text check:** on first build, every `localStorage` call
     was unguarded. Opening the actual published HTML in a real browser (this project's preview sandbox loads a
     local file as an opaque-origin snapshot) showed the Deliverables checklist, the glossary, and the how-to list
     all rendering **completely empty**, with **no visible console error** — `localStorage.getItem()` throwing
     inside `restorePick()` silently aborted the entire inline `<script>` block partway through, before the
     glossary/checklist-rendering code further down ever ran. This is the same failure class MCS-50 (Pier Wheel)
     names: a script-wide abort that every purely-textual check (T1-19, T1-21, T1-23's `node --check`) stays green
     against, because none of them execute the script or check DOM output, only its source text. Fixed by wrapping
     every `localStorage` read/write in `lsGet()`/`lsSet()` try/catch helpers so the page degrades gracefully (a
     real robustness requirement anyway — private browsing and other sandboxed contexts can throw the same way for
     a real student). Re-verified live in the browser after the fix: checklist, glossary, and how-to list all
     render, and all D1–D5 Check buttons grade correctly (spot-checked D1 and D5, including a deliberately-wrong D5
     recommendation graded "try again" and the correct one graded "✓", confirming the calculator checks arithmetic
     live and never leaks the verdict).
   - Also fixed one figure-caption label so an SVG text element didn't clip past its own diagram's viewBox
     (`"Set-and-Drift Datum + box"`, cosmetic only, no check flags text overflow).
3. **P7 gap found and closed for real, not force-passed.** The first P7 cold-read (fresh subagent, zero context)
   against the newly-built HTML named 9 genuinely unexplained real-world terms — `datum`, `bearing`/`true`, `sweep
   width`, `track spacing`, `sea state`, `optimal search factor`, `total probable error of position`, `the watch
   changed over`, `marine-band scanner` — and one structural gap: nothing in the case described the actual physical
   search operation (what "fully searching a box" means as a flown pattern), only the box's geometry. Fixed by (a)
   adding 9 new `STORY_GLOSSARY` entries with real, verified-live citations (`en.wikipedia.org` for bearing/watch
   system/sea state/marine VHF radio; the case's own already-cited CGADD source document, `rdept.cgaux.org`, for
   the Coast-Guard-specific planning terms datum/sweep width/track spacing/optimal search factor/total probable
   error, since that primary source literally defines its own terms — at least as legitimate a citation as a
   secondary source) and inline `sterm` hover annotations at each term's first mention in the prose, and (b) adding
   one new `STORY_GLOSSARY` entry plus a plain-language sentence in Appendix A describing the real parallel-track
   search pattern (straight, evenly-spaced passes at the stated track spacing, "the way a lawnmower covers a
   lawn") — described honestly, with no invented precision beyond what the case already states. A second, fresh
   zero-context subagent cold-read of the rebuilt packet came back clean: **0 unexplained real-world concepts, and
   the one candidate "central invented mechanism" (the two disagreeing search boxes) judged clearly picturable from
   the packet's own diagram description.** See the P7 section below for the full verdict.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** (adjudicated) | fresh subagent, given only the packet, independently worked D1–D5 correctly and reached B (Set-and-Drift Datum) via the right route — named the metric (POD per flight-hour), showed correct arithmetic (areas 3.706/6.126 sq NM, coverage factors ≈36.9/22.3, POC 55%/64.75% → 0.1447/0.1704), and correctly identified MA13 (poc_A_pct) as the load-bearing assumption. It flagged Appendix F's MA13 sentence ("55% is chosen as a value below... 64.75%") as a possible partial leak — adjudicated **not a real leak**: that same comparison (55% vs 64.75%) is already stated directly, side by side, in Appendix E's own POC table, so the MA13 sentence adds no route-shortcut beyond what the raw appendix data already shows; the solver still had to do the full D1–D5 chain (including recognizing both boxes are POD-saturated) to reach the recommendation, and did so. Matches the 2026-08-31 record's own P1 adjudication style (a textual coincidence/pre-existing appendix content, not a hand-out of the verdict). |
| P2 both-sides | **PASS** (adjudicated) | fresh subagent built a real quantitative case for each option; A's best argument (smaller box, better-sourced growth constant, a hedge against the endurance assumption) survives a first read but collapses at "given coverage factors of 37 and 22, doesn't POD round to ~1.0 for both — so what's actually different besides POC, and why weight an unsourced 55% over a sourced 64.75%?" B's case holds. Matches the 2026-08-31 finding. |
| P3 trap | **PASS** (adjudicated) | fresh subagent, reading the packet cold, independently named the same trap `FACILITATOR.md`'s "## The trap" section names almost word for word: picking the smaller box (Windward) without checking that it still loses on POC-weighted detection odds. |
| P4 twist | **PASS** (adjudicated) | fresh subagent confirmed the twist (doubling MA12) invalidates the intuitive-but-wrong belief that the least-sourced assumption must be the most load-bearing one, using only the packet's own stated D5 formula and figures — no hidden convention required. Re-verified live in the rebuilt interactive calculator: toggling "Recompute with the twist applied" (`growth_rate_B_kt` 0.45→0.9) still leaves B ahead (podfh A=0.1447 vs B=0.1698), matching `sensitivity_model.py`'s and `FACILITATOR.md`'s prior finding that the real flip threshold is ~1.55 kt, not 0.9 kt. |
| P5 sensitivity | **PASS (disclosed)** | mechanical re-run of the unmodified `sensitivity_model.py`: reproduces `case.json.balance.computed_2026-08-30` exactly (A=0.1447, B=0.1704); MA13 (`poc_A_pct`) flips at +50% (real threshold ≈64.75%, disclosed in `case.json.sensitivity_disclosure[]`, category X); MA12 (`growth_rate_B_kt`) does not flip within ±50% in either direction (real threshold ≈1.55 kt, ~3.4×). Identical to the 2026-08-31 finding — nothing about the case's math changed this run. |
| P6 data decay | **PASS** (verified by direct fetch, 2026-09-18) | delegated to a fresh subagent with live network access: fetched the single cited PDF (`rdept.cgaux.org/.../USCG_SAR_Addendum.pdf`, HTTP 200, ~8.5 MB, unchanged), extracted text, and re-confirmed all 10 cited figures (S1–S10) present verbatim or in exact numeric agreement — 90 kt (S1), 0.1→0.4 NM PFD-corrected sweep width (S2), the leeway equation/divergence/standard-error (S3), the coverage-factor/POD formulas (S4/S5), the 85%-endurance rule (S6), 6.0 hr H-60 MAX endurance (S7), 64.75% POC at fs=1.1 (S8), the qualitative Figure H-22 divergent-vs-single-point framing (S9), and the total-probable-error/optimal-search-factor definitions (S10). No source moved, 404'd, or dropped its figure. |
| P7 accessibility | **PASS** | see "What was built and fixed" above for the remediation. Final fresh cold-read (2026-09-18, zero-context subagent, reading the rebuilt `published/` HTML's own text): **0 unexplained real-world concepts named** (every term — marine-band scanner, watch/change-of-watch, SMC, bearing, PFD, leeway, set-and-drift, sweep width, sea state, track spacing, parallel-track search pattern, datum, total probable error, optimal search factor, SAROPS, CGADD — had an inline definition the subagent judged sufficient), and **no unpicturable central mechanism** (the two-disagreeing-search-boxes setup was judged clearly picturable from the packet's own figure description). Clears the 0–1-unexplained-concept threshold cleanly — no `P7_waiver` needed. |

**All 7 probes PASS, 0 FAIL, 0 NOT RUN.**

### Framing-discipline re-check (SPEC §6 human-reviewed sensitivity flag — person-overboard scenario)

Re-verified against the same standard the 2026-08-30 human review approved: the new `published/` HTML's Overview and
Background paragraphs are copied verbatim/near-verbatim from the already-approved `case.md` prose (present-tense
procedural urgency, no injury/peril detail, decision point only); the Twist section reveals only the same
verified-methodology finding already in `FACILITATOR.md` (which unsourced assumption is actually load-bearing), not
any narrative escalation; and the new `STORY_GLOSSARY`/diagram additions describe real Coast Guard search-planning
mechanics (a parallel-track flight pattern, sweep width, sea state) — methodology only, never depicted injury,
peril, or outcome. Appendix G's real 2013 Aldridge-rescue citation is unchanged. **Consistent — no re-review
needed.**

### Report back

**State reached: TIER2_PASS.** Tier 1: 0 BLOCKERs, 1 GAP (T1-10, pre-existing doctrine-approved carve-out), 1
POLISH. Tier 2: 7/7 probes PASS (P1–P6 re-verified against the unmodified case content and the new published
artifact; P7 is newly run for the first time against this case and now genuinely passes after real remediation, not
a waiver). `margin_pct` = 15 (≈15.1% precise), unchanged from the 2026-08-30/31 record — **no shared read-model file
was touched** (`readmodel/standards_spine.json`, `readmodel/gap_queue.json`, `readmodel/cases_index.json` untouched),
and **`case-publish` was not run**. Framing-discipline register (SPEC §6) preserved throughout.

**Report path:** `cases/the-search-box/QA_REPORT.md`
**Model:** `cases/the-search-box/sensitivity_model.py` (unmodified)
**New artifact:** `cases/the-search-box/published/The Search Box - Interactive.html`

---

## case-readiness run — 2026-08-31 (remediation)

**State:** DRAFT → **TIER1_PASS**. Tier 2 run; 5/6 probes resolved, 1 adjudicated false positive.

This run remediates the 2026-08-31 BLOCKED run recorded further below (kept for history). All 6
Tier 1 BLOCKERs and all 4 GAPs from that run are fixed or explicitly carved out; a
`sensitivity_model.py` was authored and MA12/MA13 were mechanically verified against it.

### What was fixed

1. **T1-04 (Challenge 5 boilerplate)** — the `<!-- FACILITATOR ONLY -->` comment was appended
   directly after Challenge 5's text with no section boundary between it and `## Appendix A`, so
   the diff captured it as part of Challenge 5. Moved the comment to the very end of the document
   (after Appendix H), matching the house pattern already used in `cases/bioreactor-bid/case.md`.
   Challenge 5 now diffs verbatim against `doctrine/CHALLENGE_BOILERPLATE.md`.
2. **T1-10 (empty `new_coverage[]`)** — this is a deliberate second-pass/redundancy case (Polar &
   Parametric already has `n>=1` coverage for all 6 claimed skills). Added
   `case.json.reinforcement_note`, which records that the adjacent Vectors group (also `n=1`,
   `covered_by: ["Wind Triangle"]`) was checked and honestly ruled out — this case's deliverables
   (D1-D5) don't force vector-magnitude/dot-product work. Downgrades T1-10 from BLOCKER to GAP per
   the 2026-08-17 reinforcement-carve-out doctrine amendment.
3. **T1-13 (facilitator guide)** — `FACILITATOR.md` was fully rewritten using
   `cases/cooling-curve/FACILITATOR.md` as the structural template: full anchor ladder (Intro,
   Launch, Anchor 1-4, Data Deep Dive, Twist, Immediate recommit, Deep conflict, 45-minute timed
   Socratic plan with 7 timed rows naming the TWIST moment, Close, Lessons Learned, Standards
   Touched On), a real Twist (see below), and 5 single-line Socratic questions (the multi-line
   wrapped originals didn't match the QA regex, which requires the `?` on the same source line as
   the list marker — rewrapped as single lines). Content is specific to Dana Okafor, the Windward
   Datum vs. Set-and-Drift Datum decision, and the real ~15.1% margin.
4. **T1-14 (continuity drift)** — `case.json.balance.margin_pct = 15` now appears verbatim in
   FACILITATOR.md's Balance flag section (`**margin_pct = 15**`), alongside the more precise
   `≈15.1%`. The 4 previously-orphaned numbers (14.5, 15.1, 17.0, 99.99) are gone from the
   rewritten guide; the new guide's numbers (0.1447, 0.1704, 36.9, 22.3, 3.706, 6.126, 0.9999,
   0.55, 0.6475, etc.) all match `case.json.balance.computed_2026-08-30` exactly. The new
   sensitivity-verification numbers this rewrite introduced (0.225, 0.675, 0.9, 1.55, 3.4, 15.1,
   244.0) were given a checkable home in a new `case.json.balance.sensitivity_check_2026-08-31`
   object and `margin_pct_precise: 15.1`.
5. **GAPs** — 5 real Socratic questions (all end in `?`, all case-specific, all inside the
   sensitivity-safe register), a `cohort_bands[]` array (8-12 / 13-18 / 19-24, each with a concrete
   facilitation-change note) added to `case.json`, `case.json.qa.case_md_sha256` refreshed.
6. **`sensitivity_model.py` authored** (`cases/the-search-box/sensitivity_model.py`) — see the
   dedicated section below. This was the highest-priority item: it replaces two unverified author
   assertions in case.md's original Appendix F with mechanically-checked numbers, and both turned
   out to be **wrong or materially different** from what was originally claimed.
7. **case.md leak fix (found during remediation, not in the original blocker list)** — the original
   Appendix F MA13 row stated "the current margin (≈15%, Option B ahead)" directly in student-facing
   text, violating the rule that case.md must never state the balance margin. Reworded MA12/MA13's
   Sensitivity column to point to FACILITATOR.md instead of stating a margin or a flip direction.
8. **case.json.balance.argument_a/argument_b were prose-only, no numbers** — found via Tier 2 Probe
   2 (see below), not the original blocker list. Rewritten with real quantitative content (leeway
   equation coefficients, box areas, coverage factors, POC figures) so each argument is an
   actually-defensible quantitative case, not restated qualitative framing.

## Preflight lint (advisory, non-blocking)

Same 4 pre-existing false positives documented in the prior run (`check_student_facing_leak()`
splits on the literal substring `<!-- FACILITATOR ONLY -->`, not the actual house convention
`<!-- FACILITATOR ONLY: balance argument... -->`, so the split never fires and the whole document
gets scanned). Two new instances appear at the MA12/MA13 rows because the remediation rewrote them
to say "SEE FACILITATOR.md" instead of stating the margin — the same known linter bug, not a new
defect. Left unfixed per the prior run's judgment; a fix-the-linter task remains out of scope for
this gate run.

## Tier 1 — structural (20 checks)

**PASS 19 · GAP 1 · FAIL 0 — VERDICT: TIER1_PASS** — sha256(case.md) = `be42e562c1c0eba8...`
(matches `case.json.qa.case_md_sha256`)

| id | result | note |
|---|---|---|
| T1-01 – T1-09 | PASS | unchanged from the prior run |
| T1-10 | GAP | `new_coverage[]` empty, reinforcement carve-out recorded (`case.json.reinforcement_note`) — downgraded from BLOCKER per doctrine, not a per-case waiver |
| T1-11, T1-12 | PASS | |
| T1-13 | PASS | full anchor ladder, Twist section, 45-minute timed plan (7 rows, names TWIST), 5 Socratic questions |
| T1-14 | PASS | `margin_pct = 15` present verbatim in FACILITATOR.md; no orphan numbers remain |
| T1-15 | PASS | no `published/` yet |
| T1-16 | PASS | `case_md_sha256` refreshed and matches |
| T1-17 | PASS | `cohort_bands[]` declared (8-12, 13-18, 19-24) |
| T1-18 – T1-20 | PASS (POLISH) | no `published/` directory yet |

**0 BLOCKERs, 1 GAP (carve-out), 5 POLISH notes.**

## Tier 2 — simulated play

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **ADJUDICATED FALSE POSITIVE** (see below) | mechanical leak check flags "15" near "%" |
| P2 both-sides-solve | **PASS** (adjudicated) | both arguments now quantitative; adjudication below |
| P3 trap-check | **PASS** (adjudicated) | guide's named trap matches the actual most-plausible wrong path |
| P4 twist-integrity | **PASS** (adjudicated) | twist invalidates a real position and survives every defensible reading |
| P5 assumption-sensitivity | **PASS (disclosed)** | machine-run; see the dedicated MA12/MA13 section below |
| P6 data-decay | **PASS** (verified by direct fetch) | all 10 sources reachable, cited figures confirmed present |

### P1 cold-solve — adjudicated false positive

Mechanical result: `FAIL` — `balance_test.margin_pct = 15 appears in the packet`. The match is
`cases/the-search-box/case.md`'s Appendix G/Sources row for **S6**: *"Search endurance = 85% of
on-scene endurance (remaining **15%** reserved for identifying sighted objects and end-of-leg
turns)"* — a real, sourced Coast Guard figure (CGADD §H.5.2.2, independently verified live during
P6 below: *"assumed to be 85 percent of on scene endurance, allowing 15 percent for identifying
sighted objects..."*). This is a numeric coincidence, not a leak: S6's 15% is the Coast Guard's own
published search-efficiency reserve, unrelated to and nowhere near the balance-margin sentence, and
no student reading "15% reserved for identifying sighted objects and end-of-leg turns" could infer
the balance verdict from it. The check's own `require_unit` heuristic (look for `%`/`point` within
15 characters after the number) cannot distinguish this from an actual leak because both are
percentages. Manually confirmed: `case.md` contains no other reference to a margin, a winner, or a
recommendation (`grep -in "margin|wins|winner|recommend"` returns only structural/generic
sentences — see the diff in "What was fixed," item 7, for the one real leak this remediation did
find and fix). **Adjudicated PASS** — the packet does not actually hand the solver the answer.

### P2 both-sides-solve — adjudicated

Mechanical result after the argument rewrite: `READY` (no missing arguments, no low-number
arguments, no concession-only framing). Adjudication:

- **Best sentence for A:** "The Windward Datum searches the smaller of the two boxes (3.706 sq NM
  vs. 6.126), built from a real, published leeway equation validated for exactly this object
  category, and still reaches a coverage factor (~37) that guarantees near-certain detection within
  the helicopter's fuel budget."
- **Best sentence for B:** "Even though its box is larger, the Set-and-Drift Datum carries a real,
  sourced 64.75% probability of containment (S8) versus the Windward Datum's discounted, unsourced
  55% (MA13) — and since both boxes are already searched to near-certain detection, that
  containment gap is what actually decides the odds of finding the person per flight-hour."
- **Which collapses first:** Argument A, under the question "if your box is smaller, why is your
  detection probability still lower?" A's defender has no sourced containment figure to fall back
  on — MA13's 55% is an author estimate, not a citation — while B's defender can point to S8's real
  64.75%. This matches both the guide's stated trap (picking the smaller box without checking POC)
  and the verified sensitivity finding (MA13, not box size, is what actually decides it).

### P3 trap-check — adjudicated

Reading `case.md` cold (ignoring the Guide Notes): the most plausible wrong path is a student
picking whichever candidate box is *smaller* — the Windward Datum, at 3.706 sq NM vs. 6.126 — on
the intuition that a smaller, fully-searchable box is "more efficient" or "more thorough," without
running D5's probability-of-containment-weighted comparison. `FACILITATOR.md`'s "## The trap"
section names exactly this path ("The plausible wrong answer is picking whichever box is
smaller... without checking that a smaller box searched completely can still carry a *lower*
probability of detection..."). **Match confirmed — PASS.**

### P4 twist-integrity — adjudicated

1. **Does the twist invalidate a real position?** Yes. A real room, having been told at Anchor 4
   that MA12 (Option B's growth-rate constant) has *no published source at all* — a weaker sourcing
   story than MA13's at-least-graph-grounded 55% — will plausibly conclude MA12 is the case's real
   weak point. The Twist (doubling MA12 to 0.9 kt) directly tests and invalidates that belief: per
   `sensitivity_model.py`, doubling MA12 does not flip the recommendation (the real flip threshold
   is ~1.55 kt, about 3.4× the stated value), so a room that voted "unstable because of MA12" is
   shown to be wrong about *which* assumption is load-bearing.
2. **Does it survive every defensible reading of the case's own stated assumptions?** Yes — the
   Twist only touches MA12 (`growth_rate_B_kt`), which enters the case's math through a single,
   unambiguous chain (E(t) = rate × t → R = fs × E(t) → area = (2R)² → coverage factor → POD →
   POD-per-flight-hour). Unlike Cold Chain's sequential/parallel amortization ambiguity, there is no
   alternate reading of how MA12 combines with the other Appendix A-E figures; `elapsed_time_hr`
   (MA2) and `search_factor` (S10's fs = 1.1) are held fixed and uncontested. **No hidden
   convention required — PASS.**

### P5 assumption-sensitivity (MA12/MA13) — the user's specific request

**Machine result: `PASS (disclosed)`.** `cases/the-search-box/sensitivity_model.py` (PARAMS/FLEX =
`["poc_A_pct", "growth_rate_B_kt"]`, i.e. exactly MA13 and MA12 — the only two dials
`case.json.modeling_assumptions` marks `"flippable": true`) reproduces
`case.json.balance.computed_2026-08-30` to 4 decimal places (A = 0.1447, B = 0.1704
POD-per-flight-hour) and was swept ±50% on both dials, then bisected for the exact flip threshold.
**Both of case.md's original Appendix F claims are wrong or materially off, and the correct,
verified numbers are recorded now in `case.json.balance.sensitivity_check_2026-08-31` and
`FACILITATOR.md`'s Balance flag section:**

- **MA12 (Option B's search-radius growth-rate constant, stated 0.45 kt):** case.md's Appendix F
  claimed *"a real per-hour current-uncertainty figure smaller than ~0.35 kt... could flip the
  recommendation."* **This is not confirmed — it is backwards.** A ±50% swing (0.225–0.675 kt) does
  **not** flip the recommendation in either direction, and *decreasing* the growth rate never flips
  it at all (verified down to 1e-6 kt) — Option B stays coverage-saturated across the whole range,
  so its POD-per-flight-hour is pinned near its ceiling (POC_B ÷ endurance ≈ 0.1704) regardless of
  how small the growth rate gets. The real flip threshold, found by bisection, is an **increase** to
  approximately **1.55 kt** (≈3.4× the stated value, a +244% swing) — the opposite direction and a
  much larger magnitude than the case's original claim.
- **MA13 (Option A's assumed probability of containment, stated 55%):** case.md's Appendix F
  claimed the flip point was *"roughly 61%."* **The verified threshold is ≈64.75%**, not 61% — this
  is Option B's own real, sourced POC (S8), which makes sense once both options are recognized as
  POD-saturated: the whole comparison reduces almost exactly to POC_A vs. POC_B. A +50% swing
  (55% → 82.5%) **does** cross this threshold and flips the recommendation to Option A; a −50% swing
  does not.
- Both the +50% MA13 flip and both-direction 20%-cap breaks on MA13 are recorded in
  `case.json.sensitivity_disclosure[]` (category **X** — the true divergent-datum POC is knowable in
  principle but not published as an exact digit; 55% is a documented good-faith estimate below the
  real 64.75%, consistent with CGADD Figure H-22's graphed shape). This satisfies the
  disclosure-aware pass state (2026-08-13 doctrine) — MA13's instability is disclosed, not
  eliminated, which is an honest and permitted outcome, not a corner cut.

**Bottom line for the user's question:** Option B (Set-and-Drift Datum, real margin 15.1%) does
**not** survive a ±50% swing on MA13 alone (it flips at +50%, at a verified real threshold of
~64.75%, not the ~61% the case originally claimed) — this instability is real, disclosed, and
inside SPEC's permitted disclosure path. Option B **does** survive a ±50% swing on MA12 (it does
not flip in either direction) — and the case's original claim about MA12's direction of fragility
was actually wrong: MA12 would have to roughly triple, not shrink, to matter.

### P6 data-decay — verified by direct fetch (2026-08-31)

The QA sandbox note about no outbound network did not apply in this environment — network access
was available, so this probe was run directly rather than delegated. All 10 sources (S1-S10) cite
the same single PDF, `https://rdept.cgaux.org/documents/ManualsTemp/USCG_SAR_Addendum.pdf`
(*CGADD to the U.S. National SAR Supplement*, COMDTINST M16130.2F). Fetched (HTTP 200, ~8.5 MB),
converted to text, and confirmed every cited figure is still present verbatim:

- S1 (90 kt reference speed, PIW factor 1.0) — Table H-9 "Search Aircraft Speed Correction" present.
- S2 (0.4 NM sweep width) — Table H-15 "Uncorrected Visual Sweep Width – Helicopters for Altitudes
  300-500 Feet" present.
- S3 (leeway equation, ±30° divergence, 0.35 kt standard error) — Table H-7 "Leeway Speed and
  Direction Values for Drift Objects" present, multiple "0.35" hits in the surrounding text.
- S4/S5 (coverage-factor and POD formulas) — §H.5.5 "Coverage Factor (C)" present verbatim.
- S6 (85%/15% search endurance rule) — §H.5.2.2 text confirmed verbatim: *"assumed to be 85 percent
  of on scene endurance, allowing 15 percent for identifying sighted objects..."*
- S7 (H-60 6.0-hour MAX endurance) — Table 5-3 "Coast Guard Aircraft Characteristics" confirmed,
  H-60 row: MAX Endurance (hrs.) = **6**.
- S8 (64.75% POC at fs=1.1) — confirmed verbatim: *"As shown in Figure H-24, an optimal search
  factor of 1.1 produces a POC of 64.75%."*
- S9 (Figure H-22, divergent vs. single-point datum curves) — figure title present in the table of
  contents and figure list.
- S10 (total probable error / optimal search factor concept) — §H.2.1.1/§H.5.6.3 language ("total
  probable error of position," "optimal search factor") confirmed present.

No source 404s, moved, or dropped its cited figure. **PASS.**

---

**Framing-discipline check (SPEC §6 human-reviewed sensitivity flag — person-overboard scenario).**
Re-verified after the full `FACILITATOR.md` rewrite: every new section (Intro, Launch, all 4
Anchors, Data Deep Dive, Twist, Immediate recommit, Deep conflict, Close, Lessons Learned, and all 5
Socratic questions) stays inside the same register the original human review approved — real
leeway/set-and-drift modeling methodology and decision-making mechanics only, no depicted injury,
peril, or outcome. The Twist in particular was deliberately built from a genuine, verified
modeling-methodology finding (which unsourced assumption is actually load-bearing) rather than any
narrative escalation. `case.md`'s Appendix G still cites the real 2013 Aldridge rescue as
successful-rescue-methodology evidence, unchanged. **Consistent.**

---

## Report back

**State reached: TIER1_PASS.** Tier 1: 0 BLOCKERs, 1 GAP (T1-10, doctrine-approved
reinforcement carve-out), 5 POLISH notes (all `published/`-pending, nothing to fix pre-publish).

**Tier 2: 5/6 probes PASS, 1 adjudicated false positive (P1).** No open Tier 2 blockers.

**MA12/MA13 verified sensitivity (the user's specific question) — real numbers, not the case's
original unverified claims:**

| assumption | case's original claim | verified (sensitivity_model.py, 2026-08-31) |
|---|---|---|
| MA12 (growth_rate_B_kt, stated 0.45 kt) | flips below ~0.35 kt | does **not** flip within ±50% in either direction; real flip threshold is an **increase** to ~1.55 kt (~3.4×, +244%) — opposite direction, much larger magnitude |
| MA13 (poc_A_pct, stated 55%) | flips above ~61% | flips at +50% (55%→82.5%); real flip threshold is **~64.75%** (Option B's own sourced POC), disclosed per `case.json.sensitivity_disclosure[]` (category X) |

Option B (Set-and-Drift Datum, verified margin ≈15.1%) is genuinely fragile to MA13 but not to
MA12 — and the case's own prior claims about both dials were incorrect in direction, magnitude, or
both.

**Report path:** `cases/the-search-box/QA_REPORT.md`
**Model:** `cases/the-search-box/sensitivity_model.py`

---

## Prior run — 2026-08-31 (BLOCKED, superseded by the remediation above)

*Kept for history. See "What was fixed" above for how each finding was resolved.*

**State reached:** DRAFT (Tier 1 BLOCKED, did not reach TIER1_PASS)

**BLOCKERs (6):** T1-04 Challenge 5 boilerplate diverges (facilitator-only comment appended
without separation); T1-10 empty `new_coverage[]` with no carve-out note; T1-13 ×3 (no anchor
ladder, no Twist section, no 45-minute Socratic plan); T1-14 `margin_pct` continuity drift between
`case.json` (15) and `FACILITATOR.md` (no 15% stated anywhere).

**GAPs (4):** 0 Socratic questions vs. 5 required; 4 orphan numbers in `FACILITATOR.md` (14.5,
15.1, 17.0, 99.99) with no home in case.md/case.json; no `case_md_sha256` recorded; no
`cohort_bands[]` declared.

**MA12/MA13 individual sensitivity:** Not established — Tier 2/P5 never ran (blocked by Tier 1 and
by a missing `sensitivity_model.py`).
