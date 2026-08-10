# Lifecycle Script — Admin → Guide → Student → Guide, live on the real product

**What this is:** one script, organized by *who does what*, not by feature tab. The core loop
this product exists to run has exactly four beats, and the guide shows up twice — once to match a
student to the right challenge, once to close the loop after they've done it:

1. **ADMIN** — manages the class (who's enrolled, which cohort, which program).
2. **GUIDE** — matches the context and challenge to the student (assigns the right case).
3. **STUDENT** — learns and does the work (the actual case, the actual math).
4. **GUIDE** — checks for mastery, gives feedback, and assigns the next challenge — which loops
   back to step 2. This is the whole product. Everything else (the curriculum map, the rubric
   library, the tracker) exists to make these four beats possible and honest, not to replace them.

This is the same live loop `LIVE_DEMO_SCRIPT.md` performs, restructured so the role changing hands
is the thing you narrate, not an implementation detail. Use whichever script format fits the
room — this one if the audience needs to *see themselves* in a specific role; `LIVE_DEMO_SCRIPT.md`
if a flat step-by-step is easier to follow along with; `DEMO_SCRIPT.md` if there's no live app
access and you're narrating Maya/Ben's existing history from local files instead.

- **Live admin app:** https://math-builder-three.vercel.app (needs your passcode)
- **Real history already on it:** Maya Whitfield and Ben Okafor, both with a completed case, a
  confirmed score, and a growth trajectory — untouched by anything in this script.

**One honest scope note:** the ADMIN/GUIDE side (roster, assign, score, confirm, tracker) is live
on the internet. The actual case a STUDENT works — the interactive HTML page — is not hosted yet;
open it as a local file, same as it's always been. Say so if it comes up.

**Total time:** ~20 minutes for the full loop.

**Before you start:** open two things —
1. A browser tab to the live admin app, logged in.
2. `cases/archery-camp/published/Archery Camp - Interactive.html`, opened locally (double-click,
   or drag into a browser tab) but **not loaded yet** — that's Beat 3.

---

## Opening (1 min)

> "This product has exactly one job: help a guide match a student to the right challenge, let the
> student do real work on it, and give the guide an honest read on whether they actually mastered
> it — then do it again with the next challenge. I'm going to run that loop from scratch, live, in
> front of you. No seed data, no mockup."

---

## Beat 1 — ADMIN: manage the class (2 min)

**Role:** the person running the program day to day — not necessarily the same person as the
guide who'll show up in Beats 2 and 4, though on a small program it often is.

**Screen:** the live admin app, **Learners** tab.

- Point at **Add a learner**: "One student at a time — name, program, cohort." Type a name (e.g.
  **"Priya Shah"**), pick a program, click **Add learner**. It appears in the list immediately.
- Point at **Upload a class (CSV)** right under it: "But onboarding a new cohort isn't adding one
  student — it's a class list." Click **Download CSV template**, then upload a small CSV (2-3
  rows, one deliberately wrong — e.g. a misspelled program name). Show the **per-row result**:
  which rows were added, which were skipped, and *why* — never a silent all-or-nothing.

**The point to land:** class management doesn't require anyone hand-editing a JSON file or
paging an engineer. This beat has nothing to do with any *specific* student's learning — it's
pure roster administration, and it's the only beat where that's true.

---

## Beat 2 — GUIDE: match the context and the challenge (2 min)

**Role:** now switch hats — the person deciding *what this specific student should work on next*,
which is a pedagogical judgment, not an admin task, even though it happens in the same app.

**Screen:** **Assign a Case** tab.

- Pick **Priya Shah**, then the case dropdown. Before picking, say why the dropdown itself
  enforces something: "Only cases that have passed the publish gate show up here — the same rule
  the system enforces everywhere, not a UI suggestion. Nothing half-baked reaches a student."
- Pick **Archery Camp** — a real, defensible two-sided decision (which field combination fits a
  hard per-head cost ceiling). Set a due date if you like. Click **Assign**.
- Flip to **Learners**, expand Priya's card — the assignment now shows `archery-camp · assigned`.

**The point to land:** matching context to challenge is a real judgment call — tier, band, and
which skill gap this student needs closed — not a random draw from the corpus. The system's only
job here is to make sure whatever the guide picks has actually earned the right to be assigned.

---

## Beat 3 — STUDENT: learn and do the work (5 min, or 1 min if short on time)

**Role:** now switch again — this is what Priya would actually see and use. Nothing about it is
admin-only or hidden from her.

**Screen:** the local `Archery Camp - Interactive.html` tab.

- Scroll **Overview → Background → Dilemma**: a real decision, real prices, a hard $110/head
  ceiling — two genuinely defensible sides, not a rigged choice.
- Open the **Working Notebook**, pick a deliverable, type a wrong number first, hit **Check** —
  it says `try again`, nothing more. It does **not** hand over the correct answer; that's a
  calculator, not an answer key. Then type the right number and show it pass.
- Hover a glossary term, click through to its linked outside lesson.

**If short on time:** skip straight to "she did the work" and move to Beat 4 — the point (a real
calculator with real scaffolding, not decoration) lands in under a minute of scrolling even
without solving anything.

**For Beat 4, save something to upload as "her submission."** Fastest path: a short text file
with 2-3 sentences taking a real position, e.g. *"I recommend option A because it holds more
archers per dollar of counselor pay even though the per-head cost is slightly higher — the
board's $110 ceiling still holds, and it leaves the most room to grow toward 150."*

---

## Beat 4 — GUIDE: check for mastery, give feedback, assign next (5 min)

**Role:** back to the guide — but a different act than Beat 2. Beat 2 was *choosing*; this beat is
*judging*, and then choosing again to close the loop.

**Screen:** the live admin app, **Learners** → Priya's card, now `archery-camp · assigned`.

- **Record the submission:** upload the file you just saved, paste its path into the pitch field,
  click **Record submission** — status flips to `submitted`.
- **Run the machine first pass:** paste the same path into "File path(s) to score," click
  **Score it**. A real subprocess scores it against the real rubric in seconds — likely mostly
  "Not Yet" for a quick demo submission, and that's the honest result, not a bug.
  > "Say this plainly: that's a *draft*, not a grade. Nothing counts until a named human confirms
  > it."
- **Guide confirm — the mastery check:** type a name, click **Confirm**. To show the override
  mechanism, pick one criterion the machine got wrong, set the real level, type a one-line reason,
  confirm — that reason is saved permanently as calibration data, not discarded.
- **Feedback — the review outcome:** pick **accepted** (or **revise** — a genuinely common real
  case: right math, no real position taken), write a specific note, **Save review**.
- **Log participation** twice (the case requires two logged discussions before it can close), then
  **Mark complete** with a badge slot once outcome is `accepted` and 2/2 discussions are logged.
- **Close the loop — assign next:** flip back to **Assign a Case** and give Priya a *different*
  published case. This is Beat 2 again, for real — the guide is back to matching context and
  challenge, this time informed by what Beat 4 just showed about where she is.

**The point to land:** every step where a human's judgment matters — was the math right, was the
argument defended, what should she work on next — a human's judgment is literally required.
Nothing here silently promotes itself, and the loop doesn't end at "graded" — it ends back at
"assigned," because that's what actually happens with a real student.

---

## Closing — this loop has already run for real, twice (2 min)

**Screen:** Learners tab, Maya Whitfield and Ben Okafor.

> "Everything you just watched — admin enrolls, guide assigns, student works, guide checks and
> reassigns — Maya and Ben have already been through it for real. Maya's was the clean path:
> assigned, worked, confirmed, badge-eligible. Ben's is the more interesting one: his first
> submission computed everything right but took no real position — the guide caught it, sent it
> back with a specific note, and his growth score moved from 24.5 to 69.0 across the revise cycle.
> That's the loop working exactly as designed, not a demo track separate from the real product."

Click into Maya's or Ben's card to show the confirmed scores and growth numbers.

---

## Cleanup

Delete the demo learner(s) you created (Priya Shah, and any CSV rows) via **Delete learner
(permanent)** on the Learners tab — the confirmation names exactly what gets removed. Confirm via
a fresh look at the Learners tab that only real students remain.

---

## Anticipated questions

**"Why does the guide show up twice in your diagram?"**
Because assigning and evaluating are different acts that happen to use the same login. Assigning
is a forward-looking judgment (what does this student need next); evaluating is a backward-looking
one (did they actually get it). Conflating them is how "assign once, never revisit" programs
happen.

**"Is any of what I just watched fake or seeded?"**
No — everything in Beats 1-4 was created live, on the real hosted database. The only pre-existing
data is Maya and Ben's, and that's real too.

**"What stops the machine from just being wrong a lot?"**
Every override is logged with a reason — that's the calibration data. A criterion wrong more than
~30% of the time gets demoted to guide-only automatically, not left silently anchoring the guide.

**"Why isn't the student-facing case page hosted too?"**
Scope, not oversight — the admin/guide side needed to be reachable from anywhere; the case page
is still a local file for now. A clean next step, not a redesign.

**"What would it take to run this with a real class?"**
Real learners in the roster (minutes of setup via Beat 1), cases assigned (Beat 2), and the same
loop you just watched. Nothing else has to be built to start.
