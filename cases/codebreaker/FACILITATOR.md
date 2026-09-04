# Guide Notes: Codebreaker

**Case:** Codebreaker · **Tier:** T3 · **Band:** MS-stretch / HS-entry · **Studio:** Heroes Academy
**Standards:** Factorial / scientific notation, permutation & probability, histogram & pie chart,
2-digit multiplication and addition — see `case.json.standards[]` for exact ids.

Migrated from the original 2020 Guide Notes (`source/Y1/Session 4/Codebreaker/Guide Notes.docx`)
into the current 11-anchor ladder. The legacy Open/Q1/Q2/Q3/Close shape is preserved inside
Anchors 1-4 below; nothing from "Lessons Learned" was dropped.

## Intro

Frame the format: this is not a worksheet, it is a decision Charmichael has to defend out loud.
Name the opener before doing anything else — lights off, walk the room in silence, "sit" someone
next to a pre-chosen Hero and pass an envelope hand to hand without a word, the way the original
handout staged it. Let the silence run longer than feels comfortable.

## Launch

Read the Overview aloud, cold, no summary first. Stop at "He doesn't answer yet." Ask: "What code
would you choose, right now, gut instinct, before you've seen either cipher's rules?" Do not let
anyone open Appendix A or B yet.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Alphanumeric? With Circle Shift?" Show of hands, no
discussion. Record the count — Close asks them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'secure'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which cipher has more
possible keys" — push back: "More possible keys than what, guessed how, by whom, over how long?"
If the room lands on its own on "secure against a single guess" vs. "secure against sustained
use" being two different questions, that is the case working as designed. (Original Guide Notes'
Anchor 2: "What question do we need to ask in order to make a decision? Do we agree?")

Once that confusion has run its course, point the room back at Background: London's cable is
explicit that this decision is judged on the probability Klaus's message arrives with zero
errors, not on how many keys a cipher has. That line is now in the packet every Hero reads —
use it to settle Anchor 2's question, not to skip it. The room still has to work out *why* that
stated standard maps onto D7 and not D3, and a Hero is still free to argue London's standard is
wrong; case.md states what the decision is graded on, it does not hand out the arithmetic.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once "secure" has a working definition, ask the room to name the actual steps before touching
Appendix A/B: count what Klaus actually has to write by hand for two real messages (D4) and turn
that into a zero-error transcription probability (D7); separately, count each cipher's keyspace
(D1/D2) and turn that into a blind-guess probability (D3). Naming D4/D7 first here is deliberate —
case.md's own Challenge 3 now walks the deliverables in that order, precisely so the room's first
concrete number is the transcription-probability track, not the keyspace one. Re-ask: "Is our
question still the right one, now that we can see there are two separate probabilities here, not
one — and neither of them gets to just win by being computed first or looking bigger?"
(Original: "How did you get these numbers? Do you agree on that algorithm? What is a
combination? What is a permutation?")

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix D's four conventions honestly: the multiplier range (1-9) the terror cell is
assumed to search, the skip-value range for Circle Shift, the representative multiplier (2) used
in the worked examples, and Convention 4's per-character transcription error rate. Ask which one,
if it changed, would actually flip anyone's recommendation — most Heroes will say none of them
meaningfully change D1's astronomical keyspace number (worth noticing out loud), but Convention
4's error rate is the one that actually moves D7's margin (Probe 5's own sensitivity sweep found
it does, right up toward the SPEC balance cap) — flag that asymmetry now, before Data Deep Dive,
so the room already knows the two tracks aren't equally sensitive to their own assumptions.

## Data Deep Dive

Now the numbers, in the same order case.md's Challenge 3 now presents them. Walk D4-D7 first —
the real character counts (120 vs. 50 across the two required messages), and D7's zero-error
transcription probability built from them (Alphanumeric 83.5% vs. Circle Shift 92.8%, a real,
computed 11.1% margin). Let the room sit with this number as a genuinely close call before they've
seen anything else. Only then walk D1-D3 — the keyspace count and the blind-guess probability D3
derives from it (see `case.json.derived` for the exact figures). The astronomical keyspace number
will still land hard when it arrives; that's fine and expected. What it must not do is arrive
*first* and pre-empt the room's read of D7 before D7 has even been computed — if a Hero tries to
call the vote for Option A the moment D1 lands, redirect: "hold that thought until we've walked
D7 too — which of these numbers is actually what Charmichael's decision turns on?"

## Twist

At roughly the 15-minute mark:

> "A few months later. You are now inside the terror cell. In Klaus's coat, you find a note: one
> of your associates is a trained codebreaker, and they've been quietly collecting every message
> Klaus has sent for the last six months — all encrypted with the same key, the same cipher,
> every time. They didn't need to brute-force 3.63×10²⁷ possibilities. They ran **frequency
> analysis** on the pile of intercepted ciphertext instead — counting which numbers (or letters)
> show up most often and matching that pattern against ordinary written English. Sixty seconds:
> does this change your recommendation, or not?"

This is a real, sound mechanism, not an invented plot device — a monoalphabetic substitution
cipher (a cipher, like Option A here, that always swaps the same plaintext letter for the same
output value every time it appears) preserves the plaintext's own letter-frequency pattern in its ciphertext no
matter how large its one-time keyspace is, which is exactly why real cryptographers consider raw
keyspace a poor stand-in for real security once a key is reused (Wikipedia, "Frequency analysis"
— Appendix E). **Checked against every stated assumption, sequentially and simultaneously**: it
does not depend on which multiplier was chosen (Appendix D Convention 3 — frequency analysis
attacks the *pattern*, not the specific multiplier value), it does not depend on which of the two
required messages is intercepted (Appendix C — it gets stronger the *more* messages accumulate,
which six months of "helpful intel from Klaus," stated in Background, guarantees), and it does
not contradict D1-D3's blind-guess probabilities, which are still correct as *one-shot* guesses —
the twist reveals that "one-shot guess" was never the terror cell's real attack, not that D1-D3's
arithmetic was wrong. It also does not silently hand Option B the win: Circle Shift's tiny
keyspace (≤26 for these messages) means it can be brute-forced by hand in minutes the moment it's
even suspected, which is its own real vulnerability the twist does not erase.

**Follow-up, always:** "What just broke in your model? Were you wrong, or just missing
information?" Some Heroes realize Option A's keyspace argument was never really about resisting
*this one message* — it's about how long the key survives *repeated* use, which depends on
message volume, not raw combinatorics.

## The Trap

Name it explicitly for yourself before the discussion, even if you never say the word "trap" out
loud in the room: **the trap is NOT stopping at D1.** Challenge 3 makes D1-D8 mandatory, so every
Hero who follows the brief computes D7's real, close 11.1% transcription-probability margin —
the metric this case actually grades. The trap survives that: a Hero can correctly compute every
number from D1 through D7, arrive at D8 ("a recommendation weighing each cipher's keyspace,
error-free transcription probability, and how much Klaus has to correctly handwrite by hand"),
and *still* recommend Alphanumeric — not because they skipped the math, but because at the
weighing step they let D1's astronomical, catastrophic-sounding keyspace number override the
graded D7 metric that actually favors Circle Shift. This is a **D8 synthesis failure**, not a
D7 computation failure: 3.63×10²⁷ *feels* like it should dominate any 11-point margin, and
"secure against sustained reuse" reads as higher-stakes than "occasionally miscopies a digit" —
but the case's own framing (Convention 4, `case.json.primary_metric`) says D7 is what Klaus is
actually being graded on for THIS delivery, and D1-D3's keyspace only matters once the Twist's
six-months-of-reuse scenario is in play. A Hero who has all eight numbers right on paper and
still picks Option A has a confident, wrong-shaped *recommendation*, not a math error — that is
the harder trap to catch, because there's nothing to mark wrong in their work up through D7.
As of the 2026-08-18 fix, Background now states London's own stated standard for this decision
in writing (zero-error transcription probability, not keyspace) and D8 asks the Hero to check
their D8 answer against that stated standard by name — the trap now has to survive a Hero who
has read that sentence and still chooses to override it. Watch for a Hero who names D7 as the
"graded" number and picks Option A anyway on a values judgment (key compromise being
irreversible while a resend is merely annoying) — press them: "London didn't ask you which risk
sounds worse. London asked you a specific question. Did you answer it, or a different one?"

## Five Socratic Questions

1. D1 gives the Alphanumeric Cipher a keyspace of roughly 3.63×10²⁷ possible keys. Does a bigger keyspace automatically mean a more secure cipher, once the SAME key gets reused across six months of messages?
2. You computed D7's zero-error transcription probability at a real, favors-Circle-Shift margin of 11.1%. If your D8 recommendation didn't follow that number, what did you weigh instead — and can you say, in the case's own terms, why that thing should outrank the metric Charmichael is actually graded on?
3. Circle Shift's keyspace for "Your brothers are alive" is only 22 possible skip values. Once the terror cell even suspects Circle Shift is in use, how long would it realistically take them to just try all 22?
4. D6's Pigeonhole Principle check says some digit must repeat at least 12 times across your combined Alphanumeric cipher texts. Does your histogram bear that out, and what would it mean if it didn't?
5. If Charmichael only had to send ONE message, ever, would your recommendation change? What does that tell you about which of D1's keyspace or D7's transcription probability actually matters more for THIS case?

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch (see Launch above), 30-second gut-instinct commitments, stand/sit vote — no explanation yet |
| **3:00–10:00** | Position defense: "Convince us why your cipher is better, not just that it feels safer" |
| **10:00–15:00** | Pressure-test: "Whose plan is most fragile if the terror cell gets lucky, or gets patient?" |
| **15:00** | **DROP THE TWIST** — the frequency-analysis note in Klaus's pocket, delivered slowly, with pauses |
| **15:00–20:00** | Immediate recommit: who reverses? "What just broke in your model?" |
| **20:00–30:00** | Threaded deep conflict: (1) raw keyspace vs. real sustained security, (2) Klaus's error-proneness vs. Charmichael's own fluency, (3) one-shot brute force vs. six months of accumulated ciphertext |
| **30:00–45:00** | Close, re-vote, reflection, Lessons Learned |

## Close

**VOTE AGAIN.** "Did we ask the right question at Anchor 2? What math was new to you today, and
how did you attack it — did you look something up, ask a fellow Hero, work it out from scratch?"

## Lessons Learned

*(Preserved from the original Guide Notes, expanded.)* A cipher's raw keyspace and its real-world
security are not the same number. A cipher that is nearly impossible to guess in one try can
still fail if it is reused — the failure mode is about *how the cipher is used*, not just how it
is built. Meanwhile the "weaker" cipher on paper may be the *more secure choice in practice* for
a specific, real person (untrained, under time pressure, writing by hand) precisely because it is
harder for that person to get wrong. Good cryptography, like good case-study math, is never one
number — it's a tradeoff you have to be able to name out loud.

## Standards Touched On

Factorial · Scientific & standard notation · Permutation · Event, outcome, probability · Single-
event probability · Histogram · Pie chart · Bar graph · 2-digit multiplication and addition ·
Comparing values. See `case.json.standards[]` for the full list of spine ids.

## Sensitivity note

This case involves espionage, a fictional terrorist organization, and a civilian source (Klaus)
whose life is explicitly on the line if the wrong choice is made. Keep the discussion's stakes on
the *math* — keyspace, probability, character counts — not on real-world terrorism tactics,
intelligence tradecraft, or violence. If a Hero brings up a real current event, redirect to the
case's own numbers. See SPEC.md Section 6.

## Cohort bands

See `case.json.cohort_bands[]` for the three required bands (Full / Compressed / 1:1).
