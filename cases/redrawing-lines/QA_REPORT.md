# QA_REPORT — redrawing-lines ("Redrawing Lines")

## case-readiness run — 2026-08-18 — three open author decisions resolved

**State:** TIER2_PASS → **TIER2_PASS** (unchanged; all three previously-open author decisions from
the 2026-08-12 run are now closed, not just disclosed) · **Verdict:** TIER2_PASS
**case.md sha256:** `df7a285e9883f3c1041fe0e1acb5dba5c0efd37f3833d8c393e1ebfd408c0f14`
**Model:** `cases/redrawing-lines/sensitivity_model.py` (unchanged; still self-tests clean)

This run was explicitly instructed to make real, documented calls on the three items the
2026-08-12 report handed to a human, not to describe options again. All three are resolved below.

### Issue 1 — MA5, the water-boundary convention

**The two readings, arithmetic shown.** `crossings()` in `sensitivity_model.py`: the Kennebec
Split's district line runs along the Hancock–Knox border (Hancock lands in the northern district,
Knox in the southern); The Hancock Line's does not (both counties sit in the southern district).

| Reading | A (Kennebec Split) | B (Hancock Line) | Margin |
|---|---|---|---|
| **Counted** — all 34 Appendix B borders, water included | 9 borders + 1 severance = **10** | 11 borders, no severance = **11** | (11−10)/10 = **10.0%**, A wins |
| **Excluded** — Hancock–Knox dropped | 8 borders + 1 severance = **9** | 11 borders, no severance = **11** | (11−9)/9 = **22.2%**, A wins, past the SPEC §2 cap |

**Decision: COUNTED is the correct reading, decided on its own merits.** The question the task
poses is which convention "a legislative apportionment analyst would actually use," not which
number is smaller, and worked through honestly the two readings are not equally credentialed:

- The Census County Adjacency File [S4] — the exact document real redistricting analysts and their
  GIS tooling use to determine county adjacency (it is the Census Bureau's own product for its
  Redistricting Data Program, and it is what commercial and public redistricting software builds
  its contiguity graphs from) — draws no distinction between a land border and a water border. It
  lists Hancock and Knox as neighbors because their legal county boundaries touch, full stop.
- Excluding water boundaries is not "the professional default with a footnote" — it is a rule this
  case has no source for. It would require answering "how much water is too much?" (a strait? a
  bay? a river mouth?) with no citable threshold, which is precisely the kind of invented number
  SPEC §5 and this project's whole placeholder discipline exist to prevent.
- "Contiguity by water" is itself an accepted, unremarkable concept in real redistricting law and
  practice (islands reachable only by boat are routinely treated as contiguous to their district).
  There is no professional convention that discounts a water-only county boundary as not being a
  real border.

So the reading that would need defending is EXCLUDED, not COUNTED — and it is also the reading that
breaches the cap. That is not a coincidence to be resolved by picking COUNTED to dodge 22.2%; it is
COUNTED being correct on independent grounds that happen to also keep the case in balance. Per the
task's own instruction, if the more defensible reading had been the one that breached the cap, the
fix would have been to retune a different constraint (e.g., MA1's severance weight, which the
sensitivity sweep already shows brings A up to a tie at weight 2 and to a 15.8% margin at weight
1.5) rather than switch MA5 to dodge it. That mechanism was not needed here because the honest
answer to "which reading is defensible" and "which reading keeps margin_pct at 10.0%, inside SPEC
§2's cap" are the same reading. `case.json.modeling_assumptions[MA5].basis` and case.md's Appendix H
MA5 row are both updated to state the real-world grounding and mark this RESOLVED, not merely
disclosed. The 22.2% alternate reading remains fully disclosed — in Appendix B's caveat, Appendix H
MA5's sensitivity column, `balance.stability_note`, and FACILITATOR.md — as a legitimate classroom
challenge a Hero can raise, exactly as SPEC §2 and this project's sensitivity doctrine require. It
is not suppressed; it is correctly labeled as the *non*-committed reading.

### Issue 2 — Appendix F prints the case's own answer, defeating the trap

**Fix applied, matching the `six-degrees-of-exposure` pattern** (disclose enough surrounding data
for real derivation, don't print the graded number). `case.md` Appendix F's first row previously
read `65,536 — or 65,534 once you drop the two that leave a district empty`. It now reads:

> *the tool's claim — a Hero computes this from APPENDIX A's county list and the Fundamental
> Counting Principle, then drops the two assignments that leave a district empty*

Appendix A's full 16-county list was already public (it has to be, for Appendix A's own purpose),
so this is real, checkable derivation (2¹⁶ = 65,536, minus the 2 degenerate assignments = 65,534),
not guesswork — exactly the same shape as the `six-degrees-of-exposure` repair, which disclosed the
raw weighted-degree column so the graded 27,643 figure was derivable rather than printed. D1 already
required the Hero to compute this total via the Fundamental Counting Principle and show that the
binomial size-breakdown row sums to it; the appendix simply no longer hands them the checksum before
they do the work. FACILITATOR.md's primary trap description is updated to note this makes the trap
*stronger*: a Hero who does the honest work of deriving 65,534 is, if anything, more likely to
mistake their own derivation for an audit than a Hero who was just handed the number — the
misconception D3's induction proof exists to correct is unchanged either way. Confirmed by the fresh
P1 cold solve below, which derived 65,536/65,534 correctly and unprompted from Appendix A alone.

### Issue 3 — D4(iii)'s method was unspecified

**Fix applied.** `case.md`'s D4(iii) now reads (added text in bold):

> at least one district must contain at least two of Maine's four largest counties, with the
> population consequence of that fact stated in people as the **guaranteed minimum**: Pigeonhole
> proves that *some* two of the four largest counties share a district, but it does not tell you
> which two, so the only population figure the principle actually guarantees is the smallest
> possible sum over any two of those four counties — not the largest, and not whichever pair looks
> most dramatic on the page. State that minimum pairing's sum and show the arithmetic that makes it
> the floor, not just a pairing.

**Why this reading and not the other.** Pigeonhole is an existence proof: 4 counties into 2
districts forces some pair together, but the principle itself is silent on *which* pair. The only
claim licensed by "at least two of the four largest share a district" that is true under *every*
possible plan is the smallest population any such pair could sum to — i.e. the two smallest of the
four largest counties, Penobscot and Kennebec. Reporting the largest, most dramatic pairing
(Cumberland + York) instead states a number that is true of *a* plan, not a number Pigeonhole
guarantees of *every* plan — the exact over-read FACILITATOR.md already flagged as "the same error
[as the audit trap] with a bigger number." This was already the guide's intended reading before this
fix; it is now explicit in the student-facing text instead of being left for the guide to catch
after the fact only if a Hero happened to get it wrong.

### Fresh cold solve — P1, re-run 2026-08-18

A genuinely fresh, unbriefed subagent was dispatched with only
`/tmp/coldsolve-redrawing-lines/PACKET.md` (regenerated after all three fixes above; grepped clean
of `65,53x`, `FACILITATOR`, and any margin/percent leak beyond the sanctioned closing comment) and
no other file or web access.

**Result: PASS.** The solver chose **A**, named its optimized metric (maximum population deviation
as a percent of the ideal — deliberately *not* the crossings proxy, reasoning explicitly that
crossings flips under the opposite MA2 convention, exactly the sensitivity the case discloses),
showed fully correct arithmetic for both plans (681,179/681,180 vs. 683,062/679,297; deviations
0.000147% and 0.5527%(sic 0.5528% rounding) against the Karcher/Tennant benchmarks), answered all 7
required questions including the strongest counter-argument (Tennant rewards never splitting a
county), the most sensitive assumption (MA2), an ignored appendix item (the four dominated Appendix
D rows), and the least-supported number (MA1's severance weight). It additionally, unprompted:
(a) derived Appendix F's now-redacted total correctly, 2¹⁶ = 65,536 / 65,534 non-empty, from
Appendix A's county list, and correctly explained that the gap between 65,534 and the 1,734
contiguous plans is why D1–D3 matter; (b) applied D4(iii)'s now-explicit method correctly, computing
Penobscot + Kennebec = 275,841 as the guaranteed floor and explicitly rejecting Cumberland + York =
515,041 as "not guaranteed." Both redactions/clarifications hold up under a genuine blind solve: the
case remains fully solvable end to end from the packet alone, and the two previously-ambiguous
methods are now followed correctly rather than merely likely to be followed correctly.

### Tier 1 — structural (19 checks), re-run after all edits

`python3 skills/case-readiness/scripts/tier1_structural.py --case redrawing-lines` →
**checks run: 19 · PASS 19 · GAP 0 · FAIL 0 · VERDICT: TIER1_PASS**. 0 BLOCKER, 0 GAP. Same 4 POLISH
items as every prior run (T1-07 separator-run note; T1-15/18/19 — no `published/` directory yet, so
nothing to check there).

### Tier 2 — the other five probes

Not re-dispatched to fresh subagents this run (none of the three fixes touch P2–P6's underlying
numbers, the twist, the sensitivity sweep, or the sources) — re-verified mechanically instead:
`sensitivity_model.py` still self-tests clean (`python3 cases/redrawing-lines/sensitivity_model.py`
reproduces every figure in `case.json.derived` including the unchanged 10.0% margin, the MA2
counter-check at 9.1%, and the MA5 counter-check at 22.2%) and `case.json` is still valid JSON with
`standards[]` resolving in the spine. P2/P3/P4/P5/P6 verdicts carried forward from the 2026-08-12
run as **PASS**, unchanged, since none of the facts they graded moved.

### case.json.qa, as written by this run

`state: TIER2_PASS · verdict: PASS · run_on: 2026-08-18 · blockers_open: 0 · gaps_open: 0 ·
case_md_sha256: df7a285e9883f3c1041fe0e1acb5dba5c0efd37f3833d8c393e1ebfd408c0f14`. `gaps_open`
drops from 1 to 0 — the D4(iii) ambiguity that was the sole open gap is now resolved, not just
adjudicated around.

### Next step

`Run case-publish on redrawing-lines`. Tier 3 (human dry-run) is still `NOT RUN` — schedule it
before any ✅ in `DOCTRINE_LEDGER.md`; `PUBLISHED` is not `VERIFIED`.

---

## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → **TIER2_PASS**  ·  **Verdict:** TIER2_PASS
**case.md sha256:** `6447b8059661c9ac5a8b…` (recomputed after the P1 leak repairs below; the earlier
`cc6390a2…741cb` described the pre-repair file and is superseded)
**Model:** `cases/redrawing-lines/sensitivity_model.py`

### P1 · Cold solve — **PASS**, second pass (2026-08-12), genuine blind run

**This supersedes the in-process "PASS (protocol deviation)" recorded below**, which was not a blind
cold solve and should not have counted. Re-run by a fresh solver reading **only**
`/tmp/coldsolve-redrawing-lines/PACKET.md` — no repo access, no facilitator material.

**Both stage-2 repairs confirmed to hold.** All 16 Appendix A counties sum to exactly **1,362,359**;
the twelve municipalities sum to 53,595, giving 681,179 / 681,180. Both options clear every stated
benchmark — Kennebec Split **0.0001%** (a one-person deviation), Hancock Line **0.5527%**, below both
Karcher's struck-down 0.6984% and Tennant's upheld 0.79%. The case is solvable from the packet
alone, with nothing assumed and nothing looked up, and the solver reached a defensible
recommendation that is reachable both ways — which is the design.

**Finding — ANSWER LEAKS in the student-facing assumption table. REPAIRED.** Four places handed the
Hero a result before they computed it:

| Row | What it leaked | Repair |
|---|---|---|
| MA1 | Disclosed its own ±50% flex result ("the ranking does not move"), which is part of D5 — *and* leaked internal QA language, "Tier 2 probe 5", into a student packet | Now asks the Hero to run the flex and see |
| MA2 | Named which plan wins under the opposite convention | Now states that the counts change unequally, and to compute both |
| MA3 | Named which Appendix D row the rule selects | Now says only that it selects Option B from those rows |
| MA5 | Closing clause implied which plan leads | Now asks the Hero to say which plan it favours, and whether the widened gap still sits inside the balance cap |

**Deliberately NOT repaired:** Appendix F printing 65,536 / 65,534 *is* D1's answer, but that
assertion is load-bearing for `FACILITATOR.md`'s primary trap — "a count is not an audit." Removing
it would kill the trap. See the open author decision below. The blind solver hit this exactly as
designed, reporting an induction that "fails by exactly 2" as a real trap — that is the trap working,
not a defect.

**Unresolved ambiguity, not repaired:** D4(iii), "the population consequence of that fact stated in
people," names no method. The solver used the minimum forced pair (Penobscot + Kennebec = 275,841)
and notes another honest student would answer Cumberland + York = **515,041**. Two defensible,
different numbers.

> **This run also repaired the case.** `case-readiness` normally only gates (SKILL.md, "Never fix
> the case"). This run was explicitly instructed to apply the stage-2 repairs the probes demanded,
> so it did both. The stage-2 work is recorded below as *Repairs applied* so that the separation is
> at least visible on the record. Everything written is inside `cases/redrawing-lines/`. Nothing in
> `readmodel/` was touched; nothing was published; nothing was committed.

---

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 … T1-19 | PASS | all nineteen clean on the final re-run |

**BLOCKER (0)** — none.

**GAP (0)** — T1-16 (MCS-11 hash currency) was a GAP throughout the run because no
`case_md_sha256` had been recorded yet; it cleared when the hash above was written. Final Tier 1
run: **checks run: 19 · PASS 19 · GAP 0 · FAIL 0 · VERDICT: TIER1_PASS**.

**POLISH (4)**
* `[T1-07]` parsed 14 labels (14 bulleted, 0 from separator-run lines)
* `[T1-15]` no `published/` directory yet — nothing to drift
* `[T1-18]` no `published/` directory yet — MCS-37 has nothing to check
* `[T1-19]` no `published/` directory yet — MCS-39 has nothing to check

Tier 1 was re-run after **every** `case.md` edit; the last run is the one recorded above.

---

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** (protocol deviation, see below) | The packet is now solvable end-to-end from Appendix A/B/C/D/E/H: ideal 681,179.5; A = 681,179/681,180, max deviation 1 (0.000147%), 9 borders + 1 severance = 10 crossings; B = 683,062/679,297, max deviation 3,765 (0.5527%), 11 crossings. Both A and B are reachable as defensible positions and the optimised metric is nameable. **Before the repair this probe FAILED**: Appendix A printed only 15 of Maine's 16 counties (Somerset, 50,477, was missing), so the fifteen rows summed to 1,311,882 against a printed total of 1,362,359 and no solver could reproduce the northern district the case told them to check. |
| P2 both-sides | **PASS** | Neither side collapses. Best sentence for A: *"A is off by one person — the least Maine's odd population allows — and it still beats B on Margo's own rubric, 10 crossings to 11."* Best sentence for B: *"B divides nobody, and its 0.5527% sits below both the deviation the Court struck in Karcher and the one it upheld in Tennant; the single crossing it concedes is a weight this case invented."* A is pressed hardest at *"if B is already lawful, what is your extra precision buying?"*; B at *"Karcher says avoidable deviation needs justification, and A proves it was avoidable."* Both have answers. **Before the repair this probe FAILED**: Option B was The Oxford Line, whose 1.2277% maximum deviation is above *both* Appendix E benchmarks — above the 0.79% upheld **and** the 0.6984% struck down — while its entire advantage was one crossing produced solely by MA1's invented severance weight (at weight 0 the two plans tied). B collapsed at the first legality question, and the recorded 11.11% was a paper margin. |
| P3 trap | **PASS** | Independently derived wrong path from the packet alone: quoting *one district's distance from the ideal* (half-size) against Karcher's and Tennant's maximum-deviation percentages. The guide now names it. It also names the primary trap — reading Appendix F's 65,534 as an audit and writing "the commission examined every plan" without the D3 induction. **Before the repair the deviation-basis trap was unnamed and Appendix E never stated how its own percentages were computed**, which at the twist turns 1.2277% into 0.6139% and reverses the legal conclusion. |
| P4 twist | **PASS** | (1) The twist invalidates positions on both sides: the Oxford substitution takes the primary metric away from A (9 against 10, 11.11% the other way) and takes legal comfort away from B (1.2277%, above both benchmarks). (2) Re-derived under every defensible reading of every stated assumption: MA1 across its whole flex band (0.5/1.0/1.5) — the metric flip holds; MA5 water boundary excluded (A 9, Oxford 8) — holds; MA2 minority convention — the *metric* flip does **not** occur, because A was already scoring 12 and the whole-county side was already ahead, but the legal half of the twist lands with full force. No effect depends on a convention the case fails to state; MA1, MA2 and MA5 are all printed in Appendix H, and the MA2 case is now written into the guide so a room that has already overturned MA2 does not blindside the facilitator. |
| P5 sensitivity | **PASS** | Machine sweep, base A=11/B=10 (transformed; raw crossings 10 vs 11), base margin 10.0%, winner A. `severance_weight` −50% → 15.8%, +50% → 4.8%; no flip, cap not broken. Three of the four `FLEX[]` dials are non-numeric conventions (`split_county_assignment`, `shortlist_rule`, `water_boundaries`) and cannot be swept ±50%; each was flexed by hand through the model and the results are stated in the case, not hidden: MA2 → B wins by 9.1%; MA5 → A wins by 22.2% (**past SPEC §2's 20% cap**); MA3 → a different Appendix D row becomes Option B. |
| P6 data decay | **PASS** | All **9** URLs fetched live this run. All reachable, none moved, every recorded value still present. S1 Maine 1,363,582 · 2 seats and the "used for apportionment purposes only" footnote, read out of the PDF itself. S2/S3 the P.L. 94-171 zip downloaded and parsed: all 16 county counts and the state total 1,362,359 match to the person, the 30 Kennebec subdivisions sum to 123,642, and the 12 statutory CD-1 municipalities sum to 53,595. S4 adjacency file parsed: 16 Maine counties, **34** distinct borders, adjacency identical to Appendix B. S5 statute: 12 CD-1 / 18 CD-2 Kennebec municipalities, names matching. S6 ideal 681,179.5, CD-1 681,179, CD-2 681,180. S7 September 27, 2021. S8 527,472/523,798, 3,674, 0.6984%, struck down, quote verbatim. S9 4,871, 0.79%, upheld, "valid, neutral state districting policies", never-divided-a-county finding — and the caveat already recorded in `sources[S9].note` re-confirmed: the string "567 U.S. 758" still does not appear on that Cornell page, and the entry still does not assert it. |

**Protocol deviation on P1 (recorded, not waived).** The skill requires a *genuinely fresh
subagent*. This run was placed under a hard no-subagent budget constraint, so P1 was adjudicated
in-process by the same agent that had already read `FACILITATOR.md`. It is therefore a reasoned
solvability adjudication, **not a blind cold solve**. The specific thing it cannot prove is what a
reader who has never seen the guide would actually do. Re-run P1 with a fresh solver before Tier 3.

---

### Repairs applied (stage-2 work, re-entered per PIPELINE "What goes backwards")

1. **Appendix A restored Somerset County (50,477) [S2].** The table printed 15 of 16 counties
   against a 16-county total. Root cause of the P1 failure. Table now carries all sixteen and an
   explicit "check that your column adds to the total" instruction.
2. **Option B retuned from The Oxford Line to The Hancock Line** — the constraint retuned is
   **MA3**, the staff shortlist rule, from *"fewest county-line crossings"* to *"closest to equal
   population."* Ranked that way, Appendix D puts Hancock (3,765 people apart, 0.5527%) on the
   table instead of Oxford (8,363, 1.2277%). This is the P2 repair: B is now lawful under Tennant
   on Tennant's own reasoning, and the margin no longer depends on a plan that clears neither
   Appendix E benchmark. **No data was hidden to achieve this** — every Appendix D row is still
   printed, including Oxford's, and the Oxford plan is now the twist.
3. **Twist inverted accordingly**: a floor motion to strike MA3 and substitute Oxford. It now
   breaks the A position (loses the rubric) and the B position (loses legal comfort) at once.
4. **Appendix E now states the basis of its own percentages** — maximum deviation = larger district
   minus smaller, over the ideal — and D5 asks for both deviation figures and for one sentence on
   why the half-size figure is not comparable. This is the P3 repair.
5. **MA5 added**: the water-boundary counting convention, previously an unstated choice sitting
   loose in an Appendix B caveat. Its effect is stated openly, including that it pushes the margin
   to **22.2%, past SPEC §2's cap, in A's favour**.
6. **`sensitivity_model.py`** was found describing a different case from `case.md` (it already
   scored Hancock as Option B while `case.md`, `case.json` and `FACILITATOR.md` all still said
   Oxford — an inconsistency no Tier 1 check can see). Model, case, guide and `case.json.derived`
   are now one story; the model gained `water_boundaries` as an MA5 dial and self-test assertions
   pinning the 10.0% margin and both counter-conventions.
7. **Pigeonhole rigour (D4-iii):** the guide previously offered only Cumberland + York (515,041),
   which pigeonhole does **not** guarantee. It now also gives the guaranteed floor — the smallest
   pair among the four largest, Penobscot + Kennebec, **275,841** — and flags quoting 515,041 as a
   floor as the same over-read with a bigger number.

**Balance of record.** `margin_pct` **10.0** on county-line crossings: The Kennebec Split 10 (9
borders + MA1's severance weight), The Hancock Line 11 (11 borders, no severance).

**Subject-matter check (SPEC §6).** The case still uses population, geography and case law only —
no election results, no party registration — and neither option is a partisan position. Appendix E
names Karcher and Tennant as genuinely contested against each other rather than smoothing them,
and Appendix H MA4 keeps saying that The Hancock Line was never formally proposed to anyone.

---

### Tier 3 — human dry-run

**NOT RUN.** No `cases/redrawing-lines/runs/RUN_*.md` on file.

---

### Next step

`Run case-publish on redrawing-lines` — subject to the two open human checks listed below.
`PUBLISHED` is not `VERIFIED`; schedule the Tier 3 dry-run before any ✅ in `DOCTRINE_LEDGER.md`.

**Open for a human**

1. **Re-run P1 with a genuinely fresh subagent.** The verdict above is honest about being
   in-process. It is the one probe on this report that was not run to its stated protocol.
2. **Confirm the MA5 disclosure is the treatment you want.** Excluding the Hancock–Knox water
   boundary widens the margin to 22.2%, past SPEC §2's 20% cap. The case states it in the open
   (Appendix B, Appendix H MA5, the balance note and the guide's opening) rather than suppressing
   it, which is PIPELINE's sanctioned remedy — *state the convention, or state the instability* —
   but it is a judgement call and it is not the machine's to make.
3. **`published/` does not exist yet**, so T1-15/18/19 (artifact staleness, MCS-37 interactive
   HTML, MCS-39 glossary) had nothing to check. They are POLISH today and become real checks the
   moment `case-publish` runs.
