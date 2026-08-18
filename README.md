# Math Builder — Learn Math by Case Study

> **What this is:** A production system for Acton-style quantitative case studies for middle and high school. It ingests three years of existing curriculum, maps it against an atomic standards spine and a MS→university curriculum tree, finds the holes, and runs new cases through a seven-stage pipeline from concept to published packet to student tracking.

**State:** ACTIVE · **Phase:** 2 (Build) · **Independent project as of 2026-08-01** — see
`00_SESSION.md` for the full per-project instructions block.

**Where it stands (2026-08-12).** Spine locked, pipeline built and run repeatedly, a corpus of
authored cases, three QA/scoring modules tested end to end, and — new since 2026-08-08 — a **live
hosted admin app** (Flask on Vercel + Neon Postgres) that runs the real learner loop from any
device. The full assign → submit → machine-score → guide-confirm → revise → complete cycle has run
for real, more than once, against real submission files. **Zero cases are `VERIFIED`**: no case has
been run with a real cohort in a real room, which is the only thing still standing between this and
Phase 3. That gap is now scheduling, not engineering.

> **This project is two things sharing one read-model**, and conflating them causes real errors: a
> **local authoring pipeline** with static `file://` dashboards, and a **hosted learner-management
> app**. The boundary is deliberate — see `TECH_STACK.md` and MCS-42/43. Practical consequence:
> promoting a case is a local act, and the live app needs a **redeploy** before it can assign it.

> **Don't trust a count written in prose here.** Corpus size, coverage and per-case status change
> several times a day while authoring is active. Every number below carries an "as of" date and is
> derived from `readmodel/`. To get the truth right now, run the commands in *Regenerating*.

---

## Start here

0. **`00_SESSION.md`** — the paste-ready per-project instructions block (what to read, in what order, the hard lines). Read this first if you're starting a session cold in this folder.
1. **`SPEC.md`** — the contract. What a case study *is*, its seven required sections, the balance test, the difficulty tiers, and the facilitator artifacts. Everything else enforces this.
2. **`app/dashboard.html`** — open it. Eight views over the whole corpus: curriculum tree, coverage heatmap, case library, **root connections**, **rubric & scoring**, **pipeline**, gap queue, tracker. One pipeline, not two: the pipeline view is a live map of every concept, native case, *and* legacy case against the real six pipeline stages (concepting → drafting → research → readiness → promotion → verified). Native cases carry a Tier 1 status re-run live at build time (`app/build_pipeline.py`), not read from a cached field. The 55 pre-pipeline corpus cases are triaged into the same six columns by real signal read from their source `.docx` (`app/build_legacy_readiness.py`) — a locked binary dilemma with Guide Notes and standards tagging lands in Drafting as `NEAR READY`; a dilemma that isn't strictly binary yet lands in Concepting, the same design decision a brand-new concept needs — because the current locked `CHALLENGE_BOILERPLATE.md` wording and the 11-anchor Guide Notes ladder both postdate this corpus, so a case is placed by what it actually has, not failed for predating doctrine it couldn't have followed. A small number of cases whose `.docx` can't be triaged at all (misfiled asset, missing core section) are named as exceptions rather than guessed at. Every case asset is a working link that opens the real `.docx`/`.xlsx`/`.pdf` from `file://`; every view cross-navigates to every other; `/` searches everything; the Back button and the browser's own back both work. A guide/student role switch lives in the top bar — see *Two builds* below.
3. **`skills/PIPELINE.md`** — how the six authoring skills chain together and what gates sit between them.
4. **`cases/cold-chain/`** — the worked reference case. Read `case.md`, then `FACILITATOR.md`, then `case.json`. For a case that clears the *current* gate end to end, read `cases/plaza-pavers/` instead — it ships `TIER2_PASS`, a sensitivity model, a QA report and the full five-file packet.
5. **`TECH_STACK.md`** — this project's own complete stack record, and the doc that explains the two-halves split. Read it before assuming anything about hosting, auth or where data lives.
6. **`student_work/UAT_LOG.md`** — the real bug ledger from actually using the thing. If you want to know what breaks in practice rather than in theory, this is the file.

---

## What the corpus actually contains

*As of 2026-08-12. Authoring is active — re-derive rather than cite these.*

| | Count |
|---|---|
| Case studies in the source corpus (Y1–Y3 + Best of Studio) | **55** (stable — read-only input) |
| Cases authored by this pipeline | **16+ and climbing** (was 1 on 2026-08-01) |
| — of those, at `TIER2_PASS` with a sensitivity model, QA report and full 5-file packet | 5, all authored 2026-08-12 |
| — of those, at `TIER1_PASS` only, demoted from `published` by D-020 | 10, the 2026-08-04/05 batch |
| Cases `VERIFIED` by a real cohort | **0** — the one blocker (ROADMAP A3) |
| Atomic skills in the standards spine | **437** across 11 domains (322 original MS + 115 Pre-Calc/Calculus/Discrete, added 2026-08-01 — ROADMAP B2). All ids globally unique (MCS-36) |
| Skills with zero coverage | moving fast as cases land — `standards_spine.json.totals.uncovered` is the only honest source |
| Cases with facilitator Guide Notes | 40 of 55 legacy |
| Cases with a timed 45-minute Socratic plan | 2 of 55 legacy; every pipeline case ships one (MCS-16) |

**The headline finding about the legacy corpus: the standards matrix is roughly three years stale.** More than half of it had never been tagged. `case-reconcile` worked that backlog to its honest ceiling on 2026-08-01 (28 → 45 tagged cases, uncovered 97 → 93), and the remaining 20 titles were *read*, not skipped — 2 are revisions of already-tagged cases, 18 genuinely name no math vocabulary. **Tag before you author.** The dashboard keeps this reconciliation rail separate from the authoring backlog for exactly this reason.

**The headline finding about the pipeline (2026-08-12): it outran its own gate, then fixed itself.** The Aug 4–5 batch shipped ten cases to `published` at `TIER1_PASS` — no sensitivity model, so Tier 2 probe 5 returned `NOT RUN` — while Cold Chain sat demoted to `qa` for being at exactly that level. The five cases authored 2026-08-12 all clear `TIER2_PASS` with the full packet, a *higher* bar than Cold Chain ever reached. The rule is now written down (MCS-41, D-020) and the ten are demoted by `scripts/apply_publish_gate.py`. Backfilling them is the top Track A queue item.

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
├── skills/                      ← the pipeline skills + PIPELINE.md
│   └── case-publish/scripts/    ← build_docx.js (Node, the `docx` package)
├── cases/
│   ├── _concepts/               ← brainstorm output, pre-approval
│   └── <case-id>/               ← one folder per case; cold-chain is the reference
│       ├── case.md · case.json · FACILITATOR.md · LEARNING_GOALS.md
│       ├── QA_REPORT.md · sensitivity_model.py   ← both REQUIRED for published (MCS-41)
│       └── published/           ← Case Study .docx · Facilitator Guide .docx
│                                  Data .xlsx · Interactive .html · MANIFEST.json
├── app/
│   ├── dashboard.html           ← the guide cockpit (regenerate, don't hand-edit)
│   ├── student.html             ← the learner build: separately redacted, role-locked
│   ├── build_dashboard.py       ← reads readmodel/*.json + RUBRIC.md → emits both
│   ├── build_domains.py · build_pipeline.py · build_legacy_readiness.py
│   ├── validate_domains.py      ← 28 independent checks over the domain spine
│   ├── admin_core.py            ← THE state machine (assign→score→confirm→complete)
│   ├── admin_html.py            ← the admin UI
│   ├── admin_server.py          ← local transport, binds 127.0.0.1 only (D-015)
│   ├── store_local.py / store_postgres.py   ← the two store adapters (MCS-43)
│   └── admin_web/app.py         ← hosted transport, Flask (D-016)
├── api/index.py                 ← Vercel entry point → admin_web
├── sql/schema.sql               ← Neon Postgres: the 4 runtime-mutable docs only
├── scripts/
│   ├── migrate_to_neon.py       ← one-time JSON → Postgres migration
│   └── apply_publish_gate.py    ← MCS-41 sweep; --confirm to write (D-020)
├── templates/                   ← interactive_shell.html · CONTRACT · RUN_REPORT
│                                  PEER_REVIEW · SELF_REVIEW
├── student_work/                ← per-learner submissions + SCORE.md
│   ├── UAT_LOG.md               ← the real bug ledger. Best artifact in the repo
│   ├── LIFECYCLE_SCRIPT.md      ← the live end-to-end demo walkthrough
│   └── <learner>/<case>/        ← submitted/ + SCORE.md
├── doctrine/                    ← CHALLENGE_BOILERPLATE.md (character-locked)
├── vercel.json · requirements.txt · package.json
└── source/                      ← the original corpus, read-only, GITIGNORED (140MB)
    ├── Y1/ Y2/ Y3/              ← 55 cases by session, with guide notes + assets
    └── Best Of Studio/          ← student exemplars + the standards workbook
```

> **`source/` is gitignored.** A fresh clone cannot run `build_legacy_readiness.py` (it reads the 55
> legacy `.docx` directly) until that folder is restored out of band. Everything else builds.

---

## Hard lines

- **Never fabricate a number.** Every figure is cited, or explicitly declared a stated assumption in the open. There is no third category. `case-write` physically cannot write a number.
- **Absent data is a first-class state.** "NOT PUBLISHED" is a valid cell value and renders differently from zero. Three branches have no standards rows; the dashboard says so rather than showing 0%.
- **Machine drafts, human promotes.** Nothing reaches the read-model without a QA pass and a human confirm.
- **The Tracker opens on an exception queue**, not a dashboard.
- **Both options must be defensible.** Margin over ~20% on the primary metric fails the balance test and the case gets retuned — by adjusting a constraint, never by hiding data.
- **`published` requires `TIER2_PASS`** (MCS-41, D-020). That flag is what makes a case assignable to a real learner, so it is never bookkeeping. A case with no `sensitivity_model.py` has never had its verdict swung ±50% against its own stated assumptions — probe 5 returns `NOT RUN`, which is never a pass.
- **Decision and incident logs are append-only.**
- New rules need a `DOCTRINE_LEDGER` row and a named enforcement point, or they stay UNWIRED.
- **A decision that changes the stack updates `TECH_STACK.md` in the same pass**, not only `DECISIONS.md`. This line exists because that failed once, for eleven days.
- **More than one session may be in this repo at once.** `main` can move under you mid-task. Re-check `git log`/`git status` before merging, committing or deploying — never act on a snapshot from earlier in your own session.

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

`--verify` runs **150 checks** (as of 2026-08-12), including the two that matter most operationally:
every asset href is decoded, resolved against `app/` and `stat()`ed on disk (285/285 today), and
every WCAG AA colour pair is computed rather than eyeballed (26 pairs, lowest 5.27:1).

### The hosted admin app

The commands above rebuild the **local** artifacts. The live app is a separate surface:

```bash
python3 app/admin_server.py                 # local admin, 127.0.0.1 only (D-015)
python3 scripts/apply_publish_gate.py       # dry-run the MCS-41 publish gate
python3 scripts/apply_publish_gate.py --confirm   # apply it (snapshots first)
vercel --prod                               # deploy the hosted variant (D-016)
```

Because only four read-model docs are runtime-mutable (MCS-43), **a case promoted locally is not
assignable in the live app until you redeploy.** That is by design — the hosted app runs the
learner loop, never the authoring pipeline.

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
