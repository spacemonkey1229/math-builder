# RESEARCH_LOG.md — Prove It Scales

`case-research` pass, 2026-09-01. 18 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
11 SOURCED, 7 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Days from case launch to release freeze (Appendix A)

Searched: nothing — this is explicitly framed in the placeholder text as "stated in-scenario,"
i.e. an authorial narrative choice, not a real-world fact to source. No search performed.

**Outcome: ASSUMPTION.** MA1 = 3 days, matching the Overview's "night before the release freeze."
Decorative, not load-bearing.

## P02 — Maximum account-hierarchy nesting depth observed (Appendix A)

Searched: "AWS Organizations maximum nesting depth organizational units 5 levels." Fetched
`aws.amazon.com/organizations/faqs/` directly. Found an exact, current, official FAQ answer:
"You can nest your OUs five levels deep. Including root and AWS accounts created in the lowest
OUs, your hierarchy can be five levels deep."

Meterworks is fictional, so no billing-platform-specific figure exists to source. AWS Organizations
is the closest real, published, multi-tenant nested-account-hierarchy depth figure I could find —
it is a cloud-account hierarchy, not a usage-billing rollup hierarchy, so it's a proxy.

**Outcome: SOURCED, MEDIUM.** S5 = 5 levels. Cited with the proxy caveat stated explicitly.

## P03 — Billing rollup calls processed per night (Appendix A)

Searched: "usage-based billing platform nightly aggregation rollup calls per day disclosed scale
Stripe OR Metronome OR Orb," then followed up on Metronome specifically (Stripe acquired Metronome
Jan 2026; Metronome's Confluent customer-story page discloses "streaming billions of events per
day" and "tens of thousands of invoices processed per second," attributed to a named Metronome
engineer, quoted directly). Fetched `confluent.io/customers/metronome/` directly to confirm the
exact quotes appear in the page (`grep` on the raw HTML, not just a search snippet).

No page discloses a "rollup calls per night" figure in exactly that unit — this is expected;
"rollup" is Meterworks' own fictional terminology. Rejected trying to convert "events/sec" to a
"per-night" total by assuming a nightly batch-window length: that would require stacking an
un-sourced assumption (window length) on top of an already-proxy figure, which the skill's rule
against layered invention argues against. Used the real, quotable figure directly instead.

**Outcome: SOURCED, MEDIUM.** S6 = "billions of events per day; tens of thousands of invoices per
second" (Metronome, via Confluent). Proxy units and undated page, both disclosed.

## P04 — Latency SLA, ms per 10,000 rollups (Appendix A)

Searched: `"ms per" OR "milliseconds" batch processing SLA "10,000 records" OR "per 10000" data
pipeline latency published`. Results only produced general qualitative latency-benchmark guidance
(operational streaming SLAs typically "tens to hundreds of ms," per StreamNative/Databricks-style
sources) — nothing published a concrete SLA figure in the specific unit "ms per 10,000 operations."

**Outcome: NOT FOUND → ASSUMPTION.** MA2 = 500 ms, a round value inside the general published
range found above. Sensitivity noted: does not flip the recommendation, since Option A's real
Deep-row cost (~3.12 million ms) blows past any SLA from 50 ms to 5,000 ms — the SLA choice only
changes how badly it's missed.

## P05 — Target language/runtime for the release (Appendix A)

Framed by the placeholder text itself as "stated in-scenario," i.e. an authorial choice — not
independently sourceable since Meterworks is fictional and hasn't picked a runtime in the real
world. Chose Go deliberately, because Go's own tail-call behavior (P07 below) is real, well
documented, and gives the case its actual analytical fork — this is exactly what the case's
Background section needs.

**Outcome: ASSUMPTION.** MA7 = Go. Flagged HIGH sensitivity — this is the single most
dilemma-relevant modeling choice in the whole case (see P07 and the margin computation).

## P06 / P17 — Lines of code, recursive / iterative implementations (Appendix B, C)

Framed as "stated in-scenario code length" — pure narrative flavor, not sourceable or
dilemma-relevant (does not appear anywhere in `balance.margin_basis`).

**Outcome: ASSUMPTION (both).** MA3 = 16 lines (recursive), MA4 = 34 lines (iterative).

## P07 — Does the target runtime (Go) guarantee or reliably apply TCO? (Appendix B)

Searched: "Go language specification tail call optimization guarantee compiler does not eliminate
tail calls." Found `github.com/golang/go/issues/22624`, opened and fetched directly. Ian Lance
Taylor (Go team) states plainly: "The current Go language does not support tail calls, because
they affect `runtime.Callers` and stack backtraces and the like." This is a clean, direct,
primary-source answer from the language's own maintainers — not a secondary blog's interpretation.

**Outcome: SOURCED, HIGH.** S4. Answer: No, Go does not guarantee or reliably apply TCO.

## P08–P10 — Appendix D, Shallow row (Iterative / TCO-honored / TCO-not-honored)

Searched: "Felipe Dutra Tine e Silva Medium Go benchmark iterative tail-recursive recursive
ns/op." Found two candidate articles by the same author. `WebFetch` returned HTTP 403 on Medium
directly (Medium blocks the fetcher's UA); routed around it via the `r.jina.ai` reader proxy,
which returned full page text. Cross-validated the exact figures against the WebSearch tool's own
independent snippet extraction (both landed on identical numbers) before trusting them.

Confirmed: "Iterative vs Recursive vs Tail-Recursive in Golang" (2017-01-25) benchmarks
Fibonacci(10) only, one input size, three variants in the same run:
`Benchmark_FibIterative_10-4 100000000 16.4 ns/op`,
`Benchmark_FibTailRecursive_10-4 50000000 33.3 ns/op`,
`Benchmark_FibRecursive_10-4 5000000 394 ns/op`.

These match the brief's target figures exactly. Converted ns/op → ms/10,000 ops (×0.01):
0.164 / 0.333 / 3.94.

Note for the record: a *second*, differently-titled article by the same author ("Iterative,
Recursive and Tail Recursive Comparition," 2019-02-12) benchmarks a different function (sum of
first N integers) across six input sizes (10 through 1,000,000) and shows tail-recursion
performing *no better* than plain recursion in Go for that function shape — a real, useful,
but *different* benchmark. Rejected using it as the Shallow-row anchor because the brief
specifically names the Fibonacci figures (16.4/33.3/394), and mixing function shapes across
Appendix D's three rows would undermine "same benchmark" continuity. Logged here so a future pass
doesn't waste time re-discovering it.

**Outcome: SOURCED, HIGH.** S1.

## P11–P13 — Appendix D, Medium row (all three cells)

Searched repeatedly for an intermediate-depth (roughly n=20–30) three-way Go benchmark (iterative
/ recursive / tail-recursive) to avoid interpolating: "golang benchmark fibonacci recursive
iterative tail-recursive ns/op fib(20) OR fib(25) OR fib(30)," "go benchmark
BenchmarkFibRecursive BenchmarkFibIterative BenchmarkFibTailRecursive n=20." Neither search
surfaced a real published benchmark at an intermediate depth in this exact three-way comparison.

**Outcome: NOT FOUND → derived (interpolated) + disclosed Modeling Assumption (MA5).** Rather than
inventing a plausible-looking number, interpolated between the two real endpoints already sourced
(S1 at n=10, S2 at n=40): linear interpolation for the Iterative and TCO-honored columns (both are
O(n) — a single pass or a compiled loop, which is a defensible reason to interpolate linearly),
log-linear (geometric) interpolation for the TCO-not-honored column (naive Fibonacci recursion is
exponential in n). Logged as source S8, `derived: true`, confidence LOW (the two real anchors are
five years and different hardware/Go-version apart, so cross-benchmark interpolation is inherently
soft — this was confirmed empirically: naively linear-scaling the *TCO-honored* column from n=10
to n=40 using only the Shallow-row per-unit rate predicts ~133 ns/op, but S2's real *measured*
TCO-honored figure at n=40 is 35.36 ns/op — a large miss, proving simple linear extrapolation across
these two specific benchmarks is unreliable on its own and must be anchored at *both* real
endpoints, not projected from one).

Explicitly checked: does S8/MA5 carry the margin computation? No — `margin_pct` is computed at the
Shallow row (S1, real, HIGH), so the Medium row's derived figures are illustrative only. This
satisfies the skill's rule that a LOW-confidence figure may never carry a constraint.

## P14 — Appendix D, Deep row, Iterative cell

The only real Deep-depth (n=40) benchmark found (pope/go_recursive_benchmark, see P16 below)
does not include an iterative implementation — only `BasicRecursion`, `ExtraCaseRecursion` (both
non-tail-callable), and `TCORecursion` (tail-callable).

**Outcome: NOT FOUND → derived + disclosed Modeling Assumption (MA6).** Set equal to the same
row's TCO-honored figure (35.36 ns/op) via a structural argument, not a guess: under a
TCO-honoring compilation, a tail call is compiled into the same loop structure as an explicit
iterative implementation — that is what tail-call optimization *is*. Logged as source S7,
`derived: true`, confidence MEDIUM. Does not affect margin_pct (computed at Shallow row).

## P15–P16 — Appendix D, Deep row, TCO-honored / TCO-not-honored columns; E2 — extreme-case benchmark

Searched: "pope go_recursive_benchmark github fib tail call ns/op." Found
`github.com/pope/go_recursive_benchmark`. `WebFetch` hit a 403; fetched successfully via plain
`curl` on `raw.githubusercontent.com` (README, `main.go`, `main_test.go`) and via the GitHub REST
API (`api.github.com/repos/.../commits`) for repo dates. Confirmed via `main_test.go`:
`var num = 40` — i.e. this is Fibonacci(40), naive double-recursion, run against three variants:

```
BenchmarkBasicRecursion-8       4          312238250 ns/op
BenchmarkExtraCaseRecursion-8   7          150884179 ns/op
BenchmarkTCORecursion-8         33120693   35.36 ns/op
```

`BasicRecursion` = naive, non-tail-callable (TCO not honored). `TCORecursion` = restructured to be
tail-callable (TCO honored). `ExtraCaseRecursion` is a third variant, still non-tail-callable
(more base cases, same double-recursion shape) — not used, since Appendix D only has two recursive
columns and `BasicRecursion` is the cleaner "naive" anchor. Repo's most recent relevant commit:
2022-12-31 (via GitHub API).

**Outcome: SOURCED, HIGH (both cells).** S2. Also directly answers Appendix E's extreme-case-gap
placeholder (E2) — same source, same figures, ~8.8-million-times gap (312,238,250 / 35.36).

## E1 — Publicly documented production postmortem, recursive map-reduce billing-aggregation bug

Searched: `Ayende Rahien "Production postmortem" "Your math is wrong" recursion RavenDB`. Found
and fetched `ayende.com/blog/197637-A/production-postmortem-your-math-is-wrong-recursion-doesnt-work-this-way`
directly (also confirmed via the page's embedded JSON-LD: `"datePublished":"2022-07-13T12:00:00+00:00"`,
`"author":{"name":"Oren Eini"}`). The postmortem describes a multi-map-reduce billing index
(Users, Credits, Charges) whose reduce function assumed every invocation would have a document
with a `Name` property — an assumption that held at the top of the aggregation but silently failed
once an already-reduced intermediate result was fed back into the same reduce function on a
different cluster node. Divergent totals for the same account, on different nodes: **-67,343** and
**+67,329**. Matches the brief's target figures exactly.

Confirmed the case-md language keeps this clearly attributed to RavenDB, not Meterworks — Appendix
E's italic note and the Background paragraph both say "documented industry precedent... not an
incident at Meterworks itself."

**Outcome: SOURCED, HIGH.** S3.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): ['S8']
needs_source OPEN remaining: 0
```

S8 (LOW) is the only LOW-confidence source, and it appears only in Appendix D's Medium row, which
is explicitly disclosed as interpolated (MA5) and is **not** the row `margin_pct` is computed
from — confirmed it carries no constraint, per the skill's rule.

## Margin (facilitator-only — computed here, not written into case.md)

At the Shallow depth (closest to Appendix A's real max hierarchy depth, S5 = 5 levels), under Go
(MA7) which does not honor TCO (S4): Option A (recursive) = 3.94 ms/10,000 rollups (S1); Option B
(iterative) = 0.164 ms/10,000 rollups (S1). **margin_pct = (3.94-0.164)/3.94 × 100 = 95.8%.
Winner: Option B, The Guaranteed Floor.**

This is well past the ~20% guideline and is reported plainly, not softened, per instruction.
Checked the counterfactual (TCO-honored runtime instead of Go): margin would still be
(0.333-0.164)/0.333 = 50.8% — also far over 20%. The real, sourced D4 numbers show iterative
beating recursive decisively under *both* runtime regimes at the Shallow depth; MA7 changes how
large the gap is, not whether Option B wins on raw numbers. The case's genuine balance is
qualitative (D1's permanent correctness guarantee vs. D4's real performance cost), which is already
how `FACILITATOR.md`'s `balance.argument_a` / `argument_b` are written. Full arithmetic trail is in
`case.json`'s `balance.margin_note`.

## MCS-46 waiver — 2026-09-01

This case proceeds under an MCS-46 waiver (`case.json.balance_test_waiver`), granted by the
project owner (manan.atit@gmail.com), rather than a further retune pass. Both real, sourced margin
figures computed above — 95.8% under Go/non-TCO (the case's actual named target runtime, MA7) and
50.8% under the TCO-honoring counterfactual — sit far past SPEC.md §2's ~20% balance cap, and the
counterfactual check specifically ruled out MA7 as the lever driving the blowout: flipping the
runtime assumption did not bring the margin back under the cap, it only reduced it from ~24x to
~2x, meaning the real S1/S2 benchmark data is decisively lopsided under either runtime. That
persistence across the counterfactual is exactly the "size of the gap is a real surprise,
discoverable only by computing it" condition MCS-46 requires, and the case's own induction proof
(D1) versus flat-cost-guarantee (D4) tension still forces genuine multi-step proof work regardless
of which runtime wins the numeric race. The waiver downgrades case-readiness's T1-09
structural-check severity from BLOCKER to GAP; it does not alter or hide the reported margin
numbers (95.8% / 50.8%), which remain as computed above and in `case.json`'s `balance.margin_note`.

## Next step

Run `case-qa` on `prove-it-scales`.
