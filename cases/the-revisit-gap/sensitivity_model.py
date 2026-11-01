"""Sensitivity model for The Revisit Gap (SPEC section 2 balance test, case-readiness Tier 2
probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

The metric here is hectares of confirmed illegal clearing detected per dollar of annual imagery
cost, and HIGHER really is better for both options -- no inversion needed.

Verified by hand against case.json (2026-09-18): base evaluate(PARAMS) reproduces
ratio_A=0.0003273, ratio_B=0.0003914, winner=B (Sentinel Free), margin=16.4%, matching
case.json's own `balance`/`derived` blocks to the stated precision.

PARAMS is split into SOURCED (case.md Appendix A/B/G, a citation id in the comment) and ASSUMED
(case.md Appendix E, Modeling Assumptions, an MA id in the comment). FLEX lists the single dial
Appendix E's own Sensitivity note names as load-bearing: MA6 (the share of annual clearing that
is sub-Sentinel-detectable). MA1-MA5 are documented in case.json as scaling both options
proportionally or affecting only narrative/D1/D3/D4 content, and are left fixed here.
"""

PARAMS = {
    # --- SOURCED (not flexed) ---
    "area_km2": 25.0,                 # case.md Appendix B -- reserve area monitored
    "price_tasking_per_km2": 12.0,    # [S5] SkyFi Planet Select, SkySat Flexible Tasking
    "weeks_per_year": 52.0,
    "scenes_per_year_B": 73.0,        # 365 / 5-day Sentinel-2 revisit [S1]

    # --- ASSUMED (case.md Appendix E, Modeling Assumptions) ---
    "hourly_cost": 35.0,              # MA2
    "hrs_per_scene_A": 1.5,           # MA3
    "hrs_per_scene_B": 3.0,           # MA4
    "total_clearing_ha": 6.0,         # MA5

    # --- ASSUMED, load-bearing -- flexed by probe 5 ---
    "f_small": 0.50,                  # MA6 -- share of clearing sub-Sentinel-detectable
}

FLEX = ["f_small"]


def evaluate(params, f_small_override=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    f_small = f_small_override if f_small_override is not None else p["f_small"]

    subscription_A = p["area_km2"] * p["price_tasking_per_km2"] * p["weeks_per_year"]
    labor_A = p["weeks_per_year"] * p["hrs_per_scene_A"] * p["hourly_cost"]
    total_cost_A = subscription_A + labor_A

    labor_B = p["scenes_per_year_B"] * p["hrs_per_scene_B"] * p["hourly_cost"]
    total_cost_B = labor_B  # no subscription fee

    det_A = p["total_clearing_ha"]
    det_B = p["total_clearing_ha"] * (1.0 - f_small)

    return {"A": det_A / total_cost_A, "B": det_B / total_cost_B}


def evaluate_twist(params):
    """The case's own twist: an independent field audit finds that 75% of this reserve's real
    clearing activity is small enough to evade Sentinel Free's detection floor -- not the 50%
    the original estimate assumed (loggers exploiting cloud cover during the wet season, when
    most real clearing happens, to cut small, hard-to-spot patches). Modeled as f_small=0.75."""
    return evaluate(params, f_small_override=0.75)


def _report(label, ev):
    winner = max(ev, key=ev.get)
    denom = ev[winner] if ev[winner] != 0 else 1.0
    margin = 100.0 * abs(ev["A"] - ev["B"]) / denom
    print(f"{label}: A={ev['A']:.7f} ha/$  B={ev['B']:.7f} ha/$  winner={winner}  margin={margin:.2f}%")
    return winner, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "B", f"Base model drifted: expected Sentinel Free (B) to win, got {winner}"
    assert abs(margin - 16.4) < 0.2, f"Base margin drifted from case.json's disclosed 16.4%: got {margin:.2f}%"

    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (f_small=0.75, independent field audit)", twist)
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
            print(f"  {key:10s} {label:5s}  A={ev['A']:10.7f}  B={ev['B']:10.7f}  winner={hi}  margin={m:6.2f}%{flagstr}")
