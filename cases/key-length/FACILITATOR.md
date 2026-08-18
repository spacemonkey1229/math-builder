# Guide Notes: Key Length

**Case:** Key Length · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Factoring group (partial, Basic Operations) + Digit/Odd (Number Sense) + Logical
Statement (Discrete Mathematics) — all `new_coverage` (see `case.json.standards[]` for the exact
ids)

Researched and margin-resolved 2026-08-12 (`margin_pct` = 14.48, see `sensitivity_model.py`). This
file is re-checked for drift at every readiness run (the continuity checks in `case-readiness`).

## Intro

Frame the format before anything else: this is a real training-design decision built on the exact
math that makes online security work, not a worksheet. Name the opener — "Forty minutes, a
whiteboard, and two numbers. Only one of them is going on tomorrow's slide." Let the stakes land
before moving to the Launch.

## Launch

Write 143 and 323 on the board with no other information. Ask: "Which one do you think is harder to
factor, just by looking at it?" Do not confirm or correct answers here. The point is a gut read
before anyone touches a calculator.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Elena on Candidate B — the one that takes longer to
factor?" Show of hands, both options, no discussion. Record the count — Close will ask them to vote
again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What does 'better for the exercise' actually mean?"**

Let confusion grow here — this is deliberate. Heroes will want to reach for "faster to factor =
better, wastes less time" as the obvious rule. Push on it: "Elena isn't trying to finish fast. She's
trying to hit a specific target difficulty. Is faster always better for that?" If the room starts
asking "what's the target?" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the actual steps before touching the
appendices: factor both candidates (D1-D2), understand why oddness alone doesn't guarantee safety
(D3-D4), connect the toy exercise to real key sizes (D5), then compare both candidates' actual
difficulty to Elena's stated target (D6-D7). Re-ask: "Is our question still the right one, now that
we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix D's two Modeling Assumptions (MA1 Elena's target
difficulty, MA2 the two candidate numbers themselves) are stated, not sourced from a public
database — no public archive of real training-exercise moduli exists. Ask which one actually
changes the recommendation if it moves (MA1 — see Data Deep Dive).

## Data Deep Dive

Now, and only now, the numbers. Walk D1-D6's factoring and D7's margin comparison together as a
room, cold-calling for D1/D2 (the actual trial-division process) and D6 (the target-distance
comparison) specifically — these are the two places a Hero who stops at "which one is easier" and
never checks the target will visibly miss the point, which is useful information for the
facilitator, not a moment to rescue.

**Facilitator-only factoring note.** Candidate A = 143: test 2 (no), 3 (no), 5 (no), 7 (no), 11
(yes, 143 = 11 × 13) — **5 primes tested**. Candidate B = 323: test 2, 3, 5, 7, 11, 13 (all no), 17
(yes, 323 = 17 × 19) — **7 primes tested**. Both factor pairs are two odd primes (D3); 143 itself is
a clean counterexample for D4 (odd, but not prime — 11 × 13).

**Facilitator-only margin note.** √143 ≈ 11.96, √323 ≈ 17.97. Elena's target is **15.2**. Distance:
Candidate A = |11.96 − 15.2| = **3.24**, Candidate B = |17.97 − 15.2| = **2.77**. Margin: **14.48%**,
Candidate B wins (closer to target). This margin holds Candidate B as the winner across a ±50% flex
of MA1's calibration buffer (effective target 15.125-15.275) — margin ranges 10.09%-18.68%, no flip.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"It's the middle of the discussion. Elena double-checks the practice key-generator's logs and finds
a bug in its random seed — Candidate B wasn't actually generated correctly. She reruns it with the
corrected seed."

"The corrected Candidate B is a different number. Does it still deserve more trust than Candidate
A?"

**Facilitator-only: what the numbers actually do.** The corrected Candidate B is **391** (17 × 23),
not 323 — a real, disclosed generator-bug scenario. Recomputed: √391 ≈ 19.77, distance from target
= |19.77 − 15.2| = **4.57** — now *larger* than Candidate A's unchanged 3.24. **The verdict flips:
Candidate A is now the closer match**, by a real **29.12%** margin. Do not hand this reasoning over
unprompted; let a Hero who did D6 carefully recompute Candidate B's square root with the corrected
value — the real skill being tested is recognizing that a "closer to target" verdict is only as
trustworthy as the number it was computed from.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the correction change your vote, or just how confident you
are in it?" That distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20-30 min)

1. **Easier isn't automatically better.** Candidate A takes less time to factor. Why does the case's
   actual verdict favor the *harder* one — and what would it take for "easier" to actually be the
   right call?
2. **Necessary vs. sufficient.** D3 shows every valid candidate must be odd. D4 shows odd alone
   doesn't make a number prime, let alone secure. Where else in real security does "meets one
   necessary condition" get mistaken for "is actually safe"?
3. **A verdict that flips on a generator bug.** The twist doesn't change Elena's target or her
   method — only the input data. Is a margin that can flip from a corrected random seed ever really
   "safe," or is that exactly why real systems double-check their own key generation?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — write both numbers on the board, cold-call for a gut read, no factoring yet |
| 3:00–10:00 | Position defense — *"Convince us faster-to-factor isn't automatically the better choice"* |
| 10:00–15:00 | Pressure-test the models — *"Whose distance-from-target is most fragile?"* |
| **15:00** | **DROP THE TWIST** — the generator-bug correction, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (easier vs. better; necessary vs. sufficient; a flip on a generator bug) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will assume the "easier," faster-to-factor candidate (A) must be the better teaching
choice, since it wastes less of the room's time — and will skip actually computing D6's distances,
never noticing that Candidate B, despite taking longer, is the one that actually matches Elena's own
stated target difficulty. Watch for a pitch that reports both candidates' trial-division counts and
never compares them to the target — it has not actually made Elena's decision.

## Socratic questions

1. Candidate A is the "easier" number, Candidate B is closer to Elena's target. Why isn't "easier" automatically the better choice for a training exercise?
2. D3 explains why every candidate built this way must be odd. D4 asks whether being odd is enough to call a number "safe." What's the difference between a necessary fact and a sufficient one?
3. Appendix B explains why nobody needs to test past √N. If a candidate's square root were much larger, what would that do to how long the exercise takes — and does D6 already show you that relationship?
4. D5 connects this toy exercise to real 2048-bit and 3072-bit keys. How many decimal digits longer is the real key than the toy candidates, roughly? What does that gap tell you about why nobody factors a real key by hand?
5. Elena has one candidate to put on tomorrow's slide. What does she tell her co-trainer — and does the twist change the answer?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that didn't
move at all after the twist is worth asking about directly: did the twist not land, or did the room
already understand how a corrected input could change the answer?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes distrusted "faster to factor = better" on their own, or needed the twist to see the
  risk of picking on ease alone.
- Whether D3/D4's necessary-vs-sufficient distinction (odd but not prime) landed as a genuine
  insight or was treated as just another vocabulary check.
- Whether the twist's "generator bug, not Elena's own error" framing produced different reflection
  than a self-caused error would have (compare to Apron Order's transcription-error twist).

## Standards Touched On

Factor · Prime · How to factor a number · Digit · Odd · Logical Statement

## Facilitator note — sensitivity

None required (SPEC §6) — the stakes here are a training-exercise design choice, not personal loss
or hardship.
