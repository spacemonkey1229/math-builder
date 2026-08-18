# LEARNING GOALS — Reroute Or Wait

Bidirectional deliverable ↔ spine-skill matrix (`case-write` step 10, MCS-10). Every Challenge-3
deliverable must force at least one named spine skill; every skill in `case.json.standards[]` must
be forced by at least one deliverable. "Forces" test: *could a competent student produce this
deliverable correctly without ever performing this skill?* If yes, the mapping is fake.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 drawn weighted network graph, vertex/edge counts, edge weights from printed clock times | `discrete-mathematics-graph-vertices-and-edges`, `discrete-mathematics-vertex`, `discrete-mathematics-edge`, `discrete-mathematics-weighted-graph`, `measurement-how-to-find-elapsed-time` |
| D2 cycle-and-cut inventory: one cycle written out; every edge on no cycle, with the two pieces removal creates | `discrete-mathematics-cycle`, `discrete-mathematics-edge`, `discrete-mathematics-graph-vertices-and-edges` |
| D3 shortest-path table for five trips, on three versions of the network, with minimality shown | `discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph`, `discrete-mathematics-path`, `discrete-mathematics-weighted-graph` |
| D4 rider-minutes ledger, waiting vs in-vehicle, converted to rider-hours per weekday and over the closure | `measurement-how-to-convert-between-units-of-time` |

## Why each mapping survives the "forces" test

- **D1 → Graph (Vertices And Edges), Vertex, Edge, Weighted Graph.** The deliverable *is* a graph:
  a student cannot draw it, count its vertices, count its edges, or attach a number to each edge
  without using all four ideas by name. The edge labels are what make it weighted rather than a
  sketch of a bus map.
- **D1 → How to find elapsed time.** Appendix B prints clock times and deliberately does **not**
  print running times. Every edge weight has to be produced by subtracting one printed clock time
  from another across an am/pm boundary in several rows. There is no other route to a labelled
  edge.
- **D2 → Cycle.** The inventory asks for a cycle written out as an ordered vertex sequence that
  returns to its start, and then for the complement — every edge on no cycle. Both halves are the
  definition of a cycle applied twice.
- **D2 → Edge, Graph.** Deciding which pieces the network breaks into when an edge is removed is
  edge-by-edge work on the graph object itself.
- **D3 → How to find the shortest path between two vertices in a weighted graph.** Five origin
  and destination pairs, three network versions each, and the deliverable explicitly demands the
  comparison work that proves minimality — the plain statement of the skill.
- **D3 → Path.** The answer format is a path: an ordered vertex sequence. A total in minutes with
  no vertex sequence does not satisfy D3.
- **D3 → Weighted Graph.** The whole point of the three versions is that the *weights* change (one
  edge is removed, another is lengthened) while the vertex set does not.
- **D4 → How to convert between units of time.** The ledger is computed in rider-minutes and must
  be reported in rider-hours per weekday **and** rider-hours over the whole closure. Two unit
  conversions, both required, neither optional.

## Skills deliberately NOT claimed

- `discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit` — the
  eighth skill in the Discrete Mathematics / Graph Theory group and the only one this case leaves
  at `n == 0`. **No deliverable here forces it.** Nothing in this case requires traversing every
  edge exactly once; claiming it would mark a gap closed that no student ever touched. It is left
  open for a future case.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 9    new_coverage: 7
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  PHANTOM SKILLS (forced by a deliverable but absent from standards[]): none
  RESULT: PASS
```

Gap group closed (partially): **Discrete Mathematics / Graph Theory** — 7 of its 8 skills move
from `n == 0`, all seven in `new_coverage[]`.
