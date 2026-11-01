# Research Log — The Overlap Call

Stage 3 (`case-research`) run on `cases/the-overlap-call/`. 12 `{{NEEDS_SOURCE}}` placeholders in
`case.md`, plus one pre-flagged candidate Modeling Assumption in `case.json.assumptions[]`
(`dual-exposure-rate-candidate`, anticipated likely NOT FOUND). Worked in load-bearing order: the
two real contact-circle datasets first (everything else is computed from them), then the
secondary-attack-rate figure(s), then the kit allotment.

## P01–P05 — The two real ego-Facebook contact circles (Appendix A)

**Searched:** confirmed the SNAP `ego-Facebook` dataset page is still live.

**Fetched directly:** `https://snap.stanford.edu/data/ego-Facebook.html` — confirmed 4,039 nodes,
88,234 edges, 10 ego networks, McAuley & Leskovec, NIPS 2012, with a direct download link to the
raw archive.

**Fetched directly (raw data, not just the landing page):**
`https://snap.stanford.edu/data/facebook.tar.gz` — downloaded and extracted the actual archive
(732,104 bytes). This contains one `<ego-id>.feat` / `.edges` / `.circles` file set per ego node
(ego ids: 0, 107, 348, 414, 686, 698, 1684, 1912, 3437, 3980). `<ego-id>.feat` lists one row per
friend of that ego — its first column is the friend's node id — so `wc -l <ego>.feat` gives the
ego's total contact-circle size directly from the raw file, and `<ego-id>.edges` lists edges among
those friends (used below for the outlier check).

**Selection process (which two ego-ids, and why):** Circle sizes range from 59 (ego 3980) to 1,045
(ego 107). A pairwise intersection scan across all 10 egos' friend-id sets found that most pairs
share **zero or one** node — expected, since these are ten different people's real, largely
separate friend groups drawn from one combined 4,039-node graph. Only two pairs show a real,
non-trivial overlap: (698, 686) with 27 shared ids, and (414, 348) with 44 shared ids. Chose
**ego 698 (Index Patient 1) and ego 686 (Index Patient 2)**: their circle sizes (66 and 170) are
usable for a classroom exercise — large enough that the union is a real "more names than kits"
problem, small enough to reproduce and hand-count in full — versus 414/348's larger 159-and-227
circles, which would make Deliverable D1's full-set-notation write-out unwieldy for the MS band
without adding pedagogical value.

**Exact sets extracted (raw, before the D4 outlier decision):**
- Index Patient 1 (ego 698): 66 contacts — node ids 697, 703, 708, 713, 719, 729, 745, 747, 753,
  769, 772, 774, 776, 798, 800, 803, 804, 805, 810, 811, 819, 823, 825, 828, 830, 840, 856–895.
- Index Patient 2 (ego 686): 170 contacts — node ids 687–856 (contiguous in this anonymized id
  range).
- Intersection: 27 ids — 697, 703, 708, 713, 719, 729, 745, 747, 753, 769, 772, 774, 776, 798,
  800, 803, 804, 805, 810, 811, 819, 823, 825, 828, 830, 840, 856.
- Union: 209 ids.

**Outcome:** SOURCED as [S1] (dataset landing page, context/citation) and [S2] (raw archive,
`derived: true` — the set sizes, union, and intersection are computed directly from the raw files,
not themselves stated anywhere on the SNAP site). HIGH confidence on both — primary publisher,
raw data fetched and computed by hand, no proxy involved.

## P06 — The flagged outlier contact (Appendix A Data Note / Deliverable D4)

**Method:** "Appears in an implausibly large share of both circles" was read as *unusually high
connectedness within each circle*, not mere intersection membership (all 27 intersection ids are
"in both" by definition — that alone isn't implausible). For each of the 27 intersection ids,
computed its degree within Index Patient 1's `698.edges` file and within Index Patient 2's
`686.edges` file, and compared to each circle's own average internal degree (a real, computable
baseline from the same raw files: circle 698 averages 8.18 internal edges per member out of 65
possible, i.e. ~12.6%; circle 686 averages 19.48 out of 169 possible, ~11.5%).

**Finding:** node **828** is connected to 19 of the other 65 members of Index Patient 1's circle
(29.2%, ~2.3× that circle's average) and 77 of the other 169 members of Index Patient 2's circle
(45.6%, ~4.0× that circle's average). This is a real, computed statistical outlier, not an invented
one.

**Correction (2026-09-13, found during case-readiness remediation's P6 data-decay re-verification):**
the figures originally recorded here and propagated to case.md/case.json (38/65=58.5%, 154/169=91.1%,
averages 25.2%/23.1%) were exactly 2x the correct values. Root cause: `<ego>.edges` files in this
SNAP dataset list every undirected edge as TWO directed lines ("u v" and "v u"); the original script
counted raw line-appearances of node 828 (38 and 154 lines respectively) instead of de-duplicating
to unique neighbor ids (19 and 77). Because both the outlier's count and the circle-wide average were
computed the same doubled way, the RATIO (~2.3x/~3.9x, now ~2.3x/~4.0x) survived unchanged and the
D4 pedagogical conclusion (828 is a genuine, real statistical outlier) is unaffected — only the
absolute percentages were wrong. Independently re-derived directly from a fresh download of
`facebook.tar.gz` on 2026-09-13 (de-duplicating each `frozenset({u,v})` edge before computing
degree): |A|=66, |B|=170, intersection=27, union=209 all reproduce exactly (unaffected by this bug);
node 828's corrected shares are 19/65=29.2% and 77/169=45.6%, corrected circle averages 12.6%/11.5%.
Fixed in case.md, case.json, and published/The Overlap Call - Interactive.html.

**Outcome:** node 828 is the flagged contact in Appendix A's Data Note. Case.md states the raw
computed shares and lets the student reason to a verdict (D4); it does not tell them the "right"
answer. Facilitator materials record a real-contact-tracing-practice-consistent canonical
resolution (drop it as a likely data artifact pending investigation) for computing the margin, and
disclose the alternative (keep it) as a sensitivity check — see FACILITATOR.md.

## P07 — Weekly test-kit allotment (Appendix B)

**Searched:** "public health contact tracer weekly test kit allotment capacity per case
investigator CDC" — did not surface a literal published "kits per week" figure; county lab
processing-capacity numbers of this kind are operational/internal, not publicly tabulated.

**Fetched directly:** `https://www.cdc.gov/mmwr/volumes/70/wr/mm7003a3.htm` (MMWR, Jan 22 2021,
reporting on 61 U.S. health departments, June 25–July 24, 2020) — confirmed a median caseload of
**31 cases per case investigator** and **29 contacts per contact tracer**, both defined explicitly
in the article's methodology as *cumulative over the one-month evaluation period*, not a daily or
weekly rate.

**Outcome: NOT FOUND** as a literal "test-kit allotment" figure. **Exit chosen: Modeling
Assumption (MA1)**, weekly kit allotment = **45**. Basis: the real CDC figure describes tracer/
investigator *caseload* (people assigned for follow-up), not test-kit supply, and is a monthly, not
weekly, figure — it cannot be read off directly as a kit count. MA1 is disclosed as a scenario
constraint sized to be operationally plausible against that real caseload context (a small
county unit handling dozens of contacts a month implies a weekly test-kit budget in the same
rough order of magnitude, scaled up modestly for a team rather than one tracer) — not derived
arithmetically from the CDC figure, and not presented as if it were.

## P08 — Secondary-case (positivity) rate, single exposure (Appendix B)

**Searched:** "CDC secondary attack rate household close contact percent contact tracing"

**Fetched directly:** `https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2774102` —
confirmed: Madewell ZJ, Yang Y, Longini IM Jr, Halloran ME, Dean NE. "Household Transmission of
SARS-CoV-2: A Systematic Review and Meta-analysis." *JAMA Network Open.* 2020;3(12):e2031756.
Published Dec 14, 2020. Pooled estimate from 54 studies / 77,758 participants: **overall household
secondary attack rate 16.6% (95% CI, 14.0%–19.3%)**.

**Outcome:** SOURCED as [S3], HIGH confidence — peer-reviewed, dated, large pooled sample, clear
population and exposure type (household close contact). Used as the case's single-exposure
secondary-case rate, applied to contacts tested under Widest Net (Appendix B), disclosed
explicitly as a real-world epidemiological rate applied by analogy to this case's fictional
contact-tracing framing (COVID-19 household transmission, not literally the disease in this case,
which is never named) — consistent with Appendix C's real-network-proxy disclosure.

## P09 — Secondary-case (positivity) rate, dual/compounded exposure (Appendix B)

**Searched:** `"dual exposure" OR "two index cases" OR "multiple exposures" secondary attack rate
higher risk contact tracing study`; also reviewed Park YJ et al., "Contact Tracing during
Coronavirus Disease Outbreak, South Korea, 2020," *Emerging Infectious Diseases* 26(10), which
reports household (11.8%, 95% CI 11.2–12.4%, n=10,592) vs. non-household (1.9%, 95% CI 1.8–2.0%,
n=48,481) secondary attack rates from the same cohort — a real, dated, single-study example that
secondary attack rate does vary substantially by exposure type/intensity.

**Considered and rejected:** deriving a compound rate mathematically from [S3] via an independence
assumption (1 − (1 − 0.166)² ≈ 30.4%), and using the Park et al. household/non-household ratio
(~6.2×) as a proxy multiplier. Both were rejected for the same reason: **either approach forces
the two options' per-kit ratios apart by 80%+ regardless of which two ego-networks or which kit
allotment is chosen** (the ratio in this case's arithmetic reduces to the rate itself, independent
of population size — see the margin derivation in FACILITATOR.md), which cannot be brought inside
SPEC §2's ~20% balance cap by retuning a constraint. Manufacturing a same-order-of-magnitude
"plausible" compounding factor just to hit the cap would be exactly the "plausible number is not a
true number" failure SPEC §5 warns against — a number invented to make the case balance, not
because it is true.

**Outcome: NOT FOUND**, as `case.json.assumptions[]` already anticipated. **Exit chosen: the
pre-flagged fallback from case-write, executed as written** — the sourced single-exposure rate
[S3] (16.6%) is applied to **both** the union-only and intersection groups (MA2), with the
explicit disclosure (per case-write's own instruction) that this likely **understates** the
intersection group's true risk concentration, not overstates it, since every real source found
(Park et al. included) shows closer/more concentrated exposure raising secondary attack rate, not
lowering it. This keeps the case's headline metric honest and inside the balance cap; the real
pedagogical payoff — investigated in FACILITATOR.md's Thread 1 — is that a careful, honestly
sourced computation finds the two plans nearly tied on raw per-kit yield, so the decision has to
rest on the *other* real differences between the two plans (guaranteed partial coverage vs.
guaranteed full coverage of a smaller group), not on a rate advantage that doesn't actually exist
in the available data.

**Supplemental, not used in arithmetic:** Park et al. cited as [S4], MEDIUM confidence,
supplemental — establishes that exposure type does affect secondary attack rate in real contact
tracing (motivating why the dual-exposure search was worth attempting) without supplying a usable
dual-index-specific number itself.

## Summary table

| ID | Placeholder | Resolution | Value | Confidence |
|---|---|---|---|---|
| P01–P05 | Two real ego-Facebook contact circles, union, intersection | SOURCED ([S1] landing page, [S2] raw archive, derived) | Ego 698: 66; Ego 686: 170; ∩=27; ∪=209 | HIGH |
| P06 | Flagged outlier contact | SOURCED/derived from [S2]'s raw edge data; corrected 2026-09-13 (see above) | Node 828: 29.2% / 45.6% internal-degree share (~2.3×/~4.0× circle averages) | HIGH (derived from raw data, re-verified) |
| P07 | Weekly test-kit allotment | NOT FOUND as a literal figure — ASSUMPTION (MA1), informed by [S4-caseload] | 45 kits/week | n/a (assumption) |
| P08 | Single-exposure secondary-case rate | SOURCED ([S3]) | 16.6% (95% CI 14.0–19.3%) | HIGH |
| P09 | Dual-exposure secondary-case rate | NOT FOUND — ASSUMPTION (MA2): reuse [S3]'s rate for both groups, disclosed as likely understating intersection risk | 16.6% (same as single) | n/a (assumption) |

Sourced: 3 sources used directly/derived from ([S1], [S2], [S3]). Supplemental: 1 ([S4], Park et
al., context only). Assumption: 2 (MA1 kit allotment, MA2 dual-rate reuse). Dropped: 0. Open: 0.
All 12 `{{NEEDS_SOURCE}}` placeholders in `case.md` are resolved (9 filled by [S1]/[S2]'s real
data, 2 by [S3], 1 — the dual-exposure rate row — by the disclosed MA2 fallback).

## Margin (facilitator-only; not written to case.md)

Canonical resolution (D4 outlier dropped from both sets, matching real contact-tracing practice —
see FACILITATOR.md): Index Patient 1 = 65, Index Patient 2 = 169, intersection = 26, union = 208.
At K=45 kits/week and a flat 16.6% rate: Widest Net tests 45 (of 208), expected confirmed cases
round(45×0.166)=7, ratio 7/45=15.56%. Shared Risk fully tests all 26 (19 kits unused), expected
confirmed cases round(26×0.166)=4, ratio 4/26=15.38%. **Margin = 1.11%**, Widest Net (A) narrowly
ahead — well inside the ~20% cap, and this tight precisely because the underlying rate is
identical for both groups; the tiny gap is a whole-number-rounding artifact of testing 45 people
vs. 26, not a real difference in risk. Sensitivity: if D4 is instead resolved by keeping node 828
(raw intersection = 27, union = 209), margin widens slightly to 5.00% (still A) — recorded in
`case.json.balance_test` and `FACILITATOR.md`, never in `case.md`.

## Next step

Run `case-readiness` on `the-overlap-call`.
