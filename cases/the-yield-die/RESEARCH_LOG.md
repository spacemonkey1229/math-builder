# RESEARCH_LOG.md — The Yield Die

One row per `{{NEEDS_SOURCE}}` placeholder from `case-write`. Confirmed via live WebSearch/WebFetch
on 2026-09-09.

## P01 — Wafer lots committed to TSMC this quarter (Appendix A)

**Searched:** n/a — this is a scenario fact about Priya's fictional company's budget, not an
independently verifiable real-world figure. **Disposition:** ASSUMPTION (narrative). Recorded as
"1 lot (fixed)" directly in Appendix A with no further sourcing needed, same treatment as
`the-bracket-bet`'s narrative-only deadline figures.

## P02 — TSMC standard wafer diameter (Appendix B)

**Searched:** "300mm wafer diameter area cm2 usable die area edge exclusion standard." **Found:**
300mm (12-inch) is the current industry-standard leading-edge wafer diameter; multiple corroborating
sources (Wevolver's 200mm-vs-300mm technical comparison, WaferWorld). **Disposition:** SOURCED,
HIGH confidence — S1.

## P03 — Wafer usable area, computed (Appendix B)

**Computed:** `Aw = pi * (300mm/2/10)^2 cm^2 = pi * 15^2 = 706.858 cm^2`, expressed in scientific
notation as `7.07 x 10^2 cm^2`. **Disposition:** SOURCED (derived from P02/S1), `derived: true`.

## P04 — Gross-die-per-wafer geometry formula (Appendix B)

**Searched:** "gross die per wafer formula AnySilicon wafer diameter die area square root 2" and
independently verified against "GDPW Calculator" at siliconanalysts.com. **Found:** Two independent
industry-technical sources state the same edge-loss-corrected formula:
`Gross Dies = (Wafer Area / Die Area) - (pi x Wafer Diameter) / sqrt(2 x Die Area)`. AnySilicon's
own prose worked example uses a cruder flat 5-10% edge-loss haircut in one place, which is a
separate, less precise shortcut on the same page — the formula actually used here is the more
precise edge-loss-corrected version corroborated independently by siliconanalysts.com's GDPW
formula (which additionally subtracts a 2-3mm edge-exclusion margin `E` from the diameter before
squaring; this case omits `E` for simplicity, a disclosed simplification — see Modeling
Assumptions-adjacent note in Appendix B). Cross-checked against siliconanalysts.com's own published
reference table (Smartphone SoC ~120 mm^2 -> ~580 GDPW; Laptop CPU ~200 mm^2 -> ~340 GDPW; Nvidia
H100 ~814 mm^2 -> ~80 GDPW) — this case's no-edge-exclusion numbers (306 for a 200 mm^2 die) land
in the same order of magnitude as their edge-exclusion-adjusted 340, the difference fully explained
by the omitted `E` term. **Disposition:** SOURCED, MEDIUM-HIGH confidence (two independent
industry-technical sources, formula corroborated, but not a standards-body primary source) — S2.

## P05/P06 — Option A/B die areas (Appendix B)

**Searched:** the same siliconanalysts.com GDPW reference table used for P04 also doubles as
real-world grounding for realistic die sizes: Small IoT MCU 25 mm^2, Smartphone SoC ~120 mm^2,
Laptop CPU ~200 mm^2, Nvidia H100 ~814 mm^2. **Disposition:** ASSUMPTION — these are case-author
scenario design choices (Priya's own two floorplans), not independently researched facts about a
real chip. Chosen as clean, round figures sitting inside the real, cited range of actual product
die sizes: Option A ("The Compact Die") = 100 mm^2 (between the IoT/smartphone-SoC range), Option B
("The Full Die") = 200 mm^2 (matching the cited Laptop CPU reference point almost exactly) — a 2x
area ratio. Recorded as MA-adjacent design choices, grounded via S3 (the same siliconanalysts.com
table as P04).

## P07/P08 — Gross dies per wafer, Option A/B (Appendix B)

**Computed** from P04's formula with P02/P03's wafer geometry and P05/P06's die areas:
`Gross_A = 706.858/1.00 - (pi*30)/sqrt(2.00) = 640.215 -> 640`
`Gross_B = 706.858/2.00 - (pi*30)/sqrt(4.00) = 306.305 -> 306`
**Disposition:** SOURCED (derived), `derived: true`.

## P09 — Transistor density at the assumed leading-edge logic node (Appendix C)

**Searched:** "TSMC N3 transistor density million transistors per mm2 published." **Found:** a
range of publicly reported figures for TSMC's N3-generation logic process: TSMC's own
technology-symposium target of 250 MTr/mm^2 (WikiChip Fuse), an independently reported ~290-300
MTr/mm^2 estimate (TechPowerUp, PhoneArena), and lower actual-implementation figures around 167-216
MTr/mm^2 depending on standard-cell library (high-density vs. high-performance). **TSMC does not
publicly confirm one single exact density for any specific customer's tape-out** — these are
target/estimated figures, not this case's chip's own confirmed specification. **Disposition:**
ASSUMPTION (MA1) — a round, representative figure of 2.00 x 10^8 transistors/mm^2 (200
million/mm^2) was chosen, sitting within the cited 167-300 MTr/mm^2 range, disclosed explicitly as
representative rather than exact. Grounded via S4.

## P10/P11 — Transistor count, Option A/B (Appendix C)

**Computed:** `TC_A = 2.00x10^8 transistors/mm^2 * 1.00x10^2 mm^2 = 2.00x10^10` (20 billion);
`TC_B = 2.00x10^8 * 2.00x10^2 mm^2 = 4.00x10^10` (40 billion). **Disposition:** SOURCED (derived),
`derived: true`.

## P12 — Defect-density yield model (Appendix D)

**Searched:** "die yield model wafer defect density formula Murphy Seeds negative binomial
semiconductor." **Found and directly verified by fetching the PDF:** Prof. Robert C. Leachman
(UC Berkeley, IEOR 130, "Yield Modeling and Analysis," Spring 2014) derives the Poisson model
(`DY = e^(-D0*A)`), the Murphy model (`DY = [(1-e^(-A*D0))/(A*D0)]^2`), and, as the alpha=1 special
case of the negative binomial model, the **Seeds model**: `DY = 1/(1+A*D0)`. This case uses the
Seeds model specifically because it requires no exponential evaluation — pure arithmetic on a
scientific-notation defect-density figure, matching this case's target skills — and is a real,
named, citable model (not invented for this case). **Disposition:** SOURCED, HIGH confidence
(primary academic course-notes source, formula independently corroborated by the general
description of the Seeds/negative-binomial model family found via the initial search) — S5.

## P13 — Defect density assumed for this tape-out's process node (Appendix D)

**Searched:** "'defect density' 'defects per cm2' advanced node leading edge typical range 0.1 0.5
semiconductor yield" and Vik's Newsletter ("How Foundries Calculate Die Yield," Vikram Sekar,
2024-09-15, directly fetched and confirmed). **Found:** a widely repeated industry benchmark that
`D0 < 0.1 defects/cm^2` corresponds to roughly 90% yield for a 1 cm^2 die and is treated as the mark
of a "mature, manufacturable" process; a general "good manufacturing process" benchmark of
`D0 < 0.5 defects/cm^2`; and a real, disclosed figure for Intel's 18A node of `D0 < 0.40
defects/cm^2` (cited by Intel itself per Vik's Newsletter, in the context of Intel abandoning its
20A node) as real corroborating order-of-magnitude context. **No foundry publicly discloses its
live, current defect density for a specific customer's tape-out** — this is commercially sensitive
and changes continuously as a process line matures. **Disposition:** ASSUMPTION (MA2) — the
round, representative benchmark figure `D0 = 1.0 x 10^-1 defects/cm^2` (0.10) was chosen directly
from the widely-cited "mature, manufacturable" reference point, comfortably below Intel's real
disclosed 18A ceiling of 0.40 (i.e., representing a *more* mature, better-yielding line than
Intel's own newest node, a defensible modeling choice for "a leading-edge but not bleeding-edge"
tape-out). This is the one figure in the case that is not knowable in advance for any specific,
not-yet-running process line, and is the case's sole `FLEX[]` sensitivity parameter (see
`sensitivity_model.py`). Grounded via S6.

## P14/P15 — Yield, Option A/B (Appendix D)

**Computed:** `Y_A = 1/(1 + 0.10*1.00) = 1/1.10 = 0.9091` (90.91%);
`Y_B = 1/(1 + 0.10*2.00) = 1/1.20 = 0.8333` (83.33%). **Disposition:** SOURCED (derived).

## P16/P17 — Net good dies per wafer, Option A/B (Appendix D)

**Computed:** `Good_A = floor(640 * 0.9091) = floor(581.82) = 581`;
`Good_B = floor(306 * 0.8333) = floor(255.00) = 255`. **Disposition:** SOURCED (derived).

## P18 — Real-world reference for the dollars-per-transistor benchmark (Appendix E)

**Searched:** "Nvidia H100 transistor count 80 billion price per unit street price analyst
estimate" and confirmed against Nvidia's own official Hopper Architecture whitepaper (via a
search directly quoting the whitepaper: "80 billion transistors," TSMC 4N process). **Found:**
Nvidia's H100 GPU compute die (GH100) carries 80 billion transistors (8.0 x 10^10) — Nvidia's own
official, disclosed figure, HIGH confidence. Real-world street/OEM pricing for the packaged H100
GPU module is reported in the $25,000-$40,000 range as of early 2026 (IntuitionLabs' 2026 Nvidia AI
GPU pricing guide), an analyst/market estimate, not an official Nvidia list price.
**Important caveat, disclosed in Appendix E and the Modeling Assumptions block:** this is the price
of the fully packaged, sold GPU product (die + HBM memory + board + cooling + Nvidia's own margin),
**not** a bare die's price — it is used here only as an illustrative real-world anchor to derive a
representative dollars-per-transistor rate, not as this fictional case's own chip's actual market
price. **Disposition:** ASSUMPTION (MA3) — S7 (transistor count, HIGH) + S8 (price range, MEDIUM);
midpoint of the disclosed range, $30,000, used for the derivation.

## P19 — Derived dollars-per-transistor figure (Appendix E)

**Computed:** `rate = $30,000 / 8.0x10^10 transistors = 3.75 x 10^-7 $/transistor`. **Disposition:**
SOURCED (derived from P18/S7/S8), `derived: true`.

## P20/P21 — Price per good die, Option A/B (Appendix E)

**Computed:** `Price_A = 3.75x10^-7 * 2.00x10^10 = $7,500`; `Price_B = 3.75x10^-7 * 4.00x10^10 =
$15,000`. **Disposition:** SOURCED (derived).

## P22/P23 — Revenue per wafer, Option A/B (Appendix E)

**Computed:** `Revenue_A = 581 * $7,500 = $4,357,500`; `Revenue_B = 255 * $15,000 = $3,825,000`.
**Disposition:** SOURCED (derived).

## P24/P25/P26 — Modeling Assumptions block values (MA1/MA2/MA3)

Cross-references to P09/P13/P18 above — same figures, same dispositions, restated in the visible
Modeling Assumptions block per `case-write`'s placement rule.

## MA4 — Flagship pricing premium (added during case-readiness remediation, 2026-09-09)

**Searched:** "Nvidia L4 GPU transistor count billion price official specs Ada Lovelace," to find a
real, smaller/cheaper real AI-chip product to compare against the H100 anchor already used for
MA3. **Found:** Nvidia L4 (Ada Lovelace, TSMC 4nm-class): 35.8 billion transistors, ~$2,000-$3,000
street price. Implied dollars-per-transistor: ~7e-8, versus the H100's 3.75e-7 -- the larger,
more-capable chip's real per-transistor rate runs roughly 5x higher than the smaller chip's, not
merely proportionally higher (both are Nvidia GPUs, so this isolates a real "larger/flagship chips
carry disproportionate pricing power" effect from a same-vendor comparison). **Disposition:**
ASSUMPTION (MA4) -- this case applies a deliberately conservative 19% premium (a small fraction of
the real ~5x gap) to Option B's price only, disclosed in Appendix E and the Modeling Assumptions
block, grounded via new source S9. This addition was made specifically because two independent
Tier 2 probes (P2 both-sides-solve, P4 twist-integrity) found that without it, Option A won on
revenue per wafer at every possible defect density -- a real authoring defect, not a false alarm --
which made the case's disclosed defect-density assumption (MA2) unable to ever genuinely flip the
verdict. See QA_REPORT.md for the full probe record.

---

## Balance-test verification arithmetic (revised after Tier 2 P2/P4 remediation)

The case's first-draft calibration (D0=0.10, pure linear pricing with no premium) was replaced
after two independent fresh-subagent Tier 2 probes (P2 both-sides-solve, P4 twist-integrity) both
found, by independent derivation, that Option A won on revenue per wafer at *every* non-negative
defect density under that calibration — meaning the case's disclosed "assumption" (MA2) could never
actually flip the verdict, and D5's own prompt ("what value would have to take for your
recommendation to flip") had no valid answer. See `QA_REPORT.md` for the full probe transcripts and
remediation record. The fix, applied 2026-09-09:

1. MA2 (assumed defect density) moved from 0.10 to **0.30 defects/cm^2** — still real and
   defensible (below Intel's own disclosed 18A ceiling of D0<0.40, S6), and arguably more
   defensible than 0.10 given this is the company's *first* tape-out on a not-yet-mature line.
2. A new disclosed Modeling Assumption, **MA4**, adds a flagship pricing premium (x1.19) to Option B
   only, grounded in the real Nvidia L4-vs-H100 dollars-per-transistor gap (S9, roughly a 5x real
   gap, of which this case uses a conservative 19% fraction).

```
Wafer area           = pi * 15.0^2                    = 706.858 cm^2   (7.07e2 cm^2)
Gross dies A          = 706.858/1.00 - pi*30/sqrt(2.00)  = 640.215 -> 640
Gross dies B          = 706.858/2.00 - pi*30/sqrt(4.00)  = 306.305 -> 306
Transistor count A    = 2.00e8 * 1.00e2                = 2.00e10  (20 billion)
Transistor count B    = 2.00e8 * 2.00e2                = 4.00e10  (40 billion)
$/transistor          = 30,000 / 8.0e10                = 3.75e-7
Price/die A           = 3.75e-7 * 2.00e10              = $7,500
Price/die B (naive)   = 3.75e-7 * 4.00e10              = $15,000
Price/die B (w/ MA4)  = 15,000 * 1.19                  = $17,850

-- BASE CASE (D0 = 0.30, MA2) --
Yield A (Seeds)       = 1/(1+0.30*1.00)                = 0.7692   (76.92%)
Yield B (Seeds)       = 1/(1+0.30*2.00)                = 0.6250   (62.50%)
Good dies A           = floor(640*0.7692)              = 492
Good dies B           = floor(306*0.6250)              = 191
Revenue/wafer A       = 492 * 7,500                    = $3,690,000
Revenue/wafer B       = 191 * 17,850                   = $3,409,350
Margin                = (3,690,000 - 3,409,350)/3,409,350 = 8.23%   -- Option A (Compact Die) wins

-- SENSITIVITY: D0 = 0.15 (-50% flex) --
Yield A = 0.8696  Yield B = 0.7692  Good A = 556  Good B = 235
Revenue A = $4,170,000   Revenue B = $4,194,750
Margin = 0.59% -- Option B (Full Die) wins  *** VERDICT FLIPS ***

-- SENSITIVITY: D0 = 0.45 (+50% flex) --
Yield A = 0.6897  Yield B = 0.5263  Good A = 441  Good B = 161
Revenue A = $3,307,500   Revenue B = $2,873,850
Margin = 15.09% -- Option A (Compact Die) wins

-- CROSSOVER (scanned numerically against the case's own floor-function arithmetic) --
D0 ~= 0.157-0.16 defects/cm^2 is the approximate point where Revenue A = Revenue B.
```

Margin at the base case (8.23%) sits inside the approved concept sheet's 8-14% target band and
comfortably inside SPEC §2's 20% cap. The disclosed assumption (MA2) now genuinely flips the
verdict within the standard ±50% sensitivity range, giving D5's "what value would flip it" question
a real, findable answer (~D0=0.157-0.16) for the first time.

**Naive-trap check (not shown to students, facilitator-only):** comparing gross die count alone
(640 vs. 306, a 109% "advantage") still vastly overstates Option A's true edge once yield and price
are correctly applied (8.23% at the base case, and Option A doesn't even win at every defect
density) — this is the concept sheet's stated trap, reproduced exactly by this case's own numbers,
now with the added nuance that the naive comparison also hides that the "right" answer is itself
contingent on an unknowable input.

**Sensitivity check (±50% flex of the one free assumption, D0) — GENUINELY FLIPS:** at D0=0.15
(-50%), Option B wins by 0.59%. At D0=0.45 (+50%), Option A wins by 15.09%. See
`sensitivity_model.py` for the runnable check.

## Sources fetched and verified

All 8 sources below were fetched directly (WebFetch) or confirmed via multiple independent
WebSearch results on 2026-09-09; no citation below is a search-summary paraphrase taken at face
value without at least one direct-fetch or multi-source cross-check. One caution logged for the
record: an initial WebSearch summary claimed a specific "Cerebras WSE-2, 0.09 defects/cm^2, 510
mm^2, ~60% yield" example attributed to Vik's Newsletter; direct WebFetch of both of that
newsletter's candidate articles found **no such figures anywhere in the actual page text** — this
was a search-tool synthesis artifact, not a real citation, and was discarded rather than used. This
is exactly the kind of failure this skill exists to catch — see `case-research` SKILL.md's "never
cite a URL you did not fetch" rule.
