# RESEARCH_LOG.md — The Clampband Margin

Run: `case-research`, 2026-08-30. 34 `{{NEEDS_SOURCE}}` placeholders enumerated in `case.md`.

---

## The headline finding: a mis-attribution had to be corrected

The task brief for this run stated that NASA GD-ED-2214's numeric margins — "a preload gapping
margin of 1.25, a release-element margin >2.00 — were found in prior research this session" and
asked me to "verify and cite properly."

I fetched and read the actual GD-ED-2214 PDF in full (all 8 pages, via
`https://extapps.ksc.nasa.gov/Reliability/Documents/Preferred_Practices/2214.pdf`, mirrored at
Wikimedia Commons). **The document does not contain the numbers 1.25 or 2.00 anywhere.** Its only
stated preload-design criterion is qualitative: *"The criterion for designing strap preloads is
that no gapping occurs when the maximum expected load is applied."* No numeric factor, ratio, or
percentage margin appears in the text.

I then searched specifically for where "gapping margin 1.25" and "release margin >2.00" actually
originate. Found: **C. Lazansky (Sierra Nevada Corporation), "Refinement of a Low-Shock Separation
System,"** a paper presented at the European Space Mechanisms and Tribology Symposium (hosted at
`esmats.eu/amspapers/pastpapers/pdfs/2012/lazansky.pdf`). Page 11 of that paper states verbatim:
*"A reasonable choice is to design and test to 1.25x worst case load predictions. Maintaining high
margins on the release element (>2.00) has been recommended... A margin on gapping of 1.25 is
normally applied to this result."* The paper's own reference list attributes the release-element
figure further to a 1995 Aerospace Mechanisms Symposium paper on Clementine (Purdy & Hurley, "The
Clementine Mechanisms") — not independently re-verified here (tier-3 secondary attribution, not
load-bearing enough on its own to chase further).

**Resolution:** both numbers are real and genuinely used in industry practice — they are just
attributed to the wrong document in the original brief. GD-ED-2214 is cited (S1) for its own real,
qualitative content. The Lazansky/SNC paper is cited (S2) for the numeric 1.25/2.00 values. Both
appear correctly attributed in `case.md` Appendix B and Appendix F, with an explicit correction
note in both places and in `case.json`'s `needs_source[]` entries. This is exactly the SPEC §5
scenario the skill exists to catch — a plausible-looking figure attached to the wrong source is as
dangerous as an invented one, because it reads as verified when it isn't.

---

## Placeholder-by-placeholder log

**Appendix A (3 placeholders) — scenario constraints, not external research.**
Filled directly from the Overview's own stated "two weeks" (→ 14 days) and Background's "no
on-orbit rework" (→ No revisit; exactly one methodology). No search needed; these are narrative
consistency checks, not sourced claims.

**Appendix B — guideline document / gapping margin / release-element margin / worked definition.**
- Searched: `GD-ED-2214 "Marman Clamp System Design Guidelines" NASA preferred reliability
  practices`. Found the real document at two mirrors (NASA KSC extapps, Wikimedia Commons).
  `WebFetch` on the NASA KSC URL failed with a TLS certificate error; downloaded directly via
  `curl --insecure` instead and read the PDF locally — confirmed genuine NASA/GSFC document,
  8 pages, Preferred Reliability Practices series.
- Searched: `Marman clamp "gapping margin" 1.25 OR "release margin" separation system NASA` and
  `"gapping margin" clampband preload margin of safety spacecraft separation joint`. Found the
  Lazansky/SNC ESMATS paper (downloaded via curl, extracted text with PyPDF2 since it was a
  15-page scanned/text-layer PDF too large for one Read call).
- **Worked definition connecting tolerance-stack to margin: NOT FOUND in either source.** Neither
  GD-ED-2214 nor the Lazansky paper converts a dimensional tolerance-stack value into these
  dimensionless load-safety factors — they're answering a different question (how much load
  margin to design the band/release device to) than the one this case's D3/D4 need (how does a
  tolerance stack, in inches, compare to a margin threshold). **Exit taken: stated Modeling
  Assumption (MA4)** — a disclosed 0.070 in nominal per-joint gapping allowance, margin =
  allowance ÷ predicted tolerance. Flagged in FACILITATOR.md as the single most load-bearing
  assumption in the case, since it determines exactly where the Worst-Case/RSS crossover in D3
  lands.

**Appendix C — ISO 2768 tolerance classes and per-interface real values.**
- Searched: `ISO 2768-1 tolerance classes fine medium coarse very coarse table mm`. ISO 2768-1
  itself is a paywalled standard (no free official hosting) — expected per SKILL.md's worked
  example (metals pricing/standards are often paywalled). Tier-2 exit: found the full numeric
  table reproduced consistently across multiple independent industry pages (jlccnc.com,
  haizol.com, rivcut.com, rpproto.com). `WebFetch` fetched the RpProto-hosted PDF successfully
  after the RivCut PDF's initial fetch attempt returned an unreadable/encoded response; read the
  downloaded PDF directly and extracted the full Table 1 (Linear Dimensions) for all four classes
  across all nominal-length ranges. Cross-validated: all sources agree exactly, so graded HIGH
  despite being a secondary republication of a paywalled primary standard.
- Searched: `Protolabs CNC machining tolerances fine tuning tolerances for CNC machined parts`,
  then `WebFetch` directly on
  `https://www.protolabs.com/resources/design-tips/fine-tuning-tolerances-for-cnc-machined-parts/`.
  Primary source, confirmed ±0.005 in (0.13 mm) standard tolerance, stated as consistent with ISO
  2768-1-1989-f (metals) / -m (plastics). No date visible on page.
- `WebFetch` directly on
  `https://www.protolabs.com/resources/blog/injection-molding-tolerances/`. Primary source, dated
  2023-02-07. Confirmed ±0.003 in (0.076 mm) mold-tool tolerance and ±0.002 in/in (minimum)
  resin/shrink tolerance — two distinct figures, both real, both reported with their distinct
  units in Appendix C's reference table.
- **Nominal diameter (flange OD / ring ID) and nominal bolt+shim stack height: genuinely
  unsourceable**, exactly as the task brief anticipated — no real program is named in this case.
  **Exit taken: stated Modeling Assumption (MA3)** — 15.000 in nominal diameter, 0.500 in nominal
  stack height, chosen as representative of a small-satellite Marman clampband and used only to
  select which ISO 2768-1 dimension-range row governs each interface.
- Assigned governing standard per interface (a case-author scenario choice, consistent with the
  concept sheet's framing that "assigning each named supplier's part a standard tolerance class"
  is the point of the exercise): Supplier B (flange OD) and Supplier C (bolt+shim stack) → ISO
  2768-1 class f (fine); Supplier A (ring ID) → Protolabs' published CNC tolerance. This produced
  three genuinely different, genuinely cited tolerances (±0.0079 in, ±0.0050 in, ±0.0039 in)
  rather than three copies of one number.

**Appendix D — stack-up table across n = 3, 6, 7, 10.**
Pure arithmetic from Appendix C's real values and the two real formulas in Appendix D (no search
needed): $T_{WC}(3)=0.0168$ in, $T_{RSS}(3)=0.0101$ in exactly, derived by direct sum and
root-sum-square. Average per-interface tolerance for extension rows: $0.0168/3 = 0.0056$ in
exactly (MA2). Future supplier counts (MA1) were not picked arbitrarily — I first computed where,
under MA4's margin bridge, the Worst-Case Stack's margin against the 2.00 release-element
threshold crosses below 1: solving $0.070/(n \times 0.0056) = 2.00$ gives $n = 6.25$, so n=6 (still
passes) and n=7 (first fails) bracket the real crossover; solving the same equation against the
1.25 gapping threshold gives $n = 10$ exactly, landing Worst-Case right at that floor. Choosing
n = 6, 7, 10 makes both crossovers visible in a 4-row table instead of being invented arbitrary
round numbers.

**Appendix E, MA1/MA2 (values and basis) — filled directly**, since these ask the case to state
its own scenario extension, not to find an external citation (see above).

**Appendix F — sources table.** Five sources (S1–S5) assembled from the above, each with claim,
value, org, title, URL, access date, and confidence grade. See `case.json` `sources[]` for the
full structured records.

---

## Verification pass

```
placeholders remaining: 0
citation markers with no source row: set()
source rows never cited in text: set()
```
Confirmed by re-scanning `case.md` for `{{NEEDS_SOURCE` (zero hits) and cross-checking every
`[S1]`–`[S5]` marker against Appendix F's table.

## Confidence summary

| Source | Confidence | Why |
|---|---|---|
| S1 (GD-ED-2214) | HIGH | Primary NASA/GSFC document, read in full |
| S2 (Lazansky/SNC, ESMATS 2012) | MEDIUM-HIGH | Named practitioner's peer-presented conference paper reporting real industry practice; not itself a NASA-issued numeric standard, and its release-element figure traces to a further secondary source not independently re-verified |
| S3 (ISO 2768-1 table) | HIGH | Paywalled primary standard; cross-validated across 4 independent industry republications, all identical |
| S4 (Protolabs CNC) | HIGH | Primary manufacturer source, fetched directly |
| S5 (Protolabs injection molding) | HIGH | Primary manufacturer source, fetched directly, dated |

**NOT FOUND count: 1** — the worked definition connecting a dimensional tolerance-stack value to
GD-ED-2214/Lazansky's dimensionless load-safety-margin factors. Exit taken: stated Modeling
Assumption (MA4), disclosed as the case's single most load-bearing assumption.

**Computed (facilitator-only) results:** `margin_pct` = 39.9 (percent difference between RSS's and
Worst-Case's predicted tolerance at n=3). Winning option under the case's own scaling frame: **B
(RSS Stack)** — Worst-Case fails the release-element margin at n=7 and sits at the gapping-margin
floor at n=10; RSS clears both thresholds at every modeled n. Full numbers in FACILITATOR.md and
`case.json`'s `balance` object; none of this appears in `case.md` per SPEC.

Next step: `case-readiness` on `the-clampband-margin`.

---

# RETUNE PASS — 2026-08-30

## Why this pass exists

`the-clampband-margin` failed SPEC.md §2's balance test: the Worst-Case Stack and the RSS Stack
differed by 39.9% at this build's real n=3, well over the project's ~20% ceiling. The task was to
re-derive a genuinely realistic, defensible, close dilemma through further real research — not to
bump the number to make it pass.

## What was investigated

**1. Is n=3 an undercount of a real Marman clampband's toleranced interfaces?**
Re-read GD-ED-2214 in full via a local `pdftotext` extraction (the earlier WebFetch-only attempts on
both GD-ED-2214 and the Lazansky PDF failed — both are image/JPX-encoded PDFs that WebFetch's model
cannot read directly; downloading via `curl --insecure` and running `pdftotext -layout` locally
worked, same technique the original research pass used). GD-ED-2214's Figure 1 nomenclature and body
text describe a real Marman joint as: tension strap, V-segments, two ring flanges (inner/outer),
tensioning bolts, bathtub fittings, and (per Section 3) 2–4 redundant release devices depending on
band diameter (<0.5m: 2 devices; 1.5m: 3; 2m: 4). This is a real, useful, previously-uncited datum
(band-diameter-to-release-device-count scaling), but it does NOT fix the balance problem — see
"Why more interfaces doesn't help" below. It was not used to change n; it's flagged as an available
real anchor if a future pass wants to reframe "growing supplier count" as "growing band diameter."

**Why more interfaces doesn't help:** the percent difference between Worst-Case ($\sum t_i$) and RSS
($\sqrt{\sum t_i^2}$) for tolerances of comparable magnitude is $1 - 1/\sqrt{n}$ for equal
tolerances — a value that *increases* with $n$, from 0% at n=1 toward 100% as $n\to\infty$. At n=3
it's already ~42% for equal tolerances (close to the case's actual 39.9% with its three real,
non-identical tolerances). Checked n=2 combinations of this build's three real tolerances: all land
in the 25–29% range, still over the ceiling. Solved algebraically for what tolerance ratio two real
interfaces would need for the margin to hit 20%: about 1:3.2 — none of Appendix C's real, cited
ISO 2768-f / Protolabs-CNC tolerances are that skewed (and forcing a skewed pairing, e.g. by
assigning one interface a coarse ISO 2768 class, would itself be an unrealistic, hard-to-defend
choice for a flight-critical mating flange). **Conclusion: raising n, or re-picking which n=2/3
tolerances to compare, cannot close this gap with real, defensible numbers — the imbalance is a
structural property of comparing linear ($\sum$) to root-sum-square ($\sqrt{\sum(\cdot)^2}$) growth,
which is also literally the pedagogical content (D1/D2) this case teaches.**

**2. A more realistic framing: "today's N vs. next year's contracted M"?**
Considered per the task brief. This reframing doesn't change the underlying math problem above —
any metric derived from ratios of $T_{WC}(n)$ and $T_{MRSS}(n)$ (or a load-based margin computed
from either) preserves the same percent-difference structure, since margin is just allowance
divided by a stacking-method's tolerance value. No real, citable cost or schedule data was found
(and none was invented, per the hard line against fabricating numbers) that would let a genuinely
different metric — e.g., dollar cost of early qualification vs. risk of deferring — be built without
inventing figures. This framing was set aside, not pursued into a rewrite.

**3. More precise real tolerance data that would change the crossover?**
Downloaded and `pdftotext`-extracted the Lazansky/SNC paper locally (WebFetch alone could not read
it — image-encoded PDF, same issue as GD-ED-2214). Found a real, previously-uncited datum: SNC's
FEM analysis of their sub-24" (61 cm) Low-Profile Separation System predicted **local gapping of
.0015"–.0035" (38–89 µm) at the joint heel at 9,200-lb nominal band tension** (Lazansky, p.341/651).
This is real and sourced, but it answers a different physical question than Appendix E's MA4 (it's
a predicted elastic-deformation gap under a specific real system's load, not a general dimensional
gapping-allowance budget for an arbitrary joint's tolerance stack) — substituting it directly for
MA4's 0.070 in would make both stacking methods fail NASA-adjacent thresholds already at n=3,
destroying the premise that Wes has a real choice today. Not used as a direct substitute; flagged
here as a real number future authors could use if MA4 is ever revisited with a different bridging
model.

**4. Is there a more realistic version of "the RSS Stack" itself?**
This is what resolved the case. Searched `modified RSS tolerance stack-up "1.5" safety factor
semi worst case aerospace tolerance analysis` and follow-ups. Found and verified via a primary
academic/industry source — **F. Scholz (Boeing Research & Technology / Boeing Information &
Support Services), "Tolerance Stack Analysis Methods" (December 1995)**
(`https://faculty.washington.edu/fscholz/Reports/isstech-95-030.pdf`) — downloaded and
`pdftotext`-extracted locally (WebFetch on this PDF also failed to extract useful text on the first
pass; the local extraction worked and is authoritative here, confirmed against `grep` hits for
"1.5", "modified", "mrss", "bender", "motorola"). The paper documents, quotes, and reproduces the
equation for a real, well-established correction to naive RSS tolerance stacking:

- **A. Bender Jr. (1962), "6 × 2.5 = 9, Benderizing tolerances — a simple practical probability
  method of handling tolerances for limit-stack-ups," Graphic Science, 17-21.** Bender's finding:
  real shop-floor tolerances, when specified from limited experience, often really describe a
  ±2σ range rather than the ±3σ range naive RSS assumes — so RSS should be corrected by a factor
  of 3/2 = 1.5.
- Scholz's paper (Eq. 4, p.16): $T^{Bender}_{assy,stat} = 1.5\sqrt{\sum a_i^2 T_i^2} = 1.5\,T_{assy,stat}$.
- Scholz also cites **Harry, M.J. and Stewart, R. (1988), "Six Sigma Mechanical Design
  Tolerancing," Motorola Government Electronics Group** as the source that carried this same ×1.5
  correction ("the Motorola formula") into standard Six Sigma mechanical-design practice.
- Scholz's own analysis (p.16-17) proves an important, non-obvious fact used to justify that this
  isn't a number picked to make the case's math work: **for n=2 contributing tolerances,
  $1.5\sqrt{a_1^2T_1^2+a_2^2T_2^2} \ge |a_1|T_1+|a_2|T_2$ — i.e., Modified RSS is MORE conservative
  than Worst-Case at n=2.** It only becomes less conservative than Worst-Case once enough
  comparable-magnitude tolerances stack up (this build's real n=3 is right at that transition),
  which is itself a genuinely interesting, real result to surface to students.
- Cross-checked the 1.5 factor and its "Benderizing"/Motorola-formula history against two secondary
  sources (`eng-tips.com` forum thread — WebFetch on this page returned HTTP 403 and could not be
  read directly, so it was corroborated only via the WebSearch snippet, not independently verified;
  `industrialmonitordirect.com` blog post, WebFetch-readable, corroborates the same formula,
  origin, and 1.5 value, and separately notes some optics/precision-aerospace practice uses 1.4
  instead of 1.5 — not used here, since 1.5 is the figure directly attributed to Bender's original
  work and the Motorola formula in the primary Scholz source).

**Why this is the right fix, not a workaround:** Argument A (Worst-Case) has always rested on
distrust of RSS's assumption that supplier tolerances are true, independent, normally-distributed
3-sigma bounds. Modeling Option B as *naive* RSS was itself the less realistic choice — real
tolerance engineers, for exactly the reason Argument A raises, apply the Bender/Motorola ×1.5
correction instead of pure RSS. Correcting Option B to what practitioners actually use:
- brings the two methods to **9.6%** apart at n=3 (comfortably under the 20% ceiling),
- does not require inventing any number, changing which n is "today's build," or picking an
  unrealistic tolerance-class pairing,
- preserves the entire growing-supplier-count / asymptote narrative (Modified RSS still grows as
  $1.5\sqrt{n}$, so $T_{MRSS}(n)/T_{WC}(n) \to 0$ as $n\to\infty$, same as before — a constant
  multiplier does not change which function's growth rate wins), and
- makes Argument B stronger and more nuanced rather than diluting it: Option B is no longer "trust
  pure statistics," it's "use the industry-standard, already-corrected version of statistics."

## Recomputed values (verified via a local Python check, not by hand)

| n | $T_{WC}(n)$ | $T_{RSS}(n)$ (naive, no longer used) | $T_{MRSS}(n) = 1.5\times T_{RSS}(n)$ |
|---|---|---|---|
| 3 | 0.0168 in | 0.01013 in | **0.01520 in** |
| 6 | 0.0336 in | 0.01372 in | **0.02058 in** |
| 7 | 0.0392 in | 0.01482 in | **0.02222 in** |
| 10 | 0.0560 in | 0.01771 in | **0.02656 in** |

`margin_pct` (n=3, Worst-Case vs. Modified RSS): $(0.0168-0.01520)/0.0168 = 9.55\% \approx 9.6\%$.

Margins against Appendix B's real thresholds (allowance 0.070 in ÷ predicted tolerance, MA4
unchanged): WC — 4.17 (n=3), 2.08 (n=6), 1.79 FAILS 2.00 (n=7), 1.25 exactly at floor, FAILS 2.00
(n=10). Modified RSS — 4.61, 3.40, 3.15, 2.64 — clears both thresholds at every modeled n, same
qualitative story as the original (naive-RSS) run, now at a genuinely close starting margin.

## Files changed in this pass

- `case.md` — Background, Dilemma (Option B), Challenges D1/D2/D5, Appendix D (formula + table),
  Appendix E (MA2, MA3, MA4 cross-references), Appendix F (added source S6, added retune note).
- `case.json` — `options.B`, `margin_pct` (39.9 → 9.6), `primary_metric`, `deliverables[].text`,
  `sources[]` (added S6), `balance` object (argument_b, margin_basis, margin_pct_definition,
  winning_option), `modeling_assumptions[]`, `needs_source[]` resolutions for Appendix D's RSS
  column rows.
- `FACILITATOR.md` — Argument for B, "The margin" section (retune correction + new table),
  Socratic questions 1/2/4, the trap, Anchor 1's guide line.
- `RESEARCH_LOG.md` — this section.

## Verdict

**Genuinely, defensibly close now — not forced.** `margin_pct` = 9.6% at n=3, derived by modeling
Option B as the real, industry-standard, well-documented version of RSS (Bender/Motorola-corrected,
×1.5) rather than the textbook-idealized version, with a primary source (Scholz, Boeing Research &
Technology, 1995, citing Bender 1962 and Harry & Stewart 1988) for the correction factor itself.
No supplier count, allowance, or tolerance value was changed to force this outcome. The
growing-supplier-count / asymptote narrative (D1–D5) and the n=7/n=10 Worst-Case failure story are
fully preserved. Winning option remains **B (the Modified RSS Stack)**, once the scaling frame is
engaged — see FACILITATOR.md for the full argument.

Next step: `case-readiness` on `the-clampband-margin` (re-run, since case.md/case.json changed).
