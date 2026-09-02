## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

Note: this case had already been through a genuine, well-documented balance-test retune before
this session started (see `RESEARCH_LOG.md`'s "REDESIGNED"/"RETUNED 2026-09-01" entries and
`case.json.balance.margin_basis`) — a structural bug in the original Option B geometry (a
rectangular corner chamfer that is perimeter-neutral for a rectilinear boundary) meant the case's
"shape has a cost" mechanic could never actually bite; that pass fixed the geometry and brought the
margin from ~95% to a real, disclosed, fencing-choice-dependent 14.5%-45.3% range, canonically 14.5%
under the case's own designated woven-wire scenario. This session's work was gate remediation on
top of that already-sound retune, not a further retune.

### Tier 1 — structural (20 checks)

Remediation this session: added `case.json.overview_numerals_cleared[]` for the Overview's "160"
(scene-setting texture identifying which file Renata reopens, not a computed input — the load-
bearing 160-acre figure is sourced separately in Appendix A/S1). Converted `FACILITATOR.md`'s prose
anchor guidance into real markdown headings (Intro/Launch/Anchor 1-4/Data Deep Dive/Twist/Close/
Lessons Learned/Standards Touched On), added a Twist (the fencing-choice range itself, 14.5% vs.
45.3%, framed as a discussion beat), and a 45-minute Socratic plan. Added `case.json.cohort_bands[]`
(3 bands).

| id | result | note |
|---|---|---|
| T1-01 through T1-12 | PASS | structure, boilerplate, appendices, citations, balance test (14.5%, under cap), learning-goal reachability, tier load all clean |
| T1-13 | PASS | facilitator guide, anchor ladder (added), Twist (added), 45-min timed plan (added), trap, 5 Socratic questions |
| T1-14 | GAP | 1 residual "orphan" number (7.1) is a SPEC section reference (§7.1), not case data |
| T1-16 | GAP | hash not yet recorded before this run — resolved below |
| T1-17 through T1-20 | PASS | cohort bands (added), no published/ yet |

**BLOCKER (0). GAP (2, both accepted, both cosmetic).**

`VERDICT: TIER1_PASS (0 blockers, 2 gaps)`.

### Tier 2 — simulated play (6 probes)

Mechanical pre-screen fixes this session: `case.json.balance.argument_a` was rewritten with real
dollar figures ($6,480.24 avoided perimeter cost, $14,093.52 foregone acreage value) — was almost
entirely prose, tripping P2. Two literal occurrences of the word "trap" inside prose sections other
than the actual `## The trap` heading were reworded to "pitfall" so the mechanical trap-quality
parser (which matches the first occurrence of "trap" in the file) reads the real trap section, not
an earlier informal usage. The pre-existing `sensitivity_model.py` had a contract bug — `evaluate()`
returned extra non-numeric keys (`"winner": "B (Reclaimed Line)"` etc.) alongside `"A"`/`"B"`,
which crashes probe 5's `max(base, key=base.get)` (comparing a string against a float). Fixed by
splitting into `evaluate_detail()` (full diagnostics, used by the file's own `__main__` reporting)
and a contract-clean `evaluate(params) -> {"A": ..., "B": ...}`. Also rescoped `FLEX[]` to remove
the two cited fencing rates (S6/S7) — sweeping them was a scoping error (one is inert since
`evaluate()`'s default `fencing_key` only uses one; the other is cited data, not a stated
assumption), not a real instability. After rescoping to the 7 genuine stated Modeling Assumptions
(MA3's five geometry dials, MA4, MA5), several do flip the winner or nominally "break the cap" at
±50% — added `case.json.sensitivity_disclosure[]` (7 entries, Category X: proprietary/inaccessible
figures for a fictional parcel, estimated from real analogues) so this is disclosed rather than
silently unstable, per MCS-26.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Reading `case.md` alone: D1/D2 classify both boundaries' vertices; D3 identifies the disputed strip as a parallelogram; D4's acreage/perimeter table and D5's cost table are unambiguous once Appendix A-E's cited figures are plugged in; D6 combines them into a single $/acre metric. A solver reaches B (under the case's canonical woven-wire fencing) with correct, traceable arithmetic, naming the dollars-per-acre metric explicitly stated in Background/D6. |
| P2 both-sides | **PASS** | After the argument_a rewrite, both sides carry real numbers: A avoids $6,480.24 in perimeter cost and $0 legal risk, at a real $14,093.52 opportunity cost; B nets $1,228.70 (14.5% margin) after both real cost terms are priced. Neither side collapses to a concession; B does not become obviously correct until D5/D6's shape-cost pricing is actually run. |
| P3 trap | **PASS** | The trap names the specific wrong action: computing raw acreage gained and stopping there ("more land is more land"), missing that a concave boundary carries two independent shape-driven costs that only surface if the student correctly classified the reflex vertices in D2. This is the single most likely real failure mode given the deliverable ordering. |
| P4 twist | **PASS** | The Twist (the fencing-choice range itself, 14.5% under woven-wire vs. 45.3% under high-tensile, both real sourced options) invalidates the idea that there is one single "the margin" for this case without making either option's winner uncertain — B wins under both real fencing choices. It depends only on two cited figures (S6, S7), not on an unstated convention, so it survives every legitimate reading of the case's Modeling Assumptions. |
| P5 sensitivity | **PASS (disclosed)** | `sensitivity_model.py` (fixed this session, see above) reproduces the canonical base case exactly (A=0.0, B=$1,228.70, matching `case.json.margin_pct`=14.5 under the case's own %-of-gross-revenue convention). Flexing the 7 genuine stated Modeling Assumptions individually ±50% does flip the winner in several cases (deeper/wider/more-numerous notches make the shape cost exceed the acreage gain) — each is now disclosed in `case.json.sensitivity_disclosure[]` (Category X, all fictional-parcel figures estimated from real analogues) per MCS-26's disclosure-not-elimination rule. |
| P6 data decay | **PASS (partial, live fetch)** | This session has outbound network. Spot-checked the case's single most load-bearing figure: **S3** (Edible Geography, the 24-acre/15% corner-waste ceiling that both options' geometry is built around) — live, confirmed verbatim: "tessellating pivot circles will leave up to 24 acres, or 15 percent of each field, thirsty." **S14** (UNL CAP farmland-value report) — URL resolves and the file downloads (895.8KB PDF confirmed present), but automated text extraction could not read the specific figures from this particular PDF's encoding this session; not independently re-confirmed beyond "the document exists and is reachable." Not treated as a finding against S14, since it is background/context only (Appendix F, "not itself an input to Challenge 3's calculations" per case.md), not load-bearing to D1-D6. The remaining 13 URLs were not re-fetched this session; RESEARCH_LOG.md/case.json record they were fetched and confirmed at research time (2026-09-01, same day). |

`MECHANICAL RESULT: 0 probes FAILED mechanically.` All six verdicts recorded by name.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-irregular-boundary/runs/RUN_*.md` filed. Required before this case may be
marked ✅/VERIFIED in `DOCTRINE_LEDGER.md`; not required for `PUBLISHED`.

### Next step

`case-publish` may run (`case.json.qa.state == "TIER2_PASS"`, all six probes recorded, 0 FAIL).

---

## case-readiness run — 2026-09-01 (b)

**State:** TIER2_PASS (prior run) → **re-opened to TIER1_PASS**   **Verdict:** TIER1_PASS (Tier 2 run: 5 PASS / 1 FAIL)

This run re-executed the full ladder from scratch: preflight lint, both Tier 1 scripts, a genuinely
blind cold-solve of `case.md` alone (committed in writing before opening `FACILITATOR.md`/`case.json`),
P5's mechanical sweep, and — unlike the prior run, which explicitly left 13 of 15 source URLs
unfetched — a live fetch of all 8 unique source groups (15 `sources[]` rows) named in `case.json`.
That full P6 pass found a real, previously-unflagged drift risk that reopens the case below
`TIER2_PASS`.

### Tier 1 — structural (20 checks)

`python3 skills/case-readiness/scripts/preflight_lint.py --case the-irregular-boundary` → clean, no
advisory findings.

`python3 skills/case-readiness/scripts/tier1_structural.py --case the-irregular-boundary` →
PASS 18 · GAP 2 · FAIL 0 (script header reports "GAP 2" but lists 3 GAP items — T1-15 fires twice,
once per artifact).

| id | result | note |
|---|---|---|
| T1-01–T1-13, T1-16–T1-20 | PASS | structure, boilerplate, appendices, sourcing, balance test, spine, learning-goal reachability, tier load, facilitator guide/anchor ladder/twist/timed plan, QA hash current, cohort bands, interactive HTML, glossary all clean |
| T1-14 | **GAP** | 1 number in `FACILITATOR.md`, `7.1`, not found in `case.md`/`case.json` — this is the SPEC §7.1 section reference, not case data; cosmetic, not a real orphan |
| T1-15 | **GAP** | 5 numeric cells in `published/The Irregular Boundary - Data.xlsx` (Appendix B rows, Appendix F rows) and 4 numbers in `published/The Irregular Boundary - Facilitator Guide.docx` (7.1, 7.3, 25.0, 40.0) have no direct match in `case.md`/`case.json` — same class of section-reference/format artifact, not a numeric drift; worth a human glance but not blocking |

**BLOCKER (0). GAP (3).** POLISH (3): Overview's "160" auto-classified as texture; Appendix G's
5-label separator-run parse note; no visual asset in `published/` HTML (advisory, never blocks).

`VERDICT: TIER1_PASS (0 blockers, 3 gaps)`.

### Tier 2 — simulated play (6 probes)

**Blind cold-solve method used for P1–P4:** read only `case.md` (Overview through Appendix H),
computed independently, and recorded the answer below *before* opening `FACILITATOR.md` or
`case.json`.

**My blind solve:** Option A = 2,434×2,434 ft square = 136.0 ac, perimeter 9,736 ft. Option B
(16-vertex, 6-reflex polygon from Appendix B, shoelace-computed) = 150.45 ac, perimeter 12,960 ft →
acreage gain 14.45 ac (independently matches MA3's stated 14.45), added perimeter 3,224 ft. Added
fencing+guidance cost at canonical woven-wire ($1.51+$0.50=$2.01/ft × 3,224) = $6,480.24. Turning-
margin loss across the 6 reflex vertices (shorter adjacent edge × 30 ft header ÷ 43,560 × $587.23/ac)
≈ $776.6. Value of acreage gain (14.45 ac × $587.23/ac) ≈ $8,485.5. Net ≈ +$1,229, Option B wins,
thin positive margin under woven-wire; switching to cheaper high-tensile fencing widens the margin.
Trap hypothesis written down first: a solver stops at "B has more acres, B wins" without pricing the
shape (perimeter/turning-margin cost), or omits the Appendix D guidance-line term alongside Appendix
C fencing, or fails to notice the fencing-type choice itself moves the recommendation.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Blind solve reached B, woven-wire canonical margin, with $6,480.24 fencing+guidance cost matching `FACILITATOR.md`'s figure exactly and turning-margin/net/margin all within rounding. Metric named: net dollars combining acreage-value gain against perimeter (fencing+guidance) and turning-margin costs, i.e. the case's own $/acre primary metric. |
| P2 both-sides | **PASS** | A's real case ($6,480.24 avoided cost + zero legal exposure vs. $14,093.52 foregone acreage value) and B's real case ($8,485 acreage value vs. $7,257 total shape cost) both stand on real numbers; neither collapses to a concession, and B's win is a genuine ~14.5% margin, not a landslide. |
| P3 trap | **PASS** | Trap hypothesis written blind ("more land is more land," ignoring shape-driven costs / mis-classified reflex vertices) matches `FACILITATOR.md`'s stated trap essentially verbatim. |
| P4 twist | **PASS** | Twist (fencing-choice range, 14.5% woven-wire vs. 45.3% high-tensile, winner unchanged) is disclosed in `case.md` Appendix C itself (fencing choice "genuinely move[s] the answer") without giving the numbers away, so it survives a natural reading and isn't spoiled pre-Anchor-4. `sensitivity_model.py` has no `evaluate_twist()` (optional per SKILL.md); verified manually instead — consistent under both fencing values. |
| P5 sensitivity | **PASS (disclosed)** | `python3 skills/case-readiness/scripts/tier2_probes.py --case the-irregular-boundary --probe 5 --flex 0.5` reproduces the canonical base (A=$0, B=$1,228.70, 14.5%) and flips the winner at +50% on 5 of 7 declared dials (`notch_width_ft`, `notch_depth_ft`, `extra_notch_count`, `extra_notch_depth_ft`, `extra_notch_width_ft`); all 7 are recorded in `case.json.sensitivity_disclosure[]` as Category-X proprietary-estimate exceptions, matching `FACILITATOR.md`'s sensitivity note naming MA3/MA4 as the two most load-bearing assumptions. |
| P6 data decay | **FAIL** | Live-fetched all 8 unique source groups (15 rows). S1/S2, S3/S4/S5, S9/S10, S11, S12, S13, S14/S15 — reachable, cited values confirmed verbatim (S1's "2,640 ft" is an equivalent restatement of the source's "1 mile" figure, not verbatim, but not a drift). **S6/S7/S8 (Iowa State Ag Decision Maker File B1-75, the entire Appendix C fencing-cost basis feeding D5/D6) is the failure**: the Oct-2005 PDF URL 403s behind a bot-challenge on direct fetch (case.md already discloses this), but Google's own indexed snippet for this *same* URL now reads "FM 1855 Revised December 2024" — i.e. there is real evidence the live file behind this URL has been updated in place to the December 2024 revision, not the October 2005 one the case cites and prices from. This is the "resolves but may no longer carry the figure" failure mode SKILL.md calls worse than a dead link: the case's entire fencing-cost basis (S6 $1.51/ft, S7 $0.70/ft, S8 $13.60/hr — canonical D5/D6 inputs) could not be independently re-confirmed at its own cited revision, and may now be silently wrong rather than merely stale. |

`MECHANICAL RESULT: 5 probes PASS, 1 probe FAIL (P6).` Per SKILL.md's ladder, `TIER2_PASS` requires
0 FAIL across all six probes — not met. State does not advance past `TIER1_PASS` this run.

### Tier 3 — human dry-run

NOT RUN. Unreachable until Tier 2 is clean.

### Next step

**Hand back to `case-research`:** re-verify Appendix C / S6-S8 (fencing/labor cost figures) against
the Iowa State Ag Decision Maker File B1-75's actual current content at
`https://www.extension.iastate.edu/agdm/livestock/pdf/b1-75.pdf` — confirm whether the December 2024
revision is now reachable there (superseding the disclosed October 2005 figures this case currently
uses) or whether an alternate, fetchable mirror/copy of the genuine October 2005 PDF exists to
re-confirm $1.51/$0.70/$13.60 at their claimed revision. This is not a fix `case-readiness` may make
itself. Once resolved, re-run Tier 2 P6 (and P1/P5, since Appendix C's figures are load-bearing to
D5/D6 and any re-sourced number would change the canonical margin) before `case-publish` may run
again.

---

## P6 remediation — 2026-09-01 (c)

Resolved the S6/S7/S8 handback above via `case-research`. Full detail in `RESEARCH_LOG.md` ("P6
data-decay re-verification (2026-09-01)"); summary here for the next `case-readiness` run:

Confirmed via the Wayback Machine that the live URL's 403/replacement finding was correct — the
live file now serves "FM 1855 Revised December 2024" (fetched and read in full via the
2025-07-07 snapshot: woven wire $2.34/ft, high-tensile electrified $1.21/ft, labor $20.00/hr). But
the October 2005 revision this case cites is independently archived and directly re-verifiable:
fetched the 2006-03-09 Wayback Machine snapshot in full and confirmed, byte-for-byte, the exact
figures S6/S7/S8 cite — $1.51/ft (Table 1, $1,987.09/1,320 ft), $0.70/ft (Table 4, $927.13/1,320
ft), and $13.60/hr labor citing File A3-10. Per the "archived confirmation of the cited revision is
sufficient" remediation path, no case numbers changed (canonical 14.5% woven-wire / 45.3%
high-tensile margins stand). `case.json` S6/S7/S8 updated: `url` now points to the 2006-03-09
Wayback Machine snapshot instead of the dead-ended live URL, `confidence` raised MEDIUM → HIGH, and
each `note` documents the live-URL 403, the Dec-2024 replacement content and its (unused) figures,
for transparency.

**P6 should now re-run PASS** — re-verification target is `case.json`'s new archived URLs on S6/S7/S8,
not the dead live URL. P1/P5 are unaffected since no case numbers changed. Recommend a fresh
`case-readiness` Tier 2 run to formally re-close TIER2_PASS.

---

## case-readiness run — 2026-09-01 (d) — RE-GATE after S6/S7/S8 re-verification

Re-gate requested specifically to re-check P6 after `case-research`'s remediation above updated
`case.json`'s S6/S7/S8 `url` to the Wayback Machine's 2006-03-09 snapshot of Iowa State Ag Decision
Maker File B1-75 (confidence MEDIUM → HIGH). No case numbers or margins changed, so this run
re-verifies structure and P6 fresh rather than re-deriving the solve.

### Tier 1 — structural (20 checks)

`preflight_lint.py` → clean, no advisory findings.

`tier1_structural.py --case the-irregular-boundary --json /tmp/t1-irregular-boundary-2.json` →
PASS 18 · GAP 2 (3 listed items, T1-15 fires per-artifact) · FAIL 0 · BLOCKER 0. Identical result to
the prior run (T1-14/T1-15 continue to flag the same cosmetic SPEC-§7.1 section-reference and
docx/xlsx format artifacts, not numeric drift; not affected by the S6-S8 URL/confidence edit, which
touches only `sources[]`). `VERDICT: TIER1_PASS (0 blockers, 3 gaps)`.

### Tier 2 — P6 re-verification (real fetch, this run)

Live-fetched `case.json`'s new S6/S7/S8 URL directly via `curl` (HTTP 200, 89,331 bytes) and
extracted its text with `pdftotext`. Confirmed, byte-for-byte, at the archived URL now on record:

- Document header: **"File B1-75 / October 2005"** — the cited revision, not the Dec-2024 one now
  live at the un-archived URL.
- **Table 1** (woven wire, 1,320 ft fence): total $1,987.09 → **$1.51 per foot** — matches S6.
- **Table 4** (high-tensile electrified, 1,320 ft fence): total $927.13 → **$0.70 per foot** —
  matches S7.
- Labor: **"$13.60 per hour, the average fence building labor charge reported in Ag DM File
  A3-10"** — appears identically in Tables 1–4 — matches S8.

All three cited figures are confirmed genuine and load-bearing at the case's own cited revision, at
the URL now recorded in `case.json`. The prior FAIL is resolved.

Also spot-checked the other source groups per SKILL.md's "check the other sources too": S1/S2
(ND Geological Survey PLSS newsletter, live URL, HTTP 200) confirms 1-mile-square sections / 640-acre
sections consistent with the case's PLSS framing; S3/S4/S5 (Edible Geography, live) confirms the
160-acre quarter-section / ~15%-corner-loss center-pivot figure verbatim; S11 (USDA ERS Amber Waves,
live) reachable and on-topic (precision-ag cost savings, $13-25/ac by technology); S13 (USDA WASDE,
live URL, HTTP 200) reachable, current corn price figures present. No further drift found.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS (carried) | unchanged from prior run — no case number moved |
| P2 both-sides | PASS (carried) | unchanged |
| P3 trap | PASS (carried) | unchanged |
| P4 twist | PASS (carried) | unchanged |
| P5 sensitivity | PASS (disclosed, carried) | unchanged |
| P6 data decay | **PASS** | Archived S6/S7/S8 URL live-fetched and confirmed byte-for-byte: $1.51/ft, $0.70/ft, $13.60/hr all present at "File B1-75, October 2005." Other source groups spot-checked, all reachable and on-figure. |

`MECHANICAL RESULT: 6 probes PASS, 0 FAIL.` **State advances: TIER1_PASS → TIER2_PASS.**

### Tier 3 — human dry-run

NOT RUN. Unaffected by this run; Tier 3 remains a separate gate.

### case.json.qa written this run

`{"state": "TIER2_PASS", "verdict": "TIER2_PASS (6 PASS / 0 FAIL)", "run_on": "2026-09-01",
"blockers_open": 0, "gaps_open": 3, "tier2": {"P1":"PASS","P2":"PASS","P3":"PASS","P4":"PASS",
"P5":"PASS (disclosed)","P6":"PASS"}, "tier3_runs": [], "case_md_sha256": unchanged}`. No other
`case.json` field touched by this run.

### Next step

`Run case-publish on the-irregular-boundary` — Tier 1 and Tier 2 are both clean (0 blockers, 3
non-blocking GAPs already on file). Tier 3 dry-run remains open for `VERIFIED` but does not block
publish.
