# Facilitator Guide — The Late Run

**FACILITATOR ONLY. Do not distribute to Heroes.** This file, and `case.json`'s `balance` object,
are the only places the argument, the margin, and the pitfall notes may live — never in `case.md`.

**Case:** The Late Run · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Pre-Calculus — Pythagorean Identity, Inverse Trigonometric Function, How to verify a
trigonometric identity, How to solve a trigonometric equation over a given interval, How to
evaluate an inverse trigonometric function (see `case.json.standards[]` for exact ids, including
the round-out Angle / percent-of-a-number skills).

**Status:** Researched and independently re-verified 2026-08-31 (`RESEARCH_LOG.md`). Every
`{{NEEDS_SOURCE}}` placeholder is closed. The margin below is **confirmed, not preliminary** —
`case.json.balance.margin_pct` is `10.7`, not `null`.

## Context: why this case exists

This case replaces `cases/the-locks-window/` (same protagonist, same location, same skill group),
which failed `case-qa`'s balance test for a structural reason: it compared glare on GLASS vs. glare
on WATER, and glass reflects roughly twice the Brewster-angle glare water does, as a fixed
consequence of the two materials' refractive indices — no real shoot date, time, or camera
position could close that gap (`cases/the-locks-window/RESEARCH_LOG.md`, "RETUNE PASS" section).
This case fixes that by comparing the **same material** (the viewing-room glass) at **two
different real angles of incidence**, driven by real sun-position geometry on two real calendar
dates. See `cases/_concepts/CONCEPTS_precal-second-pass_2026-08-30.md`, concept C7, for the full
research trail, including the real NOAA Solar Calculator sessions this pass ran.

## Argument for A (The August Call)

The August 19 shoot sits almost exactly at the glass window's own Brewster angle — real NOAA
solar-position data, applied to the same south-facing window orientation this location's earlier
research pass already established (Modeling Assumption MA1, carried forward), puts the real
incidence angle within roughly a degree of Brewster's angle for glass. At an incidence that close
to Brewster, the reflected light is very nearly fully polarized, so a well-tuned filter removes
essentially all of the window's own glare — the ceiling on image quality is about as high as this
optical system ever gets. August 19 also isn't an arbitrary date: it is the real, government-data-
confirmed single best Chinook day of the season, so the crew isn't trading image quality for a
mediocre fish day — the fish activity is independently verified as the best available.

## Argument for B (The September Call)

The September shoot is real too, and it is not interchangeable with more Chinook footage: Coho are
a different species, running at a different, later, real, documented part of the season (the last
two weeks of September, per multiple converging Seattle-area sources), and it is the closing
salmon-viewing opportunity of the year for this production. The real sun-incidence angle on that
date sits noticeably farther from the glass's Brewster angle than August's does, so the polarizer's
ceiling is measurably lower — but "measurably lower" is not "bad": even the worse of the two real
options still lands in the high-80s-to-low-90s percent range for glare removed, a genuinely usable
professional shot, not a ruined one. A producer who values species completeness over the very last
few points of optical polish has real grounds to pick B.

## The margin — confirmed

Using n_glass = 1.52 (Brewster angle 56.66°), and NOAA-derived incidence angles of ≈55.9° for
August 19, 2026, 2:00 PM PDT and ≈44.4° for September 22, 2026, 2:00 PM PDT (both under the
south-facing MA1 orientation), the Fresnel-derived "percent of the window's own glare a
perfectly-tuned polarizer removes" comes out to **99.96%** for the August Call and **90.30%** for
the September Call — a relative margin of **10.70%** (`(99.96−90.30)/90.30`), **Option A winning**.
This is an independent re-derivation from freshly-fetched sources this pass (not a copy of the
design-phase estimate), and it lands within a rounding error of that earlier ~10.7% estimate — a
sign the underlying live sources (NOAA sun position, WDFW counts) are stable, not a coincidence.
Full arithmetic in `RESEARCH_LOG.md` and `case.json.balance.computation_note`.

**The one caveat that matters more than the headline number: this margin is NOT robust to MA1
(window orientation).** Re-checked, mechanically, against four other candidate window-normal
azimuths besides the due-south value the case uses:

| Normal azimuth | Relative margin | Winner |
|---|---|---|
| 90° (E) | +26.6% | A |
| 135° (SE) | −8.9% | **B** |
| **180° (S, used)** | **+10.70%** | **A** |
| 225° (SW) | +6.6% | A |
| 270° (W) | −7.3% | **B** |

Two of the four untested orientations (135° SE, 270° W) **flip the winner to Option B**. The
due-south value is the only one of the five with an actual documentary basis (two independently
fetched sources place the fish ladder/viewing room on the south side of the Locks complex; neither
gives the window's exact compass bearing) — but that means a Hero who challenges MA1 has real
grounds, not just a rhetorical move. **By contrast, MA2 (call time) and MA3 (September date) are
robust: the winner stays Option A across every tested value of both** (1:00/2:00/3:00 PM under
MA2; September 15/22/29 under MA3) — only the margin's size moves, never its sign. MA4 (glare
tolerance) changes the September Call's D2 worksheet answer substantially across its tested range
and barely moves August's, but does not touch the D4 margin or winner at all (MA4 only feeds D2,
not D4). This asymmetry — one assumption that flips the case, two that don't, one that doesn't even
touch the graded metric — is deliberately built as this case's real intellectual center, and is
this pass's own new finding (the design-phase concept sheet did not surface the MA1 orientation
table). See `case.json.modeling_assumptions[]` for the full numeric detail behind each row; none of
it appears in `case.md`, which discloses only the qualitative direction (SPEC §5/§6 discipline —
Appendix G may state what was assumed, why, and whether a flex flips the winner, but never the
actual base-case margin or worksheet answer).

**Margin basis for `case-research`:** compare `(R − R_p/2)/R × 100` (percent of a surface's own
Fresnel reflectance removable by a perfectly-tuned polarizer) between the August Call's and the
September Call's real sun-incidence angles, using the already-sourced refractive-index/Fresnel
formulas and freshly-sourced NOAA Solar Calculator readings for both dates.

## Intro

Frame the format before anything else: this is a real, one-shot production booking decision with a
hard deadline, not a worksheet. Name the opener — "You are Mara Ellison, director of photography,
cursor parked on a blank booking form, and a production coordinator down the hall who locks travel
and the viewing-room reservation the moment you say a date out loud." Let the stakes land — one
day, period, for the whole film — before moving to the Launch.

## Launch

Show Appendix A (the glass window's fixed Brewster angle, 56.66°) and Appendix C (the two real sun
positions) side by side, with no Fresnel percentages yet. Ask: "The glass doesn't change between
these two dates. The sun does. Just from the sun's elevation numbers in Appendix C — August 53.55°,
September 40.77° — which shoot do you think gets a cleaner shot, and why?" Do not confirm or
correct answers here. Most rooms will reason from elevation alone ("higher sun in August, so
better") — record that instinct out loud, because it is exactly the pitfall named below, and it
happens to reach the right conclusion for the wrong reason this time, which is worth surfacing
later.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the September Call — the option that gives up the
verified best Chinook day for a Coho window that isn't even single-day-confirmed?" Show of hands,
both options, no discussion. Record the count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'a cleaner shot'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which date has
better light," but push on what the polarizer actually does and doesn't remove: "The Background
says the polarizer's ceiling depends on how close the real sun-incidence angle sits to the glass's
one Brewster angle — not on 'better light' in general. So what, precisely, is the question Appendix
D is asking you to answer?" If the room lands on "what percent of the window's own glare can a
perfectly-tuned polarizer remove at each date's real incidence angle" on its own, the case is
working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room names the real question, ask them to name the actual steps before touching the
appendices: find the glass's one fixed Brewster angle from its refractive index (D1, Appendix A),
find each date's real incidence angle from the sun position and window orientation (Appendix C),
use the Fresnel reflectance formulas to find how much of each date's reflected glare is polarizable
versus permanently unremovable (Appendix D), solve for the rotation-offset angle that hits the
stated production tolerance on each date (D2), verify the Pythagorean identity and use it to
cross-check the transmitted-glare function (D3), then compute and compare the percent of each
date's own glare a perfectly-tuned filter removes, stating the margin (D4). Re-ask: "Is our question
still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: the window's exact compass orientation (MA1), the exact call time
on both dates (MA2), the exact date chosen within the documented Coho window (MA3), and the
production glare tolerance used in D2 (MA4) are all stated Modeling Assumptions, not sourced
figures. Ask which ones actually change the *graded* D4 result if they move. Let a sharp Hero find,
without being told outright, that MA2 and MA3 only ever change *how much* Option A wins by — never
*whether* it wins — while MA1 is the one that can actually flip the recommendation, and MA4 doesn't
touch D4 at all (it only changes D2's rotation-offset answer). This is the case's real intellectual
center: not every assumption carries equal weight, and only checking each one honestly (not
guessing) tells you which.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's Brewster angle, D2's rotation-offset solve, D3's identity
check, and D4's percent-removed comparison together as a room, cold-calling for D4 specifically —
this is where a Hero who reasoned from elevation alone in the Launch will visibly struggle to
explain why August's advantage is as large as it is, given September's sun is not *that* much lower.

**Facilitator-only arithmetic note.** D1: θ_p = arctan(1.52) = 56.66°. D2/D3/D4 inputs (both dates,
under MA1's due-south orientation, n₁=1.00 air / n₂=1.52 glass, Snell's Law + Fresnel equations, per
Appendix D): August incidence 55.9° → R_s 15.16%, R_p 0.006%, R 7.58%, residual R_p/2 0.003%,
percent removed 99.96%. September incidence 44.4° → R_s 9.45%, R_p 1.02%, R 5.23%, residual R_p/2
0.51%, percent removed 90.30%. D2 (tolerance = 2× each date's own residual): August's rotation-offset
answer ≈1.1°; September's ≈19.1° — the same Malus's-Law equation, `I(θ) = R_p/2 + (R − R_p/2)sin²θ`,
solved for θ at each date's own R and R_p. D3: `sin²θ = 1 − cos²θ` substituted into `I(θ)` gives the
alternate checkable form `I(θ) = R − (R − R_p/2)cos²θ`; both forms agree by construction once the
identity is verified algebraically, not just plugged in numerically. D4: `(99.96 − 90.30) /
90.30 × 100 = 10.70%` relative margin, August Call ahead. Full derivation in `RESEARCH_LOG.md`.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"The location scout who told you the viewing room sits on 'the south side of the canal' — go back
and check what she actually verified. She confirmed which side of the Locks complex the building is
on. She never took a compass reading of the glass pane itself. The window could be angled
south-southeast or south-southwest and still be honestly described as being on the 'south side.'"

"If you're not actually certain the window faces due south — only that it faces roughly southward —
does your D4 recommendation still hold?"

**Facilitator-only: what this actually does, and does not, change.** This is not a new sourced
number — MA1's own basis line already discloses that no floor plan gives the window's exact
bearing, and this twist is the natural consequence of a Hero re-reading that basis line critically
instead of accepting "south-facing" as settled. Walk a Hero through the orientation table above: at
the due-south value used and at 225° (SW), Option A still wins; at 135° (SE) and 270° (W), the
recommendation **inverts to Option B**. **The recommendation does not survive every honest reading
of MA1** — this is a real, mechanically-verified finding, not a rhetorical hedge. What the twist
does *not* do is hand a Hero a better estimate of the window's true orientation; the case has no
sourced answer for the window's exact bearing beyond "south side of the complex," and inventing a
more precise value here would be exactly the fabrication SPEC §5 forbids. **The twist reframes, it
doesn't resolve:** "which call wins under the due-south assumption" is a different question from
"is due-south actually where this window points," and a Hero who only answers the first hasn't
interrogated the assumption the whole D4 margin is built on.

## Immediate recommit

Re-vote immediately. Ask by name: "Does the orientation question change your vote — or does it just
tell you that 'south-facing' was an assumption worth pressure-testing, not a settled fact?" That
distinction is the transferable skill, not the vote itself.

## Deep conflict — three threads (20–30 min)

1. **A lower sun is not the same as a worse incidence angle.** September's sun sits over a degree
   lower in the sky at the shoot hour, but a vertical window's incidence angle depends on the sun's
   azimuth relative to the window's own normal, not elevation alone. Why does reasoning from
   elevation alone in the Launch get the right winner here but for an incomplete reason, and what
   would have to be true about the azimuth swing for that same reasoning to get the wrong winner?
2. **One disclosed assumption can flip a case that three others can't touch.** MA2 and MA3 each get
   tested across a real range and neither ever changes the winner — only MA1 does. What does it
   mean that the case's real fragility lives entirely in the one assumption with the *weakest*
   sourced basis (a general "south side" description, not a floor plan)?
3. **Is a confirmed single-day advantage worth more than a confirmed species?** Even setting the
   orientation question aside, is the optical advantage the August Call carries under the used
   assumption worth giving up the only Coho footage this film will ever get? What would the case
   have to show you — about the size of that advantage, or about how confident you are in MA1 — to
   change your answer?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — show Appendix A and C side by side, cold-call for a gut read from elevation alone, no Fresnel numbers yet |
| 3:00–10:00 | Position defense — *"Convince us your date actually wins on percent of glare removed, not just on 'better light'"* |
| 10:00–15:00 | Pressure-test the models — *"Which of MA1, MA2, MA3, or MA4 would have to change, and how, for your answer to flip?"* |
| **15:00** | **DROP THE TWIST** — the window-orientation uncertainty behind MA1, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (elevation vs. azimuth; MA1's fragility vs. MA2/MA3's robustness; a confirmed advantage vs. a confirmed species) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

A Hero who assumes "lower sun in the sky always means a worse angle on a vertical window" will
walk straight past the actual math. On a south-facing vertical pane, the incidence angle depends on
**both** the sun's elevation and its azimuth relative to the window's outward normal — not
elevation alone. A lower sun with a larger azimuth swing away from due south can land *closer* to
Brewster's angle than a higher sun with a smaller azimuth swing. In this case, reasoning from
elevation alone happens to land on the right winner (August) — but for the wrong reason, since the
real driver of the incidence-angle gap between the two dates is the combination of elevation *and*
azimuth working together under the assumed due-south orientation, not elevation by itself. The trap
is treating solar geometry as a single number (season, or time of day) when it is really two numbers
(elevation and azimuth) that only the NOAA calculator — not intuition — resolves, and a Hero who
never checks azimuth won't be able to explain why the gap is as large (or as fragile to MA1) as it
is.

## Socratic questions

1. Your D1 worksheet gives the glass window one fixed Brewster angle no matter what day you shoot — so what, exactly, is different between the August Call and the September Call: the material, or something else?
2. If a Hero says "the sun is lower in the sky in September, so of course the angle is worse" — is that true here, and which of the two quantities NOAA gives you for the sun's position actually moved the incidence angle the most?
3. The September Call still removes over 90% of the window's own glare — is a real, but not huge, relative gap in optical performance worth giving up the only Coho footage this film will ever get?
4. Appendix D gives you a floor — R_p/2 — that no amount of polarizer rotation removes — what does it mean, physically, that this floor is nonzero on one date and almost zero on the other?
5. Appendix G tells you the window's exact compass orientation is a stated assumption, not a sourced fact — does the choice between A and B survive every honest reading of that assumption?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight, and
how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for the
August Call at Anchor 1 purely on "higher sun feels better" and stays with the August Call after the
twist for a *different, Fresnel-and-orientation-based* reason has genuinely moved, even if the vote
count looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Anchor 4's "MA1 is the load-bearing assumption, not MA2/MA3/MA4" finding landed as a
  discovery or had to be told outright.
- Whether the elevation-vs-azimuth trap was the actual sticking point, or whether D2's
  trig-equation solve and D3's identity-verification step were the harder gate for most Heroes.
- Whether the window-orientation twist felt like a genuine new constraint or felt like the case
  dodging a clean numeric answer — worth listening for directly, since this case's own balance note
  records a 10.70% margin (well inside SPEC §2's cap) that the twist does not erase, only qualifies.

## Standards Touched On

Pythagorean Identity · Inverse Trigonometric Function · How to verify a trigonometric identity ·
How to solve a trigonometric equation over a given interval · How to evaluate an inverse
trigonometric function

## Sensitivity note (SPEC §6)

NONE required. This is an engineering/optics and professional-scheduling trade-off; the
endangered-species framing (Chinook salmon / Southern Resident orca population) is factual and
sourced, not exploitative. Facilitators should keep tone documentary and factual, not alarmist —
carried over unchanged from the superseded case's own sensitivity_note.
