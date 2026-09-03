CONFIG = {
    "strand_summary": "Recursive Sequences &middot; Explicit Formulas",
    "protagonist": "the pricing analyst",
    "option_a_label": "The Quick-Quote Card",
    "option_a_text": "Meridian's published flat-rate reference card for this AUC band -- fast to quote today, but a flat rate, not the true recursive fee.",
    "option_b_label": "The Full Ladder",
    "option_b_text": "Walk the real recursive tier structure by hand -- exact, but takes longer than the client's timeline allows today.",
    "challenge3_summary": "Include: <strong>D1</strong> the Full Ladder's fee, computed by walking Appendix C's recursion tier-by-tier (each tier's fee applied to the balance remaining after the previous tier's fee was subtracted); <strong>D2</strong> the Quick-Quote Card's flat-rate fee; <strong>D3</strong> the percent gap between them; <strong>D4</strong> a check that the gap's percentage is the same regardless of client AUC size (scale invariance); <strong>D5</strong> a recommendation memo.",
    "deliverables": [
        ["D1", "Full Ladder fee via the tier-by-tier recursion"],
        ["D2", "Quick-Quote Card flat-rate fee"],
        ["D3", "Percent gap between the two fees"],
        ["D4", "Scale-invariance check across AUC sizes"],
        ["D5", "Recommendation memo"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Walk the Full Ladder's recursion (D1)</h4>
    <div class="goal">Appendix C's rule: each tier's fee is charged on the balance <em>remaining after the previous tier's own fee was already subtracted</em> &mdash; not a flat sum of rate &times; total AUC. Starting from Appendix A's client AUC and Appendix C's four tier rates, walk the recursion one tier at a time: fee = rate &times; current balance; balance = balance &minus; fee. Enter your final total fee.</div>
    <div class="fieldrow"><label for="s1auc">Client AUC (USD)</label><input type="number" id="s1auc" step="1"></div>
    <div class="fieldrow"><label for="s1fee">Full Ladder total fee (USD)</label><input type="number" id="s1fee" step="0.01"><span id="fb1a" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Quick-Quote fee, the gap, and scale invariance (D2&ndash;D4)</h4>
    <div class="goal">Compute the Quick-Quote Card's flat-rate fee (rate &times; AUC), then the absolute dollar gap and the percent gap against your Step 1 recursive fee. Then try a different AUC in Step 1 and recompute here &mdash; does the <em>percent</em> gap change?</div>
    <div class="fieldrow"><label for="s2quickfee">Quick-Quote fee (USD)</label><input type="number" id="s2quickfee" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2gappct">Percent gap between Quick-Quote and the Full Ladder</label><input type="number" id="s2gappct" step="0.01"><span id="fb2b" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
    <p class="side-note">Does the percent gap depend on the AUC you entered in Step 1? Try two different AUC values and compare.</p>
  </div>
""",
    "twist_narrative_html": """
      <p>A real SEC enforcement record: a major custody bank was found to have overcharged clients for years through an undisclosed markup, collecting $170 million in overcharges before it was caught &mdash; and had to pay back tens of millions more once it was (Appendix F, S3).</p>
      <p>That case wasn't a quoting shortcut like the Quick-Quote Card &mdash; it was undisclosed. But it raises the real question for D5: is a <em>disclosed</em>, bounded, known error acceptable in a way an undisclosed one never can be, even if the dollar gap looks similar on a given day? Revisit your D5 recommendation with that distinction in mind.</p>
""",
    "twist_apply_label": "I've considered the disclosed-vs-undisclosed distinction in my D5 recommendation",
    "js_data_block": """
const PARAMS = {
  client_auc: 850000000.0,
  quick_quote_rate_bp: 3.90,
  tier1_bp: 2.00, tier2_bp: 1.25, tier3_bp: 0.75, tier4_bp: 0.50,
};
function trueFeeRecursive(auc, tierRatesBp){
  let balance = auc, totalFee = 0;
  tierRatesBp.forEach(rateBp => {
    const r = rateBp / 10000.0;
    const fee = r * balance;
    balance -= fee;
    totalFee += fee;
  });
  return totalFee;
}
function evaluateDetail(params){
  const p = Object.assign({}, PARAMS, params||{});
  const auc = p.client_auc;
  const tierRates = [p.tier1_bp, p.tier2_bp, p.tier3_bp, p.tier4_bp];
  const feeBTrue = trueFeeRecursive(auc, tierRates);
  const feeA = auc * (p.quick_quote_rate_bp / 10000.0);
  const gap = feeA - feeBTrue;
  const marginPct = feeBTrue ? Math.abs(gap) / feeBTrue * 100.0 : Infinity;
  return {feeA, feeBTrue, gap, marginPct};
}
function evaluate(params){
  const d = evaluateDetail(params);
  return {A: -Math.abs(d.gap), B: 0.0};
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const auc = parseFloat(val('s1auc')) || PARAMS.client_auc;
  const tierRates = [PARAMS.tier1_bp, PARAMS.tier2_bp, PARAMS.tier3_bp, PARAMS.tier4_bp];
  const trueFee = trueFeeRecursive(auc, tierRates);
  fb('fb1a', near(parseFloat(val('s1fee')), trueFee, Math.max(1, trueFee*0.001)));
}
function checkStep2(){
  const auc = parseFloat(val('s1auc')) || PARAMS.client_auc;
  const d = evaluateDetail({client_auc: auc});
  fb('fb2a', near(parseFloat(val('s2quickfee')), d.feeA, Math.max(1, d.feeA*0.001)));
  fb('fb2b', near(parseFloat(val('s2gappct')), d.marginPct, 0.5));
}
""",
    "glossary_js": """{
  "Recursive Formula": {def: "A rule that defines each term in a sequence using the value of a previous term, rather than its position number.",
    url: "https://www.mathsisfun.com/algebra/sequences-series.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- literally \\"per hundred.\\"",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Ratio": {def: "A way of comparing two quantities by division, written a:b or a/b.",
    url: "https://www.khanacademy.org/math/get-ready-for-6th-grade/x55793c7ff6b02d3d:get-ready-for-ratios-rates-and-percentages"},
  "Decimal": {def: "A number written with place value to the right of a decimal point, e.g. 0.34.",
    url: "https://www.khanacademy.org/math/arithmetic/arith-decimals"},
  "Sequence": {def: "An ordered list of numbers, each one called a term.",
    url: "https://www.mathsisfun.com/algebra/sequences-series.html"},
  "Absolute Value": {def: "How far a number is from zero on the number line -- always zero or positive.",
    url: "https://www.khanacademy.org/math/algebra-home/alg-absolute-value"},
  "Scientific Notation": {def: "A compact way to write very large or very small numbers: a number from 1-10 times a power of 10.",
    url: "https://www.khanacademy.org/math/8th-grade-illustrative-math/unit-7-exponents-and-scientific-notation"},
  "Data": {def: "Facts or numbers collected for reference or analysis.",
    url: "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics"}
}""",
    "howto_js": """[
  ["how to write a recursive formula for a sequence", "Recursive Formula"],
  ["how to convert a recursive formula to an explicit formula", "Recursive Formula"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
