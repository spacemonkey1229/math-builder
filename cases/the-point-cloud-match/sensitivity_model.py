"""Sensitivity model for The Point Cloud Match (SPEC section 2 balance test, case-readiness
Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

READ THIS BEFORE TRUSTING THE ±50% NUMBERS BELOW. This case is not shaped like a normal
sensitivity case, and treating it like one is misleading. The case's real decision is binary
and evidentiary -- "did the student catch that Marker 3's actual position is a reflection, not
noise, and therefore that the rig's self-reported 0.40mm (MA4) cannot be trusted" -- not a smooth
trade-off that degrades gracefully as a dial moves. Once a student does D2-D4 correctly, Option
A's REAL leftover error is ~160.65mm (case.json balance.true_reveal_ratio_note), a fixed geometric
fact derived from Appendix B's given coordinates -- it is not a modeling assumption and is not
swept here. Nothing in Appendix E (MA1-MA6) can make that 160.65mm number go away; a defensible
solution always ends at Option B once the reflection is found. So the ±50% sweep below answers a
narrower, real, but secondary question: does flexing the case's genuine modeling-assumption
dials (MA1's tolerance, MA2/MA3's manual-time estimates) change what the FACE-VALUE ratio in
Challenge 3 D5 says BEFORE a student has caught the trap? That's still worth knowing (a student
who has NOT yet caught the mirror is reading D5's naive ratio, and whether that naive ratio is
fragile matters to how convincing the trap is) -- but it is a different, weaker claim than "the
recommendation is sensitive to assumptions," and this file is explicit about that distinction
throughout, per this pipeline stage's own instructions.

MA4 (rig's self-reported 0.40mm) and MA5 (manual-correction residual 0.55mm) are themselves
disclosed Modeling Assumptions in case.md Appendix E, but they are not swept by FLEX[] here: they
are the case's central *trap* values (case.json modeling_assumptions[] MA4/MA5 sensitivity notes:
"the whole margin_pct rests on it being trusted", "sits just above the tolerance ... by design"),
the object of Tier 2 Probe 3 (trap check) and Probe 6 (data decay/plausibility), not a scenario
dial a case author picked to be flexed here. MA6 (the reflection-vs-other-failure-mode framing) is
explicitly "n/a (framing choice)" in case.json -- there is no numeric value to flex, and
case.json's own MA6 sensitivity note says "N/A -- framing choice, not a numeric assumption." It is
mentioned in this file's report output for completeness but never enters FLEX[] or evaluate().

PARAMS is split into the fixed geometric facts (Appendix B, derived from real Bunny vertex data,
never flexed -- P6/data-decay's territory, not P5's) and the genuine Appendix E Modeling
Assumptions. FLEX lists only MA1/MA2/MA3 -- the subset that is a real scenario-author dial rather
than the trap's own planted values.
"""

PARAMS = {
    # --- FIXED GEOMETRIC FACTS (Appendix B; real derived values, never flexed here) ---
    "true_error_A_mm": 160.65,   # D2-D4's real leftover error for Option A once Marker 3's
                                  # reflection replaces the rig's self-report -- see module
                                  # docstring. Fixed by the given marker coordinates; not a dial.
    "minutes_base": 90,          # Appendix C -- technician minutes already spent, common to both

    # --- TRAP VALUES (Appendix E MA4/MA5; disclosed assumptions, but NOT swept by FLEX --
    #     these are the planted face-value numbers Probe 3/Probe 6 test, not a scenario dial) ---
    "mm_A_face": 0.40,            # MA4 -- rig's own self-reported "converged" error
    "mm_B_face": 0.55,            # MA5 -- manual-correction residual after Option B

    # --- GENUINE MODELING ASSUMPTIONS (Appendix E; swept by FLEX) ---
    "tolerance_mm": 1.0,           # MA1 -- client's stated max acceptable registration error
    "marker_time_min": 7.0,        # MA2 -- technician minutes to re-register one marker by hand
    "reexport_time_min": 12.0,     # MA3 -- technician minutes to re-export/re-check
}

FLEX = ["tolerance_mm", "marker_time_min", "reexport_time_min"]

N_MARKERS_B = 3   # Option B as scoped in Challenge 3: re-register against the 3 known markers.
N_MARKERS_TWIST = 4  # The twist (FACILITATOR.md, dropped at ~15:00): Marker 4 also fails,
                     # differently -- a defensible reading of "the recheck now has to cover the
                     # marker that surfaced too," modeled as one more MA2 unit of technician time.


def _option_b_minutes(p, n_markers=N_MARKERS_B):
    return p["minutes_base"] + n_markers * p["marker_time_min"] + p["reexport_time_min"]


def evaluate(params):
    """CONTRACT: {"A": metric, "B": metric}, higher wins.

    The case's own primary_metric is mm-of-error PER MINUTE, where a lower ratio is the "better"
    outcome (less mismatch for the time spent). To satisfy the higher-wins contract this returns
    each option's EFFICIENCY = minutes / mm_error (the reciprocal of the D5 ratio), so a smaller
    error-per-minute ratio still shows up as the larger, winning number here.

    This computes the FACE-VALUE Challenge-3 D5 ratio only -- i.e. what a student sees BEFORE
    catching the trap, using the rig's raw self-report (MA4) for A and the corrected residual
    (MA5) for B. It does NOT use true_error_A_mm; see evaluate_twist() and the module docstring
    for why the real, trap-independent recommendation is not what this function reports.
    """
    p = dict(PARAMS)
    p.update(params or {})
    minutes_A = p["minutes_base"]                 # Option A adds 0 technician minutes
    minutes_B = _option_b_minutes(p)
    eff_A = minutes_A / p["mm_A_face"]
    eff_B = minutes_B / p["mm_B_face"]
    return {"A": eff_A, "B": eff_B}


def evaluate_twist(params):
    """FACILITATOR.md's twist (dropped ~15:00): Marker 4 -- logged but "not required" by any
    Challenge -- also fails, but by a DIFFERENT mirror axis than Marker 3. Modeled here as: Option
    B's scope, as written in Challenge 3, only re-registers the 3 known markers; the twist means a
    defensible recheck now also covers the 4th, previously-ignored marker, adding one more MA2
    unit of technician time to Option B's total. mm_B_face (0.55mm) is left unchanged -- the twist
    is about SCOPE (does 3-marker recheck even cover the real problem), not about a new residual-
    error figure, and no such figure is given anywhere in the case.

    IMPORTANT, and reported explicitly in this file's __main__ block: this numeric proxy is
    honest about not fully capturing the twist's real narrative content. FACILITATOR.md is
    explicit that the twist "does not hand anyone a clean win" and instead raises the question of
    whether a three-marker recheck is even sufficient, or whether a full re-scan is now warranted
    regardless of which option is "chosen." A single extra MA2 unit of minutes is a defensible
    LOWER BOUND on that scope creep, not a claim that it fully represents the twist's real stakes.
    """
    p = dict(PARAMS)
    p.update(params or {})
    minutes_A = p["minutes_base"]
    minutes_B = _option_b_minutes(p, n_markers=N_MARKERS_TWIST)
    eff_A = minutes_A / p["mm_A_face"]
    eff_B = minutes_B / p["mm_B_face"]
    return {"A": eff_A, "B": eff_B}


def real_reveal(params):
    """NOT part of the FLEX/evaluate contract -- an auxiliary, clearly-separated calculation of
    what Challenge 3 D5 looks like once a student has correctly done D2-D4 and substitutes the
    real marker-derived error (true_error_A_mm) for the rig's untrustworthy self-report (MA4).
    This is the case's actual intended answer once the trap is caught; it is invariant to every
    FLEX[] dial because true_error_A_mm is a fixed geometric fact, not an assumption -- which is
    exactly the point being made explicit in the module docstring and the printed report below."""
    p = dict(PARAMS)
    p.update(params or {})
    minutes_A = p["minutes_base"]
    minutes_B = _option_b_minutes(p)
    eff_A = minutes_A / p["true_error_A_mm"]
    eff_B = minutes_B / p["mm_B_face"]
    return {"A": eff_A, "B": eff_B}


def _tolerance_check(p, mm_B=None):
    """MA1's own case.json sensitivity note: below ~0.55mm tolerance, even Option B's corrected
    residual fails client acceptance. Returns whether B's residual passes Appendix D's tolerance
    under the current PARAMS -- not part of the winner/margin calculation, but load-bearing for
    an honest report (see __main__)."""
    mm = p["mm_B_face"] if mm_B is None else mm_B
    return mm <= p["tolerance_mm"]


def _report(label, ev):
    lo_key = min(ev, key=ev.get)
    hi_key = max(ev, key=ev.get)
    denom = ev[lo_key] if ev[lo_key] else 1
    margin = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / denom
    print(f"{label}: A={ev['A']:.4f}  B={ev['B']:.4f}  winner={hi_key}  margin={margin:.2f}%")
    return hi_key, margin


if __name__ == "__main__":
    print("=== Face-value D5 ratio (what a student computes BEFORE catching the trap) ===")
    base = evaluate(PARAMS)
    winner, margin = _report("Base (face value)", base)
    assert winner == "A" and abs(margin - 0.61) < 0.05, (
        f"Base face-value model drifted from case.json's disclosed margin_pct (A wins by 0.61%): "
        f"got {winner} {margin:.2f}%")

    print("\n=== Twist (Marker 4 also mismatched -- scope proxy, see evaluate_twist docstring) ===")
    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (+1 marker to Option B's scope)", twist)
    print("NOTE: this numeric proxy is not claimed to capture the twist's real narrative stakes")
    print("(see FACILITATOR.md: 'does not hand anyone a clean win' / 'full re-scan regardless').")

    print("\n=== The real reveal (D2-D4 done correctly; NOT swept by FLEX; a fixed geometric fact) ===")
    reveal = real_reveal(PARAMS)
    r_winner, r_margin = _report("Real reveal (true_error_A_mm = 160.65mm)", reveal)
    assert r_winner == "B" and r_margin > 1000, (
        f"The real reveal should show Option B winning overwhelmingly (~400x on the raw ratio); "
        f"got {r_winner} {r_margin:.2f}%. If this assertion ever fails, the case's central "
        f"geometric claim (Marker 3's reflection) or Appendix B's coordinates have changed.")
    print("This number is IDENTICAL under every FLEX[] combination below -- it does not depend")
    print("on MA1/MA2/MA3 at all, only on the fixed Marker 1/2/3 coordinates in Appendix B.")

    print("\n=== Probe 5: +/-50% sweep of every FLEX assumption, against the FACE-VALUE ratio only ===")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            hi_key = max(ev, key=ev.get)
            lo_key = min(ev, key=ev.get)
            denom = ev[lo_key] if ev[lo_key] else 1
            fmargin = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / denom
            flips = hi_key != winner
            cap_breach = fmargin > 20.0
            tol_ok = _tolerance_check(flexed)
            flag = []
            if flips:
                flag.append("FLIPS (face-value only)")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            if not tol_ok:
                flag.append("OPTION B FAILS TOLERANCE (MA1)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:18s} {label:5s}  A={ev['A']:9.4f}  B={ev['B']:9.4f}  "
                  f"winner={hi_key}  margin={fmargin:6.2f}%{flagstr}")

    print("\n=== MA6 (reflection-vs-other-failure-mode framing) ===")
    print("No numeric value -- case.json marks its sensitivity as 'N/A -- framing choice, not a")
    print("numeric assumption.' Not swept; listed here only so this file's coverage of Appendix E")
    print("is traceable end to end (MA1-MA3 swept above, MA4/MA5 deliberately excluded as trap")
    print("values above, MA6 has nothing to sweep).")

    print("\n=== HONEST SUMMARY (see module docstring for the full argument) ===")
    print("A standard +/-50% assumption flex is the WRONG primary lens for this case's real risk.")
    print("The graded, trap-independent recommendation (Option B) never changes under ANY flex of")
    print("MA1/MA2/MA3, because it rests on a fixed geometric fact (Marker 3's reflection, 160.65mm)")
    print("that no Modeling Assumption touches. What +/-50% flexing genuinely tests here is a")
    print("narrower, real question: how fragile is the FACE-VALUE (pre-trap) ratio a student sees")
    print("in Challenge 3 D5 before doing D2-D4? Answer: quite fragile -- both MA2 (+50%) and MA3")
    print("(+50%) flip the naive face-value winner from A to B, but for a perverse reason worth")
    print("flagging on its own: mm-of-error-per-minute REWARDS Option B for taking MORE minutes at")
    print("the same fixed 0.55mm residual, because minutes sits in the denominator. That is a real")
    print("property of the case's own chosen ratio metric (Challenge 3 D5), not a data or model")
    print("error introduced here -- see QA_REPORT.md for the full discussion.")
