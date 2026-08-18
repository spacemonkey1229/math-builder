# FACILITATOR — Reroute Or Wait

Guide Notes to the SPEC anchor ladder, plus the balance arguments, the wrong path to watch for,
the twist and the timed Socratic plan. **Do not hand this file to a Hero.** Every figure here is the figure of
record in `case.md` / `case.json`; if you find a disagreement, `case.md` wins and the case goes
back to QA.

**Primary metric:** total added rider-minutes per weekday, summed across every Line 20 rider.
**Lower is better.**

| | Option A — The Long Way Round | Option B — The Clean Break |
|---|---|---|
| Added rider-min / weekday | **26840.7** | **30285.8** |
| of which waiting | 23825.0 | 0 (nobody's headway changes) |
| of which in-vehicle | 3015.7 | 30285.8 |
| Rider-hours / weekday | 447.3 | 504.8 |
| Rider-hours over the closure | 581548 | 656192 |
| **Verdict** | **wins by 11.38%** | |

The margin of record is **11.38%** — inside SPEC §2's 20% cap, and close enough that the room has
a genuine fight. **It is not a stable 11.38%**: see *Anchor 4* and *Sensitivity* below.

---

## Intro

Frame the format in one minute. This is a case, not a problem set: there is no answer key, and the
grade is the defence, not the choice. Name the opener — *"By the end of this hour every one of you
will have told the riders' committee something, and you will have to live with it."*

State the two options by name and stop. **Do not put a number on the board yet.**

## Launch

Show the county's own project page for the Earthquake Ready Burnside Bridge (`case.md` Appendix F,
S6) — the recommended option is a **full closure**, four to five years. Let the room sit with the
duration before anything else. A bridge closing for a season is an inconvenience; a bridge closing
for five years is a service plan.

If you have a projector, put up the Line 20 timetable (S2) and let them notice it is one unbroken
row of timepoints from Beaverton to Gresham.

## Anchor 1 — TAKE A STAND AND VOTE

No reasoning yet. Thirty seconds, then hands.

> *"Is anyone courageous enough to stand with the plan that makes every single rider wait longer?"*

Record the split. You will re-vote at the Close and the movement is the artifact.

Expect a strong majority for **A** on instinct — "don't make people transfer" is the intuitive
humane answer, and it is also (on the base numbers) the correct one. That is a problem for the
discussion, not a gift: they will be right for the wrong reason. See the wrong path named below.

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

Let confusion grow here. Do not rescue it.

> *"What do you mean by 'better'? Better for whom?"*
> *"Is 'total minutes lost' the right question, or is it the easy question?"*

The move you are fishing for: **total** rider-minutes and **per-rider** minutes are different
metrics that recommend different plans, and the case has picked one of them. Option A spreads a
small cost across everybody; Option B lands a large cost on a few. A room that never notices it is
optimising a *sum* has not done Anchor 2.

Say out loud: *"Wow, this is a challenging problem."* Then move on without resolving it.

## Anchor 3 — WHAT IS THE PROCESS?

> *"If we go and get every number in these appendices, what do we then do with them to decide?"*

Push until someone says, in some form: *turn the corridor into a graph, weight the edges with
minutes, find the shortest path under each plan, multiply by how many people walk that path.*
That sentence is the whole case. Write it on the board.

Then re-ask: *"Is our question still the right question?"*

## Anchor 4 — WHAT DON'T WE KNOW?

The honest list, and it is short. Every ridership and timetable figure is published and cited
(Appendix F). What is **not** known is in Appendix G, and two entries matter:

- **MA4 — the 8-minute east-half extension from SE 12th to Rose Quarter.** This is the single
  most powerful number in the case and it is an assumption, not a measurement. Hand it to the room
  directly. At 4 minutes **Option B wins by 5.14%**; at 12 minutes Option A's lead reaches
  **23.55%**, which is outside the balance cap entirely. Nothing else in the case can flip it.
- **MA1 — Option A's 20-minute headway.** Someone will say *"why not just buy more buses?"* That
  is a real question and the answer is that it is a different option that is not on the wall. Do
  not let it become a third choice; let it become the observation that **Option A's entire cost is
  a fleet decision, not a geometry decision.**

Also flag MA6, the crossing-share method, and state its known direction of error: the closed edge
sits nearer the middle of the route and in its densest stretch, so the true crossing share is
probably **higher** than 12.658%, which pushes *against* Option A — the plan the arithmetic
favours.

## Data Deep Dive

Now, and only now, the numbers.

**The graph.** 14 vertices. Edges are exactly the Appendix B segments — 11 Line 20 segments, plus
the W5–PSN walk, plus RQ–PSN rail, plus the RQ–E12 street segment Option B needs.

**The derivation nobody expects to be able to do.** Route length is not published anywhere. It is
*derived* from four figures that are:

```
revenue hours = 9530 / 35.2       revenue miles = 32726 / 9.0
average speed = revenue miles / revenue hours
route length  = average speed x 120 min  ->  26.861 mi
```

Crossing share = 3.4 / 26.861 = **12.658%**, so **1206.3** of 9530 weekday riders cross.

**Option A.** Headway 15 → 20 min, so every rider waits **2.5** min more: 9530 x 2.5 = **23825.0**
rider-min. Crossing riders also pay the detour: 1206.3 x 2.5 = **3015.7**. Total **26840.7**.

**Option B.** Nobody's headway changes, so non-crossing riders pay nothing. A crossing rider pays
8 (bus to RQ) + 3.75 (wait, two rail lines at 15 min each) + 9 (rail RQ→PSN) + 2.857 (walk 600 ft
at 3.5 ft/s) + 7.5 (wait for the west half) − 6 (the Burnside segment no longer ridden) =
**25.107** min. Times 1206.3 = **30285.8**.

> **Watch for this:** the rail segment is **9** minutes on *both* the Blue and the Red line. An
> earlier draft of this case printed 8. If a Hero's ledger comes out near 29079, they have used
> the old figure — or read the RQ column as the PSN column, which is exactly how the error
> happened. Have them point at the two printed clock times they subtracted.

## The trap

**Heroes will compare the two per-person penalties and stop.** A 2.5 against a 25.107 is a factor
of ten, it is visible without a calculator, and it says Option A in enormous letters.

It is the wrong comparison, and it happens to reach the right answer, which is what makes it
dangerous — you cannot catch it by looking at the conclusion. **The denominators differ.** Option
A's 2.5 minutes is charged to 9530 people; Option B's 25.107 is charged to 1206.3. The whole case
is the product, not the rate.

The tell that a Hero has fallen in: they cannot say what the crossing share is, or they never
computed route length at all. **Ask every Hero who picks A: "how many people actually cross?"** If
they do not have 1206.3 (or their own defensible version of it), their answer is a guess wearing
arithmetic.

The mirror-image trap, rarer: a Hero computes the crossing share, finds it small, and concludes
Option B is therefore cheap — forgetting that Option B charges nothing to the other seven in
eight, which is the *argument for* B, not against it.

## Twist

**Drop at 15:00, slowly, with pauses.**

> *"A letter arrives from the county. The bridge the detour was going to use is having its own
> deck rehabilitated in the same window. Option A's buses have to go around again — one more
> detour, four more minutes for every rider who crosses. Option B is untouched: its river crossing
> is the light rail, which is on a different structure and a different programme."*
>
> *"You have 60 seconds. Are you changing your recommendation — or not?"*

**What it does to the arithmetic.** Option A's crossing riders now pay 2.5 + 4 = 6.5 minutes of
detour. Option A rises to **31665.7**; Option B is unchanged at **30285.8**. **The verdict flips
to B by 4.36%.**

> **State this convention when you drop the twist, or the room will diverge from your numbers.**
> The second detour is absorbed by layover recovery at the terminals, so it adds in-vehicle time
> only — the headway stays at 20 minutes. Say so out loud. A Hero who objects that MA1's own
> fixed-fleet logic should widen the headway *again* is applying the case's stated mechanism
> correctly, and they are worth more than the guide's own number: on that reading Option A gets
> worse still and the flip to B is larger. **The twist holds under both readings** — only the
> size of the gap changes, not the winner. Do not tell such a Hero they are wrong; tell them they
> found the load-bearing sentence the case left implicit.

This is a real flip, not a scare: it invalidates the majority position from Anchor 1 without
making B obviously right — 4.36% is closer than the 11.38% it replaces, so the room ends up with
*less* certainty than it started with, which is the honest state of this decision.

The follow-up is the whole point:

> *"What just broke in your original model? Were you wrong — or just missing information?"*

The transferable answer: nothing about their arithmetic was wrong. Option A was always the plan
whose cost depended on a road they did not control, and Option B was always the plan that owned
its own crossing. **Fragility is a property of a plan, not an error in a calculation.**

## Close — VOTE AGAIN

Re-vote. Count the movement, name it out loud.

> *"Did we ask the right question?"*
> *"What math was new to you, and how did you attack it?"*

Ask the room to finish this sentence: *"I would change my answer if ___."* Anyone who cannot fill
the blank has not modelled anything; they have picked a side.

## Five Socratic questions

1. Option A charges a 2.5 to each of 9530 riders and Option B charges a 25.107 to each of 1206.3 —
   so why does the plan with the *smaller* per-person cost not win by a factor of ten?
2. Route length is published nowhere; you derived 26.861 miles from four figures in Appendix D.
   Which one of those four, if it were wrong by a third, would move your recommendation most?
3. Appendix G MA4 puts Option B's east-half extension at 8 minutes. What would that number have to
   be for you to switch your recommendation, and is that a distance you would bet on?
4. MA6 says the true crossing share is probably higher than 12.658%. If it were double, which
   option does that help — and does it help it enough to matter?
5. After the twist, Option A costs 31665.7 and Option B costs 30285.8. Is a 4.36% margin a reason
   to change a public service plan, or is it inside the noise of everything you assumed?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Intro + Launch. County closure page, "four to five years." Cold-call, 30-second commitments, stand/sit vote. **No explanation, no numbers.** |
| 3:00–10:00 | Anchors 2 and 3. *"Better for whom?"* → total vs per-rider. Push to "graph it, weight it, shortest-path it, multiply by riders." Write that sentence up. |
| 10:00–15:00 | Anchor 4 + Data Deep Dive opens. Pressure-test: *"Whose plan is most fragile?"* Surface MA4 and MA1. Get the route-length derivation on the board. |
| **15:00** | **DROP THE TWIST** — the detour bridge's own deck closes. Delivered slowly, with pauses. 60 seconds to recommit. |
| 15:00–20:00 | Immediate recommit. Who reverses? *"What just broke?"* Land: fragility is a property of the plan. |
| 20:00–30:00 | Threaded deep conflict — (i) sum vs per-person: is spreading a cost thinly the same as it being small? (ii) who owns your crossing: control vs cost. (iii) the riders' committee is in the room on Thursday — does a 4.36% margin survive being said out loud to a person? |
| 30:00–45:00 | Close, re-vote, *"I would change my answer if ___"*, lessons learned, standards touched on. |

**Cohort bands** are declared in `case.json.cohort_bands[]` — Full (12–20), Compressed (6–11),
1:1/pair (1–2). Read the band note before the session; at Compressed you run one deep-conflict
thread, not three, and at 1:1 there is no vote to take.

## Sensitivity

**SPEC §6 subject-matter note:** none required. This case's stake is *access* — minutes of a
person's day — not illness, death, money stress or family hardship. The only care needed is that
the riders in question are real people in a real city: keep the discussion on "what do we owe the
people who cross" and away from treating 1206.3 riders as an abstraction to be minimised.

**±50% assumption sweep (Tier 2 probe 5), by declared dial:**

| Dial (Appendix G) | −50% | +50% | Flips? |
|---|---|---|---|
| MA2 detour extra minutes | A by 16.35% | A by 6.40% | no |
| MA3 walk distance | A by 6.03% | A by 16.15% | no |
| **MA4 east-half extension** | **B by 5.14%** | A by 23.55% | **YES — and breaks the 20% cap upward** |

**The guide must not defend 11.38% as a solid number.** One stated assumption moves the answer,
and it is named in Appendix G where a Hero can find it. A Hero who attacks MA4 and wins the
argument has done the best available work in this case — reward it.

MA1 (Option A's 20-minute headway) is excluded from the sweep because it is a plan parameter, not
an uncertain quantity; its "what if we bought more buses" version is handed to the room at Anchor
4 instead.

## Lessons Learned

- A cost spread across everybody can be larger than a cost concentrated on a few. Rates do not
  compare; totals do.
- A network is the right object here, and drawing it is not decoration — the cut edge, the cycle,
  and the shortest path are the three ideas that make the two plans comparable at all.
- A number that is not published can still be *derived* from numbers that are. Route length is the
  case's best moment: nobody publishes it, and it falls out of four figures that everyone does.
- Plans have fragility as well as cost, and the twist is how you feel the difference.

## Standards Touched On

Seven Discrete Mathematics / Graph Theory skills, all at zero prior coverage:
Graph (Vertices And Edges) · Vertex · Edge · Path · Cycle · Weighted Graph ·
How to find the shortest path between two vertices in a weighted graph.

Plus two already-covered Measurement skills that the deliverables genuinely force:
How to find elapsed time (every edge weight comes from subtracting printed clock times) ·
How to convert between units of time (rider-minutes → rider-hours → rider-hours over the closure).

**Not claimed:** *How to determine whether a graph has an Euler path or circuit* — the eighth skill
in the group. No deliverable in this case forces it. It stays open for a future case.
