"""Sensitivity model for The Mooring Choice (SPEC section 2 balance test, case-readiness Tier 2
probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

The metric here is net buoyant lift per dollar of total material cost (kg/$), and HIGHER really
is better for both options -- no inversion needed (contrast Pixel Snap's sensitivity_model.py,
whose real metric is lower-is-better and so negates).

Verified by hand against case.json (2026-09-18): base evaluate(PARAMS) reproduces
ratio_A=0.6663, ratio_B=0.8257, winner=B (Spherical Design), margin=19.30%, matching
case.json's own `balance`/`derived` blocks to the stated precision.

PARAMS is split into SOURCED (case.md Appendix A/B/G, a citation id in the comment) and ASSUMED
(case.md Appendix E, Modeling Assumptions, an MA id in the comment). FLEX lists the two dials
Appendix E's own Sensitivity note names as load-bearing: MA4 (shared steel plate thickness) and
MA6 (the Spherical Design's stability-ballast fraction). MA1/MA2/MA3/MA5/MA7 are documented in
case.json as either shared-equally-by-both-options or not meaningfully load-bearing for
margin_pct, and are left fixed here, matching case.json's own sensitivity_note.
"""

import math

PARAMS = {
    # --- SOURCED (not flexed) ---
    "steel_price_per_lb": 2660.55 / 2000.0,   # [S1] Gordian, July 2026, $/ton -> $/lb
    "seawater_density": 1025.0,               # [S2] kg/m3
    "steel_density": 7850.0,                  # [S3] kg/m3
    "concrete_price_per_yd3": 179.95,         # [S4] ConcreteNetwork, 2026 national avg
    "concrete_density": 2400.0,               # [S5] kg/m3

    # --- geometry, MA1-MA3, MA5 (not flexed here -- shared or not case-defining) ---
    "r_spar": 0.60,          # MA2 -- Spar cylinder/cone radius, m
    "h_cyl": 5.40,           # MA2 -- Spar cylinder height, m
    "h_cone": 0.80,          # MA2 -- Spar cone height, m
    "r_sph": 1.15,           # MA3 -- Spherical Design radius, m
    "sinker_base": 1.50,     # MA5 -- shared sinker base side, m
    "sinker_height": 1.00,   # MA5 -- shared sinker height, m
    "ballast_cost": 50.0,    # MA7 -- fixed, small; not flexed

    # --- ASSUMED, load-bearing (case.md Appendix E) -- flexed by probe 5 ---
    "plate_thickness_m": 0.010,   # MA4 -- shared steel hull plate thickness
    "ballast_fraction": 0.65,     # MA6 -- Spherical Design stability ballast, fraction of its own steel weight
}

FLEX = ["plate_thickness_m", "ballast_fraction"]

M3_PER_YD3 = 0.764554857984


def _geometry(p):
    r_spar, h_cyl, h_cone = p["r_spar"], p["h_cyl"], p["h_cone"]
    l_cone = math.sqrt(r_spar**2 + h_cone**2)
    vol_cyl = math.pi * r_spar**2 * h_cyl
    vol_cone = (1 / 3) * math.pi * r_spar**2 * h_cone
    vol_spar = vol_cyl + vol_cone
    sa_spar = (2 * math.pi * r_spar * h_cyl) + (math.pi * r_spar**2) + (math.pi * r_spar * l_cone)

    r_sph = p["r_sph"]
    vol_sph = (4 / 3) * math.pi * r_sph**3
    sa_sph = 4 * math.pi * r_sph**2

    s, h = p["sinker_base"], p["sinker_height"]
    vol_pyr = (1 / 3) * s**2 * h
    slant = math.sqrt((s / 2)**2 + h**2)
    sa_pyr_lateral = 2 * s * slant

    return vol_spar, sa_spar, vol_sph, sa_sph, vol_pyr, sa_pyr_lateral


def _steel_cost(sa, p):
    mass_kg = sa * p["plate_thickness_m"] * p["steel_density"]
    mass_lb = mass_kg * 2.20462262185
    return mass_kg, mass_lb * p["steel_price_per_lb"]


def evaluate(params, fab_surcharge_frac=0.0):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. fab_surcharge_frac (default 0, i.e.
    no surcharge) is the twist's own lever -- see evaluate_twist()."""
    p = dict(PARAMS)
    p.update(params or {})

    vol_spar, sa_spar, vol_sph, sa_sph, vol_pyr, sa_pyr_lateral = _geometry(p)

    mass_spar, cost_spar_steel = _steel_cost(sa_spar, p)
    mass_sph, cost_sph_steel = _steel_cost(sa_sph, p)
    cost_sph_steel *= (1.0 + fab_surcharge_frac)   # twist lever: specialty curved-plate surcharge

    mass_pyr_kg = vol_pyr * p["concrete_density"]
    cost_pyr = (vol_pyr / M3_PER_YD3) * p["concrete_price_per_yd3"]
    sinker_submerged_kg = (p["concrete_density"] - p["seawater_density"]) * vol_pyr

    ballast_mass = p["ballast_fraction"] * mass_sph
    ballast_cost = p["ballast_cost"]

    disp_spar = vol_spar * p["seawater_density"]
    disp_sph = vol_sph * p["seawater_density"]

    net_spar = disp_spar - mass_spar - sinker_submerged_kg
    net_sph = disp_sph - mass_sph - sinker_submerged_kg - ballast_mass

    total_cost_spar = cost_spar_steel + cost_pyr
    total_cost_sph = cost_sph_steel + cost_pyr + ballast_cost

    return {"A": net_spar / total_cost_spar, "B": net_sph / total_cost_sph}


def evaluate_twist(params):
    """The case's own twist: the shop's steel supplier reports that the Spherical Design's
    compound-curved plates cannot be rolled in-house and must be subcontracted, at a stated 40%
    surcharge on the Spherical Design's own steel cost (not the Spar's -- the Spar's flat
    cylindrical sides need no specialty rolling, per Background)."""
    return evaluate(params, fab_surcharge_frac=0.40)


def _report(label, ev):
    winner = max(ev, key=ev.get)
    loser = min(ev, key=ev.get)
    denom = ev[winner] if ev[winner] != 0 else 1.0
    margin = 100.0 * abs(ev["A"] - ev["B"]) / denom
    print(f"{label}: A={ev['A']:.4f} kg/$  B={ev['B']:.4f} kg/$  winner={winner}  margin={margin:.2f}%")
    return winner, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "B", f"Base model drifted: expected Spherical Design (B) to win, got {winner}"
    assert abs(margin - 19.3) < 0.2, f"Base margin drifted from case.json's disclosed 19.3%: got {margin:.2f}%"

    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (40% specialty-rolling surcharge on Spherical Design's steel)", twist)
    if t_winner != winner:
        print(f"  NOTE: twist FLIPS the winner from {winner} to {t_winner} -- this is the intended finding.")

    print("\n--- Probe 5: +/-50% sweep of every FLEX assumption ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            hi = max(ev, key=ev.get)
            denom = ev[hi] if ev[hi] != 0 else 1.0
            m = 100.0 * abs(ev["A"] - ev["B"]) / denom
            flips = hi != winner
            cap_breach = m > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:20s} {label:5s}  A={ev['A']:8.4f}  B={ev['B']:8.4f}  winner={hi}  margin={m:6.2f}%{flagstr}")
