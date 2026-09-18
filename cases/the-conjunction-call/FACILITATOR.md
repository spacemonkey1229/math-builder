# Guide Notes: Conjunction Call

MS | Guide Notes | Launchpad | 2026-27
**Tier:** T3 (MS-stretch/HS-entry) · **Primary metric:** kilograms of reserve propellant required to cover this season's real threshold-crossing conjunctions, compared against propellant available after the mandatory disposal reserve · **Margin:** **14.64% — Fly The Season (B) wins, on the numbers as currently predicted**

---

## Status note

This file's numbers are real or clearly disclosed assumptions. `case.md`'s Appendix A cites NASA's
real CARA collision-probability threshold (1×10⁻⁴) and Appendix D cites the real Busek BIT-3
thruster's specific impulse (2,150 s). Appendix B's screening-population count (MA1), Appendix C's
six-event conjunction log (MA2), and Appendix D's wet mass/reserve-propellant/disposal-reserve
figures (MA3–MA5) are disclosed Modeling Assumptions for the fictional Aurora-7 — no real satellite's
per-shell screening count, per-event conjunction history, or current fuel state is ever publicly
reported, so these could not be sourced and are stated in the open instead. Full trail:
`RESEARCH_LOG.md`; full records: `case.json.sources[]` and `case.json.modeling_assumptions[]`.

---

## Argument for A (De-Orbit Now)

De-Orbit Now is certain. Zero propellant is spent on a maneuver that might turn out to be
unnecessary (most Appendix C events, even the ones that cross the real threshold, carry a
collision probability still under 1 in 1,000), and the mandatory disposal burn (Appendix D, MA5)
happens today, while there is no argument about whether enough fuel remains to do it. The strongest
real version of this argument does not deny that Fly The Season's arithmetic works out — it argues
that "works out with 14.64% to spare" is not the same as "safe." A margin computed from a stated
six-event log (MA2) is only as good as that log; one more event, or one event whose real delta-v
turns out larger than predicted, and Aurora-7 could be left without enough propellant to complete
the exact disposal burn Option A completes with certainty right now.

## Argument for B (Fly The Season)

Fly The Season wins on this case's actual computed primary metric, using only real, cited numbers
for the two facts that matter most: NASA's real 1×10⁻⁴ maneuver threshold decides which of the six
Appendix C events actually require a burn (four of them: E2, E4, E5, E6), and the real Busek BIT-3
specific impulse (2,150 s) converts each maneuver's required delta-v into an actual propellant
mass. The total — 0.011951 kg — fits inside the 0.0140 kg Aurora-7 has left after reserving MA5's
mandatory 0.0100 kg disposal minimum, with propellant to spare. Forty-five more days of
already-funded, still-working ocean-color data is a real asset, and the numbers, as currently
predicted, show the season is affordable.

## Margin

**Computed: 14.64%, Fly The Season (Option B) wins — on the conjunctions currently predicted.**

| Quantity | Value |
|---|---|
| Events crossing the real 1×10⁻⁴ threshold (Appendix A) | E2, E4, E5, E6 (4 of 6) |
| Total avoidance delta-v required | 21.0 m/s |
| Propellant per m/s (12.0 kg wet mass ÷ (2,150 s × 9.80665 m/s²)) | 5.691×10⁻⁴ kg/(m/s) |
| Total propellant required this season | 0.011951 kg |
| Total reserve propellant (MA4) | 0.024 kg |
| Mandatory disposal reserve (MA5) | 0.0100 kg |
| Propellant available for avoidance (0.024 − 0.0100) | 0.0140 kg |
| Propellant left over after this season's maneuvers (0.0140 − 0.011951) | 0.002049 kg |

`margin_pct = (0.0140 − 0.011951) / 0.0140 × 100 = 14.64%`. This is comfortably inside SPEC §2's
20% cap, but not by a wide margin — the whole point of the case is that a Hero has to actually
compute this rather than assume either "of course there's enough fuel" or "of course she should
just de-orbit, she's almost out."

**How the margin was tuned to land inside SPEC §2's ~20% cap:** the two real cited facts (the CARA
threshold and the BIT-3's Isp) are fixed and were not tuned. What *was* tuned, deliberately, to
produce a genuinely close call rather than an obvious one: MA4's reserve-propellant figure
(0.024 kg) and MA5's disposal-reserve figure (0.0100 kg). An earlier draft used a much larger
reserve (0.10 kg), which made Option B win by well over 80% — not a real dilemma, since nobody
would seriously argue for de-orbiting a satellite with that much fuel to spare. Shrinking the
reserve to a value consistent with the case's own "aging, low-fuel" framing, and requiring a
disposal reserve that eats a real fraction of it, is what turns this from an arithmetic exercise
into an actual decision. Full reasoning in `RESEARCH_LOG.md`.

---

## Five Socratic questions

1. "Your propellant-budget table says this season's real threshold-crossing maneuvers cost about
   0.012 kg, out of 0.014 kg available. If you round that to 'about a hundredth of a kilogram, out
   of a hundredth and a half,' does that sound safe to you? Now say it as a percentage. Did your gut
   match your arithmetic?"
2. "Two of the six events in Appendix C have a maximum Pc under the real threshold — 2.7×10⁻⁵ and
   8.1×10⁻⁵. Why does the case ask you to compute the absolute-value margin for those events too, if
   they don't require a maneuver at all?"
3. "You used the real Busek BIT-3 specific impulse to get kilograms of propellant per meter/second
   of delta-v. What would happen to your D3 table if Aurora-7's actual wet mass were double what
   this case states? Which of your appendix figures would you go challenge first?"
4. "Appendix D's disposal reserve (0.0100 kg) applies under both options — Option A spends it today,
   Option B defers it to the end of the season. Why does that make the two options genuinely
   comparable on propellant, instead of Option A looking artificially cheap?"
5. "If a seventh conjunction showed up tomorrow, at a probability just over the real threshold, would
   your recommendation survive it? Show me the number that would have to change for your answer to
   flip."

## The trap

**Most learners will eyeball the six probabilities in scientific notation instead of actually
converting and subtracting, and most students will assume a probability that "looks small" is
automatically under the threshold.** Two of the six events in Appendix C are given with a Pc that
looks numerically close to 1×10⁻⁴ (8.1×10⁻⁵ and 1.1×10⁻⁴) — a Hero who skips the standard-notation
conversion and just compares exponents by eye will frequently get these two backwards, either
maneuvering for the one that doesn't need it or missing the one that does. The
case is built specifically so that "close in appearance" and "close in value" are not the same
thing in scientific notation, which is exactly why Challenge D2 forces the standard-notation
conversion and the explicit absolute-value subtraction rather than letting a Hero compare exponents
by eye. A learner who reports which events "cross the threshold" without showing the converted,
subtracted values has fallen into the trap and should be asked directly: "show me the standard-
notation form of both of those probabilities, side by side."

A second, quieter version: a Hero who computes D1's factorial-based combination count correctly but
then treats that count (630, or the 35 pairs involving Aurora-7) as if it were relevant to D2's
per-event risk math has confused "how many things we had to screen" with "how risky any one of
them is." The two are unrelated in this case's actual math — D1 is a scale-of-the-problem number,
not a risk number — and a pitch that tries to connect them ("with 630 pairs, of course something
was going to cross the threshold") is treating a combinatorics result as if it were a probability
statement, which it is not.

## Twist

**A seventh conjunction event is discovered mid-discussion.** At the fifteen-minute mark, deliver
slowly: *"New SOCRATES screening result, just in. A previously uncataloged fragment — debris from
an unrelated collision two weeks ago — has just been tracked for the first time. It's screened
against Aurora-7. Time of closest approach: day 44, one day before the season ends. Maximum
predicted Pc: 6.0×10⁻⁴. Required avoidance delta-v: 5.5 meters per second. You now have sixty
seconds. Are you changing your plan — or not?"*

This crosses the real threshold by a wide margin (6× the 1×10⁻⁴ cutoff — by the same real decision
rule everyone has been using all discussion, this event unambiguously requires a maneuver) and
costs 5.5 × 5.691×10⁻⁴ ≈ 0.003130 kg of propellant. Aurora-7 has only 0.002049 kg left after E2,
E4, E5, and E6 — a shortfall of about 0.001081 kg. **The twist does not make either original
position obviously correct.** It invalidates the confident "the math already showed there's plenty
of margin" version of Option B, since that margin (14.64%) is now provably not enough to cover a
real, newly-discovered threat under the same threshold rule the room has been applying all along —
but it does not vindicate Option A cleanly either, since Option A's Heroes already banked a
zero-data outcome days ago and never had to update anything; the room should be pushed on whether
"I got lucky that my original guess didn't get tested" is the same thing as "I was right."

**The follow-up, which is the actual point:** *"What just broke in your original model? Were you
wrong to recommend Flying The Season — or just missing information that no one, including Priya,
could have had four days ago? And if it's the second one, does that change how much cushion you'd
want built in next time?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. Read the Overview aloud. *"Thirty seconds — de-orbit her now, or fly the season?"* Stand/sit vote, no calculation yet. |
| **3:00–10:00** | Position defense. *"Convince us — not just that your choice feels safer, but that the numbers back you up."* Press anyone arguing from gut feel alone: *"Where's your propellant table?"* |
| **10:00–15:00** | Pressure-test the models. *"Which of the six Appendix C events are you least sure about? Walk me through converting E6's probability to standard notation — is 1.1×10⁻⁴ above or below the real threshold, and by how much?"* |
| **15:00** | **DROP THE TWIST** — the seventh conjunction event, delivered slowly, full pause before "sixty seconds." |
| **15:00–20:00** | Immediate recommit. Re-vote. *"What just broke? Were you wrong, or just missing information?"* |
| **20:00–30:00** | Two threads: **(1) margin vs. certainty** — "a 14.64% cushion looked comfortable until one real event ate through it — how much cushion would you actually want, and what would you give up to get more of it?"; **(2) combinatorics vs. risk** — "D1 told you there are 630 possible pairs in this screening population. Does that number tell you anything about how likely any single one of them is to actually threaten Aurora-7? Why or why not?" |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, today's case is a real risk-and-resource trade-off: a satellite operator has to decide
whether "the math says it's probably fine" is good enough when there's no fuel left for a second
mistake.

### Launch
Read the Overview aloud, then show Appendix A's real threshold table (1×10⁻⁴) without yet showing
Appendix C's event log. *"Every satellite operator alive uses a number just like this one to decide
whether to spend fuel dodging debris. Priya has six real screening results this week. Which way do
you think she should go — end it clean now, or fly it out?"*

### Anchor 1 — Take a stand and vote
De-Orbit Now or Fly The Season. No reasoning yet. Hands up, write the split on the board.
*"Is anyone courageous enough to stand with flying it, knowing she's almost out of fuel?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- What is the actual question? Is it "will Aurora-7 get hit"? "Can she afford to try to avoid every
  possible hit"? "Can she afford to avoid the ones that actually matter, by a real rule, and still
  have fuel left to leave cleanly"? **Those are three different questions.**
- Someone will say "obviously you maneuver whenever there's a chance of a collision." Push: is
  every chance worth spending irreplaceable fuel on? What tells you which chances are worth it?
- Let the confusion grow. *"Wow. This is a genuinely hard question to even state precisely."*

### Anchor 3 — What is the process?
- If we just eyeball the six probabilities in Appendix C, are we done? (No — two of them look
  deceptively close in scientific notation and have to actually be converted and subtracted to
  know which side of the real threshold they're on.)
- Once we know which events cross the threshold, is the propellant question just "add up the
  delta-v's"? (No — delta-v has to be converted into a mass of propellant using the real thruster's
  specific impulse, and that mass has to be checked against what's actually left over, not against
  the full reserve, since some of the reserve is never actually available.)
- Is our question still the right question?

### Anchor 4 — What don't we know?
- What's missing that we'd need to answer this properly? (Priya doesn't know whether more
  conjunctions will be discovered after today's screening — SOCRATES only propagates seven days
  forward, three times a day, and the season is 45 days long.)
- Appendix B's screening-population count (36) and Appendix C's whole conjunction log are stated
  assumptions, not real feed data for a real satellite. Do you believe they're realistic? What would
  you need to see to trust them more?
- MA4's reserve-propellant figure is the single most sensitive number in this case. What would you
  ask Priya to double-check about it before you'd trust either recommendation?

## Data Deep Dive
Walk the room through the factorial-based combination count (D1), the scientific/standard-notation
conversion and absolute-value margin for each event (D2), the compound-unit conversion from
delta-v to propellant mass using the real Isp (D3), and the final decision memo (D4). Ground truth:

| Quantity | Value |
|---|---|
| Total pairwise combinations (36 objects) | 630 |
| Pairs involving Aurora-7 | 35 |
| Events crossing the real threshold | E2, E4, E5, E6 |
| Total propellant required this season | 0.011951 kg |
| Propellant available for avoidance | 0.0140 kg |
| Margin | 14.64% |

## Close
- Vote again. Who moved, and why?
- Was "will there be a collision" the right question, or was it really "is there enough fuel to
  handle the real threats and still leave clean"?
- What math was new to you here — the factorial simplification, the notation conversion, or the
  compound-unit conversion at the end?

## Lessons Learned
The case's real lesson is that a "close call" in scientific notation is not something you can
eyeball — two probabilities that look similar as exponents can be on opposite sides of a real
decision threshold once actually converted and subtracted, and a resource margin that looks
comfortable (14.64%) can be consumed entirely by a single event nobody could have predicted four
days earlier. Both of those are genuine properties of the math, not manufactured drama.

## Standards Touched On

**New coverage:** none — see `case.json.reinforcement_note`. This case reinforces all 5 remaining
thin (n=2) skills in Advanced Operations/Scientific Notation, Factorial, Absolute Value from n=2 to
n=3, the group's entire remaining thin set, plus reinforces Scientific Notation and its reverse
how-to (n=5→6) and the compound-units how-to (n=19→20).

**Claimed:** Standard Notation · Factorial · Absolute Value · Scientific Notation · How to write a
number in standard notation given its scientific notation · How to evaluate a factorial expression
· How to write a number in scientific notation given its standard notation · How to convert an
amount with compound units

## Facilitator note — sensitivity

None required. This is an engineering/operations resource decision (fuel and risk management for a
satellite) with no death, illness, or family-hardship stakes — SPEC §6 does not apply.
