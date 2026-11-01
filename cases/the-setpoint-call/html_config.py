CONFIG = {
    "strand_summary": "Derivatives &middot; Critical Points &middot; Optimization",
    "protagonist": "Marisol Feng",
    "option_a_label": "The Guarding Upgrade",
    "option_a_text": "Fund a guarding/interlock retrofit now to legally clear Line 3 for the calculus-derived cost-minimizing speed.",
    "option_b_label": "The Rated Cap",
    "option_b_text": "Hold Line 3 at its current manufacturer-rated maximum safe speed for the life of the contract, with no capital outlay.",
    "challenge3_summary": "Include: <strong>D1</strong> the cost-rate and time-per-bottle functions; <strong>D2</strong> the derivative and the calculus-optimal speed r*; <strong>D3</strong> total cost per bottle at r* versus at the rated cap; <strong>D4</strong> the retrofit's amortized cost; <strong>D5</strong> the total-cost comparison and recommendation.",
    "deliverables": [
        ["D1", "Cost-rate and time-per-bottle functions"],
        ["D2", "Derivative and calculus-optimal speed r*"],
        ["D3", "Total cost per bottle at r* and at the rated cap"],
        ["D4", "Retrofit cost amortized per bottle"],
        ["D5", "Total-cost comparison and recommendation"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; The calculus-optimal speed r* (D1&ndash;D2)</h4>
    <div class="goal">Using Appendix A's cost-rate function CR(r) = a + br and time-per-bottle function MPU(r) = 1/r + d, form TC(r) = CR(r)&times;MPU(r), take its derivative, set it to zero, and solve for the cost-minimizing speed r* = &radic;(a/(bd)).</div>
    <div class="fieldrow"><label for="s1rstar">Calculus-optimal speed r* (bottles/min)</label><input type="number" id="s1rstar" step="0.1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1tcstar">Total cost per bottle at r* ($)</label><input type="number" id="s1tcstar" step="0.0001"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; True total cost per bottle, each option (D3&ndash;D5)</h4>
    <div class="goal">Option B's total cost is just TC evaluated at Appendix B's rated safe-speed ceiling. Option A's total cost is TC(r*) PLUS the retrofit cost amortized over Appendix C's contract volume (U/Q). Compare the two and find the margin.</div>
    <div class="fieldrow"><label for="s2tcB">Option B: total cost per bottle at the rated cap ($)</label><input type="number" id="s2tcB" step="0.0001"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2totalA">Option A: true total cost per bottle, including amortized retrofit ($)</label><input type="number" id="s2totalA" step="0.0001"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Margin between the two options (percent)</label><input type="number" id="s2margin" step="0.1"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>
""",
    "twist_narrative_html": """
      <p>Corporate calls: the sports-drink brand has exercised a guaranteed volume-renewal option, tripling Line 3's total contract commitment. The retrofit's cost hasn't changed &mdash; but the number of bottles it gets spread across just did. Toggle the switch below to see what a 3&times; contract volume does to Option A's amortized cost (Option B's per-bottle rate never touches contract volume at all &mdash; it has no retrofit to amortize).</p>
""",
    "twist_apply_label": "Recompute Option A's amortized cost at 3&times; contract volume (30,000,000 bottles instead of 10,000,000)",
    "js_data_block": """
const PARAMS = { a: 0.90, b: 0.0004, d: 0.02, r_cap: 150.0, U: 44000.0, Q: 10000000.0 };
function rStar(p){ return Math.sqrt(p.a/(p.b*p.d)); }
function tc(r, p){ const cr = p.a + p.b*r; const mpu = 1.0/r + p.d; return cr*mpu; }
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const rstar = rStar(p);
  const tcStar = tc(rstar, p);
  const tcB = tc(p.r_cap, p);
  const totalA = tcStar + p.U/p.Q;
  const totalB = tcB;
  return {A: -totalA, B: -totalB, rstar, tcStar, tcB, totalA, totalB};
}
function evaluate_twist(params){
  // Twist triples Q for Option A's amortization only -- Option B is untouched.
  const p = Object.assign({}, PARAMS, params||{});
  const rstar = rStar(p);
  const tcStar = tc(rstar, p);
  const tcB = tc(p.r_cap, p);
  const totalA = tcStar + p.U/(p.Q*3.0);
  const totalB = tcB;
  return {A: -totalA, B: -totalB, rstar, tcStar, tcB, totalA, totalB};
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const r = evaluate(PARAMS);
  fb('fb1a', near(parseFloat(val('s1rstar')), r.rstar, 1));
  fb('fb1b', near(parseFloat(val('s1tcstar')), r.tcStar, 0.0005));
}
function checkStep2(){
  const r = window.__TWIST_APPLIED__ ? evaluate_twist(PARAMS) : evaluate(PARAMS);
  const lo = Math.min(r.totalA, r.totalB), hi = Math.max(r.totalA, r.totalB);
  const margin = lo ? 100.0*(hi-lo)/lo : 0;
  fb('fb2a', near(parseFloat(val('s2tcB')), r.tcB, 0.0005));
  fb('fb2b', near(parseFloat(val('s2totalA')), r.totalA, 0.0005));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 1));
}
""",
    "glossary_js": """{
  "Derivative": {def: "The instantaneous rate of change of a function -- used here to find the speed where total cost per bottle is minimized.",
    url: "https://www.mathsisfun.com/calculus/derivatives-introduction.html"},
  "Critical Point": {def: "A point where a function's derivative is zero or undefined -- a candidate for a maximum or minimum.",
    url: "https://www.mathsisfun.com/calculus/derivatives-introduction.html"},
  "Concavity": {def: "Whether a function curves upward (concave up, a minimum) or downward (concave down, a maximum) at a critical point.",
    url: "https://www.mathsisfun.com/calculus/continuity.html"},
  "Product Rule": {def: "The rule for differentiating a product of two functions: (fg)' = f'g + fg'.",
    url: "https://www.mathsisfun.com/calculus/derivatives-rules.html"},
  "Power Rule": {def: "The rule for differentiating a power of a variable: the derivative of x&#8319; is n&middot;x&#8319;&#8315;&sup1;.",
    url: "https://www.mathsisfun.com/calculus/derivatives-rules.html"},
  "Optimization": {def: "Using calculus to find the input that makes a function's output as large or as small as possible.",
    url: "https://www.mathsisfun.com/calculus/derivatives-introduction.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- used here to compare the two options' total costs.",
    url: "https://www.mathsisfun.com/definitions/percent.html"},
  "Rate": {def: "A ratio comparing two quantities with different units, such as dollars per minute or bottles per minute.",
    url: "https://www.mathsisfun.com/definitions/rate.html"}
}""",
    "howto_js": """[
  ["how to find a derivative using the power rule", "Power Rule"],
  ["how to use the product rule to differentiate a product of functions", "Product Rule"],
  ["how to find critical points of a function", "Critical Point"],
  ["how to use the first derivative test to classify a critical point", "Concavity"],
  ["how to solve an optimization problem using derivatives", "Optimization"],
  ["how to find the percent of a number", "Percent"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
