# FACILITATOR.md — The Locks Window

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Locks Window · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Pre-Calculus/Trigonometric Identities — Pythagorean Identity, Inverse
Trigonometric Function, and three "how to…" skills, plus Angle (Geometry) and Advanced Numbers
percent-of-a-number (thickness — see `case.json.standards[]` for exact ids). This is a
**second-pass case**: all 5 scored skills already show `n>=1`; `new_coverage[]` is empty by
design.

All 24 `{{NEEDS_SOURCE: ...}}` placeholders have been sourced or converted to a disclosed
Modeling Assumption by `case-research` (SEE `case.json.needs_source[]`, `case.json.sources[]`,
`RESEARCH_LOG.md`). One decorative placeholder (the Tiffen Multi Rota Tray mount's physical
rotation-range spec) was searched for in good faith and dropped rather than guessed — nothing in
this case depends on it. Two genuine gaps — the underground viewing-room window's real compass
orientation, and the exact minute of the shoot — have no public source and are recorded as
Modeling Assumptions MA1 and MA2 in `case.md` Appendix G, with sensitivity ranges.

## Facilitator-only arithmetic note (sourced values — margin computed here, not in case.md)

Using the sourced refractive indices $n_{water} = 1.33$ [S1] and $n_{glass} = 1.52$ [S2] with
$\tan\theta_p = n_2/n_1$ [S3]: Brewster angle for water $= 53.06°$; Brewster angle for glass
$= 56.66°$. The angular gap between the two is small — $3.60°$.

Each surface's $I_0$ (Appendix D) — the fraction of incident light reflected as polarized glare
at that surface's own Brewster angle — is derived from the Fresnel s-polarization reflectance
formula [S4], using that at Brewster's angle the p-reflectance is exactly zero, so the
unpolarized-light reflectance is $R_s/2$: $I_{0,glass} = 7.83\%$, $I_{0,water} = 3.86\%$. Glass
reflects roughly **twice** as much of the incident light as glare at its own Brewster condition
as water does — this is the number that actually decides the case, not the angular gap.

**Margin computation (this is the interpretation used for `margin_pct`; SEE `case.json.balance`
and `RESEARCH_LOG.md` for the full derivation and an alternative reading that was considered and
rejected):** setting the ring to a surface's own Brewster angle fully nulls that surface (100% of
its $I_0$ removed). At the non-prioritized surface, the ring sits off that surface's own null by
the $3.60°$ gap, so Malus's Law removes only $\sin^2(3.60°) = 0.39\%$ of *that* surface's own
glare — both options leave the secondary surface almost entirely glared, exactly as
`argument_a`/`argument_b` already say. Total glare removed, as a share of the combined
maximum-possible glare ($I_{0,glass}+I_{0,water}=11.69\%$ of incident light):

- **Glass Call (A):** $7.83 + 3.86 \times \sin^2(3.60°) = 7.85\%$ of incident light removed →
  **67.1%** of the combined maximum.
- **River Call (B):** $3.86 + 7.83 \times \sin^2(3.60°) = 3.89\%$ of incident light removed →
  **33.2%** of the combined maximum.

**`margin_pct` = 33.9 percentage points. Winning option: A, the Glass Call** — driven almost
entirely by glass simply reflecting more glare at Brewster's angle than water does, not by the
small angular gap and not by the sun-incidence-geometry figures in Appendix C (those ground the
student's D2 worksheet in real geometry but do not change this margin under the model used here).
This is a **substantive, decisive margin**, not the "close call" the angular-gap framing alone
would suggest — confirm at `case-readiness`/`case-qa` that this matches the intended model before
this margin is treated as final; a differently-weighted reading of "percent removed, net of
reappearing" was considered (a raw-percentage-point difference rather than a share-of-maximum
comparison) and produces a much smaller margin (~4 percentage points of incident light, same
winner) — see `RESEARCH_LOG.md` for both readings side by side.

## Intro

Frame the format before the numbers: this is a one-shot, one-frame decision, not a homework
problem — "You are Mara Ellison. One filter, one rotation angle, one take. You cannot re-shoot
the peak of the run." Let that land before Launch.

## Launch

Show two images with no context: the underground window shot and the open-river shot, each with
visible glare. Ask for a gut read: "Same filter, same rotation ring. Why can't one setting fix
both?" Do not resolve the "why" yet — that's Anchor 2's job.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the River Call — the wider shot, glare-free, and let
the window keep its glare?" Show of hands, both options, no discussion. Record the count for the
Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "Why would the same filter setting not work for both
surfaces?"**

Let confusion grow. Heroes will want to assume "just split the angle down the middle." Push
until someone notices that a polarizer only fully nulls glare at one specific angle per surface
(that surface's Brewster angle), and that glass and water don't share one. If the room reaches
"there are two different target angles, not one" on its own from the setup rather than from being
told, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening the appendices:
find each surface's Brewster angle from its refractive index (feeds D1), figure out how far off
each surface sits from its own null when the polarizer favors the other surface (feeds D2), use
the double-angle identity to double-check the $\cos^2\theta$ math (D3), then turn "how much
light gets through" into "what percent of glare is actually removed" for each option (D4).
Re-ask: "Now that we can see the steps — is our question still the right one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix G's stated gap honestly: this case doesn't yet know the exact camera position or
window orientation relative to true north and the river surface, because Ballard Locks hasn't
published a detailed floor plan of the underground viewing gallery. If `case-research` cannot
close that gap from public site photography, it becomes a disclosed Modeling Assumption — ask the
room which parts of this case are real, cited physics (the refractive indices, Brewster's angle
formula, the polarizer's real spec sheet, the real sun position from NOAA's calculator) versus
which one thing is a stated scenario choice.

## Data Deep Dive

Now, and only now, the numbers. Walk D1 as a room (deriving both Brewster angles), then split
into two desks for D2 and D3 — one solves the rotation-angle equation for each surface, one
verifies the double-angle identity — before reconvening to build D4's comparison table and D5's
graph together.

## Twist

**The angular gap between the two Brewster angles is small — but "small gap" does not mean
"small stakes."** A Hero who stops after computing the $\approx 3.6°$ gap and assumes the two
options must therefore be nearly identical has not yet reckoned with Appendix D's $I_0$ values:
each surface reflects a different fraction of incident light as polarized glare in the first
place, so the *same* small angular penalty applied to two different starting glare intensities
does not produce the same absolute glare left over. Drop Appendix E's real historical run-count
context at this point too: in a year where the run is running unusually low relative to the
historical series, the open-river establishing shot may be documenting something rarer than the
window shot ever could that season — a consideration the primary metric's optics math never
touches at all.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on their answer because of the glare-removal margin, or because of the run-count
context, or both?

## Deep conflict — two threads (20:00–30:00)

1. **A small angular gap vs. a real percent difference.** The two Brewster angles differ by only
   a few degrees. Is that gap "close enough to ignore," or does the non-linear $\cos^2\theta$
   shape of Malus's Law mean a small angular gap can still produce a meaningful percent-removed
   difference once the two surfaces' own reflectivities are accounted for?
2. **What the metric does and doesn't know.** The primary metric is entirely about glare removal.
   It says nothing about which shot the film actually needs more this particular week (Appendix
   E). Is it fair to call one option "the better shot" using a metric that was never built to
   capture that?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — two glare-filled images, no context, gut-check vote |
| 3:00–6:00 | Anchor 1 vote recorded |
| 6:00–9:00 | Anchor 2 — why one filter setting can't null both surfaces |
| 9:00–12:00 | Anchor 3 — name the four-step process before opening the appendices |
| 12:00–15:00 | Anchor 4 — separate real, cited physics from the one open modeling gap |
| **~15:00** | **TWIST drops** — a small Brewster-angle gap does not guarantee a small glare-removal difference, and the run-count data adds a non-optics reason the choice matters |
| 15:00–20:00 | Data Deep Dive — D1 worked as a room |
| 20:00–30:00 | Deep conflict — two threads (angular gap vs. percent difference; what the metric does/doesn't capture) |
| 30:00–40:00 | Data Deep Dive continued — D2–D5 in two desks, reconvene for the shared table and graph |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Heroes will compute the angular gap between the two Brewster angles, see that it's small, and
conclude the two options must be nearly interchangeable — missing that Malus's Law is a
$\cos^2\theta$ relationship, not linear, so the same small angular penalty lands differently
depending on each surface's own starting reflectivity (Appendix D's $I_0$ values). A second,
subtler trap: Heroes may treat "percent of glare removed" as the whole decision and never engage
with Appendix E's run-count context — the case's primary metric is purely optical and was never
built to weigh which shot matters more in a given year, and a strong pitch should say so
explicitly rather than pretend the optics settle everything.

## Socratic questions

1. The two Brewster angles differ by only a few degrees. Does that gap, by itself, tell you
   whether the two options are close on percent-of-glare-removed — or do you need the actual
   reflectivity of each surface too?
2. D3 asks you to verify $\cos^2\theta = (1+\cos 2\theta)/2$ algebraically using the Pythagorean
   identity. What would it mean if your two forms of the transmitted-glare fraction *didn't*
   agree once you plugged in numbers?
3. If the sun's position at the moment Mara rolls were different from what Appendix C states —
   say, later in the day, lower in the sky — would you expect the angle of incidence on the glass
   and on the water to change by the same amount, or different amounts? Why does that matter for
   which Brewster angle ends up closer to being satisfied?
4. Appendix E shows a real historical run-count time series. If this particular week's Chinook
   run were running unusually low, would that change which option you'd defend — even if the
   glare-removal margin stayed exactly the same?
5. The primary metric never mentions which shot the film needs more this season. Is that a flaw
   in the metric, or is it fair to expect Mara to weigh the optics and the run-count context
   separately, the same way Danny in a different case has to weigh flow rate and obstruction
   clearance separately?

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes noticed on their own, in Anchor 2, that a polarizer nulls only one angle per
  surface — or needed a direct hint.
- Whether the small angular gap was treated as proof the options are interchangeable, or whether
  the non-linear $\cos^2\theta$ shape was caught before D4.
- Whether the run-count context (Appendix E) surfaced unprompted as a reason to weigh the two
  options differently, or only after the Twist.

## Standards Touched On

Pythagorean Identity · Inverse Trigonometric Function · How to verify a trigonometric identity ·
How to solve a trigonometric equation over a given interval · How to evaluate an inverse
trigonometric function · Angle · How to find the percent of a number

## Sensitivity note (SPEC §6)

NONE. This is an engineering/optics trade-off. The endangered-species framing (Chinook salmon as
a primary Southern Resident orca food source) is factual and sourced, not exploitative, and the
math never asks a student to reason about the orca population's decline as a quantity — it only
ever touches the real historical Chinook run-count series as context for which shot matters more
in a given year (protection/documentation framing, not casualty framing). Facilitators should
keep tone documentary and factual, per the approved concept sheet — no special content
restriction is needed beyond that.
