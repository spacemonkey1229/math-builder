# Learning Goals — The One-Pass Route

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — vertex-degree table | discrete-mathematics-vertex |
| D2 — written Euler-circuit determination | discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit, discrete-mathematics-cycle |
| D3 — minimum repeat-mileage route (odd-vertex pairing) | discrete-mathematics-path, discrete-mathematics-vertex, discrete-mathematics-cycle |
| D4 — connector cost-vs-savings comparison | discrete-mathematics-vertex, discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit |

**"Forces" test applied to each row:**

- D1: a vertex-degree table cannot be built without knowing what a vertex is and counting the
  edges that touch each one — the term is load-bearing, not decorative.
- D2: the three-way determination (circuit / path-only / neither) is literally the definition of
  the how-to skill. Stating whether the route can *close into one continuous loop* also forces the
  vocabulary term Cycle — a student who cannot distinguish "a route that returns to its start" from
  "a route that does not" cannot write a correct D2 answer.
- D3: pairing odd-degree vertices by shortest connecting path is a direct application of Path (the
  connecting route between two vertices), performed on top of the Vertex labels from D1. The
  resulting augmented route is asked to "close into one continuous loop" exactly as D2 defines a
  cycle — a student cannot verify their augmented route is actually the single-pass loop the case
  wants without applying the Cycle concept a second time, now to the *augmented* graph.
- D4: recomputing the degree of the two connector-joined vertices is a second, harder application
  of Vertex (the graph has changed, so the count must be redone, not looked up), and reapplying the
  Euler how-to to the changed graph is what tells the student how much repeat mileage the connector
  actually removes — the number the entire cost/savings comparison depends on.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 4    new_coverage: 3
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## Note on the Vertex overlap with `six-degrees-of-exposure`

`discrete-mathematics-vertex` is claimed here in `standards[]` because D1, D3, and D4 all
genuinely force it — this case cannot be written without it. It is **not** claimed in
`new_coverage[]`. The sibling case `six-degrees-of-exposure` (same session batch) already claims
`discrete-mathematics-vertex` as `new_coverage[]`, and at the time this case was written the spine
still shows `n=0` for that id (six-degrees has not been published/counted yet). Double-claiming the
same `n=0` skill as `new_coverage[]` in two sibling cases would let one skill get counted as "newly
closed" twice, which is the exact coverage-inflation failure mode noted for `the-keyspace-decision`
and `pattern-rights`. This case's reason to exist does not depend on Vertex being unclaimed
elsewhere — `discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit`,
`discrete-mathematics-path`, and `discrete-mathematics-cycle` are all genuinely untouched by any
sibling case and are sufficient on their own to justify this case. Vertex is listed in `standards[]`
as honest reinforcement of a skill the deliverables truly use, with `six-degrees-of-exposure`
remaining the sole owner of that skill's `new_coverage[]` claim.
