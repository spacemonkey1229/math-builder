CONFIG = {
    "strand_summary": "Matrices &middot; Ratios",
    "protagonist": "Aisha",
    "option_a_label": "Suspend Ring Alpha",
    "option_a_text": "A dense connection matrix flagged by connectivity-based detection, with a real published detection-accuracy range behind the modeled false-positive rate.",
    "option_b_label": "Suspend Wave Nine",
    "option_b_text": "A high-volume posting cluster flagged by content/volume-based detection during the platform's highest-traffic surge weekend, when that detection method has a real, documented weak point.",
    "challenge3_summary": "Include: <strong>D1</strong> Ring Alpha's connection matrix and its density; <strong>D2</strong> Wave Nine's posting-volume comparison against the real published rate ceiling; <strong>D3</strong> each cluster's modeled false-positive rate and its sourcing; <strong>D4</strong> the confirmed-bots-per-false-positive ratio for both clusters; <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Ring Alpha connection matrix and density"],
        ["D2", "Wave Nine posting-volume comparison"],
        ["D3", "Each cluster's modeled false-positive rate"],
        ["D4", "Confirmed-bots-per-false-positive ratio, both clusters"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; False positives and confirmed bots for one cluster (D3&ndash;D4)</h4>
    <div class="goal">Using Appendix A's flagged-account count and Appendix E's modeled false-positive rate for a cluster, compute the number of false positives (flagged &times; FP rate) and confirmed bots (flagged &times; (1 &minus; FP rate)).</div>
    <div class="fieldrow">
      <label for="s1cluster">Cluster</label>
      <select id="s1cluster"><option value="A">Ring Alpha</option><option value="B">Wave Nine</option></select>
    </div>
    <div class="fieldrow"><label for="s1fp">False positives</label><input type="number" id="s1fp" step="0.1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1conf">Confirmed bots</label><input type="number" id="s1conf" step="0.1"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; The primary metric: confirmed bots per false positive (D4&ndash;D5)</h4>
    <div class="goal">For BOTH clusters, compute the ratio of confirmed bots to false positives. A higher ratio means fewer innocent accounts get suspended per confirmed bot removed.</div>
    <div class="fieldrow"><label for="s2ratioA">Ring Alpha ratio</label><input type="number" id="s2ratioA" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2ratioB">Wave Nine ratio</label><input type="number" id="s2ratioB" step="0.01"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">Notice which numbers from Appendix A cancel out of this ratio entirely. Does cluster size matter to your recommendation, or only the false-positive rate?</p>
  </div>
""",
    "twist_narrative_html": """
      <p>The surge subsides. It's six hours later, traffic is back to normal, and the incident review board wants the numbers recomputed under <em>ordinary</em>, non-surge conditions &mdash; the real, unscaled academic baseline false-positive rate (Appendix D/S1: 15%) for BOTH clusters, no surge premium on Wave Nine.</p>
      <p>Recompute Step 1/2 for both clusters at the real 15% baseline rate. Does the recommendation change? Was the original call wrong &mdash; or was it right for conditions that no longer apply?</p>
""",
    "twist_apply_label": "Recompute both clusters at the real unscaled 15% baseline (no surge premium)",
    "js_data_block": """
const PARAMS = { flagged_a: 250.0, flagged_b: 200.0, fpr_a: 0.20, fpr_b: 0.225 };
function optionDetail(flagged, fpr){
  const falsePositives = flagged * fpr;
  const confirmedBots = flagged * (1 - fpr);
  return {falsePositives, confirmedBots, ratio: confirmedBots / falsePositives};
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const a = optionDetail(p.flagged_a, p.fpr_a);
  const b = optionDetail(p.flagged_b, p.fpr_b);
  return {A: a.ratio, B: b.ratio};
}
function evaluate_twist(params){
  return evaluate(Object.assign({fpr_a: 0.15, fpr_b: 0.15}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {fpr_a:0.15, fpr_b:0.15}) : PARAMS;
  const cluster = val('s1cluster');
  const flagged = cluster === 'A' ? p.flagged_a : p.flagged_b;
  const fpr = cluster === 'A' ? p.fpr_a : p.fpr_b;
  const d = optionDetail(flagged, fpr);
  fb('fb1a', near(parseFloat(val('s1fp')), d.falsePositives, 0.5));
  fb('fb1b', near(parseFloat(val('s1conf')), d.confirmedBots, 0.5));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {fpr_a:0.15, fpr_b:0.15}) : PARAMS;
  const r = evaluate(p);
  fb('fb2a', near(parseFloat(val('s2ratioA')), r.A, 0.05));
  fb('fb2b', near(parseFloat(val('s2ratioB')), r.B, 0.05));
}
""",
    "glossary_js": """{
  "Matrix": {def: "A rectangular array of numbers arranged in rows and columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Matrix Dimension": {def: "The size of a matrix, written rows x columns.",
    url: "https://www.mathsisfun.com/algebra/matrix-introduction.html"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Probability": {def: "A number between 0 and 1 describing how likely an event is to happen.",
    url: "https://www.khanacademy.org/math/statistics-probability/probability-library"},
  "Rate": {def: "A ratio that compares two quantities with different units, like posts per hour.",
    url: "https://www.khanacademy.org/math/pre-algebra/pre-algebra-ratios-rates"},
  "Data": {def: "Facts or numbers collected for reference or analysis.",
    url: "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"}
}""",
    "howto_js": """[
  ["how to add and multiply matrices", "Matrix"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
