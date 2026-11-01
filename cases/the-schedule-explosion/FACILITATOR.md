# FACILITATOR.md — The Schedule Explosion

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the end of case.md.*

**Case:** The Schedule Explosion · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** MS Adventure
**Standards:** Advanced Operations — Factorial, and the how-to for evaluating a factorial expression
(see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-09). All `{{NEEDS_SOURCE}}` placeholders in `case.md`
are resolved: two real, cited computer-science/industry facts (the n! feasible-orderings rule from
Cornell's Optimization Wiki, and real 2026 Nvidia/AWS GPU-fleet growth for scale-grounding), one real
benchmarked range (AWS's own model-loading timing data) that grounds a Modeling Assumption, one
definitional citation (nearest-neighbor as a standard heuristic), and three explicit Modeling
Assumptions (the switchover-cost matrix, the assumed schedule-search evaluation rate, and the
nightly batch window). `case.json.balance.margin_pct` is a real, computed **13.9%** on the six-job
graded batch. Everything below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary workplace stakes only (a team lead's headcount tied to a
utilization target) — no illness, death, or family hardship.

## Argument for A — The Full Sweep

On the ONE batch size small enough to actually check exhaustively — Vantage's real six-job pilot
batch — The Full Sweep is provably, calculably better: its true-optimal ordering (LLM Fine-Tune →
Diffusion Model → Vision Transformer → Speech Model → Anomaly Detector → Recommender) wastes only
**62 minutes** of idle switchover time, verified by checking all 6! = 720 possible orderings. The
Greedy Queue's nearest-neighbor ordering (LLM Fine-Tune → Vision Transformer → Recommender →
Diffusion Model → Anomaly Detector → Speech Model) wastes **72 minutes** on the exact same six jobs
— a real, computed 10-minute, 13.9% gap. This is not an approximation or a guess; it is the
mathematically best possible answer for that batch. **If Vantage only ever ran six-job batches,
there would be no real argument for anything else.**

## Argument for B — The Greedy Queue

Appendix B's own numbers are the whole argument: Vantage's *typical* nightly batch is already 12
jobs — twice the size of the pilot batch — heading toward 18-20 within the year as the fleet grows
(real, publicly announced Nvidia/AWS GPU-fleet growth, Appendix E). At 12 jobs, The Full Sweep's
exhaustive search still finishes in about 48 seconds. At 15 jobs, it takes about 36.3 hours — already
more than four times Vantage's own 8-hour nightly window. At 18 jobs, about 20.3 years. At 20 jobs,
about 7,709 years. **A strategy that cannot finish computing an answer some nights is not a real
strategy for those nights, no matter how good its answer is on nights small enough for it to
finish.** B's case is not "The Full Sweep gives a worse answer" — on the pilot batch it gives a
provably *better* one — it is "The Full Sweep gives no answer at all, most nights that actually
matter."

## The margin — real numbers, and why six jobs, not Vantage's real batch size

`case.json.balance.margin_pct` = **13.9%**, inside the SPEC §2 target 8-15% band. The arithmetic, in
full (both computed by `sensitivity_model.py`'s exhaustive search and nearest-neighbor simulation
over Appendix A's switchover-cost matrix):

- **The Full Sweep (A), six-job pilot batch:** true optimum over all 720 orderings — **62 minutes**.
- **The Greedy Queue (B), six-job pilot batch:** nearest-neighbor from LLM Fine-Tune — **72 minutes**.
- **Margin:** |72 − 62| / 72 = 10 / 72 = **13.9%**.

**Why the graded comparison is the six-job pilot batch, not Vantage's real 12-to-20-job nightly
batch — say this out loud to a Hero who asks:** at realistic batch sizes, The Full Sweep cannot be
run to completion at all inside the nightly window (D2's own feasibility-crossing arithmetic: n=12
still fits at ~48 seconds, but n=15 already takes ~36.3 hours). There is no "true optimal" total
idle-time figure to compare The Greedy Queue against at realistic scale, because nobody — not
Vantage, not anyone — can actually finish computing it in time. The six-job pilot batch is the
*largest* batch size where a genuine head-to-head margin can be computed at all, which is precisely
why it is the graded comparison: it is not a shrink-to-fit window chosen to manufacture a comfortable
margin, it is the boundary of what is even measurable. This mirrors the structural move in
a sibling case in this corpus (an eighteen-month graded window vs. a dramatic lifetime reveal) —
here the "dramatic reveal" is D2's feasibility-crossing table, not a second dollar figure.

## Five Socratic questions

1. The Full Sweep beats The Greedy Queue by 13.9% on the six-job pilot batch — a real, provable, mathematically best answer. Why isn't that the end of the discussion?
2. Your D2 table shows The Full Sweep still finishes in about 48 seconds at 12 jobs, but takes about 36.3 hours at 15 jobs — just three more jobs. Why does adding three jobs multiply the time by roughly 2,730 times, instead of by some smaller, proportional amount?
3. If a much faster computer let Vantage evaluate orderings 1,000.0 times faster than Appendix C assumes, would The Full Sweep become feasible at realistic job counts? Use your D2 numbers to check, rather than guessing.
4. The Greedy Queue never looks ahead and never reconsiders a choice once made — why might that specific limitation (not "it's not exhaustive," but the never-look-ahead, never-reconsider rule itself) cause it to land on a worse ordering than the true optimum?
5. If Vantage's fleet stopped growing today and every batch stayed at six jobs forever, would your recommendation change? What does that tell you about whether this is really a math problem about six jobs, or a math problem about growth?

## The trap

**A learner who sees The Full Sweep beat The Greedy Queue by 13.9% on the six-job pilot batch and
recommends shipping The Full Sweep company-wide — without ever running D2's feasibility-crossing
arithmetic at Vantage's own actual batch sizes — has fallen into the case's main trap.** This is
exactly the rubric trap named in the approved concept sheet: assuming "computers are fast" makes
brute-force scheduling always feasible, without actually computing how large the factorial becomes
at realistic job counts. The six-job margin is real and correctly computed — the trap is not bad
arithmetic on D3, it is treating a result that is true at n=6 as if it generalizes to n=12 or n=15,
when D2's own numbers (which the same student had to compute) say otherwise. A pitch that argues for
The Full Sweep using ONLY the D3 margin, without engaging D2's feasibility-crossing finding at all,
has fallen into this trap even if D3's arithmetic is flawless.

**A second, milder trap:** assuming the factorial explosion is roughly proportional — that going from
12 jobs to 15 jobs (a 25.0 percent increase in job count) should cost roughly 25.0 percent more time.
The real jump is from ~48 seconds to ~36.3 hours, a factor of about 2,730 times (exactly 15!/12! =
15 x 14 x 13 = 2,730, since search time scales directly with n! at a fixed evaluation rate). A
learner who expresses surprise at
this, or who tries to "sanity check" it by assuming a smaller, linear-feeling increase, has
demonstrated the actual pedagogical point of the case: intuition about growth rates trained on
everyday linear and even exponential quantities badly underestimates factorial growth.

## Twist

Structural, not a scripted mid-discussion reveal, and it is the same finding as the trap above,
delivered as new information rather than as a warning: **The Full Sweep's own D2 numbers, which the
room has already computed, show that it stops being runnable at all somewhere between 12 and 15
jobs — and Appendix B states Vantage's batch size is already at 12 and growing.** Facilitators should
deliver this directly, at roughly the 30-minute mark, once D3's 13.9% margin has been established and
a recommendation has started to form around The Full Sweep: *"Appendix B says Vantage's batches are
already at 12 jobs and heading toward 18-20 within the year. Pull up your own D2 numbers. At exactly
which job count does The Full Sweep stop finishing before the batch window closes — and what happens
the first night it doesn't?"* This does not make The Greedy Queue's answer better on the six-job
metric — it never becomes better there — it reframes what the six-job metric was actually measuring:
the best possible answer to a question Vantage will only get to ask a shrinking fraction of the time.

## Guide Notes — the anchor ladder (SPEC, facilitator-artifacts anchor-ladder subsection)

### Intro

Frame the format: a scheduling engineer with a working, better-scoring "perfect" scheduler on her
screen, and a VP meeting in ten minutes asking whether it will keep working as the fleet grows. This
is a story about whether a provably better answer is actually a usable one.

### Launch

Read the Overview aloud. Stop at "Her cursor sits in the next cell, empty, waiting for the number
that comes after it." Ask the room: "What number do you think she's about to type — and why does it
matter which one it is?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Full Sweep or The Greedy Queue — show of hands." Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which scheduler gives a better answer" toward "which scheduler can actually
produce an answer, every night, at whatever job count that night has." Let the room sit with the
fact that Vantage's batch size is not fixed — it is growing.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching any numbers, get the room to state the actual method out loud: evaluate n! for each
job count (D1), convert that into real search time at the assumed evaluation rate (D2), and
separately, for the one batch size small enough to check completely, actually run both strategies
and compare (D3). Re-ask: "Now that we have a process, is 'which scheduler gives a better answer'
still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name what the case does NOT give the room: no appendix states how fast Vantage's real
(not-yet-built) scheduler will actually run a search, or exactly how many minutes any specific job
switch really costs — those are stated Modeling Assumptions (Appendix A, Appendix C), not measured
facts. "Does that change how much weight you put on the exact 13.9% figure — and does it change
whether the explosion itself is real?"

### Data Deep Dive

Now open Appendices A-D. Run D1-D5 as a room, or have groups report out. This is also the moment to
run Socratic Questions 2 and 4.

### Twist

Once D3's 13.9% margin is on the table and a recommendation has started to form, deliver the twist
described above: Appendix B's own batch sizes mean The Full Sweep stops being runnable at all
somewhere between 12 and 15 jobs. Run Socratic Question 1 immediately after.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, are you defending The Full Sweep for
the six-job batch specifically, or for Vantage's actual nightly operation?"

### Lessons Learned

The core transferable idea: a provably optimal answer to a small version of a problem is not
automatically a usable answer to the real version of that problem, when the cost of finding it grows
factorially with size. Intuition trained on everyday linear or even exponential growth badly
underestimates how fast factorial growth explodes — three more jobs (12 → 15) turned a 48-second
search into a 36.3-hour one.

### Standards Touched On

Factorial; How to evaluate a factorial expression.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00-3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no numbers shown yet |
| 3:00-8:00 | Position defense: "Convince us your pick actually ships a schedule every night, not just a better one sometimes" |
| 8:00-20:00 | Data Deep Dive — build D1's factorial table and D2's search-time conversions as a room |
| 20:00-30:00 | Run D3's six-job exhaustive search and nearest-neighbor comparison; confirm the 13.9% figure and where it comes from |
| **30:00** | **DROP THE TWIST** — Appendix B's own batch sizes mean The Full Sweep stops finishing somewhere between 12 and 15 jobs; run Socratic Question 1 |
| 30:00-38:00 | Pressure-test the recommendation: does the feasibility-crossing framing change anyone's vote, and does it survive Socratic Question 3 (a 1,000x faster computer)? |
| 38:00-45:00 | Close, re-vote, D4/D5's full explosion table and chart reveal (n=18: ~20.3 years; n=20: ~7,709 years), lessons learned |

## Cohort bands (SPEC, facilitator-artifacts cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12-20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6-11)** | smaller room | Anchors 2-3 combine into one pass; D3's six-job exhaustive search is worked as one shared example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1-2)** | tutoring context | No vote at Anchor 1 — ask for a stated initial position and why instead; the facilitator plays devil's advocate directly rather than cold-calling the room; the D2 feasibility-crossing reveal (30:00-38:00 equivalent) still runs in full, since it is the single most important move in the case |
