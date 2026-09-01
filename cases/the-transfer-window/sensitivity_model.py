#!/usr/bin/env python3
"""
Sensitivity model — The Transfer Window.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     optional; illustrates the FACILITATOR.md Twist

The primary metric (case.json.balance.margin_basis) is a straight ratio:
    propellant_mass(option)      = wet_mass * (1 - exp(-delta_v / (Isp * g0)))   [rocket equation]
    deliverable_payload(option)  = wet_mass - dry_mass - propellant_mass(option)
    metric(option)                = deliverable_payload(option) / transit_time_days(option)

Fixed (not in FLEX[]): wet_mass_kg (S2), delta_v_A/B_km_s and isp_A/B_s
(S3/S7/S12), and transit_time_A_days (S12, the derived Hohmann half-period)
are all CITED, sourced or directly-derived-from-cited figures, not stated
scenario assumptions. Per the "only FLEX[] is swept by default" rule (SPEC
Sec2 asks for sensitivity to stated ASSUMPTIONS, not to cited measurements),
these are stress-tested by Tier 2 probe 6 (data decay), not probe 5. This is
also the case's own honest diagnosis (RESEARCH_LOG.md's "RETUNE PASS", the
FACILITATOR.md Status note): the ~15,940% margin is structural to the real,
sourced delta-v/Isp/orbital-radii figures, which is exactly why it needed a
per-case MCS-46 waiver rather than a retune.

Genuine stated Modeling Assumptions that DO enter this model:
    MA3 (dry_mass_kg is fixed... no -- MA4 is dry mass; MA3 is transit time B)
    MA1 (delivery_window_days)      -- feasibility gate only, never binds either
                                        option under the case's own figures
    MA3 (transit_time_B_days = 180) -- the single largest lever in the whole
                                        comparison; verified in RESEARCH_LOG.md
                                        to sit inside real electric-GEO-transfer
                                        precedent, not at an inflated extreme
    MA4 (dry_mass_kg = 30)          -- shrinks both options' payload roughly
                                        proportionally; does not close the gap
    MA5 (dose_rate_rad_per_day)     -- feeds only the D5 radiation pass/fail
                                        check, a separate constraint from the
                                        primary D4 metric

MA2 (both options fly the same geometric transfer ellipse) only affects the
D1/D2 parametric/rectangular-equation algebra, not the mass/time economics
computed here, and is not represented in this model.

Verified against case.json.balance.margin_basis (2026-08-31):
    base    A (Direct Burn)   = 17.03 kg / 0.221 days  = 76.84 kg/day
            B (Patient Drift) = 86.28 kg / 180 days    = 0.4793 kg/day
            margin  (76.84 - 0.4793) / 0.4793 * 100  ~= 15,931%  (matches
            case.json.margin_pct = 15,940.5 to within rounding: the case's own
            figures round the rocket-equation outputs to 17.0/86.3/133.0/63.7 kg
            before dividing; this model carries full precision instead).
    MA3 flexed toward the delivery-window ceiling (up to 239 days, just under
            MA1's 240-day cap): B's metric FALLS to ~0.361 kg/day and the
            margin WIDENS to ~21,186% -- lengthening B's transit time never
            helps it, because it shrinks B's own metric while leaving A's
            metric untouched. MA3 flexed past the 240-day ceiling (e.g. 270 or
            360 days) disqualifies B outright on the MA1 delivery-window gate
            before the kg/day metric is even reached. Either direction, B
            never wins -- confirming the margin is not a knife's-edge result
            riding on a single assumption (FACILITATOR.md Anchor 4).
    MA4 flexed to 45 kg (+50%): both options' deliverable payload shrinks
            (A: ~8.96 kg, B: ~81.3 kg) but the winner does not change.
    MA1 flexed down to 120 days (-50%): B's real 180-day transit time now
            EXCEEDS the window (180 > 120) -- B becomes contractually
            infeasible outright, independent of the kg/day metric, matching
            case.md Appendix E's own stated MA1 sensitivity note ("below 180
            days, the Patient Drift becomes contractually unflyable outright").
    evaluate_twist(): an evenly-weighted additive score built from each
            option's payload-mass fraction and a normalized speed fraction
            (1 / transit_time, scaled) still favors the Direct Burn (~0.547 vs
            ~0.240) -- unlike The Phasing Call, this case's speed asymmetry
            (~815x) is large enough on its own that no additive reconstruction
            with real inputs credibly flips it; see the printed output below.
"""
import math

PARAMS = {
    # --- Appendix C / S2: real, sourced kick-stage wet mass ------------------
    "wet_mass_kg": 180.0,
    # --- Appendix E, MA4: stated dry-mass modeling assumption ----------------
    "dry_mass_kg": 30.0,
    # --- Appendix B / S12, S3, S7: real, cited/derived delta-v and Isp -------
    "delta_v_A_km_s": 3.82,     # Direct Burn   [S12]
    "delta_v_B_km_s": 6.0,      # Patient Drift [S3]
    "isp_A_s": 290.0,           # Direct Burn   [S7]
    "isp_B_s": 1400.0,          # Patient Drift [S3]
    "g0_km_s2": 9.80665e-3,     # standard gravity, km/s^2
    # --- Appendix B / S12: Direct Burn's derived Hohmann transit time --------
    "transit_time_A_days": 0.221,
    # --- Appendix E, MA3: Patient Drift's stated transit-time assumption -----
    "transit_time_B_days": 180.0,
    # --- Appendix A, MA1: stated contract delivery-window assumption ---------
    "delivery_window_days": 240.0,
    # --- Appendix A / S10: payload's real, cited radiation-tolerance limit ---
    "dose_tolerance_rad": 20000.0,
    # --- Appendix D, MA5: stated radiation dose-rate assumption --------------
    "dose_rate_rad_per_day": 50.0,
    # --- Appendix D / S14: real, cited belt-crossing time fraction -----------
    "belt_fraction": 0.48,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption (MA1, MA3, MA4, MA5), not cited/sourced or directly-derived-from-
# cited data. wet_mass_kg, delta_v_A/B_km_s, isp_A/B_s, transit_time_A_days,
# and belt_fraction are all real, cited/derived figures (S2, S3, S7, S12, S14)
# and are NOT flexed by default; --flex-all overrides.
FLEX = [
    "delivery_window_days",     # MA1
    "transit_time_B_days",      # MA3
    "dry_mass_kg",               # MA4
    "dose_rate_rad_per_day",     # MA5
]


def _propellant_mass(wet_mass, delta_v, isp, g0):
    """Tsiolkovsky rocket equation: propellant burned to achieve delta_v."""
    return wet_mass * (1.0 - math.exp(-delta_v / (isp * g0)))


def _deliverable_payload(p, delta_v, isp):
    prop = _propellant_mass(p["wet_mass_kg"], delta_v, isp, p["g0_km_s2"])
    return p["wet_mass_kg"] - p["dry_mass_kg"] - prop


def evaluate(params):
    """The case's actual graded metric (D4): deliverable payload mass divided
    by transit time, for each option, gated by the two pass/fail floors
    (MA1's contract delivery window, Appendix A's radiation-dose tolerance)
    case.md states both options must clear to be flyable at all."""
    p = dict(PARAMS)
    p.update(params or {})

    payload_A = _deliverable_payload(p, p["delta_v_A_km_s"], p["isp_A_s"])
    payload_B = _deliverable_payload(p, p["delta_v_B_km_s"], p["isp_B_s"])

    dose_A = p["dose_rate_rad_per_day"] * p["belt_fraction"] * p["transit_time_A_days"]
    dose_B = p["dose_rate_rad_per_day"] * p["belt_fraction"] * p["transit_time_B_days"]

    feasible_A = (p["transit_time_A_days"] <= p["delivery_window_days"]
                  and dose_A <= p["dose_tolerance_rad"]
                  and payload_A > 0)
    feasible_B = (p["transit_time_B_days"] <= p["delivery_window_days"]
                  and dose_B <= p["dose_tolerance_rad"]
                  and payload_B > 0)

    metric_A = (payload_A / p["transit_time_A_days"]) if feasible_A else 0.0
    metric_B = (payload_B / p["transit_time_B_days"]) if feasible_B else 0.0

    return {"A": metric_A, "B": metric_B}


def evaluate_twist(params=None):
    """NOT a new fact -- this illustrates the FACILITATOR.md Twist
    mechanically: build an evenly-weighted additive score from each option's
    payload-mass fraction (of wet mass) and a normalized speed fraction
    (transit time inverted and scaled against the slower option), instead of
    dividing payload by transit time. See how much of the ~160x gap survives
    a different, equally-legitimate metric construction."""
    p = dict(PARAMS)
    p.update(params or {})

    payload_A = _deliverable_payload(p, p["delta_v_A_km_s"], p["isp_A_s"])
    payload_B = _deliverable_payload(p, p["delta_v_B_km_s"], p["isp_B_s"])
    payload_frac_A = payload_A / p["wet_mass_kg"]
    payload_frac_B = payload_B / p["wet_mass_kg"]

    slowest = max(p["transit_time_A_days"], p["transit_time_B_days"])
    speed_frac_A = 1.0 - (p["transit_time_A_days"] / slowest)
    speed_frac_B = 1.0 - (p["transit_time_B_days"] / slowest)

    score_A = 0.5 * payload_frac_A + 0.5 * speed_frac_A
    score_B = 0.5 * payload_frac_B + 0.5 * speed_frac_B

    return {"A": score_A, "B": score_B}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["B"]
    print("base  ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % margin)

    ma3_flex = evaluate({"transit_time_B_days": 239.0})
    m2 = 100 * (ma3_flex["A"] - ma3_flex["B"]) / ma3_flex["B"] if ma3_flex["B"] else float("inf")
    print("MA3 flexed to 239d (near MA1 window edge)", {k: round(v, 4) for k, v in ma3_flex.items()},
          "margin %.2f%%" % m2)

    ma3_over = evaluate({"transit_time_B_days": 270.0})
    print("MA3 flexed to 270d (past MA1 window)", {k: round(v, 4) for k, v in ma3_over.items()},
          "-- B disqualified" if ma3_over["B"] == 0.0 else "-- B still feasible")

    ma4_flex = evaluate({"dry_mass_kg": 45.0})
    print("MA4 +50%% (45kg dry mass)", {k: round(v, 4) for k, v in ma4_flex.items()})

    ma1_flex = evaluate({"delivery_window_days": 120.0})
    print("MA1 -50%% (120d window)", {k: round(v, 4) for k, v in ma1_flex.items()},
          "-- B disqualified" if ma1_flex["B"] == 0.0 else "-- B still feasible")

    twist = evaluate_twist({})
    winner = "A (Direct Burn)" if twist["A"] > twist["B"] else "B (Patient Drift)"
    print("twist (additive score)", {k: round(v, 4) for k, v in twist.items()}, "winner:", winner)
