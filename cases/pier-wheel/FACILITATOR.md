# Guide Notes: Pier Wheel

**Case:** Pier Wheel · **Tier:** T4 · **Band:** HS · **Studio:** MS Launchpad
**Standards:** see `case.json.standards[]` for the exact ids (9 skills — amplitude, period of a
function, the cosine function, radian, degrees-to-radians conversion, finding amplitude/period of
a sine or cosine function, inverse trigonometric function, evaluating an inverse trig function,
solving a trig equation over a given interval)

**Facilitator-only. Never copy any of this into case.md.**

## Intro

Frame the format before any math: this is a real capital-review recommendation, not a worksheet
with a Ferris wheel stapled on. Name the opener — "Renata has forty minutes, two spec binders
that agree on almost everything, and a board that has never once overridden her memo. Whatever
she writes down, in every way that matters, is the decision." The tension is not "which wheel is
bigger" — it's "which wheel wins on the rule the authority actually uses to decide."

## Launch

Read the Overview aloud, then Background's first two paragraphs — who Renata is, that both
designs are real, already-built reference installations, and that the board asks her to *score*
the two options, not just describe them. Stop before reading the paragraph that states the
per-meter-of-diameter scoring rule. Ask: "Just from what you've heard so far — is 'pick the wheel
with more sunset-view time' obviously the right way to decide this?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Option A (Thames-side, smaller diameter) or Option B (Las Vegas Strip, larger diameter)?" Show
of hands, no discussion yet. Record the count — Close asks again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "What do you mean by 'better design'?"**

Push on what "better design" means here. Better as in more total sunset-view minutes for riders?
Better as in the most efficient use of the capital the authority is putting into steel and
foundation? Those are not the same question, and the case has not yet told the room which one the
board is actually grading. Let the room sit in that ambiguity — "Is anyone courageous enough to
say what 'better' means before we start computing anything?"

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has proposed a working definition of "better," ask them to name the actual steps:
build a height-versus-time function for each wheel (D1), convert each wheel's rotation rate to
radians (D2), graph each function against the qualifying sunset-view height (D3), solve for the
exact interval each option's riders spend above that height (D4), and turn that interval into a
rate — minutes of qualifying view per hour (D5). Re-ask, once the steps are named: "Given how we
just defined 'better' at Anchor 2 — is 'total qualifying minutes per hour' actually the number
that answers it, or could there be another way to state that same rate?" Do not answer this yet;
plant it.

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix E's two Modeling Assumptions as a group, out loud, before anyone computes
anything: the 250 ft / 76.2 m qualifying sightline height (MA1) and the 2 m boarding-platform
clearance (MA2). Ask which one the room thinks matters more to the final answer. (Facilitator
note: MA1 is the load-bearing one — see Sensitivity Note below — but let the room reason about
which is doing more work before confirming it.)

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D4 together as a room.

**Option A** (Thames-side reference): h(t) = 62 − 60·cos(ωt) meters — radius 60 m (half of the
120 m diameter, Appendix A), boarding clearance 2 m (MA2), midline 62 m, period 30 min, ω = 2π/30
rad/min (Appendix D). Solving 62 − 60·cos(ωt) ≥ 76.2 (Appendix C / MA1) gives a continuous dwell
window covering about 12.72 of the rotation's 30 minutes — about **25.44 qualifying minutes
per operating hour**.

**Option B** (Las Vegas Strip reference): h(t) = 81.25 − 79.25·cos(ωt) meters — radius 79.25 m
(half of the 158.5 m diameter, Appendix B), same boarding clearance, midline 81.25 m, same period
and ω. Solving 81.25 − 79.25·cos(ωt) ≥ 76.2 gives a dwell window covering about 15.61 of the
rotation's 30 minutes — about **31.22 qualifying minutes per operating hour**, roughly **18.5%
more** than Option A in raw terms. Option B also carries far more riders per rotation (1,120 vs. 800 rated
capacity, Appendices A/B).

**Stop here and cold-call before revealing D5's second column.** "By total qualifying minutes per
hour, which option wins, and by how much?" Let the room commit to B on the raw number. Then hand
back the paragraph from Background they skipped past at Launch: the authority does not score raw
output, it scores qualifying minutes **per meter of wheel diameter** — because a taller, wider
wheel costs far more than a proportional multiple of a smaller one to build. Divide each option's
raw rate by its own diameter:

- Option A: 25.44 ÷ 120 m ≈ **0.212 qualifying min/hr per meter of diameter**
- Option B: 31.22 ÷ 158.5 m ≈ **0.197 qualifying min/hr per meter of diameter**

On the authority's own scoring rule, **Option A wins** — the same wheel that just lost the raw-
total vote a minute ago.

**The trap:** most Heroes will treat "more qualifying minutes per hour" as self-evidently the
winning number, because it is the bigger, more impressive-sounding figure and because computing
it (D4/D5's raw totals) is the natural stopping point once the trigonometry itself is done. They
will recommend Option B on that basis and never notice that Background already told them the
authority's *actual* scoring rule — a policy detail buried in a paragraph about foundation loads
and steel tonnage, easy to skim past once the trig feels finished and satisfying. Cold-call on
this directly: "You just computed two different numbers for Option B — 31.22 and 0.197. Which one
did the case actually ask you to report, and did you notice there were two?" The trap is not a
trig error; it is stopping the analysis one step early, at the number that feels like the answer
instead of the number Background actually asked for.

## Twist — N/A, justified

This case's tension already turns on reading Background's scoring rule correctly rather than on
new information withheld until mid-discussion; a late reveal would compete with, not sharpen,
that structural read — the whole pedagogical weight already rests on whether the room notices the
per-meter rule, not on a fact nobody had yet. No twist is dropped in the 45-minute plan below for
this reason (see the timed plan's 15:00–20:00 row). A future revision could add a twist where the
board reveals a hard construction-footprint or foundation-load limit that structurally rules out
Option B regardless of score — deliberately not added here so the case's whole weight sits on the
scoring-rule read, per the trap above.

## Immediate recommit

Re-vote immediately after the per-meter score is revealed. "Did the per-meter recompute change
your hand — or did it just change *why* you're holding it up?"

## Close

Re-vote once more after full discussion. Ask: "Did we ask the right question at Anchor 2, or did
'better' turn out to mean something different by the end?" And: "What math was new to you today,
and how did you attack it?"

## Lessons Learned

The case's central move is not a trig trick — it's that two competing, both-legitimate ways to
measure the same physical result (a total rate, and that same rate per unit of the thing that
costs money to build) can rank the same two options in opposite orders. Read only the raw D5
number, Option B wins by 18.5%. Read the number the authority's own capital-review policy
actually asks for, Option A wins by 7.08% — a real but modest margin, not a rout. The
transferable lesson: **when someone hands you a scoring rule, check which number it actually
names before you compute the number that merely looks biggest.**

## Five Socratic Questions

Use these across Anchors 2–4 and the Data Deep Dive — each is answerable only with this case's
own numbers, not general opinion.

1. Option B delivers about 18.5% more total qualifying sunset-view minutes per hour than Option A. If that's true, why doesn't the memo simply recommend B?
2. The authority didn't ask you to maximize qualifying minutes — it asked you to score qualifying minutes *per meter of diameter*. What real cost driver is diameter standing in for, and why would an agency prefer that measure over the raw total?
3. Both options assume a 250-foot qualifying sightline height, and the case tells you that number isn't public record — it's a stated scenario assumption. If the board's engineer had instead set that height higher, which option's score would move more, and why?
4. Both options add the same 2-meter boarding-platform clearance to their midline. Does that assumption change which option wins? Why or why not — what does it actually do to each height function?
5. Your D4 solution should give you two times within one rotation where height equals the qualifying height. What do those two times represent physically, and why does the *later* solution (not the first one you'd naturally compute with a calculator's principal value) matter just as much as the first?

## Standards Touched On

See `case.json.standards[]` (9 ids) and `LEARNING_GOALS.md` for the full deliverable ↔ skill
matrix. In brief: amplitude, period of a function, the cosine function, radian, how to convert
between degrees and radians, how to find the amplitude and period of a sine or cosine function,
inverse trigonometric function, how to evaluate an inverse trigonometric function, and how to
solve a trigonometric equation over a given interval.

## Cohort Bands

See `case.json.cohort_bands[]`.

| Band | Typical size | What changes |
|---|---|---|
| Full | 10-16 | Anchors and the timed plan below run as written |
| Compressed | 5-8 | Anchors 2-3 combine into one pass; the 20:00-30:00 deep-conflict thread drops to one thread (the scoring-rule read) instead of two |
| 1:1 / pair | 1-2 | No vote; Hero states an initial position at Anchor 1. Guide plays devil's advocate directly, pushing the raw-total reading before pointing back to the per-meter rule already sitting in Background |

## Sensitivity Note

Both `sensitivity_model.py`'s FLEX dials are stated Modeling Assumptions, per SPEC.md section 6:

- **MA1 (qualifying sightline height, 250 ft / 76.2 m)** is the load-bearing dial. Flexing it
  changes each option's dwell interval by a different absolute amount because the two options
  have different amplitudes — a taller qualifying height erodes Option B's larger dwell window
  faster in percentage terms than it erodes Option A's, which can narrow or reverse the 7.08%
  margin. Run `python3 sensitivity_model.py` for the exact flip point; do not state it to
  students.
- **MA2 (boarding clearance, 2 m)**, applied identically to both options, has a much smaller
  effect on the margin — it shifts both midlines equally, so it only matters through the
  nonlinearity of the cosine inversion, not as a first-order effect.

## 45-Minute Socratic Plan

| Time | Move |
|---|---|
| 0:00-2:00 | Intro — frame the stakes, no numbers yet |
| 2:00-5:00 | Anchor 1: cold-call launch, 30-second commitments, stand/sit vote — no explanation |
| 5:00-10:00 | Anchor 2: "What do you mean by 'better design'?" — let the ambiguity sit |
| 10:00-15:00 | Anchor 3: name the process (D1–D5); re-ask whether the raw total is really what "better" meant |
| 15:00-20:00 | Anchor 4: surface MA1/MA2 as a group. **No Twist scheduled here or anywhere in this plan — Twist: N/A, justified above; the whole weight of this case rests on the scoring-rule read, not a late reveal.** |
| 20:00-30:00 | Data Deep Dive: walk D1–D4, cold-call the raw-total vote, then reveal the per-meter score and name the trap |
| 30:00-40:00 | Deep-conflict thread: raw output vs. per-diameter capital efficiency as competing decision frames |
| 40:00-45:00 | Close, re-vote, reflection, Lessons Learned |
