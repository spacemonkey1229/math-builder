# Facilitator Guide — Constellation Bid

**Sensitivity flag:** none. This is an engineering/business launch-strategy decision about hardware and mission economics, no personal, medical, or family stakes (SPEC §6 does not apply).

---

## The balance

**Argument for A (Consolidated Launch).** On the case's own computed primary metric, A wins: **10 satellites placed for $6.3 million** (1.587×10⁻⁶ sats/$) versus B's **60 satellites for $45 million** (1.333×10⁻⁶ sats/$) — a **19.05%** edge for A. The rideshare price per kilogram is so much lower than a dedicated Electron launch that even though five-sixths of the constellation is stranded in the wrong plane, A's per-dollar coverage still edges out B's guaranteed-but-expensive full deployment.

**Argument for B (Distributed Launch).** B is the only option that actually finishes the mission — all 60 satellites, zero placement risk, zero dependence on a propellant budget holding up under real flight conditions. A's 19.05% "win" depends on treating 50 stranded satellites as an acceptable trade for a lower sticker price; a constellation architect answering to a coverage map, not a spreadsheet, would call a five-sixths-incomplete constellation a failed mission no matter what the per-dollar ratio says.

**The margin:** 19.05%, computed as `100 × (ratio_A − ratio_B) / ratio_B` from `case.json`'s `balance.margin_basis`. Just inside SPEC §2's 20% cap — genuinely close, and `sensitivity_disclosure[]` shows it does not survive a ±50% flex on the propellant-allowance assumption in either direction.

## The trap

**There are three traps in this case, and a strong facilitator should watch for all three.**

**Trap 1 — the mechanical one, and the one most Heroes will actually fall into.** Appendix B states Plane 4 and Plane 5 at RAAN offsets of 240° and 300°. A Hero working quickly plugs those numbers straight into the Δv formula instead of first finding the *minimum* angular separation (Appendix B's own footnote: a burn can always go the shorter way around, so 240° is really a 120° separation and 300° is really a 60° separation). It looks convincing because 240° and 300° are literally the numbers printed in the table next to those planes' names — nothing flags them as needing conversion first. A Hero who skips this step gets wildly inflated Δv and propellant figures for two of the six groups, and may mark them NOT FEASIBLE when they are actually identical in cost to Plane 1/Plane 2's already-computed (and correctly feasible-or-not) figures. **Ask directly: "Plane 5 is at 300° — is that really how far it has to burn?"**

**Trap 2 — the headline-cost trap.** A Hero who compares only the headline totals ($6.3M vs. $45M, a >7× gap) or the raw per-kilogram launch rates ($7,000/kg rideshare vs. ~$25,000/kg dedicated) will declare Option A the obvious, overwhelming winner — without ever checking whether the "cheap" satellites can actually reach their assigned planes. Challenge D3 exists specifically to break that reasoning: once the propellant math is done honestly (and Trap 1 is avoided), only the ten seed-plane satellites (Plane 0) are ever feasible at all.

**Trap 3 — the overcorrection, and the mirror image of Trap 2.** A sharper Hero who *does* run the feasibility check correctly may swing too far the other way — concluding Option A is "obviously broken" (it only delivers one-sixth of the constellation!) and recommending B without ever actually computing Option A's per-dollar ratio. But the numbers, run honestly, still show A wins the case's own stated metric by 19.05% — a genuinely close, fragile margin, not a landslide either way. A live cold-solve of this exact case (run during authoring) reached this precise fork: the solver did every calculation correctly, named the metric explicitly, and *still* recommended B over A — not because the arithmetic was wrong, but because they judged "satellites per dollar" the wrong metric for a mission that either closes a coverage gap or doesn't. **That is not a failure of the case — it is the case working as intended: both A and B are genuinely defensible, and the real discussion is about which metric to trust, not just which number is bigger.**

## Five Socratic questions

1. Your table says the Consolidated Launch is more than seven times cheaper per kilogram. So why does the case ask you to compute a propellant budget at all — what does raw launch price not tell you?
2. Option A only correctly places 10 of 60 satellites, yet it still wins on satellites-per-dollar. How can "fewer satellites placed" and "the winning option" both be true at once? What does that say about the metric Aisha's board actually chose to optimize?
3. The propellant allowance is set at 4.0 kg per satellite. If Solara's propulsion lead had signed off on 6.0 kg instead, would the recommendation change? Show the new feasibility table, not just a guess.
4. Appendix C's plane-change formula uses sin(Δθ ÷ 2), not sin(Δθ). Why does the formula divide the angle in half before taking the sine — what would change about the numbers in D3 if a Hero forgot that division?
5. SpaceX's rideshare price has climbed from $5,500/kg to $6,500/kg to $7,000/kg over the years covered in Appendix H. At exactly what price per kilogram does Option A stop winning? Is that price closer to "unlikely" or "a couple of years away" given the pattern?

---

## Intro

Frame the format for the room: this is a Socratic discussion, not a lecture. Name the opener — "Aisha has to recommend one launch strategy to Solara's board before tomorrow's nonrefundable deposit deadline" — and remind Heroes that today's job is to defend a stance with numbers, not just an instinct about which price tag looks smaller.

## Launch

Read the Overview's last two paragraphs aloud, stopping exactly where the case stops: Aisha's cursor over the sine key, the deposit still due tomorrow.

## Anchor 1

**TAKE A STAND AND VOTE. No reasoning yet, just commit.** "Is anyone courageous enough to stand with the Consolidated Launch? With the Distributed Launch?" Count hands or have the room physically stand/sit. No justification allowed yet.

## Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?** "Is 'which option costs less' the right question, or is it 'which option actually finishes the constellation'?" "What do you mean by 'correctly placed' — does a satellite that's stuck in the wrong plane still count as deployed?" Let confusion grow on purpose: "Wow, a cheaper rocket that might not actually deliver the mission — that's a harder question than it looked."

## Anchor 3

**WHAT IS THE PROCESS?** "If we find each group's required delta-v and propellant cost, and each option's total launch cost, how exactly do we decide?" Re-ask Anchor 2's question once the room has a process in hand: "Now that we know how we'd decide — is our question still the right one?"

## Anchor 4

**WHAT DON'T WE KNOW?** "Do we need to assume anything to answer this?" Steer toward Appendix F: the constellation's altitude (MA1), the plane-change modeling formula's use on a RAAN change rather than an inclination change (MA2), the satellite's wet mass (MA3), and — above all — the propellant allowance (MA4) are all stated assumptions, not measured facts. "Which of these, if wrong, would worry you the most?" — the room should converge on MA4 before Data Deep Dive if the discussion is working.

## Data Deep Dive

Now, and only now, work the numbers as a room: unit-circle values, delta-v, propellant feasibility, and the final per-dollar ratio. This is where D1–D4 get compared out loud. Watch for the trap (above) — someone will announce a winner off the headline launch costs alone, and someone else may overcorrect once the feasibility table appears.

## Twist

At roughly the 15-minute mark: **SpaceX's account rep calls with the next rideshare price step — $9,000 per kilogram, up from $7,000, effective on Solara's actual launch window** — grounded in the real, repeated historical pattern Appendix H documents ($5,500/kg in 2019, $6,500/kg in 2023, $7,000/kg in 2026). Deliver it slowly: the call, the new number, nothing else.

Recompute at $9,000/kg (everything else unchanged; full arithmetic in `case.json.balance.twist_effect` and cross-checked by `sensitivity_model.py`'s `evaluate_twist()`):
- Option A's total cost: **$8,000,000** (up from $6,300,000)
- Option A's ratio: **1.25×10⁻⁶ sats/$** (down from 1.587×10⁻⁶)
- Option B's ratio, unchanged: **1.333×10⁻⁶ sats/$**

**The winner flips to B, by a 6.67% margin.** Push: "at what exact price does this flip?" Setting Option A's ratio equal to Option B's gives a breakeven rideshare price of **$8,411.76/kg** (`case.json.derived.breakeven_price_per_kg_usd`) — below that, A wins; above it, B wins.

**"Sixty seconds. Does your recommendation change?"** — this twist is designed to flip a genuine share of the room, since the base margin (19.05%) was already close to the breakeven price ($8,412) relative to the base price ($7,000). Push further: "was 19.05% ever a comfortable margin to build a launch recommendation on, or was it always this close to flipping?"

## Close

**VOTE AGAIN.** "Did we ask the right question at the start? What math was new to you today, and how did you attack it?"

## Lessons Learned

A cheaper price per kilogram is not the same as a cheaper mission — Option A's headline advantage looked overwhelming (>7×) until the trig showed that most of what it launches never reaches where it's supposed to go. The case's real lesson is that a per-dollar *rate* comparison and a raw *total* comparison can point in completely different directions, and only the rate is the metric that actually answers Aisha's question.

## Standards Touched On

Unit circle; tangent function; sine function; cosine function; radian; how to convert between degrees and radians; how to find the sine, cosine, and tangent of an angle using the unit circle; circumference; how to find the measure of the circumference of a circle; ratio.

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch: "Consolidated, or Distributed — thirty seconds, no explanation, stand if Consolidated, sit if Distributed." |
| 3:00–10:00 | Position defense: "Convince us why it's *better*, not just cheaper." Watch for the headline-cost trap (see above). |
| 10:00–15:00 | Pressure-test: "Whose plan is most fragile? What single number, if it moved, would break your position?" |
| 15:00 | **DROP THE TWIST** — the rideshare price step to $9,000/kg. Deliver it slowly: the call, the new number, nothing else. |
| 15:00–20:00 | Immediate recommit: who reverses? "What just broke in your model — or did anything?" |
| 20:00–30:00 | Threaded deep conflict, two threads: (1) rate vs. raw total — is "satellites per dollar" really the right way to score a mission that either finishes or doesn't; (2) assumption ownership — MA4's propellant allowance is the case's real soft spot; whose job is it to verify a number like that before betting a launch-slot deposit on it? |
| 30:00–45:00 | Close, re-vote, reflection: "What math was new to you, and how did you attack it? Was our original question — 'which option costs less' — still the right question, or should it have been 'which option actually finishes the mission'?" |

---

## Cohort bands

See `case.json.cohort_bands[]` for the machine-readable record. Summary:

- **Full (12–20):** run the plan above as written; both 20:00–30:00 threads run.
- **Compressed (6–11):** Anchors 2–3 combine into one pass; run only the sharper of the two threads; total runtime shortens proportionally.
- **1:1/pair (1–2):** no vote at Anchor 1 — the learner states an initial position instead; guide plays devil's advocate directly; twist still lands, "who reverses" becomes "would you reverse, and why."

## Sensitivity note

The base 19.05% margin is genuinely fragile on two of its three stated assumptions: `sensitivity_model.py`'s ±50% sweep shows satellite wet mass (MA3) flips the winner in BOTH directions (+50% flips to B at 26.0%; −50% widens A's win to a 614% cap breach), and the propellant allowance (MA4) breaches the cap at +50% (257%, still A) while −50% leaves the base case unchanged. Constellation altitude (MA1), by contrast, does **not** destabilize the verdict at all across a ±50% sweep — a real, disclosed, and slightly counter-intuitive finding in its own right. **All of this is disclosed, not hidden** — see `case.json.sensitivity_disclosure[]`. The single most dilemma-relevant real-world risk remains the rideshare-price twist above, which is grounded in a real, repeated historical pattern rather than a synthetic stress test.
