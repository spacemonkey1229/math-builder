# Facilitator Guide — College Admissions

MS | Heroes Academy | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric:** SAT Composite point gap between Tisha Ackerman and Harrison Carter, expressed
as a percent of the lower score · **Margin:** 2.7% — stable by construction (both scores are given
verbatim, not computed from any flexible assumption). See the Sensitivity note before Lessons
Learned for the case's *other*, genuinely unstable comparison (D5).

Legacy source: `source/Y1/Session 3/College Admissions/Guide Notes.docx` was **not present** in the
legacy folder (only the case study docx, an acceptance-letter PDF, and a stale 2019-2020 Common
Data Set PDF were provided) — see `case.json.legacy_conversion_note`. This guide is authored fresh
against the current 11-anchor ladder; there is no prior Guide Notes content to migrate or preserve,
and no pre-existing Lessons Learned to carry forward.

---

## Intro

Frame the format: this is a real decision structure (one open seat, two strong finalists) that
real admissions officers actually face every cycle. Don't open with the data. Open with the two
folders on the table and the question hanging in the room: "Who's it going to be?"

## Launch

Read the Overview aloud. Stop exactly where the case stops — Jack Ygarret's mouth open, no answer
yet. Do not hand out Appendices C and D until Anchor 1's vote is taken.

## Anchor 1 — TAKE A STAND AND VOTE

"Knowing nothing yet but that these are the two finalists — Tisha or Harrison — who are you
admitting?" Cold-call for a gut vote before any data is shown. Write the split on the board.

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to compare here?" Let the room articulate, in their own words, that
they need a way to weigh two different applicants against each other *and* against what Stanford's
own data says its admitted class looks like. If the room lands on "which one is more like a
typical Stanford student," that is close enough to Appendix A's purpose — name it and move on.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had to be fair to both applicants, what would we actually measure?" Push toward a concrete
list: test scores, GPA, class rank, and whatever Stanford itself publishes as a benchmark. This is
where Appendices A-D get handed out.

## Anchor 4 — WHAT DON'T WE KNOW?

"What's missing from these two files?" Let the room notice, ideally unprompted, that Harrison's
application never states his high school's size — while Tisha's does. Bank this; do not resolve it
yet. It is exactly what D5 and the Twist come back to.

## Data Deep Dive

Let Heroes work D1-D3 (the box-and-whisker plot, the scatter plot, and the 5-data-point table)
before anyone starts D4's SAT-gap computation or D5's percentile-to-raw-count conversion.

## Twist

**Drop this at roughly the 15-20 minute mark**, after the room has read "Tisha: 3rd percentile"
vs. "Harrison: 7th percentile" and (very likely) already treated Tisha's number as the clearly
stronger one.

> "One more thing. A class-rank percentile only tells you a *fraction* of the class — it doesn't
> tell you how many actual people that fraction represents. Tisha's school has more than 3,200
> students. Harrison's application doesn't say how big his school is at all. Before you compare
> '3rd percentile' to '7th percentile' as if they mean the same thing, figure out: how many
> classmates does each number actually put above Tisha and Harrison?"

**What this invalidates:** the comfortable read that a smaller percentile number is automatically
the stronger rank. It doesn't invalidate percentile rank as real information — it means percentile
rank alone, without a school size, is not yet a comparable number across two different schools.

**The follow-up (the whole point):** *"Once you convert both percentiles into an actual headcount,
does your ranking still hold? What did you have to assume to even get a headcount for Harrison,
and how much do you trust that assumption?"* Push the room to notice that Harrison's headcount
depends entirely on a national-average stand-in (Appendix B) — a real number, but not *his* real
number. This is the transferable skill: a normalized statistic (a percentile, a rate, a per-capita
figure) can silently hide the population it was computed against.

**Soundness check (SPEC.md §6 / case-write §11):**
*Sequential reading* — work through MA1 → MA2 → MA3 → MA4 in order. MA1 establishes the fictional
frame and the real data source. MA2 states the school-size substitution and flags it as sensitive.
MA3 flags the ranking-methodology gap. MA4 flags the median-as-midpoint simplification for D1's
box plot. None of these contradicts a later one — MA2's substitution is exactly what the Twist
asks students to interrogate, and MA3's methodology caveat sits alongside it without conflict.
*Simultaneous reading* — holding all four at once, D1-D4's arithmetic is entirely unaffected (none
of them touch class rank or school size); only D5's raw-count comparison is live, and it is live
under MA2 whether or not a student has consciously separated MA2 from MA3. No assumption is
invalidated by another, and the Twist adds a computational requirement, not a contradiction, to
either reading. Verified sound under both readings.

## Close (10 minutes left)

VOTE AGAIN. "Did the school-size headcount change your mind? If it didn't, say why not — a stable
answer under new information is a real, defensible answer, not automatically a mistake." Ask who
moved because of D4's SAT-gap computation versus who moved because of D5's headcount reveal — those
are two different kinds of reasoning shift and worth separating out loud.

## Lessons Learned

There is no single "correct" admit here, and that is the point: Jack Ygarret's real job requires
weighing GPA, test scores, class rank, and context against each other with no formula that
resolves the tie for him. The case's real payoff is narrower and more concrete: a percentile
number, by itself, is not a complete statistic — it always implicitly depends on the size of the
population it was measured against, and comparing two percentiles from two different-sized
populations without accounting for that is a common, plausible-sounding error.

## Standards Touched On

See `case.json.standards[]` and the case.md Appendix E "How To…" list — generated mechanically
from `readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. Tisha's class-rank percentile (3rd) is a smaller number than Harrison's (7th). Why doesn't that automatically mean fewer students academically outrank her?
2. You estimated roughly 96 students rank above Tisha at her 3,200-student school. What two numbers did you multiply to get that, and what would change if her school had half as many students?
3. Harrison's application never states his school's size. What did you use instead, where did that number come from, and how confident are you that it's close to his school's actual size?
4. D4 says Harrison's SAT Composite beats Tisha's by 2.7% of her score. Is that gap, by itself, a strong enough reason to admit Harrison over Tisha? What else in Appendices C and D would you want to weigh against it?
5. Stanford's published SAT Composite middle-50% range is 1,510-1,570. Tisha's score (1,480) sits below that range entirely. Does that automatically disqualify her application? What in her file might the committee weigh against a below-range test score?

## The trap, named explicitly

A Hero reads "Tisha: 3rd percentile" and "Harrison: 7th percentile" and concludes Tisha's class
rank is unambiguously the stronger credential, because 3 is a smaller number than 7. This is the
plausible reasoning that produces a confident, incomplete answer: a percentile rank is only
meaningful relative to the size of the class it was measured in, and the case never states
Harrison's school size at all. A Hero who works D5 correctly has to notice this gap, choose a
real, sourced stand-in for the missing number (Appendix B), and recompute both applicants'
estimated raw headcount before the percentile comparison actually means what it appears to mean.
Facilitators should let the room commit to "3rd beats 7th, obviously" out loud in Anchor 4 before
the Twist and D5 complicate it — that reversal, or non-reversal depending on the numbers a student
lands on, is the case's real payoff.

## Sensitivity note

A college-admissions decision case. Real financial-aid and income-bracket data appear in both
applicants' own files (Appendix C, D) exactly as the original applicants reported them — facilitators
should treat these as ordinary background context, the same way a case would treat any other
applicant-reported demographic field, not as a topic requiring special framing. No
illness/death/acute-hardship content requiring a SPEC.md §6 flag beyond that.

**Assumption-sensitivity disclosure (required reading before you run D5):** D5's raw-count-above
comparison depends on MA2's national-average school-size substitution for Harrison
(`cases/college-admissions/sensitivity_model.py`, Tier 2 probe 5). Flexing that assumed enrollment
figure by ±50% changes Harrison's estimated headcount substantially — roughly a 3x range across
the swept values — but does NOT change the *direction* of the comparison anywhere in that range:
Harrison's estimated headcount-above stays lower than Tisha's fixed ~96 at every flex point tested.
That directional robustness is real and worth naming to a room that reaches D5. It is not,
however, a reason to treat the exact number as solid: Harrison's application simply does not
report his school's size, so any number used in its place is a real assumption, not a fact, and
D5's conclusion should be presented to students as a reasoned estimate whose *direction* is
fairly robust but whose *exact size* is not verified. The case's *graded* primary metric (D4's
SAT-gap percentage) does not depend on this assumption at all and is stable by construction,
since both SAT scores are given directly in the applicants' own files.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read aloud), gut-vote before any data (Anchor 1) |
| 3:00-10:00 | Define the real question and a fair process (Anchors 2-3); hand out Appendices A-D |
| 10:00-15:00 | Data Deep Dive: D1 (box-and-whisker), D2 (scatter plot), D3 (data table) in progress; surface the missing-school-size gap (Anchor 4) |
| **15:00-20:00** | **DROP THE TWIST** — delivered slowly, with the follow-up question |
| 20:00-30:00 | D4 (SAT-gap %) and D5 (headcount estimate) worked; compare which deliverable moved each Hero's position |
| 30:00-40:00 | Threaded conflict: GPA/rank (favors Tisha) vs. test scores (favors Harrison) vs. the headcount reveal's real uncertainty |
| 40:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands
declared per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
