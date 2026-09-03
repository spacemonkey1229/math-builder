CONFIG = {
    "strand_summary": "Scientific Notation &middot; Absolute Value",
    "protagonist": "Priya Nathan",
    "option_a_label": "The Short Ladder",
    "option_a_text": "Roll reserves almost entirely into 4-week Treasury bills, minimizing how far the reserve price can ever drift from $1.00.",
    "option_b_label": "The Extended Ladder",
    "option_b_text": "Shift part of the reserve into 6-week Treasury bills &mdash; a real, meaningfully longer maturity than the Short Ladder, still well inside the GENIUS Act's 93-day ceiling &mdash; for more yield.",
    "challenge3_summary": "Include: <strong>D1</strong> a scientific-notation reserve &amp; yield table; <strong>D2</strong> an absolute-value peg-deviation worksheet on Appendix D's five snapshots; <strong>D3</strong> a yield-per-risk efficiency table (dollars of annual yield per basis point of duration-scaled risk) and its percent difference; <strong>D4</strong> a sensitivity check rerunning D3 under Appendix E's alternate scaling readings; <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Scientific-notation reserve & yield table"],
        ["D2", "Absolute-value peg-deviation worksheet (5 snapshots)"],
        ["D3", "Yield-per-risk efficiency table and percent difference"],
        ["D4", "Sensitivity check under Appendix E's alternate readings"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Scientific notation (D1)</h4>
    <div class="goal">Write Northlight's total reserve amount (Appendix A) in scientific notation, as a mantissa (1&ndash;10) and a power-of-10 exponent. Then compute each option's total annual dollar yield (reserve total &times; annual yield rate, Appendix B/C).</div>
    <div class="fieldrow"><label for="s1mant">Reserve total, mantissa (1&ndash;10)</label><input type="number" id="s1mant" step="0.0001"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1exp">Reserve total, power of 10</label><input type="number" id="s1exp" step="1"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1yA">Option A annual yield (USD)</label><input type="number" id="s1yA" step="1"><span id="fb1c" class="fb"></span></div>
    <div class="fieldrow"><label for="s1yB">Option B annual yield (USD)</label><input type="number" id="s1yB" step="1"><span id="fb1d" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Peg deviation and the efficiency ratio (D2&ndash;D3)</h4>
    <div class="goal">Using Appendix E's primary (square-root-of-time) reading, compute Option B's duration-scaled peg-deviation figure in basis points, then divide each option's annual yield (Step 1) by its deviation in basis points to get dollars of annual yield per basis point of risk. State the percent difference.</div>
    <div class="fieldrow"><label for="s2devb">Option B risk figure, primary reading (bps)</label><input type="number" id="s2devb" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2effA">Option A efficiency ($ per bp)</label><input type="number" id="s2effA" step="1"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2effB">Option B efficiency ($ per bp), primary reading</label><input type="number" id="s2effB" step="1"><span id="fb2c" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Percent difference between the two efficiencies</label><input type="number" id="s2margin" step="0.01"><span id="fb2d" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 3 &mdash; Sensitivity check (D4)</h4>
    <div class="goal">Appendix E gives two alternate ways to derive Option B's risk figure: linear duration scaling, and a "no extra risk" floor case. Recompute the margin under each. Does the recommendation change under either one?</div>
    <div class="fieldrow"><label for="s3marginLinear">Margin under linear scaling (%)</label><input type="number" id="s3marginLinear" step="0.01"><span id="fb3a" class="fb"></span></div>
    <div class="fieldrow"><label for="s3marginFloor">Margin under the floor case (%)</label><input type="number" id="s3marginFloor" step="0.01"><span id="fb3b" class="fb"></span></div>
    <button onclick="checkStep3()">Check</button>
    <p class="side-note">The notebook checks your arithmetic. It does not tell you which ladder to recommend &mdash; that's D5.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>One more real number, spelled out. Option B's risk figure in Appendix E was never measured &mdash; it was <em>derived</em>, by scaling Option A's real 30 bps reference using one particular method (the square-root-of-time rule). There is another real, defensible method for doing that same scaling, and a third, more conservative reading that assumes no extra risk at all from the longer duration.</p>
      <p>Rerun Step 2's efficiency numbers using each of Appendix E's alternate readings (Step 3 above). Does your recommendation change? Which real, defensible assumption are you actually trusting when you pick a winner?</p>
""",
    "twist_apply_label": "Recompute Step 2 using the floor-case reading (no incremental duration risk) instead of square-root-of-time",
    "js_data_block": """
const PARAMS = {
  reserve_total: 73434000000.0,
  yield_a_rate: 0.0375,
  yield_b_rate: 0.0381,
  dev_a_bps: 30.0,
  duration_a_days: 28.0,
  duration_b_days: 42.0,
  dev_b_scaling_exponent: 0.5,
};
function evaluateFull(params, scalingExponent){
  const p = Object.assign({}, PARAMS, params||{});
  const exponent = (scalingExponent === undefined) ? p.dev_b_scaling_exponent : scalingExponent;
  const ratio = p.duration_b_days / p.duration_a_days;
  const devBbps = p.dev_a_bps * Math.pow(ratio, exponent);
  const yieldA = p.reserve_total * p.yield_a_rate;
  const yieldB = p.reserve_total * p.yield_b_rate;
  const effA = yieldA / p.dev_a_bps;
  const effB = yieldB / devBbps;
  return {metrics: {A: effA, B: effB}, yieldA: yieldA, yieldB: yieldB, devBbps: devBbps};
}
function evaluate(params){
  return evaluateFull(params).metrics;
}
// Twist / D4: same formula, alternate scaling exponent (1.0 = linear, 0.0 = floor case)
function evaluate_twist(params){
  return evaluateFull(Object.assign({}, params, {dev_b_scaling_exponent: 0.0})).metrics;
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const mant = parseFloat(val('s1mant'));
  const exp = parseFloat(val('s1exp'));
  const yA = parseFloat(val('s1yA'));
  const yB = parseFloat(val('s1yB'));
  const trueMant = 7.3434, trueExp = 10;
  const full = evaluateFull({});
  fb('fb1a', near(mant, trueMant, 0.001));
  fb('fb1b', near(exp, trueExp, 0));
  fb('fb1c', near(yA, full.yieldA, 1000));
  fb('fb1d', near(yB, full.yieldB, 1000));
}
function checkStep2(){
  const devb = parseFloat(val('s2devb'));
  const effA = parseFloat(val('s2effA'));
  const effB = parseFloat(val('s2effB'));
  const marginEntered = parseFloat(val('s2margin'));
  const full = evaluateFull({});
  const trueMargin = 100 * (full.metrics.A - full.metrics.B) / full.metrics.A;
  fb('fb2a', near(devb, full.devBbps, 0.05));
  fb('fb2b', near(effA, full.metrics.A, 1000));
  fb('fb2c', near(effB, full.metrics.B, 1000));
  fb('fb2d', near(marginEntered, trueMargin, 0.5));
}
function checkStep3(){
  const marginLinear = parseFloat(val('s3marginLinear'));
  const marginFloor = parseFloat(val('s3marginFloor'));
  const linear = evaluateFull({}, 1.0).metrics;
  const floor = evaluateFull({}, 0.0).metrics;
  const trueLinear = 100 * (linear.A - linear.B) / linear.A;
  const trueFloor = 100 * (floor.B - floor.A) / floor.B; // floor case: B wins
  fb('fb3a', near(marginLinear, trueLinear, 0.5));
  fb('fb3b', near(marginFloor, Math.abs(trueFloor), 0.5));
}
""",
    "glossary_js": """{
  "Scientific Notation": {def: "A compact way to write very large or very small numbers: a number from 1-10 times a power of 10.",
    url: "https://www.khanacademy.org/math/8th-grade-illustrative-math/unit-7-exponents-and-scientific-notation"},
  "Absolute Value": {def: "How far a number is from zero on the number line -- always zero or positive.",
    url: "https://www.khanacademy.org/math/algebra-home/alg-absolute-value"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"},
  "Exponent": {def: "A small raised number showing how many times to multiply a base by itself, e.g. the 3 in 2\\u00b3.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals"},
  "Base": {def: "The number being multiplied repeatedly in an exponential expression, e.g. the 2 in 2\\u00b3.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals"},
  "Square Root": {def: "A value that, multiplied by itself, gives the original number -- the square root of 9 is 3.",
    url: "https://www.mathsisfun.com/square-root.html"}
}""",
    "howto_js": """[
  ["how to write a number in scientific notation given its standard notation", "Scientific Notation"],
  ["how to evaluate an absolute value expression", "Absolute Value"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  // Re-run Step 2/3's own checks under the floor-case reading (exponent=0)
  // instead of the primary square-root-of-time reading -- does not print
  // any verdict, just lets the notebook's existing Check buttons grade
  // against the twist model too.
  const applied = document.getElementById('applyTwist').checked;
  window.__TWIST_APPLIED__ = applied;
}
""",
}
