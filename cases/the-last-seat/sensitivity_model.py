#!/usr/bin/env python3
"""
SENSITIVITY MODEL -- The Last Seat.

Re-computes every number in the case from the Census Bureau's published apportionment
populations (Table C2). Contract (case-readiness Tier 2, probe 5):
    PARAMS, FLEX, evaluate(params) -> {"A": score, "B": score}  (higher is better),
    evaluate_twist(params) (2010 census).

SCORE = 1000 / (max persons-per-representative / min persons-per-representative).
Higher score = smaller worst gap = better. Because the probe's margin is
(score_winner - score_loser) / score_loser, this equals (r_loser - r_winner) / r_winner:
the gap divided by the winner's ratio, the case's single margin convention (4.11% in 2020).

Option A = Huntington-Hill (equal proportions); Option B = Webster.

FLEX: the only dial a student can re-choose is the House size. The case treats 435 as
statute, so flexing it is a scenario question ("what if Congress also changed the size"),
disclosed in sensitivity_disclosure[]. Cited populations are NOT flexed (probe 6 covers sources).

Run:  python3 sensitivity_model.py        (asserts every published number)
"""
import heapq, math

POP_2020 = {
    "Alabama": 5030053,
    "Alaska": 736081,
    "Arizona": 7158923,
    "Arkansas": 3013756,
    "California": 39576757,
    "Colorado": 5782171,
    "Connecticut": 3608298,
    "Delaware": 990837,
    "Florida": 21570527,
    "Georgia": 10725274,
    "Hawaii": 1460137,
    "Idaho": 1841377,
    "Illinois": 12822739,
    "Indiana": 6790280,
    "Iowa": 3192406,
    "Kansas": 2940865,
    "Kentucky": 4509342,
    "Louisiana": 4661468,
    "Maine": 1363582,
    "Maryland": 6185278,
    "Massachusetts": 7033469,
    "Michigan": 10084442,
    "Minnesota": 5709752,
    "Mississippi": 2963914,
    "Missouri": 6160281,
    "Montana": 1085407,
    "Nebraska": 1963333,
    "Nevada": 3108462,
    "New Hampshire": 1379089,
    "New Jersey": 9294493,
    "New Mexico": 2120220,
    "New York": 20215751,
    "North Carolina": 10453948,
    "North Dakota": 779702,
    "Ohio": 11808848,
    "Oklahoma": 3963516,
    "Oregon": 4241500,
    "Pennsylvania": 13011844,
    "Rhode Island": 1098163,
    "South Carolina": 5124712,
    "South Dakota": 887770,
    "Tennessee": 6916897,
    "Texas": 29183290,
    "Utah": 3275252,
    "Vermont": 643503,
    "Virginia": 8654542,
    "Washington": 7715946,
    "West Virginia": 1795045,
    "Wisconsin": 5897473,
    "Wyoming": 577719,
}

SEATS_2020_PUBLISHED = {
    "Alabama": 7,
    "Alaska": 1,
    "Arizona": 9,
    "Arkansas": 4,
    "California": 52,
    "Colorado": 8,
    "Connecticut": 5,
    "Delaware": 1,
    "Florida": 28,
    "Georgia": 14,
    "Hawaii": 2,
    "Idaho": 2,
    "Illinois": 17,
    "Indiana": 9,
    "Iowa": 4,
    "Kansas": 4,
    "Kentucky": 6,
    "Louisiana": 6,
    "Maine": 2,
    "Maryland": 8,
    "Massachusetts": 9,
    "Michigan": 13,
    "Minnesota": 8,
    "Mississippi": 4,
    "Missouri": 8,
    "Montana": 2,
    "Nebraska": 3,
    "Nevada": 4,
    "New Hampshire": 2,
    "New Jersey": 12,
    "New Mexico": 3,
    "New York": 26,
    "North Carolina": 14,
    "North Dakota": 1,
    "Ohio": 15,
    "Oklahoma": 5,
    "Oregon": 6,
    "Pennsylvania": 17,
    "Rhode Island": 2,
    "South Carolina": 7,
    "South Dakota": 1,
    "Tennessee": 9,
    "Texas": 38,
    "Utah": 4,
    "Vermont": 1,
    "Virginia": 11,
    "Washington": 10,
    "West Virginia": 2,
    "Wisconsin": 8,
    "Wyoming": 1,
}

POP_2010 = {
    "Alabama": 4802982,
    "Alaska": 721523,
    "Arizona": 6412700,
    "Arkansas": 2926229,
    "California": 37341989,
    "Colorado": 5044930,
    "Connecticut": 3581628,
    "Delaware": 900877,
    "Florida": 18900773,
    "Georgia": 9727566,
    "Hawaii": 1366862,
    "Idaho": 1573499,
    "Illinois": 12864380,
    "Indiana": 6501582,
    "Iowa": 3053787,
    "Kansas": 2863813,
    "Kentucky": 4350606,
    "Louisiana": 4553962,
    "Maine": 1333074,
    "Maryland": 5789929,
    "Massachusetts": 6559644,
    "Michigan": 9911626,
    "Minnesota": 5314879,
    "Mississippi": 2978240,
    "Missouri": 6011478,
    "Montana": 994416,
    "Nebraska": 1831825,
    "Nevada": 2709432,
    "New Hampshire": 1321445,
    "New Jersey": 8807501,
    "New Mexico": 2067273,
    "New York": 19421055,
    "North Carolina": 9565781,
    "North Dakota": 675905,
    "Ohio": 11568495,
    "Oklahoma": 3764882,
    "Oregon": 3848606,
    "Pennsylvania": 12734905,
    "Rhode Island": 1055247,
    "South Carolina": 4645975,
    "South Dakota": 819761,
    "Tennessee": 6375431,
    "Texas": 25268418,
    "Utah": 2770765,
    "Vermont": 630337,
    "Virginia": 8037736,
    "Washington": 6753369,
    "West Virginia": 1859815,
    "Wisconsin": 5698230,
    "Wyoming": 568300,
}

SEATS_2010_PUBLISHED = {
    "Alabama": 7,
    "Alaska": 1,
    "Arizona": 9,
    "Arkansas": 4,
    "California": 53,
    "Colorado": 7,
    "Connecticut": 5,
    "Delaware": 1,
    "Florida": 27,
    "Georgia": 14,
    "Hawaii": 2,
    "Idaho": 2,
    "Illinois": 18,
    "Indiana": 9,
    "Iowa": 4,
    "Kansas": 4,
    "Kentucky": 6,
    "Louisiana": 6,
    "Maine": 2,
    "Maryland": 8,
    "Massachusetts": 9,
    "Michigan": 14,
    "Minnesota": 8,
    "Mississippi": 4,
    "Missouri": 8,
    "Montana": 1,
    "Nebraska": 3,
    "Nevada": 4,
    "New Hampshire": 2,
    "New Jersey": 12,
    "New Mexico": 3,
    "New York": 27,
    "North Carolina": 13,
    "North Dakota": 1,
    "Ohio": 16,
    "Oklahoma": 5,
    "Oregon": 5,
    "Pennsylvania": 18,
    "Rhode Island": 2,
    "South Carolina": 7,
    "South Dakota": 1,
    "Tennessee": 9,
    "Texas": 36,
    "Utah": 4,
    "Vermont": 1,
    "Virginia": 11,
    "Washington": 10,
    "West Virginia": 3,
    "Wisconsin": 8,
    "Wyoming": 1,
}

PARAMS = {"house_size": 435}
FLEX = ["house_size"]


def huntington_hill(pop, H):
    seats = {s: 1 for s in pop}
    pq = [(-pop[s] / math.sqrt(2), s) for s in pop]
    heapq.heapify(pq)
    for _ in range(H - len(pop)):
        _, s = heapq.heappop(pq)
        seats[s] += 1
        n = seats[s]
        heapq.heappush(pq, (-pop[s] / math.sqrt(n * (n + 1)), s))
    return seats


def webster(pop, H):
    seats = {s: 1 for s in pop}
    pq = [(-pop[s] / 1.5, s) for s in pop]
    heapq.heapify(pq)
    for _ in range(H - len(pop)):
        _, s = heapq.heappop(pq)
        seats[s] += 1
        heapq.heappush(pq, (-pop[s] / (seats[s] + 0.5), s))
    return seats


def webster_by_divisor(pop, d):
    return {s: max(1, math.floor(pop[s] / d + 0.5)) for s in pop}


def max_min_ratio(pop, seats):
    ppr = {s: pop[s] / seats[s] for s in pop}
    return max(ppr.values()) / min(ppr.values())


def quota_error(pop, seats, H):
    T = sum(pop.values())
    return sum(abs(seats[s] - pop[s] * H / T) for s in pop)


def _score(pop, H):
    H = int(round(H))
    ra = max_min_ratio(pop, huntington_hill(pop, H))
    rb = max_min_ratio(pop, webster(pop, H))
    return {"A": 1000.0 / ra, "B": 1000.0 / rb}


def evaluate(params):
    return _score(POP_2020, params["house_size"])


def evaluate_twist(params):
    """Twist: the 2010 census, same yardstick."""
    return _score(POP_2010, params["house_size"])


def margin_pct(a, b):
    """Gap divided by the winner's (smaller) value; lower-is-better metrics."""
    lo, hi = sorted((a, b))
    return 100.0 * (hi - lo) / lo


if __name__ == "__main__":
    H = 435
    for yr, pop, pub in (("2020", POP_2020, SEATS_2020_PUBLISHED), ("2010", POP_2010, SEATS_2010_PUBLISHED)):
        a, b = huntington_hill(pop, H), webster(pop, H)
        assert a == pub, yr + " HH does not reproduce the published seats"
        diff = {s: (a[s], b[s]) for s in pop if a[s] != b[s]}
        ra, rb = max_min_ratio(pop, a), max_min_ratio(pop, b)
        ea, eb = quota_error(pop, a, H), quota_error(pop, b, H)
        print(yr, "differ (HH, Webster):", diff)
        print(yr, "max/min HH %.4f Webster %.4f margin %.2f%%" % (ra, rb, margin_pct(ra, rb)))
        print(yr, "quota error HH %.3f Webster %.3f margin %.2f%%" % (ea, eb, margin_pct(ea, eb)))
    d = sum(POP_2020.values()) / 435
    assert webster_by_divisor(POP_2020, d) == webster(POP_2020, 435)
    mn = POP_2020["Minnesota"] / math.sqrt(8 * 7)
    ny = POP_2020["New York"] / math.sqrt(27 * 26)
    need = mn * math.sqrt(27 * 26)
    print("priority MN8 %.3f NY27 %.3f ; NY needed %.2f ; shortfall %.2f" % (mn, ny, need, need - POP_2020["New York"]))
    for yr, pop in (("2020", POP_2020), ("2010", POP_2010)):
        cnt = {"A": 0, "B": 0, "tie": 0}
        for h in range(300, 601):
            ra = max_min_ratio(pop, huntington_hill(pop, h)); rb = max_min_ratio(pop, webster(pop, h))
            cnt["A" if ra < rb - 1e-12 else "B" if rb < ra - 1e-12 else "tie"] += 1
        print(yr, "H=300..600 winners on max/min:", cnt)
