#!/usr/bin/env python3
"""
Sensitivity model -- The Tilt Decision.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain), and cases/bioreactor-bid/sensitivity_model.py
for a second worked example.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The metric is the case's actual primary_metric (case.json): weighted effective
kWh generated per panel per year, each month's PVWatts-modeled output (Appendix
B) weighted by SMUD's time-of-use rate multiplier for that month (Appendix C) --
the summer on-peak multiplier for June-September, 1.0 for every other month.

PARAMS carries every stated dial in the case, per the case-readiness brief --
including the site/panel/racking/tilt specification (Appendix A) and the rate
schedule (Appendix C) -- even though most of those do not feed evaluate()
directly. Appendix B's twelve monthly kWh figures per option ARE the dial that
actually drives the metric, and they are cited PVWatts model output [S5], not a
stated Modeling Assumption -- so they, the tilt angles, and the panel spec stay
out of FLEX. Appendix C's summer on-peak rate ($0.3765) and the "which
non-summer rate is 'the' non-summer rate" choice ARE flexed: the case's own S6
source note and sensitivity_note treat that choice (off-peak $0.1285 vs.
on-peak $0.1776) as an explicit, acknowledged modeling convention, not a single
unambiguous fact -- SMUD publishes both, and the case picked one deliberately.
MA1 (panel count) is included in FLEX only to make its own case.md claim
machine-checkable: the metric is stated per panel, so panel count cancels out
of the A-vs-B comparison and should never move the result.

Verified against case.md Appendix B/C and case.json.derived (2026-08-31):
    base (off-peak non-summer rate, $0.1285)   A = 1163.1  B = 1187.5   margin (B over A) = 2.10%
    alt  (on-peak non-summer rate, $0.1776)    A =  951.7  B =  964.5   margin (B over A) = 1.35%
    case.json.derived records these as 1162.8/1187.5 (2.13%) and .../1.37% -- the ~0.3 kWh, ~0.03pp
    gap between this model's totals and case.json's is expected display-rounding propagation:
    Appendix B publishes each month to 1 decimal place, and 659.4 (sum of those twelve rounded
    Option A figures) already differs from case.md's own published annual total (659.3) for the
    identical reason. Same phenomenon, same direction, same tiny size -- not a data-entry error.
    Summer Shift (B) wins under both readings; only the margin size changes, matching
    RESEARCH_LOG.md's own documented finding.
"""

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SUMMER_MONTHS = {"Jun", "Jul", "Aug", "Sep"}   # Appendix C

# --- Fixed: cited PVWatts model output, Appendix B / source S5 -------------
MONTHLY_KWH_A = [35.5, 45.5, 58.0, 60.4, 61.3, 63.2, 66.5, 66.9, 64.4, 60.0, 41.7, 36.0]
MONTHLY_KWH_B = [31.4, 41.4, 56.2, 62.0, 66.2, 69.9, 72.6, 69.7, 63.1, 55.4, 36.9, 31.4]

PARAMS = {
    # --- Appendix A: site, panel, racking spec -- cited, not modeling assumptions
    "site_latitude_deg": 38.5816,          # [S1]
    "panel_rated_power_w": 400.0,          # [S2]
    "racking_min_tilt_deg": 10.0,          # [S3]
    "racking_max_tilt_deg": 60.0,          # [S3]
    "tilt_a_deg": 39.0,                    # Option A, latitude rounded [S1, derived]
    "tilt_b_deg": 24.0,                    # Option B, latitude - 15 rule [S4, derived]
    # --- MA1: panel count. Stated per case.md Appendix A / Modeling Assumptions.
    #     The metric is per-panel and identical for both options, so this cannot
    #     move the comparison -- flexing it is a machine check of that claim.
    "panel_count": 20.0,
    # --- Appendix C: SMUD rate schedule -- summer rate is cited; the choice of
    #     WHICH non-summer rate to use as "the" denominator is the modeling
    #     convention this case documents and defends (S6 note, sensitivity_note).
    "summer_onpeak_rate_usd_per_kwh": 0.3765,   # [S6]
    "nonsummer_rate_used_usd_per_kwh": 0.1285,  # [S6] -- off-peak reading, the case's choice
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption / documented modeling convention, not cited PVWatts/NOAA data.
# Appendix B's monthly kWh figures, the tilt angles, and the rate schedule's
# summer rate are cited data -- P6 (data decay) stress-tests those, not P5.
# --flex-all overrides and sweeps every PARAMS entry.
FLEX = [
    "panel_count",                       # MA1 -- documented as a zero-sensitivity no-op
    "nonsummer_rate_used_usd_per_kwh",   # the off-peak-vs-on-peak modeling choice (S6)
]


def _weighted_annual_kwh(monthly_kwh, multiplier):
    total = 0.0
    for month, kwh in zip(MONTHS, monthly_kwh):
        total += kwh * (multiplier if month in SUMMER_MONTHS else 1.0)
    return total


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    multiplier = p["summer_onpeak_rate_usd_per_kwh"] / p["nonsummer_rate_used_usd_per_kwh"]

    # Primary metric is stated PER PANEL (case.json.primary_metric) -- panel_count
    # is applied identically to both options and cancels in the comparison, per
    # MA1's own documented sensitivity claim ("None ... cancels out entirely").
    a_per_panel = _weighted_annual_kwh(MONTHLY_KWH_A, multiplier)
    b_per_panel = _weighted_annual_kwh(MONTHLY_KWH_B, multiplier)

    return {"A": a_per_panel, "B": b_per_panel}


def raw_totals(params=None):
    """Not part of the Tier 2 contract -- the un-weighted raw annual kWh per
    panel (Latitude Lock's actual argument), used to reproduce case.json's
    raw_margin_pct_a_over_b (0.47%) for verification."""
    return {"A": sum(MONTHLY_KWH_A), "B": sum(MONTHLY_KWH_B)}


if __name__ == '__main__':
    base = evaluate({})
    print("base (off-peak non-summer rate)", {k: round(v, 1) for k, v in base.items()},
          "margin(B over A) %.2f%%" % (100 * (base["B"] - base["A"]) / base["A"]))

    alt = evaluate({"nonsummer_rate_used_usd_per_kwh": 0.1776})
    print("alt  (on-peak non-summer rate) ", {k: round(v, 1) for k, v in alt.items()},
          "margin(B over A) %.2f%%" % (100 * (alt["B"] - alt["A"]) / alt["A"]))

    raw = raw_totals()
    print("raw annual kWh/panel (unweighted)", {k: round(v, 1) for k, v in raw.items()},
          "Latitude Lock margin(A over B) %.2f%%" % (100 * (raw["A"] - raw["B"]) / raw["B"]))
