# Roadmap — Math Builder

**Last refreshed: 2026-09-01 (v2.16), against live scripts, not carried-forward numbers.**
For the full reasoning behind any line below — why a number moved, what broke, what was fixed —
see **[ROADMAP_HISTORY.md](ROADMAP_HISTORY.md)**, the complete narrative log. This file is just
the status page: what's done, what's not, what's next.

---

## Right now — the 5 things that matter most

| # | What | Why it's first |
|---|---|---|
| 1 | **Run the first real case with a real learner** (Track A3) | The single blocking fact — 0 cases have ever been run with a real learner, out of 111 now cleanly published (`python3 app/build_pipeline.py`, stage=promotion, TIER1_PASS). Everything else is still a machine claim until this happens |
| 2 | **Push `app/student-moksh-atit.html` to the live site** | Currently local-only; his first assigned month can't actually be used until this ships |
| 3 | **Get `a-coachs-dilemma` a real Tier 2 re-run** | Its own `QA_REPORT.md` (2026-08-21) says `qa.state` should not sit at `TIER2_PASS`/`published` until a full Tier 1 + Tier 2 re-run happens against its current NBA/Priya Shah content — that re-run has never happened; the recorded Tier 2 result is against retired NCAA content. `tier1_structural.py --case a-coachs-dilemma` now correctly flags this as the corpus's only live BLOCKER (T1-16, stale QA hash) after this session's packet rebuild fixed the other 3 (T1-15 staleness) |
| 4 | **Push a `case-publish` to Google Drive for the first time** | Every case published across recent sessions built its packet and promoted the read-model, but Drive upload has been held back pending separate approval every time — still an open step for all of them |

---

## What's actually ready to use right now

**Moksh Atit is set up and has his first month assigned** — 5 cases toward Badge 1, all genuinely
quality-checked: Phone Plans → Family Trip → Key Length → Field Watch → Apron Order. His page:
`app/student-moksh-atit.html`. Not yet pushed to the live site — still local only.

**111 cases** are genuinely ready to hand to any learner (passed every quality check this project
requires, live re-scan via `app/build_pipeline.py`, stage=promotion + TIER1_PASS + 0 blockers).
1 more sits at stage=promotion but is genuinely `BLOCKED` — `a-coachs-dilemma`, see item 3 above,
not force-passed. The previously-flagged batch of 10 mis-published cases (`archery-camp`,
`baseball-lineup`, `cardiology`, `catering`, `house-plans`, `lebron-vs-michael`, `nuclear-waste`,
`phone-plan`, `rent-vs-own`, `robotics-engineer`) remains remediated — each still carries a
recorded `TIER2_PASS` with all six Tier 2 probes passing; see their individual `QA_REPORT.md`
files for the per-case fix log.

**19 new cases published across two batches since 2026-08-30** (see the 2026-09-01 note below for
the full list and the MCS-46/redesign detail). **6 cases remain in flight** — 5 at readiness (`the-cheap-approximation`, `the-dosing-curve`,
`the-irregular-boundary`, `the-search-box`, `the-stake-out` — the last of these is TIER1_PASS/0
blockers and TIER2_PASS-recorded (2026-09-01) but not yet promoted: it is in `cases_index.json`
but not yet credited in `standards_spine.json`'s `covered_by[]`, a pending human-confirm step per
MCS-12, not a defect) and 1 at research (`the-locks-window`, kept as a documented historical record
of a structurally one-sided dilemma, not revived) — live re-scan via `app/build_pipeline.py`.

**0 concepts remain unwritten** (was 9 as of 2026-08-30). This is a corrected number, not just a
lower one: the pipeline-native concept board (`app/build_pipeline.py`'s `parse_concept_sheets()`)
was undercounting by 1 due to a genuine title-drift bug — concept C9 "Redrawing the Lines" had
already been written and published as `cases/redrawing-lines/` (case.json title "Redrawing Lines",
an internal "the" dropped) but the matcher only strips a *leading* "The ", so it never recognized
the match and kept showing the case as an unwritten concept. Fixed with a `CONCEPT_TITLE_ALIASES`
entry in `app/build_pipeline.py`, mirroring the existing `LEGACY_TITLE_ALIASES` pattern — this also
resolves the Housekeeping-table item "confusing near-duplicate case name needs a human check
(`redrawing-lines`)" below. All 9 previously-listed concepts from `CONCEPTS_pim-sector-gaps_2026-08-24.md`
and the rest of this session's batches are now written and published. Both remaining Pre-Calculus
gaps (Polar/Parametric, Trig Identities) stay closed.

---

## Status by area

Legend: ✅ done · 🔄 in progress · 🔜 next up · ⏳ open, not started · ⛔ blocked / needs a decision

### Quality — is any case actually good enough?

| Item | Status | What's left |
|---|---|---|
| Fix the flagship case (Cold Chain) | ✅ Done | — |
| Require a "stress test" before any case ships | ✅ Enforced by a script | 10 cases slipped through once; all 10 since remediated to TIER2_PASS |
| **Run the first case with real students** | ⛔ **Not started — the #1 blocker** | Pick any of the 80 clean cases, run it, fill in the results |
| Reusable case-page template | ✅ Done | Proven across many cases already |
| Facilitator "cohort size" guidance | 🔄 Only 1 case has it | Every case with facilitator notes needs its own |
| Fix the 10 mis-published cases | ✅ Done | All 10 now carry a recorded `TIER2_PASS` |

### Coverage — does the case library actually teach the whole curriculum?

| Item | Status | What's left |
|---|---|---|
| Tag old cases against the skill map | ✅ Done | Worked to its honest limit |
| Add Pre-Calculus / Calculus / Discrete Math to the skill map | ✅ Done | — |
| Give every case facilitator discussion notes | 🔄 In progress | 16 of 56 older cases still missing them |
| **Write/finish cases for Geometry & Pre-Calculus gaps** | 🔄 In progress | Pre-Calculus is fully closed; Geometry's Quadrilaterals & Polygons and Visual Perceptibility are now also fully closed — only Surface Area & Volume (1 skill: sphere volume) remains, plus the pre-existing Calculus/Derivatives (quotient rule) and Calculus/Series (Taylor series, 2 skills) clusters — see table below |
| Some subject areas have almost no cases at all | ⏳ Not started | Number Theory is the thinnest |

**Geometry & Pre-Calculus gap tracker** (reprioritized ahead of other subjects per direct request):

| Subject | Topic | Gap | Status |
|---|---|---|---|
| Pre-Calc | Matrices | 7 skills | ✅ Published (`the-multiplier-recruit`) |
| Pre-Calc | Intro to Limits | 5 skills | ✅ Published (`the-reserve-asymptote`) |
| Pre-Calc | Polar & Parametric | 6 skills | ✅ Published (`feedback`) |
| Pre-Calc | Trig Identities | 5 skills | ✅ Published (`deluge-gun`) |
| Geometry | Fundamentals | 7 skills | ✅ Published (`roofline-call`) |
| Geometry | Quadrilaterals & Polygons | 0 of 22 uncovered | ✅ Closed |
| Geometry | Visual Perceptibility | 0 of 11 uncovered | ✅ Closed |
| Geometry | Surface Area & Volume | 1 of 10 uncovered | 🔄 9/10 covered — "How to find the volume of a sphere" remains |

### Interface — the dashboards and student-facing app

| Item | Status | What's left |
|---|---|---|
| Main dashboard (case library, coverage map, pipeline view) | ✅ Done | — |
| Shareable links to a specific view | ⏳ Open | Needs a technical decision about how the app is hosted |
| Students submit their work into the system | 🔄 Designed | Never actually tested with a real submission |
| "Which skills has this student actually practiced" view | ⏳ Open | Data already exists, just needs a screen |
| Broken data link (an old bug) | ✅ Fixed, verified 2026-08-19 | — |
| Pipeline status view (what's in progress, what's stuck) | ✅ Done | — |

### Delivery — getting a finished case into someone's hands

| Item | Status |
|---|---|
| Publish a case for real (not just locally) | ⏳ Open |
| Every case ships the same standard file bundle | ⏳ Open |
| Someone has actually printed a packet and checked it reads well on paper | ⏳ Open — nobody has yet |
| Clean up old cases' inconsistent file naming | ⏳ Open |

### Evaluation — grading and feedback quality

| Item | Status |
|---|---|
| Scoring rubric | ✅ Shipped, ⚠️ never calibrated against real student work |
| One scoring criterion ("framing the question") may be too hard | ⏳ Open |
| Track who's actually talking in discussions | ⏳ Open |
| Two facilitators independently score the same work, compare | ⏳ Open |
| Watch for the grading machine getting overridden a lot | 🔄 Ongoing |

### Engagement — making cases genuinely fun/compelling, not just correct

| Item | Status |
|---|---|
| Build in a deliberately tempting *wrong* answer | ⏳ Open |
| Give each "character" secret info that forces real collaboration | ⏳ Open, most interesting unexplored idea |
| Connect the math explicitly to the career that uses it | ⏳ Open |
| Use live/real-time data sources | ⏳ Open — needs a deliberate decision first |
| Cases about surprising subjects (drill team math, textile grading, etc.) | ⏳ Open |

### Housekeeping

| Item | Status |
|---|---|
| Automated tests for the admin app | ⏳ Open — currently zero |
| Real per-user login (currently one shared password for everyone) | ⏳ Open |
| ~~A confusing near-duplicate case name needs a human check (`redrawing-lines`)~~ | ✅ Fixed 2026-09-01 | It was not a duplicate — concept sheet C9 "Redrawing the Lines" and the published `cases/redrawing-lines/` ("Redrawing Lines") are the same case; `app/build_pipeline.py`'s title-matcher only stripped a leading "The ", not an internal "the", so it never recognized the match. Added a `CONCEPT_TITLE_ALIASES` entry (mirrors `LEGACY_TITLE_ALIASES`) |
| **`app/dashboard.html` is a static build artifact — goes stale after every `case-publish` unless someone manually reruns `python3 app/build_dashboard.py`** | ⚠️ **Process gap, not automated** | Rebuilt 2026-08-24 (had been stale since before Grant Reach/Perimeter Protocol published, meaning the live dashboard was missing 4 published cases for several sessions with nobody noticing). The page's own masthead shows `built <date>` once logged in — check that date against today before trusting what's on screen. No CI/git-hook enforces the rebuild yet; it's still a manual step someone has to remember after every publish |
| `build_dashboard.py --verify`'s 2 remaining failing self-checks | ⏳ Open, not investigated | (1) one zero-coverage cluster (Calculus/Derivatives) with no closing domain recorded, (2) tracker live exception queue not empty (`phone-plans`/Moksh Atit). Neither blocks a valid `dashboard.html` build; neither investigated further yet |
| ~~`legacy_readiness` case count vs. `corpus_index` legacy count mismatch~~ | ✅ Fixed 2026-08-30 | Root cause was two compounding bugs: (1) `app/build_pipeline.py`'s `LEGACY_TITLE_ALIASES` didn't cover 4 legacy→published title renames (Movie Producer→Movie Executive, College Football Playoff Committee→Playoff Committee, Medical Statician→Medical Statistician, AirBnb→AirBnb Or Landlord), so those 4 published cases still showed as `legacy-untouched` "NEEDS A REAL DESIGN DECISION" cards on the pipeline board; (2) `corpus_index.json` never clears a row's `status: "legacy"` flag once that case is converted and published — true for all 43 already-converted legacy cases, not just the 4 with the title-alias bug (e.g. Payroll and Gerrymandering were also mislabeled, which is what caused the separate "legacy cases carrying `margin: 0` instead of `null`" self-check to fail too). Fixed both: added the 4 missing aliases, and flipped `status` to `"published"` on the 43 corpus_index.json rows for titles `build_pipeline.py` already recognizes as converted. `legacy_readiness.json`'s `n_legacy_cases` dropped from 45 to 2 (the two genuine remaining exceptions: `Castle Securtiy` — typo'd source folder name, and `Investing - Stock Market - Options (Jia)` — case doc is an .xlsx, not a .docx). Both self-checks now pass |

---

## The numbers, for reference

| | |
|---|---|
| Cases that are genuinely ready to assign (published, live re-scan, `python3 app/build_pipeline.py`) | **111** |
| Cases at stage=promotion but genuinely `BLOCKED` (not force-passed) | **1** — `a-coachs-dilemma`, see item 3 above |
| Total case directories under `cases/` (pipeline-authored corpus) | **119** (`ls -d cases/*/ \| wc -l`) |
| Cases in drafting / research / readiness | **6** — 0 drafting, 1 research, 5 readiness (see note above; the pipeline is not empty this refresh) |
| Concepts scoped but not yet written into a case | **0** (was 9 — see the 2026-09-01 note; includes a genuine title-matcher bug fix, not just new writing) |
| Cases ever run with a real student | **0** |
| Skills in the curriculum map | 437 (`readmodel/standards_spine.json.totals.skills`) |
| Skills with zero coverage (n=0) | **6** — Number Sense (2: Depth, Digit), Geometry/Surface Area & Volume (1: sphere volume), Calculus/Derivatives (1: quotient rule), Calculus/Series (2: Taylor series) |
| Skills "thin" (1 ≤ n ≤ 2, the project's tracked thin-coverage threshold, `standards_spine.json.totals.thin_1_2`) | 211 |
| Distinct case titles credited in the spine (`standards_spine.json.totals.cases`) | 123 |
| Legacy source-corpus cases still un-triaged/exception (`readmodel/pipeline_status.json.legacy_exceptions`) | 2 (`Castle Securtiy`, `Investing - Stock Market - Options (Jia)`) |
| Concept-sheet backlog files (`cases/_concepts/CONCEPTS_*.md`) | 14 sheets, 0 unwritten C-numbered concepts remaining across all of them |
| `app/dashboard.html` last rebuilt | **2026-09-01** — must be rerun (`python3 app/build_dashboard.py`) after every future `case-publish`, or the live site keeps serving stale data even though the underlying case files are correct. `--verify` clean at 206 checks, 2 pre-existing documented failures (Calculus/Derivatives zero-coverage cluster; `phone-plans`/Moksh Atit tracker exception), 1080/1080 asset links resolved |
| `readmodel/domains.json` / `domain_coverage.json` | 40 domains, 12 clusters, `app/validate_domains.py` 28/28 checks passing |

**2026-08-30 note:** `bioreactor-bid`, `enclosure-call`, `fret-board`, `alert-curve`,
`compute-lease`, `cooling-curve`, `downbeat-split`, and `placement-test` — all 8 cases that were
in flight — reached `TIER2_PASS` and published this session (packet + interactive HTML +
read-model promotion). Google Drive upload was not pushed for any of them, held for separate
approval. `fret-board`, `alert-curve`, `compute-lease`, `cooling-curve`, `downbeat-split`, and
`placement-test` all required a genuine retune first (see the note above for what changed in
each).

**2026-09-01 note — staleness sweep + a 19-case batch's worth of pipeline/dashboard rebuild.**
Two things happened between the 2026-08-30 refresh and this one, across several concurrent
sessions working this repo: (1) 19 new cases were published in two batches — `prove-it-scales`,
`the-attribution-sample`, `the-bot-farm`, `the-bracket-cliff`, `the-cold-start`,
`the-contrapositive-claim`, `the-course-correction`, `the-dosing-curve`, `the-fee-ladder`,
`the-irregular-boundary`, `the-mainline-margin`, `the-peg-line`, `the-plaza-bid`,
`the-qubit-budget`, `the-repeat-match`, `the-rig-budget`, `the-rig-split`, `the-stake-out`,
`the-trial-size`; and (2) a 6-case Precal depth/redundancy batch (`the-tilt-decision`,
`the-crosswind-cut`, `the-skin-pack-atlas`, `the-search-box`, `the-clampband-margin`,
`the-late-run`) reached `TIER2_PASS`, alongside **two dilemma redesigns**: `the-locks-window`
(structurally one-sided, superseded by `the-late-run`, left in place as a documented historical
record rather than deleted) and `the-transfer-window` (chemical-vs-electric propulsion found to be
a structurally unfixable ~800x transit-time gap, superseded by `the-phasing-call`, a same-technology
direct-vs-phasing rendezvous rebuild). **MCS-46** (a narrow, project-owner-approved per-case waiver
of MCS-02's ~20% balance cap, for real dilemmas with a landslide margin driven by real
physics/economics where the *problem-solving process* is still genuinely hard) was added and used
to publish `the-phasing-call` (~1991% real margin, waived) and `the-transfer-window` (kept as
historical record, not revived under the waiver).

This session's own work, on top of that: found the corpus's live `--verify` state did **not**
match the task brief's premise — `the-stake-out` was not `BLOCKED`; it was already `TIER1_PASS`
(0 blockers) at stage=readiness (published packet built, `cases_index.json` entry present, not yet
promoted into `standards_spine.json.covered_by[]` — a pending human-confirm step, not a defect).
The real staleness sweep instead found **5 genuine `stage=promotion` `BLOCKED` cases**, all fixed
by rebuilding the actual broken artifact (never by weakening a check or fabricating a pass):
`deluge-gun`, `gerrymandering`, `redrawing-lines`, `speed-climbing`, and `the-keyspace-decision`
each had a Working Notebook `<input placeholder>` in its published Interactive HTML containing the
exact numeric answer the Check button grades against (MCS-37/T1-18) — every digit was replaced
with a format-only hint (e.g. `placeholder="e.g. 569068"` → `placeholder="whole number"`), and all
5 now re-verify `TIER1_PASS`/0 blockers. `a-coachs-dilemma` had a real, pre-existing, already
partly-diagnosed issue (its own `QA_REPORT.md`, dated 2026-08-21): case.md was edited to remove a
worked-answer leak, but `published/*.docx`/`*.xlsx`/`MANIFEST.json` were never regenerated and
`case.json.qa`'s hash/Tier-2 result still describe a *retired* NCAA-content version of the case.
The packet was mechanically rebuilt from the current case.md (clearing 3 of 4 blockers); the 4th
(`T1-16`, stale QA hash) was deliberately **left BLOCKED and reported, not forced green** — a real
Tier 1 + Tier 2 re-run against the current NBA/Priya Shah content is still owed and is now item 3
in "Right now" above. Also found and fixed a genuine title-drift bug in `app/build_pipeline.py`'s
concept-matcher (see the Housekeeping table) that was inflating the unwritten-concepts count by 1.
Full pipeline/dashboard/domains rebuild run clean afterward (`build_pipeline.py`,
`build_dashboard.py` + `--verify`, `build_legacy_readiness.py`, `build_domains.py` +
`validate_domains.py`) — see the numbers table above for every resulting figure and its source
command.

Full derivations, per-script commands, and the reasoning trail for every one of these numbers are
in [ROADMAP_HISTORY.md](ROADMAP_HISTORY.md).
