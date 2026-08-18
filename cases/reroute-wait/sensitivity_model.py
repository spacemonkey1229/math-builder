"""Sensitivity model for Reroute Or Wait (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

PRIMARY METRIC: total added rider-minutes per weekday, summed across every Line 20 rider.
LOWER IS BETTER. The framework's evaluate() contract is "higher wins", so evaluate() applies the
same ceiling transform Plaza Pavers uses (value = 2*worse_cost - cost), which is positive for both
options and collapses the framework's generic (max-min)/min margin formula back to exactly the
(worse - better)/worse definition this case records in case.json.

EVERY PARAM below is tagged with its provenance:

  SOURCED   - a figure printed in a real, fetched, cited document (Appendix F id in the comment).
  DERIVED   - computed here from SOURCED figures only; the derivation is written out in case.md
              Appendix E so a student reproduces it by hand.
  PLAN      - a parameter of one of the two service plans being compared. It is a given of the
              scenario, in the same way "the plaza is 200 x 150 ft" is a given in Plaza Pavers.
  ASSUMED   - a stated Modeling Assumption (case.md Appendix G, id in the comment).

FLEX lists EVERY ASSUMED scalar whose value is genuinely uncertain. Exactly one ASSUMED entry is
excluded, and the exclusion is recorded here rather than left implicit, because an undocumented
FLEX exclusion is indistinguishable from gaming the probe:

  * option_a_headway_min (MA1) is a PLAN parameter, not an uncertain quantity. Halving it to 10
    minutes would mean the detoured line runs MORE often than it does today, which is not a
    sensitivity test of Option A but a different, better, unavailable option. The real uncertainty
    it carries - "could TriMet just buy more buses?" - is a discussion move, and FACILITATOR.md
    Anchor 4 hands it to the room directly rather than burying it in a sweep.

CORRECTED 2026-08-12 (case-readiness Tier 2 probe 5). rq_to_e12_bus_min (MA4) was previously
excluded from FLEX on the grounds that it is "stated geometry." That exclusion was wrong and is
reversed. MA4 is a stated Modeling Assumption, it is genuinely uncertain, and the sweep shows it
is the single dial that can flip this case: at -50% (8 min -> 4 min) Option B wins by 5.14%, and
at +50% (12 min) Option A's margin reaches 23.55%, past the SPEC section 2 20% cap. Excluding the
one assumption that flips the verdict is precisely the failure this docstring claims to guard
against. The instability is now declared in case.json.balance.instability, in case.md Appendix G
MA4, and in FACILITATOR.md, per case-readiness probe 5 ("not forbidden - but it must say so").
"""

PARAMS = {
    # --- SOURCED (case.md Appendix B / Appendix D) ---
    "line20_weekday_boardings": 9530.0,      # S1 -- Route Ridership Report, Weekdays, Spring 2024
    "line20_passenger_miles": 32726.0,       # S1 -- same report
    "line20_rides_per_revenue_hour": 35.2,   # S1 -- same report
    "line20_pass_miles_per_revenue_mile": 9.0,   # S1 -- same report
    "line20_avg_trip_len_mi": 3.4,           # S1 -- same report
    "line20_oneway_run_min": 120.0,          # S2 -- 12:35pm Beaverton TC to 2:35pm Gresham Central TC
    "line20_headway_min": 15.0,              # S2 -- 12:35 / 12:50 / 1:05 departures
    "burnside_segment_min": 6.0,             # S2 -- W Burnside & SW 5th 1:18pm to E Burnside & SE 12th 1:24pm
    "max_rq_to_psn_min": 9.0,                # S3 -- MAX Blue, Rose Quarter TC 12:05pm to Pioneer Sq N 12:14pm
                                             #        (S4 MAX Red publishes the same 9 min: 12:28pm to 12:37pm)
    "max_line_headway_min": 15.0,            # S3, S4 -- Blue and Red both on 15-minute midday departures
    "max_lines_at_transfer": 2.0,            # S3, S4 -- Blue and Red both serve RQ and PSN
    "walk_speed_fps": 3.5,                   # S8 -- MUTCD 4I.06(7) pedestrian design walking speed
    "twist_shuttle_headway_min": 3.5,        # S9 -- midpoint of "about every two to five minutes"

    # --- PLAN (a parameter of one of the two options being compared) ---
    "option_a_headway_min": 20.0,            # MA1 -- Option A's definition: detour, fixed fleet, next clock-face step

    # --- ASSUMED (case.md Appendix G, Modeling Assumptions) ---
    "option_a_detour_extra_min": 2.5,        # MA2 -- extra in-vehicle time for a crossing rider under Option A
    "walk_psn_to_w5_ft": 600.0,              # MA3 -- three downtown Portland blocks
    "rq_to_e12_bus_min": 8.0,                # MA4 -- Option B east-half extension, ~1 mi at Line 20's own pace
    "closure_weekdays": 1300.0,              # MA5 -- five years x 260 weekdays; scales both options identically
    "twist_shuttle_ride_min": 13.0,          # twist only -- bus in mixed traffic over the rail segment
    "twist_option_a_extra_detour_min": 4.0,  # twist only -- second detour when the near bridge's roadway also shuts
}

FLEX = ["option_a_detour_extra_min", "walk_psn_to_w5_ft", "rq_to_e12_bus_min"]


# ----------------------------------------------------------------- derivations ----
def route_length_mi(p):
    """DERIVED, exactly as case.md Appendix E instructs a student to do it by hand."""
    revenue_hours = p["line20_weekday_boardings"] / p["line20_rides_per_revenue_hour"]
    revenue_miles = p["line20_passenger_miles"] / p["line20_pass_miles_per_revenue_mile"]
    avg_speed_mph = revenue_miles / revenue_hours
    return avg_speed_mph * (p["line20_oneway_run_min"] / 60.0)


def crossing_riders(p):
    """DERIVED. Appendix G MA6's stated method, applied to SOURCED inputs only."""
    share = p["line20_avg_trip_len_mi"] / route_length_mi(p)
    return p["line20_weekday_boardings"] * share, share


def walk_min(feet, p):
    return feet / (p["walk_speed_fps"] * 60.0)


def transfer_penalty_min(p):
    """Option B: minutes a river-crossing rider pays, net of the direct segment they no longer ride."""
    max_wait = (p["max_line_headway_min"] / p["max_lines_at_transfer"]) / 2.0
    return (p["rq_to_e12_bus_min"]                       # ride the extended east half to RQ
            + max_wait                                   # wait for a train
            + p["max_rq_to_psn_min"]                     # ride across
            + walk_min(p["walk_psn_to_w5_ft"], p)        # walk to the west half
            + p["line20_headway_min"] / 2.0              # wait for the west half
            - p["burnside_segment_min"])                 # minus the direct segment, no longer ridden


# ------------------------------------------------------------------- the ledger ----
def ledger(p, detour_extra=None, transfer_extra=0.0):
    n_cross, share = crossing_riders(p)
    added_wait_a = (p["option_a_headway_min"] - p["line20_headway_min"]) / 2.0
    detour = p["option_a_detour_extra_min"] if detour_extra is None else detour_extra

    a_wait_min = p["line20_weekday_boardings"] * added_wait_a       # EVERY rider pays this
    a_ride_min = n_cross * detour                                   # only crossing riders pay this
    b_min = n_cross * (transfer_penalty_min(p) + transfer_extra)    # only crossing riders pay anything

    return {"A_cost": a_wait_min + a_ride_min, "B_cost": b_min,
            "A_wait_min": a_wait_min, "A_ride_min": a_ride_min,
            "crossing_riders": n_cross, "crossing_share": share,
            "route_length_mi": route_length_mi(p),
            "transfer_penalty_min": transfer_penalty_min(p),
            "added_wait_per_rider_a_min": added_wait_a}


def _contract(costs):
    a, b = costs["A_cost"], costs["B_cost"]
    ceiling = 2 * max(a, b)
    return {"A": ceiling - a, "B": ceiling - b}


def evaluate(p):
    """CONTRACT: {"A": metric, "B": metric}, higher wins."""
    return _contract(ledger(p))


def twist_ledger(p):
    """TWIST (FACILITATOR.md): the roadway Option A's detour depends on is itself shut for a
    stretch, so Option A's buses must take a second, longer detour. Option B is untouched --
    its river crossing is the rail segment, which is on a different deck and a different plan.
    The twist therefore attacks the winner, not the loser, which is the whole point."""
    return ledger(p, detour_extra=p["option_a_detour_extra_min"] + p["twist_option_a_extra_detour_min"])


def evaluate_twist(p):
    return _contract(twist_ledger(p))


def _report(label, c):
    a, b = c["A_cost"], c["B_cost"]
    better = "A" if a < b else "B"
    worse = max(a, b)
    margin = (worse - min(a, b)) / worse * 100
    print(f"{label}: A {a:,.1f} rider-min/weekday | B {b:,.1f} rider-min/weekday "
          f"(better: {better}, margin {margin:.2f}%)")
    return margin


if __name__ == "__main__":
    p = PARAMS
    c = ledger(p)
    print(f"route length (derived)      : {c['route_length_mi']:.3f} mi")
    print(f"crossing share (derived)    : {c['crossing_share']*100:.3f}%")
    print(f"crossing riders / weekday   : {c['crossing_riders']:,.1f}")
    print(f"Option A added wait / rider : {c['added_wait_per_rider_a_min']:.2f} min")
    print(f"Option B transfer penalty   : {c['transfer_penalty_min']:.3f} min per crossing rider")
    print(f"A = wait {c['A_wait_min']:,.1f} + in-vehicle {c['A_ride_min']:,.1f}")
    base_margin = _report("BASE ", c)
    print(f"  A = {c['A_cost']/60:,.1f} rider-hours/weekday, {c['A_cost']*p['closure_weekdays']/60:,.0f} over the closure")
    print(f"  B = {c['B_cost']/60:,.1f} rider-hours/weekday, {c['B_cost']*p['closure_weekdays']/60:,.0f} over the closure")

    t = twist_ledger(p)
    _report("TWIST", t)

    ev = evaluate(p)
    better = max(ev, key=ev.get); worse = min(ev, key=ev.get)
    ev_margin = (ev[better] - ev[worse]) / ev[worse] * 100
    assert abs(ev_margin - base_margin) < 0.05, f"contract transform drifted: {ev_margin} vs {base_margin}"
    print(f"\nevaluate() contract check OK: winner={better}, margin={ev_margin:.2f}% (matches the raw ledger)")
