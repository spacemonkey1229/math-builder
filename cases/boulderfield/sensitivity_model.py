"""Sensitivity model for Boulderfield (SPEC §2 balance test, case-readiness Tier 2 probe 5).

CONTRACT: evaluate(params) -> {"A": metric, "B": metric}, higher wins. The metric here is total
estimated ground-team travel time in minutes from the Longs Peak Trailhead to the patient, via
The Keyhole Route (A) vs. The Loft (B). Lower time is better, so evaluate() uses the
ceiling-collapse transform used elsewhere in this corpus (Dice Roll, Full Reach, Apron Order):
value = 2*max(times) - time, which preserves ranking and lets the same "higher wins" contract
cover a lower-is-better metric.
"""

PARAMS = {
    "pace_mph": 3.0,                    # S4 -- Naismith's Rule (1892), horizontal-travel constant
    "climb_rate_ft_per_hr": 2000.0,     # S4 -- Naismith's Rule (1892), ascent constant (2000 ft/hr)

    # Appendix A -- 14ers.com route statistics, one-way (round-trip figures / 2 for distance;
    # elevation gain is already a one-way ascent total)
    "keyhole_oneway_mi": 7.25,          # S1 -- Keyhole Route, 14.5 mi RT / 2
    "keyhole_gain_ft": 5100.0,          # S1 -- Keyhole Route total elevation gain
    "loft_oneway_mi": 6.5,              # S2 -- The Loft, 13.0 mi RT / 2
    "loft_gain_ft": 5300.0,             # S2 -- The Loft total elevation gain

    # Shared lower segment (both routes), used only by evaluate_twist()
    "boulderfield_oneway_mi": 5.5,      # MA-BF -- East Longs Peak Trail to the Boulderfield
    "boulderfield_gain_ft": 3360.0,     # MA-BF -- elevation gain, trailhead to Boulderfield

    "night_pace_multiplier": 1.3,       # MA1 -- night/full-gear rescue-pace slowdown vs. a
                                         # standard Naismith day-hiker estimate
    "technical_penalty_min": 55.0,      # MA2 -- route-finding/exposure penalty, The Loft's
                                         # unmaintained, unmarked upper section
}

FLEX = ["night_pace_multiplier", "technical_penalty_min"]
# NOTE: pace_mph and climb_rate_ft_per_hr are Naismith's Rule's own published constants (S4) --
# not a stated assumption of this case, so they stay out of FLEX (P6 data-decay covers citations,
# not P5). keyhole/loft distance and elevation gain are cited route statistics (S1, S2) -- also
# excluded from FLEX for the same reason. Only MA1 (night_pace_multiplier) and MA2
# (technical_penalty_min) are genuinely author-chosen assumptions in this case's time model.


def _route_time_min(oneway_mi, gain_ft, p, penalty_min=0.0):
    hrs = (oneway_mi / p["pace_mph"] + gain_ft / p["climb_rate_ft_per_hr"]) * p["night_pace_multiplier"]
    return hrs * 60.0 + penalty_min


def time_breakdown(p):
    a_naismith_hr = p["keyhole_oneway_mi"] / p["pace_mph"] + p["keyhole_gain_ft"] / p["climb_rate_ft_per_hr"]
    b_naismith_hr = p["loft_oneway_mi"] / p["pace_mph"] + p["loft_gain_ft"] / p["climb_rate_ft_per_hr"]
    a_total = _route_time_min(p["keyhole_oneway_mi"], p["keyhole_gain_ft"], p)
    b_total = _route_time_min(p["loft_oneway_mi"], p["loft_gain_ft"], p, p["technical_penalty_min"])
    return {
        "a_naismith_hr": a_naismith_hr, "b_naismith_hr": b_naismith_hr,
        "A_min": a_total, "B_min": b_total,
    }


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Ceiling-collapse transform."""
    b = time_breakdown(p)
    a_min, b_min = b["A_min"], b["B_min"]
    ceiling = 2 * max(a_min, b_min)
    return {"A": ceiling - a_min, "B": ceiling - b_min}


def evaluate_twist(p):
    """Twist: the patient has self-descended to the Boulderfield, the point where both routes
    share the same trail. Recompute using only the shared lower segment -- tests whether the
    ~10% time margin survives once the technical-terrain penalty (which only applies above the
    Boulderfield) no longer enters the comparison at all."""
    t = _route_time_min(p["boulderfield_oneway_mi"], p["boulderfield_gain_ft"], p)
    return {"A": t, "B": t}


if __name__ == "__main__":
    b = time_breakdown(PARAMS)
    print(f"Keyhole (A) Naismith base: {b['a_naismith_hr']:.4f} hr  -> total {b['A_min']:.2f} min")
    print(f"The Loft (B) Naismith base: {b['b_naismith_hr']:.4f} hr -> total {b['B_min']:.2f} min "
          f"(+{PARAMS['technical_penalty_min']:.0f} min technical penalty)")
    faster = "A" if b["A_min"] < b["B_min"] else "B"
    other = "B" if faster == "A" else "A"
    times = {"A": b["A_min"], "B": b["B_min"]}
    margin = (times[other] - times[faster]) / times[other] * 100
    print(f"Faster: {faster}   margin: {margin:.2f}%")

    ev = evaluate(PARAMS)
    ev_margin = (max(ev.values()) - min(ev.values())) / min(ev.values()) * 100
    print(f"\nCONTRACT evaluate(): {ev}  (margin check: {ev_margin:.2f}%)")
    assert abs(ev_margin - margin) < 0.01

    tw = evaluate_twist(PARAMS)
    print(f"\nTwist (patient at Boulderfield, shared segment only): {tw}")

    print("\nFLEX sensitivity (+/-50%):")
    for key in FLEX:
        for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
            p2 = dict(PARAMS); p2[key] = PARAMS[key] * mult
            r = time_breakdown(p2)
            ch = "A" if r["A_min"] < r["B_min"] else "B"
            ot = "B" if ch == "A" else "A"
            v = {"A": r["A_min"], "B": r["B_min"]}
            m = (v[ot] - v[ch]) / v[ot] * 100
            print(f"  {key} {label}: A={r['A_min']:.2f} B={r['B_min']:.2f} faster={ch} margin={m:.2f}%")
