# QA Report — Speed Climbing

## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

sha256(case.md) = `cdfc055fc7f17e60583f17ce2057c6ca8a24cb169a5d1ce9311ed123c8c4d936` (final, after the
P6 Appendix E correction below — Tier 1 was re-run clean against this exact hash)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview length/no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Carlos Chen." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | numeral form |
| T1-06 | PASS | appendices lettered/ordered, no orphans |
| T1-07 | PASS | final appendix verbatim spine labels |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | balance test: both arguments, margin 3.9% ≤ 20% |
| T1-10 | GAP | new_coverage[] empty — legacy-conversion carve-out (see case.json.new_coverage_note) |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier T3 vs numeric load |
| T1-13 | PASS | facilitator guide, anchor ladder, twist, timed plan, sensitivity note |
| T1-14 | PASS | continuity — FACILITATOR.md agrees with case.md/case.json |
| T1-15 | PASS | no published/ yet, nothing to drift |
| T1-16 | PASS | hash matches (re-run after the P6 correction) |
| T1-17 | PASS | cohort-size bands declared |
| T1-18 | PASS | no published/ yet |
| T1-19 | PASS | no published/ yet |

**BLOCKER (0)**

**GAP (1):** T1-10 (legacy-conversion new_coverage carve-out, expected and documented).

**POLISH (4):** T1-07 (all 14 final-appendix labels are bulleted, none from a separator run — not
a defect, just a note on how the legacy script would have parsed it), T1-15/18/19 (no `published/`
directory yet — nothing to check).

**VERDICT: TIER1_PASS**

---

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | fresh subagent, packet only — see below |
| P2 both-sides | PASS | see below (worked directly) |
| P3 trap | PASS | fresh subagent — see below |
| P4 twist | PASS | fresh subagent — see below |
| P5 sensitivity | PASS | machine-run, 0 flips, 0 cap breaches — see below |
| P6 data decay | PASS (1 fix applied) | fetch subagent — see below |

**P2 (both-sides-solve, worked directly, mechanical prescreen READY after fixing `argument_b`'s
digit density — see below):**

- *Argument for A, best single sentence:* "This roster is provably the fastest team The Summit can
  field on today's data — every other choice costs real seconds on race day, and nothing in the
  parents' letter changes what the stopwatch says." A does not collapse under pressure: it is the
  *mathematical optimum* of the stated metric by construction (8 fastest official times), so no
  counter-argument can show a faster legal roster exists. It survives the Twist too — recomputed,
  A's own bench (alternate Jane, 8.47) costs only +0.27 combined points, the smallest possible
  degradation available from this data.
- *Argument for B, best single sentence:* "For about a second and a half of combined team time —
  3.9% — you keep both team captains, both climbers your own teammates trust most under pressure,
  and the two athletes actually getting faster fastest (Gertrude +23.3%, Jane +21.8%), none of which
  a stopwatch-only metric can see." B does not fully collapse either — it holds a real, quantified
  position throughout — but it has one genuine, specific pressure point: **at the Twist**, B's own
  bench (alternate Victoria, 8.70) is measurably weaker than A's (Jane, 8.47) — B's combined
  composite degrades by +1.47 vs. A's +0.27, roughly 5.4× worse. This directly undercuts one
  popular pro-B claim ("a character-based team handles adversity better") on this specific metric,
  for this specific injury. B's available rebuttal is real but partial: the absolute gap (0.47s on
  one team) is small, and "resilience" was never claimed to mean "identical backup speed."
- *Which side collapses first, and at which question:* **Neither fully collapses.** B is
  pressure-tested hardest, and cleanly, at exactly the Twist's bench-depth question — that is a
  real, disclosed vulnerability (see `sensitivity_note`), not a paper margin. Since B's numeric
  position survives with a genuine (if partial) rebuttal rather than folding, the recorded 3.9%
  margin is not a paper number — SPEC §2's balance test holds. **PASS.**

**P1 (cold solve, fresh subagent, packet only — `/tmp/coldsolve-speed-climbing/PACKET.md`):**
Genuinely fresh solve. The solver's **first instinct was the exact wrong path** (rank by Appendix
A's single fastest trial climb, tempted by Kylie's 6.89s) — then self-corrected by actually reading
Appendix D/F before committing, exactly the intended behavior for a careful reader. Final answer:
chose **A**, metric = combined team-composite score, arithmetic matches the case's own reference
model **exactly** (30.82s combined; Team 1 15.10, Team 2 15.73; consistency ranges Emily 0.13/
Gertrude 0.15/Jesse 5.89/Kylie 7.61; 6-month trends Emily +17.18%/Gertrude +23.29%/Rebecca +17.92%/
Ava −17.86%/Kylie −7.03% — all independently re-derived, not copied). Named the metric, showed
correct arithmetic, named the strongest counter-argument (Ava's 0.36s cut margin is within normal
run-to-run variance), correctly identified MA1 (most-recent-month vs. all-time-best) as the most
load-bearing assumption and specifically named Ava and Kylie as the two athletes it swings, ignored
National Ranking with a sound justification (populated for only 3/12), and flagged Appendix B's
"Best Practice" single-month snapshot as the least-supported figure. **Reached the answer by the
right route. PASS.**

**P3 (trap check, fresh subagent):** independently predicted the exact same trap as
`FACILITATOR.md`'s "The Trap" section — ranking off Appendix A's single-fastest-trial-climb instead
of Appendix D's mandated Appendix B metric, naming the same two athletes (Kylie, Jesse) and the same
outlier mechanism, unprompted. Full match, no divergence to adjudicate. **PASS.**

**P4 (twist integrity, fresh subagent):** independently re-derived both rosters and both team
assignments from Appendix A/B data and Appendix D/F's rules (not trusting `case.json`'s stated
numbers) and confirmed they match exactly, with no unstated convention required — MA2's
alternating-seed rule is unambiguous, and Appendix D's "the alternate's time doesn't count unless
she replaces a teammate" pins the substitution to each team's own alternate. Confirmed the twist
breaks a specific, plausible belief (that the 4th roster name is a formality, not a real backup
plan). Found one genuine arithmetic nit: the originally-stated post-twist margin (5.14%) was
computed from rounded display values rather than full precision (correct value 5.16%) — **fixed**
in `case.json.derived` and `FACILITATOR.md` (both now read 5.16%; see `RESEARCH_LOG.md`-adjacent
fix history). Also flagged "percentage points" as loose phrasing for a relative-percent figure —
**fixed** in `FACILITATOR.md` to read "percent." Neither finding changes the winner, the
pedagogical point, or the twist's soundness. **PASS.**

**P6 (data decay, fetch-capable subagent, all 4 URLs live-fetched):** S1 (wall specs), S2 (women's
WR), S3 (men's WR) all fully confirmed — reachable, and the cited figures appear verbatim on the
page. S4 (USA Climbing) was reachable and confirmed the core claim (Speed is a real, currently-run
discipline at Youth Nationals) but could **not** confirm the additional "seeding-round-then-bracket
format" detail this case originally cited alongside it — that phrase does not appear on the fetched
page. Per house doctrine ("a URL that resolves but no longer carries the figure is worse, because
nothing else in the pipeline would ever notice"), **fixed**: removed the unconfirmed detail from
both `case.md` Appendix E and `case.json.sources[]` S4's `claim`/`note`, leaving only the
directly-confirmed fact cited. None of S1-S4 are load-bearing for any calculation in the case
(real-world-grounding context only), so this fix has zero effect on the math, the balance test, or
any deliverable. **PASS (after one correction, applied).**

**P5 (assumption-sensitivity, machine, `sensitivity_model.py`):** swept all 8 declared
character-rubric weight dials (`captain_pts`, `mentor_pts`, `trust_survey_pts`, `discipline_pts`,
`multiyear_pts`, `nationals_pts`, `culture_pos_pts`, `culture_neg_pts`) at ±50%. **0/16 flips,
0/16 broke the 20% cap** — base margin ranged 3.8%–6.7% across every flex. This is a genuinely
robust finding: Option B's roster composition (and therefore the balance test) does not depend on
the exact point values chosen for the facilitator's reference rubric — the gaps between climbers'
character scores are large enough that reasonable reweighting doesn't reorder the top 8. **PASS.**

### Tier 3 — human dry-run

NOT RUN. This is expected — `case-readiness` stops at `TIER2_PASS`, which licenses `case-publish`
but not a Tier 3 dry-run (that requires the case to actually be published and run with real
learners first).

---

## Final verdict

**State: TIER2_PASS.** Tier 1 clean (0 BLOCKERs, 1 disclosed/expected GAP). All six Tier 2 probes
recorded, 0 FAIL, one real (non-blocking) correction applied during P4 and one during P6, both
fixed before this report was finalized. `case.json.qa` records
`{"state": "TIER2_PASS", "verdict": "PASS", "blockers_open": 0, "tier2": {"P1":"PASS","P2":"PASS",
"P3":"PASS","P4":"PASS","P5":"PASS","P6":"PASS"}}` with the current `case_md_sha256`.

**Per this project's task instructions, case-publish is explicitly NOT run.** Next step, if/when
authorized: `case-publish` on `speed-climbing`.
