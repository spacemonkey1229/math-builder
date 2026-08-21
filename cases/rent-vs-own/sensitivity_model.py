#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Rent vs. Own.

Tier 2 probe 5 needs a runnable model of the case's own arithmetic. Reproduces
case.json's derived{} block from Appendix A/B's given data plus Appendix C's
two stated modeling assumptions (MA1 mortgage rate, MA2 bundled PMI/tax/ins).

CONTRACT — exactly two public names (plus optional evaluate_twist):
    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     the twist: rate moves from 3.0% to 3.5% before closing

Metric convention: A/B here are NEGATIVE total monthly housing cost (renting
vs. owning) so that "higher is better" holds — the case's primary_metric is a
cost comparison where lower cost wins, so we negate to fit the evaluate()
contract's higher-is-better shape.

FLEX SCOPING — only the case's own stated MODELING ASSUMPTIONS (Appendix C),
not Appendix A/B's given family-budget or purchase-terms figures:
  - annual_rate            (MA1 — "a real, disclosed approximation ... not the
                             Newmans' exact locked-in rate")
  - bundled_pmi_tax_ins    (MA2 — "a stated bundled estimate ... not three
                             separately sourced rates")
  - twist_rate             (the twist's own scenario dial, FACILITATOR.md)
NOT flexed: sale_price, down_payment_pct, closing_cost_pct (Appendix B, the
bank's actual pre-qualification terms — given data, not an authorial choice),
rent/renters_insurance/income (Appendix A, the fictional-but-fixed household
budget), term_months (a fixed 30-year conventional product, not a dial).

Verified against cases/rent-vs-own/case.json derived{}:
    base  monthly_principal_interest = 1479.83   total_monthly_owning_cost = 1789.83
          current_total_monthly_rent = 1512.21   margin 18.36%
    twist monthly_principal_interest = 1576.15   total_monthly_owning_cost = 1886.15
"""

PARAMS = {
    # --- Appendix B, given purchase terms (bank pre-qualification) ----------
    "sale_price": 360000.0,
    "down_payment_pct": 0.025,
    "closing_cost_pct": 0.035,
    "term_months": 360,
    # --- Appendix A, given family budget -------------------------------------
    "rent": 1500.0,
    "renters_insurance": 12.21,
    # --- Appendix C, Assumption 1 (MA1) — the mortgage rate ------------------
    "annual_rate": 0.03,
    # --- Appendix C, Assumption 2 (MA2) — bundled PMI/tax/insurance ----------
    "bundled_pmi_tax_ins": 310.0,
    # --- the Twist (FACILITATOR.md): rate moves before closing ---------------
    "twist_rate": 0.035,
}

# Only the case's own STATED MODELING ASSUMPTIONS, per Appendix C / MA1-MA2.
# Appendix A/B figures are given data (real household numbers, real bank
# terms), not an author's chosen dial -- flexing those would be testing a
# different case, not this case's sensitivity. See docstring above.
FLEX = [
    "annual_rate",           # Appendix C, Assumption 1 (MA1)
    "bundled_pmi_tax_ins",   # Appendix C, Assumption 2 (MA2)
    "twist_rate",            # the twist's own scenario dial
]


def _monthly_pi(loan_amount, annual_rate, term_months):
    r = annual_rate / 12.0
    n = term_months
    if r == 0:
        return loan_amount / n
    return loan_amount * r * (1 + r) ** n / ((1 + r) ** n - 1)


def _owning_cost(p, annual_rate):
    down_payment = p["sale_price"] * p["down_payment_pct"]
    closing_costs = p["sale_price"] * p["closing_cost_pct"]
    loan_amount = p["sale_price"] - down_payment
    pi = _monthly_pi(loan_amount, annual_rate, p["term_months"])
    return pi + p["bundled_pmi_tax_ins"]


def evaluate(params):
    p = dict(PARAMS); p.update(params or {})
    rent_total = p["rent"] + p["renters_insurance"]
    owning_total = _owning_cost(p, p["annual_rate"])
    # higher is better -> negate cost
    return {"A": -rent_total, "B": -owning_total}


def evaluate_twist(params):
    p = dict(PARAMS); p.update(params or {})
    rent_total = p["rent"] + p["renters_insurance"]
    owning_total = _owning_cost(p, p["twist_rate"])
    return {"A": -rent_total, "B": -owning_total}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    rent = -base["A"]; own = -base["B"]
    print("base  rent=%.2f own=%.2f margin=%.2f%%" % (rent, own, 100 * (own - rent) / rent))
    rent_t = -tw["A"]; own_t = -tw["B"]
    print("twist rent=%.2f own=%.2f margin=%.2f%%" % (rent_t, own_t, 100 * (own_t - rent_t) / rent_t))
