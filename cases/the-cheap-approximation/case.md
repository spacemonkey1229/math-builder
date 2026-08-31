# Case Study: The Cheap Approximation

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Naomi Kessler has two blinking dev boards on her desk, each hooked to the same aluminum enclosure through a ribbon cable, and neither number on either screen agrees with the other one after the environmental chamber cycles down toward its cold setpoint. On one laptop tab sits a firmware branch that solves the sensor's nonlinear curve on the fly, a handful of multiply-and-add instructions tucked into the read routine. On the other tab sits a second branch that never solves anything — it just looks the answer up, one flash-memory row at a time, and blends between neighbors. Both branches pass on the bench at room temperature. Neither has been proven at the two ends of the part's accuracy-guaranteed range yet, and the release train for the calibration firmware locks at the end of the week.

A coin-cell-powered field node doesn't get a wall outlet or a heatsink; every extra CPU cycle Naomi burns on math is a cycle the battery pays for, and every extra byte she reserves for lookup data is a byte some other feature on the part doesn't get. Her manager wants one branch merged, not both, before the flash image ships to the pilot customer, whose units sit unconditioned in attics and equipment enclosures — spaces that swing from a near-freezing morning low to a scorching mid-afternoon high, but never see a walk-in freezer's or an industrial oven's extremes. The chamber cycles past its cold setpoint again, and the two boards' readings drift a little further apart on her screen. Naomi pulls up both branches side by side, cursor hovering over the merge button on one of them, and does not click yet.

---

## Background

Naomi Kessler is a firmware engineer at a sensor manufacturer, responsible for the calibration code that converts a temperature sensor's raw analog-to-digital reading into a degrees-Celsius output before it ever leaves the chip. The sensor element itself is a thermistor, a component whose electrical resistance changes with temperature along a curve that is smooth but genuinely nonlinear — a straight-line fit is only good near the point where it was calibrated, and gets progressively worse the farther a reading strays from that point. Naomi's part ships in a coin-cell-powered field sensor with no wall power, so every choice about how the chip performs that conversion trades directly against battery life, and the part's flash memory is shared across several firmware features, not reserved for calibration data alone — on this particular pilot run, calibration data is squeezed down to just a handful of spare bytes once the wireless stack, drivers, and bootloader take their share (SEE APPENDIX C).

Two firmware branches are under consideration for the release, and Naomi's recommendation decides which one ships (SEE APPENDIX A).

**Option A — The Series Path.** The firmware works out the sensor's degrees-Celsius conversion by evaluating a 2nd-order Taylor series expansion of the thermistor's nonlinear response curve, centered at the sensor's factory calibration point, directly on-chip. The math costs only a handful of CPU cycles per reading and uses no additional flash memory (SEE APPENDIX B), but a low-order Taylor expansion is exact only at the point it was expanded around — the farther a real-world reading sits from that center point, the more the approximation can drift from the thermistor's true response (SEE APPENDIX A).

**Option B — The Table Path.** The firmware stores the thermistor's full nonlinear response curve as a lookup table of point measurements in flash memory, then linearly interpolates between the two nearest table entries whenever a real reading falls between them. A finer table — more entries spaced more closely together — tracks the true curve more faithfully at every point, including the extremes, but consumes more of the part's limited flash budget for every entry added, and reading flash and interpolating both cost CPU cycles the Series Path doesn't spend (SEE APPENDIX B, APPENDIX C).

What Naomi's release train needs is not the branch with the least error, full stop, and not the branch that runs fastest, full stop — it is the branch that buys the most accuracy at the sensor's rated operating extremes for every microsecond of on-chip compute time it spends getting there. The thermistor's published datasheet and the target microcontroller's own cycle-timing tables anchor the figures below; every hard number in this case is either sourced with a citation (SEE APPENDIX D) or, where no public figure exists, stated openly as a Modeling Assumption once research is complete (SEE MODELING ASSUMPTIONS).

The vocabulary and "how to…" skills this case will ask you to research are listed in Appendix E — that is where Challenge 1 sends you.

---

## Dilemma

You are Naomi Kessler.

Do you:

**A.)** Ship the Series Path — compute a 2nd-order Taylor series approximation of the sensor's response curve on-chip for every reading **OR**

**B.)** Ship the Table Path — store the sensor's full response curve as a flash-memory lookup table and interpolate for every reading

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A Taylor series derivation.** Derive the 2nd-order Taylor series of the sensor's response function, expanded at the calibration center point given in Appendix A, showing every term and coefficient of your expansion.
- **D2 — A convergence check.** Apply a convergence test to the full (non-truncated) Taylor series of the same response function, and state the interval of temperatures over which it is guaranteed to converge — checked against Appendix A's full rated operating range.
- **D3 — An error-at-the-extremes table.** Using D1's 2nd-order approximation, compute the degrees of error between the approximation and the thermistor's true response value at each end of the rated operating range in Appendix A.
- **D4 — A compute-time table.** Using Appendix B's cycle-timing spec, compute the on-chip evaluation time, in microseconds, for the Series Path's 2nd-order polynomial (from D1) and for the Table Path's lookup-plus-interpolation, at the table resolution Appendix C's flash budget allows.
- **D5 — A degrees-of-error-per-microsecond comparison and recommendation.** Combine D3's error figures with D4's compute-time figures into the case's primary metric for each option, and recommend which path Naomi should ship.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Thermistor Datasheet: Nonlinear Response Curve & Accuracy Spec

The sensor element is an NTC (negative-temperature-coefficient) thermistor. Its resistance-to-temperature relationship is commonly modeled by the Steinhart-Hart equation, a well-established nonlinear model that thermistor manufacturers publish as three fitted coefficients:

**1/T = A + B·ln(R) + C·[ln(R)]³**, where T is temperature in kelvin and R is the thermistor's resistance in ohms.

The sensor's response function — the function D1 asks you to expand — is temperature as a function of **ln(R)**, not of R directly: T(u) = 1/(A + Bu + Cu³), where u = ln(R). This is the natural variable the manufacturer's own coefficients are fitted to (see the equation above), and it is the variable your Taylor expansion in D1 must be taken with respect to.

| Quantity | Value |
|---|---|
| Thermistor part / manufacturer referenced | Omega Engineering 44000 Series precision thermistor element, Model 44004 (2252 Ω nominal at 25 °C) [S1] |
| Steinhart-Hart coefficient A | 1.468 × 10⁻³ [S2] |
| Steinhart-Hart coefficient B | 2.383 × 10⁻⁴ [S3] |
| Steinhart-Hart coefficient C | 1.007 × 10⁻⁷ [S4] |
| Factory calibration / Taylor-expansion center point, °C (i.e. u₀ = ln(R at 25 °C)) | 25 °C [S5] |
| Rated accuracy-guaranteed operating temperature range, °C | 0 °C to 70 °C [S6] [S11] |
| Rated accuracy tolerance at the operating extremes, °C | ±0.20 °C, at both 0 °C and 70 °C [S7] |

Referenced from Background and forces the Taylor-series derivation and error calculation in Challenges D1–D3.

---

## Appendix B — Microcontroller Cycle-Timing Spec

The Series Path and the Table Path both run on the same target microcontroller. Its published cycle-timing table sets how many CPU cycles each option's arithmetic actually costs, and its clock speed converts cycles into microseconds.

| Quantity | Value |
|---|---|
| Target microcontroller identified for this coin-cell part | STMicroelectronics STM32L011F4 (Arm Cortex-M0+ ultra-low-power MCU) [S8] |
| Clock speed, MHz | 32 MHz [S9] |
| Cycles per multiply instruction | 1 cycle (MA1) |
| Cycles per add instruction | 1 cycle [S10] |
| Cycles for one flash-memory read access | 3 cycles (MA2) |
| Operations the Series Path's 2nd-order polynomial requires (Horner form) | 2 multiplies + 3 adds |
| Operations the Table Path's lookup-plus-interpolation requires | 2 flash reads + 1 multiply + 2 adds |

Referenced from Background and forces the compute-time calculations in Challenges D4 and D5. The
operation counts above are fixed by each path's arithmetic structure, not a modeling choice — a
2nd-order polynomial evaluated in Horner form is always 2 multiplies and 3 adds regardless of its
coefficients, and linear interpolation between two stored points is always 2 reads, 1 multiply,
and 2 adds regardless of table size.

---

## Appendix C — Flash Memory Budget for Calibration Data

The Table Path's lookup table competes for flash memory against every other firmware feature on the part. How many table entries fit, and how closely spaced they can be across the rated operating range (Appendix A), depends on this budget.

| Quantity | Value |
|---|---|
| Flash memory budget reserved for calibration data, bytes | 6 bytes (MA3) |
| Bytes required to store one lookup-table entry | 2 bytes (MA4) |

Referenced from Background and forces the table-resolution calculation feeding Challenge D4.

---

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author where no public figure exists for this fictional firmware project's own internal specs.
> A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Cycles per multiply instruction | 1 cycle | The Arm Cortex-M0+ Technical Reference Manual (Table 3-1) states a `MULS` instruction costs "1 or 32" cycles, because a silicon vendor may implement the multiplier as either a fast single-cycle array or a 32-cycle iterative multiplier — an implementation choice the core manual leaves open. Which variant STMicroelectronics chose for the STM32L011 could not be confirmed from a fetchable public document. This case assumes the fast single-cycle multiplier. | If the part instead uses the 32-cycle iterative multiplier, the Series Path's evaluation time grows from 2 multiplies × 1 cycle to 2 × 32 = 64 cycles for that part alone — a roughly 13× increase in its total on-chip time. The Series Path still spends far fewer cycles than a single flash read costs, so this does not flip the recommendation, but it substantially narrows the compute-time gap between the two options. |
| MA2 | Cycles for one flash-memory read access | 3 cycles | The Arm Cortex-M0+ TRM gives `LDR` as 2 cycles under its own explicit "zero wait-states" assumption; any nonzero flash latency above that baseline is a silicon-specific fact set by the vendor's flash controller, not specified in the core manual. This case adds 1 wait-state cycle at the MCU's 32 MHz maximum clock — the smallest nonzero addition possible — since the STM32L011's own flash-timing table could not be reached in this research pass. | A larger wait-state count (2–4 cycles is typical for ultra-low-power parts running near their top clock speed) makes the Table Path's per-reading cost grow roughly linearly, since it spends two flash reads per lookup. This is the single assumption most likely to matter to D4 and D5 if revisited. |
| MA3 | Flash memory budget reserved for calibration data | 6 bytes | No public memory map exists for this fictional firmware project. An earlier scoping pass assumed 64 bytes (a modest slice of the STM32L011F4's real, published 16 Kbyte total flash) and found the Table Path won so overwhelmingly, at every budget size from 3 to 256 entries, that the case was not a genuine dilemma. 6 bytes reflects a genuinely flash-starved coin-cell part, where the wireless stack, drivers, and bootloader consume nearly all of the part's flash and calibration data is squeezed into the last few spare bytes — giving 3 table entries at 2 bytes each (MA4). | This is the most load-bearing assumption in the case. A modest increase in this budget (e.g. to 8 bytes / 4 entries) noticeably widens the Table Path's advantage, and the original 64-byte budget returns the same lopsided win the case had before the range and budget were revised together. A Hero should treat this figure as worth pressing on directly. |
| MA4 | Bytes required to store one lookup-table entry | 2 bytes | 16-bit fixed-point is a standard width for embedded sensor calibration tables — enough resolution for a temperature reading without spending 4 bytes (float) per entry on a flash-constrained part. | A wider entry (4 bytes) would halve the number of table entries the same MA3 budget allows, roughly doubling the Table Path's interpolation error — still far smaller than the Series Path's D3 error at either extreme. |

---

## Appendix D — Sources

All figures in this case are sourced in this appendix, or, where no public figure exists, stated
openly in the Modeling Assumptions block above.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Thermistor part / manufacturer | Omega Engineering 44000 Series, Model 44004 (2252 Ω @ 25 °C) | Omega Engineering — "44000 Series Thermistor Elements" datasheet ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | MEDIUM |
| S2 | Steinhart-Hart coefficient A | 1.468 × 10⁻³ | Omega Engineering — "44000 Series Thermistor Elements" datasheet, Table 1 ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | MEDIUM |
| S3 | Steinhart-Hart coefficient B | 2.383 × 10⁻⁴ | Omega Engineering — "44000 Series Thermistor Elements" datasheet, Table 1 ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | MEDIUM |
| S4 | Steinhart-Hart coefficient C | 1.007 × 10⁻⁷ | Omega Engineering — "44000 Series Thermistor Elements" datasheet, Table 1 ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | MEDIUM |
| S5 | Calibration / expansion center point | 25 °C | Omega Engineering — "44000 Series Thermistor Elements" datasheet (R25°C nominal-resistance convention) ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | HIGH |
| S6 | Rated accuracy-guaranteed operating temperature range | 0 °C to 70 °C | Omega Engineering — "44000 Series Thermistor Elements" datasheet, Model 44004 spec table ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | HIGH |
| S7 | Rated accuracy tolerance at operating extremes | ±0.20 °C at 0 °C and at 70 °C | Omega Engineering — "44000 Series Thermistor Elements" datasheet, Table 2 (Model 44004, ±0.20 °C class) ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | HIGH |
| S8 | Target microcontroller | STMicroelectronics STM32L011F4 (Arm Cortex-M0+) | STMicroelectronics — STM32L011F4 product page ([link](https://www.st.com/en/microcontrollers-microprocessors/stm32l011f4.html)) | accessed 2026-08-31 | MEDIUM |
| S9 | Clock speed | 32 MHz | STMicroelectronics — STM32L011F4 product page ([link](https://www.st.com/en/microcontrollers-microprocessors/stm32l011f4.html)) | accessed 2026-08-31 | MEDIUM |
| S10 | Cycles per add instruction | 1 cycle (zero wait-state system) | Arm — Cortex-M0+ Technical Reference Manual (DDI 0484B), Table 3-1 ([link](https://www.keil.com/dd/docs/datashts/arm/cortex_m0p/r0p0/ddi0484b_cortex_m0p_r0p0_trm.pdf)) | 2012 (accessed 2026-08-31) | HIGH |
| S11 | Datasheet's own accuracy-spec range, stated directly in prose (not inferred from adjacent table rows) | "...±0.10°C and ±0.20°C from 0 to 70°C (32 to 158°F)" | Omega Engineering — "44000 Series Thermistor Elements" datasheet, p. D-10, "Tolerance Curves" section ([link](https://assets.omega.com/spec/44000_THERMIS_ELEMENTS.pdf)) | undated (accessed 2026-08-31) | HIGH |

Notes on confidence: S1–S4 are graded MEDIUM rather than HIGH because the Omega datasheet carries
no visible revision date in its text, though it is a genuine, currently-published manufacturer
document — every other HIGH-confidence criterion (primary source, unambiguous units, exact figure
needed) is met. S6 and S7 were revised to a narrower range after a full direct fetch of the
datasheet's body text turned up its own explicit prose statement (S11) that its accuracy spec is
guaranteed only "from 0 to 70°C" — the original scoping had instead spliced together two different
spec lines (a 150°C "Maximum Working Temp" and a −80°C "Storage and Working Temp for Best
Stability") that the datasheet never states as one combined range; S6/S7 are now graded HIGH
because they are a direct textual quote and a directly tabulated figure, not an inferred pairing.
S8 and S9 are graded MEDIUM because `st.com` could not be directly re-fetched during this research
pass (repeated timeouts, consistent with bot-protected delivery); the figures are corroborated by
independent distributor listings for the same part number but are not a verified direct read of
the primary page. See RESEARCH_LOG.md for the full search trail, including two placeholders
(cycles per multiply, cycles per flash read) that returned NOT FOUND for this specific
microcontroller and were resolved as Modeling Assumptions instead — see Modeling Assumptions MA1
and MA2 above — and for the full root-cause investigation and fix trail that produced the revised
Appendix A range and Appendix C flash budget.

---

## Appendix E — "How To…" Math Questions To Research

**Vocabulary terms**

- Series
- Taylor Series

**"How to…" questions**

- How to determine whether a series converges or diverges
- How to find the Taylor series of a function at a point
