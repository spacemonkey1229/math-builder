"""
sensitivity_model.py -- The Minimum-Payment Trap

Graded primary metric (case.json.primary_metric): total interest paid over the
eighteen months before Priya's planned mortgage pre-approval conversation,
comparing The Minimum Track (A, pay only the recalculating required minimum)
against The Fixed Push (B, pay a fixed $309.20 every month regardless of how
far the required minimum drops). Lower interest paid is better for Priya, so
evaluate() returns the NEGATIVE of each option's 18-month interest total --
higher score = better, matching this script's "higher wins" convention (same
convention as cases/the-deferred-repair/sensitivity_model.py).

    balance_0 = starting balance                                  (base case)
    balance_n = balance_(n-1) x (1 + monthly_rate) - payment_n     (recursive step)
    interest_n = balance_(n-1) x monthly_rate
    payment_n (Minimum Track)  = max(min_pct x balance_(n-1) + interest_n, min_floor)
    payment_n (Fixed Push)     = fixed_payment  (constant every month)

Appendix A's starting balance [S1] and APR [S2] are real, sourced figures --
NOT flexed by default (cited data, stress-tested by P6 instead). Appendix B's
minimum-payment formula terms (the 1% rate and the $40 floor) [S3] are also a
real, cited, currently-published issuer formula -- not an authored scenario
assumption, so also not swept by FLEX by default. The ONE dial this case
authored as a scenario choice, rather than sourcing or deriving, is the
eighteen-month reference horizon itself (Priya's stated mortgage-conversation
timeline) -- but that is a comparison WINDOW, not a PARAM inside evaluate(),
so it is handled by evaluate()'s own `months` argument rather than by FLEX.

FLEX is therefore empty by default: every numeric PARAM here is either a real
sourced figure (balance, APR, min_pct, min_floor) or a derivation from sourced
figures (fixed_payment, from the standard 36-month amortization formula run on
balance/apr). Per skills/case-readiness/SKILL.md's P5 rule ("Only FLEX[] is
swept by default... cited data is stress-tested by P6 instead"), a case that
authored no scenario assumption correctly sweeps nothing by default. Run with
--flex-all to stress-test the sourced figures anyway.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base (18mo)  A = $2,695.37 interest  ·  B = $2,404.58 interest  ·  margin 10.8%  (A costs more -- matches case.json)
    base (full)  A = 233 months (~19.42y), $14,465.14 total interest
                 B = 36 months, $3,375.11 total interest
"""

PARAMS = {
    # --- Appendix A [S1]/[S2], sourced ---------------------------------------
    "balance0": 7756.0,
    "apr": 0.252,
    # --- Appendix B [S3], sourced minimum-payment formula (Chase) -----------
    "min_pct": 0.01,
    "min_floor": 40.0,
    # --- Appendix C [S4], derived from balance0/apr via the standard 36-month
    #     amortization formula (not a case-authored scenario assumption) -----
    "fixed_payment": 309.20,
}

# No scenario assumption was authored for this case (RESEARCH_LOG.md) -- every
# PARAM above is sourced or a derivation from sourced figures, so FLEX is
# correctly empty by default (see module docstring). --flex-all overrides.
FLEX = []


def _simulate(balance, apr, months_cap, payment_fn):
    """Iterate the recursive balance model. Returns (total_interest, total_principal, months_run, ending_balance)."""
    r = apr / 12.0
    total_interest = 0.0
    total_principal = 0.0
    m = 0
    while balance > 0.01 and m < 1200:
        m += 1
        interest = balance * r
        payment = payment_fn(balance, interest, m)
        payment = min(payment, balance + interest)  # never overpay past $0
        principal = payment - interest
        balance = balance - principal
        total_interest += interest
        total_principal += principal
        if months_cap and m >= months_cap:
            break
    return total_interest, total_principal, m, balance


def _min_payment(balance, interest, pct, floor):
    return max(pct * balance + interest, floor)


def evaluate(params, months=18):
    """Returns {"A": score, "B": score} for the `months`-long reference window (default 18, the graded horizon).
    Score is NEGATIVE total interest paid in that window (higher score = cheaper = better for Priya)."""
    p = dict(PARAMS)
    p.update(params or {})
    ti_a, _, _, _ = _simulate(p["balance0"], p["apr"], months,
                               lambda b, i, m: _min_payment(b, i, p["min_pct"], p["min_floor"]))
    ti_b, _, _, _ = _simulate(p["balance0"], p["apr"], months,
                               lambda b, i, m, pay=p["fixed_payment"]: pay)
    return {"A": -ti_a, "B": -ti_b}


def evaluate_full_payoff(params):
    """Full lifetime payoff for each strategy -- the dramatic, un-engineered D4 numbers.
    Returns dict with months/years/total_interest per option. Not used for the graded margin
    (see FACILITATOR.md's 'why eighteen months, not lifetime')."""
    p = dict(PARAMS)
    p.update(params or {})
    ti_a, tp_a, m_a, _ = _simulate(p["balance0"], p["apr"], None,
                                    lambda b, i, m: _min_payment(b, i, p["min_pct"], p["min_floor"]))
    ti_b, tp_b, m_b, _ = _simulate(p["balance0"], p["apr"], None,
                                    lambda b, i, m, pay=p["fixed_payment"]: pay)
    return {
        "A": {"months": m_a, "years": round(m_a / 12.0, 2), "total_interest": round(ti_a, 2), "total_paid": round(ti_a + tp_a, 2)},
        "B": {"months": m_b, "years": round(m_b / 12.0, 2), "total_interest": round(ti_b, 2), "total_paid": round(ti_b + tp_b, 2)},
    }


if __name__ == '__main__':
    base = evaluate({})
    ia, ib = -base["A"], -base["B"]
    win = "A" if ia < ib else "B"
    lo, hi = min(ia, ib), max(ia, ib)
    margin = 100.0 * (hi - lo) / hi
    print("18-month interest: A=$%.2f  B=$%.2f  cheaper=%s  margin=%.1f%%" % (ia, ib, win, margin))

    full = evaluate_full_payoff({})
    print("Full payoff -- A: %d months (%.2fy), $%.2f total interest, $%.2f total paid" %
          (full["A"]["months"], full["A"]["years"], full["A"]["total_interest"], full["A"]["total_paid"]))
    print("Full payoff -- B: %d months (%.2fy), $%.2f total interest, $%.2f total paid" %
          (full["B"]["months"], full["B"]["years"], full["B"]["total_interest"], full["B"]["total_paid"]))
