# Facilitator Notes — The Trial Size

**Status:** draft, written at case-write time (2026-09-01). Answer-key content — never copy any
of this into `case.md`.

## Argument for A — Full Precision

Full Precision's only data collection is inside the 16 clusters the team already has staffed,
permitted, and present in, at n=658. Applying the real Henderson & Sundaresan (1982) cluster-
survey precision formula — d = z·√(deff·p(1−p)/n), with z=1.96, deff=2, p=0.5, the same
worst-case parameters the classic 30-cluster EPI design itself used — to that real n gives a 95%
CI half-width of **±5.4%**, comfortably tighter than the classic WHO EPI ±10% actionable-precision
benchmark. Full Precision never attempts the new district at all, so ±5.4% is both its best and
its only (and therefore its worst) CI half-width. It leaves zero budget unspent. This is the
stronger argument whenever the campaign genuinely cannot act on a coverage estimate it can't
defend statistically, or whenever "half the report is unusable" is a worse outcome than "the whole
report covers less ground."

## Argument for B — Reserve And Expand

Reserve And Expand tests the certified-adequate n=192 in the same 16 existing clusters — a real
CI half-width of **±10.0%**, landing almost exactly on the classic WHO ±10% benchmark (a genuine,
checkable corroboration between Carcelen et al. 2020's own n=192 and the Henderson-Sundaresan
formula's own implied sample size for that target) — and reroutes every dollar that frees
($13,980) into 8 new clusters (floor(13,980/1,620), $1,620 each, a real $1,020 unspent remainder)
in a district with **zero** existing survey data. At the same certified-adequate density (12
participants/cluster, a disclosed Modeling Assumption — Carcelen et al. 2020 never states a
new-cluster sample size, since the source study never opened new clusters), those 8 clusters total
n=96, giving a CI half-width of **±14.1%** in the new district — wider than the classic ±10%
benchmark. Reserve And Expand's worst CI half-width (its weakest link, since a campaign report is
only as trustworthy as its loosest estimate) is therefore ±14.1%, not ±10.0% — driven by the new
district, not the one already mapped.

## The margin

**REDESIGNED 2026-09-01, second pass** (EPI precision-vs-n rebuild; see RESEARCH_LOG.md addendum).
A first remediation pass (also documented in RESEARCH_LOG.md) had already confirmed Carcelen et al.
2020 reports only two disease-specific seroprevalence CIs and never CI-width-as-a-function-of-n, so
it fell back to a $/cluster metric (34.3% margin, Reserve And Expand winning, under an MCS-46
waiver). This pass searched the WHO EPI cluster-survey methodology literature specifically for the
missing precision-vs-n relationship, and found it: **Henderson RH, Sundaresan T, "Cluster sampling
to assess immunization coverage...," Bull World Health Organ 60(2):253–260 (1982) [S7]** — the
foundational paper behind the worldwide-standard 30×7 (n=210) design — corroborated numerically by
**Rhoda DA et al., "Sample Size Parameters for Vaccination Coverage Cluster Surveys...," J Survey
Stat Methodol 13(5):587–614 (2026) [S8]**, which explicitly quotes the deff=2 / effective-n=96 /
actual-n=192 / design-n=210 derivation. Applying the real formula to Carcelen's own real, already-
cited sample sizes gives a single real statistical unit — percentage points of 95% CI half-width —
that applies identically wherever either design collects any data. This is the actual fix: not
another $/cluster workaround, but a genuine sourced precision-vs-n relationship, combined honestly
with Carcelen's real cost data (two different real papers, each figure attributed to its actual
source, no invented conversion factor).

**New `primary_metric`: worst (widest) 95% CI half-width the design's overall deliverable
produces anywhere it collects data.** Full Precision: ±5.4% (its only data collection). Reserve
And Expand: ±14.1% (its new district — its existing-district estimate, ±10.0%, is actually its
*better* number). **`margin_pct` = 61.7** (100·(14.1 − 5.4)/14.1). **Winner: Full Precision** —
a **reversal** from the prior $/cluster pass's winner. This is expected and correct: the two passes
measure genuinely different things (cost efficiency per cluster vs. worst-case statistical
precision), and this pass's job was to find the real, previously-missing precision-vs-n
relationship and let it determine the metric honestly, not to preserve the earlier winner.

61.7% exceeds the SPEC §2 ~20% cap. **Retune considered:** solving for the new-district CI
half-width that would bring the margin to exactly 20% gives d≈6.75%, which back-solves to n≈419
new-district participants — a density of ≈52/cluster across the 8 new clusters, over 4× the
certified-adequate density (12/cluster) Reserve And Expand's own philosophy would ever use, and
unsupported by anything in Carcelen et al. 2020 or the EPI literature. No defensible retune was
found. This is a candidate for a fresh MCS-46 `balance_test_waiver` (a genuine, sourced, large
effect — the new district's small cluster count structurally cannot reach classic EPI precision
without far more new-cluster participants than the freed budget buys — not a modeling shortcut),
but the *prior* waiver (granted for the now-superseded $/cluster metric's 34.3% margin) does not
carry forward automatically; `case.json`'s `balance_test_waiver.granted` is left `false` pending
fresh project-owner review under these new numbers.

The trap below is updated for this reframe, but the underlying mistake it catches is the same
shape as before: a hero who treats the freed $13,980 as if it buys a *proportional* share of the
existing district's precision, rather than recognizing that clusters and participants sit on
completely different cost *and* precision curves, will overstate Option B's case.

## Anchor ladder (SPEC §7.1)

### Intro

Frame the format: this is a real budget sign-off with a field team standing in the doorway waiting
on it, not a worksheet. Name the opener — "You are Dr. Amara Kondwani. The motorbikes are idling.
The coordinator has two cooler boxes and a clipboard, and the rains are coming. You have to pick a
design before the sampling window closes."

### Launch

Read the Overview aloud, stop at "starts reading," and show the two-design split with no numbers
yet: one plan spends the whole budget deeper into territory the team already knows; the other
spends the same money to reach territory nobody has ever measured. Ask: "Just from that framing —
before any arithmetic — which one would you defend first, and why?"

### Anchor 1 — Take a stand and vote

"Is anyone courageous enough to stand with Full Precision — spend it all on the clusters we
already have?" Count hands. "And Reserve And Expand — spend less here, reach further?" Count
hands. Record the split; it is the number the Close comes back to.

### Anchor 2 — What is the problem we're solving?

Let confusion grow. Heroes will want to jump straight to "which design is better," but push:
"What does 'better' even mean here — tighter statistics on what we already know, or any real data
on what we don't? Can you put both of those on the same ruler?" Let the room discover on its own
that this can't be settled by feel — it takes a real, published formula (the classic WHO cluster-
survey precision relationship in Appendix D) applied honestly to both districts before "tighter"
and "wider" can even be compared as numbers, and it is exactly that formula, plus D1–D4's cost
algebra, that the Data Deep Dive uses to settle it.

### Anchor 3 — What is the process?

Walk the room toward: derive the fixed and marginal cost from the two real data points (D1), graph
it (D2), read the Budget-Remaining line and its x-intercept (D3), then solve the break-even system
of equations (D4) before bringing in the real precision formula (Appendix D) to compute each
design's actual CI half-width. "Is our question still the right one, now that we can see the
process?"

### Anchor 4 — What don't we know?

Surface the honest open items: the fixed infrastructure cost is not stated directly anywhere in
the source paper — it has to be derived algebraically (D1), not looked up. The new-cluster
participant density (12/cluster) is a disclosed Modeling Assumption, not a number either source
paper states — Carcelen et al. 2020 never actually opened new clusters. Every other figure in
Appendices A–D is a real, directly sourced number from one of two published studies — ask "does
that change how confident you are in the final number, versus a case where these were guesses?"

### Data Deep Dive

Now the numbers. Walk the room through D1's derivation of the fixed cost (F = 68,558 − 30·658 =
$48,818) and the resulting Cost(n) = 48,818 + 30n line, then D3's Budget-Remaining line and its
x-intercept, then D4's break-even system of equations. Only after that, bring in Appendix D's real
precision formula and reveal the CI half-width comparison: Full Precision ±5.4% (n=658, existing
district only); Reserve And Expand ±10.0% in the existing district (n=192, right at the classic
WHO benchmark) but **±14.1% in the new district** (n=96 across 8 new clusters) — its actual weakest
link. Have the room compute the formula themselves at each n before revealing the full table.

### Twist

Reveal that the ±14.1% new-district figure depends entirely on a disclosed Modeling Assumption:
that new clusters get tested at the same 12-participants/cluster density as the certified-adequate
existing design. Ask: "Reserve And Expand's whole argument for opening 8 clusters instead of fewer,
bigger ones assumed this density. What if the freed budget were spent on 4 new clusters tested twice
as deep instead of 8 tested at the certified floor — does the new district's precision improve, get
worse, or does the total new-district n (and therefore the CI half-width) stay exactly the same
either way?" (Answer, mechanically checkable: the formula only depends on total n, not on how it's
split across clusters, so 4 clusters × 24 participants and 8 clusters × 12 participants give the
*identical* ±14.1% — but deff=2 already prices in the extra variability from fewer, bigger clusters,
so splitting the same total n across *fewer* clusters would in reality violate the same deff
assumption the whole formula relies on. The real lever is total n, not cluster count — and total n
is capped by the same $1,620/cluster marginal cost either way.) This surfaces that Reserve And
Expand's shortfall against the WHO benchmark is a real structural feature of how much total data
$13,980 can buy in brand-new territory, not an artifact of how the clusters happen to be split.

### Close

Re-vote. Compare against the Anchor 1 tally. "Did we ask the right question at Anchor 2? Was this
ever really a question about which design is 'more scientific,' or about whether a first estimate
in a district with none is worth accepting at a wider precision than the field's own standard?"

### Lessons Learned

- A fixed cost that is identical under both options cancels out of an honest comparison and should
  never be cited as an advantage for either side — several Heroes will try anyway.
- A metric has to use the same unit for both options before a percentage margin means anything.
  The first version of this case's metric (precision vs. discrete cluster count) could not be
  honestly compared at all; a later pass reframed around dollars-per-cluster, which worked
  arithmetically but sidestepped precision entirely. The real fix was finding an actual published
  precision-vs-sample-size relationship (Henderson & Sundaresan 1982) and applying it to both
  districts — the same unit, in the same formula, wherever either design collects data.
- "Worst case" can beat "average case" as the fairer metric when a report's overall credibility
  depends on its weakest estimate, not its typical one — Full Precision's single ±5.4% estimate
  beats Reserve And Expand's better-in-one-place, worse-in-another pair (±10.0% and ±14.1%) exactly
  because the campaign has to trust the worse of the two.

### Standards Touched On

Statistics And Probability/Algebra — X-Intercept, Y-Intercept, Slope, System Of Equations, and the
5 how-to skills (identify slope from data/graph/equation, write a linear equation from data, write
a linear equation from a graph, draw a line from an equation, solve a system of linear equations).
`new_coverage[]` is empty by design — see the reinforcement note in `case.json`.

---

## 45-Minute Socratic Plan (SPEC §7.3)

| Time | Move |
|---|---|
| 0:00–3:00 | Cold-call launch (Intro/Launch above), 30-second commitments, stand/sit vote (Anchor 1) — no explanation yet. |
| 3:00–10:00 | Position defense: "Convince us why it's better, not just cheaper" (Anchor 2 — can precision and reach even be compared?). |
| 10:00–15:00 | Pressure-test the models: process and open assumptions (Anchors 3–4) — derive the fixed cost, name what's genuinely sourced vs. derived. |
| 15:00–25:00 | Data Deep Dive — D1–D4 together, then reveal the real CI half-width comparison via Appendix D's formula. |
| **25:00** | **DROP THE TWIST** — the new-district density assumption and whether cluster-count vs. participant-count changes the answer, delivered slowly. |
| 25:00–30:00 | Immediate recommit — who reverses? "Does the new district's shortfall survive, or was it just how we split the clusters?" |
| 30:00–40:00 | Threaded deep conflict, two named threads: (1) worst-case vs. average-case as the fairer way to judge a two-district report; (2) tighter precision on the known district vs. any real (if wider) data on the unmapped one. |
| 40:00–45:00 | Close, re-vote, Lessons Learned. |

---

## Five Socratic questions

1. Full Precision spends every dollar on participants inside the same clusters — once you've computed the fixed cost and the marginal cost per participant, at what sample size does that spending stop being worth it, and how would you show that turning point on your graph?
2. Reserve And Expand frees up money by testing fewer people, but opening a brand-new cluster costs far more per cluster than testing one more person costs per participant. How many participants' worth of savings does it actually take to fund even one new cluster, and does that change which plan you'd defend?
3. Your x-intercept on the Budget-Remaining line tells you the exact sample size where the budget runs out. What would have to change about the fixed cost or the marginal cost for that x-intercept to move, and which of those two is the campaign more likely to actually control?
4. If the national office told you tomorrow that one whole district had zero survey coverage at all, would that change how you weigh "tighter precision in a mapped district" against "any real (if wider) data in an unmapped one," and where does that trade-off show up in your system of equations?
5. Your system-of-equations solution finds the sample size where Full Precision and Reserve And Expand cost exactly the same. Whose argument gets stronger the further the actual chosen n moves away from that break-even point, and whose gets weaker — and separately, does that break-even sample size have anything to do with which design hits the WHO ±10% precision benchmark, or are those two different questions?

## The trap

Heroes will compute "dollars saved" by testing fewer participants under Reserve And Expand and
treat that savings as if it directly buys proportional new coverage or proportional precision. It
doesn't: clusters and participants are priced on completely different marginal cost scales, and
precision scales with the square root of sample size, not linearly — so doubling the new-district
participant count only shrinks its CI half-width by a factor of √2, not by half. A pitch that
stops at "look how much money is left over" or "look how many new clusters we opened" without
running the real precision formula on the resulting n is making an argument the numbers don't
actually support — in either direction. The mirror-image trap: Heroes defending Full Precision
sometimes argue from the derived fixed cost (the y-intercept) itself, treating it as "wasted"
money — it isn't; that infrastructure cost is identical and unavoidable under both designs, so it
cancels out of any honest A-vs-B comparison and should never be cited as an advantage for either
side. A third trap specific to this reframe: Heroes may assume "more clusters always means better
overall precision" — it doesn't, because precision is computed per-district, not summed or
averaged across districts; opening more clusters in a new district can *lower* the campaign's
worst-case precision even while *raising* its total geographic reach.

## Sensitivity note (SPEC §6)

This case names a real disease context (measles/rubella) and a real public-health surveillance
setting. Framing is protective throughout — finding and closing immunity gaps ahead of a
vaccination campaign — with no disease-outcome, mortality, or outbreak-harm content anywhere in
the student-facing material. Standard "keep the case on the neutral computational question" note
applies; no elevated handling needed beyond that.

## Disclosed research gaps (for case-research) — RESOLVED 2026-09-01, see RESEARCH_LOG.md

1. **The fixed cost (y-intercept) is derived, not directly quoted.** Neither source paper states
   the fixed infrastructure cost as a standalone figure. It must be recovered algebraically from
   two real published figures (a total cost at a known n, and the real marginal cost per
   participant) — the same derivation D1 asks the student to perform. `case-research` should
   re-derive it explicitly from the primary source and cite both real inputs used, not treat the
   derived value as if it were itself a directly-quoted number.
2. **A per-dose vaccine price was considered and explicitly excluded.** An earlier framing of
   this concept considered pricing "what else the freed budget could buy" in terms of additional
   vaccine doses, sourced from UNICEF Supply Division measles-rubella vaccine price data. Every
   UNICEF Supply Division PDF returned an automated-fetch block (HTTP 403) during concept
   research. The case as written does **not** depend on that figure — the freed-budget framing
   uses only the real, already-sourced additional-cluster cost instead — but `case-research`
   should not spend time trying to force a vaccine-dose price into this case's math. If a future
   revision wants that framing, it should be retried via a direct browser fetch of the UNICEF PDF
   rather than automated `WebFetch`, and should be treated as a likely NOT FOUND / Modeling
   Assumption risk going in, not assumed to resolve cleanly.
3. **The missing precision-vs-n relationship was found in the EPI cluster-survey literature, not
   in Carcelen et al. 2020 itself — RESOLVED 2026-09-01, see RESEARCH_LOG.md "EPI precision-vs-n
   rebuild" addendum.** Henderson & Sundaresan (1982) [S7] established the classic design; a
   first-party quote of its exact formula could not be extracted directly (the source PDF is
   page-image-only with no accessible text layer to `WebFetch`), so the exact numeric derivation
   is corroborated instead via Rhoda et al. (2026) [S8], a peer-reviewed paper that quotes it
   explicitly. `case-research` should not assume a future revision needs to re-derive this from
   S7's raw PDF — S8's quote is sufficient and already cited.
