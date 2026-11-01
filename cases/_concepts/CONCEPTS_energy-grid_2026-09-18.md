# Concept sheet — Energy Generation & the Grid — 2026-09-18

Target domain: `readmodel/domains.json` → `energy-grid` (cluster "Food, Energy & Resources").
Spine sweep (2026-09-18) confirms the whole spine currently has **zero skills at n==0** (same
finding as `the-turbine-channel`, `wind-call`), so this concept is scored on the reinforcement
carve-out basis. Thinnest energy-grid-reachable group: **Statistics And Probability/Data
Analysis** — `how to find a missing data element given the mean and the remaining elements of its
set` (n=1), `quartiles` (n=3), `outlier` (n=4), `median` (n=8), `range` (n=8). Secondary:
`Advanced Operations/Variables` — `how to solve a multi-step equation with a variable on one side`
(n=4).

| # | Title | score | tier | feasibility |
|---|---|---|---|---|
| C1 | **Firm Power** | 7.8 | T3 | HIGH |
| C2 | The Curtailment Hour | 5.2 | T3 | MEDIUM |
| C3 | Rate Case | 4.4 | T2 | MEDIUM |

**Recommendation:** Write **C1 — Firm Power**. It closes the thinnest reachable group (Data
Analysis) plus a thin Advanced Operations how-to, grounded in a real, live-fetched CAISO hourly
demand dataset and a real, named industry-standard cost methodology (Lazard's published "Cost of
Firming Intermittency" analysis) rather than an invented formula. C2 (curtailment economics) and
C3 (rate-case allocation) are killed: both lean on already-thick Percent/Mean skills and don't
reach Data Analysis's genuinely thin skills the way C1's missing-data-reconstruction and quartile
work does.

---

### C1 — Firm Power   ·   score 7.8   ·   tier T3

**Protagonist.** A resource adequacy planner at a California community choice aggregator (a real
kind of public power entity), who must recommend which new capacity contract to sign before the
board vote.

**The dilemma.** A.) Sign the Peaker Contract — new natural-gas peaking capacity OR B.) Sign the
Firmed Solar Contract — solar-plus-storage capacity, firmed to the same reliability standard via a
real published capacity-accreditation charge.

**Primary metric.** Dollars per megawatt-hour of 100%-firm capacity delivered during the actual
observed evening peak window.

**Why it's close.** Solar-plus-storage's own raw levelized cost is cheaper than gas peaking's, but
CAISO's own published capacity-accreditation value ("ELCC") for solar-plus-storage is well under
100%, so bringing it up to full reliability parity requires an additional, real, published firming
charge. Whether that firmed total still beats the cheapest realistic gas-peaking quote is genuinely
close once both are priced honestly on the same reliability basis — not a case where one option
is obviously bigger or cheaper before any analysis.

**Would close (10 skills, 5 how-to / 5 term):**
| id | kind | label |
|---|---|---|
| statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-elements-of-its-set | how-to | How to find a missing data element given the mean and the remaining elements of its set |
| statistics-and-probability-quartiles | term | Quartiles |
| statistics-and-probability-outlier | term | Outlier |
| statistics-and-probability-median | term | Median |
| statistics-and-probability-range | term | Range |
| statistics-and-probability-mean | term | Mean |
| statistics-and-probability-how-to-find-the-mean-of-a-set-of-data | how-to | How to find the mean of a set of data |
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side | how-to | How to solve a multi-step equation with a variable on one side |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | How to find the percent of a number |
| measurement-how-to-convert-an-amount-with-compound-units | how-to | How to convert an amount with compound units |

**Data feasibility: HIGH.** Named sources I expect to exist and have reason to believe are live:
CAISO's own public "Today's Outlook" historical demand CSV feed (`caiso.com/outlook/history/...`,
no key required, real 5-minute-resolution grid data); Lazard's "Levelized Cost of Energy+" report
(a real, free, widely-cited annual industry report with a published "Cost of Firming
Intermittency" section giving real ELCC, Net CONE, and levelized firming cost figures by balancing
authority). Not confident about: a single named California CCA's real published peak-demand share
of CAISO's total system — likely resolves as a disclosed scenario assumption scaling real CAISO
system-wide data down to a plausible mid-size CCA's scale.

**Sensitivity (SPEC §6).** NONE — a capacity-procurement business decision, no death/illness/
hardship stakes.

**Split risk.** NONE — 10 skills is within the single-case range.

---

### C2 — The Curtailment Hour · score 5.2 · tier T3
**Protagonist.** A transmission planner deciding whether to fund a transmission upgrade or accept
a stated curtailment rate for a wind farm.
**Killed because:** the natural math (percent of a number, mean) all lands in already-thick spine
groups and never reaches the Data Analysis group's genuinely thin skills.

### C3 — Rate Case · score 4.4 · tier T2
**Protagonist.** A utility rate analyst allocating a fixed-cost recovery across two customer
classes.
**Killed because:** almost entirely percent/ratio arithmetic in already-saturated groups; no path
to quartiles, outliers, or missing-data reconstruction.

**Next step:** Approve C1, then run case-write on it.
