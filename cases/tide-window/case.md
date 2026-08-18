Case Study: Tide Window
MS | Math | Case Study | 2026-27 | Launchpad

## Overview

The radio in Amara Osei's hand goes quiet the second the tug captain stops talking, and for a
moment all she can hear is water sliding along the hull below her boots. She is standing on the
bridge wing of the *Solveig Trader*, loaded and waiting in the dark, and the call in front of her
is hers alone to make. Six months a licensed harbor pilot, and this is the first time no one
senior is standing beside her.

Behind her, on the chart table, two tide curves are pinned side by side, and neither one is
comfortable. The rain that soaked her jacket on the walk down to the pilot boat has stopped, but
the barometer in the wheelhouse hasn't moved the way she'd like. Somewhere below the waterline,
the *Solveig Trader*'s keel is closer to the harbor bottom than either of the ship's own officers
seem to appreciate.

The tug captain wants an answer before the current turns. The shipping line wants the berth kept
on schedule. And Amara — whose name goes on the pilotage log either way — wants the arithmetic to
be right before she says a word into the radio.

She looks at the chart, then at the clock, then at the chart again.

"Two options," the tug captain says. "Tell me which one."

## Background

Amara Osei is a harbor pilot for the Port of Kesterhaven Pilots' Association, licensed six months
ago after a multi-year apprenticeship. Once she boards a vessel and takes the conn for a transit,
she is legally responsible for its safe passage through the harbor channel — the ship's own
captain retains command, but the pilotage log carries her name and her judgment.

The *Solveig Trader* is a loaded cargo vessel under charter to a shipping line with a fixed
delivery window at the container berth (SEE APPENDIX C). Two transit options are on the table
tonight.

**The Dawn Transit** would move the ship out through the channel during the marginal low tide
before sunrise, keeping the delivery on its contracted schedule. The tide prediction for the
station (SEE APPENDIX A) shows the water level at that hour is low enough that the under-keel
clearance — the gap between the ship's loaded draft and the charted channel depth (SEE APPENDIX
B) — is real but thin.

**The Slack Tide** would hold the ship at berth until the next high tide, several hours later,
when the clearance is comfortable under any reasonable reading of the data. It guarantees a safe
transit but breaks the shipping line's contracted delivery window, triggering a penalty (SEE
APPENDIX C).

Two complicating conditions apply to either choice. First, the harbor's tide station reports
water level as a predicted curve, not a fixed number — the actual level at any given moment can
run higher or lower than predicted under real barometric and wind conditions (SEE APPENDIX D).
Second, the Pilots' Association's own safety manual sets a minimum acceptable under-keel
clearance below which a pilot may not authorize a transit, regardless of schedule pressure (SEE
APPENDIX B).

Amara has the tide predictions, the ship's draft, and the contract terms in front of her. She does
not have another pilot to check her arithmetic against. Where a figure below is not a matter of
public record, it is stated as an explicit modeling assumption (SEE APPENDIX E) rather than
guessed.

The vocabulary and the "how to…" skills this case will ask of you are listed in **Appendix G** —
that is where Challenge 1 sends you. (SEE APPENDIX F for further reading on harbor pilotage and
tide prediction.)

## Dilemma

You are Amara Osei.
Do you:
A.) Authorize the Dawn Transit — move the *Solveig Trader* out through the channel on the marginal
low tide, keeping the delivery on schedule OR
B.) Hold for the Slack Tide — wait for the next high tide, missing the contracted delivery window

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A worked angle table for each key clock time across the transit window: the time
    converted to the tide model's angle in degrees and in radians, the reference angle, and the
    sine, cosine, and tangent of that reference angle, found using the unit circle.
    D2. A stated sine or cosine function modeling the tide station's predicted water level over
    the transit window, naming its amplitude and period, fitted to the real harmonic data in
    Appendix A.
    D3. An under-keel clearance table comparing the Dawn Transit and the Slack Tide, in feet,
    built by evaluating your D2 model at the times from D1.
    D4. A written sensitivity check: using the barometric/storm-surge range in Appendix D, show
    whether the Dawn Transit's clearance margin survives the worst case in that range, and state
    the assumption you used to model it.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A: Tide Station Predictions

| | Value |
|---|---|
| Station name and NOAA station id | Charleston, SC — NOAA station 8665530 [S1] |
| Mean sea level datum (ft, station datum) | 5.69 ft (epoch 1983-2001) [S2] |
| Dominant tidal constituent (M2) amplitude (ft) | 2.52 ft [S3] |
| Dominant tidal constituent (M2) period (h) | 12.42 h (derived from the constituent's published speed, 28.984104°/hour) [S3] |
| Predicted water level, key times across the transit window (ft, MLLW) | Low 04:33 (−0.176 ft) · High 10:51 (5.831 ft) · Low 16:52 (0.016 ft) · High 23:01 (5.865 ft) — 2026-08-15/16 [S4] |

## Appendix B: Vessel Draft & Channel Clearance

| | Value |
|---|---|
| *Solveig Trader* loaded draft (ft) | 49 ft (modeled on the Maersk A-class, 8,272 TEU, 15 m draft) [S5] |
| Charted channel depth at the pilot station (ft) | 54 ft (entrance channel); 52 ft (inner harbor) [S6]. **This case's clearance figures use the 54 ft entrance-channel depth as the governing depth for the Dawn Transit — see Modeling Assumptions, MA4.** |
| Pilots' Association minimum under-keel clearance policy | 1 meter (≈3.28 ft) during channel/basin transit [S7] |

## Appendix C: Charter & Delivery Terms

| | Value |
|---|---|
| Contracted delivery window | See Modeling Assumptions, MA1 — no public figure exists for this fictional charter's own terms |
| Late-delivery penalty | See Modeling Assumptions, MA2 — no public figure exists for this fictional charter's own terms |

## Appendix D: Barometric & Storm-Surge Variability

A nearby storm can move the water level away from its predicted tide curve in **two different,
opposite-signed ways**, and getting the Dawn Transit's clearance right depends on telling them apart:

| | Value |
|---|---|
| Inverse-barometer water-level effect | Low air pressure lets the sea surface **rise** — roughly 1 cm of rise per 1 hPa (millibar) of pressure drop, ≈0.39 in per mb [S8]. This is the mechanism behind ordinary storm surge. |
| Wind-driven setdown | A **separate, opposite-signed** effect: when a storm's wind blows *away* from the coast, it physically pushes water offshore, **lowering** the local water level below the predicted curve — "reverse storm surge." Real, documented, and not small: Tampa Bay's water level dropped roughly 4 ft below prediction from wind-driven setdown during Hurricane Ian (2022) [S10]. |
| Local water-level effect modeled for a nearby-but-offshore system | See Modeling Assumptions, MA3. Kesterhaven's exposure on this specific night is modeled as a **net setdown** (water-level reduction), consistent with an offshore, non-landfalling system whose wind pushes water away from the harbor rather than piling it in — the specific magnitude is not knowable in advance. |

## Appendix E: Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author, each with a real basis named below. A Hero may challenge them in discussion — that is a
> legitimate move, and Appendix G names the skill a Hero would need to test one.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Contracted delivery window | The Dawn Transit meets it; the Slack Tide misses it by enough to trigger MA2 | No public source states a specific fictional charter's delivery window; the case needs only that the Slack Tide option misses it, not a specific hour count | Does not flip the dilemma on its own — the case's tension is clearance vs. penalty, not the exact window width |
| MA2 | Late-delivery penalty | **$18,000 flat penalty** — roughly one day of a real worked charter-party demurrage example ($20,000/day; real range for container demurrage generally runs $75–$300 per container per day) | This fictional charter's exact penalty clause cannot exist publicly; $18,000 is grounded in real industry figures, not invented from nothing | Directly load-bearing on Argument A — if set materially lower, Option B dominates outright; if materially higher, Option A does. `case-qa` Tier 2 should flex this ±50% once a `sensitivity_model.py` exists for this case. |
| MA3 | Local water-level reduction modeled for the nearby storm | **0.91 ft wind-driven setdown** — a genuine but non-extreme fraction of the real, documented magnitude such setdowns reach (Tampa Bay measured ~4 ft during Hurricane Ian [S10]), modeled for an offshore, non-landfalling system with pressure at or just above the real Category-1-hurricane threshold (>980 mb, vs. a ~1013 mb fair-weather baseline [S9]) whose wind pushes water away from Kesterhaven rather than piling it in — **CORRECTED 2026-08-12**: earlier drafts of this case misattributed this reduction to the inverse-barometer rate in Appendix D (S8), which is a real relationship but produces a **rise**, not a reduction, and cannot honestly justify this row's sign. The mechanism is wind-driven setdown (S10), a separate, real, opposite-signed effect — see RESEARCH_LOG.md. | Chosen well within the real documented range for this phenomenon, not picked to force an outcome — see RESEARCH_LOG.md for the correction and the full arithmetic | This reduction directly narrows the Dawn Transit's clearance margin over the Pilots' Association's policy floor — work out D3/D4's own comparison to see by how much, and whether it changes the recommendation. |
| MA4 | Governing depth for the Dawn Transit's clearance calculation | **54 ft (the entrance-channel depth)** | Appendix B cites two real, both-sourced, dated depths for this harbor — 54 ft (entrance channel) and 52 ft (inner harbor) [S6] — without which one applies to this fictional vessel's specific route, which is not a matter of public record for a fictional charter. This case models the Dawn Transit's controlling clearance moment as occurring at the harbor entrance itself (the transit's final and most exposed segment on the way to open water), which is where the real NOAA tide station this case's Appendix A predictions are drawn from is sited. **CORRECTED 2026-08-12**: earlier drafts used 54 ft without stating this as a choice — a Hero reading Appendix B literally could equally defensibly apply the shallower 52 ft figure instead. | This is the single largest lever in the whole case. A Hero who challenges this convention and argues for the shallower 52 ft reading has a legitimate, defensible point worth exploring in discussion. |

## Appendix F: Learn More

Optional further reading for the curious — not required to complete the Challenges or resolve the
Dilemma.

- [The American Pilots' Association](https://www.americanpilots.org) — the real national association representing U.S. marine/harbor pilots, with background on what pilotage is and why ports require it.
- [NOAA: Tides and Water Levels tutorial](https://oceanservice.noaa.gov/education/tutorial_tides/welcome.html) — NOAA's own educational tutorial on what causes tides and how they are monitored and predicted.
- [NOAA: What is storm surge?](https://oceanservice.noaa.gov/facts/stormsurge-stormtide.html) — NOAA's explainer distinguishing storm surge from storm tide, the real phenomenon behind Appendix D.
- [Math Is Fun: The Unit Circle](https://www.mathsisfun.com/geometry/unit-circle.html) — a clear walkthrough of the unit circle and how it defines sine, cosine, and tangent, useful background for Challenge 3's D1.

*Links verified live 2026-08-18.*

## Appendix G: "How To…" Math Questions To Research

**Vocabulary terms**

- Radian
- Unit Circle
- Sine Function
- Cosine Function
- Tangent Function
- Amplitude
- Period (Of A Function)
- Reference Angle

**"How to…" questions**

- How to convert between degrees and radians
- How to find the sine, cosine, and tangent of an angle using the unit circle
- How to find the amplitude and period of a sine or cosine function

<!-- FACILITATOR ONLY -->

## Balance draft (facilitator only — never shipped to students)

**Argument for A (Dawn Transit).** The tide model predicts a real, positive under-keel clearance
at the marginal low, and the Pilots' Association's own minimum-clearance policy is met under the
predicted (non-adjusted) water level. Holding for the Slack Tide is certain to trigger the
contracted late-delivery penalty, a real and immediate cost with no offsetting benefit if the
predicted clearance holds.

**Argument for B (Slack Tide).** The predicted clearance at the marginal low is thin enough that a
plausible, real wind-driven setdown (Appendix D) could erase it, and the Pilots'
Association's policy exists precisely to bar a pilot from authorizing a transit on a margin that
thin. The penalty for missing the window is a known, bounded cost; a grounding is not.

**Margin basis (resolved 2026-08-05, mechanism corrected 2026-08-12).** Comparing Option A's clearance margin directly against
Option B's is not the right shape for this case — the Slack Tide is a high-tide transit and will
always clear by several times more than the Dawn Transit's marginal-low transit; that gap is a
structural fact of the two options, not a close call, and Appendix A/B's real sourced NOAA/vessel
figures cannot honestly be adjusted to force one. Instead, `margin_pct` measures how close the
Dawn Transit's real safety margin comes to the Pilots' Association's policy floor under MA3's
storm twist — the only genuinely adjustable, disclosed-as-uncertain quantity in this case. Under
the predicted (non-adjusted) water level and MA4's governing-depth convention, Option A clears the floor by 1.544 ft (47% of the 3.28
ft floor) — a real, comfortable margin, not artificially forced close. Under MA3's storm twist
(a 0.91 ft wind-driven setdown, well inside the real documented range for the phenomenon — see
Appendix D and RESEARCH_LOG.md), that margin erodes to 0.634
ft — **19.33% of the policy floor**, inside SPEC's ~20% cap. `margin_pct` = 19.33.

**Five Socratic questions (draft — refine once numbers land).**

1. Your model says the Dawn Transit clears the harbor floor by a real margin. What would the
   wind-driven setdown have to be for that margin to reach zero?
2. The Pilots' Association's minimum-clearance policy exists for a reason. Whose job is it to
   decide when a "thin but positive" margin is not thin enough — the model, or the pilot?
3. If you were the shipping line's dispatcher instead of the pilot, would you weigh the penalty
   differently? Why is that not actually Amara's problem to solve?
4. Your D1 table required sine, cosine, *and* tangent of the reference angle. Which of the three
   did you actually use in your final clearance number — and why did the case ask for all three
   anyway?
5. Suppose the real data shows the wind-driven setdown on the actual night was smaller than the
   worst case you modeled in D4. Was Amara wrong to be cautious, or just unlucky in a good way?
6. Appendix B gives two different charted depths for this harbor. This case uses the deeper one
   (54 ft) as the governing depth (see MA4) — what happens to your answer if you use the
   shallower one (52 ft) instead, and is that a legitimate challenge to raise?

**The trap (two — see FACILITATOR.md for the full breakdown).** (1) Most Heroes will compute the
*predicted* clearance, find it positive, and stop there, never touching D4's sensitivity check. (2)
**Added 2026-08-12, the more dangerous one:** a Hero applies the familiar inverse-barometer rule
(pressure drop -> water rises) to this storm instead of the wind-driven setdown Appendix D actually
models, and produces a complete, confident-looking D4 that gets the twist's direction backwards.

**Sensitivity note (SPEC §6).** None required — the stakes here are commercial and professional
(schedule penalty, a pilot's license), not personal loss or hardship.
