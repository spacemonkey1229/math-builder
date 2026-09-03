CONFIG = {
    "strand_summary": "Exponents &middot; Order of Operations",
    "protagonist": "Sam Okafor",
    "option_a_label": "The Near-Term Register",
    "option_a_text": "20 qubits, cheaper and inside this quarter's budget, but its 2&sup2;&#8304; state space can't fully represent the client's 24-variable problem, forcing a classical-heuristic approximation on 4 of the lanes.",
    "option_b_label": "The Full Register",
    "option_b_text": "24 qubits, whose 2&sup2;&#8308; state space represents the client's problem exactly, but real published hardware error rates compound faster as circuit width grows, and cloud-quantum time is billed per shot regardless of whether that shot lands below the error threshold.",
    "challenge3_summary": "Include: <strong>D1</strong> a state-space computation (2&sup2;&#8304; and 2&sup2;&#8308;, and their ratio as a single power of 2); <strong>D2</strong> a circuit gate-count table at 20 and 24 qubits; <strong>D3</strong> a below-threshold success-probability computation for each register size; <strong>D4</strong> a cost-per-successful-shot table and percent margin; <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "State-space computation (2^20 vs 2^24, ratio as a power of 2)"],
        ["D2", "Circuit gate-count table at 20 and 24 qubits"],
        ["D3", "Below-threshold success-probability computation, both register sizes"],
        ["D4", "Cost-per-successful-shot table and percent margin"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Below-threshold success probability (D1&ndash;D3)</h4>
    <div class="goal">Using Appendix D's calibrated gate-count model (gates(N) = 10 &times; N two-qubit gates) and the real published median two-qubit gate error rate (Appendix D/S2), compute the number of two-qubit gates and the below-threshold success probability F(N) = (1 &minus; gate error rate)^(gates) for a register of your chosen size. Order of operations matters: the parenthesized subtraction happens before the exponent.</div>
    <div class="fieldrow">
      <label for="s1n">Register size, N (qubits)</label>
      <select id="s1n"><option value="20">20 (Option A)</option><option value="24">24 (Option B)</option></select>
    </div>
    <div class="fieldrow"><label for="s1gates">Two-qubit gates, gates(N)</label><input type="number" id="s1gates" step="1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1prob">Success probability F(N)</label><input type="number" id="s1prob" step="0.0001"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Cost per successful shot and the margin (D4&ndash;D5)</h4>
    <div class="goal">Using Appendix B/C's per-shot price and your Step 1 success probabilities for <em>both</em> register sizes, compute dollars per successfully-completed shot for each option, then the percent margin between them. (Effective price also folds in Appendix B/C's per-task fee, spread across IonQ's stated minimum shots/task &mdash; see Appendix F.)</div>
    <div class="fieldrow"><label for="s2costA">Option A cost / successful shot (USD)</label><input type="number" id="s2costA" step="0.0001"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2costB">Option B cost / successful shot (USD)</label><input type="number" id="s2costB" step="0.0001"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Percent margin between them</label><input type="number" id="s2margin" step="0.01"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">The notebook checks your arithmetic. It does not tell you which register size to recommend &mdash; that's D5.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>One more real number. IonQ's own benchmark paper &mdash; the same one your Appendix D numbers come from &mdash; says something else: their published gate-count model, the one <em>they</em> use to certify a circuit width as "working," isn't the simple one this case gave you. It's not 10 gates per qubit. It's qubits, squared.</p>
      <p>If you recompute using qubit-count-squared instead of the calibrated model in Appendix D &mdash; 200 gates at 20 qubits becomes 400, and 240 gates at 24 qubits becomes 576 &mdash; does Option A still win? By how much? And does that change what you'd tell the CFO &mdash; not which box to pick, but how confident you'd sound saying it?</p>
""",
    "twist_apply_label": "Recompute Step 1/2 using gates(N) = N&sup2; instead of 10N",
    "js_data_block": """
const PARAMS = {
  n_a: 20.0, n_b: 24.0,
  gate_error_rate: 0.00464,
  gates_per_qubit: 10.0,
  price_per_shot: 0.08,
  price_per_task: 0.30,
  shots_per_task: 2500.0,
};
function successProbability(nQubits, p, gatesPerQubitOverride){
  const gpq = (gatesPerQubitOverride !== undefined) ? gatesPerQubitOverride : p.gates_per_qubit;
  const gates = gpq * nQubits;
  return Math.pow(1 - p.gate_error_rate, gates);
}
function costPerSuccessfulShot(nQubits, p, gatesPerQubitOverride){
  const f = successProbability(nQubits, p, gatesPerQubitOverride);
  const effectivePrice = p.price_per_shot + (p.price_per_task / p.shots_per_task);
  return effectivePrice / f;
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const costA = costPerSuccessfulShot(p.n_a, p);
  const costB = costPerSuccessfulShot(p.n_b, p);
  return {A: -costA, B: -costB};
}
// Twist: gates(N) = N^2 (IonQ's own #AQ worst-case formula) instead of gates_per_qubit * N
function evaluate_twist(params){
  const p = Object.assign({}, PARAMS, params||{});
  const fA = Math.pow(1 - p.gate_error_rate, p.n_a * p.n_a);
  const fB = Math.pow(1 - p.gate_error_rate, p.n_b * p.n_b);
  const effectivePrice = p.price_per_shot + (p.price_per_task / p.shots_per_task);
  return {A: -(effectivePrice / fA), B: -(effectivePrice / fB)};
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const n = parseFloat(val('s1n'));
  const gatesEntered = parseFloat(val('s1gates'));
  const probEntered = parseFloat(val('s1prob'));
  const trueGates = PARAMS.gates_per_qubit * n;
  const trueProb = successProbability(n, PARAMS);
  const okGates = near(gatesEntered, trueGates, 0.5);
  const okProb = near(probEntered, trueProb, 0.001);
  fb('fb1a', okGates);
  fb('fb1b', okProb);
}
function checkStep2(){
  const costA = parseFloat(val('s2costA'));
  const costB = parseFloat(val('s2costB'));
  const marginEntered = parseFloat(val('s2margin'));
  const trueCostA = costPerSuccessfulShot(PARAMS.n_a, PARAMS);
  const trueCostB = costPerSuccessfulShot(PARAMS.n_b, PARAMS);
  const trueMargin = 100 * Math.abs(trueCostB - trueCostA) / Math.max(trueCostA, trueCostB);
  fb('fb2a', near(costA, trueCostA, 0.002));
  fb('fb2b', near(costB, trueCostB, 0.002));
  fb('fb2c', near(marginEntered, trueMargin, 1.0));
}
""",
    "glossary_js": """{
  "Exponent": {def: "A small raised number showing how many times to multiply a base by itself, e.g. the 3 in 2\\u00b3.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals"},
  "Base": {def: "The number being multiplied repeatedly in an exponential expression, e.g. the 2 in 2\\u00b3.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-exponents-radicals"},
  "Order of Operations": {def: "The agreed sequence for evaluating a multi-step expression: parentheses, exponents, multiplication/division, addition/subtraction.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-arith-review/pre-algebra-order-of-operations/a/order-of-operations-review"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Probability": {def: "A number between 0 and 1 describing how likely an event is to happen.",
    url: "https://www.khanacademy.org/math/statistics-probability/probability-library"},
  "Scientific Notation": {def: "A compact way to write very large or very small numbers: a number from 1-10 times a power of 10.",
    url: "https://www.khanacademy.org/math/8th-grade-illustrative-math/unit-7-exponents-and-scientific-notation"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"}
}""",
    "howto_js": """[
  ["how to evaluate an exponential expression", "Exponent"],
  ["how to evaluate an expression with multiple operations with exponents (order of operations)", "Order of Operations"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  // Re-run Step 1/2's own checks under the twist's gates(N)=N^2 model instead
  // of the calibrated linear model -- does not print any verdict, just lets
  // the notebook's existing Check buttons grade against the twist model too.
  const applied = document.getElementById('applyTwist').checked;
  window.__TWIST_APPLIED__ = applied;
}
""",
}
