# Concepts — Nuclear Energy (non-sports slot D) — 2026-10-03

Domain: `nuclear-energy` (Nuclear Energy & Radioactive Waste, cluster Food, Energy & Resources). Paired with the sports-science wave
(release plan slot 8). Brief from the plan: decay/shielding angle preferred; NOT waste storage (`nuclear-waste` exists); outage
scheduling deliberately avoided (reviewer: weak 7th-12th grade engagement).

**Overlap check (done).** `cases_index.json` and a keyword scan of every `case.md` and every `cases/_concepts/*.md`: the only nuclear-energy
case is `nuclear-waste` (cylinder/cube container packing, storage contract). `firm-power` (gas vs solar+storage capacity contract) and
`the-interconnection-queue` (substation headroom) are grid cases with no nuclear content. Zero hits anywhere for Fukushima, Chernobyl,
Diablo Canyon, Palisades, technetium, Mo-99, half-life-as-decision. No title collision. Existing `the-dosing-curve` is veterinary dosing
(no radioactive decay). Note: the domain file's own scan said ~4 nuclear hits; the rest are incidental words (`airstrike`, `bioreactor-bid`, `the-sample-plan`).

**Target.** Not a gap-queue group: this is a diversity-slot brief. Spine gaps used where they fit: Geometry / Surface Area And Volume
(cylinder surface area, cylinder volume at n=2 each), which `nuclear-waste` also touches, so C1 below leans on that group only via a shielding
jacket, not a packing problem.

Evidence tags: **[WEB-CONFIRMED]** I fetched or searched it this session (source named); **[SEARCH-ONLY]** a search result states it, I could not
open the primary page (site blocked the fetcher); **[DERIVED]** arithmetic from confirmed numbers; **[ASSUMPTION]** scenario value, must be disclosed;
**[UNVERIFIED]** could not confirm, do not ship without a source. Protagonists are invented; the events, dates and organisations are real.

| Rank | Concept | Real event | Math | Score | Data | Tier |
|---|---|---|---|---|---|---|
| 1 | **C1 The Two-Hour Robot** | Fukushima Daiichi Unit 2 robot probes, 2017 (and 2024 retrieval) | Exponential attenuation (half-value layers), inverse-square, cylinder volume and surface area, scientific notation | 1.2 | MEDIUM | T3 |
| 2 | **C2 Moly Monday** | Oct-Nov 2024 Mo-99/Tc-99m shortage (Petten HFR restart delay) | Half-life, exponent, ratios, time-of-day dose scheduling | 0.0 (see note) | HIGH | T2 |
| 3 | **C3 The 2030 Vote** | Diablo Canyon licence renewed Apr 2026, state authorisation ends 2030 | Percent, ratio, unit conversion, scientific notation | 0.0 (see note) | MEDIUM | T2 |

Score note: the formula counts only skills at n<=2 (thin). C2 and C3 close none (their skills sit at n=3-89), so they score 0.0 by the
formula even though C2 has the best data and a live, recognisable event. Ranking 2 vs 3 is a stated tie-break (data grade, event
recency, student fit), not a score difference. No concept exceeds 15 skills; no split risk.

**Recommendation.** Write **C1 The Two-Hour Robot**: it is the only one that is genuinely decay/shielding and it closes the thin cylinder
volume / surface-area how-tos in a real engineering use; robots are a student-relatable hook; the key numbers are real and published. Its
weak point is data: the geometry and shielding numbers will be disclosed assumptions (see C1 feasibility), so run `case-research` first and
cut if the half-value-layer figures cannot be sourced from NIST. If C1 stalls, **C2 Moly Monday** is the safe fallback (best data, very recent
event, relatable to anyone who has had a scan) but it adds almost no thin-skill coverage. Kill **C3**: it overlaps the grid cluster in spirit
(`firm-power`, `energy-grid` concepts), is the most politically loaded, and its balance depends on a replacement-cost number we cannot source cleanly.

---

### C1 — The Two-Hour Robot   ·   score 1.2   ·   tier T3
**Protagonist.** Mina Okabe (invented), robot design lead at a decommissioning contractor preparing a camera-and-cleaner robot for a
containment vessel where nobody can go. Personally at stake: if the robot dies before it reaches the debris, the team loses a year and the
inspection window.
**The dilemma.** A.) Shield it: wrap the camera and electronics in a thicker lead-equivalent jacket, accepting the extra mass and a bulkier
head OR B.) Stand it off: keep the head light and bare, and mount it on a longer boom so it works farther from the debris, accepting a poorer
view and a shorter reach to the target.
**Primary metric.** Square metres of debris surface imaged per sortie before the electronics reach their total-dose limit (m^2 per sortie).
**Why it's close.** Shielding cuts dose by a factor that doubles each half-value layer, but every layer adds mass, and mass is capped by how
the arm and the access pipe can carry it. Standing off cuts dose with the square of distance, but the farther lens sees less detail and the
boom can reach less area. Each wins on one axis (dose per minute vs. area per minute); the metric forces the tradeoff.
**Real event (the setting).**
- Feb 2017, Fukushima Daiichi Unit 2: a remote-controlled robot cleaning a path in the primary containment vessel measured radiation up to
  650 Sv/h; TEPCO had earlier (2 Feb 2017) estimated 530 Sv/h from camera image noise. [SEARCH-ONLY: TEPCO release 1375551_10469 and WNN
  surfaced in search; TEPCO page returned 403 to the fetcher; the 530 and 650 figures appear in secondary summaries]
- The robot and cameras were designed to withstand 100 Sv/h for 10 hours (= 1,000 Sv total, [DERIVED]). [WEB-CONFIRMED: World Nuclear News,
  2015 article on the Toshiba/IRID robot, "around ten hours in an environment with a dose rate of 100 sieverts per hour"]. At 650 Sv/h that
  gives about 1.5 h [DERIVED]; secondary sources say the robot "lasted two hours". [SEARCH-ONLY; verify against the TEPCO release before
  using "two hours" in the case title or text]
- Nov 2024: first fuel-debris sample (~0.7 g) retrieved from Unit 2 with a telescopic device up to 22 m long; sample dose rate <24 mSv/h at 20 cm.
  [WEB-CONFIRMED: World Nuclear News; first attempt suspended Aug 2024 because the push-pipe sections were in the wrong order, camera
  faults in Sept, sample grasped 30 Oct, trial retrieval completed 7 Nov 2024]. This gives a real "stand-off arm" counterpart for option B.
- The 2017 robot ran into trouble but exact failure mode (cable, camera, dose) is [UNVERIFIED]: do not state a cause.
**Would close (2 thin how-to):**
| id | kind | label |
|---|---|---|
| geometry-how-to-find-the-volume-of-a-cylinder | how-to | How to find the volume of a cylinder (shield jacket as outer cylinder minus inner cylinder, then mass = density x volume) |
| geometry-how-to-find-the-surface-area-of-a-cylinder | how-to | How to find the surface area of a cylinder (area of the jacket to be wrapped) |

Score: raw 2.0 (n=2 each, 2 how-to x 1.0), no group bonus, x MEDIUM 0.6 = 1.2.
**Already-covered skills it also exercises.** `advanced-operations-exponent-also-power` (8), `advanced-operations-how-to-evaluate-an-exponential-expression` (8:
dose = D0 x (1/2)^(thickness / HVL)), `measurement-how-to-find-a-missing-amount-in-a-proportion` (13: inverse-square as a ratio of squared
distances), `measurement-how-to-convert-an-amount-with-compound-units` (20: Sv/h to Sv per minute), `advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation` (6).
All ids checked against `standards_spine.json` this session.
**Data feasibility: MEDIUM.** Named sources:
- TEPCO Fukushima Daiichi decommissioning pages (PCV investigation reports, Unit 2) for the dose-rate readings and robot specs.
  [SEARCH-ONLY: pages appear in search; fetcher got 403, so fields not confirmed by me]
- World Nuclear News articles on the 2015/2017/2024 robots (free). [WEB-CONFIRMED for 2015 specs and 2024 sample]
- NIST XCOM photon cross-section database (physics.nist.gov/PhysRefData/Xcom): free, input an element and energy, returns mass attenuation
  coefficients; this is the honest source for lead/steel/tungsten half-value layers. [WEB-CONFIRMED the tool exists and is free; terms of use
  not stated on the page, NIST data is typically public domain, confirm before quoting a licence line]
- 10 CFR 20.1201 (NRC occupational dose limit) as a human-worker comparison. [UNVERIFIED: eCFR fetch was redirected; do not state the number until opened]
Sources I am NOT confident about: gamma energy of the dominant source term at the debris (Cs-137 662 keV is the usual assumption: [ASSUMPTION]);
the distance from robot head to debris and the pipe diameter/payload limit that caps shield mass (will be scenario values, [ASSUMPTION]);
dose is not truly inverse-square from an extended debris bed (disclosed simplification, graded "what the model leaves out" step). Density
of lead is textbook, fine. So the real data anchors the story and the budget; the options are scenario design.
**Sensitivity (SPEC §6).** Nuclear accident site. Facilitator flag: frame as an engineering problem on an unmanned probe; no casualty content;
note that the 650 Sv/h figure is an instrument/robot estimate, and the case uses machine tolerance, never human dose.
**Split risk.** NONE (about 8 skills).

---

### C2 — Moly Monday   ·   score 0.0 (formula), best data   ·   tier T2
**Protagonist.** Dana Whitcomb (invented), lead nuclear medicine technologist at a regional hospital. A generator arrives Monday, the week's
supply is cut, and the schedule has 40 patients waiting. Personally at stake: she signs the schedule that decides who is scanned this week.
**The dilemma.** A.) Keep standard per-patient activity and scan fewer patients, deferring the rest OR B.) Cut per-patient activity and run longer
acquisitions so more patients are scanned this week, accepting longer table time and a tighter camera schedule.
**Primary metric.** Completed diagnostic-quality studies per curie of Mo-99 ordered (studies per Ci).
**Why it's close.** Image counts scale with activity times scan time, so halving activity roughly doubles the scan time; B stretches the same
supply across more patients but is capped by camera hours and by how long a patient can lie still. Tc-99m also decays with a 6 h half-life, so
a dose drawn at 2 pm needs about twice the generator activity of the same dose drawn at 8 am (reasoning, not data): front-loading the
morning, which A does naturally, is cheaper per patient than B's spread. Both sides defensible, no dominated option.
**Real event (the setting).**
- Oct 2024: Petten HFR (Netherlands) failed to restart after maintenance because of a pipe deformation above the vessel; the 10 Oct restart was
  postponed. [WEB-CONFIRMED: Dutch regulator ANVS notice 22 Oct 2024 (via search result), SNMMI]. SNMMI (Oct 19 and 30): "up to 50%" supply
  reductions expected over three weeks; regions saw "shortages ranging from 50% to 100% of normal requirements"; MARIA (Poland) restart
  scheduled Oct 31; BR-2 (Belgium) down to early-to-mid Dec; HFR restart planned Nov 4 pending approval; normal supply expected Nov 11.
  [WEB-CONFIRMED: snmmi.org news article, fetched]. Verify the final actual restart date; it may have moved.
- ASNC clinical guidance: "Consider reducing the per-patient activity... you will need to increase the acquisition time to maintain the same
  quality of images", consider stress-first protocols, defer non-essential testing. [WEB-CONFIRMED: asnc.org, fetched]. This is both options in the real guidance.
- Earlier precedent: 2009-10 shortage, NRU (Chalk River, shut 14 May 2009) and HFR supplied about two-thirds of world Mo-99. [SEARCH-ONLY]
**Would close (0 thin skills; thickens covered ones).** No n<=2 skill is forced. Closest: `advanced-operations-how-to-write-a-number-in-standard-notation-given-its-scientific-notation`
(n=3, one above the thin line), curies/MBq in scientific notation.
| id | kind | label |
|---|---|---|
| advanced-operations-how-to-evaluate-an-exponential-expression | how-to | (n=8, thickens) half-life decay (1/2)^(t/T) |
| measurement-how-to-find-a-missing-amount-in-a-proportion | how-to | (n=13, thickens) activity needed at a later time |
| measurement-how-to-convert-between-units-of-time | how-to | (n=15, thickens) hours to days across the week |
| advanced-numbers-how-to-find-the-percent-of-a-number | how-to | (n=89) the 50% supply cut |
**Data feasibility: HIGH.** Named, checked sources:
- Lantheus TechneLite generator package insert on DailyMed (free, FDA label): Mo-99 half-life 66 h, Tc-99m 6.02 h, calibration at noon on
  manufacture day, sizes 37-740 GBq (1-20 Ci), eluate use within 12 h, decay tables (Mo-99: 78% at 1 day, 60% at 2 days; Tc-99m: 50% at 6 h,
  25% at 12 h, 6% at 24 h). [WEB-CONFIRMED: DailyMed page fetched]. Yield chart PDF (`technelite-tc99m-yield-chart-mon-thru-fri.pdf`)
  exists but I could not read its table (no text layer): [UNVERIFIED values], student can read it from the PDF themselves.
- SNMMI and ASNC shortage notices (above, free).
- BNL NNDC NuDat 3 for half-lives (free interactive tool; terms of use not stated on the page). [WEB-CONFIRMED the tool exists]
- NASEM "Molybdenum-99 for Medical Imaging" (2016, free on nap.edu/NCBI). [SEARCH-ONLY: NCBI blocked the fetcher with a captcha; chapter contents not verified]
Sources I am NOT confident about: how many curies a mid-size hospital actually orders and its per-study activities (stated scenario
values from published procedure standards, [ASSUMPTION], find a standard to cite); camera hours and acquisition-time scaling (assume
counts proportional to activity x time, disclosed). SNMMI journal articles on coping strategies are paywalled (JNMT), do not cite numbers from them.
**Sensitivity (SPEC §6).** Patient-care flag: clinical triage is a physician decision; the case is a scheduling-arithmetic exercise. No real
patients, no diagnostic claims; deferral framed as "scheduling", with the facilitator note.
**Split risk.** NONE (about 6 skills). Low coverage value is the issue, not inflation.

---

### C3 — The 2030 Vote   ·   score 0.0 (formula)   ·   tier T2
**Protagonist.** Luis Herrera (invented), energy analyst on a state legislative committee, drafting the one-page recommendation on whether to
extend a nuclear plant past its state deadline. Personally at stake: his name is on the memo.
**The dilemma.** A.) Extend operation beyond 2030, up to the new federal licence end (2044/2045) OR B.) Let the plant retire on the 2030 schedule
and contract replacement power.
**Primary metric.** Dollars per MWh of carbon-free energy delivered over the extension period.
**Why it's close.** Extension keeps about a tenth of the state's electricity zero-carbon with sunk plant and refuelled units, but carries
continuing cost, the offsetting federal subsidy, and ageing-equipment risk; retirement frees money and queue space but must be replaced with
a mix that may be cheaper per MWh yet less firm. Cannot be judged balanced until a replacement-cost source is found.
**Real event (the setting).**
- 2 Apr 2026: NRC approved Diablo Canyon licence renewals; plants now licensed through 2044 and 2045; state law (SB 846, Sept 2022)
  authorises operation through 2030, anything later needs legislative action; about 10% of California's electricity and 16% of its zero-carbon
  electricity in 2024; up to $1.1 billion federal Civil Nuclear Credit Program award. [WEB-CONFIRMED: Governor's office release, fetched]
- Exact unit retirement dates under SB 846 (2029 and 2030?) [UNVERIFIED]; CPUC SB 846 page exists [SEARCH-ONLY].
**Would close (0 thin skills).** `advanced-numbers-how-to-find-the-percent-of-a-number` (89), `measurement-ratio` (29), scientific notation for MWh/TWh
(`advanced-operations-how-to-write-a-number-in-scientific-notation-given-its-standard-notation`, n=6). No gap value.
**Data feasibility: MEDIUM.** EIA Open Data: free, API key registration required; nuclear plant outage series pulled daily from NRC; generation
and capacity-factor series not confirmed on the page I fetched. [WEB-CONFIRMED outages; generation UNVERIFIED]. PG&E 10-K on SEC EDGAR for cost
(search surfaced FY2025 10-K; contents not read) [SEARCH-ONLY]. NRC datasets page returned 403 to my fetcher, the domain file lists it as
LIVE, treat as unconfirmed by me. Not confident: replacement-power cost (no clean public number), plant cost per MWh.
**Sensitivity (SPEC §6).** Active state politics, nuclear policy is partisan-adjacent; needs a neutral-framing facilitator note.
**Split risk.** NONE. Honest flag: closest to the grid cluster, weakest dilemma balance, lowest student pull.

---

## Notes for the review pass
- Not proposed: outage/refuelling scheduling (per brief), spent-fuel storage (`nuclear-waste` exists), Chernobyl tourism (high sensitivity, ongoing war damage, would need its own review).
- Open items before any case-write: (1) open the TEPCO 2017 release by hand and confirm 530/650 Sv/h, robot tolerance and what actually ended the mission;
  (2) source an HVL or mass attenuation value for lead at 662 keV from NIST XCOM; (3) for C2, read the Lantheus yield chart and pick a published
  administered-activity standard; (4) confirm HFR's actual 2024 restart date.
- Gap flagged: the spine has no logarithm, exponential-function or inverse-variation skills, so decay can only be taught through exponent
  evaluation and proportions; a log-based half-life solve (time to fall below a threshold) cannot be claimed.

---

# Round 2 revision (2026-10-04)

Original sheet above is kept unchanged. Decision: **C2 Moly Monday is now the primary pick; C1 The Two-Hour Robot is demoted to reserve; C3 stays killed.**

## Why C1 was not rebuilt
Decision rule: rebuild C1 only with real sourced constraints from primary documents I actually fetch. This session, the TEPCO 2017 release
(`tepco.co.jp/en/press/corp-com/release/2017/1375551_10469.html`) again returned HTTP 403, so the 530 vs 650 Sv/h dates, the real access-pipe
diameter and the robot's payload/mass/reach were NOT obtained. Without them the mass cap (and so the answer) stays an invented number, which is
R1a's objection. R1a's lead-shield figures (HVL 0.555 cm at 662 keV; x3.9 / 16.8 kg at 1.1 cm; x15.6 / 38 kg at 2.2 cm; x514 / 119 kg at 5 cm;
bare lifetime 1000/650 = 1.54 h) are reviewer-computed and I did not re-derive them from XCOM here. Shielding and standoff also combine, so the
binary is false. C1 is not shippable; if revived it needs the carried-forward conditions below.

**Conditions carried on C1 (R1b corrections, apply only if revived).**
- Say the 650 Sv/h figure is an estimate derived from camera image noise (roughly 30% uncertainty), not "measured".
- Resolve the 530 Sv/h date (2 Feb vs 8 Feb 2017) from the TEPCO release itself, opened by hand; state neither date until then.
- Do not merge the separate "scorpion" robot mission into the story.
- NIST XCOM is **not** simply "public domain". Fetched this session (nist.gov/open/license): non-SRD NIST data is not subject to US copyright
  (17 U.S.C. 105) and may be copied, distributed and used to make derivative works royalty-free worldwide, but may be protected abroad; modified
  data needs a notice that it was changed, with date and nature; citation should give author, year, title, publisher, URL and access date; data
  is provided "AS IS" with no warranty. Standard Reference Data products carry a separate copyright statement ("Copyright [YEAR] by the U.S.
  Secretary of Commerce on behalf of the United States of America"). I did not confirm which category XCOM falls under, so quote that XCOM page's
  own terms before shipping.
- Do not cite any 10 CFR 20.1201 limit unless the eCFR page is opened (it was not).
- Electronics tolerance is absorbed dose in gray (Gy), not sievert (Sv). The earlier "Sv/h" tolerance wording on C1 is wrong for machines.

## Protagonist rename
"Dana Whitcomb" collides with hydrology C2 (and `CONCEPTS_next10-batch` has a near-twin "Dana Whitcombe"). Moly Monday protagonist is now
**Rosalind Teague** (invented), lead nuclear medicine technologist; grep of `cases/` found no existing use of this name.

---

## C2 — Moly Monday (revised, primary)   ·   tier T2   ·   data HIGH

**The dilemma (binary).** Monday morning the supplier confirms the generator allotment is cut, quoted as 30-50% below the standing order. The lab
has three gamma cameras and a waiting list of 220 myocardial perfusion studies for the week. Rosalind signs the schedule before the final cut is
known.
A.) **Standard activity.** Keep 500 MBq of Tc-99m per study, 15 min acquisition, so each camera slot is short; scan until the eluate runs out each
day and defer the remaining patients.
B.) **Half activity, double scan.** Give 250 MBq, scan 30 min (counts ~ activity x time, so image quality is held), so every dose stretches twice
as far but each camera slot is 45 min instead of 30 min.

**Primary metric (revised).** *Diagnostic-quality studies completed in the Monday-to-Friday week.* NOT studies per Ci (R1a: that favours B
unless camera-hour capacity binds, and it ignores that B burns camera time). Both limits are now in the metric: supply (A binds) and camera
hours (B binds).

**Real inputs (what is sourced vs scenario).**
| Input | Value | Source / tag |
|---|---|---|
| Tc-99m half-life | 6.02 h; 50% at 6 h, 25% at 12 h, 6% at 24 h | TechneLite label, DailyMed setid 3ae14c6b-3daf-4dd1-bbdb-e990fe8100e4. [WEB-CONFIRMED, fetched] |
| Mo-99 half-life, decay | 66 h; 78% at 1 day, 60% at 2 days, 47% day 3, 37% day 4 | Same label. [WEB-CONFIRMED via search result and fetch; my 66 h model gives 77.7% / 60.4%, consistent] |
| Branching to Tc-99m | ~88% of Mo-99 decays | Same label. [WEB-CONFIRMED via search result excerpt] |
| Ingrowth | ~47% of max Tc-99m at 6 h, 95% at 23 h; eluate use within 12 h | Same label. [WEB-CONFIRMED] |
| Generator sizes | 37 GBq (1 Ci) to 740 GBq (20 Ci) of Mo-99 at calibration | Same label. [WEB-CONFIRMED] |
| Administered activity, cardiac SPECT | Two-day: 350-700 MBq/study; one-day: 250-400 MBq first injection, 3x for second; for 15 min acquisition, adult BMI <25, conventional camera | EANM procedural guidelines for myocardial perfusion SPECT (2015), pp. 19-20 of the PDF text I extracted. [WEB-CONFIRMED, fetched and text-extracted] |
| Capacity limit on option B | "Total acquisition times should be no longer than 20-30 min" (patient motion); "should not exceed 30 min" for gated studies | Same EANM document. [WEB-CONFIRMED] This is the real reason B cannot go below ~half activity. |
| The reduce-activity/lengthen-scan option itself | ASNC shortage guidance: consider reducing per-patient activity and increasing acquisition time to keep image quality | asnc.org (fetched in round 1). [WEB-CONFIRMED] |
| Supply cut and timeline | up to 50% reductions over ~3 weeks; Petten HFR restarted Mon 4 Nov 2024; normal supply expected week of 11 Nov | SNMMI (round 1, fetched); ASNC "HFR Reactor Restarted" and AuntMinnie results this session. [WEB-CONFIRMED for the 4 Nov restart date via search results; I did not open the ASNC restart page itself] |
| Scenario values | 3 cameras, 8 h/day, 15 min per-slot turnover, 90% elution efficiency, 45 min uptake lag, one 08:00 elution/day Mon-Fri, generator reference = Monday 08:00, 500 MBq (inside the 350-700 range), list of 220 | [ASSUMPTION], disclosed. The ASNC/SNMMI position statements did not give a mid-lab activity; the cited standard is EANM (European), not ASNC/SNMMI, so say so and let students swap in their own site values. |
| Lantheus yield chart (Mo-99 -> mCi Tc-99m by weekday) | exists as a PDF on lantheus.com | I could not read its table. [UNVERIFIED values]; students read it themselves, case should not quote it. |

The ASNC/SNMMI cardiac guideline (2016 joint imaging guideline) with its own activities was not opened; EANM is the cited standard.

## Cold solve (Python, run this session)
Model: one generator eluted 08:00 each weekday. Eluate = 37,000 MBq/Ci x G x 0.5^(24d/66) x 0.88 x 0.90 x (1 - 0.5^(24/6.02)). A patient injected
h hours after elution draws a x 2^(h/6.02) MBq of eluate. Camera slots: 3 cameras x 8 h starting 08:30; slot = acquisition + 15 min. Each
study runs until eluate or camera slots or the 220 list run out (greedy, same order for both options).
A = 500 MBq / 15 min / 30-min slot. B = 250 MBq / 30 min / 45-min slot. Camera ceiling: A 240/week, B 150/week (3 x 10 slots x 5 days).
Hospital standing order G_normal = 1.8 Ci of Mo-99 at reference. Cut c scales G.

| Supply cut | A studies (per day Mon..Fri) | B studies | B minus A |
|---|---|---|---|
| 0% | 199 (48,48,41,34,28) | 150 (30 per day) | -49 |
| 20% | 177 | 150 | -27 |
| 30% | 161 (45,38,31,26,21) | 150 | -11 |
| 37% | 149 | 150 | +1 (break-even) |
| 40% | 144 | 149 | +5 |
| 50% | 126 (36,30,24,20,16) | 145 | +19 |

- A is supply-bound (daily counts fall because Mo-99 decays 22% a day and late-day doses cost 2^(h/6) more eluate); B is camera-bound (30 a day).
  Neither option dominates: A wins for cuts below about 37%, B wins above.
- Maximum regret over the quoted 30-50% window: A loses by 19 (at 50%), B loses by 11 (at 30%). Over 0-50%: A 19, B 49.
- Sensitivity of the break-even cut: 500 MBq -> 37%; at G_normal = 2.2 Ci it is 48%; at 2.0, 43%; at 1.5, 24%. Activity 350 MBq -> 64%
  (at G 2.2), 700 MBq -> 27%. Turnover 10 / 15 / 20 min -> 39 / 48 / 53% (at G 2.2). The break-even moves a lot with site inputs.
- Day-by-day eluate at a 50% cut (G = 0.9 Ci): 24.7, 19.2, 14.9, 11.6, 9.0 GBq Mon-Fri.
- Bare check: an injection 6 h after elution needs 2x the eluate (label: 50% at 6 h), a 24 h-old injection 16x.

## Balance test: honest status
- **Passes structurally:** neither option dominates. The sign of "B minus A" flips inside the supplier's quoted range, B pays on camera hours,
  A pays on supply, and the metric counts both.
- **Caveat 1 (tuned):** G_normal = 1.8 Ci was chosen so the break-even (37%) sits inside the quoted 30-50% window. That is a scenario value,
  disclosed as such; the case should present the sweep and let students find the break-even themselves rather than hand them a point answer.
  A different standing order moves the answer (table above), so it is not a robust "discovery" unless the case asks for the break-even cut.
- **Caveat 2 (assumed fixed):** the equal-quality premise (counts ~ activity x time) is the ASNC/EANM position but a simplification; the
  case must say so.
- **Not claimed:** a clean pass on "close call at one point". At 40-50% B wins by 3-15%; at <=30% A wins by 7-30%. I compute no pass on a single
  headline number.
- The spine still has no log or exponential-function skills; "time to fall below" is not claimable. Exponent evaluation, proportion, percent and
  time-unit skills carry the math (unchanged from the original coverage list).

## Sensitivity: patient triage
Tc-99m cardiac scans are diagnostic and clinical triage is a physician decision. Handling: (1) all patients are anonymous slots, counts only;
no names, ages, diagnoses, no real patient data, no story of a patient harmed or a death; (2) "deferred" is framed as rescheduling, with a
facilitator note that real prioritisation follows physician and ASNC/SNMMI guidance; (3) Rosalind decides activity and schedule structure, not who
is sick enough to be scanned; (4) the case does not claim either option is clinically equivalent, only that image-count scaling is the stated
guideline assumption; (5) no dramatisation of a delayed diagnosis.

## Status of the original open items
(1) TEPCO release: still not opened (403), C1 reserve only. (2) XCOM HVL: not sourced; NIST licence terms read as above. (3) Lantheus yield chart still
unreadable; EANM activity standard now cited. (4) Petten restart: reported as 4 Nov 2024 (search results; ASNC restart page not opened).
