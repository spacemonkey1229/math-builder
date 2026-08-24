# Learning Goals — Perimeter Protocol

Bidirectional deliverable ↔ skill matrix (SPEC §1.5 item 3 / case-write §10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — two complete truth tables for p OR q and p AND q | discrete-mathematics-truth-table, discrete-mathematics-how-to-construct-a-truth-table-for-a-compound-statement, discrete-mathematics-conjunction, discrete-mathematics-disjunction, discrete-mathematics-logical-statement |
| D2 — worked classification table applying both truth tables to the Traffic Sample | discrete-mathematics-conjunction, discrete-mathematics-disjunction, discrete-mathematics-logical-statement |
| D3 — negation of p, q, and Rule Set A's block condition, applied to the Traffic Sample | discrete-mathematics-negation, discrete-mathematics-logical-statement |
| D4 — converse/inverse/contrapositive analysis of the watchlist conditional | discrete-mathematics-conditional-statement, discrete-mathematics-how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement |
| D5 — false-positive-cost comparison producing the primary-metric margin | discrete-mathematics-conjunction, discrete-mathematics-disjunction (reuses the D2 classification counts — a student cannot total true-threats-blocked or false-positives-generated per rule set without having correctly evaluated the conjunction/disjunction conditions first) |

## LEARNING GOAL CHECK

```
deliverables: 5    claimed skills: 8    new_coverage: 7
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

- Every claimed skill (discrete-mathematics-conjunction, -disjunction, -negation, -conditional-statement,
  -truth-table, -how-to-construct-a-truth-table-for-a-compound-statement,
  -how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement,
  -logical-statement) is forced by at least one deliverable above.
- Every deliverable (D1–D5) maps to at least one claimed skill.
- `discrete-mathematics-logical-statement` (n=1 pre-case) is thickened, not claimed as new coverage —
  it was already exercised by the Key Length case; this case gives it a second, independent
  application (p and q as the atomic logical statements underlying two compound firewall rules).
- The seven skills in `new_coverage[]` are all at n=0 pre-case: conjunction, disjunction, negation,
  conditional-statement, truth-table, how-to-construct-a-truth-table-for-a-compound-statement, and
  how-to-determine-the-converse-inverse-and-contrapositive-of-a-conditional-statement. See case.json
  for the authoritative list.
