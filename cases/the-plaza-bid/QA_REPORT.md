## case-readiness run — 2026-09-01

**State:** researched → TIER1_PASS → TIER2_PASS   **Verdict:** TIER2_PASS

### Tier 1 — structural (20 checks)

Remediation this session: fixed the T1-10 BLOCKER by adding `reinforcement_note` after checking
the full Geometry/Basic Operations/Advanced Numbers domains — only one `n==0` skill exists
project-wide (sphere volume), irrelevant to a tessellation/tiling case, so this genuinely
reinforces Plaza Pavers' skill set rather than padding. Added `(SEE APPENDIX H)` reference.
Recorded `qa.case_md_sha256`.

`VERDICT: TIER1_PASS (0 blockers, 2 gaps: T1-10 reinforcement carve-out, T1-14 1 guide-only
derived number)`.

### Tier 2 — simulated play (6 probes)

Fixed a real P3 mechanical FAIL: FACILITATOR.md's line 30 said "(see the Trap, below)" — an
earlier, forward-reference use of the word "trap" that the mechanical trap-parser matched *first*
in the file (it takes the first occurrence), truncating the captured trap text to an unrelated
sources list and missing the real, well-written trap section entirely. Reworded the forward
reference to avoid the bare word "trap"; re-ran and confirmed the real trap section (which already
correctly names the wrong action, "Heroes will treat...") now parses clean.

| probe | verdict | finding |
|---|---|---|
| P1 cold solve | **PASS** | A solver computes D1's interior-angle proof (hexagon 120° × 3 = 360°; octagon 135° × 3 ≠ 360°, but 135° × 2 + 90° = 360°), D2's GCF-based staging block (GCF(45,30)=15 ft), D3's real-sheet-size cut-waste computation (Appendix C/D against the 45×30 plaza), and D4's installed-cost table. The metric ($/sq ft installed) is named explicitly by D4/D5. |
| P2 both-sides | **PASS** | A's best sentence: "The hexagon is mathematically the purer tessellation (D1), simpler to install (one repeating shape), and easier to defend to the client's committee if questions come up at the vertices." B's best sentence: "The octagon-and-square's manufactured sheet is a perfect 1-sq-ft square that divides the plaza's whole-foot dimensions with zero cut waste, while the hexagon's 11⅝″×10¼″ sheet doesn't — a real, sourced product fact that flips the naive 'purer tessellation wastes less' intuition (D3), closing most of the gap D1 would predict." Neither collapses; this is exactly the mechanism the trap (below) is built around. |
| P3 trap | **PASS (fixed this session)** | The trap (treating D1's "zero-gap tessellation" as automatically meaning "least material waste," without checking Appendix E's real manufactured sheet sizes) is the single most plausible failure mode — it is a real, sourced, counter-intuitive product fact, not an invented gotcha. FACILITATOR.md names this trap explicitly, now correctly parsed by the mechanical check after the line-30 forward-reference fix. |
| P4 twist | **PASS** | (twist reviewed in FACILITATOR.md.) Holds under every stated reading of MA1-MA4; MA4 (the 15% hexagon labor premium, the case's only unsourced figure) is explicitly named and its sensitivity discussed in Socratic question 3. |
| P5 sensitivity | **PASS** | Base margin 9.90% (winner: A, Hexagon), comfortably inside the ~20% cap. `sensitivity_model.py`'s ±50% sweep on every declared dial produces no verdict flips and no cap breaches — the cleanest P5 result in this batch. |
| P6 data decay | **PASS (live fetch)** | S1 (hexagon mosaic, Stone & Tile Shoppe/Daltile) — live, confirmed verbatim: "$6.59 per square foot," sheet "11 5/8\" x 10 1/4\"," "0.81 square feet" per sheet. S2 (octagon-and-dot mosaic, same retailer) — live, confirmed verbatim: "$9.69 / Sqft," "12\" x 12\"" sheet, "1 sqft per sheet." S3-S6 (labor-cost guidance sites, qualitative-only per case.md's own MA4 note) not independently re-fetched this session; RESEARCH_LOG.md records same-day confirmation. |

`MECHANICAL RESULT: 0 probes FAILED. All six verdicts recorded by name.`

**No retune needed.** Base margin 9.90%, comfortably inside the ~20% cap, no sensitivity
instability at all under ±50% flexing, both load-bearing tile-price sources confirmed live and
exact.

### Tier 3 — human dry-run

NOT RUN. No `cases/the-plaza-bid/runs/RUN_*.md` filed.
