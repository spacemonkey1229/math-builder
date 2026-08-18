# Concept sheet — Manufacturing, Cutting & Material Nesting (`manufacturing-nesting`)

Single-concept sheet, target pre-selected from `ROADMAP.md` §B4 item 3. Approved by the user's
standing instruction to work Queue 1 in order.

**Rescope note.** The domain's own `uncovered_signature_skills` list (11 skills) was computed
before Plaza Pavers and Company Front ran; both already closed most of the Transformations-group
overlap (transformation, translation, clockwise, counter-clockwise, the translate/rotate-90-cw/
rotate-180/reflect-y-axis how-tos, and geometry-congruent). Re-scanning the spine after those two
promotions, only **6 skills from this domain are still genuinely at n=0**: the Fundamentals-of-
Geometry "Congruent" duplicate, Face, Edge, Pyramid, and the two Visual Perceptibility how-tos
(draw-the-net, name-a-3-D-shape). This concept targets those 6 honestly rather than re-claiming
skills already closed elsewhere.

### C1 — Vent Cap · score ~5.6 (raw 4.8 how-to/term-weighted, no group-completion bonus — Visual
Perceptibility has 11 skills, 8 uncovered before this case, 2 closed here) · tier T2

**Protagonist.** Mara Okafor, CNC nesting engineer at a sheet-metal fab shop (same protagonist
family as Company Front's Mara — a deliberate callback, not required by the pipeline, since these
are otherwise unrelated fictional roles), choosing a flat-pattern nesting layout for a 70-unit
production run before the afternoon cutting run locks in.

**The dilemma.** A.) The 4-Panel Cut — four separate triangular panels per cap, tighter nesting,
four weld seams OR B.) The 3-Panel Fold — one pre-joined folded panel per cap, looser nesting,
three weld seams.

**Primary metric.** Total job cost (material + weld labor) for a 70-cap batch.

**Why it's close.** Tighter nesting (14 vs. 12 caps/sheet) genuinely saves material — real,
disclosed dollars. But labor, priced per seam rather than per sheet, moves in the opposite
direction and by a larger amount for this job size: one fewer seam per cap, 70 times over, beats
one fewer sheet.

**Would close (6 skills, 3 how-to / 3 term):**

| id | kind | label |
|---|---|---|
| geometry-fundamentals-of-geometry-congruent | term | Congruent |
| geometry-face | term | Face |
| geometry-edge | term | Edge |
| geometry-pyramid | term | Pyramid |
| geometry-how-to-draw-the-net-of-a-3-d-shape | how-to | How to draw the net of a 3-D shape |
| geometry-how-to-name-a-3-d-shape | how-to | How to name a 3-D shape |

**Already-covered skills it also exercises.** `geometry-net` (n=1).

**Data feasibility: MEDIUM**, matching `domains.json`'s own grade. Named sources: sheetmetal.me's
gauge chart (real, HIGH), a real dated sheet-steel price listing (M&K Metal, MEDIUM — the source's
own "sample pricing" caveat), a real sheet-metal worker wage figure (PayScale, HIGH) used to derive
a defensible per-seam production labor cost, and the real ESICUP/OR-Library benchmark-dataset
existence (context only, per the domain's own note that no public "real factory parts" library
exists — part geometry and nesting results are case-authored, declared as such).

**Sensitivity (SPEC §6).** None required — stakes are a production deadline and a job-costing
decision, not personal loss or hardship.

**Split risk.** None — 6 skills is a real, if modest, close given how much of this domain's
original scope Plaza Pavers/Company Front already absorbed; every skill traces to a specific
deliverable (see `LEARNING_GOALS.md`).

## Recommendation

Write C1 as specified — only concept on this sheet, pre-selected by queue order.
**Next step:** approved by queue order — proceed to `case-write`.
