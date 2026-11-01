# Case Study: Turbine Channel

MS | Math | Case Study | 2026-27 | Launchpad

---

## Overview

Dana Okafor braces against the gunwale as the survey boat swings hard on its mooring line, the current shoving broadside even though the engine has been dead in the water for ten minutes. Out past the bow, a lobster buoy dips completely under, drags a beat, and pops back up somewhere else entirely — that's the Narrows doing what the Narrows does. Dana has been out here at slack water and at full flood, in both channels, for three weeks straight, and her boots have not been properly dry since the second day.

She is the siting engineer for the utility's first tidal-power pilot, and the board wants a recommendation by Friday. Not a study. A channel. The lease options on both sites expire the same week, and the pilot program can only afford to exercise one.

Her laptop is open on the chart table below, current-speed readings scrolling past from two NOAA stations she has stared at for so long she can trace the shape of each curve with her eyes closed — one tall and narrow, one low and wide. She still cannot say, with the kind of certainty she'd want to put her name on, which one actually moves more water through a turbine's face per cycle, rather than just past it.

Her phone buzzes against the laptop, screen-down, rattling on the chart table. It's the program director. Dana looks at the two folders on the seat beside her — one labeled NARROWS, one labeled REACH — and picks up the phone.

---

## Background

Dana Okafor is the marine energy siting engineer for the utility's tidal-power pilot program. She is responsible for recommending, to the utility's board, exactly one channel where the program's first turbine array will be installed — and for defending that recommendation with real current data, not a general sense of which site "feels" faster.

Two sites are under lease option: **the Narrows**, a narrow, fast tidal channel with a short, sharply-peaked flow window each cycle, and **the Reach**, a wider, slower channel with a longer, flatter flow window. Both leases were secured on identical terms and cost the pilot program the same amount, and the turbine array itself — its rated capacity, its physical footprint (SEE APPENDIX C) — does not change depending on which site it goes into. The decision therefore turns entirely on which channel moves more water, efficiently, through the array's swept face — not on which channel is cheaper or which array is bigger.

NOAA operates a current-meter station at each site (SEE APPENDIX A, APPENDIX B) that has recorded current speed at six-minute intervals across at least one full tidal cycle. Neither station publishes a formula for current speed over time — only discrete readings, which is exactly why a curve has to be fit to each channel's data before anything can be integrated.

The lease-option window closes in 12 days. After that, the utility must begin permitting on whichever channel Dana has recommended, or lose both options and restart the site search from scratch next season.

Converting a channel's current-speed curve into a usable comparison takes two more pieces of information beyond the NOAA readings themselves: the channel's cross-sectional area, which turns an integrated speed into an actual volume of water (SEE APPENDIX C), and a generation-potential conversion factor, which turns that volume into kilowatt-hours (SEE APPENDIX D). Appendix E notes where that second figure is not yet resolved.

The vocabulary and the "how to…" skills this case will ask you to research are listed in **APPENDIX F** — that is where Challenge 1 sends you. Every sourced figure and stated assumption in this case is documented in **APPENDIX G**.

She answers the phone.

---

## Dilemma

You are Dana Okafor.

Do you:

**A.)** Recommend the Narrows — the narrow, fast channel with a short, sharply-peaked flow window **OR**

**B.)** Recommend the Reach — the wider, slower channel with a longer, flatter flow window

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A scatter plot** of the raw current-speed readings for each channel across one full tidal cycle, time since slack water on the horizontal axis and current speed on the vertical axis, one plot per channel.
- **D2 — A fitted-curve worksheet** for each channel: the polynomial function you fit to that channel's scatter plot, and its indefinite integral (antiderivative), found term-by-term using the power rule, shown as work.
- **D3 — A definite-integral volume table**: for each channel, the definite integral of your fitted curve over its flow window (evaluated using the Fundamental Theorem of Calculus), converted using the channel's cross-sectional area into a total volume of water moved, in cubic meters, per tidal cycle.
- **D4 — A Riemann-sum cross-check**: for each channel, a Riemann sum built directly from the raw six-minute-interval readings (not your fitted curve) approximating that same per-cycle volume, stated side-by-side with your Challenge D3 result, with a note on how closely the two methods agree.
- **D5 — A generation-potential ratio table**: for each channel, your total per-cycle volume from D3, the channel's generation-potential ratio (kilowatt-hours per cubic meter of water moved), and every unit conversion you used to get there, shown step by step.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A — The Narrows: Current-Speed Record

**Modeled on NOAA station ca0101 — Cape Cod Canal, West End, Massachusetts** (Cape Cod/Buzzards Bay PORTS®, a registered NOAA real-time data network; bin depth 13 ft — the specific depth below the surface this instrument's reading applies to, not the channel's total depth), a real, narrow (480 ft / 146.3 m wide), fast, engineered tidal strait. The Narrows' current-speed record below is the real published NOAA current-prediction time series (a computed forecast built from this station's historical current-meter data, not a live-instant reading) for this station's ebb pulse — the outgoing-tide half of the cycle — on 2026-09-01. Dana's fictional "Narrows" channel is explicitly modeled on this real station's real published flow pattern [S1].

| Time since slack water (min) | Current speed (knots) |
|---|---|
| 0 | 0.11 |
| 60 | 2.50 |
| 120 | 4.82 |
| 156 (near peak) | 5.28 |
| 216 | 4.40 |
| 288 | 2.43 |
| 366 (next slack) | 0.01 |

*Note: NOAA's published record for this station reports a reading every six minutes for the full duration of the cycle (61 readings across this 366-minute ebb pulse). The seven rows above are a representative subset for readability. The complete six-minute-interval series is a dated, reproducible export of the same NOAA product: `https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=currents_predictions&station=ca0101&begin_date=20260901&end_date=20260901&interval=6&units=english&time_zone=lst_ldt&format=json` (fetched and confirmed live 2026-09-11) — pull this URL for the full 61-point record Challenge D1's scatter plot and Challenge D2's curve fit are built from. Current speed here is reported as an unsigned magnitude (NOAA's own published series is signed, negative on the ebb and positive on the flood, flood direction 040°/ebb direction 230° for this station); direction does not affect the volume moved through the channel's cross-section, which is what this case's math needs — volume moved depends on how fast the water is crossing that cross-section and for how long, not which of the two directions it happens to be pointed.*

> *Source: [S1] NOAA Tides & Currents (tidesandcurrents.noaa.gov / api.tidesandcurrents.noaa.gov), CO-OPS current predictions product, station ca0101 "Cape Cod Canal, West End, MA," 2026-09-01 tidal cycle. Confirmed live 2026-09-11 by direct API fetch.*

---

## Appendix B — The Reach: Current-Speed Record

**Modeled on NOAA station cb0102 — "Cape Henry LB 2CH," Chesapeake Bay South PORTS®** (bin depth 55 ft), a real current station near the wide (roughly 12-mile-wide, Cape Henry to Cape Charles) entrance to Chesapeake Bay, Virginia. The Reach's current-speed record below is the real published NOAA current-prediction time series for this station's flood pulse — the incoming-tide half of the cycle — on 2026-09-01. Dana's fictional "Reach" channel is explicitly modeled on this real station's real published flow pattern [S2], which is both lower-peaked (1.53 kn vs. the Narrows' 5.28 kn) and longer in duration (456 min vs. 366 min) than Appendix A's. *(The Narrows' record happens to be its ebb pulse and the Reach's its flood pulse — each is simply the one complete, cleanly-recorded half-cycle available for that real station; flood vs. ebb is just which direction the tide is running, and direction does not change the volume-moved math below, only speed and duration do.)*

| Time since slack water (min) | Current speed (knots) |
|---|---|
| 0 | 0.01 |
| 72 | 0.64 |
| 144 | 1.27 |
| 210 (near peak) | 1.53 |
| 282 | 1.32 |
| 354 | 0.83 |
| 456 (next slack) | 0.04 |

*Note: same convention as Appendix A — seven representative rows here. The complete six-minute-interval series (77 readings across this 456-minute flood pulse) is a dated, reproducible export of the same NOAA product: `https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=currents_predictions&station=cb0102&begin_date=20260901&end_date=20260901&interval=6&units=english&time_zone=lst_ldt&format=json` (fetched and confirmed live 2026-09-11). Current speed is reported here as an unsigned magnitude, same convention as Appendix A. The Reach's flow window is indeed longer and flatter than the Narrows' — visible directly in the two tables above.*

> *Source: [S2] NOAA Tides & Currents (tidesandcurrents.noaa.gov / api.tidesandcurrents.noaa.gov), CO-OPS current predictions product, station cb0102 "Cape Henry LB 2CH" (Chesapeake Bay South PORTS®), 2026-09-01 tidal cycle. Confirmed live 2026-09-11 by direct API fetch.*

---

## Appendix C — Channel Geometry and Turbine Array

| Quantity | The Narrows | The Reach |
|---|---|---|
| Channel cross-sectional area at the turbine array site (m²) | 1,427.0 [S3, S8, derived] | 4,290.6 [MA1, derived] |
| Charted mean depth at the array site (m) — the federally authorized depth (the depth the U.S. Army Corps of Engineers has approved and commits to maintaining by dredging, not the channel's deepest point), same figure both ways | 9.75 [S8] | 16.76 [S4] |
| Channel width at the array site (m) | 146.3 [S3] | 256 [MA1] |

| Quantity (identical for both sites) | Value |
|---|---|
| Turbine array rated capacity (kW) | 1,050 [S5] |
| Turbine array swept footprint (m²) | 589.0 [S5, derived] |

*This case treats each channel's cross-sectional area as constant across the flow window — a simplification, since real channel depth varies somewhat with tide stage. If that matters to your answer, say so and show what changes.*

*A turbine array's rated (nameplate) capacity above is the power it produces only when water moves through its swept footprint at its design current speed; slower water through that same footprint produces less power, and the footprint's size sets how much moving water the array can act on at all — this is why capacity, design speed, and swept footprint all have to be reported together rather than capacity alone.*

*For scale: the array's swept footprint occupies about 41% of the Narrows' channel cross-section but only about 14% of the Reach's — the Narrows site is far more "crowded" by its own array than the Reach site is (see Background/Argument for A).*

---

## Appendix D — Generation-Potential Conversion Factors

| Quantity | Value |
|---|---|
| Seawater density (kg/m³) | 1,025 [S6] |
| Generation-potential conversion factor (kWh per m³ of water moved through the array's swept face, per cycle) | 0.00022 [MA2] |

*See Appendix E — the conversion factor above is a stated Modeling Assumption, derived from a real turbine's real published rated output and design flow speed rather than a directly-published "kWh per m³" spec (no manufacturer publishes that ratio directly).*

---

## Appendix E — Modeling Assumptions

> These figures are **not sourced** as direct external citations. They are stated scenario assumptions, each grounded in a real basis described below. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The Reach's channel width at the proposed array site | 256 m (cross-section 4,290.6 m², using the real 16.76 m charted depth [S4]) | No single real "array site" width exists for a fictional channel modeled on a real bay entrance that is itself ~12 miles (19 km) wide end to end [S7]. 256 m is a stated scenario slice of that entrance — comparable in scale to real tidal-array project footprints (e.g., MeyGen's Inner Sound development channel is described as multiple kilometers wide, with the actual turbine deployment occupying a much narrower working section) — chosen specifically so the Reach's cross-section is realistic in scale for a single pilot array site, not the full bay mouth. | This is the single most dilemma-relevant assumption in the case. At the real charted depth (16.76 m), a width much above ~310 m would push the Reach's volume advantage past SPEC's ~20% balance cap; a width below ~200 m would flip the recommendation to the Narrows. The margin is directly sensitive to this number, and a Hero who argues for a different realistic width is making exactly the kind of defensible challenge this case is built for. |
| MA2 | Generation-potential conversion factor | 0.00022 kWh per m³ (2.20 × 10⁻⁴ kWh/m³) | Derived, not invented: Verdant Power's real Gen5 KHPS turbine array (as deployed in the Roosevelt Island Tidal Energy project, East River, NYC) is rated at a real, published 1,050 kW combined output (30 × 35 kW turbines) at a real, published 2.25 m/s design current speed, through a real 589.0 m² swept footprint (30 turbines × a real 5 m rotor diameter) [S5]. Dividing real published power by real published flow-through-rotor-face volume rate (1,050 kW ÷ (2.25 m/s × 589.0 m²) = 0.7922 kJ per m³ = 0.00022 kWh per m³) gives a real, physically grounded ratio — not a manufacturer-published "kWh/m³" line item, since no such line item is publicly published for any small tidal-turbine array. This case applies that single ratio identically to both channels' full channel-cross-section volumes (Appendix C, D3), a simplifying scenario choice consistent with this case's primary metric; a real installed array would only capture the fraction of channel flow that actually passes through its own swept footprint (see the Appendix C note above and Argument for A), not the entire channel cross-section. | Because the **same** factor is applied to both channels, it does not change which channel wins Challenge D5's ratio — that comparison is decided entirely by Challenge D3's volume, which is exactly Argument-for-B's point. It does change the **absolute** kWh figures both channels report: if the true real-world capture ratio is smaller (because a real array occupies less of the channel than this simplification implies), both channels' total kWh values shrink proportionally, but the *comparison* between them is unaffected. |

*No other figure in this case required a Modeling Assumption — see `RESEARCH_LOG.md` for the full source-by-source trail, including two figures that were real, cited values used directly with no assumption needed.*

---

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Antiderivative
- Definite Integral
- Indefinite Integral
- Riemann Sum

**"How to…" questions**

- How to find an antiderivative using the power rule
- How to evaluate a definite integral using the Fundamental Theorem of Calculus
- How to approximate area under a curve using a Riemann sum
- How to convert an amount with compound units
- How to create a scatter plot given a set of data

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | The Narrows' current-speed record | Cape Cod Canal, West End (station ca0101), 6-min ebb-pulse readings, 2026-09-01 | NOAA Tides & Currents / CO-OPS current predictions ([data](https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=currents_predictions&station=ca0101&begin_date=20260901&end_date=20260901&interval=6&units=english&time_zone=lst_ldt&format=json)) | accessed 2026-09-11 | HIGH |
| S2 | The Reach's current-speed record | Cape Henry LB 2CH (station cb0102), 6-min flood-pulse readings, 2026-09-01 | NOAA Tides & Currents / CO-OPS current predictions ([data](https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=currents_predictions&station=cb0102&begin_date=20260901&end_date=20260901&interval=6&units=english&time_zone=lst_ldt&format=json)) | accessed 2026-09-11 | HIGH |
| S3 | Cape Cod Canal channel width | 480 ft (146.3 m) wide | ASCE, ["Cape Cod Canal" historic landmark summary](https://www.asce.org/about-civil-engineering/history-and-heritage/historic-landmarks/cape-cod-canal) | accessed 2026-09-12 | HIGH |
| S4 | Chesapeake Bay entrance federal channel depth near Cape Henry | 55 ft (16.76 m) main channel | NOAA Office of Coast Survey, *U.S. Coast Pilot 3*, Chapter 9 ([PDF](https://nauticalcharts.noaa.gov/publications/coast-pilot/files/cp3/CPB3_C09_WEB.pdf)) | accessed 2026-09-11 | HIGH |
| S8 | Cape Cod Canal current federal-project (authorized) channel depth | 32 ft (9.75 m) | NOAA Office of Coast Survey, *U.S. Coast Pilot 2*, Chapter 5 ([PDF](https://nauticalcharts.noaa.gov/publications/coast-pilot/files/cp2/CPB2_C05_WEB.pdf)) | accessed 2026-09-12 | HIGH |
| S5 | Small tidal-turbine array rated capacity, design current speed, and rotor diameter | 1,050 kW combined (30 × 35 kW), 2.25 m/s design current speed, 5 m rotor diameter | Verdant Power Gen5 KHPS turbines, Roosevelt Island Tidal Energy (RITE) project, East River, NYC — [Tethys/PNNL project page](https://tethys.pnnl.gov/project-sites/roosevelt-island-tidal-energy-rite-project-pilot); design speed and diameter confirmed via ["Tides of change in New York," Power Technology / NRi Digital, Jan 2021](https://power.nridigital.com/future_power_technology_jan21/new_york_tidal_energy_verdant) | accessed 2026-09-11 | HIGH |
| S6 | Standard seawater density | 1,025 kg/m³ | Compiled physical-constants reference citing *Encyclopaedia Britannica* and *CRC Handbook of Chemistry and Physics*, 48th ed. ([The Physics Factbook](https://hypertextbook.com/facts/2002/EdwardLaValley.shtml)) | accessed 2026-09-11 | HIGH |
| S7 | Width of the Chesapeake Bay entrance (Cape Henry to Cape Charles) | ~12 miles (~19 km) | [SpinSheet, "Chesapeake Bay Facts and Figures for Sailors"](https://www.spinsheet.com/chesapeake-bay/chesapeake-bay-facts-and-figures) | accessed 2026-09-11 | MEDIUM |

*Modeling Assumptions MA1 and MA2 are documented in Appendix E, not repeated here. Full search trail, rejected sources, and derivation arithmetic: `RESEARCH_LOG.md`.*

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
