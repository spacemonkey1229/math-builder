#!/usr/bin/env python3
"""
Sensitivity model -- The Bracket Cliff.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The primary metric (case.json.primary_metric / balance.margin_basis) compares,
per affected household near the 400%-FPL threshold:
    Hold The Cliff's cost  = the D1/D2 jump discontinuity a household absorbs
                              (Household 2's unsubsidized premium minus
                              Household 1's subsidized premium, Appendix B, S3)
    Build The Bridge's cost = the state's real cost to cap that same
                               household's payment at Appendix C's 8.5% income
                               cap (Appendix C, S5)
evaluate() returns the NEGATIVE of each option's cost as its metric (higher
metric = lower cost = better), so metric_A > metric_B exactly when Hold The
Cliff is cheaper, matching case.json.balance.margin_pct's sign (A wins).

Fixed (NOT in FLEX[]): unsubsidized_premium, subsidized_premium (S3) and
cap_pct (S5) are all CITED, sourced figures, not stated scenario assumptions
-- per the "only FLEX[] is swept by default" rule (SPEC Sec2 asks for
sensitivity to stated ASSUMPTIONS, not to cited measurements). Only
Appendix E's MA1-MA4 are genuine stated Modeling Assumptions, and
FACILITATOR.md's own margin note already discloses that none of them enters
the per-household ratio at all: MA1 (enrollment) and MA2 (near-threshold
share) are pure population scale factors that multiply both option's TOTAL
cost by the same number and cancel out of the ratio; MA4 (days to markup)
never enters the D1-D4 math at all. Only MA3 (the one-time $8M discretionary
line item) is represented here, as a pass/fail feasibility gate on whether
Build The Bridge's real annual state-scale cost is even fundable this cycle
-- consistent with case.md Appendix E's own stated MA3 sensitivity note.

Verified against case.json.derived.per_household (2026-09-01):
    base    A (Hold The Cliff)   cost = 8,756   (metric = -8,756)
            B (Build The Bridge) cost = 9,491   (metric = -9,491)
            margin  (8,491's negative done right): (-8756 - -9491) / 9491 * 100
                    = 735 / 9491 * 100 = 7.744...%  (matches case.json.margin_pct = 7.74)
    MA3 (line item) flexed to $4,000,000 (-50%) or $12,000,000 (+50%): does not
            change the per-household metric at all (it is a state-scale
            feasibility gate, not an input to the per-household ratio) -- it
            only changes whether Build The Bridge is PRACTICALLY fundable this
            budget cycle at this state's estimated scale, which is exactly
            what FACILITATOR.md's margin note already says.
"""

PARAMS = {
    # --- Appendix B / S3: real KFF worked-example premiums --------------------
    "unsubsidized_premium_usd": 14931.0,   # Household 2, 409% FPL, no subsidy
    "subsidized_premium_usd": 6175.0,      # Household 1, 396% FPL, subsidized
    "threshold_income_usd": 64000.0,       # Household 2's income (Appendix B)
    # --- Appendix C / S5: ARP/IRA enhanced-formula income cap ------------------
    "cap_pct": 0.085,
    # --- Appendix E, MA3: one-time discretionary line item available ----------
    "line_item_usd": 8000000.0,
    # --- Appendix D: real per-state wraparound program cost, used as the ------
    #     feasibility floor MA3 is tested against (cheapest real comparable:
    #     New Mexico's ~$38.8M combined appropriation, Appendix D / S9-S10)
    "min_state_program_cost_usd": 38800000.0,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption (MA3). unsubsidized_premium_usd, subsidized_premium_usd, and
# cap_pct are all real, cited figures (S3, S5) and are NOT flexed by default;
# --flex-all overrides. MA1/MA2 are population-scale factors that provably
# cancel out of the per-household metric (not represented here at all, per
# the docstring); MA4 never enters the D1-D4 math.
FLEX = [
    "line_item_usd",   # MA3
]


def evaluate(params):
    """The case's actual per-household comparison (D1-D4): each option's
    real dollar cost, negated so higher = better (cheaper)."""
    p = dict(PARAMS)
    p.update(params or {})

    discontinuity = p["unsubsidized_premium_usd"] - p["subsidized_premium_usd"]
    capped_payment = p["cap_pct"] * p["threshold_income_usd"]
    bridge_cost = p["unsubsidized_premium_usd"] - capped_payment

    metric_A = -discontinuity      # Hold The Cliff's cost (borne by the household)
    metric_B = -bridge_cost        # Build The Bridge's cost (borne by the state)

    return {"A": metric_A, "B": metric_B}


def feasible_B(params=None):
    """MA3 feasibility gate: can the one-time line item even fund a real
    state-scale wraparound program this cycle? (Does not affect evaluate()'s
    per-household metric -- a separate, disclosed practical constraint on D5.)"""
    p = dict(PARAMS)
    p.update(params or {})
    return p["line_item_usd"] >= p["min_state_program_cost_usd"]


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / abs(base["B"])
    print("base  ", {k: round(v, 2) for k, v in base.items()}, "margin %.2f%%" % margin,
          "winner:", "A (Hold The Cliff)" if base["A"] > base["B"] else "B (Build The Bridge)")

    low = evaluate({"line_item_usd": 4000000.0})
    margin_low = 100 * (low["A"] - low["B"]) / abs(low["B"])
    print("MA3 -50%% ($4M line item)", {k: round(v, 2) for k, v in low.items()},
          "margin %.2f%%" % margin_low, "-- metric unchanged (feasibility gate only);",
          "B fundable?" , feasible_B({"line_item_usd": 4000000.0}))

    high = evaluate({"line_item_usd": 12000000.0})
    margin_high = 100 * (high["A"] - high["B"]) / abs(high["B"])
    print("MA3 +50%% ($12M line item)", {k: round(v, 2) for k, v in high.items()},
          "margin %.2f%%" % margin_high, "-- metric unchanged (feasibility gate only);",
          "B fundable?", feasible_B({"line_item_usd": 12000000.0}))
