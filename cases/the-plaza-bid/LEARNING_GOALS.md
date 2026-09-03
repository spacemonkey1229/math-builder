# LEARNING_GOALS.md — The Plaza Bid

Bidirectional deliverable ↔ skill matrix (SPEC §7 / case-write step 10).

| Deliverable | Skills it forces (spine ids) |
|---|---|
| D1 — interior-angle-sum tessellation proof (hexagon; octagon alone fails; octagon+square works) | geometry-hexagon, geometry-octagon, geometry-regular-polygon, geometry-sum-of-the-interior-angles-of-a-polygon-theorem, geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles |
| D2 — GCF staging-block computation | basic-operations-greatest-common-factor, basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers |
| D3 — cut-waste computation (sheets purchased, waste %) for both options | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D4 — total installed cost table (material + labor, per sq ft) | advanced-numbers-percent, advanced-numbers-how-to-find-the-percent-of-a-number |
| D5 — recommendation memo, defended with D1's geometry + D3's waste % + D4's cost | geometry-sum-of-the-interior-angles-of-a-polygon-theorem, advanced-numbers-percent |

**Forcing test applied:** *could a competent student produce this deliverable correctly without
ever performing this skill?* For each mapping above, no — D1 cannot be written without actually
computing a regular hexagon's and a regular octagon's interior angle from the theorem and checking
which vertex combinations sum to exactly 360°; D2 requires actually finding the greatest common
factor of 45 and 30, not guessing a "nice" block size; D3 requires actually computing a
percentage (purchased coverage vs. net area) from a real rounded sheet-grid count, not copying a
number off the appendix; D4 requires computing percent-based cost adjustments (the waste-inflated
material purchase, the labor premium) and combining them into a single per-square-foot figure; D5
requires weighing D1's tessellation fact against D3's real (and counter-intuitive) waste result —
a student who never separated "which shape tessellates the plane" from "which manufactured
product wastes less material on this specific plaza" cannot write a D5 memo that gets the
*reasoning* right, even if they copy the correct final number.

```
LEARNING GOAL CHECK
  deliverables: 5    claimed skills: 9    new_coverage: 0 (thickening pass — see note below)
  UNMAPPED DELIVERABLES: none
  UNREACHABLE SKILLS: none
  RESULT: PASS
```

**new_coverage note.** All 9 claimed skills already show `n>=1` in `readmodel/standards_spine.json`
(`geometry-hexagon` n=1, `geometry-octagon` n=1, `geometry-regular-polygon` n=2,
`geometry-sum-of-the-interior-angles-of-a-polygon-theorem` n=1,
`geometry-how-to-find-the-measure-of-an-interior-angle-of-a-polygon-given-the-other-angles` n=2,
`basic-operations-greatest-common-factor` n=2,
`basic-operations-how-to-find-the-greatest-common-factor-of-a-set-of-numbers` n=2,
`advanced-numbers-percent` n=55, `advanced-numbers-how-to-find-the-percent-of-a-number` n=61, all
counts as of the pre-authoring read of the spine). `new_coverage[]` is therefore correctly `[]` per
SPEC §4's literal rule (a skill already at `n>=1` cannot be claimed as newly-closed). This matches
the concept sheet's own framing for C5 ("0 new zero-coverage skills — thickens GCF/interior-
angle-sum-family skills") exactly: this case's authoring value is (1) reinforcing a thin
Hexagon/Octagon/Regular-Polygon/interior-angle-sum cluster that currently sits at only 1-2 cases
each, and (2) opening `tiling-pattern-art` as a domain — a zero-existing-case, HIGH-authoring-
priority domain per `readmodel/domains.json` — which counts toward the number-theory branch's
starved feeding-domain set, not toward any spine id's new-coverage count. Flagged here, as
`prove-it-scales`' LEARNING_GOALS.md flags its own analogous reinforcement case, for `case-qa` to
confirm as a disclosed, deliberate deviation rather than an undisclosed zero-new-coverage defect.
