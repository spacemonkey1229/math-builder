CONFIG = {
    "strand_summary": "Sampling &middot; Standard Error &middot; Percent",
    "protagonist": "Derek Okafor",
    "option_a_label": "The Pooled Random Sample",
    "option_a_text": "One simple random sample of clicks drawn from the entire week's pooled stream, fast to set up but liable to draw almost nothing from the small Influencer/Affiliate channel.",
    "option_b_label": "The Channel-Stratified Sample",
    "option_b_text": "Four separate random samples, one guaranteed per channel including a real minimum for the small one, at the cost of more analyst setup time and a much tighter fit against the deadline.",
    "challenge3_summary": "Include: <strong>D1</strong> a Pooled Random Sample precision table (per-channel standard error); <strong>D2</strong> a Channel-Stratified Sample design (allocation and standard errors); <strong>D3</strong> an analyst-hours cost table for both options; <strong>D4</strong> a primary-metric comparison (pooled standard error per analyst-hour); <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Pooled Random Sample precision table (per-channel SE)"],
        ["D2", "Channel-Stratified Sample design (allocation, SE)"],
        ["D3", "Analyst-hours cost table, both options"],
        ["D4", "Primary-metric comparison (pooled SE per analyst-hour)"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Affiliate-channel standard error under each option (D1&ndash;D2)</h4>
    <div class="goal">The Influencer/Affiliate channel is only 2% of pooled clicks (Appendix A). Using Appendix A's channel share and Appendix D's per-channel true-install rate, compute the Affiliate channel's <em>expected sample size</em> under the Pooled Random Sample (share &times; 400), then its standard error, SE = &radic;(p(1&minus;p)/n). Then do the same under the Channel-Stratified Sample, where Affiliate gets a guaranteed floor sample instead (Appendix C).</div>
    <div class="fieldrow"><label for="s1nA">Option A: Affiliate expected sample size, n</label><input type="number" id="s1nA" step="0.1"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1seA">Option A: Affiliate SE (percentage points)</label><input type="number" id="s1seA" step="0.01"><span id="fb1b" class="fb"></span></div>
    <div class="fieldrow"><label for="s1seB">Option B: Affiliate SE (percentage points), using the floor sample</label><input type="number" id="s1seB" step="0.01"><span id="fb1c" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Pooled standard error per analyst-hour (D3&ndash;D5)</h4>
    <div class="goal">Using every channel's allocation and standard error, compute each option's <em>pooled</em> (whole-report) standard error in percentage points (weight each channel's variance by its click-volume share). Then, using Appendix E/F's setup and per-click verification times, compute total analyst-hours for each option, and divide pooled SE by hours to get the primary metric: attribution error per analyst-hour.</div>
    <div class="fieldrow"><label for="s2pooledA">Option A pooled SE (pp)</label><input type="number" id="s2pooledA" step="0.001"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2pooledB">Option B pooled SE (pp)</label><input type="number" id="s2pooledB" step="0.001"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2hoursA">Option A total analyst-hours</label><input type="number" id="s2hoursA" step="0.01"><span id="fb2c" class="fb"></span></div>
    <div class="fieldrow"><label for="s2hoursB">Option B total analyst-hours</label><input type="number" id="s2hoursB" step="0.01"><span id="fb2d" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">Do both options fit inside Appendix A's 13-hour weekend budget? The notebook checks your arithmetic, not that feasibility call &mdash; that's part of D5.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>Monday, 8:50 a.m. &mdash; ten minutes before the stand-up. Driftline's marketing lead pings again: the board deck now specifically names the Influencer/Affiliate channel's "true install rate" as a headline number, not just Monday's channel-cut decision. Whichever option Derek ran, that number is what gets read out loud in the boardroom next week.</p>
      <p>Does that change how much precision on the Affiliate channel actually matters? Recompute Step 1 with the Affiliate channel's true-install rate at the <em>low end</em> of the real published industry range (Appendix D/S2 cites 15-30% fraud, i.e. 70-85% true-install) instead of the case's stated 85% &mdash; does either option's standard error change enough to matter for a number that's about to be read out loud to a board?</p>
""",
    "twist_apply_label": "Recompute Step 1 using the low end of the real Affiliate true-install range (70%)",
    "js_data_block": """
const CHANNELS = ["san", "dsp", "owned", "affiliate"];
const PARAMS = {
  share_san: 0.62, share_dsp: 0.26, share_owned: 0.10, share_affiliate: 0.02,
  p_san: 0.95, p_dsp: 0.85, p_owned: 0.89, p_affiliate: 0.85,
  time_san: 1.0, time_dsp: 2.0, time_owned: 2.0, time_affiliate: 5.0,
  n_total_a: 400.0, setup_hours_a: 0.5,
  floor_affiliate_b: 40.0, setup_hours_b: 1.4,
  hours_budget: 13.0,
};
function seOf(p, n){
  if(n <= 0) return Infinity;
  p = Math.min(Math.max(p, 0.001), 0.999);
  return Math.sqrt(p * (1 - p) / n);
}
function optionAAllocation(p){
  const n = p.n_total_a;
  const a = {};
  CHANNELS.forEach(c => a[c] = p['share_'+c] * n);
  return a;
}
function optionBAllocation(p){
  const floor = p.floor_affiliate_b;
  const remaining = p.n_total_a - floor;
  const others = CHANNELS.filter(c => c !== 'affiliate');
  const weightSum = others.reduce((s,c) => s + p['share_'+c], 0);
  const a = {affiliate: floor};
  others.forEach(c => a[c] = remaining * p['share_'+c] / weightSum);
  return a;
}
function pooledSE(alloc, p){
  let total = 0;
  CHANNELS.forEach(c => {
    const w = p['share_'+c];
    const pc = Math.min(Math.max(p['p_'+c], 0.001), 0.999);
    total += w * w * pc * (1 - pc) / alloc[c];
  });
  return Math.sqrt(total);
}
function verificationHours(alloc, p){
  let minutes = 0;
  CHANNELS.forEach(c => minutes += alloc[c] * p['time_'+c]);
  return minutes / 60.0;
}
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const allocA = optionAAllocation(p), allocB = optionBAllocation(p);
  const seA = pooledSE(allocA, p), seB = pooledSE(allocB, p);
  const hoursA = verificationHours(allocA, p) + p.setup_hours_a;
  const hoursB = verificationHours(allocB, p) + p.setup_hours_b;
  const ratioA = seA * 100 / hoursA, ratioB = seB * 100 / hoursB;
  return {A: -ratioA, B: -ratioB};
}
// Twist: Affiliate true-install rate at the low end of the real range (70%)
function evaluate_twist(params){
  return evaluate(Object.assign({p_affiliate: 0.70}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {p_affiliate: 0.70}) : PARAMS;
  const trueNA = p.share_affiliate * p.n_total_a;
  const trueSEA = seOf(p.p_affiliate, trueNA) * 100;
  const trueSEB = seOf(p.p_affiliate, p.floor_affiliate_b) * 100;
  fb('fb1a', near(parseFloat(val('s1nA')), trueNA, 0.5));
  fb('fb1b', near(parseFloat(val('s1seA')), trueSEA, 0.3));
  fb('fb1c', near(parseFloat(val('s1seB')), trueSEB, 0.3));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {p_affiliate: 0.70}) : PARAMS;
  const allocA = optionAAllocation(p), allocB = optionBAllocation(p);
  const trueSEA = pooledSE(allocA, p) * 100, trueSEB = pooledSE(allocB, p) * 100;
  const trueHoursA = verificationHours(allocA, p) + p.setup_hours_a;
  const trueHoursB = verificationHours(allocB, p) + p.setup_hours_b;
  fb('fb2a', near(parseFloat(val('s2pooledA')), trueSEA, 0.05));
  fb('fb2b', near(parseFloat(val('s2pooledB')), trueSEB, 0.05));
  fb('fb2c', near(parseFloat(val('s2hoursA')), trueHoursA, 0.2));
  fb('fb2d', near(parseFloat(val('s2hoursB')), trueHoursB, 0.2));
}
""",
    "glossary_js": """{
  "Sample": {def: "A collection of data from part of a population.",
    url: "https://www.mathsisfun.com/data/sampling.html"},
  "Population": {def: "The whole group a study is interested in.",
    url: "https://www.mathsisfun.com/data/sampling.html"},
  "Sample Size": {def: "The number of items or people included in a sample.",
    url: "https://www.mathsisfun.com/data/sampling.html"},
  "Simple Random Sampling": {def: "Choosing a sample so that every member of the population has an equal chance of being picked.",
    url: "https://www.mathsisfun.com/data/sampling.html"},
  "Stratified Sampling": {def: "Dividing a population into groups (strata) first, then sampling proportionally from each group.",
    url: "https://www.mathsisfun.com/data/sampling.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"}
}""",
    "howto_js": """[
  ["how to find the percent of a number", "Percent"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
