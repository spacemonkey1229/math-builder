# Learning Goals — Robotics Engineer

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — coordinate-plane plot of Sites A, B, C | `geometry-coordinate-plane`, `geometry-coordinate-pair-also-ordered-pair`, `geometry-how-to-graph-a-coordinate-pair-on-the-coordinate-plane` |
| D2 — three pairwise distances via the distance formula, shown as a Pythagorean-theorem calculation | `geometry-right-triangle`, `geometry-hypotenuse`, `geometry-pythagorean-theorem`, `geometry-how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane` |
| D3 — total travel time for both route orders, units converted at every step | `measurement-unit`, `measurement-how-to-convert-an-amount-from-one-unit-to-another-unit` |
| D4 — Container B's integrity remaining on arrival, per route order | `advanced-numbers-percent`, `advanced-numbers-how-to-find-the-percent-of-a-number` |
| D5 — one-sentence recommendation on which order is faster, and by how much | `number-sense-how-to-compare-two-or-more-values` |
| D6 — verify the three D2 distances satisfy the Triangle Inequality Theorem | `geometry-triangle-inequality-theorem` |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 13    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Correction (2026-08-05):** `how-to-find-the-distance-between-two-coordinate-pairs-on-a-coordinate-plane`
was originally claimed as new coverage. It is not -- `readmodel/standards_spine.json` shows
`covered_by=['Airstrike', 'Robotics Engineer']`, n=2. 'Airstrike' is a real, currently-taught Acton
legacy case (confirmed via `readmodel/pipeline_status.json`: status `legacy-untouched`, not yet
reformatted into this pipeline) whose original standards tagging already includes the distance
formula -- the spine correctly reflects that, it is not stale/leftover data. The real, verified new
coverage is `geometry-triangle-inequality-theorem` (D6, added 2026-08-05, confirmed n=0 pre-claim) --
see below.

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `coordinate-plane` / `coordinate-pair` / `how-to-graph-a-coordinate-pair` — D1 explicitly requires
  plotting three named points from Appendix A's given coordinates. Forced.
- `right-triangle` / `hypotenuse` / `pythagorean-theorem` / `how-to-find-the-distance-between-two-coordinate-pairs`
  — D2 explicitly requires the distance formula *shown as* a right-triangle calculation, not just a
  read-off-the-grid estimate — the case's own wording ("not just read off the grid") exists
  specifically to force the underlying Pythagorean derivation, not a shortcut. Forced, but the
  distance-formula how-to is not new coverage (see correction above).
- `unit` / `how-to-convert-an-amount-from-one-unit-to-another-unit` — D3 requires reconciling
  Ultron's stated mph rate against the map's meter-based distances; there is no way to produce a
  correct total-time figure without a real unit conversion. Forced.
- `percent` / `how-to-find-the-percent-of-a-number` — D4 requires computing integrity loss from a
  stated %-per-hour decay rate over a computed elapsed time — a direct percent-of-a-number
  calculation. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction ("which order is faster, and by how
  much") requires a direct numeric comparison of the two computed totals. Forced.
- `triangle-inequality-theorem` — D6 requires checking that no one of D2's three distances exceeds
  the sum of the other two. This is the genuine new coverage: it reuses D2's own output (no new data
  needed) and its margin (1.271 m) is the same real number the case's existing Twist mechanic already
  uses for the post-explosion detour distance -- not a contrived add-on. Forced.

No skill here is claimed on the strength of "the case is about geometry generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for why
this conversion computes its own honest coordinate/distance data rather than replicating the
original's hand-illustrated (and not machine-readable) obstacle map.
