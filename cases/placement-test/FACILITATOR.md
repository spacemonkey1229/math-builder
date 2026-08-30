# Guide Notes: The Placement Test

**Case:** The Placement Test · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Statistics And Probability/Probability — Permutation / How to determine the number
of outcomes of a permutation; Basic Operations/Division — Division / How to divide decimal
numbers; Advanced Numbers/Percents — Percent / How to find the percent of a number (see
`case.json.standards[]` for exact ids; this is a reinforcement case, not a new-skill-coverage
case — see `case.json.reinforcement_note`).

Researched 2026-08-26 (`RESEARCH_LOG.md`, all placeholders resolved). **Balance flag, read before
you facilitate:** on the primary metric (statistically attributable conversions per dollar of ad
spend), Option A (The Straight Cut) and Option B (The Full Rotation) are an **exact tie**,
`margin_pct` = 0.0%. This is not an accident of a missing computation — the case originally shipped
with `margin_pct` left `null` and its stated $18,000 budget (MA2) left every Full Rotation variant
below Appendix C's minimum-viable-spend threshold, a genuine SPEC §2 balance failure (Option A
would have won by construction). That was first resolved by raising MA2 to $30,000, the exact flip
threshold the case's own sensitivity note documented — but that setting sat exactly ON the
threshold with zero slack, and a 2026-08-27 QA pass found that any of three plausible assumption
moves (MA1 up, MA2 down, MA3 up) each flipped all six Full Rotation variants below threshold at
once (they are excluded together, not gradually, since every variant gets an identical split
spend), handing Option A a ~100%-margin win. **2026-08-30: MA2 was raised again, to $60,000,
specifically to give the tie real slack.** Full Rotation's split is now $10,000/variant — double
the $5,000/variant Appendix C threshold, not exactly at it — and a re-run of the ±50% assumption
flex sweep confirms 0 of 10 flex directions across all five stated dials flips the recommendation.
The tie still ties exactly (MA4/MA5 apply identically to both options once every variant clears),
but it is no longer a knife's edge. See the "Facilitator-only numbers" section below for the full
arithmetic.

## Intro

Frame the format before anything else: this is a real budget recommendation with Jaylen's name on
it, due to the growth lead and finance team, not a worksheet. Name the opener: *"You have one shot
at defending this recommendation before next quarter's budget locks. The math has to hold up in
the room."* Say plainly that both plans are already running somewhere in the industry and the
room's job is to decide which one they would put their own name behind.

## Launch

Read the Overview's two open tabs aloud, or project them side by side — the one-slide Straight Cut
plan and the sprawling, color-coded Full Rotation test matrix. Ask one question and take answers
without correcting any of them: *"The growth lead wants real signal. The media buyer wants to
protect the budget. Which one of them is Jaylen more likely to disappoint?"* Let the gut reads
stand; the Close revisits them.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Jaylen on The Full Rotation — testing all six
variants, not just running the one safe plan?"* Stand-or-sit, both options, no discussion
permitted. Record the count — the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'more signal'?"**

Let confusion grow here; it is deliberate. The room will want to say "more variants tested is more
information, so it must be the better plan" without asking whether every one of those variants can
actually produce a *usable* read. Push:

- *"If a variant's budget is too thin to trust its numbers, is running it still 'information' —
  or is it just spending money to generate noise?"*
- *"The Straight Cut only ever tests one combination. Is 'more information' automatically better
  if some of that information can't be trusted?"*

Do not resolve this. A room that leaves Anchor 2 arguing about what actually counts as *usable*
signal, not just *more* signal, is exactly where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make them name the steps before any appendix is opened:

1. Count the distinct production-order sequences for the three placement-timing cuts across the
   production weeks available (D1) — this is what shows the test-design space is bigger than the
   fixed production calendar can fully explore.
2. Split the fixed budget one way (Straight Cut) and six ways (Full Rotation), in dollars per
   variant, with the arithmetic shown (D2).
3. Check every variant's split budget against the ad platform's minimum-viable-spend threshold —
   as a percent of that threshold (D3).
4. Only once D3 is known, compute attributable conversions per dollar of ad spend for each plan,
   excluding any variant that never cleared the threshold (D4), and recommend.

Re-ask: *"Is our question still the right one, now that we can see the steps?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which live in `case.md` Appendix E:

- Production weeks remaining (MA1, 5 weeks) — internal to Jaylen's employer, unsourceable.
- Total fixed ad-spend budget (MA2, $60,000) — also internal and unsourceable.
- Assumed cost per attributable conversion (MA3, $20) — neither platform publishes a dollar
  minimum, only a conversion-count minimum (S1, S2); this is a stated estimate, not a citation.
- Industry benchmark conversion rate and CPM (MA4, MA5) — both contested figures with no free
  authoritative point figure; stated mid-range values.

Ask which of these actually changes the *graded* D4 recommendation if it moves, and which only
changes magnitude. The honest answer, after the 2026-08-30 retune: **none of the five flips it on
its own within a plausible ±50% move.** MA1 and MA3 both still feed the Appendix C threshold
formula (50 events/week × weeks_remaining × $20/conversion) — raising either one raises the dollar
threshold Full Rotation has to clear — but at the case's current $60,000 budget ($10,000/variant),
even the worst single move (either dial at +50%, raising the threshold to $7,500/variant) still
clears with $2,500 (33%) to spare. MA2 itself moving down 50% lands exactly back on the case's own
prior $30,000 setting, which still clears (it does not fall below). MA4 and MA5 remain genuinely
inert either way: they apply identically to both options in D4, so neither can flip it on its own.
Let a sharp Hero try to find a move that flips it and discover none of the five stated assumptions
does, within a reasonable swing — that itself is worth surfacing: **a tie that survives real
scrutiny is a different, stronger kind of tie than one that only holds by coincidence.**

## Data Deep Dive

Now, and only now, the numbers. Work D1 through D4 as a room, cold-calling specifically on **D3**
— this is where a Hero who computed D1/D2 cleanly but never checked each variant's split budget
against Appendix C's threshold will visibly struggle to explain why "six variants" doesn't
automatically mean "six usable numbers."

Full worked figures are in `case.json.derived` and reproduced in the **Facilitator-only numbers**
section below. Do not read that section's totals aloud before D4 is worked — it is the answer key.

## Twist

**Twist: N/A.** This case's dilemma is a one-shot budget-allocation recommendation with a hard
deadline (the quarter's budget locks) — there is no real, sourceable fact this case's research
turned up that could honestly be withheld from Background and then revealed mid-discussion without
either fabricating a number (forbidden by SPEC §5) or simply restating information the Hero
already has by Anchor 4. The natural candidate — "what if the budget shrinks after fees" — was
considered and rejected for the same reason `The Optimal Can`'s twist was: introducing a second,
unsourced dollar figure here would either leak the tie's fragility early or require inventing a
number this case's research does not turn up a defensible basis for. Anchor 4 and the Deep
Conflict section below already carry the "what if the numbers move" pressure a twist would
otherwise add — and because this case's tie sits exactly at the threshold with no slack, that
pressure is unusually real without needing an invented event to create it.

## Deep conflict — one thread (T2 compression: pick one, do not attempt three)

**A tie the math genuinely cannot break.** D4 comes out identical for both options, and — after the
2026-08-30 retune — it stays identical under every reasonable single-assumption swing the room can
propose (±50% on any of MA1–MA5, checked mechanically by `sensitivity_model.py`). Push: *"If you
were Jaylen, and the quantitative metric refuses to pick a winner no matter how you stress-test the
assumptions, what do you actually recommend — and on what basis, if not the number?"* This is the
case's real tension once D4 is worked: the quantitative primary metric cannot settle it, so the
room has to argue from Argument A's single-hypothesis reliability against Argument B's genuine
multi-variant signal, with no numeric tie-breaker to fall back on.

**Why this is stronger material than a QA checkbox.** An earlier version of this case had the tie
sitting at a genuine zero-slack boundary, where three separate assumptions (MA1 up, MA2 down, MA3
up) could each independently flip the recommendation to a large Option A win — a fragile tie that
was really an accident of arithmetic dressed up as a design choice. That fragility was closed by
raising MA2 to $60,000 (Full Rotation's split is now $10,000/variant, double the $5,000/variant
threshold), so none of MA1–MA3 flips it within a plausible ±50% move any more. If a room has time,
this history itself is worth surfacing as a closing question: *"The math used to be one bad
assumption away from flipping this recommendation entirely. Now it isn't. Does that make The Full
Rotation a stronger pick than it was — or was the earlier fragility actually more honest about how
real budget decisions work?"* A Hero who can articulate that a robust tie and a fragile tie carry
different weight, even at the identical `margin_pct`, is engaging with the case at its intended
depth.

## The trap

A Hero will often correctly compute D1's 60-sequence permutation count and D2's $10,000/variant
budget split, and still recommend The Full Rotation purely on the reasoning "more variants tested
is more information, so it must be the better plan" — missing D3 entirely, never checking whether
each of those six $10,000 splits actually clears the platform's $5,000/variant minimum-spend
threshold. Six variants that each individually produce unusable, noise-level conversion estimates
are not six times the information; they can be closer to *no* usable information at all, while
still costing the full $60,000 budget. Watch for a pitch that cites "six variants tested" as the
win condition without ever reporting D3's clearance percentages. (This run's numbers happen to
reward that instinct — D3 shows every variant clears comfortably, at 200% of the threshold — but a
Hero who skipped D3 got the right answer for the wrong reason, and should be pushed on it exactly
the same way: what if the budget had been half as large?)

## Socratic questions

1. The Full Rotation tests six variants instead of one. If every one of those six variants clears the platform's minimum-spend threshold, is there still any reason to prefer The Straight Cut?
2. You computed the number of distinct production-order sequences for the three placement-timing cuts in D1. Why does that number matter to Jaylen's decision, if the team only ever needs to pick *one* order to actually produce?
3. Suppose one of The Full Rotation's six variants comes in just under Appendix C's minimum-spend threshold. What should Jaylen do with that variant's conversion numbers — report them anyway, throw them out, or something else — and why?
4. The Straight Cut and The Full Rotation draw from the exact same total budget. Given this case's numbers, once every Full Rotation variant clears the threshold, is it even possible for one plan to beat the other on conversions-per-dollar — or does clearing the threshold guarantee a tie?
5. If the finance team cut the fixed test budget for next quarter by half, would you expect that to change which plan wins — and if so, which one does it hurt more? (It would need to fall further than that before Full Rotation's per-variant spend actually drops below the platform's minimum-spend threshold — try the arithmetic.)

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"* Compare the closing vote to Anchor 1's — a room
that voted for B at Anchor 1 purely on "more variants must be better" and stays with B after
working D3/D4 for a *different, threshold-and-arithmetic-based* reason has genuinely moved, even
if the vote count looks unchanged. A room that flips to A purely on reliability-under-uncertainty
grounds is just as legitimate a landing as one that stays with B for the genuine-signal argument —
this case does not
have a single correct final vote.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "none of the five assumptions flips it within ±50%" finding landed as a
  discovery (a Hero tried to find a flip and couldn't) or had to be told outright.
- Whether the Deep Conflict thread (a tie the math can't break) produced real disagreement, or
  whether most Heroes treated a tie as automatically meaning "either answer is fine" without
  engaging the reliability-vs-signal argument the case is actually testing.
- Whether skipping a Twist was missed — if a room clearly wants a mid-discussion reveal, that is
  worth recording as a signal this case should get one on the next revision.

## 45-minute Socratic plan

| Time | Beat |
|---|---|
| 0:00–3:00 | Intro + Launch — frame the budget-lock stakes, read the Overview's two tabs, take the gut-read question without correcting anyone |
| 3:00–8:00 | Anchor 1 — take a stand and vote, no reasoning yet |
| 8:00–15:00 | Anchor 2 — "what is the problem we're solving?" Let the room sit in the ambiguity of "more variants tested" vs. "more usable signal" |
| 15:00–20:00 | Anchor 3 — name the four-step process before opening any appendix |
| 20:00–25:00 | Anchor 4 — surface the five assumptions (MA1–MA5); ask which can actually flip D4 (none can, within ±50%) |
| 25:00–35:00 | Data Deep Dive — work D1→D4 as a room, cold-call on D3's clearance check |
| 35:00–40:00 | Deep conflict — a tie the math can't break. No twist to drop in this case (see Twist: N/A above); this slot carries the "what do you recommend when the number won't decide it for you" pressure instead |
| 40:00–45:00 | Close — re-vote, "did we ask the right question?", lessons learned |

## Standards Touched On

Permutation · How to determine the number of outcomes of a permutation · Division · How to divide
decimal numbers · Percent · How to find the percent of a number

## Facilitator note — sensitivity (SPEC §6)

**SPEC §6: NONE.** This case is routine marketing-analytics math — which paid-placement test plan
a brand strategist runs against a fixed budget. No protected subject matter, no facilitator content
flag needed beyond ordinary classroom awareness.

## Facilitator note — coverage

Both claimed permutation skills (`statistics-and-probability-permutation` and
`statistics-and-probability-how-to-determine-the-number-of-outcomes-of-a-permutation`) were
already at `n=1` (covered once, by `Codebreaker`) before this case was written, so
`case.json.new_coverage[]` is an empty array — this case closes no coverage gap. It was written
anyway per the approved concept sheet, which explicitly authorized an empty `new_coverage[]` as
long as it is flagged (see `LEARNING_GOALS.md` for the full flag and `n` values verified against
`readmodel/standards_spine.json`, and `case.json.reinforcement_note` for the transcribed
justification).

## Facilitator-only numbers

Every figure below resolves in `case.json.derived`. Do not read this section aloud before D4 is
worked — it is the answer key.

**D1.** `P(5,3) = 5 × 4 × 3 = 60` distinct production-order sequences (5 weeks available [MA1], 3
cuts required).

**D2 — budget per variant.** Straight Cut: `$60,000 / 1 = $60,000.00/variant`. Full Rotation:
`$60,000 / 6 = $10,000.00/variant`.

**D3 — threshold clearance.** Appendix C's derived threshold is `$5,000/variant`. Straight Cut:
`$60,000 / $5,000 × 100 = 1200%`. Full Rotation: `$10,000 / $5,000 × 100 = 200%` — clears with real
room to spare: double the threshold, not exactly at it.

**D4 — conversions per dollar.** Using the stated conversion rate (2% [MA4]) and CPM ($15 [MA5]):
impressions/dollar `= 1000 / 15 = 66.6667`; conversions/dollar `= 66.6667 × 0.02 = 1.333333`.
Straight Cut: all $60,000 clears, so total conversions `= $60,000 × 1.333333 = 80,000`;
conversions/dollar `= 80,000 / $60,000 = 1.333333`. Full Rotation: all six variants clear, so
total conversions `= 6 × ($10,000 × 1.333333) = 6 × 13,333.33 = 80,000`; conversions/dollar
`= 80,000 / $60,000 = 1.333333`. **Identical.**

**The verdict.** `margin_pct = 100 × (winner − loser) / loser = 0.0%` — an exact tie on the
quantitative primary metric. This is not a coincidence: MA4/MA5 apply identically to whichever
variant(s) actually clear the threshold, so once every Full Rotation variant clears, splitting the
same total budget six ways versus spending it on one variant produces the same total conversions
and the same conversions-per-dollar rate. **The tie now has genuine slack, not just a bigger
cliff.** Full Rotation's variants clear Appendix C's threshold at 200%, not exactly at 100%. An
earlier version of this case set MA2 at exactly $30,000, where the same tie held but with zero
slack — Full Rotation's $5,000/variant split equaled the threshold precisely, and any of three
assumptions (MA2 down, MA3 up, MA1 up) independently flipped all six variants below threshold at
once, handing Option A a ~100%-margin win. `sensitivity_model.py`'s ±50% sweep, re-run after the
2026-08-30 retune to $60,000, confirms **0 of 10 flex directions across all five stated dials flip
the recommendation or breach the 20% cap**: the worst single move (MA1 or MA3 at +50%, raising the
threshold to $7,500/variant) still clears the $10,000/variant split with $2,500 (33%) to spare, and
MA2's own −50% flex lands exactly back on the old $30,000 boundary and still clears rather than
falling below it. (See `case.json.balance.margin_note` for the full two-stage retune history — this
case first shipped at an $18,000 budget where all six variants failed to clear, a genuine SPEC §2
balance failure; raised to $30,000 to fix that but landed on a zero-slack boundary; raised again to
$60,000 to give the tie real robustness, verified by re-running the flex sweep, not just asserted.)
