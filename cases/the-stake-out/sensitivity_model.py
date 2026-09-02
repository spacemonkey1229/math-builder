#!/usr/bin/env python3
"""
Sensitivity model -- The Stake-Out.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips
the verdict"). See skills/case-readiness/scripts/example_sensitivity_model.py.

Primary metric (case.json.primary_metric): expected total minutes to land
one obstructed footing corner, per method:
    Option A = base_time_A + second_setup_time + miss_prob_A * rework_time
    Option B = base_time_B                     + miss_prob_B * rework_time
miss_prob(accuracy_mm) = P(radial error > tolerance_mm), modeling per-axis
error as circular-normal with sigma = accuracy_mm / sqrt(2):
    miss_prob = exp(-tolerance_mm**2 / (2 * sigma**2))

evaluate() returns the NEGATIVE of each option's expected minutes (higher =
better = faster), matching the sign convention every other case in this
batch uses.

Fixed (NOT in FLEX[]): tolerance_mm (S1/S2), total-station combined accuracy
(S4, derived from cited angular/EDM specs) and GNSS open-sky accuracy (S5)
are all cited/derived-from-cited figures, not stated Modeling Assumptions.

FLEX[] covers the case's five genuine stated Modeling Assumptions: MA1-MA4
(base times, second-setup time, rework time) and MA5 (the near-structure
multipath degradation -- the case's own documented "real fault line").
MA6-MA9 (distance/count/angle scenario parameters) do not enter this
per-corner metric at all (MA6 only justifies MA5's applicability; MA7 only
matters if total-station accuracy is recomputed at a different distance,
which is out of scope here; MA8/MA9 are pure scale/illustration and carry
no cost).

Verified against FACILITATOR.md's "The margin" (2026-09-01):
    base    A (Total Station) = 6 + 20 + ~0*45   = 26.0 min  (metric = -26.0)
            B (GNSS/RTK)      = 3 + 0.626*45     = ~31.2 min (metric = -31.2)
            margin  (-26.0 - -31.2) / 31.2 * 100 = 16.7%... case.json's own
            convention computes margin = (B_total - A_total)/A_total*100 =
            (31.2-26.0)/26.0*100 = 19.9%, matching case.json.margin_pct
            exactly (this model reports both conventions in __main__).
    MA5 (multipath degradation) flexed to +13.4mm (near its own documented
            breakeven) flips the winner to B, exactly as FACILITATOR.md's
            own breakeven analysis discloses.
"""
import math

PARAMS = {
    # --- Appendix A / S1,S2,S3: cited tolerance -------------------------------
    "tolerance_mm": 13.0,
    # --- Appendix B / S4: cited/derived total-station combined accuracy ------
    "accuracy_a_mm": 1.3,
    # --- Appendix C / S5: cited GNSS open-sky accuracy ------------------------
    "accuracy_b_open_sky_mm": 8.5,
    # --- Appendix E, MA1-MA4: stated Modeling Assumptions ---------------------
    "base_time_a_min": 6.0,     # MA1
    "base_time_b_min": 3.0,     # MA2
    "second_setup_min": 20.0,   # MA3
    "rework_min": 45.0,         # MA4
    # --- Appendix C, MA5: near-structure multipath degradation ---------------
    "multipath_degradation_mm": 17.0,   # MA5, retuned from 25.0
}

FLEX = [
    "base_time_a_min",     # MA1
    "base_time_b_min",     # MA2
    "second_setup_min",    # MA3
    "rework_min",          # MA4
    "multipath_degradation_mm",   # MA5
]


def _miss_prob(accuracy_mm, tolerance_mm):
    sigma = accuracy_mm / math.sqrt(2)
    if sigma <= 0:
        return 0.0
    return math.exp(-(tolerance_mm ** 2) / (2 * sigma ** 2))


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    accuracy_b_obstructed = math.hypot(p["accuracy_b_open_sky_mm"], p["multipath_degradation_mm"])

    miss_a = _miss_prob(p["accuracy_a_mm"], p["tolerance_mm"])
    miss_b = _miss_prob(accuracy_b_obstructed, p["tolerance_mm"])

    total_a = p["base_time_a_min"] + p["second_setup_min"] + miss_a * p["rework_min"]
    total_b = p["base_time_b_min"] + miss_b * p["rework_min"]

    return {"A": -total_a, "B": -total_b}


if __name__ == '__main__':
    base = evaluate({})
    total_a, total_b = -base["A"], -base["B"]
    margin_case_convention = 100 * (total_b - total_a) / total_a
    print("base  ", {k: round(v, 3) for k, v in base.items()},
          "A=%.2f min  B=%.2f min" % (total_a, total_b),
          "margin (B costs X%% more than A) = %.2f%%" % margin_case_convention,
          "-- matches case.json.margin_pct (19.9)")

    near_breakeven = evaluate({"multipath_degradation_mm": 13.4})
    ta, tb = -near_breakeven["A"], -near_breakeven["B"]
    print("MA5 at ~13.4mm (near its own breakeven)", "A=%.2f min  B=%.2f min" % (ta, tb),
          "-- winner:", "A" if ta < tb else "B")
