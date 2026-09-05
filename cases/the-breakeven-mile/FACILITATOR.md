# FACILITATOR.md — The Breakeven Mile

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries no facilitator-only marker by design (see the "Balance argument" guidance in `case-write`
SKILL.md); the balance argument, margin, and sensitivity notes live only here and in `case.json`'s
`balance` object.*

**Case:** The Breakeven Mile · **Tier:** T4 (HS) · **Studio:** Heroes Academy
**Standards:** Statistics And Probability/Algebra — System Of Equations, How to solve a system of
linear equations (see `case.json.standards[]` for exact ids).

**Status:** Redesigned 2026-09-03 from the original calculus/quotient-rule version, which
`case-research` returned as `blocked_needs_redesign` because its load-bearing premise (an
accelerating, mileage-driven depreciation-per-mile curve) does not hold against real data — see
`RESEARCH_LOG.md` for the original search trail and `case.json.redesign_2026_09_03` for what
carried forward. This version uses the concept sheet's own documented fallback: a simple linear
breakeven-mileage model. All figures are sourced or disclosed as Modeling Assumptions; nothing is
open. `case.json.status` is `researched`.

---

## Numbers (for the facilitator's own use — never paste verbatim into case.md)

- Option A (Keys of Her Own): `C_A(m) = 3039 + 0.2303m`
  - Fixed costs: $1,572 insurance + $854 loan interest + $613 registration = **$3,039/year** [S1]
  - Per-mile operating cost: **$0.2303/mile** [S2]
- Option B (The All-App Life): `C_B(m) = 1.50m`
  - Rideshare rate: **$1.50/mile** [S3]
- **Breakeven mileage:** solving `3039 + 0.2303m = 1.50m` gives `m* = 3039 / 1.2697 ≈ 2,393.5
  miles/year`. Below ~2,393.5 mi/yr, The All-App Life is cheaper; above it, Keys of Her Own is
  cheaper, and the gap widens quickly because Option A's per-mile rate is roughly 1/6.5 of
  Option B's (`case.json.derived.cost_ratio_B_over_A_per_mile`).
- **At Renata's own estimated mileage (MA1, 2,760 mi/yr):** `C_A = $3,674.63`, `C_B = $4,140.00`.
  Keys of Her Own is cheaper by **$465.37/year** (`case.json.derived.savings_at_MA1_usd`), an
  11.24% margin — inside the concept sheet's 8–12% target and comfortably under SPEC §2's 20%
  unbalanced-case ceiling. That's **366.5 miles** above breakeven
  (`case.json.derived.miles_above_breakeven_at_MA1`).
- **At the US average mileage (S4, 13,662 mi/yr):** `C_A = $6,185.35`, `C_B = $20,493.00`. Keys of
  Her Own wins by **69.8%** (`case.json.derived.margin_pct_at_national_average`) — a landslide.
  This is intentional and useful for discussion (see Socratic question 4): it shows how fast the
  margin moves once you're well clear of `m*`, and why MA1's own value (not the national average)
  is the number the decision actually rides on.
- **Budget check (MA2, $350/month = $4,200/year cap,** `case.json.derived.annual_budget_cap_usd`
  **):** at MA1's 2,760 mi/yr, both options fit — `C_A` is $306/month, `C_B` is $345/month. Neither
  option is ruled out by the budget at this mileage; the budget becomes binding only if Renata's
  real mileage (or a higher rideshare-rate scenario) pushes either cost past $350/month. This is a
  legitimate "checked and passed" use of MA2, not a decorative constraint — D3 requires the check
  regardless of outcome.

**How this case was retuned to pass the balance test (SPEC §2):** the sourced fixed costs, the
sourced per-mile operating rate, and the sourced rideshare rate are all real, cited figures and are
not adjustable. The only free dial is MA1 (Renata's own mileage), which is — by definition — a
disclosed scenario assumption, not a sourced fact. The original quotient-rule case's MA1 was
11,500 mi/yr (roughly the national-average ballpark); at that mileage, Keys of Her Own wins by
about 67% under the linear model — a landslide, and unbalanced per SPEC §2. Rather than hide that
or force an artificial number, MA1 was revised down to 2,760 mi/yr with an explicit, arithmetic
justification (a compact single-neighborhood route: ~10 mi/workday × 250 workdays + ~260 mi/yr of
errands), which is both a defensible estimate for the narrative given and lands the margin at
11.24% — squarely in the concept sheet's 8–12% target. This is exactly the "retune a constraint,
not hide data" move SPEC §2 asks for, and MA1's sensitivity is itself made a Socratic question
(see below) rather than swept under the rug.

---

## SENSITIVITY FLAG — read before facilitating

This case is built around a low-wage worker (a home health aide) with no financial safety net
making a decision she genuinely cannot afford to get wrong. Per SPEC §6, keep the discussion on
the neutral, computable question — where does the breakeven mileage fall, and where does Renata's
own mileage sit relative to it — not on moralizing about her financial precarity, her employer's
pay, or gig-economy/rideshare-driver labor conditions more broadly. If a Hero pushes the room
toward "she should just get a better job" or similar, redirect to the math: "Set that aside — walk
me through what `m*` actually is, and whether her route puts her above or below it."

---

## Intro

Frame the format: this is a decision Renata has to make in the next twenty minutes, with real
numbers behind both paths, not a story where the "right answer" is obvious from the setup. Don't
open with the math — open with the stakes: a price hold that expires at close today, and a phone
she isn't answering yet.

## Launch

Read the Overview aloud. Pause where the case does — Renata parked in the clinic lot, both tabs
open, clock reading 4:41, touching neither one. Do not reveal Appendix A/B/C's numbers yet, and do
not reveal MA1 (Renata's own mileage estimate) until Anchor 4.

## Anchor 1 — TAKE A STAND AND VOTE

"Is anyone courageous enough to stand with Option A — Keys of Her Own?" Cold-call for a vote, no
reasoning allowed yet. Write the split on the board (e.g., "8 buy / 6 rideshare / 4 unsure").

## Anchor 2 — WHAT IS THE PROBLEM WE'RE SOLVING?

"What are we actually trying to find out here?" Let it get messy before steering. A room that lands
on "which one is cheaper" is close but still vague — push further: cheaper *at what mileage*? The
whole point of Background's two straight-line framing is that the answer depends on a number
(Renata's annual mileage) nobody has stated yet.

## Anchor 3 — WHAT IS THE PROCESS?

"If we had both options' cost formulas, how would we actually decide which one Renata should
pick?" Push for a concrete process, not a vibe: two linear equations, one crossing point, and a
comparison of Renata's own mileage against that crossing point. Re-ask Anchor 2's question once a
process is on the board: "Given this process, is our question still the right one?"

## Anchor 4 — WHAT DON'T WE KNOW?

"What are we assuming? Which assumptions are load-bearing?" Surface, without confirming or denying
yet: how many miles does Renata actually drive in a year? Is the US national average a fair stand-in
for her specific short, local route? Does her monthly budget rule either option out on its own?
Bank these — Anchor 4's questions are exactly what Appendix D's three stated Modeling Assumptions
(MA1–MA3) answer.

## Data Deep Dive

Now, and only now, hand out Appendices A–D. Let Heroes work D1 (the two equations) and D2 (the
algebraic solve for `m*`) before revealing MA1's specific value if they haven't found it themselves
in Appendix D. Expect D2 to land at `m* ≈ 2,393.5` mi/yr. Let the room sit with that number, and ask
where they think Renata's real mileage falls relative to it, before D3's comparison table settles
it.

## Twist

**Drop this at roughly the 15-minute mark**, after the room has worked through D2's breakeven
mileage and D3's comparison table, but before the room has voted a second time.

> "One more thing. RideWise, the source behind Appendix C's $1.50/mile rideshare rate, reports that
> rate as a *national average* — but its own data shows real city-by-city rates from about $0.90 a
> mile in most US cities up to $2.50+ a mile in the highest-cost metros (New York City among them).
> Renata doesn't live in an average metro; she lives in one specific city, and we don't know which
> end of that range she's actually on. Take 60 seconds: at the LOW end ($0.90/mile) and the HIGH
> end ($2.50/mile), holding everything else the same, which option wins, and by how much?"

**What this invalidates:** the comfortable read that D3's 11.24% margin is a fixed, settled number
that closes the question. It doesn't — it was computed at one specific point within a real,
disclosed range, and the two ends of that range don't just move the margin, they **change which
option wins**. At $0.90/mile, `C_B(2760) = $2,484.00` against the unchanged `C_A(2760) =
$3,674.63` — The All-App Life wins, by about 32.4% (`case.json.derived.twist_low_margin_pct`). At
$2.50/mile, `C_B(2760) = $6,900.00` — Keys of Her Own wins by about 46.7%
(`case.json.derived.twist_high_margin_pct`). Nobody in the room, including the case's own author,
knows which end Renata's real city sits closer to — this is a genuine, disclosed unknown, not a
trick with a hidden right answer. The point is not that Option A or B is "really" correct; it's
that a Hero who treated the original $1.50/mile as a fixed fact instead of a national average
standing in for a wide real range was answering a narrower question than the one Renata actually
faces.

**The follow-up (the whole point):** *"You just re-ran the whole comparison twice with one number
changed each time, and got two different winners. What does that tell you about how much
confidence to put in the original 11.24% number — and what would you actually need to find out
about Renata's specific city to resolve it?"* Push the room toward the general skill: a system of
two linear equations is reusable exactly because you can re-solve it with a new input instead of
starting over, and a "national average" source is often standing in for a real range that a
specific case can fall anywhere within — sometimes wide enough to flip the decision either way.

## Close (10 minutes left)

VOTE AGAIN. "Did we ask the right question? Who's changing their answer, and why?" Ask specifically
who moved because of D3's corrected comparison versus who moved because of the Twist's rate change.
Push back on anyone who claims the Twist "proves" the original 11.24% margin was wrong — it wasn't
wrong, it was computed at a stated rate; the Twist just shows how sensitive the picture is to a
rate that was always disclosed as a range.

## Lessons Learned

This case's own math is a clean example of a recurring skill: two straight-line cost models,
correctly built, cross at exactly one point, and everything about the decision — which option
wins, and by how much — depends on where the actual mileage sits relative to that one crossing
point. The comfortable wrong path (named explicitly in the section that follows this one) is
anchoring on a big, official-looking number (the national average) instead of solving for `m*` and
checking the protagonist's own situation against it. The Twist adds a second lesson: a "national
average" rate is a summary of a range, not a fixed fact, and a system of equations built correctly
is reusable — re-solving it with a new input is fast precisely because the method, not just the
answer, was the point.

## Standards Touched On

See `case.json.standards[]` and case.md Appendix G "How To…" list — generated mechanically from
`readmodel/standards_spine.json`, not retyped by hand.

---

## 45-minute Socratic plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch, 30-second commitments, stand/sit vote at Anchor 1 — no explanation |
| 3:00–10:00 | Position defense: "convince us it's cheaper, not just that you'd pick it" |
| 10:00–15:00 | Pressure-test the models: "what number is this whole decision actually riding on?" |
| **15:00** | **DROP THE TWIST** — the rideshare-rate range, delivered slowly |
| 15:00–20:00 | Immediate recompute: who reverses? "What just changed, and in which direction?" |
| 20:00–30:00 | Threaded deep conflict (2–3 named threads: breakeven-vs-average anchoring; fixed-cost risk tolerance; how much a "national average" source can hide) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

---

## Balance argument

**Argument for A (Keys of Her Own).** The fixed costs are real, but they're spread over comparably
few miles once you account for how short Renata's actual route is — and the per-mile cost of
owning is roughly a sixth of the rideshare rate. Past the breakeven mileage `m*` (about 2,393.5
mi/yr), every additional mile she drives costs six times less to own than to ride-share, and her
own estimated mileage clears that bar comfortably (2,760 mi/yr), putting Keys of Her Own about 11%
cheaper for her specific situation.

**Argument for B (The All-App Life).** Zero fixed-cost exposure: a light week costs almost
nothing, and there's no loan or insurance bill sitting there whether or not she drives. If Renata's
actual mileage is lower than she thinks — say her route shrinks, or she picks up fewer errand
trips — The All-App Life's cost drops right along with it, while Keys of Her Own's $3,039 fixed
floor never moves. Below `m*`, staying car-free is unambiguously cheaper, and the margin near `m*`
is thin enough (11.24% at her own estimate) that a meaningfully wrong mileage guess could flip the
answer entirely.

**The margin.** `margin_pct = 11.24` at MA1 (2,760 mi/yr), computed as `(C_B − C_A) / C_B`.
Breakeven mileage `m* ≈ 2,393.5 mi/yr`. Both values are final — no further sourcing is needed for
either.

---

## Five Socratic questions

1. "You solved for a breakeven mileage `m*` around 2,393.5 miles a year. Does the gap between the two options grow the further you get from `m*`, or stay about the same?"
2. "Your D2 solve used substitution or elimination on the system from D1. What would go wrong if you tried to find `m*` just by plugging in a few guesses for `m` until the two costs looked close?"
3. "Renata's own mileage estimate (2,760 mi/yr) is only about 366.5 miles above breakeven. If her route actually adds up to 3,500 miles a year instead, does Keys of Her Own still win, and by roughly how much?"
4. "At the US national average mileage (13,662 mi/yr, Appendix D), Keys of Her Own wins by nearly 70% instead of 11%. Why does the margin grow so much faster than the mileage does?"
5. "Both options fit under Renata's $350/month budget at her own estimated mileage. Does that mean the budget number doesn't actually matter to this decision? What would have to change about her situation for the budget, rather than the breakeven point, to be the deciding constraint?"

---

## The trap

A Hero compares Option A's total cost and Option B's total cost at one arbitrary mileage — most
often the US national average from Appendix D (13,662 mi/yr), since it's the only "official"
looking number on the page — instead of first solving for the breakeven mileage `m*` and checking
where Renata's own route actually falls relative to it. Using the national average produces a
technically correct but wildly overstated margin (nearly 70%) that has nothing to do with Renata's
actual situation, and a Hero who anchors on it will badly misjudge how close this decision really
is for her specifically. The entire point of D1–D2 is to find the mileage that actually matters
(`m*`) and D3 to test it against Renata's real numbers, not a generic national one.

---

## Sensitivity note

The case's outcome is sensitive to MA1 (Renata's own mileage estimate) more than to any sourced
figure: the margin swings from 0% at `m* ≈ 2,393.5 mi/yr` to about 70% at the national average
(13,662 mi/yr) — a huge range for one disclosed, unsourced assumption. This is disclosed openly in
`case.md`'s Modeling Assumptions block (MA1's sensitivity row) and is the intended discussion
lever, not a flaw to paper over. MA2 (the $350/month budget) and MA3 (0 days left on the hold) are
both far less sensitive at MA1's value — MA2 doesn't bind either option at 2,760 mi/yr, and MA3 is
fixed by the Overview's own narrative, not a lever at all. See `sensitivity_model.py` in this
case's directory for a runnable ±50% flex of MA1 (Tier 2 Probe 5).
