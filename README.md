# Math Builder — Learn Math by Case Study

> **What this is:** A production system for Acton-style quantitative case studies for middle and high school. It ingests three years of existing curriculum, maps it against an atomic standards spine and a MS→university curriculum tree, finds the holes, and runs new cases through a seven-stage pipeline from concept to published packet to student tracking.

**State:** ACTIVE · **Phase:** 2 (Build) · **Independent project as of 2026-08-01** — see
`00_SESSION.md` for the full per-project instructions block. Spine locked, pipeline built, one
case shipped end-to-end, both QA modules tested end to end (2026-08-01).

---

## Start here

0. **`00_SESSION.md`** — the paste-ready per-project instructions block (what to read, in what order, the hard lines). Read this first if you're starting a session cold in this folder.
1. **`SPEC.md`** — the contract. What a case study *is*, its seven required sections, the balance test, the difficulty tiers, and the facilitator artifacts. Everything else enforces this.
2. **`app/dashboard.html`** — open it. Eight views over the whole corpus: curriculum tree, coverage heatmap, case library, **root connections**, **rubric & scoring**, **pipeline**, gap queue, tracker. One pipeline, not two: the pipeline view is a live map of every concept, native case, *and* legacy case against the real six pipeline stages (concepting → drafting → research → readiness → promotion → verified). Native cases carry a Tier 1 status re-run live at build time (`app/build_pipeline.py`), not read from a cached field. The 55 pre-pipeline corpus cases are triaged into the same six columns by real signal read from their source `.docx` (`app/build_legacy_readiness.py`) — a locked binary dilemma with Guide Notes and standards tagging lands in Drafting as `NEAR READY`; a dilemma that isn't strictly binary yet lands in Concepting, the same design decision a brand-new concept needs — because the current locked `CHALLENGE_BOILERPLATE.md` wording and the 11-anchor Guide Notes ladder both postdate this corpus, so a case is placed by what it actually has, not failed for predating doctrine it couldn't have followed. A small number of cases whose `.docx` can't be triaged at all (misfiled asset, missing core section) are named as exceptions rather than guessed at. Every case asset is a working link that opens the real `.docx`/`.xlsx`/`.pdf` from `file://`; every view cross-navigates to every other; `/` searches everything; the Back button and the browser's own back both work. A guide/student role switch lives in the top bar — see *Two builds* below.
3. **`skills/PIPELINE.md`** — how the six authoring skills chain together and what gates sit between them.
4. **`cases/cold-chain/`** — the worked reference case. Read `case.md`, then `FACILITATOR.md`, then `case.json`.
5. **`TECH_STACK.md`** — this project's own complete stack record: Python + python-docx/openpyxl, a flat-JSON read-model, a single-file HTML/vanilla-JS dashboard, no server.

---

## What the corpus actually contains

| | Count |
|---|---|
| Case studies in the source corpus (Y1–Y3 + Best of Studio) | **55** |
| Cases authored by this pipeline | 1 (Cold Chain) |
| Cases tracked in the legacy standards matrix | 27 |
| Cases with **no standards row at all** | **31** |
| Matrix columns with no source folder | 5 (+3 fuzzy filename joins) |
| Atomic skills in the standards spine | **437** across 11 domains (322 across the original 8 MS domains + 115 across Pre-Calculus/Calculus/Discrete Mathematics, added 2026-08-01 — see ROADMAP.md B2) |
| Skills with zero coverage | **97** (was 100 before Cold Chain) |
| Unique skill **ids** (2 labels appear in two groups each) | 320 — see DOCTRINE_LEDGER G1 |
| Cases with facilitator Guide Notes | 39 / 55 |
| Cases with a timed 45-minute Socratic plan | **1** / 55 legacy (Cold Chain makes 2 of 56) |

**The headline finding: the standards matrix is roughly three years stale.** More than half the corpus has never been tagged. That means the "97 uncovered skills" number is an *upper bound* — some of those skills are probably already exercised by untagged cases. **Tag before you author.** The dashboard separates this reconciliation backlog from the genuine authoring backlog for exactly this reason.

---

## The two spines

**`readmodel/standards_spine.json`** — 437 atomic skills (vocabulary terms and "how to…" procedures) across 11 domains: the original 8 MS domains inherited from the school's own matrix (Number Sense, Basic Operations, Fractions, Advanced Numbers, Geometry, Measurement, Advanced Operations, Statistics & Probability — 322 skills) plus 3 HS/Advanced domains authored 2026-08-01 to give Pre-Calculus, Calculus, and Discrete Mathematics real rows for the first time (115 skills — see ROADMAP.md B2). Each skill carries `covered_by[]` and `n`; the new rows all start at `n:0`, honestly, since no case has been authored against them yet. This is the join key for everything.

**`readmodel/curriculum_tree.json`** — the four-phase Tree of Thought from Pre-Algebra to Linear Algebra, with prerequisites, core topics, and critical dependencies. Branches link to the legacy domains through `acton_domains[]`.

Per-branch coverage is rendered live in the dashboard and deliberately **not** duplicated here — a hand-maintained copy drifts, and the first one did. Open the Curriculum Tree tab.

As of 2026-08-01 every branch has real standards rows — Pre-Calculus, Calculus, and Discrete Mathematics were the last three with **no rows at all** (rendered distinctly from 0% coverage everywhere in the system, per MCS-07), and now genuinely sit at 0% (real rows, none covered yet, honestly disclosed rather than hidden). Geometry (52%) and Linear Algebra (44%) are the weakest branches with pre-existing case coverage; the three new domains are weaker still (0%) because no case has been authored against HS-stretch content yet — that's the next authoring frontier, not a data gap.

**Biggest authoring holes:** Geometry → Transformations (20/20 uncovered), Quadrilaterals & Polygons (19/22), Fundamentals of Geometry (19/24), Surface Area & Volume, and Statistics → Algebra (9/9).

### The third spine — `readmodel/domains.json`

Where the first two spines say *what* to teach and *in what order*, this one says **where the numbers come from**. 40 application domains in 12 clusters, each carrying validated spine skill ids, the curriculum branches it genuinely consumes, 2–5 named free data sources whose URLs were all fetched before being written down, 2–4 binary decision archetypes, a career layer that names the actual computation, and an authoring priority. `readmodel/domain_coverage.json` is the derived join: which domains feed each branch, how many existing cases sit there, and which uncovered skills are reachable from a compelling domain.

This replaces the three-line `intersections[]` that used to be Phase 4 of the tree. All 95 uncovered spine skills — including every one of the 20 Transformations skills — are now reachable from at least one domain with named data behind it. Rebuild with `python3 app/build_domains.py`; check with `python3 app/validate_domains.py`.

---

## The pipeline

```
gap_queue ─▶ case-brainstorm ─▶ [human picks] ─▶ case-write ─▶ case-research
                                                     │              │
                                              learning-goal      cited numbers
                                                 check          or NOT FOUND
                                                     ▼              ▼
                                                  case-qa ─▶ BLOCKER/GAP/POLISH
                                                     │
                                            0 BLOCKERs + hash match
                                                     ▼
                                              case-publish ─▶ docx + xlsx + guide
                                                     │         + read-model promotion
                                                     ▼         + Drive push (confirm)
                                               case-track ─▶ exception queue
```

Six skills in `skills/`. Each one refuses to run if its upstream gate hasn't passed. `case-write` never invents a number — it emits `{{NEEDS_SOURCE}}` placeholders that only `case-research` may fill.

---

## Folder map

```
Math Builder/
├── README.md                    ← you are here
├── SPEC.md                      ← the case study contract (LOCKED v1.0)
├── DOCTRINE_LEDGER.md           ← every rule: PROPOSED → CODIFIED → WIRED → VERIFIED
├── DECISIONS.md                 ← append-only decision log
├── ROADMAP.md                   ← shipped / next / why
│
├── readmodel/                   ← the frozen source of record
│   ├── standards_spine.json     ← 437 atomic skills, coverage per skill
│   ├── curriculum_tree.json     ← MS → university branch tree, prereqs
│   ├── domains.json             ← 40 application domains: data sources, careers, priority
│   ├── domain_coverage.json     ← derived: domain × branch × skill join
│   ├── gap_queue.json           ← derived: thin & uncovered clusters, ranked
│   ├── corpus_index.json        ← 55 cases, per-case asset manifests
│   ├── cases_index.json         ← pipeline case registry
│   ├── roster.json              ← learners (seed)
│   └── submissions.json         ← submissions + discussion participation (seed)
│
├── skills/                      ← the six pipeline skills + PIPELINE.md
├── cases/
│   ├── _concepts/               ← brainstorm output, pre-approval
│   └── cold-chain/              ← the reference case
│       ├── case.md · case.json · FACILITATOR.md · QA_REPORT.md
│       └── published/           ← .docx case, .docx guide notes, .xlsx workbook
├── app/
│   ├── dashboard.html           ← the guide cockpit (regenerate, don't hand-edit)
│   ├── student.html             ← the learner build: separately redacted, role-locked
│   └── build_dashboard.py       ← reads readmodel/*.json + RUBRIC.md → emits both
├── doctrine/                    ← CHALLENGE_BOILERPLATE.md (character-locked)
└── source/                      ← the original corpus, read-only
    ├── Y1/ Y2/ Y3/              ← 55 cases by session, with guide notes + assets
    └── Best Of Studio/          ← student exemplars + the standards workbook
```

---

## Hard lines

- **Never fabricate a number.** Every figure is cited, or explicitly declared a stated assumption in the open. There is no third category. `case-write` physically cannot write a number.
- **Absent data is a first-class state.** "NOT PUBLISHED" is a valid cell value and renders differently from zero. Three branches have no standards rows; the dashboard says so rather than showing 0%.
- **Machine drafts, human promotes.** Nothing reaches the read-model without a QA pass and a human confirm.
- **The Tracker opens on an exception queue**, not a dashboard.
- **Both options must be defensible.** Margin over ~20% on the primary metric fails the balance test and the case gets retuned — by adjusting a constraint, never by hiding data.
- **Decision and incident logs are append-only.**
- New rules need a `DOCTRINE_LEDGER` row and a named enforcement point, or they stay UNWIRED.

---

## Regenerating

```bash
cd "Math Builder"
python3 app/build_domains.py              # rebuild domains.json + domain_coverage.json
                                          #   (also refreshes curriculum_tree.intersections[])
python3 app/validate_domains.py           # 28 independent checks over the domain spine
python3 app/build_legacy_readiness.py     # rebuild legacy_readiness.json (reads the 55 legacy .docx directly)
python3 app/build_legacy_readiness.py --verify
python3 app/build_pipeline.py             # rebuild pipeline_status.json (live Tier 1 per case + legacy fold)
python3 app/build_pipeline.py --verify    # check it's current without rewriting
python3 app/build_dashboard.py            # rebuild dashboard from read-model
python3 app/build_dashboard.py --verify   # check a build without rewriting
```

Run `build_domains.py` **before** `build_dashboard.py` — the dashboard's Root Connections view reads the derived `intersections[]` that `build_domains.py` writes. Run `build_legacy_readiness.py` **before** `build_pipeline.py` — `build_pipeline.py` folds all 55 legacy cases into the same six-column board by reading `legacy_readiness.json`'s per-case signal, so a stale or missing one silently drops the legacy fold. Run `build_pipeline.py` before `build_dashboard.py` too, for the same live-derivation reason — the Pipeline tab reads its derived `pipeline_status.json`, and that file's per-case Tier 1 status is a **live re-run at generation time**, not a cached field, so it goes stale the moment a case changes.

The dashboard inlines the read-model so it works from `file://`. Always regenerate after a case is promoted — never hand-edit `dashboard.html`.

`--verify` runs **138 checks**, including the two that matter most operationally: every asset href is
decoded, resolved against `app/` and `stat()`ed on disk (283/283 today), and every WCAG AA colour pair
is computed rather than eyeballed (26 pairs, lowest 5.27:1).

### Two builds, one generator

`build_dashboard.py` emits two files from one template:

| File | Audience | Payload |
|---|---|---|
| `app/dashboard.html` | Guide | The whole read-model. The role switch flips to a **preview** of student mode; the file still contains everything, and the role bar says so. |
| `app/student.html` | Learner | Role-locked. Contains one learner's assignments and badge progress, that learner's own skill map, the rubric, and Root Connections as career exploration — and nothing else. |

Student redaction happens in the generator (`build_student()` / `student_doc()`), not in CSS. Guide
Notes, Socratic plans, twists, QA reports, the gap queue, override bias, other learners and the growth
score are **absent from the file**, not hidden in it — a learner opening devtools finds nothing.
`--verify` greps the emitted literal for each of them. See DOCTRINE_LEDGER **MCS-34**.

> The growth score is deliberately not shown to learners at all. RUBRIC is explicit that it is a
> coaching tool for the guide; what a learner sees is which criteria are still Not Yet.
