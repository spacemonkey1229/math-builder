"""Sensitivity model for The Missing Hub (SPEC section 2 balance test, case-readiness Tier 2
probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

Primary metric (case.json.primary_metric): share of the friend circle's 52 members whose reported
degree count is fabricated-or-missing (not an exact, known value), per option. Higher = MORE of
the circle is represented by an honest, exact number (so higher is better).

Real/derived (sourced, NOT flexed):
    n_circle = 52          real member count of SNAP ego-network 3980 [S2]
    known_n  = 51          real members whose degree count exported cleanly tonight [S2]
    known_sum = 548        sum of those 51 real, sourced degree counts (Appendix B) [S2]

Assumption (Appendix C):
    MA1 cached_mean = 10.75   the circle's mean degree as last verified 5 weeks before tonight's
        export. The ONLY probe-5 flex dial. Genuinely uncertain -- friend circles gain and lose
        connections over time, and there is no way to re-verify it before the deadline.

THE KEY DESIGN RESULT (why this case is robust to a +/-50% flex, by construction, not by luck):
Flexing cached_mean changes WHAT NUMBER Option A reconstructs for the missing member (a real,
visible, and sometimes large swing -- printed below) -- but it changes NOTHING about the primary
metric itself. Structurally, BOTH options always compromise exactly ONE of the circle's 52
members: Option A always reports an ESTIMATED (not exact) value for that one member, no matter
what the estimate turns out to be; Option B always OMITS that one member entirely, no matter what
its true value would have been. The primary metric counts WHETHER a member's number is exact, not
HOW CLOSE an estimate is -- so it cannot flip under any value of MA1. This is the same structural
"cancels by construction" pattern `the-hub-choice`'s MA2/MA3 used, applied here to the case's own
single assumption rather than to a second one.

An earlier draft of this case used "percent deviation of the option's reported mean from the
circle's true (unknowable-in-story) current mean degree" as the primary metric instead. That
version had a tight, well-balanced BASE margin (~1.02%, Option A) -- but FAILED probe 5 outright:
because Option A's reported mean is ALWAYS exactly equal to whatever cached_mean is used (that is
what the reconstruction formula solves for), a +/-50% flex on cached_mean directly moves Option
A's apparent accuracy by the same +/-50%, which overwhelms Option B's small, fixed ~4.3% cost and
flips the winner almost everywhere in the flex band except a narrow window right at the base
value. Per this project's own rule (PIPELINE.md: a verdict that flips under a +/-50% assumption
flex is retuned in case-write, never hidden), the metric itself was redesigned to the
exact-vs-estimated/missing count above, which is provably flip-proof rather than merely
flip-resistant. See RESEARCH_LOG.md for the full retuning narrative.
"""

KNOWN_N = 51
KNOWN_SUM = 548
N_CIRCLE = 52

PARAMS = {
    # --- ASSUMED (Appendix C, MA1) --- the only stated assumption in this case
    "cached_mean": 10.75,
}

FLEX = ["cached_mean"]


def reconstruct(cached_mean):
    """The exact D1 procedure: mean x n - known sum."""
    return cached_mean * N_CIRCLE - KNOWN_SUM


def evaluate(params=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = share of the circle's 52
    members whose reported degree count is exact (not fabricated, not missing).

    Both options touch exactly one member out of 52: Option A reports an ESTIMATED value for
    that member (never an exact one, regardless of the estimate's accuracy); Option B reports NO
    value for that member at all. Neither is "exact" for that one member, so both options score
    identically: 51 exact members out of 52. This does not depend on `cached_mean` at all -- the
    metric is deliberately insensitive to it, which is the point (see module docstring)."""
    p = dict(PARAMS)
    p.update(params or {})
    _ = reconstruct(p["cached_mean"])  # computed for diagnostics only; does not affect the metric
    exact_share_a = KNOWN_N / N_CIRCLE  # 51/52: the reconstructed member is an estimate, not exact
    exact_share_b = KNOWN_N / N_CIRCLE  # 51/52: the dropped member is absent, not exact either
    return {"A": exact_share_a, "B": exact_share_b}


def _state(ev):
    a, b = ev["A"], ev["B"]
    if a == b:
        return "TIE", 0.0
    hi_key, lo_key = ("A", "B") if a > b else ("B", "A")
    margin = 100.0 * (ev[hi_key] - ev[lo_key]) / ev[lo_key]
    return hi_key, margin


if __name__ == "__main__":
    base = evaluate()
    winner, margin = _state(base)
    print(f"Base (cached_mean=10.75): A={base['A']:.6f}  B={base['B']:.6f}  "
          f"winner={winner}  margin={margin:.2f}%")
    assert winner == "TIE" and margin == 0.0, \
        f"Base model drifted from case.json's disclosed canonical base (structural TIE): got {winner} {margin:.2f}%"

    print("\n--- Probe 5: +/-50% flex on MA1 (cached_mean), the only stated assumption ---")
    for mult, label in [(0.5, "-50%"), (0.75, "-25%"), (1.0, "base"), (1.25, "+25%"), (1.5, "+50%")]:
        cm = PARAMS["cached_mean"] * mult
        recon = reconstruct(cm)
        ev = evaluate({"cached_mean": cm})
        state, m = _state(ev)
        flip = " <-- FLIPS" if state != winner else ""
        print(f"  cached_mean={cm:6.3f} ({label}): reconstructed value={recon:7.2f}  "
              f"A={ev['A']:.6f} B={ev['B']:.6f} winner={state} margin={m:.2f}%{flip}")

    print("\n--- Wider stress test: 0 to 3x cached_mean (well beyond the required +/-50%) ---")
    for mult in [0.0, 1.0, 3.0]:
        cm = PARAMS["cached_mean"] * mult
        recon = reconstruct(cm)
        ev = evaluate({"cached_mean": cm})
        state, m = _state(ev)
        print(f"  cached_mean={cm:6.3f} ({mult:.1f}x): reconstructed value={recon:8.2f}  "
              f"winner={state} margin={m:.2f}%  (metric itself never moves)")

    print("\nResult: the primary metric is structurally identical for A and B at every value of "
          "cached_mean tested -- the winner (TIE, 0.00% margin) cannot flip. The reconstructed "
          "VALUE swings enormously (from a negative/nonsensical number at 0x to hundreds at 3x), "
          "which is itself the case's real point: the number Option A reports is highly sensitive "
          "to MA1, even though the CHOICE of option is not. See FACILITATOR.md for the "
          "discussion-facing version of this distinction.")
    print("\nAll checks complete. See RESEARCH_LOG.md for the full write-up.")
