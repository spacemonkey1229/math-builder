# LEARNING_GOALS — The Overlap Call

Bidirectional deliverable ↔ spine-skill matrix (SPEC §1.5 item 3 deliverables vs. `case.json.standards[]`).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 both contact lists as labeled sets, with subset relationship identified | discrete-mathematics-set, discrete-mathematics-subset, discrete-mathematics-vertex, discrete-mathematics-edge, discrete-mathematics-graph-vertices-and-edges |
| D2 single Venn diagram, both sets, empty-region check | discrete-mathematics-venn-diagram, discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram, discrete-mathematics-empty-set |
| D3 union and intersection written out explicitly | discrete-mathematics-union, discrete-mathematics-intersection, discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets |
| D4 outlier-contact decision, with reasoning | statistics-and-probability-outlier, discrete-mathematics-intersection |
| D5 secondary-cases-per-kit comparison table, union vs. intersection | discrete-mathematics-union, discrete-mathematics-intersection, discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets |

**Why D1 also forces the graph-theory trio.** A student cannot correctly write Priya's two contact
sets without first reading them off the real network in Appendix A — the index patient is a
vertex, each recorded contact is a vertex joined to the index patient by an edge, and the whole
structure is a graph. Skipping that step and just copying a pre-summarized list would not produce
a defensible D1, because the raw data in Appendix A is delivered as a network, not a pre-built set.

**Why D4 also forces Intersection, not just Outlier.** Deciding whether the flagged contact is a
real dual exposure or a data error is, mechanically, a decision about whether that specific person
belongs in $A \cap B$ at all — a student who cannot correctly evaluate set membership cannot
correctly resolve D4 either.

**Why D3 and D5 both force the same three set-theory skills.** D5 cannot be produced correctly
without D3's own union/intersection counts (a student who guesses at $|A \cup B|$ or $|A \cap B|$
gets a wrong ratio in D5, not just an imprecise one) — the dependency is load-bearing, not
decorative, the same pattern as Bioreactor Bid's D3/D4.

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 12    new_coverage: 0 (REINFORCEMENT CASE)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**Reinforcement, not new coverage (2026-09-13 remediation).** At case-write time this case claimed
8 discrete-mathematics set-theory skills as `new_coverage[]`. By case-readiness remediation time,
`readmodel/standards_spine.json` showed all 8 already at `n=2`, `covered_by: ["Grant Reach", "The
Overlap Send"]` — two other cases published concurrently with this one, teaching the identical
union/intersection-of-two-real-world-sets dilemma. `new_coverage[]` is now correctly `[]`, and
`case.json.reinforcement_note` records the full check (including the adjacent Discrete
Mathematics/Graph Theory group, which has no zero-coverage skill either, and none of whose
path/cycle/weighted-graph skills is forced by D1–D5). This case ships as a third real-data
reinforcement case for this skill group, using a genuinely different scenario (contact-tracing/
epidemiology rather than mail routing or messaging reach) — not a padded new-coverage claim.

- **UNMAPPED DELIVERABLES:** none — D1–D5 each map to at least one claimed skill.
- **UNREACHABLE SKILLS:** none — all 12 claimed skills are forced by at least one deliverable:
  `discrete-mathematics-set` (D1), `discrete-mathematics-subset` (D1), `discrete-mathematics-vertex`
  (D1), `discrete-mathematics-edge` (D1), `discrete-mathematics-graph-vertices-and-edges` (D1),
  `discrete-mathematics-venn-diagram` (D2), `discrete-mathematics-how-to-represent-a-set-relationship-using-a-venn-diagram`
  (D2), `discrete-mathematics-empty-set` (D2), `discrete-mathematics-union` (D3/D5),
  `discrete-mathematics-intersection` (D3/D4/D5), `discrete-mathematics-how-to-find-the-union-and-intersection-of-two-sets`
  (D3/D5), `statistics-and-probability-outlier` (D4).
