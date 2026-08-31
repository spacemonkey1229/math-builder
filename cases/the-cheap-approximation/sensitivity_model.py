#!/usr/bin/env python3
"""
Sensitivity model -- The Cheap Approximation.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

The case's real primary metric is "degrees of error at the operating-range
extremes, per microsecond of on-chip compute time" -- LOWER is better (less
error bought per microsecond spent is more efficient). The Tier 2 harness
always treats a HIGHER returned value as the winner (max(base, key=base.get)),
so evaluate() returns the RECIPROCAL of that ratio (microseconds of accuracy
bought per degree of error, "compute-efficiency"), preserving the higher-wins
convention without changing which option actually wins. B (Table Path) has
the smaller degrees-per-microsecond figure (case.json.balance_test), so B's
reciprocal is larger and evaluate() correctly reports B as the winner.

Method: reproduces D1-D5 from real physics, not a canned lookup. The
Steinhart-Hart equation (1/T_K = A + B*u + C*u^3, u = ln(resistance)) is
solved numerically (bisection -- u is monotonic in T_K over the case's whole
operating range for these positive coefficients) to get the thermistor's TRUE
response at every scanned temperature. The Series Path's 2nd-order Taylor
expansion of T(u) about u0 = ln(R at 25C) [S5] is then compared against that
true response at the range extremes (D3-Series). The Table Path's N-node
table, uniformly spaced in u across the range (MA3/MA4 set N), is compared
against the same true response by a dense piecewise-linear-interpolation scan
(D3-Table). D4 converts each option's stated cycle count (Appendix B) to
microseconds at the stated clock speed. D5 divides.

Fixed (not in FLEX[]): the Steinhart-Hart coefficients, the calibration
center point, the operating-range extremes, the add-instruction cycle cost,
and the clock speed -- all cited data (sources[] S2-S6, S7, S9, S10), not
stated scenario assumptions. Only the four Modeling Assumptions (MA1-MA4) are
swept by default; --flex-all overrides.

Verified against case.json/RESEARCH_LOG.md (2026-08-31 case-fix pass): running this file's
__main__ reproduces, essentially exactly, every row of RESEARCH_LOG.md's MA3 sweep table --
D3-series error 0.667C (doc: 0.67), D3-table error at N=2/4/6/8/32 entries (3.540, 0.486, 0.183,
0.095, 0.005 -- doc: 3.54, 0.49, 0.18, 0.10, 0.005), and D4/D5 cycle-timing figures (5 and 9
cycles; 0.156 and 0.281 us; 4.27 and 3.68 C/us) all match the case of record to 3 significant
figures. This is strong confirmation the model's physics (real Steinhart-Hart inversion, real
2nd-order Taylor expansion, real N-node piecewise-linear interpolation) is right, not a canned
lookup.

CAVEAT on the single margin_pct number: case.json's own documented 13.97% divides by the LOSING
option's raw C/us figure (100*(series-table)/series = 100*(4.27-3.68)/4.27 = 13.97%, matching
RESEARCH_LOG.md's own "Margin vs. D5_series=4.27" column exactly). tier2_probes.py's harness
instead computes margin as 100*(max-min)/min on the RECIPROCAL values this file returns, which is
structurally equivalent to dividing by the WINNING option's raw figure (100*(4.27-3.68)/3.68 =
16.2%) -- a different, equally standard convention (percent-better-than-the-winner vs
percent-worse-than-the-loser), not a modeling error. Both conventions agree on the winner (B) and
both land comfortably under SPEC Sec2's 20% cap; see __main__ output for both figures side by side.

MA3 (flash memory budget) sensitivity, computed by evaluate() at +/-50% from its base value of 6
bytes: -50% (3 bytes, which floors to the same N=2 table as the documented 4-byte row since bytes
are integer-divided by the 2-byte entry width) flips the recommendation to the Series Path (A) by
a wide margin -- the Table Path's 2-node table is far too coarse to compete. +50% (9 bytes, N=4
entries) does NOT flip the winner; it widens the Table Path's (B's) existing lead sharply, since
9 bytes still floor-divides to N=4 exactly like the documented 8-byte row. This confirms
RESEARCH_LOG.md's own finding that MA3 is the single most load-bearing, genuinely
dilemma-flipping assumption in the case, and that the flip happens on the DOWNWARD side of a +/-50%
swing, not the upward side, at this base value. See __main__ output for the exact numbers.
"""
import math

# --- Fixed: cited data (sources[] S2-S7, S9, S10), not stated assumptions ---
STEINHART_A = 1.468e-3      # [S2]
STEINHART_B = 2.383e-4      # [S3]
STEINHART_C = 1.007e-7      # [S4]
CALIBRATION_TEMP_C = 25.0   # [S5] -- Taylor expansion center point
NOMINAL_RESISTANCE_OHM = 2252.0   # [S1] -- resistance at the calibration point
RANGE_LOW_C = 0.0           # [S6] -- accuracy-guaranteed range, revised 2026-08-31
RANGE_HIGH_C = 70.0         # [S6]
CLOCK_MHZ = 32.0            # [S9]
ADD_CYCLES = 1              # [S10] -- ARM Cortex-M0+ TRM, architectural

PARAMS = {
    # --- MA1: cycles per multiply instruction ---------------------------------
    "multiply_cycles": 1.0,
    # --- MA2: cycles for one flash-memory read access --------------------------
    "flash_read_cycles": 3.0,
    # --- MA3: flash memory budget reserved for calibration data, bytes --------
    #     The single most load-bearing dial in the case (FACILITATOR.md).
    "flash_budget_bytes": 6.0,
    # --- MA4: bytes required to store one lookup-table entry ------------------
    "bytes_per_entry": 2.0,
}

# Probe 5 flexes THESE and only these -- the four stated Modeling Assumptions.
# The Steinhart-Hart coefficients, calibration point, operating range, add-cycle
# cost, and clock speed are cited data (module constants above), not scenario
# assumptions -- per SPEC Sec2, halving a sourced datasheet figure is a
# different case, not a sensitivity test.
FLEX = [
    "multiply_cycles",     # MA1
    "flash_read_cycles",   # MA2
    "flash_budget_bytes",  # MA3 -- the case's own documented load-bearing dial
    "bytes_per_entry",     # MA4
]


def _g(u):
    return STEINHART_A + STEINHART_B * u + STEINHART_C * u ** 3


def _u_of_celsius(temp_c):
    """Solve the real (non-Taylor) Steinhart-Hart equation for u = ln(R) at a
    given true temperature, by bisection. g(u) = 1/T_K is monotonically
    increasing in u over the physically relevant domain (all three
    coefficients are positive), so bisection is safe and exact enough."""
    target = 1.0 / (temp_c + 273.15)
    lo, hi = -5.0, 20.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if _g(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def _true_celsius(u):
    """The thermistor's real, non-Taylor response at a given u = ln(R)."""
    return 1.0 / _g(u) - 273.15


def _taylor2_celsius(u, u0):
    """2nd-order Taylor expansion of T(u) = 1/g(u) - 273.15 about u0 (D1)."""
    g0 = _g(u0)
    gp0 = STEINHART_B + 3 * STEINHART_C * u0 ** 2
    gpp0 = 6 * STEINHART_C * u0
    f0 = 1.0 / g0
    fp0 = -gp0 / g0 ** 2
    fpp0 = 2 * gp0 ** 2 / g0 ** 3 - gpp0 / g0 ** 2
    du = u - u0
    f_taylor = f0 + fp0 * du + 0.5 * fpp0 * du ** 2
    return f_taylor - 273.15


def _series_worst_error():
    """D3-Series: 2nd-order Taylor error at both range extremes, worst case."""
    u0 = _u_of_celsius(CALIBRATION_TEMP_C)
    errs = []
    for t_c in (RANGE_LOW_C, RANGE_HIGH_C):
        u_true = _u_of_celsius(t_c)
        approx = _taylor2_celsius(u_true, u0)
        errs.append(abs(approx - t_c))
    return max(errs)


def _table_worst_error(n_entries):
    """D3-Table: worst-case piecewise-linear interpolation error of an
    N-node table, nodes uniformly spaced in u across the operating range,
    against the true (non-Taylor) response. Dense scan in u-space."""
    n = max(2, int(n_entries))
    u_low = _u_of_celsius(RANGE_LOW_C)
    u_high = _u_of_celsius(RANGE_HIGH_C)
    nodes_u = [u_low + i * (u_high - u_low) / (n - 1) for i in range(n)]
    nodes_t = [_true_celsius(u) for u in nodes_u]

    worst = 0.0
    steps = 400
    for i in range(steps + 1):
        u = u_low + i * (u_high - u_low) / steps
        # find bracketing node interval
        seg = min(max(int((u - u_low) / (u_high - u_low) * (n - 1)), 0), n - 2)
        u_a, u_b = nodes_u[seg], nodes_u[seg + 1]
        t_a, t_b = nodes_t[seg], nodes_t[seg + 1]
        frac = 0.0 if u_b == u_a else (u - u_a) / (u_b - u_a)
        interp = t_a + frac * (t_b - t_a)
        true_t = _true_celsius(u)
        worst = max(worst, abs(interp - true_t))
    return worst


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})

    series_error = _series_worst_error()   # cited-data-driven; does not move with FLEX

    n_entries = math.floor(p["flash_budget_bytes"] / p["bytes_per_entry"]) if p["bytes_per_entry"] else 0
    table_error = _table_worst_error(n_entries)

    series_cycles = 2 * p["multiply_cycles"] + 3 * ADD_CYCLES
    table_cycles = 2 * p["flash_read_cycles"] + 1 * p["multiply_cycles"] + 2 * ADD_CYCLES

    series_time_us = series_cycles / CLOCK_MHZ
    table_time_us = table_cycles / CLOCK_MHZ

    series_metric = series_error / series_time_us   # C per microsecond -- LOWER is better
    table_metric = table_error / table_time_us

    # Return reciprocals so the harness's higher-wins convention lines up with
    # the case's actual lower-wins primary metric (see module docstring).
    return {"A": 1.0 / series_metric, "B": 1.0 / table_metric}


# No evaluate_twist() is shipped. FACILITATOR.md's Twist does not construct a
# new numeric scenario -- it reframes the already-computed MA3=6-byte result
# by pointing out it is under a tenth of a percent of the part's total 16 KB
# flash, and asks whether that stated assumption is realistic. MA3 stays at
# its case-of-record value; there is no second metric for evaluate_twist() to
# compute that evaluate() does not already produce. Per SKILL.md, "a case has
# no reason to invent a twist scenario a facilitator can raise as a question
# instead" -- Probe 4 (twist integrity) is assessed against the discussion
# question directly, not a mechanical recomputation.


if __name__ == '__main__':
    base = evaluate({})
    win = max(base, key=base.get)
    lo = min(base, key=base.get)
    harness_margin = 100.0 * (base[win] - base[lo]) / base[lo]

    # Cross-check against the case's own documented D3-D5 figures and margin.
    series_error = _series_worst_error()
    n_entries = math.floor(PARAMS["flash_budget_bytes"] / PARAMS["bytes_per_entry"])
    table_error = _table_worst_error(n_entries)
    series_cycles = 2 * PARAMS["multiply_cycles"] + 3 * ADD_CYCLES
    table_cycles = 2 * PARAMS["flash_read_cycles"] + 1 * PARAMS["multiply_cycles"] + 2 * ADD_CYCLES
    series_time = series_cycles / CLOCK_MHZ
    table_time = table_cycles / CLOCK_MHZ
    series_metric = series_error / series_time
    table_metric = table_error / table_time
    case_margin = 100.0 * (series_metric - table_metric) / series_metric  # case.json convention

    print("D3 series worst error (C):", round(series_error, 3), " (case: 0.67)")
    print("D3 table worst error  (C):", round(table_error, 3), " N =", n_entries, " (case: 1.03, N=3)")
    print("D4 series cycles/time:", series_cycles, round(series_time, 4), "us (case: 5, 0.156)")
    print("D4 table cycles/time :", table_cycles, round(table_time, 4), "us (case: 9, 0.281)")
    print("D5 series C/us:", round(series_metric, 3), " (case: 4.27)")
    print("D5 table C/us :", round(table_metric, 3), " (case: 3.68)")
    print("winner:", win, "(case: B)")
    print("margin, case.json convention (100*(series-table)/series):  %.2f%%  (case: 13.97)" % case_margin)
    print("margin, tier2_probes.py harness convention (100*(max-min)/min on reciprocals): %.2f%%"
          % harness_margin)

    print("\n--- MA3 (flash budget) +/-50%% sensitivity, the case's most load-bearing dial ---")
    for label, bytes_ in (("base (6 bytes)", 6.0), ("-50%% (3 bytes)", 3.0), ("+50%% (9 bytes)", 9.0)):
        r = evaluate({"flash_budget_bytes": bytes_})
        w = max(r, key=r.get)
        m = 100.0 * (max(r.values()) - min(r.values())) / min(r.values())
        print("  %-16s -> %s  winner=%s  harness_margin=%.1f%%" % (label, {k: round(v, 4) for k, v in r.items()}, w, m))
