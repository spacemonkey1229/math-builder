# Guide Notes: Apron Order

**Case:** Apron Order · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Fractions / Addition And Subtraction (partial) + Multiplication (partial) +
Division (partial) — all `new_coverage` (see `case.json.standards[]` for the exact ids)

Researched and margin-resolved 2026-08-12 (`margin_pct` = 8.62, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real cost decision, not a worksheet. Name the
opener — "You are cutting fabric at 6 AM for a rush order due Thursday. Whichever marker you cut
from is the one the shop is stuck with." Let the stakes land before moving to the Launch.

## Launch

Show both marker layouts side by side (the same pair described in the Overview) with no prices
labeled — just the shapes on the fabric. Ask: "Which one do you think costs less to run, just from
looking at it?" Do not confirm or correct answers here. The point is a gut read before anyone
touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Devon on Cut on the Fold — the one that isn't the
tighter fabric layout?" Show of hands, both options, no discussion. Record the count — Close will
ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'costs less'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which one uses
less fabric," but the real question has two separate legs that pull in different directions:
material cost (which favors Cut Open) and labor cost (which favors Cut on the Fold). Push on it:
"Devon isn't pricing one number. She's pricing two, priced in totally different units — yards and
minutes. How do you even compare those?" If the room lands on "convert both to dollars" on its own,
the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the actual steps before touching the
appendices: work out the pattern's own real dimensions (D1-D2), work out yield and remnants
(D3-D4), compare the waste fractions (D5), check the hem (D6), then price both layouts out in full
(D7). Re-ask: "Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix F's three Modeling Assumptions (MA1 the labor rate, MA2
the pattern's own yardage/time figures, MA3 the Twist's directional-print scenario) are all
stated, not sourced — no public "real shop marker" database exists for this authored pattern. Ask
which one actually changes the recommendation if it moves (MA1 — see Data Deep Dive).

## Data Deep Dive

Now, and only now, the numbers. Walk D1-D6's fraction arithmetic and D7's cost comparison together
as a room, cold-calling for D3 (aprons per bolt) and D6 (the hem check) specifically — these are
the two places a Hero who tries to shortcut fraction division by converting everything to decimals
first will visibly lose precision or lose the pattern of *why* the division works, which is useful
information for the facilitator, not a moment to rescue.

**Facilitator-only fraction note.** D3 (22½ ÷ 1¼ = 18) and D6 (5 ÷ ⅝ = 8) both come out to clean
whole numbers — not an accident, but not something to tell a Hero in advance either. If a Hero's
answer isn't a whole number, that's a real, useful signal they made an arithmetic error somewhere,
not a sign the case's numbers are "supposed" to be messy.

**Facilitator-only cost note.** Option A: $180.00 material + $32.00 labor = **$212.00**. Option B:
$168.00 material + $64.00 labor = **$232.00**. Margin: **8.62%**, Option A cheaper. The single
biggest lever is MA1 (the $16/hr labor rate) — flexed ±50% the margin holds between 2.00% and
13.64%, Option A stays cheaper throughout. This is a genuinely stable result — the real tension is
that the number that "sounds" more responsible (less fabric waste) is not the number that decides
the job at this order size.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. The boutique client calls. They've picked the fabric — a
directional canvas print, an arrow pattern, that has to run the same way up on every piece."

"Cutting on the fold means pieces come out upside-down unless you add extra fabric, averaged across
the whole order, to reposition them. Does Cut on the Fold still win?"

**Facilitator-only: what the numbers actually do.** A directional print forces Option A's yardage
up by a flat ⅛ yard per apron, applied uniformly across all 40 aprons in the order (a real,
disclosed scenario — MA3; this ⅛ yd/apron is a batch-averaged repositioning allowance, not a claim
that every individual piece needs it — treat it as uniform for the arithmetic). Option A's total
rises from $212.00 to **$230.00**; Option B is untouched at $232.00. The margin collapses from
8.62% to **0.86%** — Option A is *still* cheaper, but only by $2.00 on a $232 job, a margin so thin
it's arguably a coin flip in practice. **The twist does not flip the verdict; it nearly erases it.**
Do not hand this reasoning over unprompted; let a Hero who did D7 carefully reason toward it — the
real skill being tested is recognizing that "still technically cheaper" and "actually a safe
recommendation" are not the same thing once the margin gets this thin.

**Facilitator-only: twist × wage-rate interaction.** MA1's $16.00/hr labor rate is itself an
unverified assumption ("mid-teens" wage data, not a single primary source). Composing the twist
with MA1's own ±50% sensitivity band: A_total(w) = 198 + 2w, B_total(w) = 168 + 4w, which cross at
exactly **w = $15.00/hr** — just $1 below the base assumption. Below $15/hr, Option B becomes
cheaper *even with the twist applied*. This is real and worth knowing before the discussion, but is
not a reason to withhold the twist or change the base case: it sharpens, rather than undermines, the
Deep Conflict thread on "a margin that survives is not the same as a margin that's safe" — if a Hero
pushes on the wage assumption post-twist, the honest answer is that the verdict is genuinely on a
knife's edge, not merely "thin."

## Immediate recommit

Re-vote immediately. Ask by name: "Does the directional print change your vote, or just how
confident you are in it?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **Two units, one decision.** Yards and minutes aren't the same thing, and D7 forces converting
   both into dollars before they can even be compared. Is there a cost to compressing two very
   different kinds of resource into one number?
2. **The "responsible-sounding" answer isn't always the cheap one.** Less fabric waste sounds like
   the professional choice. Why did the actual math say otherwise at this order size — and would a
   bigger order change that?
3. **A margin that survives is not the same as a margin that's safe.** After the twist, Option A
   is still cheaper by $2.00. Is $2.00 out of $232 a real reason to stick with A, or has the
   decision effectively become a coin flip?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both layouts, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us the tighter fabric layout isn't automatically the cheaper job"* |
| 10:00–15:00 | Pressure-test the models — *"Whose cost number is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the directional print, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (two units, one decision; the responsible-sounding trap; a surviving margin vs. a safe one) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will notice Cut Open wastes less fabric, conclude the tighter layout must be the
cheaper one, and stop — treating fabric as the whole cost story because "less waste" sounds like
the responsible, professional answer. Watch for a pitch that reports the waste comparison (D5) and
never prices out the marking time (D7) — it has not actually costed the job.

## Socratic questions

1. Cut Open saves real fabric. Cut on the Fold saves real time. Which one is Devon actually being paid to optimize for — and does the shop owner's own words in the Overview answer that?
2. D3 tells you a full bolt yields a whole number of aprons under Cut on the Fold. Is that a coincidence, or did the case pick those numbers on purpose — and does Cut Open's yardage divide as evenly?
3. MA1's $16/hr labor rate is an assumption, not a citation. What would you want to see before you trusted it, and what happens to the verdict if the real rate is higher?
4. D5 asks you to compare waste fractions directly. Does the option that wastes less fabric also turn out to be the cheaper option overall — and if not, why not?
5. Devon has one cut to make. What does she tell her boss — and does the twist change the answer?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the
room already understand how thin the margin was?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether D3/D6's clean whole-number answers helped Heroes self-check their fraction work, or
  whether Heroes distrusted a "too clean" answer and second-guessed correct work.
- Whether the "responsible-sounding answer isn't the cheap one" trap landed as a genuine surprise.
- Whether the twist's "still cheaper but by almost nothing" framing produced real reasoning about
  what a thin margin means in practice, or just a shrug that the vote didn't have to change.

## Standards Touched On

How to subtract fractions · How to subtract with mixed numbers · How to multiply a fraction and a
mixed number · How to divide a fraction by a whole number · How to divide a whole number by a
fraction · How to divide fractions and mixed numbers

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a shop's rush-order deadline and a real cost
decision, not personal loss or hardship.
