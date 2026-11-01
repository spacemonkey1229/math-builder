# Guide Notes: Wind Call

MS | Guide Notes | Launchpad | 2026-27
**Tier:** T4 (HS) · **Primary metric:** gallons of Jet-A burned per nautical mile of net progress · **Margin:** thin — see `case.json.balance` for the exact figure

---

## Argument for A (Niner-Thousand)

No supplemental oxygen required at all — the operationally simpler release. In a four-minute
window before the dispatch lock, skipping the oxygen-bottle pull, weigh, log, and crew briefing is
a real, defensible operational argument on its own, even before any fuel arithmetic is done. A
guide should let a Hero who picks A entirely on this ground defend it — it does not require the
wind-triangle math to be a legitimate position, and a room that only argues fuel numbers has
missed half the case.

## Argument for B (One-Eight-Thousand)

Wins on the case's own primary metric. Solving each altitude's wind triangle (real winds-aloft
data as a vector, added to the Caravan's true-airspeed vector) gives a slightly higher resultant
groundspeed at the higher altitude, because more of that altitude's wind lies along the true
course — not because the wind there is faster in raw terms; it is actually the slower of the two
winds by raw speed. At the case's fixed fuel-flow assumption, the higher groundspeed burns
marginally fewer total gallons over the fixed route distance.

## Margin

**Computed: margin_pct = 0.6%, One-Eight-Thousand wins.** Using each altitude's resultant
groundspeed (from the dot-product wind decomposition in the case's own Appendix C data), the fixed
route distance (Appendix A), and the fixed fuel-flow rate (Appendix B, MA1):
`gal_per_nm = (distance / groundspeed) × fuel_flow / distance`, compared across the two altitudes.
See `case.json.balance.margin_pct` and `RESEARCH_LOG.md` for the full derivation. **This case's
margin is deliberately razor-thin** — in the tradition of SPEC's own gold-standard precedent case,
where a route won by a fraction of a percent and the class still had to defend it with real
numbers.

---

## Five Socratic questions

1. Your two wind-component tables (D2) show different headwind/tailwind components even though the
   9,000 ft wind is the *faster* of the two raw wind speeds. How is that possible — and what does
   it tell you about which number actually matters for this decision?
2. If you only had wind *speed* (no direction) for each altitude, could you have solved this case
   at all? What does that tell you about why this is a vector problem and not just an arithmetic
   one?
3. Your two gallons-per-nautical-mile answers land extremely close together. Does a margin that
   thin mean the decision doesn't matter — or does it mean something else is actually deciding it?
   What is that something else?
4. Appendix D's oxygen requirement never appears in your D5 ratio at all. Should it? Argue both
   ways.
5. If Renata's captain radios that the portable oxygen bottle just failed its pre-flight check,
   what does that do to your recommendation — and does it change your *math*, or only your
   *decision*?

## The trap

**A student compares raw wind *speeds* between the two altitudes and assumes the faster raw wind
must produce the faster groundspeed and therefore the lower fuel burn — without ever decomposing
either wind vector against the actual true course.** This is wrong: what matters is not wind speed
alone, but how much of that wind's speed lies *along the course* (the dot-product component from
D2). The higher-altitude wind is more closely aligned with the course direction than the
lower-altitude wind is, even though it is the slower wind by raw speed — and that alignment, not
raw speed, is what actually decides the case. A Hero who skips D2's dot-product work and reasons
from wind speed alone will reach a confident, wrong conclusion.

## Twist

**N/A.** This case's tension is genuinely mathematical and operational rather than
information-withheld — there is no piece of hidden data that, revealed mid-discussion, would
invalidate a popular position without simply making one side obviously correct. Socratic Question 5
(the oxygen bottle failing its pre-flight check) can serve as an informal late-discussion prompt if
a guide wants one, but it is not authored as a formal twist per SPEC's own Twist guidance: it would end the
discussion by removing Option B outright (an aircraft with failed oxygen equipment cannot legally
fly that option at all) rather than invalidating an argument while leaving both sides live. Authors
considered a twist and found none that met the bar; N/A is the honest call here, same as
`the-turbine-channel`'s own N/A call for a structurally similar reason (real technical tension, no
personal-stakes information to withhold).

---

## 45-minute Socratic plan

| Time | Move |
|---|---|
| **0:00–3:00** | Cold-call launch, 30-second commitments, stand/sit vote at Anchor 1 — no explanation yet. |
| **3:00–10:00** | Position defense. *"Convince us why your altitude is better, not just simpler."* Press anyone arguing from raw wind speed alone: *"Which direction is that wind blowing, relative to where the airplane is actually going?"* |
| **10:00–15:00** | Pressure-test the models. *"Whose plan is most fragile if the next wind forecast cycle changes these numbers?"* |
| **15:00–20:00** | Walk the room through D1–D3 together. **No twist drops here** — see Twist: N/A above; this slot is used instead to surface the trap (raw wind speed vs. course-aligned component) if no one in the room has caught it yet. |
| **20:00–30:00** | Two named threads: **(1)** does a margin this thin justify an operational trade-off (the oxygen logistics) at all?; **(2)** is holding fuel flow constant across altitudes (MA1) a reasonable simplification, or a hidden thumb on the scale? |
| **30:00–45:00** | Close, re-vote against the Anchor 1 board, reflection, lessons learned. |

---

## Guide Notes — the anchor ladder

### Intro
Heroes, today's case is a dispatcher's real four-minute decision: which altitude to lock on the
release, when the wind data says one thing and the operations paperwork says another.

### Launch
Read the Overview aloud, or show it on screen. Stop at "She pulls both printouts toward her."
*"She has both numbers already. What she doesn't have is time."*

### Anchor 1 — Take a stand and vote
Niner-Thousand or One-Eight-Thousand. No reasoning yet. Hands up, write the split on the board.
*"Is anyone courageous enough to stand with the altitude that means pulling the oxygen bottle out
of the locker?"*

### Anchor 2 — What is the problem we're solving?
Do not let them calculate yet.
- Is this actually a fuel question, or is it an operations/logistics question wearing a fuel
  question's clothes?
- Someone will say "obviously the smoother wind wins." What do they mean by *smoother* — faster,
  or better-aligned?
- Let the confusion grow. *"We don't even agree yet on what we're optimizing."*

### Anchor 3 — What is the process?
- If we just compare the two wind speeds, are we done? (No — the faster raw wind does not belong
  to the altitude that wins.)
- If we get the wind data and the aircraft's numbers, how do we actually turn that into one
  comparable number?
- Is our question still the right question?

### Anchor 4 — What don't we know?
- Do we need to assume anything? Which assumption is load-bearing? (Steer toward MA1 — holding
  fuel flow constant across altitudes — without naming it outright.)
- What would Renata still not know, even with both wind-triangle answers in hand?

## Data Deep Dive
Walk the room through decomposing each altitude's wind vector with the dot product (D2), finding
the resultant groundspeed and required heading (D3), and converting that into flight time and fuel
burned (D4–D5). Ground truth for cross-checking a Hero's own work is in `case.json.balance` — do
not read the exact figures aloud before the room has attempted D1–D5 themselves.

## Close
- Vote again. Who moved, and why?
- Was "which wind is faster" the right question, or was it really "which wind is better aligned"?
- What math was new to you here — the vector diagram, the dot product, or the unit conversions at
  the end?

## Lessons Learned
The case's real lesson sits in the gap between wind *speed* and wind *usefulness*. A learner who
only compares the two raw speeds has answered a question the case never actually asked. Solving a
wind triangle with the dot product is not a manufactured classroom exercise — it is the literal
daily task of the job this case is modeled on.

## Standards Touched On

**New coverage:** none — see `case.json.reinforcement_note`. This case reinforces all seven
Pre-Calculus/Vectors skills, plus Geometry/Triangles' Pythagorean Theorem and Hypotenuse, plus two
Measurement/Time and Measurement/Units how-tos.

**Claimed:** Vector · Magnitude (Of A Vector) · Unit Vector · Dot Product · Pythagorean Theorem ·
Hypotenuse · How to find the magnitude and direction of a vector · How to add and subtract vectors
· How to find the dot product of two vectors · How to find elapsed time · How to convert an amount
with compound units

## Facilitator note — sensitivity

None required. This is an operational dispatch decision with no death, illness, or family-hardship
stakes — SPEC §6 does not apply. The one thing worth flagging to a guide is not a sensitivity topic
but a math-fragility one: the case's own margin is unusually thin, and a strong Hero challenging
the constant-fuel-flow assumption (MA1) is engaging with the case exactly as intended, not
finding a flaw in it.

## What a strong defense sounds like

Not "the higher altitude is better because the wind is more favorable" — that's the conclusion,
not the defense. A strong defense shows the wind-component work (D2), names why raw wind speed is
a misleading proxy, states the fuel-flow assumption (MA1) out loud and says whether it changes
their confidence, and is honest that the margin is thin enough that the oxygen-logistics argument
for Niner-Thousand is not unreasonable even if the numbers favor the alternative.
