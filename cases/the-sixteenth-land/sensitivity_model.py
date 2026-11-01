"""The Sixteenth Land -- exact model (hypergeometric, 40-card deck).  Higher = better.
PARAMS are every dial the case states; FLEX are the ones that are ASSUMPTIONS (MA1-MA5).
Deck size, hand size and the two land counts are the ballot / game rules and are not flexed
by P5 (flexing deck or hand size is a different game; see DECK_HAND_SWEEP below).
"""
from fractions import Fraction as F
from math import comb

PARAMS = {
    "lo": 3,            # MA2 window lower bound (lands)
    "hi": 6,            # MA2 window upper bound
    "turn": 4,          # MA3 horizon: cards seen through this turn
    "play_share": 0.5,  # MA4 share of games on the play
    "deck": 40, "hand": 7, "lands_A": 16, "lands_B": 17,
}
FLEX = ["lo", "hi", "turn", "play_share"]

def hyp(N, L, n, lo, hi):
    return F(sum(comb(L, k) * comb(N - L, n - k) for k in range(lo, hi + 1)
                 if 0 <= k <= L and 0 <= n - k <= N - L), comb(N, n))

def cards_seen(p, on_play):
    return int(p["hand"]) + int(round(p["turn"])) - (1 if on_play else 0)

def smooth(p, L):
    lo, hi = int(round(p["lo"])), int(round(p["hi"]))
    f = F(p["play_share"]).limit_denominator(1000)
    pl = hyp(p["deck"], L, cards_seen(p, True), lo, hi)
    dr = hyp(p["deck"], L, cards_seen(p, False), lo, hi)
    return float(f * pl + (1 - f) * dr)

def evaluate(p):
    return {"A": smooth(p, p["lands_A"]), "B": smooth(p, p["lands_B"])}

# Twist: free one-time redraw of the opening hand when it has 0,1,6 or 7 lands (second hand kept).
def _after(N, L, k, draws, lo, hi):
    rem = N - 7; rl = L - k
    return sum(F(comb(rl, j) * comb(rem - rl, draws - j), comb(rem, draws))
               for j in range(draws + 1) if lo <= k + j <= hi)

def _twist_one(p, L, draws):
    N = p["deck"]; lo, hi = int(round(p["lo"])), int(round(p["hi"]))
    h = lambda k: F(comb(L, k) * comb(N - L, 7 - k), comb(N, 7))
    tot = F(0)
    for k in range(8):
        if k in (0, 1, 6, 7):
            tot += h(k) * sum(h(k2) * _after(N, L, k2, draws, lo, hi) for k2 in range(8))
        else:
            tot += h(k) * _after(N, L, k, draws, lo, hi)
    return tot

def evaluate_twist(p):
    out = {}
    for key, L in (("A", p["lands_A"]), ("B", p["lands_B"])):
        f = F(p["play_share"]).limit_denominator(1000)
        t = int(round(p["turn"])); pl = _twist_one(p, L, t - 1); dr = _twist_one(p, L, t)
        out[key] = float(f * pl + (1 - f) * dr)
    return out

def margin(r):
    a, b = r["A"], r["B"]
    return 100 * abs(a - b) / max(a, b)

if __name__ == "__main__":
    b = evaluate(PARAMS); print("base", b, "margin %.3f%%" % margin(b), "winner", "A" if b["A"] > b["B"] else "B")
    t = evaluate_twist(PARAMS); print("twist", t, "margin %.3f%%" % margin(t), "winner", "A" if t["A"] > t["B"] else "B")
    assert abs(b["A"] - 0.84461) < 1e-4 and abs(b["B"] - 0.85095) < 1e-4
