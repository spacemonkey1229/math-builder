## case-readiness run — 2026-08-31 (supersedes the run above)

**This run supersedes the 2026-08-31 BLOCKED run above in full.** Since that run, remediation closed
all three Tier 1 BLOCKERs (Twist section, anchor ladder, and the `new_coverage[]`/reinforcement-note
finding), added `FACILITATOR.md`, `sensitivity_model.py`, `RESEARCH_LOG.md`, and `cohort_bands[]`, and
this run re-executes Tier 1 clean and then runs all six Tier 2 probes to completion.

**State:** TIER1_PASS → TIER2_PASS   **Verdict:** PASS

`sha256(case.md) = 0b0469551066fa2c436d3d48791674ce8477afddf39fe19a284c9d63d56e89e4`

### Tier 1 — structural (20 checks, re-run)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are <X>." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | Challenge numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | final-appendix lines are verbatim spine labels (11 bulleted labels parsed) |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments written, margin ≤ 20% (2.13%) |
| T1-10 | GAP | `new_coverage[]` empty — reinforcement carve-out applies (`reinforcement_note` records the adjacent-skill check honestly; project-owner-approved 2026-08-17 doctrine, not a per-case waiver) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, 5 Socratic questions, sensitivity note all present |
| T1-14 | PASS | CONTINUITY — FACILITATOR.md's derived figures agree with case.json.derived; balance figures agree |
| T1-15 | PASS | no published/ artifacts yet — nothing to drift |
| T1-16 | PASS | QA hash current as of this run |
| T1-17 | PASS | `cohort_bands[]` declared (Full/Compressed/1:1) |
| T1-18 | PASS | n/a — no published interactive HTML yet |
| T1-19 | PASS | n/a — no published interactive HTML yet |
| T1-20 | PASS | n/a — advisory, no published visual asset yet |

**checks run: 20   PASS 19 · GAP 1 · FAIL 0**

### BLOCKER (0)
None.

### GAP (1) — verbatim from the script
* [T1-10] SPEC §8 — `new_coverage[]` is empty; the case closes no NEW gap (reinforcement carve-out: `case.json.reinforcement_note` records that adjacent uncovered skills were checked and honestly ruled out — downgraded from BLOCKER per 2026-08-17 doctrine amendment, project-owner approved, not a per-case waiver)

### POLISH (5)
* [T1-07] parsed 11 labels (11 bulleted, 0 from separator-run lines) — the separator run is the half the legacy check skipped
* [T1-15] no published/ directory yet — nothing to drift
* [T1-18] no published/ directory yet — MCS-37 has nothing to check
* [T1-19] no published/ directory yet — MCS-39 has nothing to check
* [T1-20] no published/ directory yet — T1-20 has nothing to check

---

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A genuinely fresh subagent, given only the leak-free `PACKET.md` (no `FACILITATOR.md`/`case.json`), reached Option B (Summer Shift) via correct arithmetic and named the right metric (TOU-weighted effective kWh/panel/year), independently reproducing the case's own numbers: weighted A ≈ 1163.0, weighted B ≈ 1187.5, ~2.1% margin, versus a *lower* raw annual total for B (656.2 vs 659.3, B trailing by 0.47%). It also cross-checked Appendix B's monthly figures against solar geometry (cosine angle-of-incidence at June/December solar noon) and found them directionally consistent — a real, arithmetic-grounded pass, not a guess landing on the "right" letter. |
| P2 both-sides | **PASS** | Both `case.json.balance.argument_a` and `argument_b` already carry real, specific quantitative content (A: 659.3 vs 656.2 kWh, 0.47% edge; B: 1187.5 vs 1162.8 weighted kWh, 2.93× summer multiplier, 2.13% margin) — no thin/qualitative-only prose found, no fix needed. Adjudication: Argument A is genuinely defensible ("we deliver more usable electricity over a full year — the number every competing bid is built on") but collapses exactly at the question the guide's own Anchor 2 is built around — "does SMUD pay the same for every kWh?" — once forced to confront the case's own stated time-of-use billing, A has no rebuttal. Argument B is more durable: it is the one still standing after the case's own harder stress-test (the twist's on-peak-rate reading), surviving with a thinner but real margin (1.37%). The 2.13% margin is not a paper number — B's side does not collapse. |
| P3 trap | **PASS** | The same fresh, blind subagent, asked (before reading any guide material) to name the most plausible wrong path, wrote: *"Picking Latitude Lock because Appendix B's annual totals (659.3 vs 656.2) show more raw kWh — mirroring the competitor's bid and Mrs. Reyes' own confusion — while ignoring that summer on-peak kWh is priced ~3× everything else."* This matches `FACILITATOR.md`'s stated trap ("comparing the two options on raw total annual kWh alone") exactly, independently derived. The guide has anticipated the trap that actually catches a fresh reader. |
| P4 twist | **PASS** | (1) The authored twist — SMUD's rate page publishes two different non-summer rates ($0.1285 off-peak vs. $0.1776 on-peak) for the same 5–8pm window — genuinely pressures the room's confidence in the 2.13% margin, which is exactly the position a room would hold after Anchor 3. (2) Re-derived under the stricter (on-peak) reading via `sensitivity_model.py`: `evaluate({"nonsummer_rate_used_usd_per_kwh": 0.1776})` still returns B ahead of A (margin narrows from 2.13% to 1.37%, winner unchanged) — the twist survives the case's own stated assumption read the harshest defensible way. **Adjacent finding, not a P4 failure:** the same blind solver independently raised a *different* critique the guide does not name — that Appendix C/D4's multiplier is applied to a whole summer month's kWh rather than only the actual 5–8pm on-peak hours, which (absent hourly production data the case does not have) could over- or under-state B's true economic edge by an unknown amount. This is a real, unaddressed adjacent risk, but it does not invalidate the *authored* twist's survival (P4's actual test), and Deep Conflict thread 2 ("a rate convention is only as solid as the usage pattern it assumes") is broad enough that a guide running it would not be caught flat-footed if a room raises this specific version of the challenge. Recorded here so a future revision can consider naming it explicitly rather than relying on the general framing. |
| P5 sensitivity | **PASS** (mechanical, `tier2_probes.py --case the-tilt-decision`) | Base: A=1163.12, B=1187.52, winner B, margin 2.1%. Swept both declared `FLEX[]` dials ±50%: `panel_count` (±50%, 10→30 panels) never moves the result (1163.12/1187.52 unchanged either direction — confirms MA1's own "cancels out entirely" claim mechanically); `nonsummer_rate_used_usd_per_kwh` ±50% ($0.06425–$0.19275) moves the margin between 1.1% and 3.4% but **never flips the winner** — B (Summer Shift) wins on every swept value. No `breaks_20pct_cap` flags. |
| P6 data decay | **PASS**, with 2 disclosed findings and corrections | See full findings below. All 7 sources fetched live 2026-08-31. Net: S2/S4/S6/S7 confirmed exact matches; S3 confirmed still bot-blocked on both URLs (matches the case's own pre-existing disclosure, not new information); S1 had a small immaterial coordinate drift, now corrected; S5's domain initially read as a possible typosquat and was independently investigated and confirmed legitimate. |

**P6 detail:**
- **S1** (site lat/lon, findlatitudeandlongitude.com) — reachable. Live page now reads 38.582301°N/-121.49332°W vs. the case's recorded 38.5816°N/-121.4944°W (~90m drift). **Corrected** in `case.md` Appendix F and `case.json.sources[0].note` to record the current live value and confirm immateriality (still rounds to a 39° Latitude Lock tilt; no other figure depends on this to a precision finer than ~90m resolves).
- **S2** (Qcells Q.PEAK DUO BLK M-G11, 400W) — reachable, PDF confirms 380–400Wp series, 400W selection valid. No change.
- **S3** (Clenergy racking tilt range 10°–60°) — both the primary URL and the ENF Solar cross-listing still return HTTP 403 (bot-blocked), confirmed via two independent fetch methods. This matches the case's own existing S3 note verbatim ("direct fetch of clenergy.com was blocked by the site's bot-protection") — not a new finding, and not load-bearing (both option tilts sit well inside the range regardless).
- **S4** (Lave & Kleissl 2011, "latitude − 15°") — reachable (direct download after a WebFetch TLS hiccup), PDF text confirms the rule as stated. No change.
- **S5** (NREL PVWatts v8 API, `developer.nlr.gov`) — **investigated as a possible spoofed/typosquatted domain** (the old `developer.nrel.gov` now fails DNS resolution outright, and the live `developer.nlr.gov` page describes itself as "National Laboratory of the Rockies," a name not previously known to this reviewer). Independently verified, not taken on the page's own word: the U.S. Department of Energy renamed NREL to the National Laboratory of the Rockies (NLR) effective 2025-12-01, confirmed via `energy.gov`'s own announcement and DOE's OpenEI wiki — both authorities independent of the cited page. The domain and figures are legitimate; `case.json.sources[4].note` updated to record the independent verification so a future reviewer does not have to re-litigate this.
- **S6** (SMUD Schedule R-TOD) — reachable, all three cited figures ($0.3765 summer on-peak, $0.1285 non-summer off-peak, $0.1776 non-summer on-peak) confirmed exact match. No change.
- **S7** (NOAA solar-position equations, solareqns.PDF) — reachable, confirmed as the correct NOAA Global Monitoring Division document. No change.

### Tier 3 — human dry-run
NOT RUN (expected — not required for `TIER2_PASS`; required before `VERIFIED`).

---

**case.json.qa written:** `{"state": "TIER2_PASS", "verdict": "PASS", "run_on": "2026-08-31", "blockers_open": 0, "gaps_open": 1, "tier2": {"P1": "PASS", "P2": "PASS", "P3": "PASS", "P4": "PASS", "P5": "PASS", "P6": "PASS"}, "tier3_runs": [], "case_md_sha256": "0b0469551066fa2c436d3d48791674ce8477afddf39fe19a284c9d63d56e89e4"}`

**Next step:** `case-publish` may now run on `the-tilt-decision`. Before Tier 3 (`VERIFIED`), consider whether the P4 adjacent finding (whole-month vs. 5–8pm-hour weighting) is worth naming explicitly in `FACILITATOR.md`'s Deep Conflict thread — not a blocker, but the sharpest critique a real room is likely to raise that the guide does not currently call by name.
