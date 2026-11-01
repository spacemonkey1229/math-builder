"""Sensitivity model for The Turbine Channel (SPEC section 2 balance test,
case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     N/A for this case -- see note below

The case's real chain is: integrate current speed over the flow window (m) x
cross-sectional area (m^2) = volume moved per cycle (m^3); volume x Appendix D's
shared conversion factor (MA2) = kWh per cycle. case-research's own ground truth
(RESEARCH_LOG.md "Balance computation") is a numerical trapezoidal integration of
each station's COMPLETE real 6-minute NOAA series (61 points for the Narrows,
77 for the Reach) -- this file does not re-embed all 138 raw points. Instead it
represents each channel's real, sourced curve by its two structurally decisive,
cited scalars -- peak current speed and flow-window duration (case.md Appendix
A/B, [S1]/[S2]) -- combined with a per-channel SHAPE FACTOR calibrated once
against case-research's own full-series numerical integration so that
evaluate(PARAMS) reproduces case.json's disclosed base case (Narrows 10,889
kWh, Reach 11,993 kWh, margin 9.21%, Reach wins) to within rounding.

Verified against a fresh, independent re-fetch of both live NOAA endpoints
(2026-09-12, this QA pass) and a from-scratch trapezoidal re-integration of the
exact same ebb/flood pulses case-research selected (Narrows 00:48-06:54,
Reach 07:48-15:24): peak speeds match exactly (5.28 kn / 1.53 kn), and the
re-derived volumes/kWh (Narrows ~49.46M m^3 / 10,886 kWh; Reach ~54.50M m^3 /
11,994 kWh; margin 9.24%) agree with case.json's recorded figures (49,480,854 /
10,889; 54,498,397 / 11,993; margin 9.21%) to within the expected rounding
noise from case.json's own area figures (1,427.0 rounded vs. the unrounded
146.3 x 9.75 = 1,426.425 this file and the fresh re-integration both use).

PARAMS is split into SOURCED (a citation id in the comment; case.md Appendix A/
B/C, real NOAA data and real channel geometry) and ASSUMED (case.md Appendix E,
an MA id in the comment). FLEX lists only the two ASSUMED scalars -- MA1 (the
Reach's array-site width) and MA2 (the generation-potential conversion factor)
-- per case-readiness's default-scope rule: P5 sweeps stated assumptions, not
cited measurements. The peak-speed and window-duration scalars are real NOAA
data ([S1]/[S2]), not assumptions the case chose, so they are correctly left
out of FLEX and are instead swept in this file's own `__main__` block as an
EXTRA, clearly-labeled analysis (see "why the extra sweep" below) rather than
folded into probe 5's mechanical FLEX[] pass -- exactly the FLEX-scoping
distinction skills/case-readiness/SKILL.md's P5 section describes ("is this
PARAM a real assumption the case had to choose ... or is it given/cited data").

This case has no twist (case.json facilitator.has_twist = false, FACILITATOR.md
"Twist: N/A"). `evaluate_twist` is therefore intentionally NOT defined -- P4 is
scored as N/A rather than run against a fabricated twist.

why the extra sweep: this QA pass was explicitly asked to flex the real station
data (peak speed, window duration) by +/-50% in addition to MA1/MA2, on top of
the standard P5 FLEX scope, precisely because a margin this tight (9.21%) sits
close enough to zero that instability hiding in "given" data rather than
"assumed" data would still be a real, reportable finding -- P5's scope rule
governs what the MACHINE PASS/FAIL gate sweeps by default, it does not forbid
an author from also checking the cited inputs by hand. See QA_REPORT.md for
what this surfaced.
"""

import math

KNOT_TO_MPS = 0.514444444  # 1 knot = 0.514444444 m/s, standard conversion

PARAMS = {
    # --- SOURCED (real NOAA data / real channel geometry; not in FLEX) ---
    "narrows_peak_kn": 5.28,        # Appendix A [S1] -- Narrows peak current speed, real NOAA series
    "narrows_window_min": 366,      # Appendix A [S1] -- Narrows real flow-window duration (slack to slack)
    "narrows_width_m": 146.3,       # Appendix C [S3] -- real Cape Cod Canal width
    "narrows_depth_m": 9.75,        # Appendix C [S3] -- real Cape Cod Canal authorized depth
    "reach_peak_kn": 1.53,          # Appendix B [S2] -- Reach peak current speed, real NOAA series
    "reach_window_min": 456,        # Appendix B [S2] -- Reach real flow-window duration (slack to slack)
    "reach_depth_m": 16.76,         # Appendix C [S4] -- real Chesapeake Bay entrance charted depth

    # --- structural, not flexed: per-channel shape factors calibrated once
    # against case-research's own full-61/77-point numerical (trapezoidal)
    # integration (RESEARCH_LOG.md "Balance computation"). Both channels'
    # real tidal-current curves are close to, but not exactly, a half-sine
    # over their flow window; these constants correct the closed-form
    # sine-integral approximation below back to the real integrated value at
    # each channel's own base peak/duration. Not a dial either channel
    # "chose" -- it is fixed by the shape of the real, already-cited data --
    # so it is neither in FLEX nor swept by the extra analysis.
    "narrows_shape_factor": 0.9131,
    "reach_shape_factor": 0.9265,

    # --- ASSUMED (case.md Appendix E, Modeling Assumptions) ---
    "reach_width_m": 256.0,         # MA1 -- the Reach's array-site width
    "kwh_per_m3": 0.00022,          # MA2 -- generation-potential conversion factor (unrounded 2.2004e-4 used below)
}

FLEX = ["reach_width_m", "kwh_per_m3"]

# unrounded MA2 for internal use (case.md prints the rounded 0.00022; the
# derivation itself -- 1050 / (2.25 * 589.0) / 3600 -- carries more precision).
_MA2_UNROUNDED = 1050.0 / (2.25 * 589.0) / 3600.0


def _half_sine_integral_knot_min(peak_kn, window_min, shape_factor):
    """Closed-form integral of a half-sine speed curve v(t) = peak*sin(pi*t/T)
    over [0, T], corrected by the channel's calibrated shape factor:
        integral_0^T peak*sin(pi t/T) dt = 2*peak*T/pi
    """
    return (2.0 * peak_kn * window_min / math.pi) * shape_factor


def _channel_volume_m3(peak_kn, window_min, shape_factor, width_m, depth_m):
    integral_knot_min = _half_sine_integral_knot_min(peak_kn, window_min, shape_factor)
    integral_m = integral_knot_min * KNOT_TO_MPS * 60.0  # knot*min -> m
    area_m2 = width_m * depth_m
    return integral_m * area_m2


def evaluate(params):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. A = Narrows, B = Reach."""
    p = dict(PARAMS)
    p.update(params or {})

    factor = p.get("kwh_per_m3", _MA2_UNROUNDED)

    narrows_vol = _channel_volume_m3(
        p["narrows_peak_kn"], p["narrows_window_min"], p["narrows_shape_factor"],
        p["narrows_width_m"], p["narrows_depth_m"])
    reach_vol = _channel_volume_m3(
        p["reach_peak_kn"], p["reach_window_min"], p["reach_shape_factor"],
        p["reach_width_m"], p["reach_depth_m"])

    return {"A": narrows_vol * factor, "B": reach_vol * factor}


def _report(label, ev):
    lo_key = min(ev, key=ev.get)
    hi_key = max(ev, key=ev.get)
    margin = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
    print(f"{label}: A(Narrows)={ev['A']:.1f} kWh  B(Reach)={ev['B']:.1f} kWh  "
          f"winner={hi_key}  margin={margin:.2f}%")
    return hi_key, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "B", f"Base model drifted from case.json's disclosed base (B/Reach wins): got {winner}"
    assert abs(margin - 9.21) < 1.0, \
        f"Base margin drifted from case.json's disclosed 9.21%: got {margin:.2f}%"
    assert abs(base["A"] - 10889) / 10889 < 0.02 and abs(base["B"] - 11993) / 11993 < 0.02, \
        f"Base kWh drifted from case.json/FACILITATOR.md: A={base['A']:.1f} B={base['B']:.1f}"

    print("\n--- Probe 5: +/-50% sweep of FLEX[] (the case's stated assumptions, MA1/MA2) ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            hi_key = max(ev, key=ev.get)
            lo_key = min(ev, key=ev.get)
            m = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
            flips = hi_key != winner
            cap_breach = m > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:16s} {label:5s}  A={ev['A']:10.1f}  B={ev['B']:10.1f}  "
                  f"winner={hi_key}  margin={m:6.2f}%{flagstr}")

    print("\n--- EXTRA (beyond default P5 scope, requested for this QA pass): "
          "+/-50% sweep of the real, CITED station data (peak speed, window "
          "duration) -- P6's territory in the normal ladder, checked here by "
          "hand because the base margin (9.21%) is tight enough that fragility "
          "hiding in 'given' rather than 'assumed' data is still worth surfacing ---")
    cited_keys = ["narrows_peak_kn", "narrows_window_min", "reach_peak_kn", "reach_window_min"]
    for key in cited_keys:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            hi_key = max(ev, key=ev.get)
            lo_key = min(ev, key=ev.get)
            m = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
            flips = hi_key != winner
            flagstr = " <-- FLIPS" if flips else ""
            print(f"  {key:20s} {label:5s}  A={ev['A']:10.1f}  B={ev['B']:10.1f}  "
                  f"winner={hi_key}  margin={m:6.2f}%{flagstr}")
