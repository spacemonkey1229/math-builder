# Catering — Maya Whitfield

## Challenge 1 — Research

How to solve a multi-step equation with a variable on one side:
https://www.mathsisfun.com/algebra/equations-solving.html

I used this for D5, where I had to solve `12.59x - 588.20 = 950.00` for x. The page's rule —
"what we do to one side of the = we must also do to the other side" — is exactly the move I
needed: add 588.20 to both sides first, then divide both sides by 12.59, instead of trying to
divide first and getting a fraction that didn't make sense.

## Challenge 2 — The Pitch

I recommend Option A — the Beal wedding. Order A is the right choice for Victorino this month,
and the numbers back it up in a way that survives the strongest argument against it.

Start with the plain comparison. The wedding nets $897.42 after every fee is paid — event fee,
delivery, ingredients, all of it. The corporate party nets $760.62. That is a real 17.99% margin
in the wedding's favor, computed the same way for both events so it is an apples-to-apples
comparison, not a trick of which costs got counted where.

The strongest argument against picking the wedding is the one Maggiano's own background data
points to: corporate clients call back. A wedding is a one-time booking; a satisfied corporate
client tends to reorder for the next quarterly lunch or holiday party. If Victorino is building a
business, not just working a single month, that repeat-business angle is a real, legitimate
reason to weight the corporate event's profit higher than its raw dollar number suggests.

Here is why I don't think it changes the recommendation for THIS decision. This is a real trade-off
between two competing variables — immediate profit (the wedding's $897.42 vs. the corporate
event's $760.62) against future repeat-business value (which the wedding, a one-time booking, has
none of, and the corporate event has some of). I'm weighing that trade-off and coming down on the
side of the immediate profit, because Victorino isn't choosing which relationship to invest in
long-term — Challenge 3 makes clear this is a single booking decision for a specific month, and
nothing in the case says he has to pick only one type of client going forward. He can serve the
wedding this month and still go after corporate repeat business the next time a corporate lead
calls. The repeat-business argument is a reason to keep pursuing corporate clients over time, not
a reason to turn down $136.80 in extra profit on the booking directly in front of him right now.
Reordering value is real, but it is not the deciding factor when this specific choice doesn't
foreclose it — at the cost of a slightly lower one-time profit, Victorino would be buying a
loyalty benefit he doesn't actually need to sacrifice this booking to get.

There's a second thing my numbers turned up that neither event's raw profit shows on its own —
see D5 below. Neither event, by itself, covers Victorino's $950 monthly loan payment. That
doesn't change my recommendation, but it does mean the wedding's advantage matters more than the
percentage alone suggests: the wedding gets him closer to covering it, and closer is the direction
that matters when the payment is fixed and due regardless of which event he takes.

## Challenge 3 — The Work

### D1 — Order quantity (proportion, 7% buffer)

Wedding order qty: 110 guests x 1.07 = 117.7, rounded up to whole servings = **118 servings**.
Corporate order qty: 100 guests x 1.07 = 107.0 = **107 servings**.

### D2 — Revenue and ingredient cost

Wedding revenue: $3,186.00
Wedding ingredient cost: $1,700.38
Wedding gross profit: $1,485.62

### D3 — Fees

Wedding event fee: $575.00
Wedding delivery fee: $13.20
(kitchen and venue are in the same city, so delivery is the flat in-city rate — not the higher
out-of-town rate the corporate event pays)

### D4 — Net profit

Wedding net profit: Revenue $3,186.00 minus ingredient cost $1,700.38 minus event fee $575.00
minus delivery fee $13.20 = **$897.42**.

Corporate revenue: $3,135.10. Corporate ingredient cost: $1,769.78. Corporate event fee: $575.00.
Corporate delivery fee: $29.70 (out-of-town rate). Corporate net profit = **$760.62**.

### D5 — Solving for the loan-covering order size

Victorino's loan payment is $950.00 a month. I want to know how many servings the wedding order
alone would need to sell for its net profit to cover that by itself.

Each extra serving carries the wedding's own margin per serving: gross profit $1,485.62 divided by
118 servings = $12.59 margin per serving. The fixed costs that don't scale per serving are the
event fee plus delivery fee: $575.00 + $13.20 = $588.20 fixed.

Equation: 12.59x - 588.20 = 950.00, solve for x.

Add 588.20 to both sides: 12.59x = 1538.20
Divide both sides by 12.59: x = 122.18, round up to **123 servings**.

The wedding is only booked for 118 servings — 5 short of 123. At the actual 118-serving booking,
net profit is $897.42, which is $52.58 short of the $950.00 target. So the wedding's profit alone
does not fully cover this month's loan payment either — it just gets much closer than the
alternative.

For the corporate event, the same method (margin per serving $12.76, fixed costs $604.70) gives
a target of 122 servings against its actual 107-serving booking — a $189.38 shortfall, over three
times larger than the wedding's.

### D6 — Recommendation, informed by D5

Net profit alone favors the wedding by $136.80 (17.99%). D5 adds real weight to that: neither
event covers the loan on its own, but the wedding's shortfall ($52.58) is much smaller than the
corporate event's ($189.38). Both facts point the same direction. I recommend Option A, the
wedding.

### Original data — per-serving and per-guest margin (not in the case appendix)

D6's recommendation above optimizes for total net profit per event, since that's what Appendix A names as the metric. But I wanted to check whether the wedding's advantage held up under a different metric — profit per guest actually served, instead of profit per event — since a bigger event could look more profitable just by being bigger, not by being more efficient.

| Event | Net profit | Guests served | Profit per guest |
|---|---|---|---|
| Wedding | $897.42 | 110 | $8.16 |
| Corporate | $760.62 | 100 | $7.61 |

(897.42 / 110 = 8.156..., rounds to $8.16. 760.62 / 100 = $7.61 exactly.)

Even sliced per guest instead of per event total, the wedding still wins — $8.16 vs $7.61 per
guest actually served. That's a smaller gap in percentage terms than the raw net-profit
comparison, but it's the same direction, which told me the wedding's advantage isn't just an
artifact of it being a bigger event — it holds up per-guest too.

![Per-guest profit comparison chart](per-guest-profit-chart.png)

## Challenge 4 — Appendix of work

Worked every step above by hand first with a calculator, then double-checked D5's equation by
plugging 123 back in: 12.59 x 123 = 1548.57, minus 588.20 = 960.37 — that's slightly over 950,
which makes sense since 123 is rounded UP from 122.18 (you can't sell a fraction of a serving, and
122 servings alone would land under the target, at 12.59 x 122 - 588.20 = 948.78, which is still
$1.22 short). Rounding up to 123 is the only whole-serving count that actually clears the target.

I also sanity-checked the whole thing by asking: does a bigger event automatically mean more
profit? No — the per-guest table above shows profit doesn't scale purely with event size, since
ingredient cost and fees scale differently for each event. That's why I ran the per-guest version
instead of just trusting the raw totals.
