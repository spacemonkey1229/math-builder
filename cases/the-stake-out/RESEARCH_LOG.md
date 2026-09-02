# Research Log: The Stake-Out

Run: `case-research`, 2026-09-01. 22 open `{{NEEDS_SOURCE}}` tokens enumerated from `case.md`
and cross-checked against `case.json.needs_source[]` and the three specific priorities flagged in
`case.json.open_research_items[]` / `FACILITATOR.md`.

All 22 resolved: 12 SOURCED (real citation), 10 ASSUMPTION (disclosed Modeling Assumption, no
public figure exists). Zero left OPEN. Zero LOW-confidence sources used anywhere load-bearing.

---

## P01 — ACI 117M-10 exact tolerance value (Appendix A) — flagged priority #1

**Searched:** "ACI 117M-10 location displacement tolerance footing 13 mm 1/2 in concrete.org";
direct fetch of concrete.org's own ACI 117M-10 preview PDF; direct fetch of a civilenghub-hosted
sample PDF; direct fetch of theconstructor.org's summary article.

**Found:**
- concrete.org's own preview PDF (`117m-10web.pdf`) fetched directly — contains only front
  matter and the table of contents (pp. 117M-1 through 117M-4). Section 3 "Foundations"
  (which holds 3.2 "Deviation from location") is at p. 117M-25, beyond what the free preview
  exposes. **Genuine primary-source attempt made; document is paywalled beyond the preview.**
- civilenghub's sample PDF fetched directly — content came back compressed/unreadable to the
  fetch tool; no usable table text recovered.
- theconstructor.org (secondary, but names the primary standard and states the figure plainly):
  "greater of 13 mm or 2% of specified dimension" for a foundation dimension ≤ 2.4 m. **Used as
  S2, MEDIUM confidence** — it is a secondary summary, not the primary text itself.
- Independently, at concept-write time, the US-customary companion standard (ACI 117-10, not
  117M-10) was found in a Pennsylvania Dept. of Labor & Industry ICC code-review comment PDF —
  the committee's own Section 3.2.1 text, verbatim: "the greater of ±2% of specified dimension
  or 1/2 in." for a dimension under 8 ft. **Used as S1, HIGH confidence** (primary committee
  text, government-hosted, dated, unambiguous units).
- S1 and S2 corroborate each other in substance and in unit-converted magnitude (1/2 in. =
  12.7 mm ≈ 13 mm; 8 ft ≈ 2.4 m).

**Outcome:** Cited both S1 (primary, US-customary) and S2 (secondary, metric) with the caveat
spelled out in Appendix G. The exact verbatim metric ACI 117M-10 text remains behind ACI's
paywall — this was a genuine attempt at the primary source, not a shortcut past it.

---

## P02 — Footing dimension used in this case (Appendix A)

**Searched:** "typical residential strip footing width inches townhome foundation IRC code
minimum."

**Found:** IRC-derived footing sizing tables (Knox County TN's public 2018 IRC-based table,
itself sourced from IRC Table R403.1) give minimum footing widths by story count and soil
bearing value. Selected: 2-story, light-frame construction, slab-on-grade, 2,000 psf soil =
**12 in.** — a realistic, code-minimum townhome strip footing.

**Outcome:** SOURCED, S3, HIGH confidence.

---

## P03–P06 — Total station model and spec (Appendix B)

**Searched:** "Leica Viva TS16 total station datasheet angular accuracy EDM accuracy pdf";
direct fetch of Leica Geosystems' own datasheet PDF.

**Found:** Leica's own datasheet, fetched directly: angular accuracy options 1″/2″/3″/5″; EDM
accuracy ±(1 mm + 1.5 ppm) single/prism. Selected the 5″ class as the construction-grade option
(the case does not require the survey-control-grade 1″/2″ variants).

**Derived (not published):** combined positional error at a 100 ft (30.48 m) stakeout distance,
by root-sum-square of the angular-linear term (0.74 mm) and the EDM term (1.05 mm) = **≈1.3 mm**.
Marked `derived: true` in spirit (the spec inputs are cited; the combination is case-research's
own arithmetic, shown in Appendix B).

**Outcome:** SOURCED, S4, HIGH confidence.

---

## P07–P08 — GNSS/RTK receiver model and open-sky spec (Appendix C)

**Searched:** "Trimble R12i GNSS receiver datasheet RTK horizontal precision spec"; direct fetch
of Trimble's own datasheet PDF (mirrored by a reseller).

**Found:** ±(8 mm + 1 ppm) RMS, single baseline < 30 km. At this job's assumed short site
baseline (0.5 km), that is 8.5 mm.

**Outcome:** SOURCED, S5, HIGH confidence.

---

## P09 — Exact RTK near-structure multipath degradation magnitude (Appendix C) — flagged priority #3

**Searched:** "RTK GPS multipath error magnitude near building wall reflective surface mm
degradation study"; "GNSS RTK multipath error near building wall cm case study distance meters
reflective"; "Mekik Can multipath effects in RTK GPS and a case study pdf full text"; "Mekik Can
investigation on multipath errors in real time kinematic GPS method results cm error abstract."
Direct fetch attempts on: ResearchGate's paper page (403, blocked), Academia.edu's paper page
(403, blocked), Semantic Scholar's paper page (returned empty), and a ResearchGate figure page
specifically captioned "Positional errors from C Mode and reference observations at 2m distance"
(403, blocked) — this figure looked like it might have been the exact number, but access was
denied on every attempt.

**Found (qualitative, real, peer-reviewed):**
- Mekik, C. & Can, O. (2010), "An Investigation on Multipath Errors in Real Time Kinematic GPS
  Method" / "Multipath Effects in RTK GPS and a Case Study," *Scientific Research and Essays*,
  Vol. 5, No. 16, pp. 2186–2200 — confirmed real via three independent aggregators
  (Semantic Scholar, ResearchGate, Academia.edu), but full text blocked on all three.
- Multiple additional peer-reviewed sources (PMC-indexed GNSS deformation-monitoring papers;
  O'Connor et al. 2024) converge on: multipath-induced carrier-phase error near a reflective
  structure "can reach several centimeters at most."

**Outcome:** Genuine multi-angle search (4 distinct query framings) plus 4 direct-fetch attempts
on the most promising primary sources, all blocked by publisher access control — not a search
failure, an access failure. Per SKILL §5, this is a clean **NOT FOUND** for the exact figure.
**Exit chosen: Modeling Assumption (MA5)**, not redesign or drop — the obstruction's multipath
effect on GNSS is the case's entire second pillar (alongside the total station's blocked
sightline) and cannot be dropped without gutting the dilemma. Value originally used: +25 mm RMS
additional error (root-sum-square with the open-sky spec), chosen as a midpoint of the
literature's "several centimeters" range. **Flagged HIGH sensitivity** — this is the single
assumption most likely to flip the case's recommendation; breakeven computed at ≈13.4 mm, which
sits inside the same documented range the assumption was drawn from.

**RETUNE (2026-09-01, post-`case-readiness`):** at +25 mm RMS the case's margin came out to
47.4%, which exceeds SPEC.md §2's ~20% unbalanced-case cap ("if the better option wins by more
than ~20% on the primary metric, the case is unbalanced and must be retuned by adjusting a
constraint"). Re-derived the literature range from the sources already cited rather than
inventing a new figure: S4 (Leica Viva TS16, combined ≈1.3 mm at 30.48 m — Option A's spec, not
MA5's), S5 (Trimble R12i, ±8 mm+1 ppm RMS open-sky — the baseline MA5 degrades from), and S6/S7
(Mekik & Can 2010; O'Connor et al. 2024 — qualitative "several centimeters," roughly 10–50 mm as
already characterized in `case.json.modeling_assumptions[].MA5` and `FACILITATOR.md`). The
original 25 mm sat at the high end of that 10–50 mm range; nothing in S6/S7 singles out the high
end as the correct point for this specific distance/structure (both are qualitative, not
distance-calibrated), so a lower point in the same real range is at least as defensible.
Solved numerically (root-sum-square combine with the 8.5 mm open-sky spec, then the case's own
2D circular-normal miss-probability model) for the MA5 value that brings margin_pct to ≈20%:
**+17 mm RMS**, giving combined accuracy ≈19.0 mm RMS, GNSS miss probability ≈62.6%, and
margin_pct = 19.9%. Option A (Total Station Polar Staking) still wins.

Note on breakeven direction: this retune moves MA5 *closer* to its ≈13.4 mm breakeven (from
~11.6 mm above it, down to ~3.6 mm above it), not farther from it — lowering MA5 is what shrinks
the margin, since Option B's expected cost rises monotonically with MA5. This means the retuned
case is smaller-margin but *more*, not less, sensitive to a further downward challenge on MA5;
that fragility is now called out explicitly in `case.json.balance.margin_basis`,
`case.json.sensitivity_note`, and `FACILITATOR.md`, including its knock-on effect tightening the
MA3 breakeven (~32 min → ~25.2 min) and MA4 breakeven (~29 min → ~36.7 min). No secondary
assumption (MA3, MA4) needed its own value changed; only their breakeven arithmetic shifted as a
consequence of MA5's retune. See `case.json.modeling_assumptions[]` (MA5) and `FACILITATOR.md`
for the full updated breakeven analysis.

---

## P10–P13, P16 — Site layout & corner data (Appendix D)

**Searched:** these are fixed facts about a specific fictional lot (control-point distances,
corner counts, which corners are obstructed) — no public record can exist for a fictional job
site, so no search was performed beyond confirming this reasoning holds (there is no real
"Lot 4" to look up). **Exit chosen: Modeling Assumption for all five** (MA6–MA9), each with a
stated, defensible basis (realistic residential-lot distances; a documented multipath test-range
distance; a modest multi-unit townhome footprint corner count). None of these are margin-driving
per D6's own per-obstructed-corner framing (see MA8's sensitivity note).

---

## P14 — Base per-point layout time, each method (Appendix E) — flagged priority #2

**Searched:** "total station stakeout productivity minutes per point construction layout
RSMeans"; "total station stakeout minutes per point OR points per hour productivity construction
layout survey"; "Alphageo GNSS RTK 500 points per hour productivity survey stakeout article";
direct fetch of the Alphageo article; direct fetch attempt on an openpr.com press release citing
a "150-point stakeout... 4 to 5 hours" figure (403, blocked, and openpr.com is an unattributed
press-release distribution site — would have graded LOW even if fetched, per SKILL.md's grading
rules, and a LOW figure may not carry a constraint).

**Found:** Alphageo's real, dated, named-publisher article states "a single operator [can]
collect 500 or more points per hour" — but explicitly for open-terrain bulk point collection
(road construction, agricultural grading, large earthworks), not footing-corner stakeout with
verification and marking. No RSMeans or other industry productivity-cost figure with an exact
minutes-per-corner number was found for either method under footing-corner conditions.

**Outcome:** **NOT FOUND** for an exact, task-matched figure for either method. **Exit chosen:
Modeling Assumption for both** (MA1: 6 min/corner, Total Station; MA2: 3 min/corner, GNSS/RTK —
informed by, but explicitly not equal to, the real Alphageo figure, which is cited as directional
context in Appendix E and Appendix G, S8).

---

## P15 — Second total-station setup time (Appendix E)

**Searched:** "total station second instrument setup relocate resection time minutes construction
survey."

**Found:** General descriptions of resection/setup procedure, no timing figures.

**Outcome:** NOT FOUND. **Exit chosen: Modeling Assumption (MA3, 20 min)**, flagged MODERATE
sensitivity — breakeven at ≈32 min.

---

## P17 — Rework time for an out-of-tolerance corner (Appendix E)

**Searched:** "concrete footing rework re-shoot corner cost delay hours construction rebar strip
out of tolerance."

**Found:** General rework-cost ranges for multi-trade construction rework ($5k–$50k, labor
$40–$120/hr), nothing at the single-stake re-shoot granularity this case needs.

**Outcome:** NOT FOUND. **Exit chosen: Modeling Assumption (MA4, 45 min)**, flagged MODERATE
sensitivity — breakeven at ≈29 min.

---

## P18 — GNSS miss probability, derived (Appendix E)

Not a research item — a computed value once Appendix A (tolerance) and Appendix C (degraded
accuracy) were both resolved. Modeled radial position error as a 2D circular-normal distribution
(per-axis σ = combined RMS ÷ √2); P(radial error > 13 mm) = exp(−13²/2σ²). Option A ≈ 0% (its
own accuracy spec is ~10× tighter than tolerance). Option B ≈ 78% at an obstructed corner (its
combined accuracy of 26.4 mm RMS is roughly double the tolerance). Shown with full arithmetic in
`case.md` Appendix E; marked as a derived value in `case.json`.

---

## P19–P21 — Equipment rental rates (Appendix F)

**Searched:** "robotic total station rental rate per day 2026 survey equipment"; "Trimble R12i
GNSS receiver rover rental rate per day survey equipment"; "GNSS rover rental $ per day survey
equipment kit RTK 2026." Direct fetch of a Washington State DES government-hosted rental rate
PDF, and of two KWIPPED marketplace listing pages.

**Found:**
- Total station: Washington State DES's rate sheet names a Topcon Robotic Total Station at
  $275/day (S9); KWIPPED's marketplace average across actual quotes from the last 12 months is
  $269/day (S10) — strong corroboration between an independent government rate sheet and a
  marketplace aggregate.
- GNSS rover: no R12i-specific daily rate was found listed anywhere; KWIPPED's Trimble R12 (same
  product family) listing shows two real, named suppliers at $150/day and $250/day (S11).

**Outcome:** Both SOURCED, MEDIUM confidence (named vendors/marketplaces, real current listings,
but undated rate sheets or marketplace rolling averages rather than a single dated invoice).

---

## P22 — Full source list (Appendix G)

Compiled from S1–S11 above; see `case.json.sources[]` for the complete structured records.

---

## Summary table

| Placeholder | Appendix | Outcome | Confidence |
|---|---|---|---|
| ACI tolerance value | A | SOURCED (S1 primary + S2 secondary corroboration) | HIGH / MEDIUM |
| Footing width | A | SOURCED (S3) | HIGH |
| Total station model/angular/EDM/combined | B | SOURCED (S4) + derived combined-error arithmetic | HIGH |
| GNSS model/open-sky spec | C | SOURCED (S5) | HIGH |
| Multipath degradation magnitude | C | **ASSUMPTION (MA5)** — flagged HIGH sensitivity | — |
| Corner count / obstructed count / distances / deflection angle | D | **ASSUMPTIONS (MA6–MA9)** | — |
| Base layout time, both methods | E | **ASSUMPTIONS (MA1, MA2)** | — |
| Second setup time | E | **ASSUMPTION (MA3)** — flagged MODERATE sensitivity | — |
| Rework time | E | **ASSUMPTION (MA4)** — flagged MODERATE sensitivity | — |
| GNSS miss probability | E | Derived (not a placeholder needing a source) | — |
| Total station rental rate | F | SOURCED (S9 + S10) | MEDIUM |
| GNSS rover rental rate | F | SOURCED (S11) | MEDIUM |
| Full source list | G | SOURCED (compiled) | — |

**NOT FOUND count: 3** (the exact ACI 117M-10 verbatim metric text; the exact multipath
degradation magnitude at a specific distance; the exact base/setup/rework minutes figures) — all
three were anticipated in `case.json.open_research_items[]` at write time, and all three resolved
to disclosed Modeling Assumptions after genuine multi-angle search and direct-fetch attempts, per
SKILL §5. Zero figures were invented, rounded from memory, or laundered with hedge words.

**Next step:** `case-readiness` (per instruction). Facilitator-only: `case.json.balance.margin_pct`
= 19.9% (retuned 2026-09-01 from an original 47.4% — see the MA5 retune entry above), winner =
Option A (Total Station Polar Staking) — a balanced margin under SPEC.md §2's ~20% cap, reported
without softening, but flagged in `FACILITATOR.md` and `case.json.sensitivity_note` as highly
sensitive to MA5 (breakeven ≈13.4 mm, inside the same documented literature range MA5 was drawn
from — and now only ~3.6 mm below the retuned +17 mm value) and secondarily to MA3/MA4 (both
breakevens tightened by the retune).
