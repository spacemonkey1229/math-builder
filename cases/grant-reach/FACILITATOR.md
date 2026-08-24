# Facilitator Notes — Grant Reach

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices.*

**Case:** Grant Reach · **Tier:** T2 (MS-core) · **Studio:** Heroes Academy
**Standards:** Discrete Math — Set, Subset, Union, Intersection, Empty Set (see `case.json.standards[]`
for exact ids).

## Intro

Frame the format before the numbers: this is a one-shot budget decision with a hard constraint —
"You are Deja Whitfield. Two mail-house order forms are sitting on your desk, both filled out,
both ready to submit. You can only submit one." Let that land before Launch.

## Launch

Put the two orders side by side with only the headline tradeoff visible: Order A (mails more
students, all on the university's own dime) vs. Order B (mails fewer students, but costs the
university $0.00). Ask for a gut read: "Same students needing the same reminder. Which order do
you submit?" Do not correct an early answer yet — that instinct is exactly what the case is built
to test.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's with the free option, Order B?" Show of hands, both options, no discussion. Record the
count for the Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better' mean here?"**

Let confusion grow here. Heroes will want to just ask which order is cheaper, and stop there.
Push: "Deja isn't being asked which order costs less. She's being asked how many real students
actually keep their aid." If the room arrives at "we need to compare renewals, not just dollars"
on its own, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening Appendix B: build
the Venn diagram of the two eligibility sets (D1), confirm the union algebraically (D2), name the
empty set under each order (D3), project renewals under both orders using the mailed/unmailed
rates (D4), total the university cost of each order (D5), and compare (D6). Re-ask: "Now that we
can see the steps — is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the Modeling Assumptions block honestly: MA2 (the 18.6% state-eligible share, anchored to
California's real statewide Cal Grant ratio), MA3 (the 80% Pell/state overlap, a qualitative
estimate — no public overlap statistic exists for any real campus), and MA4/MA5 (the 55%/70%
renewal rates, informed by direction and scale from a real reminder-effect study — Appendix D —
but not a direct transfer of its numbers, since that study measured a different channel and
window). Ask which ones are actually load-bearing for the final recommendation (MA3, MA4, MA5 all
are — the case's own Modeling Assumptions table marks each "the answer is sensitive to this
value") and which is closer to a fixed scenario constraint (MA1, MA6).

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D3 as a room (the Venn diagram, the union calculation, and
the empty-set argument), then split into two desks for D4 and D5 — one projects renewal counts by
region, one builds the total-cost table — before reconvening to compare and for D6's margin.

**Facilitator-only arithmetic note.**

Order A reaches all 3,250 eligible students (the union) and, under MA4/MA5, projects **2,275**
on-time renewals for **$1,517.75** of university money. Order B reaches only the 1,336-student
intersection and projects **1,988** on-time renewals for **$0.00** of university money. The gap:
287 real students renew under A who would not under B. Margin, computed on total renewals
achieved: (2,275 − 1,988) / 2,275 = **12.6%** (`case.json.margin_pct`).

## Twist

**Order B's $0.00 university cost is a ratio artifact, not proof that nothing is lost.** A Hero
who reads "free" as an unambiguous win and stops there has not yet confronted Deliverable D6:
287 real students, in this case's own numbers, do not renew on time under Order B who would have
under Order A — and each of those students is walking away from thousands of real dollars of aid
(Appendix E), money the case's headline per-renewal metric never counts, because it only tracks
the university's own spending, not the students'. The twist fires the moment a Hero notices the
real question is not "which order is cheaper" but "what does cheaper actually cost."

## The trap

The obvious, confident wrong move is reading Order B's $0.00 university cost as an unambiguous
win and stopping there — "it's free, why would you ever spend money when the free option exists."
That reasoning skips straight past the fact that "free" is a ratio artifact, not a statement that
nothing is lost: 287 real students, in this case's own numbers, do not renew on time under Order B
who would have under Order A, and each of those students is walking away from thousands of real
dollars of aid (Appendix E) — money the case's headline metric never counts, because it only
tracks the university's own spending, not the students'. A Hero who fixates on $0.00 without
reading Deliverable D6's total-renewals comparison has found the number, not the answer.

A second, subtler trap: the case's literal `primary_metric` (dollars spent per renewal) is
**degenerate for Order B** — $0.00 university cost divided by any positive renewal count is
always $0.00, regardless of how many students are reached. A Hero who takes that $0.00 at face
value as "infinitely efficient" has mistaken a mathematical artifact of dividing by a
university-only cost for a real efficiency claim. That's exactly why the case's formal
`margin_pct` is computed on total renewals achieved instead (see `case.json`'s
`balance.margin_basis` field) — Socratic Question 1 exists specifically to catch this.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on Order A for the real reason — 287 real students — or did they just guess right?

## Deep conflict — two threads (20:00–30:00)

1. **Cost-efficiency vs. total-reach.** Order B is free and reaches the highest-overlap group.
   Is "free and mostly effective" ever the wrong call purely because a cheaper option exists, or
   does the office have a real obligation to reach every eligible student it can afford to reach?
2. **Discretionary-budget vs. one-time spend.** Order A consumes nearly all of the year's $1,600
   discretionary budget on this one mailing. Does that change the recommendation even if the
   renewal numbers stayed exactly the same?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — headline tradeoff only, gut-check vote |
| 3:00–6:00 | Anchor 1 vote recorded |
| 6:00–9:00 | Anchor 2 — pressure-tests "better, measured how?" |
| 9:00–12:00 | Anchor 3 — name the six-step process before opening Appendix B |
| 12:00–15:00 | Anchor 4 — surface MA2–MA5, ask which are load-bearing for the recommendation |
| **~15:00** | **TWIST drops** — Order B's $0.00 cost vs. the 287 students who don't renew |
| 15:00–20:00 | Data Deep Dive — D1–D3 worked as a room |
| 20:00–30:00 | Deep conflict — two threads (cost-efficiency vs. total-reach; discretionary budget vs. one-time spend) |
| 30:00–40:00 | Data Deep Dive continued — D4–D6 in two desks, reconvene for the shared comparison |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## Socratic questions

1. Order B's cost-per-renewal is $0.00 and Order A's is about $0.67. If cost-per-renewal is the *only* thing that matters, does the discussion even need to happen — and if it isn't the only thing that matters, what did we leave out of that number?
2. Deliverable D3 asks you to name the empty set under each order. Under Order A, which set is empty — and what does it mean, in plain language, that a set of *people* can be empty?
3. If Modeling Assumption MA3 (the 80% overlap) were wrong — if the real overlap were meaningfully smaller than 80% — which counts in your Venn diagram change, and which stay fixed?
4. Cascade State's discretionary mailing budget is $1,600 for the *whole year*, not just this one mailing. What does Order A do to the office's ability to fund anything else this year, and does that change your recommendation even if the renewal numbers stayed exactly the same?
5. MA4 and MA5 are both explicitly flagged "the answer is sensitive to this value." Using only Appendix D's real study, do you think the true gap between mailed and unmailed renewal rates is bigger or smaller than the 15 points this case assumes — and what would that do to the case's conclusion?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes reached for the $0.00 cost-per-renewal comparison first, and how much nudging it
  took to get to the 287-student gap in D4/D6.
- Whether the empty-set argument (D3) was treated as a real check on the two orders or as a box to
  tick before D4.
- Whether the discretionary-budget tension (Order A eating nearly all of the year's $1,600) came
  up on its own or needed a direct hint.

## Standards Touched On

Set · Subset · Union · Intersection · Empty Set · Venn Diagram · How to find the union and
intersection of two sets · How to represent a set relationship using a Venn diagram

## Facilitator note — margin stability (Tier 2 P5)

The recommendation is **not** stable under every stated assumption's plausible range. Flexing MA4
(the no-reminder rate) up 50% or MA5 (the with-reminder rate) down 50% both flip the winner to
Order B; several other flexes on MA2/MA3/MA4/MA5 push the margin past SPEC §2's 20% cap without
flipping the winner. See `case.json.sensitivity_disclosure[]` (all Category F — genuinely
irreducible unknowns, not proprietary data someone forgot to look up: no public dataset measures
Cascade State's own renewal-rate lift from a mailed reminder specifically). This is disclosed, not
hidden, and it is not new information — the Modeling Assumptions table itself already flags MA2
through MA5 "the answer is sensitive to this value." If a Hero treats the 12.6% margin as
rock-solid, Anchor 4 exists specifically to surface this before the numbers are worked: ask which
assumption the recommendation would flip under, and how far it would have to move.

## Sensitivity note (SPEC §6)

Checked directly against SPEC.md §6. This case is routine administrative/financial-aid outreach
math — no illness, death, or family-hardship framing, no protected-subject sensitivity. No
facilitator content warning is required.
