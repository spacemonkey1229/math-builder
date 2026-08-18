# QA Report — Six Degrees of Exposure

## case-readiness run — 2026-08-15

**State:** DRAFT → TIER1_PASS   **Verdict:** TIER1_PASS (0 blockers, 1 gap)

### Pre-Tier-1 work done this run

- Confirmed `case.md` ships zero `{{NEEDS_SOURCE}}` placeholders (`grep -c NEEDS_SOURCE` = 0);
  `case.json.needs_source[]` shows all 15 tokens as `status: "SOURCED"`.
- Confirmed `case.json.standards[]` / `new_coverage[]` — all 5 spine ids resolve, and since this
  is a fresh-authored case (no `legacy_conversion_note`), the T1-10 legacy carve-out does not and
  should not apply: `new_coverage[]` here is a real, substantial claim (5 skills, all genuinely
  forced by D1–D4 per `LEARNING_GOALS.md`'s bidirectional check), not padding.
- Authored `sensitivity_model.py` from scratch. FLEX-scoping decision, documented in the file's own
  docstring: only `n_wide` (Wide Net's headcount, Appendix E MA3) is swept. `n_hub` is a stated
  MA3 assumption too, but is **not** included in FLEX — Appendix B publishes the exact real top-50
  result (27,643 weight from 5,859 distinct edges) but not the full 13,838-edge list, so there is
  no honest way to recompute weight-eliminated for a different-sized hub set without fabricating a
  number the case's own published data can't support. This mirrors the reference model's treatment
  of structural-but-unflexed constants (BOXES_A/BOXES_B). MA1 (which real network stands in for
  Calloway County's) and MA2 (edge-weight interpretation) are correctly excluded from FLEX as
  categorical/non-arithmetic per the FLEX-scoping doctrine note (2026-08-13) — MA2 explicitly
  doesn't change the arithmetic per the case's own text, and MA1 isn't a numeric dial.
- Verified `evaluate({})` reproduces case.json's stated figures exactly: A = 27643.0,
  B = 27366.7, margin (A−B)/A = 1.00% — matches `case.json.margin_pct` = 1.0 and
  `case.json.balance.margin_basis` exactly.
- Ran a preview ±50% sweep on `n_wide` by hand (not a formal Tier 2 P5 run, which is out of scope
  for this pass): n_wide=250 → B=14,720.9 (A wins, no flip); n_wide=750 → B=37,937.4 (B wins — a
  genuine flip). This is flagged here as a real finding for whoever runs Tier 2 P5: the margin is
  extremely thin (1.0%) and a +50% swing in Wide Net's headcount alone is enough to flip the
  verdict. This is consistent with, and does not contradict, `case.json.modeling_assumptions`
  MA1's own sensitivity note about how fragile the primary-metric margin is.
- Built `published/Six Degrees Of Exposure - Interactive.html` from `templates/interactive_shell.html`
  per `INTERACTIVE_HTML_CONTRACT.md`: real case-specific Overview/Background/Dilemma/Challenges/
  Appendices A–G, a rendered Appendix B (full real top-50 table) and Appendix C (real subgraph, SVG
  diagram + weighted-edge table), a 5-step Working Notebook (degree of a vertex, weighted-edge sum,
  live counting-argument calculator for Wide Net's expected value, the D3 budget-consistency check,
  and the D4 shortest-notification-path check), and a JS port of `sensitivity_model.py`'s
  `PARAMS`/`FLEX`/`evaluate()` kept in sync by hand. No twist reveal exists for this case (see
  FACILITATOR.md's `Twist: N/A` — the pedagogical surprise is structural, the per-head/per-budget
  trap, not a narrative event), so "The Trap" section reuses the shell's reveal-gate mechanism
  instead of a numeric twist recompute.
- Rewrote `FACILITATOR.md` to add the full MCS-14 anchor ladder (Intro/Launch/Anchor 1–4/Data Deep
  Dive/Twist/Close/Lessons Learned/Standards Touched On, in the required order, Anchors 2–3 before
  the Data Deep Dive), a real 45-minute timed Socratic plan naming the trap's moment, and 5
  single-line Socratic questions (the original multi-line wrapped questions did not match Tier 1's
  line-scoped regex). The original file had none of the MCS-14/15/16 mechanical structure and would
  have been a hard BLOCKER as first drafted.

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | |
| T1-02 | PASS | |
| T1-03 | PASS | |
| T1-04 | PASS | |
| T1-05 | PASS | |
| T1-06 | PASS | |
| T1-07 | PASS | POLISH: separator-run parse found 0 (Appendix G's vocab is bulleted here, not middot-separated — not applicable to this case) |
| T1-08 | PASS | |
| T1-09 | PASS | margin_pct = 1.0, within the 20% cap |
| T1-10 | PASS | new_coverage[] is real (5/5 skills genuinely forced); no legacy carve-out claimed or needed |
| T1-11 | PASS | mutual learning-goal reachability confirmed by LEARNING_GOALS.md |
| T1-12 | PASS | T3 tier matches numeric/probabilistic load (4 deliverables, counting-argument probability content) |
| T1-13 | GAP | MCS-15 — Twist section present and reads "Twist: N/A" with a written justification (this case's surprise is structural, delivered as "The Trap," not a staged narrative reveal); Tier 1 flags this pattern for human confirmation by design, not as an error |
| T1-14 | PASS | continuity confirmed after fixing one orphan number (a since-removed "0–3 cases" aside) |
| T1-15 | PASS | published HTML built after case.md's last edit |
| T1-16 | PASS | case_md_sha256 recorded and current |
| T1-17 | PASS | cohort_bands[] declared with size + note for all 3 bands |
| T1-18 | PASS | interactive HTML present, fresh, no balance_test.margin_pct leak found |
| T1-19 | PASS | 8 glossary terms, all https://mathsisfun.com, all fetched and confirmed live this session |

BLOCKER: none. GAP: 1 (T1-13, Twist: N/A — human confirmation invited, not required to close).
POLISH: 1 (T1-07, informational).

### Tier 2 — simulated play (6 probes)

NOT RUN this pass — out of scope for this authoring/gating run per the task instructions (Tier 1
only). Flagged for the next `case-readiness` run: P5 (assumption sensitivity) will need to record
the real instability noted above (n_wide +50% flips the verdict) rather than a bare PASS/FAIL.

### Tier 3 — human dry-run

NOT RUN.

### case.json.qa (set by this run)

```json
{"state": "TIER1_PASS", "verdict": "PASS", "run_on": "2026-08-15", "blockers_open": 0,
 "gaps_open": 1, "case_md_sha256": "3eb9c08bb9e24eacc07fe2144e07334c1be5e64510f07f6bfdf6d136426327cb"}
```

**Next step:** Run Tier 2 (`tier2_probes.py --case six-degrees-of-exposure`) before `case-publish`.

## case-readiness run — 2026-08-17 (Tier 2)

**State:** TIER1_PASS → **BLOCKED**   **Verdict:** BLOCKED (Tier 2: 3 of 6 probes FAIL)

### Tier 1 reconfirmation

Re-ran `tier1_structural.py --case six-degrees-of-exposure`. Still clean: 17 PASS, 2 GAP
(T1-13 twist-N/A justification — present and written out; T1-14 orphan-number sweep — 9
guide-only derived numbers, e.g. `0.45737`, `10.1`, `552.9`, not mirrored into
`case.json.derived`), 0 BLOCKER, 1 POLISH. `case_md_sha256` unchanged:
`3807c30d2861e53e794ef00b4c70aa25715b1bdb8271b8ec6aaed1791ce62cbe` — matches
`case.json.qa.case_md_sha256`, no drift.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | Fresh subagent chose **B** (Wide Net); the case's intended winner is **A** (Hub Sweep) by 1.0%. The subagent's arithmetic is internally correct and its metric-naming is correct — but it could not get closer than an estimate for Hub Sweep's exact weight-eliminated, because **`case.md` never gives students the number they need.** D3 asks for "the total weight of every edge with at least one endpoint in [Hub Sweep's] vaccinated set," but Appendix B publishes only the top-50's *summed degree* (6,241, explicitly flagged as double-counting) — not the 27,643-weight, 5,859-distinct-edge figure the case's own `balance` block uses to declare A the winner. That exact figure exists nowhere in `case.md`. The subagent's honest, disclosed proxy (mean network edge-weight × 6,241) landed at ≈26,993 — below Wide Net's rigorously-derivable 27,366.7 — which is why it picked B. Because the true margin (1.0%) is thinner than the gap between "exact 27,643" and the best estimate a student can build from the given appendices (~2.3%), **the packet does not actually support the precision its own graded answer requires.** This is not solver error; it is a data-completeness gap in the case as authored. (Separately: the published interactive HTML — `published/Six Degrees Of Exposure - Interactive.html` — does contain the exact `27,643` figure, hard-coded into its `PARAMS.hub_weight_50` and also spelled out in body text inside the "Trap" reveal panel ("...compare Step 3's answer to Appendix B's 27,643"). That panel is guarded only by "ask your facilitator before revealing" — a self-service click, not a real gate — so a self-guided or absent student (Challenge 5 explicitly provides for this) can reveal the answer instead of deriving it. T1-18's leak screen does not catch this because it only pattern-matches `balance_test.margin_pct` literals, not this figure.) |
| P2 both-sides | **FAIL** | Built the strongest quantitative case for each option directly from `case.md`. Wide Net's case is rigorous end-to-end (closed-form hypergeometric counting argument, no missing inputs). Hub Sweep's case collapses at exactly the question P1 also hit: "state Hub Sweep's total weight-eliminated with the same rigor." The packet supports only an estimate for that number, and the estimate is not obviously an upper bound (hub-adjacent edges are plausibly above the network mean, so a mean-weight proxy can underestimate) — so Side A cannot be stated with the confidence its 1.0%-margin "win" implies. SPEC §2's balance test is not really passed: the recorded margin is a fact about data the case-writer had, not data the room has. |
| P3 trap | **PASS** | The case's real trap (per-*head* vs per-*budget*) is present in the packet's own framing ("judged on a single number... per dollar of the shared budget") and is named explicitly by `FACILITATOR.md`'s "The trap" section, which describes exactly what a learner will do wrong (compute weight/head, see Hub Sweep "win" by ~10×, stop). A model working from the packet alone independently identifies this same per-head/per-budget conflation as the likely wrong path. Matches. |
| P4 twist | **PASS** | No live twist; `FACILITATOR.md` states `Twist: N/A` with a written structural justification (the per-head/per-budget reversal does the twist's job without a fictional event) — T1-13's GAP is exactly this pattern, confirmed present and written out. This probe passes on its own terms; the interactive HTML's leak of the trap's payoff number is reported under P1, not here, since it is a solvability/leak defect, not a twist-vs-assumptions integrity defect. |
| P5 sensitivity | **PASS (disclosed)** | `tier2_probes.py --probe 5 --flex 0.5`: base state A=27643.0, B=27366.74, A wins by 1.0%. Sweeping the one declared `FLEX` dial (`n_wide`, Appendix E MA3) ±50%: at −50% margin balloons to 87.8% (breaks the 20% cap); at +50% the verdict **flips to B** and margin is 37.2% (also breaks the cap). This is a genuine, real instability — but it is disclosed exactly where SPEC §2/MCS-19 require: `case.json.sensitivity_disclosure[]` names `n_wide`, states the swing flips the winner and breaks the cap, and gives the justification (Calloway County's real 50/500 split is not public record, so it is fixed as the county's stated plan rather than derived). Qualifies for the disclosure-aware pass state, not the stable-margin state. |
| P6 data decay | **FAIL** | S1 (`pmc.ncbi.nlm.nih.gov/articles/PMC9532365/`) — reachable, confirms "$38" median / "$9 to $206" range verbatim. PASS. S3 (`snap.stanford.edu/data/CollegeMsg.html`) — reachable, confirms Nodes 1899 / Temporal Edges 59835 / Time span 193 days verbatim. PASS. **S2 (`https://www.cdc.gov/eid/article/31/7/24-1827_article`) — DEAD as cited: returns CDC's "Page Not Found" page (`www.cdc.gov` host).** The article is real and still live, but only at the `wwwnc.cdc.gov` host — `https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article` — confirmed reachable there, and it still states "Labor cost per contact was estimated at $175.94 (range $79.97–$293.51)" verbatim, matching the case's cited value exactly. Per house doctrine, a URL that 404s while its figure is load-bearing (S2 feeds Appendix D's $175.94 and the derived $213.94 fully-loaded Hub Sweep cost, which is half of the Deep-Conflict-thread-2 discrepancy discussion) is a BLOCKER even though the figure itself is unfabricated and the correct URL is one host-prefix away. `case.json.sources[1].url` and `case.md`'s Appendix F / footer link both need updating to `https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article`. |

### Tier 3 — human dry-run

NOT RUN.

### Blockers to close before re-running Tier 2

1. **[P6]** Fix S2's dead URL in `case.json.sources[]` and every place `case.md`/the published HTML cite it (`https://www.cdc.gov/eid/article/31/7/24-1827_article` → `https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article`).
2. **[P1/P2]** Close the D3 data gap: either (a) publish the number D3 actually asks for — Hub Sweep's exact 27,643-weight, 5,859-distinct-edge result — into `case.md`'s Appendix B (not just the interactive HTML's hidden `PARAMS`), so a cold solver working from the packet can state Side A's number with the same rigor as Side B's; or (b) rewrite D3's ask so it explicitly calls for an *estimate* of Hub Sweep's total weight (with a stated method, e.g. mean-edge-weight proxy) rather than "the total weight... with the full arithmetic shown," and disclose in `case.json` that the exact figure is not derivable from the published appendices. Either fix also removes the interactive HTML's incentive to leak `27,643` inside the "Trap" panel.
3. **[P1, secondary]** Once (2) is fixed, re-gate or remove the interactive HTML's plain-text disclosure of `27,643` inside `#twist`'s reveal panel (`published/Six Degrees Of Exposure - Interactive.html`, `onTwistToggle()`), since a self-guided/absent student (Challenge 5) can currently self-reveal the exact deliverable answer with one click.

**Next step:** Hand to `case-write`/`case-research` to close the 3 blockers above, then re-run
`case-readiness` Tier 2 in full (all six probes) before `case-publish` may run.

## case-readiness run — 2026-08-17 (Tier 2 re-gate)

**State:** BLOCKED → **BLOCKED** (unchanged). None of the three prior blockers have been closed;
this run reconfirms Tier 1 and re-runs all six Tier 2 probes with fresh evidence.

### Tier 1 reconfirmation

Re-ran `tier1_structural.py --case six-degrees-of-exposure`. Still clean: 16 PASS, 3 GAP, 0
BLOCKER, 1 POLISH. `case_md_sha256` unchanged:
`3807c30d2861e53e794ef00b4c70aa25715b1bdb8271b8ec6aaed1791ce62cbe` — matches
`case.json.qa.case_md_sha256`, no drift. (T1-10 is now a GAP rather than PASS relative to the
2026-08-15 run — the 2026-08-17 reinforcement-carve-out doctrine amendment changed how an empty
`new_coverage[]` is scored; not a regression in this case's own content.)

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | A fresh cold-solve result was supplied for adjudication this run, but it does not cold-solve this case's actual dilemma. The case's cold-solve packet asks the solver to choose between Operation Hub Sweep (A) and Operation Wide Net (B) using D1–D4's counting-argument and budget arithmetic over Appendices A–G, and to name the metric it optimized (weight-eliminated per dollar of shared budget). The supplied result instead reports on an unrelated exercise — matching the literal digit "1" against three regex strategies run over a "PACKET.md" description as "a case with no margin_pct field at all," measuring the false-positive rate of a bare-digit leak-detector fallback. It names no `chosen_option` of A or B answering this case's dilemma, does no arithmetic over this case's actual appendices, and names as its optimized metric "false-positive rate of the P1 bare-digit fallback match" — not this case's balance metric. This does not meet SKILL.md's P1 pass criterion ("the solver reaches a defensible position, with correct arithmetic, and can name the metric it optimised" — of *this case's* dilemma). Scored FAIL: no valid cold-solve of Six Degrees of Exposure has been produced. Separately, and independent of this scoring: even a genuine cold-solve attempt would still hit the same data-completeness gap recorded in the prior run below (Appendix B never publishes Hub Sweep's exact 27,643-weight/5,859-edge result that D3 asks for), which remains unfixed. |
| P2 both-sides | **FAIL** | Unchanged from the 2026-08-17 run above — re-confirmed by inspection this run: Appendix B (`case.md` lines ~135-160) still publishes only the top-50 list and its double-counted degree sum (6,241), not the 27,643-weight/5,859-distinct-edge figure `case.json.balance` uses to declare Hub Sweep (A) the winner. Side A still cannot be stated with the rigor its 1.0% "win" implies from the packet alone. |
| P3 trap | **PASS** | Unchanged. `FACILITATOR.md`'s "The trap" section still names the per-head vs. per-budget conflation explicitly and matches what a packet-only read independently surfaces as the likely wrong path. |
| P4 twist | **PASS** | Unchanged. `Twist: N/A` with a written structural justification stands; T1-13's GAP is this exact pattern, confirmed present. |
| P5 sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --case six-degrees-of-exposure --probe 5 --flex 0.5`: base A=27643.0, B=27366.74, A wins by 1.0%. `n_wide` ±50%: −50% → margin 87.8% (breaks 20% cap); +50% → verdict **flips to B**, margin 37.2% (breaks cap). Identical to the prior run. `case.json.sensitivity_disclosure[]` still names `n_wide`, states the flip and the cap breach, and gives the justification — qualifies for the disclosure-aware pass state. |
| P6 data decay | **FAIL** | Fetched all three `sources[]` URLs live this run. S1 (`pmc.ncbi.nlm.nih.gov/articles/PMC9532365/`) — reachable, confirms "Median cost per vaccination was $38... range from $9 to $206" verbatim. PASS. S3 (`snap.stanford.edu/data/CollegeMsg.html`) — reachable, confirms "Nodes: 1899, Temporal Edges: 59835" and "Time span: 193 days" verbatim. PASS. **S2 as cited (`https://www.cdc.gov/eid/article/31/7/24-1827_article`) — still DEAD, now returning HTTP 403 (previously a "Page Not Found" page; same underlying defect, wrong host).** `https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article` is confirmed reachable and still states "Labor cost per contact was estimated at $175.94 (range $79.97–$293.51)" verbatim, matching the cited value exactly — but `case.json.sources[1].url` (line 49) and `case.md`'s Appendix D/F citation (line 240, `[cdc.gov](https://www.cdc.gov/...)`) still cite the dead `www.cdc.gov` host. Unfixed since the prior run. BLOCKER per house doctrine (load-bearing figure behind a 404/403-ing URL). |

### Blockers still open (none of the three closed since 2026-08-17's first Tier 2 run)

1. **[P6]** S2's URL is still cited as `https://www.cdc.gov/eid/article/31/7/24-1827_article` in both `case.json.sources[1].url` and `case.md` line 240. Fix to `https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article` in both places (and the published HTML if it also cites the old host).
2. **[P1/P2]** Appendix B still does not publish Hub Sweep's exact weight-eliminated result (27,643, 5,859 distinct edges) that D3 asks for — only the double-counted top-50 degree sum (6,241). Either publish the exact figure into `case.md` Appendix B, or rewrite D3 to explicitly call for a disclosed estimate.
3. **[P1, secondary]** The published interactive HTML (`published/Six Degrees Of Exposure - Interactive.html`, lines 606, 642, 1116) still hard-codes and displays the literal `27,643` inside the Trap/twist-reveal panel, self-revealable with one click. Still needs re-gating once (2) is resolved.

### Tier 3 — human dry-run

NOT RUN.

### case.json.qa (set by this run)

```json
{"state": "BLOCKED", "verdict": "BLOCKED", "run_on": "2026-08-17", "blockers_open": 3,
 "gaps_open": 3, "tier2": {"P1": "FAIL", "P2": "FAIL", "P3": "PASS", "P4": "PASS",
 "P5": "PASS_DISCLOSED", "P6": "FAIL"},
 "case_md_sha256": "3807c30d2861e53e794ef00b4c70aa25715b1bdb8271b8ec6aaed1791ce62cbe"}
```

**Next step:** Close the 3 blockers above (dead S2 URL; Appendix B data gap; interactive-HTML
leak of 27,643), then re-run `case-readiness` Tier 2 in full before `case-publish` may run. The
P1 cold-solve step in particular must be re-dispatched as a genuine fresh subagent working from
`PACKET.md` and the seven questions `tier2_probes.py --probe 1` prints — not substituted with an
unrelated technical exercise.

## case-readiness run — 2026-08-17 (Tier 2 re-gate #2)

**State:** BLOCKED → **BLOCKED** (unchanged). S2's dead URL is now fixed (P6 flips to PASS), but
the core P1/P2 data-completeness blocker is still open, so the gate does not clear.

### Tier 1 reconfirmation

Re-ran `tier1_structural.py --case six-degrees-of-exposure`. Clean: 16 PASS, 3 GAP, 0 BLOCKER, 1
POLISH (T1-10 reinforcement carve-out; T1-13 Twist: N/A justification; T1-14 9 guide-only derived
numbers not mirrored into `case.json.derived` — same as prior run, unfixed but not blocking).
`case_md_sha256` = `aae86028bd6a4ad40ddc9cc8ee775ba3b80f50e7188e792a5bb6fb5e94dde562` — matches
`case.json.qa.case_md_sha256` exactly, no drift.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **FAIL** | A fresh cold-solve result was supplied for adjudication: `chosen_option` = A (Hub Sweep), metric named as weight-eliminated per dollar of shared budget, with arithmetic citing "Hub Sweep 27,643 vs Wide Net's expected 27,366.74." Scored against SKILL.md's pass criterion ("reaching the intended answer by the wrong route is a FAIL"): **FAIL, for the same data-completeness reason as the prior run, now directly re-confirmed against the actual dispatch packet.** Re-generated `PACKET.md` via `tier2_probes.py --probe 1` and grepped it: Appendix A gives only network-wide summary stats (1,899 vertices, 13,838 edges, 59,835 total weight, mean/median/max/min degree) and Appendix B gives only the top-50 degree-ranked list plus its explicitly double-counted sum (6,241) — the packet contains no path from those numbers to the exact "27,643" / "5,859 distinct edges" figure the supplied answer states as Hub Sweep's total weight-eliminated. That figure exists nowhere in the packet; it matches `case.json.balance`'s internal record exactly, which a solver confined to `PACKET.md` cannot have derived without either the full 13,838-edge adjacency list (not published) or access to the answer key. The supplied result also does not answer the dispatch's 7 required questions in order (arithmetic shown, strongest counter-argument, most-sensitive assumption, an appendix item ignored, least-supported number) — it reads as case-level QA adjudication reasoning, not a worked student solve. Both defects independently fail the probe. This is the same root cause flagged in the 2026-08-17 first and second Tier 2 runs (Appendix B data gap) and it remains unfixed in `case.md`. |
| P2 both-sides | **FAIL** | Re-confirmed directly against current `case.md`: Appendix B (lines 135–169) still publishes only the top-50 candidate list and the double-counted 6,241 degree sum — not the 27,643-weight/5,859-distinct-edge figure `case.json.balance` uses to declare Hub Sweep (A) the winner. Wide Net's case (Side B) remains fully rigorous — a closed-form hypergeometric counting argument with no missing inputs. Side A still cannot be stated with the same rigor its 1.0% "win" implies from the packet alone; the recorded margin is still a fact about data the case-writer had, not data the room has. Unchanged from both prior Tier 2 runs. |
| P3 trap | **PASS** | Re-confirmed. `FACILITATOR.md`'s "The trap" section still names the per-head (≈10.1×, Hub Sweep favored) vs. per-budget (≈1% margin) conflation explicitly, with the exact arithmetic (552.9 vs 54.7 weight-eliminated per dose) a room would compute first. Matches the wrong path a packet-only read independently surfaces. |
| P4 twist | **PASS** | No live twist. `FACILITATOR.md` states `Twist: N/A` with the same written structural justification (the per-head/per-budget reversal does the twist's job without a fictional event), confirmed present at the "## Twist" heading. Twist N/A → PASS per this run's instructions. |
| P5 sensitivity | **PASS (disclosed)** | Re-ran `tier2_probes.py --case six-degrees-of-exposure --probe 5 --flex 0.5`: base A=27643.0, B=27366.74, A wins by 1.0%. Sweeping the sole declared `FLEX` dial (`n_wide`): −50% → margin 87.8% (breaks the 20% cap); +50% → verdict **flips to B**, margin 37.2% (also breaks the cap). Identical to both prior runs — a genuine, real instability. `case.json.sensitivity_disclosure[]` still names `n_wide`, states the flip and both cap breaches, and gives the Category-X justification (Calloway County's real split is not public record). Qualifies for the disclosure-aware pass state per SKILL.md's P5 rules. |
| P6 data decay | **PASS** | Fetched all three `sources[].url` live this run. **S1** (`https://pmc.ncbi.nlm.nih.gov/articles/PMC9532365/`) — reachable, confirms "Median cost per vaccination was $38... from $9 to $206" verbatim (Table 2: Median $38, Min $9, Max $206). PASS. **S2** (`https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article`) — **now resolves cleanly at the corrected `wwwnc.cdc.gov` host** (the prior `www.cdc.gov` 404/403 is fixed in both `case.json.sources[1].url` and `case.md` line 240); confirms "the mean labor cost for contact investigation from the 10 studies was $175.94... 95% nonparametric bootstrapped CI... $79.96–$293.51" — matches the case's cited $175.94 and upper bound $293.51 exactly; the case's stated lower bound ($79.97) is one cent off the source's exact CI floor ($79.96), an immaterial rounding difference, not a load-bearing discrepancy. PASS. **S3** (`https://snap.stanford.edu/data/CollegeMsg.html`) — reachable, confirms "Nodes 1899", "Temporal Edges 59835", "Time span 193 days" verbatim. PASS. All three sources current (accessed 2026-08-13, within the 365-day freshness window) and none flagged for staleness. |

### Blockers still open

1. **[P1/P2]** Appendix B still does not publish Hub Sweep's exact weight-eliminated result (27,643, 5,859 distinct edges) that D3 asks students to show "with the full arithmetic" — only the double-counted top-50 degree sum (6,241). A cold solver confined to the packet cannot reproduce the case's own graded answer. Fix: either (a) publish the exact figure into `case.md` Appendix B (or provide the full 13,838-edge list / an equivalent honest derivation path), so Side A can be stated with the same rigor as Side B's closed-form counting argument; or (b) rewrite D3 to explicitly call for a disclosed *estimate* of Hub Sweep's total weight (with a stated method) rather than "the full arithmetic shown," and disclose in `case.json` that the exact figure is not derivable from the published appendices.
2. **[P1, secondary]** The published interactive HTML (`published/Six Degrees Of Exposure - Interactive.html`, lines 606/642/1116) still hard-codes and displays the literal `27,643` inside the "Trap"/twist-reveal panel, self-revealable with one click by an absent/self-guided student (Challenge 5 provides for this). Needs re-gating once blocker 1 above is resolved — either the figure becomes legitimately derivable (making the reveal safe) or the reveal needs a real gate, not a self-service click.

### Blockers closed since the prior run

- **[P6]** S2's dead URL is fixed: both `case.json.sources[1].url` and `case.md`'s Appendix D/F citation now point to `https://wwwnc.cdc.gov/eid/article/31/7/24-1827_article`, confirmed live and carrying the cited $175.94 figure. P6 verdict flips FAIL → PASS.

### Tier 3 — human dry-run

NOT RUN.

### case.json.qa (set by this run)

```json
{"state": "BLOCKED", "verdict": "BLOCKED", "run_on": "2026-08-17", "blockers_open": 2,
 "gaps_open": 3, "tier2": {"P1": "FAIL", "P2": "FAIL", "P3": "PASS", "P4": "PASS",
 "P5": "PASS_DISCLOSED", "P6": "PASS"},
 "case_md_sha256": "aae86028bd6a4ad40ddc9cc8ee775ba3b80f50e7188e792a5bb6fb5e94dde562"}
```

**Next step:** Close the 2 blockers above (Appendix B data gap; interactive-HTML leak of 27,643,
contingent on how blocker 1 is resolved), then re-run `case-readiness` Tier 2 in full — P1 in
particular must be re-dispatched as a genuine fresh subagent working strictly from a freshly
generated `PACKET.md` and answering the seven required questions in order, not a summary
adjudication of the whole case — before `case-publish` may run.
