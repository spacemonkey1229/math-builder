# QA_REPORT.md — The Surge Trigger

## case-readiness run — 2026-09-18

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (24 checks)

| id | result | note |
|---|---|---|
| T1-01 | PASS | seven structural sections present |
| T1-02 | PASS | Overview has no load-bearing numerals |
| T1-03 | PASS | Dilemma binary, opens "You are Dr. Renata Cho." |
| T1-04 | PASS | Challenges 1/2/4/5 verbatim boilerplate |
| T1-05 | PASS | no numeral-form drift |
| T1-06 | PASS | all appendices referenced, no orphans |
| T1-07 | PASS | final appendix (E) verbatim spine labels; POLISH note: 5 labels all bulleted |
| T1-08 | PASS | every number cited or declared an assumption |
| T1-09 | PASS | margin_pct = 10.12 computed and recorded in both case.json.margin_pct and balance.margin_pct |
| T1-10 | GAP | new_coverage[] empty; downgraded from BLOCKER to GAP by the reinforcement carve-out — see case.json.reinforcement_note |
| T1-11 | PASS | learning-goal mutual reachability |
| T1-12 | PASS | tier vs numeric load (T4: derivatives, functions, assumptions stated and defended) |
| T1-13 | PASS | FACILITATOR.md has full anchor ladder, twist, timed 45-minute plan, 5 Socratic questions, cohort bands |
| T1-14 | GAP | 1 number ("7.0") in FACILITATOR.md not in case.md/case.json — false-positive match on "SPEC Section 7" heading text, same precedented class as cases/the-approval-gate/QA_REPORT.md and cases/the-overlap-send |
| T1-15 | PASS | published/ artifacts built after case.md/FACILITATOR.md, no drift |
| T1-16 | PASS | case.json.qa.case_md_sha256 matches case.md |
| T1-17 | PASS | cohort_bands[] declared (Full / Compressed / 1:1 pair) |
| T1-18 | PASS | interactive HTML present, fresh, leak-free (balance_test verdict never printed as a static literal) |
| T1-19 | PASS | hover+hyperlink math glossary, 10 terms, all verified khanacademy.org links |
| T1-20 | PASS | (advisory) no chart/diagram image; text-based derivative work is the case's own visual medium, notebook computes live |
| T1-21 | PASS | STORY_GLOSSARY present (advisory GAP class, not BLOCKER per MCS-47) |
| T1-22 | PASS | published HTML's sections match case.md's |
| T1-23 | PASS | published HTML's inline `<script>` parses clean (`node --check`) |
| T1-24 | PASS | (see tier1_structural.py output) |

**BLOCKER (0). GAP (2), both documented, not defects:**
- **[T1-10]** `new_coverage[]` is empty. `case.json.reinforcement_note` records that all 5 claimed
  skills already have n>0 in `readmodel/standards_spine.json` (checked live 2026-09-18: chain-rule
  n=1, product-rule n=2, quotient-rule n=1, tangent-line-at-a-point n=2, local-maximum n=2), that
  every other skill in Calculus/Derivatives and Calculus/Applications Of Derivatives was checked
  and honestly ruled out, and that this case reinforces a genuinely thin cluster — same evidentiary
  pattern as `cases/the-approval-gate/case.json` and `cases/the-two-offers/case.json`.
- **[T1-14]** A false-positive number match on "SPEC Section 7" (the anchor-ladder subsection
  heading text in FACILITATOR.md) parsed as the bare number 7.0. Not a real drift — no actual
  figure in FACILITATOR.md is unsourced from case.md/case.json; every real derived number (t_A,
  t_B, lag, gap_cases, local_max_t, costs, margin) is present in `case.json.derived` and matches
  exactly. Same precedented false-positive class documented in `cases/the-approval-gate/QA_REPORT.md`.

### Tier 2 — simulated play (7 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | Dispatched to a fresh, unbriefed subagent given only the packet (`/tmp/coldsolve-the-surge-trigger/PACKET.md`). Its arithmetic matched `sensitivity_model.py` exactly: t_A≈10.41, t_B≈14.43, lag≈4.0 days, gap≈4.89 cases/day, cost(A)=$1,700 flat, cost(B)≈$1,526. It named "total expected cost" as its metric, then chose Option A anyway on an explicit, reasoned qualitative override (treating the pure-dollar metric as "a floor, not the full picture" because it can't price a false all-clear signal) — a defensible position with correct arithmetic, matching the same "certainty vs. cheaper-but-riskier" tension FACILITATOR.md's own Argument for A independently makes. Unprompted, it correctly named MA5 (the $1,700 verification cost) as both the most sensitive assumption and the least-supported figure — exactly the dial `sensitivity_disclosure[]` flags as Category X. |
| P2 both-sides | **PASS** | Dispatched to a fresh subagent reading only case.md. Built a real, numbers-driven best sentence for each side (A: certainty and a flat known cost vs. B's compounding, open-ended risk; B: I(t) is an unconfirmed model resting on challengeable assumptions, D(t) is the only curve the department can actually observe/defend). Found B's *safety* framing collapses specifically at D3's local-maximum finding (a falling reported curve does not mean the outbreak is slowing) — but confirmed B's *practical* no-model-dependence argument survives that collapse, and the total-cost comparison (D4) is what makes the inversion dollar-explicit. Neither side is a bare concession. |
| P3 trap check | **PASS** | Dispatched to a second fresh subagent, case.md first. Independently predicted the same central trap the guide names verbatim ("the reported curve is just the true curve, delayed" — a shifted copy, not a differently-shaped curve) before ever reading FACILITATOR.md, then confirmed the guide names it as the central trap and also independently surfaced the guide's own second trap (choosing on raw speed without pricing D4's actual costs). |
| P4 twist integrity | **PASS** | Dispatched to a fresh subagent with case.md, FACILITATOR.md, and case.json. (1) Confirmed the twist invalidates a real room position ("reported cases falling means the outbreak is slowing"). (2) Independently re-derived D(t)'s critical point from the case's own I(t)/c(t) formulas by hand — confirmed t*=32.695 exactly, confirmed the bracket k·c(t)−m is linear and strictly decreasing (exactly one sign change, so exactly one local maximum, not an artifact), and confirmed I'(t) is never zero (I(t) has no turning point at all, not just none in this window). Checked for alternate readings (unit ambiguity, c(t) domain floor) and found none that break the twist within the case's stated ~0–40-day window; flagged the unstated c(t)≥0 floor (valid to ≈43.33 days) as a latent-but-non-blocking fragility, not a twist failure. |
| P5 assumption sensitivity | **PASS (disclosed)** | `cases/the-surge-trigger/sensitivity_model.py` authored (contract: PARAMS, evaluate(params), FLEX=["verification_cost"] — the one assumption tested and found safe to sweep ±50%; I0/MA1 and c0,m/MA3 were tested and found structurally unsafe to flex — see sensitivity_model.py's FLEX[] comment — and are held fixed for the same documented reason `the-approval-gate` holds its own structural thresholds fixed). Base: A=$1,700.00, B=$1,527.92, margin 10.12% (winner B, lower cost). verification_cost is genuinely unstable: −50% FLIPS the winner to A (44.4% margin, breaks the 20% cap); +50% also breaks the cap (40.1% margin, B still wins). Both disclosed in `sensitivity_disclosure[]` as Category X — machine-verified PASS (disclosed), matching `tier2_probes.py`'s own printed verdict. |
| P6 data decay | **PASS** | Fetched all 4 unique `sources[]` URLs directly during case-research (same day, age 0d at QA time). S1 (PMC7392464, CDC *Emerging Infectious Diseases*) — reachable, quote-confirmed ("Li et al. covered cases reported by January 22 and found a doubling time estimate of 7.4 (95% CI 4.2–14) days"). S2 (PMC5769785, CDC *MMWR*) — reachable, quote-confirmed ($49,769 and $18,423 figures). S3 (mobilehealthmap.org) — reachable, quote-confirmed ("~$275,000" average annual operating cost). S4 (statista.com) — reachable, quote-confirmed ("$312... 2016-2017"). No dead links, no figure drift. |
| P7 accessibility | **PASS** | Mechanical pre-screen: no deliverable uses sketch/diagram/graph-type language requiring a matching visual (D1–D5 are derivative/algebra work, not drawing requests), so the mechanical check is a clean pass by construction. Model-judged cold-read: dispatched to a fresh, zero-context subagent against the packet built from the published Interactive HTML. Result: **0 unexplained real-world concepts** named under question 1 (every term — exponential growth, growth rate, testing capture rate, doubling time, chain/product/quotient rule, local maximum, tangent line, cost-per-case, mobile clinic operating cost — was either defined inline or ordinary math vocabulary), and **0** under question 2 (MCS-51: no central invented mechanism the reader couldn't visualize — the one mobile unit, two curves, and same-day redeployment call were all described concretely enough to picture clearly). Genuine PASS, no P7_waiver needed. |

### Tier 3 — human dry-run
NOT RUN.

---

**Summary of what this run did:**
1. Ran `case-write` + `case-research` together: wrote the case spine with all figures as
   `{{NEEDS_SOURCE}}` placeholders, then immediately filled every one — 2 real, sourced figures
   used directly (S1 informing the growth-rate constant; S4 used directly as the per-case cost),
   2 real supplemental sources (S2, S3) grounding the framing/informing an assumption's basis, and
   5 disclosed Modeling Assumptions (MA1–MA5) for figures no public source can carry for a
   fictional county.
2. Computed the case's real numbers via `sensitivity_model.py` (a numeric bisection root-finder,
   since the trigger-day equations are transcendental): t_A=10.406, t_B=14.434, lag=4.028,
   gap_cases=4.897, local max of D(t) at t=32.695, cost(A)=$1,700.00, cost(B)=$1,527.92,
   margin=10.12% (within the approved concept's 8–15% target).
3. Tested `sensitivity_model.py`'s FLEX[] scope directly: found I0 (MA1) and the capture-rate pair
   c0/m (MA3) structurally unsafe to sweep ±50% (they can push D'(t) out of ever crossing
   threshold_B, producing degenerate/negative results rather than a real answer) — held fixed with
   the same documented reasoning the corpus already uses for structural thresholds, rather than
   reporting a broken/nonsensical sweep. Only `verification_cost` (MA5) remained as a genuine,
   safely-sweepable dial; it is disclosed as unstable per P5 above.
4. Ran Tier 1 (`tier1_structural.py`): TIER1_PASS, 0 blockers, 2 documented GAPs (T1-10
   reinforcement carve-out, T1-14 known false-positive on a section-number heading).
5. Ran all seven Tier 2 probes — P1–P4 and P7 via fresh, independently-dispatched subagents with
   no access to FACILITATOR.md/case.json (except P4, which is explicitly a twist-integrity
   re-derivation against the case's own stated formulas and therefore reads all three files by
   design); P5 mechanically via `tier2_probes.py`; P6 directly (this session already had live
   fetch confirmations for all 4 sources from the research pass). All seven: PASS.
6. `case.json.qa` updated to `state: TIER2_PASS`, `verdict: PASS`, `blockers_open: 0`,
   `gaps_open: 2`, all seven Tier 2 verdicts recorded by name, hash current.

## Live browser audit — 2026-09-18

Per this project's own convention (text-only checks miss real rendering/behaviour bugs), the
published Interactive HTML was opened in a real browser (Claude_Browser tools) and clicked
through end to end, not just read as text.

**Confirmed working:**
- Page renders correctly (title block, tier/band pills, tab nav, Overview/Background prose).
- Working Notebook Steps 1-4: entering the correct computed values (I'(0)=0.376, t_A=10.41;
  D'(0)=0.1844, t_B=14.43; local-max day=32.695, D(32.695)=13.796; lag=4.03, gap=4.897,
  cost A=$1,700, cost B=$1,527.92) all returned a green check; entering wrong values (e.g. 99)
  correctly returned "try again" for every field tested — confirms the page's JS-ported
  `evaluate()` matches `sensitivity_model.py` to the cent.
- Twist reveal/apply: revealing the twist shows the narrative without ever printing a literal
  dollar figure (per MCS-37); checking "Recompute with the tightened verification-protocol cost"
  correctly changes Step 4's Option A grading target from $1,700.00 to $2,550.00 (confirmed via
  `evaluate_twist({})` returning `costA: 2550`, exactly matching the already-disclosed +50% flex
  result) — re-submitting the old $1,700 value after applying the twist correctly flips to "try
  again."
- No console errors on load or after interaction; the page's single inline `<script>` block
  parses clean under `node --check`.

**A real defect was found and fixed during this audit:** on first load, the math glossary
(Appendix E), the deliverables checklist, the auto-linked in-prose glossary terms, and the
CSV/PDF-per-table download buttons all rendered **empty** — despite the Working Notebook and
Twist toggle working correctly. Root cause, found via direct JS console inspection: `restorePick()`
(one of the very first top-level script statements to run after the case's own data block) calls
`localStorage.getItem()` unguarded; in an environment where `localStorage` throws (this browser
tool's file-preview sandbox is one real example — it renders local files as `data:` URLs, and
`data:` origins disable storage — but a real Safari private-browsing tab or a locked-down school
Chromebook profile can throw here too), the uncaught exception aborted every subsequent top-level
statement in the script: the `GLOSSARY`/`HOWTO` render, the deliverables checklist render, and the
CSV button wiring never ran, even though earlier-defined `onclick` handler functions (already
hoisted) kept working — exactly the "one uncaught error silently disables every later feature"
failure class this project's own doctrine (MCS-50/T1-23) already treats as a hard defect, except
this is a *runtime* exception rather than a *syntax* error, so `node --check` cannot catch it.

**Fix applied** (to `published/The Surge Trigger - Interactive.html` directly, not to the shared
`templates/interactive_shell.html`, since this is a per-case artifact): added a small defensive
`safeStorage` wrapper (`getItem`/`setItem`, each wrapping the real `localStorage` call in
`try/catch` with an in-memory `Map` fallback) immediately after the `CASE_ID` declaration, and
replaced all 11 raw `localStorage.getItem`/`setItem` call sites (dilemma-pick restore/save,
deliverables-checklist read/write, notebook-note save, and the submission-packet export) with
`safeStorage` equivalents. Re-verified after the fix: `node --check` still clean, and a fresh page
load now correctly renders 8 math-glossary terms, 4 how-to links, a populated deliverables
checklist, 12 CSV/PDF download buttons, and 2 auto-linked in-prose glossary terms, with zero
console errors — confirmed via direct DOM inspection in the live browser tab, not by reading the
file's source text. `tier1_structural.py` re-run clean afterward (unchanged `TIER1_PASS`, 0
blockers, 2 gaps).

**Residual note:** this fragility class (unguarded `localStorage` calls at page-load time) exists
in `templates/interactive_shell.html` itself (`restorePick()`, `renderChecklist()`'s reads,
`toggleChk()`/`saveNote()`'s writes, `exportSubmissionPacket()`'s reads) — every case built from
this shell inherits the same crash-on-blocked-storage risk. Fixing it in the shared template is
out of scope for a single case's QA pass; flagged here so a future shell-maintenance pass can port
the same `safeStorage` pattern upstream once, instead of every case re-discovering and re-patching
it independently.
