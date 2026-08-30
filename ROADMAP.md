# Roadmap — Math Builder

**Last refreshed: 2026-08-30 (v2.15), against live scripts, not carried-forward numbers.**
For the full reasoning behind any line below — why a number moved, what broke, what was fixed —
see **[ROADMAP_HISTORY.md](ROADMAP_HISTORY.md)**, the complete narrative log. This file is just
the status page: what's done, what's not, what's next.

---

## Right now — the 5 things that matter most

| # | What | Why it's first |
|---|---|---|
| 1 | **Run the first real case with a real learner** (Track A3) | The single blocking fact — 0 cases have ever been run with a real learner, out of 88 now published. Everything else is still a machine claim until this happens |
| 2 | **Push `app/student-moksh-atit.html` to the live site** | Currently local-only; his first assigned month can't actually be used until this ships |
| 3 | **Write the 9 remaining scoped-but-unwritten concepts** | A fresh career/industry-gap batch (`CONCEPTS_pim-sector-gaps_2026-08-24.md`) — the drafting/research/readiness pipeline is now fully empty, so this is the next real work |
| 4 | **Push a `case-publish` to Google Drive for the first time** | Every case published this session (8 total) built its packet and promoted the read-model, but Drive upload was held back pending separate approval each time — still an open step for all of them |

---

## What's actually ready to use right now

**Moksh Atit is set up and has his first month assigned** — 5 cases toward Badge 1, all genuinely
quality-checked: Phone Plans → Family Trip → Key Length → Field Watch → Apron Order. His page:
`app/student-moksh-atit.html`. Not yet pushed to the live site — still local only.

**88 cases** are genuinely ready to hand to any learner (passed every quality check this project
requires, live re-scan via `app/build_pipeline.py`). The previously-flagged batch of 10
mis-published cases (`archery-camp`, `baseball-lineup`, `cardiology`, `catering`, `house-plans`,
`lebron-vs-michael`, `nuclear-waste`, `phone-plan`, `rent-vs-own`, `robotics-engineer`) has since
been remediated — each now carries a recorded `TIER2_PASS` with all six Tier 2 probes passing; see
their individual `QA_REPORT.md` files for the per-case fix log.

**The entire drafting/research/readiness pipeline is now empty (2026-08-30) — all 8 cases that were
in flight reached `TIER2_PASS` and published.** `bioreactor-bid` and `enclosure-call` cleared
cleanly (12.4% and 8.85% margins). The other 6 — `fret-board`, `alert-curve`, `compute-lease`,
`cooling-curve`, `downbeat-split`, `placement-test` — all hit a genuine SPEC §2 balance failure
(margins from 51.6% up to 350%, one case with a structurally zero-cost option, one with a
zero-slack tie) and needed a real retune, not a number tweak: reframed primary metrics
(`fret-board` → total shop-time, `downbeat-split` → expected studio time including redelivery
risk), re-sourced or corrected Modeling Assumptions grounded in better research
(`cooling-curve`'s mold-cost gap, `compute-lease`'s growth-rate proxy — whose fix flipped the
recommended winner entirely), an expanded/more-realistic dataset (`alert-curve`'s historical log,
6→14 rows), and added real budget slack (`placement-test`, $30k→$60k). All 8 have full packets,
interactive HTML, and are promoted in the read-model. Google Drive upload was intentionally held
back on every one, pending separate approval. Per-case detail and full retune reasoning is in each
case's `QA_REPORT.md`.
**9 concepts remain unwritten** — a fresh career/industry-gap batch
(`CONCEPTS_pim-sector-gaps_2026-08-24.md`). Both remaining Pre-Calculus gaps (Polar/Parametric,
Trig Identities) are closed.

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
| **Write/finish cases for Geometry & Pre-Calculus gaps** | 🔄 In progress | Pre-Calculus is now fully closed; Geometry gaps remain — see table below |
| Some subject areas have almost no cases at all | ⏳ Not started | Number Theory is the thinnest |

**Geometry & Pre-Calculus gap tracker** (reprioritized ahead of other subjects per direct request):

| Subject | Topic | Gap | Status |
|---|---|---|---|
| Pre-Calc | Matrices | 7 skills | ✅ Published (`the-multiplier-recruit`) |
| Pre-Calc | Intro to Limits | 5 skills | ✅ Published (`the-reserve-asymptote`) |
| Pre-Calc | Polar & Parametric | 6 skills | ✅ Published (`feedback`) |
| Pre-Calc | Trig Identities | 5 skills | ✅ Published (`deluge-gun`) |
| Geometry | Fundamentals | 7 skills | ✅ Published (`roofline-call`) |
| Geometry | Quadrilaterals & Polygons | 2 skills | ⏳ Low priority — barely worth its own case now |
| Geometry | Visual Perceptibility | 2 skills | ⛔ No case concept exists yet at all |
| Geometry | Surface Area & Volume | 3 skills | ⛔ No case concept exists yet at all |

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
| A confusing near-duplicate case name needs a human check (`redrawing-lines`) | ⏳ Open |
| **`app/dashboard.html` is a static build artifact — goes stale after every `case-publish` unless someone manually reruns `python3 app/build_dashboard.py`** | ⚠️ **Process gap, not automated** | Rebuilt 2026-08-24 (had been stale since before Grant Reach/Perimeter Protocol published, meaning the live dashboard was missing 4 published cases for several sessions with nobody noticing). The page's own masthead shows `built <date>` once logged in — check that date against today before trusting what's on screen. No CI/git-hook enforces the rebuild yet; it's still a manual step someone has to remember after every publish |
| `build_dashboard.py --verify`'s 3 failing self-checks | ⏳ Open, not investigated | Confirmed pre-existing (found 2026-08-24, unrelated to that day's rebuild): (1) `legacy_readiness` case count vs. `corpus_index` legacy count mismatch (45 vs. expected 84 — corpus_index likely isn't clearing a case's `legacy` status flag on conversion), (2) one zero-coverage cluster (Calculus/Derivatives) with no closing domain recorded, (3) legacy cases carrying `margin: 0` instead of `null`. None block a valid `dashboard.html` build; none investigated further yet |

---

## The numbers, for reference

| | |
|---|---|
| Cases that are genuinely ready to assign (published, live re-scan) | **88** |
| Cases in drafting / research / readiness | **0** — the pipeline is fully empty |
| Concepts scoped but not yet written into a case | 9 |
| Cases ever run with a real student | **0** |
| Skills in the curriculum map | 437 |
| `app/dashboard.html` last rebuilt | **2026-08-30** — must be rerun (`python3 app/build_dashboard.py`) after every future `case-publish`, or the live site keeps serving stale data even though the underlying case files are correct |

**2026-08-30 note:** `bioreactor-bid`, `enclosure-call`, `fret-board`, `alert-curve`,
`compute-lease`, `cooling-curve`, `downbeat-split`, and `placement-test` — all 8 cases that were
in flight — reached `TIER2_PASS` and published this session (packet + interactive HTML +
read-model promotion). Google Drive upload was not pushed for any of them, held for separate
approval. `fret-board`, `alert-curve`, `compute-lease`, `cooling-curve`, `downbeat-split`, and
`placement-test` all required a genuine retune first (see the note above for what changed in
each).

Full derivations, per-script commands, and the reasoning trail for every one of these numbers are
in [ROADMAP_HISTORY.md](ROADMAP_HISTORY.md).
