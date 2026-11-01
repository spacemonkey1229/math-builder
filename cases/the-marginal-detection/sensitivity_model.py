"""
sensitivity_model.py -- The Marginal Detection

Graded primary metric (case.json.primary_metric): transit-dip significance ratio,
computed two ways from the same Appendix A dataset -- against a line-of-best-fit's
residual standard deviation (the "naive" read, sig_naive) and against the
box-and-whisker distribution's 0.7413xIQR spread (the "robust" read, sig_robust) --
each compared to the survey's own 3.0 follow-up threshold (MA2).

Modeling choice for this script's evaluate() contract (skills/case-readiness/SKILL.md's
P5 spec: evaluate(params) -> {"A": metric, "B": metric}, higher wins): this case's two
"options" are not independently priced the way a dollar-cost case's A/B are -- they are
two competing METHODS of reading the same 20 numbers. sig_naive is treated as "A"'s
reading (the method favoring re-observation, since it is the more commonly taught tool
and the one Argument A leans on) and sig_robust is treated as "B"'s reading (the method
favoring abandonment, the one Argument B leans on). Higher score wins, so this asks: on
the strength of a blind trust in whichever method reports the LARGER number, has the
candidate been shown significant enough to justify the slot? Margin follows the
corpus-standard winner-minus-loser-over-loser convention.

The underlying data-generation logic (Appendix A's 20-point light curve: a quadratic,
non-linear systematic drift plus Gaussian noise, with a real transit-like decrement
added at t=8..11) is reproduced below so PARAMS' two Modeling Assumptions -- the dip
depth (MA1) and the follow-up threshold (MA2) -- can be flexed honestly and the whole
light curve, line fit, and box-and-whisker statistics recomputed from scratch at each
flexed value, not just rescaled after the fact.

Verified against case.json.balance / FACILITATOR.md's margin arithmetic:
    base   sig_naive = 3.006 (A, winner)  ·  sig_robust = 2.521 (B)  ·  margin 19.2%
"""
import random

PARAMS = {
    # --- Appendix A, Modeling Assumption MA1 -- the real astrophysical dip added on
    #     top of the night's systematic drift, at time steps 8-11. Not published
    #     anywhere (this is a constructed scenario) -- see RESEARCH_LOG.md.
    "transit_dip_ppm": 160.0,
    # --- Appendix B, Modeling Assumption MA2 -- the Sable Peak Survey's own
    #     internal "worth a follow-up slot" significance threshold. Not published
    #     anywhere; set well below Kepler's real, sourced 7.1-sigma discovery bar [S2].
    "followup_threshold_sigma": 3.0,
    # --- Fixed scenario construction parameters (not flexed -- these set the shape
    #     of the systematic drift and noise, bounded by TESS's real photometric
    #     precision [S1], not the load-bearing decision dials themselves).
    "drift_amplitude": 1.6,     # ppm per (time-step)^2, quadratic drift curvature
    "drift_offset": -60.0,      # ppm, drift's vertex offset
    "noise_sd_ppm": 55.0,       # ppm, per-point Gaussian noise, within TESS's bound [S1]
    "random_seed": 21,
}

# Only the genuine Modeling Assumptions that this evaluate() contract can actually
# test are swept. transit_dip_ppm (MA1) changes both sig_naive and sig_robust in
# tandem (it feeds _generate_light_curve directly) and can flip which method reads
# higher -- a real, mechanically testable flex. followup_threshold_sigma (MA2) is
# NOT swept here: evaluate()'s A/B scores are the two significance READINGS
# themselves (sig_naive vs sig_robust), not a comparison against the threshold, so
# flexing the threshold has no effect on this particular win/lose test by
# construction -- exactly the same "held fixed, not a dial to flex" situation as
# cases/the-approval-gate/sensitivity_model.py's MA2 (its two gate thresholds).
# MA2's real sensitivity here is qualitative and structural (see
# case.json.modeling_assumptions[MA2].sensitivity and FACILITATOR.md): moving the
# 3.0 threshold changes whether EACH reading individually clears the bar, which is
# a different question from which reading is numerically larger.
FLEX = ["transit_dip_ppm"]


def _generate_light_curve(p):
    """Rebuild the full 20-point Appendix A dataset from PARAMS, deterministically."""
    rnd = random.Random(p["random_seed"])
    n = 20
    transit_idx = [8, 9, 10, 11]
    flux = []
    for t in range(n):
        drift = p["drift_amplitude"] * (t - 9.5) ** 2 + p["drift_offset"]
        val = drift + rnd.gauss(0, p["noise_sd_ppm"])
        if t in transit_idx:
            val -= p["transit_dip_ppm"]
        # Appendix A publishes whole-ppm values; round here too so the base-case
        # (PARAMS unmodified) run reproduces the exact published table and its
        # exact derived statistics in case.json.derived, not a higher-precision
        # near-miss. A flexed run still rounds at each new dip depth, which is the
        # honest behavior (the case's own table would also be reported in whole ppm).
        flux.append(round(val))
    return flux, transit_idx


def _line_fit(xs, ys):
    n = len(xs)
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den = sum((x - mean_x) ** 2 for x in xs)
    m = num / den if den else 0.0
    c = mean_y - m * mean_x
    return m, c


def _stdev(vals):
    n = len(vals)
    if n < 2:
        return 0.0
    mean = sum(vals) / n
    var = sum((v - mean) ** 2 for v in vals) / (n - 1)
    return var ** 0.5


def _percentile(sorted_vals, pct):
    n = len(sorted_vals)
    if n == 1:
        return sorted_vals[0]
    k = (n - 1) * (pct / 100.0)
    f, c = int(k), min(int(k) + 1, n - 1)
    if f == c:
        return sorted_vals[f]
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


def _median(sorted_vals):
    n = len(sorted_vals)
    mid = n // 2
    if n % 2:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0


def significances(params=None):
    """Recomputes sig_naive and sig_robust from PARAMS, exactly mirroring case.json.derived."""
    p = dict(PARAMS)
    p.update(params or {})
    flux, transit_idx = _generate_light_curve(p)
    n = len(flux)
    oot_idx = [i for i in range(n) if i not in transit_idx]
    oot_t = [float(i) for i in oot_idx]
    oot_flux = [flux[i] for i in oot_idx]
    transit_flux = [flux[i] for i in transit_idx]

    # Method 1 -- naive line of best fit through the out-of-transit points.
    m, c = _line_fit(oot_t, oot_flux)
    resid = [oot_flux[i] - (m * oot_t[i] + c) for i in range(len(oot_t))]
    resid_sd = _stdev(resid)
    line_at_transit = [m * i + c for i in transit_idx]
    naive_dip = sum(line_at_transit) / len(line_at_transit) - sum(transit_flux) / len(transit_flux)
    sig_naive = naive_dip / resid_sd if resid_sd else 0.0

    # Method 2 -- box-and-whisker / IQR-based robust read.
    s = sorted(oot_flux)
    q1, q3 = _percentile(s, 25), _percentile(s, 75)
    iqr = q3 - q1
    robust_sigma = 0.7413 * iqr
    median_oot = _median(s)
    robust_dip = median_oot - (sum(transit_flux) / len(transit_flux))
    sig_robust = robust_dip / robust_sigma if robust_sigma else 0.0

    return {"sig_naive": sig_naive, "sig_robust": sig_robust,
            "resid_sd": resid_sd, "robust_sigma": robust_sigma,
            "naive_dip": naive_dip, "robust_dip": robust_dip}


def evaluate(params):
    """higher-wins contract: A = naive reading, B = robust reading."""
    s = significances(params)
    return {"A": s["sig_naive"], "B": s["sig_robust"]}


def evaluate_twist(params):
    """No withheld-information twist in this case (see FACILITATOR.md) -- the
    'twist' is structural (revealing the second method's answer), not new data.
    Returns the same evaluate() result unmodified so tier2_probes.py's P4 machine
    recomputation has a defined, harmless no-op to compare against."""
    return evaluate(params)


if __name__ == '__main__':
    base = evaluate({})
    a, b = base["A"], base["B"]
    win = "A" if a > b else ("B" if b > a else "TIE")
    lo, hi = min(a, b), max(a, b)
    margin = 100.0 * (hi - lo) / lo if lo else 0.0
    threshold = PARAMS["followup_threshold_sigma"]
    print("base sig_naive=A=%.3f  sig_robust=B=%.3f  winner=%s  margin=%.1f%%  threshold=%.1f" %
          (a, b, win, margin, threshold))
    print("  naive clears threshold:", a >= threshold, " robust clears threshold:", b >= threshold)

    print("\n--- +/-50%% flex sweep (FLEX[] only) ---")
    for name in FLEX:
        base_val = PARAMS[name]
        for label, mult in (("-50%", 0.5), ("+50%", 1.5)):
            flexed = evaluate({name: base_val * mult})
            fa, fb = flexed["A"], flexed["B"]
            fwin = "A" if fa > fb else ("B" if fb > fa else "TIE")
            flo, fhi = min(fa, fb), max(fa, fb)
            fmargin = 100.0 * (fhi - flo) / flo if flo else 0.0
            flip = " <<< FLIPS" if fwin != win else ""
            cap = " (breaks 20% cap)" if fmargin > 20 else ""
            print("  %-24s %-5s -> A=%.3f B=%.3f winner=%s margin=%.1f%%%s%s" %
                  (name, label, fa, fb, fwin, fmargin, flip, cap))

    print("\n--- qualitative check: followup_threshold_sigma (MA2), held fixed but reported ---")
    print("  (not swept by FLEX[] -- see the note above evaluate(); this loop only checks,")
    print("   at each threshold, whether each reading individually clears the bar)")
    for thr in (2.5, 2.8, 3.0, 3.1, 3.5):
        print("  threshold=%.1f  naive clears=%-5s  robust clears=%-5s  %s" %
              (thr, a >= thr, b >= thr,
               "AGREE" if (a >= thr) == (b >= thr) else "DISAGREE (the live tension)"))
