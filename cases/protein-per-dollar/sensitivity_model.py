"""Sensitivity model for Protein Per Dollar (SPEC section 2, case-readiness Tier 2 probe 5).

CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins.
Metric = grams of protein bought in the quarter on the stated budget, planned at the
August 2024 prices times a quarter-price ratio. With the ratios at 1.0 this is the
case's primary metric (grams of protein per dollar) times the budget.

    A (Eggs)    : budget_q / (egg_price * egg_price_ratio)  * 12 * egg_weight_g * egg_protein / 100
    B (Chicken) : budget_q / (chk_price * chk_price_ratio)  * grams_per_lb * chk_protein / 100

FLEX (what probe 5 sweeps): the stated assumptions only -- MA1 budget, MA2 (the quarter's
price relative to the August planning price: the order is price-floating), and MA3-MA5
(egg weight, egg protein, chicken protein; UNVERIFIED because FoodData Central was not
reachable). The three BLS prices and the pound in grams are cited data (P6 covers them).
"""
PARAMS = {
    "budget_month": 12000.0,          # MA1
    "egg_price": 3.204,               # Appendix A, S1 (cited, Aug 2024)
    "chk_price": 3.952,               # Appendix A, S2 (cited, Aug 2024)
    "grams_per_lb": 453.6,            # Appendix C, S2 (cited)
    "egg_weight_g": 50.0,             # MA3 (UNVERIFIED)
    "egg_protein_per100": 12.56,      # MA4 (UNVERIFIED)
    "chk_protein_per100": 22.5,       # MA5 (UNVERIFIED)
    "egg_price_ratio": 1.0,           # MA2: quarter's egg price / Aug 2024 price
    "chk_price_ratio": 1.0,           # MA2: quarter's chicken price / Aug 2024 price
}
FLEX = ["budget_month", "egg_weight_g", "egg_protein_per100", "chk_protein_per100",
        "egg_price_ratio", "chk_price_ratio"]

# Post-decision monthly BLS prices, Oct-Dec 2024 (the quarter ordered): facilitator-only.
TWIST_MONTHS = {"egg": [3.370, 3.649, 4.146], "chk": [4.037, 4.011, 4.104]}


def _g_per_dollar(p, which):
    if which == "A":
        return 12 * p["egg_weight_g"] * p["egg_protein_per100"] / 100.0 / (p["egg_price"] * p["egg_price_ratio"])
    return p["grams_per_lb"] * p["chk_protein_per100"] / 100.0 / (p["chk_price"] * p["chk_price_ratio"])


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    q = 3 * p["budget_month"]
    return {"A": q * _g_per_dollar(p, "A"), "B": q * _g_per_dollar(p, "B")}


def evaluate_twist(params):
    """Quarter ordered, priced at the actual Oct-Dec 2024 monthly prices (floating order)."""
    p = dict(PARAMS); p.update(params or {})
    a = sum(p["budget_month"] * 12 * p["egg_weight_g"] * p["egg_protein_per100"] / 100.0 / x
            for x in TWIST_MONTHS["egg"])
    b = sum(p["budget_month"] * p["grams_per_lb"] * p["chk_protein_per100"] / 100.0 / x
            for x in TWIST_MONTHS["chk"])
    return {"A": a, "B": b}


def margin_pct(r):
    hi, lo = max(r.values()), min(r.values())
    return 100.0 * (hi - lo) / hi          # gap / winner (the case's convention)


if __name__ == "__main__":
    base = evaluate({})
    print("base ", {k: round(v) for k, v in base.items()}, "margin gap/winner %.2f%%" % margin_pct(base))
    tw = evaluate_twist({})
    print("twist", {k: round(v) for k, v in tw.items()}, "margin gap/winner %.2f%%" % margin_pct(tw))
    for name in FLEX:
        for mult in (0.5, 1.5):
            r = evaluate({name: PARAMS[name] * mult})
            w = max(r, key=r.get)
            print(f"{name:20s} x{mult}: winner {w}  margin {margin_pct(r):6.2f}%")
    print("-- plausible-range (+/-5% on the three nutrition values) --")
    for name in ("egg_weight_g", "egg_protein_per100", "chk_protein_per100"):
        for mult in (0.95, 1.05):
            r = evaluate({name: PARAMS[name] * mult})
            print(f"{name:20s} x{mult}: winner {max(r, key=r.get)}  margin {margin_pct(r):6.2f}%")
    r = evaluate({"chk_protein_per100": 23.1})
    print("chicken 23.1 g/100g: winner", max(r, key=r.get), "margin %.2f%%" % margin_pct(r))
