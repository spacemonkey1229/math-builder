# FACILITATOR.md — The Approval Gate

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Approval Gate · **Tier:** T3 (MS-stretch / HS-entry) · **Studio:** MS Adventure
**Standards:** Discrete Mathematics/Formal Logic — Logical Statement, Conjunction, Disjunction,
Negation, Conditional Statement, Truth Table, and two "how to…" skills (truth-table construction,
converse/inverse/contrapositive) — see `case.json.standards[]` for exact ids.

**Status:** `case-research` complete (2026-09-09). All `{{NEEDS_SOURCE: ...}}` placeholders in
`case.md` are resolved — one real Appriss Retail/Deloitte fraud-rate figure is sourced (Appendix F,
[S2]), three supplemental real sources ground the platform realism and inform two assumptions'
basis ([S1], [S3], [S4]), and the request-volume breakdown, gate thresholds, escalation cost, and
average value at risk are disclosed Modeling Assumptions MA1–MA4, because no publishable figure
exists for any of them. `case.json.balance.margin_pct` is a real, computed **9.8%**. Everything
below is the case of record, not a placeholder.

**Sensitivity note (SPEC §6):** ordinary workplace pressure — a mid-level manager facing a
same-day deployment deadline and a VP pushing a specific technical decision. No illness, death, or
family hardship. Standard facilitator handling suffices.

## Argument for A — The Compound Gate

Option A's escalation rule (¬p ∨ ¬q ∨ r) is the **mathematically correct** De Morgan's-Laws
negation of Compliance's own approve rule (p ∧ q ∧ ¬r) — nobody can dispute its logical
correctness, because it is derived, not designed. It escalates 1,600 of the 3,600 monthly requests
[MA1] — every category that fails at least one safety condition — at a total cost of
1,600 × $9.00 [MA3] = **$14,400.00**. A's case is that correctness is not optional in a
compliance-adjacent system: every request that fails even one safety condition gets a human's
eyes on it, producing zero systematic false approvals of "unsafe" requests. **Under the case's own
current numbers, A is also the cheaper design overall** (see "The margin" below), despite
escalating 106x more requests than B — its real strength is that avoiding the expected fraud/error
loss from under-escalation outweighs its much larger escalation-labor bill.

## Argument for B — The Streamlined Gate

Option B's real, quantitative case is workload: escalating only 15 of the 3,600 monthly requests
[MA1] — the single rarest category, where every condition is unfavorable at once — at a direct
escalation cost of just $135.00, meaning 3,585 requests a month clear automatically versus A's
2,000. B's argument is not "it's the same rule" (that claim is what Challenge 3 (D3) disproves) —
B's honest argument is a workload argument. Its weakness: 1,585 of those auto-approvals are
requests that fail at least one of Compliance's own safety conditions, and at a real 15.14% fraud
rate [S2] against an average $66.00 value at risk [MA4], this produces **$15,972.95** in expected
total cost — higher than A's, despite B's dramatically lower escalation count.

## The margin — real numbers, and how fragile this case actually is

`case.json.balance.margin_pct` = **9.8%**, within the approved concept's 8–15% margin target. The
arithmetic, in full (margin computed by dividing by the LOSING option's cost, the corpus's
standard convention):

- **Escalation counts:** Option A escalates 1,600 requests (every category except p=T,q=T,r=F).
  Option B escalates only 15 (only p=F,q=F,r=T).
- **Option A (The Compound Gate):** 1,600 × $9.00 = **$14,400.00** (winner, lower cost).
- **Option B (The Streamlined Gate):** 15 × $9.00 + 1,585 × (0.1514 × $66.00) = $135.00 +
  1,585 × $9.9924 = $135.00 + $15,837.95 = **$15,972.95** (loser, higher cost).
- **Margin:** |$15,972.95 − $14,400.00| / $15,972.95 = **9.8%** (the winner A is the cheaper
  option — lower cost wins on this case's metric, unlike the corpus's more common "higher is
  better" cases).

**Under the case's current numbers, A is the lower-total-cost option** — a genuinely
counter-intuitive result, since A escalates 106x more requests than B. This margin is a designed
property of four authored Modeling Assumptions (MA1–MA4's values), not an empirical finding — only
the 15.14% return-fraud rate [S2] is a real, sourced figure used directly.

**Why this matters for the facilitator, specifically:** `sensitivity_model.py`'s ±50% flex sweep
found that the 8 request-volume category counts (MA1) leave the margin essentially unchanged
(~9.8–9.9%) and never flip the winner — the total-cost comparison is structurally robust to any
single category count moving on its own. But **two dials are genuinely unstable**: `cost_per_escalation`
(MA3) and `avg_value_at_risk` (MA4). A -50% flex on `avg_value_at_risk` FLIPS the winner to B
(44.1% margin); a +50% flex on `cost_per_escalation` also FLIPS the winner to B (25.7% margin);
both directions of both dials breach the SPEC §2 20% cap. Both are disclosed in
`case.json.sensitivity_disclosure[]` as Category X. **Do not treat a student who challenges
`avg_value_at_risk` downward or `cost_per_escalation` upward as having missed the point — that is
exactly the case's most defensible line of attack, since neither figure has a hard public source
behind it.**

## Five Socratic questions

1. Option B escalates far fewer requests than Option A — if fewer escalations mean lower labor cost, why might Option B still not be the cheaper design overall?
2. The VP called Option B "the same policy, just cleaner." Using Appendix A's own De Morgan's-Laws derivation, is that claim true, and if not, where does it first go wrong?
3. Compliance's rule says auto-approve only when p ∧ q ∧ ¬r — what is the actual converse of "if a request is auto-approved, then p ∧ q ∧ ¬r," and is that converse even a true statement here?
4. Appendix D's $66 average value at risk and $9 cost per escalation are both disclosed estimates, not sourced facts — if the real average value at risk were meaningfully lower than $66, does the recommendation flip to Option B?
5. Both designs agree completely on Compliance's original approve rule and disagree only on everything else — why does a single wrong OR/AND swap in the "everything else" case matter this much in dollar terms?

## The trap

**A learner who reads Option A and Option B's plain-English descriptions side by side and
concludes they're "basically opposites of the same rule" without ever building the truth table has
fallen into the case's central trap.** ¬p ∧ ¬q ∧ r (Option B) is not the logical negation of
p ∧ q ∧ ¬r — the correct negation, via De Morgan's Laws, swaps AND for OR: ¬p ∨ ¬q ∨ r (Option A).
A pitch that treats the two designs as interchangeable rewordings, or that never produces a
genuine 8-row truth table to check row-by-row where the two rules actually diverge, has not done
the deliverable's real work even if it lands on a confident recommendation.

**A second, related trap:** a student who correctly proves the two rules are not equivalent can
still recommend the wrong design by comparing raw escalation counts (Option B escalates far fewer
requests) without ever pricing out the false-approval loss risk that Option B's under-escalation
creates. Fewer escalations is not automatically cheaper once the expected loss from the requests
that should have been escalated, and weren't, is added in.

## Twist

The structural twist lives in the fact that "simpler-sounding" and "logically equivalent" are not
the same claim, and the case is built so a room's early instinct — trust the VP's plain-English
description, since it sounds like it must be the same rule — is falsified by the actual truth
table, not by an appeal to authority. Facilitators can manufacture the twist moment directly by
asking Socratic Question 2 if no student raises the discrepancy unprompted, then letting the room
sit with the fact that Legal/Compliance already signed off on Option B's *wording* without anyone
checking its *logic*.

---

## Guide Notes — the anchor ladder (SPEC Section 7, anchor-ladder subsection)

### Intro

Frame the format: an AI ops lead has to ship one of two refund-approval gate designs today, and
the two designs were pitched as "the same policy, just cleaner" — the room's job is to check
whether that's actually true before trusting the dollar math.

### Launch

Read the Overview aloud. Stop at "One gate. One config. One number to defend when Legal asks why."
Ask the room: "Before you've built a single truth table, do you believe the VP's rewrite really is
the same policy, just cleaner? Why or why not?"

### Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. "The Compound Gate or The Streamlined Gate — show of hands." Record the split.

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Push the room past "which rule sounds simpler" toward "are these two rules actually logically
different, and if so, what does that difference cost in real dollars." Let the room sit with the
fact that nobody — not Legal, not the VP — actually built a truth table before signing off.

### Anchor 3 — WHAT IS THE PROCESS?

Before touching Appendix C/D's numbers, get the room to state the actual comparison method out
loud: build both truth tables (D1), state the shared rule as a conditional and find its converse/
inverse/contrapositive (D2), apply De Morgan's Laws to check whether B really is A's negation (D3),
then price out both designs against real monthly volume (D4). Re-ask: "Is 'which rule sounds
simpler' still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?

Name the load-bearing unknowns explicitly: Foothill Outfitters' own request volume and category
breakdown, and the real dollar figures behind escalation cost and false-approval loss, are not
public data anywhere — every one is either a disclosed Modeling Assumption or informed by real,
cited industry research. "Which of these figures would you most want to challenge, and why?"

### Data Deep Dive

Now open Appendices A–E. Run D1–D5 as a room, or have groups report out.

### Twist

Once D3's De Morgan's-Laws verdict is on the table, run Socratic Question 2 directly if it hasn't
come up yet: "The VP called this 'the same policy, just cleaner.' Is that true?" Let the room
discover exactly which row of the truth table the two designs disagree on, and how large that
disagreement turns out to be once D4's dollar figures are run.

### Close

VOTE AGAIN. "Did the vote move? For the people who didn't move, what would it take to change your
mind?"

### Lessons Learned

The core transferable idea: two compound logical statements that sound like restatements of each
other can be genuinely different, and the only reliable way to check is to build the truth table —
not to trust how the sentence reads. A second, equally real lesson: even after proving two rules
are different, the cheaper-sounding one is not automatically the better business decision until
its risk is actually priced out.

### Standards Touched On

Logical Statement, Conjunction, Disjunction, Negation, Conditional Statement, Truth Table; How to
construct a truth table for a compound statement; How to determine the converse, inverse, and
contrapositive of a conditional statement.

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold read of the Overview, gut-check vote (Anchor 1) — no truth table shown yet |
| 3:00–8:00 | Position defense: "Convince us your gate is the right call, not just that it sounds simpler or stricter" |
| 8:00–20:00 | Data Deep Dive — build both truth tables (D1) and the conditional/converse/inverse/contrapositive (D2) as a room |
| 20:00–30:00 | Run the De Morgan's-Laws derivation (D3) and build D4's cost comparison; confirm the margin and where it comes from |
| **30:00** | **DROP THE TWIST** — Socratic Question 2: is the VP's rewrite actually the same policy? |
| 30:00–38:00 | Pressure-test the case's assumptions directly: how close is the margin to flipping, and what would a defensible challenge to the request-volume mix or the cost figures actually change? |
| 38:00–45:00 | Close, re-vote, D2's converse/contrapositive findings, lessons learned |

## Cohort bands (SPEC Section 7, cohort-bands subsection)

| Band | Typical size | What changes |
|---|---|---|
| **Full (12–20)** | the size this case is written for | Anchors and the 45-minute timed plan run as written above |
| **Compressed (6–11)** | smaller room | Anchors 2–3 combine into one pass; the 20:00–30:00 De Morgan's-Laws/cost build-out runs as a single worked example instead of small-group work; total runtime shortens proportionally |
| **1:1 / pair (1–2)** | tutoring context | No vote at Anchor 1 — a stated initial position instead; facilitator plays devil's advocate directly; the 30:00–38:00 sensitivity pressure-test still runs in full |
