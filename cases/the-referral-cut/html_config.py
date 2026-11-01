CONFIG = {
    "strand_summary": "Mixed Numbers &middot; Fraction Multiplication &middot; Simplifying",
    "protagonist": "Mia Torres",
    "option_a_label": "Fulfilled by Merchant (FBM)",
    "option_a_text": "Mia keeps fulfilling every order herself -- pays her own packaging and postage.",
    "option_b_label": "Fulfilled by Amazon (FBA)",
    "option_b_text": "Mia hands fulfillment over to Amazon's own warehouses, in exchange for a per-unit fulfillment fee plus a fuel-and-logistics surcharge.",
    "challenge3_summary": "Include: <strong>D1</strong> post-referral-fee proceeds per unit; <strong>D2</strong> Option A's net margin per unit and per month; <strong>D3</strong> Option B's total fulfillment fee (multiplicative, not additive) and net margin; <strong>D4</strong> the monthly net-margin comparison; <strong>D5</strong> a working-capital comparison; <strong>D6</strong> a side-by-side visual.",
    "deliverables": [
        ["D1", "Post-referral-fee proceeds per unit"],
        ["D2", "Option A net margin per unit and per month"],
        ["D3", "Option B total fulfillment fee and net margin"],
        ["D4", "Monthly net-margin comparison"],
        ["D5", "Working-capital comparison"],
        ["D6", "Side-by-side visual"],
    ],
    "notebook_steps_html": """
  <div class="stepbox">
    <h4>Step 1 &mdash; Post-referral proceeds and Option B's total fee (D1&ndash;D3)</h4>
    <div class="goal">Using Appendix B's referral fee, find what Mia keeps per unit after Amazon's referral cut. Then, using Appendix C's base fulfillment fee and fuel surcharge, find Option B's TOTAL fulfillment fee &mdash; remember the surcharge multiplies the fee, it does not add a flat amount.</div>
    <div class="fieldrow"><label for="s1proceeds">Post-referral-fee proceeds per unit ($)</label><input type="number" id="s1proceeds" step="0.0001"><span id="fb1a" class="fb"></span></div>
    <div class="fieldrow"><label for="s1feeB">Option B: total fulfillment fee per unit ($)</label><input type="number" id="s1feeB" step="0.0001"><span id="fb1b" class="fb"></span></div>
    <button onclick="checkStep1()">Check</button>
  </div>

  <div class="stepbox">
    <h4>Step 2 &mdash; Monthly net margin, each option (D4)</h4>
    <div class="goal">Subtract each option's own costs from the post-referral proceeds to get net margin per unit, then multiply by Rivendell's guaranteed monthly order quantity (Appendix A).</div>
    <div class="fieldrow"><label for="s2marginA">Option A: monthly net margin ($)</label><input type="number" id="s2marginA" step="0.01"><span id="fb2a" class="fb"></span></div>
    <div class="fieldrow"><label for="s2marginB">Option B: monthly net margin ($)</label><input type="number" id="s2marginB" step="0.01"><span id="fb2b" class="fb"></span></div>
    <div class="fieldrow"><label for="s2margin">Margin between the two options (percent)</label><input type="number" id="s2margin" step="0.1"><span id="fb2c" class="fb"></span></div>
    <button onclick="checkStep2()">Check</button>
  </div>
""",
    "twist_narrative_html": """
      <p>Mia's own packaging/postage estimate ($3-1/8 per unit) is her own number, not a published rate &mdash; nobody outside her shop could verify it exactly. Toggle the switch below to see what happens if it's actually 50% higher than she thinks.</p>
""",
    "twist_apply_label": "Recompute at a 50% higher packaging cost ($4.6875 instead of $3.125)",
    "js_data_block": """
const PARAMS = {
  price: 18.75, packaging_cost: 3.125, production_cost: 6.5, monthly_units: 40,
  referral_fee: 0.15, base_fba_fee: 3.68, fuel_surcharge: 0.035,
};
function evaluate(params){
  const p = Object.assign({}, PARAMS, params||{});
  const proceeds = p.price * (1 - p.referral_fee);
  const marginUnitA = proceeds - p.packaging_cost - p.production_cost;
  const feeB = p.base_fba_fee * (1 + p.fuel_surcharge);
  const marginUnitB = proceeds - feeB - p.production_cost;
  const monthlyA = marginUnitA * p.monthly_units;
  const monthlyB = marginUnitB * p.monthly_units;
  return {A: monthlyA, B: monthlyB, proceeds, feeB, monthlyA, monthlyB};
}
function evaluate_twist(params){
  return evaluate(Object.assign({packaging_cost: 4.6875}, params||{}));
}
""",
    "notebook_check_functions": """
function checkStep1(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {packaging_cost: 4.6875}) : PARAMS;
  const r = evaluate(p);
  fb('fb1a', near(parseFloat(val('s1proceeds')), r.proceeds, 0.001));
  fb('fb1b', near(parseFloat(val('s1feeB')), r.feeB, 0.001));
}
function checkStep2(){
  const p = window.__TWIST_APPLIED__ ? Object.assign({}, PARAMS, {packaging_cost: 4.6875}) : PARAMS;
  const r = evaluate(p);
  const lo = Math.min(r.A, r.B), hi = Math.max(r.A, r.B);
  const margin = lo ? 100.0*(hi-lo)/lo : 0;
  fb('fb2a', near(parseFloat(val('s2marginA')), r.A, 1));
  fb('fb2b', near(parseFloat(val('s2marginB')), r.B, 1));
  fb('fb2c', near(parseFloat(val('s2margin')), margin, 1));
}
""",
    "glossary_js": """{
  "Mixed Number": {def: "A number written as a whole number together with a fraction, such as 18 and 3/4.",
    url: "https://www.mathsisfun.com/mixed-fractions.html"},
  "Improper Fraction": {def: "A fraction where the numerator is greater than or equal to the denominator, such as 75/4.",
    url: "https://www.mathsisfun.com/mixed-fractions.html"},
  "Simplify": {def: "Reducing a fraction to its lowest terms by dividing the numerator and denominator by their greatest common factor.",
    url: "https://www.mathsisfun.com/simplifying-fractions.html"},
  "Percent": {def: "A ratio that compares a number to 100 -- used here for Amazon's referral fee and fuel surcharge.",
    url: "https://www.mathsisfun.com/definitions/percent.html"},
  "Fraction": {def: "A number representing a part of a whole, written as a numerator over a denominator.",
    url: "https://www.mathsisfun.com/fractions.html"},
  "Product": {def: "The result of multiplying two or more numbers together.",
    url: "https://www.mathsisfun.com/definitions/product.html"},
  "Net Margin": {def: "What is left over per unit sold after every real cost (fees, packaging, production) is subtracted from the sale proceeds -- a form of profit.",
    url: "https://www.mathsisfun.com/definitions/profit.html"},
  "Multiplicative": {def: "Combined by multiplying rather than by adding -- the fuel surcharge scales the fulfillment fee, it does not add a flat amount to it.",
    url: "https://www.mathsisfun.com/fractions_multiplication.html"}
}""",
    "howto_js": """[
  ["how to simplify a fraction", "Simplify"],
  ["how to convert a mixed number to an improper fraction", "Mixed Number"],
  ["how to convert an improper fraction to a mixed number", "Improper Fraction"],
  ["how to multiply a fraction and a whole number", "Fraction"],
  ["how to multiply two fractions", "Product"],
  ["how to multiply a fraction and a mixed number", "Mixed Number"],
  ["how to multiply two mixed numbers", "Mixed Number"]
]""",
    "on_twist_toggle_js": """
function onTwistToggle(){
  window.__TWIST_APPLIED__ = document.getElementById('applyTwist').checked;
}
""",
}
