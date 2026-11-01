#!/usr/bin/env python3
"""
SENSITIVITY MODEL — The Equivalent Ledger.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own D5 cost-comparison arithmetic.

CONTRACT — exactly two public names, plus an optional twist:

    PARAMS                     dict[str, number]   every dial the case states
    evaluate(params) -> dict   {"A": metric, "B": metric}  higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

This model covers ONLY D5's cost comparison (Option A's expected cost of shipping
unverified vs. Option B's cost of a full factoring verification). D1-D4's proof
that O(n) and R(n) are NOT the same expression outside n={4,10} is a fixed
structural fact of the two constructed formulas (MA1/MA2), not a stated scenario
assumption -- it is not a FLEX dial, and it is verified separately below via
gcf()/is_prime() rather than swept.

Metric convention: both options are COSTS (lower is better), so evaluate()
returns the NEGATIVE of each cost -- "higher is better" then means "the option
with the smaller cost has the larger (less negative) value," matching the
tier2_probes.py contract.

Verified against cases/the-equivalent-ledger/case.json and FACILITATOR.md:
    base   A = -850.00  ·  B = -783.04  ·  margin 7.88%   (B / The Full Factor wins)
    twist  A = -25920.00 · B = -783.04  ·  B wins by a much wider margin
"""
from math import gcd
from functools import reduce

PARAMS = {
    # --- Appendix C: verification staffing/cost (MA7, [S1]) -----------------
    "engineers": 2,
    "hours_per_engineer": 8.0,
    "wage_per_hour": 48.94,          # [S1] BLS OEWS 15-1253, cited -- not flexed
    # --- Appendix D: risk exposure if deployed unverified (MA8, MA9) --------
    "p_defect": 0.034,
    "cost_of_error": 25000.0,
    # --- The Twist (FACILITATOR.md): the newly-announced ~40-item batch -----
    "twist_batch_n": 40,
    "twist_nights_until_detected": 4,
}

# Probe 5 flexes THESE and only these. SPEC §2 asks for sensitivity to STATED
# ASSUMPTIONS, not to cited measurements: wage_per_hour is cited ([S1]) and is
# deliberately excluded, same reasoning as Cold Chain's cold_life_A_h/B_h.
# "engineers" (a simple headcount of 2) is a minor operational choice already
# well-represented by flexing hours_per_engineer; left out to avoid a redundant,
# less meaningful dial ("1.5 engineers" has no real-world reading).
FLEX = [
    "hours_per_engineer",   # MA7 -- verification-time estimate
    "p_defect",             # MA8 -- grounded by [S2], but the specific value is assumed
    "cost_of_error",        # MA9 -- the case's single most load-bearing dial
]

# --- The two constructed formulas (MA1, MA2) -- fixed scenario facts, not flexed.
def O(n):
    return 48 * n**2 + 180 * n


def R(n):
    return 54 * n**2 + 96 * n + 240


def is_prime(k):
    if k < 2:
        return False
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True


def gcf_of(values):
    return reduce(gcd, values)


def d4_proof():
    """The case's actual mathematical payload: fully factor O(n) and R(n) by
    pulling the GCF of their coefficients, and determine whether every term of
    each shares a common factor of n. This is the structural fact D4 asks
    students to name -- it is NOT a function of any FLEX[] dial."""
    gcf_o = gcf_of([48, 180])
    gcf_r = gcf_of([54, 96, 240])
    o_has_n_factor_everywhere = (O(0) == 0)   # every term of O(n) carries n <=> O(0)=0
    r_has_n_factor_everywhere = (R(0) == 0)
    same_for_all_n = o_has_n_factor_everywhere and r_has_n_factor_everywhere and gcf_o == gcf_r
    agreement_ns = [n for n in range(0, 101) if O(n) == R(n)]
    return {
        "gcf_O": gcf_o,
        "gcf_R": gcf_r,
        "O_factored": f"{gcf_o}n({48//gcf_o}n + {180//gcf_o})",
        "R_factored": f"{gcf_r}({54//gcf_r}n^2 + {96//gcf_r}n + {240//gcf_r})",
        "O_has_common_n_factor": o_has_n_factor_everywhere,
        "R_has_common_n_factor": r_has_n_factor_everywhere,
        "provably_equivalent_for_all_n": same_for_all_n,
        "agreement_points_checked_0_to_100": agreement_ns,
    }


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    cost_B = p["engineers"] * p["hours_per_engineer"] * p["wage_per_hour"]
    cost_A = p["p_defect"] * p["cost_of_error"]
    return {"A": -cost_A, "B": -cost_B}


def evaluate_twist(params):
    """The twist: compliance confirms next quarter's batch will run ~40
    unmatched items/night from a newly onboarded partner bank -- far outside
    the two batch sizes (4, 10) the rewritten formula has ever been tested
    against. Once D4's proof exists, Option A's true expected cost is no
    longer a flat probability-weighted estimate: it is the ACTUAL per-night
    dollar gap (R(n) - O(n) at the new batch size) accumulated over however
    many nights pass before anyone notices."""
    p = dict(PARAMS)
    p.update(params or {})
    n = p["twist_batch_n"]
    per_night_gap = abs(R(n) - O(n))
    cost_A_twist = per_night_gap * p["twist_nights_until_detected"]
    cost_B = p["engineers"] * p["hours_per_engineer"] * p["wage_per_hour"]
    return {"A": -cost_A_twist, "B": -cost_B}


if __name__ == '__main__':
    base = evaluate({})
    tw = evaluate_twist({})
    proof = d4_proof()
    base_costs = {k: -v for k, v in base.items()}
    lo = min(base_costs, key=base_costs.get)
    hi = max(base_costs, key=base_costs.get)
    margin = 100.0 * (base_costs[hi] - base_costs[lo]) / base_costs[hi]
    print("base costs", {k: round(v, 2) for k, v in base_costs.items()},
          "winner (lower cost) =", lo, "margin %.2f%%" % margin)
    print("D4 proof:", proof)
    print("twist costs", {k: round(-v, 2) for k, v in tw.items()})
