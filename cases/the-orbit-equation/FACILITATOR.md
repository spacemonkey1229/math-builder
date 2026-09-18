# Guide Notes: The Orbit Equation

MS/HS | Guide Notes | Launchpad | 2026-27
**Tier:** T3 (HS-entry) · **Primary metric:** percent of frame the boss occupies, per ms of per-frame camera computation · **Margin:** 3.71% (A wins, base case — very thin, and the twist flips it — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, Devon has one camera path to lock before tomorrow's blocking review, and two candidates that both look genuinely good in isolation. One is a cheap, unwavering circle. The other tightens dramatically at exactly the right moment — and costs more math, every frame, to pull off. There's no camera I'd pick either — Devon's lead doesn't know until the numbers are run.

## Launch

Show a short clip or GIF of an orbiting third-person camera (any boss-fight or action game will do) and ask: *"If you were the camera engineer, would you rather lock in a camera that does the exact same thing every single frame, or one that changes what it's doing depending on what's happening in the fight?"*

Let them argue it cold, no numbers yet. Then: *"Devon has to hand off one rig tomorrow morning. Same boss, same arena, completely different bet on how the camera should behave."*

> **Hero name — which rig do you ship? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

The Fixed-Radius Orbit or The Variable-Radius Push-In. No reasoning yet.

Hands up for A (Fixed). Hands up for B (Push-In). Write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What's the actual question, in one sentence?
- Is it "which rig frames the boss best at the most dramatic moment"? Is it "which rig is safest against the arena wall"? Is it "which rig delivers the best framing for the compute it costs, averaged across the whole fight"? **Those sound similar and are not the same question** — only the last one is what Devon's rig is actually graded on.
- Someone will say "obviously the Push-In, it looks way better in the trailer moment." Push: *"Better where, exactly? At one instant, or across the whole fight?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — that's not as obvious as it sounded a minute ago."* Do not rescue them.

**The trap to let them walk into:** most learners will fixate on the single dramatic telegraph frame — the Push-In's 25.00% vs. the Fixed Orbit's 16.67%, a 50% relative improvement — and conclude the Push-In is clearly the better rig. The real trap is that this is only *one* of the eight sampled frames in the fight, and the Push-In also pays its extra per-frame compute cost on *every single one* of those eight frames, not just the flashy one. Averaged honestly across the whole orbit, the Push-In's framing edge shrinks from a dramatic 50% at one instant to a modest 6% overall (17.68% vs 16.67%) — not enough to outrun its higher cost. A learner who grades the rig on its best moment instead of its average, and who never actually runs D3's arithmetic, will misjudge which rig is really ahead.

## Anchor 3 — What is the process?

- What's the process we'll go through to answer it?
- If we just compare the two rigs' framing at the flashiest moment, are we done? Is that the same as comparing what the camera does across the *entire* fight?
- If we end up with two numbers like 833.33 and 803.55, how do we decide that's close enough to be a real discussion, versus one rig just winning? What's our tiebreaker *before* we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What's missing that we'd need to answer this properly?
- Appendix E gives you the assumptions behind every non-sourced figure — the clipping radius, the framing formula's constant, both per-frame compute costs, and the push-in's depth. Do you believe them? None of them are pulled from a real published number for any specific game's own arena geometry or camera-code timing — **have them actually try a bigger and a smaller push-in depth and see how much the comparison moves.**
- What are we assuming stays fixed about the animation team's plans for tomorrow's blocking review? (This is the case's built-in opening for the twist — don't tip it.)

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — confirm Option A is really a fixed orbit (D1).** Convert two or three of Appendix B's waypoints to polar form: e.g. W1 = (12.73, 12.73) → r = √(12.73² + 12.73²) ≈ 18.00, θ = 45°. Every waypoint converts to r ≈ 18 — confirmed fixed-radius.

**Step 2 — graph both rigs and check clipping (D2).** r_A = 18 for all θ. r_B(θ) = 18 − 6 cos θ ranges from a minimum of 12 (at θ = 0°, the telegraph angle) to a maximum of 24 (at θ = 180°). Minimum radius 12 vs. the 8.5-unit clipping radius (Appendix C) — clears by 3.5 game-units. Safe, but not by a huge margin.

**Step 3 — framing and cost (D3).**

| Rig | Avg. percent of frame | Per-frame cost | Primary metric (percent/ms) |
|---|---|---|---|
| A — Fixed-Radius Orbit | 16.67% (constant at every angle) | 0.020 ms | **833.33** |
| B — Variable-Radius Push-In | 17.68% (averaged over the 8 sampled angles) | 0.022 ms | **803.55** |

**The Fixed-Radius Orbit wins by 3.71%** — comfortably inside the 20% balance cap, and genuinely thin.

**Push the room directly:** *"At the telegraph moment alone, the Push-In beats the Fixed Orbit by 50% (25.00% vs 16.67% of frame). Why does the Fixed Orbit still win overall?"* (Answer, if nobody gets there: that 50% advantage only exists at one of eight sampled frames; at the other seven the Push-In is often *worse* than the Fixed Orbit — e.g. 12.50% at θ=180° vs. the Fixed Orbit's constant 16.67% — and the Push-In pays its higher per-frame cost at all eight frames, not just the good one.)

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"The animator's back at your desk. She watched the Push-In clip again."*
>
> (pause)
>
> *"She wants it more dramatic. 'Push in harder,' she says. 'Make the room actually flinch.'"*
>
> (pause)
>
> *"You bump the push-in depth from 6 game-units to 9. Recheck your numbers before you say yes."*

**Facilitator only — read before you drop this, do not read aloud.** Amplitude 6 → 9 raises the Push-In's average frame percentage from 17.68% to 19.25% (compute cost is unchanged — the governing equation isn't more complex, just deeper). Recompute Step 3: Push-In's ratio becomes 19.25 / 0.022 = **874.82**, beating the Fixed Orbit's unchanged 833.33 by **4.98%** — **the winner flips to B.** But also recheck Step 2: the Push-In's minimum radius drops from 12 to 9 game-units — the clipping radius is 8.5, so the rig now clears the wall by only **0.5 game-units**, down from 3.5. Confirm a room that gets there against these numbers, not just the vibe — this is a real, computable flip (and a real, computable near-miss on the wall), driven by exactly one dial (the push-in depth), not a vaguely-worded "make it better" twist.

Now: **"Sixty seconds. Do you sign off on the deeper push-in — or not?"**

## Immediate recommit

- Who is **not** changing their pick? Why?
- Who is reconsidering, even if they're not flipping?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this one.)
- Who built their case entirely on "the flashy moment looks better" without ever running D3's full-orbit average?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Cheap-and-flat vs. expensive-and-dramatic.** The Fixed-Radius Orbit's cost structure never changes no matter how the framing constant is argued about — it's the same two trig evaluations every frame, always. *"If the Push-In only wins by 5% even at a deeper push-in, and it's already living dangerously close to the wall, is 5% worth the risk of a clipping bug a playtester will actually see?"* Push toward: a thin *numeric* win doesn't automatically mean the safer engineering choice is wrong to prefer — the case doesn't resolve that judgment call, it just makes the trade-off visible.

**Thread 2 — Fragility to a single number.** Every non-sourced figure in Appendix E (clipping radius, framing constant, both per-frame costs, push-in depth) is a disclosed production assumption with no real public source behind it. Flex either per-frame cost by 50% in either direction, and the winner flips *and* blows past the 20% balance cap (see `sensitivity_model.py` — do not read this section aloud, but use it to steer questions). *"Which rig would you defend to a lead who asks 'what if the Push-In's math is actually a hair more expensive than you estimated?'"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — Fixed or Push-In?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just flashier."* · *"What's your rig's actual percent-of-frame-per-millisecond — the real number, not a guess."* |
| **10:00–15:00** | Pressure-test the models. *"Which rig is more fragile to one wrong cost estimate?"* · *"How close is the Push-In really cutting it against the wall?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Do you sign off on the deeper push-in — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: cheap-and-flat vs. expensive-and-dramatic · fragility to a single cost assumption. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: a polar equation tells you exactly how far the camera is from
the boss at every angle, and averaging a rate over a full orbit — not just its best moment — is what
turns a flashy single frame into an honest comparison. The Fixed-Radius Orbit's win (3.71%) is real
on tonight's numbers, and it is also razor-thin — a single, disclosed production dial (the push-in
depth) flips it with a completely plausible, entirely reasonable creative request. That is a
**disclosed, not eliminated** sensitivity — `case.json.sensitivity_disclosure[]` carries a Category-F
entry for both per-frame compute costs and for the push-in amplitude, because none of them can be
tightened by more research; they are genuine studio-internal production unknowns no public source
measures.

A facilitator running this room should say plainly what the case says: The Fixed-Radius Orbit wins on
the numbers as modeled, that win is real, and it is also genuinely fragile to a single, easily
plausible creative decision — both things are true at once, and naming both is stronger than picking
one.

---

## Standards Touched On

**Polar Coordinate · Unit Circle · Tangent Function · How to convert a point between rectangular and
polar coordinates · How to graph a polar equation · How to find the sine, cosine, and tangent of an
angle using the unit circle.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]`
reinforces 6 already-thin (n=2) skills rather than claiming a strictly uncovered (n=0) one — none
exist in either target group or the adjacent Vectors group this case's D4 also touches.

---

## Facilitator note — sensitivity

No SPEC Section 6 subject-matter sensitivity applies. This is a game-engineering production decision
with no death, illness, or family-hardship stakes.
