# Case Study: Prove It Scales

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Devon Achebe has two terminal windows open side by side, and one of them is still running.

The left window reads `recursive_rollup_test... PASS`, account hierarchy after account hierarchy —
each pass another quiet confirmation that the function does exactly what its induction argument
says it must. The right window holds a chart on Devon's second monitor, still climbing, its line
pushing further into red every time the test suite reaches an account nested a little deeper.

It's the night before the release freeze for Meterworks' billing engine, and Devon decides which
version of `RollUpCharges` ships — the function that walks every customer's nested account tree,
turning raw usage events into the number that lands on somebody's invoice. Ship the wrong version,
and customers could get billed the wrong amount, or the night's whole invoice run could hang.

Devon pulls the two branches up side by side. On the left: fewer lines of code, and a written
proof — base case and inductive step — that the recursive version is correct for a hierarchy of any
depth. On the right: no proof, just a comment reading `// walked this by hand, seems fine`, and a
runtime graph that barely moves no matter how deep the tree goes.

One fact Devon has to take as given tonight: the left-hand version runs fine on some computer
setups. But on the setup this company will actually use, it doesn't get a speed-up trick some
other setups get — so it can go from fast to explosively slow as the account structure nests
deeper, with no way around that on this company's setup.

Devon's phone buzzes, face-down. A message from the platform team, subject line visible: which
language runtime the release will actually ship on.

Devon doesn't turn it over yet.

---

## Background

Devon Achebe is a senior software engineer on the Billing Aggregation team at Meterworks, a usage-metering and billing platform that other software companies plug into so they can bill their own customers by consumption — API calls, compute-seconds, storage, however each customer's product is metered. Devon owns `RollUpCharges`, the function that turns raw usage events into a final billing total for every account in Meterworks' system, including accounts nested inside other accounts — a parent organization with sub-accounts, sub-accounts with their own sub-accounts underneath, arbitrarily deep (SEE APPENDIX A). The function is recursive by nature: computing a parent account's total requires first having the already-computed totals of every child account beneath it.

Two implementations are ready to ship, and Devon must recommend one before the release freeze.

**The Provable Path** is written as a direct translation of that recursive definition: a base case for an account with no children, and an inductive step that combines a parent account's own usage events with the already-computed totals of its children. Because it mirrors the mathematical recurrence exactly, Devon can prove — by induction on hierarchy depth — that it produces the correct total for every account, at every depth (SEE APPENDIX B).

**The Guaranteed Floor** rewrites the same logic as an explicit loop over a flattened, depth-ordered list of accounts, with a per-call cost that holds steady no matter how deep any one hierarchy goes. Its correctness rests on a walkthrough of representative test hierarchies, not a proof (SEE APPENDIX C).

The two implementations' real runtime cost does not diverge by one fixed amount — it depends on a simple fact about the computer setup Meterworks actually ships the billing engine on: some setups have a speed-up trick that makes the recursive version's repeated step almost free, and some don't (SEE APPENDIX B and APPENDIX D — that trick has a technical name, defined in Appendix G for anyone who wants to look it up). On a setup that has the trick, the two implementations run close to identically fast. On a setup that doesn't, the recursive version costs substantially more per call, and the gap widens further — explosively — as hierarchy depth grows (SEE APPENDIX D). Meterworks' billing pipeline runs against a fixed nightly compute budget and a fixed per-batch latency SLA that the next release must not miss (SEE APPENDIX A).

Billing-aggregation code carries its own history at Meterworks: the team has already shipped one production defect where a recursive rollup's own assumption — true at the top of an account tree — silently failed once an already-aggregated intermediate result was fed back into the same function one level down, producing a billing total that did not match reality. That incident is why a formal correctness argument is on the table for this release at all, not only a performance question — a documented industry precedent of exactly this failure shape exists outside Meterworks as well (SEE APPENDIX E). Full source citations for every figure in this case are in APPENDIX F.

---

## Dilemma

You are Devon Achebe.

Do you:

**A.)** Ship **the Provable Path** — the recursive `RollUpCharges`, proven correct for every account-hierarchy depth by mathematical induction **OR**

**B.)** Ship **the Guaranteed Floor** — the iterative rewrite, with a flat per-call runtime cost that does not depend on whether this company's computer setup happens to have the speed-up trick or not

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — An induction proof that `RollUpCharges`'s recursive version is correct for every account-hierarchy depth.** State the base case explicitly, state the inductive step explicitly, and write the closing argument that connects the two into a proof for a hierarchy of any depth.
- **D2 — A labeled recursion trace on a sample account hierarchy.** Draw or diagram the recursive version executing on a small sample hierarchy (at least three levels deep), marking which call is the base case and which calls are inductive-step invocations.
- **D3 — A per-call cost interpretation.** Using the inductive step you named in D1, explain in your own words why the recursive version performs one full combine operation per level of the account hierarchy, and use that structural fact to interpret Appendix D's measured runtime figures for the recursive implementation.
- **D4 — A runtime comparison table.** Milliseconds per 10,000 billing rollups for the iterative version and for the recursive version (under both a tail-call-optimizing runtime and a non-tail-call-optimizing runtime), at three account-hierarchy depths (Appendix D). Add a column showing the number of inductive-step invocations each depth requires.
- **D5 — A recommendation memo.** State which version Devon should ship, defended with D1's proof status, D4's numbers, and Appendix A's target-runtime fact — including whether the Provable Path's induction guarantee remains true regardless of which runtime it runs on, and whether that guarantee is worth the runtime cost D4 shows under the runtime Meterworks actually plans to ship to.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: Meterworks' Billing Pipeline Constraints

| Quantity | Value |
|---|---|
| Days from case launch to the release freeze | 3 days [MA1] |
| Maximum account-hierarchy nesting depth observed among current Meterworks customers | 5 levels [S5] |
| Billing rollup calls processed per night across all customer accounts | Billions of usage events processed per day, sustained (real usage-billing-platform proxy figure) [S6] |
| Maximum allowed runtime per batch of 10,000 rollups (latency SLA) | 500 ms [MA2] |
| Target language/runtime for the next billing engine release | Go [MA7] |

*Note: Meterworks is a scenario construction for this case — there is no real company by this name.*

---

## Appendix B: Option A — The Provable Path (Recursive `RollUpCharges`)

| Spec | Value |
|---|---|
| Lines of code, recursive implementation | 16 lines [MA3] |
| Base case | An account with zero child accounts; its total is the sum of its own raw usage events. |
| Inductive step | An account's total equals its own raw usage events plus the sum of its children's already-computed totals. |
| Does the target runtime named in Appendix A guarantee or reliably apply tail-call optimization to this function? | No. Go's own compiler team has repeatedly and publicly declined to add general tail-call optimization to the language, citing the need to keep `runtime.Callers` and stack backtraces predictable [S4]. |

---

## Appendix C: Option B — The Guaranteed Floor (Iterative `RollUpCharges`)

| Spec | Value |
|---|---|
| Lines of code, iterative implementation | 34 lines [MA4] |
| Implementation approach | Explicit loop over a flattened, depth-ordered list of accounts (children processed before parents), with an explicit stack replacing the call stack. |
| Correctness argument on file | A walkthrough of representative test hierarchies up to a stated depth; no induction proof. |
| Does this version's runtime depend on the target runtime's tail-call behavior? | No — per-call cost is fixed and does not depend on tail-call optimization. |

---

## Appendix D: Measured Runtime — Recursive vs. Iterative `RollUpCharges`

| Account-hierarchy depth | Iterative (ms / 10,000 rollups) | Recursive, TCO honored (ms / 10,000 rollups) | Recursive, TCO not honored (ms / 10,000 rollups) |
|---|---|---|---|
| Shallow | 0.164 [S1] | 0.333 [S1] | 3.94 [S1] |
| Medium | 0.259 [S8] | 0.343 [S8] | 3,508 [S8] |
| Deep | 0.354 [S7] | 0.354 [S2] | 3,122,383 [S2] |

*Shallow and Deep are directly measured (S1, S2); Medium is interpolated between them — see Modeling Assumption MA5. The Deep-row Iterative figure (S7) is not an independent measurement — see MA6.*

*Figures in this appendix are scaled from published language-runtime benchmarks of a canonical recursive function's (Fibonacci's) iterative, tail-recursive, and non-tail-recursive implementations, not from Meterworks' own (fictional) production telemetry — see the Modeling Assumptions block and Appendix F.*

---

## Appendix E: Documented Precedent — Recursive Aggregation Failures in Production

| Item | Value |
|---|---|
| A publicly documented production postmortem describing a recursive map-reduce billing/aggregation bug and the divergent totals it produced | Oren Eini (Ayende Rahien), founder of RavenDB — "Production postmortem: Your math is wrong, recursion doesn't work this way" (2022-07-13). A multi-map-reduce billing-aggregation index silently violated its own assumption once an already-reduced intermediate result was fed back into the same reduce function on a different cluster node, producing two different totals for the same account: **–67,343** and **+67,329** [S3]. |
| A published benchmark showing the extreme end of the non-tail-callable recursion cost gap | pope/go_recursive_benchmark (GitHub) — a naive, non-tail-callable recursive Fibonacci(40) runs at **312,238,250 ns/op**; the same function restructured to be tail-callable runs at **35.36 ns/op** — roughly an **8.8-million-times** gap [S2]. |

*This appendix documents a real, external precedent of the same failure shape described in Background — an already-aggregated intermediate result recursively re-fed into the same reduce function, violating an assumption that held only at the top level. It is cited as industry precedent, not as an incident at Meterworks itself.*

---

## Modeling Assumptions

> These figures are **not sourced** from Meterworks (a fictional company) or, in most cases, from
> any external record at all. They are stated scenario assumptions chosen by the case author, or
> figures derived by interpolating between two real, cited benchmarks. A Hero may challenge any of
> them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Days from case launch to release freeze | 3 days | Matches the Overview's "night before the release freeze" framing. | None — flavor only, not load-bearing. |
| MA2 | Latency SLA per batch of 10,000 rollups | 500 ms | No public SLA exists in exactly this unit; general published low-latency data-pipeline guidance puts operational batch targets in the tens-to-hundreds-of-ms range, so a round, conservative value is stated. | Does not flip the recommendation — Option A's real Deep-row cost (Appendix D, ~3.12 million ms) blows past *any* SLA from 50 ms to 5,000 ms. Changing MA2 changes only how badly the SLA is missed, not whether it is. |
| MA3 | Lines of code, recursive implementation | 16 lines | Illustrative — matches the case's "fewer lines of code" framing for the direct recursive translation. | None — flavor only. |
| MA4 | Lines of code, iterative implementation | 34 lines | Illustrative — an explicit flattening loop plus a manual stack is longer than the direct recursive translation. | None — flavor only. |
| MA5 | Appendix D, Medium row (all three cells) | Iterative 0.259 ms, TCO-honored 0.343 ms, TCO-not-honored 3,508 ms | Linearly interpolated (Iterative, TCO-honored columns) or log-linearly interpolated (TCO-not-honored column) between the two directly-measured endpoints in Appendix D — Shallow (S1) and Deep (S2). Iterative and TCO-honored code are both effectively O(n) (a single pass / a compiled loop), which justifies linear interpolation; naive non-tail recursion is exponential in depth, which justifies log-linear interpolation. | Does not affect `margin_pct` (computed at the Shallow row). The two anchor benchmarks were run five years apart on different hardware and Go versions, so treat the exact Medium numbers as order-of-magnitude illustrations of the trend, not measurements. |
| MA6 | Appendix D, Deep row, Iterative cell | 0.354 ms (set equal to the same row's TCO-honored figure) | No standalone iterative Fibonacci(40) benchmark was published in the cited repository. Under a TCO-honoring compilation, a tail call compiles to the same loop structure as an explicit iterative implementation — that structural equivalence is the basis for reusing the TCO-honored figure here. | Does not affect `margin_pct` (computed at the Shallow row). |
| MA7 | Target language/runtime for the release | Go | Go is a widely used systems/backend language for high-throughput metering and billing services, and its compiler team has repeatedly and publicly declined to guarantee general tail-call optimization (Appendix B, S4) — this is what supplies the case's real analytical fork. | **HIGH — this is the single most dilemma-relevant modeling choice in the case.** Had Meterworks instead targeted a runtime that reliably applies TCO, the cost gap would collapse toward the Shallow row's TCO-honored-vs-iterative ratio (real, ~2x, S1) instead of the ~24x-to-6-million-times gap the TCO-not-honored columns show (S1, S2). A Hero should be pushed to notice this is a stated choice, not an immovable fact. |

---

## Appendix F: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Go benchmark, Fibonacci(10): iterative vs. tail-recursive vs. plain recursive, ns/op | Iterative 16.4 ns/op; tail-recursive 33.3 ns/op; plain recursive 394 ns/op | Felipe Dutra Tine e Silva — ["Iterative vs Recursive vs Tail-Recursive in Golang"](https://medium.com/@felipedutratine/iterative-vs-recursive-vs-tail-recursive-in-golang-c196ca5fd489) (Medium) | 2017-01-25 | HIGH |
| S2 | Go benchmark, Fibonacci(40): naive (non-tail-callable) recursion vs. a tail-call-restructured rewrite, ns/op | BasicRecursion 312,238,250 ns/op; TCORecursion 35.36 ns/op | K. Adam Christensen ("pope") — [go_recursive_benchmark](https://github.com/pope/go_recursive_benchmark) (GitHub; input value `n=40` confirmed in `main_test.go`) | 2022-12-31 | HIGH |
| S3 | Publicly documented production postmortem: recursive map-reduce billing-aggregation bug, divergent totals | –67,343 and +67,329 on the same account | Oren Eini (Ayende Rahien) — ["Production postmortem: Your math is wrong, recursion doesn't work this way"](https://ayende.com/blog/197637-A/production-postmortem-your-math-is-wrong-recursion-doesnt-work-this-way) (ayende.com) | 2022-07-13 | HIGH |
| S4 | Whether Go guarantees or reliably applies tail-call optimization | No — Go does not support tail calls; the language keeps `runtime.Callers`/stack backtraces predictable instead | Ian Lance Taylor (Go team) — [golang/go issue #22624](https://github.com/golang/go/issues/22624) | Ongoing (issue open) | HIGH |
| S5 | Maximum nesting depth of a real, published multi-tenant nested-account hierarchy | 5 levels deep (root + OUs + member accounts) | AWS — [AWS Organizations FAQs](https://aws.amazon.com/organizations/faqs/) | Current | MEDIUM — real and precisely dated-as-current, but AWS Organizations is a cloud-account hierarchy, not a usage-billing rollup hierarchy; used as the closest public analog since Meterworks is fictional. |
| S6 | Disclosed processing scale of a real usage-based billing platform | "Streaming billions of events per day"; "tens of thousands of invoices processed per second" | Metronome, via [Confluent customer case study](https://www.confluent.io/customers/metronome/) | Undated page (accessed 2026-09-01) | MEDIUM — real, named, attributed quote, but the unit is usage events/invoices per second, not literally "rollup calls per night," and the page carries no publication date. |
| S7 | Derived: Appendix D, Deep row, Iterative cell | 35.36 ns/op (= same row's TCO-honored figure, S2) | Derived from S2 via structural equivalence (a TCO'd tail call compiles to the same loop as an iterative implementation) — see MA6 | 2022-12-31 (S2's date) | MEDIUM (derived, not independently measured) |
| S8 | Derived: Appendix D, Medium row (all three cells) | Iterative 25.88 ns/op; TCO-honored 34.33 ns/op; TCO-not-honored 350,798 ns/op (all ×0.01 for ms/10,000) | Interpolated between S1 (n=10) and S2 (n=40) — see MA5 for method and basis | 2017-01-25 / 2022-12-31 (S1, S2 dates) | LOW-MEDIUM (derived across two benchmarks run on different hardware/Go versions) |

*Unit conversion used throughout Appendix D: ms per 10,000 rollups = ns/op × 10,000 ÷ 1,000,000 = ns/op × 0.01.*

---

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Mathematical Induction
- Base Case
- Inductive Step

**"How to…" questions**

- How to prove a statement using mathematical induction

*Note on tail-call optimization (not a spine vocabulary term; background context only): this is the "speed-up trick" the Overview and Background refer to*
*without naming it — a compiler technique that reuses the current function call's stack space for*
*a recursive call that happens as the very last step, instead of stacking up a new frame for every*
*nested call. Go, the language/runtime this case's company targets, does not apply it — see the*
*real GitHub discussion at Appendix F, source S4.*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
