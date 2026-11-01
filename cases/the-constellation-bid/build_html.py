#!/usr/bin/env python3
"""Fill templates/interactive_shell.html for Constellation Bid."""
import re

PROJECT = "/Users/manan/Documents/Claude/Projects/Math Builder"
SHELL = f"{PROJECT}/templates/interactive_shell.html"
OUT = f"{PROJECT}/cases/the-constellation-bid/published/Constellation Bid - Interactive.html"

html = open(SHELL, encoding="utf-8").read()

REPL = {}

REPL["{{CASE_TITLE}}"] = "Constellation Bid"
REPL["{{CASE_YEAR}}"] = "2026-27"
REPL["{{CASE_TIER}}"] = "T3"
REPL["{{CASE_BAND}}"] = "MS-Stretch / HS-Entry"
REPL["{{CASE_STRAND_SUMMARY}}"] = "Unit Circle &middot; Trigonometric Functions"
REPL["{{CASE_ID}}"] = "the-constellation-bid"
REPL["{{CASE_GLOSSARY_APPENDIX_LETTER}}"] = "Appendix G"
REPL["{{CASE_GLOSSARY_VERIFIED_DATE}}"] = "2026-09-18"
REPL["{{CASE_PROTAGONIST}}"] = "Aisha Odom"
REPL["{{CASE_OPTION_A_LABEL}}"] = "Consolidated Launch"
REPL["{{CASE_OPTION_A_TEXT}}"] = ("All 60 satellites on one large rocket into a single seed plane, then each "
    "off-plane satellite walks itself to its assigned plane on its own propellant.")
REPL["{{CASE_OPTION_B_LABEL}}"] = "Distributed Launch"
REPL["{{CASE_OPTION_B_TEXT}}"] = ("Six dedicated smaller rockets, one per target plane, so every satellite is "
    "delivered already correctly placed.")
REPL["{{CASE_SPECIFIC_CSS}}"] = ""
REPL["{{CASE_SPECIFIC_ICON_SYMBOLS}}"] = ""
REPL["{{CASE_OVERVIEW_BANNER_SVG}}"] = ""

REPL["{{CASE_OVERVIEW_TEXT}}"] = """
  <p class="lede">Aisha Odom has two spreadsheets open and one launch-slot deposit deadline blinking at the top of her inbox. Solara Orbital's board wants her recommendation in writing by tomorrow morning, and the deposit &mdash; nonrefundable &mdash; is due the same day she has to send it.</p>
  <p>Sixty satellites. Six target orbital planes, sixty degrees apart around the equator, each one needed to close a gap in Solara's coverage map before a competitor files for the same radio spectrum. One path puts all sixty on a single rocket, into a single plane, and lets each satellite burn its own propellant afterward to walk itself around to its assigned plane. The other path books six smaller rockets, one aimed straight at each target plane, so every satellite arrives already exactly where it needs to be.</p>
  <p>She pulls up the propellant budget her propulsion lead signed off on last month &mdash; a number that looked generous on a slide deck and considerably less generous now that she's staring at how far some of these satellites will actually have to travel. Her cursor sits over the sine key on her calculator. Behind her, the office is empty; everyone else left for the night two hours ago.</p>
  <p>Aisha bookmarks the launch-cost quote in one tab, the propulsion budget in the other, and starts working the angles.</p>
"""

REPL["{{CASE_BACKGROUND_TEXT}}"] = """
  <p>Aisha Odom is the constellation architect at Solara Orbital, a small-satellite operator, and she owns the launch-strategy recommendation the board will vote on this week. Solara's sixty-satellite constellation is designed as a Walker-style pattern: six orbital planes, evenly spaced sixty degrees apart in right ascension of ascending node (RAAN &mdash; the angle that fixes where a satellite's orbital plane crosses the equator), with ten satellites assigned to each plane.</p>
  <p>Two paths are open to her:</p>
  <p><strong>Consolidated Launch</strong> &mdash; book one large rocket, carry all sixty satellites to orbit together in a single "seed" plane, and let each satellite that isn't already in its assigned plane spend its own onboard propellant on a plane-change burn to walk itself over (SEE APPENDICES B, C and D).</p>
  <p><strong>Distributed Launch</strong> &mdash; book six smaller, dedicated rockets, one flown directly into each of the six target planes, so every satellite is delivered already correctly placed and no satellite ever needs to change planes after launch (SEE APPENDIX E).</p>
  <p>Every satellite's assigned position starts as an angle &mdash; how far its target plane sits around the equator from wherever it's actually delivered &mdash; and Solara's ground-station network reads a satellite's real-time position in orbit the same way: as an angle, whose sine, cosine, and tangent are exactly what a satellite-tracking analyst computes from the unit circle (SEE APPENDIX A). The Consolidated Launch's plane-change burns are expensive in direct proportion to how large that angle is. Each of Solara's satellites has a fixed, board-approved propellant allowance set aside for this kind of maneuver; a satellite that cannot complete its assigned plane change within that allowance never reaches its target plane at all (SEE APPENDIX D).</p>
  <p>None of the figures in this case describing Solara, Aisha, or this specific sixty-satellite mission are invented outright &mdash; every real-world figure is either cited to a real, live source or stated openly as a scenario assumption, disclosed in <strong>APPENDIX F</strong>.</p>
"""

REPL["{{CASE_CHALLENGE_3_DELIVERABLES_SUMMARY}}"] = ("Include: <strong>D1</strong> a unit-circle trig table for "
    "each of the six target planes; <strong>D2</strong> an arc-length table; <strong>D3</strong> a delta-v and "
    "propellant feasibility table; <strong>D4</strong> a cost-and-coverage decision memo.")

REPL["{{CASE_DELIVERABLES_ARRAY}}"] = """[
  ["D1", "Unit-circle trig table for all six target planes"],
  ["D2", "Arc-length table"],
  ["D3", "Delta-v and propellant feasibility table"],
  ["D4", "Cost-and-coverage decision memo"]
]"""

# ---------------------------------------------------------------- Appendices
REPL["{{CASE_APPENDICES_A_THROUGH_F}}"] = """
<details open id="apx-a">
<summary>Appendix A &mdash; Solara's Orbit and the Unit Circle</summary>
<div class="inner">
<p>Solara's constellation flies at a 550 km circular altitude &mdash; the same altitude SpaceX's own first operational Starlink shell was approved to fly at by the FCC [S1].</p>
<table id="tblA"><tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Orbital altitude</td><td class="num">550 km [MA1]</td></tr>
<tr><td>Earth's mean radius</td><td class="num">6,371 km</td></tr>
<tr><td>Orbital radius</td><td class="num">6,921 km</td></tr>
<tr><td>Earth's standard gravitational parameter (&mu;)</td><td class="num">398,600.4418 km&sup3;/s&sup2;</td></tr>
<tr><td>Orbital speed (v) &mdash; derived</td><td class="num">7,589.0 m/s</td></tr>
<tr><td>Orbital circumference &mdash; derived</td><td class="num">43,486.5 km</td></tr>
</table>
<p class="side-note">A ground-station analyst reads a satellite's elevation angle as it rises over the horizon using the tangent of the angle between line of sight and the ground &mdash; Appendix G's how-to skill covers finding sine, cosine, AND tangent of an angle using the unit circle.</p>
</div></details>

<details id="apx-b">
<summary>Appendix B &mdash; Solara's Six Target Planes</summary>
<div class="inner">
<table id="tblB"><tr><th>Target plane</th><th>RAAN offset from seed plane</th><th>Satellites assigned</th></tr>
<tr><td>Plane 0 (seed)</td><td class="num">0&deg;</td><td class="num">10</td></tr>
<tr><td>Plane 1</td><td class="num">60&deg;</td><td class="num">10</td></tr>
<tr><td>Plane 2</td><td class="num">120&deg;</td><td class="num">10</td></tr>
<tr><td>Plane 3</td><td class="num">180&deg;</td><td class="num">10</td></tr>
<tr><td>Plane 4</td><td class="num">240&deg;</td><td class="num">10</td></tr>
<tr><td>Plane 5</td><td class="num">300&deg;</td><td class="num">10</td></tr>
</table>
<p class="side-note">A burn can always go the shorter way around the circle &mdash; the burn Plane 4 or 5 actually needs is sized to the smaller of the stated offset and 360&deg; minus that offset, not the full stated number.</p>
</div></details>

<details id="apx-c">
<summary>Appendix C &mdash; The Plane-Change Maneuver</summary>
<div class="inner">
<p>The required delta-v for a single combined-maneuver plane-change burn is <strong>&Delta;v = 2&middot;v&middot;sin(&Delta;&theta; &divide; 2)</strong>, the standard astrodynamics relation for a single-burn orbital-plane rotation [S2]. This case applies it to a RAAN change as a disclosed simplification (MA2) &mdash; real RAAN changes are normally achieved via slow J2-perturbation drift, not a direct burn.</p>
</div></details>

<details id="apx-d">
<summary>Appendix D &mdash; Thruster, Propellant, and the Walk Budget</summary>
<div class="inner">
<table id="tblD"><tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Specific impulse (Isp), rated maximum</td><td class="num">2,150 s [S3]</td></tr>
<tr><td>Standard gravity (g&#8320;)</td><td class="num">9.80665 m/s&sup2;</td></tr>
<tr><td>Satellite wet mass</td><td class="num">15.0 kg [MA3]</td></tr>
<tr><td>Per-satellite propellant allowance for the walk</td><td class="num">4.0 kg [MA4]</td></tr>
</table>
</div></details>

<details id="apx-e">
<summary>Appendix E &mdash; Launch Costs</summary>
<div class="inner">
<table id="tblE"><tr><th>Quantity</th><th>Value</th></tr>
<tr><td>Total constellation mass (60 satellites)</td><td class="num">900.0 kg</td></tr>
<tr><td>Consolidated Launch: rideshare base price, first 50 kg</td><td class="num">$350,000 [S4]</td></tr>
<tr><td>Consolidated Launch: rideshare price per kg beyond 50 kg</td><td class="num">$7,000/kg [S4]</td></tr>
<tr><td>Distributed Launch: list price per dedicated Electron launch (up to 300 kg)</td><td class="num">$7,500,000 [S5]</td></tr>
<tr><td>Distributed Launch: number of dedicated launches required</td><td class="num">6</td></tr>
</table>
</div></details>

<details id="apx-f">
<summary>Appendix F &mdash; Modeling Assumptions</summary>
<div class="inner">
<blockquote>These figures are <strong>not sourced</strong>. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion &mdash; that is a legitimate move.</blockquote>
<table id="tblF"><tr><th>#</th><th>Assumption</th><th>Value used</th><th>Sensitivity</th></tr>
<tr><td>MA1</td><td>Solara's constellation altitude</td><td class="num">550 km</td><td>Scales orbital speed and every group's delta-v.</td></tr>
<tr><td>MA2</td><td>Modeling a RAAN change with the single-burn combined plane-change formula</td><td>&Delta;v=2v&middot;sin(&Delta;&theta;/2)</td><td>Does not change which angle is cheaper, but changes the exact propellant figures.</td></tr>
<tr><td>MA3</td><td>Satellite wet mass</td><td class="num">15.0 kg</td><td>Every propellant figure scales directly with this value.</td></tr>
<tr><td>MA4</td><td>Per-satellite propellant allowance for the walk</td><td class="num">4.0 kg</td><td>The single most dilemma-relevant assumption in the case.</td></tr>
</table>
</div></details>

<details id="apx-i">
<summary>Appendix I &mdash; Plain-English Notes on Real-World Terms</summary>
<div class="inner">
<p><strong>Picturing the "walk."</strong> Picture Earth from above the North Pole. Each of the six target orbital planes is a giant circular path, tilted at its own angle around the equator, like six hula-hoops all balanced on the same center point but each rotated to a different angle. A plane-change burn is a single, short engine firing that gives the satellite a sideways shove big enough to swing its entire circular path over until it lines up with a different hoop. An orbit is not a fixed track &mdash; it is simply the one circular path consistent with the satellite's current position and current velocity direction, so redirecting that velocity for an instant is the same thing as reassigning which hoop the satellite belongs to.</p>
<table><tr><th>Term</th><th>Plain-English explanation</th></tr>
<tr><td>RAAN</td><td>The angle, measured around the equator, marking where a satellite's orbit crosses from south to north &mdash; it says which way a given "hoop" is rotated.</td></tr>
<tr><td>Specific impulse (Isp)</td><td>How efficiently a thruster converts propellant into thrust &mdash; higher means more push per kilogram, the same way miles-per-gallon measures a car's efficiency.</td></tr>
<tr><td>J2 perturbation</td><td>Earth's slight equatorial bulge slowly rotates every satellite's orbital plane over time, for free &mdash; real operators often use this instead of a direct burn.</td></tr>
<tr><td>Sun-synchronous orbit</td><td>An orbit shaped so a satellite crosses any given point on Earth at the same local time every day.</td></tr>
<tr><td>Rideshare vs. dedicated launch</td><td>Rideshare splits one rocket's capacity across many customers (cheaper per kg); dedicated reserves the whole rocket for one customer (costlier, but you choose the exact orbit).</td></tr>
</table>
<p><strong>Hover any real-world term below for a plain-English explanation; click it for a real source.</strong></p>
<div class="glossary-grid" id="storyGlossaryGrid"></div>
</div></details>
"""

# ---------------------------------------------------------------- Notebook
REPL["{{CASE_NOTEBOOK_STEPS}}"] = """
  <div class="stepbox">
    <h4>Step 1 &mdash; Unit circle, delta-v, and propellant feasibility (D1&ndash;D3)</h4>
    <div class="goal">Pick the Plane 3 group (180&deg; offset &mdash; the largest walk) and the Plane 1 group (60&deg; offset &mdash; the smallest nonzero walk). For each, find the minimum angular separation, its half-angle's sine (from the unit circle), the resulting delta-v, and the propellant it costs.</div>
    <div class="fieldrow"><label for="s1sin180">sin(90&deg;) &mdash; half of Plane 3's 180&deg; separation</label><input type="number" id="s1sin180" step="0.001"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1dv180">Plane 3 delta-v (m/s)</label><input type="number" id="s1dv180" step="1"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1prop180">Plane 3 propellant required (kg)</label><input type="number" id="s1prop180" step="0.01"><span id="fb1c" class="fb"></span></div>
    <div class="fieldrow"><label for="s1prop60">Plane 1 propellant required (kg)</label><input type="number" id="s1prop60" step="0.01"><span id="fb1d" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Cost and coverage decision (D4)</h4>
    <div class="goal">Using Step 1's feasibility results across all six groups, find how many of Solara's 60 satellites Option A actually places, each option's total launch cost, and each option's satellites-correctly-placed-per-dollar.</div>
    <div class="fieldrow"><label for="s2placedA">Option A: satellites correctly placed</label><input type="number" id="s2placedA" step="1"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2costA">Option A: total launch cost ($)</label><input type="number" id="s2costA" step="1000"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2costB">Option B: total launch cost ($)</label><input type="number" id="s2costB" step="1000"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>
"""

REPL["{{CASE_TWIST_NARRATIVE}}"] = """
      <p>SpaceX's account rep calls with the next rideshare price step &mdash; following the real, repeated historical pattern of roughly $500-$1,000/kg increases ($5,500/kg in 2019, $6,500/kg in 2023, $7,000/kg in 2026), a hypothetical next jump to <strong>$9,000/kg</strong> is announced as the price Solara's launch would actually be booked at.</p>
"""
REPL["{{CASE_TWIST_APPLY_LABEL}}"] = "Recompute Option A's cost at the twist rideshare price ($9,000/kg instead of $7,000/kg)"

REPL["{{CASE_SOURCES_LIST}}"] = """
      <li>[S1] Spaceflight Now &mdash; <a href="https://spaceflightnow.com/2019/04/30/fcc-approves-spacexs-plan-to-operate-starlink-satellites-at-lower-altitude/" target="_blank" rel="noopener">FCC approves SpaceX's plan to operate Starlink satellites at lower altitude</a> (2019-04-30)</li>
      <li>[S2] Standard combined plane-change formula &mdash; <a href="https://en.wikipedia.org/wiki/Orbital_inclination_change" target="_blank" rel="noopener">Orbital inclination change</a></li>
      <li>[S3] Busek Co. Inc. &mdash; <a href="https://www.busek.com/bit3" target="_blank" rel="noopener">BIT-3 RF Ion Thruster product page</a></li>
      <li>[S4] New Space Economy &mdash; <a href="https://newspaceeconomy.ca/2026/02/27/spacex-rideshare-pricing-as-of-february-2026-what-it-costs-whats-included-and-how-buyers-budget-a-mission/" target="_blank" rel="noopener">SpaceX Rideshare Pricing as of February 2026</a></li>
      <li>[S5] SpaceNexus &mdash; <a href="https://spacenexus.us/rockets/electron" target="_blank" rel="noopener">Electron: Launch Cost, Next Launch, Specs &amp; Record (2026)</a></li>
"""

# ---------------------------------------------------------------- JS data
REPL["{{CASE_JS_DATA_BLOCK}}"] = """
// Ported from cases/the-constellation-bid/sensitivity_model.py
// sha256(case.md) = ae744b63f768303bb0ca1f9214279c025747b668e03c4fca4a8621c08cf4bd53
const PARAMS = {
  isp_s: 2150.0, g0_ms2: 9.80665,
  rideshare_base_usd: 350000.0, rideshare_base_kg: 50.0, rideshare_rate_usd_per_kg: 7000.0,
  electron_price_usd: 7500000.0,
  n_satellites: 60, n_planes: 6, sats_per_plane: 10,
  mu_km3s2: 398600.4418,
  altitude_km: 550.0, wet_mass_kg: 15.0, propellant_allowance_kg: 4.0,
  twist_rideshare_rate_usd_per_kg: 9000.0,
};
const FLEX = ["altitude_km", "wet_mass_kg", "propellant_allowance_kg"];
const GROUPS = [[0,10],[60,10],[120,10],[180,10],[120,10],[60,10]];

function orbitalSpeedMs(p){
  const rKm = 6371.0 + p.altitude_km;
  return Math.sqrt(p.mu_km3s2 / rKm) * 1000.0;
}
function propellantPerMs(p){ return p.wet_mass_kg / (p.isp_s * p.g0_ms2); }

function optionA(p, rideshareRate){
  const v = orbitalSpeedMs(p);
  const propPerMs = propellantPerMs(p);
  let placed = 0;
  for(const [thetaDeg, n] of GROUPS){
    const dv = 2.0 * v * Math.sin((thetaDeg/2.0) * Math.PI/180.0);
    const propNeeded = dv * propPerMs;
    if(propNeeded <= p.propellant_allowance_kg) placed += n;
  }
  const totalMass = p.n_satellites * p.wet_mass_kg;
  const rate = (rideshareRate === undefined) ? p.rideshare_rate_usd_per_kg : rideshareRate;
  const cost = p.rideshare_base_usd + rate * Math.max(0, totalMass - p.rideshare_base_kg);
  return {placed, cost};
}
function optionB(p){
  return {placed: p.n_satellites, cost: p.n_planes * p.electron_price_usd};
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const a = optionA(p), b = optionB(p);
  return {A: a.placed/a.cost, B: b.placed/b.cost, placedA: a.placed, costA: a.cost, placedB: b.placed, costB: b.cost};
}
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  const a = optionA(p, p.twist_rideshare_rate_usd_per_kg), b = optionB(p);
  return {A: a.placed/a.cost, B: b.placed/b.cost, placedA: a.placed, costA: a.cost, placedB: b.placed, costB: b.cost};
}
"""

REPL["{{CASE_NOTEBOOK_CHECK_FUNCTIONS}}"] = """
function checkStep1(){
  const r = evaluate();
  const v = orbitalSpeedMs(PARAMS);
  const propPerMs = propellantPerMs(PARAMS);
  const dv180 = 2.0*v*Math.sin(90*Math.PI/180.0);
  const prop180 = dv180*propPerMs;
  const dv60 = 2.0*v*Math.sin(30*Math.PI/180.0);
  const prop60 = dv60*propPerMs;
  fb('fb1a', near(parseFloat(val('s1sin180')), 1.0, 0.01));
  fb('fb1b', near(parseFloat(val('s1dv180')), dv180, 5));
  fb('fb1c', near(parseFloat(val('s1prop180')), prop180, 0.05));
  fb('fb1d', near(parseFloat(val('s1prop60')), prop60, 0.05));
}
function checkStep2(){
  const twistApplied = window.__TWIST_APPLIED__;
  const r = twistApplied ? evaluate_twist() : evaluate();
  fb('fb2a', near(parseFloat(val('s2placedA')), r.placedA, 0.5));
  fb('fb2b', near(parseFloat(val('s2costA')), r.costA, 1000));
  fb('fb2c', near(parseFloat(val('s2costB')), r.costB, 1000));
}
"""

REPL["{{CASE_ON_TWIST_TOGGLE_FUNCTION}}"] = """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
document.getElementById('storyGlossaryGrid').innerHTML = Object.keys(STORY_GLOSSARY).map(k => stermHTML(k)).join('');
"""

REPL["{{CASE_GLOSSARY_OBJECT}}"] = """{
  "Unit Circle": {def: "A circle of radius 1 centered at the origin, used to define sine, cosine, and tangent for any angle.",
    url: "https://www.mathsisfun.com/geometry/unit-circle.html"},
  "Tangent Function": {def: "The trig ratio equal to sine divided by cosine -- also the slope of the line of sight at an angle.",
    url: "https://www.mathsisfun.com/geometry/tangent-line.html"},
  "Sine Function": {def: "A trig function giving the vertical (y) coordinate of a point on the unit circle at a given angle.",
    url: "https://www.mathsisfun.com/algebra/trig-sine-law.html"},
  "Cosine Function": {def: "A trig function giving the horizontal (x) coordinate of a point on the unit circle at a given angle.",
    url: "https://www.mathsisfun.com/algebra/trig-cosine-law.html"},
  "Radian": {def: "A unit of angle measure: the angle where the arc length equals the circle's radius -- 2\\u03c0 radians = 360\\u00b0.",
    url: "https://www.mathsisfun.com/geometry/radians.html"},
  "Circumference": {def: "The distance all the way around a circle, found as 2\\u03c0r.",
    url: "https://www.mathsisfun.com/geometry/circumference.html"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.mathsisfun.com/definitions/ratio.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.mathsisfun.com/percentage.html"}
}"""

REPL["{{CASE_HOWTO_ARRAY}}"] = """[
  ["how to find the sine, cosine, and tangent of an angle using the unit circle", "Unit Circle"],
  ["how to convert between degrees and radians", "Radian"],
  ["how to find the measure of the circumference of a circle", "Circumference"]
]"""

REPL["{{CASE_STORY_GLOSSARY_BLOCK}}"] = """
const STORY_GLOSSARY = {
  "RAAN": {desc: "Right ascension of ascending node -- the angle, measured around the equator, marking where a satellite's orbit crosses from south to north. It says which way a given orbital plane is rotated.",
    link: "https://en.wikipedia.org/wiki/Orbital_node"},
  "Delta-v": {desc: "Engineers' standard way of measuring how big a maneuver is: the total change in velocity a burn requires, independent of the spacecraft's actual mass.",
    link: "https://en.wikipedia.org/wiki/Delta-v"},
  "Specific impulse": {desc: "A standard measure of how efficiently a thruster converts propellant into thrust -- higher means more push per kilogram spent.",
    link: "https://en.wikipedia.org/wiki/Specific_impulse"},
  "Ion thruster": {desc: "A small electric engine that produces thrust by accelerating a stream of charged propellant particles, rather than burning chemical fuel.",
    link: "https://en.wikipedia.org/wiki/Ion_thruster"},
  "J2 perturbation": {desc: "Earth's slight equatorial bulge slowly rotates every satellite's orbital plane over time, for free -- real operators often use this natural drift instead of a direct burn.",
    link: "https://en.wikipedia.org/wiki/Nodal_precession"},
  "Sun-synchronous orbit": {desc: "An orbit shaped so a satellite crosses any given point on Earth at the same local time every day.",
    link: "https://en.wikipedia.org/wiki/Sun-synchronous_orbit"},
  "Rideshare launch": {desc: "A launch that splits one rocket's total capacity across many different customers' satellites, which is cheaper per kilogram because the rocket's fixed cost is shared.",
    link: "https://en.wikipedia.org/wiki/Rideshare_(aerospace)"},
  "Walker constellation": {desc: "A standard way of arranging a satellite constellation into evenly-spaced orbital planes so satellites are spread out for continuous coverage.",
    link: "https://en.wikipedia.org/wiki/Satellite_constellation"},
  "Launch-slot deposit": {desc: "A payment an operator puts down to reserve a spot on a specific future rocket launch, typically nonrefundable once paid.",
    link: "https://en.wikipedia.org/wiki/Commercial_use_of_space"}
};
function stermHTML(label, textOverride){
  const g = STORY_GLOSSARY[label];
  if(!g) return textOverride || label;
  const text = textOverride || label;
  return `<a class="sterm gterm" data-term="${label}" href="${g.link}" target="_blank" rel="noopener">${text}<span class="tip">${g.desc}<span class="go">Learn more &rarr;</span></span></a>`;
}
"""

REPL["{{CASE_JS_DATA_BLOCK}}"] = REPL["{{CASE_JS_DATA_BLOCK}}"] + "\n" + REPL["{{CASE_STORY_GLOSSARY_BLOCK}}"]
del REPL["{{CASE_STORY_GLOSSARY_BLOCK}}"]

for k, v in REPL.items():
    if k not in html:
        raise SystemExit(f"MISSING PLACEHOLDER IN SHELL: {k}")
    html = html.replace(k, v)

leftover = [m for m in re.findall(r'\{\{[A-Z_]+\}\}', html) if m != '{{PLACEHOLDER}}']
if leftover:
    raise SystemExit(f"Unfilled placeholders remain: {leftover}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print("wrote", OUT)
