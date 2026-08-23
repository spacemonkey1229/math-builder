## case-readiness run — 2026-08-19
**State:** TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (19 checks)
Re-run this pass (`tier1_structural.py --case baseball-lineup`), matching the state already on file:

| id | result | note |
|---|---|---|
| T1-01..T1-17, T1-19 | PASS | 18/19 clean |
| T1-18 | GAP | 30 decorative numbers in the interactive HTML (icon viewBox coords, input `step=` attrs) outside the case.md/case.json number universe — same accepted false-positive class `INTERACTIVE_HTML_CONTRACT.md` documents for Cold Chain, not real drift |

BLOCKER (0) / GAP (1, above) / POLISH (1, T1-07 separator-run label parsing note, cosmetic).

`sensitivity_model.py` authored this run at `cases/baseball-lineup/sensitivity_model.py` — reproduces the case's own published base numbers exactly (Ash .514/424 AB, Venicia .475/451 AB, 8.2% margin) and the twist's slugging figures exactly (Ash .917, Venicia .958). See the file's docstring for what is and is not a legitimate FLEX dial in this case: Appendix A's player stats are given/cited data (not swept, per P6/FLEX-scoping doctrine), Appendix C Assumption 1 (AB excludes walks) is a cited real-baseball convention (not an authorial dial), so `FLEX = ["avg_round_decimals", "margin_from_rounded"]` — the two genuine author-chosen conventions Appendix C, Assumption 2 actually states.

### Tier 2 — simulated play (6 probes)
| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh subagent (no access to FACILITATOR.md/case.json/QA_REPORT.md), reading only the leak-free packet, chose **A (Ash)**, reproduced the case's exact arithmetic (218/424=.514 vs 214/451=.475), correctly named batting average as its optimized metric with sound reasoning for why, and — unprompted — flagged that the metric choice itself is the fragile point and that swapping to slugging could flip the recommendation (independently anticipating the case's own twist). Correct answer for the right reasons. |
| P2 both-sides | PASS | Option A: Ash's lineup posts a real .514 combined AVG (8.2% edge) built around Swensen (.630) and Jacoby (.615), the two hottest bats on the whole roster, neither on Venicia's list — a strong, quantitative, non-concession argument. Option B: Venicia's lineup posts 39 HR vs Ash's 24 (62.5% more) and a .958 team SLG vs .917 (4.5% edge), anchored by Poppins (14 HR in 72 PA, individual SLG 1.292, the single most dangerous bat on either roster) whom Ash did not pick. Neither side collapses under pressure — both survive a "what's your best number and does it hold up" challenge; the case's own `balance.margin_basis` names this exact irresolution as the intended discussion, not an oversight. |
| P3 trap | PASS | A second fresh subagent (case.md only, no FACILITATOR.md/case.json access) named the trap unprompted: computing combined batting average, finding Ash ahead, and stopping — treating that first number as the whole answer while batting average "completely erases" extra-base power (Poppins' 14 HR/8 3B) and ignores walks. This is exactly what FACILITATOR.md's "The trap" section names: "A Hero computes combined batting average, finds Ash ahead, and stops... watch for a pitch that reports one statistic and calls the case closed." Independent match. |
| P4 twist | PASS | `evaluate()`/`evaluate_twist()` mechanically recomputed (script's automatic recompute branch didn't fire because `case.json` has no top-level `facilitator.twist` key for this legacy case, so this was done by hand from the model): base winner **A** (.514 vs .475, 8.2%), twist winner **B** (.958 vs .917, 4.5%) — the winner flips, satisfying "does the twist invalidate a position a real room would hold." The twist recomputes slugging (total bases / AB) from the *same* Appendix C definitions (AB excludes walks, 3-decimal rounding) already governing the base metric — no undisclosed convention is needed to make it work, and it survives every natural reading of Appendix C's stated assumptions. No BLOCKER. |
| P5 sensitivity | PASS | `tier2_probes.py --probe 5 --flex 0.5` against `sensitivity_model.py`. Swept the 2 declared `FLEX[]` dials (`avg_round_decimals`, `margin_from_rounded`) ±50%. Base: A=.514, B=.475, margin 8.2%. All 4 flexed rows: winner stays **A** in every case, margin moves only from 8.2% to 8.2%–8.5% (rounding-noise scale), no 20% cap breach. `machine_status: PASS`, zero flips, zero unstable params. This case's real inputs (Appendix A's fixed roster stats) are given/cited, not an authorial scenario choice, so there is genuinely little to destabilize the verdict — a legitimate finding, not a thin test. |
| P6 data decay | PASS | `case.json.sources[]` is empty (legacy case; Appendix A is the case's own fixed dataset, not an externally-cited figure), so the formal fetch worklist is empty — nothing load-bearing to decay-check. As additional diligence, fetched all 5 optional Appendix D "Learn More" links live: MLB.com Glossary (reachable, batting-average definition confirmed verbatim-consistent with Appendix C), FanGraphs/THT "Constructing Lineups" (reachable, on-topic), Wikipedia "Batting Order (baseball)" (reachable, on-topic), Sports Betting Dime sabermetrics guide (reachable, on-topic). The Khan Academy counting-principle video URL could not be confirmed by the fetch tool (client-rendered SPA returns only a bare page shell) — reported as **NOT FOUND / inconclusive per MCS-21**, not asserted dead or alive. None of these 5 links are load-bearing (Appendix D is explicitly optional background, not a source for any Appendix A/B figure), so the inconclusive result is not a BLOCKER, but is named here rather than silently passed over. |

### Tier 3 — human dry-run
NOT RUN

## case-publish run — 2026-08-22
Built the missing packet artifacts: `Baseball Lineup - Facilitator Guide.docx` and
`Baseball Lineup - Data.xlsx` (student-facing `Case Study.docx`/`Interactive.html` already existed
and were spot-checked, not rebuilt — no `FACILITATOR ONLY`/trap leak found in the Case Study docx).
`MANIFEST.json` written. `tier1_structural.py --case baseball-lineup` re-run after the build:
**0 BLOCKER, 2 GAP, 1 POLISH.**

- **T1-18 GAP** — pre-existing, unchanged (30→29 decorative CSS/SVG decimals in the interactive
  HTML outside case.md/case.json's number universe; same accepted false-positive class documented
  for Cold Chain in `INTERACTIVE_HTML_CONTRACT.md`).
- **T1-15 GAP (new)** — `[45.0]` in the new Facilitator Guide docx has no match in case.md/case.json.
  This is the "45-Minute Run of Show" heading/schedule (0:00–45:00), reproduced verbatim from
  FACILITATOR.md's own "45-minute Socratic plan" table. `T1-14`'s check on FACILITATOR.md itself
  already has a regex that strips `\d+\s*-?\s*minute` facilitation-timing idioms before flagging
  orphan numbers, precisely because session-duration figures are guide-only scheduling metadata,
  not case data, and are expected to have no home in case.md/case.json. `T1-15`'s docx-continuity
  sweep has no equivalent strip, so it flags the same legitimate class of number that T1-14 already
  forgives. Not real drift — no case.md/case.json edit would remove it without deleting the run-of-show
  schedule itself. Accepted as a GAP, same disposition as T1-18's.
- **T1-15 staleness check: clean.** Facilitator Guide docx was built after the current case.md/
  FACILITATOR.md, no CONTINUITY STALE blocker.

No BLOCKERs. Packet is publish-ready per `case-publish` SKILL.md step 1; read-model promotion
(step 2) and Drive push (step 3) were not run in this pass — build-only per the requesting task.
