Case Study: Feedback
MS | Math | Case Study | 2026 | Launchpad

*(Band: HS. This case uses precalculus vocabulary — polar coordinates and parametric equations —
and is written for a Hero who has finished trigonometry basics and is ready to apply them to a
real, professional decision.)*

## Overview

Forty minutes to doors, and Priya Nakamura is on her knees behind the House-Right speaker stack
with a multimeter, watching a fault light blink where a fault light has no business blinking. The
second monitor amp channel is dead. Not dim, not crackling — dead, confirmed twice, and the
rental company's after-hours line rings through to a voicemail box that hasn't been checked
tonight.

That leaves one working monitor circuit for the whole show, and one decision that has to be made
before the house manager starts seating people: which floor wedge gets the lead vocal.

She already knows both candidate spots. The venue's crew has used the House-Left position for
years out of habit. Nobody has ever measured whether it's actually the better one — they've just
never had a reason to ask, because there used to be two wedges and it never mattered which was
which. Tonight it matters.

Priya pulls up the stage plot on her laptop, the mic's spec sheet in a browser tab beside it, and
the blocking notes from Tuesday's run-through. Somewhere upstairs, the house manager is telling
early arrivals that doors are running a few minutes behind schedule. Priya doesn't look up.

She opens a blank sheet of graph paper and starts plotting.

## Background

Priya Nakamura is the front-of-house sound engineer for tonight's performance at the Ridgeline
Playhouse, a mid-sized community theater. She owns the mix for the evening and is the person the
house manager will come find if the show gets stopped by a feedback squeal mid-song. With the
second monitor amp channel down (SEE APPENDIX A), she has to commit the lead vocal's floor wedge
to one of exactly two physical positions before the doors open:

**House-Left** — the wedge position the crew has used by default for years, roughly in front of
the mic and somewhat off to one side (SEE APPENDIX A).

**House-Right** — the position that opened up only because the failed amp channel used to feed a
second wedge there; it sits closer to the mic but almost directly off to the side of it (SEE
APPENDIX A).

The risk both positions share is the same one every live sound engineer manages: a floor monitor
is a loudspeaker sitting near an open, live microphone, and if too much of the monitor's own sound
finds its way back into that microphone, the system re-amplifies its own signal until it
squeals — audio feedback. How close a mix can be pushed before that happens is called the **gain
before feedback**, and it depends on exactly two things once the loudspeaker's own output is
fixed: how far the monitor sits from the mic, and how sensitive the mic actually is in the
*direction* the monitor sits in (SEE APPENDIX D). The lead vocal mic is a directional, cardioid
model — most sensitive straight ahead, and built to reject sound from other angles by different
amounts depending on how far off-axis that angle is (SEE APPENDIX B). A monitor that sits closer
but nearly out of the mic's pickup pattern can, in principle, be safer than one that sits farther
away but more in line with it — which is exactly why the two candidate positions are not an easy
call by eye.

The lead vocalist, Dana Voss, sings the opening verse standing at a fixed mic stand — but during
the bridge, she picks up the same mic handheld and crosses the stage to hit a new mark for the
final chorus, holding the mic's aim steady throughout (SEE APPENDIX C, MA2). Whichever position
Priya commits to has to stay safe not just for the static verse, but for every blocking mark Dana
actually holds during the number. Where a figure in this case is not a matter of public record, it
is stated as an explicit modeling assumption (SEE APPENDIX E) rather than guessed, and every
sourced figure is listed in **APPENDIX F**. The vocabulary and "how to…" skills this case will ask
of you are listed in **APPENDIX G** — that is where Challenge 1 sends you.

## Dilemma

You are Priya Nakamura.
Do you:
A.) Commit the lead vocal wedge to House-Left — the position closer to the mic's on-axis line, but
farther away OR
B.) Commit the lead vocal wedge to House-Right — the position much closer to the mic, but almost
directly off to its side

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A rectangular-to-polar conversion table (SEE APPENDIX A): for House-Left and House-Right,
    each wedge's position stated as a rectangular (x, y) pair in feet from the mic, converted to
    polar coordinates (r, θ) measured off the mic's on-axis heading, with the full conversion
    shown for both.
    D2. A graph of the microphone's cardioid polar equation (SEE APPENDIX B), drawn over a full
    revolution, with both wedges' θ from D1 marked on the curve and each wedge's pattern-rejection
    value (in decibels) labeled at its marked point.
    D3. The performer's cross written as a pair of parametric equations x(t) and y(t) (SEE
    APPENDIX C), with the parameter eliminated to state the single rectangular equation of the
    line Dana walks — and, using that equation, the exact stage position where her cross crosses
    the fixed follow-spot focus line y = 2 (needed for the light-board operator's iris cue).
    D4. A gain-before-feedback table (SEE APPENDICES A, B, C AND D) covering every blocking
    moment this case gives you for Dana's mic — the static verse position, and both ends of the
    bridge cross from D3 — for House-Left and for House-Right: distance term (dB), pattern-rejection
    term (dB), and the combined gain-before-feedback score, with the arithmetic shown for every
    cell.
    D5. A final decision table (SEE APPENDIX A) identifying, for each wedge, its single worst
    (lowest) gain-before-feedback moment from D4 and the overall margin between the two wedges at
    their respective worst moments — with your recommendation stated and defended using that
    margin.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Stage Plot and the Two Wedge Positions

All positions in this case are given in feet, in the mic's own reference frame: the origin is the
fixed mic-stand position Dana sings from during the opening verse; the **+x axis is the mic's
on-axis (front, most-sensitive) heading**, which stays fixed for the entire number (SEE APPENDIX
C, MA2); the **+y axis is 90° to the side**. This is a standard way audio crews overlay a
microphone's own polar pattern directly onto a stage plot, so every position in this case can be
read straight into APPENDIX B's polar equation without any extra rotation.

| | House-Left (Option A) | House-Right (Option B) |
|---|---|---|
| Position (x, y), feet from mic | **(6, 5)** [MA1] | **(0, 6)** [MA1] |
| Distance from mic, r (ft) | *(Challenge D1)* | *(Challenge D1)* |
| Angle off the mic's on-axis heading, θ | *(Challenge D1)* | *(Challenge D1)* |

Both positions are the venue's own fixed hardware locations for tonight (SEE APPENDIX E, MA1) —
neither wedge can be relocated before doors without re-running cable through a load-in door that
is now blocked by the seated orchestra pit crew.

## Appendix B — The Microphone's Polar Pattern

Dana's handheld vocal mic is a cardioid dynamic microphone. A cardioid microphone's directional
sensitivity, as a function of the angle θ off its on-axis heading, follows the cardioid polar
equation:

**g(θ) = 0.5 · (1 + cos θ)**, normalized so that g(0°) = 1 (full sensitivity, on-axis) [S1].

This is the real, published polar equation for a cardioid microphone pattern, and it is the
manufacturer's own equation for exactly the mechanism described in Background — a cardioid
pattern is built by combining, in equal parts, an omnidirectional pickup pattern (equally
sensitive from every direction) and a bidirectional "figure-8" pickup pattern (sensitive front and
back, rejecting the sides) [S1].

A microphone's sensitivity is converted to a decibel **pattern-rejection** value — how many
decibels *less* sensitive the mic is at angle θ than it is on-axis — using:

**Pattern rejection (dB) = −20 · log₁₀(g(θ))**

Three real, published reference points confirm this equation against an actual manufacturer's
measured cardioid pattern [S1]: at θ = 0° the pattern is at full sensitivity (0 dB of rejection);
at θ ≈ 65.5° the real, measured rejection is **3 dB**; at θ = 90° it is **6 dB**; and at θ = 180°
(directly behind the mic) real cardioid microphones measure "in practice greater than 20 dB" of
rejection, even though the idealized equation above predicts a mathematical null (g = 0,
infinite rejection) exactly at 180° [S1].

## Appendix C — The Bridge Cross

During the opening verse, Dana stands at the fixed mic stand — the origin of Appendix A's
coordinate system — and the mic's distance/angle to each wedge is exactly the (r, θ) pair from
Challenge D1.

During the bridge, Dana takes the mic handheld and crosses the stage to a new mark for the final
chorus, walking at a constant pace and holding the mic's aim on the same fixed heading the entire
time (SEE MA2 below). Her cross is defined by:

| | Value |
|---|---|
| Starting position (x₀, y₀), feet — where she picks up the handheld | **(2, 1)** [MA3] |
| Ending position (x₁, y₁), feet — her held mark for the final chorus | **(0, 3)** [MA3] |
| Duration of the cross, T (seconds) | **4** [MA3] |
| Motion | constant speed, straight line, start to end |

**MA2 — mic orientation held fixed.** The blocking note for this number directs Dana to keep the
mic capsule aimed on the same heading throughout the cross rather than turning to face the
audience or a scene partner. This is what makes Appendix A's fixed +x on-axis heading valid for
every position in this case, not only the static verse. (SEE APPENDIX E, MA2, for the basis and
the sensitivity of this choice.)

**Where Priya actually checks gain-before-feedback.** Priya does not compute a continuous curve
of gain-before-feedback over every instant of the cross — she checks it at the specific blocking
marks the director actually calls in rehearsal, because those are the only moments she can
practically prep a fader move for: the static verse position, the moment Dana picks up the
handheld (start of the cross), and the mark she holds through the final chorus (end of the cross)
(SEE APPENDIX E, MA4).

## Appendix D — How Gain-Before-Feedback Is Combined

Gain-before-feedback in a real system depends on several factors — the microphone's directivity,
the distance between microphone and loudspeaker, the acoustic environment, and how many
microphones are open at once, among others [S2]. Two of those factors are exactly the two things
that differ between House-Left and House-Right tonight: the mic-to-wedge distance and the angle of
the wedge off the mic's on-axis heading. (The other factors — the room, the loudspeaker itself,
the number of open mics — are identical for both options tonight, so they do not enter the
comparison; SEE APPENDIX E, MA4.)

**The distance effect** follows the inverse-square law: halving the distance from a sound source
to a microphone increases the potential gain before feedback by 6 dB, and doubling it decreases
gain before feedback by 6 dB [S2]. Expressed as a running decibel value relative to a 1-foot
reference distance, distance term (dB) = **20 · log₁₀(r)**, r in feet (the 1-foot reference is a
scaling convention only — it appears identically in both options' distance terms and cancels out
of every A-vs-B comparison in this case).

**The directivity effect** is Appendix B's pattern-rejection term: a monitor sitting where the mic
is *less* sensitive contributes fewer decibels of its own sound back into the mic, which is
exactly why sound engineers aim a directional mic's least-sensitive angle at the monitor whenever
they can [S2].

**This case's gain-before-feedback score** for a given wedge, at a given blocking moment, combines
both effects:

**GBF score (dB) = distance term (dB) + pattern-rejection term (dB)**

A **higher** score means more headroom before feedback — the safer reading at that moment. Because
the room, the loudspeaker, and the number of open mics are identical for both wedges tonight,
those factors would add the same constant to both options' scores and are not tracked separately
here (SEE APPENDIX E, MA4) — this case's score isolates exactly the two factors that make House-Left
and House-Right different.

## Appendix E — Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | House-Left and House-Right wedge positions (Appendix A) | (6, 5) ft and (0, 6) ft, in the mic's own reference frame | The Ridgeline Playhouse is a fictional venue; there is no real stage plot to source. The two positions are dimensioned to be realistic for a small community-theater stage — a handful of feet from a center-stage mic stand, one noticeably farther but more forward, one noticeably closer but nearly abeam — and were not chosen to make either option obviously better by eye. | The comparison between the two wedges depends directly on these four coordinates. A different real stage plot would give different exact numbers; that dependency is disclosed here, not hidden. |
| MA2 | The mic's on-axis heading is held fixed throughout the whole number, including while Dana is handheld and moving | applied to the static verse and the entire bridge cross | A real performer's handheld mic technique varies — some singers rotate the capsule as they turn to face different parts of the room. Holding the heading fixed is what makes a single, stated stage-plot reference frame valid for every position in this case, and matches a real director's blocking note asking a performer to "keep the mic up and aimed out" during a cross. | If a performer instead re-aimed the mic to face the audience at every instant, every angle in Appendices C and D would change with her heading, not just her position — a materially different and much harder case. This case's whole geometry depends on MA2 holding. |
| MA3 | Dana's bridge-cross start point, end point, and duration (Appendix C) | (2, 1) ft to (0, 3) ft, 4 seconds | Both the venue and the number are fictional, so there is no real blocking script to source. The values are dimensioned to be a realistic few-foot cross completed within one musical phrase of a mid-tempo number. | The specific worst-case gain-before-feedback moment for each wedge — and therefore which wedge wins — depends on these four numbers. The answer is sensitive to this value, which is exactly why D4 asks you to check every blocking mark rather than assume the static verse position is the whole story. |
| MA4 | Priya checks gain-before-feedback only at named blocking marks (the verse position, and both ends of the bridge cross), not continuously throughout the number; and treats the room, loudspeaker, and open-mic count as identical between the two wedges tonight | applied throughout | A live engineer preps fader moves for the marks a director actually calls, not for an unbounded number of in-between instants; and tonight's room, PA, and mic count genuinely do not change based on which wedge is chosen. | This narrows the case to a tractable, real engineering practice rather than a full continuous optimization, and does not by itself favor either wedge — both are checked at the same set of moments. |

## Appendix F — Sources

| id | Claim | Value | Source | Accessed | Confidence |
|---|---|---|---|---|---|
| S1 | The cardioid microphone polar pattern equation, and real measured reference points confirming it | Polar equation: 0.5(1 + cos θ); measured points: 0 dB at 0°, 3 dB rejection at ≈65.5°, 6 dB rejection at 90°, "in practice" greater than 20 dB at 180° (idealized equation predicts an exact null at 180°) | DPA Microphones, "Cardioid Microphone," DPA Microphones Mic University dictionary entry ([dpamicrophones.com/dict/cardioid-microphone/](https://www.dpamicrophones.com/dict/cardioid-microphone/)) | 2026-08-19 | HIGH — a working professional microphone manufacturer's own published technical dictionary entry, fetched directly, giving both the exact polar equation and independent measured reference points that reproduce it (65.5° at −3 dB checks exactly against the equation: 20·log₁₀(0.5(1+cos 65.5°)) ≈ 3.0 dB) |
| S2 | The mechanism of gain-before-feedback: its dependence on mic-to-loudspeaker distance via the inverse-square law (6 dB per doubling/halving of distance), and on aiming a directional mic's least-sensitive angle at the loudspeaker | "Greater GBF is obtained with the performer closer to the microphone; an instance of the inverse-square law … if the performer reduces the distance to the microphone by half, the PAG is increased by 6 dB." "Directional microphones … are aimed such that their pickup pattern is weakest in the direction of the loudspeakers." | Wikipedia, "Gain before feedback" ([en.wikipedia.org/wiki/Gain_before_feedback](https://en.wikipedia.org/wiki/Gain_before_feedback)) | 2026-08-19 | MEDIUM — a general encyclopedia entry, not a peer-reviewed or manufacturer source, but it states a standard, uncontested piece of acoustics (the inverse square law applied to gain-before-feedback) consistently with every other source found during this case's research (see RESEARCH_LOG.md); the quoted distance rule is used here for a mic-to-loudspeaker distance exactly as the source itself states it |
| S3 | The general structure of a real potential-acoustic-gain calculation: a 20·log₁₀ distance-ratio term, plus separate additive terms for microphone directivity pattern and for the number of open microphones | "Estimate uses a PAG-style distance relationship: 20 log10((D0 x Ds) / (D1 x D2)), then applies open-mic, pattern, room, and feedback-stability adjustments." Pattern bonus modeled as 0 to +8 dB depending on directivity; open-mic penalty modeled via a 10·log rule (≈−3 dB per doubling of open mics). | CMUSE, "Gain Before Feedback Calculator for Live Sound" ([cmuse.org/gain-before-feedback-calculator](https://www.cmuse.org/gain-before-feedback-calculator)), dated 2026-06-29 | 2026-08-19 | MEDIUM — a trade/hobbyist audio publication, not a peer-reviewed or manufacturer source, but it corroborates the same 20·log₁₀ distance-ratio and additive-directivity-term structure this case's own GBF score uses (Appendix D), independently of source S2; used here only to confirm the *shape* of a real PAG-style calculation, not for any specific numeric value used in this case |

## Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Polar Coordinate
- Parametric Equation
- Parameter

**"How to…" questions**

- How to convert a point between rectangular and polar coordinates
- How to graph a polar equation
- How to eliminate the parameter to find a rectangular equation

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
