#!/usr/bin/env python3
"""
Sensitivity model -- The Clampband Margin.

Tier 2 probe 5 ("flex each stated assumption by +/-50%; report which flips the
verdict") needs a runnable model of the case's own arithmetic. See
skills/case-readiness/scripts/example_sensitivity_model.py for the contract
and worked reference (Cold Chain), and cases/bioreactor-bid/sensitivity_model.py
for a second worked example of the feasibility-gated metric pattern used here.

CONTRACT:
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]           the subset flexed by default
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better

THE REAL DILEMMA, ENCODED HONESTLY (not the raw n=3 ratio):
`case.json.balance.margin_pct` (9.6%) is the percent difference between the two
stack-up methods' predicted tolerance AT n=3 ONLY. That is NOT what actually
decides the case -- per FACILITATOR.md's own "winning_option" note, the case is
built so that a Hero who stops at n=3 sees a false tie ("both methods pass, so
it doesn't matter") and misses the real dilemma: whether each method clears
BOTH of NASA-adjacent industry's margin thresholds (Appendix B: gapping >= 1.25,
release-element >= 2.00) across the FULL modeled supplier-count range Wes's
sign-off is actually setting policy for (n = 3, 6, 7, 10 -- Appendix D / MA1).

So `evaluate()` mirrors the case's real recommendation logic, not the raw n=3
ratio: an option that fails EITHER threshold at ANY modeled n is disqualified
(scored 0), exactly the way the case's own balance note disqualifies the
Worst-Case Stack ("Option A fails the release-element margin starting at n=7").
A surviving option's score is its worst (minimum) margin across the modeled
range -- a durability score, higher is better among options that survive at
all. `raw_ratio_n3()` is kept separately to reproduce the case's stated 9.6%
margin_pct figure for verification -- it is NOT what evaluate() uses.

Fixed (not in FLEX[]): the future supplier counts themselves (MA1: n=6,7,10)
and the specific real per-interface tolerances at n=3 are structural/cited
(Appendix C, S3/S4) rather than the two dials this QA pass was specifically
asked to stress: the x1.5 Bender/Motorola correction factor (S6) itself, and
the underlying ISO 2768/Protolabs tolerance base values (S3/S4). MA4's 0.070in
gapping allowance is included in FLEX too since case.md/FACILITATOR.md both
call it "the single most load-bearing assumption in the case" -- leaving it
out of a sensitivity sweep of load-bearing assumptions would be the same
under-scoping mistake SPEC Sec2 warns against.

Verified against case.md / FACILITATOR.md (2026-08-31 QA pass):
    base    A (Worst-Case) = 0.0 (disqualified: fails release-element margin at n=7, n=10)
            B (Modified RSS) = 2.638... (clears both thresholds at every modeled n; its
            worst/minimum margin, at n=10, is the reported score)
    raw n=3 ratio only (case.json.balance.margin_pct): 9.55% ~= 9.6%, A's raw tolerance
            bigger than B's -- but this ratio is NOT the quantity that decides the case.
"""
import math

# --- the four modeled supplier counts (Appendix D / MA1) -- structural, not a
#     "dial" a Hero could flex; changing these changes WHICH n's are sampled,
#     not the two things this QA pass was asked to stress-test.
MODELED_NS = (3, 6, 7, 10)

PARAMS = {
    # --- Appendix C / S3, S4: this build's three real, cited per-interface
    #     tolerances (inches), used directly at n=3 and averaged for n>3 (MA2).
    "tol_flange_in": 0.0079,      # Supplier B, ISO 2768-1 class f [S3]
    "tol_ring_in": 0.0050,        # Supplier A, Protolabs CNC [S4]
    "tol_boltshim_in": 0.0039,    # Supplier C, ISO 2768-1 class f [S3]
    # --- Appendix D / Appendix F S6: the x1.5 Bender/Motorola correction
    #     factor applied to RSS. THIS is the number this QA pass was asked to
    #     stress-test directly.
    "correction_factor": 1.5,
    # --- Appendix E, MA4: the nominal per-joint gapping allowance that
    #     bridges Appendix B's dimensionless margin factors (1.25, 2.00) to
    #     Appendix C/D's dimensional tolerance-stack values. Both case.md and
    #     FACILITATOR.md call this the single most load-bearing assumption in
    #     the case.
    "gapping_allowance_in": 0.070,
    # --- Appendix B / S2: the two NASA-adjacent industry margin thresholds a
    #     stack-up method's margin (allowance / predicted tolerance) must
    #     clear. Real, cited numbers (not modeling assumptions) -- included as
    #     PARAMS so the model is fully self-contained, but NOT flexed by
    #     default (not in FLEX[]): flexing a cited pass/fail bar is a
    #     different question ("what if the standard were different") than
    #     flexing the case's own stated modeling choices.
    "gapping_threshold": 1.25,
    "release_threshold": 2.00,
}

# Probe 5's DEFAULT sweep (its doctrinal scope, per SPEC Sec2 and
# example_sensitivity_model.py's own contract) is stated MODELING ASSUMPTIONS
# only -- MA4 (gapping_allowance_in) is the one dial in this case's own
# modeling_assumptions[] that is a genuinely authorial scenario convention,
# not cited/sourced data. correction_factor (S6) and the three tol_*_in
# dials (S3/S4) are real, cited, HIGH/MEDIUM-confidence measured figures --
# per tier2_probes.py's own doctrine note, sweeping cited data in the default
# FLEX[] and reporting any resulting instability as an undisclosed-assumption
# finding would be a scoping error in the model, not a real case defect
# (cited-data robustness is P6 data-decay's job, not P5's).
#
# This QA pass (2026-08-31) was SPECIFICALLY asked to stress-test the x1.5
# correction factor and the underlying tolerance base values too, despite
# them being cited data -- run this module directly (`python3
# sensitivity_model.py`), or `tier2_probes.py --case the-clampband-margin
# --probe 5 --flex-all`, to sweep ALL of PARAMS (adds correction_factor and
# the three tol_*_in dials to the default MA4-only sweep) and see that
# specific, explicitly-requested result reported separately from the
# doctrinal P5 pass/fail gate.
FLEX = [
    "gapping_allowance_in",  # MA4 -- the case's own most load-bearing assumption
]


def _T_WC(n, t1, t2, t3):
    """Worst-Case Stack: direct sum. At n=3, the three real interfaces
    (Appendix C). Beyond n=3, MA2's rule: every added interface uses the
    average of the three real tolerances (case.md Appendix D/E)."""
    avg = (t1 + t2 + t3) / 3.0
    return (t1 + t2 + t3) if n == 3 else n * avg


def _T_MRSS(n, t1, t2, t3, corr):
    """Modified RSS Stack: 1.5x RSS. At n=3, RSS of the three real,
    non-identical interfaces (matches case.md's 0.0152in exactly -- using
    the average instead would under-count, since RSS of unequal values
    exceeds RSS of three copies of their mean). Beyond n=3, MA2's averaging
    rule: RSS of n copies of the average tolerance."""
    avg = (t1 + t2 + t3) / 3.0
    if n == 3:
        return corr * math.sqrt(t1 ** 2 + t2 ** 2 + t3 ** 2)
    return corr * avg * math.sqrt(n)


def _durability_score(p, T_fn, *T_args):
    """The case's real recommendation logic (FACILITATOR.md 'winning_option'):
    an option that fails EITHER of Appendix B's thresholds at ANY modeled n is
    disqualified (score 0). A surviving option's score is its worst (minimum)
    margin across the modeled range -- how much room it has left in its worst
    case, not just at n=3."""
    margins = []
    for n in MODELED_NS:
        T = T_fn(n, *T_args)
        margin = p["gapping_allowance_in"] / T if T else float("inf")
        if margin < p["gapping_threshold"] or margin < p["release_threshold"]:
            return 0.0
        margins.append(margin)
    return min(margins)


def evaluate(params):
    p = dict(PARAMS)
    p.update(params or {})
    t1, t2, t3 = p["tol_flange_in"], p["tol_ring_in"], p["tol_boltshim_in"]

    a = _durability_score(p, _T_WC, t1, t2, t3)
    b = _durability_score(p, _T_MRSS, t1, t2, t3, p["correction_factor"])
    return {"A": a, "B": b}


def raw_ratio_n3(params=None):
    """NOT part of the Tier 2 contract -- reproduces case.json.balance.margin_pct
    (9.6%), the raw percent difference between the two methods' predicted
    tolerance AT n=3 ONLY. Kept for verification; evaluate() above is what
    Probe 5 actually runs, because the n=3-only ratio is not what decides the
    case (see module docstring)."""
    p = dict(PARAMS)
    p.update(params or {})
    t1, t2, t3 = p["tol_flange_in"], p["tol_ring_in"], p["tol_boltshim_in"]
    wc3 = _T_WC(3, t1, t2, t3)
    mrss3 = _T_MRSS(3, t1, t2, t3, p["correction_factor"])
    return 100.0 * (wc3 - mrss3) / wc3


if __name__ == '__main__':
    base = evaluate({})
    print("base (feasibility-gated, worst-case-across-n)", {k: round(v, 4) for k, v in base.items()})
    print("raw n=3 ratio (margin_pct check) = %.2f%%" % raw_ratio_n3({}))

    print("\n--- direct check: does the case's real winner survive the two flex dials this ---")
    print("--- QA pass was specifically asked about? ---")
    for name, lo_mult, hi_mult in (("correction_factor", 0.5, 1.5),):
        base_val = PARAMS[name]
        for label, mult in (("-50%", lo_mult), ("+50%", hi_mult)):
            r = evaluate({name: base_val * mult})
            print(f"{name} {label} (-> {base_val*mult:.4f}):", {k: round(v, 4) for k, v in r.items()})
    for name in ("tol_flange_in", "tol_ring_in", "tol_boltshim_in"):
        base_val = PARAMS[name]
        for label, mult in (("-50%", 0.5), ("+50%", 1.5)):
            r = evaluate({name: base_val * mult})
            print(f"{name} {label} (-> {base_val*mult:.5f}):", {k: round(v, 4) for k, v in r.items()})
