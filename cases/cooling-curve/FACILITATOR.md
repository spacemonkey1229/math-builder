# The Cooling Curve — Facilitator Notes (draft, stage 2)

**Status:** draft at `case-write` time. Every figure below is placeholder-dependent until
`case-research` fills `case.md`'s `{{NEEDS_SOURCE}}` tokens; this file records the *shape* of the
argument now, while the balance is freshest in the writer's head, and should be updated in stage 3
once real numbers land.

## Argument for A — the Pyramid Array

A pyramid encloses strictly more surface area than a cone sharing the same base footprint and
height — four flat triangular faces versus one curved lateral surface. Appendix A ties heat
dissipation directly to exposed fin surface area, so per individual fin, the Pyramid Array should
move more heat. The mold for a four-face cavity costs more to cut, but that is a one-time,
amortized cost spread across every fin the mold ever produces — while the extra surface area pays
back on every single cooling cycle, for the life of the deployment. If the site's real constraint
is thermal headroom rather than sticker price, the pyramid's watts-per-fin advantage can be the
whole argument.

## Argument for B — the Cone Standoffs

A conical fin is a shape of revolution — tooled on a lathe-style single-cavity mold that is
faster and cheaper to cut than a four-face pyramid mold. That per-mold savings is not paid once;
it shows up as a lower cost on every one of the tens of thousands of fins this deployment needs
(Appendix E), and at that volume even a modest per-fin cost gap compounds into real money.
The Pyramid Array's extra surface area is real, but it is not free — if the cone's watts-per-fin
deficit turns out to be small relative to how much cheaper it is to mold at scale, the cone wins
on the metric that actually decides this case: watts dissipated per dollar spent, not watts alone.

## The margin

**Margin basis:** each design's D4 watts-per-dollar figure — [D2 surface area × Appendix A
dissipation rate] ÷ D3 cost per fin — once Appendix A's dissipation rate, Appendix B's fin
dimensions, and Appendix C's material and mold costs are sourced or stated as Modeling Assumptions
by `case-research`. Record the actual margin here, and in `case.json.balance.margin_pct`, once
those figures land — do not estimate it now.

Two things worth flagging to whoever runs `case-research` on this case, so the balance can be
checked honestly rather than assumed:

- The mold-cost gap between a pyramidal and a conical cavity is the single figure most likely to
  come back `NOT FOUND` as a public number — expect it to become a stated Modeling Assumption,
  and expect the case's balance to be sensitive to exactly how large that gap is judged to be.
- Because mold cost is a one-time cost amortized across a large fin count (Appendix C, Appendix E),
  the deployment's total fin count matters to the balance almost as much as the per-fin geometry
  does — a small deployment favors the cheaper mold outright; a very large one gives the pyramid's
  per-fin surface-area edge more cycles to pay back the mold-cost gap. Whoever fills Appendix E's
  fin-count figures should sanity-check that the resulting margin still sits inside SPEC §2's ~20%
  band before this case proceeds to `case-qa`.

## Five Socratic questions

1. Your D4 watts-per-dollar figures — which design wins, and by how much? Now imagine the
   deployment were ten times smaller. Does your D3 cost-per-fin math tell you that answer would
   change, and why?
2. The Pyramid Array wins on D2 surface area every time, by construction. So why isn't the answer
   to this case just "always build the pyramid"?
3. Your D3 table treats the mold cost as a cost per fin, spread across the number of fins one mold
   produces (Appendix C). What happens to your D4 result if that mold produces twice as many fins
   before it needs replacing — and which option benefits more from that change?
4. Appendix D gives an industry cost-per-watt benchmark as a cross-check. If your D4 figure for the
   option you'd recommend comes out worse than that industry benchmark, does that mean your
   recommendation is wrong, or does it mean something else?
5. A pyramid has more surface area than a cone of the same base and height — but "more" is not a
   number. What would have to be true about the size of that surface-area gap, relative to the
   mold-cost gap, for your recommendation to flip?

## The trap

The plausible wrong answer is picking the Pyramid Array on the strength of Appendix A alone —
"more surface area always means better cooling" — without ever running D3's cost math or D4's
per-dollar comparison. More surface area is real, but the case's primary metric is watts per
*dollar*, not watts per fin, and a design can dissipate more heat per fin while still losing badly
on cost once mold complexity and deployment scale (Appendix E) are priced in. The reverse trap is
symmetric: picking the Cone Standoffs purely because the mold is cheaper, without checking whether
the surface-area deficit costs the deployment more in under-dissipated heat than the mold savings
are worth. The case forces D1 through D4, in that order, specifically so no one can jump from "one
number looks better" straight to a recommendation.

## Sensitivity note (SPEC §6)

None declared by the concept sheet — routine facilities-engineering math, no contested or
emotionally weighted subject matter. The mold-cost-gap figure (Appendix C) is the one most likely
to arrive as a stated Modeling Assumption rather than a hard citation; if `case-research` cannot
source it, state it as an assumption in the open per SPEC §5, and note in the Modeling Assumptions
block that the case's answer is sensitive to it — never the size or direction of that sensitivity,
per `case-write` SKILL.md §8.
