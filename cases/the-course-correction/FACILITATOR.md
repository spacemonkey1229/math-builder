# FACILITATOR.md — The Course Correction

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Course Correction · **Tier:** T2 (MS-core) · **Studio:** Launchpad
**Standards:** Pre-Calculus/Vectors — Vector, Magnitude (Of A Vector), Unit Vector, Dot Product,
and their three how-tos (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01) — all `{{NEEDS_SOURCE}}` tokens closed (4 SOURCED
data figures, 4 resolved sensitivity placeholders, 0 OPEN; see `RESEARCH_LOG.md`).
`case.json.status` is `"researched"`. `margin_pct` is `16.88` (see the Balance section below) —
not `null`. Not yet run through `case-qa`; treat the numbers as sourced-and-computed but not yet
QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **NDBC Data Buoy 44090, Cape Cod Bay, MA** — a real, currently active NOAA current-observation
  buoy. The current used in this case (27 cm/s toward 340° T, observed 2026-09-01 21:30 UTC) is a
  live reading, not a hypothetical — a Hero can pull today's actual reading at
  `ndbc.noaa.gov/data/realtime2/44090.adcp` and see a different number. Worth naming out loud:
  most NDBC ADCP-equipped stations checked while researching this case (44029, 41013, 44025,
  45008, 41012, 42865, 42882) were either reporting "No Current Reports" (seasonal buoy retrieval,
  disestablished stations, sensor gaps) or a similarly weak current — 44090's 0.52 kt is genuinely
  representative of open-shelf conditions, not cherry-picked for drama.
- **R/V Medeia (Alaska Department of Fish and Game)** — a real 110-foot state fisheries research
  vessel. Its published speed/fuel figures (8.5 kt/19 gal/hr; 9.5 kt/32 gal/hr; ~11.5 kt/60 gal/hr)
  are the real anchor for Appendix C's fuel curve, and the real news story behind them — the crew
  found that shaving one knot off cruising speed cut fuel burn by 30–35%, not the ~12% you'd expect
  from a naive "fuel scales with speed" intuition — is a genuinely useful real-world hook for
  Anchor 2/Intro: ship fuel economics are not linear in speed, and this case's whole tension runs on
  that fact.
- **"Set and drift"** — the real marine-navigation term (see Appendix G's Dead Reckoning link) for
  exactly what Option B does: hold a heading and let the current move you off your intended track.
  Worth naming this term explicitly in Launch — it signals this is a real, named professional
  practice, not an invented math-class scenario.

## Intro

Frame the format: this is a real watch-standing decision — Priya has the conn, and whichever
heading she orders is hers to defend at breakfast. Name the opener — "You have the watch. The
buoy hasn't moved. The current has. Which one do you steer for?" Mention, once, that "set and
drift" is the real term mariners use for exactly the problem the uncorrected option accepts.

## Launch

Show the two chalked courses exactly as the Overview describes them — no numbers yet, just "hold
the straight bearing and throttle back" vs. "correct into the current and push harder." Ask:
"Which one would you order, just from what you see here?" Do not confirm or correct. Most rooms
will split on gut instinct ("obviously the cheaper one" vs. "obviously the one that gets there").
Record the split; Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with The Steady Burn — burn less fuel, let the current do
what it does?" Show of hands, both options, no discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'cheaper'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "which one burns less
fuel per hour" (obviously The Steady Burn, per Appendix C). Push on what the case is actually
asking: "Cheaper per hour, or cheaper to actually get to the buoy? Are those the same question?"
If the room lands on "we need to know how much fuel *each option actually spends getting there*,
not just its hourly rate," the case is working as designed — that's exactly the primary metric
(fuel cost per net nautical mile of progress), and it's a ratio precisely because the two
questions aren't the same one.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "burns less per hour" from "costs less to actually arrive," ask them to
name the actual steps before touching the appendices: resolve the measured current into
components (D1); build the course unit vector and each option's heading vector (D2); for the
uncorrected option, add heading and current as vectors and split the result along-track/cross-track
with a dot product (D3); draw both vector triangles to scale (D4); and turn all of that into a
real dollar-per-net-mile number for each option, checked against the weather window (D5). Re-ask:
"Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: the *Coastal Aster*'s actual distance and bearing to the buoy
(MA1) and the actual hours left in the weather window (MA2) are both stated scenario numbers, not
sourced facts — the ship and its watch schedule are fictional. Ask which of these is actually
load-bearing. The honest answer, from `sensitivity_model.py`'s flex sweep: MA1 and MA2 together are
the single most load-bearing pair in the whole case — they set Option A's required
speed-over-ground, which decides how far up Appendix C's real fuel curve Option A has to climb.
Loosen the window by about a quarter and the *cheaper* option flips from B to A. This is a case
where "how much time do we actually have" matters more to the dollar answer than the current itself
does.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's current-vector resolution, D2's unit vectors, D3's
along-track/cross-track split, and D4's two vector diagrams together as a room, cold-calling for
D3 specifically — this is where a Hero who built a correct D1/D2 but never actually projects the
resultant onto the course line will visibly struggle to explain why The Steady Burn doesn't arrive
exactly where it's pointed. Land on D5's two $/nm numbers together, out loud: $15.99 (A) vs.
$13.29 (B) — close enough that the room should feel real tension, not a runaway winner.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses: "Here's what the plotter doesn't tell you. Every reading you've been
using — the direction, the speed — is real, and it's from right now. But it's *one* reading, at
*one* depth, at *one* moment. NOAA's own current sensors, on buoys just like this one, keep
dropping out entirely — retrieved for winter, sensor gaps, stations that just stopped reporting.
The number you built your whole vector correction on could be stale by the time you're an hour
into the transit."

"If the current changes — direction, speed, either one — while The True Line is already
committed to its corrected heading, what happens to that heading? And what happens to The Steady
Burn, which was never betting on the current staying put in the first place?"

**Facilitator-only: what this does and doesn't change.** This does not change the researched D5
numbers — Appendix B's reading is real and stands as measured. It is proof that Option A's
precision (a resultant landing *exactly* on the course line) is precision with respect to a
snapshot, not a promise about the whole transit — while Option B's "let it drift, correct at the
end" strategy is, structurally, a design that's already built to tolerate exactly this kind of
change. A Hero who has fully reckoned with D3/D4 should be able to say *which* option's real-world
risk this twist actually raises, not just that "the numbers might be wrong."

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchor 2 — what does "cheaper" actually mean here?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface MA1/MA2 as the real load-bearing figures. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call D3's along-track/cross-track split specifically. |
| **25:00** | **DROP THE TWIST** — the real risk of a stale/changing current reading, delivered slowly, with pauses. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — the current reading, or your trust in what the correction actually buys you?" |
| 30:00–40:00 | Threaded deep conflict — see the three named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **"Cheaper per hour" is not "cheaper to get there."** A Hero who reads Appendix C and stops at
   "8.5 kt burns the least fuel of any speed, so Option B wins" has not actually computed the
   case's primary metric — they've computed a different, easier question. Push: "You've told me
   which option burns less fuel per *hour*. I asked which one costs less per net mile of *actual
   progress toward the buoy*. Are those the same number here? Why or why not?"
2. **A weak-looking current still moves you.** 0.52 kt sounds small next to an 8.5–11.5 kt boat
   speed — a Hero's gut says "that's basically nothing." Push: "If it's basically nothing, why does
   ignoring it cost Option B an extra 1.67 nautical miles and 22 minutes? What does that tell you
   about the difference between a force feeling small and a force *doing* something small?"
3. **Precision bought at a snapshot vs. a plan built to tolerate change.** The True Line's
   correction is exact *given* Appendix B's reading; The Steady Burn never depended on that
   reading holding steady in the first place. Push, post-twist: "If you don't trust the current
   reading to hold for the whole transit, does that make you trust The True Line's correction
   less — or does it just mean you'd have to re-solve it partway through? Which option handles
   being wrong about the current better?"

## The trap

Heroes will treat "8.5 kt is the cheapest speed on the fuel table" as the whole answer and
recommend The Steady Burn on that basis alone, without ever completing D3's dot-product split or
D5's actual $/nm computation — missing that the case's own primary metric is explicitly a ratio
(cost per net mile of progress), not a flat hourly rate, precisely so that "burns less fuel" isn't
allowed to win by default (see the concept sheet's own framing). A second, related trap: treating
the 0.52 kt current as negligible because it's small relative to boat speed, without noticing that
over a multi-hour transit a "small" cross-track rate compounds into a real, costed detour — the
twist exists specifically to catch a Hero who has decided the current "doesn't matter enough to
worry about" without ever running the numbers that show it costs Option B a real 22 minutes.

## Socratic questions

1. Your D5 table shows Option A costing more per net mile than Option B, but Option A is the only one that reliably makes the weather window. If you had to defend a single number to the Captain at breakfast, which one would it be — and why isn't the case's primary metric (D5) the whole story?
2. Appendix C shows fuel consumption rising much faster than speed does (a jump from 8.5 to 9.5 kt costs 68% more fuel for only 12% more speed). Why does that fact alone make "just correct for the current, it can't cost that much more" a risky assumption to make without doing D5's actual computation?
3. The twist points out that Appendix B's current reading is one snapshot, not a guarantee for the whole transit. Does that change which option you'd recommend — or does it just change how confident you are in the number you already computed?
4. If the weather window in Appendix A were twice as long, would you expect Option A's or Option B's advantage to grow? Use D5's structure (not just intuition) to explain why.
5. Appendix H sends you to research "how to add and subtract vectors" and "how to find the dot product of two vectors." Which of those two operations did you actually need to answer *this specific dilemma* — Option A's course, or Option B's drift — and which one turned out to matter more to the final dollar figure?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the
twist should be pressed to explain the move using D3/D5, not just the twist's emotional weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Vector · Magnitude (Of A Vector) · Unit Vector · Dot Product · How to find the magnitude and
direction of a vector · How to add and subtract vectors · How to find the dot product of two
vectors

## Balance argument (SPEC §2)

**Argument for A (The True Line).** The corrected heading lands the resultant exactly on the
shortest real-distance line to Buoy 44090 — the only option with zero wasted distance — and it is
solved specifically to make the 3.0-hour weather window, with zero slack. The extra cost is real
and computable: $15.99 per net nautical mile against Option B's $13.29, a 16.9% premium for both
distance efficiency and a schedule that actually holds.

**Argument for B (The Steady Burn).** It holds the *Coastal Aster*'s single most fuel-efficient
throttle setting — the lowest burn rate of any speed in Appendix C — for the whole transit, and it
still reaches the buoy. The extra distance the current drifts it (1.67 nm of 27.0, about 6%) costs
far less than the fuel premium Option A pays for its higher throttle. On the case's own primary
metric, Option B wins by 16.9% — real money against a cruise's finite underway-fuel budget — and
the missed weather window is a real but separate risk against a "tightest part of the window"
framing, not a guaranteed failure.

**Margin — COMPUTED 2026-09-01 (case-research, `sensitivity_model.py`).** `margin_pct: 16.88`.
**Winner (cheaper per net nautical mile): Option B, The Steady Burn.** Option A: required
speed-over-ground 9.000 kt (27.0 nm / 3.0 hr), solved boat speed 9.0153 kt, interpolated fuel rate
25.699 gal/hr (MA3), fuel 77.096 gal, cost $431.66, metric $15.9875/nm. Option B: heading 8.5 kt
(S2's economical point) plus the real current (S1) resolves to a resultant of 8.5162 kt at
253.53° T; dot product against the course gives an along-track rate of 8.5000 kt and a cross-track
rate of 0.5248 kt; total time 3.3726 hr (22.4 min over the window), engine distance 28.6671 nm,
fuel 64.079 gal, cost $358.78, metric $13.2882/nm. margin_pct = (15.9875-13.2882)/15.9875 × 100 =
16.88%.

**This margin sits comfortably under SPEC §2's ~20% guideline — no retune was needed.** But it is
not a *stable* 16.88%: `sensitivity_model.py`'s flex sweep shows the winner flips from B to A if
the weather window (MA2) loosens by roughly 25% or more, or if the transit distance (MA1) shortens
by roughly 20-25% or more, holding the other fixed. That sensitivity is disclosed, not hidden — see
`case.json.sensitivity_note` and the Modeling Assumptions table in `case.md` Appendix E.

**What this means for facilitation.** The room's real work is not just computing D5's two numbers
— it's recognizing that the 16.9% gap sits near a real edge, and that the case's qualitative
tension (cheapest-per-mile vs. reliably-on-time) is exactly as close as the numeric one. A Hero who
argues either option defensibly, using D3/D5, has done the case's actual job.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine maritime-operations math — no subject-matter sensitivity flag applies.
