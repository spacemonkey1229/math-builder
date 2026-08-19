# Roadmap — Math Builder

**v2.10 · 2026-08-18.** Supersedes v2.9. **Delta: the ten cases sitting in the pipeline's
`readiness` stage were re-verified against the actual gate scripts rather than trusted at their
self-reported `case.json.qa` state, and all ten are now genuinely `TIER2_PASS`/`published`.** Five
had already reached that bar in a prior session (`a-coachs-dilemma`, `codebreaker`, `cold-chain`,
`end-of-life`, `seton-hall`) and were re-verified clean, not re-worked. The other five needed real
fixes before the claim was true, not just a status flip:

- **`airplane-manufacturer` and `family-trip`** were `BLOCKED` on live re-run (`T1-15`/`T1-18`
  CONTINUITY STALE — their `published/*.html` predated the last edit to `case.md`). Both were a
  genuine staleness, not a content defect: a prior session had moved facilitator-only content out
  of the student-facing `case.md` into `FACILITATOR.md` (correct, per the "never ship the answer in
  the student packet" rule) without regenerating the HTML afterward. Rebuilt/re-verified and both
  cleared `TIER1_PASS` (0 blockers) again. `family-trip` additionally had a stale `qa.case_md_sha256`
  (T1-16) and a real, small propagation bug caught while rebuilding its packet: the Overview still
  said Allegiant's lap-child policy is "one per adult" after Appendix D and `case.json` had already
  been corrected to the airline's real rule ("one per row") — the same class of single-line
  propagation miss `seton-hall`'s own QA history already named once. Fixed in `case.md` and the
  interactive HTML both.
- **`family-trip` itself was only `TIER1_PASS`** at the start of this pass — no full Tier 2 run had
  ever been recorded, just a standalone mechanical P5. Ran the other five probes for real (a
  genuinely fresh subagent for P1 and a second one for P3, direct work for P2/P4, live fetches of
  all 10 web sources for P6). P6 found two real, load-bearing defects: `S8`'s URL was a dead
  third-party mirror and the case's stated policy text was itself wrong (Allegiant's real rule is
  "per row," not "per adult" — the same fact as above, caught twice from two directions); `S12`
  resolved but backed the wrong IRS mileage-rate announcement (72.5¢, not the case's cited 76¢) —
  the 76¢ figure itself was correct, re-pointed to the announcement that actually states it. Both
  fixed. `family-trip` reached genuine `TIER2_PASS` with 0 real FAIL (P5 stays PASS-disclosed, the
  project's standing state for a stated-assumption instability that's written down rather than
  hidden — the same treatment `wildfire`/`airstrike` already use).
- **`airstrike`, `wildfire`, `redrawing-lines` were already genuinely `TIER2_PASS`** on arrival —
  their `QA_REPORT.md` files record real fresh-subagent P1/P3 runs, real live P6 fetches, and (for
  `airstrike` and `wildfire`) real defects that a prior pass found and fixed before the probes
  actually passed (a leaked trap-detector-defeating wording, a `FLEX` sweep that was a structural
  no-op and vacuously "passed" P4/P5 against parameters `evaluate()` never reads). No rework needed;
  re-verified live and left alone.
- **All four `qa`-status cases plus `family-trip` were promoted through `case-publish`**: built the
  missing packet files (student `.docx`, facilitator-guide `.docx`, `.xlsx` workbooks where the
  appendices warranted one, `MANIFEST.json`) for whichever were missing — `redrawing-lines` had
  **no `published/` directory at all** and needed its interactive HTML built from
  `templates/interactive_shell.html` from scratch, the project's first real proof that the A7
  scaffold works for a case authored after Cold Chain. Every rebuilt student `.docx` was rendered to
  PDF and read to confirm no facilitator content (the trap, the balance arguments, the margin)
  leaked across — 0 leaks found across all five packets. Promoted each to the read-model
  (`standards_spine.json`/`cases_index.json`/`gap_queue.json`) and flipped `case.json.status` to
  `"published"`.

**A real regression was found and fixed in the read-model itself, not in a case.** After all five
promotions, `standards_spine.json.totals.uncovered` read 76 — down only 5 from the 81 measured at
the start of this pass, when the eight individually-verified newly-closed skill ids
(`geometry-vertex`/`concave`/`irregular-polygon`/`quadrilateral` from `airplane-manufacturer`;
`discrete-mathematics-base-case`/`mathematical-induction`/`inductive-step`/its how-to from
`redrawing-lines`) should have moved it by 8. Diffing the promotion script's own
`readmodel/_snapshots/` (its safety net, working exactly as designed) found the cause: the
`family-trip` promotion's write — which should have been a pure no-op, since `family-trip`'s title
was already in `standards_spine.json.cases[]` from the original pre-pipeline corpus scan and its
own `case.json.new_coverage[]` is empty — instead **silently stripped `airplane-manufacturer` from
62 skills' `covered_by[]` and `wildfire` from 77**, cutting their broad legacy-scan-era tagging down
to only their narrow, freshly-curated `standards[]` claim (97→35 and 92→15 respectively). This
pattern — a legacy-converted case keeping both its old broad corpus-scan tag *and* its new curated
claim — is normal and matches every other legacy-converted case in the corpus (`codebreaker` is
26 curated vs. 42 total covered; `end-of-life` is 11 vs. 49); nothing else in the pipeline
documents or authorizes silently retiring the broad tag, so this was data loss, not a cleanup.
**Fixed by restoring `standards_spine.json` from the promotion script's own pre-write snapshot**
(`readmodel/_snapshots/standards_spine.20260818T220557.json`, the state immediately after
`redrawing-lines`'s correct promotion and immediately before `family-trip`'s), regenerating
`gap_queue.json` from the restored spine, and confirming `cases_index.json` was never touched by
the same bug (diffed clean against its own snapshot pair, only `family-trip`'s own row legitimately
changed). Root cause not fully diagnosed — the documented `case-publish` §2 script only ever
*appends* to `covered_by[]`, so this was very likely an ad hoc rewrite the promoting agent wrote
itself to handle the "title already in `cases[]`, still need to flip `status`" edge case the
documented script doesn't explicitly cover, not the script as written. Worth a real fix to
`case-publish`'s own promotion snippet (an explicit idempotent-but-still-flip-status path) so the
next case with this exact shape doesn't reopen the same hole; **not done in this pass**, filed
below.

**Where the chunk of ten ended up, all ten now genuinely `TIER2_PASS`/`published`:**

| case | starting `qa.state` / `status` | ending `qa.state` / `status` | what actually changed |
|---|---|---|---|
| `a-coachs-dilemma` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `codebreaker` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `cold-chain` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `end-of-life` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `seton-hall` | `TIER2_PASS` / `published` | unchanged | re-verified live, clean, no rework |
| `airplane-manufacturer` | `TIER2_PASS` (self-reported) / `qa` | `TIER2_PASS` / `published` | was `BLOCKED` on live Tier 1 (stale published HTML) — rebuilt; packet completed (docx/xlsx/facilitator guide/MANIFEST); promoted |
| `airstrike` | `TIER2_PASS` / `qa` | `TIER2_PASS` / `published` | live Tier 1/2 re-verify clean, no rework; packet completed; promoted |
| `wildfire` | `TIER2_PASS` / `qa` | `TIER2_PASS` / `published` | live Tier 1/2 re-verify clean, no rework; facilitator-guide docx + MANIFEST added; promoted |
| `redrawing-lines` | `TIER2_PASS` / `qa` | `TIER2_PASS` / `published` | had **no `published/` directory at all** — full packet built from scratch, including the interactive HTML from the A7 shell (case #2 proof); promoted |
| `family-trip` | `TIER1_PASS` / `qa` | `TIER2_PASS` / `published` | ran the 5 missing Tier 2 probes for real; fixed 1 propagation bug + 2 P6 citation defects; built the full packet; promoted |

`python3 app/build_pipeline.py`: `readiness` stage 10 → **0**, `promotion` stage 38 → **49**.
`python3 app/build_dashboard.py --verify`: 4 pre-existing, unrelated failures remain (down from 11
before this pass rebuilt the dashboard's cached page — the rebuild alone closed 7 of the original
11, which were the dashboard's own embedded coverage numbers having gone stale against the spine,
not real defects). The 4 that remain predate this session and are untouched by it:
`legacy_readiness` case count vs. `corpus_index` legacy count (45 vs. 63, a pre-existing corpus-
accounting drift), `derived skill ids match cases_index standards_count` (a pre-existing list of
cases whose `cases_index.json` cached `standards_count` has drifted from their live `case.json`),
the 2-cluster B2 backlog (`Calculus`/`Derivatives`, `Discrete Mathematics`/`Formal Logic` — already
documented, not newly found), and legacy cases carrying `margin: 0` instead of `null`. None are new
regressions from this pass; 0 self-checks newly broke.

**Coverage after the chunk closes:** `standards_spine.json.totals`: `skills` 437 (unchanged),
`cases` 71 (was 69), `uncovered` **73** (was 81 at the start of this pass), `thin_1_2` 196.
`readmodel/domain_coverage.json` was **not** regenerated in this pass (out of scope — the task
asked to run `build_pipeline.py`/`build_dashboard.py --verify`, not a domain-coverage rebuild) and
is now stale against the spine (`spine_skills_uncovered: 199` there vs. the live 73) — flagged
honestly, not silently trusted, the next time someone reads that file.

---

## Track B — major remaining skill gaps (2026-08-18 snapshot)

19 spine groups still carry at least one zero-coverage skill, 73 skills total. The ten highest by
raw zero-count, most recomputed after this pass's two closes above:

| zero | of | domain / group |
|---|---|---|
| 8 | 8 | Discrete Mathematics / Set Theory |
| 7 | 24 | Geometry / Fundamentals Of Geometry |
| 7 | 8 | Discrete Mathematics / Formal Logic |
| 7 | 7 | Pre-Calculus / Matrices |
| 6 | 6 | Pre-Calculus / Polar And Parametric |
| 6 | 6 | Calculus / Limits And Continuity |
| 5 | 5 | Pre-Calculus / Trigonometric Identities |
| 5 | 5 | Pre-Calculus / Introduction To Limits |
| 4 | 5 | Calculus / Series |
| 3 | 10 | Geometry / Surface Area And Volume |

`cases/_concepts/CONCEPTS_next10-careers-gapclose_2026-08-18.md` already scopes ten career-anchored
concepts against exactly these groups, ranked by skills-closed × feasibility. **Two of its ten need
re-checking before anyone writes them, because this pass's promotions moved the ground under them
without anyone intending to:** `redrawing-lines`'s `new_coverage[]` fully closed Discrete
Mathematics / Proof And Recursion (4 of 7 zero → 0 of 7) — **C9 "Prove It Scales" is now moot, its
entire target skill set already covered, drop it from the queue rather than write it.**
`airplane-manufacturer`'s closed Geometry / Fundamentals Of Geometry's `vertex` and Geometry /
Quadrilaterals And Polygons' `concave`/`irregular-polygon`/`quadrilateral` — **C7 "The Roofline
Call" now closes 7 skills instead of 8, and C8 "The Irregular Boundary" now closes 2
(`convex`/`parallelogram`) instead of 5**, which likely moves C8 below the write-worthiness bar the
concept sheet itself set (it was already the lowest-scored, MEDIUM-feasibility entry in the batch).
The other seven concepts (**C1** Grant Reach, **C2** The Contrapositive Claim, **C3** The
Multiplier Recruit, **C4** The Fan Formation, **C5** The Reserve Asymptote, **C6** The Tracker's
Angle, **C10** The Cheap Approximation) are untouched by anything in this pass. The concept sheet's
own recommendation stands and is now stronger: write **C5 (The Reserve Asymptote, score 12.2)**
first — it closes two full zero-coverage groups at once (Pre-Calculus Introduction To Limits +
Calculus Limits And Continuity, 11 skills, HIGH feasibility off public SOA/CDC mortality tables) —
then **C1** and **C3**, both HIGH-feasibility, both untapped careers, both still a clean one-group
fit.

---

**v2.9 · 2026-08-12.** Supersedes v2.8. **Delta: this file was eleven days stale, and the gap was
structural rather than clerical.** Between 2026-08-04 and 2026-08-12 the project shipped an entire
architecture that no roadmap track described — a local admin server (D-015), a hosted Flask app on
Vercel + Neon Postgres with passcode auth (D-016), an override-id fix (D-017), a public
student-facing case page (D-018), an Assign-a-Case redesign (D-019) — plus roughly fifteen more
authored cases. None of it appeared here, in README, in TECH_STACK or in DOCTRINE_LEDGER; a grep of
all six governance docs for `vercel|neon|postgres` returned zero hits. Corrected in this pass, with
five new doctrine rows (MCS-41→45).

**Three claims in v2.8 below are now false, and are corrected rather than deleted** (the v2.8 text
is left as written, per append-only discipline — read it as a 2026-08-01 snapshot):

1. **"Do not author case #2 until Cold Chain is `VERIFIED`"** (Track A's depth-before-breadth rule)
   — roughly fifteen more cases were authored. Tide Window was recorded as a deliberate stated
   exception; the Aug 4–5 batch of ten was not recorded as anything. The rule was not repealed, it
   was simply outrun. **What actually happened is more interesting than a rule violation:** the
   batch that ignored the rule produced ten cases at `TIER1_PASS` with no sensitivity model and no
   QA report, and the five cases authored 2026-08-12 — after the tooling matured — all clear
   `TIER2_PASS` with the full five-file packet. Depth-before-breadth was right about *why*, and the
   fix was better tooling rather than slower authoring. Track A's rule is hereby amended to the
   thing it was actually protecting: **do not mark a case `published` below `TIER2_PASS`** (MCS-41).
2. **A7 "no case #2 has used [the interactive shell] yet"** — every authored case now ships an
   `Interactive.html`. The scaffold is proven. What remains open is the narrower original point: no
   case's Working Notebook JS is a genuine *port* of its `sensitivity_model.py`, so the two can
   still silently drift (see `templates/INTERACTIVE_HTML_CONTRACT.md`).
3. **A2 "every future case needs its own `sensitivity_model.py`"** — stated as an open item, then
   not enforced for ten cases. Now mechanically swept by `scripts/apply_publish_gate.py` (MCS-41).

**The blocking fact is unchanged and is now the *only* blocker: no case is `VERIFIED`.** What has
changed is why. On 2026-08-01 there was no path to get a case to a learner and a score back. That
path now exists, is deployed, and has run the full assign → submit → machine-score → guide-confirm →
revise → resubmit → accept → complete cycle for real, repeatedly, with real submission files (see
`student_work/UAT_LOG.md`, `student_work/LIFECYCLE_SCRIPT.md`). **A3 is now a scheduling and
facilitation problem, not an engineering one.**

**New top-of-queue item — A8 · backfill the ten demoted cases.** D-020 demoted the Aug 4–5 batch
from `published` to `qa`, which makes them unassignable in the live app until each has a
`sensitivity_model.py` and a real Tier 2 run. Ten cases × (a declarative model + a probe run + a
QA report). This is now the largest single piece of open Track A work, and it is a direct,
quantified cost of having shipped past the gate — worth stating plainly rather than burying.

---

**v2.8 · 2026-08-01.** Supersedes v2.7. Delta: three roadmap items closed in one session —
**A7** (`templates/interactive_shell.html` + `INTERACTIVE_HTML_CONTRACT.md`, the case-agnostic
scaffold Cold Chain's hand-built interactive HTML never had), **B2** (spine extended into
Pre-Calc/Calculus/Discrete Mathematics, 322 → 437 skills, all three branches' `has_standards_rows`
flips true for the first time), and **C3** (Drive-folder submission intake designed against
`roster.json`/`submissions.json`/`case-track`, MCS-40). `build_domains.py`/`validate_domains.py`
(28/28) and `build_dashboard.py --verify` (140/140) all re-run clean, including three self-test
assertions that B2 made false and were fixed to test the real invariant rather than a
now-stale fact. Cold Chain itself was deliberately left untouched throughout. See
`DOCTRINE_LEDGER.md`'s 2026-08-01 change-log entries for each.

**v2.7 · 2026-08-01.** Supersedes v2.6. Delta: project renamed to Math Builder — folder physically renamed (`Math Case Studies/` → `Math Builder/`, 320 files verified intact) and every forward-facing title/reference updated to match (README, this file, DOCTRINE_LEDGER, TECH_STACK, DECISIONS, 00_SESSION, both skill docs with literal paths, the dashboard generator + regenerated dashboard.html/student.html, the Cold Chain interactive HTML footer). Historical changelog rows describing pre-rename events were left as written, per append-only discipline. `build_dashboard.py --verify`: 140/140 pass post-rename.

**v2.6 · 2026-08-01.** Supersedes v2.5. Delta: graduated to a fully independent project — `00_SESSION.md` is now this project's complete, self-contained instructions (no longer deferring to Best Practices' reading list or hard lines); `TECH_STACK.md` rewritten as this project's own authoritative record (no longer "reference + addendum"); the ACTIVE/WIP-3-cap conflict resolved by exit, not by triage — a workspace survey found 8+ other projects already over that cap, a pre-existing condition outside this project's scope. See `DOCTRINE_LEDGER.md`.

**v2.5 · 2026-08-01.** Supersedes v2.4. Delta: formally onboarded into the Best Practices governance system on request — added `00_SESSION.md` (per-project instructions block, `SESSION_PROTOCOL.md` template) and `TECH_STACK.md` (reference + addendum, not a copy); README.md now declares State/Phase in `PORTFOLIO_WIP.md` vocabulary. Flagged, not resolved: this project is honestly ACTIVE, and the portfolio was already known to be over the 3-ACTIVE cap — see `00_SESSION.md`.

**v2.4 · 2026-08-01.** Supersedes v2.3. Delta: verifying the already-shipped root-connections spine (rather than trusting the task list) caught real drift from the day's other changes — `domains.json` rebuilt fresh, a genuine two-skills-share-one-label gap fixed for Digit and Congruent (see `DOCTRINE_LEDGER.md`), `dashboard.html`/`student.html` rebuilt (were 1 day stale). `validate_domains.py` 28/28, `build_dashboard.py` 140/140, both clean. **v2.3 delta (superseded by this one):** RUBRIC.md C1 amended for MCS-39's tension with Challenge 1; B1 (`case-reconcile`) worked to its honest ceiling — 28 → 45 cases, 97 → 93 uncovered. Delta: RUBRIC.md C1 amended for the tension MCS-39 created (the case's own glossary now answers Challenge 1's "research it yourself" questions) and `score_submission.py` flags a byte-identical repost; B1 (`case-reconcile`) worked to its honest ceiling — a human read all 30 remaining 0-HIGH/0-MEDIUM cases, fixed a real plural-matching bug in the tool, and hand-confirmed 10 more cases with genuine evidence — `standards_spine.json.cases[]` 28 → 45, `uncovered` 97 → 93, 20 titles remain correctly untagged (2 revisions, 18 with no explicit math content). **v2.2 delta (superseded by this one):** MCS-39 (hover+hyperlink math glossary) shipped and locked into `case-readiness` as `T1-19`; B1 first pass confirmed 7 cases, 28 → 35. v2.1 delta (A1/A2/A5/A6 done, new A7) and v2.0 logic otherwise unchanged. v1.0 kept at the bottom as the shipped record.

Six tracks. They are **not** sequential — but there is a hard ordering rule inside two of them, and one fact blocks everything.

> **The blocking fact.** No case in this system is `VERIFIED`. Cold Chain was rewritten on 2026-07-31 to close the allocation ambiguity that first blocked it, and now reaches `TIER1_PASS` (0 blockers) with Tier 2 PASS-with-disclosed-findings on four probes (re-verified with fresh, uncontaminated subagents), a mechanical FAIL on the fifth (a real, disclosed sensitivity — not a defect), and the sixth — **attempted for real on 2026-08-01** with live network access — genuinely partial: 3 of 11 distinct cited URLs confirmed live and accurate, 1 real finding flagged for a human to check, 7 inconclusive because several source sites (UNICEF, CDC, medRxiv) block automated fetchers outright and one WHO PDF link now redirects to a JS app shell. Not a clean `TIER2_PASS` either way. That is real progress, and it is still not `VERIFIED` — no case has run with real learners. Until one does, every quality claim here is a machine claim. HIGH GRADE cleared thirteen structural checks and six simulated probes and still failed in a live room. Track A exists because of that sentence. **Resolved:** `case.json`/`cases_index.json` had both said Cold Chain's `status` was `"published"`, inconsistent with a `qa.state` that has never reached `TIER2_PASS`. User's rule: publish only on a confirmed QA-threshold pass. Corrected both to `status: "qa"` — the published files on disk are untouched, only the pipeline's own state flag moved to match reality. **Cold Chain is not currently assignable** (`case-track` requires `published` or `legacy`) until it genuinely clears `TIER2_PASS` and runs through `case-publish`.

---

## Where things actually stand

| | |
|---|---|
| Case studies in the corpus | 56 (55 legacy + Cold Chain) — note: `case-reconcile`'s own docx-title accounting (which excludes `Best Of Studio` duplicates and reads each doc's real title) found 37 untagged titles against this corpus, not exactly `56 − standards_spine.cases`; the two counts use different methods and were never fully reconciled |
| Cases with a standards row (`standards_spine.json.cases[]`) | 45, up from 28 before `case-reconcile`'s two 2026-08-01 passes (7 automated HIGH/MEDIUM confirms, then 10 more from a human read-through of the LOW-only backlog) |
| Atomic skills | 437, up from 322 — B2 (2026-08-01) added 115 across three new Pre-Calc/Calculus/Discrete domains; all 437 ids globally unique |
| Skills with zero coverage | 208, up from 93 — the 115 new B2 rows all start at `n:0` honestly (no case exercises HS-stretch content yet); the pre-existing 93 is **still technically an upper bound** per the same caveat as before (20 read-by-hand untagged titles, 2 confirmed revisions, 18 genuinely name no math content) |
| Curriculum branches with no standards rows at all | **0**, down from 3 — Pre-Calc/Calculus/Discrete all now have real rows (B2, 2026-08-01) |
| Application domains mapped | 40, across 12 clusters, 121 live-verified sources |
| Uncovered skills now reachable from a domain | 116 of 208 — the pre-B2 93 stayed fully reachable; 92 of the 115 new B2 rows are not yet folded into a domain's `signature_skills[]` (disclosed, not hidden: `domain_coverage.json.totals.uncovered_skills_still_orphaned`) |
| Cases with Guide Notes | 40 of 56 |
| Cases with a timed Socratic plan | 2 of 56 |
| Cases `VERIFIED` by human dry-run | **0** |
| Cases currently passing the readiness gate | Cold Chain: `TIER1_PASS` (0 blockers) &middot; Tier 2 PASS-with-findings on 4 probes, mechanical FAIL on 1 (disclosed), 1 genuinely partial (3/11 URLs confirmed live 2026-08-01, 7 inconclusive/bot-blocked, 1 finding flagged) — not `TIER2_PASS`, and `status` corrected to `"qa"` (2026-08-01) to match — not currently assignable |
| Cases shipping a case-owned `sensitivity_model.py` | 1 of 1 pipeline cases (Cold Chain) |
| Cases shipping the MCS-37 interactive HTML | 1 of 1 pipeline cases (Cold Chain) — hand-built; a reusable scaffold now exists (`templates/interactive_shell.html`, A7, 2026-08-01) but no case #2 has used it yet |
| Cases shipping the MCS-39 hover+hyperlink math glossary | 1 of 1 pipeline cases (Cold Chain) — 15 terms, 14 how-to links, all urls fetched and confirmed live |

---

# TRACK A · Quality — make one case actually trustworthy

**The rule for this track: depth before breadth. Do not author case #2 until Cold Chain is `VERIFIED`.** A pipeline that produces twelve cases carrying the same undisclosed-convention defect is worse than one that produces a single clean case slowly.

### A1 · Unblock Cold Chain ✅ *(done 2026-07-31 — re-verified with fresh subagents)*

Fixed by redesign, not disclosure: Order A rebuilt as 4 boxes ($408.84 of $420, 3 truck + 1 motorcycle, stated as Appendix F Assumption 0), so the allocation question the old design left ambiguous is now moot — there's no shortfall left to allocate. Re-ran the full ladder afterward with **fresh, uncontaminated subagents** for the four simulated-play probes: all four passed, and they found two smaller, real, previously-undisclosed sensitivities (the twist's `opening_cost_h ≥ ~2.65h` floor; Assumption 2's ±50% fragility) which are now disclosed in Guide Notes and `case.json` rather than hidden. See `cases/cold-chain/QA_REPORT.md` § *Rewrite + re-verification*. **P6 attempted for real 2026-08-01** (see § *Tier 2 probe 6 attempted for real*) — 3/11 URLs confirmed, 7 inconclusive due to site-side bot blocking, not something more network access alone fixes next time either. **Still open, and not something this pipeline can close alone:** A3 (the actual human dry-run) needs a real guide and room.

### A2 · Ship a `sensitivity_model.py` per case ✅ *(done for Cold Chain 2026-07-31)*

Tier 2 probe 5 returns `NOT RUN` without a declarative model. `cases/cold-chain/sensitivity_model.py` now ships as the case's own model (not the skill's reference model) — `PARAMS`, `FLEX = [opening_cost_h, in_spec_fraction]`, `evaluate()`, `evaluate_twist()`, verified to reproduce the published 8,200/7,000 base and the twist's tie. **Still open:** every future case needs its own; there is no scaffold/template yet that generates the boilerplate half of this file.

### A7 · Templatize the interactive-HTML generator (MCS-37) ✅ *(scaffold done 2026-08-01)*

Cold Chain's `published/*.html` was hand-built end to end — narrative markup, SVG diagrams, the self-checking calculator's JS, and (as of 2026-08-01) the MCS-39 math glossary were all authored bespoke for this one case. That does not scale past case #2. Built `templates/interactive_shell.html` (the crest/icon `<defs>`, CSS design system, nav/tab scaffolding, checklist/localStorage logic parameterized by `CASE_ID`, dilemma-pick widget, twist-reveal gating, and the `gtermHTML`/`renderGlossary` glossary render function — all case-agnostic, extracted verbatim from Cold Chain and marked with `{{PLACEHOLDER}}` tokens for every case-specific block) and `templates/INTERACTIVE_HTML_CONTRACT.md` (the `sensitivity_model.py` ↔ JS-port contract — same `PARAMS`/`FLEX`/`evaluate()`/`evaluate_twist()` names on both sides, which Cold Chain itself does *not* follow today, its JS tally being a hand-derived parallel rather than a port; the `T1-18`/`T1-19` gotchas, incl. the JS-data-object-wins-over-static-anchors precedence bug MCS-39 already found once; and a 14-term starter glossary reusing Cold Chain's own already-fetched-and-confirmed Khan Academy links verbatim, since MCS-21 treats a reused verified source as legitimate, not fabricated). `skills/case-publish/SKILL.md` §1 updated to point at the shell instead of a blank file, and its `MANIFEST.json` template now lists the `.html` (previously undocumented — case-publish doesn't build or verify it, but it should at least be recorded). **Still open:** this is a scaffold, not a generator — a human still authors each case's diagrams, narrative, and notebook logic by filling the shell; there is no code that emits a filled `.html` from `case.json` automatically. It has not yet been proven against a real case #2, because none has been authored since Cold Chain (Track A's own depth-before-breadth rule). Cold Chain's own file was deliberately left untouched rather than retrofitted onto the shell, to avoid risking regression in the one case closest to `VERIFIED`.

**Update, same day:** the shell shipped with a real bug — a nested HTML comment closed 20 lines early and mangled the raw file when opened in a browser (caught by the user actually opening it). Fixed and verified with a proper comment tokenizer. Also added `autoLinkGlossaryTerms()` on request: MCS-39 asks for hover+hyperlink "on any concepts that need explanation," which Appendix G alone doesn't deliver — the shell now auto-wraps the first mention of each glossary term wherever it actually appears in the case's own prose (Overview, Background, Appendices, Notebook, Twist), not just in a list at the bottom. Verified end-to-end against a filled test fixture (built and torn down inside the project folder so the browser preview actually ran the JS) — caught and fixed a second real bug in the process (the seeding step was counting Appendix G's own anchors as "already linked," silently defeating the whole feature). See `templates/INTERACTIVE_HTML_CONTRACT.md` §4 and DOCTRINE_LEDGER's 2026-08-01 entry.

### A3 · First human dry-run → first `VERIFIED` case

A guide runs Cold Chain with a real cohort and fills `templates/RUN_REPORT.md` **during** the session. Facts first. Use the **"can't tell"** column honestly. This is the only way to learn whether the twist lands, whether Anchor 2 keeps learners off the calculator, and whether 45 minutes is the right length.

### A4 · Wire the last UNWIRED rules ✅ *(done — verified 2026-08-01)*

MCS-29 (`tier3_verify.py`), MCS-31 (`guide_confirm.py --audit --write` + the `demoted_criteria.json` overlay), and MCS-17 (`case-reconcile`, built in B1) are all genuinely `WIRED`. This item's real work turned out to be a ledger correction, not new code: `DOCTRINE_LEDGER.md` carried a stale, contradictory duplicate row for each of the three — left over from before the Tier 1/2/3 gate rebuild and `case-reconcile` — still claiming `CODIFIED`/`UNWIRED` alongside the later, correct `WIRED` row. Removed the stale duplicates so each rule has exactly one row, matching what the ledger's own UNWIRED queue had already (correctly) marked `CLOSED`. See DOCTRINE_LEDGER's 2026-08-01 "A4 closed" change-log entry.

### A5 · Fix the duplicate skill ids ✅ *(done 2026-07-31)*

Group-scoped the 2 colliding ids (`Digit` in Numbers-And-Counting, `Congruent` in Fundamentals) to `number-sense-numbers-and-counting-digit` / `geometry-fundamentals-of-geometry-congruent`, keeping the ids `domains.json` already referenced unchanged. 322 skills, 322 unique ids now, both pairs were n=0 so no case data moved. See MCS-36.

### A6 · Design cohort bands ✅ *(done 2026-07-31, applied to Cold Chain)*

Three named bands — Full (12–20), Compressed (6–11), 1:1 or pair (1–2) — each saying what compresses in the anchor ladder and which Deep Conflict threads survive. Transferred from the HIGH GRADE kit as process only. See MCS-25 and `case.json.cohort_bands[]`. **Still open:** only Cold Chain has bands; every other case with Guide Notes (B3) will need its own.

---

# TRACK B · Coverage — close the map

**Ordering rule: tag before you author.** The uncovered-skills figure was a 97-skill upper bound polluted by untagged cases; `case-reconcile` has now worked that backlog to its honest ceiling (see B1) and the real number is 93. Authoring against a wrong gap list wastes the most expensive resource here.

### B1 · `case-reconcile` — tag the untagged cases ✅ *(built, run, and worked to its honest ceiling — 2026-08-01)*

Built and run for real against the corpus (not the estimated 31 — **37** untagged cases actually found; source docs live under messy, inconsistent folder names, so the skill reads each doc's own title heading rather than trusting the folder). Every proposed skill carries a quoted evidence sentence and a HIGH/MEDIUM/LOW confidence grade. **First pass:** 7 cases carried a real vocabulary section and matched cleanly at HIGH confidence, confirmed automatically (College Football Playoff Committee, Driving Age, Fast Food, Life Insurance Agent, Medical Statistician, City Planner, Robotics Engineer). **Second pass — the human read the SKILL.md itself calls for:** all 30 remaining 0-HIGH/0-MEDIUM cases were read directly, source docx by source docx. That read (1) caught and fixed a real precision bug in the matcher (`match_term()`'s word-boundary regex didn't tolerate a plain plural, so "Histograms" never matched the "Histogram" skill), and (2) hand-confirmed 10 more cases via `--skills` where the actual sentence showed genuinely load-bearing math content rather than coincidental English — Acton Survey (a real sampling-methodology case), Biostatician, Caribbean Internet Cafe, Electoral College, Loan Officer, Medical Transport, Player Of The Year, Logic, Gerrymandering, Insurance Actuary. `standards_spine.json.cases[]`: 28 → 45, `uncovered`: 97 → 93. **Closed, not abandoned:** the remaining 20 titles were also read, not skipped — 2 are genuine revisions of already-tagged cases (Phone Plans/2.0 against "Phone Plan"; Which (Investment) Portfolio? against "Investment Portfolio" — same character, same premise, a rewrite), and 18 genuinely name no explicit math vocabulary anywhere in their source text. That is this corpus's real ceiling, not unfinished work.

### B2 · Extend the spine into Pre-Calc, Calculus, Discrete ✅ *(done 2026-08-01)*

Three branches had *no rows at all*. Added 115 skill rows across three new `standards_spine.json` domains — **Pre-Calculus** (41 skills / 6 groups: trig functions, identities, polar & parametric, vectors, matrices, intro to limits), **Calculus** (38 skills / 6 groups: limits & continuity, derivatives, applications of derivatives, integrals, applications of integrals, series), **Discrete Mathematics** (36 skills / 5 groups: set theory, formal logic, graph theory, combinatorics, proof & recursion) — following the existing id/group/`covered_by`/`n` conventions exactly (MCS-36's id-collision rule checked programmatically; 0 collisions). `curriculum_tree.json`'s three branches now carry `acton_domains: ["Pre-Calculus"]` / `["Calculus"]` / `["Discrete Mathematics"]`, so `has_standards_rows` flips to `true` for all three automatically. `readmodel/standards_spine.json.totals`: `skills` 322 → 437, `uncovered` 93 → 208 (every new row starts at `n:0`, honestly — no case exercises HS-stretch content yet). Snapshot taken before write (MCS-22). New spine ids also folded into 12 existing domains' `signature_skills[]` where the fit is real (not padding) — oceanography's tides (`pre-calculus-sine-function`/`amplitude`/`period-of-a-function`, `calculus-definite-integral`), aviation/surveying-geodesy's bearing math (`pre-calculus-vector`), spaceflight's rocket equation (`calculus-derivative`), computer-graphics' transforms (`pre-calculus-matrix`), cryptography-security/network-science/maritime-shipping/education-systems/tiling-pattern-art's counting and graph problems (`discrete-mathematics-*`), music-acoustics' waveforms (`pre-calculus-sine-function`). `build_domains.py`/`validate_domains.py` (28/28) and `build_dashboard.py --verify` (140/140) all re-run and pass — three of the 140 checks had hardcoded a now-false assumption (that these 3 branches would *always* render "unmapped," never a real 0%) and were fixed to assert the actual invariant (0% is never used to mean "no rows exist") rather than the stale fact. **Honestly disclosed, not closed:** only 116 of the 208 total uncovered skills are reachable from a domain's `signature_skills[]` today (`domain_coverage.json.totals.uncovered_skills_still_orphaned: 92`, almost all of them the newly-added rows) — B2 built the taxonomy; folding every new skill into a domain the way the original 93 were is B4-shaped follow-on authoring work, not done here.

### B3 · Backfill Guide Notes and Socratic plans

16 cases have no Guide Notes. 54 have no timed plan. The discussion is where the learning lands, so a case without facilitator scaffolding is half an artifact. Prioritize by actual use, not alphabetically.

### B4 · The authoring queue — gap-driven, domain-anchored

All 93 currently-uncovered skills are now reachable from a domain with named free data, so the queue writes itself. In priority order by skills closed:

| # | Case concept | Domain | Closes | Why |
|---|---|---|---|---|
| 1 | Tiling / pattern commission | `tiling-pattern-art` | **27** | Hits the polygon *and* transformation clusters at once; MIT Tiling Search gives real measurable patterns |
| 2 | Marching band drill design | `drill-choreography` | 14 | A football field is a painted coordinate grid. 14 of the 20 transformations. The surprising one |
| 3 | Sheet-metal nesting | `manufacturing-nesting` | 12 | Rotate-to-save-a-sheet — a transformation with money attached |
| 4 | Pattern grading | `textiles-pattern` | 12 | Grading *is* non-uniform dilation; FreeSewing exposes the formulas |
| 5 | Survey monument dispute | `surveying-geodesy` | 11 | Parallel lines and transversals; NGS datasheets let students check their own trig |
| 6 | Image registration | `remote-sensing` | 8 | Translation + dilation on free Landsat/Sentinel scenes |
| 7 | Key-length decision | `cryptography-security` | 8 | The only domain that closes the entire Factoring group, 6/6 |

**Addendum, 2026-08-01 — Pre-Calc/Calculus/Discrete queue.** The table above targets the original
MS-domain gaps; B2 (same day) opened a second, separate queue for the three branches that had no
standards rows at all until today. Six ranked concepts brainstormed against `gap_queue.json`
(regenerated first — see DOCTRINE_LEDGER) in
`cases/_concepts/CONCEPTS_precalc-calculus-discrete_2026-08-01.md`: **Tide Window** (Pre-Calc
Trig Functions, score 9.8, recommended first), **The Optimal Can** (Calculus Applications of
Derivatives, 7.7), **Wind Triangle** (Pre-Calc Vectors, 7.4), **Total Flow** (Calculus Integrals,
7.4), **The Keyspace Decision** (Discrete Combinatorics, 5.8), **Six Degrees of Exposure**
(Discrete Graph Theory, partial, 3.4, carries a SPEC §6 sensitivity note).

**Update, same day — C1 written.** User chose to write Tide Window now, a deliberate, stated
exception to the depth-before-breadth rule (Cold Chain is still not `VERIFIED`). `cases/tide-window/`
now has `case.md`/`case.json`/`LEARNING_GOALS.md`/`FACILITATOR.md`; bidirectional LEARNING GOAL
CHECK passes (4 deliverables, 11 skills, 0 unmapped, 0 unreachable); Tier 1 structural gate finds
exactly the two blockers expected at this stage (11 open `{{NEEDS_SOURCE}}` placeholders,
`margin_pct` null) and nothing else — see DOCTRINE_LEDGER for the real authoring defects that run
caught and fixed along the way.

**Update, same day — `case-research` run.** 9 of 11 placeholders sourced live (4 straight from
NOAA's own API — real station, real datum, real M2 constituent, real predicted water levels for a
real date), 2 honest `NOT FOUND`s became stated Modeling Assumptions with real industry figures as
their basis. Research forced a real finding before it forced a fake one: working the case's own
clearance-vs-policy arithmetic with real numbers showed the drafted Twist couldn't flip the
verdict without stretching the storm into hurricane territory the case's own narrative rules out —
rather than pick an assumption value to force a reversal, set it to the middle of a real range,
computed the honest result (margin erodes ~42%, doesn't flip), and rewrote the Guide Notes to argue
from that. Tier 1 re-run: 1 blocker left (`margin_pct`, correctly deferred to `case-qa`), 0 open
placeholders. **Next: `case-qa` / `case-readiness` on `tide-window`, then a `sensitivity_model.py`
before Tier 2 can run.** The other four concept-sheet options (C2/C3/C4/C6/C9, plus the C11+C12
pair) remain unwritten.

**Transformations — the largest hole at 20/20 — is closed by concepts 1–3 and 6 together.**

### B5 · Domain-starved branches

`number-theory` is both domain- and case-starved (4 domains, 4 cases) — the thinnest branch in the file. `precalc` / `calculus` / `linear-algebra` are *case*-starved but not domain-starved: the mapping exists, the cases don't. `calculus` has only two HIGH domains (oceanography, spaceflight) — the weakest pipeline.

---

# TRACK C · Interface

### C1 · Ship what was just built ✅

Cases open from the dashboard (283 links, all resolving on disk), a graph router with Back, global `/` search, a Root Connections tab over 40 domains, a Rubric & Scoring tab, and a separate role-locked `student.html`.

### C2 · Deep links

`pushState` with a URL throws on `file://` (opaque origin), so Back works but you cannot link someone to a view. Fix needs either hash-routing or serving over `http://`. Decide which — it still gates the "real upload form" option that C3 didn't take.

### C3 · Submission intake ✅ *(designed 2026-08-01 — unproven live)*

A Hero downloads a packet and submits… somewhere. The tracker had the schema; there was no path in. Chose **a per-learner Drive folder** over a watched local folder or a real upload form — the latter needs a server (C2 still gates that option specifically, not this one). `roster.json` gained `drive_folder_id`/`drive_folder_url` per learner; `submissions.json` gained `source` (`facilitator-dictated` | `drive-intake`) and `drive_artifacts{}` on `submissions[]`; `skills/case-track/SKILL.md` gained a full "Drive intake" operation reusing `case-publish`'s already-connected Drive MCP server, on its read/download side this time — locate-or-create the learner's folder (asked, not assumed), diff new files against what's already recorded, confirm before writing, download a local copy to `student_work/<learner>/<case>/submitted/` before recording anything. See DOCTRINE_LEDGER MCS-40. **This blocks the entire scoring loop from ever running at scale, and still does** — the mechanism is fully specified but has never touched a real Drive account; the honest next step is one real learner, one real folder, one real file, before trusting the diff logic in a live cohort.

### C4 · Per-learner standards heatmap

Student mode shows badge progress but not *which skills this Hero has actually exercised*. Probably the most motivating view in the system, and the data already exists.

### C5 · Fix the orphan override record

`score_overrides.json` references a `score_id` present in no `scores[]` record. Currently surfaced in the UI rather than swallowed. Add referential integrity to the writer.

### C6 · Pipeline view — where every case actually is ✅ *(done 2026-08-01)*

There was no single place to see "concepting vs. drafting vs. stuck in readiness" across the whole
corpus — `cases_index.json` only gains an entry at *publish* time, so a mid-pipeline case (Tide
Window, sitting in `research`→`readiness`) was invisible to it entirely. Built `app/build_pipeline.py`
(derives `readmodel/pipeline_status.json` by scanning `cases/*/case.json` directly and
`cases/_concepts/*.md`, live-re-running Tier 1 per case rather than trusting `case.json.qa`) and a
new **Pipeline** tab in the dashboard — six stage columns (concepting → drafting → research →
readiness → promotion → verified), a stat-tile summary, per-case gate-status cards with a
computed next-action, legacy corpus cases shown as an explicit separate bucket rather than
force-fit into a stage. `build_dashboard.py --verify`: 145/145 (5 new checks). **Real side effect
this surfaced**: `case.json.qa` was not even a consistent shape across the two real cases —
fixed both to match. **Still open:** the stage list is accurate to today's pipeline; if a stage's
actual mechanics change (e.g. case-readiness splits further), `build_pipeline.py`'s
`stage_for_case()` needs a matching update — it is not self-deriving from doctrine text.

**Update, same day — the 55 legacy cases scored too, on their own honest terms.** User asked to
review the existing corpus against the readiness gate. `tier1_structural.py` can't run against
them directly (wrong file shape — `case.md`/`case.json` vs. raw `.docx`), and a deeper look showed
a verbatim-boilerplate or exact-anchor-heading diff would fail all 55 for predating the doctrine,
not for being bad. Built `app/build_legacy_readiness.py` instead: structural shape (Overview/
Background/binary Dilemma/Challenges/Appendices, loosely matched — fair to ask of a pre-doctrine
doc) checked separately from current-doctrine artifacts (cohort bands/interactive HTML/glossary —
reported as "0/55, absent by construction," not a per-case defect list). Real findings: 20.4%
(11 cases) have a genuine third dilemma option, spot-checked against source text and confirmed
real (Pets: dog/cat/bird), predating SPEC's strictly-binary rule; 61.5% of Guide Notes mention a
twist somewhere despite only 2.6% using the literal "Standards Touched On" heading. Caught and
fixed two real bugs in the checker itself along the way (a case-sensitivity regex bug, a title-
escaping mismatch undercounting standards-tagged cases by one). Surfaced as a scorecard panel in
the same Pipeline tab, not a stage column — showing them "in" the pipeline would misrepresent them
the same way a verbatim diff would. `build_dashboard.py --verify`: 148/148. **Also found, not
fixed:** one legacy case (`Investing - Stock Market - Options (Jia)`) has an `.xlsx` misfiled as
its `case_doc` asset in `corpus_index.json` — a small pre-existing data bug, tracked, not touched
in this pass. See D4 (legacy packet normalization).

**Second update, same day — collapsed into one pipeline, per explicit user objection.** User: "i
reallly don't want two pipelines... let's put them in the right place." The scorecard-panel design
above was a genuine attempt to avoid misrepresenting pre-doctrine cases, but it built a second view
instead of placing them — not what was asked. Rewrote `build_pipeline.py` to triage all 55 using
`legacy_readiness.json`'s already-computed signal and fold each into the *same* six-column board:
not-strictly-binary lands in Concepting (23 cases — the same design decision a new concept needs);
structurally-sound-plus-Guide-Notes-plus-tagged lands in Drafting as `NEAR READY` (18); partial
signal lands `MODERATE WORK`/`MORE WORK` (7 + 5). 53 of 55 folded cleanly; the 2 that couldn't
(one misfiled `.xlsx`, one missing core sections) are named `legacy_exceptions[]`, not guessed at —
minimizing exceptions was the explicit ask. Dashboard's old scorecard panel replaced with legacy-
origin cards inside the real columns (effort-tier badge instead of a Tier-1 verdict) plus a small
callout naming just the 2 exceptions. `--verify`: 150/150 (was 148). Visually confirmed in-browser.
**Not done:** no legacy case has actually been converted yet — spot-checking Payroll (a "NEAR
READY" candidate) found 34 legacy-tagged standards skills, well past the ~8-15 healthy range
`case-brainstorm` itself guards against, meaning real curation is still required, not mechanical
transcription. Board structure now matches the instruction; sequencing the actual conversion of
the 18 NEAR READY cases toward `case-publish` is the next open decision.

---

# TRACK D · Download & delivery

### D1 · Drive publishing — one real run

`case-publish` has the step and has never executed against the connected account. Until it does, "publish" means "wrote a file locally."

### D2 · Packet standardization

Cold Chain's filenames don't follow the convention `case-publish` specifies. Every case should emit an identical bundle: case `.docx`, Guide Notes `.docx`, workbook `.xlsx`, RUN_REPORT, `MANIFEST.json`. HIGH GRADE's assembly-and-print checklist is the model — *print this / handwrite that / assemble in this order*.

### D3 · Print discipline

These get printed and handed out. **Nobody has printed one.** Check page breaks, whether appendix tables split across pages, whether the workbook fits one sheet, and whether a guide can hold the Socratic plan in one hand.

### D4 · Legacy packet normalization

55 legacy cases are loose `.docx` in session folders with inconsistent naming (`Guides Notes.docx`, `Castle Securtiy`). Normalize into the standard bundle so the tracker treats all 56 identically. Add to this backlog: `Investing - Stock Market - Options (Jia)`'s `corpus_index.json` entry lists an `.xlsx` as its `case_doc` asset (found running `app/build_legacy_readiness.py`, 2026-08-01) — `readmodel/corpus_index.json` needs the real case `.docx` identified and the asset entry corrected.

---

# TRACK E · Evaluation

### E1 · Calibrate the rubric ✅ shipped · ⚠ uncalibrated

`RUBRIC.md` v1.0 is **PROPOSED, not locked.** The weights assert that argument and correctness matter 4× the research link. Defensible, untested. One real cohort confirms or moves them.

### E2 · C7 needs a reality check

"Framing the question" has no legacy precedent — none of the 40 Guide Notes score it. It may be too hard at T1–T2. **If nearly everyone lands Not Yet, the criterion is wrong, not the Heroes.**

### E3 · Record discussion participation

C6 needs per-Hero contribution counts. The schema exists; the habit does not. Without it, one of seven criteria is unscoreable — and it is the one measuring the thing the whole format exists for.

### E4 · Inter-rater check

Two guides, one submission, compare. Until that has happened once, every Exemplary is one guide's opinion rather than a system verdict.

### E5 · Watch the override log

The machine's C1/C2/C7 detection is cue-phrase based and will miss unusual phrasing. Every override is a training signal. The 30% demotion rule needs enforcement (A4) and a real n before it means anything.

---

# TRACK F · Engagement

The brief asked for cases that *teach math and show applications* — engaging problems with real data. Tracks B and E make cases correct and gradeable. This track makes them worth doing.

### F1 · Engineer the herring

HIGH GRADE builds the *seductive wrong answer* first, with real supporting evidence, and constructs the truth around it. Cold Chain's trap was noticed during authoring, not designed. Invert it: `case-brainstorm` should ask "what is the plausible wrong path?" **before** "what is the answer?"

### F2 · The jigsaw variant *(the most interesting unexplored idea here)*

HIGH GRADE gives each character **information rights** — what they know, may reveal, must conceal. The analogue: different Heroes receive different appendices and must combine them to see the whole picture. Turns a solo case into a genuinely collaborative one and makes the discussion structurally necessary rather than merely scheduled.

### F3 · Career surfacing

`domains.json` carries 120 careers with the *specific computation* each uses — "fits dose-response curves and computes number-needed-to-treat," not "uses statistics." Surface it at the point of work: *the math you just did is what an epidemiologist does on a Tuesday.* Today it lives only in Root Connections; it belongs in the case packet.

### F4 · Live data

Several domains expose live feeds (GTFS transit, NOAA, USGS, FRED). A case whose appendix regenerates against this week's data is a different kind of artifact — and a maintenance burden, and a reproducibility problem for grading. Decide deliberately; don't drift into it.

### F5 · The surprising ones

Deliberately author the domains a teenager would not expect to be mathematical: marching-band drill, textile pattern grading, tiling, music acoustics, archaeology. `drill-choreography` sits at #2 on the authoring queue for exactly this reason.

---

## Sequencing

### As of v2.10 · 2026-08-18

**Now, in order:**
1. **A3 — first `VERIFIED` case.** Still the single blocking fact — no case in this system has run
   with real learners. The pool of genuinely `TIER2_PASS`/`published` candidates just grew from 5 to
   **15** (the original five plus this pass's ten), so the choice of which case runs first is wider,
   not the blocker itself. This is calendar work, not engineering work, and remains the one thing
   nothing in this pipeline can do for itself.
2. **Fix `case-publish`'s promotion snippet for the "already in `cases[]`, still need to flip
   `status`" case** (new — see this version's header). The documented script's idempotent-stop path
   correctly does nothing when a title is already in `standards_spine.json.cases[]`, but a case in
   that exact shape (a legacy conversion, already spine-tagged, freshly reaching `TIER2_PASS`) still
   legitimately needs its `status` flipped to `published` — the gap between those two facts is
   exactly what produced this pass's 62/77-skill data-loss regression when an agent wrote ad hoc
   logic to bridge it. Write the explicit path into `SKILL.md`'s own script rather than leaving the
   next promoting agent to reinvent it.
3. **Write C5 (The Reserve Asymptote) next**, per the Track B update above — highest-value concept
   in the current queue, closes two full zero-coverage groups (11 skills) in one case, HIGH
   feasibility, untapped career (actuarial analyst). Re-scope C7/C8 first (see Track B) before
   anyone writes those two specifically — C9 is moot, drop it.
4. **Regenerate `readmodel/domain_coverage.json`.** Flagged stale in this pass (`199` uncovered
   there vs. the spine's real `73`) but not fixed — out of scope for what this pass was asked to do.
   Whoever picks up B4/the concept queue next should regenerate it first rather than read stale
   `uncovered_skills_still_orphaned` numbers.
5. **A regression net over the admin core.** Unchanged from v2.9 — `admin_core.py`,
   `store_postgres.py` and `admin_web/app.py` still have zero automated tests.
6. **Real auth (MCS-44).** Unchanged from v2.9 — one shared passcode still guards write access to
   real learner data with no per-user identity.

**Done since v2.9 (2026-08-12 → 2026-08-18):** the ten `readiness`-stage cases re-verified against
live gate scripts rather than trusted at self-report — 5 were already clean, 5 needed real fixes
(2 stale-published-artifact rebuilds, a full 5-probe Tier 2 run for `family-trip`, a real
propagation bug and two real P6 citation defects found and fixed, one case's packet built from
scratch including its first-ever case-#2 proof of the A7 interactive-HTML shell) — all ten now
genuinely `TIER2_PASS`/`published`; a real `standards_spine.json` data-loss regression found (via
the promotion script's own snapshot safety net) and fixed; `uncovered` 81 → 73.

**Ongoing:** E5 override watch · E3 discussion participation (still the least-instrumented of the
seven rubric criteria, and the one measuring the thing the format exists for).

**One line:** the ten-case backlog this pipeline itself created by outrunning its gate is now
actually closed, not just relabeled — every claim in the table above was checked against a live
script run, not a JSON field — and the project is back to the same one blocker it's had since
Cold Chain: no case has run with real learners yet.

### As of v2.9 · 2026-08-12

**Now, in order:**
1. **A3 — first `VERIFIED` case.** A real guide, a real room, a filled `RUN_REPORT`. The live app
   removed every technical excuse; this is calendar work now. Run it on one of the five
   `TIER2_PASS` cases (`plaza-pavers`, `company-front`, `vent-cap`, `apron-order`, `survey-corner`),
   not on Cold Chain — those clear a higher bar.
2. **A8 — backfill the ten demoted cases** (new; see the v2.9 header). Sensitivity model + Tier 2
   run + QA report each, then re-promote via `case-publish`. Until then they are correctly
   unassignable.
3. **Close MCS-41 at the gate.** `scripts/apply_publish_gate.py` sweeps after the fact;
   `case-publish` should refuse to stamp `published` below `TIER2_PASS` in the first place.
4. **A regression net over the admin core.** `admin_core.py`, `store_postgres.py` and
   `admin_web/app.py` have zero automated tests. Every production bug so far was caught by a human
   using the app (D-017, D-019, both MCS-45 failures). That has worked and does not scale.
5. **Real auth (MCS-44).** One shared passcode currently guards write access to real learner data,
   with no per-user identity — the audit trail records a typed name, not an authenticated actor.

**Done since v2.8 (2026-08-01 → 2026-08-12):** the local admin server (D-015) · the hosted
Vercel + Neon variant with a shared core across both transports (D-016) · the override-id collision
fix (D-017) · the public student case page (D-018) · the Assign-a-Case redesign (D-019) · the
publish gate written down and swept (D-020, MCS-41) · roughly fifteen more authored cases, the last
five at `TIER2_PASS` with full packets · A7's shell proven across every case · five doctrine rows
for the architecture that had none (MCS-41→45).

**Ongoing:** E5 override watch · E3 discussion participation (still the least-instrumented of the
seven rubric criteria, and the one measuring the thing the format exists for).

**One line:** the pipeline got good enough to outrun its own gate, the gate is now written down and
enforced, and the only thing left between this system and Phase 3 is putting one case in front of
real students.

### As of v2.8 · 2026-08-01 (historical)

**Now:** A3 (first VERIFIED case — needs a real guide and room, the one thing this pipeline cannot do for itself)
**Done since v2.7:** A1 · A2 · A7 (interactive-HTML scaffold) · B1 · B2 (spine extended) · C3 (Drive intake designed)
**Next:** prove A7's shell and C3's Drive intake against something real — either counts as case #2/first-real-submission groundwork — · E3 · D1
**Ongoing:** E5 override watch · A4 wiring

**One line:** fix the case the gate caught (done), tag the untagged cases (done), extend the spine and scaffold the tooling case #2 will need (done) — run one case with real learners is still the one blocker nothing in this session could close, and everything else now genuinely waits on it.

---

<details>
<summary><strong>v1.0 — shipped 2026-07-31 (historical record)</strong></summary>

| Deliverable | Notes |
|---|---|
| `SPEC.md` v1.0 | Case anatomy, balance test, 4 tiers, facilitator artifacts §7, Definition of Done |
| `standards_spine.json` | 322 atomic skills, 8 domains |
| `curriculum_tree.json` | 4 phases, 10 branches, prereq graph |
| `corpus_index.json` | 56 cases with asset manifests |
| Six pipeline skills | brainstorm → write → research → qa → publish → track |
| `dashboard.html` | 5 views, 46 self-checks |
| **Cold Chain** | First pipeline case. T3. Closed 3 zero-coverage skills |
| Doctrine | DOCTRINE_LEDGER (20 rules), DECISIONS, README |

Added later the same day: `domains.json` (40 domains, 121 live-verified sources) · `RUBRIC.md` · `case-readiness` (3-tier gate) · `submission-score` · `PROCESS_TRANSFER.md` · dashboard v2 (140 checks, 7 tabs, `student.html`) · DOCTRINE_LEDGER to 35 rules.

</details>
