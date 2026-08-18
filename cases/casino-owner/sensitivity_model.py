"""
Casino Owner -- sensitivity model (case-readiness Tier 2 probe 5 contract).

Given data (Appendix A/B/C, kept verbatim from the legacy docx) is hardcoded below as
INDIGO_BUCKETS / VIDEO_BETS / TRAFFIC -- these are NOT swept by probe 5; only PARAMS entries
listed in FLEX are genuine stated modeling assumptions (Appendix E) eligible for the +/-50% sweep.

PARAMS/FLEX/evaluate()/evaluate_twist() is the fixed four-name contract skills/case-readiness/
SKILL.md's Tier 2 probe 5 expects. See templates/INTERACTIVE_HTML_CONTRACT.md Section 2 for the
JS-port contract this file's arithmetic must be mirrored into (published/*.html's <script> block).
"""

INDIGO_BUCKETS = [
    (100,500,     0.310,0.081,4.3,   0.114,0.082,6.7,   0.078,0.082,4.3),
    (500.01,1000, 0.276,0.064,9.8,   0.206,0.065,11.2,  0.215,0.065,9.8),
    (1000.01,2500,0.218,0.075,15.2,  0.385,0.074,18.5,  0.373,0.072,15.2),
    (2500.01,5000,0.103,0.082,31.8,  0.144,0.082,34.0,  0.204,0.082,31.8),
    (5000.01,7500,0.077,0.089,46.2,  0.107,0.087,50.3,  0.072,0.087,46.2),
    (7500.01,10000,0.016,0.099,54.2, 0.044,0.098,61.2,  0.058,0.098,54.2),
]
VIDEO_BETS = [(0.50,0.487,8),(1.00,0.256,15),(1.50,0.153,25),(2.50,0.104,50)]
TRAFFIC = {
    "weekday": {"days":4, "blocks":[("04:00-10:00",2.2,18.6),("10:00-16:00",3.1,34.4),("16:00-22:00",5.7,56.1),("22:00-04:00",5.2,67.9)]},
    "weekend": {"days":3, "blocks":[("04:00-10:00",3.5,31.4),("10:00-16:00",4.9,54.8),("16:00-22:00",6.9,78.9),("22:00-04:00",6.7,85.2)]},
}

def _tier_for(avg_players):
    r = round(avg_players)
    if r<=3: return "1-3"
    if r<=5: return "4-5"
    return "6-7"

def _indigo_tier_stats():
    out={}
    for label,(fi,ri,ti) in [("1-3",(2,3,4)),("4-5",(5,6,7)),("6-7",(8,9,10))]:
        rev=0.0; t=0.0
        for row in INDIGO_BUCKETS:
            lo,hi=row[0],row[1]; f=row[fi]; rake=row[ri]; tm=row[ti]
            mid=(lo+hi)/2
            rev += f*mid*rake
            t += f*tm
        out[label] = {"avg_rake": rev, "avg_time_min": t, "games_per_hr": 60.0/t}
    return out

def _video_ev_per_play():
    ev=0.0
    for b,f,o in VIDEO_BETS:
        p = 1.0/(o+1)
        profit = 0.65*b*(1-p) - p*b
        ev += f*profit
    return ev

PARAMS = {
    "peak_hours_per_day": 12,          # MA1 -- hours/day the new room is assumed open (6-hr blocks, ranked by traffic)
    "indigo_tables_built": 4,          # MA3 -- south lobby max capacity, Appendix A
    "video_machines_built": 25,        # MA3 -- south lobby max capacity, Appendix B
    "indigo_tables_staffed": 4,        # base case: all built tables have a trained dealer; the Twist flexes this down
    "dealer_wage_per_hr": 12.50,       # given data, Appendix A -- not a FLEX dial
    "security_wage_per_hr": 7.50,      # given data, Appendix B -- not a FLEX dial
    "security_staff_count": 2,         # given data, Appendix B -- not a FLEX dial
}
FLEX = ["peak_hours_per_day", "indigo_tables_staffed"]

def _open_blocks(day_type, hours_per_day):
    blocks = TRAFFIC[day_type]["blocks"]
    n_blocks = max(1, round(hours_per_day / 6))
    n_blocks = min(n_blocks, len(blocks))
    ranked = sorted(blocks, key=lambda b: b[2], reverse=True)  # by video occupancy % as the traffic proxy
    return ranked[:n_blocks]

def evaluate(params):
    tiers = _indigo_tier_stats()
    ev_play = _video_ev_per_play()
    plays_per_hr = 3600.0/17.9

    indigo_rev = 0.0
    video_rev = 0.0
    indigo_staffed = params["indigo_tables_staffed"]
    indigo_built = params["indigo_tables_built"]
    video_built = params["video_machines_built"]

    for day_type, meta in TRAFFIC.items():
        days = meta["days"]
        for seg, avg_players, occ_pct in _open_blocks(day_type, params["peak_hours_per_day"]):
            tier = tiers[_tier_for(avg_players)]
            indigo_hr = tier["avg_rake"] * tier["games_per_hr"] * indigo_staffed
            indigo_rev += indigo_hr * 6 * days
            active_m = video_built * occ_pct/100.0
            video_hr = active_m * plays_per_hr * ev_play
            video_rev += video_hr * 6 * days

    hours_open_per_week = round(params["peak_hours_per_day"]/6)*6 * 7
    dealer_cost = indigo_staffed * hours_open_per_week * params["dealer_wage_per_hr"]
    security_cost = params["security_staff_count"] * hours_open_per_week * params["security_wage_per_hr"]

    return {"A": indigo_rev - dealer_cost, "B": video_rev - security_cost}

def evaluate_twist(params):
    p = dict(params)
    p["indigo_tables_staffed"] = 2  # only 2 of 4 tables have a currently-trained Indigo dealer
    return evaluate(p)

if __name__ == "__main__":
    base = evaluate(PARAMS)
    print("base", base, "margin_pct", 100*(base["A"]-base["B"])/base["B"])
    tw = evaluate_twist(PARAMS)
    print("twist", tw, "margin_pct(B over A)", 100*(tw["B"]-tw["A"])/tw["A"])
    # P5 flex checks
    for k in FLEX:
        for mult in (0.5,1.5):
            p2 = dict(PARAMS); p2[k] = PARAMS[k]*mult
            r = evaluate(p2)
            winner = "A" if r["A"]>r["B"] else ("B" if r["B"]>r["A"] else "TIE")
            print(k, mult, r, "winner", winner)
