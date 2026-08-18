# LEARNING GOALS — The Sunset Ramp

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 continuous model P(t) + power-rule derivative, reported as instantaneous rate of change | calculus-derivative, calculus-instantaneous-rate-of-change, calculus-how-to-find-a-derivative-using-the-power-rule |
| D2 tangent line equation at the steepest instant + differentiability justification | calculus-tangent-line, calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point, calculus-differentiable |
| D3 ramp-response capability table (battery vs. peaker vs. required rate, in MW/min) | measurement-how-to-convert-an-amount-with-compound-units |
| D4 dollars-per-MW/minute-covered calculation and percent margin | measurement-how-to-convert-an-amount-with-compound-units, advanced-numbers-how-to-find-the-percent-of-a-number |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 8    new_coverage: 6
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** The deliverable explicitly demands a polynomial model P(t) and a derivative found
  **using the power rule** — the only differentiation technique a term-by-term polynomial in t
  requires or permits at this level. `calculus-instantaneous-rate-of-change` is forced because the
  deliverable requires dP/dt to be *reported as* the rate of change of generation with respect to
  time, not merely produced as a symbolic byproduct — a student who differentiates correctly but
  cannot say what dP/dt physically means (MW of generation lost per minute) has not completed the
  artifact as specified.
- **D2 — no.** Writing "the equation of the tangent line" at a named instant is exactly the
  procedure `calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point` names, and there is no
  other route to a line equation anchored at one point with a given slope. The deliverable also
  demands an explicit statement that P(t) **is differentiable** at that point — including a reason
  the raw hour-boundary data is not itself smooth — which is precisely the vocabulary term
  `calculus-differentiable`, not an incidental aside.
- **D3 — no.** The battery and peaker ramp-rate figures in Appendix A arrive in mixed native units
  (a response time in seconds, an hourly ramp rate, etc.) and must be converted to a single
  MW-per-minute basis before they can be compared against the D2 instantaneous rate at all — that
  chained unit conversion is exactly `measurement-how-to-convert-an-amount-with-compound-units`.
- **D4 — no.** Converting a total capital-cost dollar figure into a *rate*-normalized figure
  (dollars per MW **per minute**) is itself a compound-unit conversion (dollars ÷ a rate quantity).
  Reporting "the percent margin between Option A's and Option B's cost-per-ramp-rate-covered" is a
  percent-of-a-number computation applied to a quantity the student just derived, not a number they
  can read off a table.

## Skills deliberately NOT claimed

- **`calculus-how-to-differentiate-a-product-of-two-functions` / `calculus-how-to-differentiate-a-
  quotient-of-two-functions` / `calculus-how-to-differentiate-a-composition-of-functions-using-the-
  chain-rule`** are not claimed. P(t) is fit as a single polynomial in one variable; nothing in D1
  or D2 requires differentiating a product, a quotient, or a composed function, and claiming these
  on the strength of "it's still calculus" would be exactly the "sounds related" failure mode
  SPEC's forces test exists to catch.

## Already-covered skills also exercised, not claimed in `new_coverage[]`

`measurement-how-to-convert-an-amount-with-compound-units` (n=6),
`advanced-numbers-how-to-find-the-percent-of-a-number` (n=24).

## Gap group closed

`calculus-derivative`, `calculus-instantaneous-rate-of-change`,
`calculus-how-to-find-a-derivative-using-the-power-rule`, `calculus-tangent-line`,
`calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point`, `calculus-differentiable` — all
six at `n = 0` in `readmodel/standards_spine.json` at authoring time (verified 2026-08-13; the
sibling case `the-optimal-can` claims three of these same six ids but had not been published as of
this run, so the spine's `n` counters were still unmoved — see verification block below).
Deliberately **not** claiming `calculus-how-to-differentiate-a-product-of-two-functions`,
`calculus-how-to-differentiate-a-quotient-of-two-functions`, or the chain-rule how-to — 6 of the 9
skills in the immediate Calculus/Derivatives neighborhood, by design.

### new_coverage overlap check (against `the-optimal-can`)

`calculus-derivative`, `calculus-instantaneous-rate-of-change`, and
`calculus-how-to-find-a-derivative-using-the-power-rule` were also claimed by `the-optimal-can`
(case.json `status: "researched"`, not `"published"`). Per SPEC §7 / pipeline convention, coverage
`n` only moves at `case-publish` time. The spine check run at the top of this case's authoring
(`skills/case-write/SKILL.md` §1) showed all three still at `n = 0`, so they remain valid
`new_coverage[]` claims here. If `the-optimal-can` publishes before this case does, whichever case
reaches `case-publish` second must re-run the spine check and drop any now-covered id from its own
`new_coverage[]` (it may still list the id in `standards[]` as reinforcement).
