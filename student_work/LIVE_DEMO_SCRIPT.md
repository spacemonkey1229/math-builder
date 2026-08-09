# Live Demo Script — the full loop, hands-on, on the real product

**What this is, and how it's different from `DEMO_SCRIPT.md`:** that script narrates *existing*
data (Maya and Ben's real, already-completed case histories) to a director as a pitch, opening
local files. **This** script actually *performs* the full lifecycle live, on the real hosted admin
app, in front of whoever's watching — add a student, assign work, do the work, submit it, score it,
review it, log discussions, complete it, assign a second case, and remove a student — end to end,
nothing pre-staged except the two things that were already true before you start:

- **Live admin app:** https://math-builder-three.vercel.app (needs your passcode)
- **Real history already on it:** Maya Whitfield and Ben Okafor, both with a completed case, a
  confirmed score, and a growth trajectory — untouched by anything in this script, and worth
  pointing at once near the end as "this isn't day one, there's already a real cohort's worth of
  history in here."

**One honest scope note, worth saying out loud if anyone asks:** the admin/tracking side (this
script's whole point) is live on the internet. The actual case a student *works* — the interactive
HTML page with the Working Notebook, the glossary, the deliverables checklist — is **not** hosted
yet; you open it as a local file, same as it's always been. That's a deliberate, current scope
line, not an oversight — say so if it comes up (see "Anticipated questions" at the end).

**Total time:** ~20 minutes for the full loop. Trim the "do the work" section if you're short on
time — see the note there.

**Before you start:** open two things —
1. A browser tab to the live admin app, logged in.
2. `cases/archery-camp/published/Archery Camp - Interactive.html`, opened locally (double-click, or
   drag into a browser tab) but **not loaded yet** — you'll open it live during Part 3.

---

## Opening (1 min)

> "Everything I'm about to do is real — no seed data, no mockup. I'm going to add a student from
> scratch, assign her a real case, actually do a piece of the work as if I were her, submit it,
> score it, review it, and mark it complete — the same loop a facilitator runs for real, on the
> actual live app, not a local file on my laptop."

---

## Part 1 — Admin: add a student (2 min)

**Screen:** the live admin app, **Learners** tab.

- Point at the **Add a learner** card. "One student at a time — name, program, cohort." Type a
  name (e.g. **"Priya Shah"**), pick a program, click **Add learner**. It appears in the list
  immediately below.
- Then point at **Upload a class (CSV)** right under it. "But a facilitator getting a new cohort
  isn't adding one student — it's adding a class list." Click **Download CSV template** to show
  the expected columns, then upload a small CSV (2-3 rows, one deliberately wrong — e.g. a
  misspelled program name) to show the **per-row result**: which rows were added, which were
  skipped, and *why* — never a silent all-or-nothing.

**The point to land:** managing a roster doesn't require anyone hand-editing a JSON file or asking
an engineer — this is genuinely self-serve.

---

## Part 2 — Guide: assign a case (2 min)

**Screen:** **Assign a Case** tab.

- Pick **Priya Shah** as the learner, **Archery Camp** as the case. Point at the case dropdown:
  "Only cases that have passed the publish gate show up here — the same rule the system enforces
  everywhere, not just a UI suggestion." Set a due date if you like. Click **Assign**.
- Flip to **Learners**, find Priya's card (click to expand) — the assignment now shows
  `archery-camp · assigned`.

**The point to land:** assigning work is one click, and it's impossible to assign a case that
hasn't actually cleared quality review.

---

## Part 3 — Student: do a slice of the actual work (5 min, or skip to 1 min — see below)

**Screen:** switch to the local `Archery Camp - Interactive.html` tab.

> "This is what Priya would actually see and use — nothing about this is admin-only or hidden."

- Scroll **Overview → Background → Dilemma**: Karen Dobson has to pick between two field
  combinations for a summer archery camp — real prices, real per-counselor costs, a hard $110/head
  ceiling the board set. Two genuinely defensible options, not a rigged choice.
- Open the **Working Notebook**, pick a couple of the six deliverables (e.g. D1 — total ranges and
  max capacity; D3 — total cost and per-participant charge), type in real numbers, hit **Check**.
  Show a wrong answer getting caught, then a right one passing.
- Hover a glossary term, click through to its linked outside lesson — "every term is
  hoverable, every link real and checked."

**If short on time:** skip straight to "she did the work" and move to Part 4 — the point (a real
calculator, not an answer key, with real scaffolding) is made in under a minute of scrolling even
without solving anything.

**For Part 4, you'll need something to actually upload as "her submission."** Fastest path: save a
short markdown or text file right now with 2-3 sentences taking a real position — e.g. *"I recommend
option A because it holds more archers per dollar of counselor pay even though the per-head cost is
slightly higher — the board's $110 ceiling still holds, and it leaves the most room to grow toward
150."* That's genuinely enough content for the machine scorer to have something real to read.

---

## Part 4 — Guide: record the submission, run the scorer, review, confirm (4 min)

**Screen:** back to the live admin app, **Learners** → Priya's card, now showing
`archery-camp · assigned`.

- **Record a submission**: click **Upload**, pick the file you just saved (this really uploads to
  the live database — say so). Paste that same path into the Challenge 2 pitch field. Click
  **Record submission** — status flips to `submitted`.
- **Run the machine first pass**: paste the same file path into "File path(s) to score," click
  **Score it**. A real subprocess runs against the real case rubric and comes back with a
  criterion-by-criterion first pass in a few seconds — likely mostly "Not Yet," since this is a
  quick, incomplete demo submission, and that's the honest, correct result, not a bug.

  > "This is the important part to say plainly: that's a *draft*, not a grade. Nothing here counts
  > toward anything until a named human confirms it."

- **Guide confirm**: type a name, click **Confirm** — status flips to `confirmed`. If you want to
  show the override mechanism, pick one criterion, set it to a different level, type a one-line
  reason, and confirm — point out that reason is saved permanently as calibration data, not
  discarded.
- **Set review outcome**: pick **accepted** (or **revise**, to show the other path — a genuinely
  common real case: right math, no real position taken), write a specific note, **Save review**.

**The point to land:** every step where a human's judgment matters, a human's judgment is
literally required — nothing here silently promotes itself.

---

## Part 5 — Guide: discussion, complete, see the tracker update (3 min)

**Screen:** still on Priya's card.

- **Log participation** twice (Challenge 5 requires two logged discussions before a case can
  close) — pick a mode, add a short note each time, click **Log participation** twice.
- Once 2/2 discussions and an `accepted` outcome are both true, **Mark complete** appears — set a
  badge slot, click it. Status flips to `complete`.
- Flip to **Exception Queue**: Priya briefly appeared there earlier (e.g. "AWAITING REVIEW") and
  is now either gone or showing progress toward her next badge slot — "this is the facilitator's
  actual home screen, not a report someone has to remember to check."
- Flip to **Badges**: Priya now shows real progress (e.g. 1/5 cases toward her first badge).

**The point to land:** nothing on this screen is typed in by hand — every number is computed live
from the actions you just took.

---

## Part 6 — Guide: assign a second case (1 min)

**Screen:** **Assign a Case** tab again.

- Assign Priya a *different* published case (e.g. **Catering** or **House Plans**). "This is the
  actual day-to-day loop — a facilitator doesn't do this once, they do it every time a case closes.
  Nothing about the second assignment is different or special-cased."

---

## Part 7 — Admin: remove a student (2 min)

**Screen:** **Learners** tab, Priya's card.

- Point at **Set status: active / paused / alumni** first: "This is the right button 95% of the
  time — a student pausing or leaving the program keeps their entire history intact. Use this."
- Then point at **Delete learner (permanent)**, styled deliberately differently (red, its own
  warning line above it). Click it — show the confirmation dialog, which names exactly what gets
  destroyed (this learner, plus every assignment/submission/discussion/score tied to them) and
  explicitly tells you to use Set status instead if this is a real departure.
- Confirm. Show the result message: *"Deleted Priya Shah — removed 2 assignment(s), 1
  submission(s), 2 discussion(s), 1 score row(s)."* — an exact accounting, not a silent wipe.

**The point to land:** deletion exists, but it's clearly the unusual path — for fixing a mistake
(a duplicate, a test account, exactly what you just created for this demo), not for a real student
leaving. Say that distinction out loud; it's a deliberate design choice, not a missing feature.

---

## Closing — point at what's already real (2 min)

**Screen:** Learners tab, scroll to Maya Whitfield and Ben Okafor.

> "Everything you just watched me do from scratch — Maya and Ben already have. Real cases, real
> submissions, a real revise-and-resubmit cycle for Ben, confirmed scores, real growth
> trajectories. What I just built in front of you isn't a demo track separate from the real
> product — it's the same loop, and it's already been run for real, twice, before today."

Click into Maya's or Ben's card, show their `confirmed` scores and growth numbers as the payoff.

---

## Anticipated questions

**"Is any of what I just watched fake or seeded?"**
No — everything in this script was created live, in front of you, on the real hosted database.
The only pre-existing data is Maya and Ben's, and that's real too (see `DEMO_SCRIPT.md` for their
full story).

**"Why isn't the student-facing case page hosted too?"**
Scope, not oversight. The admin/tracking side needed to be reachable from anywhere — that's what
today's build was for. The student-facing interactive case is still a local file for now; putting
it online is a clean, separate next step, not a redesign.

**"What stops someone from deleting a real student by accident?"**
The confirmation dialog names exactly what's about to be destroyed, and the UI puts "Set status"
front and center as the normal path with an explicit note pointing there first. It's also
snapshotted before every write, so nothing is unrecoverable at the data layer even if the UI is
bypassed.

**"Who else can get into this?"**
Right now, one shared passcode — deliberately simple to get a live demo working fast, with a real
login system as the named next step, not a permanent decision.
