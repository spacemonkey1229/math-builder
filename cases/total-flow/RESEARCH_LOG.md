# RESEARCH LOG — Total Flow

**Stage 3 (`case-research`), run 2026-08-12.** 18 `{{NEEDS_SOURCE}}` placeholders opened by
`case-write`; 0 remain. 14 SOURCED, 2 ASSUMPTION, 2 DROPPED. Ten sources (S1–S10), every one
fetched live in this session — by `curl` against a machine-readable service, or by `WebFetch`
against a rendered page, or by downloading a PDF and extracting its text locally. **No URL in
`sources[]` was written from memory (MCS-21).**

Data cutoff for every still-moving figure: **2026-08-12** (Appendix F, MA5).

---

## 1. Site selection — the long part of this run

The concept sheet flagged USGS National Water Information System streamflow data as an "exact-fit"
source. **That is true for the hydrographs and only for the hydrographs.** Verified directly: the
NWIS daily-values service returns approved daily mean discharge for any gaged site, and the
`get_ratings` and StreamStats services add a real stage-discharge rating and real flood-frequency
quantiles. Everything on the *cost* side had to be found elsewhere, and one piece of it could not
be found at all (§4).

The case needs something the concept sheet did not specify: **two real floods at the same gage
where the higher-peaked one carries the smaller volume.** Without that inversion there is no
dilemma — one storm simply beats both designs and the integration is decorative. Finding it was a
search, not an assumption.

| Step | What was done | Outcome |
|---|---|---|
| 1 | Pulled the full daily-mean record (1900→2026) for 10 candidate gages across IA/IL/PA/IN/OH/MN/MO and scanned every above-threshold event for peak, duration and volume | Susquehanna at Harrisburg (01570500) and Iowa River at Wapello (05465500) both showed inversions at a percentile threshold |
| 2 | Replaced the percentile threshold with each gage's **real** NWS minor flood stage, converted to discharge through that gage's **real** USGS rating | Harrisburg's inversion **disappeared** at its true flood-stage discharge (308,892 cfs) — at that threshold Tropical Storm Lee has both the higher peak and the larger volume. Recorded because it is exactly the kind of result that would have been invisible if the threshold had been chosen for convenience |
| 3 | Rejected all three large-river candidates on **physical scale**: excess volumes of 250,000–800,000 acre-feet cannot be held by any plausible storage option, so Option B would have been dominated by physics rather than by a trade-off | Narrowed to drainage areas of 150–1,400 sq mi |
| 4 | Enumerated 433 NOAA National Water Prediction Service gauges over the Upper Midwest, fetched each one's detail record for its USGS id and published flood-category stages, joined to USGS drainage areas, and kept the 73 with a real minor flood stage and a drainage area in range | 73 candidates |
| 5 | For each: fetched its USGS rating, interpolated the discharge at its real minor flood stage, and searched its whole record for unimodal, post-1975, fully-approved (code `A`, no estimated values) storm pairs showing the inversion at that real threshold, with excess volumes in a buildable 5,000–35,000 acre-foot range | 12 qualifying pairs across 6 gages |
| 6 | Picked the best | **Henderson Creek near Oquawka, IL (05469000)** — and the two design storms are **ten weeks apart in the same year (2019)**, so no rating change, no watershed change and no cross-decade comparability question sits between them |

**Why the site was not chosen to force an answer.** The threshold is the gage's published NWS
minor flood stage put through the gage's published rating — both fetched, neither picked. Appendix
F states in the open that this convention is the most decisive line in the case and invites a Hero
to attack it.

---

## 2. Placeholder-by-placeholder

| # | Placeholder | Searched / fetched | Outcome |
|---|---|---|---|
| P01–P03 | gage identity, drainage area, gage datum | USGS NWIS Site Service, expanded RDB record for 05469000 | **SOURCED S1** — 432 sq mi, 540.64 ft NAVD88, Henderson County IL |
| P04 | short high-peak flood series | USGS NWIS Daily Values, 2019-02-15→2019-03-08 | **SOURCED S2** — 8 days published, peak 8,060 cfs, all code `A` |
| P05 | long lower-peak flood series | USGS NWIS Daily Values, 2019-04-24→2019-05-14 | **SOURCED S3** — 10 days published, peak 6,700 cfs, all code `A` |
| P06 | per-day gage height alongside each discharge | Requested parameter 00065 with statistic 00003 from the same service, for both windows | **DROPPED.** The service returns discharge only — this site publishes no daily-value gage-height series. Rather than invent a stage column, the case drops it and publishes the gage's real **stage-discharge rating** instead (Appendix B), which carries the stage information the case actually needs and is load-bearing rather than decorative |
| P07 | channel capacity | NOAA NWPS gauge OQUI2 for the stage; USGS `get_ratings` (exsa) for the conversion | **SOURCED S4 + S5** — minor flood stage 21.5 ft → 1,933.91 cfs. Two sources compose; both fetched. The API also confirms OQUI2's USGS id is 05469000, which ties the stage to the discharge record |
| P08 | 1% AEP peak discharge | USGS StreamStats GageStats, station 05469000, `includeStats=true` | **SOURCED S6** — at-site 1% AEP 27,800 cfs (1924–2017). The same record returns the full quantile table (published in Appendix B as deliberately over-complete data) and `isRegulated: false` |
| P09 | levee reach length | No public figure can exist for a fictional district | **DROPPED.** Once both bids were priced at the same appropriation, reach length stopped being an input to any calculation. It survives only inside MA1's scope justification (2.50 miles), never in the scoring number — a decorative constraint removed rather than assumed |
| P10 | Crest Standard design discharge | Same USGS rating, at the stage given by Bid A's crest-raise scope | **SOURCED S5** — 26.00 ft → 5,927.22 cfs (a 4.50 ft raise on the 21.50 ft minor flood stage). The scope height was 5.00 ft (26.50 ft → 7,048.65 cfs) until the 2026-08-12 readiness run; see §6 |
| P11 | Basin Standard storage volume | 16 U.S.C. § 1002, the Watershed Protection and Flood Prevention Act | **SOURCED S8** — 12,500 acre-feet of floodwater detention per structure is the statutory ceiling; Bid B is two structures at it |
| P12 | levee raise cost | Four search framings; USACE cost documents (§4); Construction Equipment Guide's report of the Kansas City project, fetched and read | **ASSUMPTION MA1**, grounded in **S9**: $258M for an average 5 ft raise across a 17-mile project → about $2,874 per linear ft (author's arithmetic, disclosed) |
| P13 | storage cost | Five search framings, four direct fetches (§4) | **ASSUMPTION MA1**, grounded in **S10**: Illinois cropland $9,850/acre. **No public unit cost per acre-foot of rural flood-detention storage was found** — see §4 |
| P14–P15 | cfs-day → acre-feet; acre-foot in cubic feet | `wdr.water.usgs.gov/current/termDefs.html` (**HTTP 403, not cited**), then the USGS *Water Resources Data — Definition of Terms* PDF, downloaded and text-extracted | **SOURCED S7** — 1 cfs-day = 86,400 ft³ = 1.98347 acre-feet, plus the sentence that makes D1 exact for the published record |
| P16 | district appropriation | Fictional district, no public figure exists | **ASSUMPTION MA1** — $38,000,000, set so both bids' scopes are realistic against S9 and S10 |
| P17 | the Sources table | — | **SOURCED** — filled, 10 rows |
| P18 | the Modeling Assumptions table | — | **ASSUMPTION** — filled, 5 rows |

---

## 3. A structural change research forced, and the hand-back

`case-write` shipped Option B as a **levee setback** whose storage was the reactivated floodplain.
Research killed it on arithmetic, not on taste: a 2.5-mile setback of any plausible width stores a
few thousand acre-feet, against the 19,374 and 33,255 acre-feet these two storms actually deliver
above channel capacity. Option B would have lost by construction, and no honest choice of numbers
could have saved it.

Per `case-research`'s own rule — *if research forces a structural change, say so and hand it back*
— the change was handed back to `case-write` and applied there, not smuggled into an appendix:
Option B became **The Basin Standard**, two upstream floodwater detention structures. That put its
capacity on a **sourced statutory ceiling** (S8) instead of an authorial guess, which is strictly
better for the case. `case.md`'s Background, Dilemma, Challenge 3 and Appendix C were all rewritten
to match; `case.json.options`, `deliverables[]` and `appendices[]` follow.

---

## 4. NOT FOUND — the honest hole

**A published unit cost per acre-foot of rural flood-detention storage does not appear to exist in
public, and it is not in this case pretending to.**

| Attempt | What happened |
|---|---|
| USACE *Upper Mississippi River Comprehensive Plan*, Appendix D — Cost Estimates (March 2008), the single most likely primary publisher | **HTTP 403** on `WebFetch` and again on a direct `curl` with a browser user agent. **NOT FETCHED, THEREFORE NOT CITED** — MCS-21 does not have an exception for a document you are confident about |
| Iowa Watershed Approach / Iowa Flood Center | No per-acre-foot figure published |
| Van Allen Design Group, *Preliminary Regional Water Detention Plan… Muscatine, IA* (2014) | Downloaded and read in full. It is a **student capstone report**, not an engineering authority, and its pond costs are urban stormwater scale. Rejected on provenance |
| Harris County Flood Control District (Mercer basin, about $28,900/acre-ft) | Real, but urban Houston land and construction costs are a poor proxy for rural western Illinois, and it was only reachable through secondary reporting. Rejected on fit — *plausible is not the same as true, and neither is "expensive somewhere else"* |
| NRCS PL-566 programme pages | Gave the **capacity ceiling** (which became S8) but no costs |
| Naturally Resilient Communities, *Setback Levees* | Fetched successfully: $2.5–5M per mile including acquisition (Pierce County WA), about $20M per mile (West Sacramento). Real, but it prices the design that §3 removed. Recorded in `case.json.excluded_sources` so the next author does not re-run the search |

**The exit taken (case-research §5, exit 1 — stated Modeling Assumption).** Rather than launder a
mismatched number, the case states MA1 in the open: both bids come in at the board's published
appropriation. Two consequences, both good:

1. The board's scoring number has the **same denominator for both options**, so the unsourceable
   cost figure cannot decide the case — the two real hydrographs and the two sourced capacities do.
2. The appropriation becomes **margin-invariant**: flexing it ±50% in Tier 2 probe 5 leaves the
   margin at 4.26%. An assumption that cannot move the answer is the right place to put a hole.

S9 and S10 are still fetched, cited and published — they are what shows each bid's scope is the
right order of magnitude for the appropriation. Neither enters the scoring number, and Appendix E
says so.

---

## 5. Two figures deliberately **not** used

- **The regression and weighted flood-frequency estimates** returned alongside the at-site
  quantiles (1% AEP 25,100 and 27,000 cfs). Appendix B publishes the at-site column only, with the
  date range stated. Printing three competing estimates of the same quantity with no guidance
  would be noise, not filtering practice.
- **Instantaneous peaks as if they were daily means.** S6's quantiles are instantaneous; every
  other discharge figure in the case is a daily mean. Appendix B says so on the page rather than
  letting a Hero silently compare 8,060 against 27,800. This is the case's one genuine "messy real
  data" trap and it is labelled as a distinction, not as an answer.

---

## 6. Verification run at the end of this stage

- 0 `{{NEEDS_SOURCE}}` tokens remain in `case.md`.
- Every `[S<n>]` marker in `case.md` resolves to a `sources[]` row, and every `sources[]` row is
  cited at least once.
- Every `sources[]` row carries `claim`, `value`, `units`, `org`, `title`, `url`, `accessed`,
  `confidence`.
- 0 LOW-confidence sources. 7 HIGH, 3 MEDIUM, each MEDIUM with its reason written into the row.
- Every figure in `case.md` is either carrying an `[S<n>]` marker, derived in the open from figures
  that do, or sitting in Appendix F's Modeling Assumptions table.

**Next step:** `case-readiness` — Tier 1, then Tier 2 with `cases/total-flow/sensitivity_model.py`.

---

## §6 — Readiness-run addendum, 2026-08-12 (case-readiness Tier 2)

Tier 2 probe 2 (both-sides solve) returned a **balance FAIL** on the case as researched: with Bid
A's crest raise at 5.00 ft (26.50 ft → 7,049 cfs) the Crest Standard's shortfall was only 2,005
acre-feet against the Basin Standard's 9,255, and the Basin Standard had **no reachable winning
argument at all** — its one lever, usable storage, is capped by 16 U.S.C. 1002 at 25,000 acre-feet
[S8], and even a perfect 25,000 left Option A ahead by 12.35%. Per `skills/PIPELINE.md` that is a
stage-2 (`case-write`) return: *retune a constraint, never hide data*.

**The constraint retuned:** Bid A's scope, from a 5.00 ft crest raise to a **4.50 ft** crest raise
across the same 2.50-mile reach. The design discharge is still read off the same published rating
[S5] — one row down, 26.00 ft = 5,927.22 cfs — so **no new figure was introduced and nothing was
hidden**. Base margin 14.32% → **4.26%**, Option A still ahead; the Basin Standard now wins under
the twist (5.43%) and wins the base metric outright if channel capacity is set one row up the same
rating, at 22.00 ft (0.98%). Both of those routes are visible from the student packet.

**Re-verification of the citation used.** The `exsa` rating file was re-fetched during the same
run and byte-checked: RETRIEVED header `2026-07-02 17:40:01`, rating id `31.0`, and every row of
Appendix B's excerpt reproduced exactly, including 26.00 ft = 5927.22 and 26.50 ft = 7048.65. The
figure this repair rests on was fetched, not inferred.

**Two other Tier 2 findings, both fixed in the same pass:**

- The primary metric was stated two ways — "floodwater safely managed" (Background, D4) and
  "acre-feet safely managed" (Appendix D) — and the two readings scored different totals
  (floodwater only, vs the whole hydrograph including flow the channel carries anyway). Background
  now **defines floodwater** as the volume above channel capacity, Appendix D repeats the metric in
  the same words, and D4 names the same quantity.
- D1's Riemann sum could not reproduce the volume the case treats as exact under [S7]. Appendix D
  now states the time convention that makes it reproducible: each row is a daily *mean* over a
  whole day, an *n*-row storm spans *n* days, one subinterval per row. See FACILITATOR.md's Data Deep
  Dive for the three wrong sums a guide should expect to see.
