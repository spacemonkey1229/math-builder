# RESEARCH_LOG.md — The Cheap Approximation

`case-research` pass. 14 `{{NEEDS_SOURCE}}` placeholders enumerated from `case.md` (Appendix A: 7,
Appendix B: 5, Appendix C: 2). Log below is one entry per placeholder — searched, found/rejected,
final disposition.

---

## Appendix A — Thermistor datasheet

**P01 — Thermistor part / manufacturer.**
Searched: "Vishay NTC thermistor datasheet Steinhart-Hart coefficients A B C" (NTCLE100E3),
"Murata NTC thermistor datasheet Steinhart-Hart coefficients", "TE Connectivity NTC thermistor
Steinhart-Hart coefficients pdf", "Amphenol NTC thermistor Steinhart-Hart coefficients", "YSI
precision thermistor Steinhart-Hart coefficients 44xxx", "US Sensor / Littelfuse Steinhart-Hart
coefficients."
Fetched: Vishay NTCLE100E3 datasheet (vishay.com/docs/29049/ntcle100.pdf, Rev. 07-May-2025) —
publishes only the B25/85 (beta) value per part, not Steinhart-Hart A/B/C; directs users to an
online curve-computation tool instead of a static table. **Rejected as the anchor source** — the
skill requires the actual A/B/C figures to be *published*, not generated on request from a web
tool with no fixed, citable output.
Fetched: Omega Engineering "44000 Series" thermistor-element datasheet
(assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf) — **this one directly publishes a Table 1
"Steinhart-Hart Constants" with A, B, C per model number**, plus a Table 2 tolerance-vs-temperature
curve and an operating/storage temperature spec for the same model numbers. This is the real,
currently-published, primary-source datasheet used to anchor Appendix A.
Selected: **Model 44004** (2252 Ω nominal at 25 °C, ±0.2 °C interchangeability class, 150 °C max
working temp) — chosen because it is the one row in Table 1 that also has a matching row in
Table 2, so the accuracy-tolerance figure and the Steinhart-Hart coefficients come from the same
part number in the same document.
Confidence: **MEDIUM** — genuine manufacturer datasheet, currently live, but the PDF carries no
visible revision date or year in its text (checked via full-text extraction; none found), so the
"carries a date" HIGH-confidence criterion is not met. Grade held at MEDIUM for this reason alone;
everything else about the source (primary, unambiguous units, the exact figure needed) is clean.

**P02–P04 — Steinhart-Hart coefficients A, B, C.**
Same document, same table, same row (Model 44004): A = 1.468×10⁻³, B = 2.383×10⁻⁴,
C = 1.007×10⁻⁷. Confidence MEDIUM (same reasoning as P01 — undated document).

**P05 — Calibration / Taylor-expansion center point.**
The datasheet itself designates 25 °C as thermistor curve reference ("R25°C" appears as the
column header for nominal resistance throughout both tables, and the Steinhart-Hart constants are
explicitly derived from "3 temperature test points" referenced to that same nominal value). Using
25 °C as the calibration center is the datasheet's own convention, not an outside guess.
Confidence: HIGH (unambiguous within the source; this is literally what "R25°C" designates in the
document).

**P06 — Rated operating temperature range.**
Datasheet's own spec table for Model 44004: "Maximum Working Temp: 150 °C (300 °F)" and Table 2's
tolerance curve is tabulated from −80 °C through 150 °C. Used −80 °C to 150 °C as the rated range,
spanning exactly the interval the datasheet itself characterizes. Confidence: MEDIUM (the −80 °C
end comes from the "Storage and Working Temp for Best Stability" line rather than a single
explicit "operating range" label — the datasheet does not use that exact phrase — so this is a
reasonable but not word-for-word reading of two adjacent spec lines in the same table).

**P07 — Rated accuracy tolerance at the operating extremes.**
Table 2 ("Interchangeability Tolerances"), Model 44004 (±0.20 °C class): ±1.00 °C at −80 °C and
±1.00 °C at 150 °C — both temperature extremes, same table, same part. Confidence: HIGH (directly
tabulated, unambiguous, exact match to both stated extremes).

---

## Appendix B — Microcontroller cycle-timing spec

**P08 — Target microcontroller.**
Searched: "STM32L011 datasheet ultra-low-power Cortex-M0+ clock speed flash wait states coin
cell," and confirmed via ST's own product-family page content (surfaced through search, since
direct `WebFetch` of st.com timed out repeatedly — see note below) and cross-referenced against
Digi-Key/Mouser distributor listings for the same part, which independently state "32-Bit 32MHz
16KB (16K×8) FLASH" for STM32L011 parts. Selected **STMicroelectronics STM32L011F4** (Arm
Cortex-M0+ core), explicitly marketed by ST for 1.65–3.6 V operation "suitable for coin cell
applications." Confidence: MEDIUM — the claim is accurate and cross-corroborated by two
independent distributor listings, but `st.com` could not be directly re-fetched within this
research pass (repeated timeouts, likely bot-protection/JS-rendering on ST's site), so it is not a
verified direct fetch of the primary page, only a search-engine synthesis of it plus distributor
corroboration.

**P09 — Clock speed.** Same basis as P08: 32 MHz maximum. Confidence: MEDIUM.

**P10 — Cycles per multiply instruction.**
Fetched (directly, successfully): ARM **Cortex-M0+ Technical Reference Manual** (ARM DDI 0484B),
Table 3-1, "Cortex-M0+ instruction summary." States cycle counts are "based on a system with zero
wait-states," and lists `MULS Rd, Rm, Rd — Multiply — 1 or 32ᵃ` cycles, with footnote (a)
explaining the Cortex-M0+ implements the 32-bit multiply as *either* a fast single-cycle array
*or* a 32-cycle iterative multiplier — an implementation choice each silicon vendor makes, not
something the core TRM itself fixes. Searched specifically for which variant STMicroelectronics
chose for the STM32L0 family (RM0451/RM0377 reference manuals, STM32 community posts) — the
reference manuals are 700+ page documents that repeatedly timed out on direct fetch, and no
community post surfaced a citable, dated confirmation of the multiplier variant for this specific
part. **Result: NOT FOUND** for the vendor-specific choice. **Disposition: Modeling Assumption
(MA1)** — assumes the fast single-cycle (1-cycle) multiplier, anchored to the real, fetched ARM
Cortex-M0+ TRM's documented range, with the 32-cycle alternative flagged explicitly as the
sensitivity case.

**P11 — Cycles per add instruction.**
Same ARM Cortex-M0+ TRM, Table 3-1: `ADDS Rd, Rn, Rm — All registers Lo — Add — 1` cycle
(zero-wait-state system). This is architectural — every Cortex-M0+ implementation, including the
STM32L0 family, uses this exact core, so the figure applies directly. Confidence: **HIGH** (primary
source, ARM's own document, directly fetched and read, unambiguous).

**P12 — Cycles for one flash-memory read access.**
Searched: STM32L0 reference manuals (RM0451, RM0377) for the FLASH_ACR wait-state table; attempted
direct fetch of `st.com`'s hosted PDF (timed out — same bot-protection pattern as P08/P09) and a
Mouser-hosted mirror (redirected to an HTML wrapper, not the PDF itself). Two distinct search
framings ("STM32L0 flash wait states 16MHz 32MHz ACR", "STM32L011 flash access cycles datasheet")
turned up only STM32 community forum threads discussing wait-state *concepts* in general, with no
citable, dated, STM32L011-specific wait-state table reachable within this pass. **Result: NOT
FOUND. Disposition: Modeling Assumption (MA2)** — same ARM Cortex-M0+ TRM gives `LDR Rd,[Rn,#imm]`
as 2 cycles at zero wait-states; this case assumes 1 additional wait-state cycle at the MCU's
32 MHz maximum clock (a single added cycle is the smallest nonzero latency a flash controller can
add, and the TRM's own zero-wait-state caveat makes explicit that *any* nonzero value here is a
silicon-specific fact outside the core TRM's scope), for a total of 3 cycles per flash read.

---

## Appendix C — Flash memory budget

**P13, P14 — Flash budget (bytes) and bytes per lookup-table entry.**
These are facts about *this specific fictional firmware project's* memory map — there is no public
document to search for a project that does not exist outside the case. Not attempted as a search
target; going straight to Modeling Assumption per the skill's guidance that project-internal
figures with no possible public source do not need a "NOT FOUND" search trail.
**Disposition: Modeling Assumption (MA3, MA4)** — 64 bytes reserved for calibration data (a modest
slice of the STM32L011F4's real, sourced 16 Kbyte total flash, consistent with a part that also
carries wireless-stack, driver, and bootloader code sharing the same flash), and 2 bytes per table
entry (16-bit fixed-point, a standard width for embedded sensor calibration tables). Together these
give 32 lookup-table entries across the 230 °C rated range (Appendix A), a table resolution of
about 7.2 °C between neighboring points.

---

## Rejected / considered-and-dropped searches

- Vishay NTCLE100E3 — rejected as the anchor thermistor (see P01): Steinhart-Hart A/B/C not
  statically published, only generatable via an online tool with no fixed citable output.
- Copley Controls AN144 "Thermistor Steinhart-Hart Coefficients for Calculating Motor Temperature"
  — a real, fetched application note, but it derives *example/illustrative* coefficients for a
  generic PTC motor sensor via three-point calibration, not published manufacturer figures for a
  specific catalog part. Not used.
- Generic Steinhart-Hart calculator/blog pages (thinksrs.com, daycounter.com, getzenquery.com,
  Wikipedia) — useful for confirming the equation form, never used as the source of a numeric
  coefficient (LOW-tier, no manufacturer provenance).
- YSI 44xxx / Omega D-7, D-9 series catalog PDFs other than the one used — same underlying
  Steinhart-Hart-constants table format; the 44000-series element sheet actually fetched was
  preferred because it is the cleanest single-document source covering both the coefficient table
  and the tolerance-vs-temperature table for the same part number.

## Fetch reliability note

`st.com` (both the STM32L011F4 product page and the STM32L0 reference-manual PDFs) and one
DigiKey product page returned either a 403 or a 60-second timeout on every direct-fetch attempt in
this pass — consistent with bot-protection/JS-gated delivery rather than the content not existing.
This is why the two MCU-identity placeholders (P08, P09) are graded MEDIUM rather than HIGH despite
being accurate and cross-corroborated, and why P10 and P12 (multiplier variant, flash wait-state
count) could not be pinned to a vendor-specific figure and became Modeling Assumptions instead —
exactly the outcome flagged as expected in this case's brief.

## Verification

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
LOW-confidence sources: []
```

---

# CASE-FIX PASS — 2026-08-31

The `case-research` pass above came back with `margin_pct = 99.86`, winner B (Table Path) by
roughly 730x — flagged by both `case.json.balance.computed_2026-08-31` (original) and
FACILITATOR.md as far above the pipeline's ~20% retune threshold, not a genuine T2 dilemma. This
entry documents the quantitative root-cause investigation and the fix search that followed,
per the case-fix task brief.

## Part 1 — Quantitative root cause

Using the real, sourced Steinhart-Hart coefficients (Model 44004: A=1.468e-3, B=2.383e-4,
C=1.007e-7) and the real MCU cycle-timing figures already in case.json, computed the 2nd-order
Taylor series error T_2(u) - T(u) directly (T(u) = 1/(A+Bu+Cu^3) - 273.15, u=ln(R), expanded about
u0=ln(R at 25C)) at 5C steps from -80C to 150C. Confirmed the research agent's headline numbers
exactly: **+21.43C at -80C, -9.84C at 150C**.

**Is the error driven by distance-in-Celsius or distance-in-u?** Computed |u - u0| at each
temperature: 6.60 at -80C vs. only 3.99 at 150C — despite -80C being *closer* to 25C in Celsius
terms (105C away) than 150C is *farther* (125C away). The error is asymmetric in exactly the
opposite direction of raw Celsius distance, because this is an NTC thermistor: resistance rises
steeply at cold temperatures and only gently falls at hot ones, so u=ln(R) is stretched on the cold
side and compressed on the hot side of the curve. This confirms the error is fundamentally an
error in **log-resistance space**, not degrees-C space — the case's own choice to expand in
u=ln(R) (the Steinhart-Hart equation's natural variable) is correct and unavoidable, but it means
"symmetric degrees from center" is not what drives the blowout.

**Does the truncation order matter, independent of range?** Computed 3rd/4th/5th/6th-order Taylor
expansions of the same T(u) (via symbolic differentiation, `sympy`) at the same u0. Results (worst
abs error across -80C to 150C):

| Order | Error at -80C | Error at 150C |
|---|---|---|
| 2 | 21.43 | -9.84 |
| 3 | -10.34 | -2.86 |
| 4 | 4.96 | -0.83 |
| 5 | -2.38 | -0.24 |
| 6 | 1.14 | -0.07 |

Error falls by roughly half an order of magnitude per additional order — consistent with a
Lagrange remainder scaling as (u-u0)^n, and confirms the case's forced "2nd-order" choice, not the
Taylor-series concept itself, drives most of the blowout at this range. Even 6th order barely
clears a ±1C spec at the cold extreme, though.

**Does the full series even converge over this range?** Found the singularities of
1/(A+Bu+Cu^3) by solving A+Bu+Cu^3=0 (`numpy.roots`): one real root at u≈-6.07, a complex-conjugate
pair at u≈3.03±48.93i. Nearest-singularity distance from u0 (radius of convergence) ≈13.79 — more
than double the max |u-u0|≈6.60 needed to cover the *original* full -80C/150C range. **Conclusion:
the full (non-truncated) series converges comfortably everywhere in the operating range,
regardless of how that range is scoped. Convergence was never the problem.** The 2nd-order
truncation's accuracy near the range edges was the problem — a distinct calculus concept from
convergence, which is exactly the distinction the case's D2-vs-D3 challenge structure is designed
to surface (see FACILITATOR.md Socratic question 2, unchanged by this fix).

**Does the Table Path's structural advantage hold at every table size?** Modeled the Table Path's
worst-case piecewise-linear interpolation error (dense numerical scan of the true response function
against a uniform-in-u N-node table) for N=2 through N=256 over the original -80C/150C range:
N=8 gives ~1.96C, N=32 gives ~0.12C, N=256 gives well under 0.01C — while its per-reading compute
cost (2 flash reads + 1 multiply + 2 adds = 9 cycles) is fixed regardless of N. This confirms the
research agent's structural diagnosis: because Table's cost doesn't scale with size while its error
shrinks with size, it wins the degrees-of-error-per-microsecond metric at essentially any
"reasonable" table size over the full range, and only a genuinely degenerate table (N=2, just the
two endpoints) brings its ratio down anywhere near the Series Path's over that range.

**Answer to the framing question:** the 2nd-order-and-single-point concept is not *fundamentally*
unsalvageable — the full series converges fine, and going to 4th-6th order helps a lot — but forcing
2nd order over a genuinely 105C-wide span centered 55-80C off-center in log-resistance space is a
mis-scoping, not a law of nature. The real fix, per the task brief's stated preference order, is to
find a real, narrower, sourced range where 2nd order genuinely competes (Part 2), since re-deriving
the case around a higher Taylor order would also require rewriting Challenge D1's "2nd-order"
instruction and does not, by itself (tested above), close the gap against a generously-provisioned
Table Path anyway.

## Part 2 — Fix search

**Option 1 tried first (task's stated preference): a real, differently-scoped operating range.**
Re-fetched the full body text of the Omega 44000 Series datasheet directly (not just the two
tables originally extracted) — `assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf`. This turned up
text the original research pass had not quoted: under "Tolerance Curves" (p. D-10), the datasheet
states plainly, "we list two basic accuracy/interchangeability specifications for our thermistors,
±0.10°C and ±0.20°C **from 0 to 70°C** (32 to 158°F)... The accuracy specification of ±0.1% or
0.2% means that each thermistor's resistance will fall within these limits **between 0 and 70°C**."

This means the original Appendix A range (-80C to 150C, S6 in the original pass) was never a
single figure the datasheet states — it spliced two different spec lines from the same "To Order"
table: "Maximum Working Temp" (150C, an absolute ceiling, not an accuracy claim) and "Storage and
Working Temp for Best Stability" (-80 to 120C, a stability/storage claim, not an accuracy claim,
and inconsistent with the 150C ceiling on its own upper end). The datasheet's *actual*
accuracy-guaranteed range, stated in its own words, is **0C to 70C** — a genuinely real, sourced,
narrower range for the exact same real part (Model 44004), corresponding to an indoor or
equipment-enclosure-type application rather than a walk-in-freezer/cryogenic one. This directly
matches the task brief's Option 1 (a real narrower-range application of the same real product).

Re-ran the 2nd-order series error calculation over 0C-70C: **+0.169C at 0C, -0.667C at 70C**
(worst case 0.667C at the hot end — the tolerance at both ends per Table 2 is ±0.20C, so even this
narrower, real range does not make the 2nd-order series *pass* the accuracy spec, it just brings
its miss down from tens of degrees to sub-degree, which is the honest, computed result, not
softened).

**Checked whether narrowing the range alone closes the D5 margin — it does not.** Re-ran the Table
Path's error model over 0C-70C at the case's *original* 32-entry (64-byte) table: worst-case error
~0.005C, giving D5_table ≈ 0.018 C/us vs. D5_series ≈ 4.27 C/us — margin ≈99.6%, an even *more*
lopsided landslide than the original scoping, because a fine table over a narrow range is even more
accurate than the same table over a wide one, while the Series Path's cost is unchanged. **Range
alone, holding the original flash budget fixed, cannot produce a genuine dilemma** — this
confirmed the task brief's warning that closing this case might require more than one lever.

**Option 2 (higher-order Taylor / piecewise) checked, not adopted as the primary fix.** Per Part
1's table, 4th-6th order series bring the D3 error down substantially, but even paired with the
narrower 0-70C range, a Horner-scheme series of any order tested (2 through 6) costs at most 13
cycles (0.41us) against the Table Path's fixed 9 cycles (0.28us) — and the Table Path's error over
the narrow range is already so small (sub-0.1C at any reasonable N) that raising the series order
alone still leaves Table winning overwhelmingly. Also rejected as the *primary* fix because
Challenge D1 explicitly requires deriving "the 2nd-order Taylor series" — changing that would touch
the case's core skill-target language for no payoff, since it doesn't close the margin on its own
(see Part 1 for the specific numbers tested).

**Option 3 (tighter, more realistic flash budget) — the lever that actually closes the gap, used
in combination with Option 1.** Re-examined MA3 (flash budget for calibration data), which the
original pass had already flagged in its own sensitivity note as "the only direction that could
narrow the gap." The original 64-byte assumption was never sourced (no public memory map exists for
this fictional project) — it was always a disclosed Modeling Assumption, so tightening it is
explicitly within the case-fix task's sanctioned scope (task brief Option 3). Tested MA3 values
from 2 to 32 bytes (1 to 16 entries) against the *revised* 0-70C range:

| MA3 (bytes) | N entries | Table worst-case error (C) | D5_table (C/us) | Margin vs. D5_series=4.27 | Winner |
|---|---|---|---|---|---|
| 4 | 2 | 3.54 | 12.59 | 66% | A (series) |
| 6 | 3 | 1.03 | 3.68 | **13.97%** | **B (table)** |
| 8 | 4 | 0.49 | 1.73 | 60% | B |
| 12 | 6 | 0.18 | 0.65 | 85% | B |
| 16 | 8 | 0.10 | 0.34 | 92% | B |
| 64 (orig.) | 32 | 0.005 | 0.018 | 99.6% | B |

**6 bytes (N=3 table entries) is the value adopted** — it produces `margin_pct ≈ 13.97`, winner B,
comfortably inside the pipeline's normal range for other published cases (most sit between 5% and
20%; see the case index). It is a defensible, if stringent, real-world assumption: a coin-cell part
whose flash is mostly consumed by a wireless stack, drivers, and bootloader, leaving calibration
data squeezed into a single-digit-byte remainder — explicitly disclosed as MA3 in case.md and
case.json, not presented as a sourced fact. The table's worst-case error at N=3 occurs near the
interval's midpoint (~50C), not at either endpoint (which are themselves exact table nodes with
zero error by construction) — this nuance is recorded in `case.json.balance.computed_2026-08-31`.

**Note on stability of the fix.** This margin is sensitive to MA3 in both directions (8 bytes
already reopens a ~60% margin for B; the original 64 bytes returns the ~99% landslide) — flagged
explicitly in FACILITATOR.md and in MA3's own sensitivity note in case.json/case.md, per the
requirement to record the *direction* of sensitivity, not manufacture false precision. A Hero
challenging the 6-byte figure as unrealistically small is raising a legitimate point, exactly the
kind of "Modeling Assumption may be challenged in discussion" case this format is designed for.

## Disposition

- Appendix A operating range: **-80C to 150C → 0C to 70C**, re-sourced to S6/S7 (revised) plus new
  S11, all now HIGH confidence (direct textual quote + directly tabulated values), up from MEDIUM.
- Appendix C flash budget (MA3): **64 bytes → 6 bytes**, remains an explicitly disclosed Modeling
  Assumption, not claimed as sourced.
- `margin_pct`: **99.86 → 13.97**. `winner`: B (Table Path), unchanged.
- `new_coverage` (calculus-taylor-series, calculus-how-to-find-the-taylor-series-of-a-function-at-
  a-point): unaffected — D1 still requires a 2nd-order Taylor derivation at the same real
  calibration center point (25C), just checked against the revised, real, narrower range.
- case.md Overview/Background narrative revised to match the real 0-70C scoping (an
  attic/equipment-enclosure coin-cell sensor rather than a walk-in-freezer/cryogenic one) — the
  math and sourcing drove this change, not the reverse.

## Verification (post-fix)

```
case.json valid JSON: yes
new_coverage unchanged: yes (2 skills, both still closed by this case)
margin_pct: 13.97 (was 99.86)
winner: B (unchanged)
all Appendix A/C figures in case.md cross-checked against case.json sources/modeling_assumptions: yes
```
