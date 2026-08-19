# Facilitator Notes — Grant Reach

## Argument for A (mail the union)

Order A reaches every eligible student — all 3,250 of them, no exceptions — and, under this
case's renewal-rate assumptions (MA4/MA5), produces **2,275** projected on-time renewals versus
**1,988** under Order B. That's 287 real students who keep aid they would otherwise lose, for
$1,517.75 of the university's own money — about $5.29 of university spending per additional
renewal earned over the Order B baseline. Order A also has a structural argument on its side
independent of any rate assumption: it is the only order under which the set of eligible,
unreached students is provably empty (Deliverable D3).

## Argument for B (mail only the intersection)

Order B costs the university **exactly $0.00** and still reaches the highest-overlap group —
students eligible for both programs, arguably the group with the most at stake per student. It
recovers roughly 87% of Order A's renewal outcome (1,988 of 2,275) at 0% of Order A's university
cost, leaving essentially all of the year's $1,600 discretionary mailing budget available for
whatever else the office needs to fund this year. In a year where that budget genuinely has other
claims on it, "free and still gets most of the outcome" is not a weak position.

## The margin

The case's literal stated `primary_metric` (SPEC §4 field: "dollars of university budget spent
per student who actually renews aid on time") is **degenerate for Order B** — its university-side
cost is $0.00 by construction (the state funds it), so any per-renewal ratio built on that
numerator is $0.00 regardless of how many students it reaches. That is real and worth keeping in
the case (Deliverable D5 makes students compute and confront it directly), but it cannot serve as
SPEC §2's two-sided balance comparison, since a $0.00-vs-positive ratio has no meaningful percent
margin.

The formal balance/margin figure in `case.json` is computed instead on **total on-time renewals
achieved**, which is well-defined for both orders: (2,275 − 1,988) / 2,275 = **12.6%** — inside
SPEC §2's 20% cap, and a genuinely close comparison. This is a documented, deliberate substitution
of comparison axis, not a hidden one — see `case.json`'s `balance.margin_basis` field.

## Five Socratic questions

1. Order B's cost-per-renewal is $0.00 and Order A's is about $0.67. If cost-per-renewal is the
   *only* thing that matters, does the discussion even need to happen — and if it isn't the only
   thing that matters, what did we leave out of that number?
2. Deliverable D3 asks you to name the empty set under each order. Under Order A, which set is
   empty — and what does it mean, in plain language, that a set of *people* can be empty?
3. If Modeling Assumption MA3 (the 80% overlap) were wrong — if the real overlap were smaller,
   say 60% instead of 80% — which counts in your Venn diagram change, and which stay fixed?
4. Cascade State's discretionary mailing budget is $1,600 for the *whole year*, not just this one
   mailing. What does Order A do to the office's ability to fund anything else this year, and does
   that change your recommendation even if the renewal numbers stayed exactly the same?
5. MA4 and MA5 are both explicitly flagged "the answer is sensitive to this value." Pick one and
   argue, using only Appendix D's real study, whether you think the true gap between mailed and
   unmailed renewal rates is bigger or smaller than the 15 points this case assumes — and what
   that would do to the case's conclusion.

## The trap

The obvious, confident wrong move is reading Order B's $0.00 university cost as an unambiguous
win and stopping there — "it's free, why would you ever spend money when the free option exists."
That reasoning skips straight past the fact that "free" is a ratio artifact, not a statement that
nothing is lost: 287 real students, in this case's own numbers, do not renew on time under Order B
who would have under Order A, and each of those students is walking away from thousands of real
dollars of aid (Appendix E) — money the case's headline metric never counts, because it only
tracks the university's own spending, not the students'. A Hero who fixates on $0.00 without
reading Deliverable D6's total-renewals comparison has found the number, not the answer.

## Sensitivity note (SPEC §6)

Checked directly against SPEC.md §6. This case is routine administrative/financial-aid outreach
math — no illness, death, or family-hardship framing, no protected-subject sensitivity. No
facilitator content warning is required.
