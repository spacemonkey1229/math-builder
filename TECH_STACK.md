# Tech Stack — Math Builder

> **Graduated 2026-08-01.** This project is now self-governed — it no longer references or
> defers to `Best Practices/TECH_STACK.md`. This doc was originally written as a "reference +
> addendum" to that canonical file; on graduation it was reframed as the authoritative, complete
> record of this project's own stack. The content below reflects real choices already running in
> this codebase, not aspirational ones. Anything past decisions worth carrying to a future
> project is this project's own call, not something the canonical doc needs to absorb.

> **Updated 2026-08-12.** This doc previously declared "there is no server, no login, no database,
> no deploy step." That stopped being true on 2026-08-08 (D-015) and 2026-08-09 (D-016) and the
> statement stood here uncorrected for eleven days — a project review found it by grepping every
> governance doc for `vercel|neon|postgres` and getting zero hits across all six. The rewrite below
> is what actually runs. The old text is preserved verbatim in *The line that used to be here* at
> the bottom, because MCS-22's principle applies to prose too: nothing is superseded silently.

## The shape of this project

Math Builder is **two things sharing one read-model**, and keeping them distinct is the whole
design:

1. **A local content-generation pipeline with a static artifact viewer.** Output is a folder of
   `.docx`/`.xlsx`/`.html` files plus two dashboards that read a JSON read-model off disk. This
   half has no server, no login and no deploy step — it runs from the command line against the
   local filesystem, and its deliverables are files a guide opens directly. This is still the
   larger half and still where every case is authored.
2. **A hosted learner-management app.** A Flask app on Vercel backed by Neon Postgres, guarded by a
   shared passcode, which runs the day-to-day loop a guide needs from any device: assign a case,
   record a submission, run the machine scorer, confirm a review, mark complete, award a badge.

The boundary between them is deliberate and load-bearing (MCS-42/MCS-43): **the read-model may be
written by a server; the dashboards may never be served by one.** `dashboard.html` and
`student.html` stay pure derived views that work from `file://` with no runtime fetch. And only the
four docs that are genuinely written at runtime live in Postgres — everything else is build-time
content shipped as static files, which is why promoting a case requires a redeploy before the live
app can assign it.

## The actual stack

- **Authoring & pipeline scripts** — Python 3, stdlib plus `python-docx` (Word generation),
  `openpyxl` (Excel generation). One Node script also exists — `skills/case-publish/scripts/
  build_docx.js`, using the `docx` npm package (`package.json`); `node_modules/` is gitignored, the
  lockfile is not.
- **Read-model** — flat JSON files under `readmodel/`, the source of record for authoring. Every
  local write is preceded by a snapshot to `readmodel/_snapshots/<file>.<timestamp>` (MCS-22) —
  this project's substitute for transactional safety. **Split by mutability (MCS-43):** exactly
  four docs are written at runtime and therefore live in Postgres when hosted — `roster.json`,
  `submissions.json`, `score_overrides.json`, `demoted_criteria.json`. The rest
  (`standards_spine.json`, `curriculum_tree.json`, `domains.json`, `domain_coverage.json`,
  `cases_index.json`, `gap_queue.json`, `corpus_index.json`, `pipeline_status.json`,
  `legacy_readiness.json`, `reconcile_queue.json`) is build-time content, never written at runtime,
  and ships as static files in the deployment.
- **Admin write path** — two transports over one core (MCS-42). `app/admin_core.py` holds the
  entire state machine (assign → submit → score → confirm → complete, badge math, eligibility
  checks, exception queue) parameterized on a `store` object, so there is no duplicated policy to
  drift. `app/store_local.py` (real files) backs `app/admin_server.py`, a stdlib-only server bound
  to `127.0.0.1`. `app/store_postgres.py` (Neon) backs `app/admin_web/app.py`, the Flask app
  deployed via `api/index.py`. `PostgresStore.materialized_project()` bridges the gap for the two
  scoring scripts that genuinely need a filesystem: it builds a temp project tree in `/tmp`, runs
  `score_submission.py`/`guide_confirm.py` unmodified, and syncs the mutations back.
- **Hosting** — Vercel (`vercel.json`, `api/index.py`, 60s function ceiling) + Neon Postgres
  (`sql/schema.sql`, migrated by `scripts/migrate_to_neon.py`). `requirements.txt` pins Flask and
  `psycopg`. Auth is a single shared passcode (`ADMIN_PASSCODE`) behind a signed session cookie —
  a **named stopgap, not a design endorsement** (MCS-44); there are no roles and no per-user
  identity, so the audit trail records a typed guide name rather than an authenticated actor. The
  one deliberately public route is the student-facing interactive case page, scoped to exactly one
  filename shape (MCS-45).
- **Dashboard / student view** — single-file HTML + vanilla JS + inline CSS
  (`app/dashboard.html`, `app/student.html`), generated by `app/build_dashboard.py` which inlines
  the JSON read-model directly into the page at build time. No framework, no bundler, no build
  step beyond running the Python generator. Opened via `file://`, not served.
- **Interactive case artifacts** — single-file HTML per case (e.g.
  `cases/cold-chain/published/Cold Chain - Interactive.html`), inline SVG only (MCS-37 — no
  external image dependencies), vanilla JS self-checking calculators, `localStorage` for a
  student's own in-session progress (checklist state, notes). `templates/interactive_shell.html` is
  the case-agnostic scaffold (A7) and `templates/INTERACTIVE_HTML_CONTRACT.md` the contract.
  **`localStorage` is now a stated limitation rather than a free choice:** these pages are served
  over `https://` by the hosted app (MCS-45), so a learner's checklist state is per-device and
  per-origin, and does not follow them between the `file://` copy and the hosted one.
- **QA / gating** — pure Python scripts, no external services: `tier1_structural.py` (mechanical
  structural checks), `tier2_probes.py` (simulated-play probes, some requiring a fresh subagent),
  `tier3_verify.py` (human dry-run gate), `score_submission.py` + `guide_confirm.py` +
  `cohort_rollup.py` (submission scoring). All run from the command line against the local
  filesystem.
- **Source verification** — a web-fetch tool at authoring time only, to confirm every cited
  figure and every glossary URL (MCS-21, MCS-39) before it's written into a case. Nothing is
  fetched at runtime; the QA sandbox this project's scripts run in has no outbound network, which
  is why Tier 2 probe 6 (data decay) and Tier 1's URL checks are DELEGATED rather than
  self-executing.

## What this project deliberately does NOT have

- **No CI, and no automated tests over the hosted app.** The repo's only test file is
  `skills/case-readiness/scripts/selftest_tier1.py`. `admin_core.py`, `store_postgres.py` and
  `admin_web/app.py` — the code now handling real learner data over the internet — are covered by
  the manual UAT checklist in `student_work/UAT_LOG.md` and nothing else. Every production bug found
  so far was found by a human using the app. That has worked and does not scale; it is on the
  UNWIRED queue, not defended as a choice.
- **No roles, and no real auth.** One shared passcode (MCS-44). Guide/student *content* separation
  is still done at generation time (MCS-34 — `build_student()` emits a genuinely separate redacted
  payload, verified by `--verify` greps), which is stronger than a login gate and unaffected by the
  above. What's missing is per-guide identity on the write path.
- **No runtime data fetch in the dashboards.** Deliberate and enforced (MCS-42): both HTML builds
  stay self-contained and openable from `file://`.
- **No authoring pipeline in the hosted app.** It runs the learner loop only. Publishing a case is
  still a local command-line act followed by a redeploy (MCS-43).

## If this ever needs to change

This section used to say "if a future need shows up — real hosting, multiple concurrent guides, a
shared login — treat it as a new architectural decision and write it into `DECISIONS.md`."
**That is exactly what happened** (D-015, D-016, D-018), and the process half worked: the decisions
were written, and this doc was not updated to match for eleven days. So the rule gets one addition:
a decision that changes the shape of the stack must update **this file in the same pass**, not only
`DECISIONS.md`. A `DECISIONS.md` entry records *why*; this file is what a cold session reads to
learn *what runs*.

The next architectural decisions already named and deferred: a real auth provider with per-guide
identity (MCS-44), and a regression net over the admin core.

## The line that used to be here

Preserved verbatim, superseded 2026-08-12 by D-015/D-016 — kept because a doc that quietly rewrites
its own history teaches the next reader that its current claims are equally disposable:

> Math Builder is a **local content-generation pipeline with a static artifact viewer** — output is
> a folder of `.docx`/`.xlsx`/`.html` files plus one dashboard that reads a JSON read-model off
> disk. It is not a hosted Operator Cockpit, not a deployed multi-user web app, and not a physical
> product — there is no server, no login, no database, no deploy step. Everything runs from the
> command line against the local filesystem, and the deliverables are files a guide opens directly.
