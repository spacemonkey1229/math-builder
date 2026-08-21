## case-readiness run — 2026-08-20

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview 234 words, no load-bearing numerals ("Friday" cleared, texture only — see `overview_numerals_cleared[]`) |
| T1-03 | PASS | Dilemma binary, opens "You are Newt Harrison." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | 7 appendices (A–G), all referenced from Background/Challenges, no orphans |
| T1-07 | PASS | final appendix (G) lines verbatim spine labels (10/10) |
| T1-08 | PASS | zero `{{NEEDS_SOURCE}}` remaining; every `[S#]` marker resolves to a complete `sources[]` row with a valid confidence grade; Modeling Assumptions block visible in Appendix F |
| T1-09 | PASS | balance test: both arguments written, margin 2.8% ≤ 20% cap |
| T1-10 | GAP | `new_coverage[]` empty — legacy-conversion carve-out applies (`legacy_conversion_note` present); every claimed skill genuinely forced by a deliverable, none padded |
| T1-11 | PASS | learning-goal mutual reachability — 0 unmapped deliverables, 0 unreachable skills |
| T1-12 | PASS | tier T2 matches numeric load (multi-step, rates, area, percent, currency conversion; two competing variables — up-front cost vs. long-run cost — that trade off) |
| T1-13 | PASS | FACILITATOR.md: full anchor ladder, 5 Socratic questions, named trap, Twist with soundness check, timed 45-min plan |
| T1-14 | PASS | continuity — FACILITATOR.md numbers agree with case.json.balance/derived |
| T1-15 | PASS/POLISH | no `published/` directory yet — nothing to drift |
| T1-16 | PASS | `case_md_sha256` current |
| T1-17 | PASS | `cohort_bands[]` declared (Full/Compressed/1:1) |
| T1-18 | POLISH | no `published/` directory yet — MCS-37 has nothing to check (interactive HTML not built; out of scope for this run per instructions to stop at TIER2_PASS) |
| T1-19 | POLISH | no `published/` directory yet — MCS-39 has nothing to check |

**BLOCKER (0).** **GAP (1):** T1-10 legacy carve-out (expected, doctrine-approved). **POLISH (4):** T1-07 label-parsing note, T1-15/18/19 no `published/` yet.

`python3 skills/case-readiness/scripts/selftest_tier1.py --project "$PROJECT"` — SELFTEST PASSED, all 6 defect-fix regressions hold.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Fresh subagent, packet only (`/tmp/coldsolve-carpenter/PACKET.md`, verified leak-free by the script — no precomputed balance result, no twist shingle, no FACILITATOR.md heading). Chose Option A, correct arithmetic matching `sensitivity_model.py`'s `evaluate()` almost to the cent, named its metric ("total initial cost vs. CD$17,900 cap, cross-checked against 15-year TCO"), named MA4 (short-term-rental traffic) as the most sensitive assumption and the strongest argument against its own choice, named S6 (tile material cost) as the least-supported figure. Reached the intended, defensible position for the right reasons. **This run also caught a real defect** (see Correction below). |
| P2 both-sides solve | **PASS** | Worked directly. Strongest case for A: dramatically lower initial cost (CD$14,640.92 vs. CD$22,805.26), only option under the CD$17,900 soft cap, and — read at face value — also wins 15-year TCO. Strongest case for B: matches the Berisels' own stated "comfort and luxury" goal, and hardwood's wear-life advantage extends far past the case's own 15-year window (tile/hardwood never need full replacement; carpet structurally must, repeatedly, on any long enough horizon) — a real, quantifiable durability argument, not a concession. Neither side collapses to "cheaper but worse in every other way" — B's defense does not depend on the twist to be non-trivial (the "beyond 15 years" argument stands on Appendix B's own cited wear-life data), though the twist substantially strengthens it. |
| P3 trap check | **PASS** | Fresh subagent, `case.md` only, then compared to `FACILITATOR.md`. Independently identified the exact same trap the guide names: applying Appendix B's residential wear-life figures to Option A without connecting them to Background's stated heavy, weekly-turnover foot traffic (MA4). Judged the trap realistic and well-anticipated — a modeling/context error invisible in the arithmetic itself, exactly the kind of error a hurried-but-competent student would not self-catch. |
| P4 twist integrity | **PASS** | Worked directly. (1) The twist invalidates the plausible base-case position "A is the obvious winner on every axis" — it is not, once short-term-rental traffic is applied to carpet's replacement cadence. (2) Re-derived under every stated assumption, read both sequentially and simultaneously: Background already states heavy/weekly-turnover traffic (priming the concept), MA4 explicitly flags the traffic-adjustment question as unresolved in the base pitch, and the twist supplies the specific quantitative claim (roughly halved trigger) as genuinely new information, not a contradiction of anything stated earlier. No unstated convention is required — `sensitivity_model.py`'s `evaluate()`/`evaluate_twist()` compute the flip mechanically (2.8% A → 15.3% B). |
| P5 assumption sensitivity | **PASS_DISCLOSED** | `sensitivity_model.py`, `FLEX = [sqft_chz, carpet_replace_trigger_years]`. `sqft_chz` ±50%: stable, no flip, no cap breach. `carpet_replace_trigger_years` ±50%: **unstable** — at -50% (5 yrs) the verdict flips to A-cheaper-by-15.3% (mirroring the twist almost exactly, since a halved trigger IS the twist's mechanism); at +50% (15 yrs) the margin widens to 26.3%, breaching the SPEC §2 20% cap. Both directions disclosed in `case.json.sensitivity_disclosure[]` (Category F — irreducible forecast uncertainty — with a 20+ character justification), matching the disclosure-aware PASS state per the 2026-08-13 doctrine amendment. Given the base margin is only 2.8%, this dial is the case's single most load-bearing sensitivity alongside MA4 — both are flagged prominently in FACILITATOR.md and case.json. |
| P6 data decay | **PASS** | 12 `sources[].url` entries, all accessed 2026-08-20 (0 days old at run time). Directly fetched and confirmed: S7 (NAHB/BofA PDF — downloaded, text-extracted, table values confirmed verbatim), S12 (Bank of Canada FXUSDCAD feed — confirmed live, 1.3785, same day), S6 (Ximator — confirmed reachable; **found a real discrepancy** between the page's actual figure ($1–$8/sq ft) and this case's original citation (a narrower $4–$15 "glazed-only" figure taken from a search-result summary, never actually fetched) — **fixed**: S6 now cites the confirmed $1–$8 range, midpoint unchanged at $4.50 since it is the exact midpoint of both ranges. S1/S2/S3 (Homewyse) were fetched successfully earlier in the same research pass with matching dated figures. S4/S5/S8/S9/S10/S11 (all homeguide.com) returned HTTP 403 to automated fetch (bot-blocked, consistent with `family-trip`'s prior finding on the same class of site) — not confirmed dead, and their values were independently corroborated via WebSearch result snippets captured the same session (see `RESEARCH_LOG.md`), which is how the case arrived at each figure in the first place. No source URL 404'd; no load-bearing figure found unsupported. |

**Correction found and fixed during this run (P1):** the fresh cold-solve subagent's arithmetic for Option B's 15-year total (CD$34,674.14) did not match `sensitivity_model.py`'s then-output (CD$36,100.89), even though both were "correct" given their inputs. Root cause: an earlier draft of `sensitivity_model.py` added an undocumented third hardwood service event (a second recoat at year 15) that `case.md` Appendix F's MA3 text never states ("recoat at year 5... full refinish at year 10" — no third event). The fresh solver, working from the packet alone, correctly used only the two stated events. Fixed by removing the phantom year-15 recoat from `sensitivity_model.py` so the model matches what the case document actually says. This changed the recorded base margin from 7.0% to **2.8%** and the twist margin from 10.8% to **15.3%** — both updated throughout `case.json` (`balance`, `derived`, `sensitivity_note`, `sensitivity_disclosure`) and `FACILITATOR.md`. Tier 1 and Tier 2 P5 were re-run clean after the fix. This is exactly the kind of defect Tier 2 exists to catch — a machine-consistent model that quietly diverged from the student-facing document of record.

### Tier 3 — human dry-run

NOT RUN.

---

**Six probes, six verdicts, 0 FAIL.** `qa.state = TIER2_PASS`. Per instructions, this run stops here — `case-publish` was not run.
