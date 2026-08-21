# Facilitator Guide — Insurance Actuary

**Sensitive-subject flag (SPEC §6):** this case touches money stress indirectly (a company's
revenue collapse, layoffs of prior leadership) but its core math is about *classifying risk*,
not human harm — no casualty or mortality optimization here. No special content warning needed
beyond the ordinary "this is about a real company's business decision" framing.

## The balance argument

**Argument for A (discontinue Young, 14–24):** Young drivers carry the single highest per-vehicle
claims rate of the three age classes in the 2019 forecast — Ĉ2,112/vehicle, versus Senior's
Ĉ2,089 and Middle-aged's Ĉ1,866. On a "which class is worst in isolation" reading, Young is the
worst actor, full stop. Cutting Young also removes the smallest, least-established piece of
Safetylife's book (≈226,600 forecast car-years, versus ≈647,700 for Senior) — far less customer
and premium disruption, less political/PR risk for a brand-new CEO. This matches real actuarial
practice: IIHS data shows 16–19-year-old drivers have a fatal crash rate over 3× that of drivers
20+, largely attributed to inexperience (Appendix D, [S1]).

**Argument for B (discontinue Senior, 65+):** Even though Young's own rate is a hair higher in
isolation, Senior carries nearly 3× Young's exposure and the *second*-highest per-vehicle rate of
the three classes. Discontinuing Senior removes ≈Ĉ1.35 billion of forecast 2019 claims cost
(versus only ≈Ĉ0.48 billion for Young) and produces a *lower* blended claims-cost-per-vehicle for
Safetylife's surviving book than discontinuing Young does. Real-world data also backs a genuine
65+ risk threshold: IIHS attributes older drivers' elevated fatal-crash risk to injury severity
and medical complications, not crash frequency (Appendix D, [S2]) — a different, equally real
reason to flag the class.

**The margin — 2.19%.** Option A's remaining book (Middle + Senior) blends to ≈Ĉ1,952/vehicle in
2019. Option B's remaining book (Young + Middle) blends to ≈Ĉ1,910/vehicle. B is lower — better —
by 2.19%. This is a thin, exemplar-quality margin, well inside SPEC §2's ~20% cap: both sides are
genuinely defensible, and the "obvious" read (cut the class with the worst individual rate) does
not match the number that actually drives Kimuni's promise. Full computation:
`cases/insurance-actuary/sensitivity_model.py:evaluate()`.

## The trap

A student computes each age class's own per-vehicle claims rate in isolation, sees Young's rate
is the single highest of the three, and stops there: "obviously cut Young — it's the worst
individually." That reasoning is mathematically incomplete. It answers "which single class looks
worst on its own" and silently substitutes that for "which cut most improves the company's
*remaining* book" — two different questions that happen to have different answers here, because
Senior's much larger exposure means removing it drags the blended average down further even
though Senior's own rate sits a hair below Young's. This is precisely the Guide Notes' own stock
Anchor 2 question: *"Is it just as simple as deciding which group costs the company the most, or
is there something else we need to consider?"* Watch for a Hero who never computes D2 (the blended
remaining-book comparison) at all, and defends A purely off D1's per-class table.

## The twist

**Drop it around minute 15, slowly.** Reveal Appendix B's risk-tier composition breakdown, which
the launch packet includes but most Heroes will not have processed as load-bearing:

> "Senior's Low-risk sub-segment alone — drivers coded ...SL across all three vehicle sizes — is
> **≈488,000 car-years of exposure**. Young's *entire* book, every risk tier combined, is
> **≈659,000 car-years**. Cutting all of Senior throws out a low-risk customer pool almost as
> large as the whole Young age class — drivers who have never filed a High-tier claim. Does that
> change your recommendation?"

And, pointed the other way, for a room that has already swung hard toward B:

> "Young's High-risk tier is **42.0%** of its exposure — the largest High-risk share of *any* of
> the three age classes (Senior's is 33.4%; Middle-aged's is 25.6%). If Young is proportionally
> the riskiest-skewed class even though its blended rate isn't the deciding factor in D2, does
> that change anything?"

**Does it survive the case's own stated assumptions?** Yes, under every reading. The Appendix B
composition numbers are given data (not modeling-assumption-dependent). The operative constraint
that forecloses a "just keep writing the low-risk Senior policies separately" escape hatch is
Background's own framing of Kimuni's plan: one age class is "discontinued entirely — no new
policies, no renewals." The Dilemma itself is posed as a whole-class choice (Young OR Senior),
not a risk-tier-level choice — a Hero reading that framing naturally has no basis to invent a
sub-tier carve-out. (Carbosian law's five-coverage bundling requirement, cited earlier in
Background, is about coverage *types* within one policy, not about which age classes an insurer
may underwrite — it does not itself forbid tier-level selectivity, so it isn't the rule doing the
real work here; the whole-class framing is.) The twist genuinely forces a defended trade-off, not
a technicality.

## Five Socratic questions

1. Your blended-rate comparison favors discontinuing Senior by about 2%. If the trend-continuation assumption behind that forecast is wrong by even 10%, does that 2% edge survive?
2. Young's own per-vehicle claims rate is the highest of the three age classes. Why doesn't that alone make Option A the better financial choice?
3. Senior's Low-risk sub-segment is nearly as large as Young's entire book. If Safetylife cuts all of Senior, what happens to the low-risk Senior customers who have never filed a High-tier claim?
4. Young's High-risk tier is 42% of its exposure — the largest High-risk share of any age class. What would it take for Safetylife to cut only the risk-heavy Young sub-classes instead of the whole age class, and why can't Sofia's team do that under this Dilemma?
5. Kimuni promised the Board a 2% *revenue* increase, not a 2% cost decrease. Where's the gap in that promise, and does either option actually close it?

## Sensitivity note

One stated modeling assumption: `MA1` — the 2016–2018 quarterly trend continues unchanged into
2019 (`trend_continuation = 1.0`). `sensitivity_model.py` flexes this ±50%
(`trend_continuation` ∈ {0.5, 1.5}). Recorded Tier 2 Probe 5 result:

```
base        A metric = 512.33   B metric = 523.53   winner: B   margin 2.2%
trend x0.5  A metric = 528.24   B metric = 539.24   winner: B (unmoved)   margin 2.1%
trend x1.5  A metric = 497.75   B metric = 509.14   winner: B (unmoved)   margin 2.3%
```

B wins under every flex tested — the verdict is stable to how aggressively the 2016–2018 trend is
assumed to continue, and the margin stays in a tight 2.1–2.3% band throughout. (`evaluate()`
reports a scaled reciprocal of each option's remaining-book Ĉ/vehicle rate — higher is better, per
the Probe 5 contract; see `sensitivity_model.py` docstring for why a reciprocal preserves this
case's real percent margin.)

## Anchor ladder (Guide Notes)

### Intro
Display a boardroom image. Frame the format: "You are Sofia Ficonia's team. The Board votes
today." Name the opener: Kimuni is about to pitch a plan neither the Board nor the room has seen
the numbers behind yet.

### Launch
Read the Overview aloud, cold. Stop exactly where the case stops: Sofia's cursor over an unopened
spreadsheet.

### Anchor 1 — TAKE A STAND AND VOTE
"Is anyone courageous enough to stand with cutting Young? With cutting Senior?" No reasoning yet,
just commit. Let confusion and chaos grow: *"Wow, this is a challenging problem."*

### Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?
"Is it just as simple as deciding which group costs the company the most, or is there something
else we need to consider?" "What do you mean by 'costs the most'?" "Is this the right question?"
Let this run long — this is the case's real crux, and Guide Notes explicitly reward a room that
spends real time here before computing anything.

### Anchor 3 — WHAT IS THE PROCESS?
"If we go through this process and find the data, how will we decide?" "If we end up with Young's
rate higher and Senior's total dollars higher, how do we make the final call?" Re-ask: "Is our
question still the right question?"

### Anchor 4 — WHAT DON'T WE KNOW?
"Do we need to make any assumptions to answer this?" Surface MA1 (the 2019 trend-continuation
assumption) here, before the Data Deep Dive — the Hero should name it as a real gap in what
Safetylife knows, not have it handed to them.

### Data Deep Dive
Now, and only now, walk Appendix A and Appendix B.

### Twist
See above, ≈minute 15.

### Close
Vote again. "Did we ask the right question?" "What math was new to you, and how did you attack it?"

### Lessons Learned / Standards Touched On
See the section at the end of this document.

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote on A vs. B — no explanation |
| 3:00–10:00 | Position defense: *"Convince us why it's better, not just fair"* |
| 10:00–15:00 | Pressure-test: *"Whose plan is most fragile if the 2019 forecast is off?"* |
| **15:00** | **DROP THE TWIST** — the Senior Low-risk / Young High-risk composition reveal, delivered slowly |
| 15:00–20:00 | Immediate recommit: who reverses? *"What just broke in your model?"* |
| 20:00–30:00 | Threaded deep conflict: (1) per-vehicle rate vs. blended-book rate as competing metrics; (2) claim frequency (Young) vs. claim severity (Senior) as different real-world risk stories; (3) the unstated gap between Kimuni's *revenue* promise and the case's *cost* data |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Cohort bands

| Band | Size | What changes |
|---|---|---|
| Full | 14–18 | Anchor timings and the 45-minute plan run as written. |
| Compressed | 7–9 | Anchors 2–3 combine into one pass; deep-conflict threads drop from 3 to 1 (pick per-vehicle-vs-blended, it's the case's real crux); runtime shortens proportionally. |
| 1:1 / pair | 1–2 | No vote — Anchor 1 becomes a stated initial position; guide plays devil's advocate directly; the twist still lands but "who reverses" becomes "would you reverse, and why." |

## Lessons learned / Standards touched on

A rate that looks worst in isolation is not automatically the one whose removal helps the most —
exposure size changes the arithmetic. Linear trend forecasting from limited historical data is a
real, standard actuarial technique, and it is also an assumption, not a fact, that must be named
and stress-tested. Skills touched: mean, linear equations from data, percent, ratio (see
`LEARNING_GOALS.md`).
