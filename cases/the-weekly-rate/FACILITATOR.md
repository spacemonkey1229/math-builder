# Facilitator Notes — The Weekly Rate

**Case:** The Weekly Rate · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Adventure
**Standards:** see `case.json.standards[]` for the exact ids (28 skills — variable, constant,
coefficient, term, like terms, distributive property, x-intercept, y-intercept, slope, system of
equations, percent, rounding, addition, multiplication, and their paired "how to…" skills)

**SPEC §6 flag:** none required. This case does not touch illness, death, or acute family
hardship — Dara's stakes (a tuition deadline, a weekly budget) are real and personal but not the
kind of subject matter SPEC §6 asks facilitators to flag. Keep it grounded and concrete rather
than played for sympathy.

## Intro

Frame the format: a real personal-finance decision built from real, currently-live company
pricing — not a worksheet with a story stapled on. Name the opener: "Dara rides six days a week
for two delivery apps. Every week, she pays a company named Zoomo thirty-nine dollars to rent the
e-bike she rides. Today she has to decide whether to keep paying that, or to walk into a bike
shop and just buy one." Worth naming: Dara used to do data entry for a claims office — the
laminated index card on her handlebars isn't a quirk, it's a professional habit that didn't stop
when the job did.

## Launch

Read the Overview aloud, then Background's first three paragraphs — Dara is not deciding whether
to keep dashing, only how to pay for the bike, and the acceptance email has just fixed *how long*
she plans to keep doing it: 21 months, not indefinitely. Do not show Appendix A's dollar figures
yet. Ask: "Just from what you've heard — does 'the one with no upfront cost' sound like it settles
this, or not?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Buy the bike, or keep the subscription?" Show of hands, no discussion yet. Record the count —
Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Push on what "cheaper" actually means here. Cheaper starting tomorrow? Cheaper over Dara's whole
career as a courier? Cheaper over the specific 21 months she's actually committing to? Those are
three different questions with three different right answers, and the room needs to notice that
before anyone opens a calculator. "Is anyone courageous enough to say which of those three
questions we're actually answering — before we start comparing dollars?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of "cheaper, over what window," ask them to name the actual
steps: what does each option cost, week by week (Appendix A); how do you turn a list of per-week
and one-time costs into a single equation for each option (D1); how do you find the exact week
where the two equations cross (D2); and what does the crossing point actually mean for someone
with a *fixed* 21-month horizon, not an open-ended one (D3, D6)? Re-ask: "Given how we just defined
'cheaper' — is that still the right process, or does the fixed 21-month horizon change which
number actually answers Dara's question?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix C's four Modeling Assumptions as a group, out loud, before anyone computes
anything. Ask which ones the room thinks matter most. (Facilitator note: MA4 — the 91-week decision
horizon — is the single most load-bearing assumption in the whole case, with MA3's $900/year
self-maintenance estimate a close second; MA1 and MA2 barely move the answer at all. Let the room
guess first — the Data Deep Dive and Q1/Q2 below are where this gets tested directly.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1 (deriving both cost functions from Appendix A's rate
components) and D2 (the break-even system) together as a room, then D6 (the horizon evaluation).

**The trap:** most Heroes will compute the break-even point (≈106 weeks), see that Ownership wins
"eventually," and declare Ownership the obvious right answer — treating "eventually cheaper" as the
same thing as "cheaper for Dara." That reasoning skips the one number that actually answers her
question: her horizon is 91 weeks, about 15 weeks *short* of break-even, so for the actual 21
months she's committing to, Subscription is cheaper — by 8.20%. Cold-call on this specifically:
"You found the break-even week. Now check it against Appendix C's MA4 — is 91 more or less than
106? What does that tell you?"

Show the actual split:

- **Option A (Ownership Path)** — purchase $2,299.00 + (charging $0.986/week + maintenance
  $17.3077/week) × 91 weeks = **Total A = $3,963.72**
- **Option B (Subscription Path)** — ($39.00/week + $0.986/week charging) × 91 weeks =
  **Total B = $3,638.72**
- **Margin: 8.20%** — B is cheaper by $325.00 over Dara's actual 91-week horizon, even though A
  would be the cheaper choice if she rode for longer than about 106 weeks.

## Twist — drop this at roughly the 20-minute mark

**This is the same Twist already live in `published/The Weekly Rate - Interactive.html`'s gated
"Reveal the Twist" panel — deliver that one, do not invent a competing twist.**

Deliver slowly, with pauses:

"You just found something on Zoomo's own blog. They've done this before: a plan that used to cost
$39 a week now costs $49 a week — about a 26% increase — after they added more coverage (Appendix
D, S5a). Suppose that happens again to the Standard Plan Dara's actually on, exactly halfway
through her 21 months — the first 40 weeks at $39, the last 51 weeks at $49.14."

Ask the room: "Recompute Option B's total at the new rate. Does your recommendation change — or
not?"

**Facilitator-only — the recompute.** Option A is completely unaffected (it never depended on
Zoomo's rate). Option B's new total: ($39.00 × 40 weeks) + ($49.14 × 51 weeks) + (charging cost for
all 91 weeks) = **$4,155.86**. Option A's $3,963.72 is now the cheaper choice, by about 4.62%. The
recommendation flips — not because anything about Dara's own riding changed, but because a cost she
does not control moved. A Hero who leaned hard on "Subscription always wins because it includes
everything" now has to reckon with what happens when the thing that was included gets more
expensive to include.

Ask: "Does this change your recommendation — or not?" Either answer can be defended; the point is
forcing a Hero to say *which* number moved and why, not just which hand goes up.

**Twist soundness check (SPEC §6/case-readiness P4).** This twist changes exactly one input
(`subscription_weekly_rate`, and only for weeks 41-91) and is grounded in a real, cited precedent
(S5a) rather than an invented what-if. `sensitivity_model.py`'s `evaluate_twist()` confirms the
recompute mechanically: base margin 8.20% (B wins) → twist margin 4.62% (A wins), a genuine flip,
not just a wobble. It survives every reading of the case's stated assumptions because it touches
none of them — MA1-MA4 are unchanged by the twist; only a cited, real, externally-caused price
change is applied.

## Immediate recommit

Re-vote immediately. "Did the recompute change your hand — or did it just change how confident you
are about *why* you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2 — 'cheaper
over what window' — or did the answer turn out to depend on something else entirely by the end?"
And: "What math was new to you today, and how did you attack it?"

## Lessons Learned

The case's own numbers make a point neither option can dodge: "eventually cheaper" and "cheaper for
the time period you actually have" are two different questions, and a margin that looks decisive
(8.20%) can flip entirely on one input outside anyone's control (a rental company's own pricing
history). The transferable lesson: **before you trust a total-cost comparison, ask what window it's
computed over, and whether that window is the one that actually matches your situation** — the same
break-even math tells two different, both-correct stories depending on whether you're standing at
week 45, week 91, or week 150.

## Five Socratic Questions

Use these across Anchors 2-4, the Data Deep Dive, and after the Twist — each is answerable only
with this case's own numbers, not general opinion.

1. Dara's break-even point is about 106 weeks, but her actual horizon is 91 weeks — what would her decision horizon have to become before Ownership wins instead of Subscription, and how far is that from where she actually is?
2. Appendix C sets Dara's own maintenance cost at $900/year, extrapolated upward from a $400+/year "regular commuter" figure — if that extrapolation is wrong by 50% in either direction, does the recommendation change, and by how much does the margin move?
3. D3 asks for the x-intercept of the net-savings function and, separately, its y-intercept — what does each one mean in plain English, and why is the y-intercept negative?
4. Appendix B graphs a Whizz plan Dara isn't choosing between — what makes its equation structurally different from Option B's, and why doesn't that difference matter to Dara's actual decision?
5. A friend asks Dara: "Why not just buy the bike right before your program ends, once you're sure Subscription won by the horizon that actually happened?" — using the case's own equations, what's wrong with that plan as a *general* strategy, not just for this one case?

## Standards Touched On

See `case.json.standards[]` (28 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: variable, constant, coefficient, term, like terms, distributive property,
x-intercept, y-intercept, slope, system of equations, percent, rounding, addition, and
multiplication, each paired with its "how to…" skill where one exists.

## Cohort Bands

See `case.json.cohort_bands[]`.

- **Full (12-20):** Anchors 2-3 run as written; the room splits into an "ownership wins eventually"
  faction and a "match the horizon you actually have" faction before the Twist forces a live
  recompute of Option B's rate.
- **Compressed (6-11):** Anchors 2-3 combine into one pass; D1's cost-function derivation is
  worked as one shared example on the board instead of every Hero deriving both functions
  independently.
- **1:1 / pair (1-2):** No vote to take — Anchor 1 becomes a stated initial position instead of a
  cold-call show of hands; the facilitator plays devil's advocate directly, arguing whichever
  option the Hero didn't pick.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-3:00 | Cold-call launch, 30-second commitments, stand/sit vote (Anchor 1) — no explanation |
| 3:00-8:00 | Position defense: "Convince us why it's the right call for Dara's actual timeline, not just cheaper in general" |
| 8:00-13:00 | Define the process (Anchor 3): what data would actually settle this, and over what window? |
| 13:00-20:00 | Data Deep Dive: derive both cost functions, solve the break-even system, evaluate at 91 weeks — name the trap |
| **20:00** | **DROP THE TWIST** — Zoomo's own documented 26% price-increase precedent, delivered slowly |
| 20:00-25:00 | Immediate recommit: does any hand move? "What actually broke?" |
| 25:00-35:00 | Threaded deep conflict — two named threads: (1) "eventually cheaper" vs. "cheaper over the window you actually have," as competing definitions of the right question; (2) a margin (8.20%) that looked settled vs. one shown to flip on a single real-world, cited precedent |
| 35:00-45:00 | Close, re-vote, reflection, Lessons Learned |
