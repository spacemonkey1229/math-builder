# Case Study: The Yield Die

MS | Math | Case Study | 2026-27 | Adventure

---

## Overview

Priya Anand has the reticle-order screen open on her laptop, the cursor parked on a field marked
DIE SIZE (MM²) that will not let her submit until it is filled. Behind her, the small conference
room's speakerphone is muted but blinking — the board is already dialed in, waiting on the number
she promised them an hour ago. Someone taped a printout of two chip floorplans to the whiteboard
this morning, side by side, one noticeably smaller than the other, both labeled only "Option A"
and "Option B" in marker.

TSMC's wafer-start slot for their process quarter closes today. Once Priya submits this field and
the mask set is cut, there is no redo — the company's entire first tape-out budget rides on
whichever number goes in that box next. Her phone buzzes face-down on the table: the CEO, again,
asking if she's decided.

She has run each option's numbers twice already and gotten two different confident answers
depending on which sheet she was reading. The engineer at her elbow, headset still around his
neck from the last stand-up, taps the smaller floorplan. "More chips per wafer. It's not close."

Priya doesn't reach for the field yet. More chips is not the same question as more money, and she
has not yet run both all the way through. She opens a blank spreadsheet instead of typing the
number.

---

## Background

Priya Anand is the director of silicon engineering at a fabless AI-chip startup preparing its
first commercial tape-out with **TSMC**, the foundry that manufactures the company's chip design
onto physical silicon wafers. Priya has final sign-off on one irreversible decision before the
mask set (the physical stencil used to pattern every wafer) is cut: how large, in square
millimeters, to make the die — the single rectangle of silicon that becomes one finished chip once
the wafer is cut apart. Two floorplans are ready to go, labeled **The Compact Die** and **The Full
Die** (SEE APPENDIX B).

A wafer is a large, thin, circular disc of silicon; TSMC patterns many identical copies of a die
onto one wafer, then cuts the wafer apart into individual chips (SEE APPENDIX B). A smaller die
means more copies fit on each wafer — but it is not the only thing that changes. Wafers are not
manufactured perfectly: microscopic manufacturing flaws, called defects, land at random across the
wafer's surface, and any die unlucky enough to contain one at all normally fails testing and cannot
be sold. A larger die area is more likely to contain at least one defect than a smaller die area
is, so the two options do not just differ in how many dies fit on a wafer — they differ in what
fraction of those dies actually work (SEE APPENDIX D). The two options also do not carry the same
chip: the Full Die packs proportionally more transistors — and therefore more compute capability —
onto its larger area, which the company can sell for a proportionally higher price per chip (SEE
APPENDIX C, APPENDIX E).

The company has committed to exactly one wafer lot with TSMC this quarter — the budget will not
stretch to run both options — so Priya's decision is final for this product generation, and the
mask order must be placed before today's reticle lock deadline (SEE APPENDIX A). Every
number in this case, from the wafer's own area down to the fraction of a defect per square
centimeter, is large or small enough that it is normally written in scientific notation rather than
standard notation; TSMC's own engineering documentation does the same (SEE APPENDIX F). The
vocabulary and the "how to…" skills this case will ask you to research are listed in the final
appendix — that is where Challenge 1 sends you (SEE APPENDIX F). All figures in this case are
sourced (SEE APPENDIX G). Real-world industry terms used throughout this case are defined in plain
language (SEE APPENDIX H).

---

## Dilemma

You are Priya Anand.

Do you:

**A.)** Order the **Compact Die** — the smaller floorplan, more gross dies per wafer, but a smaller
share of the company's total transistor budget and compute capability per chip **OR**

**B.)** Order the **Full Die** — the larger floorplan, fewer gross dies per wafer, but more
transistors and more compute capability — and a higher price — per chip

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case
study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would
choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A scientific-notation conversion table.** Convert every raw figure in Appendices B–E
  (the wafer's diameter and area, both die-option areas, the transistor density, and the defect
  density) from standard notation into scientific notation, and convert at least one given
  scientific-notation figure back into standard notation — showing the exponent shift for every
  row, not just the final form.
- **D2 — A transistor-count comparison.** Compute the total transistor count for each die option
  (transistor density × die area) entirely in scientific notation, showing the exponent arithmetic
  when the two scientific-notation figures are multiplied together.
- **D3 — A gross-die-per-wafer table.** Apply Appendix B's wafer-geometry formula for both options,
  carrying every intermediate figure in scientific notation, then convert each final gross-die
  count back to standard notation.
- **D4 — A yield-and-net-good-die table.** Apply Appendix D's defect-density yield model for both
  options with the defect density entered in scientific notation, showing the resulting yield
  percentage and the net (good, sellable) die count per wafer for each option.
- **D5 — A revenue-per-wafer recommendation memo.** Compute net good dies × price per die
  (Appendix E) for both options, with every figure shown in scientific notation before it is
  converted to a final dollar total, recommend a die size, and name the one figure in this case
  your recommendation depends on most — and state what value that figure would have to take for
  your recommendation to flip.

4.) An appendix showing evidence of your original thinking, work, calculations and processes you
used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix
does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a
discussion post 500 "excellent" words on the questions above.

---

## Appendix A — Priya's Wafer Commitment and the Reticle Lock Deadline

The concrete constraints Priya is operating under before the mask set is cut.

| Quantity | Value |
|---|---|
| Wafer lots committed to TSMC for this tape-out, this quarter | 1 lot (fixed; the company cannot afford to run both options)* |
| Hours remaining before the reticle (mask) order locks | 3 hours* |

*Narrative detail only — not a researched figure; see RESEARCH_LOG.md.

Referenced from Overview and Background.

---

## Appendix B — Wafer and Die Geometry

The physical geometry behind how many dies of each option fit on one wafer.

| Quantity | Value |
|---|---|
| TSMC standard wafer diameter used for this tape-out | 300 mm (3.00 × 10² mm) = 30.0 cm (3.00 × 10¹ cm) [S1] |
| Wafer usable area (computed from diameter, **converted to cm first** — every other figure in this appendix is in cm²) | 706.86 cm² (7.07 × 10² cm²) — computed as π × (30.0 cm ÷ 2)² = π × (15.0 cm)² |
| Gross-die-per-wafer formula (the second term subtracts the die-shaped positions lost to edge loss, near the wafer's round rim, that a purely square/rectangular grid of dies can't cleanly fill) | Gross Dies = (Wafer Area ÷ Die Area) − (π × Wafer Diameter) ÷ √(2 × Die Area) [S2] |
| Option A — "The Compact Die" — die area | 100 mm² = 1.00 cm² (1.00 × 10⁰ cm²) [S3] |
| Option B — "The Full Die" — die area | 200 mm² = 2.00 cm² (2.00 × 10⁰ cm²) [S3] |
| Option A — gross dies per wafer (computed) | 640 dies (6.40 × 10² dies) |
| Option B — gross dies per wafer (computed) | 306 dies (3.06 × 10² dies) |

Referenced from Background and forces D1's and D3's scientific-notation geometry computations.

---

## Appendix C — Transistor Density and Chip Compute Scale

How many transistors — and therefore how much compute capability — each option actually packs onto
its silicon.

| Quantity | Value |
|---|---|
| Transistor density at the leading-edge logic node used for this tape-out | 2.00 × 10⁸ transistors/mm² (200 million/mm²) — see Modeling Assumptions, MA1 [S4] |
| Option A total transistor count (computed) | 2.00 × 10¹⁰ transistors (20 billion) |
| Option B total transistor count (computed) | 4.00 × 10¹⁰ transistors (40 billion) |

Referenced from Background and forces D2's scientific-notation multiplication.

---

## Appendix D — The Defect-Density Yield Model

The real yield mechanics that make gross die count alone the wrong number to compare.

| Quantity | Value |
|---|---|
| Defect-density yield model used | Seeds model: DY = 1 ÷ (1 + A × D₀), where A is die area (cm²) and D₀ is defect density (defects/cm²) [S5] |
| Defect density assumed for this tape-out's process node | 3.0 × 10⁻¹ defects/cm² (0.30) — see Modeling Assumptions, MA2 [S6] |
| Option A — yield (computed) | 1 ÷ (1 + 0.30 × 1.00) = 0.7692 (76.92%) |
| Option B — yield (computed) | 1 ÷ (1 + 0.30 × 2.00) = 0.6250 (62.50%) |
| Option A — net good dies per wafer (computed) | 492 dies (4.92 × 10² dies) |
| Option B — net good dies per wafer (computed) | 191 dies (1.91 × 10² dies) |

Referenced from Background and forces D4's yield computation. **Both options' yields must be
computed from the same defect density.** A pitch that applies a different defect density to each
option, or skips computing yield for one option, has not completed D4.

---

## Appendix E — Pricing: What Each Die Is Worth

The revenue side of the decision — each option is not just a different die size, it is a
different, differently-priced product.

| Quantity | Value |
|---|---|
| Real-world reference used to anchor a dollars-per-transistor figure | Nvidia H100 GPU compute die: 8.0 × 10¹⁰ transistors (80 billion) [S7], street/OEM price range $25,000–$40,000, midpoint $30,000 used [S8] — see Modeling Assumptions, MA3 |
| Derived dollars-per-transistor figure | $30,000 ÷ 8.0 × 10¹⁰ = 3.75 × 10⁻⁷ $/transistor |
| Option A — price per good die (computed) | 3.75 × 10⁻⁷ × 2.00 × 10¹⁰ = $7,500 |
| Flagship pricing premium applied to Option B only | ×1.19 — see Modeling Assumptions, MA4 [S9] |
| Option B — price per good die (computed) | (3.75 × 10⁻⁷ × 4.00 × 10¹⁰) × 1.19 = $15,000 × 1.19 = $17,850 |
| Option A — revenue per wafer (computed) | 492 × $7,500 = $3,690,000 |
| Option B — revenue per wafer (computed) | 191 × $17,850 = $3,409,350 |

Referenced from Background and forces D5's revenue-per-wafer computation.

---

## Modeling Assumptions

> These figures are **not TSMC's own disclosed, exact figures** — no foundry publicly discloses its
> current proprietary defect density or transistor density for a specific node. They are
> industry-representative figures, chosen from real published ranges and disclosed here rather than
> presented as this case's chip's own confirmed specification. A Hero may challenge them in
> discussion — that is a legitimate move.

| # | Assumption | Value used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | Transistor density at the assumed leading-edge logic node | 2.00 × 10⁸ transistors/mm² (200 million/mm²) | A round, representative figure chosen from within the real published range for TSMC's N3-generation logic process — 167 to ~300 million transistors/mm² across a disclosed target figure and independently-reported estimates (see Appendix G — Sources, S4). | This figure scales both options' transistor counts and prices by the same factor, so it does not change which option wins — only the absolute dollar figures in D5. |
| MA2 | Defect density assumed for this tape-out's process node | 3.0 × 10⁻¹ defects/cm² (0.30) | A representative figure for a leading-edge line that has **not yet fully matured** — this is the company's *first* tape-out on this node, so a higher, less-mature defect density is a more defensible planning assumption than the "mature, established line" benchmark, while still sitting below the real, disclosed ceiling a major foundry has reported for one of its own newest nodes (see Appendix G — Sources, S6). This is the one figure in the case that is not knowable in advance for any specific, not-yet-running process line — every foundry treats its live defect density as commercially sensitive. | Work D4/D5 under this value to see which option wins, and by how much. If the true defect density were meaningfully higher or lower than this figure, would your recommendation change — and at roughly what value would it flip? |
| MA3 | Real-world product used to derive the dollars-per-transistor pricing benchmark | Nvidia H100 GPU compute die: 80 billion transistors, $30,000 midpoint of its disclosed street/OEM price range (see Appendix G — Sources, S7/S8) | The real product's own price is for a fully packaged, sold unit, not a bare die — used here only as an illustrative proxy to derive a per-transistor benchmark, disclosed rather than presented as this case's own chip's confirmed market price. | Affects both options' absolute prices equally (same per-transistor rate applied to both), so it does not change which option wins — only the absolute dollar figures in D5. |
| MA4 | Flagship pricing premium applied to Option B (the Full Die) only, beyond pure linear per-transistor scaling | ×1.19 | Real market pricing shows a large, more-capable chip does not sell for a merely proportional multiple of a smaller chip's price — comparing two real, disclosed products (a smaller real inference-class GPU against the Nvidia H100 used for MA3) shows the larger, more-capable chip's real dollars-per-transistor rate running several times higher than the smaller chip's, not just proportionally higher (see Appendix G — Sources, S9). This case applies a deliberately conservative, disclosed fraction of that real effect (a 19% premium above pure linear scaling) rather than the full empirical ratio, so the dilemma stays genuinely close rather than one-sided. | **This is the figure most directly in tension with MA2.** A higher premium favors Option B; a higher defect density favors Option A. Work D5's "what would flip it" question against MA2 first — the premium is held fixed for this case's D5, but naming which of the two assumptions your recommendation is *more* sensitive to is itself worth discussing. |

Referenced from Appendix D and Appendix E.

---

## Appendix F — "How To…" Math Questions To Research

**Vocabulary terms**

- Standard Notation
- Scientific Notation

**"How to…" questions**

- How to write a number in scientific notation given its standard notation
- How to write a number in standard notation given its scientific notation

---

## Appendix G — Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Standard leading-edge silicon wafer diameter | 300 mm | Wevolver — [200 mm Wafer vs 300 mm Wafer: A Technical Comparison for Engineers](https://www.wevolver.com/article/200-mm-wafer-vs-300-mm-wafer-a-technical-comparison-for-engineers) | current industry standard | HIGH |
| S2 | Gross-die-per-wafer geometry formula (edge-loss corrected) | Gross Dies = (Wafer Area ÷ Die Area) − (π × Wafer Diameter) ÷ √(2 × Die Area) | AnySilicon — [Die Per Wafer Formula & Free Calculators](https://anysilicon.com/die-per-wafer-formula-free-calculators/); Silicon Analysts — [How Many Chips Per Wafer? GDPW Calculator & Die Yield Guide](https://siliconanalysts.com/guide/chips-per-wafer) | 2026 | MEDIUM |
| S3 | Realistic real-world die-size range (grounds Option A/B's design-choice areas) | IoT MCU ~25 mm², Smartphone SoC ~120 mm², Laptop CPU ~200 mm², Nvidia H100 ~814 mm² | Silicon Analysts — [How Many Chips Per Wafer? GDPW Calculator & Die Yield Guide](https://siliconanalysts.com/guide/chips-per-wafer) | 2026 | MEDIUM |
| S4 | Transistor density range, TSMC N3-generation (3nm-class) logic node | 167–300 million transistors/mm² (target 250) | TechPowerUp — [TSMC 3nm Process Packs 250 Million Transistors Per Square Millimeter](https://www.techpowerup.com/265991/tsmc-3nm-process-packs-250-million-transistors-per-square-millimeter); corroborated by WikiChip Fuse and PhoneArena reporting the same figure | 2026 | MEDIUM |
| S5 | Seeds defect-density die-yield model | DY = 1 ÷ (1 + A×D₀) | UC Berkeley IEOR, Prof. Robert C. Leachman — [Yield Modeling and Analysis, IEOR 130](https://fog.misty.com/perry/cod/references/yield_models.pdf) | Spring 2014 course notes (model: Seeds, 1967) | HIGH |
| S6 | Representative "mature, manufacturable" defect-density benchmark; real Intel 18A figure | D₀ < 0.1 defects/cm² → ~90% yield (1 cm² die) benchmark; Intel 18A reported D₀ < 0.40 defects/cm² | Vik's Newsletter (Vikram Sekar) — [How Foundries Calculate Die Yield](https://www.viksnewsletter.com/p/how-foundries-calculate-die-yield) | 2024-09-15 | MEDIUM |
| S7 | Nvidia H100 (GH100) compute-die transistor count | 80 billion transistors | NVIDIA — [H100 Tensor Core GPU Architecture (Hopper Whitepaper)](https://www.advancedclustering.com/wp-content/uploads/2022/03/gtc22-whitepaper-hopper.pdf) | 2022 | HIGH |
| S8 | Real-world street/OEM price range, packaged Nvidia H100 GPU module | $25,000–$40,000 (midpoint $30,000 used) | IntuitionLabs — [NVIDIA H100 Price 2026: $25K–40K, Plus H200/B200/B300](https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide) | early 2026 | MEDIUM |
| S9 | Real-world evidence that a larger, more-capable chip commands a per-transistor price well above a smaller chip's, not merely a proportional multiple | Nvidia L4 (smaller, inference-class GPU): 35.8 billion transistors, ~$2,000–$3,000 street price (implied ~7 × 10⁻⁸ $/transistor) versus Nvidia H100's ~3.75 × 10⁻⁷ $/transistor (S7/S8) — roughly a 5× real gap, of which this case applies only a 19% fraction (MA4) | JarvisLabs — [NVIDIA L4 GPU: Price, Specs & Cloud Pricing Guide](https://jarvislabs.ai/blog/l4-gpu-price) | 2026 | MEDIUM |

A full record of what was searched, found, and set aside while sourcing this case is kept in a
separate research log, outside this document.

---

## Appendix H — Real-World Vocabulary

This case uses real semiconductor-industry terms. None of these are math vocabulary (that list is
Appendix F) — this table is here so the industry setting itself does not get in the way of the
math.

| Term | Plain-language definition |
|---|---|
| Tape-out | The point at which a chip's design is declared finished and sent to a foundry to be manufactured. Everything before this is design work; everything after is manufacturing. |
| Fabless (company) | A company that designs chips but does not own or operate the factories that manufacture them — it pays a foundry like TSMC to do the physical manufacturing. |
| Foundry | A company that manufactures chips designed by other companies, using its own factories. TSMC is the world's largest foundry. |
| Silicon | The base material chips are manufactured from — a thin, hard, semiconducting element. "Silicon" is also used loosely to mean "chips" in general. |
| Wafer | A large, thin, circular disc of silicon on which many identical copies of a chip design are manufactured at once, then cut apart. |
| Wafer lot | A batch of wafers processed together as one manufacturing order. A foundry commitment is usually made and billed by the lot, not by the individual wafer. |
| Process quarter / wafer-start slot | Foundries schedule manufacturing capacity in advance; a "wafer-start slot" is a reserved place in that schedule for a customer's wafers to begin processing during a given quarter. Missing the slot means waiting for the next available one. |
| Process node | A named generation of manufacturing technology (for example, a "3-nanometer-class" node) that determines how small and how densely packed a chip's transistors can be. Newer nodes generally pack more transistors into the same area. |
| Mask set / reticle | The physical stencil(s) used to pattern each layer of a chip design onto a wafer, similar to a stencil used in printing. Once a mask set is manufactured for a specific die design and size, changing the die size means starting over with a new, separately paid-for mask set — this is why the decision in this case is treated as irreversible once ordered. |
| Floorplan | The physical layout of a chip's internal components — where each functional block sits on the die. Two floorplans of different sizes can implement different amounts of the same underlying design. |
| Die | A single, individual rectangle of silicon — one un-packaged chip — before it is cut from the wafer and packaged. |
| Transistor | The basic microscopic on/off switch that all digital computation is built from. A chip's total transistor count is a rough proxy for how much computing capability it has. |
| Defect | A microscopic manufacturing flaw (a stray particle, a processing error, etc.) that lands at random on a wafer during manufacturing and can make any die it lands on stop working correctly. |
| Yield | The fraction (or percentage) of manufactured dies that actually work and can be sold, out of all the dies attempted. |
| Edge loss | Gross die counts near the round edge of a circular wafer are reduced because square/rectangular dies cannot be cut cleanly from a curved edge — some die-shaped positions there are unusable. |
| GDPW | An abbreviation for "Gross Dies Per Wafer" — the raw count of die-shaped positions that fit on a wafer, before accounting for yield. |
| GPU | "Graphics Processing Unit" — a type of chip originally built for rendering images, now also widely used for AI computation because of its ability to do many calculations in parallel. |
| SoC | "System on a Chip" — a single chip that combines multiple functions (such as a processor, memory controller, and graphics) that might otherwise be separate chips. |
| MCU | "Microcontroller Unit" — a small, simple, low-power chip used to control a single device or function (for example, inside an IoT sensor), much less powerful than a GPU or SoC. |
| Packaged chip vs. bare die | A "bare die" is the raw silicon rectangle straight from the wafer. A "packaged chip" (or module) is that die mounted, wired, and enclosed in a protective housing with connectors — ready to be installed and sold as a finished product. A packaged product's price includes far more than just the silicon. |
| OEM price | "Original Equipment Manufacturer" price — the price a manufacturer or authorized reseller charges, as distinct from a marked-up retail or resale price. |
| Street price | The price real buyers actually pay in the open market, which can differ from any single published list price — it moves with supply, demand, and discounting, which is why sources in this case give a *range* ($25,000–$40,000, for example) rather than one fixed number. |
| Board (of directors/leadership) | The small group of senior leaders and/or investor representatives a company's executives are accountable to for major decisions. "The board is dialed in" means company leadership is on the call waiting for Priya's recommendation. |
| CEO | "Chief Executive Officer" — the single most senior executive running the company day-to-day, who reports to the board above. |
| Reticle-order screen | The internal software portal through which a chip company formally submits its finalized die design and size to the foundry, starting the manufacturing process — the specific "submit" action in this case. |
| Reticle lock deadline | The cutoff time by which the die-size decision must be finalized and submitted, because once the reticle (mask) is manufactured to a specific size, it cannot be resized — it is the same event as "the mask set is cut" in Background, described from the scheduling side rather than the manufacturing side. The wafer-start slot and the reticle lock deadline in this case fall on the same day: the slot cannot be used until the reticle for it is locked. |
| Leading-edge (node) | Among the newest, smallest, most advanced manufacturing technology generations a foundry offers — as opposed to older, larger, cheaper "mature" nodes still used for simpler chips. Leading-edge nodes typically have higher defect densities early on because the process itself is newer and less proven. |
| First tape-out (as a company milestone) | A company's very first time sending a design to be manufactured is treated with extra caution because the company has no track record with that specific foundry, process, or design flow yet — unlike a company on its tenth tape-out, there is no prior real-world yield data of its own to lean on, which is part of why this case treats the defect density as an assumption rather than a known fact. |
| Flagship pricing premium | A real, common industry pricing practice: a company's largest, most-capable product in a lineup is often priced *more than proportionally* higher than a smaller product, not just scaled up by size or transistor count — because a limited number of customers need that top tier of capability and are willing to pay disproportionately for it. This case applies a modest, disclosed version of that real practice to Option B's price (see Appendix E, MA4). |
| Commercially sensitive (data) | Information a company deliberately keeps private because revealing it would help competitors or hurt negotiating position — which is why no foundry publishes its actual, current defect density for a specific customer's manufacturing line. |
| How many wafers are in "one lot" | This case does not state an exact wafer count for "one lot" — only that it is the single, fixed unit of manufacturing capacity the company has committed to and cannot exceed this quarter. A real wafer lot is typically a small batch (commonly cited industry practice: roughly two dozen wafers), but the exact number does not change any of this case's math, which is computed on a per-wafer basis and simply scales up by however many wafers are in the lot. |
| Wafer-start slot vs. reticle lock deadline — same event | These are the same underlying cutoff, described from two different angles: the "wafer-start slot" is the foundry's scheduling term for when Priya's wafers are allowed to begin processing, and it cannot open until the "reticle" (the physical mask, sized to Priya's chosen die) has been finalized and sent to be manufactured — that finalization moment is the "reticle lock." Appendix A's 3-hour countdown is the time left to lock the reticle before today's wafer-start slot is forfeited. |
| Compute capability | The practical amount of useful computation (e.g., how much AI model math) a chip can perform per unit time. It is not a single directly-observable number in this case — the case uses transistor count only as a rough stand-in for it, the same way a car's engine size is a rough (not perfect) stand-in for how powerful the car is. |
| Flagship (product) | The single most capable, most expensive product in a company's lineup at a given time — as opposed to entry-level or mid-range products in the same family. A "flagship" GPU is the biggest, fastest one a company currently sells. |
| AI chip / AI-chip startup | A chip (or a company that designs chips) built specifically to run the heavy repetitive math behind AI models efficiently, as opposed to general-purpose chips built to run any ordinary software. GPUs (see above) are the most common real-world example of AI chips today. |
| Director of silicon engineering | A senior engineering leadership title at a chip company, typically responsible for the technical decisions and tradeoffs involved in actually designing and manufacturing a chip (as opposed to, say, sales or finance roles) — which is why this is the person with authority to sign off on a physical decision like die size. |
| "Seeds" (in "Seeds model") | The surname of the model's original author (R.B. Seeds, who published it in 1967) — like many named formulas, it is simply called after the person credited with first deriving it, not an acronym or description of what it does. |
| "N3" / "3nm" (node naming) | A marketing/generational label, not a literal physical measurement of any single feature on the chip today — modern "Nnm" node names track a foundry's own generation numbering more than one exact real-world distance. What matters for this case is only the relative ordering (a newer, smaller-numbered node packs transistors more densely than an older, larger-numbered one), not the literal nanometer value. |
| Intel | A large, real semiconductor company that, like TSMC, both designs and (unlike most of TSMC's customers) manufactures its own chips in its own factories — it is one of TSMC's real-world competitors as a manufacturer. "18A" is simply Intel's own name for one of its newest manufacturing nodes, cited here only for its disclosed defect-density figure, not because Intel is otherwise part of this story. |
| Compute die | On a multi-chip product (like a modern GPU module, which can combine a main logic die with separate memory dies), the "compute die" is specifically the one doing the actual calculations — as opposed to memory or other supporting dies on the same package. This case's transistor-count and pricing figures for its real-world reference products refer to the compute die specifically. |
| Inference-class (GPU) | AI use splits roughly into "training" (the slow, extremely compute-heavy process of teaching a model) and "inference" (the faster, lighter process of actually using an already-trained model to answer a question). An "inference-class" GPU is built and priced for the lighter, cheaper inference workload rather than the heaviest training workloads. |
| Hero | This program's own term for the student completing the case study — used the same way "the reader" or "the student" would be used elsewhere. |
| Adventure (studio label) | An internal label naming which format/track of case study this is, out of more than one the program offers — not something that changes how the math works. |
| "Excellent" (word-count quality bar) | This program's own standard for thorough, well-reasoned writing (as opposed to word count alone) — the specific rubric for what counts as "excellent" is set by the discussion facilitator/instructor, not by this document. |
| Stand-up (meeting) | A short daily team meeting (commonly held standing up, to keep it brief) common in engineering workplaces — used here only as background texture for the scene, not something the case's math depends on. |
| CPU | "Central Processing Unit" — the general-purpose main chip of a computer, historically the single chip that ran most software (as distinct from a GPU, which specializes in the parallel math AI and graphics need). |
| IoT | "Internet of Things" — small, often single-purpose internet-connected devices (sensors, smart appliances, etc.), the typical use case for a small, low-power MCU. |
| GH100 | Nvidia's own internal engineering name for the specific compute die used inside the H100 product — "H100" is the product name a customer buys; "GH100" is the die itself. |
| Whitepaper | A detailed technical document a company publishes to describe how a product works, typically aimed at engineers and customers rather than general consumers — the source for this case's real Nvidia transistor-count figure. |
| IEOR | "Industrial Engineering and Operations Research" — the university department whose course produced the yield-model source cited in this case. |
| Logic (node/process) | Chips broadly split into "logic" (the switching circuits that perform computation — CPUs, GPUs, SoCs) and "memory" (circuits that store data). A "logic node" or "logic process" is a manufacturing process tuned for building computation circuits specifically, as opposed to memory chips, which are often manufactured differently. |
| Sensitivity (as an analysis concept) | How much a final answer or recommendation would change if one particular input turned out to be wrong or different — a figure the recommendation is "highly sensitive to" is one where getting that input wrong would likely change the conclusion; a figure it's "not sensitive to" barely matters even if it's off. |
| Confidence rating (HIGH/MEDIUM/LOW, in Appendix G) | This case's own label for how trustworthy each cited source is. "Primary" means the source is the original organization the fact is actually about (for example, Nvidia's own document about its own product). "Corroborated" means two or more independent outlets report the same figure, which makes it more trustworthy than any one of them alone. HIGH = a primary source, or multiple independent outlets agreeing; MEDIUM = a real source with some caveat (an estimate, a stand-in figure, or only one non-primary outlet); LOW (not used in this case) = a source too weak to rely on for a real conclusion. |

---

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
