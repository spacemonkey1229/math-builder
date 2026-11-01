# LEARNING GOAL CHECK — The Hub Choice

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 network map and city-pair count | discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-graph-vertices-and-edges, discrete-mathematics-binomial-coefficient, discrete-mathematics-how-to-compute-a-binomial-coefficient |
| D2 weighted route-time comparison table | discrete-mathematics-weighted-graph, discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph |
| D3 weekly time-saved calculation | discrete-mathematics-fundamental-counting-principle |
| D4 cost-per-benefit table | discrete-mathematics-weighted-graph |
| D5 recommendation memo | discrete-mathematics-binomial-coefficient |

**Why each mapping holds:**

- **D1** cannot be produced without drawing the network as vertices and edges (a student who
  doesn't know a "vertex" is an airport and an "edge" is a route cannot label the map at all),
  and the "total possible city-pairs" figure is, by definition, the binomial coefficient
  C(n,2) — there is no other correct way to compute it. A student who just counts existing
  routes has skipped the deliverable.
- **D2** requires reading the *existing* network as a weighted graph (each existing route
  carries a real flight-time weight) and finding the fastest existing path between ITH and ELM
  (which, since no direct edge exists yet, may require combining edge weights — this is exactly
  the shortest-path skill, even in this case's simple network) before it can be compared to the
  new direct edge's weight.
- **D3** requires combining two independent estimated quantities (weekly travelers × minutes
  saved) — the fundamental counting principle, applied to a two-factor total rather than a
  discrete outcome count, is the generalizable skill: how many total person-minutes result from
  independently varying "how many travelers" and "how many minutes each."
- **D4** re-reads the same weighted-graph route-cost data from D2/Appendix E as a rate (minutes
  saved per dollar), which requires treating the annual operating cost as another edge-level
  weight to be divided against.
- **D5** cannot correctly justify "why not build every route" without explicitly citing the D1
  binomial-coefficient count — a memo that just says "there are a lot of possible routes" without
  the computed number has not used the deliverable.

## UNMAPPED DELIVERABLES: none
## UNREACHABLE SKILLS: none

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 2
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```
