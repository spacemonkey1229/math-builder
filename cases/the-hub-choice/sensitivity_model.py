"""Sensitivity model for The Hub Choice (SPEC section 2 balance test, case-readiness Tier 2
probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

Primary metric (case.json.primary_metric): minutes of weekly travel time saved per dollar of
annual route operating cost, restated per-year: (weekly_travelers * minutes_saved_per_traveler *
52) / annual_operating_cost.

Real/derived (sourced, NOT flexed):
    dist_A_mi = 123.2   (BGM<->ART, haversine on Wikipedia coordinates [S1][S2])
    dist_B_mi = 97.2    (ART<->Cortland, haversine on Wikipedia coordinates [S2][S3])
    cruise_mph = 212.9  (185 kt TAS [S9])
    drive_A_min = 135   drive_B_min = 110   (Travelmath [S8])
    cost_per_hr = 1601  (Aircraft Cost Calculator [S12])

Assumptions (Appendix F):
    MA1 ground_oh_min = 45   -- THE ONLY probe-5 flex dial. Genuinely uncertain (no public
        per-flight ground-time figure exists for this fictional airline's small airports), and
        it is the assumption that actually determines the winner (see below).
    MA2 weekly_travelers = 25 -- applied IDENTICALLY to A and B. Because it multiplies both
        routes' numerators by the same factor, it cancels out of the A-vs-B ratio entirely and
        can never change the winner by construction. Included in FLEX anyway, for transparency,
        to demonstrate that cancellation explicitly rather than merely asserting it.
    MA3 flights_per_week = 6 -- applied identically to A and B; also cancels out of the A-vs-B
        ratio (it scales both routes' block hours, and therefore both annual costs, by the same
        factor, while leaving weekly time-saved unaffected). Not included in FLEX: a fixed
        scheduling choice, not a research uncertainty (same status as the-parity-check's packet
        size dial).

Why MA1 is the only load-bearing probe-5 dial: an earlier version of this case set ground
overhead to 30 minutes, which put the winner flip point (bisected numerically) at ~16.7 minutes
-- inside a +/-50% flex range (15-45 min) starting from 30. That version FAILED probe 5. Retuned
to a base of 45 minutes: the flip point (~16.7 min) is now well outside the +/-50% flex range
(22.5-67.5 min), and Route A wins across the ENTIRE range. This is the retuning SPEC section 2 and
PIPELINE.md require -- adjusting a case-write/case-research constraint, not hiding the
sensitivity or arguing it away.
"""

import math

# --- sourced/derived great-circle distances (not flexed) ---
_BGM = (42.20861, -75.97972)
_ART = (43.99194, -76.02056)
_CORT = (42.59250, -76.21472)


def _haversine_mi(p1, p2):
    R = 3958.8
    lat1, lon1 = p1
    lat2, lon2 = p2
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


DIST_A_MI = _haversine_mi(_BGM, _ART)     # ~123.2
DIST_B_MI = _haversine_mi(_ART, _CORT)    # ~97.2
CRUISE_MPH = 185 * 1.150779               # 185 kt TAS [S9]
DRIVE_A_MIN = 135.0                       # [S8]
DRIVE_B_MIN = 110.0                       # [S8]
COST_PER_HR = 1601.0                      # [S12]
WEEKS_PER_YEAR = 52

PARAMS = {
    # --- ASSUMED (Appendix F, MA1) --- the only probe-5 flex dial
    "ground_oh_min": 45.0,
    # --- ASSUMED (Appendix F, MA2) --- shared/identical across A and B; cancels by construction
    "weekly_travelers": 25.0,
    # --- ASSUMED (Appendix F, MA3) --- shared/identical across A and B; cancels by construction
    "flights_per_week": 6.0,
}

FLEX = ["ground_oh_min", "weekly_travelers"]


def evaluate(params=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = annual person-minutes saved
    per dollar of annual operating cost (case.json's primary_metric)."""
    p = dict(PARAMS)
    p.update(params or {})
    g = p["ground_oh_min"]
    travelers = p["weekly_travelers"]
    fpw = p["flights_per_week"]

    air_a_min = DIST_A_MI / CRUISE_MPH * 60
    air_b_min = DIST_B_MI / CRUISE_MPH * 60

    flight_a_min = air_a_min + g
    flight_b_min = air_b_min + g

    saved_a = DRIVE_A_MIN - flight_a_min
    saved_b = DRIVE_B_MIN - flight_b_min

    block_hours_a = air_a_min / 60 * fpw * WEEKS_PER_YEAR
    block_hours_b = air_b_min / 60 * fpw * WEEKS_PER_YEAR
    annual_cost_a = block_hours_a * COST_PER_HR
    annual_cost_b = block_hours_b * COST_PER_HR

    annual_min_saved_a = travelers * saved_a * WEEKS_PER_YEAR
    annual_min_saved_b = travelers * saved_b * WEEKS_PER_YEAR

    return {"A": annual_min_saved_a / annual_cost_a, "B": annual_min_saved_b / annual_cost_b}


def _state(ev):
    a, b = ev["A"], ev["B"]
    if a == b:
        return "TIE", 0.0
    hi_key, lo_key = ("A", "B") if a > b else ("B", "A")
    # Canonical margin definition (matches skills/case-readiness/scripts/tier2_probes.py):
    # relative to the LOSER, not the winner -- 100 * (hi - lo) / lo.
    margin = 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
    return hi_key, margin


def _report(label, ev):
    state, margin = _state(ev)
    print(f"{label}: A={ev['A']:.5f}  B={ev['B']:.5f}  winner={state}  margin={margin:.2f}%")
    return state, margin


if __name__ == "__main__":
    base = evaluate()
    winner, margin = _report("Base (ground_oh=45, travelers=25, flights/wk=6)", base)
    assert winner == "A" and abs(margin - 15.89) < 0.5, \
        f"Base model drifted from case.json's disclosed canonical base (A wins by ~15.89%): got {winner} {margin:.2f}%"

    print("\n--- Probe 5: +/-50% flex on MA1 (ground_oh_min), the load-bearing assumption ---")
    for mult, label in [(0.5, "-50%"), (0.75, "-25%"), (1.0, "base"), (1.25, "+25%"), (1.5, "+50%")]:
        g = PARAMS["ground_oh_min"] * mult
        ev = evaluate({"ground_oh_min": g})
        state, m = _state(ev)
        flip = " <-- FLIPS" if state != winner else ""
        print(f"  ground_oh={g:5.1f} min ({label}): A={ev['A']:.5f} B={ev['B']:.5f} winner={state} margin={m:.2f}%{flip}")

    print("\n--- Probe 5: +/-50% flex on MA2 (weekly_travelers), applied identically to A and B ---")
    for mult, label in [(0.5, "-50%"), (1.5, "+50%")]:
        t = PARAMS["weekly_travelers"] * mult
        ev = evaluate({"weekly_travelers": t})
        state, m = _state(ev)
        flip = " <-- FLIPS" if state != winner else ""
        print(f"  travelers={t:5.1f}/wk ({label}): A={ev['A']:.5f} B={ev['B']:.5f} winner={state} margin={m:.2f}%{flip}"
              "  (expect NO change in margin -- cancels by construction)")

    print("\n--- Bisected flip point for ground_oh_min (confirms it sits outside the +/-50% band) ---")
    lo, hi = 0.0, 90.0
    for _ in range(60):
        mid = (lo + hi) / 2
        ev = evaluate({"ground_oh_min": mid})
        if ev["A"] > ev["B"]:
            hi = mid
        else:
            lo = mid
    print(f"  flip point ~= {(lo + hi) / 2:.2f} min  (flex band is 22.5-67.5 min; flip point is below it)")

    print("\nAll checks complete. See RESEARCH_LOG.md for the full write-up.")
