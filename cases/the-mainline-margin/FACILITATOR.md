# FACILITATOR.md — The Mainline Margin

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — see the
guard comment at the bottom of case.md.*

**Case:** The Mainline Margin · **Tier:** T2 (MS-core) · **Studio:** Heroes Academy
**Standards:** Advanced Operations/Variables — the full 11-skill group (see `case.json.standards[]`
for exact ids).

**Status:** Researched. `case-research` ran on 2026-09-01: all 23 NEEDS_SOURCE tokens are
resolved (15 SOURCED, 7 stated Modeling Assumptions, 1 DROPPED as decorative). See
`RESEARCH_LOG.md` for the full trail and `case.json`'s `sources[]` / `modeling_assumptions[]` for
the structured record.

## Argument for A — The Lean Main

The smaller-diameter PVC mainline costs less per foot and weighs less per foot than the wider
option, so it wins outright on up-front material spend before any reimbursement or operating cost
is even considered — the option that looks cheapest on the purchase-order line alone, and the one
a bid built purely on sticker price would favor. If its design velocity stays under NRCS Code
430's ceiling at the farm's actual required flow rate, this is a legitimate, defensible pick: lower
capital cost, and Denise's bid clears the competing contractor's number more easily on the
front end.

## Argument for B — The Margin Main

The next-size-up PVC mainline keeps flow velocity comfortably under NRCS Code 430's ceiling and,
because Hazen-Williams friction loss scales with roughly the diameter's −4.87 power, cuts the
pipeline's friction loss — and therefore the pump's total dynamic head and annual energy cost —
enough (from ~$229/yr down to ~$56/yr) to beat the Lean Main on TRUE cost alone, with zero subsidy
counted, by a real if thin ~1.3%. It also earns a much larger per-pound EQIP reimbursement, since
Practice 430 pays by weight installed — which is what turns that thin 1.3% true edge into the
~50.3% gap that actually shows up on Denise's bid. Most importantly, if the Lean Main's velocity
crosses Code 430's ceiling, its EQIP reimbursement is forfeited in full, not reduced — turning the
"cheaper" option into the one that actually costs the client more once certification risk is priced
in. Neither option is a free lunch: the Margin Main's higher material cost and higher farmer co-pay
are real out-of-pocket costs regardless of the reimbursement rate.

## The margin — REFRAMED 2026-09-01: two figures, not one

**This case now grades on TWO explicit metrics instead of blending them into one number.** See
RESEARCH_LOG.md's dated addendum for the full narrative; the short version:

- **PRIMARY metric — TRUE (subsidy-free) cost per acre-inch.** Material + labor + pump energy
  only, NO EQIP reimbursement term. This isolates real engineering efficiency.
- **SECONDARY metric — NET-OF-SUBSIDY cost per acre-inch.** The same cost, minus each option's
  EQIP Practice 430 reimbursement (forfeited entirely on failed certification, Appendix E). This is
  what actually shows up on Denise's bid.

**Winner: B — The Margin Main, under BOTH metrics.** But the two metrics do not agree on the size
of the gap:

| | Option A (Lean Main) | Option B (Margin Main) |
|---|---|---|
| Velocity at 440 GPM | ~4.99 ft/s — **PASSES** (ceiling 5.0, ~0.16% to spare) | ~2.81 ft/s — **PASSES** |
| Installed cost (material + labor) | $39,732 | $42,636 |
| Annual pump energy cost | ~$229.23/yr | ~$56.47/yr |
| **TRUE annualized cost (PRIMARY, no subsidy)** | **~$2,215.83/yr** | **~$2,188.27/yr** |
| EQIP reimbursement | ~$13,369 (certifies) | ~$23,173 |
| **NET-OF-SUBSIDY annualized cost (SECONDARY)** | **~$1,547.38/yr** | **~$1,029.63/yr** |
| **Margin (B's advantage)** | — | **TRUE: ~1.3% · NET-OF-SUBSIDY: ~50.3%** |

**Why this matters — this is the case's real twist.** Stripped of the EQIP subsidy entirely, the
Margin Main's energy savings barely beat the Lean Main's lower material cost — a genuine ~1.3%
engineering toss-up, not a landslide. The ~50.3% gap that shows up on Denise's actual bid is real
money, but roughly **49 of those 50.3 percentage points come from the subsidy formula itself** —
EQIP Practice 430 pays per pound of pipe installed, so the heavier Margin Main earns a much bigger
reimbursement (~$23,173 vs. ~$13,369) regardless of which pipe is actually more efficient to buy and
run. A Hero who reports only the net-of-subsidy number has correctly priced Denise's bid but has
not noticed that the number is doing something closer to "which pipe weighs more" than "which pipe
is the better engineering choice." (For the record: this reframe is a metric-framing change only —
it does not touch NRCS Code 430 certification, MA1's 440 GPM, MA3's 88 acres, or any sourced figure
S1-S12. The prior 50.3%-vs-~20%-target discussion, the MA1/MA3 retune history, and the
`balance_test_waiver` are preserved in case.json/RESEARCH_LOG.md for the record — they now describe
the SECONDARY metric, not the case's primary grading metric.)

**The lever that flipped:** the farm's design flow rate (MA1) previously sat ~2% *over* the Lean
Main's certified maximum of ~440.7 GPM (causing the forfeiture and the 115.8% margin); it now sits
~0.16% *under* that same cutoff (440 GPM), so Option A certifies. Either way, the certification
question stays genuinely close and non-obvious — that closeness, not which side of the cliff MA1
lands on, is the point of D4 and D6, and is worth naming explicitly in discussion (see Socratic
question 3 below).

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: a real bid with two ways to lose (fail certification, or lose on price), not a
worksheet. Name the opener: "You are Denise Okafor. Two pipe sizes circled on a spec sheet. A
competing bid face-down on the tailgate. You haven't written anything under either one yet."

### Launch

Read the Overview aloud, stop at "doesn't write anything under either one," and ask: "Before any
numbers — a cheaper pipe that might fail a government inspection, or a pricier pipe that definitely
passes. Which risk would you rather carry into a bid?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with the Lean Main — cheaper, but close to the line?" Count
hands. "And the Margin Main — pricier, but safe?" Count hands. Record the split.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump to "which pipe is cheaper" — push instead: "Is this
actually a question about price, or about what happens to the price if a design fails
certification?" The room should arrive at "we need one expression that already has the
reimbursement forfeiture risk built in" before Anchor 3.

### Anchor 3 — What is the process?

Walk the room toward: build each option's total-annualized-cost expression (D1), substitute the
farm's real numbers (D2), simplify and combine like terms (D3), run the exact certification check
(D4), rearrange Hazen-Williams to explore a diameter-for-energy-cost trade (D5), then find the
break-even flow rate and recommend (D6).

### Anchor 4 — What don't we know?

Surface honestly: the farm's design flow rate (MA1) is a stated scenario assumption, not a public
figure — and it happens to sit only ~0.16% below the Lean Main's certified maximum. Ask: "Which
number in this case, if it moved by less than 1%, would change the entire recommendation?" (Answer:
MA1 — see the Twist.)

### Data Deep Dive

Walk D1 through D6 together, building BOTH figures each time, not one blended number. Reveal the
real velocity results (~4.99 ft/s vs. ~2.81 ft/s against a 5.0 ft/s ceiling), then both cost tables:
TRUE cost (no subsidy) $2,215.83/yr for A vs. $2,188.27/yr for B, a ~1.3% margin; then NET-OF-SUBSIDY
cost $1,547.38/yr for A vs. $1,029.63/yr for B, a ~50.3% margin. Cold-call specifically for whether a
Hero ran D4's exact one-step-equation check rather than eyeballing "440 vs. about 440" as "close
enough to certify," AND whether they noticed the two margins (1.3% vs. 50.3%) don't match before
you say so out loud.

### Twist — Part 1: the certification cliff

Reveal that the farm's design flow rate (MA1, 440 GPM) sits only ~0.16% below the Lean Main's
certified maximum (~440.7 GPM) — close enough that a slightly different, equally plausible farm
(a few more irrigated acres, a slightly higher per-acre design rate) would push the Lean Main over
the ceiling and forfeit its entire EQIP reimbursement outright. Ask: "If Denise's own farm turns out
to need even 1% more flow than she assumed, what happens to her whole recommendation for Option A —
not just its cost, but its eligibility?" This invalidates the reading that Option A is a safely
cheaper choice — it shows the two options are exposed to genuinely different kinds of risk (a
cliff-edge eligibility risk for A vs. a smoother cost picture for B).

### Twist — Part 2: the subsidy is doing almost all of the work

This is the case's real twist, and it should land second, after Part 1: ask the room to recompute
both options' cost WITHOUT the EQIP reimbursement term at all — just material, labor, and energy.
That true, subsidy-free gap is only **~1.3%**, not 50.3%. Ask directly: "You just computed two
different margins for the same two pipes. Why are they so different, and which one is Denise
actually being paid on?" Land the mechanism explicitly: EQIP Practice 430 reimburses **by the pound
of pipe installed** (Appendix E), not by efficiency — so the heavier Margin Main earns a
reimbursement roughly $9,800 bigger than the Lean Main's, regardless of which pipe is actually the
better engineering choice. Roughly 49 of the 50.3 percentage points in the net-of-subsidy gap come
from that subsidy formula, not from real efficiency. Ask: "If you were only handed the net-of-subsidy
number — the one that shows up on the bid — would you have known you were being nudged by a subsidy
formula rather than by which pipe is actually better?" This does not reverse the recommendation
(B still wins on both metrics) — it reframes *why* B wins, and by how much a government payment
formula, rather than physics, is responsible for the size of that margin.

### Close

Re-vote. "Did we ask the right question at Anchor 2? Was this ever really about which pipe is
cheaper, or about which pipe is cheaper *and eligible* — and once you strip the subsidy out, how
much of 'cheaper' was ever really about the pipe at all?"

### Lessons Learned

- An all-or-nothing eligibility rule (Code 430's forfeiture condition) can make a "cheaper" option
  the more expensive one in expectation — the pitfall is stopping at sticker price.
- A design margin of 0.16% is not the same as "safely certifies" — D4's exact check exists
  precisely because eyeballing a close call is unreliable.
- EQIP's pay-by-weight structure means the cheaper, lighter pipe also earns a smaller
  reimbursement — two effects that look independent on the spec sheet actually compound in the
  same direction against the Lean Main.
- A subsidy that pays by weight, not by efficiency, can manufacture almost the entire "gap" between
  two options on paper (~49 of ~50.3 points here) — the true, subsidy-free efficiency gap (~1.3%)
  is a genuinely different, much smaller number, and a recommendation that never separates the two
  has quietly let a government payment formula do the deciding instead of engineering judgment.

### Standards Touched On

Advanced Operations/Variables — Variable, Constant, Coefficient, Term, Like Terms, Distributive
Property, and the 5 how-to equation-solving/evaluation skills (see `case.json.standards[]`).
`new_coverage[]` is empty by design — see the reinforcement note above and in `case.json`.

---

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchor 2). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — what's real, sourced Code 430 physics vs. a stated scenario flow rate. |
| 15:00–25:00 | Data Deep Dive — D1–D6 together, reveal BOTH margins: ~1.3% true vs. ~50.3% net-of-subsidy. |
| **25:00** | **DROP THE TWIST, TWO PARTS** — (1) MA1's 0.16% cliff-edge certification margin; (2) the subsidy formula alone explains ~49 of the ~50.3 points, delivered slowly. |
| 25:00–30:00 | Immediate recommit — who reverses? "What just broke — the cost comparison, the certification, or your trust in which number was the 'real' one?" |
| 30:00–40:00 | Threaded deep conflict, three named threads: (1) sticker price vs. all-or-nothing reimbursement risk; (2) a smooth 50.3% net-of-subsidy gap vs. a cliff-edge eligibility risk; (3) the ~1.3% true efficiency gap vs. the ~50.3% number that actually lands on the bid. |
| 40:00–45:00 | Close, re-vote, Lessons Learned. |

---

## Socratic questions

1. Your D1 expression for each option includes a term for the EQIP reimbursement. What happens to that term — not just its value, but its very presence in the expression — if a design's velocity crosses Code 430's ceiling?
2. The Lean Main costs less per foot and weighs less per foot than the Margin Main. Does "weighs less" cut in the same direction as "costs less" once you look at how EQIP actually pays out, or does it work against the Lean Main in a way the sticker price alone doesn't show?
3. Your D4 certification check gives each option a maximum flow rate before it crosses the velocity ceiling. How much margin does each option actually have between that maximum and the farm's real required flow rate — and does either option's margin look uncomfortably thin?
4. Your D6 break-even point tells you the flow rate at which both options cost the same. Is the farm's actual required flow rate close to that break-even point, or far from it — and what does that tell you about how confident Denise should be in her recommendation?
5. If the farm's required flow rate turned out to be somewhat higher than Appendix A states, which option would that change hurt more — the one with less certification margin, or the one with a thinner cost advantage?
6. D1 asks you to build a true (subsidy-free) expression and a net-of-subsidy expression for each option. Once you evaluate both, the two margins between the options are very different sizes. What has to be true about EQIP's payment formula for that to happen — and does it change which option Denise should recommend, or only how she should explain the size of the gap?

## The trap

Heroes will compare the two options' material cost per foot directly — the number printed on the
distributor's price sheet — and conclude the cheaper number is the better spec. That comparison
silently ignores two things Code 430 and EQIP both make load-bearing: a design that fails the
velocity ceiling forfeits its entire reimbursement, not a prorated share of it, so "cheaper per
foot" can flip to "more expensive once you're paying for a design that doesn't certify"; and EQIP
pays by weight, not by sticker price, so the cheaper pipe also earns a smaller reimbursement,
narrowing exactly the gap the trap assumes is wide. A Hero who never runs D4's certification check
against the farm's real required flow rate has not actually found out whether the "cheap" option is
even eligible for the reimbursement its own cost expression assumes.

**A second, subtler trap (the reframe's twist):** a Hero who builds ONLY the net-of-subsidy
expression (D1(ii)) and reports its ~50.3% margin has a correct answer to "which bid number wins,"
but not to "which pipe is actually the better engineering choice" — and may not even notice the
difference, because nothing in a single blended cost figure flags that ~49 of its ~50.3 percentage
points come from a per-pound payment formula rather than from material cost or energy efficiency.
The case now requires D1(i)'s true, subsidy-free expression specifically so that gap cannot hide.

## Sensitivity note

Confirmed, not just anticipated: Appendix A's design flow rate (MA1, a stated Modeling Assumption,
retuned 2026-09-01 to 440 GPM — no citable "typical mainline design flow" figure exists for a
specific fictional farm) sits only ~0.16% below the Lean Main's certified maximum of ~440.7 GPM.
This single figure flips Option A from disqualified to certifiable, and — because Code 430's
forfeiture rule is all-or-nothing — that flip alone is responsible for most of the swing from the
case's original ~115.8% margin down to the ~50.3% net-of-subsidy margin (now the SECONDARY metric).
This is exactly the kind of single load-bearing figure SPEC §5's Modeling Assumptions discipline
exists to surface honestly rather than bury: MA1's table row in case.md marks its sensitivity as
HIGH for this reason. **Since the 2026-09-01 reframe, MA1's certification-cliff sensitivity applies
to the SECONDARY (net-of-subsidy) metric and to D4, not to the case's new PRIMARY metric** — the
true, subsidy-free cost comparison has no reimbursement term, so it computes the same ~1.3% margin
regardless of which side of MA1's certification cliff the Lean Main lands on. `case-qa` should
confirm this note, and the primary/secondary split, stay consistent with whatever numbers ship.

**A second, separate fragility — expected, given how thin the primary margin already is.** Tier 2
probe 5 (2026-09-01, `±50%` flex) found that dropping either MA1 (design flow rate) or MA5 (annual
operating hours) by 50% flips the PRIMARY metric's winner from B to A. Re-deriving the actual flip
points in `sensitivity_model.py` shows the case doesn't even need a swing that large: MA1 flips the
primary winner at only about **-5.9%** (440 → ~414.0 GPM), and MA5 flips it at about **-16.0%**
(1,200 → ~1,008.6 hr/yr). Neither figure is fictional or unresearchable — both are real, sourced
Modeling Assumptions (Appendix A) — so this isn't a case of an unknowable dial driving the result.
It's the flip side of the coin the reframe itself surfaced: once the EQIP subsidy is stripped out,
Option B's win over Option A comes down to Hazen-Williams's steep diameter sensitivity (~diameter^
-4.87) just barely outweighing its higher material cost. A margin that thin (~1.3%) is *supposed* to
be this touchy to its own inputs — a verdict this close to a coin flip that DIDN'T move under a
reasonable swing in flow rate or operating hours would be the surprising result, not the other way
around. Treat this as confirmation of the "genuine engineering toss-up" framing in the margin
section above, not as a defect to fix by retuning MA1/MA5 — SPEC §2/MCS-26 calls for disclosing an
unstable verdict, not eliminating it when the instability is itself informative. See
`case.json.sensitivity_disclosure` for the full documented entries.

## Facilitator note — sensitivity (SPEC §6)

NONE. This is routine agricultural-engineering and cost-share economics — no protected-subject
flag applies, per the approved concept sheet.

## Facilitator note — new_coverage status (flag for human review)

This case's `new_coverage[]` is empty. Verified live against `readmodel/standards_spine.json` on
2026-09-01: all 11 claimed skills already have coverage elsewhere in the corpus (n ranging from 1
to 10); none is at n=0. The concept sheet's own description — "closing all five of the group's
n=1 skills" — is accurate on its own terms (five of the eleven do sit at n=1 today and this case
would move them to n=2), but SPEC §4/§7's `new_coverage[]` field is specifically the n==0 test, not
an n==1 test. See `case.json.reinforcement_note` and `LEARNING_GOALS.md` for the full detail. This
case was written per explicit instruction with locked content regardless of this finding; whether
to accept it as a documented reinforcement case (a SPEC deviation requiring a DOCTRINE_LEDGER row),
fold in a genuinely n=0 skill to legitimize `new_coverage[]`, or shelve it, is a decision for a
human, not this write pass.
