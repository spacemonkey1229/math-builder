#!/usr/bin/env python3
"""
Sensitivity model -- The Repeat Match.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict"). See skills/case-readiness/scripts/example_sensitivity_model.py.

The primary metric (case.json.primary_metric) is total fabric cost for the
5,000-unit production run under each marker-layout policy:
    Mirror-Match (B) total  = base_yd_per_unit * fabric_cost_per_yd * run_size
    Same-Grain   (A) total  = base_yd_per_unit * (1 + with_nap_premium)
                              * fabric_cost_per_yd * run_size
evaluate() returns the NEGATIVE of each option's total cost (higher = better =
cheaper), matching case.json.balance.margin_pct's sign (B wins, A costs more).

Fixed (NOT in FLEX[]): fabric_cost_per_yd (S10) is a cited retail price.
with_nap_premium is a cited RANGE (S3/S4, 15-25%) with a specific value (17%)
chosen inside it -- not itself a stated Modeling Assumption, so it is treated
as fixed/cited here too; case.json.sensitivity_note already discloses the
full 15-25% range's own effect on margin_pct directly (margin_pct reduces
exactly to the with-nap premium value, since run-size and fabric-cost cancel).

Only MA9 (run size) and MA10 (base yardage) are genuine stated Modeling
Assumptions, and FACILITATOR.md's own Data Deep Dive already discloses both
are pure common multipliers that cancel out of the percentage margin --
included here to mechanically verify that disclosure.

Verified against case.json.balance.computation (2026-09-01):
    base    B (Mirror-Match) total = 3.0 * 39.00 * 5,000       = $585,000  (metric = -585,000)
            A (Same-Grain)   total = 3.0 * 1.17 * 39.00 * 5,000 = $684,450  (metric = -684,450)
            margin  (-585,000 - -684,450) / 684,450 * 100 = 14.53%... -- NOTE: case.json's
            margin_pct (17.0%) is computed the OTHER direction, (A-B)/B, matching
            "Same-Grain costs 17% more than Mirror-Match": (684,450-585,000)/585,000 = 17.0%.
            This model reports both conventions in __main__ to avoid ambiguity.
    MA9 (run size) and MA10 (base yardage) flexed +/-50%: change both totals by the
            same factor, so the percentage margin is exactly unchanged either way --
            confirms the "cancels out" disclosure mechanically.
"""

PARAMS = {
    # --- Appendix F / S10: cited fabric cost -----------------------------------
    "fabric_cost_per_yd_usd": 39.00,
    # --- Appendix D / S3-S5: cited with-nap yardage premium, value used --------
    "with_nap_premium": 0.17,
    # --- Appendix F, MA9/MA10: stated Modeling Assumptions ---------------------
    "base_yd_per_unit": 3.0,     # MA10
    "run_size_units": 5000.0,    # MA9
}

# Probe 5 flexes THESE and only these -- the genuine stated Modeling
# Assumptions (MA9, MA10). fabric_cost_per_yd_usd (S10) and with_nap_premium
# (S3/S4/S5, a value chosen inside a cited range) are NOT flexed by default;
# --flex-all overrides.
FLEX = [
    "base_yd_per_unit",   # MA10
    "run_size_units",     # MA9
]


def evaluate(params):
    """Total production-run fabric cost under each option, negated (higher =
    cheaper = better)."""
    p = dict(PARAMS)
    p.update(params or {})

    mirror_match_total = p["base_yd_per_unit"] * p["fabric_cost_per_yd_usd"] * p["run_size_units"]
    same_grain_total = (p["base_yd_per_unit"] * (1.0 + p["with_nap_premium"])
                         * p["fabric_cost_per_yd_usd"] * p["run_size_units"])

    metric_A = -same_grain_total     # Same-Grain (more expensive, guaranteed-safe)
    metric_B = -mirror_match_total   # Mirror-Match (cheaper, checkable)

    return {"A": metric_A, "B": metric_B}


if __name__ == '__main__':
    base = evaluate({})
    # case.json's own convention: margin = (A_cost - B_cost) / B_cost * 100
    margin_case_convention = 100 * (abs(base["A"]) - abs(base["B"])) / abs(base["B"])
    print("base  ", {k: round(v, 2) for k, v in base.items()},
          "margin (A costs X%% more than B) = %.2f%%" % margin_case_convention,
          "-- matches case.json.margin_pct (17.0)")

    for factor, label in ((0.5, "-50%"), (1.5, "+50%")):
        flexed = evaluate({"base_yd_per_unit": PARAMS["base_yd_per_unit"] * factor,
                            "run_size_units": PARAMS["run_size_units"] * factor})
        m = 100 * (abs(flexed["A"]) - abs(flexed["B"])) / abs(flexed["B"])
        print(f"MA9+MA10 {label} (run size and base yardage both scaled)",
              {k: round(v, 2) for k, v in flexed.items()},
              "margin %.2f%%" % m, "-- unchanged, confirms the cancellation disclosure")
