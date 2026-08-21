# Roadmap — Math Builder

**Last refreshed: 2026-08-19, against live scripts, not carried-forward numbers.**
For the full reasoning behind any line below — why a number moved, what broke, what was fixed —
see **[ROADMAP_HISTORY.md](ROADMAP_HISTORY.md)**, the complete narrative log. This file is just
the status page: what's done, what's not, what's next.

---

## Right now — the 5 things that matter most

| # | What | Why it's first |
|---|---|---|
| 1 | **Decide what to do about 10 mis-published cases** ([below](#-known-issue-10-cases-are-published-but-shouldnt-be)) | They're currently handed to real students without meeting this project's own quality bar |
| 2 | **Run the first real case with a real learner** (Track A3) | The single blocking fact — 0 cases have ever been run with a real learner. Everything else is still a machine claim until this happens |
| 3 | **Move `the-multiplier-recruit` and `the-reserve-asymptote` through the readiness gate** | Already fully written, just sitting unpromoted — the fastest possible progress on Track B |
| 4 | **Write the two remaining Pre-Calculus cases** (Polar/Parametric, Trig Identities) | Finishes Pre-Calculus completely — zero gaps left in that subject |
| 5 | **Write the Geometry "Roofline Call" case** | Biggest remaining Geometry gap with a case concept already scoped for it |

---

## What's actually ready to use right now

**Moksh Atit is set up and has his first month assigned** — 5 cases toward Badge 1, all genuinely
quality-checked (not from the flagged batch below): Phone Plans → Family Trip → Key Length →
Field Watch → Apron Order. His page: `app/student-moksh-atit.html`. Not yet pushed to the live
site — still local only.

**39 cases** are genuinely ready to hand to any learner (passed every quality check this project
requires). **10 more are currently live but shouldn't be** — see the flagged issue below.

---

## ⛔ Known issue: 10 cases are "published" but shouldn't be

These 10 skipped a required quality check (a "what if our numbers are wrong by 50%?" stress test)
but got marked ready anyway. They're currently assignable to a real student today.

`archery-camp` · `baseball-lineup` · `cardiology` · `catering` · `house-plans` ·
`lebron-vs-michael` · `nuclear-waste` · `phone-plan` · `rent-vs-own` · `robotics-engineer`

**Needs a decision:** pull them back from "ready" until they pass the check (`scripts/
apply_publish_gate.py --confirm` does this), or explicitly decide the bar doesn't apply here.
Either way, someone should decide — right now it's just silently wrong.

---

## Status by area

Legend: ✅ done · 🔄 in progress · 🔜 next up · ⏳ open, not started · ⛔ blocked / needs a decision

### Quality — is any case actually good enough?

| Item | Status | What's left |
|---|---|---|
| Fix the flagship case (Cold Chain) | ✅ Done | — |
| Require a "stress test" before any case ships | ✅ Enforced by a script | 10 cases slipped through anyway — see the flagged issue above |
| **Run the first case with real students** | ⛔ **Not started — the #1 blocker** | Pick any of the 39 clean cases, run it, fill in the results |
| Reusable case-page template | ✅ Done | Proven across many cases already |
| Facilitator "cohort size" guidance | 🔄 Only 1 case has it | Every case with facilitator notes needs its own |
| Fix the 10 mis-published cases | ⛔ Needs a decision | See flagged issue above |

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
| Pre-Calc | Matrices | 7 skills | ✅ Case written (`the-multiplier-recruit`) — just needs to clear the gate |
| Pre-Calc | Intro to Limits | 5 skills | ✅ Case written (`the-reserve-asymptote`) — just needs to clear the gate |
| Pre-Calc | Polar & Parametric | 6 skills | 🔜 Not written yet |
| Pre-Calc | Trig Identities | 5 skills | 🔜 Not written yet |
| Geometry | Fundamentals | 7 skills | 🔜 Not written yet ("The Roofline Call") |
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
| Two files sitting edited-but-uncommitted (`build_dashboard.py` fix, a `00_SESSION.md` note) | ⛔ Needs a decision — commit or discard |
| A confusing near-duplicate case name needs a human check (`redrawing-lines`) | ⏳ Open |

---

## The numbers, for reference

| | |
|---|---|
| Cases that are genuinely ready to assign | **39** |
| Cases currently live but flagged (see above) | **10** |
| Cases fully written, waiting on final checks | 3 |
| Cases ever run with a real student | **0** |
| Skills in the curriculum map | 437 |
| Skills with zero case coverage | 73 |
| Skills covered in Geometry specifically | all but 14 |
| Skills covered in Pre-Calculus specifically | all but 23 (12 of those already have a written, unpromoted case) |

Full derivations, per-script commands, and the reasoning trail for every one of these numbers are
in [ROADMAP_HISTORY.md](ROADMAP_HISTORY.md).
