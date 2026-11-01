#!/usr/bin/env python3
"""
Sensitivity model — Firm Power.

CONTRACT — exactly two public names used by Tier 2 probe 5:
    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

No evaluate_twist() — this case has no twist (facilitator.has_twist = false).

The case's own primary metric (dollars per megawatt-hour) is a COST metric -- lower is better.
`evaluate()` returns the NEGATIVE of each option's total dollar cost for the peak window, so
"higher is better" holds (less negative = cheaper = better), matching this script's contract.

Verified against case.json.balance (2026-09-18):
    base   A (Peaker Contract)      = -$87,996.42
           B (Firmed Solar Contract)= -$83,862.36
    winner B, margin_pct (on the underlying $/MWh rates) = 4.70%
"""

# Real, cited $/MWh rates (Lazard LCOE+ June 2025, v18.0) -- NOT in PARAMS/FLEX.
# Per skills/case-readiness/SKILL.md's P5 "FLEX[] scoping" rule: only STATED ASSUMPTIONS are
# swept, never cited measurements. The choice of WHERE in gas peaking's real range to land
# (case.json.sensitivity_disclosure[]) is real data, not an author's assumption, and is
# disclosed separately rather than folded into FLEX.
A_RATE_USD_PER_MWH = 149.0
B_RATE_USD_PER_MWH = 142.0

# Real CAISO data (case.json.sources S1) -- NOT swept.
Q3_MW = 29806.0
PEAK_MW = 33087.0
PEAK_WINDOW_HOURS = 6

PARAMS = {
    # Appendix E, MA1 -- Solano Bay's share of CAISO's total system demand.
    "ccas_share_pct": 0.03,
    # Appendix E, MA2 -- the board's monthly capacity-tranche budget. Does not enter evaluate()
    # at all (it only feeds Challenge D4's illustrative side-calculation), so flexing it is
    # expected to be a genuine no-op on the A-vs-B balance -- a correct, honest finding, not a
    # bug in this model.
    "monthly_budget_usd": 10000.0,
}

FLEX = ["ccas_share_pct", "monthly_budget_usd"]


def _mwh_needed(params):
    share = params["ccas_share_pct"]
    q3_scaled = Q3_MW * share
    peak_scaled = PEAK_MW * share
    new_capacity_mw = peak_scaled - q3_scaled
    return new_capacity_mw * PEAK_WINDOW_HOURS


def evaluate(params):
    mwh = _mwh_needed(params)
    a_cost = mwh * A_RATE_USD_PER_MWH
    b_cost = mwh * B_RATE_USD_PER_MWH
    return {"A": -a_cost, "B": -b_cost}


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner = "A" if base["A"] > base["B"] else ("B" if base["B"] > base["A"] else "TIE")
    print("base", base, "winner", winner)
    print("underlying rate margin_pct",
          round(abs(A_RATE_USD_PER_MWH - B_RATE_USD_PER_MWH) / max(A_RATE_USD_PER_MWH, B_RATE_USD_PER_MWH) * 100, 2))
    for pname in FLEX:
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            p = dict(PARAMS)
            p[pname] = PARAMS[pname] * mult
            r = evaluate(p)
            w = "A" if r["A"] > r["B"] else ("B" if r["B"] > r["A"] else "TIE")
            print(f"  flex {pname} {label}: {r}  winner={w}  (base winner={winner})")
