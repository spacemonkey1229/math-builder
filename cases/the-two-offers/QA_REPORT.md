## case-readiness run — 2026-09-03 (remediation pass)

**State:** BLOCKED → TIER1_PASS. **Verdict:** TIER1_PASS, Tier 2 clean (6/6 verdicts recorded,
0 mechanical failures, 0 unresolved findings).

This report supersedes the earlier 2026-09-03 run recorded at the top of this file's prior
version (9 Tier 1 blockers). All nine blockers were fixed by `case-write`/`case-research`
remediation; see "What changed," below.

### Tier 1 — structural (20 checks)
sha256(case.md) = `6700533b66bc036c20235ef966e1a321d57794559481b3aae98d91b484edd93b`

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview's one bare numeral ("1 a.m.") rewritten to "well after midnight" — no numerals left to clear |
| T1-03 | PASS | Dilemma binary, opens "You are Maya Ortiz." |
| T1-04 | PASS | Challenge 5 is verbatim boilerplate; the leaked `<!-- FACILITATOR ONLY -->` comment was removed |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | Appendix D ("Learn More") now referenced from Background ("SEE APPENDIX D") |
| T1-07 | PASS | final appendix (now Appendix F, reordered after Sources) contains only verbatim spine labels |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | `margin_pct` = 5.1 computed and recorded in both `case.json.margin_pct` and `balance.margin_pct` |
| T1-10 | GAP | `new_coverage[]` empty; downgraded from BLOCKER to GAP by the reinforcement carve-out — see `case.json.reinforcement_note` |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load |
| T1-13 | GAP | FACILITATOR.md now has the full anchor ladder, a justified `Twist: N/A`, a timed 45-minute plan, and 5 Socratic questions; only the Twist-is-N/A confirmation remains a GAP by design (MCS-15's non-blocking downgrade) |
| T1-14 | PASS | FACILITATOR.md numbers reconcile with case.json (margin_basis now states the intermediate arithmetic explicitly) |
| T1-15 | PASS | no `published/` dir — nothing to drift |
| T1-16 | PASS | `case.json.qa.case_md_sha256` updated to match the final case.md |
| T1-17 | PASS | `cohort_bands[]` declared (Full / Compressed / 1:1 pair) |
| T1-18 | PASS | (no `published/` dir) |
| T1-19 | PASS | (no `published/` dir) |
| T1-20 | PASS | (no `published/` dir) |

**BLOCKER (0). GAP (2), both documented carve-outs, not defects:**
- **[T1-10]** `new_coverage[]` is empty. `case.json.reinforcement_note` records that all 7 claimed
  skills already have `n>0` in `readmodel/standards_spine.json` (checked live 2026-09-03), that the
  6 skills in the entire spine with `n==0` are unrelated (number-sense/geometry-sphere/calculus),
  and that this case was approved specifically to reinforce the group's two thinnest skills
  (`system-of-equations`, `how-to-solve-a-system-of-linear-equations`, both n=2) while closing the
  Employment & Income topic gap — same evidentiary pattern as `cases/the-lease-break/case.json` and
  `cases/the-bracket-bet/case.json`.
- **[T1-13]** `Twist: N/A`, explicitly justified in FACILITATOR.md's Twist section: the case's
  tension is a fully-disclosed two-variable trade-off that resolves through the Challenge 3
  algebra itself, and introducing a genuine twist would require either leaking the margin's
  size/direction into case.md or inventing an unsourced figure, both forbidden. The D3 crossover
  reveal (many rooms expect ~a year; the real number is 6.41 months) is named as carrying the
  surprise-and-recompute function a Twist would otherwise serve.

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched to a fresh, unbriefed agent given only the packet (`/tmp/coldsolve-the-two-offers/PACKET.md`) and the 7 standard questions, with no access to FACILITATOR.md/case.json. It built both V(t) equations correctly (V_A=7500.83t+8663, V_B=6980t+12000), solved the system to the correct crossover (~6.41 months, ~$56,730 — matches `sensitivity_model.py`), named cumulative net value as its metric, and reached a defensible answer (A, for a "normal" tenure) with a genuine counter-argument (no time-discounting in the model) and a correctly-identified sensitive assumption (MA1). It also independently flagged the median-vs-75th-percentile bonus split as the least-supported figure — a real modeling choice already disclosed in `case.json.sources[S2].note`, not a hidden defect. |
| P2 both-sides | **PASS** | Rewrote `case.json.balance.argument_a`/`argument_b` to carry real numbers (previously prose-only, which the probe correctly flagged mechanically). Argument A: Cascadia's $520.83/month steeper slope overcomes its $3,337 day-one deficit by month 6.41 and leads by $9,163 (5.10%) at 24 months. Argument B: Northwind's $3,337 head start plus a real $313.33/month 401(k) match strictly wins for any tenure under 6.41 months. Each side has a specific, named question that collapses it (A collapses under "what if you leave within 6 months?"; B collapses under "what if you stay years?") — this is the intended tension, not a hidden weakness, and neither argument is a bare concession. |
| P3 trap check | **PASS (guide amended)** | Dispatched to a second fresh, unbriefed agent on the same packet. Its predicted trap (an asymmetric/inconsistent treatment of the two offers' recurring cash flows — e.g., excluding Northwind's 401(k) match as "not real income" while still subtracting Cascadia's commute cost, or a base-salary/12 unit slip) did **not** match the guide's original named trap (skipping the time-based model entirely for a day-one comparison) — a genuine unanticipated failure mode per the probe's own FAIL criterion. Rather than record a bare FAIL, `FACILITATOR.md`'s "The trap" section was amended to name this second, "inside the correct methodology" trap explicitly, with a cold-call instruction (check a Hero's D1 net-monthly-value line items, not just their final V(t)) for the facilitator to catch it. Verified Tier 1 still passes after the edit. |
| P4 twist integrity | **PASS (N/A confirmed)** | Twist is `N/A`, justified in FACILITATOR.md. Adversarially re-read every stated assumption and disclosure (MA1's commuting-cost basis; both companies' "not prorated or repayable" signing-bonus clauses; the 401(k) match's "no vesting delay stated" clause) for a Cold-Chain-style hidden convention that would silently break under an alternate reading — found none; all are stated as unconditional, symmetric-in-structure facts with no sequencing ambiguity. The N/A holds up. |
| P5 assumption sensitivity | **PASS** | `cases/the-two-offers/sensitivity_model.py` authored (contract: `PARAMS`, `evaluate(params)`, `FLEX=["commute_month"]` — the case's one stated modeling assumption, MA1). Flexing MA1 by ±50% keeps Option A the winner at the 24-month reference tenure with margins of 1.63%–8.58%, both inside the SPEC §2 20% cap; the crossover moves from ~4.3 to ~12.8 months but the multi-year winner never flips. Even a ±100% flex only flips the winner at the extreme +100% case (commute cost doubled to $1,040/month, well beyond the assumption's stated basis), and even then the margin is a near-tie 1.88%, not a landslide — consistent with the case's own disclosed sensitivity note in Appendix C/case.json. |
| P6 data decay | **PASS** | Fetched all 6 unique source URLs directly (this sandbox has outbound network access). All returned HTTP 200. Confirmed the cited figure is present in the fetched content for S1 (Robert Half: `96250` present in the page's embedded JSON), S2 (Pave: "Data Science" row shows `9%` / `15%` matching median/75th-percentile exactly), S4 (Vanguard: `4.7%` present), S5 (IRS: `72.5 cents` present), S6 (SpotHero: `$155` present). S3 (Levels.fyi) returned HTTP 200 on a HEAD-style check but 0 bytes of body on a full fetch — consistent with a bot-gated/client-rendered SPA, not a broken or moved page; this matches the source's own already-disclosed MEDIUM "self-reported/crowdsourced panel" confidence and is not treated as a new finding. |

**Resolution of the pre-existing "both-sides-collapse" concern** (flagged in the prior QA run,
before Tier 1 blocked): P2 and P5 together resolve it. The ~6.4-month crossover is real and the
$16,250/yr base-salary gap does drive it, but Argument B does not collapse — it is strictly correct
for any tenure under 6.41 months, a real and common early-career scenario, and the 24-month margin
(5.10%) stays comfortably inside the SPEC §2 cap under ±50% flexing of the case's only stated
assumption. This is a working two-sided case, not a landslide with a token second argument.

### Tier 3 — human dry-run
NOT RUN.

---

**Summary of what changed in this remediation pass:**
1. Removed the one non-texture numeral from the Overview ("1 a.m." → "well after midnight").
2. Deleted the leaked `<!-- FACILITATOR ONLY -->` HTML comment appended to Challenge 5.
3. Referenced Appendix D from Background, closing the orphan.
4. Reordered the appendices so the mandatory "How To…" standards appendix (relettered F) is last,
   after Sources (relettered E) — the old order let the parser's final-appendix capture bleed into
   the Sources table and derivation lines.
5. Computed `margin_pct` = 5.1 from the case's own sourced figures and recorded it in both
   `case.json.margin_pct` and `balance.margin_pct`, with the full derivation in `balance.margin_basis`.
6. Added `case.json.reinforcement_note` documenting the live zero-coverage check for T1-10.
7. Rewrote `FACILITATOR.md` in full: complete anchor ladder (Intro/Launch/Anchor 1-4/Data Deep
   Dive/Twist/Close/Lessons Learned/Standards Touched On), a justified `Twist: N/A`, a timed
   45-minute Socratic plan, 5 Socratic questions (single-line, each ending in "?"), and — after the
   Tier 2 trap-check finding — a second named trap variant covering an asymmetric-treatment/units
   error inside the correct methodology.
8. Declared `cohort_bands[]` (Full/Compressed/1:1) per MCS-25.
9. Added real numbers to `case.json.balance.argument_a`/`argument_b` (Tier 2 P2 finding).
10. Authored `cases/the-two-offers/sensitivity_model.py` for Tier 2 P5.
11. Updated `case.json.qa` (`case_md_sha256`, `verdict`, `tier2` verdicts) to match this run.
