# Learning Goals — The Fee Route

Bidirectional deliverable ↔ skill matrix (case-write SPEC §1.5/§10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 labeled weighted-graph drawing + cycle identification | discrete-mathematics-graph-vertices-and-edges, discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-weighted-graph, discrete-mathematics-cycle |
| D2 shortest-path determination (IB to CU, two candidate paths) | discrete-mathematics-path, discrete-mathematics-edge, discrete-mathematics-weighted-graph, discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph |
| D3 Euler-audit determination (circuit, path, or neither) | discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit |
| D4 expected-net-revenue-retained table for both rails | discrete-mathematics-weighted-graph, discrete-mathematics-path |
| D5 written recommendation in correct graph-theory vocabulary | discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-path, discrete-mathematics-weighted-graph, discrete-mathematics-cycle |

## LEARNING GOAL CHECK

**Test applied:** could a competent student produce this deliverable correctly without ever performing this skill? If yes, the mapping is fake.

- **D1** cannot be produced without treating the settlement network as an actual graph — naming every vertex (`vertex`, `graph-vertices-and-edges`), drawing every connection as a labeled edge with its fee weight (`edge`, `weighted-graph`), and finding a genuine closed loop among the vertices (`cycle`) — the graph in Appendix A contains exactly one 4-cycle (CN, AQ, MB, CU), and a student who draws only the two rails' two straight-line paths without checking for a loop among all seven vertices has not produced this deliverable. A student who lists nodes without connecting edges, or omits weights, has produced a diagram of dots, not a weighted graph. Genuinely forces `graph-vertices-and-edges`, `vertex`, `edge`, `weighted-graph`, and `cycle`.
- **D2** is impossible without applying the shortest-path method to a graph with more than one connecting route — a student who simply picks the path with fewer edges (four vertices between IB and CU) without actually summing the weights along each of the two real candidate paths would get the wrong answer, since the shorter-looking hop count (IB→CN→CU, two edges) happens to also be correct here, but a student cannot know that without doing the weighted comparison the how-to skill requires — the case deliberately makes the correct path the one requiring the weighted computation rather than the one that "looks" shorter by inspection alone; only computing both weighted totals distinguishes a correct answer from a lucky guess. Genuinely forces `path`, `edge`, `weighted-graph`, and the shortest-path how-to.
- **D3** requires counting the actual number of edges touching every one of the graph's seven vertices (`vertex`, `edge`) and applying the Euler theorem correctly (0 or 2 odd-degree vertices permits an Euler path/circuit; more than 2 does not) — a student who guesses "yes" or "no" without counting degrees, or who miscounts even one vertex's degree, cannot correctly identify that IB, CN, CU, and AW all have odd degree (four odd vertices, not zero or two) and that the network therefore admits neither an Euler path nor an Euler circuit. Genuinely forces `vertex`, `edge`, and the Euler how-to.
- **D4** requires pulling each rail's own weighted path total forward from D1/D2 (`weighted-graph`, `path`) into the actual dollar comparison — a student who has not correctly identified which edges belong to which rail's path cannot correctly compute either rail's total fee percentage, since the fee load IS the sum of the weights along that rail's specific path through the graph. Genuinely forces `weighted-graph` and `path` as applied, load-bearing quantities, not just vocabulary.
- **D5** requires writing the recommendation using actual graph-theory terms (vertex, edge, path, weighted graph, cycle) — a student who writes "the cheap option" and "the safe option" in plain English without ever referring to the graph's vertices, the two rails' paths, their weights, or the cycle finding from D1 has not met this deliverable's own stated requirement, even if the dollar conclusion is correct. Genuinely forces `vertex`, `edge`, `path`, `weighted-graph`, and `cycle` as the notation the paragraph must actually use.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

## new_coverage note

See `case.json.reinforcement_note` for the full accounting. Every one of the 8 claimed skills
(`discrete-mathematics-graph-vertices-and-edges`, `-vertex`, `-edge`, `-path`, `-cycle`,
`-weighted-graph`, `-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph`,
`-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit`) was checked against
`readmodel/standards_spine.json` before writing and every one is `n = 1` or `n = 2`, not `n = 0` —
this case reinforces a genuinely **thin** group (the concept sheet's own framing: "8 of 8 skills
thin (near-full close opportunity)") rather than closing a true zero-coverage gap. `new_coverage[]`
is `[]`, honestly, per the reinforcement carve-out (T1-10, `skills/case-readiness/SKILL.md`,
2026-08-17) — the same pattern used in `cases/the-overlap-send/LEARNING_GOALS.md`. Every one of the
8 skills is genuinely forced by at least one deliverable (see the matrix and check above), so
landing this case takes the whole Discrete Mathematics / Graph Theory group's every skill up by
one — real value against the concept sheet's gap-queue accounting, even though it is not,
technically, `new_coverage[]`.
