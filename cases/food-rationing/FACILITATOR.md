# Facilitator Guide — Food Rationing

**Content note:** this case involves a family stranded at sea, a chronic illness (Type 2 diabetes),
and a child's ongoing physical suffering (seasickness). Flag this for the discussion lead before
running it — per SPEC.md section 6, the math is about *protection* (stretching a real food supply,
protecting a real medical condition), not about optimizing anyone's death, and the discussion
should be run with that in mind.

## The balance argument

**Argument for A (Equal):** Equal rationing is verifiable and immune to being wrong about any one
person — every family member, including 70-year-old John and 2-year-old Chance, gets the identical
2,000 kcal/day, so nobody has to trust an age-and-activity table (or Tamara's judgment) about whose
body needs less. This is real international maritime practice, not an invented fairness norm — the
LSA Code's own minimum liferaft ration standard issues the same 10,000 kJ to every occupant
regardless of age or health (case.md Appendix G). It also protects against the real risk that any
one family member's published "need" turns out to be wrong under actual conditions.

**Argument for B (Need-based):** Matching each person's own published daily calorie need — from the
same official USDA/HHS table Option A's own reference number comes from — stretches the family's
real 51,650 kcal supply about 19% further (roughly one additional full day of food), because
Chance (2) and a currently sedentary, seasick Easton (9) both have genuinely lower calorie needs
than a flat 2,000-kcal adult reference assumes. John's diabetes is protected either way — his
need-based ration is his own full 2,200 kcal, prioritizing the consistency his real medical
management depends on, not a cut.

**The margin:** Option A lasts 51,650 ÷ 10,000 = 5.165 days at full recommended calories. Option B
lasts 51,650 ÷ 8,400 = 6.1488 days. Margin = 19.05% — Option B lasts longer, but the margin sits
close to SPEC section 2's 20% cap and is **not** robust to a ±50% flex of the case's own stated
assumptions (see `sensitivity_note` in case.json and `sensitivity_model.py`). Do not treat 19.05%
as a settled, robust number in front of a room — it is real, current best math, not a guarantee.

## Five Socratic questions

1. Your plan claims to protect Chance and Easton, but Option B literally gives them fewer calories than Option A's flat 2,000 — is "need-based" the same thing as "generous," or did your intuition about fairness just get the arithmetic backwards?
2. Option B stretches the supply about 19% longer than Option A — call it one extra day. If the ship doesn't come for a month, does one extra day of food change your answer at all?
3. John's ration is the same 2,200 kcal either way — so what is Option B actually doing for him, if not giving him more food?
4. Easton's ration in Option B assumes he's "sedentary," not just seasick — what happens to your whole plan if he starts moving around and eating normally again on day 3?
5. If the family finds the hidden emergency ration pack from the Twist, whose ration does that 2,390 kcal actually go to — everyone equally, or wherever it's needed most?

## The trap

**The values trap.** Heroes will instinctively assume "ration by need" means giving the more
vulnerable family members **more** food, because that's the compassionate reflex. The real math is
the opposite for Chance and Easton: their *actual* recommended daily calories are lower than a flat
adult reference, so a genuinely need-based plan gives them **less** than an equal share, not more —
only John escapes the equal share unreduced, and even his protection is about consistency, not
quantity. A Hero who designs a "need-based" plan by *increasing* the vulnerable family members'
rations has the ethics and the arithmetic backwards at the same time, and will not be able to make
Appendix F's numbers support their own pitch.

**The arithmetic-execution trap (watch for this one during work time, not just discussion).** Under
real time pressure, a working Hero is at least as likely to fumble D4's mechanics as to fall into
the values trap above: (a) mis-adding Option B's five separate daily figures (2,000 + 2,200 + 1,600
+ 1,600 + 1,000), or computing the percent difference against the wrong base (dividing by the wrong
option's total flips whether the reported margin reads as "B ahead of A" or "A ahead of B" even when
the underlying subtraction is right); and (b) quietly un-excluding Appendix D's disclosed omissions
(MA4 — the small-quantity produce, spices, and condiments) back into the total supply "to be
thorough," inflating the 51,650 kcal figure without realizing the case already addressed why they're
left out. Either error produces an internally-consistent-*looking* but wrong D4 table. If a Hero's
D3 plan and D4 comparison don't agree with each other, check these two first before assuming it's
the values trap.

## Sensitivity note

The 19.05% margin is real but close to the SPEC 20% cap. Two dials are genuinely flexible, not
cited data: Easton's Option B target (MA1, 1,600 kcal — a re-classification choice, not a sourced
figure) and Option A's flat reference (MA2, 2,000 kcal — the FDA's general reference, but choosing
*to use it* is the case's own modeling choice). A ±50% flex on either one meaningfully moves or
flips the margin — see `sensitivity_model.py`'s `FLEX` list and `case.json.sensitivity_note`. Do
not present 19.05% to a room as more stable than it is.

## Intro

Frame the format: this is a real, previously-run Acton Academy case (the original Murray family
scenario). Read the Overview aloud, or show a short clip of open-ocean storm footage as the launch
video, before revealing the Dilemma.

## Launch

Read case.md's Overview and Background aloud. Do not show Appendix D/E/F numbers yet.

## Anchor 1

TAKE A STAND AND VOTE. No reasoning yet, just commit.
*"Tamara, you have 30 seconds. Equal or need-based — what do you choose?"* Call on 2–3 Heroes
rapidly, then: *"Stand if you chose equal. Sit if you chose need-based."*

## Anchor 2

WHAT IS THE PROBLEM WE'RE SOLVING?
*"Is it just as simple as deciding which option is more fair, or is there something else we need
to consider?"* · *"What do you mean by 'equal'? What do you mean by 'need'?"* · *"Is this the right
question?"* Let confusion grow: *"Wow, this is a challenging problem."*

## Anchor 3

WHAT IS THE PROCESS?
*"If we go through this process and find the calorie data, how will we decide?"* · *"Is our
question still the right question?"* Re-ask after the group commits to a process.

## Anchor 4

WHAT DON'T WE KNOW?
*"Do we need to make any assumptions to answer our key question? Which ones are critical?"* — this
is where the group should surface that nobody knows how many days to ration for. Do not resolve it
yet; let the group feel the gap.

## Data Deep Dive

Now, and only now, hand out Appendices D, E, and F. Let Heroes compute Option A's and Option B's
days-of-coverage live if time allows.

## Twist

At roughly the 15-minute mark: *"A week passes. No ship comes."* (Pause.) *"Easton is now barely
keeping anything down at all."* (Pause.) *"John's blood sugar is becoming harder to manage."*
(Pause.) *"Then, tucked behind a bulkhead panel, Tamara finds something the family forgot was
there: a sealed, waterproof emergency ration pack — the kind every liferaft is required to carry."*
Reveal the real number: a standard LSA Code liferaft ration pack holds 10,000 kJ, about **2,390
kcal** (case.md Appendix G / `sensitivity_model.py`'s `evaluate_twist()`). Then: *"You now have 60
seconds. Are you changing your plan — or not?"*

This invalidates a position some of the room will hold confidently: that either plan is comfortably
enough food, or that one extra unaccounted person-day of supply doesn't matter. It does not make
either option obviously correct — 2,390 kcal is real, but it is not close to enough to fully solve
either plan's shortfall against a month-long wait. Follow-up: *"What just broke in your original
model? Were you wrong — or just missing information?"*

**How the found ration is actually used — state this explicitly if a Hero asks "does it matter who
gets it?" (it does, and this is not left ambiguous):** each option's own philosophy determines how
the family would use a single, one-person pack. Option A's strict-equality philosophy means the
family would split even this pack five ways, same as everything else — it just extends the flat
daily total a little. Option B's need-based philosophy means the family would give the whole pack to
Easton specifically, since he's the person the Twist's new information just identified as most at
risk — fully covering his draw from the shared pool for as many days as the pack alone can sustain
him, which frees up more of the regular supply for everyone else and extends Option B's runway by
proportionally more than Option A's. This is why the two plans pull *further* apart after the Twist,
not closer together (`sensitivity_model.py`'s `evaluate_twist()`) — a real, disclosed mechanic, not
an unstated convention.

## Close

Vote again. *"Did we ask the right question?"* · *"What math was new to you, and how did you attack
it?"* · *"If you were given a similar case study next time, what would you do differently?"*

## Lessons Learned

Math doesn't remove hard decisions — it exposes them. Two mathematically defensible plans can
disagree about who eats less, and the numbers alone don't settle which plan is *right* — only which
plan does what it claims to do.

## Standards Touched On

See case.md Appendix J.

## 45-Minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch: *"Equal or need-based — what do you choose?"* 30-second commitments, stand/sit vote, no explanation yet. |
| 3:00–10:00 | Position defense. *"Convince us why your plan is better, not just fair."* · *"Who did you prioritize in your math?"* · *"What assumption did you make about rescue timing?"* Cold-call: *"You said equal — walk me through what happens to your supply on day 6."* |
| 10:00–15:00 | Pressure-test the models. *"If rescue takes 30 days, whose plan fails first?"* · *"If rescue comes in 3 days, whose plan looks overcautious?"* · *"Which plan is most fragile to being wrong about Easton's recovery?"* |
| **15:00** | **DROP THE TWIST** (see above) — deliver it slowly, with pauses. Then: *"You now have 60 seconds. Are you changing your plan — or not?"* |
| 15:00–20:00 | Immediate recommit. *"Who is NOT changing their plan? Who is completely reversing?"* · *"What just broke in your original model? Were you wrong — or just missing information?"* |
| 20:00–30:00 | Deep conflict, threaded. **Thread 1 (Optimization vs. Fairness):** *"Should you maximize total days of coverage, or equal treatment regardless of the cost in days?"* **Thread 2 (Uncertainty):** *"Nobody knows if rescue is 1 day or 30 — who built their plan around hope, and who built it around the worst case?"* **Thread 3 (Role-based obligation):** *"Are you answering as Tamara the mother, or as Tamara the person responsible for keeping everyone alive as long as possible? Does that change who gets the sedentary-column ration?"* |
| 30:00–38:00 | Leadership & trust layer. *"Do you tell the family exactly how the rationing math works, including that Easton and Chance are getting less?"* · *"What happens if they find out the ration was calculated, not just guessed?"* |
| 38:00–43:00 | Collapse the room. *"Raise your hand if you're confident your plan is right."* (Expect hesitation.) *"Who could defend the opposite plan?"* · *"What would it take to convince you you're wrong?"* |
| 43:00–45:00 | Final curveball and exit. *"You're rescued on day 7 — everyone survives, but Easton spent the last two days severely underfed because your plan didn't account for how long his seasickness actually lasted."* Then: *"Was your decision good? Do outcomes determine a good decision, or does the process?"* |

**Facilitation notes:** stay neutral (only "why?" / "push that further" / "who disagrees?"); use
names constantly; let silence work after the Twist; force tradeoffs if a Hero hedges ("you don't
get both — choose").

## Cohort bands

See `case.json.cohort_bands[]` — Full (12–20), Compressed (6–11), 1:1/pair (1–2), each with what
changes at that size.
