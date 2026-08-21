# Facilitator Guide — Bathroom Problems

**Content note:** this case opens with a household emergency (a flood) and a real sibling injury
from a collision during a rushed morning. Per SPEC.md section 6 this is ordinary family-conflict
realism, not a health/death/financial-hardship weight — no special framing is needed, but a
discussion lead should be ready for a Hero to bring up their own sibling/bathroom conflicts, which
is exactly the kind of personal engagement this case is built to invite.

## The balance argument

**Argument for A (The Round-Robin):** Procedurally simple and unimpeachably fair in the sense that
matters most to a room full of teenagers — nobody is ever permanently stuck with the worst
position. Every family member gets the exact same 8.75-minute slot (70 minutes ÷ 8 people), and
next week the person who went last this week goes first. No judgment calls about whose need is
"more real," trivial to enforce, and immune to an argument breaking out over whose hair actually
takes 36 minutes.

This isn't just a nicety — it's a real, checkable defect in Option B. The Priority Line's turn
order (earliest leave-by time first, ties broken by lower total need) never rotates: it produces
the same order every single day. Marta has the latest leave-by time (8:00 AM) and, within that
tier, the highest remaining need — so she is *permanently* last, every morning, by the rule's own
mechanics, not by bad luck. Trace her actual finish time and it lands at **8:00:00 exactly** — her
own leave-by time, with zero buffer against any real-world slippage upstream. And because the
family's total shower demand (68 min) outstrips the water heater's hot-water supply (28 min, from
Appendix C's First Hour Rating), whoever showers last gets cold water — which under the Priority
Line's fixed order is, every single morning, Marta. The Round-Robin's rotation means no one is
stuck in that exact position two weeks running.

**Argument for B (The Priority Line):** Delivers 70.0 "useful minutes" to the family instead of
63.5 — the Round-Robin wastes 6.5 minutes/day on family members like Thomas (needs 3, gets 8.75)
and George (needs 8, capped at 8) who don't need their full flat slot, while badly shortchanging
Heather (8.75 of her stated 57 — just 15.4%) and Marta (8.75 of her stated 47 — 18.6%). Under the
Priority Line, every single family member gets exactly the same 30.8% of their own real need met
— arguably a more meaningful definition of "equal" than an equal number of raw minutes that means
something completely different to an 11-year-old than to a 16-year-old getting ready for school.

**The margin:** Useful minutes, Option A = 63.5, Option B = 70.0. Margin = (70.0 − 63.5) / 63.5 =
**10.24%**, comfortably inside SPEC section 2's 20% cap. It is real, current best math for this
case's own stated Modeling Assumption (MA1) — not a guarantee; see Sensitivity note below.

## Five Socratic questions

1. Under the Round-Robin, Thomas gets 8.75 minutes and only needs 3 — where do those extra 5.75 minutes actually go? Is "wasted time" the same kind of unfairness as "not enough time," or a different one?
2. Every person gets exactly 30.8% of their own need met under the Priority Line — is that actually "equal," or does calling it equal just hide that Marta gets 14.5 real minutes and Thomas gets under a minute?
3. Heather's Round-Robin slot (8.75 min) covers barely a fifth of the time she says hair and makeup take her (36 min alone). If she just... doesn't finish, what actually happens at 7:40?
4. You built your schedule around an 8:00 AM deadline for Marta, Olivia, and Thomas — what if Marta's actual workday starts earlier than she told the family, and 8:00 isn't a hard deadline after all?
4b. Under the Priority Line, is Marta's position in line — dead last, every single morning — a coincidence, or does the tie-break rule itself guarantee it? Under the Round-Robin, is anyone guaranteed to be dead last forever?
5. Grandma Polly and Grandpa Ben just moved in with their own suitcases. Whose 25 minutes do you cut to make room for two more people in the same 70-minute window?

## The trap

**The "equal minutes = fair" trap.** Heroes will instinctively grab the Round-Robin because "equal
time" sounds obviously fair, and will build their D4 comparison assuming Option A must therefore
be the more equitable choice. The real math runs the other way on the metric this case actually
grades: equal *minutes* produces wildly unequal *outcomes* (Heather at 15.4% of her need vs. Thomas
at over 100%), while the needs-weighted option produces the one number that actually is identical
for every family member — the *percentage* of need met (30.8%, universally). A Hero who never
separates "equal minutes" from "equal treatment" will not be able to explain, using their own D4
numbers, why the option that hands out unequal raw minutes is the one delivering equal-percentage
outcomes.

**The averaging trap (watch for this during work time).** A Hero computing the *average* percent
of need met across the family under Option A will get a deceptively high number (over 70%,
because Thomas and George's huge percentage surpluses drag the average way up) — much higher than
Option B's uniform 30.8%. This is real arithmetic, not a mistake, but it answers a different
question than D4 actually asks (total *useful* minutes, not average percent-met) and a Hero who
leads with the average will present a much rosier picture of Option A than the case's own primary
metric supports. Ask directly: "does averaging in Thomas's 291% surplus tell you anything true
about whether Heather got what she needed?"

**The "uniform percentage = fair" trap.** A Hero who computes Option B's uniform 30.8%-of-need
figure and stops there will conclude the Priority Line treats everyone identically. It doesn't:
that figure describes *minutes allocated*, not the fixed, non-rotating turn order that produces
them. Trace the actual schedule (D1) and it's mechanically guaranteed — not incidental — that
Marta finishes last every single day, with zero buffer against her own 8:00 AM leave-by time, and
showers entirely in cold water once the 28-minute hot-water supply (D3) runs out ahead of her.
Watch for a pitch that leans on the uniform-percentage number as proof of fairness without ever
checking who is actually first and last in line, and whether that changes day to day.

## Sensitivity note

The 10.24% margin depends on Modeling Assumption MA1 (case.md) — exactly when the family
devotional happens, which sets the 70-minute shared window. A ±50% flex of the resulting window
figure (`sensitivity_model.py`, `FLEX = ["window_minutes"]`) moves the margin between roughly 4%
and 17% across the tested range — narrower or wider, but Option B stays ahead throughout. Do not
present 10.24% to a room as more fixed than it is; the *direction* is stable, the *size* is not.

## Intro

Frame the format: a real family of eight sharing one bathroom after a flood, a real scheduling
conflict most Heroes have some version of at home. Read the Overview aloud, or act out the opening
knock-knock-knock scene as a cold open before revealing the Dilemma.

## Launch

Read case.md's Overview and Background aloud. Do not show Appendix D's window/policy numbers yet.

## Anchor 1

TAKE A STAND AND VOTE. No reasoning yet, just commit.
*"Will, you have 30 seconds. Round-Robin or Priority Line — what do you choose?"* Call on 2–3
Heroes rapidly, then: *"Stand if you chose the Round-Robin. Sit if you chose the Priority Line."*

## Anchor 2

WHAT IS THE PROBLEM WE'RE SOLVING?
*"Is it just as simple as deciding which schedule is 'more fair,' or is there something else we
need to consider?"* · *"What do you mean by 'fair'? What do you mean by 'need'?"* · *"Is this the
right question?"* Let confusion grow: *"Wow, this is a challenging problem."*

## Anchor 3

WHAT IS THE PROCESS?
*"If we go through this process and build the schedule, how will we actually decide which one is
better?"* · *"Is our question still the right question?"* Re-ask after the group commits to a
process.

## Anchor 4

WHAT DON'T WE KNOW?
*"Do we need to make any assumptions to answer our key question? Which ones are critical?"* — this
is where the group should surface that nobody actually knows exactly when the family devotional
happens relative to bathroom turns (MA1). Do not resolve it yet; let the group feel the gap.

## Data Deep Dive

Now, and only now, hand out Appendix D (the window and the two policies). Let Heroes build
Option A's and Option B's schedules live if time allows.

## Twist

At roughly the 15-minute mark: *"Knock, knock."* (Pause.) *"Grandma Polly and Grandpa Ben heard
about the flooding and just showed up — with their suitcases."* (Pause.) *"They're staying to help
with repairs. Now what?"*

This is preserved directly from the original Guide Notes. It invalidates a position much of the
room will hold confidently: that whichever schedule they picked is a stable, done solution. It
doesn't make either option obviously correct — recompute with 10 people sharing the same
70-minute window (`sensitivity_model.py`'s `evaluate_twist()`, using a disclosed estimate of 25
minutes/day for each grandparent, MA2 — facilitator-only, not printed in case.md since the Twist
is withheld from the student packet):

- **Option A** drops to a 7.0-minute flat slot per person — *below* George's real 8-minute need
  for the first time, meaning Option A now shortchanges someone it didn't shortchange before.
  Useful minutes fall to 66.0.
- **Option B** stays at 70.0 useful minutes (still fully proportional), but every family member's
  individual percent-of-need-met drops from 30.8% to about 25.3%.
- The margin compresses from 10.24% to 6.06% — Option B is still ahead, but by less. Neither
  option "solves" the twist; both get worse.

Follow-up: *"What just broke in your original model? Were you wrong — or just missing
information?"*

## Close

Vote again. *"Did we ask the right question?"* · *"What math was new to you, and how did you
attack it?"* · *"If you were given a similar case study next time, what would you do differently?"*

## Lessons Learned

"Equal" is not one thing — equal minutes and equal outcomes are different, sometimes opposite,
claims, and the numbers only tell you which one you actually built.

## Standards Touched On

See case.md Appendix F.

## 45-Minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch: *"Round-Robin or Priority Line — what do you choose?"* 30-second commitments, stand/sit vote, no explanation yet. |
| 3:00–10:00 | Position defense. *"Convince us your plan is better, not just fair."* · *"Who does your schedule actually protect?"* · *"What assumption did you make about when the devotional happens?"* Cold-call: *"You said Round-Robin — walk me through what happens to Heather on the morning she's last in line."* |
| 10:00–15:00 | Pressure-test the models. *"Whose plan is most fragile if someone runs two minutes over?"* · *"Which plan survives a bad morning better?"* · *"Does either plan actually get everyone out the door on time?"* |
| **15:00** | **DROP THE TWIST** (see above) — deliver it slowly, with pauses. Then: *"You now have 60 seconds. Are you changing your plan — or not?"* |
| 15:00–20:00 | Immediate recommit. *"Who is NOT changing their plan? Who is completely reversing?"* · *"What just broke in your original model?"* |
| 20:00–30:00 | Deep conflict, threaded. **Thread 1 (Equal treatment vs. efficiency):** *"Should the family maximize total useful minutes, or protect equal treatment even if it wastes time?"* **Thread 2 (Who bears the cost of scarcity):** *"There isn't enough bathroom time for everyone's real routine either way — who should have to compromise, and who decides?"* **Thread 3 (Role-based authority):** *"Are you answering as Will the dad, or as Will the person who has to enforce this schedule every single morning at 7am? Does that change which plan you'd actually pick?"* |
| 30:00–38:00 | Leadership & trust layer. *"Do you tell the family exactly how the math works, including that under the Priority Line everyone gets the same percentage but very different real minutes?"* · *"What happens the first morning someone runs over their slot?"* |
| 38:00–43:00 | Collapse the room. *"Raise your hand if you're confident your plan is right."* (Expect hesitation.) *"Who could defend the opposite plan?"* · *"What would it take to convince you you're wrong?"* |
| 43:00–45:00 | Final curveball and exit. *"It's been three weeks. The schedule is working, mostly — except Heather has started setting her alarm 20 minutes earlier than the schedule requires, every single day, just to be safe."* Then: *"Did your plan actually solve the problem, or did it just move the cost somewhere the schedule doesn't measure?"* |

**Facilitation notes:** stay neutral (only "why?" / "push that further" / "who disagrees?"); use
names constantly; let silence work after the Twist; force tradeoffs if a Hero hedges ("you don't
get both — choose").

## Cohort bands

See `case.json.cohort_bands[]` — Full (12–20), Compressed (6–11), 1:1/pair (1–2), each with what
changes at that size.
