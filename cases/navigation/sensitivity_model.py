#!/usr/bin/env python3
"""
SENSITIVITY MODEL — Navigation.

Tier 2 probe 5 ("flex each stated assumption by +/-50%, report which flips the
verdict") needs a runnable model of the case's own arithmetic. This is that
model, for cases/navigation.

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):

    PARAMS                             dict[str, number]  every dial the case states
    FLEX                               list[str]          subset of PARAMS probe 5 flexes
    evaluate(params) -> dict           {"A": metric, "B": metric}
    evaluate_twist(params) -> dict     same shape, with the twist's own lens applied

IMPORTANT — metric direction: this case's primary metric is total drive TIME in
seconds, so LOWER is better here (same convention as cases/family-trip, whose
primary metric is a cost in USD). Callers comparing A vs B for "the winner"
should take the smaller value, not the larger one.

evaluate() returns the case's graded PRIMARY metric: total elapsed drive time,
Hotel to Hospital, on the ordinary (Route 9 highway) path -- Option A drives
every segment at the posted legal limit; Option B drives every segment at
Filberto's chosen speeding increment (case.json PARAMS.speeding_mph_over,
Appendix C / Modeling Assumption MA1: +8 mph on every segment). This matches
case.json.balance (A ~= 436.6s, B ~= 352.2s, margin ~= 19.3%, B faster).

evaluate_twist() returns the same comparison AFTER the Twist: Route 9 is
closed overnight for construction (Appendix E), forcing an all-local detour
via Fifth Ave and Ridge Rd that removes the 45 mph highway segment entirely
and adds two more stop-sign segments. This is the FACILITATOR.md Twist -- it
does not change who is faster (B is still faster), but it grows the time-saved
margin past the SPEC section 2 20% cap, weakening the base-case argument that
"the time savings from speeding are too small to be worth the risk."

Verified against cases/navigation/case.md / case.json:
    evaluate({})        A = 436.6s (7:16.6)  B = 369.5s (6:09.5)  margin (A-B)/B = 18.15%  (B faster, saves 67s / 1.12 min)
    evaluate_twist({})  A = 530.8s (8:50.8)  B = 441.6s (7:21.6)  margin (A-B)/B = 20.20%  (B faster, margin now BREAKS the 20% cap)
"""

PARAMS = {
    # --- Appendix C: Trip Segment Log (Filberto's known route, base case) ---
    "seg_A_dist_mi": 0.6,          # Cannery Row
    "seg_A_stop_delay_s": 11,      # 1 left (+4+2) + 1 right (+4+1)
    "seg_B_dist_mi": 0.8,          # Fairview Ave
    "seg_B_stop_delay_s": 21,      # 1 left (6) + 2 right (5+5) + 1 straight (5)
    "seg_C_dist_mi": 1.5,          # Route 9, divided highway, no stop signs
    "seg_C_stop_delay_s": 0,
    "seg_D_dist_mi": 0.5,          # Harbor St
    "seg_D_stop_delay_s": 11,      # 1 left (6) + 1 right (5)

    # --- Appendix E: Twist detour, replaces seg_C when Route 9 is closed ----
    "twist_detour1_dist_mi": 0.7,  # Fifth Ave
    "twist_detour1_stop_delay_s": 16,  # 1 left (6) + 1 right (5) + 1 straight (5)
    "twist_detour2_dist_mi": 0.6,  # Ridge Rd
    "twist_detour2_stop_delay_s": 11,  # 1 left (6) + 1 right (5)

    # --- Background: Filberto's known rules (fixed scenario facts) ----------
    "legal_speed_local_mph": 25,
    "legal_speed_highway_mph": 45,

    # --- Appendix D, MA1: the case author's illustrative Option B choice ----
    "speeding_mph_over": 6,

    # --- Background: Modus City's stated penalty; Appendix F, MA2 -----------
    "fine_usd": 10000,
    "annual_taxi_income_usd": 42100,
    "license_loss_years": 1,
}

# Probe 5 flexes THESE and only these -- the case's own genuinely CHOSEN
# assumptions, not the fixed fictional scenario facts (segment distances,
# stop-sign delays, posted speed limits -- all "given" Modus City canon, the
# fictional analogue of cited data) and not the one real sourced figure
# (annual_taxi_income_usd, Appendix F S1 -- stress-tested by P6, not P5).
# speeding_mph_over is the case author's illustrative choice for how much
# faster Option B drives (the case itself leaves this to the student to
# choose; FACILITATOR.md's worked example fixes it at +8 mph). license_loss_
# years is the case author's conservative-floor choice for how many years of
# income a "permanent" license revocation actually costs (the case never
# states a number of years -- see Modeling Assumption MA2).
FLEX = [
    "speeding_mph_over",       # Appendix D, MA1
    "license_loss_years",      # Appendix F, MA2
]


def _leg_time_s(dist_mi, speed_mph, stop_delay_s):
    return (dist_mi / speed_mph) * 3600.0 + stop_delay_s


def _speed(base_mph, over_mph):
    return base_mph + over_mph


def evaluate(params=None):
    """Primary graded metric: total drive time (s), Hotel to Hospital, via Route 9."""
    p = dict(PARAMS)
    p.update(params or {})
    local_A = p["legal_speed_local_mph"]
    hwy_A = p["legal_speed_highway_mph"]
    local_B = _speed(p["legal_speed_local_mph"], p["speeding_mph_over"])
    hwy_B = _speed(p["legal_speed_highway_mph"], p["speeding_mph_over"])

    time_A = (
        _leg_time_s(p["seg_A_dist_mi"], local_A, p["seg_A_stop_delay_s"])
        + _leg_time_s(p["seg_B_dist_mi"], local_A, p["seg_B_stop_delay_s"])
        + _leg_time_s(p["seg_C_dist_mi"], hwy_A, p["seg_C_stop_delay_s"])
        + _leg_time_s(p["seg_D_dist_mi"], local_A, p["seg_D_stop_delay_s"])
    )
    time_B = (
        _leg_time_s(p["seg_A_dist_mi"], local_B, p["seg_A_stop_delay_s"])
        + _leg_time_s(p["seg_B_dist_mi"], local_B, p["seg_B_stop_delay_s"])
        + _leg_time_s(p["seg_C_dist_mi"], hwy_B, p["seg_C_stop_delay_s"])
        + _leg_time_s(p["seg_D_dist_mi"], local_B, p["seg_D_stop_delay_s"])
    )
    return {"A": time_A, "B": time_B}


def evaluate_twist(params=None):
    """Post-Twist metric: Route 9 closed, all-local detour via Fifth Ave/Ridge Rd."""
    p = dict(PARAMS)
    p.update(params or {})
    local_A = p["legal_speed_local_mph"]
    local_B = _speed(p["legal_speed_local_mph"], p["speeding_mph_over"])

    time_A = (
        _leg_time_s(p["seg_A_dist_mi"], local_A, p["seg_A_stop_delay_s"])
        + _leg_time_s(p["seg_B_dist_mi"], local_A, p["seg_B_stop_delay_s"])
        + _leg_time_s(p["twist_detour1_dist_mi"], local_A, p["twist_detour1_stop_delay_s"])
        + _leg_time_s(p["twist_detour2_dist_mi"], local_A, p["twist_detour2_stop_delay_s"])
        + _leg_time_s(p["seg_D_dist_mi"], local_A, p["seg_D_stop_delay_s"])
    )
    time_B = (
        _leg_time_s(p["seg_A_dist_mi"], local_B, p["seg_A_stop_delay_s"])
        + _leg_time_s(p["seg_B_dist_mi"], local_B, p["seg_B_stop_delay_s"])
        + _leg_time_s(p["twist_detour1_dist_mi"], local_B, p["twist_detour1_stop_delay_s"])
        + _leg_time_s(p["twist_detour2_dist_mi"], local_B, p["twist_detour2_stop_delay_s"])
        + _leg_time_s(p["seg_D_dist_mi"], local_B, p["seg_D_stop_delay_s"])
    )
    return {"A": time_A, "B": time_B}


def risk_per_minute_saved(params=None):
    """Supplemental (not the graded metric): D4's dollars-risked-per-minute-saved."""
    p = dict(PARAMS)
    p.update(params or {})
    base = evaluate(p)
    seconds_saved = base["A"] - base["B"]
    minutes_saved = seconds_saved / 60.0
    total_risk_usd = p["fine_usd"] + p["annual_taxi_income_usd"] * p["license_loss_years"]
    return {
        "seconds_saved": seconds_saved,
        "minutes_saved": minutes_saved,
        "total_risk_usd": total_risk_usd,
        "risk_usd_per_minute_saved": total_risk_usd / minutes_saved if minutes_saved else None,
    }


if __name__ == "__main__":
    base = evaluate({})
    tw = evaluate_twist({})
    base_margin = 100 * (base["A"] - base["B"]) / base["B"]
    tw_margin = 100 * (tw["A"] - tw["B"]) / tw["B"]

    def fmt(s):
        m, sec = divmod(round(s, 1), 60)
        return f"{s:.1f}s ({int(m)}:{sec:04.1f})"

    print("base   (Route 9 open)   A=%s  B=%s  (A-B)/B=%.1f%%  -> %s faster" %
          (fmt(base["A"]), fmt(base["B"]), base_margin, "B" if base["B"] < base["A"] else "A"))
    print("twist  (Route 9 closed) A=%s  B=%s  (A-B)/B=%.1f%%  -> %s faster" %
          (fmt(tw["A"]), fmt(tw["B"]), tw_margin, "B" if tw["B"] < tw["A"] else "A"))
    r = risk_per_minute_saved({})
    print("D4 (context, not graded): saved %.2f min; total risk $%.2f; risk/min-saved = $%.2f" %
          (r["minutes_saved"], r["total_risk_usd"], r["risk_usd_per_minute_saved"]))
