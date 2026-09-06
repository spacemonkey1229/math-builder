Case Study: The Correction Window
MS | Math | Case Study | 2026 | Launchpad

## Overview

The rock walls fill both edges of Mara Yun's control-tablet feed, close enough that the drone's downwash kicks up a fine dust off the sandstone. Her headset crackles: base camp confirming the light is going, and that this is the only pass the battery budget allows before the crew has to fall back for the night. Somewhere below the canyon rim, a thermal camera is sweeping side to side, hunting for the one heat signature that matters — Dana Osei, the trail counter who didn't check in after yesterday's rockslide warning, and who has been out in dropping temperatures for going on two days now.

Mara built this drone's flight code herself, on a folding table at the trailhead, because the stock firmware couldn't hold a tight enough line between these walls. Her laptop still has both candidate builds open in side-by-side terminal windows, each one already compiled, already flashed to a spare flight controller, both tested on the bench that morning. They fly almost identically in calm air. It's the gusts coming off these specific walls — the ones the canyon is actually known for — that make the two builds behave differently, and Mara has maybe ninety seconds of usable light left to pick one and launch.

A gust rattles the drone on the monitor. Her thumb hovers between two identical-looking USB drives, each labeled only with a build number in her own handwriting.

## Background

Mara Yun is a volunteer search-and-rescue drone operator and the team's only member who also writes flight-control firmware. She is accountable for two things at once on this mission: keeping the drone flying a safe, steady line down the canyon, and keeping its thermal camera pointed usefully at the walls and floor long enough to find Dana. Both jobs depend on the same flight-control loop, running on the drone's onboard flight computer (SEE APPENDIX A), correcting the drone's tilt dozens of times a second so it holds a fixed sideways offset from the canyon's rock wall (SEE APPENDIX B) without drifting into it or wandering out into open air where the camera's angle stops covering useful ground.

That correction loop needs to know, every single cycle, how much sideways thrust to command for the drone's current tilt angle — a calculation that depends on the sine of that angle. A full, textbook-accurate sine function call is too slow to fit inside the loop's strict per-cycle time budget on this flight computer (SEE APPENDIX A) — profiling on the bench showed it alone eating a share of the budget that left too little margin for the thermal camera's own processing, which runs on the same chip. Mara's fix, in both builds, is to replace the full sine calculation with a Taylor polynomial approximation of sin(θ) — a short, fixed sequence of multiplications and additions that a flight computer can finish fast enough, at the cost of not being perfectly accurate at every possible tilt angle.

The two builds differ only in how many terms of that polynomial they keep (SEE APPENDIX C). Build 3 truncates after the cubic term. Build 5 keeps one more term. Every extra term buys more accuracy across a wider range of tilt angles — polynomials of this general algebraic form, and how many terms it actually takes to get there, is exactly what Challenge 1's "how to…" research (SEE APPENDIX F) and Appendix D task Mara's pitch with deriving (SEE APPENDIX D) — but every extra term also costs more of the flight computer's strictly limited per-cycle time (SEE APPENDIX A), time that competes directly with the thermal camera sweep that is the entire reason this flight exists. The canyon's own gusts, and how often they push the drone to a large tilt angle versus a small one, are laid out in (SEE APPENDIX E), along with the correction-error tolerance the team is willing to accept given how close the offset in (SEE APPENDIX B) already is. All figures needing a citation or a stated assumption are marked and resolved in (SEE APPENDIX G). Mara has to pick the one build that gets the drone through this canyon and gives the camera its best real chance at finding Dana before dark — not the one that merely looks more mathematically precise on paper.

## Dilemma

You are Mara Yun.
Do you:
A.) Fly Build 3 — the flight code approximating sin(θ) with the 3rd-order Taylor polynomial, θ − θ³/6 OR
B.) Fly Build 5 — the flight code approximating sin(θ) with the 5th-order Taylor polynomial, θ − θ³/6 + θ⁵/120

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the
case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you
would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Your pitch must include:
    D1. A term-by-term derivation of the Taylor (Maclaurin) series for sin(θ) about θ = 0,
    starting from the general Taylor series formula (SEE APPENDIX D) and computing enough
    derivatives of sin(θ) at 0 to justify BOTH Build 3's polynomial (θ − θ³/6) and Build 5's
    polynomial (θ − θ³/6 + θ⁵/120) from scratch — not quoted from a table.
    D2. An exact-error table: for each of the five gust-tilt angles in Appendix E, compute
    sin(θ), each build's polynomial approximation, and the resulting absolute error, with the
    subtraction shown for every cell — and for the two largest angles, check your subtracted
    error against the size of the next un-kept term of the series, stating in words whether
    adding still more terms would keep shrinking the error indefinitely or not.
    D3. A per-correction compute-cost derivation: for each build, count every individual
    single-cycle arithmetic operation (SEE APPENDIX A) its polynomial needs to evaluate one
    correction — showing which intermediate values (like θ²) you reused between terms — then
    convert that operation count into nanoseconds using Appendix A's flight-computer clock
    speed, with every conversion step shown.
    D4. A whole-mission compute-budget and error-rate table: using Appendix E's gust-frequency
    distribution and Appendix A's correction-loop rate, find the total number of correction
    cycles over the stated canyon-transit time, then compute, for each build, (i) the fraction
    of those cycles whose gust-tilt band exceeds Appendix E's correction-error tolerance, and
    (ii) the total milliseconds of flight-computer time the build spends on its sin(θ)
    approximation across the whole transit, using your D3 per-correction cost.
    D5. A primary-metric comparison and an original visual display: using D4's figures, compute
    (1 − error rate) ÷ (total compute-budget spent, in milliseconds) for each build, and build one
    original visual (a bar chart, a scatter plot of error rate against compute cost, or
    equivalent) comparing Build 3 and Build 5 on this metric.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

## Appendix A — The Flight Computer and the Correction Loop

Referenced in Background and Challenge 3 (D3, D4).

| Spec | Value |
|---|---|
| Flight computer | STM32F405, Arm Cortex-M4 core [S1] |
| CPU clock speed | 168 MHz [S1] |
| Cycle time per clock tick | 5.952 ns (= 1 ÷ 168,000,000 Hz) |
| Time for one single-cycle arithmetic operation (multiply, add, or fused multiply-add) | 1 clock cycle = 5.952 ns [S2] |
| Correction-loop rate | 8,000 Hz (8 kHz) [S3] |
| Correction-loop period | 125 µs (= 1 ÷ 8,000 Hz) |
| Canyon transit time (this mission) | 90 seconds (stated scenario duration) |
| Total correction cycles across the transit | 720,000 cycles (= 90,000 ms ÷ 0.125 ms) |

## Appendix B — The Canyon Corridor

Referenced in Background.

| Spec | Value |
|---|---|
| Required offset from canyon wall | 15 feet (stated scenario constraint) |

## Appendix C — Build 3 and Build 5: The Two Polynomials

Referenced in Background and Dilemma.

| Build | Polynomial approximating sin(θ) (θ in radians) |
|---|---|
| Build 3 | θ − θ³ ⁄ 6 |
| Build 5 | θ − θ³ ⁄ 6 + θ⁵ ⁄ 120 |

## Appendix D — Taylor Series Reference

Referenced in Background and Challenge 3 (D1).

The general Taylor series of a function f(θ) about θ = a is:

f(θ) = f(a) + f′(a)(θ − a) + f″(a)(θ − a)² ⁄ 2! + f‴(a)(θ − a)³ ⁄ 3! + f⁽⁴⁾(a)(θ − a)⁴ ⁄ 4! + f⁽⁵⁾(a)(θ − a)⁵ ⁄ 5! + …

For this case, a = 0 (a Maclaurin series), and f(θ) = sin(θ). Challenge 3 (D1) asks you to compute
f(0), f′(0), f″(0), f‴(0), f⁽⁴⁾(0), and f⁽⁵⁾(0) yourself, using the fact that each derivative of
sin(θ) cycles through sin(θ), cos(θ), −sin(θ), −cos(θ) and back — and to use those values in the
general formula above to build both Appendix C polynomials from scratch.

## Appendix E — Canyon Gusts, Correction Tolerance, and the Error-vs-Cost Trade-off

Referenced in Background and Challenge 3 (D2, D4). The probability figures and the tolerance
value in this appendix are stated Modeling Assumptions, not sourced figures — see the Modeling
Assumptions section for why, and for the basis behind each value.

| Gust-tilt band (representative angle) | Share of correction cycles at this tilt (MA1) |
|---|---|
| 10° | 40% |
| 20° | 27% |
| 30° | 20% |
| 40° | 10% |
| 50° | 3% |

| Quantity | Value |
|---|---|
| Correction-error tolerance (maximum acceptable \|sin(θ) − polynomial(θ)\|) | 0.0003 (MA2) |

## Modeling Assumptions

> These figures are **not sourced**. They are stated scenario assumptions chosen by the case
> author because no publishable dataset exists for a specific fictional canyon's gust profile or
> for this specific mission's acceptable correction-error tolerance. A Hero may challenge these
> numbers in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Distribution of correction cycles across the five gust-tilt bands | 40% / 27% / 20% / 10% / 3% (10°/20°/30°/40°/50°) | No public dataset gives a per-canyon gust-tilt-angle frequency distribution for a specific slot canyon — this is inherently a scenario-specific quantity nobody has measured for this location. The shape (most correction cycles at small tilt, progressively fewer at larger tilt) follows the general, well-documented atmospheric-turbulence pattern that small perturbations occur far more often than large ones. | This is the load-bearing assumption in this case — moving weight between the smaller and larger tilt bands changes each build's effective error rate over the mission, which changes the primary metric in Challenge 3 (D4, D5). A Hero who argues the gusts should be weighted differently should redo D4 and D5 with their own weights rather than treating 40/27/20/10/3 as fact. |
| MA2 | Correction-error tolerance (maximum acceptable \|sin(θ) − polynomial(θ)\|) | 0.0003 | No published tolerance standard exists for an acceptable sin(θ) approximation error in a station-keeping drone correction loop. The value is derived directly from Appendix B's 15-foot wall offset: an error of 0.0003 in sin(θ) corresponds to roughly a 0.05-inch lateral positioning miscalculation at that range (180 in × 0.0003 ≈ 0.054 in) — tight enough to matter this close to the rock wall, chosen as a defensible design tolerance rather than measured from a real flight log. | This value sits close to Build 3's actual error at the 30° gust band — a modest change to the tolerance either way can move whether that band counts as in-tolerance for Build 3, which changes Build 3's computed error rate in D4. Work Challenge 3 (D2) and (D4) again under a different tolerance before treating 0.0003 as untouchable. |

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Sequence
- Series
- Taylor Series

**"How to…" questions**

- How to find the Taylor series of a function at a point
- How to determine whether a series converges or diverges
- How to find the percent of a number
- How to convert an amount with compound units

## Appendix G — Sources

All sourced (non-assumption) figures in this case are cited here.

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Maximum CPU clock speed of the STM32F405/407, an Arm Cortex-M4-based MCU used in real flight-controller boards | 168 MHz | STMicroelectronics — [STM32F405xx/407xx Datasheet](https://www.st.com/resource/en/datasheet/dm00037051.pdf) | 2026 (current revision) | HIGH |
| S2 | Arithmetic instructions (multiply, add, and fused multiply-accumulate) on the Cortex-M4 execute in a single clock cycle | "All of the instructions are single-cycle on Cortex-M4 (except hardware divide)." | Arm — [The DSP capabilities of Arm Cortex-M4 and Cortex-M7 Processors (White Paper), T. Lorenser](https://community.arm.com/cfs-file/__key/communityserver-blogs-components-weblogfiles/00-00-00-21-42/7563.ARM-white-paper-_2D00_-DSP-capabilities-of-Cortex_2D00_M4-and-Cortex_2D00_M7.pdf) | Nov 2016 | HIGH |
| S3 | A real, documented flight-control loop rate practice: gyro/PID loops running at 8 kHz on Cortex-M4 flight controllers fast enough to keep up (the STM32F405 is; the guidance explicitly names the slower F411 as needing to drop to 4 kHz instead) | 8 kHz (125 µs loop period) | Betaflight — [Configuration Tab documentation](https://betaflight.com/docs/wiki/app/configuration-tab) | accessed 2026-09-05 | MEDIUM |

S3 is used as a real-world proxy for "flight-control loops of this kind genuinely run this fast on
this class of hardware," not a claim that Mara's own fictional rescue drone runs Betaflight —
graded MEDIUM because it documents racing-drone practice being applied here to a different
(rescue) mission profile, not because the underlying loop-rate figures themselves are in doubt.
See `RESEARCH_LOG.md` for the full search trail, including why the gust-distribution (MA1) and
correction-error tolerance (MA2) figures in Appendix E could not be sourced and were resolved as
stated Modeling Assumptions instead.

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
