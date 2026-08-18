# Facilitator Guide — Foreign Travel

MS/HS | Adventure/LP | Anchor-ladder format (SPEC.md, Section 7, "The facilitator artifacts")
**Primary metric:** total transportation cost for the nine-day trip, in USD, Car vs. Rail ·
**Margin:** 10.65% (Rail cheaper) — see the Sensitivity note before Lessons Learned. (Refreshed
2026-08-18: a QA pass corrected three sources — S14, S17, S26 — against their live cited pages, and
in the same pass found and fixed a real modeling bug where Option A's total was missing the city
metro cost that case.md's own Appendix C says both options pay. Fixing the bug moved the verdict
back to Rail-cheaper at 10.65%, after an intermediate, buggy reading had shown Car-cheaper at
4.93%. Before that, the margin was Rail-cheaper at 3.81%, and before the 2026-08-18 data-decay
refresh that corrected S1/S15/S22/S23, it was 12.25%, Rail cheaper.)

Legacy source: `source/Y2/Session 5/Foreign Travel/`. The original docx had no Guide Notes file at
all (only the case docx and a garbled rental-car PDF screenshot — see `case.json.excluded_sources`
and `legacy_conversion_note`). This guide is authored fresh, with a genuine twist sourced during
this conversion (see **Twist**, below), and its soundness is checked against every stated
Modeling Assumption under both a sequential and a simultaneous reading (see **Soundness check**).

---

## Intro

Frame the format: this is a real family logistics decision, not a puzzle with one right answer.
Two sisters, one shared budget, nine days, no switching plans partway through. Don't open with
currency conversion — open with the kitchen table, the pizza, the two folders labeled RAIL and
CAR.

## Launch

Read the Overview aloud. Stop exactly where the case does — Katie alone at the table with the
folders, mid-argument, no resolution. Don't hand out any appendix yet.

## Anchor 1 — TAKE A STAND AND VOTE

"Who's riding with Natalie — car? Who's with Katie — rail?" Cold-call for a show of hands, no
reasoning allowed yet. Write the split on the board.

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to compare here?" Let the room arrive at *total cost*, not "which is
more fun" or "which is faster" — those are real considerations but not what Challenge 3 grades.
If the room lands on cost, name it explicitly and move on. If they land on convenience/flexibility
instead, that's a legitimate answer too — Anchor 3 should still pull the room toward *how would
you actually put a number on that*.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had every price in front of us, how would we build one number for each option?" Push for:
convert everything to one currency, add every leg, don't forget a cost just because it isn't a
ticket (fuel, a parked car's daily fees, a one-time sticker).

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming, and which assumptions actually move the answer?" Surface without confirming
yet: how many miles per gallon does the rental really get? How many metro rides will they actually
take? Which Channel crossing? Bank these — they're exactly Appendix A/C/D's Modeling Assumptions
A1, C1, and D1.

## Data Deep Dive

Hand out Appendices A-D now. Let Heroes build D1's cost table before anyone touches D2's itinerary.

## Twist

**Drop this at roughly the 15-minute mark**, after the room has a rough D1 total on the board but
before anyone has finished D2's full itinerary.

> "Quick gut check. Somewhere in the middle of this trip, both the UK and mainland Europe change
> their clocks for daylight saving — on the *exact same day*. Does that mean you need to adjust
> your London-to-Paris time math differently for the legs before that Sunday versus the legs
> after it?"

Let the room debate. The honest, sourced answer (Appendix E, S29/S30): **no** — because the UK and
the EU both spring forward on the *same date* (the last Sunday in March), the one-hour gap between
London time and mainland-Europe time is exactly the same before Day 3 and after Day 3. Nothing
about the cross-Channel offset actually changes over the course of this trip.

**What this invalidates:** any Hero's D2 itinerary that tries to "correct" the time-zone offset
partway through the week — adding or subtracting an extra hour somewhere around Day 3 because
"the clocks changed." That correction is the mistake this twist is built to catch; the real
content of the twist is that *nothing about the offset moves*, even though something in the world
visibly did.

**The follow-up (the whole point):** *"So what DID change on Day 3, if not the offset?"* Push the
room toward the real, narrower effect: only clock-times that fall inside the specific 1am-2am UK
window on the night of March 27-28 lose an hour of real time; every leg on this itinerary happens
well outside that window, so in practice this trip's schedule is unaffected either way. The
transferable skill: a fact that is real and true (the clocks changed) doesn't automatically mean
it changes *your specific calculation* — check before you correct.

**Soundness check (SPEC.md §6 / case-write §11):** read sequentially, day by day, against
Appendix E: on Day 1-2 the offset is UK-GMT-vs-Europe-CET, +1 hour; the clock change happens
overnight between Day 2 and Day 3; from Day 3 onward the offset is UK-BST-vs-Europe-CEST, still
+1 hour. The offset is identical on both sides of the changeover in a sequential reading. Read
simultaneously — treating the whole 9-day trip as one block and asking "what is the UK-to-Europe
offset for this trip" without regard to day-by-day sequencing — the answer is still a flat +1 hour,
because both zones' DST start dates are literally the same real-world date (S29 confirms UK, S30
confirms EU, independently sourced). No stated assumption is contradicted by another; the twist is
sound under both readings because the underlying fact (constant offset) is true regardless of how
you slice the week.

## Close (10 minutes left)

VOTE AGAIN. "Who's still with your original choice, and why? Who moved, and was it the total-cost
number or something else?" Ask specifically whether anyone's D1 total changed after Anchor 4/the
Data Deep Dive revealed a cost category they'd forgotten (a parked car's daily fees are the most
commonly missed line item in a cold solve).

## Lessons Learned

There usually isn't a single "objectively correct" choice between a rental car and rail for a trip
like this — both sisters have a real, defensible argument, and the honest number (10.65%) is close
enough that a careful Hero on either side should be able to hold their ground under questioning.
The case's real lesson is about *completeness*, not cleverness: the Hero who correctly prices every
idle-day cost of a parked car, or who correctly reads a published arrival time as being in a
different time zone than the departure, builds a trustworthy total. The Hero who skips a line item
because it "isn't really transportation" (a Congestion Charge, a parking garage, a one-time
sticker) builds a confident, wrong one.

## Standards Touched On

See `case.json.standards[]` and case.md's Appendix G — generated mechanically from
`readmodel/standards_spine.json`, not retyped by hand.

---

## Five Socratic questions

1. Your total for your chosen option includes several line items priced in a currency other than dollars. Walk me through exactly one of those conversions — what did you multiply, and why multiplication and not addition?
2. Appendix B's Eurostar London-to-Paris row shows a real journey time of 2 hours 16 minutes, but its posted departure and arrival clock times are 3 hours 16 minutes apart. Where did the extra hour go, and why doesn't that mean the train is actually slower than advertised?
3. If Option A's daily car-access fees in London and Paris (Appendix C) turned out to be $0 instead of what's given, would your recommendation change? By how much would the total cost gap close?
4. The Twist says the UK-to-Europe time offset never actually changes during this trip, even though the clocks visibly do. What's the difference between "the clocks changed" and "my calculation needs to change" — and where in your own D2 itinerary could you have gotten that wrong?
5. Your sister argues the other option is more "worth it" even if it costs more. What's one number from this case's appendices you'd need — that isn't given — to actually put a dollar value on that argument instead of just asserting it?

## The trap, named explicitly

A Hero builds D1's total cost table using only the "obvious" line items — the intercity tickets or
the rental-and-fuel — and skips the daily costs that only apply because a car is sitting parked
and idle in a city center (Appendix C's Congestion Charge/ULEZ/parking, or the one-time Crit'Air
sticker). This produces a confident, understated Option A total that looks far more competitive
with Rail than it actually is once every real cost is counted. The second, independent trap is
behavioral: most Heroes building D2's Channel-crossing legs will take the shortcut of subtracting
the two cities' *posted* departure and arrival clock times directly, as if London and Paris (or
Amsterdam, or Brussels) run on one shared clock — they will not stop to check Appendix B's explicit
note that mainland Europe sits a constant one hour ahead of the UK, so that shortcut silently
overstates every Channel-crossing leg's real travel time by an hour. That same hurried instinct
resurfaces around Day 3: on hearing that the UK's clocks spring forward at 1am on March 28 — inside
this trip's itinerary — most Heroes will assume the changeover itself must be added into their time
math and will "correct" the London-Europe offset somewhere around that day, when in fact the UK and
mainland Europe move their clocks on the identical calendar date, so the one-hour gap never changes
and no leg on this itinerary falls inside the actual 1am-2am changeover window to begin with.

## Sensitivity note

A family-travel logistics case with no illness/death/money-hardship content — no SPEC.md §6 flag
required on that front.

**Assumption-sensitivity disclosure (required reading before you defend the 10.65% margin):**
Three genuine Modeling Assumptions feed this margin — MA1 (rental fuel economy, 40 mpg), MA3
(6 metro rides/person/day), and MA4 (ferry crossing baseline, ~£120 each way) — and
`cases/foreign-travel/sensitivity_model.py`'s Tier 2 probe 5 flexes each by ±50%. Every other
number in this case (every appendix price, every distance, both exchange rates) is cited data, not
an assumption, and is stress-tested by probe 6 (data decay) instead, per
`skills/case-readiness/SKILL.md`'s P5 doctrine — do not "fix" a probe 5 finding by flexing cited
data; that is a different, mislabeled test. Run the script for the exact flip points before citing
a specific number here. **Refreshed 2026-08-18:** after the P6 data-decay research pass re-sourced
S1 (rental rate), S15 (NS Amsterdam-Groningen currency fix), S22 (Crit'Air), and S23 (London
parking) to current live prices, the margin narrowed from 12.25% to 3.81% (Rail cheaper), and all
three flex dials flipped the verdict at one end of their ±50% sweep, not just MA4 as before.
**Refreshed again, same day:** a further QA pass found that S14 (Paris-Amsterdam), S17
(Brussels-London), and S26 (Dover-Calais ferry) needed correcting against their live cited pages
(S14 → thetrainline.com advance fare, €124.72; S17 → seat61's stated one-way fare, £52.00, not the
£78 return fare the case had been using one-way; S26 → a genuinely GBP-denominated page, £80-£193
one-way) — but that same pass also introduced a real bug into `sensitivity_model.py`: Option A's
total silently stopped including the city metro cost that case.md's own Appendix C header says both
options pay ("Getting around inside London and Paris — both options use this"). That bug made the
case look like Car had flipped to the cheaper option (4.93%). This QA pass caught and fixed the
bug — Option A now correctly carries the same $171.43 metro cost as Option B — while independently
re-confirming S14/S17/S26 remain correct on direct re-fetch. The honest current picture: **Rail is
cheaper again, by 10.65%**, and only ONE of the three flex dials still flips the verdict at either
end of its ±50% sweep (ferry_crossing_gbp_each_way, MA4, at -50%) — rental_mpg_imperial and
metro_rides_per_person_per_day no longer flip it now that both options correctly carry the same
metro cost, since a change to either parameter moves both options' totals in the same direction by
comparable amounts. This is disclosed, not eliminated: the case's own premise (a trip booked only a
few weeks out, real crossing prices that genuinely vary) makes MA4's instability the honest picture,
not a defect to paper over.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch (Overview read aloud), stand/sit vote — no explanation (Anchor 1) |
| 3:00-10:00 | Position defense: "What are we even comparing?" (Anchors 2-3, land on total cost and a process) |
| 10:00-15:00 | Pressure-test: hand out Appendices A-D, let D1's cost table develop |
| **15:00** | **DROP THE TWIST** — delivered as a question, not a statement, and let the room argue it out loud first |
| 15:00-20:00 | Immediate recommit: does anyone's D2 itinerary actually change? Walk through why or why not |
| 20:00-30:00 | Threaded deep conflict: (1) the idle-car-cost trap (D1/D3), (2) risk/flexibility arguments that aren't captured in a dollar total, (3) how sensitive the 10.65% margin is to MA4 (the one dial that still flips it) |
| 30:00-45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

See `case.json.cohort_bands[]` (Full 12-20 / Compressed 6-11 / 1:1-pair 1-2) — three bands
declared per the cohort-bands floor in SPEC.md's "Cohort bands" subsection of Section 7.
