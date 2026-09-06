# RESEARCH_LOG.md — The Correction Window

One row per `{{NEEDS_SOURCE}}` placeholder from `case-write`: what was searched, what was found
or rejected, and the final disposition (SOURCED / ASSUMPTION / DROPPED / plain scenario
constraint). See `case.json.sources[]` and `.modeling_assumptions[]` for the resolved values.

## Appendix A — The Flight Computer and the Correction Loop

**P01/P02 — flight-computer model and CPU clock speed.** Searched for a real Cortex-M4-based MCU
genuinely used in flight-controller boards, since the concept sheet names ARM CMSIS-DSP / STM32
HAL as the expected real-world grounding. Found the STM32F405, a widely used flight-controller MCU
(confirmed via multiple independent hobbyist/engineering sources describing STM32F405-based flight
controllers), with a primary manufacturer datasheet (ST, `dm00037051.pdf`) stating a maximum core
clock of 168 MHz. **SOURCED as S1, HIGH confidence** — primary manufacturer datasheet, current
revision, unambiguous units (MHz), and the exact figure the case needs (not a proxy).

**P03 — whether arithmetic/multiply/FMA instructions execute in a single clock cycle on this
core.** This was flagged at concept approval as the case's core sourcing risk (the "ARM CMSIS-DSP
/ STM32 HAL ship exactly this as a compile-time constant" claim). Search tiers:
1. Tier 1 attempt: ARM's own Cortex-M4 Technical Reference Manual (`developer.arm.com` /
   `support.arm.com`, `ddi0439/b/BEHJADED`). The page did not render extractable prose text via
   automated fetch (JS-driven documentation portal) — logged as inaccessible, not as evidence of
   absence.
2. Tier 1 fallback: found and fetched a primary Arm-published PDF white paper, "The DSP
   capabilities of Arm Cortex-M4 and Cortex-M7 Processors" (T. Lorenser, Arm, Nov 2016), hosted at
   `community.arm.com`. Read in full (19 pages). Page 6 states directly: *"All of the instructions
   are single-cycle on Cortex-M4 (except hardware divide)."* Page 18 documents `VMLA`/`VMLS`
   (floating-point multiply-accumulate) as single arithmetic instructions.
3. Cross-checked against Wikipedia's ARM Cortex-M article, which independently states "DSP
   extension: Single cycle 16/32-bit MAC" for the Cortex-M4 — consistent secondary confirmation,
   not used as the primary citation.

**SOURCED as S2, HIGH confidence** — a real, dated, primary Arm publication states the claim
directly, not a fabricated cycle-count table. This is the exact category of real, citable
embedded-systems fact the concept sheet asked the research pass to genuinely try to find before
falling back to an assumption — it did not require a fallback.

**P05/derived — a real, documented flight-control loop rate.** Searched for STM32-based flight
controller loop-rate practice. Found Betaflight's own configuration documentation
(`betaflight.com/docs/wiki/app/configuration-tab`), which states the gyro locks to 8 kHz for the
common MPU6000 gyro, and that "it's usually best to have [PID] set to the same frequency as the
gyro, or half of it if you are using a slower MCU ... (8KHz gyro would be 4KHz PID loop on an
F411)" — explicitly implying the STM32F405 class of MCU used in this case (S1, the faster of the
two named) can hold the full 8 kHz rate. **SOURCED as S3, MEDIUM confidence** — real, primary,
dated project documentation, but describing racing-drone firmware practice in general, applied
here as a real-world proxy for "a flight-control loop of this kind genuinely runs this fast on
this class of hardware," not as a literal claim that Mara's fictional rescue drone runs Betaflight.
No source publishes a loop-rate figure for a purpose-built search-and-rescue canyon drone, and a
second search pass (academic UAV-control-loop literature, confined-space multirotor control
papers) confirmed none is expected to exist for a fictional mission profile.

**Canyon transit time (90 seconds).** Not sourced or treated as a Modeling Assumption — this is a
plain stated scenario constraint, the same category as the-deferred-repair's "three more years."
It was checked against `sensitivity_model.py` and confirmed to cancel out of the
metric(A)/metric(B) ratio entirely (it multiplies both builds' total compute cost equally), so it
carries no dilemma-flipping risk and does not need MA-style sensitivity disclosure.

## Appendix B — The Canyon Corridor

**Required offset from canyon wall (15 feet).** This is the concept sheet's own fixed scenario
constraint (stated directly in the approved concept), not an independently sourceable real-world
figure for a fictional canyon. Recorded as a plain scenario constraint and used as the basis for
deriving MA2's tolerance.

## Appendix E — Canyon Gusts, Correction Tolerance, and the Error-vs-Cost Trade-off

**Gust-tilt band distribution (MA1).** Searched multiple framings: "small quadrotor UAV wind gust
tilt angle degrees," "confined canyon corridor flight response," "urban canyon UAV aerodynamic
disturbance," and fetched search summaries covering wind-gust estimation papers (ResearchGate,
ScienceDirect, MDPI Drones/Aerospace journals) on quadrotor gust response and confined-space
flight. Findings: this is a real, actively studied problem (gust estimation via tilt-angle
prediction, confined-space aerodynamic disturbance from proximity effects), but **no source
publishes a per-canyon or per-mission gust-tilt-angle frequency distribution** for any real or
fictional corridor — this is inherently a forecast of conditions specific to one flight that has
not happened, not a measurable historical dataset. Confirmed NOT FOUND after a genuine multi-tier
search, exactly as anticipated at concept approval. **Resolved as a stated Modeling Assumption,
MA1** — shape grounded in the general, well-documented atmospheric-turbulence fact that small
perturbations occur far more often than large ones; specific percentages (40/27/20/10/3) are the
case author's own scenario choice, disclosed openly and swept by Tier 2 P5.

**Correction-error tolerance (MA2).** Searched for a published station-keeping or trajectory-error
tolerance standard for small UAVs in confined spaces (aviation/UAV standards bodies, FAA UAS
guidance, academic precision-hover control papers). Found general precision-hovering research
(e.g., studies of sub-meter and sub-decimeter hover-hold accuracy) but nothing that states an
acceptable *sin(theta) approximation error* specifically — this is a case-internal derived
tolerance, not an independently measurable industry figure, and no genuine search was expected to
find one. **Resolved as a stated Modeling Assumption, MA2**, derived transparently from Appendix
B's 15-foot wall offset (a sin(theta) error of 0.0003 implies roughly a 0.05-inch lateral
positioning miscalculation at that range) rather than presented as if measured.

## Supplemental appendix materials

No additional supplemental materials (news article, Desmos graph, Google Maps route) were added in
this pass. A Desmos graph plotting sin(theta) against both Taylor polynomials would be a natural
Challenge 2 visual-display aid and is noted as a good candidate for a Hero's own Challenge 2
research, but is not required by any Challenge 3 deliverable and was not added as case-authored
content to avoid pre-building the D5 visual for the student.

## Summary

| Placeholder | Disposition |
|---|---|
| P01/P02 flight computer + clock speed | SOURCED — S1 (ST datasheet, HIGH) |
| P03 single-cycle arithmetic | SOURCED — S2 (Arm white paper, HIGH) |
| P05 correction-loop rate | SOURCED — S3 (Betaflight docs, MEDIUM, proxy) |
| Canyon transit time | plain scenario constraint (not sourced, not an MA — cancels in the ratio) |
| Wall offset (15 ft) | plain scenario constraint (concept-given) |
| Gust-tilt band distribution | ASSUMPTION — MA1 |
| Correction-error tolerance | ASSUMPTION — MA2 |

Zero placeholders remain OPEN. Zero figures were fabricated or presented as sourced without a
real citation.
