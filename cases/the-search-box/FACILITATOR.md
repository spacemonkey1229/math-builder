# FACILITATOR.md — The Search Box

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no marker comment for this by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object.*

**Case:** The Search Box · **Tier:** T3 · **Studio:** MS Adventure
**Standards:** Pre-Calculus — Polar Coordinate, Parametric Equation, Parameter, How to convert a
point between rectangular and polar coordinates, How to graph a polar equation, How to eliminate
the parameter to find a rectangular equation (see `case.json.standards[]` for exact ids).

**Status:** Researched and computed 2026-08-30; sensitivity-model-verified 2026-08-31
(`sensitivity_model.py`). All `{{NEEDS_SOURCE}}` tokens in `case.md` are closed
(`RESEARCH_LOG.md`). The D1–D5 arithmetic is done and recorded below and in
`case.json.balance`.

## Sensitivity note — read before running this case (SPEC §6, human-reviewed)

This case is a person-overboard search-and-rescue scenario. It was flagged for facilitator review
under SPEC §6 and human-reviewed 2026-08-30: **confirmed acceptable for the HS-entry/HS band this
case targets**, on the condition that the framing stays centered on the successful-rescue decision
and the real Coast Guard leeway/set-and-drift modeling methodology — not on graphic peril.

The Overview and Background were written to that discipline on purpose: present-tense procedural
urgency (fuel state, daylight, a family waiting), no injury or peril detail, and the scene stops at
the moment of the coordinator's decision. If you run this case with a younger cohort, or a cohort
with a student who has a personal connection to a maritime incident, preview the Overview yourself
first and consider whether to soften the discussion framing further (e.g., emphasize that both
candidate boxes represent live, real Coast Guard methodology used every day to find people
quickly — this is a "how do we choose well" case, not a "what went wrong" case). The case's own
narrative never states an outcome; it ends at the decision, and that is intentional — do not let
discussion drift into speculating about the person's fate. Keep the room's energy on the modeling
choice, not on the stakes underneath it. Every anchor, the Twist, and every Socratic question below
were written and re-checked against this same discipline: methodology and decision-making only.

**Balance flag, read before you facilitate:** on the primary metric (estimated probability of
detection per flight-hour), the Set-and-Drift Datum (Option B) beats the Windward Datum (Option A)
by **margin_pct = 15** (`case.json`) / **≈15.1%** (this file's own more precise arithmetic below) —
inside SPEC §2's ~20% cap. Both candidate boxes are POD-saturated (POD ≈ 0.9999 for each) given the
stated helicopter endurance and sweep width relative to either box's area, so the real margin is
driven almost entirely by the probability-of-containment (POC) gap in Appendix E, not by box size.
**This was checked against a runnable model 2026-08-31** (`cases/the-search-box/sensitivity_model.py`,
Tier 2 Probe 5). Appendix F's own prose asserted that MA12 (Option B's search-radius growth rate)
"can flip the recommendation" if a real figure turns out smaller than ~0.35 kt, and that MA13
(Option A's assumed POC) flips it above ~61%. **The model does not confirm either claim as stated:**

- **MA12 (growth_rate_B_kt):** a ±50% swing (0.225–0.675 kt) does **not** flip the recommendation
  in either direction — Option B stays coverage-saturated across that whole range, so its
  POD-per-flight-hour barely moves off its ceiling (POC_B ÷ search endurance ≈ 0.1704). Lowering
  the figure does **not** narrow Option B's advantage the way Appendix F used to claim — the metric
  is flat, not falling. The real flip only happens if this dial is instead pushed roughly
  **3.4× larger** than stated (~1.55 kt, a +244% swing) — a much larger and differently-directed
  move than "smaller than 0.35 kt."
- **MA13 (poc_A_pct):** a +50% swing (55% → 82.5%) **does** flip the recommendation to Option A; a
  −50% swing does not. But the real threshold, verified by bisection, is Option A's POC exceeding
  **≈64.75%** — Option B's own sourced POC (S8) — not ~61%. Because both options are POD-saturated,
  the comparison reduces almost exactly to POC_A vs. POC_B, so the flip point sits at the point
  where the two POC figures cross, not below it.

Appendix F's prose has been left as an author-stated Modeling Assumption rationale (it still
correctly identifies MA12 and MA13 as the two load-bearing, flippable dials — that direction is
right), but the specific thresholds quoted there are **superseded by the verified figures above**.
Facilitate from the numbers in this section, not from Appendix F's original thresholds. `MA13`'s
instability is recorded in `case.json.sensitivity_disclosure[]` (category X — the true divergent-
datum POC is knowable in principle but not published as an exact digit; 55% is a documented
good-faith estimate below the real 64.75% single-point figure, consistent with CGADD Figure H-22's
graphed shape).

## Intro

Frame the format before anything else: this is a real search-planning decision under a hard
fuel/daylight constraint, not a worksheet. Name the opener — "You are Dana Okafor, Search and
Rescue Mission Coordinator, and the helicopter crew chief just told you: one search box, not two.
Two transparencies on the light table, both built from the same radar fix, and they don't agree."
Let the stakes land — the flight-hour budget is real and finite — before moving to the Launch.

## Launch

Show Appendix C and Appendix D's two drift models side by side — the Windward Datum's wind-driven
leeway numbers, the Set-and-Drift Datum's current-driven numbers — with no Appendix E numbers yet.
Ask: "Just looking at where each model says to look, which one would you send the helicopter to?
On what?" Do not confirm or correct answers here. Most rooms will reach for "the option with the
smaller, faster-to-search box" or "the one with the stronger-sounding methodology" — both instincts
are worth recording out loud before anyone touches Appendix E's probability-of-containment figures,
because both are exactly the trap (see below).

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the Set-and-Drift Datum — the option built on the model
with no stated divergence angle?" Show of hands, both options, no discussion. Record the count —
Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which box is
more likely to contain the person," but push on what "estimated probability of detection" actually
means: "The Background says outright that Dana's recommendation is judged on one number — probability
of detection per flight-hour, not box size and not probability of containment alone. So what does
that combined quantity actually protect against, and why is it harder to eyeball than just picking
the smaller box?" If the room lands on "we need to know how likely we are to find the person for
every hour of flying we spend, not just which box is more likely to contain them in the abstract"
on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which box is more likely to contain the person" from "which box gives the
best detection odds per flight-hour," ask them to name the actual steps before touching the
appendices: convert the radar fix to a rectangular datum (D1, Appendix B), write each drift model
as parametric equations in elapsed time (D2, Appendices C/D), eliminate the parameter to get each
model's rectangular search box (D3), graph each option's polar search-radius boundary (D4, Appendix
E's coverage/POD relationship in mind), then combine box area, flight-hours, and Appendix E's POC
figures into a POD-per-flight-hour decision table and recommendation (D5). Re-ask: "Is our question
still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix C's wind speed/direction (MA8/MA9), Appendix D's current
speed/direction (MA10/MA11), Appendix D's growth-rate constant (MA12), and Appendix E's Windward
Datum POC (MA13) are all stated Modeling Assumptions, not sourced figures. Ask which ones actually
change the *graded* D5 result if they move. MA1, MA2, MA3, MA4 and the position/bearing assumptions
(MA5–MA9, MA11) scale or relocate both boxes together and don't flip anything by themselves (see
case.md's own Appendix F "Sensitivity" column). The honest answer for what *does* matter is MA12
and MA13 — but push further than the case's own printed claim: "Appendix F says MA12 can flip the
recommendation if it drops below about 0.35 kt. Does that actually check out, if both boxes are
already about as close to 100% probability of detection as they can get?" Let a sharp Hero reach
the real, verified answer themselves before confirming it (see the Balance flag above and the
Twist below) — a smaller growth rate makes an *already-saturated* box's number move less, not more.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's conversion, D2's two parametric models, D3's two
eliminated-parameter boxes, D4's two polar boundaries, and D5's POD-per-flight-hour comparison
together as a room, cold-calling for D5 specifically — this is where a Hero who correctly found
the Windward Datum's box slightly smaller will visibly struggle to explain why the Set-and-Drift
Datum still wins. That struggle is useful information for the facilitator, not a moment to rescue.

**Facilitator-only arithmetic note (see `sensitivity_model.py` for the checked, runnable version).**
Elapsed time t = 2.5 hr; search endurance = 3.8 hr; sweep width = 0.4 NM; search speed = 90 kt;
optimal search factor fs = 1.1. Option A (Windward Datum): E(t) = 0.35 × 2.5 = 0.875 NM; R = 1.1 ×
0.875 = 0.9625 NM; box (side 2R) area = 1.925² = 3.706 sq NM; coverage factor C = (0.4 × 90 × 3.8) /
3.706 = 36.9; POD = 1 − e^(−36.9) ≈ 0.9999; POC = 0.55 [MA13]; POD-per-flight-hour = (0.9999 × 0.55)
÷ 3.8 ≈ **0.1447**. Option B (Set-and-Drift Datum): E(t) = 0.45 × 2.5 = 1.125 NM; R = 1.1 × 1.125 =
1.2375 NM; box area = 2.475² = 6.126 sq NM; C = (0.4 × 90 × 3.8) / 6.126 = 22.3; POD = 1 − e^(−22.3)
≈ 0.9999; POC = 0.6475 [S8]; POD-per-flight-hour = (0.9999 × 0.6475) ÷ 3.8 ≈ **0.1704**. Both
figures match `case.json.balance.computed_2026-08-30` to four decimal places, and `sensitivity_model.py`
reproduces them exactly (2026-08-31 verification run). The margin (Set-and-Drift ahead) is
100 × (0.1704 − 0.1447) / 0.1704 ≈ **15.1%**, matching `case.json.balance.margin_pct = 15`.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"A meteorologist on watch overhears the Set-and-Drift Datum's growth-rate number and pushes back:
'That 0.45-knot-per-hour figure was never measured — it was set by analogy to the wind model's own
published uncertainty, because no equivalent Coast Guard table exists yet for surface-current
drift estimates. For tonight's sea state, the real uncertainty could plausibly run twice that
high.'"

"If the Set-and-Drift Datum's growth-rate assumption were really twice what Appendix D states,
does the recommendation change?"

**Facilitator-only: what this actually does, and does not, change.** Run it: doubling MA12 from
0.45 kt to 0.9 kt (well beyond a ±50% swing) still does **not** flip the recommendation —
`sensitivity_model.py`'s bisection shows the real flip threshold sits at roughly **1.55 kt**, about
3.4× the stated value, because Option B's box is already deep in the POD-saturated regime (coverage
factor ≈ 22, POD ≈ 0.9999) at the stated 0.45 kt. Growing the box further keeps shrinking the
coverage factor, but POD stays pinned near 1.0 across the whole doubled range, so the
POD-per-flight-hour figure barely moves. **The twist reframes, it doesn't resolve:** it corrects a
mistaken intuition (that an unsourced, "could easily be bigger" assumption is automatically the
case's weak point) with a genuinely different one — the case's real fragility, per the verified
model, is entirely on the POC side (MA13), not the growth-rate side (MA12), even though MA12 is the
dial with the shakier sourcing story. A Hero who only checks "which assumption looks least trustworthy"
will pick MA12; a Hero who actually runs the sensitivity math finds the real answer is MA13. That
gap — between which assumption *looks* fragile and which one *is* fragile — is the point of this
twist, and it stays entirely inside the modeling methodology, never touching the person in the water.

## Immediate recommit

Re-vote immediately. Ask by name: "Does doubling the growth-rate assumption change your vote — or
does it just tell you that 'looks unsourced' and 'is load-bearing' are two different things?" That
distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **A smaller box is not the same as a higher probability of detection.** The Windward Datum's box
   is smaller (3.706 vs. 6.126 sq NM) — yet it loses D5. Why does looking only at box size mislead
   here, and what does POD-per-flight-hour's dependence on both coverage factor *and* probability
   of containment actually protect against?
2. **The assumption that looks shakiest is not always the one that matters most.** The Twist shows
   that doubling MA12 (the assumption with no published source at all) barely moves the answer,
   while a much smaller relative change in MA13 (also unsourced) flips it outright. What should
   that tell the room about how to spend limited fact-checking time on a real recommendation?
3. **Both options are already "almost certain" to detect — so why isn't this an easy call?** POD is
   ≈0.9999 for both boxes. Is a decision this close, between two options that both look
   near-perfect on the headline number, still worth a firm recommendation — or does the case's own
   ~15% margin argue for stating real uncertainty rather than false confidence?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show both drift models side by side, cold-call for a gut read, no POC/POD numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your box actually wins on detection odds per flight-hour, not just on being smaller or easier to search"* |
| 10:00–15:00 | Pressure-test the models — *"Which of MA12 or MA13 would have to change, and by how much, for your answer to flip?"* |
| **15:00** | **DROP THE TWIST** — the surface-current growth-rate figure might be twice as large as stated, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (box size vs. detection odds; which assumption looks fragile vs. which one is fragile; is a close, near-saturated margin worth a firm call) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

The plausible wrong answer is picking whichever box is smaller — "faster to fully search, more
efficient" — without checking that a smaller box searched completely can still carry a *lower*
probability of detection than a larger box, once each model's own probability-of-containment figure
is folded in. The Windward Datum's box is smaller and still loses. The real skill being tested is
combining area, effort, and POC/coverage factor into a POD-per-flight-hour figure, not eyeballing
box size. A second, subtler trap: students who successfully eliminate the parameter in D3 may
assume the resulting rectangular search box is a simple axis-aligned box with a constant safety
margin in every direction — but D4 asks them to graph a polar r(θ) boundary specifically because
the total-probable-error radius is not necessarily uniform by bearing, and a student who skips D4
and just pads D3's box uniformly will get a plausible-looking but wrong area for the POD
calculation in D5. A third trap, surfaced by the Twist: assuming the assumption with the weakest
sourcing story (MA12) must also be the assumption the recommendation is most sensitive to — the
verified model shows the opposite is true here.

## Socratic questions

1. Your D1 conversion turns the vessel's own bearing-and-range fix into a rectangular datum on the case's search grid — what would change about the Windward Datum and the Set-and-Drift Datum if the vessel's own position had been recorded incorrectly?
2. Both drift models start from the exact same converted datum and the exact same elapsed time — so where, precisely, in your D2 parametric equations does the disagreement between the two boxes actually enter?
3. You eliminated the parameter in D3 to get a rectangular equation for each model's drift centerline — what does the resulting search box lose, compared to the parametric equations you started with, that D4's polar graph puts back?
4. Your D5 table combines each box's area with its probability-of-containment figure — could a box with a *smaller* area ever have a *higher* probability of detection per flight-hour than a larger one, and under what condition?
5. Appendix F flags both MA12 (the Set-and-Drift Datum's growth-rate constant) and MA13 (the Windward Datum's probability of containment) as assumptions that could flip your recommendation if they were wrong — if you could only re-check one of the two before committing the helicopter, which would you pick, and what about your own D5 math tells you that one matters more?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
the Set-and-Drift Datum at Anchor 1 purely on "the box felt more efficient" and stays with the
Set-and-Drift Datum after the Twist for a *different, POD-per-flight-hour-based* reason has
genuinely moved, even if the vote count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "which assumption is actually load-bearing" question landed as a discovery or
  had to be told outright.
- Whether the "smaller box vs. higher detection odds" trap was the actual sticking point, or
  whether D3/D4's parametric-to-polar chain itself was the harder gate for most Heroes.
- Whether the growth-rate Twist felt like a genuine "check your intuition against the math" moment
  or felt like a technicality — worth listening for directly, since this case's own verified
  sensitivity model found a real, load-bearing-but-different-than-printed finding (MA13, not MA12,
  is the assumption that actually flips the recommendation).

## Standards Touched On

Polar Coordinate · Parametric Equation · Parameter · How to convert a point between rectangular and
polar coordinates · How to graph a polar equation · How to eliminate the parameter to find a
rectangular equation
