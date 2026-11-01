# Concept sheet — Marching Drill & Choreography (`drill-choreography`) — 2026-10-27

Target: domain `drill-choreography` (cluster Culture, Play & Performance). Avoids existing premises:
`company-front` (dilate vs rotate a block), `the-bandstand-angle` (frame angles on a plat),
`downbeat-split` (arranger/tempo). Prior sheet `CONCEPTS_drill-choreography_2026-08-12.md` was Company Front only.
Thin spine skills (n<=2) are scarce in this domain; the thin ones used are listed per concept.
All numbers below recomputed in Python this session (scratchpad c.py / d.py).

## Sources actually fetched this session (LIVE)
- DCI 2026 World Championship Finals recap: https://www.dci.org/scores/recap/2026-dci-world-championship-finals/ (caption totals GE/Visual/Music, 12 corps)
- DCI 2025 World Championship Finals recap: https://www.dci.org/scores/recap/2025-dci-world-championship-finals/ (judge-by-judge, sub-captions). I verified Visual = (VisProf + VisAnalysis + ColorGuard)/2, GE = sum of 4 judge totals /2, Music = (Brass + mean of 2 Music Analysis + Perc)/2, and GE+Vis+Music = Total within 0.0025 for all 12 corps (2026 and 2025).
- DCI 2026 finals score list: https://www.dci.org/scores/final-scores/2026-dci-world-championship-finals/ (NOTE: top summary block shows 98.750 for Bluecoats which conflicts with the 99.100 table/recap; use the recap).
- BOA General Field Diagram 2025 (PDF, text extracted): hash marks HS 53'4", NCAA/TX 60', NFL 70'9" from sideline; field mics at 50 and both 35 yd lines ~16' from front sideline; front boundary 15' outside front sideline. https://marching.musicforall.org/wp-content/uploads/sites/5/2025/05/BOA-General-Field-Diagram-2025-update.pdf (the 2026 URL returned 404).
- Ohio State Marching Fundamentals (PDF, text extracted): 8-to-5 = eight 22.5-inch steps per 5 yards. https://tbdbitl.osu.edu/sites/tbdbitl.osu.edu/files/Marching-Fundamentals.pdf (6-to-5 = 30 in per step confirmed by search result summary of the same source; page text for that line not read: partially UNVERIFIED).
- Old Pasadena Rose Parade page: route 5 1/2 miles, "2 1/2-mile-per-hour pace". https://oldpasadena.org/visit/events/signature-events/rose-parade

---

### C1 — The Gap Between Fifth and Sixth (RECOMMENDED) · tier T2 · data grade HIGH

**Protagonist.** Constructed (disclosed): Dev Raman, caption supervisor for a fictional World Class corps ("the
corps") whose final-week rehearsal hours are fixed. The scores are REAL: the corps' season-end scoreline is
the real 2026 Finals recap row of the 6th-place corps (Blue Stars: GE 37.800 / Visual 28.250 / Music 28.088 = 94.137);
the corps ahead is the real 5th-place row (Santa Clara Vanguard 38.050 / 28.300 / 28.675 = 95.025). Real corps are
named only as sourced score rows, no invented quotes/people. (R1b to decide whether to anonymize as "Corps 5 / Corps 6".)

**Dilemma (binary).** Gap to the corps ahead = 0.888. A) put every remaining rehearsal hour into the Visual caption
(cleaning forms/spacing); OR B) put them into the Music caption (ensemble/brass/percussion). GE is a judged outcome of the
design and cannot be rehearsed directly; this is a stated rule of the case (R1 flag: GE has the lowest headroom share
in every row, so it must be excluded by design, not ignored).

**Primary metric.** Share of remaining caption headroom the corps must capture to close the gap =
gap / (30 - current caption score) (30 = the Visual and Music caption maximums).

**Computed, both options win somewhere (the "same rule, other season" test is the whole case):**

| Season / pair | gap | Visual share | Music share | cheaper option | margin |
|---|---|---|---|---|---|
| 2026: 6th (Blue Stars) -> pass 5th (SCV) | 0.888 | 0.507 | 0.464 | MUSIC (B) | Visual costs 9.3% more (B wins by 8.5%) |
| 2025: 8th (Blue Stars) -> pass 7th (Mandarins) | 1.650 | 0.559 | 0.695 | VISUAL (A) | Music costs 24.2% more (A wins by 19.6%) |
| 2025: 9th (Cavaliers) -> pass 8th | 0.375 | 0.134 | 0.144 | VISUAL (A) | 7.2% |
| 2026: 8th (Cavaliers) -> pass 7th | 0.425 | 0.157 | 0.210 | VISUAL (A) | 25.2% |

Headline scenario margin: 8.5% (inside the 20% cap). Break-even: A (Visual) beats B only if one rehearsal hour buys Visual
headroom at least 1.093x as efficiently as Music (rate k = 1.0926); the two real seasons straddle that threshold. Efficiency of
an hour is a DISCLOSED ASSUMPTION; the data (scores, headroom) are real.

**Thin spine skills (n<=2) it would close.**
- `statistics-and-probability-how-to-find-a-missing-data-element-given-the-mean-and-the-remaining-` (n=1; spine id is truncated in the file, pull full id from standards_spine.json) — the needed final-judge score given the mean of the other judge scores (2025 Music Analysis is a two-judge mean; Visual/GE are judge sums).
- `statistics-and-probability-how-to-create-a-box-and-whisker-plot-given-a-set-of-data` (n=1) — plot the 12 corps' Visual (or the 24 judge sub-scores) to show spread.
Plus ratio/percent/decimal subtraction (already covered). 2 thin skills, n<=2 preferred met.

**Data feasibility: HIGH.** Official DCI recaps, free, live, multi-season, student-explorable (compare any adjacent pair).
Caveats: DCI site shows a conflicting 98.750 summary block (use the recap, state it); judge-level 2026 table is flattened
(2025 judge-level table was readable); sub-caption names/judges are real people, so use only caption totals, not judge names.
Safe on SPEC §6 (no harm stakes). No private individuals.

---

### C2 — Two Ways to Hold 2.5 mph · tier T2 · data grade MEDIUM-HIGH (metric NEEDS WORK)

**Protagonist.** Constructed: Luz Ferreira, band director of a fictional high-school band marching the Rose Parade route.
**Dilemma.** The route is 5.5 miles at a ~2.5 mph parade pace (Old Pasadena, fetched). A) 8-to-5 (22.5 in) at 120 bpm
(the band's repertoire tempo) OR B) 6-to-5 (30 in) at 88 bpm.
**Computed:** A = 2.5568 mph, 129.1 min, 15,488 steps, drifts 220 yd ahead of a 2.5-mph unit over 2.2 h; B = 2.5000 mph exactly,
132.0 min, 11,616 steps (25.0% fewer), 0 drift. (8-to-5 matching 2.5 mph exactly is 117.33 bpm.) 
**Problem (be honest):** I could NOT find a single metric where both win: B matches pace and takes fewer steps, but 88 bpm is a
26.7% slower tempo than repertoire and a 30-in stride is larger than the "standard" 22.5. No verified data on stride fatigue or
repertoire tempo, so the cross-over would rest on an assumption. Margin is NOT proven <=20% — fails hard requirement 1 as it stands.
Spine: unit conversion (covered, n>2), rate/proportion; no thin skills. Treat as backup only.

---

### C3 — Ring of Forty-Eight · tier T2 · data grade MEDIUM (metric NEEDS WORK)

**Protagonist.** Constructed: Amir Kasprzak, drill writer for a fictional HS band. **Dilemma.** A 48-performer ring at a 45-in
interval (interval is an authored design choice, UNVERIFIED as a standard): A) 12-gon (4 per side, 12 corners) OR B) 16-gon
(3 per side, 16 corners). R = 48*45/(2*pi) = 343.8 in (28.6 ft; fits easily inside the 160-ft field width).
**Computed (sagitta = R(1-cos(pi/n)) vs half of a 22.5-in step = 11.25 in):** 12-gon 11.71 in = 104.1% (misses by 4.1%);
16-gon 6.61 in = 58.7%; 8-gon 26.17 in (232.6%); 24-gon 2.94 in (26.1%). 12-gon passes only if R <= 330.2 in, i.e. N <= 46 at 45 in
(or interval <= 43.2 in at N=48). Area retained vs circle: 12-gon 95.5%, 16-gon 97.5%.
**Problem:** error falls monotonically with n, so 16-gon dominates on visual accuracy; the only offset (fewer corners to teach)
has no sourced cost. Fails requirement 1 without an assumed cost per corner. Skills it would touch (n=1): `geometry-n-gon`,
`geometry-decagon`, `geometry-dodecagon`, `geometry-concave` (terms; low how-to weight). Could be repaired if the case fixes a rehearsal
budget of corners, but that would be an invented constant.

---

## Ranking and recommendation
1. C1 — only concept with live HIGH data, recomputed arithmetic checks, and cross-over proven on real adjacent-pair data (headline margin 8.5%; break-even k=1.093).
2. C2 — good real-world anchor (verified 5.5 mi, 2.5 mph, 22.5/30 in), metric unresolved.
3. C3 — clean geometry, but dominance problem.
**Recommend C1.** Open flags for R1: (a) GE exclusion rationale; (b) real corps names vs anonymization; (c) rehearsal-efficiency k is an assumption.
