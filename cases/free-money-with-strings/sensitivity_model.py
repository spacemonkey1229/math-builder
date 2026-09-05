"""Sensitivity model for Free Money, With Strings (SPEC section 2 balance test, case-readiness
Tier 2 probe 5). CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins. Metric is
each strategy's total ten-year future value (401(k) stream + "extra dollar" destination stream).

Both strategies contribute at least 6% of salary and both receive the identical employer match --
that shared stream is NOT the source of any difference. The only thing that differs is where the
"extra" 9%-of-salary goes and at what rate it grows:
    Match & Move (A): extra dollars redirected to loan paydown, growing at the loan's own
                       GUARANTEED rate (MA3 -- a mathematical equivalence, not a flexed assumption).
    Stack & Grow  (B): extra dollars added to the 401(k), growing at the ASSUMED market rate (MA1).

    V_A(10) = FV_annuity(own_cap + match, market_rate, 10) + FV_annuity(extra, loan_rate, 10)
    V_B(10) = FV_annuity(own_stack + match, market_rate, 10)
    FV_annuity(PMT, r, n) = PMT * [(1+r)^n - 1] / r
"""

PARAMS = {
    "salary": 72744.0,           # Appendix A, S1
    "match_rate": 0.50,          # Appendix A, S2
    "cap_pct": 0.06,             # Appendix A, S2
    "stack_pct": 0.15,           # Appendix A, S3
    "loan_rate": 0.0639,         # Appendix B, S6 -- MA3's guaranteed return, NOT flexed by P5
    "market_rate": 0.10,         # Appendix C, MA1 -- the case's ONE stated modeling assumption
    "horizon_years": 10.0,       # Appendix C, MA2
}

# Probe 5 flexes THIS and only this -- SPEC §2 asks for sensitivity to STATED ASSUMPTIONS, not
# to cited measurements. MA1 (assumed market growth rate) is the case's single modeling
# assumption about an unknowable future value; every other figure in PARAMS is either a cited
# source (S1, S2, S3, S6) or MA3, which is a fixed mathematical equivalence tied to the already-
# sourced loan rate S6, not an independent assumption with its own sensitivity range (see
# case.json.modeling_assumptions[MA3].sensitivity). MA2 (the 10-year horizon) is a scenario design
# choice, not swept here either -- P5 is about assumption VALUE sensitivity, not horizon-length
# sensitivity, and case.json states MA2's answer-sensitivity qualitatively rather than via flex.
FLEX = ["market_rate"]


def fv_annuity(pmt, r, n):
    return pmt * (((1 + r) ** n - 1) / r)


def streams(p):
    own_cap = p["salary"] * p["cap_pct"]
    match_amt = own_cap * p["match_rate"]
    own_extra = p["salary"] * (p["stack_pct"] - p["cap_pct"])
    own_stack = p["salary"] * p["stack_pct"]
    return own_cap, match_amt, own_extra, own_stack


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = total ten-year future value."""
    own_cap, match_amt, own_extra, own_stack = streams(p)
    n = p["horizon_years"]
    fv_401k_A = fv_annuity(own_cap + match_amt, p["market_rate"], n)
    fv_extra_A = fv_annuity(own_extra, p["loan_rate"], n)
    fv_401k_B = fv_annuity(own_stack + match_amt, p["market_rate"], n)
    return {"A": fv_401k_A + fv_extra_A, "B": fv_401k_B}


def evaluate_twist(p):
    """Twist: N/A for this case (see FACILITATOR.md) -- no separate twist scenario to evaluate.
    Provided only so callers expecting the optional hook do not fail; returns evaluate(p)."""
    return evaluate(p)


if __name__ == "__main__":
    ev = evaluate(PARAMS)
    winner = "A" if ev["A"] > ev["B"] else "B"
    other = "B" if winner == "A" else "A"
    margin = (ev[winner] - ev[other]) / ev[other] * 100
    print(f"Base case: A=${ev['A']:,.2f}  B=${ev['B']:,.2f}  winner={winner}  margin={margin:.2f}%")
    assert winner == "B", "expected Stack & Grow (B) to win at the base assumed market rate"
    assert abs(margin - 8.56) < 0.05, "margin drifted from case.json's recorded 8.56%"

    print("\nFlexing MA1 (market_rate) by +/-50%:")
    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        p2 = dict(PARAMS)
        p2["market_rate"] = PARAMS["market_rate"] * mult
        e2 = evaluate(p2)
        w2 = "A" if e2["A"] > e2["B"] else "B"
        o2 = "B" if w2 == "A" else "A"
        m2 = (e2[w2] - e2[o2]) / e2[o2] * 100
        print(f"  market_rate={p2['market_rate']:.3f} ({label}): A=${e2['A']:,.2f} "
              f"B=${e2['B']:,.2f} winner={w2} margin={m2:.2f}%")

    # Breakeven search (facilitator reference only -- never printed in case.md)
    lo_r, hi_r = 0.0, 0.20
    for _ in range(60):
        mid = (lo_r + hi_r) / 2
        p2 = dict(PARAMS)
        p2["market_rate"] = mid
        e2 = evaluate(p2)
        if e2["A"] > e2["B"]:
            lo_r = mid
        else:
            hi_r = mid
    print(f"\nBreakeven market_rate ~ {((lo_r + hi_r) / 2) * 100:.2f}% "
          f"(mathematically equal to the loan rate, {PARAMS['loan_rate']*100:.2f}%)")
