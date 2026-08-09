# PIPELINE — how the seven skills chain

**Version:** 2.0 · **Contract:** `SPEC.md` · **Doctrine:** Best Practices `UPDATE_LOOP.md`

Seven skills, one direction. Each stage consumes the previous stage's artifact, produces one of its
own, and is separated from the next by a **gate**. Nothing skips a gate.

```
   gap_queue.json
        │
        ▼
┌───────────────────┐  human picks a concept   ┌───────────────┐  0 unmapped / 0 unreachable
│ 1 case-brainstorm │─────────────────────────▶│ 2 case-write  │──────────────────┐
│  concept sheets   │                          │  case.md +    │                  │
└───────────────────┘                          │  case.json    │                  ▼
                                               └───────────────┘        ┌───────────────────┐
                                                                        │  3 case-research  │
   ┌────────────────────────────────────────────────────────────────────│  cited numbers    │
   │  0 placeholders OPEN                                               └───────────────────┘
   ▼
┌───────────────┐   PASS · 0 BLOCKERs · hash matches   ┌────────────────┐   published
│  4 case-qa    │─────────────────────────────────────▶│ 5 case-publish │──────────────┐
│  QA_REPORT.md │◀──── BLOCKED: back to 2 or 3 ────────│  packet +      │              │
└───────────────┘                                      │  read-model    │              ▼
                                                       └────────────────┘   ┌──────────────────┐
                                                                            │  6 case-track    │
                                                                            │  exception queue │
                                                                            └──────────────────┘
```

---

## Stage table

| # | Skill | Consumes | Produces | Gate to the next stage |
|---|---|---|---|---|
| 1 | **case-brainstorm** | `readmodel/gap_queue.json`, `standards_spine.json`, `cases_index.json` | `cases/_concepts/CONCEPTS_<target>_<date>.md` — 3–5 ranked concepts | **A human approves exactly one concept.** Nothing is written to `cases/<id>/` until then. |
| 2 | **case-write** | the approved concept, `SPEC.md`, `doctrine/CHALLENGE_BOILERPLATE.md`, the spine | `cases/<id>/case.md` (all figures `{{NEEDS_SOURCE}}`), `case.json`, `LEARNING_GOALS.md`, `FACILITATOR.md` | **LEARNING GOAL CHECK passes** — 0 unmapped deliverables, 0 unreachable skills — and `new_coverage[]` is non-empty, and every id resolves in the spine. |
| 3 | **case-research** | `case.md`, `case.json` | filled `case.md` + Sources appendix, `sources[]`, `modeling_assumptions[]`, `RESEARCH_LOG.md` | **Zero `{{NEEDS_SOURCE}}` remaining.** Every one is SOURCED, ASSUMPTION (in a visible block), or DROPPED. `NOT FOUND` is never silently filled. |
| 4 | **case-readiness** *(supersedes `case-qa`)* | everything above + `SPEC.md` | `cases/<id>/QA_REPORT.md`, `case.json.qa{}` incl. `state` and the six probe verdicts | **`state == TIER2_PASS`** — Tier 1 clean (0 BLOCKERs across 17 checks) AND all six Tier 2 probes recorded with 0 FAIL. GAPs need a recorded waiver. The report stores `sha256(case.md)`. |
| 5 | **case-publish** | a PASS case | `cases/<id>/published/` (.docx, optional .xlsx, facilitator guide, MANIFEST.json); mutates `cases_index.json`, `standards_spine.json`, `gap_queue.json`; optional Drive upload | **Two explicit human confirms** — one before the read-model write, one before the Drive push. Snapshot first. |
| 6 | **case-track** | `cases_index.json` (read-only), `roster.json`, `submissions.json` | assignments, submissions, discussion records, the exception queue | A recorded submission is scorable. `case-track` still never scores. |
| 7 | **submission-score** | a submission (docx/pdf/md/xlsx) + `case.json` + `RUBRIC.md` | `student_work/<learner>/<case>/SCORE.md`; `submissions.json.scores[]`; `score_overrides.json` | **A guide confirms.** `machine-first-pass` never counts toward a badge. Cohort roll-up feeds *backwards* into stage 4. |
| — | **TIER 3 dry-run** | a `PUBLISHED` case + real learners | `cases/<id>/runs/RUN_<date>_<guide>.md` (`templates/RUN_REPORT.md`) | **A filed RUN_REPORT with no unresolved artifact-attributed defect** promotes `PUBLISHED` → `VERIFIED`. Only `VERIFIED` may be ✅ in the doctrine ledger. |

---

## The gates, stated as refusals

Each stage refuses to start if its input gate is not met. These are the load-bearing lines:

1. **case-write refuses** a concept with no binary dilemma or no primary metric.
2. **case-write refuses to emit `case.json`** while any deliverable is unmapped or any claimed
   skill is unreachable. An unreachable skill inside `new_coverage[]` is the worst defect in the
   system: it marks a gap closed that no student ever touched, and every future gap query
   inherits the lie.
3. **case-research refuses** to invent. `NOT FOUND` returns three exits — stated Modeling
   Assumption, case redesign, or drop the figure. There is no fourth.
4. **case-readiness refuses** to fix anything. It names the defect and the exact repair, and hands
   back. It also refuses to record `TIER2_PASS` while any probe is `NOT RUN` — a probe that could
   not run is never reported as a probe that passed.
5. **case-publish refuses** on `verdict != PASS`, on `blockers_open > 0`, and on a **stale hash** —
   if `case.md` changed after the QA run, the report no longer describes the file.
6. **case-track refuses** to assign a case that is not `published` or `legacy`, and refuses to
   award a badge or complete an assignment without a human confirm.
7. **submission-score refuses** to mark C7 Exemplary (asserted in code), to write status
   `confirmed` (only `guide_confirm.py` can), to accept an override with no reason, and to treat
   an unreadable file or a zero discussion count as an absence of work.

## What goes backwards

| Finding | Re-enter at |
|---|---|
| QA BLOCKER on structure, boilerplate, balance, tier, learning goals | **2 case-write** |
| QA BLOCKER on an uncited number, a buried assumption, a dead link | **3 case-research** |
| Research returns NOT FOUND on a load-bearing figure and recommends redesign | **2 case-write**, or **1 case-brainstorm** if the premise is gone |
| Margin > 20% — unbalanced | **2 case-write**: retune a *constraint*. Never fix a margin by hiding data. |
| A facilitator reports the case does not work in discussion | **1 case-brainstorm** with the failure as input |
| Tier 2 probe FAIL: cold solve reaches an indefensible position, or one side collapses | **2 case-write** |
| Tier 2 probe FAIL: twist depends on an unstated convention, or verdict flips under a ±50% assumption flex | **2 case-write** — state the convention, or state the instability |
| Tier 2 probe FAIL: a cited URL is dead, or resolves but no longer carries its figure | **3 case-research** |
| Tier 3 finding attributed to **the artifact** | **4 case-readiness**, then 2 or 3 |
| Tier 3 finding attributed to **delivery** | guide coaching. Does **not** block the case |
| Cohort roll-up: >50% of a cohort Not Yet on one criterion | **4 case-readiness** — a criterion most of a room fails is a case defect until proven otherwise |

Any edit after a QA run invalidates the hash, so **any backward step forces a QA re-run.** That
is the intent.

---

## Artifact map

```
Math Builder/
├── SPEC.md                              the contract (LOCKED)
├── doctrine/
│   └── CHALLENGE_BOILERPLATE.md         canonical Challenge 1/2/4/5 text — one copy, two readers
├── readmodel/
│   ├── standards_spine.json             322 skills · covered_by[] · n   ← written only by case-publish
│   ├── gap_queue.json                   DERIVED from the spine — never hand-edited
│   ├── cases_index.json                 every case · seeded with 27 legacy · appended by case-publish
│   ├── roster.json                      learners + badge programs       ← written only by case-track
│   ├── submissions.json                 assignments·submissions·discussions ← case-track
│   │                                    scores[]                        ← submission-score ONLY
│   ├── score_overrides.json             every guide disagreement        ← submission-score ONLY
│   └── _snapshots/                      pre-promotion copies, timestamped
├── templates/
│   ├── RUN_REPORT.md                    Tier 3 human dry-run gate
│   ├── SELF_REVIEW.md   PEER_REVIEW.md  three questions each, one page each
├── student_work/<learner>/<case>/
│   ├── SCORE.md                         ← submission-score
│   └── SELF_REVIEW.md  PEER_REVIEW.md   ← the Hero and a peer
├── cases/
│   ├── _concepts/                       stage 1 output; never a full case
│   └── <id>/
│       ├── case.md  case.json  LEARNING_GOALS.md  FACILITATOR.md
│       ├── sensitivity_model.py         optional; required for Tier 2 probe 5
│       ├── RESEARCH_LOG.md   QA_REPORT.md
│       ├── runs/RUN_<date>_<guide>.md   Tier 3 evidence
│       └── published/       .docx · .xlsx · facilitator guide · MANIFEST.json
└── skills/                              seven SKILL.md files + this map
    ├── case-qa/                         SUPERSEDED — pointer + SKILL.superseded.md
    ├── case-readiness/                  supersedes case-qa; scripts/ + selftest
    └── submission-score/                scripts/ score · guide_confirm · cohort_rollup
```

**Write ownership is exclusive.** Exactly one skill writes each file. If two skills could write
the same file, one of them is wrong. `submissions.json` is the single documented exception and it
is exclusive **per array**: `case-track` owns `assignments[]`, `submissions[]` and
`discussions[]`; `submission-score` owns `scores[]`. Neither writes the other's array.

## Readiness ladder (case-readiness)

```
DRAFT --T1--> TIER1_PASS --T2--> TIER2_PASS --2 human confirms--> PUBLISHED --T3--> VERIFIED
```

| State | Requires | Licenses |
|---|---|---|
| `TIER1_PASS` | 17 structural + continuity checks, 0 BLOCKERs | Tier 2 may start |
| `TIER2_PASS` | six probe verdicts recorded, 0 FAIL | `case-publish` may run |
| `PUBLISHED` | Tier 1 + Tier 2 clean, two human confirms | the case may be assigned |
| `VERIFIED` | a filed RUN_REPORT from a real cohort | **the case may be marked ✅ in the ledger** |

`PUBLISHED` is deliberately reachable without Tier 3 — you cannot dry-run a case you have not
published. `VERIFIED` is not. Per the ledger's own rule, *no ✅ without a QA report naming the
case it was verified against.*

## Status ladder

`concept → draft → researched → qa → published` (plus `legacy` for the 27 corpus cases, and
`retired`). The status lives in `case.json.status` and is mirrored into `cases_index.json` at
publish. A case at `qa` with `verdict: BLOCKED` stays at `qa` until the blockers clear.

---

## Doctrine this pipeline inherits

From `Best Practices/UPDATE_LOOP.md` and `README.md`:

- **Machine drafts, human promotes.** Stages 1–4 stage; stage 5 promotes, and only on a confirm.
- **The SOR is frozen.** `standards_spine.json` is written at exactly one moment by exactly one
  skill, after a snapshot, idempotently.
- **Never fabricate a number.** SPEC §5. Cited, or declared an assumption in the open. Nothing else.
- **A "verbatim"/"publicly verifiable" claim needs a `sources[]` row, always** — `case-readiness`
  T1-08 blocks any `legacy`-origin case that claims real, externally-checkable data without at
  least one HIGH/MEDIUM `sources[]` entry backing it (added 2026-08-04, after a fabricated real
  clinical-trial table and a stale real-athlete season both reached `TIER1_PASS` on this exact
  gap). Populate `sources[]` — or run and record Tier 2's P6 data-decay probe — as part of the
  conversion itself, not after a QA run bounces it back.
- **`case-publish` requires `qa.state == "TIER2_PASS"`, not just Tier 1.** Tier 1 proves internal
  consistency; it cannot see whether a cited real-world number is actually true. Run Tier 2 before
  asking to publish — do not treat `TIER1_PASS` as "good enough for now."
- **A still-changing real entity (active athlete, live price, ongoing company) gets a stated "as
  of" cutoff, applied to every number tied to it** — SPEC §5.
- **Absent data is a first-class state.** `NOT FOUND`, `null`, `NOT RECORDED` are real answers
  that get surfaced — never silently replaced with a plausible value.
- **The critique pass is not optional.** BLOCKER / GAP / POLISH, and every BLOCKER resolved.
- **A machine gate proves consistency, not fitness.** The sibling HIGH GRADE kit passed all
  thirteen of its structural checks and all six of its simulated-play probes and still failed in
  front of a real room — and the post-mortem could not tell whether the artifact or the
  facilitation was at fault. That is why Tier 3 exists, why its report demands facts before
  impressions, and why it forces a design-vs-delivery attribution.
- **The home screen is an exception queue.** `case-track` defaults to the queue, not a dashboard.
- **One read-model, built first.** Every surface — the skills and the app — reads `readmodel/`.
  Nothing queries `cases/` directly.
