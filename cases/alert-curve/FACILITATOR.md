# Guide Notes: The Alert Curve

**Case:** The Alert Curve · **Tier:** T2 · **Band:** MS-core · **Studio:** Heroes Academy
**Standards:** Chain Rule / Product Rule / Tangent Line / Differentiable — see `case.json.standards[]`
for the exact ids.

**Facilitator-only. Do not distribute to students.** Balance argument, margin, and the room's
likely misstep live here and in `case.json`'s `balance` object — never in `case.md`.

**Balance flag, read before you facilitate.** On the primary metric (confirmed real incidents per
false escalation), Curve Check beats Threshold Trip by a `margin_pct` of **14.3%**, computed
directly from Appendix D's 14-row log (see `case.json.balance.margin_note` for the row-by-row
derivation) — inside SPEC §2's ~20% cap. This is a **retune, done 2026-08-29** (case-owner
decision, following the `fret-board` precedent for a genuine retune rather than accepting an
imbalance): Appendix D's log was expanded from an original 6 rows to 14, spanning just over two
shifts instead of one, which produced a genuine but far-too-wide 350.0% margin. The expansion kept
the same construction rule and the same false-positive-rate anchor to [S3]/[S4], preserved the
original twist row (row 5) and the original double-catch-false-alarm row (row 6) verbatim, and
added a Curve-Check-only false-alarm case (a derivative-noise blip, rows 12/14) that the original
6-row log didn't have room to show — a genuine addition, not a fudge, since no detection policy is
actually flawless. Both quantitative arguments below are still real and still hold; the race is
now genuinely close (Curve Check 8/4 = 2.0 vs. Threshold Trip 7/4 = 1.75) rather than a runaway.
Run the discussion below as written — it is deliberately built so the room's real tension is
*speed vs. precision*, a values question — and a sharp Hero who runs the D5 arithmetic correctly
will still land on Curve Check, but by a margin close enough that the room's reasoning, not just
the arithmetic, has to carry the case.

## Intro

Frame the format before anything else: this is a real overnight SOC decision with a live alert on
the board, not a worksheet. Name the opener — "You are Jordan Lee. It's 3 a.m., the queue just
threw a spike, and your cursor is hovering between two buttons. One of them wakes someone up." Let
the stakes land before moving to the Launch.

## Launch

Read the Overview's closing lines aloud, slowly, stopping exactly where the case stops — Jordan's
hand still on the mouse, deciding which tab to click first. Ask: "Escalate now, or wait one more
sampling interval?" Do not let anyone reach for Appendix A yet. Take the temperature of the room on
gut instinct alone.

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Is anyone courageous enough to stand with Jordan on the Curve Check — wait, and risk being the
analyst who let something run loose?" Show of hands, both options, no discussion. Record the
count — Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'accelerating'?"**

Let confusion grow here — this is deliberate. Heroes will want to jump straight to "which policy
catches more attacks," but push on what the case is actually grading: not "which policy ever
catches a real incident" (both eventually do, on this log), but "which policy's escalations are
worth trusting once you account for every false alarm it also raises." If the room lands on "the
real question is a ratio, not a raw catch count" on its own, the case is working as designed.

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room separates "who reacts sooner" from "whose escalations you can actually trust," ask
them to name the steps before touching the appendices: derive dS/dt with the chain rule (D1),
substitute into the product rule to get dA/dt (D2), justify with the definition of differentiable
why the raw count can't do this and A(t) can (D3), build the tangent line at t0 (D4), and only
then classify Appendix D's six past intervals under each policy's own rule to get a real ratio
(D5). Re-ask: "Is our question still the right one, now that we can see the steps?"

**Argument for A — The Threshold Trip.** The raw hourly alert count crossing the threshold
(Appendix C's 500 alerts/hour, MA4) is available immediately, with zero additional delay. For any
interval where a true accelerating attack does trip the threshold, the Threshold Trip policy
escalates it exactly one 5-minute sampling interval (Appendix C, S1) sooner than the Curve Check
policy ever could, since Curve Check requires waiting for that next interval before its derivative
confirmation even exists. On Appendix D's 14-row log, Threshold Trip escalates on 11 of 14 rows and
correctly catches 7 of the log's 8 confirmed real incidents — all but row 5 — every one of them at
least one full sampling interval earlier than Curve Check. Against a published 247-day mean time to
identify and contain a real breach [S2], every interval of head start is real, non-trivial time.

**Argument for B — The Curve Check.** Because A(t) is a product of traffic volume and threat
score, a pure volume spike with a flat or falling threat score can push the raw count over the
threshold without dA/dt ever turning positive. Curve Check's chain-and-product-rule confirmation
filters exactly that case out. On Appendix D's 14-row log, Curve Check's ratio is 8 confirmed
incidents to 4 false escalations (2.0), against Threshold Trip's 7 confirmed to 4 false (1.75) — a
14.3% edge that holds even though Threshold Trip is never slower on a single row of this log. Two
of Threshold Trip's 4 false escalations (rows 4 and 9) are exactly the volume-only-spike failure
mode Curve Check's derivative check is built to filter, and row 5 (410 alerts/hour, never crossing
the threshold at all) is a real incident Threshold Trip's own rule cannot catch under any reading —
not a delay, a miss.

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface the real gaps honestly: Appendix A's three coefficient sets (MA1, MA2, MA3), Appendix C's
threshold (MA4) and current instant (MA5), and Appendix D's entire 14-row log (MA6) are all
stated Modeling Assumptions, not sourced figures — no detection-engine vendor or SOC publishes any
of these internally. Ask which ones actually move the *graded* D5 ratio if they change. The honest
answer, per each assumption's own stated sensitivity: MA4 (the threshold) and MA6 (the log itself)
are both flagged **High** — MA4 is "the single most flip-capable figure in the case," and MA6 "is
what D5's ratio and its percentage margin are computed from directly... a different constructed
log could shift, or even reverse, which policy the ratio favors." MA1/MA2/MA3 (the function
coefficients) mostly change D1–D4's numeric values, not D5's classification directly. Let a sharp
Hero find this themselves before confirming it.

## Data Deep Dive

Now, and only now, the numbers. Walk D1's chain-rule derivation, D2's product-rule substitution,
D3's differentiability justification, and D4's tangent line together as a room, cold-calling for
D2 specifically — this is where a Hero who got D1 right but drops a term substituting it into the
product rule will visibly struggle. That struggle is useful information for the facilitator, not a
moment to rescue.

**Facilitator-only arithmetic note — the D5 ratio, and where the room goes wrong.** Classifying Appendix D's 14 rows
under each policy's own rule: Threshold Trip escalates on rows 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13
(11 of 14) — of those, 7 were later confirmed real incidents (rows 1, 2, 3, 7, 8, 10, 13) and 4
were false escalations (rows 4, 6, 9, 11), for a ratio of 7/4 = 1.75. Curve Check escalates on rows
1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14 (12 of 14) — of those, 8 were later confirmed real
incidents (rows 1, 2, 3, 5, 7, 8, 10, 13) and 4 were false escalations (rows 6, 11, 12, 14), for a
ratio of 8/4 = 2.0. `margin_pct = 100 × (2.0 − 1.75) / 1.75 = 14.3%` — Curve Check wins, but this
time by a margin close enough that a Hero has to actually defend it, not just cite it. **The
trap:** most Heroes will notice that Threshold Trip always catches every real incident at least as
early as Curve Check — since Curve Check can't even evaluate a derivative until it waits a full
sampling interval — and will assume Threshold Trip must therefore also have the better ratio,
because "catching it sooner is strictly better." This conflates *speed* with *precision*. The primary
metric counts every alert a policy raises, not just the real ones it catches, and a policy that
reacts to any volume spike crossing the threshold racks up false escalations exactly where the
threat score never actually moved. A Hero who never sorts Appendix D's log by whether dA/dt was
genuinely positive at the moment of escalation will overstate Threshold Trip's real advantage — and
miss the whole reason Appendix A built A(t) as a product in the first place. A second, subtler trap
this larger log now also supports: rows 12 and 14 are Curve Check's *own* false escalations (a
derivative-noise blip with no real threshold crossing at all) — a Hero who assumes Curve Check is
simply "the careful, always-right policy" will be surprised it has false alarms of its own, just
fewer of them relative to what it catches.

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Row 6 of Appendix D crossed the threshold *and* had a positive dA/dt at confirmation — both
policies escalated it. It turned out to be a false alarm either way. Jordan's shift lead pulls that
row up on screen and says: 'That one cost us nothing to get wrong — no real incident was running.
But look at row 5. Traffic never crossed the threshold at all. Threshold Trip would have sat on its
hands all night. Curve Check paged someone, and it turned out to be real.'"

"Does that change how you weigh the two policies' mistakes — or does the ratio you already computed
already account for it?"

**Facilitator-only: what this actually does, and does not, change.** Row 5 is already inside D5's
computed ratio — it is one of Curve Check's three confirmed catches, and it is exactly the kind of
interval Threshold Trip cannot catch *at all* under its own rule, because the raw count never
crosses 500. The twist does not introduce new data; it re-surfaces a row the room likely skimmed
past and asks them to notice that Threshold Trip's failure mode here isn't a false escalation, it's
a **missed escalation entirely** — a real incident the D5 ratio, as defined (confirmed incidents
per false escalation, among alerts each policy actually raises), does not penalize Threshold Trip
for missing. Ask directly: "Is the D5 ratio, as the case defines it, actually measuring everything
you'd want it to — or is there a failure mode it's blind to?" That is a genuinely open, legitimate
critique of the case's own primary metric, and a Hero who raises it is doing exactly the kind of
thinking SPEC §0's "defensible ambiguity" is meant to reward — even though, as computed, the twist
does not flip which policy wins.

## Immediate recommit

Re-vote immediately. Ask by name: "Does row 5 change your vote — or does it just tell you the ratio
you already computed was measuring the right thing all along?" That distinction is the transferable
skill, not the vote itself.

## Deep conflict — threads (20-30 min)

1. **Speed vs. precision, made concrete.** Threshold Trip is never slower on this log — so why does
   the D5 ratio still favor Curve Check by 14.3%? Push the room to state, in their own words, why
   "catches it sooner" and "catches it more trustworthily" are different claims.
2. **What the ratio doesn't count.** Row 5 shows a real incident Threshold Trip's own rule can
   never escalate on, no matter what — a miss, not a false alarm. Does a metric built around false
   escalations alone fully capture what Jordan's SOC actually cares about, or is there a second
   metric (missed incidents) this case doesn't grade but probably should?
3. **How much data does it take to trust a ratio like this?** Fourteen rows produced a 14.3%
   margin — much closer than the six-row draft this log grew from, which produced 350%. What would
   it take — how many more rows, or what kind of rows — for a Hero to trust that number the way
   they'd trust a result from a much larger dataset? This is the honest place to name MA6's own
   sensitivity note out loud: a different constructed log could still shift, or even reverse, which
   policy wins.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the Overview's closing lines, cold-call for a gut read, no formulas yet |
| 3:00–10:00 | Position defense — *"Convince us Jordan should trust your policy, not just react faster or wait more carefully"* |
| 10:00–15:00 | Pressure-test the models — *"Whose ratio is most fragile if the threshold or the log changes?"* |
| **15:00** | **DROP THE TWIST** — row 5's missed escalation, delivered slowly |
| 15:00–20:00 | Immediate recommit — who reverses, and why |
| 20:00–30:00 | Threaded deep conflict (speed vs. precision; what the ratio doesn't count; a margin this wide on data this thin) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Socratic questions

1. Your D2 gives you dA/dt at t0 as a single signed number — what does its sign alone tell you that the raw alert count at t0 by itself cannot?
2. Suppose two different intervals both cross the threshold in Appendix D — one where traffic volume is spiking and threat score is flat, another where both are rising together. Does your D2 derivative treat those two intervals the same way, and should it?
3. Your D5 ratio for the Curve Check policy has no entry for an interval where a real attack got exactly one sampling interval longer to run before anyone was paged — how do you weigh that cost against the false escalations Threshold Trip is racking up in the same log?
4. If Appendix C's sampling interval were cut in half, what happens to Curve Check's disadvantage of "waiting one more interval" — and does that change which policy your D5 ratio favors?
5. D3 argues the raw alert count itself isn't truly differentiable. If Jordan tried to eyeball "is this accelerating" straight off the raw count, without ever building the continuous model A(t), what mistake would D3's own argument predict he'd make?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's — a room that voted for
B (Curve Check) at Anchor 1 purely on "waiting feels more careful" and stays with B after the twist
for a *different, ratio-and-evidence-based* reason has genuinely moved, even if the vote count
looks unchanged.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the room discovered on its own that the D5 ratio doesn't penalize Threshold Trip for
  missing row 5 entirely, or had to be told outright.
- Whether the speed-vs-precision distinction (Anchor 2) landed as a real reframe or felt like
  semantics until the D5 numbers were on the board.
- Whether a 14.3% margin, on a 14-row log, felt to the room like a genuinely close race worth
  defending, or like the room reached for the raw catch count instead of the graded ratio anyway —
  worth listening for directly, since that confusion is exactly the trap this case is built around.

## Standards Touched On

Chain Rule · Product Rule · Tangent Line · Differentiable

## Facilitator note — assumption sensitivity (Tier 2 probe P5)

The 14.3% margin is real, but it is a **close-race** margin, not a robust one, and you should know
that going in. `cases/alert-curve/sensitivity_model.py` (verified against `case.json.balance`
exactly: base ratios Threshold Trip 1.75 / Curve Check 2.0, margin 14.3%) flexes Appendix C's
threshold (MA4) and each of Appendix D's 14 raw alert counts (MA6) by ±50% one at a time. Nearly
every one of those 15 dials either flips the nominal winner or pushes the margin back past SPEC
§2's 20% cap somewhere in that range — most sharply, raising the threshold by 50% (750/hr) means
Threshold Trip never crosses at all in this log, an undefined/infinite ratio that flips the winner
outright, and a +50% swing on row 5's count (the twist row) alone produces an exact TIE. This is
disclosed, not eliminated: `case.json.sensitivity_disclosure[]` carries a Category-X (proprietary/
inaccessible one-time estimate) entry for all 15 dials, since no SIEM/SOAR vendor publishes a
universal threshold and no real SOC's internal log is public — the same reason MA4 and MA6 are
Modeling Assumptions in the first place, not sourced figures. If a Hero pressure-tests any single
row of Appendix D or the 500/hr threshold, do not treat that as an attack on the case; it is
exactly the intended move, and the honest answer is "yes, that one row can flip it — that's what a
14-row log this close to the cap means." Do not hand over the specific ±50% flip values above
unprompted; let a Hero who runs the sensitivity check themselves discover them.

## Facilitator note — sensitivity (SPEC §6)

Financial-services SOC framing — keep the discussion strictly on the escalation-policy decision
itself. Never let it drift into treating this as a real breach, a named institution, or an actual
security incident; the stakes are a training/operations decision about *when to escalate*, not a
depiction of a real compromise. Routine register, comparable to this project's Key Length case — no
illness, death, or financial hardship to a person is involved, so SPEC §6's stronger sensitivity
handling does not otherwise apply here.
