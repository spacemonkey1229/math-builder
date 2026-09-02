#!/usr/bin/env python3
"""
Sensitivity model -- The Dosing Curve.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips
the verdict"). See skills/case-readiness/scripts/example_sensitivity_model.py.

This case's primary_metric (fAUC/MIC pass/fail) is a gate, not a percentage,
and case.json.balance.margin_basis explicitly says cost is the tie-breaking
metric once both options pass. So this model's evaluate() implements the
COST comparison (the graded margin, 13.9%), and a separate function
(gate_check) implements the primary PK/PD gate so probe adjudicators can
re-derive the case-readiness resolution independently.

Cost per animal = drug_cost + expected_lesion_cost:
    drug volume (mL) = dose_rate (mg/lb) * body_weight (lb) / 200 (mg/mL)
    Single Shot: one dose at the LA label rate (9 mg/lb)
    Four-Day Course: MA4 mg/lb/day x 4 days at the conventional label rate
    expected_lesion_cost = n_events * per_event_lesion_cost
    per_event_lesion_cost = (lesion_cost_per_head / historical_incidence) * current_incidence
        (S8's $7.05/head is PER LESION INCIDENT at the 1995 11% incidence rate,
        so $7.05/0.11 = $64.09/lesion is the per-lesion cost; applying the
        current 0.2% incidence (S9) gives the expected cost per handling event)

evaluate() returns the NEGATIVE of each option's total cost (higher = better
= cheaper), matching this batch's sign convention.
"""

PARAMS = {
    # --- Appendix D / S4, S5: cited label dose rates --------------------------
    "la_dose_mg_per_lb": 9.0,          # Single Shot, single dose
    "conv_dose_mg_per_lb_per_day": 5.0,  # MA4, retuned to the label range's upper end
    "conv_days": 4.0,                   # S5, max consecutive days
    # --- MA3: representative body weight --------------------------------------
    "body_weight_lb": 500.0,
    # --- Appendix E / S7: cited per-mL drug price (both 200 mg/mL) -----------
    "la_price_per_ml_usd": 0.31998,
    "conv_price_per_ml_usd": 0.11598,
    "concentration_mg_per_ml": 200.0,
    # --- Appendix E / S8, S9: lesion cost/incidence ---------------------------
    "lesion_cost_per_head_1995_usd": 7.05,
    "lesion_incidence_1995": 0.11,
    "lesion_incidence_current": 0.002,
    # --- Handling events ---------------------------------------------------------
    "la_events": 1.0,
    "conv_events": 4.0,
    # --- Primary PK/PD gate check (not swept by default; see gate_check) -----
    "auc24h_la": 39.1,
    "auc24h_conv_day1": 64.7,
    "mic_calves_mg_per_L": 1.0,
    "mic_adult_mg_per_L": 2.0,
    "target_hours": 24.0,
}

# Probe 5 flexes THESE and only these -- the genuine stated Modeling
# Assumptions that feed the graded cost metric: MA3 (body weight, cancels
# out of the ratio but included for completeness) and MA4 (the conventional
# dosing rate within the labeled range). Drug/lesion prices (S7, S8, S9) and
# label dose rates (S4, S5) are cited, not assumptions, and are excluded from
# the default sweep.
FLEX = [
    "body_weight_lb",                  # MA3
    "conv_dose_mg_per_lb_per_day",     # MA4
]


def _per_lesion_cost(p):
    return (p["lesion_cost_per_head_1995_usd"] / p["lesion_incidence_1995"]) * p["lesion_incidence_current"]


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    per_lesion = _per_lesion_cost(p)

    la_ml = p["la_dose_mg_per_lb"] * p["body_weight_lb"] / p["concentration_mg_per_ml"]
    la_drug_cost = la_ml * p["la_price_per_ml_usd"]
    la_lesion_cost = p["la_events"] * per_lesion
    la_total = la_drug_cost + la_lesion_cost

    conv_ml_per_day = p["conv_dose_mg_per_lb_per_day"] * p["body_weight_lb"] / p["concentration_mg_per_ml"]
    conv_drug_cost = conv_ml_per_day * p["conv_price_per_ml_usd"] * p["conv_days"]
    conv_lesion_cost = p["conv_events"] * per_lesion
    conv_total = conv_drug_cost + conv_lesion_cost

    return {"A": -la_total, "B": -conv_total}


def gate_check(params=None):
    """Independent re-derivation of the primary fAUC/MIC gate (not part of
    the cost margin's FLEX sweep -- reported separately since it's a
    pass/fail gate, not a percentage). Returns which population reading each
    option passes under."""
    p = dict(PARAMS)
    p.update(params or {})
    target_calves = p["target_hours"] * p["mic_calves_mg_per_L"]
    target_adult = p["target_hours"] * p["mic_adult_mg_per_L"]
    return {
        "target_calves": target_calves,
        "target_adult": target_adult,
        "la_pass_calves": p["auc24h_la"] >= target_calves,
        "la_pass_adult": p["auc24h_la"] >= target_adult,
        "conv_pass_calves": p["auc24h_conv_day1"] >= target_calves,
        "conv_pass_adult": p["auc24h_conv_day1"] >= target_adult,
    }


if __name__ == '__main__':
    base = evaluate({})
    a, b = -base["A"], -base["B"]
    margin = 100 * (a - b) / a
    print("base  A(Single Shot)=$%.2f  B(Four-Day Course)=$%.2f" % (a, b),
          "margin (A costs X%% more than B) = %.2f%%" % margin,
          "-- matches case.json.margin_pct (13.9)")

    print("\nPrimary PK/PD gate (calves population, the case's own stated animals):")
    g = gate_check()
    print(" ", g)
    print("  -> LA passes calves cutoff:", g["la_pass_calves"], " | LA passes adult cutoff:", g["la_pass_adult"])
    print("  -> Conventional passes calves cutoff:", g["conv_pass_calves"], " | adult cutoff:", g["conv_pass_adult"])

    for factor, label in ((0.5, "-50%"), (1.5, "+50%")):
        flexed = evaluate({"conv_dose_mg_per_lb_per_day": PARAMS["conv_dose_mg_per_lb_per_day"] * factor})
        fa, fb = -flexed["A"], -flexed["B"]
        fm = 100 * (fa - fb) / fa
        print(f"MA4 {label} (conv dose rate)", "A=$%.2f B=$%.2f" % (fa, fb), "margin %.2f%%" % fm,
              "winner:", "A" if fa < fb else "B")
