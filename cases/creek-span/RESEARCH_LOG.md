# Research Log — Creek Span

One row per placeholder: what was searched, what was found or rejected, and why.

| Placeholder | Searched | Found | Rejected | Disposition |
|---|---|---|---|---|
| Weight/ft, L2x2x1/4 angle | "L2x2x1/4 steel angle weight per foot AISC" | Engineers Edge AISC angle table: 3.21 lb/ft; cross-checked against SteelFloAI shapes database: 3.19 lb/ft (same nominal size, normal cross-source rounding) | — | **SOURCED** — S1, engineersedge.com, MEDIUM (reproduced AISC table, not the primary Steel Construction Manual) |
| Weight/ft, L3x3x1/4 angle | "L3x3x1/4 steel angle weight per foot" | Engineers Edge: 4.89 lb/ft; cross-checked SteelFloAI: 4.9 lb/ft | — | **SOURCED** — S2, engineersedge.com, MEDIUM |
| Weight/ft, L4x4x3/8 angle (original design) | "L4x4x3/8 steel angle weight per foot" | Engineers Edge: 9.72 lb/ft; STL Tech: 9.8 lb/ft | Not used in the final design — see "Redesign" note below | DROPPED (member size changed) |
| Weight/ft, L3x3x3/8 angle (retuned chord for Option B) | "L3x3x3/8 steel angle weight per foot AISC" | Engineers Edge: 7.17 lb/ft; Optimal Beam and SteelFlo both independently show 7.17-7.2 lb/ft | — | **SOURCED** — S3, engineersedge.com, MEDIUM |
| Structural steel angle price, USD/lb | "structural steel angle iron price per pound 2026"; "structural steel angle price per pound 2026 metal service center" | SteelFlo's 2026-02-12 post: angles/channels $950-$1,250/ton (early 2026, North America) | Direct retail service-center pages (Metals Depot, Coremark Metals) returned HTTP 403 to the fetch tool and could not be read; FRED PPI series (WPU1017, PCU3311103311107) carry an index value, not a directly convertible $/lb figure, without substantially more derivation work | **SOURCED as MEDIUM** — S4, midpoint of SteelFlo's stated range ($1,100/ton -> $0.55/lb). Flagged: no primary index is named by the publisher, so this is the case's single softest sourced figure; it is not, however, dilemma-flipping on its own (it scales both options' material cost by the same factor). |
| Wage rate, structural fabrication labor | "BLS occupational outlook handbook structural iron and steel workers median wage" | BLS OOH: median annual wage $62,780, May 2025 | An overall "Ironworkers" hourly figure ($29.77/hr) was also returned by search, but it aggregates a broader occupation group than the structural-iron-and-steel-workers detail this case wants | **SOURCED** — S5, bls.gov, HIGH. Hourly value is derived ($62,780 / 2,080 hr = $30.18/hr) since BLS did not publish an hourly median for this specific occupation on the fetched page; `derived: true`. |
| Gusset-plate labor hours per joint (MA1) | (anticipatory — no search performed; the case-write draft correctly predicted no public per-connection timing study would exist for small pedestrian-truss gusset fabrication) | NOT FOUND, as expected | — | **ASSUMPTION** — MA1, 1.5 hr/joint, basis stated in Appendix F. Flexed +/-50% in `sensitivity_model.py` Probe 5 (margin ranges 10.99%-16.70% across the flex, winner unchanged). |
| Triangle rigidity / why trusses are triangulated | "triangle only rigid polygon truss structural engineering explanation" | TeachEngineering "Triangles & Trusses" lesson: explicit statement that a triangle "cannot collapse" because its angles are fixed once its side lengths are fixed, unlike a square/rectangle | A TeachEngineering "Polygons, Angles and Trusses" companion lesson was checked first and only had a weaker, less explicit statement | **SOURCED** — cited in Background and Appendix H (teachengineering.org, cub_trusses_lesson01) |
| Triangle Inequality Theorem, definition | "Triangle Inequality Theorem definition site:mathsisfun.com OR site:khanacademy.org" | Math Is Fun: "Any side of a triangle must be shorter than the other two sides added together," with a < b+c etc. | — | **SOURCED** — cited in Appendix H |
| Warren truss / equilateral triangle web convention | "Warren truss diagonal members equilateral triangle web configuration textbook" | Wikipedia, Warren truss: "a type of truss employing a weight-saving design based upon equilateral triangles"; diagonals alternate tension/compression | A period reference (Milo Ketchum's "The Design of Highway Bridges") was named but not independently verified online within this pass | **SOURCED** — cited in Appendix H (Wikipedia, MEDIUM — reliable on this specific, verifiable, non-contested point) |
| Truss chord force vs. truss depth relationship | "truss depth chord force inversely proportional span bending moment structural engineering"; "chord force truss moment divided by depth explanation engineer" | teachbooks.io "Structural Design Essentials," Global Dimensioning of a Truss Beam: explicit formula and the statement "the larger the truss height, the smaller the forces in the top and bottom chords" | An SCI/steelconstruction.info NCCI PDF (SN027a) and a University Politehnica Timisoara course PDF were both fetched but returned unreadable compressed PDF text streams, not a clean quotable statement | **SOURCED** — cited in Appendix A and Appendix H (teachbooks.io, open engineering textbook, MEDIUM-HIGH) |

## Redesign note (case-write -> case-research)

The case-write draft specified an L4×4×3/8 chord for The Low Line (9.72-9.8 lb/ft, roughly double
The Warren Line's L3×3×1/4 chord). Computing the real balance test with that size and a
first-pass 1.5 hr/joint labor assumption produced a **28.9% margin favoring The Warren Line** —
over SPEC §2's ~20% cap. Rather than force a number to fit, the chord size for The Low Line was
retuned down one increment, from L4×4×3/8 to **L3×3×3/8** (7.17 lb/ft) — a real, defensible AISC
angle size still meaningfully heavier than The Warren Line's L3×3×1/4, consistent with the real
"shallower truss needs heavier chords" relationship (Appendix A/H), just not pushed to the most
extreme available size. That single retune brought material cost between the two options to
nearly a wash, leaving the panel-point/labor difference as the dominant driver of the margin, and
landed the real, computed balance test at **14.81%**, winner **The Warren Line (A)** — under
SPEC §2's cap without altering any sourced figure.

## Final balance test

Computed by `cases/creek-span/sensitivity_model.py`, `evaluate(PARAMS)`:

```
base   A=-21.2172  B=-24.9073  winner=A  margin=14.81%
twist  A=-21.2172  B=-23.0210  winner=A  margin=7.84%
```

Next step: run `case-qa` on `creek-span`.
