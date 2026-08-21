# FACILITATOR.md — Deluge Gun

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** Deluge Gun · **Tier:** T4 (HS) · **Studio:** Launchpad
**Standards:** Pre-Calculus — Pythagorean Identity, Inverse Trigonometric Function, and three
"how to…" skills, plus Sine/Cosine Function, Reference Angle, Radian, and degree-radian
conversion (thickness), plus Advanced Numbers percent-of-a-number (see `case.json.standards[]`
for exact ids).

Numbers below match the cited/assumed figures now in `case.md` and `case.json` (researched
2026-08-19) — see `RESEARCH_LOG.md` for the sourcing trail.

## Intro

Frame the format before the numbers: this is a thirty-second, one-shot decision, not a homework
problem — "You are Danny Ruiz. The monitor's pressure and tip are already locked. The only
thing you control is the angle, and you have to call it before the water leaves the barrel." Let
that land before Launch.

## Launch

Show the two numbers chalked on Danny's arm with no context: one small angle, one large angle,
both claiming to reach the same target. Ask for a gut read: "Same distance, same nozzle, same
pressure. Two totally different angles. How is that possible — and which one do you call?" Do
not resolve the "how is that possible" yet; that's Anchor 2's job.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with the High Arc — the one that spends six seconds in the
air?" Show of hands, both options, no discussion. Record the count for the Close re-vote.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "Why would two different angles reach the same spot?"**

Let confusion grow. Heroes will want to just compute one angle and stop. Push until someone
notices the range equation is symmetric in a specific way — that $\sin(2\theta)$ takes the same
value at $\theta$ and at $90°-\theta$. If the room reaches "there have to be two answers, not
one" on its own from the math rather than from being told, the case is working.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has the right question, ask them to name the steps before opening Appendix C and
D: derive the nozzle's exit velocity from the rated flow and tip size (feeds D1), solve the range
equation for both angles (D2), verify the components with the Pythagorean identity (D1), compute
hang time and apex height for each (D3), then apply the wind-loss model to find effective GPM on
target for each (D4). Re-ask: "Now that we can see the steps — is our question still the right
one?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix F's two Modeling Assumptions honestly: MA1 (the structure's height, and
therefore the exact target distance, is a stated scenario figure — Ridgeview and this fire are
fictional, even though the collapse-zone rule applied to that height is real) and MA2 (the
wind-drift loss rate per second of flight is a stated illustrative rate, grounded in the real,
qualitative fireground fact that lofted streams lose more water to wind, but not itself a
measured figure). Ask which one is load-bearing for the *comparison* — both are, since a
different standoff distance changes both solved angles, and a different loss rate changes the
margin directly — versus which is closer to a fixed physical constant that isn't really up for
debate (the discharge formula and standard operating pressure, Appendix E, are real and not
assumptions at all).

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D2 as a room (deriving exit velocity, solving both
angles), then split into two desks for D3 and D4 — one computes hang time and apex height, one
applies the wind-loss model to get effective GPM — before reconvening to compare and build D5's
graph.

**Facilitator-only arithmetic note (author's worked design values; confirm against the final
cited numbers in case.md once research runs).**

Tip: 1-3/8 in smoothbore, 80 psi standard operating pressure → rated discharge = 500 GPM
(published smoothbore discharge table value). Derived exit velocity $v = 108$ ft/s (from
continuity: $v = Q/A$). Structure height (MA1, stated) = 150 ft → mandated standoff
$R = 1.5 \times 150 = 225$ ft (real collapse-zone rule applied to a stated height). $g = 32.2$
ft/s².

$\sin(2\theta) = Rg/v^2 = (225)(32.2)/108^2 = 0.6208$, giving $2\theta = 38.37°$ or
$141.63°$, so **Low Arc $\theta = 19.21°$** and **High Arc $\theta = 70.79°$** — a
genuine complementary pair ($19.21° + 70.79° = 90°$).

Apex heights: Low Arc = 19.6 ft; High Arc = 161.5 ft. Time of flight: Low Arc = 2.21 s; High Arc
= 6.33 s — the High Arc spends roughly three times longer airborne.

With MA2's stated wind-drift loss rate (illustrative design value: 2% of flow lost per second of
flight): Low Arc effective flow = 500 × (1 − 0.02 × 2.21) = 477.93 GPM. High Arc effective flow
= 500 × (1 − 0.02 × 6.33) = 436.65 GPM. **Margin = 9.45%, Low Arc ahead on raw hydraulic
efficiency** — close enough that the obstruction-clearance argument for the High Arc is a live,
defensible counter-argument, not a formality.

**Grounding the clearance claim (D3, MA3) — do not let this rest on the apex numbers alone.** A
projectile trajectory returns to height 0 exactly at its own range, so the apex heights above
(19.6 ft / 161.5 ft) describe the *midpoint* of each flight, not the parapet remnant's actual
location. Using the trajectory-height formula $y(x)=x\tan\theta - gx^2/(2v^2\cos^2\theta)$ at the
parapet's stated location (MA3: 12 ft tall, 200 ft from the monitor — 25 ft short of the 225 ft
target): Low Arc height at $x=200$ = 7.77 ft (**below** the 12 ft remnant — blocked). High Arc
height at $x=200$ = 64.01 ft (well above the remnant — clears easily). This is the number that
actually earns the High Arc's clearance argument; an early cut of this case argued clearance from
the apex heights alone, which a sharp room can correctly reject, because the apex is nowhere near
where the parapet actually stands.

## Twist

**The Low Arc wins on the primary metric — but the primary metric doesn't know about the
debris field.** A Hero who stops at D4's 9.45% margin and calls the Low Arc the clear winner has
not yet reckoned with D3: at the parapet remnant's own location (200 ft out), the Low Arc's
trajectory is only 7.77 feet high — below the 12 ft remnant, meaning it is blocked before it ever
reaches the target. The High Arc clears the same remnant with 64.01 ft of trajectory height against a 12 ft
remnant. The twist fires the moment a Hero notices that "more gallons on target" and "actually
gets there at all" are two different questions, and the case's primary metric only ever answers
the first one.

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" A room that voted the same way both times is worth pressing:
did they land on their answer because of the hydraulic margin, or because of the clearance
argument, or both?

## Deep conflict — two threads (20:00–30:00)

1. **Flow efficiency vs. obstruction clearance.** The Low Arc delivers more effective GPM. Is an
   9.45% hydraulic edge worth throwing the stream low through a collapse zone's own debris field,
   or is any clearance risk disqualifying regardless of the flow number?
2. **What the model does and doesn't know.** The primary metric (effective GPM) is entirely
   silent on obstruction clearance — it only knows about wind loss. Is it fair to call the Low
   Arc "the better option" using a metric that was never built to capture the thing that actually
   worries Danny most?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — two angles, no context, gut-check vote |
| 3:00–6:00 | Anchor 1 vote recorded |
| 6:00–9:00 | Anchor 2 — why two angles reach the same spot |
| 9:00–12:00 | Anchor 3 — name the five-step process before opening Appendix C/D |
| 12:00–15:00 | Anchor 4 — surface MA1–MA2, separate real constants from stated assumptions |
| **~15:00** | **TWIST drops** — the 9.45% hydraulic margin vs. the parapet-clearance gap (7.77 ft vs. 12 ft vs. 64.01 ft) |
| 15:00–20:00 | Data Deep Dive — D1–D2 worked as a room |
| 20:00–30:00 | Deep conflict — two threads (flow efficiency vs. clearance; what the model does/doesn't capture) |
| 30:00–40:00 | Data Deep Dive continued — D3–D5 in two desks, reconvene for the shared table and graph |
| 40:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Heroes will solve D4, see the Low Arc win by a margin of 9.45% on effective gallons per minute, and
conclude the choice is settled — missing that the primary metric never measured the thing
Danny's actually worried about (clearing the debris field). The trap is treating "wins on the
metric we happened to build" as the same thing as "wins the decision." A second, subtler trap:
Heroes may assume the two angles are close together (both fairly steep) because they "both reach
the same place" — they are not. The complementary pair can be wildly asymmetric (here, roughly
19.21° and 70.79°), and Socratic Question 2 exists specifically to catch a Hero who assumed otherwise
without actually solving the equation.

**A third trap, at the worksheet level (watch for this while circulating during D3):** a Hero
computes each arc's *apex* height (19.6 ft / 161.5 ft), sees the Low Arc's apex (19.6 ft) clears
the 12 ft parapet on paper, and concludes the Low Arc clears the obstruction too — without
noticing the apex occurs at $x=R/2=112.5$ ft, nowhere near the parapet's actual 200 ft location.
By $x=200$ ft the Low Arc has already descended to 7.77 ft, *below* the parapet. This is an easy,
silent substitution error (apex height is the more natural number to reach for first) that
produces a plausible-looking but wrong D3 answer with no obvious red flag — watch for a Hero who
answers D3's clearance question using only the apex-height table and never actually evaluates
$y(200)$.

## Socratic questions

1. The Low Arc wins on effective gallons per minute by a margin of 9.45%. Is that margin big enough to settle the question by itself — or does it depend entirely on what you think the wind-drift loss rate actually is?
2. Before you solved D2, would you have guessed the two arcs (19.21° and 70.79°) were close together in angle, or far apart? What does that actual gap tell you about how sensitive this equation is to the target distance and the exit velocity?
3. D1 asks you to verify the velocity components using the Pythagorean identity. What would it mean, physically, if that check had *not* come out close to the nozzle's 108 ft/s rated exit velocity?
4. If the structure in Appendix F's assumption were meaningfully taller than the stated 150 ft — and the mandated standoff distance grew with it — would you expect the two solved angles to move closer together or further apart? Why?
5. The primary metric never mentions the collapse zone's debris field at all. Is that a flaw in the metric, or is it fair to expect Danny to weigh D3's clearance finding separately from D4's flow number?

**Facilitator note on Question 4 — a real, documented fragility, not a hidden one.** Question 4 asks
how $R$ moves the two *solved angles*. **If a sharp Hero pushes further and asks whether a taller
structure would change whether the Low Arc clears the parapet, the honest answer is yes, and rather
quickly:** holding MA3's parapet distance fixed at exactly 200 ft (the stated convention — the
parapet does not move just because a hypothetical building is taller), recomputing $y(200)$ as MA1
increases shows the Low Arc's clearance height crosses the 12 ft remnant at approximately
**MA1 ≈ 159 ft** — only about **9 ft (6%) above the case's stated 150 ft**. Above that, the Low Arc
would clear the same parapet it is blocked by at the case's actual stated value. (Verified
2026-08-20: MA1=150→$y(200)$=7.77 ft, blocked; MA1=158→11.63 ft, still blocked; MA1=159→12.13 ft,
clears — see `case.json.modeling_assumptions[MA3].sensitivity`.)

**This is a real, load-bearing fragility, not a defect to paper over — surface it, don't dodge it.**
The Twist's clearance verdict is correct and defensible **at the case's own stated numbers**; it is
also genuinely thin — thinner than D4's 9.45% primary-metric margin, which stays robust across MA1's
full ±50% flex (see `sensitivity_model.py`, Tier 2 P5). If a Hero surfaces this, treat it as a
strong catch, not a threat to the case: it is exactly the "T4 requires stating and defending an
assumption" skill in action, and it is good material for the Deep Conflict block — "the flow margin
is robust, but the clearance margin is not; which one should a real Danny trust more, and why might
that itself argue for the position that leaves the biggest margin for error?"

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes noticed the complementary-angle structure on their own in Anchor 2, or needed a
  direct hint.
- Whether the 9.45% margin was treated as decisive on its own, or whether the clearance argument
  from D3 surfaced without prompting.
- Whether the Pythagorean-identity verification in D1 was treated as a real check or as a box to
  tick before D2.

## Standards Touched On

Pythagorean Identity · Inverse Trigonometric Function · How to verify a trigonometric identity ·
How to solve a trigonometric equation over a given interval · How to evaluate an inverse
trigonometric function · Sine Function · Cosine Function · Reference Angle · Radian · How to
convert between degrees and radians · How to find the percent of a number

## Sensitivity note (SPEC §6)

LOW-MODERATE. This case is set at an active structure fire with a declared collapse zone, which
carries real weight, but the math never asks a student to reason about casualties or injury —
every deliverable is about water delivery and stream geometry (protection framing, consistent
with SPEC §6). Facilitators should still give it a one-line flag before Launch, since "structure
fire, collapse risk" can land heavily for a Hero with a personal connection to fire service or a
past fire experience — keep classroom framing on the engineering decision, not on danger to any
named person.
