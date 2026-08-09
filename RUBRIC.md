# RUBRIC — Evaluating Hero Work on a Case Study

**Version:** 1.1 · **Status:** PROPOSED — needs one real cohort before it locks
**2026-08-01 delta:** C1 amended for MCS-39 (every case now ships a built-in hover+hyperlink math glossary) — see the note under C1 and `score_submission.py`'s `_c1()`.
**Applies to:** every case study submission, legacy or pipeline-authored
**Enforced by:** `submission-score` (machine first pass) → guide confirms or overrides

---

## The two outputs, and why there are two

This rubric produces **two independent things from one review.** They are not the same and must never be averaged together.

**1. The mastery gate — does this case count toward a badge?**
Per criterion: **Exemplary / Proficient / Not Yet**. A case counts toward a badge only when **every criterion is at least Proficient**. There is no partial credit, no compensation, no "three Exemplaries cover one Not Yet." Five cases at Proficient earn the badge; four cases and a Not Yet earn nothing yet.

**2. The growth score — is this Hero getting better?**
A 0–100 composite, tracked over time on the dashboard, **never shown as a grade and never used for badge eligibility.** It exists so a guide can see that a learner went 61 → 68 → 74 across three cases, which the mastery gate cannot show because all three might read "Proficient."

> **Why both.** Mastery gates are honest about readiness but blind to trajectory — a Hero who barely clears Proficient five times looks identical to one who is visibly compounding. Scores show trajectory but corrupt motivation the moment they become the point. Separating them keeps the badge clean and the coaching informed. **If a learner ever asks "what's my score," the answer is that it's a tool for their guide, and the number that matters is which criteria are still Not Yet.**

---

## The seven criteria

Criteria 1–5 come directly from the five Challenges. Criterion 6 is the Socratic discussion. Criterion 7 is the one that distinguishes a case study from a worksheet.

### C1 · Research — the "how to" resource
*Challenge 1. Weight 5.*

| | |
|---|---|
| **Not Yet** | No resource posted, or a resource unrelated to any "how to…" question in the case's Appendix G. Also Not Yet if the only evidence of "research" is reposting a link the case's own interactive HTML already handed the Hero (see note below) with no sign of independent use. |
| **Proficient** | A working link to a resource that teaches one of the case's named "how to…" skills, **found and applied by the Hero** — not merely cited back from the case's own glossary. |
| **Exemplary** | The resource addresses a skill the Hero genuinely did not have, and the write-up shows it being *learned* — a false start, a correction, a "I thought X, then found Y." |

> **MCS-39 note (added 2026-08-01).** Every case now ships a built-in hover+hyperlink glossary in its interactive HTML that already answers the exact "how to…" questions this Challenge asks the Hero to research independently (`DOCTRINE_LEDGER.md` MCS-39). That glossary is authoring-side scaffolding — it exists so a Hero can understand vocabulary *while working the case*, not so Challenge 1 can be satisfied by clicking through and reposting the same URL. A Challenge 1 submission whose link is byte-identical to one already embedded in the case's own glossary is not automatically Not Yet, but it does not on its own demonstrate research — it demonstrates that the Hero found the case's own built-in help. `submission-score`'s `_c1()` flags this case (LOW confidence, explicit note) rather than silently awarding Proficient; the guide makes the actual call, same as any other LOW-confidence C1 verdict.

### C2 · The pitch — a firm stance, defended
*Challenge 2. Weight 20.*

| | |
|---|---|
| **Not Yet** | Under 250 words, or no clear position, or a position that hedges both ways ("both options are good"). |
| **Proficient** | 250+ words. Takes one side unambiguously. Uses the researched how-to in an actual calculation. Reasoning follows from the numbers rather than sitting beside them. |
| **Exemplary** | Names the strongest argument *against* their own position and answers it. States what would change their mind. Distinguishes what the data shows from what they assumed. |

> **The single most common failure mode is a pitch that computes correctly and concludes nothing.** Numbers on the page, no argument. That is Not Yet on C2 even if every calculation is right — C3 covers correctness.

### C3 · Mathematical correctness
*Underlies Challenge 3. Weight 20.*

| | |
|---|---|
| **Not Yet** | An error that changes the conclusion. Or units dropped or mismatched in a way that matters. Or a number used that appears nowhere in the case and is not declared as the Hero's own assumption. |
| **Proficient** | Arithmetic and unit conversions correct. Any error present is arithmetic-local and does not change the decision. Figures traceable to a named appendix. |
| **Exemplary** | Correct, *and* the Hero checks their own work visibly — an order-of-magnitude sanity check, a second method, a "this can't be right because…" that catches something. |

### C4 · Required deliverables
*Challenge 3. Weight 15.*

Each case names its own deliverables (Cold Chain has D1–D6). Scored against that list.

| | |
|---|---|
| **Not Yet** | Any required deliverable missing or attempted without the underlying computation. |
| **Proficient** | All deliverables present, in a form a reader can actually use — a schedule that could be handed to a driver, a cost breakdown that adds up. |
| **Exemplary** | A deliverable goes beyond the ask in a way that serves the argument, not in a way that pads it. |

### C5 · Visual display and appendix of work
*Challenges 2 and 4. Weight 15.*

| | |
|---|---|
| **Not Yet** | No original visual, or a visual copied from the case's own appendices, or an appendix with no evidence of process. |
| **Proficient** | At least one **original** visual that displays the Hero's own data and supports the position. Appendix shows real working — notes, screenshots, dead ends, calculations. |
| **Exemplary** | The visual makes the argument by itself — someone could look at it alone and understand the case for this position. Appendix shows the reasoning *changing*. |

> "Original" means the Hero built it. Re-typing Appendix A into a table is not a visual display. A chart of *their* computed SA:V against cold life is.

### C6 · Socratic participation
*Challenge 5. Weight 15.*

| | |
|---|---|
| **Not Yet** | Fewer than two contributions, and no 500-word substitute if absent. |
| **Proficient** | Two or more substantive contributions. At least one engages another Hero's reasoning rather than restating their own. |
| **Exemplary** | Changes position under new evidence and says why — or holds position under pressure and says why the pressure did not move them. Asks a question that redirects the room. |

> **Changing your mind for a stated reason scores as high as defending well.** This is deliberate and should be said out loud to learners. The Twist exists to make this possible.

### C7 · Framing the question
*Not from any Challenge. Weight 10.*

The distinguishing criterion. Anchor 2 of the Socratic ladder asks *"what is the problem we're solving?"* — this criterion asks whether the Hero ever noticed that the question was theirs to choose.

| | |
|---|---|
| **Not Yet** | Accepts the most obvious metric without comment. Optimizes something the case never asked them to optimize, unaware. |
| **Proficient** | States the metric they optimized and why that metric. Acknowledges that a different metric would give a different answer. |
| **Exemplary** | Works the case under two metrics and shows where they diverge. Or argues that the obvious metric is the wrong one, and carries it. |

---

## Scoring

**Mastery gate:** `badge_eligible = all(criterion >= Proficient)`. Nothing else enters it.

**Growth score:** Not Yet = 0, Proficient = 70, Exemplary = 100, weighted:

| C1 | C2 | C3 | C4 | C5 | C6 | C7 |
|---|---|---|---|---|---|---|
| 5 | 20 | 20 | 15 | 15 | 15 | 10 |

All-Proficient scores 70. All-Exemplary scores 100. One Not Yet on C2 caps the score at 80 *and* blocks the badge.

**Tier adjustment.** T4 (HS) work is held to T4 standards; a T1 case scored as if it were T4 is a misuse of this rubric. The machine pass reads `tier` from `case.json` and applies the tier-specific notes below. It does **not** scale the score — a Proficient T1 and a Proficient T4 both score 70, because the score tracks *this Hero's growth*, not cross-tier comparison.

| Tier | What Proficient additionally requires |
|---|---|
| T1 | — |
| T2 | The trade-off between the two competing variables is named explicitly |
| T3 | Some case data is correctly identified as irrelevant and set aside |
| T4 | At least one assumption stated, justified, and its sensitivity tested |

---

## Peer and self review

Every submission carries two lightweight reviews before the guide sees it. Neither sets the verdict; both are visible to the guide and to the Hero.

**Self-review** — three questions, answered before submitting:
1. Which criterion is your work weakest on, and why?
2. What is the strongest argument against your position?
3. What did you have to look up?

**Peer review** — one other Hero, three questions:
1. Could you follow the argument without re-reading? Where did you get lost?
2. Does the visual actually support the position, or is it decoration?
3. What would you press them on in discussion?

> Peer review is **not** scoring. It is rehearsal for the Socratic discussion, and it is the cheapest way to raise C2 and C5 across a cohort. A Hero who has been asked "where did you get lost?" once writes differently the next time.

---

## How the machine pass works, and what it must not do

`submission-score` produces a **complete first-pass verdict on all seven criteria** so that a guide reviewing twenty submissions starts from a filled-in form, not a blank one. That is the point — this has to scale.

**What it can actually see:**

| Signal | Criteria it informs |
|---|---|
| Word count, position-statement detection | C2 |
| Recomputation of every number against `case.json` appendix data | C3 |
| Deliverable checklist from `case.json.deliverables[]` | C4 |
| Image/chart presence; whether the visual's data appears in the case appendices verbatim (copied) or is derived (original) | C5 |
| Discussion contribution count and reply-depth from `submissions.json` | C6 |
| Link resolution and match against Appendix G labels; whether the link is byte-identical to a URL already embedded in the case's own MCS-39 glossary | C1 |

**What it is guessing at:** C7 entirely, the Exemplary band on C2 and C6, and any judgment about whether reasoning is *sound* rather than merely *present*. Every criterion in the machine verdict carries a **confidence flag**, and anything at LOW confidence is surfaced to the guide first, not buried.

**Three hard limits.**

1. **A machine BLOCKER on C3 is advisory, not final.** If recomputation disagrees with the Hero, the Hero may be right and the check may be wrong — especially where the Hero declared their own assumption. The guide adjudicates.
2. **The machine may never mark C7 Exemplary.** Recognizing that someone reframed the question well requires reading an argument, not scanning one.
3. **A verdict is `machine-first-pass` until a guide confirms it.** Unconfirmed verdicts do not count toward a badge and render as INTERIM on the dashboard. Machine drafts, human promotes — same rule as everywhere else in this system.

---

## Open questions before this locks

- **C1 and MCS-39 haven't been tested against a real submission yet.** The glossary-URL flag in `_c1()` is a mechanical string match (byte-identical URL), not a judgment about whether the Hero actually used the resource independently. Watch the first cohort: if most Heroes cite the case's own glossary link and that turns out fine in practice (they still show independent use in Challenge 2a), this flag should soften to a note rather than a confidence downgrade.
- **Weights are asserted, not calibrated.** They encode a judgment that argument (C2) and correctness (C3) matter twice as much as the research link (C1). Defensible, untested. One cohort of real submissions should either confirm or move them.
- **C7 has no legacy precedent.** None of the 39 Guide Notes score it and no student exemplar was written knowing it existed. It may be too hard at T1–T2. Watch the first cohort's distribution; if nearly everyone lands Not Yet, the criterion is wrong, not the Heroes.
- **Discussion scoring depends on data nobody currently records.** C6 needs contribution counts per Hero per case. Today that lives in a guide's memory. The tracker has the schema; the habit does not exist yet.
- **No inter-rater check.** Two guides scoring the same submission should agree. Until that has been tested once, treat every Exemplary as a guide's opinion rather than a system verdict.
