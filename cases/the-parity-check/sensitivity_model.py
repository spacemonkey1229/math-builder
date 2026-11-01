"""Sensitivity model for The Parity Check (SPEC section 2 balance test, case-readiness Tier 2
probe 5).

CONTRACT (skills/case-readiness/scripts/example_sensitivity_model.py):
    PARAMS                     dict[str, number]   every dial the case states
    FLEX                       list[str]            the ASSUMPTION subset probe 5 sweeps
    evaluate(params) -> dict   {"A": metric, "B": metric}   higher is better
    evaluate_twist(params)     same shape, with the case's own twist applied

Primary metric (case.json.primary_metric, restated as "catches per bit" -- the reciprocal
framing Background states directly: "which scheme catches more corrupted frames per bit spent
getting there"):

    eff_A(n, p) = P(Featherweight Check catches the frame's corruption) / n
    eff_B(n, p) = P(Full-Frame Guard catches the frame's corruption)     / 32

  where n = payload size in bytes, p = per-bit error rate (Appendix E, MA1).

  Featherweight Check is a BYTE-level check: it misses a frame's corruption only if every
  corrupted byte in the frame happens to have an EVEN (nonzero) number of flipped bits.
      P(one byte has an even flip count) = 0.5 * (1 + (1-2p)^8)      [peven(p)]
      P(A catches) = 1 - peven(p)^n

  Full-Frame Guard is CRC-32: per case.md/Appendix A, it "catches essentially every realistic
  error pattern." Modeled here as catching every corrupted frame (the real, sourced CRC-32
  miss probability is ~2^-32 per corrupted frame -- negligible at any n used in this case):
      P(B catches) = 1 - (1-p)^(8n)

  Overhead: Featherweight Check adds 1 bit/byte -> n bits/packet [S3]. Full-Frame Guard adds a
  fixed 4 bytes = 32 bits/packet regardless of size [S1][S2].

Appendix C's four candidate packet sizes are 11, 35, 125, 222 bytes (11/125/222 sourced from the
real LoRaWAN US915 payload table [S5]; 35 is MA2, a stated scenario value chosen within that real
envelope). The schemes' exact geometric break-even is n=32 bytes (1 bit/byte x 32 bytes = 32 bits
= the sourced 4-byte/32-bit CRC overhead) -- landing Appendix C row 2 exactly there (an earlier
draft's choice) produced a razor-thin ~0.02% margin, a coin-flip result the same shape as
cases/the-overlap-call's fragility. MA2 was retuned to n=35 bytes -- close enough to the
break-even to still be a genuinely live comparison (not a landslide like n=11, 125, or 222), but
far enough off the exact tie point to land inside SPEC section 2's ~5-15% target balance band
(margin ~9.4% at Appendix E's stated error rate). This is where D5 asks the Hero to land, and
where case.json's reported margin_pct is computed. PARAMS["packet_size_bytes"] defaults to 35 for
this reason; it is NOT in FLEX (Appendix C is a fixed set of scenario/sourced sizes the Hero
explores directly in D3, not an uncertain research dial -- MA1, the per-bit error rate, is the
only assumption this case's own Robustness Check requires sweeping).
"""

import math

PARAMS = {
    # --- ASSUMED (Appendix E, MA1) ---
    "error_rate": 6e-5,          # representative per-bit error rate, this case's stated value

    # --- fixed scenario/sourced size this case reports its margin at (Appendix C row 2, MA2) ---
    "packet_size_bytes": 35.0,
}

FLEX = ["error_rate"]


def peven(p):
    """P(a given byte has an even, possibly-zero, number of its 8 bits flipped)."""
    return 0.5 * (1 + (1 - 2 * p) ** 8)


def _catch_A(n, p):
    return 1 - peven(p) ** n


def _catch_B(n, p):
    return 1 - (1 - p) ** (8 * n)


def evaluate(params=None, packet_size_bytes=None):
    """CONTRACT: {"A": metric, "B": metric}, higher wins. Metric = P(scheme catches the frame's
    corruption) per overhead bit spent -- this case's own primary_metric, in its "catches per
    bit" reciprocal form (case.md Background: "which scheme catches more corrupted frames per
    bit spent getting there")."""
    p = dict(PARAMS)
    p.update(params or {})
    n = packet_size_bytes if packet_size_bytes is not None else p["packet_size_bytes"]
    rate = p["error_rate"]
    eff_a = _catch_A(n, rate) / n
    eff_b = _catch_B(n, rate) / 32.0
    return {"A": eff_a, "B": eff_b}


def evaluate_twist(params=None, packet_size_bytes=None):
    """FACILITATOR.md's twist: burst noise flips bits in clusters rather than independently, and
    a 2-bit-adjacent burst is the worst realistic case for the Featherweight Check -- it is
    EVEN by construction, every time, so parity misses every burst-corrupted byte outright.
    Modeled here as the byte-corruption probability staying the same as the base uniform model
    (a byte is "hit" at the same overall rate) but with peven forced to 1.0 for hit bytes -- i.e.
    the Featherweight Check catches nothing under burst noise, while the Full-Frame Guard (which
    does not depend on the flip pattern within a byte) is unaffected. This does not flip the
    winner at the case's reported packet size (B was already ahead); it demonstrates why the
    room's model needs re-checking, not a new number to hand them."""
    p = dict(PARAMS)
    p.update(params or {})
    n = packet_size_bytes if packet_size_bytes is not None else p["packet_size_bytes"]
    rate = p["error_rate"]
    # Every corrupted byte is, by the twist's construction, invisible to parity (peven forced
    # to 1.0 for any hit byte) -- so A's catch probability collapses to 0 outright.
    catch_a_twist = 0.0
    catch_b_twist = _catch_B(n, rate)
    return {"A": catch_a_twist / n, "B": catch_b_twist / 32.0}


def _state(ev):
    a, b = ev["A"], ev["B"]
    if a == b:
        return "TIE", 0.0
    hi_key, lo_key = ("A", "B") if a > b else ("B", "A")
    lo = ev[lo_key]
    margin = 0.0 if lo == 0 else 100.0 * (ev[hi_key] - lo) / lo
    return hi_key, margin


def _report(label, ev):
    state, margin = _state(ev)
    print(f"{label}: A={ev['A']:.6e}  B={ev['B']:.6e}  state={state}  margin={margin:.4f}%")
    return state, margin


if __name__ == "__main__":
    base = evaluate(PARAMS)
    winner, margin = _report("Base (n=35 bytes, error_rate=6e-5)", base)
    assert winner == "B" and abs(margin - 9.4) < 0.5, \
        f"Base model drifted from case.json's disclosed canonical base (B wins by ~9.4%): got {winner} {margin:.4f}%"

    twist = evaluate_twist(PARAMS)
    t_winner, t_margin = _report("Twist (burst noise, always-even flips)", twist)
    assert t_winner == "B", "Twist should widen B's lead (A's catch rate collapses), not flip it"

    print("\n--- Probe 5: sweep of MA1 (error_rate) across the disclosed real-world-plausible "
          "range (1e-6 to 1e-3) at the reported packet size (35 bytes) ---")
    for rate in [1e-6, 1e-5, 6e-5, 1e-4, 1e-3]:
        ev = evaluate({"error_rate": rate})
        state, m = _state(ev)
        flip = " <-- FLIPS" if state != winner else ""
        print(f"  error_rate={rate:.0e}  A={ev['A']:.4e}  B={ev['B']:.4e}  "
              f"state={state}  margin={m:.4f}%{flip}")

    print("\n--- Same sweep at ALL four Appendix C candidate packet sizes (winner should be "
          "stable per size across the full error_rate range -- confirms size, not error_rate, "
          "drives which option wins) ---")
    for n in [11, 35, 125, 222]:
        winners = set()
        for rate in [1e-6, 1e-5, 6e-5, 1e-4, 1e-3]:
            ev = evaluate({"error_rate": rate}, packet_size_bytes=n)
            state, m = _state(ev)
            winners.add(state)
        print(f"  n={n:3d} bytes: winner(s) across full error_rate range = {sorted(winners)}")

    print("\n--- Break-even packet size (bisection) at each tested error_rate ---")
    def diff(n, rate):
        ev = evaluate({"error_rate": rate}, packet_size_bytes=n)
        return ev["A"] - ev["B"]
    for rate in [1e-6, 1e-5, 6e-5, 1e-4, 1e-3]:
        lo, hi = 1.0, 2000.0
        flo = diff(lo, rate)
        for _ in range(100):
            mid = (lo + hi) / 2
            fm = diff(mid, rate)
            if flo * fm <= 0:
                hi = mid
            else:
                lo = mid
                flo = fm
        print(f"  error_rate={rate:.0e}: break-even n* ~= {(lo+hi)/2:.2f} bytes")

    print("\nAll checks complete. See RESEARCH_LOG.md for the full robustness-sweep writeup.")
