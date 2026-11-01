"""Sensitivity model for Pixel Snap (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

IMPORTANT -- metric direction is INVERTED from the case's own units. Pixel Snap's real metric
(case.md D5, case.json primary_metric) is "hectares of falsely-flagged new clearing per
analyst-hour spent" -- for this metric LOWER is better (less wasted field-dispatch area per hour
of registration work). The generic Tier 2 harness (tier2_probes.py) picks the winner as
max(evaluate(...)), i.e. it assumes higher-is-better. So evaluate() below returns the NEGATIVE of
the real ratio for each option -- the harness's max() then correctly recovers the option with the
smaller real ratio as the winner, exactly matching case.json's own margin_basis logic. Anywhere
this file or its __main__ block prints a human-readable ratio, it prints the real positive
hectares/analyst-hour value, not the negated one.

This file reproduces case.json's `balance.margin_basis` computation, NOT the naive single-scene
ratio the raw D5 arithmetic alone would produce. The two are deliberately different numbers, and
that gap is the case's real teaching point (FACILITATOR.md, "The trap"):

    naive, Kutai-scene-only ratio      : Fast Lock 4.8 ha/hr   vs True Lock 0.24 ha/hr  (~95% gap)
    resolved, whole-month/shared-budget: Fast Lock 4.8 ha/hr   vs True Lock 4.08 ha/hr  (15.0% gap)

Verified by hand against case.json/FACILITATOR.md (2026-09-12): base evaluate(PARAMS) reproduces
ratio_A=4.80, ratio_B=4.08, winner=B (True Lock), margin=15.0% to the same precision case.json's
`balance` object and FACILITATOR.md's "The margin" section state.

PARAMS is split into SOURCED (case.md Appendix C/G, a citation id in the comment) and ASSUMED
(case.md Appendix E, Modeling Assumptions, an MA id in the comment). FLEX lists only the three
assumption dials this case's readiness pass was asked to stress-test: MA1 (tree-edge length),
MA3 (True Lock's achieved RMSE), and the combined MA4/MA7 shared-monthly-budget/concession-count
assumption (represented here as a single dial, n_concessions, per MA4's own stated definition --
"MA4 = n_concessions * fast_lock_hours_per_scene" -- so flexing n_concessions flexes both
together, exactly as the case's own Modeling Assumptions section frames them as one decision).
MA5/MA6 (Fast Lock's/True Lock's per-scene analyst-hours) and MA2/MA8/MA9 (GCP placement, dispatch
cost, resampling scale factor) are documented in case.json as not load-bearing for margin_pct and
are left fixed here, matching the task's explicit scope.
"""

PARAMS = {
    # --- SOURCED (not flexed) ---
    "fast_lock_residual_m": 5.0,     # Appendix C [S7] -- typical whole-pixel (nearest-neighbor)
                                      # multitemporal co-registration residual, 95.5% confidence
    "native_geoloc_m": 12.0,         # Appendix C [S7] -- Sentinel-2 L2A absolute geolocation
                                      # accuracy; the residual a concession falls back to if it
                                      # gets NO registration correction at all this month
    "fast_lock_hours_per_scene": 1.0 / 3.0,   # MA5 -- 20 minutes; not flexed here (out of scope
                                               # per task instructions), held fixed
    "true_lock_hours_per_scene": 4.0,         # MA6 -- 4 hours; not flexed here, held fixed

    # --- ASSUMED (case.md Appendix E, Modeling Assumptions) -- flexed by probe 5 ---
    "tree_edge_m": 3200.0,           # MA1 -- Kutai tree-line polygon edge length exposed to
                                      # misregistration (320 px x 10 m/px)
    "true_lock_rmse_m": 3.0,         # MA3 -- True Lock's achieved sub-pixel registration RMSE
    "n_concessions": 5.0,            # MA4/MA7 combined -- number of concessions (Kutai + N-1
                                      # neighbors) sharing Priya's fixed monthly registration-hour
                                      # budget, which MA4 defines as exactly
                                      # n_concessions * fast_lock_hours_per_scene (zero slack)
}

FLEX = ["tree_edge_m", "true_lock_rmse_m", "n_concessions"]


def _ha(edge_m, residual_m):
    """Misregistration ribbon area (edge length x residual width) in hectares."""
    return edge_m * residual_m / 10000.0


def _policy_ratios(p):
    """Reproduces case.json's balance.margin_basis: Policy A (Fast Lock run on every
    concession) vs Policy B (True Lock run on Kutai only; remaining budget, if any, covers
    as many of the other concessions with Fast Lock as it can; any left over get no
    correction at all and fall back to native_geoloc_m). Returns the two REAL, positive
    hectares-per-analyst-hour ratios (lower is better)."""
    n = max(1, round(p["n_concessions"]))
    fast_ha = _ha(p["tree_edge_m"], p["fast_lock_residual_m"])
    true_ha = _ha(p["tree_edge_m"], p["true_lock_rmse_m"])
    native_ha = _ha(p["tree_edge_m"], p["native_geoloc_m"])
    fast_hr = p["fast_lock_hours_per_scene"]
    true_hr = p["true_lock_hours_per_scene"]

    monthly_budget_hr = n * fast_hr  # MA4's own definition: zero slack, N x Fast Lock's per-scene time

    # Policy A: every one of the n concessions gets Fast Lock.
    ratio_a = fast_ha / fast_hr  # total (n*fast_ha) / total (n*fast_hr) -- n cancels

    # Policy B: True Lock spent on Kutai first; whatever budget remains (if any) covers as
    # many of the other n-1 concessions with Fast Lock as it can; the rest get nothing.
    remaining_hr = max(0.0, monthly_budget_hr - true_hr)
    fast_lockable = min(n - 1, int(remaining_hr / fast_hr + 1e-9)) if fast_hr > 0 else 0
    unregistered = (n - 1) - fast_lockable

    total_fp_b = true_ha + fast_lockable * fast_ha + unregistered * native_ha
    total_hr_b = true_hr + fast_lockable * fast_hr
    ratio_b = total_fp_b / total_hr_b if total_hr_b > 0 else float("inf")

    return ratio_a, ratio_b


def evaluate(params):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Returned values are the NEGATIVE of
    the real hectares/analyst-hour ratios -- see module docstring."""
    p = dict(PARAMS)
    p.update(params or {})
    ratio_a, ratio_b = _policy_ratios(p)
    return {"A": -ratio_a, "B": -ratio_b}


def evaluate_twist(params):
    """FACILITATOR.md's twist: a cloud bank covers 3 of the tile's 4 quadrants this month, so
    True Lock can only sub-pixel-correct the one clean quadrant's GCP. Modeled here as True
    Lock achieving only the native/unregistered accuracy on Kutai itself this month (i.e. the
    quadrant actually flagged is cloud-covered) -- True Lock's real advantage over Fast Lock on
    Kutai evaporates even though its hours are still fully spent."""
    p = dict(PARAMS)
    p.update(params or {})
    p["true_lock_rmse_m"] = p["native_geoloc_m"]  # no usable GCP in the flagged quadrant this month
    return evaluate(p)


def _report(label, ev):
    real = {k: -v for k, v in ev.items()}  # back to real, positive, lower-is-better ratios
    winner = min(real, key=real.get)  # LOWER real ratio wins
    loser = max(real, key=real.get)
    denom = real["A"] if real["A"] != 0 else 1.0
    margin = 100.0 * abs(real["A"] - real["B"]) / denom  # matches case.json's own |A-B|/A convention
    print(f"{label}: A={real['A']:.4f} ha/hr  B={real['B']:.4f} ha/hr  "
          f"winner={winner}  margin={margin:.2f}%")
    return winner, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "B", f"Base model drifted: expected True Lock (B) to win, got {winner}"
    assert abs(margin - 15.0) < 0.1, \
        f"Base margin drifted from case.json's disclosed 15.0%: got {margin:.2f}%"
    real_base = {k: -v for k, v in base.items()}
    assert abs(real_base["A"] - 4.8) < 0.01 and abs(real_base["B"] - 4.08) < 0.01, \
        f"Base ratios drifted from FACILITATOR.md: A={real_base['A']:.4f} B={real_base['B']:.4f}"

    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (cloud-covered quadrant -> True Lock loses its edge on Kutai)", twist)
    # Not asserted to a specific winner: FACILITATOR.md's twist is that True Lock cannot
    # sub-pixel-correct a cloud-covered quadrant this month, so IF the flagged ribbon sits
    # there, True Lock's Kutai-scene accuracy collapses to the native/unregistered figure.
    # Modeled that way here, the margin between the two policies collapses to ~0% (True
    # Lock's whole-month advantage was entirely the RMSE gap on Kutai itself) rather than
    # flipping outright to Fast Lock -- a real, reportable Tier 2 finding in its own right
    # (see QA_REPORT.md), not a bug in this file.
    if t_margin > 1.0:
        print(f"  NOTE: twist margin ({t_margin:.2f}%) did not collapse toward 0% as expected -- investigate.")

    print("\n--- Probe 5: +/-50% sweep of every FLEX assumption ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            real = {k: -v for k, v in ev.items()}
            hi_key = min(real, key=real.get)   # winner = lower real ratio
            lo_key = max(real, key=real.get)
            denom = real["A"] if real["A"] != 0 else 1.0
            m = 100.0 * abs(real["A"] - real["B"]) / denom
            flips = hi_key != winner
            cap_breach = m > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:20s} {label:5s}  A={real['A']:8.4f}  B={real['B']:8.4f}  "
                  f"winner={hi_key}  margin={m:6.2f}%{flagstr}")
