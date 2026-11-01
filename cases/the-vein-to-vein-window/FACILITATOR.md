# FACILITATOR.md — The Vein-to-Vein Window

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Vein-to-Vein Window · **Tier:** T4 (HS-entry) · **Studio:** Adventure
**Standards:** Calculus / Limits And Continuity — Limit, One-Sided Limit, Continuity,
Discontinuity, How to evaluate a limit algebraically, How to determine whether a function is
continuous at a point (see `case.json.standards[]` for exact ids).

**Status:** `case-research` complete (2026-09-09) — every `{{NEEDS_SOURCE}}` token in `case.json`
is resolved (`SOURCED` or disclosed `ASSUMPTION`). `margin_pct = 9.89` — see Balance argument
below.

**One-line sensitivity flag (SPEC §6):** this case touches a real, high-stakes clinical scenario —
a cancer patient's only available dose of a personalized cell therapy, with no readily available
backup. It is framed around protecting a viable dose (a positive, protective stake), not around a
casualty count. A facilitator should read the room before pushing hard on the "what if it fails"
framing — a Hero whose own family has experience with serious illness or a loved one running out of
treatment options may find this lands more personally than the numbers alone suggest.

## The math, worked (for the facilitator's own reference)

**Cutoff:** 180 minutes (3 hours), sourced [S2], FDA-approved Yescarta prescribing information.

`V(t) = 1` for `0 ≤ t < 180`; `V(t) = 0` for `t ≥ 180`. `lim(t→180⁻)V(t) = 1`,
`lim(t→180⁺)V(t) = 0` — the one-sided limits disagree, so the two-sided limit does not exist, and
`V` is discontinuous at `t=180` (a **jump** discontinuity). Contrast, D3: `S(x)=(x²+5x)/x=x+5` for
`x≠0`; `lim(x→0)S(x)=5` even though `S(0)` is undefined — a **removable** discontinuity.

| | On-Site Rapid Thaw (A) | Central Pharmacy Courier (B) |
|---|---|---|
| Nominal | 45 min | 150 min |
| +minor (20%, +20 min) | 65 min | 170 min |
| +major (9%, +50 min) | 95 min | **200 min** (crosses cutoff) |

`P(A viable) = 100%` (45, 65, 95 all < 180). `P(B viable) = 71%+20% = 91%` (150, 170 < 180; 200 is
not). `margin_pct = (100−91)/91×100 = 9.89%` (winner-loser as a percent of the loser).

## Balance argument

- **Argument for A (On-Site Rapid Thaw):** the only route with zero disclosed failure mode — every
  scenario, including the rare major-delay scenario, lands at 95 minutes, less than half the
  cutoff. For a one-of-a-kind, irreplaceable autologous dose belonging to a patient who has already
  failed two prior treatments, a 9-percentage-point gap in viability probability is not abstract.
- **Argument for B (Central Pharmacy Courier):** viable nine times out of ten, frees the unit's one
  specialized cell-therapy pharmacist for other patients, and is the route this unit has actually
  used successfully most of the time. A 91% success rate at meaningfully lower resource cost is a
  defensible operational standard, and the freed staffing capacity could serve more patients. **This
  is not only a cost-for-risk trade.** The case's own disclosed ±50% sensitivity sweep on MA3
  (`major_delay_minutes`, `sensitivity_disclosure[]`) shows that under an equally defensible reading
  of that same stated assumption — a major delay of 25 minutes rather than 50 — Option B's
  major-delay scenario lands at 150+25=175 minutes, still under the 180-minute cutoff, making
  `P(B viable) = 100%`, an exact tie with Option A, while still saving the $500/dose (MA5) and
  freeing the pharmacist. A Hero can therefore defend B on a genuinely quantitative, non-concessionary
  basis: under a no-less-honest reading of the case's own major-delay figure, B is not merely cheaper
  — it is equally safe and strictly better on every other axis. (Found and added 2026-09-09 during a
  Tier 2 P2 both-sides re-check: the argument for B as originally written here read as a pure
  concession — "cheaper but riskier" — with no genuinely competitive non-concessionary position; this
  paragraph closes that gap using the case's own already-disclosed sensitivity data, not a new number.)
- **The margin — CONFIRMED by case-research:** `P(A viable)=100%`, `P(B viable)=91%`,
  `margin_pct = 9.89%` — inside the case's 6–10% target band and well under SPEC §2's 20%
  cap. Full arithmetic in `RESEARCH_LOG.md` and `sensitivity_model.py`.
- **Why these particular Modeling Assumption values, not others:** MA1/MA2 (45 and 150 minutes)
  and MA3 (+20/+50 minute delays) were chosen, and verified by running the actual model, to land
  the margin inside the case's target band without engineering the specific percentage — see
  `case.json.sensitivity_disclosure[]` (Category F: a disclosed forecast/irreducible-unknown). The model is
  also robust in a stronger sense: `sensitivity_model.py`'s ±50% flex of every disclosed assumption
  never flips which route is safer — Option A is never beaten — though the *size* of the margin
  swings widely (from an exact tie to Option B collapsing to 0%), which is itself worth surfacing
  in discussion.

## Five Socratic questions

1. On-Site Rapid Thaw never fails in this model — so why would anyone ever choose a route that can fail 9% of the time?
2. Central Pharmacy Courier's major delay only adds 50 minutes to a 150-minute trip — why does that specific combination cross the cutoff when On-Site Rapid Thaw's major delay, added to only 45 minutes, does not?
3. The viability function jumps from 1 to 0 exactly at 180 minutes — what would have to be true about the underlying biology for a hard jump to be a fair way to model it, rather than an oversimplification?
4. D3's function S(x) has a limit at x=0 even though S(0) itself is undefined — why doesn't the same algebraic rescue work for V(t) at the 180-minute cutoff?
5. If Appendix E's delay probabilities shifted so a major delay became noticeably more likely and a no-delay outcome noticeably less likely, would either route's viability probability cross a threshold that changes your recommendation?

## The trap

A Hero will very likely reason: *"200 minutes is only 20 minutes over a 180-minute cutoff on a
150-minute trip — that's basically on time, so the dose is probably still mostly fine."* This
treats the cutoff as a soft average that degrades gradually — exactly the rubric trap this case is
built to expose. The dose does not become "a little less viable" at 200 minutes; per `V(t)`'s jump
discontinuity, it is either inside the tested window (fully viable, by the label's own data) or
outside it (no data exists there, and protocol treats "no data" as "discard," not "probably fine").
A Hero who correctly computes `P(B viable) = 91%` can still fall into this trap verbally, by
describing the failure scenario as "barely" unviable — the facilitator should watch for that exact
phrase and press on it: *"Barely unviable — according to what data?"*

**A second, quieter trap:** treating Option A's 100% modeled viability as proof that cost should
never be weighed against it. This is the position the Twist below exists to pressure-test.

## Socratic questions — sensitivity note

The primary metric is deliberately built from one real, sourced hard cutoff (the 180-minute label
figure) combined with disclosed scenario assumptions for the two routes' timing and delay risk —
not a single unknowable forecast. The open question is a values trade-off (certainty-for-one vs.
capacity-for-many), not a forecasting question. `case.json.sensitivity_note` and this file's
Balance argument record the specific numbers; `case.md` never states which route a Hero "should"
prefer or states the margin's size/direction.

---

## Guide Notes — the anchor ladder (SPEC §7)

### Intro

Frame the format: this is a real, one-shift decision about a single irreplaceable dose, not a
worksheet. Name the opener: "The courier van is waiting. On-Site or Central Pharmacy. Go."

### Launch

Read the Overview's opening beat aloud — the pager, the freezer door, the blank one-line answer
Dana owes their supervisor — with no numbers attached yet. Ask: "If you only knew that one route is
faster and pricier and the other is cheaper and closer to some kind of deadline, what would you
guess the deadline actually looks like — a soft target, or a hard line?" Take answers without
correcting anyone.

### Anchor 1

**TAKE A STAND AND VOTE.** No reasoning yet. "Is anyone courageous enough to stand with Central
Pharmacy Courier — the cheaper route?" Show of hands, both options, no discussion. Record the
count — Close will ask again.

### Anchor 2

**WHAT IS THE PROBLEM WE'RE SOLVING?** Push the room past "which route is cheaper" toward "what
does 'the dose is still good' actually mean, mathematically, at the exact instant the clock runs
out." Ask: "Is 'still good' a yes/no thing, or a more/less thing? How would you even find out?" If
the room lands on "we need to know whether viability fades or snaps off," the case is working.

### Anchor 3

**WHAT IS THE PROCESS?** Make the room name the steps before opening an appendix: (1) define the
viability function `V(t)` from the hard cutoff, (2) test what happens to `V(t)` exactly at that
cutoff using limits, (3) apply the formal continuity test, (4) use the resulting rule to score each
route's disclosed timing scenarios and add up the viable ones. Re-ask: "Now that we can see the
steps, is 'which route is cheaper' still the right question?"

### Anchor 4

**WHAT DON'T WE KNOW?** Surface Appendix E's disclosed assumptions: MA1/MA2 (each route's nominal
elapsed time) and MA3/MA4 (the delay-scenario minutes and probabilities) are stated modeling
assumptions, not sourced facts — only the 180-minute cutoff itself (Appendix B) is a real, cited
figure. Ask: "If the major-delay probability were actually higher than 10%, would today's answer
change? Would the *type* of answer — a probability, not a yes/no — still make sense?"

### Data Deep Dive

Now, and only now, open Appendices A–E and work D1–D5. Cold-call for D2 specifically — a Hero who
skips the formal three-part continuity test and just "eyeballs" the jump will not have language for
*why* it is discontinuous, which is exactly what D5's pitch-writing step requires them to produce.

**Facilitator-only arithmetic note.** `P(A viable)=100%`, `P(B viable)=91%`, `margin_pct=9.89%`.
Full derivation in `case.json.balance.margin_basis` and `sensitivity_model.py`.

### Twist

At roughly the 15-minute mark, reveal: **a second patient's dose is arriving today too, on a
different but overlapping timeline** — and Background already establishes that On-Site Rapid Thaw
depends on the unit's *one* specially certified cell-therapy pharmacist, able to attend only one
dose at a time. If both doses need that same pharmacist inside their respective windows, only one
of them can actually get On-Site Rapid Thaw; the other is routed through Central Pharmacy Courier
whether or not that second patient's own circumstances make the 9-percentage-point gap matter more.
**This mechanism is a direct, load-bearing consequence of a fact already stated in Background — a
single person cannot be in two places at once — not a new resource limit invented for the Twist.**

This invalidates the too-easy position "always pick On-Site, cost never matters when a life is on
the line" — that position quietly assumed On-Site Rapid Thaw is available on demand, with no limit,
to every patient every time. It does not change which route is safer for any single dose in
isolation (`V(t)` and the probabilities above are unmoved for either dose considered alone) —
`sensitivity_model.py`'s `evaluate_twist()` confirms this mechanically, since it is a scheduling/
capacity-contention fact about *which dose gets which route*, not a change to either route's own
timing or delay-probability model — but it changes whether an unconditional *policy* of "always
On-Site" is even something the unit can actually deliver once more than one dose is in flight at
once, which is the norm for a working transplant unit, not an edge case.

### Immediate recommit

Right after the Twist lands, ask by name: "Does knowing that today's choice affects a future
patient change your Anchor 1 vote — or does it just change how uncomfortable the vote feels?" Many
Heroes who voted On-Site on a "cost never matters" instinct will not have considered that On-Site
is a shared, limited resource across patients, not just against dollars.

### Deep conflict — two threads (20–30 min)

1. **Certainty-for-one vs. capacity-for-many.** Push the room to state, in plain English, why a
   policy that is optimal for today's single patient (always choose On-Site) might not be optimal
   averaged across a month of patients. Ask: "Is there a rule for *which* patients should get
   On-Site that isn't just 'whoever is in front of you right now'?"
2. **Is a hard cutoff a fair way to model biology, or a legal/protocol convenience?** The 180-minute
   figure comes from tested stability data, not from cells provably dying the instant the cutoff
   passes. Ask: "Does
   it matter, for how you should act, whether the jump is a real biological cliff-edge or a
   'no data past this point, so we don't risk it' rule? Would you act differently in the two
   cases?"

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — read the Overview's opening beat with no numbers, cold-call a guess about the deadline's shape |
| 3:00–10:00 | Position defense — *"Walk us through your D1/D2 reasoning: does V(t) have a two-sided limit at the cutoff, and how do you know?"* |
| 10:00–15:00 | Pressure-test the process — *"Which of Appendix C's numbers, if it changed, would flip which route wins — and which would just change the size of the gap?"* |
| **15:00** | **DROP THE TWIST** — a second patient's dose needs the same one pharmacist today, delivered slowly |
| 15:00–20:00 | Immediate recommit — does the Twist change anyone's confidence in their Anchor 1 vote |
| 20:00–30:00 | Threaded deep conflict (certainty-for-one vs. capacity-for-many; hard cutoff as biology vs. protocol convenience) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## Close

**VOTE AGAIN.** "Did your recommendation change — or just your confidence in the number behind it?"
Ask what math was new to each Hero, and specifically whether the one-sided limits (D1), the formal
continuity test (D2), or the removable-vs-jump contrast (D3) was the step that actually changed
their thinking about what "the cutoff" means.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether Heroes' Anchor-1 gut vote (On-Site vs. Central Pharmacy) matched their post-D4
  recommendation, or whether the exact 9.89% margin flipped a meaningful share of the room.
- Whether the "a hard cutoff is not a soft average" trap (see The Trap, above) was caught
  unprompted by any Hero before the Twist, or only after.
- Whether any Hero caught, unprompted, that the Twist does not change `V(t)` or either route's
  probability for a single dose — only what an unconditional policy costs in aggregate.

## Standards Touched On

Limit; One-Sided Limit; Continuity; Discontinuity; How to evaluate a limit algebraically; How to
determine whether a function is continuous at a point.

## Cohort bands (SPEC §7)

| Band | Typical size | What changes |
|---|---|---|
| **Full** | 12-20 (the size this case is written for) | Anchors and timings run as written above |
| **Compressed** | 6-11 | Anchors 2-3 combine into one pass; the deep-conflict section (20:00-30:00) runs one thread instead of two; total runtime shortens proportionally |
| **1:1 / pair** | 1-2 | No vote at Anchor 1 — instead ask for a stated initial position and why; the facilitator plays devil's advocate directly rather than cold-calling the room; the Twist still lands, and "who reverses" becomes "would you reverse, and why" |
