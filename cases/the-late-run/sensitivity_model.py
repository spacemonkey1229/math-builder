#!/usr/bin/env python3
"""
Sensitivity model — The Late Run.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     optional; same shape, with the twist applied

The metric returned is the case's actual primary metric: the percent of the
glass viewing-room window's own specular glare (Fresnel reflectance at the
real sun-incidence angle) that a perfectly-tuned polarizer can remove, for
the August Call (A) and the September Call (B).

Physics reproduced end to end, not looked up: sun azimuth/elevation are
computed from a standard NOAA-style solar-position formula (Spencer's Fourier
approximation for solar declination and the equation of time -- the same
family of formulas gml.noaa.gov/grad/solcalc's own calculator implements),
not copied from the case's cited NOAA readings. This lets every Modeling
Assumption (MA1 window orientation, MA2 call time, MA3 September date) be
flexed through the SAME geometry the case's own Appendix C/D arithmetic uses,
rather than only being able to look up the three or four date/time
combinations RESEARCH_LOG.md happens to have fetched by hand.

Calibration note: this closed-form approximation reproduces the case's two
cited NOAA readings (Aug 19 2026 14:00 PDT; Sep 22 2026 14:00 PDT) to within
about 0.15 degrees of azimuth and about 0.5 degrees of elevation (the NOAA
calculator additionally applies an atmospheric refraction correction this
model omits). That is a wide enough margin, at these incidence angles, to
leave every qualitative Tier-2 finding below unchanged, but it is why this
model's own base numbers are reported alongside the case's cited figures in
the __main__ block rather than asserted to match to the decimal.

Fixed (not in FLEX[]): the glass's refractive index (n=1.52, [S1] -- a cited
material constant, not a scenario choice) and the Locks' coordinates ([S4]).
The August Call's own date (August 19, 2026) is also fixed -- it is not a
Modeling Assumption, it is the real, WDFW-count-confirmed single best Chinook
day of the season (S5), which is why FLEX only ever moves the September
date, not the August one.

Verified against case.md/case.json/RESEARCH_LOG.md (2026-08-31 case-readiness pass):
    base    A (Aug 19, 2026, 2:00 PM PDT) ~= 99.9% removed
            B (Sep 22, 2026, 2:00 PM PDT) ~= 90-91% removed
            relative margin ~= 10-11%, matching case.json.balance.margin_pct (10.7),
            Option A winning -- within this model's own ~0.5 deg calibration error.
    MA1 (window_normal_azimuth_deg) flexed across 90/135/180/225/270: FLIPS the
            winner at 135 (SE) and 270 (W); stays A at 180 (used), 225 (SW), and
            widens further at 90 (E) -- matching case.json.modeling_assumptions[MA1].
    MA2 (call_hour_offset_from_noon) flexed across 1:00/2:00/3:00 PM: winner
            stays A throughout, margin narrows toward late afternoon --
            matching MA2's recorded sensitivity.
    MA3 (sep_day_offset_from_16) flexed across Sept 15/22/29: winner stays A
            throughout, margin widens later in the window -- matching MA3's
            recorded sensitivity.
    MA4 (tolerance_multiplier) does not appear in evaluate() at all -- it only
            feeds the D2 rotation-offset worksheet (see d2_rotation_offset_deg
            below), never the D4 percent-removed/margin metric this file's
            evaluate() reproduces, matching the case's own FACILITATOR.md note
            that MA4 changes September's D2 answer substantially and August's
            barely, but touches D4's winner/margin not at all.
"""
import math

# --- Fixed: cited/derived constants, not stated modeling assumptions -------
LAT_DEG = 47.66556          # [S4] Ballard Locks coordinates
LON_DEG = -122.39722        # [S4] (east-positive convention -> west is negative)
TZ_OFFSET_HOURS = -7.0      # PDT, fixed calendar convention, not a scenario choice
N_AIR = 1.0

PARAMS = {
    # --- Appendix A: glass refractive index -- fixed, cited, NOT flexed ------
    "n_glass": 1.52,                        # [S1]

    # --- Appendix C: the August Call's date -- fixed, NOT flexed. This is the
    #     real, WDFW-count-confirmed single best Chinook day of the season
    #     (S5), not a scenario dial the case chose freely.
    "aug_month": 8,
    "aug_day": 19,

    # --- MA1: window's outward-facing compass orientation (surface normal
    #     azimuth, degrees). THE load-bearing dial -- see docstring. ----------
    "window_normal_azimuth_deg": 180.0,

    # --- MA2: shared call time on both dates, expressed as hours after solar
    #     noon (PDT) rather than a raw 24h clock hour, so a +/-50% flex lands on
    #     a physically meaningful "an hour earlier/later" swing (1:00/3:00 PM)
    #     instead of an arbitrary clock-hour arithmetic artifact (e.g. flexing
    #     the raw hour "14" by 50% would land on 7:00 AM / 9:00 PM, which is not
    #     what MA2's own sensitivity note tests). base 2.0 -> 2:00 PM. ---------
    "call_hour_offset_from_noon": 2.0,

    # --- MA3: specific September date within the documented Coho window,
    #     expressed as days after September 16 (the window's own start date)
    #     so a +/-50% flex stays inside the real documented window rather than
    #     landing outside September. base 6 -> Sept 16+6 = Sept 22. -----------
    "sep_month": 9,
    "sep_day_offset_from_16": 6,

    # --- MA4: production glare tolerance multiplier for Challenge D2 (does
    #     NOT feed evaluate()/D4 -- see docstring and d2_rotation_offset_deg).
    "tolerance_multiplier": 2.0,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption, not cited/sourced data. n_glass (S1) and the August date (S5,
# the real season-best day) are fixed inputs, not scenario choices, so they
# are NOT flexed by default; --flex-all overrides.
FLEX = [
    "window_normal_azimuth_deg",     # MA1
    "call_hour_offset_from_noon",    # MA2
    "sep_day_offset_from_16",        # MA3
    "tolerance_multiplier",          # MA4 (affects D2 only; see docstring)
]


# ------------------------------------------------------------- solar position
def _day_of_year(year, month, day):
    import datetime
    return datetime.date(year, month, day).timetuple().tm_yday


def solar_position(year, month, day, hour, minute, lat_deg, lon_deg, tz_offset_hours):
    """NOAA-style solar azimuth/elevation (Spencer's Fourier approximation for
    declination and the equation of time -- the same family of formulas NOAA's
    own Solar Position Calculator implements). lon_deg is east-positive."""
    N = _day_of_year(year, month, day)
    frac_hour = hour + minute / 60.0
    gamma = 2 * math.pi / 365.0 * (N - 1 + (frac_hour - 12) / 24.0)

    eqtime = 229.18 * (0.000075 + 0.001868 * math.cos(gamma) - 0.032077 * math.sin(gamma)
                        - 0.014615 * math.cos(2 * gamma) - 0.040849 * math.sin(2 * gamma))
    decl = (0.006918 - 0.399912 * math.cos(gamma) + 0.070257 * math.sin(gamma)
            - 0.006758 * math.cos(2 * gamma) + 0.000907 * math.sin(2 * gamma)
            - 0.002697 * math.cos(3 * gamma) + 0.00148 * math.sin(3 * gamma))

    time_offset = eqtime + 4 * lon_deg - 60 * tz_offset_hours
    tst = frac_hour * 60 + time_offset
    ha_deg = tst / 4.0 - 180.0

    lat = math.radians(lat_deg)
    ha = math.radians(ha_deg)

    cos_zenith = math.sin(lat) * math.sin(decl) + math.cos(lat) * math.cos(decl) * math.cos(ha)
    cos_zenith = max(-1.0, min(1.0, cos_zenith))
    zenith = math.acos(cos_zenith)
    elevation_deg = 90.0 - math.degrees(zenith)

    sin_zenith = math.sin(zenith)
    if abs(sin_zenith) < 1e-9:
        azimuth_deg = 180.0
    else:
        cos_az = (math.sin(lat) * cos_zenith - math.sin(decl)) / (math.cos(lat) * sin_zenith)
        cos_az = max(-1.0, min(1.0, cos_az))
        if ha_deg > 0:
            azimuth_deg = (math.degrees(math.acos(cos_az)) + 180) % 360
        else:
            azimuth_deg = (540 - math.degrees(math.acos(cos_az))) % 360

    return azimuth_deg, elevation_deg


def incidence_angle_deg(elevation_deg, sun_azimuth_deg, window_normal_azimuth_deg):
    """A vertical window's incidence angle depends on BOTH the sun's elevation
    and its azimuth offset from the window's own outward normal (Appendix D /
    the case's own trap) -- not elevation alone."""
    cos_ti = (math.cos(math.radians(elevation_deg))
              * math.cos(math.radians(sun_azimuth_deg - window_normal_azimuth_deg)))
    cos_ti = max(-1.0, min(1.0, cos_ti))
    return math.degrees(math.acos(cos_ti))


def fresnel_pct_removed(n1, n2, theta_i_deg):
    """Returns (R, R_p, residual R_p/2, percent of R removable by a
    perfectly-tuned polarizer) -- Appendix D's own formulas."""
    ti = math.radians(theta_i_deg)
    sin_tt = (n1 / n2) * math.sin(ti)
    sin_tt = max(-1.0, min(1.0, sin_tt))
    tt = math.asin(sin_tt)
    cos_ti, cos_tt = math.cos(ti), math.cos(tt)
    Rs = ((n1 * cos_ti - n2 * cos_tt) / (n1 * cos_ti + n2 * cos_tt)) ** 2
    Rp = ((n1 * cos_tt - n2 * cos_ti) / (n1 * cos_tt + n2 * cos_ti)) ** 2
    R = (Rs + Rp) / 2.0
    residual = Rp / 2.0
    pct_removed = 100.0 * (R - residual) / R if R > 0 else 0.0
    return R, Rp, residual, pct_removed


def _pct_removed_for(params, year, month, day, hour, minute, normal_az):
    az, el = solar_position(year, month, day, hour, minute, LAT_DEG, LON_DEG, TZ_OFFSET_HOURS)
    ti = incidence_angle_deg(el, az, normal_az)
    _, _, _, pct = fresnel_pct_removed(N_AIR, params["n_glass"], ti)
    return pct


def _call_hour_minute(p):
    """call_hour_offset_from_noon (hours after 12:00 noon PDT, may be
    fractional) -> (hour, minute), clamped to a sane 24h range."""
    total_min = round((12.0 + p["call_hour_offset_from_noon"]) * 60)
    total_min = max(0, min(23 * 60 + 59, total_min))
    return total_min // 60, total_min % 60


def _sep_day(p):
    """sep_day_offset_from_16 (days after Sept 16) -> a valid September day,
    clamped to [1, 30] so an out-of-range flex still lands inside September
    rather than rolling into October (kept simple on purpose: this model tests
    the STATED assumption's sensitivity, not calendar arithmetic edge cases)."""
    day = 16 + round(p["sep_day_offset_from_16"])
    return max(1, min(30, day))


def evaluate(params=None):
    """The case's real D4 metric: percent of the window's own glare a
    perfectly-tuned polarizer removes, August Call (A) vs. September Call (B)."""
    p = dict(PARAMS)
    p.update(params or {})
    normal_az = p["window_normal_azimuth_deg"]
    hour, minute = _call_hour_minute(p)
    pct_aug = _pct_removed_for(p, 2026, p["aug_month"], p["aug_day"], hour, minute, normal_az)
    pct_sep = _pct_removed_for(p, 2026, p["sep_month"], _sep_day(p), hour, minute, normal_az)
    return {"A": pct_aug, "B": pct_sep}


def evaluate_twist(params=None):
    """The case's twist is not a new number -- it is re-reading MA1 (the
    window's compass orientation) critically instead of accepting the
    location scout's 'south side of the canal' as a confirmed bearing (see
    FACILITATOR.md, 'Twist'). This reproduces the twist by recomputing under
    a representative alternate orientation (135 deg, southeast) that the
    case's own MA1 sensitivity table shows inverts the winner."""
    p = dict(PARAMS)
    p.update(params or {})
    p["window_normal_azimuth_deg"] = 135.0
    return evaluate(p)


def d2_rotation_offset_deg(params=None):
    """Not part of the Tier 2 evaluate() contract -- solves Challenge D2's own
    equation, I(theta) = R_p/2 + (R - R_p/2) sin^2(theta) = tolerance, for
    theta over [0, 90] deg, at each date's own R/R_p and the stated MA4
    tolerance. Included only to verify MA4's documented finding (it moves
    September's D2 answer substantially and August's barely, while never
    touching D4's evaluate() metric above)."""
    p = dict(PARAMS)
    p.update(params or {})
    normal_az = p["window_normal_azimuth_deg"]
    hour, minute = _call_hour_minute(p)
    out = {}
    for label, month, day in (("A", p["aug_month"], p["aug_day"]),
                              ("B", p["sep_month"], _sep_day(p))):
        az, el = solar_position(2026, month, day, hour, minute,
                                 LAT_DEG, LON_DEG, TZ_OFFSET_HOURS)
        ti = incidence_angle_deg(el, az, normal_az)
        R, Rp, residual, _ = fresnel_pct_removed(N_AIR, p["n_glass"], ti)
        tol = p["tolerance_multiplier"] * residual
        # solve for sin^2(theta): tol = residual + (R - residual) * sin^2(theta)
        denom = (R - residual)
        s2 = (tol - residual) / denom if denom > 0 else 0.0
        s2 = max(0.0, min(1.0, s2))
        theta = math.degrees(math.asin(math.sqrt(s2)))
        out[label] = theta
    return out


if __name__ == '__main__':
    base = evaluate({})
    print("base ", {k: round(v, 3) for k, v in base.items()},
          "margin %.2f%%" % (100 * (base["A"] - base["B"]) / base["B"]),
          "(case.json.balance.margin_pct = 10.7, Option A)")

    print("\n--- MA1: window_normal_azimuth_deg sweep ---")
    for az in (90, 135, 180, 225, 270):
        r = evaluate({"window_normal_azimuth_deg": az})
        margin = 100 * (r["A"] - r["B"]) / r["B"] if r["B"] else float("inf")
        winner = "A" if r["A"] > r["B"] else ("B" if r["B"] > r["A"] else "TIE")
        print(f"  az={az:>3}  A={r['A']:.2f}  B={r['B']:.2f}  margin={margin:+.2f}%  winner={winner}")

    print("\n--- MA2: call_hour_offset_from_noon sweep (1:00/2:00/3:00 PM) ---")
    for off in (1.0, 2.0, 3.0):
        r = evaluate({"call_hour_offset_from_noon": off})
        margin = 100 * (r["A"] - r["B"]) / r["B"]
        print(f"  offset={off}  A={r['A']:.2f}  B={r['B']:.2f}  margin={margin:+.2f}%  winner={'A' if r['A']>r['B'] else 'B'}")

    print("\n--- MA3: sep_day_offset_from_16 sweep (Sept 15/22/29) ---")
    for off in (-1, 6, 13):
        r = evaluate({"sep_day_offset_from_16": off})
        margin = 100 * (r["A"] - r["B"]) / r["B"]
        print(f"  sep_day={16+off}  A={r['A']:.2f}  B={r['B']:.2f}  margin={margin:+.2f}%  winner={'A' if r['A']>r['B'] else 'B'}")

    print("\n--- MA4: tolerance_multiplier sweep (D2 only, does not feed evaluate()) ---")
    for mult in (1.5, 2.0, 3.0):
        d2 = d2_rotation_offset_deg({"tolerance_multiplier": mult})
        print(f"  x{mult}  D2 offset: Aug={d2['A']:.2f} deg  Sep={d2['B']:.2f} deg")

    print("\n--- Twist: representative alternate orientation (135 deg, SE) ---")
    tw = evaluate_twist({})
    print("  ", {k: round(v, 2) for k, v in tw.items()},
          "winner:", "A" if tw["A"] > tw["B"] else "B")
