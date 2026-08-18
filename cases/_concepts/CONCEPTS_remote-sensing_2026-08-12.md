# Concept sheet — Satellite Imagery & Remote Sensing (`remote-sensing`)

Single-concept sheet, target pre-selected from `ROADMAP.md` §B4 item 6 ("Image registration").
Approved by the user's standing instruction to work Queue 1 in order.

**Rescope note.** All 14 of `domains.json`'s `signature_skills` for this domain (translation,
dilation, scale factor, coordinate-plane vocabulary, area, unit conversion) are now already
covered — mostly absorbed by Plaza Pavers/Company Front's transformation work earlier in this run,
with the remaining coordinate-plane/area/conversion terms long since covered by the legacy case
set. Rather than skip the domain, this concept pivots to its other genuinely real content: the
domain's own stated decision archetype #3 — *"Declare the field burned from the index change, or
wait one more revisit and risk the insurance deadline"* — is fundamentally a linear-equation
problem (solve for the day a monitored value crosses a threshold), which the spine still has a
whole zero-coverage **Variables** group for (5 skills: like terms, distributive property, add/
subtract expressions with variables, multi-step equations with the variable on one side and on
both sides), 4 of which this concept honestly closes with a genuinely motivated deliverable each.

### C1 — Field Watch · tier T2

**Protagonist.** A remote-sensing analyst for a crop-insurance claims service, deciding which of
two trend models to trust for a farmer's damage claim before a real filing deadline.

**The real math hook.** Two real satellites (Landsat, Sentinel-2) give free, repeat NDVI
(vegetation index) readings of the same field over time. NDVI genuinely declines under real
vegetation stress/fire damage, and — because burn/stress NDVI thresholds are not a single
universal value (real, sourced finding — SEE Appendix E) — an analyst has to build a linear model
from real field readings and solve algebraically for the day the field's NDVI is expected to cross
a stated threshold, rather than read the answer off a chart.

**The dilemma.** Three real satellite passes exist for the field (day 3, day 8, day 13 — the middle
gap matches Sentinel-2's real 5-day equatorial revisit interval). The decline rate is not constant
between the first and second interval (a genuine, common real pattern — stress often accelerates).
A.) Trust Model A, built from the first two passes (the longer, more established baseline) OR
B.) Trust Model B, built from the two most recent passes (captures the latest, possibly-accelerating
trend). Each model, solved algebraically for the threshold-crossing day, gives a different amount of
safety buffer before the real filing deadline — smaller predicted crossing day = more buffer =
safer bet.

**Would close (4 skills, all new zero-coverage):**

| id | kind | label |
|---|---|---|
| advanced-operations-like-terms | vocab | Like Terms |
| advanced-operations-distributive-property | vocab | Distributive property |
| advanced-operations-how-to-add-and-subtract-an-expression-with-variables | how-to | How to add and subtract an expression with variables |
| advanced-operations-how-to-solve-a-multi-step-equation-with-a-variable-on-one-side | how-to | How to solve a multi-step equation with a variable on one side |

**Deliberately not closed.** `advanced-operations-how-to-solve-a-multi-step-equation-with-a-
variable-on-both-sides` — the natural "where do the two models agree" deliverable turns out to be
mathematically trivial for this data (both models share the Pass-2 anchor point by construction, so
they intersect exactly there — not a genuine both-sides-equation problem). No other clean,
honestly-motivated deliverable was found for it without contriving the scenario; left for a later
case rather than padding this one.

**Data feasibility: HIGH**, matching `domains.json`'s own grade. Real, verified sources: Sentinel-2's
5-day equatorial revisit interval (ESA, HIGH), and the real finding that burn/vegetation-stress NDVI
thresholds are not a single universal value but are regionally/vegetation-type calibrated (USGS Burn
Severity Portal glossary, HIGH) — which is exactly what justifies this case's own threshold as a
disclosed Modeling Assumption rather than a fabricated "sourced" number. The specific field's NDVI
readings are the analyst's own case data (no public per-field dispute database exists, same
convention as every prior case's authored domain data).

**Sensitivity (SPEC §6).** None required — the stakes are a professional filing-deadline judgment
call, not personal loss or hardship.

**Split risk.** None — 4 skills, each with a genuinely distinct, motivated deliverable.

## Recommendation

Write C1 as specified — only concept on this sheet, pre-selected by queue order.
**Next step:** approved by queue order — proceed to `case-write`.
