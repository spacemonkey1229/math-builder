# Guide Notes: The Sunset Ramp

**Case:** The Sunset Ramp · **Tier:** T3 (Advanced) · **Band:** HS · **Studio:** Launchpad
**Standards:** six Calculus/Derivatives skills (derivative, instantaneous rate of change, power
rule, tangent line, tangent-line-at-a-point how-to, differentiable), all `new_coverage`, plus two
already-covered supports (compound-unit conversion, percent of a number). Exact ids in
`case.json.standards[]`.

**Status:** drafted at `case-write` 2026-08-13; balance argument, margin, and Facilitator-only
numbers below fill in once `case-research` lands the real EIA generation data and capital-cost
figures.

## Intro

Frame the format before anything else: the committee tomorrow does not care about total
megawatts — it is going to ask whether either bid can cover the *worst instant* of the evening
drop. Name the opener: *"You have one shift's worth of prep before the capital committee votes on
your recommendation."*

## Launch

Show a real evening net-load / "duck curve" chart for a solar-heavy grid — CAISO publishes one
daily and it is visually dramatic on its own. Ask: *"What do you think happens to everything else
on the grid in the hour after this line falls off a cliff?"* Let the gut reads stand.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

*"Is anyone courageous enough to stand with Lena on the battery, over the gas peaker?"*
Stand-or-sit, no discussion. Record the count — the Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'fast enough'?"**

Let confusion grow here; it is deliberate. The room will want to say "the bigger one" or "the one
with more megawatts" without asking fast compared to *what rate*, over *what instant*. Push:

- *"Both options produce plenty of power eventually. What does 'eventually' cost the grid?"*
- *"If the battery could respond to any rate at all, would it automatically win? What's its actual
  limit, if not speed?"*
- *"What's the peaker's limit, if not fuel?"*

Do not resolve this. A room that leaves Anchor 2 arguing about *rate versus quantity* is exactly
where it should be.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Make them name the steps before any appendix is opened:

1. Build a smooth model of the real evening solar decline from the actual hourly data (D1).
2. Differentiate it to get the instantaneous rate of generation loss at any moment (D1).
3. Find the single worst instant and write the tangent line there — that slope is the rate the
   grid must actually cover (D2).
4. Convert each resource's own physical limit into the same MW-per-minute units (D3).
5. Check which resource's capability actually covers that worst-instant rate, then compare cost
   per unit of rate covered — not cost per megawatt (D4).

Re-ask: *"Is our question still the right question, now that we can see the steps?"*

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the honest gaps, all of which will live in `case.md` Appendix C once research completes:

- Whether a published, dated figure exists for a specific battery chemistry/vendor's full-power
  ramp rate, or only a general "near-instantaneous" characterization.
- Whether a published, dated figure exists for a specific gas-turbine model's minimum start-up
  ramp rate, or only an industry-typical range.
- Whether the two technologies' capital-cost figures come from the same cost-basis year and
  region.

## Data Deep Dive

Now, and only now, the numbers. Work D1 → D4 as a room. Cold-call specifically on **D2**'s
differentiability justification: a Hero who writes a tangent line without addressing why a single
smooth P(t) is being used across an hour boundary — where the raw hourly data itself is not smooth
— has skipped the part of the deliverable that is actually named `differentiable`.

## Twist

At the 15-minute mark: reveal that real balancing authorities don't actually pick one resource
alone — CAISO's own real operational history is exactly why battery storage discharge in its
territory has tripled in recent years: peakers alone kept leaving a gap like D3's 87.5 MW/min
shortfall. Reveal that a *much smaller* battery — just enough to cover the peaker's shortfall
rather than replace it outright — could be paired with Option B for a fraction of Option A's full
battery cost. *"You now have 60 seconds: does adding a small backstop battery to the peaker change
your vote — and if it does, why didn't 'pair them' occur to you as a third path the first time
through?"*

This twist needs no new sourced number — it runs on figures already on the table (the 87.5 MW/min
gap from D3, and the $1,744/kW battery cost basis from Appendix A) and is computable live in the
room. It also exposes the case's binary framing as an intentional simplification: the real
decision doesn't have to be all-or-nothing, and noticing that is itself the lesson.

## Deep conflict — one thread (T3, one thread at full band; compress further for smaller cohorts)

**A resource that is fast but shallow, versus a resource that is slow but deep.** The battery can
match any rate the grid throws at it — for four hours. The peaker ramps at a fixed, finite rate no
matter how badly the grid needs it to go faster — but it can do that all night. Push: *"If the
measured ramp rate is faster than the peaker's real limit, is 120 MW of nameplate capacity worth
anything at all in that instant?"*

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — real evening net-load chart, cold-call for a gut read, no formulas yet |
| 3:00–8:00 | Anchor 1 vote, then Anchor 2 — push on "fast compared to what rate, over what instant?" |
| 8:00–15:00 | Anchor 3 process + Anchor 4 unknowns, named before any appendix opens |
| 15:00–30:00 | Data Deep Dive — work D1→D4 as a room; cold-call D2's differentiability justification |
| **30:00** | **DROP THE TWIST** — the backstop-battery pairing |
| 30:00–31:00 | 60-second immediate recommit — does the twist change the vote? |
| 31:00–40:00 | Deep conflict thread — fast-but-shallow vs. slow-but-deep |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Most Heroes will jump straight to D4, divide each option's total capital cost by its own
delivered rate, see that one number is smaller, and stop — they will never go back and check D3's
covered/not-covered result before writing the recommendation. Watch for a student who runs the
division, circles the cheaper dollars-per-MW/minute figure, and announces a winner without ever
saying out loud which option actually clears 137.5 MW/min and which one doesn't. That Hero has
quietly assumed "cheaper per unit" already accounts for whether the unit delivered is the right
size — they will miss that the cheap number is buying a *smaller job* than the evening actually
demands. A second group of students will make the mirror-image mistake: they will pick the
fully-covering option on reflex, purely because "it covers the whole measured rate," and never
pause to ask whether that 137.5 MW/min figure itself — built from a Modeling Assumption's peak
instant (Appendix C, MA1), not a directly measured table — is solid enough ground to justify the
larger capital premium. Either way, the tell is the same: a pitch that reports only one of D3 or
D4 out loud and treats the recommendation as settled the moment the first number lands.

## Socratic questions

1. Your D2 tangent line's slope is the instantaneous ramp rate at the worst single instant of the evening — why is that number, and not the average rate over the whole hour, the one the committee actually needs?
2. If the battery could sustain its full ramp-rate capability for only 90 minutes instead of 4 hours, would that change your D3 covered/not-covered determination, and would it change your D4 cost comparison?
3. The gas peaker has a hard physical floor on how fast it can ramp — what would have to be true about tomorrow's forecast for that floor to disqualify it entirely, regardless of cost?
4. Which of your Appendix A figures, if it moved by 20%, would flip your D4 recommendation — and which could move by 50% and still not flip it?
5. Lena's name is on this recommendation, not just the math — if one option barely covers the measured rate and the other clearly doesn't, but costs far less per unit of rate covered, which argument do you lead with in the committee room, and why?

## Close

**VOTE AGAIN.** Then: *"Did we ask the right question at the start?"* and *"What math was new to
you tonight, and how did you actually attack it?"*

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Derivative · Instantaneous Rate Of Change · Tangent Line · Differentiable · How to find a
derivative using the power rule · How to find the equation of a tangent line at a point · How to
convert an amount with compound units · How to find the percent of a number

## Facilitator note — sensitivity

None required (SPEC §6). The stakes are operational and professional — grid reliability and a
dispatcher's capital recommendation. No personal loss, no family hardship, no safety trade-off in
the sense SPEC §6 flags; keeping the lights on during a ramp is the stake, not a body count.

## Balance argument and Facilitator-only numbers

Full worked argument lives in `case.md`'s `<!-- FACILITATOR ONLY -->` section and
`case.json.derived`. Summary:

| | The Solar Stack (A) | The Peaker Call (B) |
|---|---|---|
| Total capital cost | $649,200,000 | $192,720,000 |
| Ramp-rate capability | 12,000 MW/min (derived, ~1s response) | 50 MW/min (sourced, S3) |
| D2 required rate | 137.5 MW/min | 137.5 MW/min |
| Covered? | Yes, fully | No — only 36.4% of it |
| Rate actually delivered (capped) | 137.5 MW/min | 50 MW/min |
| Cost per MW/min delivered | $4,721,455 | $3,854,400 |

**The verdict.** Option B wins the case's own primary metric (dollars per MW/minute of ramp-rate
covered) by **18.36%** — but only by counting the smaller job it actually does. Option A is the
only option that fully covers the measured worst-instant rate. This is a genuinely close, two-
sided case: cheaper-per-unit-but-incomplete versus complete-but-more-expensive-per-unit.

**Where the 137.5 MW/min figure comes from, and why it matters for the discussion.** It is the
tangent-line slope of a quadratic fit through three real-anchored hourly points (D1/D2), evaluated
at the fitted window's late edge (19:00) — not a directly measured minute-by-minute figure. The
hourly data itself is a stated Modeling Assumption (MA1) built to match one real, cited statistic
(CAISO's average 6.5 GW/hour ramp during the 6pm hour). A different, equally plausible curve
through the same hourly total could put the peak instantaneous rate anywhere from about 108 MW/min
up past 137.5 MW/min — meaning the peaker's covered/not-covered verdict is genuinely sensitive to
a modeling choice the Hero should be pushed to notice, not treat as settled fact.

**Sensitivity, one dial at a time.** If the true peak instantaneous rate were closer to the hourly
average (108 MW/min) instead of the fitted-model's edge value (137.5 MW/min), the peaker would
still fail to cover it (108 > 50), so B's covered/not-covered verdict is not fragile. B's cost per
MW/min stays flat at $3,854,400 either way, because it is always capped at B's own fixed 50 MW/min
ceiling regardless of the required rate. A's cost per MW/min, by contrast, is capital divided
directly by whatever the required rate turns out to be — a lower required rate spreads the same
$649,200,000 over a smaller denominator, so A's figure gets *worse*, not better: at 108 MW/min it
rises to about $6,011,111/MW-min, and B's percentage lead over A widens from 18.4% to about 35.9%.
The margin is real and not a knife-edge artifact of the exact 137.5 figure — if anything, the case
is conservative in A's favor as drafted.

**Disclosed P5 instability (2026-08-17).** The paragraph above tests the case's own documented
108–137.5+ MW/min range and the recommendation holds throughout it. A much larger, mechanical
±50% stress test of the raw 17:00/18:00 net-load table entries themselves (`t60_net_load_mw`,
`t120_net_load_mw` in `sensitivity_model.py`) — a far bigger swing than MA1's own disclosed
uncertainty — does flip the recommendation to Option A in every direction tested, because that big
a swing sharply changes the fitted quadratic's curvature and therefore the D2 rate itself. This is
recorded, categorized, and justified in `case.json.sensitivity_disclosure[]` (Category I —
interpolation within the fitted window, not extrapolation) rather than hidden; a guide should be
ready for a room that pushes hard on "what if the 17:00/18:00 figures were very different" to hear
that the recommendation is not resilient to a change that large, only to the smaller, more
realistic range the case itself already flags.
