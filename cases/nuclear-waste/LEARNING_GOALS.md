# Learning Goals — Nuclear Waste

Bidirectional deliverable ↔ skill matrix. Legacy conversion, 2026-08-01.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — rods per barrel/crate via volume comparison | `geometry-cylinder`, `geometry-how-to-find-the-volume-of-a-cylinder`, `geometry-volume` |
| D2 — transport + storage cost for 250,000 rods | `advanced-numbers-how-to-divide-decimal-numbers`, `advanced-numbers-how-to-multiply-decimal-numbers` |
| D3 — max container capacity and revenue at capacity | `geometry-how-to-find-the-area-of-a-circle`, `geometry-how-to-find-the-area-of-a-rectangle`, `geometry-how-to-find-the-volume-of-a-prism`, `geometry-prism` |
| D4 — safety rating comparison as a percentage | `advanced-numbers-percent` |
| D5 — recommendation weighing safety against cost | `number-sense-how-to-compare-two-or-more-values` |
| D6 — one barrel's interior surface area and total lining cost | `geometry-surface-area`, `geometry-how-to-find-the-surface-area-of-a-cylinder` |

## LEARNING GOAL CHECK

```
deliverables: 6    claimed skills: 13    new_coverage: 1
UNMAPPED DELIVERABLES: none
UNREACHABLE SKILLS: none
RESULT: PASS
```

**Correction (2026-08-02, read-model promotion):** `cylinder` / `how-to-find-the-volume-of-a-cylinder`
were originally claimed as new coverage. They are not — `covered_by[]` already listed "Nuclear Waste"
for both *before* this session's conversion (pre-existing tagging of the original legacy docx's own
vocabulary, which already said "Cylinder" in its own How To list).

**Second correction (2026-08-04, T1-10 tightened to require true self-inclusion for n=1 claims):**
`geometry-prism`, the first correction's replacement claim, also turned out invalid — the spine's n=1
at the time was "Cold Chain," not Nuclear Waste's own prior self-promotion, so it was never genuinely
new. The real, verified new coverage is `geometry-how-to-find-the-surface-area-of-a-cylinder` (D6,
added 2026-08-04, confirmed n=0) — see below.

**Forcing test applied to each skill** (*could a competent Hero produce the deliverable correctly
without ever performing this skill?*):

- `cylinder` / `how-to-find-the-volume-of-a-cylinder` / `volume` — D1 explicitly requires computing
  a cylindrical barrel's volume (V = pi r^2 h) to compare against a rod's volume. Forced, but not new
  coverage (see correction above).
- `how-to-divide-decimal-numbers` / `how-to-multiply-decimal-numbers` — D2's container counts
  (250,000 / rods-per-container) and total costs (containers x rate) are direct decimal
  division/multiplication. Forced.
- `how-to-find-the-area-of-a-circle` / `how-to-find-the-area-of-a-rectangle` / `how-to-find-the-volume-of-a-prism` / `prism`
  — D3 requires a barrel's circular footprint, a crate's square footprint, and the crate's cube
  (prism) volume to find each facility's maximum capacity. Forced, but `prism` is not new coverage
  (see second correction above — Cold Chain already covers it).
- `percent` — D4 explicitly asks for the safety-rating gap stated as a percentage. Forced.
- `how-to-compare-two-or-more-values` — D5's own instruction requires weighing safety against cost
  directly. Forced.
- `surface-area` / `how-to-find-the-surface-area-of-a-cylinder` — D6 requires computing one barrel's
  total interior surface area (both circular ends plus the curved side wall, since the barrel is
  fully sealed and lined) and the total lining cost for all 273 barrels the contract needs. This is
  the genuine new coverage (n=0, confirmed via `readmodel/standards_spine.json`). Forced.

No skill here is claimed on the strength of "the case is about nuclear policy generally" — each one
traces to a specific verb in a specific deliverable. See `case.json.legacy_conversion_note` for why
this conversion declares safety rating (not cost) as the graded primary metric — the real cost gap
is geometry-driven and too large to honestly force within SPEC's 20% balance cap.
