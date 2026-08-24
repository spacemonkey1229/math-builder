# Roadmap — Math Builder

**Last refreshed: 2026-08-24, against live scripts, not carried-forward numbers.**
For the full reasoning behind any line below — why a number moved, what broke, what was fixed —
see **[ROADMAP_HISTORY.md](ROADMAP_HISTORY.md)**, the complete narrative log. This file is just
the status page: what's done, what's not, what's next.

---

## Right now — the 5 things that matter most

| # | What | Why it's first |
|---|---|---|
| 1 | **Run the first real case with a real learner** (Track A3) | The single blocking fact — 0 cases have ever been run with a real learner, out of 80 now published. Everything else is still a machine claim until this happens |
| 2 | **Write the two remaining Pre-Calculus cases** (Polar/Parametric, Trig Identities) | Finishes Pre-Calculus completely — zero gaps left in that subject |
| 3 | **Move the 7 drafting-stage cases through research → readiness → publish** (`alert-curve`, `bioreactor-bid`, `compute-lease`, `cooling-curve`, `downbeat-split`, `enclosure-call`, `placement-test`) | Already scoped and written, just sitting in the pipeline — the fastest remaining progress |
| 4 | **Finish `fret-board`'s research stage** (already has a `RESEARCH_LOG.md` started) | Closest case to clearing the gate after the drafting batch above |
| 5 | **Push `app/student-moksh-atit.html` to the live site** | Currently local-only; his first assigned month can't actually be used until this ships |

---

## What's actually ready to use right now

**Moksh Atit is set up and has his first month assigned** — 5 cases toward Badge 1, all genuinely
quality-checked: Phone Plans → Family Trip → Key Length → Field Watch → Apron Order. His page:
`app/student-moksh-atit.html`. Not yet pushed to the live site — still local only.

**80 cases** are genuinely ready to hand to any learner (passed every quality check this project
requires, live re-scan via `app/build_pipeline.py`). The previously-flagged batch of 10
mis-published cases (`archery-camp`, `baseball-lineup`, `cardiology`, `catering`, `house-plans`,
`lebron-vs-michael`, `nuclear-waste`, `phone-plan`, `rent-vs-own`, `robotics-engineer`) has since
been remediated — each now carries a recorded `TIER2_PASS` with all six Tier 2 probes passing; see
their individual `QA_REPORT.md` files for the per-case fix log. `the-multiplier-recruit`,
`the-reserve-asymptote`, and `roofline-call` have also cleared the gate and published since the
last refresh.

**7 cases are in drafting**, written but not yet researched: `alert-curve`, `bioreactor-bid`,
`compute-lease`, `cooling-curve`, `downbeat-split`, `enclosure-call`, `placement-test`.
**1 case (`fret-board`) is in research** — sourcing has started (`RESEARCH_LOG.md` exists).
**9 concepts remain unwritten**, including the two remaining Pre-Calculus gaps below and a fresh
career/industry-gap batch (`CONCEPTS_pim-sector-gaps_2026-08-24.md`).

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
| **Write/finish cases for Geometry & Pre-Calculus gaps** | 🔄 **Active priority** | See table below |
| Some subject areas have almost no cases at all | ⏳ Not started | Number Theory is the thinnest |

**Geometry & Pre-Calculus gap tracker** (reprioritized ahead of other subjects per direct request):

| Subject | Topic | Gap | Status |
|---|---|---|---|
| Pre-Calc | Matrices | 7 skills | ✅ Published (`the-multiplier-recruit`) |
| Pre-Calc | Intro to Limits | 5 skills | ✅ Published (`the-reserve-asymptote`) |
| Pre-Calc | Polar & Parametric | 6 skills | 🔜 Not written yet |
| Pre-Calc | Trig Identities | 5 skills | 🔜 Not written yet |
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

---

## The numbers, for reference

| | |
|---|---|
| Cases that are genuinely ready to assign (published, live re-scan) | **80** |
| Cases in drafting (written, not yet researched) | 7 |
| Cases in research | 1 |
| Concepts scoped but not yet written into a case | 9 |
| Cases ever run with a real student | **0** |
| Skills in the curriculum map | 437 |

Full derivations, per-script commands, and the reasoning trail for every one of these numbers are
in [ROADMAP_HISTORY.md](ROADMAP_HISTORY.md).
