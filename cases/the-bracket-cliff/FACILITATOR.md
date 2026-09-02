# FACILITATOR.md — The Bracket Cliff

*Facilitator-only. Do not paste any of this into case.md's student-facing appendices — case.md
carries a single, self-contained marker comment for this by design (see the "Balance argument"
guidance in `case-write` SKILL.md); the balance argument, margin, and sensitivity notes live only
here and in `case.json`'s `balance` object.*

**Case:** The Bracket Cliff · **Tier:** T2 (MS-core) · **Studio:** MS Adventure
**Standards:** Calculus/Limits And Continuity — Limit, One-Sided Limit, Continuity, Discontinuity,
How to evaluate a limit algebraically, How to determine whether a function is continuous at a
point (all 6 group skills; see `case.json.standards[]` for exact ids).

**Status:** Researched 2026-09-01. All 21 `{{NEEDS_SOURCE}}` tokens are resolved — 17 sourced
(`case.json.sources[]` S1–S16, one FPL vintage explicitly disclosed as a discrepancy rather than
picked), 4 disclosed as Modeling Assumptions (MA1–MA4, Appendix E — Priya's state is illustrative,
not a real named state). `margin_pct` = **7.74**, winning option = **A (Hold The Cliff)**. See
"Facilitator note on the margin" at the bottom for the full computation — it is a genuinely close
call, not a landslide, and it is population-independent (robust to MA1/MA2's scale assumptions).

---

## SENSITIVITY FLAG — read before facilitating

This case touches real, current (2026) federal health-policy and budget debate: the ACA premium
tax credit's reinstated 400%-FPL subsidy cliff, and the CBO's real federal cost estimate for
removing it. **Keep the discussion on the neutral, computable question** — does this real cost
function have a jump discontinuity, how large is it in dollars, and what does making it continuous
actually cost — **not on which federal or state policy position is correct.** If a Hero pushes the
room toward a partisan framing ("the government should/shouldn't fund this"), redirect to the math:
"Set aside what should happen politically — walk me through what the two one-sided limits actually
are, and what Build The Bridge would cost to make them agree." No real state currently extends
smoothing above 400% FPL; be explicit that Build The Bridge is a policy option grounded in real
state precedent for *lower* income bands (Appendix D), not an already-existing above-400%-FPL
program anywhere.

---

## Balance argument (qualitative — pending research)

**Argument for A (Hold The Cliff).** Zero direct state cost, zero new administrative rule — the
exchange just applies the federal formula as published. The real jump discontinuity found in D1/D2
is real and provable, but it is a cost borne by affected households, not by the budget line Priya
is accountable for. Administrative simplicity and budget preservation are the genuine, quantifiable
case for A.

**Argument for B (Build The Bridge).** Provably continuous at the threshold (D3 passes where D1/D2
failed) — real, defensible math, not a matter of opinion. Real state precedent (New Mexico fully
replacing the lost federal enhancement, Massachusetts's named dollar addition, California's named
dollar program) shows other states have judged this kind of fix worth funding. But the CBO's
federal-scale estimate and the real single-state costs in Appendix D show it is a genuine, ongoing
budget line, not a costless fix — B's strength is that it's mathematically clean, not that it's free.

**The margin (computed — see full derivation at the bottom of this file).** Per household near the
threshold: the D1/D2 discontinuity is **$8,756** ($14,931 unsubsidized − $6,175 subsidized,
Appendix B, S3) and Build The Bridge's real per-household cost is **$9,491** (Appendix C's 8.5% cap
applied to the same $64,000 household: $14,931 − $5,440 = $9,491). Build The Bridge costs
**7.74% more** than the harm it removes — a real but modest margin, favoring **A (Hold The
Cliff)**. This ratio is population-independent: the state-scale estimate in Appendix E (MA1/MA2)
multiplies both the harm total and the cost total by the same factor and cancels out of the
margin, so the ~20% SPEC §2 cap check only needed to look at the per-household ratio, not the
state-scale numbers (which are themselves the shakiest, least-sourceable part of the case, by
design — see MA2). Separately, and more decisively for D5's practical recommendation: Appendix E's
one-time $8M discretionary line item (MA3) cannot fund an ongoing, state-scale wraparound program
regardless of the cost-effectiveness math — real per-state wraparound programs run $38.8M–$300M/yr
(Appendix D). A Hero who reasons only from the harm-vs-cost margin and ignores the funding-
mechanism mismatch has not actually engaged with Priya's real constraint.

---

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: this is a real budget recommendation with a real deadline, not a
worksheet. Name the opener — "You are Priya Nakamura, two unfinished memos open on your screen, a
markup deadline tomorrow morning, and a phone buzzing with a legislative aide who wants a number."

### Launch

Show the printed chart from the Overview — a cost curve that falls off a cliff at one
exact income point — with no numbers yet. Ask: "Just looking at this shape, what does this line
tell you about how this cost function behaves at that point? Is it something you could graph
yourself if I gave you two data points on each side?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with Hold The Cliff —
spending nothing, knowing the chart looks like that?" Show of hands, no reasoning, record the count.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump to
"which option is cheaper" or "which is fairer" — push instead on: "What does it actually mean, in
math terms, for this cost function to have a 'cliff'? What would you need to check to prove that,
rather than just eyeball the picture?" The room should arrive at "we need to check whether the two
one-sided limits at the threshold actually agree" on its own before Anchor 3.

### Anchor 3 — What is the process?

Once the room names "check the one-sided limits, then run the
continuity test," ask them to state the actual steps before opening the appendices: build C(income)
piecewise from Appendix B (D1), evaluate both one-sided limits algebraically, apply the three-part
continuity definition (D2), repeat both steps for Build The Bridge's formula in Appendix C (D3),
then weigh the dollar size of the gap against Build The Bridge's real cost (D4) before recommending
(D5).

### Anchor 4 — What don't we know?

Surface the real open items honestly: the exact 400%-FPL
family-of-four threshold has two published figures that may not fully reconcile (Appendix A); this
state's own enrollment and budget figures are illustrative, scaled from real per-state data, not a
real named state's actual internal numbers (Appendix E). Ask which of these actually changes the
*recommendation* if it moves, versus which just changes the scale of both options together.

### Data Deep Dive

Walk D1 through D4 together once research has filled the appendices — cold-call
specifically for D2's "which part of the continuity definition fails" and D3's "does Build The
Bridge actually pass," since a Hero who gets D1/D3's limit values right but never states the
continuity conclusion in words has not actually finished the deliverable.

### Twist

Reveal Appendix D's national share figures directly: only **3-5% of subsidized enrollees
nationally** sit above (or within reach of) the 400%-FPL line at all (S14/S15) — a small population.
Ask: "If so few households are actually affected, does that change whether the state should fund a
whole new wraparound program — or does it just tell you 'small share of enrollees' isn't the same
question as 'small dollar harm per affected person'?" This invalidates the naive "it's only a few
people, don't bother" read of Option A without making Option B obviously correct — Appendix E's MA3
funding-mechanism problem (a one-time line item cannot pay for an ongoing subsidy) still stands
regardless of how the population share lands, and the per-household margin (7.74%) does not move
because the same population factor cancels out of both sides of the D4 comparison (see the margin
note below). A Hero who reverses to B purely because "it's not that many people, so it can't cost
that much in total" has mixed up the total-dollar framing with the per-household margin the
decision actually turns on.

### Immediate recommit

Re-vote. "Does this change your position — or does it just tell you which
assumption is worth pressure-testing?"

### Close

Re-vote again. "Did we ask the right question at the start? Was this really about which
policy is 'right,' or about whether a specific, calculable dollar harm justifies a specific,
calculable dollar cost?"

### Lessons Learned

*(To be filled in after the first real run with a cohort — see `runs/RUN_*.md`.)* Expected
takeaway, pending a real session: Heroes who reach D2/D3 correctly (B is provably continuous, A is
provably not) often want to stop there and declare B the winner on that basis alone — watch for
whether the room catches, unprompted, that "mathematically cleaner" and "the better recommendation"
are different questions until D4's dollar comparison is actually run.

### Standards Touched On

Calculus/Limits And Continuity — Limit, One-Sided Limit, Continuity, Discontinuity, How to
evaluate a limit algebraically, How to determine whether a function is continuous at a point.
Advanced Numbers — Percent, How to find the percent of a number (D4's cost-vs-harm comparison).

---

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above): show the cliff chart, no numbers. 30-second commitments. |
| 3:00–6:00 | Anchor 1 — stand/sit vote on Hold The Cliff, no explanation yet. |
| 6:00–15:00 | Anchors 2–3 — define the problem ("what does 'cliff' mean in math terms?") and the process (one-sided limits → continuity test → D1–D3) before any appendix opens. |
| 15:00–25:00 | Data Deep Dive — walk D1–D4 together; cold-call D2's "which part of continuity fails" and D3's "does B actually pass." |
| **25:00** | **DROP THE TWIST** — Appendix D's real 3–5% national share figures, delivered slowly. |
| 25:00–30:00 | Immediate recommit — who reverses, and why? "What just broke in your model — or was it just missing information?" |
| 30:00–40:00 | Threaded deep conflict, two named threads: (1) mathematical cleanliness (B passes continuity, A doesn't) vs. real dollar cost; (2) the 7.74% cost-effectiveness margin vs. Appendix E's harder funding-mechanism mismatch (a one-time line item cannot pay for an ongoing subsidy). |
| 40:00–45:00 | Close, re-vote, Lessons Learned. |

---

## The trap

**Most learners will finish D1–D3, correctly prove Build The Bridge is continuous where Hold The
Cliff is not, and then stop — concluding "Build The Bridge is obviously correct because it's
mathematically cleaner."** A Hero will reach that conclusion by valid arithmetic on D1–D3 alone
and skip D4 entirely, or treat D4 as a formality. This is the trap: the case's actual dilemma is
not "which function is continuous" (that's settled, unambiguously, by D2/D3) — it's whether the
real dollar size of the discontinuity, at this state's actual scale, is worth Build The Bridge's
real, ongoing budget cost. A Hero who stops at "B is continuous, so B wins" has done the calculus
correctly and quietly skipped the actual decision the case asks for. Watch for this specific
failure mode: a pitch that cites D2/D3 confidently and D4 not at all. The reverse trap is
symmetric and just as common: a Hero who dismisses B's cost as obviously disqualifying without
ever computing how large the discontinuity's real dollar harm is relative to it.

**Second trap — mismatched household scale between Appendix A and Appendix B.** Appendix A's
400%-FPL threshold is stated for a family of four ($128,600) as well as a single filer ($62,600),
but Appendix B's worked examples (the $62,000/$64,000 pair that D1's limit computation actually
uses) are single-filer-scale numbers. Do not let a Hero compare the family-of-four threshold
directly against the single-filer worked examples without adjusting for household size — the two
figures sit on different household-size scales, and treating them as interchangeable would corrupt
D1's limit computation even though neither number is itself wrong.

## Sensitivity note

Flagged per SPEC §6: this case touches live 2026 federal health-policy and budget debate. Keep
framing on the neutral, computable question (see SENSITIVITY FLAG above), not on partisan policy
correctness. Also disclose explicitly, every time this case runs, that no real state currently
funds smoothing above 400% FPL — Build The Bridge is a policy option grounded in real precedent for
lower bands, not an existing program.

## Socratic questions

1. You found that `lim_{x→400%⁻} C(x)` and `lim_{x→400%⁺} C(x)` disagree under Hold The Cliff. In plain language, what does that disagreement actually mean for a household whose income crosses that exact line?
2. Build The Bridge passes the same continuity test that Hold The Cliff fails. Does that automatically make Build The Bridge the better recommendation? Why or why not?
3. Your D4 table puts a dollar figure on the size of the discontinuity and a dollar figure on Build The Bridge's cost. Which of those two figures are you least confident in, and how would your recommendation change if that figure were off by half?
4. Appendix A gives two different published values for the family-of-four 400%-FPL threshold. Does that discrepancy change your D1 calculation in any way that matters to your recommendation?
5. If the state's discretionary line item (Appendix E) were twice as large, would your recommendation change? If it were half as large? What does that tell you about how "close" this decision actually is?

## Facilitator note on the margin (computed 2026-09-01, case-research pass)

**Per-household comparison (the actual margin driver):**

- D1/D2 discontinuity, Hold The Cliff: Household 2's unsubsidized premium ($14,931) minus
  Household 1's subsidized premium ($6,175) = **$8,756** (Appendix B, source S3 — this is the
  exact figure named in the original case brief, confirming the KFF example was correctly
  identified).
- Build The Bridge's real cost to smooth that same household: apply Appendix C's 8.5% cap to
  Household 2's $64,000 income → capped household payment = $5,440. State must cover
  $14,931 − $5,440 = **$9,491** to bring that household down to the capped rate.
- Margin: (9,491 − 8,756) / 9,491 = **7.74%**. Build The Bridge costs the state 7.74% more than
  the dollar harm it removes, per affected household. **Winning option: A (Hold The Cliff)** —
  by a real but modest margin, well inside SPEC §2's ~20% cap. This is *not* softened or rounded
  away — it is reported exactly as computed from S3/S5.

**Why the state-scale estimate (Appendix E, MA1/MA2) doesn't change this ratio:** both the total
harm (discontinuity × affected households) and the total Build The Bridge cost (per-household cost
× the *same* affected-household count) scale by the identical factor, so it cancels in the ratio.
This is a genuine, useful property to surface with a Hero who wants to argue "but we don't really
know how many households are near the threshold" — correct, and it doesn't matter for the A-vs-B
call, only for the headline dollar totals in D4's table.

**Why D5 should not stop at the margin alone:** Appendix E's discretionary line item (MA3, $8M
one-time) is far short of what a state-scale wraparound program actually costs per year in the real
world (Appendix D: New Mexico ≈$38.8M, Massachusetts $250M, California $190M→$300M) — a one-time
line item cannot fund an ongoing subsidy commitment at all, independent of whether the 7.74% margin
favors A or B. A complete D5 memo should name both reasons for A: the (modest) cost-effectiveness
margin, and the harder funding-mechanism mismatch.

**Retuning note for future revisions:** if a future pass wants a different margin (e.g., to make B
the clear winner for a different classroom purpose), the lever is Appendix C's 8.5% cap value or
Appendix B's specific worked-income-pair — not the Appendix E state-scale assumptions, which are
inert with respect to this ratio by construction.
