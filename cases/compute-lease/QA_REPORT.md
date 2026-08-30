## case-readiness run — 2026-08-30 (balance retune — TIER2_PASS)

**State:** BLOCKED → TIER2_PASS   **Verdict:** PASS (0 blockers; Tier 1 clean, 0 gaps; all six
Tier 2 probes PASS or PASS (disclosed))

### What changed this pass — the retune

The 2026-08-27 run below (preserved) found T1-09 FAIL: the case's primary metric (total cost per
GPU-hour delivered) had the Long Lock beating the Open Tap at **every** Appendix D growth scenario
— Low 36.5%, Mid 63.5%, High 76.4% — well past SPEC §2's ~20% cap, with the D5 crossover
(~2.5%/month) sitting *below* the entire stated range. The case owner chose to **retune the case**
(SPEC §2), following this project's established precedent (`fret-board`, `cooling-curve`) of a
grounded, honestly-researched retune rather than accepting the imbalance.

**Diagnosis before retuning.** Checked whether MA1 (cluster size, 512 GPUs) or MA2 (starting
demand, 120,000 GPU-hrs/month) could fix this alone, since those are the usual first levers. They
cannot: under this case's "delivered = demanded" reading, Long Lock's cost floor is its own flat
rate ($2.97/GPU-hr), reached only in the hypothetical limit of 100% utilization of the committed
cluster for the full 24-month window. Even at that floor, the margin against Open Tap's $6.88/GPU-hr
is 56.8% — nearly 3x the SPEC cap. No MA1/MA2 combination could have pulled the margin under 20%
while the sourced rates (S1/S2) stayed fixed. The imbalance was baked into Appendix D's growth-rate
range, not the cluster-size/demand assumptions.

**Root cause.** Appendix D's original growth-rate range (S3/S4/S5) proxied Kestrel's demand growth
off *hyperscaler-scale* AI-infrastructure figures — the world's single largest AI data center's
compute-doubling time (Epoch AI), the training-compute trend of the largest notable AI models
(Epoch AI), and aggregate worldwide AI infrastructure capital spending (IDC). All three are real,
dated, correctly-sourced figures — the defect is fit, not veracity. Kestrel is explicitly a
*mid-size* AI cloud provider (case.md Background), not a hyperscaler, and the original sources'
own notes already flagged this mismatch ("not literally GPU-hours rented by a mid-size cloud
reseller's paying customers") without it being corrected before the first QA pass.

**Retune applied.** Appendix D was re-sourced from DigitalOcean Holdings (NYSE: DOCN) — a real,
publicly-traded, mid-size cloud infrastructure company, and the closest available real-world
analog to Kestrel's own stated scale. Fetched directly from `investors.digitalocean.com` (HIGH
confidence; SEC's own EDGAR mirror of the same releases returned HTTP 403 to automated fetches):
Low 14%/yr (DOCN Q2 2025 actual) = 1.1%/month; Mid 22%/yr (DOCN Q1 2026 actual, most recently
*reported* quarter) = 1.7%/month; High 29%/yr (DOCN Q2 2026 guidance) = 2.1%/month. All three sit
along *one real company's own disclosed growth trajectory*, not three unrelated proxies — a
tighter fit than the original sourcing. MA1 (512 GPUs), MA2 (120,000 GPU-hrs/month), and both
sourced rates (S1/S2, $6.88/$2.97) are **completely untouched**. Full search trail in
`RESEARCH_LOG.md`'s 2026-08-30 entry.

**Recomputed margin: 9.1%** (Mid scenario; was 63.5%), inside SPEC §2's ~20% cap with genuine
slack (~10.9 points), not a cap-edge nudge. **Winner flips**: the Open Tap now wins at all three
retuned scenarios — Low 15.4%, Mid 9.1%, High 4.6% — reversing the original all-scenarios-favor-
Long-Lock result. The margin *narrows* as growth rises (opposite direction from the pre-retune
case), converging toward the recomputed D5 crossover (≈2.48%/month, ≈34.2%/year), which now sits
just 5.2 annualized points above the High scenario — a real, disclosed, near-a-tie tension, not a
coincidence. `case.json.derived{}` backfills the supporting figures (crossover, the 56.8%
full-utilization floor, months-to-capacity-ceiling under the new range) so they're checkable
against the case of record.

**FACILITATOR.md fully rewritten to match.** Data Deep Dive arithmetic, Anchor/Deep-conflict
framing, "The trap," and the Socratic questions all updated for the new numbers and the new
winner. **The Twist was replaced**: the original 512-GPU physical-capacity-ceiling twist no longer
triggers within the 24-month window under the slower, retuned growth rates (demand now crosses
that ceiling 55–104 months out, per `case.json.derived`, far outside the evaluation window under
every scenario) — it is preserved in a collapsed `<details>` block for continuity/history, and
replaced with a twist built entirely from the same DigitalOcean source's own additional disclosed
figures (RPO growth "more than 10X year over year," 2027 guidance "over 50%") — no new figure
invented, it reuses S4's own citation more fully. `case.json.balance.argument_a`/`argument_b` were
also rewritten with real quantitative content (SPEC §2 requires the strongest *quantitative*
argument for each side; `tier2_probes.py --probe 2` initially FAILED mechanically on the
pre-retune prose, fixed by this rewrite).

### Tier 1 — structural (20 checks), re-run 2026-08-30

`python3 skills/case-readiness/scripts/tier1_structural.py --case compute-lease`

**PASS 20 / GAP 0 / FAIL 0. sha256(case.md) =
57b6340423e34f1d51124eb42aacc803a7954021e8069fe2c1ba2b5159ae5813**

| id | result | note |
|---|---|---|
| T1-01–T1-08 | PASS | unchanged |
| T1-09 | **PASS** | margin is now 9.1% (Mid scenario), inside the ~20% cap — genuine retune, not a coin-flip nudge |
| T1-10–T1-13 | PASS | unchanged |
| T1-14 | **PASS** | guide-only derived figures (D5 crossover, the 56.8% full-utilization floor, months-to-capacity-ceiling under the retuned range, the DigitalOcean RPO multiple) backfilled into `case.json.derived{}` so they're checkable against the case of record |
| T1-15–T1-20 | PASS | unchanged; T1-16 (QA hash) re-recorded current after the retune edits |

**BLOCKER (0). GAP (0).** Fully clean Tier 1 — no pre-approved carve-outs needed this time
(unlike `fret-board`'s T1-10 or `cooling-curve`'s T1-09-as-GAP).

Preflight linter (`preflight_lint.py --case compute-lease`) reports the same single
pre-existing advisory finding as every prior run (the `<!-- FACILITATOR ONLY -->` guard comment on
line 160 of case.md) — advisory only, unrelated to this retune, not a blocker.

### Tier 2 — simulated play (6 probes), fully adjudicated 2026-08-30

Authored `cases/compute-lease/sensitivity_model.py` (contract: `PARAMS`, `FLEX = [n_gpus (MA1),
starting_demand_gpu_hrs (MA2)]`, `evaluate()` returning the Mid-scenario cost-per-GPU-hour for
each option, negated so higher-is-better holds — same 1/x-style flip convention as
`cases/fret-board` and `cases/enclosure-call`, since the case's own metric is a cost). **Base case
reproduces `case.json` exactly:** Long Lock $7.57/GPU-hr, Open Tap $6.88/GPU-hr, Open Tap wins,
margin **9.1%**; D5 crossover recomputed independently at 2.480%/month, matching
`case.json.derived` to 2 decimal places.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched a fresh subagent with no access to `case.json`/`FACILITATOR.md`/`QA_REPORT.md`/`sensitivity_model.py`, only `/tmp/coldsolve-compute-lease/PACKET.md`. Chose **Option B (Open Tap)**, with correct arithmetic matching the case of record exactly (Long Lock $8.13/$7.57/$7.21 across Low/Mid/High vs. Open Tap's constant $6.88; D5 crossover ≈2.48%/month, outside the stated range on the high side). Named its metric explicitly (cost per GPU-hour delivered, per the board's own stated criterion), named **MA2** (starting demand) as the assumption its answer is most sensitive to — matching this case's own `sensitivity_disclosure[]` finding exactly, independently derived — and named **Appendix D's growth-rate range itself** (the DigitalOcean-revenue-growth proxy) as the least-supported number, again independently landing on the same tension this retune's own margin_note discloses. Also surfaced, unprompted, the real risk this case's argument_a leans on (on-demand prices aren't rate-guaranteed; GPU supply constraints could break the Open Tap's assumption of always-available capacity at $6.88) as its strongest counter-argument. |
| P2 both-sides | **PASS** | `case.json.balance.argument_a`/`argument_b` were rewritten this pass to carry real quantitative content per SPEC §2's "strongest QUANTITATIVE argument" requirement — `tier2_probes.py --probe 2` initially FAILED mechanically ("argument B carries almost no numbers") on the pre-retune prose, fixed by this rewrite. Built the strongest case for each option independently: A leans on the real 56.8% full-utilization floor and the fact that D5's crossover (34.2%/yr) sits only 5.2 points above Appendix D's own High scenario, with DigitalOcean's own 2027 guidance (over 50%) already past it. B leans on D4's own six-result table, all favoring Open Tap, using a real mid-size company's own growth rather than a hyperscaler's. Neither collapses to a bare concession. |
| P3 trap check | **PASS** | Independently derived trap (jumping to "the Long Lock's rate is obviously cheaper" from Appendix B/C's raw rates alone, without ever running D4's cost-per-GPU-hour-delivered ratio) matches `FACILITATOR.md`'s "The trap" and Anchor 2's framing. A second, case-specific trap this retune introduces — a Hero who votes Open Tap at Anchor 1 on gut instinct alone (rather than the rate-comparison trap) happens to land on the *correct* option without ever running D4/D5 — is also named explicitly in `FACILITATOR.md`'s "The trap" section and P1's own solver output implicitly avoided it by actually running the arithmetic rather than stopping at the vote. |
| P4 twist integrity | **PASS** | The twist (DigitalOcean's own disclosed RPO growth and 2027 guidance, both already-cited via S4) genuinely unsettles a post-Data-Deep-Dive stance that treats Appendix D's own range as the entire space of plausible outcomes. Checked against every stated Modeling Assumption (MA1–MA3) under a natural reading: the twist depends on no ambiguous convention — it is a narrative reuse of already-fetched, unambiguous source figures (a percentage and a multiple, both point values), not an interpretation-dependent calculation, so there is no Cold-Chain-style hidden-convention failure mode. It does not flip D4/D5's arithmetic (confirmed: Open Tap still wins Low/Mid/High), matching `FACILITATOR.md`'s explicit statement that the twist reframes rather than resolves. |
| P5 sensitivity | **PASS (disclosed)** | Mechanically **FAILS** the stable-margin bar — the case is genuinely sensitive to a ±50% swing on both of its declared assumption dials (MA1, MA2): `n_gpus` at −50% and `starting_demand_gpu_hrs` at +50% both flip the winner from Open Tap to Long Lock (neither breaches the 20% cap in the non-flipping direction). This is disclosed, not hidden: `case.json.sensitivity_disclosure[]` now carries one entry per dial (both Category F — fictional-scenario constructions, since Kestrel doesn't exist and neither MA1 nor MA2 is independently sourceable), each with a real justification naming the exact flip mechanism, matching this project's established disclosure-aware pass state (`fret-board`, `cooling-curve`, `enclosure-call`). `tier2_probes.py --probe 5 --flex 0.5` now reports `PASS (disclosed)` mechanically. Note: P1's independently-blind solver named MA2 as the most sensitive assumption without seeing this disclosure — real convergent evidence, not circular. |
| P6 data decay | **PASS** | All 5 sources re-fetched live 2026-08-30. **S1/S2** (`instances.vantage.sh/aws/ec2/p5.48xlarge`): reachable, on-demand $55.040/hr and 3-year RI (No Upfront) $23.777/hr both confirmed verbatim (matches the case's $6.88/$2.97 per-GPU derivations to the cited precision). **S3/S4/S5** (`investors.digitalocean.com`, two distinct DigitalOcean IR press releases): both reachable; S3's "Revenue was $258 million, an increase of 22% year-over-year" confirmed verbatim; S4/S5's release confirmed both "year over year revenue growth of approximately 29%" and "compared to 14% growth in the same quarter of 2025" verbatim. No dead links, no drifted figures, no URL moves. |

**Overall Tier 2: 6/6 clear the gate (5 PASS, 1 PASS (disclosed)).** Combined with Tier 1 fully
clean (0 blockers, 0 gaps), this reaches **`TIER2_PASS`** per SPEC §2/MCS-26, matching this
project's own precedent in `fret-board`, `cooling-curve`, and `enclosure-call`.

### Remaining genuine judgment call for a human

**The retune reversed which option wins**, from Long Lock (every scenario, pre-retune) to Open Tap
(every scenario, post-retune). This is disclosed prominently in `case.json.balance.margin_note`,
`FACILITATOR.md`'s opening retune-history note, and here — not a quiet flip. A human should be
aware that **P5's disclosed instability is real**: this case's recommendation is genuinely fragile
to a ±50% swing on either MA1 or MA2, the same two dials that were deliberately left untouched by
this retune specifically so the fix would trace to better-sourced growth data rather than to
tuning the fictional-scenario assumptions closer to the cap edge. A human could reasonably choose
to also narrow MA1/MA2 for a wider safety margin against that instability — but the current state
is honest, well-sourced (two HIGH-confidence primary citations replacing three MEDIUM-confidence
proxies), and passes every gate as written. No further action is required to reach `TIER2_PASS`;
this note flags the option for a human who wants a wider safety margin, not a defect.

### Tier 3 — human dry-run
NOT RUN. (Out of scope for `case-readiness`.)

---

## case-readiness run — 2026-08-27 (remediation pass)
**State:** BLOCKED → BLOCKED   **Verdict:** BLOCKED (Tier 1 did not clear; Tier 2 not run)

This is a re-run after `case-write`-stage remediation of the three findings from the prior run
(2026-08-27, same day). Preflight lint, Tier 1, and this report were all re-run against the
updated `case.json`/`FACILITATOR.md`. `case.md` itself was **not** changed — its sha256 is
unchanged from the prior run.

Preflight lint (`preflight_lint.py --case compute-lease`, advisory, non-blocking) still flags the
same one finding as before, for the record, not counted against the gate: line 160 of `case.md`
contains an HTML comment naming "FACILITATOR ONLY" / "balance argument, margin, and sensitivity
notes" inside the student-facing file. It is a guard comment aimed at future editors, not text a
student would read in rendered output, so it is not itself a leak — but it does name the concepts
the leak-check exists to protect, so it remains worth a human's eyes.

### What changed since the prior run

1. **T1-09 remediated (arithmetic done, but the case is genuinely unbalanced).** Computed the
   D4/D5 arithmetic from the now-sourced Appendix B/C/D figures and recorded it in
   `case.json.balance` (`margin_pct`, `margin_basis`, `margin_note`) and in `FACILITATOR.md`'s
   Data Deep Dive / Twist sections. **Result: the case fails the SPEC §2 ~20% balance cap at every
   Appendix D growth scenario** — Low 36.5%, Mid 63.5%, High 76.4% — and the D5 crossover growth
   rate (≈2.5%/month) falls *below* Appendix D's entire stated 6%–13% range, meaning the Long Lock
   wins under every sourced scenario, not just some. This was cross-checked under a second,
   capacity-capped reading of "GPU-hours delivered" (Long Lock delivery capped at the physical
   512-GPU/730-hr ceiling) as a sanity check; it narrows the margin (34.5% / 45.1% / 48.0%) but
   does not bring any scenario under the cap or change which option wins. Full derivation is in
   `case.json.balance.margin_note`. **This is recorded honestly, not hidden or forced to a
   plausible-looking number** — matching the precedent set in `cases/fret-board/case.json`, which
   remains BLOCKED for the same class of reason. T1-09 therefore still reports FAIL, correctly:
   the check is not "was a number computed" but "is the case balanced," and it genuinely is not,
   as currently sourced.
2. **T1-11 fixed.** `case.json.deliverables[D6].skills` now maps to `["calculus-series"]` — D6
   ("a recommendation... defended with D4 and D5") cannot be produced by a competent student
   without reasoning about the D4/D5 series results directly, the same skill D2/D4/D5 already
   claim. T1-11 now PASSes.
3. **T1-13 fixed.** `FACILITATOR.md` was rewritten into the full SPEC §7.1 anchor ladder
   (Intro/Launch/Anchor 1–4/Data Deep Dive/Twist/Close/Lessons Learned/Standards Touched On), with
   Anchors 2–3 correctly preceding the Data Deep Dive. A real Twist was written — the case's own
   512-GPU physical capacity ceiling (already-sourced/assumed data, no new figures invented)
   crossing under customer demand partway through the 24-month window — rather than a `Twist: N/A`
   declaration, since the data to build a real one was already in the case. A timed 45-minute
   Socratic plan (§7.3) was added, naming the moment the twist drops. The prior draft's good
   content — Argument-for-A/B, the trap, the five Socratic questions, and the sensitivity note —
   was preserved and folded into the new structure rather than discarded. T1-13 now PASSes.
4. **T1-17 (GAP, not a blocker in the prior run) also closed.** `case.json.cohort_bands[]` now
   declares three bands (Full 12–18, Compressed 6–9, 1:1/pair 1–2) per SPEC §7.4's floor.

### Tier 1 — structural (20 checks)
| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length; no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Sofia..." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no Challenge numeral-form drift |
| T1-06 | PASS | appendices lettered, ordered, no orphans |
| T1-07 | PASS | final-appendix lines are verbatim spine labels |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | **FAIL** | SPEC §2 — margin is 63.5% (mid scenario) on the primary metric, cap ~20%. Genuine imbalance, honestly computed and recorded — see above and `case.json.balance.margin_note`. Not a missing-computation issue; a real balance-retune judgment call for a human. |
| T1-10 | PASS | new_coverage[] populated, no padding |
| T1-11 | PASS | D6 now maps to `calculus-series` — MCS-10 mutual reachability satisfied |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | PASS | full anchor ladder, real Twist, timed 45-min plan, 5 Socratic questions, trap named |
| T1-14 | PASS | CONTINUITY — balance figures now populated and consistent between case.json and FACILITATOR.md |
| T1-15 | PASS | no `published/` directory yet — nothing to drift |
| T1-16 | PASS | `case_md_sha256` recorded, matches |
| T1-17 | PASS | `cohort_bands[]` now declares 3 bands (MCS-25) |
| T1-18 | PASS | no `published/` directory — MCS-37 has nothing to check yet |
| T1-19 | PASS | no `published/` directory — MCS-39 has nothing to check yet |
| T1-20 | PASS | no `published/` directory — advisory, nothing to check yet |

`sha256(case.md)` at this run: `01b90eae28bc062f9564e39806414ffb8dabd0b349b6c09387b8c1611d3269d6`
(unchanged — `case.md` itself was not edited in this remediation pass).

### BLOCKER (1)

**1. [T1-09] SPEC §2 — the case is not balanced, on any Appendix D scenario.**
The D4/D5 arithmetic is now done and recorded (`case.json.balance.margin_pct = 63.5`,
`margin_note` carries the full derivation). The Long Lock beats the Open Tap on cost per
GPU-hour delivered at **every** growth scenario in Appendix D (Low 36.5%, Mid 63.5%, High 76.4%),
and the D5 crossover growth rate (≈2.5%/month) sits below the entire stated 6%–13% range. This
was cross-checked under an alternate capacity-capped delivery reading and the conclusion holds
either way (margins 34.5%/45.1%/48.0%, still over cap, same winner throughout). **This is not a
missing-arithmetic problem** — it is a genuine, honestly-computed SPEC §2 balance failure baked
into the case's current Modeling Assumptions (MA1 = 512 GPUs, MA2 = 120,000 GPU-hours/month
starting demand) and sourced rates (S1/S2 = $6.88 vs. $2.97/GPU-hr). **Exact fix needed:** a
human decides how to retune a constraint — e.g. a smaller committed cluster (MA1), a higher
starting utilization (MA2), or a narrower/higher growth-rate range in Appendix D — to bring the
margin under ~20% at the scenario the case is meant to be judged on. This is `case-write`-stage
retuning work (changing what the case's own assumptions/sources say), explicitly out of scope for
a QA/readiness remediation pass, which computes and discloses honestly rather than inventing a
retuned figure. **Flagged for human sign-off**, matching the precedent already set by
`cases/fret-board/case.json`, which remains BLOCKED on the identical class of finding.

### GAP (0)

None open. The prior run's two GAPs (`case_md_sha256` unset, `cohort_bands[]` empty) are both
resolved.

### Tier 2 — simulated play (6 probes)
NOT RUN. Tier 1 did not reach `TIER1_PASS` (1 open BLOCKER above), and per
`skills/case-readiness/SKILL.md`'s ladder, Tier 2 may only start after Tier 1 is clean.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | NOT RUN | blocked on Tier 1 |
| P2 both-sides | NOT RUN | blocked on Tier 1 |
| P3 trap | NOT RUN | blocked on Tier 1 |
| P4 twist | NOT RUN | blocked on Tier 1 |
| P5 sensitivity | NOT RUN | blocked on Tier 1; no `sensitivity_model.py` present yet either |
| P6 data decay | NOT RUN | blocked on Tier 1 |

### Tier 3 — human dry-run
NOT RUN.
