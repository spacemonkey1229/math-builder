# Case Study: The Rig Split

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Wade Kessler has the Bakken productivity chart open in one tab and a text thread with Ray Delgado open in another, and he's been switching between them for twenty minutes without typing a word into either.

Ray has run rigs on the company's original Permian leases for eleven years. His two kids go to the same middle school as Wade's. Three lines up, Ray asks a straightforward question: are we moving or not. Wade still hasn't answered.

Friday's quarterly review is two days out. Wade's VP has already sent the agenda, and it doesn't say "options" — it says "Wade to present recommendation and defend."

Wade pulls the operations dashboard back up: the live feed from the Bakken pad, where the newest wells are running, sitting right next to the feed from the Permian leases, where the company started and where half the crew still lives a short drive from the yard. Two rigs are on the table. Ray's rigs, most likely — they're the two that come off their current pad assignment first. Wade already has the numbers loaded: barrels, days, a downtime figure the North Dakota ops lead read off over the phone last week.

What Wade doesn't have is an answer for Ray, or for the room on Friday.

The cursor blinks in the empty reply box under Ray's last message.

---

## Background

Wade Kessler is the Drilling Operations Manager for Torchline Resources, a mid-size independent oil and gas operator running rigs on both its original Permian Basin leases in West Texas and its newer Bakken acreage in North Dakota, where the company expanded three years ago. Torchline is a scenario construction for this case — there is no real company by this name. Wade owns the quarterly rig-allocation call: which rigs drill where, for the rest of the current quarter, given the fixed fleet the company has under contract right now (SEE APPENDIX A). Torchline's fleet is deliberately sized well below either basin's real industry scale (SEE APPENDIX F for real, published rig-count context).

Torchline's Bakken wells have been out-producing its Permian wells on a barrels-per-rig basis for the current window, a pattern that matches real, basin-wide productivity data the U.S. Energy Information Administration publishes for both basins (SEE APPENDIX D). Wade's VP has floated a straightforward-sounding fix, which Wade has started calling **the Basin Shift**: move two rigs off the Permian leases and onto the Bakken acreage, chasing the higher per-rig output for the rest of the quarter. The alternative, **Hold the Line**, leaves the current allocation untouched.

The complication is that moving a rig between basins is not instant. A rig coming off a Permian pad has to be shut down, disassembled, trucked roughly a thousand miles north, and reassembled before it produces a single barrel in North Dakota — a real, citable stretch of idle rig-days that industry logistics sources put in the range of one to four weeks for an out-of-region move (SEE APPENDIX A and APPENDIX E). Every day a rig sits idle during that move is a day it earns Torchline nothing, and the current quarter only has so many days left in it (SEE APPENDIX A).

There is a second cost that does not show up in any spreadsheet. The two rigs most likely to move are run by Torchline's most experienced crew — hands who have worked the company's original Permian leases for a decade, several of whom live within a short drive of the home yard. Reassigning them to North Dakota is a real disruption to real people, not just a line item, and Wade knows it. Wade's VP has been clear that the recommendation still needs a hard number behind it: total blended barrels produced per rig-day, across both basins, for the rest of the quarter (SEE APPENDIX D) — and Wade has to be ready to defend both the number and the call behind it at Friday's review. Full source citations for every figure in this case are in Appendix G, and the full standards bridge for this case is in Appendix H.

---

## Dilemma

You are Wade Kessler.

Do you:

**A.)** Execute **the Basin Shift** — move 2 rigs off the Permian leases into the Bakken, paying the relocation-downtime cost and disrupting your most experienced crew, to chase the Bakken's higher per-rig productivity for the rest of the quarter **OR**

**B.)** **Hold the Line** — keep the current allocation, no relocation downtime and no crew disruption, but the Permian rigs keep producing at their lower barrels-per-rig-day rate for the rest of the quarter

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A system of equations, set up and written in matrix form, for the Basin Shift (Option A).** Define your three unknowns (Permian-producing rig-days, Bakken-producing rig-days, and idle relocation rig-days for the rest of the quarter), write the three linear equations Appendix A and Appendix B's constraints require, and express the system as a coefficient matrix times a variable vector equal to a constant vector. State the coefficient matrix's dimensions.
- **D2 — Solve the Option A system using a matrix method.** Solve for all three unknowns using Gaussian elimination or an inverse-matrix method (your choice, but show every step). As part of your work: (a) compute the coefficient matrix's determinant by expanding along a row, showing each 2x2 minor's determinant you use along the way, to confirm the system has a unique solution; (b) verify your solution by matrix multiplication — confirm that the coefficient matrix times your solution vector reproduces the original constant vector; (c) if you use the inverse-matrix method, show that the coefficient matrix times its inverse produces the identity matrix.
- **D3 — Repeat D1–D2 for Hold the Line (Option B), using Appendix C's constraints.** Set up and solve Option B's own system the same way. (Hint: check whether Option B's coefficient matrix is the same one you used for Option A — if it is, explain why that makes sense given how the two options are related.)
- **D4 — A blended-productivity comparison table.** Using your solved rig-day values from D2 and D3 and Appendix D's real per-basin productivity rates, compute total barrels produced and blended barrels-per-rig-day for each option, and show the percent difference between them.
- **D5 — A recommendation memo.** State which option Wade should recommend, defended with D4's numbers and Appendix A/E's relocation-downtime figure. Include a sensitivity check: how many fewer relocation-downtime days would it take to flip your recommendation, and how does that number compare to the real published downtime range in Appendix E? Address the crew-disruption cost from Background explicitly — even if it isn't part of the barrels-per-rig-day number, does it belong in Wade's recommendation anyway?

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Rig Fleet & Quarter Constraints

| Quantity | Value |
|---|---|
| Total rig fleet under contract this quarter | 8 rigs [MA1] |
| Rigs currently running on Permian Basin leases | 6 rigs [MA1] |
| Rigs currently running on Bakken acreage | 2 rigs [MA1] |
| Rigs the Basin Shift would move (Permian → Bakken) | 2 rigs (given in the Dilemma) |
| Remaining days left in the current quarter, as of case launch | 60 days [MA2] |
| Relocation downtime per moved rig (idle, zero production, during the move) | 14 days [MA3] |

*Torchline's fleet numbers are a stated scenario assumption, not a real company's real fleet — see Appendix F for real, published industry-scale rig counts used only for context.*

---

## Appendix B: Option A — The Basin Shift

| Spec | Value |
|---|---|
| Rigs moved | 2, from the Permian leases to the Bakken acreage |
| Idle rig-days lost to relocation | 2 rigs x 14 days each = 28 rig-days [derived from MA3] |
| Permian rigs remaining, producing the full 60 remaining days | 4 rigs |
| Bakken rigs after the move | 2 original Bakken rigs (producing the full 60 days) + 2 relocated rigs (producing only 60 - 14 = 46 of the 60 remaining days, once their move is complete) |

---

## Appendix C: Option B — Hold the Line

| Spec | Value |
|---|---|
| Rigs moved | 0 |
| Idle rig-days lost to relocation | 0 |
| Permian rigs, producing the full 60 remaining days | 6 rigs |
| Bakken rigs, producing the full 60 remaining days | 2 rigs |

---

## Appendix D: Basin Productivity — EIA Drilling Productivity Report

| Basin | New-well oil production per rig (barrels/day) | Report period |
|---|---|---|
| Permian | 1,400 [S1] | Projected June 2024 |
| Bakken | 1,747 [S2] | Projected June 2024 |

*"New-well oil production per rig" is the U.S. Energy Information Administration's own standard measure of how many barrels per day a basin's newly drilled wells are producing, averaged per rig actively drilling — the metric an operator actually watches when judging which basin is "hotter" right now. June 2024 was the final month EIA published in this exact report before discontinuing the standalone Drilling Productivity Report (SEE APPENDIX G, sources S1/S2) and folding the same underlying data into its Short-Term Energy Outlook's regional tables instead. Every basin-productivity figure in this case is frozen at that same June 2024 cutoff, per this case's own sourcing rule — no figure here is mixed with a more recent EIA data point.*

---

## Appendix E: Real-World Rig-Relocation Logistics

| Finding | Source |
|---|---|
| Target time to relocate a rig is 2-4 days; typical actual moves take roughly twice that, running as long as 10 days in poor winter weather | Oil & Gas Journal, "Who moved my rig?" [S3] |
| For a rig transported in from another region — not a same-field, pad-to-pad move — mobilization (transport, assembly, and rig-up) often takes 1 to 4 weeks | MineralView, "How Long Does It Take to Drill an Oil Well? Spud to Royalty" [S4] |
| Roughly 25% of a rig's total activity time, industry-wide, is mobilization (rig-down, relocation, and rig-up combined) | Oil & Gas Journal, "Who moved my rig?" [S3] |

*This appendix is the real, general industry commentary Appendix A's 14-day relocation-downtime figure (MA3) is anchored to — a Permian-to-Bakken move is a genuine out-of-region move, not a same-field pad move, so the 1-4-week range (S4) is the more relevant of the two findings above. See Modeling Assumptions, MA3.*

---

## Appendix F: Industry Scale — Baker Hughes Rig Count by Basin

| Basin | Active rigs (Baker Hughes weekly count) | As of |
|---|---|---|
| Permian | 242 | 2026-01-30 [S5] |
| Williston (Bakken) | 29 | 2026-01-30 [S5] |

*Shown for real-world scale context only — Baker Hughes' weekly rig count is a real, famous, industry-standard dataset, but Torchline's own fleet (Appendix A) is a stated scenario assumption sized well below either basin's real total, consistent with "mid-size independent operator." This appendix is not used anywhere in the primary-metric computation.*

---

## Modeling Assumptions

> These figures are **not sourced** from Torchline (a fictional company) or, in most cases, from
> any external record at all. They are stated scenario assumptions chosen by the case author, or a
> figure anchored to a real, cited range. A Hero may challenge any of them in discussion — that is
> a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Torchline's total fleet and its Permian/Bakken split | 8 rigs total (6 Permian, 2 Bakken) | Stated in-scenario, sized to fit "mid-size independent operator" well below either basin's real total rig count (Appendix F). | Changes the absolute barrel totals but not the qualitative tension — the case's margin (see `case.json.balance`) comes from the ratio between relocation downtime and the basin productivity gap, not the fleet size. |
| MA2 | Remaining days left in the current quarter, as of case launch | 60 days | Stated in-scenario — the "night before Friday's quarterly review" framing implies a mid-quarter checkpoint, not the literal final day of the quarter. | Scales both options' barrel totals proportionally; does not change which option wins, since both options share the same 60-day rig-day budget (Appendix A). |
| MA3 | Relocation downtime per moved rig | 14 days | Anchored to Appendix E's real, cited 1-4-week range for an out-of-region rig move (S4) — 14 days sits in the lower-middle of that real range, reflecting an experienced crew and a motivated company, not the worst case. | **HIGH — this is the single most dilemma-relevant modeling choice in the case.** See `case.json.balance.margin_note` for the exact breakeven downtime value; the case's real recommendation flips on a change of only a couple of days either side of 14. |

---

## Appendix G: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | EIA Drilling Productivity Report: Permian new-well oil production per rig | 1,400 barrels/day | U.S. Energy Information Administration — [Drilling Productivity Report](https://www.eia.gov/petroleum/drilling/), [Permian Region](https://www.eia.gov/petroleum/drilling/pdf/permian.pdf) (May 2024 issue, projected June 2024) | 2024-05 issue / June 2024 projection | HIGH |
| S2 | EIA Drilling Productivity Report: Bakken new-well oil production per rig | 1,747 barrels/day | U.S. Energy Information Administration — [Drilling Productivity Report](https://www.eia.gov/petroleum/drilling/), [Bakken Region](https://www.eia.gov/petroleum/drilling/pdf/bakken.pdf) (May 2024 issue, projected June 2024) | 2024-05 issue / June 2024 projection | HIGH |
| S3 | Real-world rig relocation timing (target vs. typical, and mobilization share of total rig activity) | Target 2-4 days; typical actual moves ~2x that, up to 10 days in bad weather; mobilization ~25% of total rig activity time | Oil & Gas Journal — ["Who moved my rig?"](https://www.ogj.com/home/article/17294386/who-moved-my-rig) | Accessed 2026-09-01 | MEDIUM — real, named trade-press source, but the underlying study year is not restated on the page as fetched. |
| S4 | Real-world mobilization time for a rig transported in from another region | 1 to 4 weeks (transport, assembly, and rig-up) | MineralView — ["How Long Does It Take to Drill an Oil Well? Spud to Royalty"](https://www.mineralview.com/blogs/how-long-does-it-take-to-drill-an-oil-well) | Accessed 2026-09-01 | MEDIUM — real, named source, but describes moves between regions of Texas specifically, not a Permian-to-Bakken interstate move; used as the closest published analog. |
| S5 | Baker Hughes weekly rig count by basin | Permian 242 rigs; Williston (Bakken) 29 rigs | Baker Hughes weekly rig count, via Permian Basin Oil and Gas Magazine — ["Rig counts in Permian Basin, Texas continue to decline in 2026"](https://pboilandgasmagazine.com/rig-counts-in-permian-basin-texas-continue-to-decline-in-2026/) | 2026-01-30 | MEDIUM — figures are directly attributed and quoted from Baker Hughes' own weekly report, but sourced via a secondary trade-press article rather than fetched directly from rigcount.bakerhughes.com. |

---

### Appendix H — "How To…" Math Questions To Research

**Vocabulary terms**

- Matrix
- Matrix Dimension
- Determinant
- Identity Matrix

**"How to…" questions**

- How to add and multiply matrices
- How to find the determinant of a 2x2 matrix
- How to solve a system of equations using a matrix

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
