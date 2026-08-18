# Learning Goals — Six Degrees of Exposure

Bidirectional deliverable ↔ skill matrix. Every Challenge-3 deliverable must map to a claimed
spine skill; every claimed skill must be forced by at least one deliverable.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — labeled, weighted subgraph diagram | discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-graph-vertices-and-edges, discrete-mathematics-weighted-graph |
| D2 — ranked degree table (top 50) | discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-graph-vertices-and-edges |
| D3 — transmission-weight-eliminated comparison | discrete-mathematics-weighted-graph |
| D4 — shortest notification-path calculation | discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph, discrete-mathematics-weighted-graph |

**"Forces" test applied to each row:**

- D1: a diagram cannot be built without knowing what a vertex is, what an edge is, that a graph is
  the pair of the two, and what it means for an edge to carry a weight. All four terms are load-bearing.
- D2: "degree" is defined in this case as the count of edges touching a vertex — a student cannot
  produce a correct ranked list without applying the vertex/edge/graph definitions to real data.
- D3: the comparison is a sum of edge weights over two different vertex sets — the weighted-graph
  concept (an edge carries a magnitude, not just a connection) is exactly what makes D3 different
  from a simple edge count, and is exactly what the case's primary metric turns on.
- D4: the notification-cost rule is a textbook weighted-shortest-path setup (minimize summed edge
  cost across a multi-step route) — the how-to skill is the deliverable.

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 5    new_coverage: 5
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```
