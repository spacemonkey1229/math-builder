# Concept sheet — next 10 cases, drawn from the 2026-09-02 coverage worklist

Source: [ROADMAP.md](../../ROADMAP.md)'s "Next 20 cases" table, itself built from
`standards_spine.json`'s live `covered_by[]` arrays (not the stale `gap_queue.json`). This sheet
takes worklist items #1–10 (the 4 true zero-coverage clusters, then the 6 highest-severity thin
clusters) and turns each into one concrete concept — one concept per group, not the 3–5-ranked
format `case-brainstorm` uses for a single group, since the ask here was breadth across 10 gaps at
once. **These are concepts only — nothing here has been through `case-research` or `case-write`.**
No source has been checked yet; feasibility notes below are an honest best-guess, not a
confirmed grade. All ids/labels pulled live from `standards_spine.json`, not from memory.

Every concept targets SPEC §2's ~20% real-margin balance cap, aimed at 5–15% per `case-brainstorm`
doctrine — none of these are physics-forced landslides, so none should need an MCS-46 waiver.
Margin numbers below are *design targets* to write toward, not measured results — real margin is
only known after `case-research` sources the actual data.

---

## 1. The Correction Window (Taylor Series Truncation — Flight-Control Loop)
**Narrative.** Mara Yun's drone has one job tomorrow: thread a slot canyon at a fixed 15-foot
offset from the rock wall while a thermal camera sweeps for a missing hiker, leaning into every
gust just enough to hold that offset without ever touching stone. The flight code that decides
how hard to lean has to finish its own math inside a window measured in microseconds — and
whichever version she flashes tonight is the only version flying tomorrow, since the drone loses
signal the moment it drops below the canyon rim. The county's contract renewal rides on one
clean pass: code that reacts a beat too slow drifts toward the wall, and code too heavy to finish
its own calculation in time never gets the chance to correct at all. (The learner has to notice,
unprompted, *why* the on-board code can't just call a standard trig function here — a real
microcontroller flight loop can't afford a full sine calculation every cycle, so it approximates,
and the whole dilemma is which approximation to fly with. Nothing in the scenario itself should
say the word "Taylor" or "polynomial" before the learner gets there.)
**Group:** Calculus / Series — 🔴 zero-coverage (2 of 5 skills at n=0)
**Career focus:** Embedded-systems / avionics firmware engineer, tuning a drone's attitude-control
loop that has no floating-point trig hardware.
**Problem.** The control loop needs `sin(θ)` thousands of times per second and has a strict
per-cycle time budget. A.) A **3rd-order Taylor polynomial** (`θ − θ³/6`) — fast, cheap, but its
error grows past a few degrees of tilt. B.) A **5th-order Taylor polynomial**
(`θ − θ³/6 + θ⁵/120`) — more accurate through a wider tilt range, but costs more multiply-adds per
cycle, eating into the loop's timing margin. The dilemma is genuinely binary: real embedded math
libraries (e.g. CMSIS-DSP, ARM's own trig approximations) ship exactly this choice as a
compile-time constant.
**Primary metric.** Successful control corrections landed within tolerance, per millisecond of
CPU budget spent on the trig approximation (a ratio: (1 − error rate) ÷ compute cost).
**Would close:** `calculus-taylor-series` (term, n=0), `calculus-how-to-find-the-taylor-series-of-a-function-at-a-point` (how-to, n=0); reinforces `calculus-sequence` (n=2), `calculus-series` (n=1), `calculus-how-to-determine-whether-a-series-converges-or-diverges` (n=1) — full 5/5 group close if the case can naturally motivate a convergence check on the remainder term.
**Rubric.** Must force a genuine derivation of both polynomials from the Taylor series formula
(not just quote them), name the actual trade-off ratio, and set a real trap: a learner who
compares raw approximation error without weighting it against compute cost will wrongly pick the
5th-order every time. Standard 6-probe Tier 2 rubric applies (cold solve, both-sides, trap, twist,
sensitivity, data decay) once written.
**Margin target.** 8–12%. Both orders are genuinely usable in a mid-range tilt envelope; the
tension is real (Apollo-era and modern flight software both document this exact class of
trade-off), so a moderate, defensible margin should fall out of real numbers rather than needing
to be engineered.
**Feasibility (unchecked).** Likely MEDIUM. ARM CMSIS-DSP and STM32 HAL docs publish real cycle
counts for polynomial approximations; a specific published error-vs-order table for `sin`
Taylor truncation should exist in a numerical-methods reference. Confirm before writing.

---

## 2. The Painted Gallon (Spherical vs. Cylindrical Elevated Water Tank)
**Narrative.** Devon Aldrich is the water-system engineer for a drought-strained town of 4,000
whose only elevated tank has been condemned by the state after a corrosion inspection — the town
has been on a boil-water advisory for six weeks while it draws down what's left in the tank.
The bond measure that pays for a replacement goes to a public vote in three weeks, and state law
requires the ballot to name one dollar figure, not a range — so Devon has to settle on a design
before the town's two remaining budget hearings even happen. Neither camp at those hearings is
wrong: the design one contractor is pushing costs less to maintain over the 30-year bond term,
but the other contractor's bid is cheaper to build today, and today's number is the one that
actually has to survive the vote.
**Group:** Geometry / Surface Area And Volume — 🔴 zero-coverage (1 of 10 skills at n=0)
**Career focus:** Municipal water-system engineer, sizing a new elevated storage tank for a
small town.
**Problem.** Both designs hold the same required volume. A.) A **spherical tank** ("golf ball on
a stick") — minimum surface area for its volume, so less steel and less painted surface to
maintain, but a harder, costlier support-leg structure. B.) A **cylindrical standpipe** — cheaper,
simpler foundation and legs, but more surface area per gallon stored, meaning more steel and more
recurring repainting cost. This is a real, standard water-utility design choice (both tank types
are common in the US).
**Primary metric.** Total steel surface area (initial + lifecycle repaint area) per gallon of
storage capacity.
**Would close:** `geometry-how-to-find-the-volume-of-a-sphere` (how-to, n=0); reinforces
`geometry-volume` (n=2), `geometry-how-to-find-the-surface-area-of-a-prism` /
`-cylinder` / `-pyramid` and their volume counterparts (all n≤2) — a strong thickening case for a
group that's 9/10 already-thin.
**Rubric.** Must force a real sphere-volume-and-surface-area derivation and a cylinder
volume-and-surface-area derivation from the *same* target capacity (solve for radius/height given
fixed V), not looked-up dimensions. Trap: a learner who compares raw surface area without holding
volume constant will get a false "sphere always wins" result.
**Margin target.** 6–10%. AWWA (American Water Works Association) design guidance and real
utility case studies should give genuine, close numbers once foundation/support cost is folded
in — the "sphere is more efficient in isolation but costs more to hold up" tension is real.
**Feasibility (unchecked).** MEDIUM-HIGH. AWWA manuals and elevated-tank manufacturer
(Chicago Bridge & Iron / CB&I, Landmark Structures) spec sheets are real, named, and public.

---

## 3. The Marginal Call (Average Cost vs. Marginal Cost — Batch Size)
**Narrative.** Renata Osei runs operations for a nine-person furniture maker that just landed the
biggest order in its history: a hotel chain's holiday bulk buy, 5 weeks to ship. All of it has to
come from FSC-certified black walnut, which narrows her to one supplier — a family-owned mill two
states over that only has one more kiln-drying run left this season before winter shuts the yard
down. A national furniture chain is bidding on the same drying run for a job of their own, and
the mill fills orders in the sequence deposits land, not the order calls come in. Renata's
existing line of credit covers a deposit large enough to lock in enough boards for the shop's
usual run size — comfortably, no phone calls needed. Locking in the *larger* run that would drop
her per-piece cost enough to actually make money on the hotel's price needs a bigger deposit than
her credit line covers today, which means a call to her banker for a temporary increase — a call
that takes days to clear and isn't guaranteed to land before the mill's drying run fills up
without her. She has to decide the size to lock in before she knows whether the bank says yes,
and before she knows whether the competing buyer already beat her to the wood.
**Group:** Calculus / Derivatives — 🔴 zero-coverage (1 of 9 skills at n=0)
**Career focus:** Operations analyst at a small manufacturer, setting production batch size.
**Problem.** Average cost per unit is `C(x)/x` — a quotient of two functions of batch size `x`. A.)
**Run the current smaller batch now** — ties up less capital, ships sooner. B.) **Run a larger
batch to reach the point where marginal cost first exceeds average cost** — found by taking the
derivative of `C(x)/x` with the quotient rule and solving where it crosses zero — lower per-unit
cost, but more working capital tied up in inventory before it sells.
**Primary metric.** Net cost per unit actually sold within the planning quarter (average
unit cost, penalized for the carrying cost of unsold inventory).
**Would close:** `calculus-how-to-use-the-quotient-rule-to-differentiate-a-quotient-of-functions`
(how-to, n=0); reinforces `calculus-how-to-find-the-equation-of-a-tangent-line-at-a-point` (n=2),
chain/product rule skills (both n=1) if the cost function is composite.
**Rubric.** Must force an actual quotient-rule differentiation of a real or realistic cost
function, not a pre-differentiated formula. Trap: a learner who just picks the batch size that
minimizes raw average cost (ignoring carrying cost of unsold units) will pick B every time,
missing the real trade-off.
**Margin target.** 8–15%. This is a textbook-native minimum-average-cost problem; real
manufacturing cost-structure data (fixed setup cost + variable unit cost) should produce a
genuine, moderate margin.
**Feasibility (unchecked).** HIGH. Manufacturing cost-structure data (setup cost, per-unit
material/labor cost) is standard and can be grounded in a named real product category (e.g. a
small-batch consumer-goods manufacturer) with public unit-economics references.

---

## 4. The Deep End (Deep End vs. Shallow-Ramp Pool Redesign)
**Narrative.** Carla Whitfield directs the only public pool in a mid-size city, and it's closing
for a full rebuild — the question is what replaces it. The swim team's parents have packed the
last two council meetings demanding the diving well stay; a disability-rights group has packed
the same meetings demanding a zero-entry ramp instead, backed by the city's own ADA compliance
office. The vote is in two weeks and Carla has to bring the council a real number: not "which
group shouted louder," but how many actual supervised swim-hours each design delivers to the
people who'll use it.
**Groups:** Number Sense / Measurement And Data + Number Sense / Place Value — 🔴 zero-coverage
(2 of 2 skills at n=0: `Depth`, `Digit`)
**Career focus:** Public aquatics facility director, redesigning a community pool.
**Problem.** A.) **Deep-end design** — a single 8-foot depth zone for diving, read directly off a
digital depth gauge that displays whole feet. B.) **Zero-entry ramp design** — a gradually
sloping shallow entry with depth increasing by measured digit-precision increments (e.g. reading
tenths-of-a-foot depth markers), safer for young children and swimmers with mobility limits but
covering more usable pool-deck footprint for the same water volume.
**Primary metric.** Supervised swim-hours accessible to the facility's actual user base (children,
seniors, mobility-limited swimmers) per square foot of pool footprint.
**Would close:** `number-sense-depth` (term, n=0), `number-sense-digit` (term, n=0) — the case
should use both a whole-number depth reading (the diving tank) and a digit-place-value reading
(the ramp's incremental depth markers) so both skills are genuinely forced, not just one bolted
onto a case really about the other.
**Rubric.** Because both target skills are elementary-level terms rather than a `how-to`, the
"rigor" burden this case has to carry is lower than #1–3 above — this should stay a short,
early-track case, and its facilitator notes need to say so explicitly rather than padding it out.
**Margin target.** 5–10%. Real ADA pool-access guidance and drowning-prevention statistics by age
group should ground a genuine, non-inflated safety-vs-capacity trade-off.
**Feasibility (unchecked).** MEDIUM. CDC/pool-safety drowning statistics by age and ADA pool
accessibility design guidance are real and public; specific footprint/cost figures for a
zero-entry ramp vs. a diving well would likely need a named real facility case study or become a
disclosed Modeling Assumption.
**Note:** this is the one concept on this sheet that plausibly deserves a human check before
`case-write` — verify a genuinely defensible *math* dilemma exists here (not just a safety-policy
opinion dressed as one) before committing research time to it.

---

## 5. The Bandstand Angle (Roof Frame — Octagon vs. Irregular Hexagon)
**Narrative.** Tomas Reyes is a structural engineer volunteering his time for a park committee
racing a matching-grant deadline: the donor's $40,000 disappears if a permit application isn't
filed by month's end, and the permit application needs a stamped frame drawing, not a sketch. The
catch is that the surveyor won't have the corner lot's exact boundary lines finished in time —
the committee's own decade-old plat map is the only thing Tomas has to work from tonight. One
framing option is the contractor's "easy" build: identical pre-cut rafters, the fastest possible
turnaround, but it needs more setback from the lot line than the old plat map shows they might
actually have. The other option costs more in custom-cut lumber and cutting time, but was
designed to fit inside the tightest boundary reading the old map allows, whatever the real survey
turns out to say.
**Group:** Geometry / Quadrilaterals And Polygons — 🟠 thin (16 of 22 skills at n≤2, the highest
thin-severity group in the spine)
**Career focus:** Structural/architectural engineer designing a public-park pavilion roof.
**Problem.** A.) A **regular octagon** frame — symmetric, uses the sum-of-interior-angles theorem
cleanly, easy to fabricate identical rafters, but doesn't fit the site's actual property-line
constraints without extra retaining work. B.) An **irregular hexagon** frame — fitted to the real
site boundary, less retaining work needed, but requires computing each interior angle separately
(no shortcut from regularity) and produces non-identical rafter lengths, raising fabrication cost.
**Primary metric.** Total covered square footage delivered per dollar of frame material +
site-prep cost.
**Would close (targeting the group's 6 n=1 skills first, thickening the 10 n=2 skills along the
way):** `geometry-pentagon`, `geometry-heptagon`, `geometry-nonagon`, `geometry-decagon`,
`geometry-dodecagon`, `geometry-n-gon` (all n=1, used as a naming/classification thread — "why not
a pentagon or nonagon frame" as rejected alternatives) plus `geometry-parallelogram`,
`geometry-rhombus`, `geometry-trapezoid`, `geometry-kite` (all n=1, as actual roof-panel shapes)
and `geometry-sum-of-the-interior-angles-of-a-polygon-theorem` (n=2, the load-bearing how-to for
both A and B).
**Rubric.** Must force real use of the interior-angle-sum theorem for an *irregular* polygon
(where it can't be shortcut to `180(n-2)/n` per angle), and must genuinely classify at least one
roof-panel shape as a specific quadrilateral type (not just "quadrilateral"). Trap: a learner who
assumes an irregular hexagon's angles are equal because a regular one's would be.
**Margin target.** 8–14%. Real fabrication-cost differentials for non-identical vs. identical
structural members are a known, moderate real-world premium (custom vs. repeated parts), which
should ground a defensible middle-of-the-cap margin.
**Feasibility (unchecked).** MEDIUM. General park-structure cost guidance exists; exact site
boundary geometry would likely be a constructed (not real-address) scenario, disclosed as such.

---

## 6. The Overlap Send (Email List: Union or Intersection)
**Narrative.** Jess Okafor is the sole growth marketer at a subscription box company, one
$4,000 send away from the end of the quarter's ad budget and an exec team asking why revenue is
9% behind target. Two lists exist in the CRM: everyone who's bought in the last 90 days, and
everyone who's opted into the newsletter — built from different signup forms, at different times,
by different teams, so nobody has ever actually checked how much they overlap. Every name on the
send costs the same flat per-recipient fee regardless of who opens it, and Jess has to file the
send list by end of day so it's out the door in time to count toward this quarter's number at
Friday's board meeting.
**Group:** Discrete Mathematics / Set Theory — 🟠 thin (8 of 8 skills, every one at exactly n=1)
**Career focus:** Growth marketing analyst at a subscription business, planning a campaign send.
**Problem.** Two customer lists exist: recent purchasers and newsletter opt-ins. A.) Mail the
**union** of both lists — maximum reach, but a lower expected conversion rate per recipient since
many haven't shown recent purchase intent. B.) Mail only the **intersection** — recipients on
both lists — smaller reach, but a real, measurable lift in conversion rate since these customers
show two independent signals of interest.
**Primary metric.** Expected net revenue per campaign send (reach × conversion rate × average
order value, minus per-send cost).
**Would close:** all 8 group skills — `discrete-mathematics-set`, `-subset`, `-union`,
`-intersection`, `-empty-set`, `-venn-diagram`, `-how-to-find-the-union-and-intersection-of-two-sets`,
`-how-to-represent-a-set-relationship-using-a-venn-diagram` — a genuine full-group close, the
strongest single-case value on this sheet (score 16 → 0 if this lands clean).
**Rubric.** Must require the learner to actually draw/read a Venn diagram to reason about
overlap size, not just look up a stated intersection count, and must force real set notation.
Trap: naively assuming reach and conversion rate trade off 1:1, missing that the *products*
(reach × rate) are what actually decide the winner — a learner who eyeballs "union has 3x the
reach" without computing expected revenue will pick wrong if the intersection's conversion lift
is large enough.
**Margin target.** 8–15%. Real email-marketing benchmark data (segmented vs. broad-send
conversion-rate differentials) is publicly documented (Klaviyo, Mailchimp benchmark reports) and
should ground a genuine, moderate margin without needing invented numbers.
**Feasibility (unchecked).** HIGH. Public email-marketing benchmark reports exist by name
(Klaviyo, Mailchimp, HubSpot) with real segmented-vs-broad conversion rate data.

---

## 7. The Custom Die (Shipping Box: Prism vs. Wedge Packaging)
**Narrative.** Marcus Feld is the packaging engineer at a bakery that went from 40 local orders a
week to 12,000 nationwide after a single video hit a million views — and the fulfillment center
they contracted charges by the cubic inch shipped, not by the item, which means the box itself is
now the bakery's second-biggest cost line after ingredients. Tooling for a new box shape has a
six-week lead time; the next production run ships in eight. Whatever box Marcus commits to
tonight has to be cut, folded, and boxing product on the line before that six weeks is up, with
no second attempt if the numbers don't work out the way he expects.
**Group:** Geometry / Visual Perceptibility — 🟠 thin (10 of 11 skills at n≤2)
**Career focus:** Packaging design engineer at a specialty-foods company.
**Problem.** A new product (e.g. a wedge-shaped baked good, or a cone-topped product) needs a
shipping box. A.) A **rectangular prism** box — simple net, cheap tooling, but wastes interior
volume around the product's actual (non-rectangular) shape. B.) A **triangular-prism / wedge**
box fitted to the product's real shape — less wasted volume and lower per-unit material once the
custom die is amortized, but a more complex net and higher tooling cost.
**Primary metric.** Cardboard used (square inches of net) per cubic inch of product actually
shipped, amortized against tooling cost over expected order volume.
**Would close:** `geometry-face`, `geometry-edge`, `geometry-pyramid`, `geometry-cone`,
`geometry-cylinder`, `geometry-sphere` (all n=1), `geometry-net`, `geometry-prism`,
`geometry-how-to-name-a-3-d-shape` (n=2) and `geometry-how-to-draw-the-net-of-a-3-d-shape`
(n=1, the case's load-bearing how-to) — a near-full group close (10 of 11).
**Rubric.** Must force the learner to actually construct and measure a net (not just cite a
surface-area formula), and correctly name/classify multiple 3-D shape candidates before narrowing
to the two real options. Trap: computing material cost from volume instead of net surface area —
the two are not proportional once packaging shape changes.
**Margin target.** 6–12%. Real die-cutting tooling cost vs. material-waste-per-unit trade-offs
are well documented in packaging-industry sources at a moderate, genuine margin once order volume
is fixed.
**Feasibility (unchecked).** MEDIUM. Packaging-industry material cost benchmarks (per-square-inch
corrugate cost) are publicly available; a specific real product's dimensions would likely be a
constructed, disclosed scenario.

---

## 8. The Sightline Vote (Skew vs. Perpendicular Intersection Redesign)
**Narrative.** Dana Whitcombe is the city's traffic engineer, called in after the second
T-boned-car pileup in a month at the same crooked intersection — the local paper has run both
crashes on its front page. The city council votes on funding in ten days, and only two fixes are
on the table: the "big dig," which eats into two corner lots the city would have to buy from
their owners first, or the cheaper patch the public-works crew could start on next week without
buying anything at all. Both contractors insist their option clears the state's minimum
sightline-safety standard; neither number has actually been checked against that standard yet,
and the council meets before there's time to build a mockup of either one.
**Group:** Geometry / Fundamentals Of Geometry — 🟠 thin (18 of 24 skills at n=2, all n=2 — not
n=1, so lower urgency than its raw score suggests, but still the largest total-skill group with
any gap)
**Career focus:** Civil/transportation engineer redesigning a dangerous street intersection.
**Problem.** Two streets currently meet at a skewed (non-90°) angle, a known sightline-safety
issue. A.) **Realign to perpendicular** — maximizes driver sightline angle (uses vertical,
supplementary, and complementary angle relationships to model sightline geometry), the safer
option, but requires reshaping more curb and losing usable corner-lot land. B.) **Add a
transversal-offset lane** at the existing skew angle — keeps more corner land usable and is
cheaper to build, but leaves a narrower (though code-compliant) sightline angle.
**Primary metric.** Sightline safety score (a function of the intersection angle, following real
traffic-engineering sightline-distance formulas) per dollar of construction cost.
**Would close:** all 16 remaining n=2 skills in the group — `geometry-point`, `-line-segment`,
`-ray`, `-vertex`, `-degree`, `-acute-angle`, `-obtuse-angle`, `-right-angle`, `-parallel-lines`,
`-perpendicular-lines`, `-transversal-line`, `-fundamentals-of-geometry-congruent`,
`-supplementary-angles`, `-complementary-angles`, `-vertical-angles`, `-adjacent-angles`, plus
both how-tos (`-how-to-find-angle-measures-of-intersecting-lines`,
`-how-to-find-angle-measures-given-parallel-lines-a-transversal-line-and-at-least-one-angle-measure`)
— every skill in the group is n=2, so this case cannot push any of them below n=1 on its own, but
it is the single highest-leverage way to touch all 18 remaining gaps in one write.
**Rubric.** Must force real transversal/parallel-line angle-measure calculations for both
redesign options, not just angle vocabulary. Trap: assuming "more perpendicular is always safer"
without weighting it against the real cost and land-use loss — sightline safety has diminishing
returns past a certain angle, which the data should show.
**Margin target.** 8–15%. Real traffic-engineering sightline-distance standards (AASHTO Green
Book) and real intersection-redesign cost data should ground a genuine, moderate margin.
**Feasibility (unchecked).** HIGH. AASHTO's "Green Book" sightline-distance formulas are a real,
named, citable standard; municipal intersection-redesign project costs are frequently public
(city capital-improvement budget documents).

---

## 9. The Mirror Cut (Sheet-Metal Nesting: Mirrored vs. Simple Layout)
**Narrative.** Sam Delgado runs production at a six-person sheet-metal shop bidding against two
bigger competitors for the largest contract in company history — 40,000 identical brackets a
year, for three years — due tomorrow morning at 9. Whichever layout the quoted price is built on
is locked in for the life of the contract: underquote the steel and the shop eats the difference
on every part, all three years; overquote it and one of the bigger shops wins the bid on price
alone. One layout the programmer sketched gets more brackets out of each sheet by fitting every
other part upside-down against its neighbor; the other just repeats the part straight down the
sheet, plainer to program and faster on the machine, but leaves more scrap at the edges of every
single sheet.
**Group:** Geometry / Transformations — 🟠 thin (14 of 20 skills, all at n=2)
**Career focus:** Production engineer at a sheet-metal fabrication shop.
**Problem.** A batch of identical parts needs to be laser-cut from steel sheets. A.) A
**mirrored/rotated nesting layout** — parts are reflected and rotated to interlock tightly,
maximizing parts per sheet, but the cutting path is longer and more complex, costing more machine
time per sheet. B.) A **simple repeated (translation-only) layout** — parts are only translated,
never reflected or rotated, faster to program and cut, but wastes more sheet material per batch.
**Primary metric.** Net cost per finished part (material cost + machine-time cost combined).
**Would close:** `geometry-translation`, `geometry-dilation`, `geometry-scale-factor`,
`geometry-symmetry`, `geometry-line-of-symmetry` (n=2) plus the how-tos
`-how-to-translate-a-figure-on-the-coordinate-plane`, `-how-to-reflect-a-figure-across-the-x-axis`,
`-how-to-reflect-a-figure-across-the-y-axis`,
`-how-to-rotate-a-figure-on-the-coordinate-plane-90-degrees-counterclockwise`,
`-how-to-rotate-a-figure-on-the-coordinate-plane-180-degrees`,
`-how-to-dilate-a-figure-on-the-coordinate-plane-given-a-scale-factor`,
`-how-to-find-the-scale-factor-of-a-dilation` (all n=2) — a near-complete pass through the group
(11 of the 14 gap skills), skipping only `congruent`/`similar` unless the case is written to also
compare the nested parts' congruence explicitly.
**Rubric.** Must force actual coordinate-plane transformations (real reflect/rotate/translate
operations on part outlines, with coordinates), not just a verbal description of "mirroring."
Trap: assuming more transformations always means more waste saved — past a certain part
complexity, added cutting-path length can erase the material savings, which real numbers should
show.
**Margin target.** 6–12%. Real sheet-metal nesting-software case studies (Nestfab, SigmaNEST
publish material-yield comparisons) should ground a genuine, moderate margin.
**Feasibility (unchecked).** MEDIUM-HIGH. Nesting-software vendors publish real material-yield
percentage comparisons; machine cutting-time-per-inch figures are standard shop-floor data.

---

## 10. The Special Order (Lumber Stock Width — Simplify or Convert)
**Narrative.** Grace Liu manages production at a cabinet shop with a fixed-bid kitchen job and an
install date the client has already scheduled movers around. Standard nominal lumber is on the
shelf today but leaves real, fraction-denominated milling waste on every board; the exact-width
stock she actually needs has to be special-ordered, and the supplier's minimum-order quantity
only pencils out if the batch is big enough — a bet she has to place today, working straight off
the mill's own order form, which lists every width the way a tape measure actually reads them,
not rounded to the nearest decimal.
**Group:** Fractions / Understanding Fractions — 🟠 thin (8 of 11 skills at n≤2)
**Career focus:** Cabinet shop production manager, ordering dimensional lumber for a batch of
cabinet doors.
**Problem.** A cut list calls for stock in awkward fractional widths (e.g. `7/4`-inch actual
width after milling). A.) **Order standard nominal stock and mill down** — always available,
predictable lead time, but real milling loss on every board must be tracked in fractional/mixed-
number terms to know true yield. B.) **Special-order pre-milled stock at the exact fractional
width** — less waste per board, but a longer lead time and a minimum-order-quantity requirement
that only pays off past a certain batch size (found by comparing the two options' cost-per-door
as mixed-number/fraction arithmetic, not decimals, since the shop's own cut sheets and supplier
invoices are fraction-denominated).
**Primary metric.** True material cost per finished cabinet door, accounting for milling waste.
**Would close:** `fractions-equivalent-fractions`, `fractions-simplify`,
`fractions-improper-fraction`, `fractions-mixed-number` (terms) and
`fractions-how-to-find-equivalent-fractions`, `fractions-how-to-simplify-a-fraction`,
`fractions-how-to-convert-an-improper-fraction-to-a-mixed-number`,
`fractions-how-to-convert-a-mixed-number-to-an-improper-fraction` (how-tos) — a full 8/8-skill
close of every currently-thin skill in the group.
**Rubric.** Must force genuine improper-fraction ↔ mixed-number conversion and simplification on
real (or realistically fraction-denominated) lumber measurements — a case that quietly converts
everything to decimals defeats the point and should be rejected at `case-write`. Trap: comparing
unsimplified fractions directly (e.g. treating `6/8` and `3/4` as different widths) and
concluding a false difference between the two sourcing options.
**Margin target.** 5–10%. Real hardwood lumber milling-waste percentages and special-order
minimum-quantity pricing are documented in woodworking-industry sources at a genuine, moderate
margin.
**Feasibility (unchecked).** MEDIUM. Hardwood lumber pricing and standard milling-waste
percentages are publicly documented (woodworking trade publications); a specific supplier's
special-order terms would likely be a constructed, disclosed scenario.

---

## Handoff

None of these 10 have been through `case-research` — every "Feasibility" grade above is an
unchecked, honest guess, not a confirmed source check. Recommended write order: **#6 (Set
Theory) and #10 (Fractions)** first — highest confidence, full-group closes, no unusual sourcing
risk. **#2 and #3** next — the other two zero-coverage clusters with HIGH/MEDIUM-HIGH feasibility.
**#1** (Taylor Series) needs an embedded-systems source check before committing. **#4** (pool
depth/digit) needs the human sanity-check noted above before research time is spent on it. **#5,
#7, #8, #9** are all workable but each leans on at least one likely-constructed (not
real-sourced) figure — normal for this corpus, just flag it in the eventual `case.json`
Modeling Assumptions rather than presenting it as sourced.
