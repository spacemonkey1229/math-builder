# Guide Notes: Travel Planner

**Case:** Travel Planner · **Tier:** T2 · **Band:** MS · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (11 skills — percent, decimal
arithmetic, order of operations, elapsed/clock time, and comparison)

Legacy conversion, 2026-08-20, built from the original source docx
(`source/Y2/Session 1/Travel Planner/Case Study_ Travel Planner.docx`) onto the current 11-anchor
ladder. No separate Guide Notes doc exists in the source for this case — this is a from-scratch
facilitator guide, not a reformat of an existing one.

## Intro

Frame the format: this is a real family vacation budget, sealed and booked sight-unseen, not a
worksheet. Name the opener — "Gina has to book this trip today, mail it in a sealed envelope, and
she never gets to change her mind once it's sent."

## Launch

Read Appendix A aloud (what each Betteridge actually cares about), with no dollar figures computed
yet. Ask: "Just from what this family loves, which plan do you think Gina should book?" Do not
confirm or correct answers here.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who books the Wizarding World Plan? Who books the Disney Classic Plan?" Show of hands, no
discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "Is it just as simple as which trip fits the budget better, or
is there something else to consider?"**

Let confusion grow here, deliberately. Push on Background's own hint: James and Elizabeth say they
hate rigid schedules, and Gina still has to write an hour-by-hour itinerary. Is "which plan is
cheaper" the only real question, or is there a second one about whose preferences (Cassy's
2-year-old Harry Potter plan vs. Elizabeth's own treasured childhood memory) should break the tie
when both plans clear the budget?

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of the tradeoff, ask them to name the actual steps: total
each plan's tickets at the right discount tier, total the hotel at the Priceline discount, add
Gina's 4% fee, compare both grand totals to the $3,950 cap. Re-ask: "Do we agree on that process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's four assumptions: Henrietta's free-admission age cutoff, how Universal's 3
separate 1-day tickets qualify for the 6% "3+ day" tier, hotel nights equaling activity days, and
— the big one — the Anaheim Marriott Suites nightly rate ($210, the top of a real $102–$210 cited
range). Ask which one actually changes the final answer if it's off. Most barely move the total;
MA4 (the hotel rate) is the one that can actually flip which plan is cheaper (see Twist/Deep
Conflict below).

## Data Deep Dive

Now, and only now, the numbers. Walk D1's ticket table and D2's hotel discount together as a room,
cold-calling for the discount *tier* specifically — this is where a Hero who applies the 2% rate to
Plan A's Universal tickets (instead of the 6% "3+ day" tier) will get a plausible-looking wrong
number.

**D3, once D1/D2 are solid.** Cold-call for the order of operations: Gina's 4% fee is charged on
the *sum* of the discounted hotel and discounted tickets, not 4% of each separately added after.
Ask a Hero to compute it the wrong way (4% of tickets + 4% of hotel, added) and compare — same
answer here, since 4% distributes over a sum either way, but it's worth asking why that's true, and
whether it would still be true if the fee were, say, "$50 flat plus 4%" (it would not).

**D4.** The real numbers: Plan A totals $2,601.65 (34.14% of the cap left over); Plan B totals
$2,817.36 (28.67% left over). **Both plans clear the $3,950 cap comfortably.** Ask: "If both plans
fit the budget, what was the budget cap actually for?"

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Gina just checked the calendar one more time before sealing the envelope. Henrietta turns 3 —
right in the middle of the trip, on Day 3."

**Facilitator-only: what the numbers actually do (`case.json.derived`).** Henrietta stops being free
admission for any activity day on or after Day 3. For **Plan A** (Universal Days 1–3, Zoo Day 4,
beach Day 5), that means Day 3 (Universal) *and* Day 4 (Zoo) now need her own ticket — two extra
paid days, $174.28 added, pushing Plan A's total to $2,775.93. For **Plan B** (Disneyland Days 1–2,
LEGOLAND Day 3, beach Day 4), only Day 3 (LEGOLAND) needs her own ticket — one extra paid day,
$70.32 added, pushing Plan B's total to $2,887.68. **Neither total comes close to the $3,950 cap,
and Plan A is still cheaper** — but the gap between the two plans nearly halves, from 8.29% to
4.03%. A Hero who argued "Plan A is clearly the better budget pick" now has a real, harder case to
make: it's still true, but by less than half the margin they had five minutes ago, and specifically
*because* Plan A's extra park day is exactly what exposed it to more of Henrietta's new cost. Ask:
"Does this change your recommendation, or just make you defend the size of the gap more carefully?"

**Unstated convention, disclosed here:** Henrietta's newly-required Day-3 Universal ticket is
priced as a standalone 1-day admission at the **2% tier**, not folded into the rest of the
family's existing 3-day Universal booking at the 6% "3+ admission days" tier — even though she is
physically present on Day 3 of that same 3-day trip. This is a defensible modeling choice (her
ticket is a late, separate add rather than part of the original 3-ticket purchase that qualified
for the 6% tier per MA2), but it is not stated anywhere in `case.md`, and it is the one convention
that determines the exact dollar figures above — using the 6% tier for her Universal day instead
gives $163.46, not $174.28 (a small difference that doesn't change which plan is cheaper or by
roughly how much). If a Hero reasonably argues her ticket should qualify for the same 6% tier the
rest of the family's Universal days already have, that is a legitimate challenge to raise, not a
wrong answer to correct.

## Immediate recommit

Re-vote immediately. Ask by name: "Did Henrietta's birthday change anyone's answer? If you were
already on Plan A, does a shrinking gap bother you at all?"

## Deep conflict — three threads (20–30 min)

1. **Breadth vs. depth.** Plan A buys three shorter park visits (and a lower-thrill Zoo day made
   for Jimmy Jr.'s nerves); Plan B buys two full Disneyland days plus a Lego-specific day and a
   nicer divided suite. Neither is "more correct" — which one actually serves this specific family,
   per Appendix A, and does the cheaper plan automatically win?
2. **The rigid-itinerary tension.** James and Elizabeth explicitly said they hate strict daily
   plans — and Challenge D5 requires exactly that: an hour-by-hour written itinerary, sealed in an
   envelope, with no chance for the family to react before it's booked. Is Gina's job to give the
   family what they'll enjoy in the moment, or what they explicitly asked for on paper? Those are
   not obviously the same thing here.
3. **What the cap was actually testing.** Both plans clear $3,950 with real headroom (34.14% and
   28.67%). If the budget was never actually the tight constraint, was it ever really "the"
   dilemma, or was it a filter that both plans were always going to pass — meaning the real decision
   was about fit all along?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read Appendix A aloud, cold-call for a gut read, no dollar figures yet |
| 3:00–10:00 | Position defense — *"Convince us your plan is the better trip for this family, not just the cheaper one"* |
| 10:00–15:00 | Pressure-test the models — *"Whose grand total is doing the most work, and at which discount tier?"* |
| **15:00** | **DROP THE TWIST** — Henrietta turns 3 on Day 3, delivered slowly |
| 15:00–20:00 | Immediate recommit — did anyone's answer actually change |
| 20:00–30:00 | Threaded deep conflict (breadth vs. depth; the rigid-itinerary tension; what the cap was testing) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero computes both grand totals, sees Plan A is cheaper by $215.71, and stops — reporting "Plan A
wins" as if the case were only ever about which plan costs less. It never was: both plans clear the
$3,950 cap by a wide margin, which means the budget was a real constraint to check, not the actual
deciding factor. The case's real tension is fit (whose preferences this specific plan serves) versus
cost (which plan is cheaper) versus process (an itinerary neither parent actually wants written down
this precisely) — and the twist exists specifically to show that even the "cheaper plan wins"
argument is less solid than a first read suggests.

## Socratic questions

1. Plan A costs $2,601.65 and Plan B costs $2,817.36 — a real 8.29% gap, and both clear the $3,950 cap with room to spare. How would you explain to Gina why that gap is, or isn't, worth building a recommendation on by itself?
2. James and Elizabeth both say they hate a rigid daily schedule, but Challenge D5 requires an hour-by-hour written itinerary that gets sealed before they see it. Whose preference does Gina actually have to serve here — what they said they want, or what the case study requires her to produce?
3. The Anaheim Marriott Suites rate used for Plan B ($210/night) is the top of a real $102–$210 range — if the actual rate the family got booked into were closer to the bottom of that range, how would that change your recommendation?
4. Plan A anchors three shorter Universal days; Plan B anchors two full Disneyland days. Both options place five (or four) real activity days on the calendar — does "more days at more places" actually serve this family better than "fewer days, more depth," or is that just a number that sounds more generous?
5. After Henrietta's birthday twist, the gap between the two plans shrank from 8.29% to 4.03% — does that change which plan you'd book, or does it just make you less confident defending whichever one you already picked?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't move at
all after the twist is worth asking about directly: did Henrietta's birthday not matter, or did the
room already expect Plan A's lead to hold either way?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the discount-tier lookup (D1, 2% vs. 6%) or the order-of-operations trap in the agency
  fee (D3) was the place most Heroes actually got stuck.
- Whether Heroes engaged with the rigid-itinerary tension on their own or needed Anchor 2's prompt
  to surface it.
- Whether the Henrietta-turns-3 twist felt like a meaningful reveal or an expected, minor
  adjustment, given neither total came close to the cap even after it.

**A real, disclosed instability, for a facilitator who gets pushed on it:** Appendix E's MA4 (the
Anaheim Marriott Suites nightly rate) is the case's single largest modeling assumption, and it is a
genuinely live one. If a Hero (or the room) asks "what if the suite rate were lower," the honest
answer is that it matters a lot: flexing `plan_b_hotel_rate` down 50% (to $105/night, near the
bottom of the same cited $102–$210 range) drops Plan B's total to $2,417.69 — cheaper than Plan A's
$2,601.65, which **flips the cheaper plan**. No other modeling assumption in this case comes close
to flipping anything at the same flex range. This is disclosed, not eliminated, via a Category-F
`case.json.sensitivity_disclosure[]` entry. If pressed, tell the room the honest thing: Plan A's
real lead (8.29% before the twist, 4.03% after) is genuine at the rate this case uses, but it rests
on one hotel-rate choice that a real family's actual booked rate could reasonably land on either
side of.

## Standards Touched On

Percent · Decimal · Multiplication · How to find the percent of a number · How to multiply decimal
numbers · How to add decimal numbers · How to subtract decimal numbers · How to convert numbers to
percents · How to evaluate an expression with multiple operations without exponents (Order of
Operations) · How to add and subtract time · How to compare two or more values

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes are a family vacation budget decision, not personal illness,
death, or hardship.
