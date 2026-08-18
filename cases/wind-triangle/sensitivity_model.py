"""Sensitivity model for Wind Triangle (SPEC §2 balance test, case-readiness Tier 2 probes 4 and 5).

WHAT THIS FILE IS FOR
---------------------
It reproduces, from the case document alone, every number the case claims: each leg's wind
components, course unit vector, along-course and crosswind components, ground speed, leg time and
leg fuel; both routings' trip fuel; the margin; the minimum dispatch fuel under 14 CFR 121.639;
the break-even forecast error; and the Twist. A student following `case.md` Appendices A-E with a
calculator reaches the same figures — there is no hidden constant and no undisclosed blend.

WHAT IS SOURCED AND WHAT IS ASSUMED
-----------------------------------
Waypoint positions .......... SOURCED  case.md Appendix A  [S1, S2]
Forecast winds .............. SOURCED  case.md Appendix B  [S3]
Cruise TAS .................. SOURCED  case.md Appendix C  [S4]
Cruise fuel flow ............ SOURCED  case.md Appendix C  [S5]  (MEDIUM — segment average)
Reserve rule (45 min) ....... SOURCED  case.md Appendix C  [S6]
Jet fuel price .............. SOURCED  case.md Appendix D  [S7]  (as of July 2026)
Airway-structure allowance .. ASSUMED  case.md Appendix E  MA2
Departures per year ......... ASSUMED  case.md Appendix E  MA1
Jet A density ............... ASSUMED  case.md Appendix E  MA4
One wind per leg ............ ASSUMED  case.md Appendix E  MA3 — structural, non-numeric, not swept

FLEX[] lists only the ASSUMED numeric dials, per case-readiness's rule that probe 5 stress-tests
stated assumptions while probe 6 stress-tests cited measurements. Halving a National Weather
Service forecast wind is a different case, not a sensitivity test.

THE HONEST CAVEAT, STATED HERE AND NOT ONLY IN THE REPORT
--------------------------------------------------------
This case's verdict is STABLE under +/-50% of every stated assumption (Routing B stays cheaper,
margin 0.95%-2.40%) and GENUINELY FRAGILE to the cited wind data: a 20.5% uniform overstatement of
Routing A's along-course headwind components flips it. That fragility is the case's headline
finding, not a defect — deliverable D5 asks the student to compute exactly that break-even — and it
is written into case.json.balance.stability and into the Guide Notes so no guide defends a margin
that is sturdier than it is.

MA2 also carries the Twist. At the LOW end of MA2's flex range for the southern corridor (0.75%
instead of 1.5%) the Twist's reroute no longer flips the verdict. That is disclosed in the
facilitator-only half of case.md and in FACILITATOR.md's twist caveat -- NOT in MA2's student-facing
sensitivity column, because naming the Twist there would hand the room the amendment before it is
dropped.

MA5 (leg length = great-circle distance, leg course = the INITIAL great-circle course held constant)
is the geometry convention this file implements. It is stated in case.md Appendix E. Re-solving on
mean-of-initial-and-final courses, on final courses, or on true rhumb-line courses and distances
leaves Routing B cheaper in every case (margin 2.01%, 2.27%, 2.06% against the base 1.67%).
"""
import math

EARTH_RADIUS_NM = 3440.065

# --- SOURCED: waypoint reference positions, case.md Appendix A [S1, S2] -----------------------
POSITIONS = {
    "KJFK": (40.6399, -73.7787),   # New York/John F Kennedy Intl        [S1]
    "KDBQ": (42.4020, -90.7095),   # Dubuque Rgnl                        [S2]
    "KSLC": (40.7884, -111.9778),  # Salt Lake City Intl                 [S2]
    "KSGF": (37.2457, -93.3886),   # Springfield-Branson Ntl             [S2]
    "KABQ": (35.0389, -106.6083),  # Albuquerque Intl Sunport            [S1]
    "KSFO": (37.6188, -122.3754),  # San Francisco Intl                  [S2]
    "KMEM": (35.0424, -89.9767),   # Memphis Intl (Twist only)           [S2]
    "KLAX": (33.9425, -118.4080),  # Los Angeles Intl (filed alternate)  [S1]
}

# --- SOURCED: forecast wind at 34,000 ft, case.md Appendix B [S3] ------------------------------
# (direction the wind blows FROM in degrees true, speed in knots)
WINDS = {
    "KDBQ": (300, 78),   # coded 307843
    "KSLC": (200, 42),   # coded 204244
    "KSGF": (340, 14),   # coded 341441
    "KABQ": (280, 9),    # coded 280940
    "KMEM": (350, 17),   # coded 351741
    "KSFO": (150, 13),   # coded 151345
}

ROUTE_A = [("KJFK", "KDBQ"), ("KDBQ", "KSLC"), ("KSLC", "KSFO")]
ROUTE_B = [("KJFK", "KSGF"), ("KSGF", "KABQ"), ("KABQ", "KSFO")]
ROUTE_B_TWIST = [("KJFK", "KMEM"), ("KMEM", "KABQ"), ("KABQ", "KSFO")]
ALTERNATE_LEG = ("KSFO", "KLAX")

PARAMS = {
    # --- SOURCED ---
    "tas_kt": 460.0,                     # S4 — B738 cruise TAS
    "fuel_flow_lb_per_h": 5304.3,        # S5 — 40.1 kg/min x 60 x 2.20462
    "reserve_minutes": 45.0,             # S6 — 14 CFR 121.639(c)
    "fuel_price_usd_per_gal": 3.403,     # S7 — EIA, as of July 2026

    # --- ASSUMED (case.md Appendix E) ---
    "airway_allowance_a_pct": 1.0,       # MA2 — northern corridor
    "airway_allowance_b_pct": 1.5,       # MA2 — southern corridor
    "fuel_density_lb_per_gal": 6.7,      # MA4
    "departures_per_year": 730.0,        # MA1 — 2/day x 365
}

FLEX = ["airway_allowance_a_pct", "airway_allowance_b_pct",
        "fuel_density_lb_per_gal", "departures_per_year"]


# ---------------------------------------------------------------- geodesy ----
def great_circle_nm(a, b):
    la1, lo1 = map(math.radians, POSITIONS[a])
    la2, lo2 = map(math.radians, POSITIONS[b])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2)
    return 2 * math.asin(math.sqrt(h)) * EARTH_RADIUS_NM


def initial_true_course_deg(a, b):
    la1, lo1 = map(math.radians, POSITIONS[a])
    la2, lo2 = map(math.radians, POSITIONS[b])
    dlon = lo2 - lo1
    y = math.sin(dlon) * math.cos(la2)
    x = math.cos(la1) * math.sin(la2) - math.sin(la1) * math.cos(la2) * math.cos(dlon)
    return (math.degrees(math.atan2(y, x)) + 360) % 360


# ------------------------------------------------------------ wind triangle ----
def wind_vector_kt(direction_from_deg, speed_kt):
    """A wind 'from 300 at 78' BLOWS TOWARD 120 degrees. Returns (east, north) components."""
    toward = math.radians((direction_from_deg + 180) % 360)
    return speed_kt * math.sin(toward), speed_kt * math.cos(toward)


def course_unit_vector(course_deg):
    """Magnitude is exactly 1 by construction: sin^2 + cos^2 = 1 (D2's check)."""
    c = math.radians(course_deg)
    return math.sin(c), math.cos(c)


def leg_solution(frm, to, allowance_pct, tas_kt, wind_scale=1.0, wind_shift_kt=0.0,
                 wind_key=None):
    gc = great_circle_nm(frm, to)
    filed = gc * (1 + allowance_pct / 100.0)
    course = initial_true_course_deg(frm, to)
    wdir, wspd = WINDS[wind_key or to]          # MA3: wind at the downwind-end waypoint
    we, wn = wind_vector_kt(wdir, wspd)
    ue, un = course_unit_vector(course)
    along = we * ue + wn * un                   # D3: the dot product. + tailwind, - headwind
    cross = math.hypot(we - along * ue, wn - along * un)
    along = along * wind_scale + wind_shift_kt  # break-even dials only; 1.0 / 0.0 in the case
    ground_speed = math.sqrt(tas_kt ** 2 - cross ** 2) + along   # D4: magnitude of the sum
    return {"from": frm, "to": to, "gc_nm": gc, "filed_nm": filed, "course_deg": course,
            "wind": f"{wdir:03d}/{wspd:02d}", "w_east_kt": we, "w_north_kt": wn,
            "u_east": ue, "u_north": un, "along_kt": along, "cross_kt": cross,
            "gs_kt": ground_speed, "time_h": filed / ground_speed}


def route_solution(route, allowance_pct, p, wind_scale=1.0, wind_shift_kt=0.0):
    legs = [leg_solution(f, t, allowance_pct, p["tas_kt"], wind_scale, wind_shift_kt)
            for f, t in route]
    time_h = sum(l["time_h"] for l in legs)
    for l in legs:
        l["fuel_lb"] = l["time_h"] * p["fuel_flow_lb_per_h"]
    return {"legs": legs,
            "gc_total_nm": sum(l["gc_nm"] for l in legs),
            "filed_total_nm": sum(l["filed_nm"] for l in legs),
            "time_h": time_h,
            "fuel_lb": time_h * p["fuel_flow_lb_per_h"]}


def trip_fuel(p, wind_scale=1.0, wind_shift_kt=0.0, twist=False):
    a = route_solution(ROUTE_A, p["airway_allowance_a_pct"], p, wind_scale, wind_shift_kt)
    b = route_solution(ROUTE_B_TWIST if twist else ROUTE_B,
                       p["airway_allowance_b_pct"], p, wind_scale, wind_shift_kt)
    return {"A_cost": a["fuel_lb"], "B_cost": b["fuel_lb"], "A": a, "B": b}


def minimum_dispatch_fuel(p, route_fuel_lb):
    """14 CFR 121.639 [S6]: destination + most distant alternate + 45 min at cruise flow.

    The alternate leg is planned against the KSFO wind — the only wind published in the
    destination terminal area (case.md Appendix B has no KLAX row), and case.md Appendix C says
    so explicitly. No airway allowance is applied to a diversion leg."""
    frm, to = ALTERNATE_LEG
    alt = leg_solution(frm, to, 0.0, p["tas_kt"], wind_key="KSFO")
    alt_fuel = alt["time_h"] * p["fuel_flow_lb_per_h"]
    reserve = (p["reserve_minutes"] / 60.0) * p["fuel_flow_lb_per_h"]
    return {"alternate": alt, "alternate_fuel_lb": alt_fuel, "reserve_lb": reserve,
            "minimum_lb": route_fuel_lb + alt_fuel + reserve}


# ------------------------------------------------------- case-readiness API ----
def evaluate(params):
    """CONTRACT: {"A": metric, "B": metric}, higher wins.

    This case's real metric — trip fuel in pounds, and therefore pounds per nautical mile of net
    progress, which is the same ranking because both routings fly to the same destination — is
    LOWER-is-better. To satisfy the higher-wins CONTRACT *and* reproduce case.md's own margin
    definition ((worse - better) / worse) under the framework's generic (max - min) / min formula,
    each routing's fuel is subtracted from twice the worse routing's own fuel. The transform
    collapses algebraically back to exactly (worse - better) / worse, so the probe's margin and
    the case's margin are the same number rather than two silently different ones.
    """
    c = trip_fuel(params)
    ceiling = 2 * max(c["A_cost"], c["B_cost"])
    return {"A": ceiling - c["A_cost"], "B": ceiling - c["B_cost"]}


def evaluate_twist(params):
    """The Twist (FACILITATOR.md): convective weather closes the KSGF corridor, so Routing B is
    re-filed via KMEM. Uses only data already published in case.md Appendices A and B — the twist
    introduces no new number, which is why it cannot depend on an undisclosed constant."""
    c = trip_fuel(params, twist=True)
    ceiling = 2 * max(c["A_cost"], c["B_cost"])
    return {"A": ceiling - c["A_cost"], "B": ceiling - c["B_cost"]}


# ------------------------------------------------------------- break-even ----
def break_even_wind_scale(p, lo=0.0, hi=1.0, iters=200):
    """The factor k such that scaling Routing A's along-course components by k makes the two
    routings burn identical fuel. D5 asks for (1 - k) as a percentage."""
    target = trip_fuel(p)["B_cost"]
    for _ in range(iters):
        mid = (lo + hi) / 2
        if trip_fuel(p, wind_scale=mid)["A_cost"] < target:
            lo = mid
        else:
            hi = mid
    return lo


def break_even_wind_shift_kt(p, lo=0.0, hi=40.0, iters=200):
    """The same break-even expressed additively: knots of headwind removed from every Routing A
    leg."""
    target = trip_fuel(p)["B_cost"]
    for _ in range(iters):
        mid = (lo + hi) / 2
        if trip_fuel(p, wind_shift_kt=mid)["A_cost"] < target:
            hi = mid
        else:
            lo = mid
    return hi


def _margin(a_cost, b_cost):
    worse = max(a_cost, b_cost)
    return (worse - min(a_cost, b_cost)) / worse * 100


if __name__ == "__main__":
    p = dict(PARAMS)
    base = trip_fuel(p)

    for name in ("A", "B"):
        r = base[name]
        print(f"--- Routing {name}")
        for l in r["legs"]:
            print(f"  {l['from']}->{l['to']}: gc {l['gc_nm']:7.1f} nm  filed {l['filed_nm']:7.1f} nm  "
                  f"course {l['course_deg']:6.1f}  wind {l['wind']}  "
                  f"w=({l['w_east_kt']:+6.2f},{l['w_north_kt']:+6.2f})  "
                  f"u=({l['u_east']:+.4f},{l['u_north']:+.4f})  "
                  f"along {l['along_kt']:+6.2f}  cross {l['cross_kt']:5.2f}  "
                  f"GS {l['gs_kt']:6.1f}  t {l['time_h']:.4f} h  fuel {l['fuel_lb']:8,.0f} lb")
        print(f"  totals: gc {r['gc_total_nm']:.1f} nm, filed {r['filed_total_nm']:.1f} nm, "
              f"{r['time_h']:.4f} h, {r['fuel_lb']:,.1f} lb")

    direct = great_circle_nm("KJFK", "KSFO")
    a_cost, b_cost = base["A_cost"], base["B_cost"]
    margin = _margin(a_cost, b_cost)
    print(f"\ndirect KJFK-KSFO great circle: {direct:.1f} nm")
    print(f"lb per nm of net progress: A {a_cost/direct:.3f}   B {b_cost/direct:.3f}")
    print(f"BASE: A {a_cost:,.1f} lb  B {b_cost:,.1f} lb  -> cheaper "
          f"{'A' if a_cost < b_cost else 'B'}, difference {abs(a_cost-b_cost):,.1f} lb, "
          f"margin {margin:.2f}%")

    for name, cost in (("A", a_cost), ("B", b_cost)):
        m = minimum_dispatch_fuel(p, cost)
        print(f"  minimum dispatch fuel, Routing {name}: {m['minimum_lb']:,.0f} lb "
              f"(trip {cost:,.0f} + alternate {m['alternate_fuel_lb']:,.0f} + reserve {m['reserve_lb']:,.0f})")

    k = break_even_wind_scale(p)
    print(f"\nBREAK-EVEN: Routing A's along-course components at {k*100:.1f}% of forecast "
          f"(i.e. forecast overstated by {100*(1-k):.1f}%), "
          f"or {break_even_wind_shift_kt(p):.2f} kt of headwind removed per leg")

    tw = trip_fuel(p, twist=True)
    print(f"\nTWIST (Routing B re-filed via KMEM): A {tw['A_cost']:,.1f} lb  B {tw['B_cost']:,.1f} lb "
          f"-> cheaper {'A' if tw['A_cost'] < tw['B_cost'] else 'B'}, "
          f"margin {_margin(tw['A_cost'], tw['B_cost']):.2f}%  "
          f"(filed {tw['B']['filed_total_nm']:.1f} nm)")

    gal = abs(a_cost - b_cost) / p["fuel_density_lb_per_gal"]
    print(f"\nMoney: {gal:.1f} gal/flight -> ${gal*p['fuel_price_usd_per_gal']:,.2f}/flight -> "
          f"${gal*p['fuel_price_usd_per_gal']*p['departures_per_year']:,.0f}/year")

    ev = evaluate(p)
    lo_k, hi_k = min(ev, key=ev.get), max(ev, key=ev.get)
    ev_margin = (ev[hi_k] - ev[lo_k]) / ev[lo_k] * 100
    assert hi_k == ("A" if a_cost < b_cost else "B"), f"evaluate() winner drifted: {ev}"
    assert abs(ev_margin - margin) < 0.01, \
        f"evaluate() transform drifted from trip_fuel(): {ev_margin:.4f} vs {margin:.4f}"
    print(f"\nevaluate() contract check OK: winner={hi_k}, margin={ev_margin:.2f}% "
          f"(matches the raw fuel margin)")
