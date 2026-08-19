# LEARNING GOALS — Redrawing Lines

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 map-space count | discrete-mathematics-fundamental-counting-principle, discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes, discrete-mathematics-binomial-coefficient, discrete-mathematics-how-to-compute-a-binomial-coefficient |
| D2 recursion sheet | discrete-mathematics-recursive-formula, discrete-mathematics-base-case, discrete-mathematics-how-to-write-a-recursive-formula-for-a-sequence, discrete-mathematics-how-to-convert-a-recursive-formula-to-an-explicit-formula |
| D3 exhaustiveness certificate | discrete-mathematics-mathematical-induction, discrete-mathematics-base-case, discrete-mathematics-inductive-step, discrete-mathematics-how-to-prove-a-statement-using-mathematical-induction |
| D4 pigeonhole brief | discrete-mathematics-pigeonhole-principle, statistics-and-probability-mean |
| D5 crossings-and-deviation scorecard | advanced-numbers-how-to-convert-numbers-to-percents |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 14    new_coverage: 4
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**`new_coverage[]` revised 2026-08-18 (case-readiness pipeline remediation, Tier 1 T1-10).** At
authoring time (2026-08-12) all ten of Binomial Coefficient, How to compute a binomial
coefficient, Pigeonhole Principle, Recursive Formula, Base Case, How to write a recursive formula
for a sequence, How to convert a recursive formula to an explicit formula, Mathematical Induction,
Inductive Step and How to prove a statement using mathematical induction read `n=0` in the spine.
Between then and this Tier 1 run, three other cases (Pattern Rights, The Keyspace Decision, Life
Insurance) published and took the spine credit for six of those ten — Binomial Coefficient, How to
compute a binomial coefficient, Pigeonhole Principle, Recursive Formula, How to write a recursive
formula for a sequence, How to convert a recursive formula to an explicit formula — before this
case ever published. Per `tier1_structural.py`'s T1-10 rule, a claim is only valid at `n==0` or
when *this* case's own title is already in the skill's `covered_by[]`; neither holds for those six,
so the claim is stale, not padding, and T1-10 flagged it correctly. All six remain genuinely forced
by D1/D2 (see the forces-test above) and stay in `standards[]` — the case still teaches and
requires them, it is just no longer the case that gets pipeline credit for being first. Only the
four skills nobody has claimed yet — Base Case, Mathematical Induction, Inductive Step, How to
prove a statement using mathematical induction, all still `n=0` — remain in `new_coverage[]`. No
`reinforcement_note` is needed: the trimmed list is non-empty.

**Forces test applied to each mapping** ("could a competent student produce this deliverable
correctly without ever performing this skill?"):

- **D1 — no.** The headline count cannot be produced by listing plans; the only route to it is
  the Fundamental Counting Principle applied to one independent binary choice per county, which
  forces both the term and the how-to. The size-breakdown row is *defined* as a row of binomial
  coefficients, and the deliverable requires at least four of them computed by hand with the
  factorial arithmetic shown, so `how-to-compute-a-binomial-coefficient` cannot be skipped by
  quoting a table.
- **D2 — no.** Part (a) is literally "write a recursive formula for a sequence," and it is
  useless without its base case, which the deliverable requires stated separately. Part (b) is
  Pascal's rule, a second recursion with its own base cases. Part (c) is the conversion of a
  recursive formula into an explicit closed formula, and the deliverable requires the explicit
  form checked back against the D1 total — a student who never converts cannot do that check.
- **D3 — no.** A proof by induction is the only way to establish the row-sum identity for *every*
  k rather than for Maine's k alone, and the deliverable forces the base case and the inductive
  step to be labeled separately and forces the student to point at the line where the D2(b)
  recursion enters the inductive step. Restating the D1 arithmetic does not satisfy it.
- **D4 — no.** All three claims are explicitly required to be proved with no plan enumerated and
  no map drawn, which rules out every route except pigeonhole. Claim (i) is a statement about a
  value at or above the mean of the two district populations, so the mean is not decoration: the
  student must compute the ideal as a mean and then argue that some district must sit at or above
  it. Claims (ii) and (iii) are counting-pigeonhole in the plain form.
- **D5 — no.** The deviation must be reported both in people and as a percent of the ideal, which
  forces converting a raw ratio into a percent. (This is the one already-covered skill in the
  set; it is claimed because the deliverable genuinely requires it, not to pad coverage.)

**Already-covered skills also exercised, not claimed in `new_coverage[]`:**
`discrete-mathematics-fundamental-counting-principle` (n=1),
`discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes` (n=1),
`statistics-and-probability-mean` (n=16),
`advanced-numbers-how-to-convert-numbers-to-percents` (n=18).

**Gap groups this case targets.** `new_coverage[]` closes the three remaining zero-coverage skills
in **Discrete Mathematics / Combinatorics** (Binomial Coefficient, Pigeonhole Principle, How to
compute a binomial coefficient) and all seven zero-coverage skills in **Discrete Mathematics /
Proof And Recursion**. Combinatorics' other two skills (Fundamental Counting Principle and its
how-to) already read n=1 in the spine at authoring time, so they are claimed in `standards[]` and
correctly excluded from `new_coverage[]`.
