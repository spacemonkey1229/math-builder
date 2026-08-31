# Case Study: The Clampband Margin

MS | Math | Case Study | 2026-27 | Launchpad

*(Band: MS-stretch / HS-entry. This case uses precalculus limit and asymptote vocabulary — the same reasoning that describes how a value behaves as some quantity grows without bound — applied to a real spacecraft tolerance-stack decision.)*

---

## Overview

Wes Okonkwo has the drawing pulled up on two monitors and a paper printout of the same drawing on the desk between them, because he has learned not to trust himself to catch an error on a screen alone.

The satellite ships to the launch site in two weeks. Everything else on it is done — solar arrays folded and stowed, harness routed, thermal blankets closed out — except for the one signature block still empty at the bottom of the separation-joint drawing: his. The clampband is the last thing holding the satellite to the rocket, and the first thing that has to let go, cleanly, on command, four hundred miles up, with no technician standing by to give it a second try.

Three different shops made the three parts that stack together at that joint, and all three came back from inspection this morning marked "accept" — each one is genuinely within its own printed tolerance. That is exactly the problem. Wes has two spreadsheets open, each one a different way of adding those three "accept" numbers together into a single predicted margin, and the two spreadsheets do not agree on how much room the joint actually has.

His phone buzzes with a text from the program manager asking if the drawing is signed yet. Wes doesn't answer it. He minimizes the message, leans back, and looks at the two numbers side by side.

---

## Background

Wes Okonkwo is a mechanical integration engineer at a small-satellite prime contractor. He owns the mechanical sign-off on the payload separation system for the company's current spacecraft, and his signature on the clampband joint drawing is the one that certifies the joint is ready to fly. Once the satellite is integrated to the launch vehicle at the range, this decision cannot be revisited — there is no on-orbit rework for a separation joint that fails to release (SEE APPENDIX A).

The joint in question is a **Marman-style clampband** — a band that clamps two mating flanges together under preload, and is designed to release both flanges cleanly the instant the band is cut or unlatched. Three separate interfaces stack together to determine how much margin the joint actually has once it's assembled, and each interface comes from a different supplier: the bus adapter flange outer diameter, the clampband ring inner diameter, and the preload bolt-and-shim assembly (SEE APPENDIX C). Every one of the three parts delivered for this build passed its own supplier's inspection against its own printed tolerance. None of the three suppliers did anything wrong.

The question is how to combine those three independently-toleranced parts into a single predicted number for how tight or loose the joint will actually be — and how that predicted number should be checked against published clampband design-margin thresholds (a NASA design guideline's own preload criterion, paired with the numeric margins real clampband programs design to) (SEE APPENDIX B).

Two methods are on the table.

**The Worst-Case Stack.** Add all three suppliers' tolerances directly, assuming the worst possible combination of all three parts could occur at once. This is the conservative approach: it guarantees that every accepted joint releases correctly under any combination of in-spec parts, at the cost of a wider predicted tolerance band — which means rejecting (and reworking, or requesting replacement parts for) some individual parts that are genuinely within their own printed spec, simply because the specific combination on hand happens to fall near the edge.

**The Modified RSS Stack.** Combine the three suppliers' tolerances using the root-sum-square method (the square root of the sum of the squares), then apply the correction factor that real tolerance-stacking practice applies on top of it. Pure, uncorrected RSS assumes every supplier's printed ± tolerance is a true 3-sigma bound on a centered, normal, independent process — an assumption that a 1962 tolerance-stacking study (later adopted into Motorola's Six Sigma mechanical design practice) found routinely fails in practice, because printed tolerances are often really closer to a 2-sigma range. The correction is a flat ×1.5 multiplier on the RSS result (SEE APPENDIX D) — real, industry-standard practice, not a full worst-case sum, but not naive uncorrected RSS either. It still produces a narrower predicted tolerance band than the Worst-Case Stack, passing more of the individually in-spec parts on hand — but it still depends on the same underlying assumption that the three suppliers' manufacturing variations are statistically independent, an assumption that holds well across a large production run and is harder to defend for one specific joint built from one specific set of three parts.

Both methods are legitimate, real engineering practice; nothing about the joint's design requires one over the other. What changes the comparison is that this contractor's satellite line is scaling: near-term programs call for clampband joints with more than three contributing supplier interfaces (SEE APPENDIX D). Extending both stack-up formulas to those future joints, and converting NASA-adjacent industry's dimensionless margin thresholds into a comparison against a dimensional tolerance stack, requires stating a handful of scenario modeling choices, disclosed in full — including how much confidence to place in each one — in Appendix E (SEE APPENDIX E). The worst-case stack and the Modified RSS stack do not grow the same way as more suppliers are added to a joint, and Wes's sign-off has to hold not just for this satellite's three-supplier joint, but as a stated position on how the company evaluates every future joint of this kind. Published recommended design-margin thresholds for clampband systems, the real per-supplier tolerance values for this build, and the stack-up math for both methods across a growing supplier count are in the appendices below. Every external source cited anywhere in this case is collected in Appendix F. The vocabulary and "how to…" skills this case asks you to research are listed in Appendix G — that is where Challenge 1 sends you.

---

## Dilemma

You are Wes Okonkwo.

Do you:

**A.)** Sign off using **the Worst-Case Stack** — size the release-preload margin by summing all three suppliers' tolerances directly **OR**

**B.)** Sign off using **the Modified RSS Stack** — size the release-preload margin using the root-sum-square of all three suppliers' tolerances, scaled by the industry-standard ×1.5 correction factor

---

## Challenges

1.) Research and find an online resource that answers one of the "how to…" questions from the case study launch. Post a link to the resource as your submission.

2.) Post 250 or more "excellent" words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:
    a.) Use of the "how to…" resource you researched in Challenge 1.
    b.) At least one original visual display of the data.

3.) Include the following:

- **D1 — A stack-up table across a growing supplier count.** Using the per-interface tolerances in Appendix C and the stack-up formulas in Appendix D, build a table of the predicted total tolerance under the Worst-Case Stack and under the Modified RSS Stack, for a joint with 3 contributing supplier interfaces up through the largest count shown in Appendix D. From the table, estimate how each method's predicted tolerance behaves as the number of contributing interfaces keeps growing.
- **D2 — A horizontal asymptote identified algebraically.** Write the ratio of the Modified RSS Stack's predicted tolerance to the Worst-Case Stack's predicted tolerance as a function of the number of contributing supplier interfaces, $n$. Using that equation directly — not your table from D1 — identify the function's horizontal asymptote algebraically, and show the algebra.
- **D3 — A margin-threshold continuity check.** For each stack-up method, compare your D1 table's predicted margin, at every supplier count $n$, against NASA's recommended design-margin thresholds in Appendix B. State, for each method, whether the pass/fail outcome against those thresholds changes smoothly or jumps abruptly somewhere in your table — and if it jumps, name the specific supplier count where that happens.
- **D4 — The current three-supplier margin.** Using Appendix C's real per-interface tolerances for this build's actual three suppliers, compute the predicted total tolerance under each stack-up method for $n = 3$, and state how each compares to NASA's design-margin thresholds from Appendix B for this specific joint, today.
- **D5 — An original visual.** Graph both stack-up functions from D1 — the Worst-Case Stack and the Modified RSS Stack — against the number of contributing supplier interfaces, over the same range you tabulated in D1. Mark the horizontal asymptote you found in D2 and mark the supplier count you identified in D3, if any. This satisfies Challenge 2(b).

4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count.

5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 "excellent" words on the questions above.

---

## Appendix A: The Shipment Constraint

| Quantity | Value |
|---|---|
| Days remaining until the satellite ships to the launch site | 14 days |
| Number of competing stack-up methodologies the joint sign-off may use | Exactly one — the drawing carries a single signature and a single stated method |
| Whether the sign-off methodology can be revisited after the satellite is integrated to the launch vehicle | No |
| Joint type | Marman-style clampband separation joint |
| Document Wes's sign-off certifies | The mechanical closure/acceptance record for the payload separation system |

*Note: the contractor and program in this case are a scenario construction — there is no real company or spacecraft named here. The Marman clampband joint concept, the published design-margin guidance in Appendix B (a real NASA guideline's own preload criterion, paired with real numeric margins from a named clampband engineering paper), and the ISO 2768 and Protolabs tolerance references (Appendix C) are all real.*

---

## Appendix B: Marman Clamp Design-Margin Thresholds

| Quantity | Value |
|---|---|
| Guideline document (qualitative design criterion) | NASA Preferred Reliability Practices, **Guideline No. GD-ED-2214, "Marman Clamp System Design Guidelines,"** issued by Goddard Space Flight Center (GSFC). The document itself carries no printed date; it is one of roughly 100 guidelines in NASA's Preferred Reliability Practices series compiled by the NASA Reliability & Maintainability Steering Committee [S1]. |
| GD-ED-2214's own preload-design criterion | GD-ED-2214 states its criterion in words, not as a numeric factor: **"The criterion for designing strap preloads is that no gapping occurs when the maximum expected load is applied"** [S1]. |
| Numeric preload gapping margin used industry-wide (minimum) | **1.25** — i.e., the band is sized to the load needed to prevent gapping, multiplied by 1.25, so the joint still does not gap at 1.25× the predicted worst-case load [S2]. |
| Numeric release-element margin used industry-wide (minimum) | **>2.00** — the release device (bolt cutter, pyrotechnic bolt, or similar) is designed to carry more than double the predicted release load [S2]. |
| How each margin is defined relative to a predicted tolerance stack | **Neither source publishes a formula connecting a dimensional tolerance-stack value (Appendix C/D, inches) directly to these load-based margin factors** — GD-ED-2214's criterion and the 1.25/2.00 figures are load-safety-factors, not tolerance-stack ratios. This case bridges the two with a stated, disclosed Modeling Assumption (Appendix E, MA4), since no public source performs that conversion for a general clampband joint. |

*Correction from the case's original working assumption: GD-ED-2214 itself does not contain the numeric values "1.25" or ">2.00" — those numbers were mis-attributed to it in an earlier internal note. Having now read the full 8-page GD-ED-2214 document directly, its actual, real content is the qualitative no-gapping criterion above; it defines no numeric margin. The numeric 1.25 and >2.00 figures are genuinely real and genuinely industry-cited — they come from a separate, named engineering conference paper (Appendix F, S2), not from GD-ED-2214. Both sources are real; they are just two different documents, and this appendix now cites each for what it actually says. See RESEARCH_LOG.md for the full trail.*

---

## Appendix C: The Three-Supplier Tolerance Stack

*The clampband's nominal diameter (15.000 in) and the preload bolt+shim stack's nominal height (0.500 in) are a stated scenario assumption (Appendix E, MA3) — no real program's exact dimensions are named here. The tolerance **class** assigned to each supplier and the tolerance **values** themselves are real, cited figures.*

| Interface | Supplier | Governing tolerance standard/source | Toleranced dimension | Tolerance (±) |
|---|---|---|---|---|
| Bus adapter flange outer diameter | Supplier B | ISO 2768-1, tolerance class **f (fine)** [S3] | 15.000 in (381.0 mm) nominal OD | **±0.0079 in** (±0.2 mm) [S3] |
| Clampband ring inner diameter | Supplier A | Protolabs published standard CNC machining tolerance [S4] | 15.000 in (381.0 mm) nominal ID | **±0.0050 in** (±0.13 mm) [S4] |
| Preload bolt + shim stack height | Supplier C | ISO 2768-1, tolerance class **f (fine)** [S3] | 0.500 in (12.7 mm) nominal stack height | **±0.0039 in** (±0.1 mm) [S3] |

**ISO 2768-1 general tolerance classes, Table 1 — Linear Dimensions (for reference; permissible deviation in mm by nominal-length range) [S3]:**

| Tolerance class | Descriptive name | 0.5–3 mm | 3–6 mm | 6–30 mm | 30–120 mm | 120–400 mm | 400–1000 mm |
|---|---|---|---|---|---|---|---|
| f | Fine | ±0.05 | ±0.05 | ±0.1 | ±0.15 | ±0.2 | ±0.3 |
| m | Medium | ±0.1 | ±0.1 | ±0.2 | ±0.3 | ±0.5 | ±0.8 |
| c | Coarse | ±0.2 | ±0.3 | ±0.5 | ±0.8 | ±1.2 | ±2.0 |
| v | Very coarse | — | ±0.5 | ±1.0 | ±1.5 | ±2.5 | ±4.0 |

*(Full table extends to 4000 mm; only the ranges relevant to this build's dimensions are reproduced above. Supplier B's flange OD, 381.0 mm, falls in the 120–400 mm row; Supplier C's stack height, 12.7 mm, falls in the 6–30 mm row.)*

**Protolabs published CNC/injection-molding tolerance guidelines (for reference, as a cross-check on what a precision shop actually holds):**

| Process | Published standard tolerance (±) |
|---|---|
| CNC machining | **±0.005 in** (±0.13 mm) — Protolabs' standard prototype/production machining tolerance, stated as consistent with ISO 2768-1-1989-f (metals) / -m (plastics) [S4] |
| Injection molding | **±0.003 in** (±0.076 mm) mold-tool tolerance; the finished molded part's own resin/shrink tolerance is a separate, size-proportional figure of at least ±0.002 in per inch of dimension (±0.051 mm/mm) [S5] |

*Not every row above is used in every Challenge calculation. This build's three named parts (Appendix C's first table) use ISO 2768-f for two interfaces and Protolabs' CNC figure for the third; the injection-molding row is provided only as a comparison point, since none of this joint's three parts are injection-molded.*

---

## Appendix D: Stack-Up Formulas Across a Growing Supplier Count

The **Worst-Case Stack** predicts a total tolerance equal to the direct sum of every contributing interface's tolerance:

$$T_{WC}(n) = \sum_{i=1}^{n} t_i$$

The **Modified RSS Stack** predicts a total tolerance equal to the root-sum-square of every contributing interface's tolerance, scaled by a real, industry-standard correction factor of **1.5** — the "Benderizing" correction, from a 1962 tolerance-stacking study later folded into Motorola's Six Sigma mechanical-design tolerancing practice, which found that printed supplier tolerances routinely behave like a real 2-sigma spread rather than the 3-sigma spread pure RSS assumes, and corrected for it with a flat ×1.5 multiplier (SEE APPENDIX F, S6):

$$T_{MRSS}(n) = 1.5\sqrt{\sum_{i=1}^{n} t_i^2}$$

where $t_i$ is the $\pm$ tolerance of the $i$-th contributing supplier interface and $n$ is the number of contributing interfaces in the joint.

| Number of contributing supplier interfaces ($n$) | Worst-Case Stack, $T_{WC}(n)$ | Modified RSS Stack, $T_{MRSS}(n)$ (assuming interfaces of equal tolerance to Appendix C's average) |
|---|---|---|
| 3 (this build) | **0.0168 in** (0.0079 + 0.0050 + 0.0039, Appendix C's real values) | **0.0152 in** ($1.5\sqrt{0.0079^2+0.0050^2+0.0039^2}$, Appendix C's real values) |
| 6 | 0.0336 in | 0.0206 in |
| 7 | 0.0392 in | 0.0222 in |
| 10 (largest modeled) | 0.0560 in | 0.0266 in |

*The specific future supplier counts above (6, 7, 10) are a stated scenario extension of this real three-supplier joint, disclosed in full in Appendix E, MA1 — used so Challenges D1–D3 and D5 have more than a single data point to estimate a trend from. Rows beyond $n=3$ use Appendix C's average per-interface tolerance, 0.0056 in, per Appendix E, MA2 — not each future supplier's own (nonexistent) distinct value.*

---

## Appendix E: Modeling Assumptions

> These figures are **not sourced** the way Appendix B's NASA margins or Appendix C's real tolerance standards are. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.

| # | Assumption | Value / method used | Basis | Sensitivity |
|---|---|---|---|---|
| MA1 | The future supplier-interface counts used to extend Appendix D beyond this build's real 3-supplier joint | **n = 6, 7, and 10.** These are not arbitrary: given Appendix C's real per-interface tolerances, n = 6 is the last count at which the Worst-Case Stack still clears NASA's release-element margin threshold (Appendix B) under this case's margin model (Appendix E, MA4); n = 7 is the first count at which it does not; n = 10 is where the Worst-Case Stack sits almost exactly at NASA's gapping-margin floor. | No public source describes this specific contractor's future joint designs, because the contractor itself is a scenario construction. The two stack-up formulas (Appendix D) and the real margin thresholds (Appendix B) are real regardless of which future counts are chosen to illustrate the trend — these three were chosen because they are the counts where that real math actually changes the pass/fail answer. | Changing the specific future counts shifts exactly where D1's table samples the trend, but does not change which method's tolerance grows faster as $n$ increases, nor the location of the crossover — both are fixed by the two real formulas and Appendix C's real tolerances. |
| MA2 | Treating the Modified RSS Stack's future rows in Appendix D as if all contributing interfaces share one equal, average tolerance, rather than each future supplier's own distinct value | **Average of Appendix C's three real tolerances: (0.0079 + 0.0050 + 0.0039) / 3 = 0.0056 in.** Every row beyond $n=3$ in Appendix D uses this single value for every added interface, in both the Worst-Case sum and the Modified RSS root-sum-square. | No real per-supplier tolerance values exist yet for interfaces that don't exist yet on a future joint design. Using this build's own real, sourced tolerances (Appendix C) as the basis for the average keeps the extension grounded in a real, cited figure rather than an invented one. | This assumption affects the exact numeric values in Appendix D's later rows, but the qualitative finding that motivates D1–D3 (how the two methods' growth compares, and that the ratio's horizontal asymptote is 0) holds under a range of reasonable per-interface tolerance choices, since it depends only on the two formulas' structure ($n$ vs. $\sqrt{n}$), not on the specific average used, and the ×1.5 factor is a constant multiplier that does not change which growth rate wins. |
| MA3 | The clampband's nominal diameter and the preload bolt+shim stack's nominal height | **15.000 in (381.0 mm)** nominal diameter for the mating flange OD / ring ID; **0.500 in (12.7 mm)** nominal stack height for the bolt+shim assembly. | No real program's specific joint dimensions are named here — the contractor and program are a scenario construction. These values were chosen to be representative of a small-satellite Marman-clampband separation-system size (a plausible range for this class of spacecraft), and are what determines which ISO 2768-1 dimension-range row (Appendix C) governs each interface's real, cited tolerance. | Changing the nominal dimensions could shift which ISO 2768-1 dimension-range row applies (Appendix C's table), which would change the specific tolerance values and therefore the specific numbers in Appendix D — but not the underlying comparison between the Worst-Case and Modified RSS *formulas*, which is independent of which real tolerance values are plugged in. |
| MA4 | A nominal per-joint gapping allowance, used to convert Appendix B's real, cited load-safety-factor margins (1.25 and 2.00, both dimensionless) into a comparison against Appendix C/D's real, cited tolerance-stack values (in inches) | **0.070 in.** This case defines a stack-up method's "margin" against Appendix B's thresholds as (0.070 in) ÷ (that method's predicted total tolerance, Appendix D). A result ≥ 1.25 is treated as clearing the gapping-margin threshold; a result ≥ 2.00 is treated as clearing the release-element-margin threshold. | Neither GD-ED-2214 nor the industry paper that reports the 1.25/2.00 figures (Appendix F, S2) publishes a formula connecting a dimensional tolerance-stack value to those load-based factors for a general clampband joint — that conversion does not exist in the public literature for this case to cite. This case states its own simple, transparent conversion rule instead of inventing a "real" formula that does not exist. | **This is the single most load-bearing assumption in the case.** A larger allowance shifts every crossover in Challenge D3 to a higher $n$; a smaller allowance shifts it lower. The 0.070 in value was chosen so that the crossover lands inside the modeled range (n = 6–7) rather than off the edge of the table, so the case's D1–D3 "does the pass/fail outcome jump" question has a real answer to find. A Hero who changes this number changes *where* the jump happens, not *whether* Worst-Case eventually falls behind Modified RSS — that is fixed by $n$ vs. $\sqrt{n}$ growth (Appendix D, D2), unaffected by the constant ×1.5 factor. |

---

## Appendix F: Sources

| # | Claim | Value | Source | Date | Confidence |
|---|---|---|---|---|---|
| S1 | Full title, document number, issuing authority, and qualitative preload-design criterion | "The criterion for designing strap preloads is that no gapping occurs when the maximum expected load is applied." No numeric margin factor is stated in this document. | NASA Preferred Reliability Practices, Guideline No. GD-ED-2214, "Marman Clamp System Design Guidelines," Goddard Space Flight Center ([PDF](https://extapps.ksc.nasa.gov/Reliability/Documents/Preferred_Practices/2214.pdf), mirrored at [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Guideline_No._GD-Ed-2214_Marman_Clamp_Systems_Design_Guidelines.pdf)) | n.d. (undated on the document; part of NASA's Preferred Reliability Practices series) | HIGH |
| S2 | Numeric design-margin practice: a gapping margin of 1.25 applied to the computed worst-case band load, and a release-element margin of >2.00 | "A reasonable choice is to design and test to 1.25x worst case load predictions. Maintaining high margins on the release element (>2.00) has been recommended... A margin on gapping of 1.25 is normally applied to this result." | C. Lazansky (Sierra Nevada Corporation), "Refinement of a Low-Shock Separation System," presented at the European Space Mechanisms and Tribology Symposium (ESMATS) / Aerospace Mechanisms Symposium ([PDF](https://esmats.eu/amspapers/pastpapers/pdfs/2012/lazansky.pdf)) | 2012 | MEDIUM — a named practicing engineer's peer-presented conference paper in a real, committee-reviewed, NASA/ESA-adjacent proceedings series reporting industry design practice, not a NASA-issued numeric standard; the release-element figure is itself attributed within this paper to a separate 1995 Aerospace Mechanisms Symposium paper on the Clementine spacecraft (Purdy & Hurley, "The Clementine Mechanisms"), which was not independently re-verified here |
| S3 | ISO 2768-1 general tolerance table (fine/medium/coarse/very-coarse classes, permissible deviation by nominal-length range) | Fine class, 120–400 mm: ±0.2 mm. Fine class, 6–30 mm: ±0.1 mm. (Full table in Appendix C.) | ISO 2768-1:1989, as reproduced by RpProto, "ISO 2768 1 & 2 - ISO General Tolerances Chart" ([PDF](https://www.rpproto.com/wp-content/uploads/2021/05/General-Tolerances-ISO-2768.pdf)) | n.d. (reproduction of ISO 2768-1:1989; ISO 2768-1 itself is a paywalled standard with no free primary hosting) | HIGH — values cross-validated against multiple independent industry republications (jlccnc.com, haizol.com, rivcut.com), all reporting identical class values |
| S4 | Protolabs' standard CNC machining tolerance and its ISO 2768 equivalence | "The standard prototype and production machining tolerance at the Protolabs automated factory is +/- 0.005 in. (0.13mm)... in accordance with ISO 2768-1-1989-f (metals), ISO 2768-1-1989-m (plastics)." | Protolabs, "Understanding CNC Machining Tolerances" ([link](https://www.protolabs.com/resources/design-tips/fine-tuning-tolerances-for-cnc-machined-parts/)) | n.d. (no publication date visible on page) | HIGH — primary manufacturer source |
| S5 | Protolabs' standard injection-molding tolerances (mold-tool and resin/shrink) | "Our machining tolerance of +/- 0.003 in. (0.076mm) refers to the tolerance built into the mold tool... The resin tolerance... can be greater than but no less than +/- 0.002 in./in. (0.051mm/mm)." | Protolabs, "Understanding Injection Molding Tolerances" ([link](https://www.protolabs.com/resources/blog/injection-molding-tolerances/)) | 2023-02-07 | HIGH — primary manufacturer source, dated |
| S6 | The ×1.5 "Benderizing" correction factor applied to RSS tolerance stacking, and its origin/rationale | "If Ti is specified with the misconception Ti ≡ 2σi, then Ti is too small by a factor 1.5. To correct for this, Bender (1962) suggests to multiply the ±T assy-stat value by 1.5... This inflation factor 1.5 gives up a fair amount of the gain in T assy-stat. In fact, for n = 2 it is more conservative than arithmetic tolerance stacking." Also cites Harry, M.J. and Stewart, R. (1988), "Six Sigma Mechanical Design Tolerancing," Motorola Government Electronics Group, as the source that carried this correction ("the Motorola formula") into standard industry practice. | F. Scholz (Boeing Research & Technology / Boeing Information & Support Services), "Tolerance Stack Analysis Methods" ([PDF](https://faculty.washington.edu/fscholz/Reports/isstech-95-030.pdf)), citing A. Bender Jr. (1962), "6 × 2.5 = 9, Benderizing tolerances — a simple practical probability method of handling tolerances for limit-stack-ups," Graphic Science, 17-21 | 1995 (Scholz report); 1962 (Bender, original) | HIGH — primary named-author engineering report from a major aerospace prime's own research organization (Boeing), citing the original 1962 source by name and equation; the 1962 Bender paper itself was not independently re-obtained, only Scholz's direct quotation and equation reproduction of it |

*Note on a correction made during research: an earlier internal note attributed the numeric values "1.25 gapping margin" and "release-element margin >2.00" directly to NASA GD-ED-2214. Having read GD-ED-2214 in full (all 8 pages), those numbers do not appear in it — the guideline states only the qualitative no-gapping criterion (S1). The numeric values are real and are genuinely used in industry practice, but their real source is the separate engineering paper cited as S2, not GD-ED-2214. This appendix, and Appendix B, now cite each document for what it actually contains.*

*Note on a retune pass (2026-08-30): this case's Option B was originally modeled as naive, uncorrected RSS. Further research (RESEARCH_LOG.md) found that real tolerance-stacking practice does not actually use naive RSS for exactly the reason Argument A raises — RSS's assumption that printed tolerances are true 3-sigma bounds is known to be optimistic — and instead applies the real, well-documented ×1.5 Bender/Motorola correction (S6). Modeling Option B as this real, more-defensible version of RSS (rather than the textbook-idealized version) is a genuine change in method, not an unexplained change in the numbers — every input tolerance in Appendix C and D is unchanged; only the formula used to combine them differs, and that formula and its correction factor are cited above rather than invented.*

---

### Appendix G — "How To…" Math Questions To Research

**Vocabulary terms**

- Limit
- Asymptote
- Continuity (Informal)

**"How to…" questions**

- How to estimate a limit from a table or graph
- How to identify a vertical or horizontal asymptote from a function's equation

<!-- FACILITATOR ONLY: balance argument, margin, and sensitivity notes live in FACILITATOR.md and case.json's balance object, not here. -->
