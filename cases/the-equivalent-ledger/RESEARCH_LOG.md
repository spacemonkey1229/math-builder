# Research Log — The Equivalent Ledger

One row per `{{NEEDS_SOURCE}}` placeholder from `case-write`. 12 placeholders total. Per this
case's sourcing brief: the mathematical content (factoring polynomials to prove function
equivalence) is self-contained and needs no proprietary data; the business framing (enterprise
"systems of record" needing deterministic guarantees, and companies bolting AI onto legacy
deterministic systems in 2026) is a real, documented industry conversation and was searched for
real, general commentary; the constructed formula itself was never going to be sourced to a real
company — it is disclosed as an illustrative construction from the start.

---

### P01 — Appendix A: Original formula, O(n)

**Searched:** not independently searchable — no real company's actual proprietary reconciliation
formula is being sought or should be. This case's entire mathematical content is a constructed,
disclosed example built specifically to teach GCF-based factoring of a two-term polynomial.

**Disposition: ASSUMPTION (MA1).** Set to O(n) = 48n² + 180n, whose coefficients' GCF (12) is
findable by prime factorization (48 = 2⁴×3, 180 = 2²×3²×5). Disclosed explicitly in Appendix A and
the Modeling Assumptions block as an illustrative construction, not a real formula.

---

### P02 — Appendix A: AI-rewritten formula, R(n)

**Searched:** not independently searchable, same reasoning as P01.

**Disposition: ASSUMPTION (MA2).** Set to R(n) = 54n² + 96n + 240, deliberately constructed so that
R(n) − O(n) = 6n² − 84n + 240 = 6(n−4)(n−10) — a difference polynomial that vanishes at exactly two
points (n=4, n=10) and nowhere else. This is the mechanism that makes "sample-testing at those two
points" a genuine, non-contrived trap: the two formulas really do agree there, and really do
diverge elsewhere (5.5% apart at n=25; 7.7% apart at n=40). Disclosed as a constructed illustrative
example.

---

### P03 — Appendix B: The two historical batch sizes QA tested

**Searched:** not independently searchable — these are a specific fictional company's own log
records, not a publishable statistic, and are fixed by MA1/MA2's construction (they must be n=4
and n=10 for the "coincidental match" mechanism to work).

**Disposition: ASSUMPTION (MA3).** Set to n=4 and n=10.

---

### P04 — Appendix B: A representative larger, untested batch size

**Searched:** not independently searchable — protagonist-specific "typical production night"
figure for a fictional company.

**Disposition: ASSUMPTION (MA4).** Set to n=25 (chosen to be comfortably larger than both tested
batches, and to produce a clear, material $1,890 / 5.5% divergence when D3 is computed — large
enough to matter, not so large it strains plausibility for a single night's unmatched-item count).

---

### P05 — Appendix C: Hours until the deployment freeze begins

**Searched:** not applicable — restates the Overview's own narrative-fixed detail ("before
sunrise"), not an independently sourceable fact.

**Disposition: ASSUMPTION (MA5).** Set to 6 hours, matching the Overview's narrative.

---

### P06 — Appendix C: Deployment freeze duration if missed

**Searched:** "bank quarter-end close change freeze deployment core banking system"; found general,
real industry commentary (Upsun, ProSight Financial Association, and others) confirming that
quarter/period-end regulatory close commonly triggers change freezes on core financial-
infrastructure systems, and that legacy-system migration/replacement windows commonly run into
multi-week or multi-year freeze periods — but no source publishes an exact freeze-window *length*
for a specific company's specific reconciliation engine, which is inherently protagonist-specific.

**Disposition: ASSUMPTION (MA6).** Set to 6 weeks — a disclosed scenario value in the middle of
common industry change-freeze practice, not read off any single source.

---

### P07 — Appendix C: Senior engineers assigned to verification

**Searched:** not independently searchable — Ledgerline's own internal staffing decision.

**Disposition: ASSUMPTION (MA7, combined with P08).** Set to 2 engineers.

---

### P08 — Appendix C: Hours required per engineer for verification

**Searched:** not independently searchable — no source publishes a standard duration for "fully
factor and symbolically verify two short reconciliation-formula polynomials," since this is a
scenario-specific task on scenario-specific formulas.

**Disposition: ASSUMPTION (MA7, combined with P07).** Set to 8 hours (one business day) per
engineer.

---

### P09 — Appendix C: Fully-loaded hourly cost of a senior verification/QA engineer

**Searched:** "BLS Occupational Outlook Handbook software quality assurance analysts and testers
median wage"; fetched bls.gov/oes/2023/may/oes151253.htm directly (SOC 15-1253).

**Found:** median hourly wage $48.94 ($101,800/year), May 2023 — the most recent BLS data broken
out to this specific occupation code. A broader combined "Software Developers, Quality Assurance
Analysts, and Testers" category on BLS's Occupational Outlook Handbook page reports a newer
$104,300/year (May 2025) figure, corroborating the same general pay range, but is not broken out to
the QA-specific code.

**Disposition: SOURCED [S1]**, HIGH confidence (primary U.S. government source, dated, unambiguous
units).

---

### P10 — Appendix D: Probability an AI-rewritten change that passed limited testing still has an
undetected defect

**Searched:** "study AI-generated code passes tests but contains bugs defect rate"; fetched
dev.to's summary of CodeRabbit's "State of AI vs Human Code Generation" report and confirmed via
CodeRabbit's own newsroom page (coderabbit.ai/newsroom/state-of-ai-vs-human-code-generation-report).

**Found:** CodeRabbit's report (470 real-world open-source pull requests) found AI-generated code
carries 1.4-1.7x more critical/major defects than human-written code, with logic/correctness
issues 75% more common, and documented specific cases of subtly buggy AI-generated code that passed
every automated test but broke in production. This is real, general evidence that the underlying
risk category (AI-generated/AI-rewritten code passing tests while still containing defects) is real
and material — but no source publishes a residual-defect *probability* specific to a formula that
has already passed two real-batch regression tests, which is inherently a property of this specific
scenario, not a publishable industry statistic. (The overall-issues headline "1.7x" figure quoted
on CodeRabbit's newsroom page is the aggregate across all severities; the specific critical/major
breakdown and the 75% logic/correctness figure are stated on CodeRabbit's own blog post of the same
report, which is the URL cited in S2 — verified directly during Tier 2 P6 data-decay.)

**Disposition: SOURCED [S2] for the qualitative/general finding; ASSUMPTION (MA8) for the specific
3.4% value applied to this case's formula.** 3.4% is a disclosed scenario assumption grounded by,
but not read directly off, S2's aggregate PR-level statistic.

---

### P11 — Appendix D: Cost if an undetected reconciliation-sweep error reaches production

**Searched:** "average cost to investigate and resolve a bank reconciliation break operational risk
incident"; fetched summaries from Xceptor, Kani Payments, and CreateOS.

**Found:** routine per-exception reconciliation investigation costs cited in the $9–$22 range (with
one figure as high as $21.60), for a single ordinary matched-item exception a human resolves in
minutes. No source publishes a cost for the more severe, systemic scenario this case models: an
undetected *formula-level* error that recurs every affected night and requires investigation across
multiple batches plus a compliance/audit escalation once discovered post-close — categorically a
different, rarer, and more severe event than a routine exception, and inherently unpublishable for
a specific fictional company.

**Disposition: ASSUMPTION (MA9).** Set to $25,000 — well above the routine per-exception range
found in research, as a disclosed scenario value reflecting the more severe systemic-error
scenario, not derived arithmetically from the routine-exception figures.

---

### Supplemental — business-framing/narrative grounding (not tied to a numbered placeholder)

**Searched:** "AI rewriting legacy code financial systems deterministic verification risk 2026";
fetched allyticstechperspectives.com's "The End of the Legacy Rewrite Trap" directly (published
2026-07-02).

**Found:** real, current (2026) industry commentary stating plainly that "pointing a probabilistic
model at a legacy codebase is a recipe for disaster" and "you cannot run a global bank on a system
built through probabilistic experimentation and AI hallucinations" — confirming this case's central
tension (AI-assisted rewrites of deterministic financial code, and the gap between passing limited
tests and being provably correct) is a real, documented 2026 industry conversation, not an invented
premise.

**Disposition: SOURCED [S3]**, MEDIUM confidence (an analyst/trade blog, not primary data — used
only for narrative grounding, carries no numeric figure used in any calculation).

---

## Summary

| Placeholder | Status | Resolved by |
|---|---|---|
| P01 (original formula O(n)) | ASSUMPTION | MA1 |
| P02 (AI-rewritten formula R(n)) | ASSUMPTION | MA2 |
| P03 (two tested batch sizes) | ASSUMPTION | MA3 |
| P04 (representative larger batch) | ASSUMPTION | MA4 |
| P05 (hours until freeze) | ASSUMPTION | MA5 |
| P06 (freeze duration) | ASSUMPTION | MA6 |
| P07 (engineers assigned) | ASSUMPTION | MA7 |
| P08 (hours per engineer) | ASSUMPTION | MA7 |
| P09 (hourly wage) | SOURCED | S1 |
| P10 (defect probability) | SOURCED (general) + ASSUMPTION (specific value) | S2, MA8 |
| P11 (cost of undetected error) | ASSUMPTION | MA9 |
| Supplemental (narrative grounding) | SOURCED | S3 |

**0 remaining OPEN. 0 NOT FOUND left unresolved** — every placeholder is SOURCED or ASSUMPTION, per
SPEC §5. No redesign was needed: the case's core mechanism (two polynomials constructed to agree
at exactly two tested points and diverge elsewhere, provable only by fully factoring both) is
self-contained and required no proprietary data by design; the real sourcing effort went into (a)
grounding the business-framing tension in real 2026 industry commentary and (b) sourcing the one
genuinely publishable figure in the cost model (the verification engineer's wage), while every
protagonist-specific and scenario-specific figure (the formulas themselves, the tested batch sizes,
the freeze calendar, the risk probability and cost-of-error) is carried openly as a Modeling
Assumption, each with a disclosed basis.

Next step: `case-readiness` — Tier 1 structural checks, then Tier 2's six simulated-play probes.
