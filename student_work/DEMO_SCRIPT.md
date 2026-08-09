# Math Builder — Director Demo Script

**Purpose of this session:** show the director three things, in order — the vision (why this
exists), the execution (what's actually built), and the operations (does the full loop really
work, end to end, with real data). Total time: ~20 minutes, plus questions.

**Before you start:** open two files in a browser —
`app/dashboard.html` (the guide/admin view) and `app/student.html` (the learner view). No server,
no login, no internet needed — everything runs from these two files. Keep both tabs open; you'll
flip between them.

---

## Opening (1 min)

> "Every case study here is a real decision — a harbor pilot deciding whether to risk a channel
> transit, a caterer choosing which event pays off, a robotics engineer routing a rescue robot.
> The student has to compute a real answer and then defend a position, out loud, to a room that
> can push back. That's the whole idea: math as the tool you need to win an argument that matters,
> not a worksheet.
>
> What I want to show you today isn't a pitch deck. It's the actual system — the same one a
> student and a facilitator would use — with two real students' real work already run through it,
> so you can see the whole loop, not just a mockup of it."

---

## Part 1 — The vision: one curriculum, fully mapped (3 min)

**Screen:** `dashboard.html`, **Curriculum Tree** tab (default view).

Talking points:
- "This is the whole math curriculum, middle school through the start of university, broken into
  437 individually-trackable skills across 11 domains. Every ring shows real coverage — how many
  of those skills currently have a case study that actually forces a student to use them."
- Click into **Coverage Heatmap** — "Green is covered, and covered means a real case exists that a
  student can't finish without using that skill. This isn't aspirational; it's computed from the
  actual case files every time we rebuild."
- Click **Case Library** — "56 cases in the source corpus; 12 fully rebuilt and hardened this
  cycle — 10 published and assignable today, 2 one gate away."
- Click **Root Connections** — "Every skill also connects to a real career and a real data source
  — this is where 'why do I need to know this' gets answered with an actual job, not a platitude."

**The point to land:** this isn't a pile of worksheets. It's an instrumented curriculum — you can
always ask "what's covered, what's thin, what's missing" and get a real answer.

---

## Part 2 — The execution: what a case actually looks like (5 min)

**Screen:** open any case's interactive HTML directly, e.g.
`cases/catering/published/Catering - Interactive.html`.

Talking points:
- Scroll through the **Overview → Background → Dilemma**. "This reads like a story because it is
  one — a real decision with two genuinely defensible sides. The case doesn't work if one side is
  obviously right; we test that with a balance requirement before a case ever ships."
- Point at the **Working Notebook** section. "This is a calculator, not an answer key — students
  type their own numbers, hit Check, and get told if they're right without being told the answer
  first."
- Open the **glossary** (hover a term, click a term). "Every technical term is hoverable for a
  plain-English definition and clickable through to a real, verified external lesson — Khan
  Academy or equivalent, link-checked, not just assumed to work."
- Scroll to the **Deliverables checklist** and the **CSV/PDF export** buttons. "A student's work
  packages into something they can actually submit, and it saves locally in their browser as they
  go — nothing sent anywhere until they're ready."

**The point to land:** a student doesn't need a facilitator standing over their shoulder to make
real progress on a case. The scaffolding is real, not decorative.

---

## Part 3 — The guide side: what a facilitator gets (3 min)

**Screen:** open a case's `FACILITATOR.md` (e.g. `cases/catering/FACILITATOR.md`) — read it as a
formatted doc, or just scroll it in an editor.

Talking points:
- "Every case ships a full 45-minute Socratic discussion plan — timed moves, cold-call points, a
  'twist' dropped mid-discussion that forces students to recompute rather than just restate their
  first answer."
- Point at the **Deep Conflict threads** and **Socratic questions**. "These are written to have no
  clean answer — the goal isn't to get to a correct conclusion, it's to defend one under real
  pressure and know when new evidence should change your mind."
- Mention the **sensitivity note** convention. "Any case touching a genuinely serious real-world
  topic gets a one-line facilitator flag automatically — that's enforced structurally, not left to
  memory."

**The point to land:** the facilitator isn't building lesson plans from scratch. The pedagogy is
baked into the case itself.

---

## Part 4 — Operations: does the loop actually work? (7 min — the centerpiece)

This is the part to slow down on. Everything below is **real data**, not a mockup — two students
(Maya Whitfield, Ben Okafor) were actually assigned real cases, actually did the work, and it
actually went through scoring and guide review exactly the way a real cohort would use it.

**Screen:** `dashboard.html` → **Rubric & Scoring** tab.

- "Before touching any student work, here's the standard it's measured against — seven criteria,
  from 'did you find and use a real resource' to 'did you frame the question the right way.' Two
  outputs come out of every review: a strict pass/fail **mastery gate** for badge credit, and a
  separate **growth score** that tracks trajectory over time. They're never averaged together —
  that's deliberate. A student who barely clears every bar looks the same on the gate as one who's
  visibly improving, and the growth score is the only thing that shows the difference."
- Point at the **Live** banner — "2 score records on file, 3 guide overrides logged. This is real
  activity, not seed data."

**Screen:** switch to **Tracker** tab.

- "This is the actual home screen a facilitator uses day to day — not a dashboard, an exception
  queue. What needs a human's judgment right now. Right now it says nothing needs judgment, which
  is a real state, not an empty one — scroll down and you'll see two learners with real, completed
  case histories."
- Scroll to **Badge programs**. "Maya and Ben are each one case into a five-case badge. That
  number is computed live from real assignment records, not typed in."

**Now tell the two stories.** *(Have `student_work/UAT_LOG.md` open, or just narrate from memory —
the numbers below are real and traceable to `readmodel/submissions.json` and the `SCORE.md` files
in `student_work/`.)*

**Maya's story — the clean path:**
> "Maya was assigned the Catering case. She worked it for real — computed every deliverable,
> solved an actual equation for D5, took a firm position and defended it, included an original
> chart that wasn't just copy-pasted from the case's own data. The system auto-scored it against
> all seven criteria the moment it came in — that's the machine's first pass, not a final grade.
> The facilitator reviewed it, agreed with six of the seven, overrode one where the automated
> checker got confused by two very similarly-named numbers in the case data, logged *why* — that
> reasoning is saved permanently, it's literally training data for making the checker better — and
> confirmed it. Badge-eligible, growth score 76 out of 100, case marked complete."

**Ben's story — the real one, the revise loop:**
> "Ben's is more interesting, because it's the one that proves the *feedback* half of this works,
> not just the grading half. His first submission had every number right — but his actual
> recommendation was 'either option works, depends what you value.' That's a real, extremely
> common failure mode: computing correctly and concluding nothing. The system caught it
> automatically, high confidence, no override needed. The facilitator sent it back with a specific
> note — not 'try again,' but *here's the exact sentence that doesn't answer the question*. Ben
> resubmitted with an actual defended position. Growth score across those two submissions: 24.5,
> then 69.0. That trajectory — not a single grade — is the thing a facilitator actually coaches
> from."

**The point to land:** this isn't a scoring engine bolted onto content. It's a closed loop —
assign, work, submit, machine-first-pass, human judgment, feedback, revision, and the system
remembers the *reasoning* behind every human override so the machine gets better over time.

---

## Part 5 — What a student actually sees (2 min)

**Screen:** `student.html`.

- "This is a completely separate build — not the same page with things hidden by CSS, a genuinely
  different file with the facilitator's guide notes, the twist, the QA history, other students'
  data, and the growth score physically absent from what gets sent to the browser. A student
  opening dev tools finds nothing they shouldn't."
- Show **My Cases**, **My Progress** (badge rings, no numeric grade), **My Skills**, **How I'm
  Assessed** (the same rubric, in plain language, given to the student up front — nothing hidden
  about how they're judged).

**The point to land:** the growth score is a coaching tool for the adult, not a number handed to
the kid. That's a deliberate design choice, not an oversight — it's written into the rubric
itself.

---

## Closing — the honest version (2 min)

Say this part plainly. It's more convincing than pretending everything's finished.

> "What you just saw is real, not staged — real case content, a real rubric, a real scoring pass,
> a real human review with logged reasoning, a real revise cycle. What's still ahead of us is
> scale: more cases across more of the curriculum, a real cohort's first full run to calibrate the
> rubric's weights (it says so itself — it's versioned 'proposed' until that happens), and wiring
> up the Google Drive submission intake that's built but never been run against a live account.
> None of that changes the architecture. It's the same loop, more times."

---

## Anticipated questions

**"Is the scoring AI grading my kids?"**
No — it drafts. Every score is `machine-first-pass` and does not count toward anything until a
named human confirms it, and there's a hard rule in the code that a specific criterion (whether a
student reframed the question well) can *never* be marked at the top tier by the machine — only a
human can award that one.

**"What stops the machine from just being wrong a lot?"**
Every time a facilitator overrides the machine, the disagreement is logged with a reason — that's
not thrown away, it's the calibration data. If a specific criterion turns out to be wrong more
than about 30% of the time, the system is designed to stop guessing on it entirely and require a
human every time, automatically.

**"How much of this is really built vs. planned?"**
Point at the Pipeline tab. It shows the honest state of every case, live — not a status someone
typed in once and forgot to update.

**"What would it take to run this with a real class?"**
Real learners in the roster (minutes of setup), cases assigned, and the same loop you just watched
— nothing else has to be built to start.
