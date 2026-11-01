# Learning Goals — The Absorption Call

Bidirectional deliverable ↔ spine-skill matrix, run against `readmodel/standards_spine.json`.

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — Room-volume & baseline reverberation calculation | `measurement-volume`, `geometry-how-to-find-the-volume-of-a-prism`, `measurement-how-to-convert-an-amount-with-compound-units` |
| D2 — Absorption (sabins) comparison table | `geometry-surface-area`, `geometry-how-to-find-the-surface-area-of-a-prism`, `measurement-volume` |
| D3 — Treatment cost calculation | `measurement-how-to-convert-an-amount-with-compound-units`, `geometry-surface-area` |
| D4 — Scaled rear-wall panel-layout diagram | `geometry-surface-area` |

## LEARNING GOAL CHECK

```
LEARNING GOAL CHECK
  deliverables: 4    claimed skills: 5    new_coverage: 0 (see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS (reachability); new_coverage[] empty under the T1-10 reinforcement carve-out
```

Forcing test applied to each mapping ("could a competent student produce this deliverable
correctly without ever performing this skill?"):

- **D1** cannot be done without knowing the room's volume as a quantity (`measurement-volume`),
  without computing that volume as length × width × height of a rectangular prism
  (`geometry-how-to-find-the-volume-of-a-prism`), and without converting the given foot
  dimensions into the meters Sabine's equation requires
  (`measurement-how-to-convert-an-amount-with-compound-units` — converting a linear foot
  measurement into the compound cubic-meter unit the formula needs).
- **D2** requires computing the area of every one of the room's rectangular faces
  (`geometry-surface-area`, `geometry-how-to-find-the-surface-area-of-a-prism` — the room is
  a rectangular prism and its six faces are exactly a prism's surface-area components) and
  re-uses the room volume figure from D1 (`measurement-volume`) to compute RT60 via Sabine's
  equation for each scenario.
- **D3** cannot be completed without reconciling the metric wall area computed in D2 with the
  imperial ($/ft²) cost rate given in Appendix D — a genuine compound-unit conversion
  (`measurement-how-to-convert-an-amount-with-compound-units`) — and restates the treated
  surface's area (`geometry-surface-area`).
- **D4** requires labeling the treated area and tiling it with a stated panel size, which is a
  surface-area computation on the same rectangular face used in D2 (`geometry-surface-area`).

## Skill list, locked before writing prose

```
n=2  term    | Measurement/Units | Volume                                          [NEW COVERAGE]
n=19 how-to  | Measurement/Units | How to convert an amount with compound units
n=8  term    | Geometry/Surface Area And Volume | Surface Area
n=3  how-to  | Geometry/Surface Area And Volume | How to find the surface area of a prism
n=3  how-to  | Geometry/Surface Area And Volume | How to find the volume of a prism
```

**Correction on `measurement-volume` and `new_coverage` (superseding an earlier draft of this
file).** An earlier pass of this document argued `measurement-volume` could still be claimed as
`new_coverage[]` because `gap_queue.json` calls it "thin" (`n_gap: 1` in Measurement/Units) even
though the spine shows `n = 2`, not `n = 0`. Running the actual gate,
`skills/case-readiness/scripts/tier1_structural.py`, proved that reading wrong: T1-10 requires
strict `n == 0` (or this case's own title already in the skill's `covered_by[]`), with no "thin"
exception — and `measurement-volume`'s `covered_by` is `['Nuclear Waste', 'Cold Chain']`, two
other cases from the same large parallel batch this case was authored in, neither of them this
one. The approved concept sheet was accurate when it was scored; by the time this case was
written, a sibling case in the same batch had already closed the gap first. `new_coverage[]` is
now `[]`, downgraded from a T1-10 BLOCKER to a GAP via the documented `reinforcement_note` carve-out
in `case.json` (a direct query confirmed zero remaining `n == 0` skills anywhere in the Measurement
or Geometry domains — there was no adjacent skill to redirect the claim to without abandoning the
approved acoustics/Sabine's-equation premise). See `RESEARCH_LOG.md` for the full note.

The Surface-Area-And-Volume group skills and the compound-units how-to are **not** claimed as
`new_coverage[]` — they are already thickly covered (`n ≥ 3` each) — but they are still listed
in `standards[]` because the forcing test above shows the case genuinely requires them.
