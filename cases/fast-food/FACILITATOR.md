# Guide Notes: Fast Food

**Case:** Fast Food · **Tier:** T2 · **Band:** MS · **Studio:** Heroes Academy
**Standards:** see `case.json.standards[]` for the exact ids (10 skills — percent, decimal
addition/subtraction, comparison, and one-step / both-sides equations)

Legacy conversion, 2026-08-20, reformatted from the original 2021 case
(`source/Y3/Additional/Fast Food/Guide Notes.docx`) onto the current 11-anchor ladder, and
narrowed from the original's three-way Subway/Papa John's/Sonic pitch to the approved binary
(`cases/_concepts/LEGACY_DILEMMA_LOCKS_2026-08-20.md`). Numbers below are final, from
`case-research` (`RESEARCH_LOG.md`, `case.json.sources[]`/`derived{}`).

**A note for whoever facilitates this one:** the real published figures, taken at face value
(Subway's ~$500K AUV estimate vs. Papa John's own *system-median* $1.1M AUV) produce a lopsided
~98% margin favoring Papa John's — real economics, not a research error, but far outside this
project's 20% balance cap. The case is tuned to model Papa John's first-year revenue at its own
real, disclosed bottom-quartile AUV ($600K) instead of the median, on the stated rationale that a
brand-new Meridian, ID suburban location is a better match for the system's lower-volume quartile.
See `case.json.modeling_assumptions.MA3` and `RESEARCH_LOG.md`'s "balance-test finding" section —
worth reading before a Hero or the room pushes back on why Papa John's revenue estimate looks
conservative next to its own $1.1M headline figure.

## Intro

Frame the format: this is a real household betting real savings on a business neither of them has
run before. Name the opener — "Two franchise packets on the kitchen table. Investors show up in
five days. Which one do Chris and Devin walk in and defend?"

## Launch

(Adapted from the original Guide Notes' video prompt — `https://www.investopedia.com/articles/pf/07/franchises.asp` on franchise risk.) Watch or summarize the video's core warning: once you've
committed franchise-level money, you tend to stick with the business even as it loses money,
because walking away costs more than staying. Ask: "Knowing that, does the *cheaper* franchise or
the *bigger* franchise feel like the safer bet — and are those the same thing?"

## Anchor 1 — Take a stand and vote

**TAKE A STAND AND VOTE. No reasoning yet, just commit.**

"Who pitches Subway? Who pitches Papa John's?" Show of hands, no discussion. Record the count —
Close will ask them to vote again.

## Anchor 2 — What is the problem we're solving?

**"Is this the right question?" · "Is it just as simple as which franchise costs less upfront, or
is there something else to consider?"**

Let confusion grow here, deliberately — this is the original Guide Notes' own move, preserved.
Push on the real tension: a lower start-up cost (Subway) is not the same question as a better
return on that investment (either franchise). Which one should actually drive the pitch?

## Anchor 3 — What is the process?

**"If we go through this process and find the data, how will we decide?"**

Once the room has a working definition of the tradeoff, ask them to name the actual steps: total
the start-up costs (D1), find the operating costs as a percent of revenue (D2), project revenue
and net profit (D3), find break-even in months (D4) and in monthly revenue (D5), then compare
ROI (D6). Re-ask: "Do we agree that's the right process?"

## Anchor 4 — What don't we know?

**"Do we need to make assumptions? Which ones are critical?"**

Surface Appendix C's modeling assumptions (filled by `case-research` for anything Appendix A/B
could not source — e.g. Meridian-specific fixed costs like rent and utilities, which are not
published by either franchisor). Ask which one actually changes the final ROI comparison if it's
off.

## Data Deep Dive

Now, and only now, the numbers. Walk D1–D3's cost/revenue/profit chain together as a room, then
cold-call for D4's one-step equation and D5's both-sides equation specifically — this is where a
Hero who guesses a payback period without actually setting up the equation gets close to the right
number but misses the skill the case is asking for.

**The real figures (`case.json.derived`):**

| | Subway (A) | Papa John's (B) |
|---|---|---|
| Investment midpoint | $367,940 | $585,876 |
| First-year revenue (AUV) | $500,000 | $600,000 (bottom-quartile — see the note above) |
| Net profit, year 1 | $85,500 | $153,600 |
| First-year ROI | **23.24%** | **26.22%** |
| Break-even, months | 51.65 | 45.77 |
| Break-even, monthly revenue | $13,725.49 | $12,352.94 |
| Reserve of the $806,000 ceiling after investment | $438,060 (54.35%) | $220,124 (27.31%) |

**A finding worth surfacing directly, before anyone asks:** Papa John's own *top* of its
investment range ($890,267) is already larger than the group's entire $806,000 capital ceiling —
only the midpoint used in D4/D6 actually fits. Subway's investment range fits comfortably at every
point. Ask: "Does knowing the worst case of one option doesn't fit at all change how confident
you are in a recommendation built on its midpoint?"

## Twist — drop this at ~15 minutes into the discussion

Deliver slowly, with pauses:

"Idaho's minimum wage just went up, effective this year. Your labor cost as a share of revenue
just rose from 30% to 34% for both franchises."

**Facilitator-only: what the numbers actually do** (`sensitivity_model.py`'s `evaluate_twist()`).
Subway's ROI falls from 23.24% to **17.80%** (net profit $85,500 → $65,500; break-even stretches
from 51.65 to 67.41 months). Papa John's ROI falls from 26.22% to **22.12%** (net profit $153,600
→ $129,600; break-even from 45.77 to 54.25 months). **The winner does not flip — Papa John's is
still ahead — but the margin widens from 12.82% to 24.26%, past this project's own 20% balance cap.**
That's the real, disclosed fragility: a genuinely close case can stop being close under one
realistic real-world shock, and the same shock does not hit both options equally, because
Subway's thinner margin had less room to absorb it. Ask: "If you'd already picked Subway for its
safety margin, does a wage hike that shrinks its profit by nearly a quarter change how safe it
actually looks?"

*(A second, non-mechanical talking point for Deep Conflict thread 1: one of the investor families
backing out — dropping committed capital from $275,000 to $125,000 — doesn't move the ROI numbers
at all, but it does mean Papa John's reserve after investment falls from $220,124 to $70,124,
about 10.69% of the new $656,000 ceiling. Worth raising if the room hasn't already found the capital-risk
angle on its own.)*

## Immediate recommit

Re-vote immediately after the twist lands. Ask by name whether anyone's pick changed and why.

## Deep conflict — three threads (20-30 min)

1. **Lower ceiling, lower risk vs. higher ceiling, higher risk.** Subway's smaller bet leaves more
   of the $806,000 in reserve if the first year underperforms; Papa John's larger bet has more
   room to be right. Which failure mode is worse for a family staking real savings?
2. **Whose labor is actually free.** Chris is quitting his job to run this full-time — does that
   change how "break-even" should be read, since his own salary isn't in the cost table?
3. **What ROI leaves out.** A higher first-year ROI on paper says nothing about which brand Chris
   and Devin can actually run well, or want to run for ten years. Should that matter to the pitch?

## 45-minute Socratic plan

| Time | Move |
|---|---|
| 0:00–3:00 | Launch — the franchise-risk video prompt, cold-call for a gut read, no dollar figures yet |
| 3:00–10:00 | Position defense — *"Convince us your franchise is the better bet, not just the bigger number"* |
| 10:00–15:00 | Pressure-test the models — *"Whose ROI number is doing the most work?"* |
| **15:00** | **DROP THE TWIST** — Idaho minimum wage rises, labor cost 30% → 34% for both, delivered slowly |
| 15:00–20:00 | Immediate recommit — did anyone's answer actually change |
| 20:00–30:00 | Threaded deep conflict (risk ceiling vs. floor; Chris's unpaid labor; what ROI leaves out) |
| 30:00–45:00 | Close, re-vote, reflection, lessons learned |

## The trap

Watch for this specific move: a Hero finishes D1, sees Subway's investment is $217,936 lower, and
assumes that the cheaper option must also be the financially better one — most students will stop
right there, write "Subway is the safer, cheaper choice," and never notice that D2-D6's actual ROI
and break-even math say something different. They miss that Papa John's, despite costing more,
returns slightly more per dollar invested. The case's real tension is that "costs less to start"
and "performs better financially" are two different questions that can point in different
directions, and a Hero who never runs the ROI numbers never discovers that.

## Socratic questions

1. Papa John's edges out Subway on ROI by less than 3 percentage points (26.22% vs. 23.24%) — how would you explain to the investor group whether that gap is worth a $217,936 bigger bet?
2. Chris is quitting his job to run this franchise, and his salary never appears in D2's operating costs — should it, and what does leaving it out actually assume about how the business gets staffed?
3. Papa John's real, disclosed system-median revenue is $1.1M/year, but this case models it at $600K, the bottom quartile — why might that be the more honest number for a brand-new Meridian location?
4. D4 gives a break-even point in months and D5 gives one in monthly revenue — if those two answers seem to disagree with each other, what would you check first?
5. Your recommendation (D6) is built on first-year numbers only — what would you want to see about year two or three before you'd actually put your own $806,000 behind this pick?

## Close

**VOTE AGAIN.** "Did we ask the right question at the start?" "What math was new to you tonight,
and how did you actually attack it?" Compare the closing vote to Anchor 1's.

## Lessons Learned

*(To be filled after the first real run — placeholder structure only.)*

- Whether the one-step equation (D4) or the both-sides equation (D5) was where most Heroes
  actually got stuck.
- Whether Heroes noticed Chris's own labor is unpriced in the cost table without a prompt.
- Whether the twist (once finalized) felt like a meaningful reveal or an expected adjustment.

## Standards Touched On

Percent · Equation · Variable · How to find the percent of a number · How to convert numbers to
percents · How to add decimal numbers · How to subtract decimal numbers · How to compare two or
more values · How to solve a one-step equation · How to solve a multi-step equation with a
variable on both sides

## Facilitator note — sensitivity (SPEC §6 subject-matter note, plus a real disclosed instability)

No SPEC §6 content flag required — the stakes are a family business decision involving real
savings, not personal illness, death, or hardship. A guide may still want to note gently that the
case involves a couple betting a large share of their net worth, since a Hero's own family may
have had a similar real conversation.

**A real, disclosed instability, for a facilitator who gets pushed on it.** This case's 12.82%
margin is genuine but thin, and five of its own stated modeling choices (`case.json.
sensitivity_disclosure[]`) are each large enough to flip the verdict or blow past this project's
20% cap under a ±50% swing: `papa_auv` (MA3's bottom-quartile-vs-median choice — the single most
consequential dial), `subway_fixed_monthly` and `papa_fixed_monthly` (MA2's fixed-cost estimates),
and `subway_food_pct`/`papa_food_pct` (the specific point picked inside each brand's real cited
food-cost range). None of this means the case is broken — every one of these is a real, disclosed,
defensible modeling choice, not an invented number — but if a Hero or the room pushes hard on "why
that number and not a different one," the honest answer is that the case's margin genuinely does
depend on these choices, and that is exactly why they are argued for explicitly in Appendix C
rather than picked silently.

## Balance argument (final)

**Argument for A (Subway):** $367,940 midpoint investment — $217,936 less than Papa John's — 37%
less capital at risk on a business the couple has never run. That leaves $438,060 (54.35%) of the
group's $806,000 in reserve versus Papa John's $220,124 (27.31%), and Subway's 23.24% ROI is close
behind Papa John's 26.22%. A modest ROI gap does not have to be worth doubling your exposure.

**Argument for B (Papa John's):** Even modeled conservatively at its own real, disclosed
bottom-quartile system revenue ($600K, not the $1.1M median), Papa John's first-year ROI (26.22%)
still edges out Subway's (23.24%), and its break-even point (45.77 months) is faster than
Subway's (51.65 months) despite the larger bet — a materially larger revenue base dilutes fixed
costs, and a lower combined royalty/marketing burden (11% vs. Subway's 12.5%) compounds the
advantage.

**The margin:** 12.82%, Papa John's ahead, within SPEC §2's 20% cap. See
`case.json.derived` for every figure and `RESEARCH_LOG.md`'s "balance-test finding" for how this
margin was reached — the real numbers, taken at face value with Papa John's system-median AUV,
produced a margin far outside cap, and were retuned (not hidden) by using Papa John's own real
bottom-quartile figure instead, on a stated, defensible rationale.
