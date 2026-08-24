# FACILITATOR.md — The Compute Lease

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Compute Lease · **Tier:** T2 (MS-core) · **Studio:** Heroes Academy
**Standards:** Calculus/Series — Series, Sequence, and How to determine whether a series converges
or diverges (see `case.json.standards[]` for exact ids).

**Status:** DRAFT — written before `case-research` fills the 10 open `{{NEEDS_SOURCE}}`
placeholders in `case.md`. `margin_pct` below is `null` until those figures land; this document
records the *shape* of both arguments now, and gets the actual numbers reconciled once
`case-research` runs.

## Argument for A — The Long Lock

The Long Lock's per-GPU-hour rate is fixed below any on-demand rate Kestrel could get on the open
market, and that gap does not change no matter how much or how little the GPUs get used. The more
GPU-hours Kestrel's customers actually consume over the 24-month window, the more that fixed cost
gets spread across real usage — so at the mid or high end of Appendix D's growth-rate range, the
Long Lock's cost-per-GPU-hour-delivered should undercut the Open Tap even though the Open Tap's
own headline rate never moves. This is the argument a board wants to hear: predictable spend,
locked-in unit economics, no rate risk.

## Argument for B — The Open Tap

The Open Tap's total cost is a series that tracks real demand term by term — it is structurally
incapable of paying for capacity nobody rents. If Kestrel's actual growth comes in at or below the
low end of Appendix D's range, the Long Lock's fixed-payment series keeps arriving in full,
including months of committed contract that run past the 24-month evaluation window entirely,
while the Open Tap's series shrinks (or simply never grows) right along with real demand. The
Open Tap's per-unit rate is worse, but the denominator problem — paying a great rate for capacity
that sits idle — is the Long Lock's, not the Open Tap's.

## The margin

`margin_basis` (recorded now in `case.json.balance.margin_basis`, resolved after research): sum
each option's 24-month cost series from D2, divide by total GPU-hours delivered over the same
window, for each of the low/mid/high scenarios in Appendix D (D4). The margin is the percent gap
between the two options at whichever scenario sits closest to Kestrel's expected growth, and D5's
crossover-rate calculation shows how much of Appendix D's range sits on either side of the
breakeven point — i.e., how fragile the recommendation actually is to the growth-rate assumption.
Do not pre-compute or state a specific percentage here; that is `case-research`'s job once
Appendices B, C, and D carry real numbers.

## Five Socratic questions

1. Your D4 table shows six different cost-per-GPU-hour-delivered results — two options across
   three growth scenarios. Do the same six numbers all point to the same recommendation, or does
   the answer actually change depending on which scenario you believe?
2. The Long Lock's contract term runs longer than the 24-month window you were asked to evaluate.
   If you only look at the 24-month cost-per-GPU-hour number, what cost is your evaluation quietly
   leaving out — and does that omission favor the Long Lock or the Open Tap?
3. Your D3 classification says the Open Tap's underlying growth series diverges if the growth rate
   held steady forever. Kestrel isn't actually committing to "forever" — so why does that
   divergence result matter to a two-year decision at all?
4. Your D5 crossover rate tells you the exact growth rate where both options tie. Is that
   crossover rate closer to the low end, the middle, or the high end of Appendix D's range — and
   what does that position tell you about how confident Sofia should be in either direction?
5. If Kestrel's actual growth rate turned out to be *outside* Appendix D's stated range entirely —
   faster or slower than any industry disclosure predicted — which option would be more painful to
   be locked into, and why?

## The trap

Heroes will compare the two options' 24-month total dollar spend directly — not their cost *per
GPU-hour delivered* — and conclude whichever number is smaller in isolation is the better choice.
That comparison silently assumes both options deliver the same amount of usable GPU-hours to
paying customers, which is exactly what is *not* true: the Long Lock's fixed capacity sits there
whether or not customers rent it, so a low-growth scenario means the Long Lock is paying the same
total dollars for far fewer *delivered* GPU-hours than a naive total-dollar comparison would
suggest. The case's primary metric is a *ratio* — total cost divided by GPU-hours actually
delivered — specifically to force students past comparing two raw dollar totals that are not
denominated the same way.

A second, related trap: treating the Long Lock's rate advantage as fixed and permanent once
computed at one growth scenario, rather than checking where the actual crossover point (D5) falls
relative to Appendix D's full range. A Hero who computes only the mid-scenario result and stops
has not yet found out whether the recommendation is robust across the whole plausible range or
balanced on a knife's edge near one end of it.

## Sensitivity note (SPEC §6)

NONE. This is routine infrastructure-procurement and cost-modeling math — no subject-matter
sensitivity flag applies.
