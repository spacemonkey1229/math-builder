# Guide Notes: The Hundredth

MS | Guide Notes | Adventure | 2026-27
**Tier:** T2 (MS-core) · **Primary metric:** probability the ruling instrument names the swimmer whose hand reached the wall first, in a close finish · **Margin:** 0.93% (a knife-edge by design — see the sensitivity note before Lessons Learned)

---

## Intro

Heroes, tonight you are the Chief Judge. You are not judging two athletes; you are choosing which instrument gets the last word when the touchpad and the human eye could disagree, knowing the same rule will apply to the next close finish. The real ruling in 2008 stands, and we are not here to overturn it. We are here to look at the evidence the officials faced and the rule that should govern evidence like it. I don't have the answer either.

## Launch

Show the Appendix A claims table with nothing else. Ask: *"Three named sources say three slightly different things. Which of them is a measurement and which is a claim?"* Let them sort it. The point to land: the electronic times are a record; "who touched first" is a claim attributed to people, and the case never settles it.

> **Hero name it — Pad Ranks, or Contact Ranks? Commit out loud.**

---

## Anchor 1 — Take a stand and vote

Pad Ranks (A) or Contact Ranks (B). No reasoning yet. Hands up for A, hands up for B, write the split on the board.

*"Is anyone courageous enough to stand with ______?"*

## Anchor 2 — What is the problem we're solving?

Do **not** let them start calculating yet.

- What is the actual question in one sentence? Is it "who really won?" Is it "which instrument is more accurate?" Is it "which rule is better for every future race?" **Those are not the same question.**
- Someone will say "obviously the video, the video shows what happened." Push: *"A video of what? A frame is a snapshot every so often. And who decides which frame is 'first contact'?"*
- Someone else will say "obviously the pad, it measures to a thousandth." Push: *"Does the pad measure the touch, or the touch plus a delay? And does the rulebook even let the third digit count?"*
- Is that the right question?

> Let the confusion grow. Say it out loud: *"Huh — both instruments have a blur around them. We haven't said how wide."* Do not rescue them.

**The trap to let them walk into:** most learners will treat "0.01 s" as an exact gap and then ask whether the pad could be wrong by 0.01 s. Four things go wrong. (1) They forget a delay common to both swimmers cancels, so only the **difference** between the two lanes matters. (2) They compare the differential lag to zero instead of to the actual reported gap d, missing that the pad and the eye disagree only when the differential lag **exceeds d**. (3) They treat a higher frame rate as the whole video story and forget the human judgment band J. (4) They report the percent difference on an unlabelled base (points vs relative). A learner who does (1)-(4) correctly still has to decide how big the lag is, and nobody measured it.

## Anchor 3 — What is the process?

- What would we need to compute before we can say one instrument is better?
- If we only know the two reported times, how big could the true pad gap be? (D3 shows the report hides a range.)
- If we end up with two probabilities within a point of each other, how do we decide that is a real discussion rather than a tie? What is our tiebreaker *before* we see the numbers?
- Is our question still the right question?

## Anchor 4 — What don't we know?

- What is missing? The pad lag per swimmer; the camera's frame rate in 2008; how precisely a judge reads first contact. None is in any source we found.
- Appendix F calls the lag range "plausible range, not measured." Do you accept it? **Have them actually try a smaller and a larger lag and see how much the comparison moves.**
- What are we assuming about the next race? That the true gap is equally likely anywhere in ±0.05 s. Is that a fact or a definition?

---

## Data Deep Dive

Now the numbers. Work these on the board with them.

**Step 1 — speed and distance per hundredth (D1).** Speed = 100 ÷ 50.58 = **1.977 m/s**. In 0.01 s a hand travels 1.977 × 0.01 = 0.01977 m = **1.977 cm**, about 2.0 cm. It is an average: a stroking hand moves faster and a gliding hand slower near the wall.

**Step 2 — frame-rate bands (D2).**

| Frames per second | Time between frames | Hand travel per frame |
|---|---|---|
| 30 | 0.0333 s | 6.59 cm |
| 60 | 0.0167 s | 3.30 cm |
| 240 | 0.0042 s | 0.82 cm |
| 1000 | 0.0010 s | 0.20 cm |

Only 240 and 1000 fps have a frame period shorter than 0.01 s, so only those can separate a one-hundredth difference; 30 and 60 fps cannot.

**Step 3 — the range hiding inside 0.01 s (D3).** Reported 50.58 and 50.59. If the third digit is dropped: the true times are 50.580-50.589 and 50.590-50.599, so the pad gap is anywhere from **0.001 s to 0.019 s** (0.20 cm to 3.76 cm). If the time is rounded to the nearest hundredth, the gap can be anywhere from just above 0 s to just below **0.02 s** (about 0 to 3.95 cm). Either way the "0.01 s" is a middle of a range, not a point. The rule text says the third digit is "not recorded or used" and never says "round", so the case computes both and does not claim the 2008 implementation.

**Step 4 — differential-lag table (D4).** With d = 0.01 s, c = Δ − 0.01:

| Δ (s) | c (s) | First to touch |
|---|---|---|
| −0.010 | −0.020 | Phelps (about 3.95 cm ahead) |
| 0.000 | −0.010 | Phelps |
| 0.005 | −0.005 | Phelps |
| 0.010 | 0.000 | simultaneous |
| 0.015 | +0.005 | Čavić |
| 0.020 | +0.010 | Čavić |
| 0.030 | +0.020 | Čavić |

Threshold: the pad and first contact disagree only when Δ **exceeds d = 0.01 s**. Under D3's range of d, that threshold itself moves between 0.001 s and 0.019 s. Students should state their own range for Δ and defend it using the named claims (Ekumbo on stroking vs gliding; Bertaud and Serbia's protest on force on the pad) **as claims**.

**Step 5 — reliability with the scenario values (D5).** P = 1 − b ÷ (2W), W = 0.05 s. Percent difference is defined in the case as (larger − smaller) ÷ smaller × 100; accept a percentage-points answer if labelled.

- Option A: b = |Δ| = 0.010 s, so P_A = 1 − 0.010 ÷ 0.10 = **0.900 (90.0%)**.
- Option B: b = 1/240 + 0.005 = 0.00417 + 0.005 = 0.00917 s, so P_B = 1 − 0.00917 ÷ 0.10 = **0.9083 (90.8%)**.
- **Contact Ranks wins by 0.93%** (relative to P_A), about 0.8 percentage points. The break-even is Δ = 0.00917 s: above it Contact Ranks is better, below it Pad Ranks is. Note the scenario Δ of 0.010 s equals the reported gap, so first contact is exactly simultaneous there (c = 0); the model still scores the pad at 0.900 because it treats any finish inside the band as a coin flip. Say this if asked.

---

## Twist — drop this at ~15 minutes into the discussion

Deliver it slowly. Let each piece land.

> *"A technician has just walked in."*
>
> (pause)
>
> *"The fast camera's view of the wall was blocked by spray in this lane. The only angle that clearly shows both hands at the wall is the ordinary slow-motion feed."*
>
> (pause)
>
> *"Sixty frames per second."*
>
> (pause)
>
> *"The judge's reading band J is unchanged. Nobody can read between two frames — no interpolating."*

Say the last two lines explicitly, or a room will "interpolate" and reach different numbers. **This is a constructed what-if for discussion. It is not a record of what footage existed in 2008; no source found gives that frame rate.**

**Facilitator only — do not read aloud.** (Percent difference uses the same base as the baseline: the smaller probability.) The frame period becomes 1/60 = 0.01667 s, so b_B = 0.01667 + 0.005 = 0.02167 s and P_B = 1 − 0.02167 ÷ 0.10 = **0.7833**. P_A is unchanged at 0.900. **The winner flips to Pad Ranks, by 14.9%.** Confirm a room that gets there against these numbers.

Now: **"Sixty seconds. Recompute with your own Δ from D4. Are you changing your ruling — or not?"** (A room whose Δ is above about 0.022 s keeps Contact Ranks; accept about 15% if a student rounds P_B early.)

## Immediate recommit

- Who is **not** changing? Why?
- Who is reconsidering?
- **What just broke in your original model?**
- **Were you wrong — or were you just missing information?** (Sit on this.)
- Who chose Contact Ranks because "video resolves two centimetres" without ever checking which frame rates actually do?

---

## Deep conflict — threads (20–30 min)

**Thread 1 — Who decides what "first contact" is?** Pad Ranks is a rule applied identically to every race; Contact Ranks measures what the sport means to reward but needs a human to call the frame. *"If two judges would pick frames 2 ms apart, whose number is the rule?"*

**Thread 2 — Fragility to one unmeasured number.** Flex Δ, J or the frame rate by 50% in the direction that hurts and the winner flips (see `case.json` `sensitivity_disclosure`). Do not read that aloud; use it to steer. *"Which ruling would you put your name on if someone measured the pad lag next year and it was twice what you assumed?"*

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch. *"Thirty seconds — pad, or eye?"* Two or three learners, fast. Stand/sit vote, no explanation yet. |
| **3:00–10:00** | Position defense (pre-twist). *"Convince us it's better, not just more modern-sounding."* · *"What is your probability number, not a guess?"* |
| **10:00–15:00** | Pressure-test the models. *"Which ruling is more fragile to one wrong estimate?"* · *"Which single number does your ruling depend on most?"* |
| **15:00** | **DROP THE TWIST.** Slowly, with pauses. Finish with: *"Sixty seconds. Are you changing your ruling — or not?"* |
| **15:00–20:00** | Immediate recommit. Who reverses? *"What just broke?"* |
| **20:00–30:00** | The two threads: who decides first contact · fragility to one unmeasured number. |
| **30:00–45:00** | Close, re-vote, reflection, lessons learned. |

---

## Close

- **Vote again.** Compare to the Anchor 1 board. Who moved?
- We asked ______ as our key question. Was it the right one?
- What math was new to you here, and how did you attack it?
- If you got a case like this again, what would you check first?

## Lessons Learned

The arithmetic has a clean structure: a delay common to both lanes cancels, so only a **differential** lag larger than the reported gap can make the pad and first contact disagree; the video has its own band set by the frame period and the judge's reading. Contact Ranks edges Pad Ranks (0.93%) on the scenario values, and the margin is fragile by design: the break-even is a differential lag of about 0.009 s, and nobody has measured the real one. Naming both facts together is stronger than picking one. A facilitator should also say plainly that the model compares **instruments**, not the athletes, and that the real FINA ruling stands.

## Standards Touched On

**Unit · Ratio · Decimal · Percent · Rounding · Estimating · Range · Probability · Absolute Value · How to convert an amount with compound units · How to divide decimal numbers · How to multiply decimal numbers · How to subtract decimal numbers · How to round a number to a specified place value · How to evaluate a variable expression (Substitution Property) · How to evaluate an absolute value expression · How to determine the probability of a single event · How to convert numbers to percents · How to compare two or more values.**

See `LEARNING_GOALS.md` for the forces-test and `case.json.reinforcement_note` for why `new_coverage[]` is empty.

---

## Facilitator note — sensitivity

**Teacher-facing sensitivity note.** (1) This case concerns real, named people and a real protest. Keep the register neutral: describe each person by their race and protest only, never by motive; the FINA ruling stands and the case never implies it was wrong. Do not let the room drift into "who really deserved the medal" — redirect to the instrument question. (2) The three dials that decide the answer — the differential pad lag, the judge's reading band J and the footage frame rate — are **assumptions** ("plausible range, not measured"), not data. The 0.93% margin exists only for the scenario values; a ±50% change in any one of them flips the winner. Say this to the room: the point is not which option wins but which assumption you would have to measure to be sure. (3) Two contested claims (Ekumbo vs Bertaud) are presented as attributed claims. Do not resolve them.
