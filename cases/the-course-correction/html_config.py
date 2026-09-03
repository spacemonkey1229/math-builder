CONFIG = {
    "strand_summary": "Vectors &middot; Dot Product",
    "protagonist": "the officer of the watch",
    "option_a_label": "The True Line",
    "option_a_text": "Correct the heading for the measured current's cross-track effect, using vector math to find the exact boat speed and heading that gets to the buoy inside the weather window.",
    "option_b_label": "The Steady Burn",
    "option_b_text": "Hold the cheapest point on the real fuel curve and accept the current's drift, correcting course only at the end.",
    "challenge3_summary": "Include: <strong>D1</strong> the rendezvous vector, and the current vector resolved into components; <strong>D2</strong> Option A's required boat speed and heading (vector subtraction); <strong>D3</strong> Option B's along-track/cross-track decomposition (dot product) and the resulting extra distance; <strong>D4</strong> a $/nm cost comparison using Appendix C/D's fuel curve and price; <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Rendezvous and current vectors, resolved into components"],
        ["D2", "Option A's required boat speed and heading"],
        ["D3", "Option B's along-track/cross-track decomposition (dot product)"],
        ["D4", "$/nm cost comparison, both options"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Resolve the current vector into components (D1)</h4>
    <div class="goal">Appendix B gives the real measured current's speed and direction it flows TOWARD. Using standard nautical-bearing components (x = speed &times; sin(bearing), y = speed &times; cos(bearing)), resolve the current into its x/y components, first converting its speed from cm/s to knots (Appendix B/S4, 1 kt = 51.4444 cm/s).</div>
    <div class="fieldrow"><label for="s1cx">Current x-component (kt)</label><input type="number" id="s1cx" step="0.001"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1cy">Current y-component (kt)</label><input type="number" id="s1cy" step="0.001"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Cost per nautical mile, both options (D2&ndash;D5)</h4>
    <div class="goal">Option A: subtract the current vector from the required over-ground velocity vector to find the boat's own required heading vector, then its speed &mdash; look up the fuel rate at that speed (Appendix C) and compute cost per nm. Option B: hold Appendix C's economical speed and heading, use the dot product to split the resultant velocity into along-track and cross-track components, find the extra distance/time the cross-track drift costs, and compute cost per nm the same way.</div>
    <div class="fieldrow"><label for="s2costA">Option A: $/nm</label><input type="number" id="s2costA" step="0.001"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2costB">Option B: $/nm</label><input type="number" id="s2costB" step="0.001"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Percent margin</label><input type="number" id="s2margin" step="0.01"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">Does Option B's schedule still make the weather window, or does the cross-track drift push it past 3 hours?</p>
  </div>
""",
    "twist_narrative_html": """
      <p>New forecast update: the closing weather window isn't 3.0 hours anymore &mdash; conditions are worsening faster than expected, and the window is now 2.0 hours.</p>
      <p>Recompute Step 2 for both options under the tighter window. Does the $/nm winner change? What happens to Option B's chance of actually making it in time?</p>
""",
    "twist_apply_label": "Recompute using a 2.0-hour weather window instead of 3.0",
    "js_data_block": """
const GAL_PER_KT_KTS = 51.4444;
const PARAMS = {
  distance_nm: 27.0, course_deg: 250.0, window_hr: 3.0,
  current_speed_cm_s: 27.0, current_toward_deg: 340.0,
  boat_speed_b_kt: 8.5,
  fuel_pt_lo_kt: 8.5, fuel_pt_lo_gph: 19.0,
  fuel_pt_mid_kt: 9.5, fuel_pt_mid_gph: 32.0,
  fuel_pt_hi_kt: 11.5, fuel_pt_hi_gph: 60.0,
  price_per_gal: 5.599,
};
function vecOf(mag, deg){
  const r = deg * Math.PI / 180;
  return [mag * Math.sin(r), mag * Math.cos(r)];
}
function dotOf(a, b){ return a[0]*b[0] + a[1]*b[1]; }
function interpFuelGph(vKt, p){
  const pts = [[p.fuel_pt_lo_kt,p.fuel_pt_lo_gph],[p.fuel_pt_mid_kt,p.fuel_pt_mid_gph],[p.fuel_pt_hi_kt,p.fuel_pt_hi_gph]].sort((a,b)=>a[0]-b[0]);
  let v1,f1,v2,f2;
  if(vKt <= pts[0][0]){ [v1,f1]=pts[0]; [v2,f2]=pts[1]; }
  else if(vKt >= pts[2][0]){ [v1,f1]=pts[1]; [v2,f2]=pts[2]; }
  else {
    for(let i=0;i<2;i++){ if(pts[i][0]<=vKt && vKt<=pts[i+1][0]){ [v1,f1]=pts[i]; [v2,f2]=pts[i+1]; break; } }
  }
  const slope = (f2-f1)/(v2-v1);
  return f1 + slope*(vKt-v1);
}
function currentComponents(p){
  const Vc = p.current_speed_cm_s / GAL_PER_KT_KTS;
  return vecOf(Vc, p.current_toward_deg);
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const D = p.distance_nm, theta = p.course_deg, T = p.window_hr, price = p.price_per_gal;
  const currentVec = currentComponents(p);
  const u = vecOf(1.0, theta);
  const rTheta = theta * Math.PI/180;
  const uPerp = [Math.cos(rTheta), -Math.sin(rTheta)];

  // Option A
  const Rreq = D / T;
  const Ru = [Rreq*u[0], Rreq*u[1]];
  const H = [Ru[0]-currentVec[0], Ru[1]-currentVec[1]];
  const boatSpeedA = Math.hypot(H[0], H[1]);
  const fuelRateA = interpFuelGph(boatSpeedA, p);
  const timeA = D / Rreq;
  const costA = fuelRateA * timeA * price;
  const metricA = costA / D;

  // Option B
  const boatSpeedB = p.boat_speed_b_kt;
  const headingVecB = vecOf(boatSpeedB, theta);
  const resultantB = [headingVecB[0]+currentVec[0], headingVecB[1]+currentVec[1]];
  const alongB = dotOf(resultantB, u);
  const crossB = dotOf(resultantB, uPerp);
  const t1 = D / alongB;
  const crossOffset = crossB * t1;
  const extraLeg = Math.abs(crossOffset);
  const tExtra = extraLeg / boatSpeedB;
  const totalTimeB = t1 + tExtra;
  const fuelRateB = p.fuel_pt_lo_gph;
  const costB = fuelRateB * totalTimeB * price;
  const metricB = costB / D;

  return {A: -metricA, B: -metricB};
}
function evaluate_twist(params){
  return evaluate(Object.assign({window_hr: 2.0}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const cv = currentComponents(PARAMS);
  fb('fb1a', near(parseFloat(val('s1cx')), cv[0], 0.02));
  fb('fb1b', near(parseFloat(val('s1cy')), cv[1], 0.02));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {window_hr: 2.0}) : PARAMS;
  const r = evaluate(p);
  const costA = -r.A, costB = -r.B;
  const margin = 100 * Math.abs(costA - costB) / Math.max(costA, costB);
  fb('fb2a', near(parseFloat(val('s2costA')), costA, 0.02));
  fb('fb2b', near(parseFloat(val('s2costB')), costB, 0.02));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 1.0));
}
""",
    "glossary_js": """{
  "Vector": {def: "A quantity with both magnitude (size) and direction, usually drawn as an arrow.",
    url: "https://www.mathsisfun.com/algebra/vectors.html"},
  "Magnitude": {def: "The length or size of a vector, ignoring its direction.",
    url: "https://www.mathsisfun.com/algebra/vectors.html"},
  "Unit Vector": {def: "A vector with a magnitude of exactly 1, used to describe pure direction.",
    url: "https://www.mathsisfun.com/algebra/vectors.html"},
  "Dot Product": {def: "A way of multiplying two vectors that produces a single number, useful for finding one vector's component along another.",
    url: "https://www.mathsisfun.com/algebra/vectors-dot-product.html"},
  "Rate": {def: "A ratio that compares two quantities with different units, like gallons per hour.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Distance": {def: "How far apart two points or places are.",
    url: "https://www.khanacademy.org/math/cc-fifth-grade-math/imp-measurement-and-data-3"}
}""",
    "howto_js": """[
  ["how to find the magnitude and direction of a vector", "Vector"],
  ["how to add and subtract vectors", "Vector"],
  ["how to find the dot product of two vectors", "Dot Product"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
