#!/usr/bin/env python3
"""
Sensitivity model -- Phone Plan.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. Two public
names, per skills/case-readiness/scripts/example_sensitivity_model.py:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     same shape, twist applied

Metric shape: cost is *lower is better*, but the contract requires the metric
to be higher-is-better, so both evaluate() and evaluate_twist() return
NEGATIVE total cost -- the cheaper carrier has the larger (less negative)
value. A = Carrier V, B = Carrier T, matching case.json's options.

Every PARAMS entry not in FLEX is Appendix A/C given data (pricing table,
current/future line counts) or the twist's own stated dollar figure -- not
swept by P5 by default. FLEX holds only the case's two real stated
assumptions (Appendix B) plus the twist's scenario dial, the same convention
Cold Chain's example used for twist_detour_h.

Verified against cases/phone-plan/case.json's derived{} block:
    base (2 lines)   A = -86.4   B = -75.6   margin 14.29%   (T cheaper)
    3 lines          A = -102.6  B = -102.6  (break-even, both equal)
    4 lines          A = -118.8  B = -129.6  (V cheaper)
    twist (1st year) A = -886.8  B = -907.2  (V cheaper once $150 credit applied)
"""

PARAMS = {
    # --- Appendix A: given carrier pricing (NOT flexed -- cited data, P6 covers it)
    "flat_V": 80.0,
    "addl_V": 15.0,
    "flat_T": 70.0,
    "addl_T": 25.0,
    # --- Appendix C: given family line-count plan (NOT flexed -- story fact)
    "lines_now": 2,
    "lines_future": 3,
    # --- Appendix B, Assumption 1: flat plan tax -- a real stated assumption
    "tax_rate": 0.08,
    # --- Appendix B, Assumption 2: additional-line rate holds when the 3rd/4th
    #     line is actually added. Modeled as a multiplier on the additional-line
    #     rate applied ONLY to lines beyond the first 2 (n > 2); 1.0 = "rate
    #     holds exactly as published". Flexing this simulates the rate moving
    #     by the time Charity's line is added.
    "addl_rate_holds": 1.0,
    # --- the Twist (FACILITATOR.md): Carrier V's one-time device-upgrade credit,
    #     a scenario dial the author chose, same class as Cold Chain's
    #     twist_detour_h -- swept by P5, not given/cited data.
    "twist_credit_V": 150.0,
}

# Only these three are genuine stated assumptions / scenario dials. SPEC S2
# sensitivity is about assumptions, not about the given pricing table or the
# family's stated line-count plan -- those are P6's job (there's nothing to
# fetch live for them since they're fictional-but-fixed, per the
# legacy_conversion_note, but they still aren't "assumptions" to flex).
FLEX = [
    "tax_rate",          # Appendix B, Assumption 1
    "addl_rate_holds",   # Appendix B, Assumption 2
    "twist_credit_V",    # twist scenario construction (FACILITATOR.md)
]


def _monthly_cost(p, flat, addl, lines):
    extra = max(0, lines - 2)
    rate = addl * (p["addl_rate_holds"] if lines > 2 else 1.0)
    pretax = flat + rate * extra
    return pretax * (1.0 + p["tax_rate"])


def evaluate(params, lines=None):
    p = dict(PARAMS)
    p.update(params or {})
    n = lines if lines is not None else p["lines_now"]
    cost_V = _monthly_cost(p, p["flat_V"], p["addl_V"], n)
    cost_T = _monthly_cost(p, p["flat_T"], p["addl_T"], n)
    return {"A": -cost_V, "B": -cost_T}


def evaluate_twist(params):
    """First-year total cost at the family's current (2-line) need: 12 months
    of the monthly rate, minus Carrier V's one-time $150 credit."""
    p = dict(PARAMS)
    p.update(params or {})
    base = evaluate(p, lines=p["lines_now"])
    annual_V = -base["A"] * 12 - p["twist_credit_V"]
    annual_T = -base["B"] * 12
    return {"A": -annual_V, "B": -annual_T}


def break_even_lines(params=None):
    """Solve cost_V(n) == cost_T(n) for n (both sides scale by the same tax
    factor, so it cancels): 80 + 15*(n-2) = 70 + 25*(n-2)."""
    p = dict(PARAMS)
    p.update(params or {})
    # flat_V + addl_V*(n-2) == flat_T + addl_T*(n-2)
    denom = (p["addl_T"] - p["addl_V"])
    if denom == 0:
        return None
    n = 2 + (p["flat_V"] - p["flat_T"]) / denom
    return n


if __name__ == "__main__":
    for n in (2, 3, 4):
        r = evaluate({}, lines=n)
        print(f"{n} lines: V=${-r['A']:.2f}  T=${-r['B']:.2f}")
    be = break_even_lines()
    print("break-even lines:", be)
    base = evaluate({})
    cost_V, cost_T = -base["A"], -base["B"]
    margin = 100 * (cost_V - cost_T) / cost_T
    print("base margin (V costs how much more than T, %% of T) %.2f%%" % margin)
    tw = evaluate_twist({})
    print("twist (annual, 2-line):", {k: round(v, 2) for k, v in tw.items()})
