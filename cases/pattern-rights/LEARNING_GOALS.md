# LEARNING GOALS — Pattern Rights

Bidirectional deliverable ↔ skill matrix. Run per `skills/case-write/SKILL.md` §10.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 configuration-count table (FCP) | discrete-mathematics-fundamental-counting-principle, discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes |
| D2 featured-capsule selection table (binomial coefficient) | discrete-mathematics-binomial-coefficient, discrete-mathematics-how-to-compute-a-binomial-coefficient |
| D3 guaranteed-repeat collision analysis (pigeonhole) | discrete-mathematics-pigeonhole-principle |
| D4 setup-dollar synthesis (FCP, reinforcement) | discrete-mathematics-fundamental-counting-principle, discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 5    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Forces test applied to each mapping** — *could a competent student produce this deliverable
correctly without ever performing this skill?*

- **D1 — no.** The number of distinct printable configurations is not a quantity anyone can look
  up or estimate sensibly; it exists only as the product of independent choice-counts (colorways,
  and — for The Half-Drop only — each column's mirror-or-as-drawn state). The deliverable
  explicitly demands the full application of the Fundamental Counting Principle shown for at least
  one scheme, and The Straight Set and The Half-Drop have a *different number of independent
  stages* (one vs. two), so a student cannot produce a correct count for both without correctly
  identifying and multiplying the right stages for each.
- **D2 — no.** "How many distinct k-element subsets exist within an n-element tile" is, by
  definition, a binomial coefficient — not a countable-by-hand quantity once n and k are realistic
  design numbers, and not answerable by guessing "a lot" or "a few." The deliverable explicitly
  requires the full binomial-coefficient computation shown, and demands it for two different values
  of n (6 vs. 12), so the student must apply the formula twice, not memorize one answer.
- **D3 — no.** This is the one deliverable that cannot be answered by comparing sizes
  intuitively. "How many repeat units before two are guaranteed to share a configuration" is, by
  definition, the configuration count plus one — a direct, textbook application of the Pigeonhole
  Principle, and the deliverable explicitly names the principle and demands the comparison against
  a real production run's actual repeat count. A student cannot produce a defensible guarantee
  threshold by guessing at "probably unique" or "probably not" — it is a specific, computed integer.
- **D4 — no.** Total printed yards from one engraving is the product of two independent
  counts — repeat units across the real fabric width, and repeat units along one cylinder's rated
  print run — which is exactly the Fundamental Counting Principle applied to a second, freshly
  sourced pair of numbers (not a reuse of D1's abstract count). The deliverable explicitly demands
  this multiplication shown in writing before the resulting yardage is divided by setup cost.

## Skills claimed and why each is genuinely forced, not bolted on

All five skills in the concept brief's "full Combinatorics group" are claimed. Two candidate
framings were considered and rejected before landing on the ones above, in the interest of the
same discipline `the-keyspace-decision` applied to this same skill group:

- A framing where D4's part (b) — dividing D2's already-computed capsule count by setup cost —
  was *also* tagged with `discrete-mathematics-binomial-coefficient` was rejected. Producing D4(b)
  correctly requires D2 to already be correct, but D4 itself performs no new binomial-coefficient
  computation of its own — it is a straight division of a number D2 already produced. Tagging it
  again would double-count the same forcing event under a different deliverable ID, which is
  exactly the "an unreachable skill silently marks a gap closed the student never touched" failure
  mode SPEC §7 and the write procedure warn against — except in reverse (over-claiming rather than
  under-claiming). `discrete-mathematics-binomial-coefficient` is forced once, cleanly, by D2.
- A framing where D1's "independent mirror-or-as-drawn state" stage was dropped (making both
  schemes single-stage, i.e. arithmetic rather than FCP) was rejected because it would make D1
  trivial — a single count copied from Appendix A rather than a genuine multiplication — and would
  weaken the FCP forcing test to "no" going the wrong direction (a student could produce D1 without
  applying the principle at all).

## Already-covered skills also exercised, not new

`discrete-mathematics-fundamental-counting-principle` (n=1 at authoring time) and
`discrete-mathematics-how-to-apply-the-fundamental-counting-principle-to-count-outcomes` (n=1 at
authoring time) are both already covered once each, by `the-keyspace-decision`. They are claimed
here, forced genuinely by D1 and D4, but **not** counted in `new_coverage[]`.

`discrete-mathematics-pigeonhole-principle` (n=0 at authoring time, at the time this case was
drafted `the-keyspace-decision` had already claimed it as that case's sole `new_coverage[]` entry,
but had not yet published, so the spine's `n` had not yet moved). This case also genuinely forces
Pigeonhole via D3 and claims it in `standards[]` — but it is **deliberately not** claimed in
`new_coverage[]` here. See the coverage-overlap note below.

## Gap group closed

`discrete-mathematics-binomial-coefficient` and `discrete-mathematics-how-to-compute-a-binomial-coefficient`
— both at `n = 0` in `readmodel/standards_spine.json` at authoring time, and, as far as this
author can determine, unclaimed by any other case's `new_coverage[]` (unlike Pigeonhole, which
`the-keyspace-decision` had already spoken for). This is the case's whole reason to exist per
SPEC §7: the first case in the corpus that genuinely forces "n choose k" via a real,
decision-relevant subset-count (D2), not a decorative example.

## Coverage-overlap note: why Pigeonhole is claimed but not `new_coverage[]` here

`the-keyspace-decision` (a sibling case, same Combinatorics skill group, same tier) already forces
the Pigeonhole Principle via a genuine collision-bound deliverable, and lists it as that case's
sole `new_coverage[]` entry — the harder, more original piece of design work between the two
siblings on this specific skill. At the moment this case was authored, `the-keyspace-decision` had
not yet published, so the spine file still shows `n=0` for Pigeonhole, meaning this case *could*
technically claim it in `new_coverage[]` without the validation script objecting.

Doing so anyway would be coverage inflation: SPEC §7 frames `new_coverage[]` as "the reason the
case exists," and this case's actual, load-bearing reason to exist is the binomial-coefficient
group, not Pigeonhole. If both cases claimed Pigeonhole as `new_coverage[]` and both later
published, only whichever publishes second would have its claim rejected by the coverage-inflation
check downstream — an arbitrary race condition based on publish order rather than which case did
the more original forcing work. Naming this here, at write time, removes that race: this case
claims Pigeonhole in `standards[]` (it is genuinely exercised, by D3) but explicitly leaves
`new_coverage[]` credit to `the-keyspace-decision`.
