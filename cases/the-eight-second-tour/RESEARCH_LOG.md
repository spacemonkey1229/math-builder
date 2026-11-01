# Research Log — The Eight-Second Tour

Researched 2026-10-03. Four placeholders SOURCED (S1-S4); two returned NOT FOUND or were deliberately not used and became disclosed Modeling Assumptions (MA3, MA4). No fourth outcome was used.

| # | Placeholder | Searched / fetched | Found | Outcome |
|---|---|---|---|---|
| P01 | Stage 21 facts: date, distance, real times, 50 s deficit, 8 s margin, equipment, 54.545 km/h | Fetched Wikipedia "1989 Tour de France" (twice, once for stage figures, once for the equipment text in the Finale section). ProCyclingStats not used: not openly licensed. | 23 Jul 1989, 24.5 km, Versailles to Champs-Elysees; LeMond 26:57 (54.545 km/h), Fignon 27:55 (+58 s); LeMond entered 50 s behind and won by 8 s; LeMond aerodynamic handlebars, tear-drop helmet, rear disc; Fignon two discs, ordinary handlebars, bareheaded. | **SOURCED**, S1, MEDIUM (secondary, open encyclopedia). |
| P02 | Openly licensed photo of LeMond at stage 21 | Fetched the Commons file page "File:Greg LeMond 1989 Tour de France stage 21 TT.jpg"; downloaded the 1024x655 JPEG via upload.wikimedia.org (HTTP 200, valid JPEG, viewed). | Author Benjamin Werner, CC BY 2.0, original Flickr bw94/2927911618, description: LeMond beginning the stage. | **SOURCED**, S2, MEDIUM. The caption says the photo shows the start. Saved to `assets/lemond_1989_stage21_start.jpg`. |
| P03 | Peer-reviewed drag change from position (the "14%" drag figure) | NCBI esearch + efetch for García-López et al. 2008 (PMID 17943597), abstract read in full. | "Changes in the cyclists' position decreased the aerodynamic drag by 14%"; five professionals; wind tunnel; four time-trial-bike positions plus one standard racing bike; drag only, no power. | **SOURCED**, S3, HIGH. Note for the concept sheet's "neither paper compares aero bars with a conventional position": for drag this is nearly true but not exact (a standard racing bike position was among those tested for drag; the abstract says the time-trial-bike drag area was lower). The case therefore says "the 14% comes from changing position, not from a comparison of aero bars with a conventional position" and that neither study gives a power loss for aero bars versus conventional, which the abstracts support. |
| P04 | Speed above which aero gain outweighs power loss | NCBI efetch for Fintelman et al. 2014 (PMID 24726654), abstract read in full; Crossref DOI 10.1016/j.jbiomech.2014.02.029. Semantic Scholar page returned HTTP 403. | "The aerodynamic losses outweigh the power losses at cycling speeds above 46km/h"; "for speeds below 30km/h, it is beneficial to ride in a more upright TT position"; models from 19 TT cyclists at torso angles 0-24 degrees. **The abstract contains no 14% figure.** | **SOURCED** (46 km/h), S4, HIGH. The concept sheet's "peak power fell about 14% between 24 degrees and a flat torso" was NOT confirmed against the abstract (the full paper was not obtained) and is **not printed anywhere**; the 14% upper end of y is stated as the author's own assumption (MA3). |
| P05 | Sustainable-power loss y in the aero position | Searches on aero bars versus conventional position power loss (see P04 and the concept sheet's own literature notes). No peer-reviewed measurement found for aero bars against a conventional position. | Nothing citable. | **NOT FOUND -> Modeling Assumption MA3** (range 3-14%, lower bound the author's own). The case says so in Background and Appendix D. |
| P06 | Model parameters (CdA 0.32, Crr 0.004, mass 78 kg, air density 1.225) | Scenario CSV from the internal sports bundle (`07_cycling_power_speed_model.csv`: columns speed, aero power, rolling power, total power). Parameters recovered from the CSV and confirmed by recomputation (aero power at 36 km/h = 196 W; rolling 30.6 W). | A scenario model, not observed data. | **ASSUMPTION MA4**, stated openly, not cited. |

## Recomputation (done independently in `sensitivity_model.py`)

- Needed speed ratio 1675/1625 = 1.030769; cubed = 1.095177 (+9.5%).
- Cube-law break-even y = 1 - 1.0952(1 - x): 1.43 / 5.81 / 6.91 / 12.39 percent at x = 10 / 14 / 15 / 20 percent (concept table 1.4 / 5.8 / 6.9 / 12.4 confirmed).
- Full model (parameters above, baseline = Fignon's speed 52.66 km/h): 1.13 / 5.21 / 6.23 / 11.33 percent (concept table 1.1 / 5.2 / 6.2 / 11.3 confirmed). With LeMond's real speed as the baseline instead, the full-model figures are 1.15 / 5.25 / 6.27 / 11.40, so the baseline choice moves them by under 0.1 point; the case states Fignon's speed as the baseline.
- Model-mismatch: the model's power at LeMond's real 26:57 average (15.15 m/s) is 728.1 W (aero 681.7 + rolling 46.4). This number appears only in FACILITATOR.md; the student computes it in D5.

## Rejected and why

- "About a minute" gained from aero bars: unsourced, cut. The case never states how many seconds the bars gained LeMond.
- Popular "15-25%" CdA-reduction figures: not peer reviewed; named only as not used.
- Fignon's saddle sores, ponytail and sleep: contested context; kept out of the math. The Background says reports about his condition are contested and does not repeat specifics.
- Semantic Scholar: HTTP 403; the PubMed abstract (NCBI efetch) was used instead.
- The real LeMond team director is not named: not verified in this pass, and the case treats the director as a role.

## Revision 2026-10-03 (after Tier 2 P2 FAIL): MA1 redesigned

**Design change to concept C3.** The concept's MA1 (LeMond's conventional-position speed exactly equals Fignon's) was approved by the internal reviewers (R1a/b/c) without a cold solve. The cold both-sides solve (P2) showed it left Full Power a certain 50 s loss by construction, so B collapsed at "how does B win the Tour?". The coordinator directed route (a'): replace the equality with a sourced baseline.

| # | Placeholder | Searched / fetched | Found | Outcome |
|---|---|---|---|---|
| P07 | Prologue and stage 5 ITT results, LeMond and Fignon | Wikipedia "1989 Tour de France, Prologue to Stage 10", raw wikitext (the rendered-title URL "Stage 1 to Stage 11" is a 404; the correct title is "Prologue to Stage 10"). | Prologue 7.8 km: Breukink 9:54, Fignon +6 s, LeMond +6 s (tie to the second). Stage 5, 73 km: LeMond 1h 38' 12", Fignon +56 s. Page states LeMond, Yates and Hampsten used triathlon bars in stage 5. | **SOURCED**, S5, MEDIUM. |
| P08 | Mountain ITT result | Wikipedia "1989 Tour de France, Stage 11 to Stage 21", raw wikitext. | The 39 km Gap to Orcieres-Merlette ITT is numbered **Stage 15** on that page (dated 16 July; the concept sheet said "around stage 16"): Rooks 1h 10' 42", LeMond +57 s, Fignon +1' 44". Stage 21 weather: hot, dry and still. | **SOURCED**, S6, MEDIUM. |

**Observed LeMond/Fignon speed ratios:** prologue 1.0000, stage 5 1.0095 (aero bars for LeMond), stage 15 1.0109; stage 21 itself 1.0359 (hindsight; not used as a baseline). Baseline range b = 1.0000 to 1.0109. Equipment for the prologue and stage 15 is not stated on the pages, so none of the three is called a pure conventional ride.

**Result: the real baseline still leaves Full Power unable to reach the 50 s bar** (best case gains about 18 s of the 50 s). So route (b) is used as well: the primary decision criterion is the faster ride (A vs B, where b cancels), and the 50 s bar is a graded follow-on (D2-D4). With the baseline, the aero position must supply a ratio of 1.0308 / b: power factor 1.0952 (+9.5%) at b = 1.0000, 1.0601 (+6.0%) at b = 1.0109. Share of the x 10-15%, y 3-14% box where aero reaches the bar: 12.7% (cube law) / 9.3% (full) at b = 1.0000; 38.6% / 33.0% at b = 1.0109. B's case now rests on decision rule (best worst case) and the unmeasured power loss, not on reaching the target.

All earlier disclosures kept: hindsight scenario, the 728 W model mismatch (ratios only), Fintelman's 14% not printed, Fignon context out of the math.
