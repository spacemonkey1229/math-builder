"""
Sensitivity model for cases/life-insurance -- Tier 2 probe 5/4 contract
(skills/case-readiness/SKILL.md). Two public names beyond PARAMS/FLEX:
evaluate(params) -> {"A": metric, "B": metric}   (higher is better)
evaluate_twist(params) -> {"A": metric, "B": metric}

PRIMARY METRIC, retuned 2026-08-17 (P6 fix -- see case.json.qa.tier2_fixed_2026_08_17
and balance.margin_basis for the full story). sources[] S3's old "4.65% average
dividend-inclusive crediting rate" claim did not exist on the live source page;
re-fetched 2026-08-17, the page lists 5 real 2026 carrier dividend rates
(5.75%-6.60%) with NO combined average, averaging (case-computed) to 6.20%.
Using the corrected 6.20% as the graded metric blows the raw dividend-vs-CD
gap out to ~37.8%, well past SPEC.md Section 2's 20% balance cap -- so the
GRADED primary metric moved to a genuinely guaranteed-vs-guaranteed
comparison instead of being forced to keep the old, no-longer-supportable
near-tie:
  A = whole life's strongest real GUARANTEED claim: the top of Appendix D's
      real, cited 2%-4% guaranteed cash-value range (guaranteed_rate_ceiling)
  B = the best publicly available 5-year CD rate (the safe alternative if
      the family buys term and saves the premium difference themselves)

The raw, higher-stakes headline comparison (dividend_inclusive_rate, now a
real 6.20%, vs. cd_rate) is still exactly what D4 has the Hero compute and
write up ("what it does and does not show") -- it is now evaluate_twist(),
not evaluate(): the Twist reveals that if the currently-elevated, real,
non-guaranteed dividend scale holds, whole life actually wins outright. The
~12x raw premium gap (see derived_dollar_picture() below) remains real,
computed, and disclosed, but stays the case's deeper trap, not the graded
balance-test margin (same pattern as cases/a-coachs-dilemma).

FLEX[] contains ONLY genuine stated assumptions the author had to choose
(SKILL.md P5 rule) -- NEVER cited/given market data. guaranteed_growth_rate
(MA5), cv0_multiple_of_premium (MA4), and guaranteed_rate_ceiling (which end
of the real 2-4% guaranteed range is graded, case.json.sensitivity_disclosure)
are all scenario dials this case's author picked, not raw measurements.
dividend_inclusive_rate and cd_rate are real, cited, sourced numbers
(case.json sources[] S3/S4) -- stress-tested by Tier 2 probe 6 (data decay),
not swept here.
"""

# Every dial the case STATES (cited data + stated assumptions together).
PARAMS = {
    # --- cited / given (NOT flexed by default; see FLEX below) ---
    "coverage_need": 1_300_000.0,          # D1, Appendix B, rounded to nearest $50k increment
    "term_500k_monthly": 36.0,             # Appendix D / sources S1, age ~30 benchmark
    "whole_life_500k_monthly": 444.0,      # Appendix D / sources S1, age ~30 benchmark
    "term_length_years": 20,               # D2, shortest standard term covering the 17-yr need
    "dividend_inclusive_rate": 0.0620,     # Appendix D / sources S3, case-computed avg of 5 real 2026 carrier rates (corrected 2026-08-17)
    "cd_rate": 0.045,                      # Appendix D / sources S4, real cited best available rate

    # --- genuine stated assumptions (author had to choose these) ---
    "guaranteed_growth_rate": 0.03,        # MA5: midpoint of real cited 2-4% guaranteed range (D3 cash-value projection)
    "cv0_multiple_of_premium": 1.0,        # MA4: whole life cash value starts at 1x year-1 premium
    "guaranteed_rate_ceiling": 0.04,       # top of the real cited 2-4% guaranteed range; the GRADED D4 metric (balance.margin_basis)
}

# Only the genuine ASSUMPTIONS (MA4, MA5, and which end of the real
# guaranteed range is graded) are swept by Tier 2 probe 5 by default -- not
# the cited market rates (dividend_inclusive_rate, cd_rate, the $500k rate
# benchmarks), which are given/cited data, per SKILL.md's "Only FLEX[] is
# swept by default" rule.
FLEX = ["guaranteed_growth_rate", "cv0_multiple_of_premium", "guaranteed_rate_ceiling"]


def _scale(p):
    return p["coverage_need"] / 500_000.0


def _premiums(p):
    scale = _scale(p)
    term_annual = p["term_500k_monthly"] * scale * 12
    wl_annual = p["whole_life_500k_monthly"] * scale * 12
    return term_annual, wl_annual


def _cash_value(p, years):
    """Explicit (closed-form) projection of the recursive rule
    CV_n = CV_(n-1) * (1 + r), CV_0 = cv0_multiple_of_premium * annual whole-life premium."""
    _, wl_annual = _premiums(p)
    cv0 = p["cv0_multiple_of_premium"] * wl_annual
    r = p["guaranteed_growth_rate"]
    return cv0 * (1 + r) ** years


def evaluate(params=None):
    """GRADED primary metric (retuned 2026-08-17): a genuinely guaranteed-vs-
    guaranteed rate comparison.
    A = whole life's strongest real guaranteed claim -- guaranteed_rate_ceiling,
        the top of the real, cited 2%-4% guaranteed range.
    B = the safe CD alternative's rate (real, cited, contractually guaranteed).
    Higher is better."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["guaranteed_rate_ceiling"] * 100, "B": p["cd_rate"] * 100}


def evaluate_twist(params=None):
    """Twist: the real, current (2026) dividend-inclusive rate insurers are
    actually declaring is well above the guaranteed floor used for the base
    metric -- Option A is re-evaluated using the full, real, non-guaranteed
    dividend-inclusive rate (dividend_inclusive_rate, corrected 2026-08-17 to
    a real 6.20%), since that is the number Jake and the family's agent would
    actually show them, while B's CD rate stays contractually guaranteed
    either way. This is the case's own D4 headline comparison -- real,
    disclosed, and exactly what the Hero computes for D4's written
    explanation, deliberately not the graded base metric (see
    case.json.balance.margin_basis)."""
    p = dict(PARAMS)
    p.update(params or {})
    return {"A": p["dividend_inclusive_rate"] * 100, "B": p["cd_rate"] * 100}


def derived_dollar_picture(params=None):
    """Not the graded metric -- the case's disclosed 'deeper' trap numbers,
    used by FACILITATOR.md and QA, never printed to the student-facing page."""
    p = dict(PARAMS)
    p.update(params or {})
    term_annual, wl_annual = _premiums(p)
    term_total_20yr = term_annual * p["term_length_years"]
    cv_65 = _cash_value(p, 39)
    cv_80 = _cash_value(p, 54)
    wl_total_65 = wl_annual * 39
    wl_total_80 = wl_annual * 54
    return {
        "term_annual_premium": round(term_annual, 2),
        "whole_life_annual_premium": round(wl_annual, 2),
        "term_total_premiums_20yr": round(term_total_20yr, 2),
        "cash_value_at_65": round(cv_65, 2),
        "cash_value_at_80": round(cv_80, 2),
        "whole_life_total_premiums_to_65": round(wl_total_65, 2),
        "whole_life_total_premiums_to_80": round(wl_total_80, 2),
        "annual_premium_ratio_wholelife_to_term": round(wl_annual / term_annual, 2),
    }


if __name__ == "__main__":
    base = evaluate()
    twist = evaluate_twist()
    print("base  A(whole life rate)=%.2f%%  B(CD rate)=%.2f%%" % (base["A"], base["B"]))
    print("twist A(guaranteed only)=%.2f%%  B(CD rate)=%.2f%%" % (twist["A"], twist["B"]))
    print("dollar picture:", derived_dollar_picture())
