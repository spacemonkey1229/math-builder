#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Fee Ladder.

Tier 2 probe 5 ("flex each stated assumption by +-50%; report which flips
the verdict") needs a runnable model of the case's own arithmetic.

CONTRACT — two public names:

    PARAMS                     dict[str, number]   every dial the case STATES
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better

The case's SPEC Section 2 primary metric (case.json.balance.margin_basis) is
fee-quote error, as a percentage of the true recursively-computed annual fee:
    margin_pct = |FeeA - FeeB_true| / FeeB_true * 100

Higher margin_pct means a WORSE (less accurate) Option A quote. The probe's
contract is "higher is better", so this model treats accuracy as the thing
being scored: evaluate() returns the NEGATIVE of each option's dollar error
against Option B's own true fee (Option B's error against itself is
definitionally zero, so B always scores 0 -- exactly correct by
construction; A scores the negative of its dollar gap, so a smaller gap is
a higher, better score, and a LARGER gap makes A's evaluate() score more
negative, i.e. worse).

Mechanism modeled explicitly (this is the whole point of the case): Option
B's true fee is NOT a simple sum of tier_rate x AUC. It is the exact result
of a real recursive definition -- B_k = B_{k-1} * (1 - r_k), each tier's
fee computed on the balance remaining AFTER the previous tier's own fee was
already subtracted (Appendix C) -- not a standard marginal-bracket sum. The
model reproduces that recursion exactly, tier by tier, rather than
shortcutting to a closed-form product (both give the same answer; the
recursive walk is kept explicit here because it is what Appendix C/D1
actually specifies and what case-qa's probes should be checking against).

FLEX[] sweeps the case's own stated Modeling Assumptions that feed this
metric's arithmetic: MA1 (client AUC), MA5 (the Quick-Quote card's flat
rate), and MA6's four tier rates. MA2/MA3 (deadline, analyst time) and MA4
(tier count) are not swept: MA2/MA3 are narrative flavor, not load-bearing
on the numeric margin (case.json's own sensitivity notes say so
explicitly), and MA4 (tier count) is a structural choice already baked into
FLEX's four individual tier-rate parameters rather than a separate dial.
"""

PARAMS = {
    # --- Appendix A / MA1: today's client's total AUC (USD) -----------------
    "client_auc": 850_000_000.0,
    # --- Appendix B / MA5: Quick-Quote Reference Card flat rate (bp) --------
    "quick_quote_rate_bp": 3.90,
    # --- Appendix C / MA6: Full Ladder's four tier rates (bp) ---------------
    "tier1_bp": 2.00,
    "tier2_bp": 1.25,
    "tier3_bp": 0.75,
    "tier4_bp": 0.50,
}

# Probe 5 flexes THESE and only these: the case's own stated Modeling
# Assumptions that feed the graded primary metric's arithmetic.
FLEX = [
    "client_auc",          # MA1, Appendix A
    "quick_quote_rate_bp",  # MA5, Appendix B -- the case's real fulcrum (with the tier rates)
    "tier1_bp",             # MA6, Appendix C
    "tier2_bp",             # MA6, Appendix C
    "tier3_bp",              # MA6, Appendix C
    "tier4_bp",              # MA6, Appendix C
]


def _true_fee_recursive(auc, tier_rates_bp):
    """Walks Appendix C's recursion exactly: each tier's fee is computed on
    the balance remaining AFTER the previous tier's own fee was deducted."""
    balance = auc
    total_fee = 0.0
    trail = []
    for rate_bp in tier_rates_bp:
        r = rate_bp / 10_000.0
        fee = r * balance
        balance -= fee
        total_fee += fee
        trail.append({"rate_bp": rate_bp, "fee": fee, "balance_after": balance})
    return total_fee, balance, trail


def evaluate_detail(params):
    p = dict(PARAMS)
    p.update(params or {})
    auc = p["client_auc"]
    tier_rates = [p["tier1_bp"], p["tier2_bp"], p["tier3_bp"], p["tier4_bp"]]

    fee_b_true, balance_after, trail = _true_fee_recursive(auc, tier_rates)
    fee_a = auc * (p["quick_quote_rate_bp"] / 10_000.0)

    gap = fee_a - fee_b_true
    margin_pct = abs(gap) / fee_b_true * 100.0 if fee_b_true else float("inf")

    detail = {
        "fee_a_quick_quote": fee_a,
        "fee_b_full_ladder": fee_b_true,
        "balance_after_tier4": balance_after,
        "tier_trail": trail,
        "gap": gap,
        "margin_pct": margin_pct,
    }
    return detail


def evaluate(params):
    """Tier 2 probe 5 contract: evaluate(params) -> {'A': metric, 'B': metric}
    ONLY -- no extra return values. Higher is better. B is exact by
    construction (its own error against itself is 0); A scores the negative
    of its absolute dollar gap against B's true fee, so a bigger gap is a
    more negative (worse) score for A."""
    d = evaluate_detail(params)
    return {"A": -abs(d["gap"]), "B": 0.0}


if __name__ == '__main__':
    base = evaluate_detail({})
    print("Full Ladder true fee: $%.2f" % base["fee_b_full_ladder"])
    for row in base["tier_trail"]:
        print("  tier %.2fbp  fee=$%.2f  balance_after=$%.2f" %
              (row["rate_bp"], row["fee"], row["balance_after"]))
    print("Quick-Quote fee:      $%.2f" % base["fee_a_quick_quote"])
    print("gap: $%.2f   margin_pct: %.2f%%" % (base["gap"], base["margin_pct"]))
    print()

    # Scale-invariance check (D4): margin_pct should be identical at other AUC sizes.
    for auc in (300_000_000.0, 850_000_000.0, 1_200_000_000.0):
        d = evaluate_detail({"client_auc": auc})
        print("AUC $%.0f -> margin_pct %.4f%%" % (auc, d["margin_pct"]))
    print()

    # Probe-5-style +-50% flex sweep on each FLEX parameter.
    print("FLEX sweep (+-50%% on each parameter individually):")
    for key in FLEX:
        base_val = PARAMS[key]
        for mult, label in ((0.5, "-50%"), (1.5, "+50%")):
            d = evaluate_detail({key: base_val * mult})
            flips = (d["margin_pct"] > 20.0) != (base["margin_pct"] > 20.0)
            flag = "  <-- crosses SPEC Sec2 ~20% cap" if flips else ""
            print("  %-20s %-5s -> margin_pct %6.2f%%%s" % (key, label, d["margin_pct"], flag))
