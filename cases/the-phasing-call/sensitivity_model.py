#!/usr/bin/env python3
"""
Sensitivity model — The Phasing Call.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain).

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset that is a stated
                                                     Modeling Assumption
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     optional; illustrates the FACILITATOR.md Twist

The primary metric (case.json.balance.margin_basis) is a straight ratio:
    reserve_hours_remaining(profile) = total_allowance_hours - modeled_transit_hours(profile)
    workable_days_per_30(profile)    = 30 * (phase_angle_tolerance_degrees(profile) / 360)
    metric(profile)                  = reserve_hours_remaining(profile) / workable_days_per_30(profile)

Fixed (not in FLEX[]): total_allowance_hours, modeled_transit_hours(A/B), and
phase_angle_tolerance(A/B) are all CITED, sourced figures (S10, S2, S5, S11 --
see case.json.sources[] / RESEARCH_LOG.md), not stated scenario assumptions.
Per the "Only FLEX[] is swept by default" rule (SPEC Sec2 asks for sensitivity
to stated ASSUMPTIONS, not to cited measurements), these are stress-tested by
Tier 2 probe 6 (data decay), not probe 5. This is also the case's own honest
diagnosis (case.json.balance.margin_note, FACILITATOR.md's "Status" note):
none of the case's real Modeling Assumptions (MA1-MA4) is where the ~1991%
margin comes from -- the margin is structural to the real, sourced Appendix
B/D figures, which is exactly why it needed a per-case MCS-46 waiver rather
than a retune.

Only MA2 (contracted docking deadline) and MA3 (minimum required reserve
fraction) are genuine stated Modeling Assumptions that enter this model, and
both act as pass/fail feasibility gates, not as inputs to the metric's size --
consistent with case.md Appendix E's own stated sensitivity notes for MA2/MA3.
MA1 (tracked bearing/range) only affects the D1-D3 algebra, not D4-D7's
metric, and is not represented here. MA4 (constant angular rate vs. real
multi-burn sequence) only affects the D2/D3 algebra for the same reason.

`calendar_days` (the 30-day launch calendar in Appendix D / D6) is a stated
scenario constant, not a Modeling Assumption -- and it cancels out of the
metric(A)/metric(B) ratio entirely (it multiplies both profiles' denominators
by the same factor), so it is not swept either; kept in PARAMS for
transparency and to make evaluate() a faithful port of case.md's own D6/D7
arithmetic.

Verified against case.json.balance.margin_note (2026-08-31):
    base    A (Fast-Track)   = 37.92 h/day
            B (Phasing Climb) = 1.8133... h/day
            margin  (37.92 - 1.8133) / 1.8133 * 100 = 1991.18%  (matches case.json.margin_pct)
    MA2 (docking deadline) flexed to 48h (-50%): B's 60h transit exceeds the
            deadline -> B disqualified (metric 0), matching case.md Appendix E's
            own stated MA2 sensitivity ("a deadline tightened below ~60 hours
            would begin to threaten the Phasing Climb's flyability").
    MA3 (min reserve fraction) flexed to 0.225 (+50%): still well under B's
            real ~40.5% reserve fraction -- neither profile is disqualified,
            matching Appendix E's own stated MA3 sensitivity.
    evaluate_twist(): an evenly-weighted additive score built from the same
            real reserve-fraction and tolerance-fraction figures gives
            A ~= 0.512, B ~= 0.577 -- the Phasing Climb wins under this
            alternate, equally-legitimate metric construction, illustrating
            the FACILITATOR.md Twist (case.json.derived.twist_additive_score_note).
"""

PARAMS = {
    # --- Appendix C / S10: Soyuz's real total autonomous-flight allowance ----
    "total_allowance_h": 100.8,
    # --- Appendix B / S2, S5: each profile's real, cited modeled transit time -
    "transit_h_A": 6.0,     # Fast-Track  [S2]
    "transit_h_B": 60.0,    # Phasing Climb  [S5]
    # --- Appendix D / S11: each profile's real, cited phase-angle tolerance --
    "phase_tol_A_deg": 30.0,    # Fast-Track  [S11]
    "phase_tol_B_deg": 270.0,   # Phasing Climb  [S11]
    # --- Appendix D / D6: stated scenario launch-calendar length -------------
    #     Cancels out of metric(A)/metric(B) exactly -- not a genuine dial.
    "calendar_days": 30.0,
    # --- Appendix E, MA2: contracted docking deadline ------------------------
    "docking_deadline_h": 96.0,
    # --- Appendix E, MA3: minimum required reserve fraction at docking -------
    "min_reserve_frac": 0.15,
}

# Probe 5 flexes THESE and only these -- the subset that is a stated Modeling
# Assumption (MA2, MA3), not cited/sourced data. total_allowance_h,
# transit_h_A/B, and phase_tol_A/B_deg are all real, cited figures (S2, S5,
# S10, S11) and are NOT flexed by default; --flex-all overrides. calendar_days
# is a stated scenario constant that provably cancels in the ratio, so it is
# excluded from FLEX even though it is not "cited data" either.
FLEX = [
    "docking_deadline_h",   # MA2
    "min_reserve_frac",     # MA3
]


def _reserve_h(p, transit_h):
    return p["total_allowance_h"] - transit_h


def _workable_days(p, tol_deg):
    return p["calendar_days"] * (tol_deg / 360.0)


def evaluate(params):
    """The case's actual graded metric (D7): reserve-hours divided by
    workable-launch-days, gated by the two pass/fail floors (MA2 deadline,
    MA3 minimum reserve) case.md's Background states both profiles must clear
    to be flyable at all."""
    p = dict(PARAMS)
    p.update(params or {})

    reserve_A = _reserve_h(p, p["transit_h_A"])
    reserve_B = _reserve_h(p, p["transit_h_B"])

    feasible_A = (p["transit_h_A"] <= p["docking_deadline_h"]
                  and reserve_A / p["total_allowance_h"] >= p["min_reserve_frac"])
    feasible_B = (p["transit_h_B"] <= p["docking_deadline_h"]
                  and reserve_B / p["total_allowance_h"] >= p["min_reserve_frac"])

    days_A = _workable_days(p, p["phase_tol_A_deg"])
    days_B = _workable_days(p, p["phase_tol_B_deg"])

    metric_A = (reserve_A / days_A) if (feasible_A and days_A > 0) else 0.0
    metric_B = (reserve_B / days_B) if (feasible_B and days_B > 0) else 0.0

    return {"A": metric_A, "B": metric_B}


def evaluate_twist(params=None):
    """NOT a re-scoring of a new plot event -- this case's Twist is an
    analysis-construction insight, not a new fact. This function illustrates
    it mechanically: build an evenly-weighted additive score from the same
    two real quantities (reserve-fraction of total allowance, and
    phase-angle-tolerance-fraction of the full 360-degree range) instead of
    dividing one by the other, and show which option wins under THAT
    construction. See case.json.derived.twist_additive_score_note."""
    p = dict(PARAMS)
    p.update(params or {})

    reserve_frac_A = _reserve_h(p, p["transit_h_A"]) / p["total_allowance_h"]
    reserve_frac_B = _reserve_h(p, p["transit_h_B"]) / p["total_allowance_h"]
    tol_frac_A = p["phase_tol_A_deg"] / 360.0
    tol_frac_B = p["phase_tol_B_deg"] / 360.0

    score_A = 0.5 * reserve_frac_A + 0.5 * tol_frac_A
    score_B = 0.5 * reserve_frac_B + 0.5 * tol_frac_B

    return {"A": score_A, "B": score_B}


if __name__ == '__main__':
    base = evaluate({})
    margin = 100 * (base["A"] - base["B"]) / base["B"]
    print("base  ", {k: round(v, 4) for k, v in base.items()}, "margin %.2f%%" % margin)

    deadline_flip = evaluate({"docking_deadline_h": 48.0})
    print("MA2 -50%% (48h deadline)", {k: round(v, 4) for k, v in deadline_flip.items()},
          "-- B disqualified" if deadline_flip["B"] == 0.0 else "-- B still feasible")

    reserve_flex = evaluate({"min_reserve_frac": 0.225})
    print("MA3 +50%% (0.225 floor)", {k: round(v, 4) for k, v in reserve_flex.items()},
          "-- B disqualified" if reserve_flex["B"] == 0.0 else "-- B still feasible")

    twist = evaluate_twist({})
    winner = "B (Phasing Climb)" if twist["B"] > twist["A"] else "A (Fast-Track)"
    print("twist (additive score)", {k: round(v, 4) for k, v in twist.items()}, "winner:", winner)
