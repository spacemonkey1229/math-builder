# Guide Notes: AirBnb Or Landlord

**Case:** AirBnb Or Landlord · **Tier:** T2 · **Band:** MS-core · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (28 skills — percent-of-a-number,
percent premiums, decimal arithmetic, division/rounding for the monthly comparison, and two
required visual displays)

Legacy conversion, 2026-08-20, built from the original case study docx
(`source/Y3/Session 3/AirBnb/Case Study_ AirBnb Or LandLord.docx`, plus two market-data PDFs and
two AirDNA dashboard screenshots) onto the current 11-anchor ladder. No separate Guide Notes
document exists in the source for this case — this file is built from scratch. The family, home,
and household-budget facts are preserved from the source; the market figures were re-researched
for 2026 currency — see `case.json.legacy_conversion_note` for the full account.

**A note on sensitive content (SPEC §6):** this case touches a family's real household budget and
a brand-new mortgage payment. Keep the discussion on the math and the disclosed numbers, not on
facilitator or Hero personal-finance anecdotes.

## Intro

Frame the format: this is a real family's real income-property decision — not a worksheet with a
story stapled on. Name the opener — "Two ways to rent out a house nobody's living in anymore.
Same house, same mortgage, two totally different businesses."

## Launch

Read the Overview aloud, then Background's first two paragraphs (the two options, no Appendix
numbers shown yet). Ask: "Just from what you've heard — does nightly or monthly sound like the
obvious winner, or does it feel closer than that?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who's doing Airbnb? Who's doing the long-term lease?" Show of hands, no discussion yet. Record
the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Push on what "better" means here. Better as in *more total dollars per year*? Better as in *less
risk*? Better as in *less of the Daltons' own time*? Let the room sit in the ambiguity — "Is
anyone courageous enough to define 'better' before we start adding numbers?" Deliberately let it
feel underdetermined: "Wow, this is a harder question than it sounded."

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has picked a working definition of "better," ask them to name the actual steps:
gross revenue for each option, what gets subtracted (fees? cleaning? utilities?), one annual
profit number per option, then a comparison. Re-ask: "Given how we just defined 'better' — is
that still the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix F's four Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most. (Facilitator note: MA1, the furnished-rent
premium, and MA2, the average stay length, are the two that actually move the answer most — but
let the room guess first; MA1 is what the Twist leans on.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 and D2's profit breakdowns together as a room.

**The trap:** most Heroes will compute Airbnb's *gross* revenue ($37,700 — nearly 25% more than
the traditional option's gross rent), stop there, declare Airbnb the clear winner, and never
apply the 15.5% host fee or subtract the extra utility cost the Airbnb option carries that the
traditional option doesn't. Gross Airbnb revenue looks like a landslide; net Airbnb *profit* is
actually the smaller of the two numbers. Cold-call on this specifically: "Is $37,700 the number
that ends up in the Daltons' pocket, or is it the number before some real deductions?"

## Twist — drop this at roughly the 15-minute mark

Deliver slowly, with pauses:

"Everyone's Airbnb profit number so far only counts dollars. But the Daltons plan to clean the
place themselves — no cleaning service, no line item for their own time. Real number: at 58
bookings a year, two hours each, that's 116 hours of Dwayne and Wendy's own unpaid labor. That's
not a weekend project. That's almost three full 40-hour work weeks a year, spent turning over a
house they don't even live in anymore."

**Facilitator-only.** This doesn't change either dollar total — D1's $14,112.50 and D2's
$16,724.60 stand exactly as computed, still an 18.5% margin (`case.json.balance.margin_pct`) in
the traditional rental's favor. What it changes is what "profit" means. A Hero who was
defending Airbnb purely on the dollar total now has to answer a harder question: is $14,112.50 in
exchange for 116 hours of their own labor actually a *better* number than $16,724.60
(`case.json.derived.profit_difference_annual_usd` = $2,612.10 more) for near-zero ongoing labor?
The case never actually prices Dwayne and Wendy's own cleaning time — the room should notice that,
and that's the point.

Ask: "You now have 60 seconds. Does this change your recommendation — or not?" Then, the
follow-up that matters more than the vote: **"What just broke in your original model? Was your
math wrong — or was it just missing a cost the case never put a dollar sign on?"**

Do not hand over a "correct" answer. A reasonable family might genuinely value being hands-on and
in control of their own property over an extra $2,612.10 a year — that's the real, transferable
tension, not a trick.

**Twist soundness check (SPEC §6):** checked against every stated Background/Appendix fact and
Modeling Assumption, read both sequentially and simultaneously — it introduces no new figure that
contradicts an earlier one, only a second, real, disclosed lens (the labor-hours figure is pure
arithmetic from Appendix F/MA2's own 58-bookings-per-year derivation) on a cost the case never
priced. It holds under both readings and does not flip either D1 or D2's dollar total.

## Immediate recommit

Re-vote immediately. "Did the labor-hours reveal change your hand — or did it just change *why*
you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'better' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

The original case's own Challenges asked students to compute "anticipated annual profit" for each
option but never itself resolved which one was larger — that ambiguity is preserved and is exactly
where this case's real tension lives. This conversion adds two things the original case's own
structure couldn't force: (1) a **real** 2026 furnished-rental premium and Airbnb fee structure,
both of which materially changed since the source case was written (Airbnb's fee model changed
entirely in 2026), and (2) the labor-hours Twist, which the original case's own numbers already
contained (58 bookings × 2 hours) but never surfaced as a discussion point.

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's own
numbers, not general opinion.

1. Airbnb's gross booking revenue ($37,700) is nearly 25% more than the traditional rental's gross rent ($30,318.60) — so why does Airbnb still end up with the *smaller* net profit?
2. Neither option's monthly profit alone covers the Daltons' new $2,300 second-mortgage payment — does that change which option you'd recommend, or does it not matter since both are close?
3. This case's furnished-rental premium (15%) is the real sourced *low end* of a 15%–30% range — what would the traditional rental's profit be at the *high* end, and would that change the winner?
4. At 58 bookings a year and 2 hours per cleaning, the Daltons spend 116 unpaid hours a year turning over the Airbnb — what would Airbnb's real profit be if they instead paid someone $30/hour to do it?
5. Appendix B shows two different data providers reporting different Boise occupancy rates for the same period (47.8% vs. 51–67%) — which one does this case use, and what happens to Option A's profit if the higher figure is the true one?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote — no explanation (Anchor 1) |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just bigger" (Anchor 2) |
| 10:00–15:00 | Pressure-test the models: "Whose profit number is most fragile?" (Anchor 3, Anchor 4, start of Data Deep Dive) |
| **15:00** | **DROP THE TWIST** — the 116-hour self-cleaning labor reveal, delivered slowly, with pauses |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke?" |
| 20:00–30:00 | Threaded deep conflict, two named threads: (1) dollars-per-year vs. dollars-per-hour-of-labor; (2) control/flexibility (Airbnb) vs. predictability/low-effort (traditional lease) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Standards Touched On

See `case.json.standards[]` (28 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: percents (of a number, and converting a premium into a multiplier), decimal
arithmetic across all four operations, division and rounding for the monthly comparison, currency,
and two required visual displays (bar graph, pie chart).

## Cohort Bands

See `case.json.cohort_bands[]`:

- **Full (14–20):** Anchors 2–3 run as written; the room splits into an "Airbnb upside" faction
  and a "traditional-rental stability" faction before the labor-hours Twist forces everyone to
  weigh the Daltons' own unpaid cleaning time.
- **Compressed (7–13):** Anchors 2–3 combine into one pass; D4's two visual displays are worked as
  one shared example (one option) instead of every Hero building both independently.
- **1:1 / pair (1–2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the guide plays devil's advocate directly, arguing whichever side the
  Hero didn't pick.
