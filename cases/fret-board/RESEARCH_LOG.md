# Fret Board — Research Log

Stage 3 (`case-research`) log. One entry per `{{NEEDS_SOURCE}}` placeholder from the `case-write`
draft: what was searched, what was found or rejected, and what it became.

## Search strategy summary

Three real search framings were run:
1. `Stewart-MacDonald fret scale calculator rule of 18 divisor 17.817 formula`
2. `twelfth root of two equal temperament fret spacing formula luthier`
3. `acceptable guitar intonation tolerance cents professional luthier standard`
4. `standard guitar scale length 25.5 inches Fender 24.75 Gibson number of frets 22`
5. `just noticeable difference pitch cents psychoacoustics study 5 cents musicians`

Four pages were then fetched directly (not just search snippets) to pull exact formulas/values:
StewMac's "Fret Scale Rule Instructions", StewMac's "Guitar Scale Length Explained", Liutaio
Mottola's "Calculating Fret Positions", and Liutaio Mottola's "Was the Rule of 18 Good Enough?".

## Placeholder-by-placeholder

**Twelfth-root-of-two constant (Appendix A, and repeated in Appendix B).**
Found via Liutaio Mottola, "Calculating Fret Positions" — states the formula
`d = s − (s / (2^(n/12)))` and the value `1.0594630943593` directly. This is a fixed mathematical
definition (the constant that raised to the 12th power equals 2), so it needs no "as of" date and
cannot go stale. Cited as **S1**, confidence HIGH. → **SOURCED**.

**Rule-of-Eighteen divisor (Appendix C).**
This was the placeholder that required the most care. The first search turned up StewMac's own
"factor," 17.817154 — but reading further (Liutaio Mottola's "Was the Rule of 18 Good Enough?")
showed that **17.817 is the modern, refined constant**, not the original "rule of 18." The
traditional rule that gives the case its name uses the literal whole number **18** as the divisor;
17.817 is a later correction some shops substitute in its place. Building Appendix C's table with
17.817 instead of 18 would have produced a fret-12 deviation of essentially zero (verified: at 4
decimal places the two constants round to the same 12th-fret position), which would have quietly
erased the entire dilemma the case is built on. Re-read the source before committing to a number —
this is exactly the kind of mistake a "plausible-looking" search-engine summary can cause. Divisor
= 18, cited as **S3** (Liutaio Mottola, "Was the Rule of 18 Good Enough?"), confidence HIGH.
17.817154 is still cited as **S2** (StewMac) but only as *background context* inside Appendix C's
note, explaining the modern refinement — it is not the number used in the table. → **SOURCED**.

**Fret-position tables, both methods, frets 1–12 (Appendices B and C).**
Not independently sourced — these are **derived** from S1 (formula) + S3 (formula) + S4 (scale
length), computed and shown with the governing formula in-document so a reader can verify the
arithmetic. Marked `derived: true` in spirit (see `case.json` `needs_source[].resolved_as`).
→ **SOURCED** (derived).

**Scale length for this build (Appendix B/F).**
Found via StewMac, "Guitar Scale Length Explained" — names 25.5" as the Fender-style standard
(also 24.75" Gibson-style and 25" PRS-style, recorded for completeness). Chose the Fender-style
25.5" as the build spec — a real, named, sourced standard, not an invented number. Cited as **S4**,
confidence HIGH. → **SOURCED**.

**Cents-of-deviation figure at fret 12 (Appendix D).**
Not independently sourced — **derived** from the Appendix B/C 12th-fret lengths using the standard
cents formula (`1200/log10(2) ≈ 3986.3`, the universally standard 1200-cents-per-octave
definition, itself a mathematical convention needing no citation). Computed value ≈ −12.5 cents
(Rule of Eighteen flat of true pitch). This matches the *qualitative* finding in S3 that
rule-of-18 frets "trend flat" — no external source states the exact cents figure for a 25.5"
scale at 4-decimal precision, so this is honestly derived, not sourced. → **SOURCED** (derived).

**Acceptable intonation tolerance, in cents (Appendix D).**
Searched twice (forum-thread search, then a psychoacoustics/JND search) plus attempted to find a
single published trade-body standard. **NOT FOUND** as a hard, citable, single-number standard —
consistent with the concept sheet's own MEDIUM-data-feasibility flag on exactly this figure.
What exists instead is a converging but informal range: guitar-technician/luthier forum consensus
of roughly 2–6 cents, and general psychoacoustic pitch-discrimination literature placing the JND
for most listeners in a comparable few-cents range (one specific study cited 40 cents for a
different, coarser experimental paradigm — rejected as not representative of trained-ear guitar
intonation work and not used). **Exit chosen: stated Modeling Assumption (MA1)**, 5 cents, with
the range that informed it recorded in `case.json.modeling_assumptions`. Per `case-write`
SKILL.md's rule, the case itself does not print the resulting verdict (whether B's deviation
crosses this line) — that stays in `FACILITATOR.md`/`case.json.balance`, not in the student-facing
appendix.

**GCF string-length-ratio table, frets 1–5 (Appendix E).**
Not independently sourced — **derived** directly from the Appendix B Precision-Method lengths
(themselves derived from S1+S4), expressed in ten-thousandths of an inch so both terms of each
ratio are whole numbers, then reduced by GCF. Finding: none of frets 1–5 reduce to a simple
whole-number ratio; fret 12 (shown for contrast) is the one point that does, exactly 2:1, by
construction of the octave. This is a real, checkable mathematical fact about equal temperament,
not an invented result — every equal-tempered fret except the octave is an irrational multiple of
the open-string length, so a clean small-integer ratio anywhere else would be a coincidence of
rounding, not a property of the tuning system. → **SOURCED** (derived).

**Named scale-length standard for this build (Appendix F).**
Same source as the scale-length figure above — **S4**. → **SOURCED**.

**Number of frets on this neck (Appendix F).**
Searched for a "standard" fret count; found only a *range* (StewMac: 21–24 typical for modern
electric guitars), not a single figure — this build's exact count is inherently a shop/client
choice, not a discoverable fact about the world. **Exit chosen: stated Modeling Assumption (MA2)**,
22 frets, informed by the sourced range. → **ASSUMPTION**.

**Client turnaround, in days (Appendix F).**
This is a fictional-scenario detail about Yuki's specific job, not a real-world fact with a
source to find — no search was run for it. **Exit chosen: stated Modeling Assumption (MA3)**,
5 days, consistent with the Overview's "before the week is out." → **ASSUMPTION**.

## Rejected sources (kept for the next person, so this search isn't re-run)

- A Quora answer and several SEO-farm "fret calculator" tool pages (whiz.tools, calculator200.com,
  onlinecalculator1.com) repeat the same formula correctly but with no attribution and no
  publication date — LOW confidence, not used, even though the numbers agreed with the two HIGH
  sources actually cited.
- A claim (surfaced in one search-engine summary, not the primary source itself) attributing the
  "rule of 18" to Vincenzo Galilei's father in the 16th century. Liutaio Mottola's own article
  explicitly says it does **not** know of documentation for the rule's first use — the summary's
  attribution claim does not survive checking the primary source, so it was dropped rather than
  repeated.
- A JASA (Journal of the Acoustical Society of America) paper and a Stanford CCRMA PDF on pitch
  JND were surfaced but not fetched in full — one summary result cited a 40-cent JND figure from a
  different experimental context (non-musician forced-choice staircase procedure), which is not
  representative of a trained guitar tech's discrimination and was not used in MA1's basis.

## Outcome

- **43/43 placeholders resolved.** 0 remain `OPEN`.
- **40 resolved via citation or direct derivation from a citation** (S1–S4).
- **3 resolved as explicit stated Modeling Assumptions** (MA1 tolerance, MA2 fret count, MA3
  turnaround) — none silently invented; all three are visible in `case.md`'s Modeling Assumptions
  block with basis and sensitivity stated.
- **1 open judgment call flagged, not resolved here:** the derived ~12.5-cent Rule-of-Eighteen
  deviation is roughly 2.5× the stated MA1 tolerance — a real SPEC §2 balance question for
  `case-qa`/a human to weigh before this case proceeds, recorded in `case.json.balance.margin_note`
  rather than silently passed through.

Next step: run `case-qa` on `fret-board` (per this task's instructions, that step and everything
after it is intentionally **not** run in this session).

## Addendum, 2026-08-27 — primary-metric retune research

The 2026-08-26 `case-readiness` run found the original primary metric (cents of pitch deviation
at fret 12) structurally unbalanceable (100% margin) — see `QA_REPORT.md` and
`case.json.balance.margin_note`. The case owner decided to retune rather than accept the
imbalance. One additional search was run to ground the retune honestly rather than inventing a
number outright:

**Search: `how long does a guitar refret job take hours StewMac shop labor`.** Fetched
StewMac's "Guitar repair money talk: estimate hours, not dollars" directly. Found a real,
specific line item from a real shop's own published job estimate: "Refret with #0147 wire: -
.6hrs" (0.6 hours) for the fret-installation portion of one example repair job. No general
industry standard for total fretting/refret time was found (searched, not present) — this is one
professional's one real line item, not a trade standard, so it is cited as **S5**, confidence
MEDIUM, and used only as *directional, order-of-magnitude context* for the new Modeling Assumption
MA6 (45-minute shared cutting/installing/dressing baseline), not restated as the value itself —
the source's job is a repair refret (installing wire into existing slots), not this case's
fresh-neck slot-cutting job, so the values are related but not identical tasks.

No source exists, and none was expected to exist, for the two new per-fret calculation-time
figures (MA4: 20 sec, Precision Method; MA5: 14 sec, Rule of Eighteen) — these are reasoned
scenario estimates based on the real, countable difference in arithmetic steps between the two
governing formulas already in Appendices B/C (a fractional-exponent evaluation vs. a simple
division-and-subtraction), consistent with S3's own explicit historical claim that the Rule of
Eighteen's divider-based method was built specifically to avoid hand computation "in the days
before calculators and computers." Declared as Modeling Assumptions, not sourced facts, per
`case-write` SKILL.md's placeholder discipline.

**Outcome:** 1 new source added (S5, MEDIUM confidence, directional only), 3 new Modeling
Assumptions added (MA4, MA5, MA6), 0 numbers fabricated as fact. `margin_pct` recomputed at 4.2%
on the retuned primary metric (total shop time). Full derivation in `case.json.balance.margin_note`
and `case.json.derived.shop_time_primary_metric`.
