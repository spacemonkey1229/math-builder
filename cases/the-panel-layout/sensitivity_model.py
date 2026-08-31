#!/usr/bin/env python3
"""
Sensitivity model -- The Panel Layout.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The case's real dilemma turns on the primary metric: expected seconds of
predicted task-completion time per successful actuation, across the full
control sequence (case.json.primary_metric). LOWER is actually better for
that raw quantity, so evaluate() returns its NEGATIVE -- this keeps the
contract's "higher is better" convention intact (max() correctly picks the
faster/better option) while the underlying arithmetic still computes real
seconds. `raw_expected_seconds()` below exposes the real (positive, lower-is-
better) figures for human/report reading.

Fitts's Law coefficients a, b (S1: Hassan, Magee & MacKenzie, HCII 2019,
MEDIUM confidence) are cited data, not a stated Modeling Assumption -- fixed,
not in PARAMS/FLEX. Probe 6 (data decay) covers S1 instead. Every other dial
below is one of the case's 13 disclosed Modeling Assumptions (Appendix D,
MA1-MA13); MA9 (linear interpolation) is a structural modeling choice, not a
numeric dial, so it has no PARAMS entry and cannot be flexed by a percentage.

Verified against case.md, case.json and FACILITATOR.md (2026-08-31 remediation):
    base (raw, seconds, lower is better):
        T(x=0, Long Reach)          = 4.625   (case.json.derived.T_x0_s)
        T(x=1, Close Reach)         = 4.611   (case.json.derived.T_x1_s)
        T(x*=0.4273, interior min)  = 4.607   (case.json.derived.T_xstar_s)
        E(Long Reach), miss-weighted  = 4.777  (case.json.derived.E_long_reach_s)
        E(Close Reach), miss-weighted = 4.894  (case.json.derived.E_close_reach_s)
        margin_pct = 100*(E1-E0)/E0 = 2.46%    (matches case.json.balance.margin_pct)
        winner: B (Long Reach), on the miss-rate-weighted primary metric.

    Three assumptions independently flip the verdict -- MECHANICALLY VERIFIED,
    not assumed from the case's own prose (the same check on the Search Box
    case, this session, found its own claimed flip points were wrong):
        MA6 (other-controls distance, Close Reach, d_o1): verified flip
            threshold d_o1 ~= 118.07 mm (case claims "~118mm" -- MATCHES).
        MA8 (count of other required controls, n): verified continuous
            threshold n* ~= 2.36, i.e. flips between the integers n=2 and
            n=3 (case claims exactly this -- MATCHES). Case uses n=3 (B wins);
            n=1 or n=2 -> A (Close Reach) wins.
        MA13 (other-controls miss rate, Close Reach, mo1): verified flip
            threshold mo1 ~= 0.0412 (4.12%) (case claims "~4.1%" -- MATCHES).
    No discrepancy found between the case's stated flip claims and the
    mechanically re-derived thresholds for MA6, MA8, or MA13.
"""
import math

# --- Fixed: cited data (sources[] S1), not a stated Modeling Assumption ------
FITTS_A_S = 0.6992     # [S1] intercept, seconds
FITTS_B_S_PER_BIT = 0.1714  # [S1] slope, seconds/bit

PARAMS = {
    # --- Appendix A / Modeling Assumptions (Appendix D) ----------------------
    "ma1_confirm_width_x0_mm": 10.0,   # MA1  Confirm width, Long Reach (x=0)
    "ma2_confirm_width_x1_mm": 30.0,   # MA2  Confirm width, Close Reach (x=1)
    "ma3_confirm_dist_x0_mm": 120.0,   # MA3  Confirm distance, Long Reach (x=0)
    "ma4_confirm_dist_x1_mm": 60.0,    # MA4  Confirm distance, Close Reach (x=1)
    "ma5_other_dist_x0_mm": 80.0,      # MA5  Other-controls distance, Long Reach (x=0)
    "ma6_other_dist_x1_mm": 140.0,     # MA6  Other-controls distance, Close Reach (x=1)
    "ma7_other_width_mm": 20.0,        # MA7  Fixed width of each other control
    "ma8_other_count": 3.0,            # MA8  Count of other required controls
    # MA9 (linear interpolation in x) is structural, not a numeric dial --
    # no PARAMS entry; the interpolation itself is fixed in evaluate().
    "ma10_confirm_miss_x0": 0.06,      # MA10 Confirm miss rate, Long Reach (x=0)
    "ma11_other_miss_x0": 0.02,        # MA11 Other-controls miss rate, Long Reach (x=0)
    "ma12_confirm_miss_x1": 0.01,      # MA12 Confirm miss rate, Close Reach (x=1)
    "ma13_other_miss_x1": 0.07,        # MA13 Other-controls miss rate, Close Reach (x=1)
}

# Probe 5 flexes THESE and only these -- every numeric stated Modeling
# Assumption (MA1-MA8, MA10-MA13). Fitts's Law coefficients (S1) are cited
# data, excluded per the "only FLEX[] is swept" rule; --flex-all overrides.
FLEX = [
    "ma1_confirm_width_x0_mm",
    "ma2_confirm_width_x1_mm",
    "ma3_confirm_dist_x0_mm",
    "ma4_confirm_dist_x1_mm",
    "ma5_other_dist_x0_mm",
    "ma6_other_dist_x1_mm",   # case's own documented flip dial (~118mm)
    "ma7_other_width_mm",
    "ma8_other_count",        # case's own documented flip dial (n=2/3)
    "ma10_confirm_miss_x0",
    "ma11_other_miss_x0",
    "ma12_confirm_miss_x1",
    "ma13_other_miss_x1",     # case's own documented flip dial (~4.1%)
]


def _mt(distance_mm, width_mm):
    """Fitts's Law, Shannon formulation: MT = a + b*log2(D/W + 1), seconds."""
    index_of_difficulty = math.log2(distance_mm / width_mm + 1.0)
    return FITTS_A_S + FITTS_B_S_PER_BIT * index_of_difficulty


def _lerp(v0, v1, x):
    return v0 + (v1 - v0) * x


def _confirm_width(p, x):
    return _lerp(p["ma1_confirm_width_x0_mm"], p["ma2_confirm_width_x1_mm"], x)


def _confirm_dist(p, x):
    return _lerp(p["ma3_confirm_dist_x0_mm"], p["ma4_confirm_dist_x1_mm"], x)


def _other_dist(p, x):
    return _lerp(p["ma5_other_dist_x0_mm"], p["ma6_other_dist_x1_mm"], x)


def raw_time(params, x):
    """T(x): whole-panel predicted completion time for one pass, seconds
    (D1/D2/D3 -- the un-weighted movement-time model, no miss rate)."""
    p = dict(PARAMS); p.update(params or {})
    n = p["ma8_other_count"]
    mt_confirm = _mt(_confirm_dist(p, x), _confirm_width(p, x))
    mt_other = _mt(_other_dist(p, x), p["ma7_other_width_mm"])
    return mt_confirm + n * mt_other


def find_x_star(params):
    """Interior critical point of T(x) on [0,1], by fine numeric search (the
    case's own closed form is x* = 3/4 - sqrt(15)/12 at the base PARAMS;
    re-derived numerically here so a flexed model still finds its own x*)."""
    p = dict(PARAMS); p.update(params or {})
    xs = [i / 100000.0 for i in range(100001)]
    best_x, best_t = 0.0, raw_time(p, 0.0)
    for x in xs:
        t = raw_time(p, x)
        if t < best_t:
            best_t, best_x = t, x
    return best_x, best_t


def expected_seconds(params, x, miss_confirm, miss_other):
    """D4: expected seconds per successful actuation at layout x, given the
    Confirm control's and the other controls' miss rate at that x -- each
    control retried (same MT, same miss rate) until it succeeds, so the
    expected number of attempts is 1/(1-miss_rate)."""
    p = dict(PARAMS); p.update(params or {})
    n = p["ma8_other_count"]
    mt_confirm = _mt(_confirm_dist(p, x), _confirm_width(p, x))
    mt_other = _mt(_other_dist(p, x), p["ma7_other_width_mm"])
    return mt_confirm / (1.0 - miss_confirm) + n * mt_other / (1.0 - miss_other)


def raw_expected_seconds(params=None):
    """Human-readable (lower-is-better) figures for D1-D4, not part of the
    Tier 2 contract. Returns T(0), T(1), T(x*), and the D4 miss-rate-weighted
    E(Long Reach) / E(Close Reach) the case's balance_test.margin_pct is
    computed from."""
    p = dict(PARAMS); p.update(params or {})
    x_star, t_star = find_x_star(p)
    return {
        "T_x0": raw_time(p, 0.0),
        "T_x1": raw_time(p, 1.0),
        "x_star": x_star,
        "T_xstar": t_star,
        "E_long_reach": expected_seconds(p, 0.0, p["ma10_confirm_miss_x0"], p["ma11_other_miss_x0"]),
        "E_close_reach": expected_seconds(p, 1.0, p["ma12_confirm_miss_x1"], p["ma13_other_miss_x1"]),
    }


def evaluate(params):
    """Tier 2 contract: {"A": metric, "B": metric}, higher is better.
    A = Close Reach (x=1), B = Long Reach (x=0). The case's actual graded
    primary metric is D4's miss-rate-weighted expected seconds per successful
    actuation -- LOWER is really better, so the metric returned here is the
    NEGATIVE of those seconds (higher/less-negative = fewer expected seconds
    = the better option), per this file's docstring."""
    p = dict(PARAMS); p.update(params or {})
    e_close = expected_seconds(p, 1.0, p["ma12_confirm_miss_x1"], p["ma13_other_miss_x1"])
    e_long = expected_seconds(p, 0.0, p["ma10_confirm_miss_x0"], p["ma11_other_miss_x0"])
    return {"A": -e_close, "B": -e_long}


if __name__ == '__main__':
    raw = raw_expected_seconds({})
    print("base raw figures (seconds, lower is better):")
    for k, v in raw.items():
        print(f"  {k} = {v:.6f}" if k != "x_star" else f"  {k} = {v:.6f}")
    base = evaluate({})
    print("evaluate() (higher-is-better contract):", {k: round(v, 6) for k, v in base.items()})
    margin = 100.0 * (raw["E_close_reach"] - raw["E_long_reach"]) / raw["E_long_reach"]
    print(f"margin_pct (B beats A) = {margin:.4f}  (case.json.balance.margin_pct = 2.46)")

    # --- verify the three claimed dilemma-flipping assumptions mechanically --
    def bisect_threshold(param_name, lo, hi, tol=1e-6):
        """Find the value of `param_name` where evaluate()'s A/B ordering
        flips, by bisection. Assumes a single crossing in [lo, hi]."""
        def a_wins(v):
            r = evaluate({param_name: v})
            return r["A"] > r["B"]
        base_a_wins = a_wins(lo)
        for _ in range(200):
            mid = (lo + hi) / 2.0
            if a_wins(mid) == base_a_wins:
                lo = mid
            else:
                hi = mid
            if hi - lo < tol:
                break
        return (lo + hi) / 2.0

    ma6_threshold = bisect_threshold("ma6_other_dist_x1_mm", 1.0, 300.0)
    ma13_threshold = bisect_threshold("ma13_other_miss_x1", 0.0001, 0.99)
    ma8_threshold = bisect_threshold("ma8_other_count", 0.01, 20.0)
    print(f"\nMA6 flip threshold (d_o1, mm): {ma6_threshold:.3f}  (case claims ~118mm)")
    print(f"MA8 flip threshold (n, continuous): {ma8_threshold:.4f}  (case claims flips between n=2/n=3)")
    print(f"MA13 flip threshold (mo1): {ma13_threshold:.5f}  (case claims ~4.1%)")
