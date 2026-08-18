# QA_REPORT — Wind Triangle

## case-readiness run — 2026-08-12

**State:** DRAFT → **TIER1_PASS**   **Verdict reached: TIER1_PASS** (not TIER2_PASS)

Tier 1 is clean. Tier 2 is **not** clean: one probe FAILS on the repaired file (P2) and one probe
could not honestly be run (P1). Per the ladder, `TIER2_PASS` requires six recorded verdicts with
zero FAIL and zero NOT RUN, so this case may **not** go to `case-publish`.

> **Read this first.** This pass violated the skill's own rule that case-readiness never fixes its
> subject. It was directed to apply stage-2/stage-3 repairs in-line, and it did — six of them, listed
> below. Three probes (P3, P4, P6) failed on the file as found and pass only *because of repairs this
> same pass applied*. A gate that repairs its own subject is not an independent gate. **Every repair
> below needs a human read before this case moves.**

---

### Tier 1 — structural (19 checks)

`python3 skills/case-readiness/scripts/tier1_structural.py --case wind-triangle --project .`

| id | result | note |
|---|---|---|
| T1-01 … T1-15, T1-17 … T1-19 | PASS | — |
| T1-16 | GAP | MCS-11 — no `case_md_sha256` recorded yet (expected on a first run; set at the end of this report) |

**BLOCKER (0)** — none.

**GAP (1)**
* `[T1-16]` MCS-11 — no `case_md_sha256` recorded yet (expected on a first run)

**POLISH (5)**
* `[T1-02]` Overview numerals auto-classified as texture (clock/year/cleared): `['412']`
* `[T1-07]` parsed 11 labels (11 bulleted, 0 from separator-run lines)
* `[T1-15]` no `published/` directory yet — nothing to drift
* `[T1-18]` no `published/` directory yet — MCS-37 has nothing to check
* `[T1-19]` no `published/` directory yet — MCS-39 has nothing to check

Tier 1 was re-run after every `case.md` edit and after every `case.json` edit. It went BLOCKED once
mid-repair (`T1-08`, S3 confidence grade written as prose instead of the `HIGH|MEDIUM|LOW` enum) and
was returned to 0 BLOCKERs before the report was written. Final run: **0 BLOCKERs, 1 GAP.**

---

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **NOT RUN** | No uncontaminated solver was available — see below. Not a pass. |
| P2 both-sides | **FAIL** | Argument A wins on none of the metrics the case measures, and the case's framing of A as the "certain / safe" plan is backwards. |
| P3 trap | PASS *(FAIL as found — repaired in-pass)* | The guide missed the FROM/TOWARD sign inversion, the most convincing wrong path in the case; now named. |
| P4 twist | PASS *(FAIL as found — repaired in-pass)* | The twist rested on `MA5`, a modeling assumption `case.md` cited but never wrote; and its flip is conditional and was undisclosed. Both now stated. |
| P5 sensitivity | **PASS** | Base verdict stable under ±50% of all four declared dials, one at a time and at the joint corners. No flips, no breach of the 20% cap. |
| P6 data decay | PASS *(FAIL as found — repaired in-pass)* | All 7 URLs fetched. S3's URL resolved but no longer served the cited issuance; re-pinned and re-verified. One factual error in Appendix D corrected. |

#### P1 · Cold solve — **NOT RUN**

The probe requires a *genuinely fresh* solver that has not seen `FACILITATOR.md`, `case.json` or
`case.md`'s facilitator-only tail. Subagent dispatch was prohibited for this run on budget grounds,
and this agent had to read all three of those artifacts to run P2–P6 at all. **A contaminated solver
is not a cold solve, and a probe that could not be run is `NOT RUN`, which is never a pass.**

What *was* established mechanically: the packet at `/tmp/coldsolve-wind-triangle/PACKET.md` builds,
and every figure D1–D5 requires is present in Appendices A–E — the case is solvable from the student
half alone (all of `case.md`'s own leg components, ground speeds, times, trip fuels, the break-even
and the minimum dispatch fuel were independently reproduced during this pass from the appendix data
without reference to `sensitivity_model.py`'s outputs).

**But the packet leaked the answer, and the leak-detector did not catch it.** `case.md` Appendix E,
MA2's sensitivity column — student-facing, and reproduced verbatim in the packet — read
*"Routing B stays cheaper throughout and the margin moves between 0.95% and 2.40%."* That is the
answer to the dilemma, printed in the student document. The P1 leak-check reported `[READY]` anyway,
because it screens for a pre-computed `margin_pct` literal (`1.67`), which MA2's cell did not
contain. **Any prior "P1 PASS" on this case was worthless — the solver was handed the verdict.**
Repaired (R1 below). *A tooling finding, outside this case's write boundary: the P1 leak-check should
screen for prose statements of the winner, not only for the margin literal.*

#### P2 · Both-sides solve — **FAIL**

*Best sentence for B:* "Under the wind field the NWS actually published, Routing B burns 27,756.2 lb
against 28,228.9 lb and arrives 5.3 minutes earlier, while flying 136.4 nm further — fuel is bought
by the hour, not by the mile."

*Best sentence for A:* "Routing B's whole advantage is 472.8 lb, and a uniform 7.21 kt error in the
forecast headwind erases it — I am not paying 136 certain miles for a number that small."

**Which side collapses, and at exactly which question.** Argument A collapses at:
*"If you distrust the forecast, why file the plan whose cost depends on it?"*

Scaling the entire published wind field from 0× to 1.5×:

| | 0× (no wind) | 1.0× (as forecast) | 1.5× | spread |
|---|---|---|---|---|
| Routing A trip fuel | 26,133 lb | 28,229 lb | 29,622 lb | **+3,489 lb (+12.4%)** |
| Routing B trip fuel | 27,706 lb | 27,756 lb | 27,792 lb | **+86 lb (+0.3%)** |

Routing A's cost is ~40× more sensitive to the forecast than Routing B's, because Routing A is the
routing with the large winds in it. A becomes cheaper only below ≈0.80× — i.e. only if the *whole*
field is overstated by about a fifth, **and only in that direction**; a symmetric error the other way
makes A worse still. The case supplies no evidence of directional forecast bias, so A's argument
reduces to an unsupported claim about which way the error runs.

Compounding this, Argument A wins on **none** of the metrics the case actually measures — not trip
fuel, not block time (B is 5.3 min faster), not lb per nm of net progress (12.381 vs 12.592), not
minimum dispatch fuel (35,213 vs 35,685 lb). Under the published data every measured quantity favours
B, and A's foothold is entirely conditional.

**Why this is a FAIL and not a quibble:** `FACILITATOR.md`'s deep-conflict thread 1 framed A as the
prudent/robust choice ("certain cost versus forecast benefit"). That framing is *factually backwards*,
and a guide running it as written would have defended the wrong side for the wrong reason.

**What was repaired, and what was not.** The backwards framing is fixed (R4) — both `case.md`'s
facilitator half and the guide now carry the exposure figures and tell the guide not to let the room
finish that thread believing the northern routing is the safe one. **That does not clear the probe.**
Stating the asymmetry honestly makes A *harder* to defend, not easier.

**The exact fix, for a human to decide (stage 2, `case-write`).** Give Routing A a metric it can win
under the published data. The two candidates that do not require re-sourcing anything:
1. **Retune MA2's direction.** The case already concedes MA2's asymmetry is "asserted, not measured."
   But this is the wrong lever — reversing it *widens* B's margin to 2.64% (see R3). Only a much
   larger northern allowance moves A, and there is no basis for one.
2. **Change the routing pair** so that Routing A is genuinely competitive on fuel under the published
   wind field — e.g. a southern swing that pays more track miles for its shelter, or a northern track
   that clips less of the jet core.
Option 2 is a real redesign: every distance, course, component, ground speed, leg time and trip fuel
in `case.md`, `FACILITATOR.md` and `case.json.derived` would have to be re-derived. **This pass did
not attempt it, deliberately** — a QA pass inventing a new routing pair is exactly the failure mode
the skill forbids.

#### P3 · Trap check — FAIL as found → PASS after repair

*Trap named from the case alone, before re-reading the guide:* the **meteorological FROM/TOWARD sign
inversion**. Appendix B reports wind by the direction it blows *from*; a student who resolves `300/78`
into components without the 180° reversal flips the sign of every along-course figure. KDBQ then reads
**+74.8 kt of tailwind** instead of −74.8 kt of headwind, first-leg ground speed comes out at ≈534 kt
instead of 384.7 kt, and **Routing A wins by a wide, entirely spurious margin** — with a full,
confident, correct-looking table behind it. It is the single most common error in this topic.

*The guide, as found, did not name it.* It named two real traps (raw wind speed vs. the along-course
component; distance flown vs. time aloft) and gave one diagnostic — *"a D3 table whose headwind column
equals the wind-speed column."* **That diagnostic cannot detect a sign inversion**, because an inverted
table has the right magnitudes. A trap the guide has not anticipated is a FAIL by the probe's own rule.

Repaired (R5): both `FACILITATOR.md` and `case.md`'s facilitator half now name it with its own tell.

#### P4 · Twist integrity — FAIL as found → PASS after repair

*Question 1 — does it invalidate a position a real room would hold?* **Yes.** Mechanically confirmed:
Routing B re-filed via KMEM burns 28,410.4 lb against Routing A's 28,228.9 lb. The verdict flips, and
every position built on "the southern route is cheaper" is now wrong. The twist introduces no new
number — KMEM's position is in Appendix A's corridor table and its 34,000 ft wind in Appendix B.

*Question 2 — does it survive the case's own stated assumptions, read a student's way?* **Not as
found.** Two defects:

**(a) `MA5` did not exist.** `case.md` Appendix A said the leg's true course is "the **initial** course
of the leg … held constant for the whole leg (SEE APPENDIX E, MA5)" — and Appendix E contained only
MA1–MA4, as did `case.json.modeling_assumptions`. The single most load-bearing geometric convention in
the case (great-circle *distance* combined with a constant *initial* course, which is strictly a rhumb
line and not the same track) was pointed at and never written. By P4's rule — *"if the effect depends
on a convention the case never states, that is a BLOCKER"* — this was a BLOCKER. Tier 1 did not catch
it: T1-06 checks orphaned *appendices*, not dangling *MA-id* references.

Re-derived under every defensible reading of that convention:

| course convention | margin (base) | winner | twist margin | twist flips? |
|---|---|---|---|---|
| initial course + great-circle distance (as written) | 1.67% | B | 0.64% | yes |
| mean of initial and final course | 2.01% | B | 0.32% | yes |
| final course | 2.27% | B | 0.08% | yes |
| true rhumb-line course + rhumb distance | 2.06% | B | 0.25% | yes |

The base verdict is robust to the convention; the twist flip survives all four but by as little as
0.08% (≈22 lb on 28,000 lb), which is not a reversal a room can defend.

**(b) The twist's flip is conditional on MA2, and `case.md` did not say so** — while
`FACILITATOR.md` *and* `sensitivity_model.py`'s docstring both asserted "MA2's own sensitivity column
in `case.md` says so." It did not. At the low end of MA2's ±50% range for the southern corridor
(0.75%) the re-route does **not** flip the verdict — Routing B stays cheaper by 0.10%. The flip holds
for every southern allowance from ≈1.0% upward.

| southern allowance | base winner / margin | twist winner / margin | flips? |
|---|---|---|---|
| 0.75% (−50%) | B / 2.40% | **B / 0.10%** | **no** |
| 1.00% | B / 2.16% | A / 0.15% | yes |
| 1.50% (as written) | B / 1.67% | A / 0.64% | yes |
| 2.25% (+50%) | B / 0.95% | A / 1.37% | yes |

Repaired (R2, R3): MA5 is now written into Appendix E and `case.json.modeling_assumptions` with its
re-derivation; the twist's conditionality is stated in `case.md`'s facilitator-only half and in the
guide's twist caveat. It is deliberately **not** in MA2's student-facing column — naming the twist
there would hand the room the amendment before it is dropped. The two false cross-references are
corrected.

#### P5 · Assumption sensitivity — **PASS**

`FLEX[]` = the four declared numeric assumption dials (`airway_allowance_a_pct`,
`airway_allowance_b_pct`, `fuel_density_lb_per_gal`, `departures_per_year`). Base: A 28,228.9 lb,
B 27,756.2 lb, **margin 1.67%, Routing B cheaper**.

**The 1.67% margin is stable under flex — this was the run's specific question, and the answer is
clean.** One dial at a time, ±50%: Routing B wins all eight sweeps, margin **0.95%–2.40%**, no flips,
no breach of the SPEC §2 20% cap. Pushing *both* MA2 dials to opposite extremes simultaneously (a
harder test than the probe requires) widens the band to **0.46%–2.88%** and Routing B still wins all
nine corners. Adding MA5's course conventions (P4 table above): B wins all four. `fuel_density` and
`departures_per_year` are exactly neutral, as MA1 and MA4 claim.

So the case does **not** owe a stated instability on its base verdict. Two instabilities that are
real and are now stated: the **twist** flip (P4), and the verdict's genuine fragility to the **cited
wind data** — a 20.5% uniform overstatement of Routing A's along-course components, or 7.21 kt per
leg, ties the two routings. The latter is not an assumption flex (it is cited NWS data, P6's
territory) and the case already discloses it as its headline finding, which D5 makes the student
compute.

#### P6 · Data decay — FAIL as found → PASS after repair

**Every one of the 7 URLs was fetched.** No verdict below rests on recall.

| id | fetched | result |
|---|---|---|
| S1 | yes | **Verified exactly.** KJFK 40.6399/−73.7787, KBUF 42.9404/−78.7306, KDEN 39.8617/−104.6732, KLAX 33.9425/−118.408, KLIT 34.7294/−92.2248, KABQ 35.0389/−106.6083 — all match Appendix A. |
| S2 | yes | **Verified exactly.** KSFO 37.6188/−122.3754, KDBQ 42.402/−90.7095, KMEM 35.0424/−89.9767, KSLC 40.7884/−111.9778, KSGF 37.2457/−93.3886. |
| S3 | yes | **FAIL as found → repaired.** See below. |
| S4 | yes | **Verified exactly.** EUROCONTROL APDB B738: cruise TAS 460 kt, Mach 0.79, ceiling FL410 — all three as Appendix C states. |
| S5 | yes | **Verified exactly.** Standard Inputs Release 10.0.1, Table 6.1 "Average fuel burn rates (kg/minute)", en-route narrow-body **40.1 kg/min**; the source names B738 in that segment, so Appendix F's MEDIUM grade and its stated reason are correct. |
| S6 | yes | **Verified exactly, at both cited URLs.** eCFR and Cornell LII both return 14 CFR 121.639 (a)/(b)/(c) with "45 minutes at normal cruising fuel consumption" in (c). |
| S7 | yes | **Figure verified, side-claim wrong.** EIA Gulf Coast jet fuel spot, monthly: **July 2026 = $3.403/gal**, release date 8/12/2026 — exact. But Appendix D said *"The series also shows an August 2026 figure"* — **it does not; the August 2026 cell is empty.** Corrected (R6). |

**S3 in detail — the failure mode the probe calls "worse than a 404".** The cited URL
(`.../cgi-bin/afos/retrieve.py?pil=FD3US3&e=202608122100&fmt=text&dl=1`) still resolves 200, but it
**ignores the `e=` parameter** and returns whichever FD3US3 issuance is current. On fetch it returned
the `130200` issuance (`DATA BASED ON 130000Z VALID 131200Z FOR USE 0900-1800Z`) whose winds are
*entirely different numbers* — DBQ 295542 rather than 307843, SFO 310545 rather than 151345, and so on
for every station. Nothing else in the pipeline would ever have noticed, and every wind in the case is
load-bearing on the verdict.

The cited data is **not** wrong — the archive permalink `.../wx/afos/p.php?pil=FD3US3&e=202608122001`
pins the issuance, and on fetch it returned `122001`, `TEMPS NEG ABV 24000`, and **all ten** 34,000 ft
coded groups matching Appendix B character for character: JFK 287047 · BUF 317547 · DBQ 307843 ·
DEN 211141 · SLC 204244 · SGF 341441 · MEM 351741 · LIT 030741 · ABQ 280940 · SFO 151345. The product
header the case quotes (issued 122001Z, data based on 121800Z, valid 130600Z, for use 0300–1200Z) is
confirmed genuine. Repaired: S3's URL replaced in `case.md` Appendix F and `case.json.sources`, with a
note recording why the old one fails (R6). All sources are 0 days old; none is over the 365-day flag.

---

### Repairs applied by this pass

Doctrine violation, applied under explicit direction. Every one needs a human read.

| # | Where | What changed | Class |
|---|---|---|---|
| R1 | `case.md` App. E, MA2 sensitivity | **Removed the answer leak** — "Routing B stays cheaper throughout" no longer appears in the student-facing document. Replaced with the flex bands, which state the sensitivity without naming a winner. | BLOCKER (P1 leak) |
| R2 | `case.md` App. E (new MA5 row) + `case.json.modeling_assumptions` | **Wrote the missing MA5** that Appendix A had cited since `case-write`: great-circle leg distance with the leg's *initial* course held constant, with the four-convention re-derivation. | BLOCKER (P4, unstated convention) |
| R3 | `case.md` App. E MA2; `case.json` MA2; `case.md` facilitator half; `FACILITATOR.md`; `sensitivity_model.py` docstring | **Corrected a backwards factual claim** — MA2 said reversing its two values "would narrow the gap"; it **widens** it, 1.67% → 2.64%. **Stated the twist's conditionality** in the facilitator-only half. **Fixed two false cross-references** that claimed `case.md`'s MA2 column disclosed the twist instability when it did not. | factual error + P4 disclosure |
| R4 | `case.md` facilitator half; `FACILITATOR.md` thread 1 | **Corrected the backwards "certainty" framing** — added the 0×–1.5× wind-field exposure figures (A +12.4% vs B +0.3%) and the instruction not to let the room finish thread 1 believing the northern routing is the safe one. | P2 finding (does not clear P2) |
| R5 | `FACILITATOR.md` "The trap"; `case.md` facilitator half | **Named the third trap** — the FROM/TOWARD sign inversion, with its own tell, and the explicit note that the existing diagnostic cannot detect it. | FAIL (P3) |
| R6 | `case.md` App. D + App. F; `case.json.sources` S3 | **Re-pinned S3's URL** to the permalink that actually serves the cited issuance, with a note on the old one's failure mode. **Corrected Appendix D's false claim** that the EIA series shows an August 2026 figure. | FAIL (P6) |

No number that changes the verdict was altered. `margin_pct` is untouched at **1.67**; every figure in
`case.json.derived` is unchanged; `sensitivity_model.py`'s code is unchanged (docstring only); the
Challenge 1/2/4/5 boilerplate is untouched. Tier 1 was re-run after every edit and ends at 0 BLOCKERs.

---

### Open findings NOT repaired

* **P2 (FAIL).** Routing A wins no measured metric. Requires a stage-2 decision — see the fix options
  under P2. **This is what keeps the case below `TIER2_PASS`.**
* **P1 (NOT RUN).** Needs one genuinely fresh solver against the now-de-leaked packet. Cheap to close.
* **GAP — the case's own clock does not line up with its forecast's validity window.** The Overview
  has Meridian 412 pushing back "within the hour"; Background calls it a morning westbound service;
  the cited forecast is valid 130600Z **for use 0300–1200Z on 13 August**, and the release is being
  built at ≈2001Z on 12 August. A flight pushing within the hour of 2001Z (≈17:00 EDT) is outside that
  window entirely, and would properly be planned against the issuance valid 130000Z. Not repaired: the
  fix is narrative and touches the Overview, which carries SPEC §1.2 constraints — a human should
  choose the wording. No number depends on it. **Suggested fix:** state the scheduled push time
  explicitly in Background, inside the 0300–1200Z window.
* **Tooling (outside this case's write boundary).** (i) The P1 leak-check screens for the `margin_pct`
  literal but not for a prose statement of the winner — it passed a packet that named the answer.
  (ii) Tier 1 has no check for dangling `MA<n>` references, which is how MA5 survived from `case-write`
  through `case-research` to here.

---

### Tier 3 — human dry-run

**NOT RUN.** Not reachable: Tier 3 requires `PUBLISHED`, which requires `TIER2_PASS`.

---

### Next step

**Fix the P2 finding and re-run.** Specifically: (1) a human reviews the six repairs above, since the
gate applied them itself; (2) stage 2 decides whether to retune the routing pair so Routing A is
competitive on a measured metric, or to accept the case as one-sided and record why; (3) dispatch one
fresh cold solve against the de-leaked packet to close P1; (4) re-run Tier 1 and Tier 2.

**This case is not publishable in its current state.**

---

## case-readiness run — 2026-08-15 (interactive HTML build + Tier 1 re-run)

**State:** TIER1_PASS (carried forward) → **TIER1_PASS (re-verified against the built interactive HTML)**

### What this pass did

1. **Placeholder audit.** `grep -n "NEEDS_SOURCE" case.md` returns zero matches. `case.json.needs_source[]`
   (24 tokens) is all `SOURCED` / `ASSUMPTION` / a documented `DROPPED`-and-replaced — none left open.
   Confirmed `standards[]` (11 ids) all resolve in `readmodel/standards_spine.json`, and `new_coverage[]`
   (7 ids, the full Pre-Calculus/Vectors group) is genuinely a subset of `standards[]` at `n=0` at
   authoring time per `LEARNING_GOALS.md` — this is a fresh-authored case closing a real spine gap, not a
   legacy conversion, so the T1-10 legacy carve-out does not apply and was not invoked; T1-10 PASSed on
   its own merits.
2. **`sensitivity_model.py` audit.** Read in full. `evaluate()` implements the case's real graded
   `primary_metric` (trip fuel in pounds, which ranks identically to "pounds of fuel burned per nautical
   mile of net progress" since both routings divide by the same fixed direct distance) — confirmed by
   re-running the script (`python3 cases/wind-triangle/sensitivity_model.py`) and diffing its printed
   figures against `case.json.derived`: exact match on every leg's along-course/crosswind component,
   ground speed, leg fuel, both routings' trip fuel (28,228.9 lb / 27,756.2 lb), the break-even
   (20.5% / 7.21 kt), the twist (28,410.4 lb, flips to A), and `evaluate()`'s own internal assertion that
   its transformed margin equals the raw fuel margin. `FLEX[]` = `["airway_allowance_a_pct",
   "airway_allowance_b_pct", "fuel_density_lb_per_gal", "departures_per_year"]` — checked each against
   the FLEX-scoping doctrine (`case-readiness/SKILL.md`, 2026-08-13 note): all four are genuine stated
   assumptions (MA1/MA2/MA4) the case author *chose*, not cited/given data. Confirmed the specific bug
   named in the task brief does **not** appear here: sourced/cited figures (waypoint positions `[S1,S2]`,
   forecast winds `[S3]`, cruise TAS/fuel flow `[S4,S5]`, the reserve rule `[S6]`, fuel price `[S7]`) are
   all in `PARAMS` but correctly **excluded** from `FLEX[]` — probe 5 sweeps assumptions only, per the
   "Only `FLEX[]` is swept" rule; cited data is P6's territory. No fix needed.
3. **Built `cases/wind-triangle/published/Wind Triangle - Interactive.html`** from
   `templates/interactive_shell.html` per `INTERACTIVE_HTML_CONTRACT.md`. Case-specific throughout:
   Overview/Background/Dilemma copied from `case.md` verbatim (zero load-bearing Overview numerals
   beyond the already-cleared `412`); Appendices A–F transcribed as real tables (positions, coded wind
   groups, aircraft performance, fuel cost, all five modeling assumptions, all seven sources with live
   links); Appendix G glossary wired to a JS `GLOSSARY` object of **8** terms (`Vector`, `Magnitude of a
   Vector`, `Unit Vector`, `Dot Product`, `Pythagorean Theorem`, `Right Triangle`, `Compound Units`,
   `Percent`) each fetched and confirmed live on 2026-08-15 (Khan Academy `x2` and `mathsisfun.com` `x5`,
   `purplemath.com` `x1` — all on the `T1-19` allowlist); a `HOWTO` array covering all five of the case's
   "how to…" questions by reference into the same 8 keys. **JS port of `sensitivity_model.py`**:
   `greatCircleNM`, `initialCourseDeg`, `windVectorKt`, `courseUnitVector`, `legSolution`,
   `routeSolution`, `tripFuel`, `minimumDispatchFuel`, `evaluate`, `evaluateTwist`,
   `breakEvenWindScale` — ported line-for-line, same `PARAMS`/`FLEX` keys and values. **Verified
   independently**: extracted the JS data/model block, ran it standalone under `node` against the same
   `PARAMS`, and diffed every leg's along-course/crosswind/ground-speed/fuel figure, both routings'
   trip fuel, the break-even percentage, the twist figures, and `evaluate()`'s output against the
   Python script's own printed output — **exact match to the digit** on every value (see this pass's
   tool transcript). The Working Notebook (Steps 1–5, covering D1–D5) lets a Hero pick any of the six
   real legs plus the two Twist-only legs, enter their own components/ground-speed/trip-fuel figures, and
   check them live against the ported model — never a pre-computed literal. The Twist section states the
   scenario in full (KMEM re-route) without stating a resulting number or naming a winner; the `applyTwist`
   checkbox reroutes Step 5's live check to `ROUTE_B_TWIST`, it does not print an answer.
4. **`python3 skills/case-readiness/scripts/tier1_structural.py --case wind-triangle --project .`**
   First run (before the HTML existed) already showed 0 BLOCKERs, 1 GAP (T1-16, hash not yet recorded —
   since resolved). This run, against the finished interactive HTML:

   | id | result | note |
   |---|---|---|
   | T1-01 … T1-17, T1-19 | PASS | — |
   | T1-18 | **GAP** | 24 numbers in the HTML's prose/markup (outside `<script>`) don't trace to `case.md`/`case.json`: `[1.4, 1.55, 1.6, 2.5, 3.4, 16.0, 22.0, 32.0, 34.0, 46.0, 48.0, 52.0]` — all SVG `viewBox`/path-coordinate and CSS decimals from the crest and wind-icon `<symbol>` markup (the shell's own accepted false-positive class per the contract doc, §7 — "CSS/SVG decimals... don't spend time trying to eliminate those"). **No leak finding** — the T1-18 leak-detector (which screens `margin_pct` and any `*_in_spec_*` literal, boundary-aware, across the whole file including `<script>`) reported clean; `1.67`, `0.64`, and the routing winner never appear anywhere in the file as static literals, only ever produced by live computation in `evaluate()`/`evaluateTwist()`/`tripFuel()` at click-time. |

   **BLOCKER (0). GAP (1) — T1-18, the accepted SVG/CSS decimal class.** POLISH (2): T1-02 (the `412`
   texture numeral, auto-classified and already recorded in `overview_numerals_cleared[]`), T1-07 (11
   Appendix G labels, all bulleted).

   **VERDICT: TIER1_PASS (0 blockers, 1 gap)** — unchanged from the prior run's blocker count; the GAP
   moved from T1-16 (now resolved) to T1-18 (a new, cosmetic, accepted-class finding introduced by
   building the HTML that did not exist before).

### Not re-run this pass

Tier 2 (six simulated-play probes) was already run and recorded in the 2026-08-12 entry above, with two
open findings (P1 NOT RUN, P2 FAIL) that keep this case below `TIER2_PASS`. Building the interactive HTML
does not change either finding — this pass did not re-run Tier 2, per the task scope (Tier 1 structural
gate only). **This case remains not publishable**: Tier 2's P2 (Argument A wins no measured metric) and
P1 (needs one genuinely fresh cold-solve dispatch) are unchanged and still open, per the 2026-08-12 entry.

### Next step

Same as recorded 2026-08-12: close P1 with a genuinely fresh solver against the de-leaked packet, and
make the stage-2 decision on P2 (retune the routing pair so Argument A is competitive on a measured
metric, or accept and record the one-sided balance). Tier 1 is clean and does not block that work.

---

## case-readiness run — 2026-08-15 (Tier 2 completion)

**State:** TIER1_PASS → **Tier 2 run to completion: 5 PASS, 1 FAIL → BLOCKED**

This pass re-confirmed Tier 1 clean and ran all six Tier 2 probes fresh against the case as it
stands today (i.e. *after* the six repairs (R1–R6) recorded in the 2026-08-12 entry — those
repairs were not re-applied, they were already present in `case.md`/`FACILITATOR.md`/
`case.json`). No further edits were made to the case; per the skill's "Never fix the case" rule,
none of the findings below were repaired by this pass.

### Tier 1 — structural (19 checks), re-confirmed

`python3 skills/case-readiness/scripts/tier1_structural.py --case wind-triangle --project .`

18 PASS, 1 GAP (T1-18 — 24 SVG/CSS decimals in the interactive HTML's crest/wind-icon markup,
the shell's own accepted false-positive class; no leak — `1.67`, `0.64`, and the routing winner
never appear as static literals, only produced by live computation), 0 BLOCKER. Unchanged from
the prior run. `case_md_sha256` confirmed current: `af61b473f6...38d0b729`.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent dispatch (dilemma packet only, no `FACILITATOR.md`/`case.json`/`QA_REPORT.md`) reached B (Southern Swing), named the correct metric (total trip fuel, not distance or raw wind speed), reproduced the wind-triangle arithmetic to within rounding for both routings (A 27,951 lb / B 27,347 lb vs. the case's own 28,228.9 / 27,756.2 lb — same ~473–605 lb gap and same ranking; the solver's own figures diverge slightly from the case's because it used a slightly different course-averaging convention, but it independently reproduced the qualitative and quantitative shape of the answer, including the ~20–26% break-even and the MA2-reversal robustness check), and got past the FROM/TOWARD sign trap (used the FROM-blows convention correctly throughout). It named the correct strongest-argument-against-B (forecast is a forecast, single 9-hour-window issuance) and the correct most-sensitive-assumption (MA2), matching the case's own disclosed fragility structure. Reached the intended answer for the intended reasons — PASS. |
| P2 both-sides | **FAIL** | See detail below. Argument A, even in its already-repaired, honestly-reframed form ("the difference is small enough I'd rather not pay 136 certain miles for it"), collapses under a direct follow-up the case's own numbers force: *"If you distrust the forecast, which routing's fuel cost is actually more exposed to it being wrong?"* — Routing A's, by the case's own 0×–1.5× wind-scaling table (A ±12.4%, B ±0.3%). A's proponent cannot answer that question without conceding B is the lower-variance choice, which contradicts the premise that A is the "safer" plan. Argument A's remaining fallback — "a 20.5%/7.2 kt same-direction forecast error is not unusual" — has no supporting source in the case (no historical forecast-error-rate figure anywhere in Appendix F); it is asserted, not evidenced. This is a real content finding, unchanged in substance from the 2026-08-12 run: it is **not** cleared by R4's reframing, because reframing the argument's wording does not give it a metric to win or evidence for its one remaining premise. |
| P3 trap | **PASS** | Fresh read of `case.md`'s student-facing text (Appendix B's FROM/TOWARD convention, Appendix A's course/distance tables) surfaces the same three traps `FACILITATOR.md` now names: (1) comparing raw wind speed instead of the along-course component (fails at KSLC, 42 kt wind → only −13.4 kt along-course); (2) comparing distance flown instead of time aloft; (3) the FROM/TOWARD sign inversion, which flips every along-course sign and hands Routing A a wide, confident, spurious win with fully self-consistent-looking arithmetic. All three are named in `FACILITATOR.md`'s "The trap" section with the correct tell for each, including the third trap's specific tell ("a D3 table whose signs say the jet stream is helping a westbound flight") that the first trap's diagnostic cannot catch. Guide and independent read match. |
| P4 twist | **PASS** | (1) Invalidates a held position: yes, mechanically — Routing B re-filed via KMEM burns 28,410.4 lb vs. Routing A's 28,228.9 lb, reversing the base verdict, using only numbers already published in Appendix A (KMEM's position) and Appendix B (KMEM's wind), no new constant introduced. (2) Survives the case's own stated assumptions read a student's way: yes, as currently written — MA5 (the course/distance convention) is now written into Appendix E and the twist flips under all four defensible readings of it (initial course, mean course, final course, true rhumb line), by margins from 0.64% down to 0.08%. The twist's conditionality on MA2 (it does *not* flip at MA2's low end, 0.75% southern allowance — B stays cheaper by 0.10%) is explicitly disclosed in `case.md`'s facilitator-only "twist's flip is itself conditional" paragraph and in `FACILITATOR.md`. No undisclosed dependency found. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case wind-triangle --probe 5 --flex 0.5` — mechanical result: 0 probes FAILED. `FLEX[]` = the four declared assumption dials (`airway_allowance_a_pct`, `airway_allowance_b_pct`, `fuel_density_lb_per_gal`, `departures_per_year`); all four are genuine author-chosen assumptions (MA1/MA2/MA4), not cited data, per the FLEX-scoping doctrine — confirmed by inspection, no scoping bug. Base: A 28,228.95 (transformed), B 28,701.72 (transformed) → winner B, margin 1.7%, matching `case.md`'s own 1.67%. All 8 one-at-a-time ±50% sweeps: winner stays B, margin range 0.9%–2.4%, no flips, no breach of the SPEC §2 20% cap. Mechanically stable — no disclosure needed beyond what `case.md` and `FACILITATOR.md` already state (and already over-state, having also swept the joint MA2 corners and all four MA5 course conventions). |
| P6 data decay | **PASS** | All 7 `sources[]` URLs fetched live this pass. S1 (KJFK/KABQ/KBUF/KDEN/KLIT positions): exact match. S2 (KSFO/KDBQ/KMEM/KSLC/KSGF positions): exact match. S3 (FD3US3, issued 122001Z, valid 130600Z, all 10 coded 34,000 ft groups): exact match to Appendix B character for character, confirming the pinned-permalink URL correctly serves the cited issuance (the earlier `e=`-ignoring URL was already replaced by R6). S4 (B738 TAS 460 kt, Mach 0.79, ceiling FL410): exact match. S5 (40.1 kg/min en-route narrow-body fuel burn, Table 6.1): exact match. S6 (14 CFR 121.639, 45-minute reserve): exact match. S7 (EIA Gulf Coast jet fuel spot, July 2026 = $3.403/gal, no August 2026 value yet): exact match, confirming R6's correction of Appendix D's earlier false August-2026 claim. No dead links, no drifted figures, none over the 365-day flag (all accessed same-day). |

**Detail — P2 both-sides, why this is a FAIL and not a re-litigation of an already-fixed problem.**
The 2026-08-12 pass's R4 repair replaced a *factually backwards* framing ("A is the certain/safe
plan") with an *honest* one ("the difference is small enough I'd rather not pay 136 certain
miles for it") and added the exposure table (A ±12.4% vs B ±0.3%) to `case.md`'s facilitator
half. That repair was necessary and is not in question. But P2 tests whether the resulting
argument for A survives interrogation, and it still does not: once the exposure table is on the
table, the honest version of Argument A no longer claims A is safer — it concedes B is the lower-
variance choice — and instead rests entirely on the unevidenced premise that "136 certain nm"
outweighs "an expected 473 lb saving with some forecast risk attached." The case supplies no
basis (no cited forecast-error distribution, no stated risk tolerance, no dollar value assigned
to variance) for weighing those against each other, so a Hero arguing A has nothing left to
stand on once asked to defend that trade explicitly. **This is unchanged from the 2026-08-12
finding in substance** — same collapse point, same missing evidence — confirmed independently
today rather than carried forward uncritically.

**What would close this (stage-2 decision, not a QA fix, per the skill's "never fix the case"
rule):** either (a) retune the routing pair so Routing A is genuinely competitive on a measured
metric under the published wind field — the case's own analysis already found simply reversing
MA2's asymmetry moves the *wrong* way (widens B's lead to 2.64%), so this requires a different
routing pair, a re-sourced wind field, or a materially different southern-corridor allowance, all
of which are `case-write`/`case-research` work; or (b) accept the case as a legitimately
one-sided decision under the published data and rewrite the Dilemma/Challenge framing so the
Hero's task is explicitly to argue *why* a smaller, evidenced or well-reasoned risk premium could
still justify A, rather than leaving Argument A resting on an unsupported "not unusual" claim.

### Tier 3 — human dry-run

**NOT RUN.** Not reachable: Tier 3 requires `PUBLISHED`, which requires `TIER2_PASS`, which this
case does not have.

### Verdict

**BLOCKED.** Tier 1 is clean (0 blockers, 1 accepted GAP). Five of six Tier 2 probes PASS (P1,
P3, P4, P5, P6). **P2 both-sides FAILs**, and per the skill's own rule ("Never mark `TIER2_PASS`
with a probe recorded as `NOT RUN` [or FAIL]") this case cannot reach `TIER2_PASS` until P2 is
resolved. This is a real content finding carried over from 2026-08-12, re-verified independently
today, not a stale or superseded one.

### Next step

Stage 2 (`case-write`/`case-research`) makes the P2 call above — retune the routing pair/data so
Argument A has a real metric or a supported risk premium to stand on, or deliberately reframe the
Dilemma as an evidenced one-sided decision — then re-run P2 (the other five probes do not need
re-running unless the fix touches their inputs). This case remains **not publishable**.

---

## case-readiness run — 2026-08-17 (full Tier 2 re-run, all six probes)

**State:** TIER1_PASS (re-confirmed) → **Tier 2 re-run: 5 PASS, 1 FAIL → BLOCKED (unchanged)**

`case.md`, `case.json`, `FACILITATOR.md` and `sensitivity_model.py` are byte-identical in content
to the 2026-08-15 run (`case_md_sha256` unchanged: `af61b473f60d67db43b1233731...38d0b729`; this
directory is untracked in git, so there is no commit history to diff against, but the file content
matches the 2026-08-15 QA entry verbatim). No stage-2 repair has landed since. This pass re-ran
all six Tier 2 probes independently rather than carrying forward the prior verdicts, per the task
brief, and reports what it found — which is the same substantive result via independent evidence,
not a copy of the prior report.

### Tier 1 — structural (19 checks), re-confirmed

`python3 skills/case-readiness/scripts/tier1_structural.py --case wind-triangle --project .`

18 PASS, 1 GAP, 0 BLOCKER.

| id | result | note |
|---|---|---|
| T1-01 … T1-17, T1-19 | PASS | — |
| T1-18 | GAP | 23 numbers in the interactive HTML's prose/markup outside `<script>` don't trace to `case.md`/`case.json` — all SVG `viewBox`/path-coordinate and CSS decimals in the crest/wind-icon `<symbol>` markup, the shell's own accepted false-positive class (`INTERACTIVE_HTML_CONTRACT.md` §7). No leak: `1.67`, `0.64`, and the routing winner never appear as static literals anywhere in the file, only produced by live computation in `evaluate()`/`evaluateTwist()`/`tripFuel()`. |

POLISH (2): T1-02 (`412`, cleared texture numeral), T1-07 (11 Appendix G labels, all bulleted).
`case_md_sha256` confirmed current. **VERDICT: TIER1_PASS.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh dispatch (dilemma packet only). Chose **B — The Southern Swing**; named the correct primary metric (total trip fuel cost in dollars / trip fuel burn, on the reasoning that reserve fuel is identical on both routings and trip fuel is the only lever route choice actually pulls). Independently re-derived every leg's wind components, course unit vectors, along-course/crosswind dot products, ground speeds and times using the correct FROM/TOWARD 180° convention throughout (no sign-inversion trap taken): Routing A 5.322 h / 28,232 lb, Routing B 5.233 h / 27,755 lb — matches the case's own 28,228.9 lb / 27,756.2 lb to within rounding (different intermediate rounding, same ranking and ~470–480 lb gap). Computed a break-even of ~20–25% forecast overstatement (case: 20.5%/7.21 kt) as the strongest argument against B, and named MA2 (the airway-structure allowance split) as the least-supported, most-sensitive stated number — both match the case's own disclosed fragility structure exactly. Correctly identified the unused corridor-file waypoint table as scenario texture carrying no arithmetic weight. Reached the intended answer, by the intended route, for the intended reasons — **PASS** per the skill's own criterion (right answer for the right reasons; wrong route to the right answer would have been a FAIL). |
| P2 both-sides | **FAIL** | See detail below. Unchanged in substance from the 2026-08-12 and 2026-08-15 findings, reconstructed independently today rather than carried forward. |
| P3 trap | **PASS** | Read `case.md`'s student-facing text only (through the `<!-- FACILITATOR ONLY -->` marker at line 268; nothing after it was used to name the trap). Appendix B's FROM/TOWARD convention statement ("a wind from 300 at 78 knots... is moving toward 120°") is the exact mechanism a solver can miss: resolving `307843`-style groups into components without the 180° reversal flips the sign of every along-course figure and hands Routing A a wide, self-consistent-looking, entirely spurious win. This is the same trap `FACILITATOR.md`'s "The trap" section names third, with the same tell ("a D3 table whose signs say the jet stream is helping a westbound flight"), plus the two secondary traps (raw wind speed vs. along-course component; distance vs. time aloft) — also present and also named. Independent read and guide match on all three; the guide's stated diagnostic-blind-spot claim (trap 1's tell cannot catch trap 3, because a sign-inverted table has correct magnitudes) checks out arithmetically: KDBQ inverted reads +74.8 kt tailwind with the same 78 kt magnitude as the correct −74.8 kt headwind. |
| P4 twist | **PASS** | (1) Invalidates a held position: yes, mechanically confirmed by re-running `sensitivity_model.py`'s `evaluateTwist()` — Routing B re-filed via KMEM burns 28,410.4 lb against Routing A's 28,228.9 lb, reversing the base verdict, using only already-published Appendix A/B data (KMEM position and wind), no new constant. (2) Survives the case's own stated assumptions read a student's way: yes, as currently written. MA5 (leg geometry: initial course + great-circle distance) is present in Appendix E (not missing, as it was in the 2026-08-12 pre-repair state) and the twist flips under all four defensible readings of it, by margins from 0.64% down to 0.08% (re-verified: `case.md` Appendix E's own P4 table). The twist's conditionality on MA2 — it does *not* flip at MA2's low end (0.75% southern allowance, B stays cheaper by 0.10%) — is disclosed in `case.md`'s facilitator-only "twist's flip is itself conditional" paragraph (line 315) and in `FACILITATOR.md`'s twist section (line 144). No undisclosed dependency found. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case wind-triangle --probe 5 --flex 0.5` — mechanical result: 0 probes FAILED. `FLEX[]` = `airway_allowance_a_pct`, `airway_allowance_b_pct`, `fuel_density_lb_per_gal`, `departures_per_year` — all four genuine author-chosen assumption dials (MA1/MA2/MA4), not cited/given data; confirmed by inspection against the FLEX-scoping doctrine, no scoping bug (sourced figures — waypoint positions, forecast winds, cruise performance, the reserve rule, fuel price — sit in `PARAMS` but are correctly excluded from `FLEX[]`). Base: A 28,228.95 lb, B 28,701.72 lb (transformed metric) → winner B, margin 1.7%, matching `case.md`'s 1.67%. All 8 one-at-a-time ±50% sweeps: winner stays B, margin range 0.9%–2.4% (`airway_allowance_a_pct` −50%→1.2%, +50%→2.2%; `airway_allowance_b_pct` −50%→2.4%, +50%→0.9%; `fuel_density`/`departures_per_year` exactly neutral, as MA1/MA4 claim). No flips, no breach of the SPEC §2 20% cap. Mechanically stable — **PASS**, not `PASS_DISCLOSED`; no undisclosed instability to flag on the base verdict (the case's real fragility — twist conditionality, and the cited-wind-data break-even — is disclosed elsewhere and is P4's/P6's territory respectively, not P5's). |
| P6 data decay | **PASS** | All 7 `sources[].url` entries fetched live today. **S1** (KJFK/KBUF/KDEN/KLAX/KLIT/KABQ positions, aviationweather.gov API): exact match. **S2** (KSFO/KDBQ/KMEM/KSLC/KSGF positions, same API): exact match. **S3** (FD3US3, pinned permalink `e=202608122001`): raw product text fetched directly (`curl`, not the AI-summarized WebFetch, which initially misread the fixed-width column alignment and reported the 39000 ft column instead of 34000 ft — caught and corrected by re-parsing the raw `<pre>` block against the product's own `FT 3000 6000 9000 12000 18000 24000 30000 34000 39000` header). Confirmed issuance 122001Z / valid 130600Z / data based 121800Z, and all ten 34,000 ft coded groups match Appendix B character for character: JFK 287047 · BUF 317547 · DBQ 307843 · DEN 211141 · SLC 204244 · SGF 341441 · MEM 351741 · LIT 030741 · ABQ 280940 · SFO 151345. **S4** (EUROCONTROL B738: TAS 460 kt, Mach 0.79, ceiling FL410): exact match. **S5** (EUROCONTROL Standard Inputs, Table 6.1, en-route narrow-body 40.1 kg/min, B738 named in the segment): exact match. **S6** (14 CFR 121.639, 45-min reserve, confirmed at both eCFR and Cornell LII): exact match. **S7** (EIA Gulf Coast jet fuel spot, July 2026 $3.403/gal, August 2026 cell still empty): exact match. No dead links, no drifted figures, all fetched same-day (0 days old, none over the 365-day flag). |

**Detail — P2 both-sides, independent reconstruction.**

*Best case for B, from the packet alone:* trip fuel 27,756.2 lb vs. 28,228.9 lb (B cheaper by
472.8 lb / 1.67%), B is also 5.3 minutes faster and requires 472 lb less minimum dispatch fuel,
despite flying 136.4 nm further — "fuel is bought by the hour, not by the mile."

*Best case for A, from the packet alone:* Routing A's certain 136.4 nm/6.0% distance saving is
real regardless of the forecast; the break-even is a uniform 20.5% overstatement (7.21 kt/leg) of
the forecast headwind, which is not an extreme error for a forecast issued ~10 hours before the
valid window; "I would rather bank the certain distance than trust a single forecast issuance by
that much."

*Where Argument A collapses, and at exactly which question:* **"If you distrust the forecast,
which routing's fuel cost is actually more exposed to it being wrong?"** Scaling the entire
published wind field from 0× to 1.5× (mechanically re-derived from `sensitivity_model.py`'s
`PARAMS`, not merely quoted from the case) moves Routing A's trip fuel by 3,489 lb (+12.4%) and
Routing B's by only 86 lb (+0.3%) — Routing A is the routing whose cost is forecast-dependent,
because Routing A is the one with the large winds in it. A becomes cheaper only below ≈0.80× (the
whole field overstated by roughly a fifth, in one specific direction; a symmetric error the other
way makes A worse still). Once this is on the table, Argument A cannot claim to be the
lower-variance or "safer" plan — every one of the case's own measured quantities (trip fuel, block
time, minimum dispatch fuel, fuel per nm of net progress) already favors B, so Argument A has no
metric left to win. Its one remaining premise — that a 20.5%/7.2 kt same-direction forecast error
is "not unusual" for an upper-wind forecast this far out — has no supporting source anywhere in
Appendix F: no cited forecast-error-rate figure, no historical verification statistic, nothing.
Argument A is left resting entirely on an asserted, unevidenced premise, which is exactly the
"reads as a concession" failure mode the probe's machine pre-screen exists to catch, surfaced here
by the follow-up question instead.

**Why this is unchanged, not re-litigated.** This is the third independent run to reach this
finding (2026-08-12 original; 2026-08-15 Tier-2-completion re-run; this run) against unmodified
case content. The case's own already-honest framing of Argument A (`case.md` facilitator half,
line 302–313; `FACILITATOR.md` deep-conflict thread 1) already concedes the exposure asymmetry —
it does not hide it — but conceding the asymmetry is precisely what leaves Argument A without a
metric or an evidenced premise. This is a real, stable content property of the case as scoped, not
noise.

**What would close this (stage-2 decision, `case-write`/`case-research`, not a QA fix):** (a)
retune the routing pair or the wind/allowance data so Routing A is genuinely competitive on a
measured metric under the published field — the case's own sensitivity work already shows
reversing MA2's asymmetry moves the wrong way (widens B's lead to 2.64%), so this needs a
different routing pair, a re-sourced wind field, or a materially different southern allowance; or
(b) accept the case as a legitimately one-sided decision under the published data and reframe the
Dilemma/Challenge language so a Hero's task is explicitly to construct and evidence a risk premium
for A, rather than leaving Argument A to rest on an unsupported "not unusual" claim.

### Tier 3 — human dry-run

**NOT RUN.** Not reachable: Tier 3 requires `PUBLISHED`, which requires `TIER2_PASS`, which this
case does not have.

### Verdict

**BLOCKED.** Tier 1 clean (0 blockers, 1 accepted GAP — T1-18's SVG/CSS decimal class). Tier 2:
five of six probes PASS (P1, P3, P4, P5, P6); **P2 both-sides FAILs**, independently reconfirmed
today with fresh arithmetic and a fresh collapse-point derivation rather than carried forward.
Per the skill's own rule, a single Tier 2 FAIL keeps the case below `TIER2_PASS` regardless of the
other five verdicts. `case.json.qa` updated below; no case content was modified by this pass
(read-only per the skill's "never fix the case" rule).

### Next step

Unchanged: stage 2 (`case-write`/`case-research`) makes the P2 call — retune Routing A onto a
winnable metric or give it a sourced risk premium, or deliberately reframe the Dilemma as an
evidenced one-sided decision — then re-run P2 only (the other five probes do not need re-running
unless the fix touches their inputs, per the standard partial-re-run rule). This case remains
**not publishable**.

---

## case-write stage-2 fix — 2026-08-17 (P2 remediation)

**Applied by:** a `case-write`-scoped fix pass responding to the 2026-08-17 Tier 2 run's P2 FAIL
(three independent confirmations: 2026-08-12, 2026-08-15, 2026-08-17). This is a content fix, not
a QA run — it does not itself re-verify the probes.

### What was tried

1. **Real-data research for a sourced counter to Argument A.** Searched for FAA/NWS/AMS
   verification data on winds-aloft forecast accuracy, jet-stream forecast-error direction/bias,
   and diversion/turbulence-rate statistics by route type.
   - Historical winds-aloft forecast **uncertainty magnitude** (±15 kt at issuance, growing to
     ~25–30 kt across a 12-hour validity window) turned up only in a US patent's background
     section (`US5051750`) — not an authoritative verification study, and not used.
   - A genuinely usable source was found: **Schäfler et al. 2020, *Monthly Weather Review* 148(7),
     "Observation of Jet Stream Winds during NAWDEX and Characterization of Systematic
     Meteorological Analysis Errors"** (DOI `10.1175/MWR-D-19-0229.1`) — peer-reviewed, AMS-
     published, documents individual-case jet-stream-level wind-speed errors up to **±10 m/s
     (≈19.4 kt)** in NWP analyses/short-range forecasts, several times the case's 7.2 kt/leg
     break-even. It verifies a different jet and forecast system (North Atlantic, ECMWF/UK Met
     Office) than the NWS FD product this case cites, so it is disclosed as general evidence of
     documented error magnitude, not a measurement of this issuance's own error.
   - Search also surfaced evidence that cuts the **other** way: multiple sources note that upper
     tropospheric jet-core wind speeds tend to be **systematically underforecast** (a negative
     bias), which — if it applied to this issuance — would make Routing A's actual headwind worse
     than forecast, not better. This was not incorporated as a counter-argument for A (it argues
     against A), and is recorded here for the same reason the rest of this pass avoids
     cherry-picking: an honest search does not always turn up support for the side you are looking
     to help.
2. **Real routing-geometry exploration**, using only real, already-sourced or easily-sourceable
   waypoints/winds (KDEN's position and its published 210/11 kt wind were already in Appendix
   A/B's corridor-file table). Computed trip fuel for JFK→DEN→SFO and five other real waypoint
   combinations using `sensitivity_model.py`'s own functions. **Result: any routing through Denver
   dominates BOTH original options on every metric** (JFK-DEN-SFO: 2,270.1 nm filed, 26,209.3 lb —
   cheaper than both A's 28,228.9 lb and B's 27,756.2 lb, despite being almost as short as the
   original Great Circle). A dominant third route is not a fix — it destroys the dilemma rather
   than balancing it, and swapping Option A onto a Denver-routed track would also contradict the
   Overview's own framing of Option A as the track that runs "directly into the ribbon of wind."
   This redesign path was tried and rejected; **no routing change was made.**

### What was applied

Gave Argument A a real, sourced, quantitative basis for its one previously-unevidenced premise
(that a 20.5%/7.2 kt same-direction forecast error is "not unusual"), **without reinstating the
already-corrected "A is safer" framing**, which stays wrong and stays corrected. Argument A's
honest form is now: *the 472.8 lb / 1.67% margin sits inside a documented noise band* (S8), not
*Routing A is the lower-variance choice* (it is not — the 0×–1.5× exposure asymmetry, A ±12.4% vs
B ±0.3%, is unchanged and still disclosed).

* `case.md` Appendix F — added **S8** (Schäfler et al. 2020), confidence MEDIUM, with an explicit
  caveat that it verifies a different jet/forecast system than S3.
* `case.md` facilitator-only tail — rewrote "Argument for A" and the "which plan is actually
  exposed" paragraph to cite S8 and state the noise-floor framing instead of the unsupported
  "not unusual" assertion.
* `FACILITATOR.md` — rewrote deep-conflict thread 1's "defensible form of Argument A" to match.
* `case.json.sources[]` — added the S8 entry (same fields/confidence as `case.md`).
* `case.json.balance.argument_a` — rewritten to match the new, evidenced argument.
* `cases/wind-triangle/published/Wind Triangle - Interactive.html` — added S8 to both the Appendix
  F table and the footer source list; updated the embedded `case.md` sha256 comment.
* `case.json.qa.case_md_sha256` updated to the new hash (`f8309369bd...47c2`); `qa.tier2.P2`
  annotated as "fix applied, not yet re-verified" rather than left as a stale FAIL description.

**No number that decides the verdict was touched.** `margin_pct` (1.67), every figure in
`case.json.derived`, and `sensitivity_model.py`'s code are all unchanged — this fix adds evidentiary
support to an argument, it does not retune the case.

### Tier 1 — re-run after the fix

`python3 skills/case-readiness/scripts/tier1_structural.py --case wind-triangle --project .`

**18 PASS, 1 GAP (T1-18, the accepted SVG/CSS-decimal class in the interactive HTML's crest
markup — unchanged, pre-existing), 0 BLOCKER. VERDICT: TIER1_PASS.**

### Next step

This pass does not itself clear P2 — per the skill's own rule, only a fresh Tier 2 probe run can
do that. **P2 should be re-run** against the new S8-backed argument: does "the margin sits inside a
documented noise band" survive interrogation better than "B's benefit is uncertain" did? A likely
follow-up a solver will raise: S8 verifies a *different* jet stream and forecast system, so its
±10 m/s figure is suggestive, not dispositive, for this specific FBUS33 issuance — the probe should
test whether that gap is fatal or merely a disclosed limitation. The other five Tier 2 probes (P1,
P3, P4, P5, P6) do not need re-running; none of their inputs changed.

## case-readiness run — 2026-08-17 (P2 re-verification, full six-probe close-out)

**State:** TIER1_PASS → **TIER2_PASS**

This pass re-confirms Tier 1, accepts the fresh cold-solve (P1) result supplied for this run, and
independently re-verifies P2–P6 against the case content as it stands after the S8 stage-2 fix
(`case_md_sha256 = f8309369bd...47c2`, unchanged since 2026-08-17's fix pass — confirmed by
recomputing the hash this run). No case content was modified by this pass.

### Tier 1 — structural (19 checks), re-confirmed

`python3 skills/case-readiness/scripts/tier1_structural.py --case wind-triangle --project .`

18 PASS, 1 GAP (T1-18 — 24 SVG/CSS-decimal numbers in the interactive HTML's crest/wind-icon
markup, the shell's own accepted false-positive class; no leak, `1.67`/`0.64`/the routing winner
never appear as static literals), 0 BLOCKER. Unchanged. **VERDICT: TIER1_PASS.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent dispatch (packet-only, no `FACILITATOR.md`/`case.json`/`QA_REPORT.md`) chose **B — The Southern Swing**; named the correct optimized metric (D5, lb of fuel per nm of net progress vs. the 2,241.8 nm KJFK–KSFO direct reference); independently re-derived the headwind components with the correct FROM/TOWARD 180° convention on all six legs (KDBQ ≈−74.8 kt, KSLC ≈−13.4 kt, KSFO ≈+2.7 kt on A; ≈−3.3, −8.6, +9.4 kt on B) — the sign-inversion trap was not taken; identified the sensitivity structure (MA2 dominant, base verdict stable 0.95%–2.40% across the full MA2 range, widening to 2.64% on reversal) matching `case.json.derived`/`sensitivity_model.py` exactly. Right answer, right route, right metric named — **PASS** per the skill's own criterion. |
| P2 both-sides | **PASS** (reversed from the three prior FAILs, post S8-fix) | See detail below. The stage-2 fix (S8, Schäfler et al. 2020) closes the specific defect all three prior runs found (Argument A's "not unusual" premise was unevidenced) without reinstating the already-corrected backwards "A is safer" framing. |
| P3 trap | **PASS** | Independent read of `case.md`'s student-facing text (through the `<!-- FACILITATOR ONLY -->` marker only) surfaces all three traps `FACILITATOR.md`/case.md's facilitator tail name: raw wind speed vs. along-course component (fails at KSLC: 42 kt wind → −13.4 kt along-course), distance flown vs. time aloft, and the FROM/TOWARD sign inversion (Appendix B's own from-blows statement is the exact mechanism; KDBQ inverted reads +74.8 kt tailwind, same 78 kt magnitude as the correct −74.8 kt headwind, confirming the guide's claim that trap 1's diagnostic cannot catch trap 3). Independent read and guide match on all three, each with its own stated tell. |
| P4 twist | **PASS** | (1) Invalidates a held position: yes, mechanically confirmed by re-running `sensitivity_model.py` — Routing B re-filed via KMEM burns 28,410.4 lb against Routing A's 28,228.9 lb, flipping the base verdict, using only already-published Appendix A/B data (KMEM position and its 350/17 wind), no new constant. (2) Survives the case's own stated assumptions read a student's way: yes. MA5 (leg geometry: initial course + great-circle distance) is present in Appendix E, and the flip survives all four defensible readings of it (0.64% down to 0.08%). The flip's conditionality on MA2 — it does *not* flip at MA2's low end (0.75% southern allowance, B stays cheaper by 0.10%) — is disclosed in both `case.md`'s facilitator-only tail and `FACILITATOR.md`'s twist section. No undisclosed dependency. |
| P5 sensitivity | **PASS** | `python3 skills/case-readiness/scripts/tier2_probes.py --case wind-triangle --probe 5 --flex 0.5` — mechanical result: 0 probes FAILED. `FLEX[]` = `airway_allowance_a_pct`, `airway_allowance_b_pct`, `fuel_density_lb_per_gal`, `departures_per_year` — all four genuine author-chosen assumption dials (MA1/MA2/MA4), correctly excluding cited/sourced data (positions, winds, cruise performance, reserve rule, fuel price) per the FLEX-scoping doctrine. Base: A 28,228.95 lb, B 28,701.72 lb (transformed metric), winner B, margin 1.7% (matches `case.md`'s 1.67%). All 8 one-at-a-time ±50% sweeps: winner stays B, margin range 0.9%–2.4%, no flips, no breach of the SPEC §2 20% cap. Mechanically stable — **PASS**, not `PASS_DISCLOSED`. |
| P6 data decay | **PASS** | All 8 `sources[].url` entries fetched live this pass (S1–S7 via WebFetch/curl; S8 added by the 2026-08-17 fix and fetched for the first time this run). **S1/S2** (airport positions, aviationweather.gov): exact match to Appendix A. **S3** (FD3US3, pinned permalink `e=202608122001`): fetched raw product text directly via `curl` (not the AI-summarized WebFetch, which the 2026-08-17 Tier-2 run found misreads the fixed-width columns) — confirmed issuance 122001Z/valid 130600Z/data based 121800Z, and all ten 34,000 ft coded groups match Appendix B character for character: JFK 287047 · BUF 317547 · DBQ 307843 · DEN 211141 · SLC 204244 · SGF 341441 · MEM 351741 · LIT 030741 · ABQ 280940 · SFO 151345. **S4** (EUROCONTROL B738: TAS 460 kt, Mach 0.79, ceiling FL410): exact match. **S5** (EUROCONTROL Standard Inputs Table 6.1: 40.1 kg/min en-route narrow-body, B738 named): exact match. **S6** (14 CFR 121.639(c), 45-min reserve): exact match. **S7** (EIA Gulf Coast jet fuel spot: July 2026 $3.403/gal, August 2026 cell empty): exact match. **S8** (Schäfler et al. 2020, *Monthly Weather Review* 148(7), DOI `10.1175/MWR-D-19-0229.1`): DOI resolves (redirects to the AMS journal page, which 403s to automated fetch — verified instead via Crossref metadata (title/authors/journal/year all match `case.json`'s S8 entry exactly) and Semantic Scholar's indexed abstract, which states verbatim: *"large and spatially coherent wind errors up to ±10 m s⁻¹ for individual cases, with the strongest errors occurring above the tropopause in upper-level ridges"* in "analyses and short-term forecasts" — this matches `case.md` Appendix F/facilitator-tail's citation of S8 exactly, including the ±10 m/s figure, the "upper-level ridge" structure, and the "short-range forecasts" framing; the abstract also independently confirms the case's own honesty about S8's limits — it reports the *systematic bias* is small (−0.41/−0.15 m/s) and the large errors are an *individual-case* phenomenon, which is exactly how `case.md` presents it (a documented magnitude of possible error, not a claim that this specific forecast is wrong). No dead links, no drifted figures; S1–S7 all 0 days old at original access (2026-08-12/17), S8 0 days old (2026-08-17); none over the 365-day flag. |

#### P2 both-sides — detail

*Best case for B, from the packet alone:* trip fuel 27,756.2 lb vs. 28,228.9 lb (B cheaper by
472.8 lb / 1.67%), 5.3 minutes faster, 472 lb less minimum dispatch fuel, despite 136.4 nm further
— "fuel is bought by the hour, not by the mile." B wins every metric the case measures: trip fuel,
block time, minimum dispatch fuel, lb/nm of net progress (12.381 vs 12.592).

*Best case for A, after the S8 fix:* Routing A's 136.4 nm / 6.0% distance saving is certain
regardless of the forecast; the break-even is a uniform 20.5% overstatement (7.2 kt/leg) of the
forecast headwind. That is no longer an unsupported "not unusual" assertion — Schäfler et al. 2020
(S8), a peer-reviewed *Monthly Weather Review* verification study, documents individual-case
jet-stream-level wind errors up to ±10 m/s (≈19.4 kt) in NWP analyses and short-range forecasts,
concentrated in the exact upper-level-ridge structure that produces this case's own strongest
winds — several times the case's own 7.2 kt break-even. Argument A's defensible form is therefore
"the 472.8 lb margin sits inside a documented noise floor for this class of forecast, and a single
12-hour-old issuance is not solid ground to spend 136 certain miles chasing it," not "B's benefit
is uncertain" (which would falsely claim A is lower-variance).

*Interrogation — where each side is pushed, and whether either collapses.*

Pushed on B: *"If you distrust the forecast, which routing's cost is actually more exposed to it
being wrong?"* — the case's own text (`case.md` facilitator tail, `FACILITATOR.md` thread 1)
already discloses the answer (A: ±12.4% vs B: ±0.3% across a 0×–1.5× wind-field scale) **before**
a room can spring it as a gotcha. B does not collapse here; it has an additional, stronger answer
available: the case's own P5 sensitivity sweep already stress-tested the base verdict against
±50% swings on every stated assumption dial (margin holds 0.46%–2.88% across the full range,
including the joint MA2 corners) — B's advantage survives assumption uncertainty on its own
terms, independent of whether S8's magnitude applies to this specific issuance.

Pushed on A: *"S8 verifies a different jet (North Atlantic) and a different forecast system
(ECMWF/Met Office), not the domestic NWS FD3US3 product this case cites — do you have any
evidence this specific issuance is off by 7.2 kt, or is this an analogy from elsewhere?"* — A's
proponent must concede no direct measurement of this issuance's own error exists; the case says so
itself (`case.md`: *"not a direct measurement of this issuance's error"*). This is a real,
disclosed limitation, but it does not collapse the argument the way an unsupported assertion did
in the 2026-08-12/15/17 findings: S8 is on-topic (the same physical phenomenon — upper-tropospheric
jet-stream wind analysis/forecast error), independently verified this run (Crossref + Semantic
Scholar abstract match the case's citation exactly, including the ±10 m/s figure and the
short-range-forecast framing), and the honest disclosure of cross-system limits is itself evidence
the case is not overclaiming. A's remaining position — "forecasts of this exact physical
phenomenon are documented to carry individual-case errors several times our break-even, so I do
not trust this margin to the precision it would need" — survives the follow-up as a bounded,
evidenced claim rather than a bare assertion.

**Neither side collapses.** B retains every measured-metric win and a mechanically-verified
robustness result (P5); A now has real, on-topic, independently-verified peer-reviewed evidence
for its one previously-unsupported premise, with its cross-system limitation disclosed rather than
hidden. This is a genuine, defensible balance — the specific defect the prior three runs found
(Argument A's central claim was asserted, not evidenced) is closed by S8, and closing it did not
reopen the previously-fixed "A is safer" framing error. **PASS.**

### Tier 3 — human dry-run

**NOT RUN.** Reachable now that `TIER2_PASS` is recorded — Tier 3 requires `PUBLISHED`
(`case-publish`'s human-confirm gate), which has not yet run.

### Verdict

**TIER2_PASS.** Tier 1 clean (0 blockers, 1 accepted GAP). All six Tier 2 probes PASS: P1, P2, P3,
P4, P5, P6. This is the first run in this case's QA history to clear P2 — closed by the 2026-08-17
S8 stage-2 fix, verified independently against three lines of evidence this pass did not have
before (Crossref metadata, Semantic Scholar's indexed abstract, and a fresh both-sides
interrogation) rather than accepted on the fix pass's own say-so.

### Next step

**Run `case-publish` on `wind-triangle`.** Tier 1 + Tier 2 are both clean, which is what licenses
`case-publish`'s gate (`qa.state == "TIER2_PASS"`). Tier 3 (human dry-run) is not required for
`PUBLISHED` but will be needed before this case can be marked ✅ in `DOCTRINE_LEDGER.md`.
