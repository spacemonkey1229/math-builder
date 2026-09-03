# RESEARCH_LOG.md — The Rig Split

`case-research` pass, 2026-09-01. 8 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md`.
5 SOURCED, 3 ASSUMPTION (stated Modeling Assumptions), 0 DROPPED, 0 OPEN.

---

## P01 — Torchline's total fleet and Permian/Bakken split (Appendix A)

Searched: nothing directly sourceable — Torchline is a fictional company, framed in the concept
sheet as a "mid-size independent operator." Cross-checked against Appendix F's real Baker Hughes
figures (Permian 242 rigs, Williston 29 rigs, both real and dated) to make sure the stated fleet
size (8 rigs) reads as genuinely "mid-size" and well below either basin's real total, not
implausibly large.

**Outcome: ASSUMPTION.** MA1 = 8 rigs total (6 Permian, 2 Bakken). Not load-bearing on which option
wins (see margin_note) — scales both options' totals proportionally.

## P02 — Remaining days left in the current quarter (Appendix A)

Searched: nothing — framed in the concept sheet and case narrative as "stated in-scenario," i.e.
an authorial choice consistent with "Friday's quarterly review" being a mid-quarter checkpoint, not
the literal last day of the quarter.

**Outcome: ASSUMPTION.** MA2 = 60 days. Scales both options proportionally; does not change the
winner, since both options share the same 60-day rig-day budget.

## P03 — Relocation downtime per moved rig (Appendix A)

Searched: "drilling rig relocation move mobilization time days downtime rig-up rig-down basin to
basin." Found and fetched Oil & Gas Journal's "Who moved my rig?" directly
(`ogj.com/home/article/17294386/who-moved-my-rig`) — confirmed real text: "the target for
relocating the rigs was two to four days, typical moves took twice as long and lasted up to 10 days
in inclement winter weather"; "approximately 25% of average rig activity time is classified as
mobilization." This describes same-field, pad-to-pad moves primarily — not clearly an interbasin
move.

Searched further for an out-of-region figure: "moving oil drilling rigs logistics interstate."
Found and fetched MineralView's "How Long Does It Take to Drill an Oil Well? Spud to Royalty"
(`mineralview.com/blogs/how-long-does-it-take-to-drill-an-oil-well`) — confirmed real text: "Rigs
transported from other regions of Texas often require 1 to 4 weeks for transport, assembly, and
rig-up." This describes an intrastate (within-Texas) long-distance move, not literally Permian
(TX) to Bakken (ND) — closest published real analog found; a genuine Permian-to-Bakken move
(~1,000 miles) is at least as far, arguably farther, so treating the 1-4-week range as the
relevant one (rather than the shorter same-field range) is the more defensible reading, not the
more dramatic one.

Rejected inventing a more precise interbasin-specific figure — none exists publicly (this is
proprietary operator logistics data in reality, exactly as the concept sheet's "data feasibility"
note predicted).

**Outcome: ASSUMPTION.** MA3 = 14 days, anchored to the real 1-4-week range (S4), chosen at the
lower-middle of that range (reflecting an experienced crew and a motivated company, not the worst
case). Flagged **HIGH** sensitivity — see margin computation below; this is the single most
dilemma-relevant modeling choice in the case.

## P04 — EIA Drilling Productivity Report, Permian new-well oil production per rig (Appendix D)

Searched: "EIA Drilling Productivity Report Permian Bakken new-well oil production per rig barrels
per day." Learned the DPR was discontinued as a standalone report after its May 2024 issue (June
2024 was the last projected month) — EIA folded the same data into Short-Term Energy Outlook
regional tables starting June 11, 2024. Fetched `eia.gov/petroleum/drilling/` directly, which
still displays the final published figures: Permian 1,400 bbl/day (June), 1,386 bbl/day (May).

Cross-checked by fetching the actual final DPR PDF directly (`eia.gov/petroleum/drilling/pdf/dpr-full.PDF`,
a 700.8KB binary; WebFetch's text extraction failed on the raw PDF, so the file was read directly
page-by-page as images). Page 9 (Permian Region) confirms, in the EIA's own chart/callout box:
"Oil +14 / barrels/day month over month / 1,400 June / 1,386 May, barrels/day."

**Outcome: SOURCED, HIGH.** S1 = 1,400 barrels/day, June 2024 (projected, May 2024 issue) — the
final DPR figure published for this basin before the report's discontinuation.

## P05 — EIA Drilling Productivity Report, Bakken new-well oil production per rig (Appendix D)

Same fetch as P04 (same report, same PDF). Page 5 (Bakken Region) confirms: "Oil +2 / barrels/day
month over month / 1,747 June / 1,745 May, barrels/day."

**Outcome: SOURCED, HIGH.** S2 = 1,747 barrels/day, June 2024 (projected, May 2024 issue). Same
report issue as S1 — both figures share the same June 2024 cutoff, per SPEC §5's rule against
mixing dates for a still-changing real data series (the DPR itself changed format/discontinued
right after this issue, so freezing both basins at the same final issue is the correct, disclosed
cutoff).

## P06 — Real-world rig relocation timing, same-field moves (Appendix E, rows 1 and 3)

Same source as P03 (S3, Oil & Gas Journal). Used as background/context in Appendix E, not as the
direct anchor for MA3 (see P03 — the out-of-region figure, S4, is the more relevant anchor for an
interbasin move).

**Outcome: SOURCED, MEDIUM.** S3. Real, named trade-press source, directly fetched; the underlying
study's original year is not restated on the page as currently published, hence MEDIUM rather than
HIGH.

## P07 — Real-world mobilization timing for an out-of-region rig move (Appendix E, row 2)

Same source as P03 (S4, MineralView). This is MA3's real anchor.

**Outcome: SOURCED, MEDIUM.** S4. Real, named source, directly fetched and quote-confirmed;
MEDIUM because it describes intrastate (within-Texas) moves specifically, used as the closest
published analog for a genuine interbasin move rather than an exact match.

## P08 — Baker Hughes weekly rig count by basin (Appendix F)

Searched: "Baker Hughes rig count Permian Bakken basin active rigs 2026." Attempted to fetch
`rigcount.bakerhughes.com` and `rigcount.bakerhughes.com/na-rig-count` directly — both timed out
after 60 seconds (twice, on separate attempts), consistent with the site being a heavy
JS/spreadsheet-driven page not well suited to the fetch tool. Routed around it by finding and
fetching a trade-press article that directly quotes Baker Hughes' own weekly report:
Permian Basin Oil and Gas Magazine, "Rig counts in Permian Basin, Texas continue to decline in
2026" (`pboilandgasmagazine.com/rig-counts-in-permian-basin-texas-continue-to-decline-in-2026/`).
Confirmed via direct fetch: "Baker Hughes said in its weekly report of Jan. 30 there were 242 rigs
in Permian Basin... and... 29 (up 1)" for Williston.

**Outcome: SOURCED, MEDIUM.** S5. Real, dated, directly attributed figures, but sourced via a
secondary trade-press article rather than fetched directly from rigcount.bakerhughes.com itself
(direct fetch attempted twice, timed out both times). Used only for scale/context grounding in
Appendix F — explicitly not load-bearing on the primary-metric computation.

---

## Verification (skill step 7)

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources (must not be load-bearing): none
needs_source OPEN remaining: 0
```

No LOW-confidence sources in this case — S3, S4, and S5 are all MEDIUM (real, named, directly
fetched, with a stated reason for the confidence discount); S1 and S2 are HIGH (directly confirmed
in the primary EIA source document itself, read page-by-page).

## Margin (facilitator-only — computed here, not written into case.md)

Fixed inputs: R=8 rigs (MA1), D=60 remaining days (MA2), L=14 relocation-downtime days per moved
rig (MA3), k=2 rigs moved (given by the Dilemma), rP=1,400 bbl/day/rig (S1), rB=1,747 bbl/day/rig
(S2). Total rig-day budget = R*D = 480, fixed for both options.

**Option A (Basin Shift):** Permian-producing rig-days x = (P-k)*D = (6-2)*60 = 240. Idle rig-days
z = k*L = 2*14 = 28. Bakken-producing rig-days y = 480 - 240 - 28 = 212. Barrels_A = 1400*240 +
1747*212 = 336,000 + 370,364 = 706,364. Blended_A = 706,364 / 480 = 1,471.59 bbl/rig-day.

**Option B (Hold the Line):** x = P*D = 6*60 = 360. z = 0. y = 480 - 360 - 0 = 120. Barrels_B =
1400*360 + 1747*120 = 504,000 + 209,640 = 713,640. Blended_B = 713,640 / 480 = 1,486.75 bbl/rig-day.

**margin_pct = (1,486.75 - 1,471.59) / 1,486.75 x 100 = 1.02%. Winner: Option B, Hold the Line.**

This margin is comfortably inside SPEC §2's ~20% cap — no retune needed, and none attempted. It is
a genuinely close, real result: the Bakken's real per-rig productivity edge (~24.8%) very nearly,
but not quite, offsets the real relocation-downtime cost stated in MA3.

**Breakeven check (for sensitivity).** Solving (D-L)*rB = D*rP for L: L* = D*(1 - rP/rB) =
60*(1 - 1400/1747) = 60*0.198627 = 11.92 days. The case's stated MA3 value (14 days) sits only
about 2.08 days above that breakeven point — a small, plausible change to the case's single most
sensitive assumption flips the recommendation. This is a real, computed finding, not an artifact:
both endpoints of the calculation (rP, rB) are HIGH-confidence sourced figures, and the breakeven
day-count itself falls squarely inside the real, cited 1-4-week downtime range (S4) — meaning a
faster real-world move (well within published precedent) genuinely would flip the case.

## SPEC §2 self-check

- Primary metric exists and is computed for both options: yes (blended barrels-per-rig-day,
  480 rig-days for each option).
- No structurally-zero-cost option: confirmed. Option B is not free — it forgoes the Bakken's real
  per-rig productivity edge for the 46 productive days the moved rigs would otherwise have run
  there, an opportunity cost visible directly in the margin. Option A pays a real downtime cost
  (28 idle rig-days) plus a disclosed, un-modeled crew-disruption cost.
- Dilemma is not a foregone conclusion: confirmed. margin_pct = 1.02%, and the winner flips under a
  ~2-day change to MA3, which sits inside the real cited downtime range. This is a genuinely close
  case by construction from real data, not a manufactured one.
- **Verdict: PASS.** No balance concern to flag for case-readiness.

## Sensitivity model

Built `sensitivity_model.py` (PARAMS/evaluate()/FLEX[] pattern, matching
`cases/the-mainline-margin/sensitivity_model.py`). FLEX sweeps MA1 (fleet composition, expressed as
total rigs and Permian share), MA2 (remaining quarter days), and MA3 (relocation downtime days) —
the case's three stated Modeling Assumptions that feed the graded primary metric. Ran the script
(`python3 sensitivity_model.py`) and confirmed:

- Base case reproduces `margin_pct = 1.0196%` (rounds to 1.02) and `breakeven = 11.9176` days
  exactly, matching the hand computation above.
- MA1 (`total_rigs`, `permian_rigs`) does not flip the winner across a full +/-50% sweep on either
  parameter — Option B wins at every tested value.
- MA3 (`relocation_downtime_days`) flips the winner at -25% (10.5 days) and -50% (7 days) — Option
  A wins once downtime drops meaningfully below the 11.92-day breakeven — consistent with the
  hand-derived breakeven.
- MA2 (`remaining_days`) does **not** flip the winner at -25%/-50%, but **does** flip it at +25%
  (75 days) and +50% (90 days) — a longer remaining-quarter window gives the moved rigs more
  productive days to recoup the fixed 14-day downtime cost. This is a real finding the hand
  computation alone did not surface (the hand check only confirmed MA2 rescales both options
  proportionally *at* the stated 60-day value, which is true, but doesn't hold once the horizon
  gets long enough for the moved rigs to fully amortize the fixed downtime) — corrected
  `case.json`'s MA2 sensitivity field and `sensitivity_note` to reflect this after actually running
  the script, rather than leave the original, narrower hand-derived claim standing.

## Next step

Run `case-qa` on `the-rig-split`.
