# Guide Notes: Pattern Rights

**Case:** Pattern Rights · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Launchpad
**Standards:** Discrete Mathematics / Combinatorics — Fundamental Counting Principle (term +
how-to, reinforcement) and Binomial Coefficient (term + how-to, `new_coverage`), plus Pigeonhole
Principle (term, genuinely exercised, credited to a sibling case — see LEARNING_GOALS.md). Exact
ids in `case.json.standards[]`.

**Status:** drafted at `case-write`; numeric detail below is finalized once `case-research`
sources Appendices B and C. This file is re-checked for drift at every readiness run.

## Intro

Frame the format: this is not a trivia question about which repeat "looks nicer." Name the
opener: *"You don't run the press and you don't pay the setup bill — but the term you write into
this license decides what gets cut into a piece of steel Thursday morning, and nobody re-cuts a
cylinder because a Hero changed their mind. You have one shot at this term."* Say plainly that
both repeat schemes are legitimate, widely used techniques in real textile production, and the
room's job is to decide which one they'd put their signature on.

## Launch

Show two real fabric photos or swatches, side by side — one an obvious straight-grid repeat, one
an obvious half-drop (many public fabric-retailer product photos show this clearly if zoomed).
Ask one question and take answers without correcting any of them: *"Before you know a single
number, which one looks more expensive to make? Which one looks more expensive to buy?"* Let the
gut reads stand; the Close revisits them.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Priya on the straight grid?"* Stand-or-sit vote for
both options, no discussion permitted. Record the count — the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow here; it is deliberate. The room will want to say "the fancier repeat is
better" and that is under-specified in an interesting way. Push:

- *"Better for whom — the designer who wants flexibility, or the manufacturer who wants cheap
  yardage? Are those the same thing?"*
- *"The case gives you a configuration count and a cost-per-yard figure. Are those measuring the
  same kind of value?"*
- *"If a scheme unlocks more design flexibility but never gets printed because it's too expensive
  to set up, does the flexibility matter at all?"*

Do not resolve this. A room that leaves Anchor 2 still arguing about what "better" even means is
exactly where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make the room name the steps before opening any appendix:

1. Count each scheme's distinct printable configurations using the Fundamental Counting Principle
   (D1).
2. Count each scheme's distinct featured-capsule subsets using a binomial coefficient (D2).
3. Separately, bound how many repeat units a run needs before a configuration repeat is
   *guaranteed*, using the Pigeonhole Principle (D3).
4. Compute each scheme's total printable yards from one engraving, and divide by setup cost, to
   get the case's actual primary metric (D4).

Re-ask: *"Is our question still the right question, now that we can see the steps?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix D once research completes:

- Thistlebrook is fictional; its real fabric width and cylinder rated print run are grounded in a
  real mill/printer's published specs, but its actual engraving setup costs may not be public —
  see Appendix D for whichever figure had to become a stated assumption.
- The licensing terms (4 colorways, a 2-element featured capsule) are choices this specific
  negotiation made, not universal facts about textile licensing.

Ask which of these changes the recommendation if it moves, and which only changes the size of the
answer.

## Data Deep Dive

Now, and only now, the numbers. Work D1 → D4 as a room. Cold-call specifically on **D2**, the
binomial-coefficient step — this is the deliverable most likely to produce a Hero who has never
computed "n choose k" on a real design problem before, and their confusion is information, not a
moment to rescue. The sentence to fish for is some version of *"The Half-Drop's tile has twice as
many floral elements, so its subset count isn't twice as big — it's way more than twice, because
combinations grow fast."*

Full worked figures are filled in the **Facilitator-only numbers** section below once
`case-research` completes.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses.

*"Everyone in this room has now computed D1 and D2. Someone read me The Half-Drop's featured-capsule
subset count."* (Let a Hero read a number visibly larger than The Straight Set's.) *"So on design
flexibility alone, The Half-Drop wins by a landslide. Show of hands — who is recommending Option B
right now, on exactly that basis?"*

Let hands go up. Then: *"That number is real. Every digit of it is correctly computed. And it
might not be the number that decides this. Priya doesn't get paid in configurations — she gets
paid in royalties on yards actually printed and sold. You have five minutes. Go compute D4. Does
the recommendation survive?"*

**Facilitator-only: what the numbers actually do.** Both schemes' engraved cylinder has the same
circumference (set by the motif's 27-inch height) and the same sourced screen life (30,000
meters), so both schemes print the exact same total yardage — 32,808.4 yards — from one engraving.
The only thing that differs is setup cost ($650 vs. $750, Appendix D MA2), so on the case's actual
primary metric, **The Straight Set wins, 50.47 yards/$ against 43.74 yards/$ — a 13.3% margin.**
The verdict does not flip on configuration variety alone (The Half-Drop's 8 configurations and 66
capsule variants really are larger numbers) — it flips because the primary metric was never
measuring configuration variety in the first place.

## Deep conflict — threads (20–30 min)

1. **Flexibility you can prove versus flexibility you can sell.** D1 and D2's counts are exact,
   derived from the case's own stated licensing terms — nobody can argue with the arithmetic. But
   a configuration nobody prints is worth nothing to either party. Which kind of number should
   carry more weight in a licensing negotiation: the mathematically larger design space, or the
   dollar-per-yard economics of the scheme that actually gets manufactured?
2. **Whose risk is whose.** Priya is not the one paying for the engraved cylinder, and Thistlebrook
   is not the one whose reputation rides on whether the seams show. Does that change which scheme
   each party should push for, independent of which one is mathematically "better" on the case's
   own metric?
3. **The "no two repeats identical" claim.** D3 asks whether Thistlebrook could honestly market a
   featured capsule as fully unique. Is a technically-true-but-astronomically-unlikely marketing
   claim the same thing as an honest one?

## Socratic questions

1. The Half-Drop's featured-capsule subset count is larger than The Straight Set's. Why does that fact alone not settle the case?
2. Your D3 pigeonhole guarantee threshold and a real production run's actual repeat count — which one is bigger, by how much, and what does that gap actually tell you about whether "no two repeats look alike" is an honest claim?
3. D1 required a different number of independent stages for each scheme (one for The Straight Set, two for The Half-Drop). Walk through why that structural difference exists — what does the half-drop's offset actually unlock that the straight grid can't?
4. If Thistlebrook's real fabric width were narrower than the one this case sourced, which of your four deliverables would change, and which would not move at all?
5. Priya is not the one who pays Thistlebrook's engraving bill. What does that fact do to Argument B's claim that more design flexibility is automatically the right call for her to push for?

## 45-minute Socratic plan

| Time | Segment | Move |
|---|---|---|
| **0:00** | Intro + Launch | Frame the format; show the two swatches; take gut reads without correcting them |
| **0:05** | Anchor 1 | Take a stand and vote — no reasoning yet |
| **0:10** | Anchor 2 | "What is the problem we're solving?" — let "better for whom" stay unresolved |
| **0:18** | Anchor 3 | Name the four-step process (D1 → D4) before opening any appendix |
| **0:22** | Anchor 4 | Surface the honest gaps in Appendix D — which assumptions are load-bearing |
| **0:26** | Data Deep Dive | Work D1 → D4 as a room; cold-call on D2's binomial-coefficient step |
| **0:38** | **TWIST** | Drop the Twist — D1/D2 favor The Half-Drop, D4 (the real primary metric) reverses it |
| **0:41** | Deep conflict | Run the three threads (flexibility you can prove vs. sell; whose risk is whose; the honesty of the collision claim) |
| **0:45** | Close | Vote again; "Did we ask the right question at the start?" |

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Fundamental Counting Principle · Binomial Coefficient · Pigeonhole Principle · How to apply the
Fundamental Counting Principle to count outcomes · How to compute a binomial coefficient

## Facilitator note — sensitivity

None required (SPEC §6). The stakes are professional and commercial — a licensing negotiation and
a production setup decision. No personal loss, no family hardship.

## Facilitator-only numbers

Every figure below resolves in `case.json.derived`.

**D1 — Configuration counts.** The Straight Set: 4 colorways × 1 (no independent mirror choice) =
**4**. The Half-Drop: 4 colorways × 2 (independent mirror-or-as-drawn per column) = **8**.

**D2 — Featured-capsule subsets.** The Straight Set: C(6,2) = **15**. The Half-Drop: C(12,2) =
**66** (more than 4x, because The Half-Drop's true tile holds double the floral elements — see
Appendix A's corrected geometry note, RESEARCH_LOG.md).

**D3 — Pigeonhole guarantee thresholds.** The Straight Set: 4 + 1 = **5** repeat units before a
configuration is guaranteed to repeat. The Half-Drop: 8 + 1 = **9**. A real production run prints
**131,232** repeat units (3 columns across the real 54-inch fabric width × 43,744 repeats down one
engraving's 30,000-meter rated run) — dwarfing both thresholds by four orders of magnitude.
**Neither scheme could honestly support a "no two repeats identical" marketing claim.**

**D4 — Primary metric.** Total yards per engraving: **32,808.4** (identical for both schemes).
The Straight Set: 32,808.4 ÷ $650.00 = **50.47 yards/$**. The Half-Drop: 32,808.4 ÷ $750.00 =
**43.74 yards/$**. **The Straight Set wins, margin 13.3%.** Capsule-variants-per-dollar (D4b,
secondary, not the primary metric): The Straight Set 15/$650 ≈ 0.023; The Half-Drop 66/$750 ≈
0.088 — The Half-Drop wins this secondary figure by nearly 4x.

**The trap.** A Hero who finishes D1 and D2 will stop there and recommend The Half-Drop on the
strength of those two numbers alone — because the room has just watched it beat The Straight Set
by roughly 2x on configurations and better than 4x on capsule variety, and both figures are true
and correctly computed. What that Hero will skip, unless the facilitator forces the next step, is
D4: they will never divide either scheme's output by its setup cost, so they will never notice
that neither D1 nor D2 is measured in the case's actual primary metric (yards per dollar of
setup cost). The tell that a room has fallen into it: a recommendation for Option B that cites
only configuration or capsule counts and never mentions a dollar figure.

**Sensitivity.** The 13.3% margin depends entirely on Appendix D MA2 (the assumed $650/$750
engraving figures — no public, current, scheme-specific price exists). At MA2 = $0 premium (equal
setup cost), both schemes tie exactly on the primary metric, since total yardage is assumed
identical. Above roughly a $812.50 Half-Drop setup cost (a 25% premium), the margin would exceed
SPEC §2's 20% unbalanced threshold. Verified with `sensitivity_model.py` (Tier 2 probe 5, run
2026-08-17): under the probe's standard flex range, both `setup_cost_straight_usd` and
`setup_cost_half_drop_usd` individually flip the winner and blow through SPEC §2's cap in at
least one direction each. `screen_life_m` (MA1) does not flip the verdict at any tested flex,
because it scales both schemes' yardage identically. This instability is disclosed, not
eliminated, per `case.json.sensitivity_disclosure[]`
(Category F — no public, current, scheme-specific engraving quote exists; the real figure
Thistlebrook would actually be quoted is a future-quote unknown, not a research gap this case
failed to close).
