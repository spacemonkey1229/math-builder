# Guide Notes: Cold Chain

MS | Guide Notes | Heroes Academy | 2026-27
**Tier:** T3 (MS stretch / HS entry) · **Primary metric:** doses delivered within +2 °C to +8 °C · **Margin:** 17.1% (stable — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, today we're doing something they do at Harvard and at Acton Business School. I'm going to call on one of you to open. You'll lay out your position and defend it, and the rest of us are going to take it apart. There is no answer key for this one. I don't have the right answer either.

## Launch

Show a photo of a health worker carrying a cold box on the back of a motorcycle. Ask: *"How much do you think is inside that box, in dollars?"*

Let them guess. Then tell them: a $102 box can hold about **$971 to $1,200** of vaccine (6 L ÷ 2.1 cm³/dose ≈ 2,857 doses at $0.34–$0.42/dose). The container is worth about 9–10% of what's inside it.

> Adaeze has 9,000 doses, six villages, a 1,200 km circuit, and $420. Two of those villages have never seen a truck.
> **Hero name — what do you do? Open for us.**

---

## Anchor 1 — Take a stand and vote

Order A or Order B. No reasoning yet.

Hands up for A. Hands up for B. Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What is the actual question here? Say it in one sentence.
- Is it "how many doses can we carry"? Is it "how many children get vaccinated"? Is it "how many doses don't spoil"? **Those are three different questions and they have different answers.**
- Someone will say "we want to help the most people." What do you mean by *most*? Most doses, or most villages?
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Wow. This is a challenging problem."* Do not rescue them.

**The trap to let them walk into:** Order A carries enough capacity to serve every facility's full stated need — it does **not** drop any village. So most learners will assume "A serves everyone, A wins," and stop there. The real trap is arithmetic, not equity: Nyamirama's whole 800-dose shipment arrives spoiled **no matter what** — because box 3's raw, unmodified cold-life rating (132.3 h) is already less than Nyamirama's arrival time (134 h). No opening-cost adjustment, generous or stingy, changes that. A learner who assumes "if we're gentler about lid openings, Nyamirama gets saved" is wrong, and it's worth making them test it (Anchor 4).

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we just look at which order carries more litres, are we done? Order A now carries enough for every facility. Is the case over?
- If we end up with 8,200 of one thing and 7,000 of another, how will we decide? What's our tiebreaker *before* we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What is missing that we'd need to answer this properly?
- Appendix F gives you the assumptions. Do you believe them? **Have them actually try opening-cost values of 2, 4, and 6 hours per stop and check whether Nyamirama's status ever changes.** (It doesn't — that's the point, and it's worth them discovering it themselves rather than being told.)
- The water content of the 0.4 L pack isn't published. Does that matter? Where does it enter your calculation?
- What are we assuming about whether a village that receives spoiled vaccine this quarter gets a resupply next quarter?

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**The geometry finding.** Have them compute volume, surface area, and SA:V for all five containers in Appendix A. It comes out clean and it is real:

| Container | Volume (cm³) | Surface area (cm²) | **SA : V** | Cold life (h) |
|---|---|---|---|---|
| RCW4 | 30,631 | 5,906 | 0.1928 | 30.3 |
| RCW8 | 74,003 | 11,043 | 0.1492 | 57.9 |
| AOV ACB-264SL | 133,444 | 15,858 | **0.1188** | 132.3 |
| RCW25 | 194,860 | 20,385 | 0.1046 | 134.6 |
| Blowkings CB-20-CF | 252,436 | 24,270 | **0.0961** | 138.0 |

**Every single one is in order.** As surface-area-to-volume falls, cold life rises — across five real products from four different manufacturers. Heat comes in through the walls; cold is stored in the middle. Big boxes win on physics.

> **Do not overclaim this, and don't let them either.** SA:V *orders* the five containers correctly; it does not *predict* cold life. Multiply cold life by SA:V and you get 5.84, 8.64, 15.72, 14.08, 13.27 — a 2.3× spread, not a constant. And with only five products, the SA:V ordering is identical to the plain size ordering, so geometry is confounded with volume. Appendix E hands them the rival explanation: a vacuum panel at 0.004 W/m·K against foam at 0.03 is a 7.5× difference that would swamp any geometric effect.
>
> Ask: *"Can you tell the difference between 'bigger boxes hold cold longer' and 'these particular boxes have better insulation'? What data would you need to separate them?"* The honest answer is that you cannot separate them from Appendix A alone — and noticing that is a better outcome than getting the ratio right.

**The route plan.** Appendix F now states it explicitly: Order A's 4 boxes split 3-truck / 1-moto. Order B's 2 boxes are both on the truck.

- Order A: 4 × $102.21 = **$408.84** (under $420) · truck capacity 3 × 2,857 = 8,571 L (≥ 7,000 needed) · moto capacity 1 × 2,857 = 2,857 (≥ 2,000 needed). **Every facility's full demand is met: 9,000 doses delivered, zero shortfall.**
- Order B: 2 × $128.00 = **$256.00** · truck capacity 2 × 9,523 = 19,047, far more than the 7,000 truck demand needs. **7,000 delivered. Bulera and Nyamirama: zero.**

Ask: *"So Order A delivers everywhere and Order B doesn't. Why is this even a discussion?"* — hold that question; the cold-life ledger below is the answer.

**The cold-life ledger** (Assumption 1: 4 h per opening, deducted up front; Assumption 0: 3 truck boxes / 1 moto box).

- Truck boxes (Order A): worst case 2 openings each → 132.3 − 8 = **124.3 h** effective. Last truck stop, Kitovu, is at hour 96 — **28.3 h of slack.** All four truck stops in spec.
- Moto box (Order A): 2 openings → 132.3 − 8 = **124.3 h** effective. Bulera at hour 118 — **in spec, 6.3 h of slack.** **Nyamirama at hour 134 — excursion by 9.7 h.**
- Order B boxes: 2 openings each → 138 − 8 = **130 h** effective. Last stop, Kitovu, at hour 96 — **34 h of slack.** All four in spec, always zero excursions — Order B never gets close to its limit.

**The result.**

| | Order A | Order B |
|---|---|---|
| Facilities reached | **6** | 4 |
| Doses delivered | **9,000** (full demand) | 7,000 |
| Facilities receiving zero | **0** | **2** (Bulera, Nyamirama — 2,000 doses of need) |
| Arriving spoiled (excursion) | **800** (Nyamirama only) | 0 |
| **Doses in spec** | **8,200** | **7,000** |
| Cost | $408.84 | $256.00 |

**A wins by 1,200 doses — 17.1%.** Comfortably inside the 20% balance cap, and — see below — stable under any reasonable version of Assumption 1. A spends $152.84 more, reaches every village, and *still* cannot save Nyamirama. That last fact is the crux of the case, not a flaw in it.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"It's hour 96. The truck has just left Kitovu."*
>
> (pause)
>
> *"The rain that started in the storeroom hasn't stopped. The district engineer calls. The bridge on the Bulera road is under water."*
>
> (pause)
>
> *"The motorcycle can still get through — but not the direct way. The detour adds **nine hours**."*
>
> (pause)
>
> *"And Nyamirama has just called in. They have thirty-one suspected measles cases. They are the reason this circuit exists."*

> **Facilitator only — read before you drop this, do not read aloud.** The exact tie below assumes the case's default opening cost of 4 h/opening (Assumption 1). It is NOT invariant across the full 2–6 h range the way the base case is: at c = 4–6 h, both motorcycle stops excurse and you get the tie described below. But at c = 2 h, Bulera's twist-day arrival (hour 127) is still inside its effective cold life (132.3 − 4 = 128.3 h — 1.3 h of slack survives), so **the twist does nothing at all** and Order A keeps its full 8,200-vs-7,000, 17.1% margin. The crossover is c ≈ 2.65 h. If your room tested c = 2 at Anchor 4 and someone remembers it, don't paper over this — say so, and treat it the way the case wants you to treat every sensitivity finding: as a stronger answer, not a gotcha on you. (Verified in `sensitivity_model.py`'s FLEX sweep; the case's own `stability` field in `case.json.balance_test` records the same numbers.)

Now: **Bulera moves from hour 118 to hour 127. Nyamirama moves from 134 to 143.** Against the moto box's 124.3 h of effective cold life, **both** motorcycle stops are now excursions — Bulera's 1,200 that were safe a moment ago are gone too. Order A's in-spec delivery falls from 8,200 to **7,000 — a dead tie with Order B.** *(True for the case's default c = 4 h, and for c = 5 or 6 h — see the facilitator note above for c = 2 h.)*

> *"You have 60 seconds. You paid $152.84 more, and after this, you have exactly what Order B always had. Are you changing your plan — or not?"*

## Immediate recommit

- Who is **not** changing? Say why out loud — "I'd rather have tried" is a real answer, not a weak one.
- Who is completely reversing?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one. It's the transferable skill.)
- Who built a plan whose entire advantage depended on the weather holding?

Watch for the learner who says *"the tie doesn't mean it was a wash — Bulera nearly made it and B never had a chance at it."* That's the strongest read on the board: a tie in the totals is not a tie in what each plan attempted.

---

## Deep conflict — three threads (20–30 min)

**Thread 1 — Guaranteed reach vs. an unbeatable failure.** Order A serves every village's full need and still cannot save Nyamirama — not because of a planning mistake, but because the box's raw rating (132.3 h) is less than the trip (134 h). Order B never attempts Nyamirama at all. *"Is it better to try and fail at the one you can't save, or not try?"* Push: *"Which of those is actually a choice Adaeze is making, and which is physics she can't change?"*

**Thread 2 — Fragility.** Which plan survives being wrong? Order B has 34 hours of thermal slack and never leaves the truck. Order A's tightest margin is 6.3 hours, at Bulera, riding on weather holding. *"Which plan would you pick if you had to run this circuit twelve times?"* — the answer is often not the one that wins once.

**Thread 3 — Who is Adaeze accountable to?** She reports doses administered *and* doses wasted. Order A guarantees her a wastage line — a fixed, sourced, unavoidable 800 doses. Order B guarantees a clean report and two villages that never appear in it at all. *"Is a guaranteed small failure worse to report than a large one you simply didn't attempt?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Order A or Order B?"* Two or three learners, fast. Then stand/sit vote. No explanation yet, just commit. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just kinder."* · *"Which villages did you count?"* · *"What did you assume about the rain?"* Then press: *"You chose B — say out loud which villages get nothing."* |
| **10:00–15:00** | Pressure-test the models. *"Whose plan is most fragile?"* · *"How many hours of slack does your plan have?"* · *"Who built a plan that only works if they're right?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with the pauses. Finish with: *"Sixty seconds. Are you changing your plan — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* · *"Were you wrong — or missing information?"* |
| **20:00–30:00** | The three threads: guaranteed reach vs. unbeatable failure · fragility · who Adaeze is accountable to. |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the board from Anchor 1. Who moved?
- We asked ______ as our key question. Was it the right question?
- Was this case challenging? Why?
- What math was new to you here, and how did you attack it — did you Google it, ask a fellow traveller, something else?
- If you got a case like this next time, what would you do differently?

## Lessons Learned

The physics was never in doubt: bigger boxes hold cold longer, and the surface-area-to-volume ratio *orders* five real products correctly (though it does not predict cold life precisely — see the confound noted in the Data Deep Dive). The math had a clean answer. **The decision still didn't.**

Order A's win margin — 8,200 vs 7,000, 17.1% — is not a fragile number, *with respect to Assumption 1.* It holds for any lid-opening cost from 2 to 6 hours; Nyamirama's excursion is not a modeling artifact, it is a structural fact (its rated cold life is shorter than its trip, even before any opening penalty is applied at all). What *is* fragile is the twist: a nine-hour detour erases the entire margin and produces an exact tie for c ≥ 3 h — but at the low end of the case's own certified range (c = 2 h) the twist changes nothing (see the facilitator note before the Twist section). **A case can have a robust base result and a fragile margin of victory at the same time** — those are different properties, and this case has both.

There is a third layer, for a room that's ready for it. Assumption 2 (treating cold life as the full in-spec time) is named in Appendix F as an *optimistic* simplification. Tighten it — say, only half of rated cold life counts as reliably in-spec, closer to how a real warming curve leaves +8 °C before it reaches +10 °C — and Order A's base-case margin collapses to a tie (both orders land at 3,950 doses). Loosen it instead and Order A's lead widens past the 20% balance cap (28.6% at +50%). Appendix F invites exactly this stress test ("if you think that matters, model it and show what changes") — a student who runs it is doing the advanced work the case is built to reward, not breaking it. Don't volunteer this unless the room is already pushing on Assumption 2 themselves; it's an extension, not a required beat.

Every learner who worked "doses delivered" as the metric got a defensible answer. So did everyone who worked "villages fully reached." They are different answers, and the difference was decided before anyone touched a calculator — in the sentence they wrote down at Anchor 2.

Real quantitative work is like this. Choosing the metric *is* the decision. The arithmetic just tells you what you already chose.

---

## Standards Touched On

**New coverage** (zero prior cases in the standards matrix before this case): `Prism` · `Absolute Value` · `How to evaluate an absolute value expression`

**Also exercised:** Volume · Surface Area · Ratio · Unit · Percent · Decimal · Scientific Notation · Measurement · Distance · Weight · Data · Bar Graph · How to find the volume of a prism · How to find the surface area of a prism · How to find equivalent ratios · How to convert an amount from one unit to another unit · How to convert an amount with compound units · How to convert between units of time · How to find the percent of a number · How to convert numbers to percents · How to multiply decimal numbers · How to divide decimal numbers · How to write a number in scientific notation given its standard notation · How to find the mean of a set of data · How to compare two or more values · How to find elapsed time

---

## Facilitator note — sensitivity

This case involves children going unvaccinated and a measles outbreak. The stakes are real and that is the point, but the twist names 31 suspected cases in a village a learner may have just voted to under-resource. Some learners will feel that. Give it room; don't rush past it into the arithmetic. The discomfort is the lesson working, not the lesson failing.
