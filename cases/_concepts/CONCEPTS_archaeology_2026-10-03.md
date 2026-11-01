# CONCEPTS: archaeology (Deep Time & Language) - 2026-10-03

Target: domain `archaeology` (cluster Deep Time & Language), NON-SPORTS A slot in the sports-science release plan. Working direction from the plan:
"dating-a-find decision using radiocarbon decay". This sheet is a verified-concept sheet (the user asked for web checks), so feasibility grades below
rest on pages actually fetched. Overlap check: `readmodel/cases_index.json` has no archaeology case (domains.json `existing_cases: []`);
`cases/*/case.md` radiocarbon/half-life hit is only `the-dosing-curve` (pharmacology, no overlap); no archaeology concept file exists.

Evidence tags: **[FETCHED]** page opened and read this session; **[SNIPPET]** seen only in a search-result summary, not on the primary page;
**[UNVERIFIED]** could not confirm; **[ASSUMPTION]** disclosed modelling choice.

**Skill-gap honesty.** The spine has NO half-life, logarithm or exponential-decay skills (checked all ids). The case would exercise
`advanced-operations-how-to-evaluate-an-exponential-expression` (n=8, already covered) and sampling/statistics skills that are mostly well covered. Scores
below count only skills at n <= 2, so they are low by the formula; this slot is a domain-diversity pick (zero archaeology cases), not a gap-closer.
Calibration point: Cold Chain scored 4.2; none of these will reach it, and the ceiling is the spine, not the concepts.

| Rank | Concept | Story | Score | Feasibility |
|---|---|---|---|---|
| C1 | The Twenty-Eight Rings | L'Anse aux Meadows, Newfoundland (Norse site, 1021 CE) | 1.2 | HIGH |
| C2 | The Wrong-Aged King | Richard III's bones, Leicester 2012 | 0.6 | MEDIUM |
| C3 | The Tunnel Survey | Stonehenge A303 evaluation (test pits vs trenches) | 0.4 | MEDIUM-LOW |

**Recommendation.** Write C1. It is a recognizable real find, the key facts check out on the open-access paper, and its two options are differently
shaped in a way the math decides. Kill C3 unless a student-explorable site dataset is found (see its note). Keep C2 as the reserve; its primary lab
sources were blocked (HTTP 403), so it needs a source pass first.

---

### C1 - The Twenty-Eight Rings   ·   score 1.2   ·   tier T2-T3

**The true story [FETCHED unless tagged].** L'Anse aux Meadows is the only confirmed Norse site in North America. Standard radiocarbon dating gave
a window of roughly 990 to 1050 CE, mean 1014 (Wikipedia, citing earlier work). In 2021 Margot Kuitems (Univ. of Groningen) and colleagues
(Nature 601:388-391, doi 10.1038/s41586-021-03972-8; full text on PubMed Central PMC8770119) dated three felled wood pieces to exactly 1021 CE by finding the
993 CE cosmic-ray carbon-14 spike (a 0.91% jump, per Wikipedia's 993-994 spike page) in the tree rings and counting rings out to the bark. From the PMC page:
3 wood pieces (4 items in total), 83 individual rings measured, 127 radiocarbon measurements (115 at Groningen CIO, 12 at Mannheim CEZA),
precision better than +-2.5 permille (about 12 radiocarbon years). Ring count between the spike and the bark is reported as 28 to 31 on the PMC summary and 28 in press
accounts [SNIPPET]; **UNVERIFIED which is exact; do not state a single count until read from the paper's table.**

**Protagonist.** A fictional composite (disclosed): Maren Holt, radiocarbon lab manager on a Parks Canada-funded dating project, before the 2021 result.
Personally at stake: she signs the order for a fixed number of measurements and has one funding round, and a lab that returns "990 to 1050" again will not be funded twice.
(Disclose that the real team was not run this way; the case reframes the real design choice. Do not put invented quotes in a real person's mouth.)

**The dilemma.** A.) Spread the measurement budget as one bulk sample from each of many wood pieces and contexts across the site (a wide cross-section, each date loose)
OR B.) Spend the same budget on a dense run of single-ring samples from one or two long-grained pieces to catch the 993 spike (a one-year date, but only for the wood sampled).

**Primary metric.** Calendar years of uncertainty in the site-occupation date per $1,000 of measurement spend (width of the 95% range / spend).

**Why it's close.** A is robust: every piece yields a date and several pieces test whether the site has one occupation or many, but calibration plateaus keep each date
about 60 to 100 years wide. B can reach one year, but only if the piece has enough rings to contain the spike and a surviving bark edge, and it speaks only for those pieces
(old wood, reused timber). A wins on coverage and downside risk; B wins on precision and on the metric when the spike is caught. The case turns on the probability that a piece
holds the window, an [ASSUMPTION] with a sensitivity table, not a looked-up number.

**Would close (2 skills, 0 how-to / 2 term):** (only skills at n <= 2)
| id | kind | label |
|---|---|---|
| statistics-and-probability-non-linear | term | Non-linear (the decay/calibration curve is not a line) |
| statistics-and-probability-independent-event | term | Independent event (does one ring failing predict another? answer is no for count, yes for a shared piece: a real distinction) |

**Already-covered skills it also exercises.** `advanced-operations-how-to-evaluate-an-exponential-expression`, `advanced-operations-exponent-also-power`,
`statistics-and-probability-how-to-create-a-scatter-plot-given-a-set-of-data` (IntCal curve points), `statistics-and-probability-range`,
`statistics-and-probability-how-to-determine-the-probability-of-a-compound-event`, `advanced-numbers-how-to-find-the-percent-of-a-number`,
`measurement-how-to-convert-an-amount-with-compound-units` ($ per year of range).
Student-run decay step: N(t) = N0 (1/2)^(t/5730), with the 5,730-year half-life as the textbook constant (matches domains.json careers entry; confirm in drafting).

**Data feasibility: HIGH.** Named sources, with what I actually confirmed:
- Kuitems et al. 2021, Nature, via PMC8770119: open full text [FETCHED]; the authors state data and OxCal model code are in an open repository / Supplementary Information [FETCHED, repository location UNVERIFIED]. Journal page itself redirected to a login cookie flow (not used).
- IntCal20 Northern Hemisphere curve, file `intcal20.14c` at intcal.org/curves.html [FETCHED link exists; licence/terms NOT stated on the page, UNVERIFIED]. Students can plot the real calibration curve and see the 993 spike.
- Miyake et al. 2013, Nature Communications (spike discovery) [FETCHED via Wikipedia; primary not opened].
- Lab price: Beta Analytic AMS $595 (14 days), $1,190 (6 days), $1,785 (3 days) [SNIPPET only; the Beta pages fetched did not show the table and radiocarbon.com/pricing.htm returned 404]. A confirmed fallback: ANU Radiocarbon Laboratory price page lists AUD 500 + GST per commercial determination, AUD 400 internal [FETCHED].
- p3k14c (PEOPLE 3000) database of ~170,000-180,000 archaeological radiocarbon dates, CSV `p3k14c_2022.06.csv`, uncalibrated dates [FETCHED download page]; its homepage and download page do not state a licence, and US/Canadian coordinates are obfuscated to county centroids [FETCHED], **licence UNVERIFIED**. Useful for a "find other Norse-era dates" exploration.
Not confident about: exact per-ring cost for single-ring work (labs quote small-sample rates differently), exact ring count (above), whether Open Context holds anything for this site (not searched; Open Context API was blocked by an Anubis bot-check page when fetched, though its terms page [FETCHED] says content is open/CC with 3 requests/second limit).

**Sensitivity (SPEC §6).** NONE. Mention that Norse sites are on Indigenous land and the case concerns pre-Columbian contact; keep the framing on dating, not "discovery".
**Split risk.** NONE (2 new skills claimed).

---

### C2 - The Wrong-Aged King   ·   score 0.6   ·   tier T3

**The true story.** The skeleton found under a Leicester car park (Greyfriars, 2012) was radiocarbon dated by two labs. Search summaries report raw ranges of
AD 1430-1460 (SUERC Glasgow) and AD 1412-1449 (Oxford), earlier than Richard III's death in 1485, then a corrected combined range of cal AD 1455-1540
after allowing for a marine diet (about 25% of dietary protein from seafood) [SNIPPET only]. **The primary Leicester PDF and page returned HTTP 403, so all figures here are UNVERIFIED.**

**Protagonist.** Fictional composite: Dr. Priya Nair, dating specialist on the identification team (not the real scientists). At stake: whether the lab report
says "consistent with 1485" without being wrong about why.

**The dilemma.** A.) Report the raw calibrated date from the bone collagen and flag the offset as a caveat (tight range, systematically too old) OR B.) Spend the extra
budget on stable-isotope diet measurements and apply a marine-reservoir correction (an honest range about 85 years wide, with the fraction-marine itself uncertain).

**Primary metric.** Probability that the reported 95% range contains the true death year per year of range width (coverage vs width). Students compute both options' contained-the-answer test against 1485.

**Why it's close.** A is precise and cheap but its range misses 1485 entirely, which is a bias, not noise, so it dominates only if you ignore that. The balance risk is real:
B's range is wide enough that it also contains dates that would be inconsistent with the identification, so a skeptic can say B proves little. If the drafting pass shows A is
simply wrong with no defensible reading, kill this concept (it would fail the balance test).

**Would close (0 skills at n <= 2).** Exercises `advanced-numbers-how-to-find-the-percent-of-a-number` (25% marine), `statistics-and-probability-how-to-find-the-mean-of-a-set-of-data`
(combining lab means), `statistics-and-probability-range`, `statistics-and-probability-variability`. Score shown is the floor, 0.6 for one thin term at best.
**Data feasibility: MEDIUM.** The primary lab report (le.ac.uk radiocarbon-dating-glasgow-oxford.pdf) is the right source but was inaccessible here; secondary summaries only. Needs a source pass.
**Sensitivity (SPEC §6).** Human remains of a named historical person; handle respectfully, keep to the dating. Contested ethics of exhuming a monarch is out of scope.
**Split risk.** NONE.

---

### C3 - The Tunnel Survey   ·   score 0.4   ·   tier T2

**The true story.** Evaluation work for the proposed A303 Stonehenge tunnel (about 2 miles) examined some 1,800 test pits and over 400 trial trenches
[FETCHED, Archaeology Magazine 2021; Wessex Archaeology and National Highways reports exist, per search results, not fetched].

**Protagonist.** Fictional composite: Jo Okafor, field director for a contract unit with one season before construction. At stake: a finds-density report the planning inspector will read.

**The dilemma.** A.) A grid of many small test pits across the whole corridor (systematic sample, broad but shallow) OR B.) A few large trial trenches aimed at geophysical anomalies (targeted, deep, high yield per square metre).

**Primary metric.** Expected features found per square metre of ground opened (or per 1,000 person-hours).

**Why it's close.** A samples the blank areas, so it defends the claim "nothing is missing"; B concentrates on where features probably are, but cannot speak for the area between anomalies.
**Would close (1 skill, 0 how-to / 1 term, n <= 2):** `statistics-and-probability-multistage-sampling`. Also exercises `statistics-and-probability-systematic-sampling`, `...-stratified-sampling`,
`geometry-how-to-find-the-area-of-a-rectangle`, `geometry-how-to-find-the-volume-of-a-prism` (soil volume).
**Data feasibility: MEDIUM-LOW.** The 1,800 and 400 figures are confirmed for scale only. A downloadable, student-explorable dataset of per-pit finds was NOT found; reports are long PDFs on planninginspectorate.gov.uk
and highwaysengland (named in search results, not opened). Open Context was not usable (bot block). Without a dataset, results become modelled assumptions, which the user's rule disfavours.
**Sensitivity (SPEC §6).** Stonehenge tunnel is politically contested (heritage groups oppose it). Neutral framing required; the dilemma is survey design, not whether to build.
**Split risk.** NONE.

---

## Round 2 revision: C1 "The Twenty-Eight Rings" (2026-10-04)

Responds to the round-1 verdict table in `REVIEW_BRIEF_non-sports-slots_2026-10-04.md`. The original C1 text above is kept unchanged; where it conflicts, this section governs. Tags as above.

### Corrections to the facts (R1b)
- **Precision statement [FETCHED, PMC8770119].** The paper says individual 14C results are "consistently better than +-2.5 permille (1 sigma), with some averaged results better than +-1.5 permille (about 12 14C yr)". So the 12-year figure belongs to the best *averaged* results at 1.5 permille, not to 2.5. Recompute: 1.5 x 8.267 = 12.4 yr (ok); 2.5 x 8.267 = 20.7 yr. The original "+-2.5 permille about 12 years" was a conflation. Use: "individual results about 20 14C years (1 sigma) or better; best averaged results about 12". Drop any other conversion.
- **Ring count [FETCHED].** The paper's text gives only an *expected* window: the 993 CE anomaly "should be present in each of the wood pieces 26 to 31 years before they were cut" (rings -31 to -26, waney edge = ring 0). No per-piece observed count appears in the main text I could read; the Extended Data table was not retrieved. The match result is 1021 CE (95% range 1019 to 1024), 3 pieces, all with waney edge, from different trees (two fir, one juniper/thuja type). **Use: "expected 26-31 rings; the observed spike-to-edge distance is 28 (1021 minus 993, consistent with the press figure), [UNVERIFIED against the paper's per-piece table]".** Do not write "28 to 31" anywhere.
- **Spike is a property of the wood, not a purchase.** Reword the dilemma so the lab does not buy the spike: the 993 CE 14C jump is already locked into every tree ring that grew that year. The budget buys only *where you look*: ring-by-ring sampling of a piece that reaches back far enough, versus one bulk date per piece. Whether a piece contains the spike year, and a bark edge, is luck of the timber, not of the spend.
- **Framing disclosure.** The real team did what this sheet calls Option B (single-ring series on three pieces; 83 rings, 127 measurements, across Groningen and Mannheim). The A-vs-B choice is a **constructed** framing; Option A (broad bulk-sample survey) is an invented alternative, never a competing real plan. Say so in the case, and attribute no invented quotes to real people (Maren Holt stays a disclosed fictional composite).
- **Licences.** The paper is CC BY 4.0; cite that. p3k14c is CC0 (no attribution required; attribute anyway). IntCal20 data: cite the IntCal20 paper (Reimer et al. 2020, Radiocarbon) under its published licence, not "CC0". Keep the Indigenous-land note: Norse sites are on Indigenous land (Newfoundland and Labrador, Parks Canada / UNESCO World Heritage); frame the case as dating and pre-Columbian contact, not "discovery".

### Honest statement of what the math does (R1a)
The half-life formula N(t) = N0 (1/2)^(t/5730) does **not** decide this case. It is one setup line (turning a measured 14C age into a calendar question) and at most a reused skill (`evaluate an exponential expression`, n=8 already). What decides the case is: (1) **calibration plateaus**: on a flat stretch of the IntCal curve many calendar years map to one 14C age, so a 14C measurement gives a calendar range of roughly 60 to 100 years even at 12-20 14C-year precision; (2) **correlated, not independent, errors**: 15 bulk dates from the same decade sit on the same plateau, so averaging does not shrink the range by 1/sqrt(n) (this is the real "independent event" lesson, and it works against Option A's intuition); (3) the **probability of catching the spike** (does the piece reach back 26-31 rings and keep its bark edge) and the **probability a piece is reused or old wood**.
Spine skills genuinely forced: `statistics-and-probability-independent-event` (yes, and its failure for pieces sharing a plateau), `statistics-and-probability-how-to-determine-the-probability-of-a-compound-event` (spike AND bark AND not reused), `statistics-and-probability-range`, `...-non-linear` (only as a term: reading the curve), percent-of. Decay/exponent is not forced. The n<=2 skills claimed (`non-linear`, `independent-event`) still apply, but the case is a probability-and-reading-a-curve case, not a decay case; do not market it as radiocarbon decay math.

### New metric (R1a)
Retired: "years of range per $1,000" (degenerate at equal spend: B always wins on expected width).
New: **Probability the project delivers a defensible date for every occupation episode**, i.e. P(for each episode, the 95% range is no wider than a tolerance T AND no undetected reused-wood bias). A's real edge enters through coverage (30 pieces across the site test whether there are 1 or 2 episodes, and 3+ pieces per episode let you spot a reused outlier), and B's through width. Secondary tally students can also read off: independent pieces per budget (A: 30; B: 2).

### Cold solve (Python, 200,000 Monte Carlo draws per cell; script in the scratchpad, `rings.py`, not in the repo)
Model [ASSUMPTION throughout, none looked up]: budget of 30 measurements. A = 30 bulk dates, one per piece, split over the episodes; width = plateau U(50,100) + inbuilt-age spread U(10,30), shared by all pieces (correlated); a reused-piece outlier is detected and dropped when fewer than half the pieces in an episode are reused. B = 2 pieces x 15 consecutive single-ring samples; spike caught with prob ps (width 5 yr, matching the real 1019-1024 result), else wiggle-match only (width U(25,50)); reuse prob r per piece, undetected if the piece stands alone; two pieces that disagree on one episode = ambiguous = fail; with 2 episodes the pieces cover both only 50% of the time. Episodes: 2 with prob m, else 1.

| Tolerance T | ps | r | m | P(A) | P(B) | Winner |
|---|---|---|---|---|---|---|
| 30 yr | 0.2 to 0.8 | 0.1 to 0.3 | 0.2 to 0.5 | 0.00 | 0.13 to 0.69 | B in all 12 cells |
| 60 yr | 0.2 to 0.8 | 0.1 to 0.3 | 0.2 to 0.5 | 0.00 | 0.37 to 0.73 | B in all 12 cells |
| 100 yr | any | 0.1 | 0.2 | 0.60 | 0.73 | B |
| 100 yr | any | 0.1 | 0.5 | 0.60 | 0.61 | B (a tie) |
| 100 yr | any | 0.3 | 0.2 | 0.59 | 0.44 | **A** |
| 100 yr | any | 0.3 | 0.5 | 0.58 | 0.37 | **A** |

Variant, B affords only 1 piece (15 samples each side): same pattern; A wins at T=100 for r=0.3, or m=0.5 with r=0.1; B wins at T=30 or 60 everywhere (P(A)=0 there).

**Reading.** The metric fixed the dominance problem only partly. Neither option dominates *across the tolerance axis*: B wins whenever the claim must be tighter than the plateau (T of 60 or less), A wins only when the claim is loose (T about 100 yr) and reuse is plentiful (r about 0.3) or the site has two episodes. A never wins at tight T because plateau width, which no number of bulk dates removes, exceeds the tolerance.

### Does it pass the balance test? (my read; not a claimed pass)
**Not yet.** On the computed table, A wins in roughly a third of the 100-yr cells and in none of the 30/60-yr cells; whether the case is balanced depends entirely on which tolerance the story makes the protagonist need, which is a narrative choice, not a result. A plausible balanced framing exists (the funder's decision is "single 11th-century occupation or several, within a century", T about 100, with a stated reuse risk of 25-35% for logs in a sod-and-timber site), but r and m are assumptions with no source behind them. Remaining conditions for a pass:
1. Source or sensitivity-table ps (spike window plus bark edge present) and r (reuse). Source candidates: the paper's own 3-of-4 surviving-wood count at the site, and the p3k14c site records; as it stands the 3-of-4 (0.75) ratio is only an anecdote. Ship a student-facing sensitivity table (ps by r by T) rather than a point value; the dilemma then says "it depends on which tolerance you can live with".
2. Choose T from the story (what the funder can act on), then re-run; if T is genuinely 30 to 60 yr, A loses and C1 should be killed or C2 (Wrong-Aged King) promoted.
3. Review the toy A-model (combined width = plateau; no wiggle-matching of A's dates) with R1a; a smarter A (multiple dates on stratigraphically ordered pieces) would narrow the width and could help A.
Status: REVISED, balance test **not demonstrated**; resubmit to R1a only with item 2 settled.
