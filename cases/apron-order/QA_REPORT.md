## case-readiness run — 2026-08-12

**State:** DRAFT → TIER1_PASS → TIER2_PASS   **Verdict:** PASS

### Tier 1 — structural (19 checks)

First run: 1 BLOCKER (Overview numeral "6" from "6 AM," not auto-classified as clock/year) plus 5
GAPs (Overview under the 150-300 word range; Option B fuzzy-match not found in Background; `standards[]`
vs. final-appendix mismatch left over from an earlier vocabulary rescope; no `case_md_sha256` yet —
expected on a first run). All resolved: Overview reworded to "6:00 in the morning" (clears the
clock-time auto-classifier) and expanded with sensory/dialogue detail into range; Option B's
`case.json` label reworded from an abbreviated "yd/apron," token to "yards fabric," a word that
appears verbatim in Background, resolving the fuzzy-match false positive; Appendix G's leftover
Decimal/Percent/Ratio/Unit vocabulary and the extra `convert-unit` how-to line (stale from an
earlier draft) removed to match the 6 actually-claimed fraction skills, and a `**Vocabulary
terms**` heading added (this case honestly claims none) to satisfy the two-part-list structural
check; `case_md_sha256` recorded. A later fix (see P4 below) added `derived.twist_material_a_usd`
to keep a new FACILITATOR.md figure spine-checkable. **Final run: 0 BLOCKERs, 0 GAPs.**

### Tier 2 — simulated play (6 probes)

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | PASS | Fresh agent read only the packet, reached Option A with correct arithmetic ($212.00 vs $232.00, 8.62% margin), and independently cross-validated its own answer against Appendix F's stated ±50% wage sweep (2.00%-13.64%) — exact match. Correctly named total dollar cost as the optimized metric and MA1 (the $16/hr labor rate) as the most-sensitive assumption and least-supported number, matching the case's own design intent. |
| P2 both-sides | PASS | Both sides built and defended with real, quantified numbers pulled from the document (A: $32.00 labor saved vs $12.00 material saved, net $20.00/8.62%; B: $12.00 material savings and 1⅔ yd less waste, real but scoped to a materials-only claim). The agent independently recomputed all base totals from raw Appendix A/C/D figures before trusting the case's stated numbers, confirming the margin is not a paper number — B collapses specifically at D7's total-cost question, which is the case's own designed pressure point. |
| P3 trap | PASS | Fresh agent, reading case.md only, predicted the exact trap before reading the guide: stopping at D5's waste comparison and never pricing D7's marking time, wrongly concluding Cut Open (less fabric) is cheaper overall. FACILITATOR.md names this identical trap near-verbatim. No second, unanticipated trap found. |
| P4 twist | **findings, then fixed** | A fresh agent independently recomputed the twist's dollar effect from case.md's raw figures (not trusting FACILITATOR.md's stated result) and confirmed $230.00/$232.00/0.86% exactly. It then found two real issues: (1) FACILITATOR.md's twist description said "some pieces come out upside-down," leaving genuinely ambiguous whether the ⅛ yd/apron penalty applies to all 40 aprons or a subset — material at a margin this thin (0.86%). **Fixed**: reworded to state the ⅛ yd/apron figure is a flat, batch-averaged allowance applied uniformly across all 40 aprons. (2) Composing the twist with MA1's own already-disclosed ±50% wage sensitivity band reveals a breakeven wage of exactly $15.00/hr — $1 below the $16 base assumption — below which Option B becomes cheaper even under the twist. This was true of the model all along (not a new defect) but had never been surfaced; **added** as a facilitator-only note in FACILITATOR.md's Twist section (not a base-case change) since MA1 itself states the $16 rate is unverified "mid-teens" wage data, a range that plausibly includes $15 or less. Both fixes strengthen, rather than change, the case's core teaching point that this margin is thin enough to be a real judgment call. |
| P5 sensitivity | PASS | Base case (`evaluate()`, ceiling-collapse transform, same pattern as Plaza Pavers/Company Front/Vent Cap): A=252.0, B=232.0 → margin 8.6%, A cheaper. Sweep of the sole FLEX dial (`wage_per_hr`) ±50%: margin ranges 2.0%-13.6%, no flips, no cap breaks. |
| P6 data decay | PASS | S1 (Fabric Depot bolt price) and S2 (Wikipedia seam allowance) both fetched live 2026-08-12, same day as authoring. S1: page confirms "Bleached White Cotton Muslin Woven 25 YD Bolt Fabric," $90.00 ($3.60/yd) — exact match. S2: page confirms 5/8in (1.5cm) as a standard commercial-pattern seam allowance, at the upper end of a stated 1/4-5/8in home-sewing range — supports the claim; noted as a minor nuance (5/8in is the range's upper bound, not the only value in use) rather than a data-decay defect. S3 (FreeSewing) cited for existence-of-the-domain context only, not a load-bearing figure. |

### Tier 3 — human dry-run

NOT RUN — no real cohort available in this session. This case is **not `VERIFIED`, only
`PUBLISHED`-eligible** — should not be marked ✅ in `DOCTRINE_LEDGER.md` until a real guide files a
`RUN_REPORT.md` from an actual cohort.

### Minor accepted polish note

Same informal-internal-terms note carried from Plaza Pavers/Company Front/Vent Cap's QA reports
(Appendix F's sensitivity note references "Tier 2 probe 5" and `sensitivity_model.py` in
student-facing text) — present here too, doesn't leak any answer or twist, flagged for the same
future cross-case editing pass rather than a one-off fix.

### Waived GAPs at publish (`case-publish` gate, 3 total, 0 BLOCKERs — see `MANIFEST.json.waived_gaps`)

- **T1-15** (published/Apron Order - Data.xlsx, Facilitator Guide.docx): 3 xlsx cells (22.5, 28.0,
  36.0) and 1 docx number (10.0) flagged as absent from `case.md`/`case.json`'s number universe.
  Root cause confirmed by direct inspection: the checker's `NUM_RE` cannot parse a digit run
  immediately followed by a Unicode vulgar-fraction glyph (`22½`, `28½`, `36⅝` never register as
  `22`/`28`/`36` in `numbers_in()`, since Python's `\w` matches the fraction glyph and blocks the
  regex's negative lookahead) — a pre-existing limitation of the shared checker script, not a data
  defect (the xlsx values themselves are correct, verified against Appendix A/C by hand). The
  docx's `10.0` is `"10:00"` in the 45-minute Socratic plan's time-block table, confirmed by direct
  inspection of the paragraph/table text — a schedule marker, not case data.
- **T1-18** (published/Apron Order - Interactive.html): numbers 19, 37, 39 flagged in prose outside
  `<script>`. Confirmed by direct text search these come from unmodified shell-template boilerplate
  referencing check ids `T1-19`/`MCS-37`/`MCS-39` (present verbatim in the Vent Cap reference file
  this HTML was built from), not case-specific content.
- Independently re-verified the interactive HTML's balance-test leak surface by hand (stricter than
  the mechanical T1-18 scan): `8.62`, `0.86`, `212`, `212.00`, `232`, `232.00`, `230`, `230.00`
  appear nowhere in the file, including inside `<script>` — every figure is computed live from
  `PARAMS`/`GEOM`, never hardcoded as a verdict.
