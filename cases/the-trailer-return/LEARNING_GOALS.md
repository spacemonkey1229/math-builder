# Learning Goals — The Trailer Return

Bidirectional deliverable ↔ skill matrix (SPEC §1.7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Practice Block vertex-degree table | `discrete-mathematics-vertex`, `discrete-mathematics-edge` |
| D2 — full-grid Euler determination (circuit / path / neither) | `discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit`, `discrete-mathematics-cycle`, `discrete-mathematics-path`, `discrete-mathematics-graph-vertices-and-edges` |
| D3 — Practice Block closed-circuit repeat-mileage pairing | `discrete-mathematics-weighted-graph`, `discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph`, `discrete-mathematics-vertex` |
| D4 — Practice Block open-path repeat-mileage pairing | `discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit`, `discrete-mathematics-path`, `discrete-mathematics-weighted-graph` |
| D5 — full-grid cost comparison table | `discrete-mathematics-weighted-graph` |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 8    new_coverage: 0 (reinforcement -- see case.json.reinforcement_note)
  UNMAPPED DELIVERABLES: none — every deliverable (D1-D5) maps to at least one claimed skill
  UNREACHABLE SKILLS: none — every skill in standards[] is forced by at least one deliverable:
    - discrete-mathematics-how-to-determine-whether-a-graph-has-an-euler-path-or-circuit: D2, D4
      (the target thin skill this case reinforces — tested twice, once for the full grid's
      circuit/path/neither classification and once for the Practice Block's open-path re-test)
    - discrete-mathematics-vertex: D1, D3
    - discrete-mathematics-edge: D1
    - discrete-mathematics-path: D2, D4
    - discrete-mathematics-cycle: D2
    - discrete-mathematics-weighted-graph: D3, D4, D5
    - discrete-mathematics-how-to-find-the-shortest-path-between-two-vertices-in-a-weighted-graph: D3
    - discrete-mathematics-graph-vertices-and-edges: D2
  RESULT: PASS
```

**"Forces" test applied to each skill**, per case-write step 10 ("could a competent student
produce this deliverable correctly without ever performing this skill? If yes, the mapping is
fake."):

- The Euler how-to is unavoidable in D2 (the entire deliverable *is* the circuit/path/neither
  classification) and again in D4 (re-classifying the Practice Block once the closed-circuit
  requirement is relaxed to an open path — a student cannot correctly choose which pair of odd
  vertices to leave unmatched without first understanding why an Euler path tolerates exactly two
  odd vertices where a circuit tolerates none).
- Vertex/edge are unavoidable in D1 (the deliverable is literally a per-vertex degree table built
  from counting incident edges).
- Path and cycle are unavoidable in D2 (naming which of the three Euler outcomes applies requires
  the vocabulary distinction between a path and a cycle) and D4 (an Euler path is not a cycle —
  a student who conflates the two will build D4 incorrectly, matching all odd vertices as if the
  circuit still had to close).
- Weighted graph and the shortest-path how-to are unavoidable in D3/D4 (the distance table in
  Appendix C only has meaning as edge weights in a shortest-path computation) and D5 (dollars are a
  weight applied over the deadhead-ratio's mileage, the same weighted-graph concept re-applied).

No skill in `standards[]` was added to pad the list — every one is exercised by name in at least
one deliverable's actual arithmetic, verified against the current spine before writing (see
`case.json.reinforcement_note` for the full adjacent-skill check).
