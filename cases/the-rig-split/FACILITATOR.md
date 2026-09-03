# FACILITATOR.md — The Rig Split

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Rig Split · **Tier:** T2 (MS-core) · **Studio:** Adventure
**Standards:** Pre-Calculus/Matrices — Matrix, Matrix Dimension, Determinant, Identity Matrix, How
to add and multiply matrices, How to find the determinant of a 2x2 matrix, How to solve a system
of equations using a matrix (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-01) — all 8 `{{NEEDS_SOURCE}}` tokens closed (5
SOURCED, 3 ASSUMPTION, 0 DROPPED, 0 OPEN; see `RESEARCH_LOG.md`). `case.json.status` is
`"researched"`. `margin_pct` is `1.02` — a genuinely razor-thin real margin, not softened or
retuned. Not yet run through `case-qa`; treat the numbers as sourced-and-computed but not yet
QA-adjudicated.

## Real-world grounding (for the facilitator's own background, not for case.md)

- **U.S. EIA Drilling Productivity Report** (May 2024 issue, the final one published before EIA
  folded this data series into the Short-Term Energy Outlook) is the real backbone of this case:
  Permian new-well oil production per rig at 1,400 bbl/day vs. Bakken at 1,747 bbl/day — a real,
  ~24.8% per-rig productivity gap that is exactly the kind of "the data really does say one basin
  is hotter" tension the case needs.
- **Oil & Gas Journal, "Who moved my rig?"** and **MineralView's "How Long Does It Take to Drill an
  Oil Well?"** are the real anchors for the case's single most important Modeling Assumption
  (MA3, 14-day relocation downtime) — both describe a real, well-documented tradeoff in the
  drilling industry: rig mobility (moving a rig to chase a better lease) is a known lever, but it's
  never free, and the "how much does it cost in idle days" answer genuinely varies by an order of
  magnitude depending on distance.
- **Baker Hughes' weekly rig count**, real and famous, is used here only for scale — showing
  Heroes that Torchline (8 rigs) is a small operator relative to the real industry (242 Permian
  rigs, 29 Williston rigs, both real, both dated 2026-01-30) is a good discussion beat for "why
  would a company this size even be having this argument" if it comes up.

## Intro

Frame the format: this is a real operations-allocation decision a drilling manager has to defend
in front of his own boss and his own crew, not a worksheet. Name the opener — "You have two rigs.
One basin makes more money per rig, on paper. Moving them isn't free, and the two rigs on the
table are run by the guys who've worked here the longest. You have to give a number and a
recommendation by Friday." Mention, once, that this is a real, ongoing tension in the actual oil
and gas industry — rig mobility between basins is a real strategic lever operators use, and EIA
really does publish the productivity data that makes one basin look "hotter" than another.

## Launch

Show Appendix D's two real numbers side by side — Permian 1,400 bbl/day/rig, Bakken 1,747
bbl/day/rig — with nothing else yet. Ask: "Just from this, would you move the rigs?" Most rooms
will say yes immediately. Do not correct them yet. Record the vote; Close will re-ask it.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Hold the Line — leaving rigs in the basin that produces
less per rig?" Show of hands, both options, no discussion yet. Record the count.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'produces more'?"**

Let confusion grow here on purpose. Heroes will want to jump straight to "Bakken makes more oil per
rig, so move the rigs" — push on what that comparison is actually measuring: "Appendix D's number
is barrels per rig, per day, once a rig is already up and running there. Is that the same question
as 'which option produces more total barrels for Torchline, this quarter, counting every day
including the days a moved rig produces nothing at all'?" If the room lands on "per-rig-day
productivity and total-quarter output are two different questions," the case is working as
designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "which basin is more productive per rig" from "which option produces more
barrels this quarter, net of downtime," ask them to name the actual steps before touching the
appendices: define the rig-day unknowns and write the system of equations (D1); solve it with a
real matrix method for both options (D2, D3); convert the solved rig-days into total barrels and a
blended rate (D4); and decide, with a real sensitivity check, which option to recommend (D5).
Re-ask: "Is our question still the right one, now that we can see the steps?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gap honestly: Torchline's own fleet size, how many days are actually left in the
quarter, and exactly how many days a real Permian-to-Bakken rig move would cost are all currently
open `{{NEEDS_SOURCE}}` tokens — Torchline is a fictional company, so none of these can be
independently verified the way the basin productivity gap can (that part is anchored to real,
published EIA data). Ask which of the open figures is actually load-bearing for the
recommendation. The honest answer: the relocation-downtime figure (Appendix A/E) is the single
most load-bearing open item in the whole case — see the breakeven finding below.

## Data Deep Dive

Now, and only now, the numbers (once `case-research` has closed every appendix). Walk D1's system
setup, D2's matrix solve, D3's parallel solve for Option B, and D4's comparison table together as a
room, cold-calling for D4 specifically — this is where a Hero who solved D1/D2 correctly but never
converts the rig-days into a blended barrels-per-rig-day number will visibly struggle to answer
"so which option actually wins, and by how much."

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses, once Appendix E is sourced: "Ray's crew — the two most experienced
rigs, the ones that would move — comes back with new information of their own. If Torchline
front-loads two extra trucking crews and pre-stages the disassembly work the week before the move,
Ray thinks he can get the Bakken rigs producing in as little as 10 days instead of 14 — at a real,
extra logistics cost the case hasn't priced yet."

"Ten days is inside the real published range in Appendix E — nothing about this is made up. If
downtime drops from 14 days to 10 days, does the recommendation change? What's the actual number
you'd need to know — the extra logistics cost — before you could say whether that tradeoff is worth
it?"

**Facilitator-only: what this does and doesn't change.** The breakeven point (computed in
`case.json.balance.margin_note`) is 11.92 days — so a genuine drop to 10 days *does* flip the
recommendation on the barrels-per-rig-day metric alone, back toward the Basin Shift. This is a real,
computable consequence of the case's own real numbers, not a trick. The open question the Twist
is designed to expose is that "can we do it faster" is not the same question as "should we, once we
price what faster costs" — a Hero who reflexively re-votes for the Basin Shift without asking what
the extra logistics spend is has not fully reckoned with what the Twist actually handed them.

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just fair" (Anchor 2 — per-rig-day productivity vs. total-quarter output). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — name the D1-D5 steps, surface which figures are real vs. stated. |
| 15:00–25:00 | Data Deep Dive — D1-D5 together; cold-call D4's comparison table specifically. |
| **25:00** | **DROP THE TWIST** — Ray's crew's 10-day counter-offer, delivered slowly, with pauses. |
| 25:00–30:00 | Immediate recommit: who reverses? "What just broke — the math, or the price of getting there?" |
| 30:00–40:00 | Threaded deep conflict — see the three named threads below. |
| 40:00–45:00 | Close, re-vote, reflection, Lessons Learned. |

## Deep conflict — threads (20–30 min)

1. **A close margin is still a real margin.** At the case's own stated 14-day downtime, Hold the
   Line wins by about 1 percentage point — genuinely close, but not a tie. Push: "If the numbers
   are this close, does that mean the decision doesn't matter much either way — or does it mean
   the decision matters *more*, because a small, cheap change (a couple of days of downtime) is
   enough to flip it?"
2. **Is the crew-disruption cost really 'outside the model,' or does it belong in the model?**
   Background states plainly that moving Ray's crew is a real cost that never enters the
   barrels-per-rig-day number. Push: "If you could put a dollar value on crew disruption, would you
   add it to the model, or does it stay a values judgment on top of the math? What changes about
   Wade's Friday recommendation depending on which you pick?"
3. **Whose 10-day number do you trust?** The Twist hands the room a faster timeline from the person
   most motivated to make the move look better (Ray, who'd rather not lose his crew's Permian
   assignment permanently — or would he rather move, if that's framed as career growth? Either
   reading is defensible). Push: "Does it matter who's telling you the downtime number, separate
   from whether the number itself is plausible?"

## The trap

Heroes will treat Appendix D's basin-productivity numbers (1,747 vs. 1,400 bbl/day/rig) as if they
already answer the question, recommending the Basin Shift on that comparison alone — without ever
building D1-D4's actual rig-day accounting, which is the only way to see that 14 days of zero
production on 2 rigs is nearly enough to cancel out the Bakken's real per-rig edge. A second,
related trap: after the Twist, reflexively re-voting for the Basin Shift because "10 days is
better than 14" without asking what the *extra cost* of compressing the timeline actually is —
mistaking "the number moved in our favor" for "we now know enough to decide."

## Socratic questions

1. Appendix D shows the Bakken producing about 25% more barrels per rig-day than the Permian. Does that number, by itself, tell you which option produces more barrels this quarter? Why or why not?
2. Your D1/D2 system used the same coefficient matrix for both options, just a different constant vector. What does that tell you about how similar — or different — the two options actually are, structurally?
3. The case's own margin (about 1%) is much smaller than the real productivity gap between the two basins (about 25%). Where did most of that gap go?
4. If the relocation-downtime figure (Appendix A/E) turned out to be 2 days shorter than what the case states, would your recommendation change? What does that tell you about how much of this decision rests on a single assumption?
5. Background says moving Ray's crew is "a real cost that doesn't show up in any spreadsheet." Should Wade's recommendation account for that cost anyway, even though it's not part of the barrels-per-rig-day number? What would it mean to say "the math says A, but I'm recommending B"?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare to Anchor 1's vote — a room that moves after the twist
should be pressed to explain the move using D4's numbers plus the Twist's new information, not just
the Twist's emotional weight.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

## Standards Touched On

Matrix · Matrix Dimension · Determinant · Identity Matrix · How to add and multiply matrices · How
to find the determinant of a 2x2 matrix · How to solve a system of equations using a matrix

## Balance argument (SPEC §2)

**Argument for A (the Basin Shift).** The Bakken genuinely out-produces the Permian on a real,
sourced per-rig basis (1,747 vs. 1,400 bbl/day, EIA S1/S2) — a real ~24.8% edge. Even after paying
the full stated 14-day relocation-downtime cost on both moved rigs, the Basin Shift still comes
within about 1% of matching Hold the Line's total output, and the real breakeven point (11.92 days)
sits comfortably inside the real published 1-4-week downtime range (Appendix E, S4) — a modestly
faster real-world move easily flips the recommendation in A's favor.

**Argument for B (Hold the Line).** Every one of the fleet's 8 rigs keeps producing every day of
the 60 remaining days — zero idle rig-days, zero lost production, and zero disruption to Torchline's
most experienced Permian crew, a real cost Background names explicitly and that the barrels-per-
rig-day metric never captures at all. On the case's own stated 14-day downtime assumption, Hold the
Line wins the blended metric outright.

**Margin — COMPUTED 2026-09-01 (case-research).** `margin_pct: 1.02`. **Winner: Option B, Hold the
Line**, but only barely. Full arithmetic trail is in `case.json.balance.margin_note`: Option A
(Basin Shift) totals 706,364 barrels (1,471.59 bbl/rig-day blended); Option B (Hold the Line)
totals 713,640 barrels (1,486.75 bbl/rig-day blended). This margin is comfortably inside SPEC §2's
~20% cap and required no retuning — it is a genuine, razor-thin result of the case's own real,
sourced data (S1, S2) and its single most sensitive Modeling Assumption (MA3, relocation downtime).

**What this means for facilitation.** This case's tension is not manufactured — it is the direct,
computed consequence of a real ~25% basin productivity gap almost, but not quite, getting
cancelled out by a real, citable relocation-downtime cost. The room's genuine work is the D1-D4
rig-day accounting itself (most Heroes will initially treat the 25% productivity gap as decisive
and be surprised how close the actual quarter-total comparison comes out), plus the honest,
un-resolved question of whether the crew-disruption cost belongs in the decision even though it
never enters the metric.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine commercial drilling-operations resource-allocation math — no
environmental-harm or drilling-safety framing. Keep it that way in discussion: this case is about
where rigs get assigned and how a manager defends a number, not about drilling risk or
environmental impact.
