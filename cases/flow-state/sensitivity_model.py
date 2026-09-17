"""Sensitivity model for FlowState (SPEC section 2 balance test, case-readiness Tier 2 probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py, templates/
INTERACTIVE_HTML_CONTRACT.md section 2) -- exactly these public names:

    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

Every dollar figure, CPM/CPC, segment split, and funnel rate below is taken directly from
case.md Appendix A/B/C/D/E -- nothing here is invented for this file. Verified by hand against
FACILITATOR.md's per-channel table (2026-09-11): base evaluate(PARAMS) reproduces every one of
the ten channel-by-plan subscriber cells (e.g. Plan A TV-Sports = 137.24, Plan A SEO = 48.64,
Plan B SEO = 158.09) to the same two decimal places FACILITATOR.md prints, and the plan totals
(329.83 / 286.50) and margin (15.1%) match case.json's balance object exactly.

PARAMS is split into SOURCED (case.md Appendix A/D/F, a citation id in the comment) and ASSUMED
(case.md Appendix E, Modeling Assumptions, an MA id in the comment). FLEX lists only the ASSUMED
subset -- per case-readiness's rule, cited measurements (the SEO CPC/CVR, the print CPM, the
non-SEO trial-conversion rate, the two adoption-rate VALUES) are stress-tested by probe 6 (data
decay), not probe 5. The print channel's awareness/interest rate is a case-author reference
value used ONLY for this sensitivity baseline and disclosed as such in FACILITATOR.md -- the
case deliberately leaves the real value for the student to assume and justify (Challenge 3, D1),
so this file's print_awareness/print_interest are themselves flexed like any other assumption,
not treated as fixed.
"""

PARAMS = {
    # --- SOURCED (not flexed by default) ---
    "seo_cpc_usd": 5.00,          # Appendix A [S1] -- SEO cost per click
    "seo_trial_conv": 0.068,      # Appendix D [S1] -- SEO's own, higher, interested->trial rate
    "nonseo_trial_conv": 0.0117,  # Appendix D [S6] -- median DTC site conversion rate, all non-SEO channels
    "print_cpm_usd": 63.00,       # Appendix A [S4] -- 100,000-circulation magazine CPM
    "adoption_seg1": 0.358,       # Appendix D [S7] -- Followers tier, trial->paid
    "adoption_seg2": 0.520,       # Appendix D [S7] -- Average tier, trial->paid

    # --- ASSUMED (case.md Appendix E, Modeling Assumptions) ---
    "budget_usd": 60000.0,        # MA1 -- total fixed launch advertising budget
    "tv_sports_cpm": 14.00,       # MA2
    "tv_general_cpm": 30.00,      # MA3
    "radio_cpm": 10.00,           # MA4
    "tv_awareness": 0.22,         # MA6
    "radio_awareness": 0.12,      # MA7
    "tv_interest": 0.10,          # MA8 (TV)
    "radio_interest": 0.08,       # MA8 (radio)
    "print_awareness": 0.15,      # reference value for this model only -- case leaves this for the
                                   # student to assume/justify (Challenge 3, D1); FACILITATOR.md's
                                   # own calibration table uses this same 15%/12% pair
    "print_interest": 0.12,
}

FLEX = ["budget_usd", "tv_sports_cpm", "tv_general_cpm", "radio_cpm",
        "tv_awareness", "radio_awareness", "tv_interest", "radio_interest",
        "print_awareness", "print_interest"]

# Appendix C -- fixed dollar splits, both plans spend the entire budget. Expressed as a SHARE of
# the total budget so that flexing budget_usd (MA1) scales every channel's dollars together, the
# same way the case's own "the case's numbers scale with this figure" sensitivity note describes.
PLAN_SHARES = {
    "A": {"tv_sports": 18000 / 60000, "tv_general": 18000 / 60000, "radio": 12000 / 60000,
          "seo": 8000 / 60000, "print": 4000 / 60000},
    "B": {"tv_sports": 6000 / 60000, "tv_general": 6000 / 60000, "radio": 6000 / 60000,
          "seo": 26000 / 60000, "print": 16000 / 60000},
}

# Appendix D -- channel segment splits (Segment 1 share, Segment 2 share). Fixed structural data,
# not swept by probe 5 (MA5 is disclosed as "highly sensitive" in prose, but it is a paired split
# per channel, not a single scalar dial -- see this file's own module docstring / QA_REPORT.md for
# why it is documented rather than mechanically flexed).
SEGMENT_SPLIT = {
    "tv_sports": (0.65, 0.35),
    "tv_general": (0.30, 0.70),
    "radio": (0.25, 0.75),
    "print": (0.20, 0.80),
    "seo": (0.45, 0.55),
}


def _channel_subscribers(dollars, cpm_or_cpc, is_cpc, awareness, interest, trial_conv,
                          seg_split, p):
    """One channel's projected paying subscribers, chained exactly as case.md Appendix D/
    Challenge 3 (D1) describes: reach x segment share x awareness x interest x trial-conversion
    x adoption, summed across both segments."""
    reach = (dollars / cpm_or_cpc) if is_cpc else (dollars / cpm_or_cpc * 1000.0)
    seg1_share, seg2_share = seg_split
    seg1_subs = reach * seg1_share * awareness * interest * trial_conv * p["adoption_seg1"]
    seg2_subs = reach * seg2_share * awareness * interest * trial_conv * p["adoption_seg2"]
    return seg1_subs + seg2_subs


def plan_breakdown(plan, p):
    """Per-channel subscriber counts for one plan, plus the plan total. `plan` is 'A' or 'B'."""
    shares = PLAN_SHARES[plan]
    budget = p["budget_usd"]

    tv_sports = _channel_subscribers(
        budget * shares["tv_sports"], p["tv_sports_cpm"], False,
        p["tv_awareness"], p["tv_interest"], p["nonseo_trial_conv"],
        SEGMENT_SPLIT["tv_sports"], p)
    tv_general = _channel_subscribers(
        budget * shares["tv_general"], p["tv_general_cpm"], False,
        p["tv_awareness"], p["tv_interest"], p["nonseo_trial_conv"],
        SEGMENT_SPLIT["tv_general"], p)
    radio = _channel_subscribers(
        budget * shares["radio"], p["radio_cpm"], False,
        p["radio_awareness"], p["radio_interest"], p["nonseo_trial_conv"],
        SEGMENT_SPLIT["radio"], p)
    seo = _channel_subscribers(
        budget * shares["seo"], p["seo_cpc_usd"], True,
        1.0, 1.0, p["seo_trial_conv"],
        SEGMENT_SPLIT["seo"], p)
    print_ = _channel_subscribers(
        budget * shares["print"], p["print_cpm_usd"], False,
        p["print_awareness"], p["print_interest"], p["nonseo_trial_conv"],
        SEGMENT_SPLIT["print"], p)

    total = tv_sports + tv_general + radio + seo + print_
    return {"tv_sports": tv_sports, "tv_general": tv_general, "radio": radio,
            "seo": seo, "print": print_, "total": total}


def evaluate(params):
    """CONTRACT: {"A": metric, "B": metric}, higher wins."""
    p = dict(PARAMS)
    p.update(params or {})
    a = plan_breakdown("A", p)
    b = plan_breakdown("B", p)
    return {"A": a["total"], "B": b["total"]}


def evaluate_twist(params):
    """FACILITATOR.md's twist: a seasonal TV-rate premium raises both TV packages' CPM by ~50%
    (trade-show week overlapping championship-season live-sports inventory)."""
    p = dict(PARAMS)
    p.update(params or {})
    p["tv_sports_cpm"] = p["tv_sports_cpm"] * 1.5
    p["tv_general_cpm"] = p["tv_general_cpm"] * 1.5
    return evaluate(p)


def _report(label, ev):
    lo_key = min(ev, key=ev.get)
    hi_key = max(ev, key=ev.get)
    margin = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
    print(f"{label}: A={ev['A']:.2f}  B={ev['B']:.2f}  winner={hi_key}  margin={margin:.2f}%")
    return hi_key, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base", base)
    assert winner == "A" and abs(margin - 15.1) < 0.1, \
        f"Base model drifted from case.json's disclosed base (A wins by 15.1%): got {winner} {margin:.2f}%"
    assert abs(base["A"] - 329.83) < 0.05 and abs(base["B"] - 286.50) < 0.05, \
        f"Base totals drifted from case.json/FACILITATOR.md: A={base['A']:.2f} B={base['B']:.2f}"

    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (+50% TV CPM)", twist)
    assert t_winner == "B", f"Twist should flip to B per FACILITATOR.md; got {t_winner}"

    print("\n--- Probe 5: +/-50% sweep of every FLEX assumption ---")
    for key in FLEX:
        base_val = PARAMS[key]
        for pct, label in ((0.5, "+50%"), (-0.5, "-50%")):
            flexed = dict(PARAMS)
            flexed[key] = base_val * (1 + pct)
            ev = evaluate(flexed)
            hi_key = max(ev, key=ev.get)
            lo_key = min(ev, key=ev.get)
            margin = 0.0 if ev[lo_key] == 0 else 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
            flips = hi_key != winner
            cap_breach = margin > 20.0
            flag = []
            if flips:
                flag.append("FLIPS")
            if cap_breach:
                flag.append("CAP-BREACH(>20%)")
            flagstr = (" <-- " + ", ".join(flag)) if flag else ""
            print(f"  {key:16s} {label:5s}  A={ev['A']:8.2f}  B={ev['B']:8.2f}  "
                  f"winner={hi_key}  margin={margin:5.2f}%{flagstr}")
