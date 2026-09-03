# LEARNING_GOALS.md — The Qubit Budget

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — state-space computation (2^20, 2^24, ratio as a single power of 2) | advanced-operations-base, advanced-operations-how-to-evaluate-an-exponential-expression |
| D2 — circuit gate-count table from the calibrated model | advanced-operations-base |
| D3 — below-threshold success-probability computation, order of operations | advanced-operations-exponent-also-power, advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order |
| D4 — cost-per-successful-shot table and margin | advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order |
| D5 — recommendation memo, defended with D1 + D4 + Appendix A | advanced-operations-how-to-evaluate-an-exponential-expression |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without correctly
identifying the base (2) and evaluating both exponential expressions, then combining them via
exponent rules to get a single power of 2 (2⁴ = 16); D2 requires substituting a qubit count into
an exponent-adjacent linear model and reading off a gate count; D3 is the case's sharpest
forcing point — a student cannot get (1 − 0.00464)²⁰⁰ right without doing the subtraction
*inside* the parentheses before applying the exponent, which is exactly the order-of-operations
skill this case targets, and a wrong order (e.g., raising 1 to the 200th power first, then
subtracting) produces a wildly wrong and immediately implausible probability; D4 requires
carrying that same multi-operation exponent expression through a division to get a dollar figure,
and comparing two such expressions to compute a percent margin; D5 requires weighing D1's exact
state-space guarantee against D4's real-but-model-dependent cost gap — a student who never
correctly evaluated the exponent expressions cannot defend either side with real numbers.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 4    new_coverage: 0 (reinforcement — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** Two of the four claimed skills (`advanced-operations-exponent-also-power`,
`advanced-operations-how-to-evaluate-an-exponential-expression`) already show `n=4` in
`readmodel/standards_spine.json` before this case; the other two
(`advanced-operations-base`, `advanced-operations-how-to-evaluate-an-expression-with-multiple-operations-with-exponents-order`)
already show `n=1`. None are at `n=0`. This is expected and was called out explicitly in the
source concept write-up (`CONCEPTS_pim-sector-gaps_2026-08-24.md`, C10): "0 skills at true zero —
thickens Exponents from n=1-3 toward n=2-4." `new_coverage[]` is therefore correctly set to `[]`
per SPEC §4's literal rule (a skill already at `n>=1` cannot be claimed as newly-closed), and
`case.json` carries a `reinforcement_note` explaining that this case exists to reinforce a
thinly-covered Exponents group — with `advanced-operations-base` and the order-of-operations
how-to specifically genuinely load-bearing here (they are what D1/D3 actually force), not
decorative reuse. This is a deliberate, disclosed deviation from SPEC §4's "no reason to exist"
framing, same pattern as `prove-it-scales` — flagged for `case-qa` to confirm rather than silently
treated as a normal zero-new-coverage case.
