const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, ExternalHyperlink, Numbering,
  LevelFormat, convertInchesToTwip,
} = require("docx");

const PAGE = { size: { width: 12240, height: 15840 } }; // US Letter, DXA
const NAVY = "1a3a5c";
const GOLD = "c9a227";
const GREY = "5b6472";

function h1(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 240, after: 160 }, children: [new TextRun({ text, bold: true, color: NAVY, size: 32 })] });
}
function h2(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 220, after: 120 }, children: [new TextRun({ text, bold: true, color: NAVY, size: 26 })] });
}
function h3(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_3, spacing: { before: 180, after: 100 }, children: [new TextRun({ text, bold: true, color: NAVY, size: 22 })] });
}
function p(text, opts = {}) {
  return new Paragraph({ spacing: { after: 160 }, children: [new TextRun({ text, ...opts })] });
}
function pMulti(runs, opts = {}) {
  return new Paragraph({ spacing: { after: 160 }, ...opts, children: runs });
}
function bullet(text) {
  return new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 100 }, children: [new TextRun({ text })] });
}
function numbered(text, opts = {}) {
  return new Paragraph({ numbering: { reference: "numbers", level: 0 }, spacing: { after: 120 }, children: [new TextRun({ text, ...opts })] });
}
function hyperlink(text, url) {
  return new ExternalHyperlink({ link: url, children: [new TextRun({ text, style: "Hyperlink", color: "1a3a5c", underline: {} })] });
}

function cell(text, { width, header = false, bold = false, shade = null } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: shade ? { type: ShadingType.CLEAR, fill: shade } : undefined,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    children: [new Paragraph({ children: [new TextRun({ text, bold: header || bold, color: header ? "FFFFFF" : "000000", size: 20 })] })],
  });
}

function dataTable(headerRow, rows, widths) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({
        tableHeader: true,
        children: headerRow.map((t, i) => cell(t, { width: widths[i], header: true, shade: NAVY })),
      }),
      ...rows.map((r, ri) => new TableRow({
        children: r.map((t, i) => cell(String(t), { width: widths[i], shade: ri % 2 === 1 ? "F7F9FB" : null })),
      })),
    ],
  });
}

const sources = [
  ["S1", "NRCS Code 430 maximum plastic-pipe design velocity", "5 ft/sec", "USDA NRCS — Conservation Practice Standard, Irrigation Pipeline (Code 430), 430-CPS-2", "2024-11", "HIGH"],
  ["S2", "Hazen-Williams friction-loss equation, English-unit, Q-based, solved for head loss", "h_f = 4.732(Q/C_HW)^1.85 (L/D^4.87)", "USDA NRCS — Title 210, National Engineering Handbook, Part 634 “Hydraulics,” Ch. 4 “Pipe Flow,” eq. 4-28, p. 634-4.11", "2022-02 (210-634-H, 1st Ed.)", "HIGH"],
  ["S3", "Hazen-Williams roughness coefficient for PVC/PE/HDPE pipe", "C = 150", "USDA NRCS — Title 210, National Engineering Handbook, Part 634, Ch. 4, Figure 4-8", "2022-02", "HIGH"],
  ["S4", "Standard EQIP cost-share payment rate", "Up to 75% of estimated costs incurred", "7 CFR § 1466.23(b)(1)(i), Environmental Quality Incentives Program, eCFR current version", "accessed 2026-09-01", "HIGH"],
  ["S5", "EQIP Practice 430 reimbursement rate, PVC pipe, standard (non-historically-underserved) rate", "$4.22/lb", "USDA NRCS Kansas — FY2025 EQIP Payment Schedule (Rest of State), Practice 430 “Irrigation Pipeline,” row “PVC, by the pound”", "2024-11", "HIGH"],
  ["S6", "PIP weight per linear foot, 6 in and 8 in nominal, DR 32.5 / 125 psi rating", "6 in: 2.40 lb/ft; 8 in: 4.16 lb/ft", "JM Eagle — “Irrigation P.I.P.” product catalog, “Dimensions and Weights” table, p. 7", "undated document (accessed 2026-09-01)", "MEDIUM"],
  ["S7", "6 in, 125 psi gasketed PVC irrigation pipe (PIP), price per foot", "$5.10/ft", "Direct Pivot Parts — online catalog, SKU 6PIPE125", "accessed 2026-09-01", "MEDIUM"],
  ["S8", "8 in, 125 psi gasketed PVC irrigation pipe (PIP), price per foot", "$7.30/ft", "Direct Pivot Parts — online catalog, SKU 8PIPE125", "accessed 2026-09-01", "MEDIUM"],
  ["S9", "Water-horsepower-hours produced per unit of pumping energy, by fuel type", "Diesel: 12.5 whp-hr/gal; Gasoline: 8.55 whp-hr/gal; Electricity: 0.885 whp-hr/kWh", "University of Georgia CAES Field Report C965, “Irrigation Pumping Plant Performance,” Table 1", "reviewed 2012-06-22 (orig. 2009-06-25)", "MEDIUM"],
  ["S10", "Brake-horsepower pump-sizing formula and constant; typical pump efficiency", "BHP = (GPM × TDH)/(3,960 × E); E = 0.75 typical", "Texas A&M AgriLife Extension, EB-6011, “Calculating Horsepower Requirements and Sizing Irrigation Supply Pipelines,” Guy Fipps, p. 4", "2021-03", "HIGH"],
  ["S12", "U.S. average retail price of electricity, industrial sector", "9.17 cents/kWh", "U.S. Energy Information Administration, “Electricity Monthly Update”", "2026-06", "HIGH"],
];
const sourceUrls = {
  S1: "https://www.nrcs.usda.gov/sites/default/files/2024-12/Irrigation%20Pipeline%20(430)%20(Ft.)%20(11-24)%20Standard%20Document.pdf",
  S2: "https://directives.nrcs.usda.gov/sites/default/files2/1720463089/Chapter%204%20-%20Pipe%20Flow.pdf",
  S3: "https://directives.nrcs.usda.gov/sites/default/files2/1720463089/Chapter%204%20-%20Pipe%20Flow.pdf",
  S4: "https://www.ecfr.gov/current/title-7/subtitle-B/chapter-XIV/subchapter-B/part-1466/subpart-B/section-1466.23",
  S5: "https://www.nrcs.usda.gov/sites/default/files/2024-11/FY25_EQIP_CostList_RestOfState.pdf",
  S6: "https://www.jmeagle.com/sites/default/files/Irrigation_web.pdf",
  S7: "https://directpivotparts.com/products/6-Gasketed-PVC-Irrigation-Pipe-Per-Foot-Choose-PSI-/6PIPE125",
  S8: "https://directpivotparts.com/products/8-Gasketed-PVC-Irrigation-Pipe-Per-Foot-Choose-PSI-/8PIPE125",
  S9: "https://fieldreport.caes.uga.edu/publications/C965/irrigation-pumping-plant-performance",
  S10: "https://gfipps.tamu.edu/files/2021/11/EB-6011-Sizing.pdf",
  S12: "https://www.eia.gov/electricity/monthly/update/end-use.php",
};

const doc = new Document({
  numbering: {
    config: [
      { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
      { reference: "numbers", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 260 } } } }] },
    ],
  },
  sections: [{
    properties: { page: { size: PAGE.size, margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [new TextRun({ text: "Case Study: The Mainline Margin", bold: true, size: 40, color: NAVY })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 }, children: [new TextRun({ text: "MS | Math | Case Study | 2026-27 | Heroes Academy", size: 20, color: GREY, italics: true })] }),

      h2("Overview"),
      p("Denise Okafor has the pipe spec sheet in one hand and her phone in the other, and neither one is telling her what she wants to hear."),
      p("The center-pivot line behind her throws a long shadow across the tailgate where she's spread two rolls of PVC catalog pages, corners flapping in the wind kicking up off the cut alfalfa. Denise designs irrigation systems for a small farm-contracting outfit, and this week's job is a mainline retrofit that has to do two things at once: pass government certification on paper, and beat a competitor's number on the invoice. The farmer standing twenty feet away, arms crossed, isn't going to ask her which pipe size clears the velocity limit or which one wins on the spreadsheet — he's going to ask what the check looks like, both ways."),
      p("Her laptop is open on the tailgate, the spreadsheet tab still blinking where she left it: two pipe sizes, two friction numbers, two totals that refuse to agree on a winner depending on which line she trusts. She's run the smaller pipe's velocity three times now, and gotten close enough to the limit each time that “close enough” has stopped feeling like an answer."),
      p("Her phone buzzes against the catalog pages — the competing contractor's quote, forwarded by the farmer, subject line just a dollar sign and three exclamation points. Denise doesn't open it yet. She sets it face-down, picks up her pencil, and looks at the two pipe sizes circled on the spec sheet, and doesn't write anything under either one."),
      p("There's a second question underneath the first one, and it's the one Denise actually has to answer twice: which pipe is the better engineering choice, and which pipe wins on the bid the farmer actually signs. Those two questions don't have to have the same answer — a government cost-share subsidy sits between them, and it doesn't always reward the same thing an engineer would."),

      h2("Background"),
      p("Denise Okafor is an irrigation systems designer at a small farm-irrigation contracting firm. She is responsible for producing the pipe specification that goes into her firm's bid on a mainline retrofit job, and she is personally accountable for two separate things the client cares about: whether her design certifies against the federal conservation-practice standard that governs the client's cost-share contract, and whether her firm's total price beats a competing contractor's bid. Missing on either one costs the job."),
      p("Two mainline pipe options are on the table for this stretch of irrigation main, both cut from the same class of PVC pipe stock her firm regularly installs."),
      pMulti([
        new TextRun({ text: "The Lean Main.", bold: true }),
        new TextRun({ text: " The smaller-diameter PVC option. It costs less per foot of pipe and weighs less per foot (SEE APPENDIX B, C), which matters twice over: less material spend up front, but also a smaller per-pound reimbursement under the client's cost-share program, since that program pays out by the pound of pipe actually installed (SEE APPENDIX E). Running the design flow rate through a smaller pipe also drives the water faster through the same cross-section, which pushes flow velocity — and, separately, friction loss — both higher than the wider option (SEE APPENDIX D)." }),
      ]),
      pMulti([
        new TextRun({ text: "The Margin Main.", bold: true }),
        new TextRun({ text: " The next-size-up PVC option. It costs more per foot and weighs more per foot, which raises both the material bill and the per-pound reimbursement. The wider cross-section keeps flow velocity lower at the same design flow rate, and cuts the pipeline's friction loss substantially — which lowers the annual cost of running the pump that pushes water through it (SEE APPENDIX D, APPENDIX F)." }),
      ]),
      p("The client's cost-share contract is administered under USDA's Environmental Quality Incentives Program (EQIP), which will only reimburse this pipeline if it certifies against NRCS Conservation Practice Standard, Irrigation Pipeline (Code 430) (SEE APPENDIX D). Code 430 sets a hard numeric ceiling on pipeline flow velocity at the design flow rate; a design that exceeds that ceiling fails certification outright, and the EQIP reimbursement is forfeited entirely — not reduced — regardless of how the rest of the design performs (SEE APPENDIX E). Code 430 also requires friction loss to be computed by the Hazen-Williams equation, using a roughness coefficient specific to the pipe material (SEE APPENDIX D)."),
      p("The farm's field layout fixes the mainline's required design flow rate and total run length; neither is Denise's to change (SEE APPENDIX A). A competing contractor has already quoted the farmer a total out-of-pocket price for the job, and Denise's own bid has to come in below it once the client's own EQIP reimbursement is netted out (SEE APPENDIX A). Running the pump that pushes water through whichever mainline is installed costs the client money every year the system operates, at a rate that depends on the pipeline's own friction loss (SEE APPENDIX F)."),
      p("This case asks for two separate cost comparisons between the Lean Main and the Margin Main, not one blended number. The true cost comparison counts only material, installation labor, and pump energy — no EQIP reimbursement at all — and answers a purely engineering question: which pipe is actually more cost-efficient to buy and run? The net-of-subsidy comparison takes that same cost and subtracts each option's EQIP reimbursement — this is the number that actually lands on Denise's bid, since the reimbursement is real money the client gets back. These two comparisons do not have to agree on how big the gap between the options is, because EQIP pays by the pound of pipe installed (SEE APPENDIX E) — a heavier pipe earns a bigger reimbursement regardless of whether it is the more efficient design. Challenge D1 asks you to build both expressions."),
      p("Every dollar figure, rate, and physical spec this case depends on is either given directly above or fixed in Appendices A through F, with full source citations in Appendix G. The vocabulary and “how to…” skills this case will ask you to research are listed in the case's final appendix — that is where Challenge 1 sends you."),

      h2("Dilemma"),
      p("You are Denise Okafor."),
      p("Do you:"),
      pMulti([
        new TextRun({ text: "A.) ", bold: true }),
        new TextRun({ text: "Spec the Lean Main — the smaller-diameter PVC mainline " }),
        new TextRun({ text: "OR", bold: true }),
      ]),
      pMulti([
        new TextRun({ text: "B.) ", bold: true }),
        new TextRun({ text: "Spec the Margin Main — the next-size-up PVC mainline" }),
      ]),

      h2("Challenges"),
      numbered("Research and find an online resource that answers one of the “how to…” questions from the case study launch. Post a link to the resource as your submission."),
      numbered("Post 250 or more “excellent” words pitching a firm stance to your audience on which you would choose and why. Your pitch must include: a.) Use of the “how to…” resource you researched in Challenge 1. b.) At least one original visual display of the data."),
      new Paragraph({
        numbering: { reference: "numbers", level: 0 }, spacing: { after: 120 },
        children: [new TextRun({ text: "Include the following:" })],
      }),
      bullet("D1 — Two total-annualized-cost expressions for each option. Write each option's (i) true annualized cost — material cost, installation labor, and pump energy cost, with NO EQIP reimbursement counted — and (ii) net-of-subsidy annualized cost — the same cost, minus the EQIP reimbursement — each as one algebraic expression in terms of the farm's design flow rate and the mainline's run length (Appendix A). Label every variable, constant, coefficient, and term in both expressions, and show the distributive property being used to expand the labor-plus-material portion the two expressions share."),
      bullet("D2 — A substitution table. For each option, substitute the farm's actual design flow rate, run length, pipe diameter, and Hazen-Williams roughness coefficient (Appendices A, B, C, D) into the Hazen-Williams friction-loss formula, and then substitute your D1 expressions' variables with the same values to evaluate each option's true and net-of-subsidy annualized-cost expressions as two separate dollar figures."),
      bullet("D3 — Simplified annualized-cost expressions per option. Combine each option's material-cost and energy-cost terms from D1 into one simplified true-cost expression, and separately combine those same terms with the EQIP-reimbursement term into one simplified net-of-subsidy expression — for both, show which terms are like terms and how they combine under addition or subtraction."),
      bullet("D4 — A certification check. For each pipe option, solve a one-step equation to find the maximum flow rate that option can carry before its velocity reaches NRCS Code 430's numeric ceiling (Appendix D), and state plainly whether that option passes or fails certification at the farm's actual required design flow rate (Appendix A)."),
      bullet("D5 — A rearranged design formula. Starting from the Hazen-Williams friction-loss formula, isolate pipe diameter by solving a multi-step equation with the variable on one side, and use your rearranged formula to find the minimum pipe diameter that would keep the pump's annual energy cost under a stated cost cap of your choosing."),
      bullet("D6 — A break-even calculation and recommendation memo. Set the Lean Main's and the Margin Main's true total-annualized-cost-per-acre-inch expressions (from D3) equal to each other, and solve the resulting multi-step equation — with the variable on both sides — to find the design flow rate at which the two options cost the same on true engineering efficiency alone. State whether the farm's actual required design flow rate (Appendix A) falls above or below that break-even point. Then write a recommendation memo that explicitly addresses both figures: (1) the true, subsidy-free efficiency gap between the two options, and (2) the net-of-subsidy gap that will actually appear on Denise's bid — state, in percentage points, how much of the net-of-subsidy gap is attributable to the EQIP subsidy formula itself rather than to true efficiency. Defend your final recommendation with your D4 certification result and both D6 figures."),
      numbered("An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count."),
      numbered("Participate twice or more in the Case Study discussion. If you are absent the day of a discussion post 500 “excellent” words on the questions above.", { italics: true }),

      h2("Appendix A: Denise's Bid Constraints and the Farm's Field Layout"),
      dataTable(["Quantity", "Value"], [
        ["Mainline design flow rate required at the field inlet (GPM)", "440 [MA1]"],
        ["Total mainline run length (ft)", "1,320 [MA2]"],
        ["Acreage irrigated by this mainline (acres)", "88 [MA3]"],
        ["Installation labor rate ($ per foot of pipe installed)", "$25.00 [MA4]"],
        ["Competing contractor's total quoted price to the farmer, out-of-pocket, net of any EQIP reimbursement (USD)", "$24,000 [MA6]"],
        ["Annual hours the irrigation system operates (hr/yr)", "1,200 [MA5]"],
      ], [6400, 3100]),

      h2("Appendix B: Option A — The Lean Main Spec Sheet"),
      dataTable(["Spec", "Value"], [
        ["Nominal pipe diameter (in)", "6 [S6]"],
        ["Weight per linear foot (lb/ft)", "2.40 [S6]"],
        ["Material cost per linear foot (USD/ft)", "$5.10 [S7]"],
        ["Hazen-Williams roughness coefficient, C (PVC/plastic)", "150 [S3]"],
      ], [6400, 3100]),

      h2("Appendix C: Option B — The Margin Main Spec Sheet"),
      dataTable(["Spec", "Value"], [
        ["Nominal pipe diameter (in)", "8 [S6]"],
        ["Weight per linear foot (lb/ft)", "4.16 [S6]"],
        ["Material cost per linear foot (USD/ft)", "$7.30 [S8]"],
        ["Hazen-Williams roughness coefficient, C (PVC/plastic)", "150 [S3]"],
      ], [6400, 3100]),

      h2("Appendix D: NRCS Conservation Practice Standard, Irrigation Pipeline (Code 430)"),
      dataTable(["Design criterion", "Value"], [
        ["Maximum allowable pipeline flow velocity at design capacity (ft/sec)", "5 [S1]"],
        ["Friction-loss method required for certification", "Hazen-Williams equation"],
        ["Hazen-Williams equation form (as published in Code 430 or its design handbook)", "h_f = 4.732 · (Q ÷ C_HW)^1.85 · (L ÷ D^4.87) — where h_f = friction head loss (ft), Q = flow rate (cfs), C_HW = Hazen-Williams coefficient, L = pipe length (ft), D = pipe diameter (ft) [S2]"],
      ], [4400, 5100]),
      p("NRCS Conservation Practice Standard Code 430 is a real, federally published document (National Handbook of Conservation Practices, nrcs.usda.gov). Both rows above are sourced directly from that standard and its companion National Engineering Handbook chapter (SEE APPENDIX G, S1–S2). Note: Code 430's plastic-pipe velocity ceiling is 5 ft/sec — do not confuse this with the 7 ft/sec figure that appears in the separate NRCS Code 443 (Irrigation System, Surface and Subsurface) standard, which governs a different practice and is not the ceiling this case's certification depends on.", { italics: true, color: GREY, size: 18 }),

      h2("Appendix E: EQIP Cost-Share Terms for Practice 430"),
      dataTable(["Term", "Value"], [
        ["Reimbursement basis", "Per pound of pipe installed"],
        ["Standard cost-share rate (% of eligible cost)", "75% [S4]"],
        ["Reimbursement rate per pound of pipe installed (USD/lb)", "$4.22 [S5]"],
        ["Condition of payment", "Reimbursement is forfeited in full if the installed design does not certify against NRCS Code 430"],
      ], [4400, 5100]),

      h2("Appendix F: Pump Energy Cost Figures"),
      dataTable(["Quantity", "Value"], [
        ["Pump power source (fuel type) for this job", "Electricity (grid-powered pump) [MA7]"],
        ["Energy-cost conversion factor for the pump's fuel type (water-horsepower-hours per unit of fuel or per kWh)", "Electricity: 0.885 whp-hr/kWh. For reference, diesel: 12.5 whp-hr/gal; gasoline: 8.55 whp-hr/gal [S9]"],
        ["Local price per unit of pump fuel or electricity (USD)", "$0.0917 per kWh [S12]"],
        ["Brake-horsepower sizing formula constants (denominator constant and typical pump efficiency, E)", "BHP = (GPM × TDH) ÷ (3,960 × E); typical pump efficiency E = 0.75 (75%) [S10]"],
      ], [4400, 5100]),

      h2("A note on the two cost comparisons"),
      p("At the farm's sourced/assumed figures (Appendices A-F), the two comparisons this case asks for do not agree on the size of the gap between the options:"),
      dataTable(
        ["", "True cost/yr (material+labor+energy, NO subsidy)", "Net-of-subsidy cost/yr (EQIP reimbursement included)"],
        [
          ["Option A — Lean Main", "$2,215.83", "$1,547.38"],
          ["Option B — Margin Main", "$2,188.27", "$1,029.63"],
          ["Gap (B's advantage)", "~1.3%", "~50.3%"],
        ], [2600, 3600, 3300]
      ),
      p("Both options certify against NRCS Code 430 at the farm's required 440 GPM (Appendix D), so both keep their EQIP reimbursement. Once that reimbursement is counted, the Margin Main looks like the runaway winner (~50.3% cheaper). Strip the reimbursement out entirely, and the Margin Main is still the better pick — but only by about 1.3%, a genuine engineering toss-up. The difference between those two gaps (about 49 percentage points) is not noise; it is the EQIP Practice 430 reimbursement rate paying by the pound of pipe installed (Appendix E) — a structure that rewards the heavier pipe, not necessarily the more efficient one. Challenges D1, D3, and D6 ask you to build, simplify, and reconcile both figures rather than pick whichever one supports a pre-decided answer."),

      h2("Modeling Assumptions"),
      p("These figures are not sourced. They are stated scenario assumptions chosen by the case author because no public, citable figure exists for this specific farm. A Hero may challenge them in discussion — that is a legitimate move.", { italics: true }),
      dataTable(["#", "Assumption", "Value used", "Basis", "Sensitivity"], [
        ["MA1", "Mainline design flow rate", "440 GPM (retuned 2026-09-01 from 450 GPM)", "Center-pivot and mainline design capacities are commonly sized near 5 GPM per irrigated acre for full-season row-crop irrigation in the central Great Plains (published rule-of-thumb ranges run roughly 5–8 GPM/acre depending on crop and climate); paired here with MA3's 88 acres (5 × 88 = 440), the same rate used before retuning.", "HIGH — this is the single most dilemma-flipping figure in the case. Appendix D's certification math puts the Lean Main's velocity ceiling at a maximum flow of about 440.7 GPM; 440 GPM sits only ~0.16% below that cutoff — the Lean Main now certifies, but the margin is thin enough that Challenge D4's exact calculation, not a guess, is what actually settles it."],
        ["MA2", "Total mainline run length", "1,320 ft", "One quarter-mile — a common distance from a wellhead/pump station at a section-line road to a field inlet or pivot point, matching the standard U.S. Public Land Survey quarter-quarter-section grid used throughout the region this case is set in.", "LOW-MODERATE — scales material cost, pipe weight (and therefore the EQIP reimbursement), and friction loss proportionally for both options at once, so it changes the size of the gap between options but not its direction."],
        ["MA3", "Acreage irrigated by this mainline", "88 acres (retuned 2026-09-01 from 90 acres)", "Paired with MA1's 5 GPM/acre design rate to produce the stated 440 GPM design flow; 88 acres is smaller than a full quarter-section pivot's typical ~125–130 acre footprint, consistent with a “mid-size” field, and barely different from the original 90-acre figure.", "LOW — enters only the per-acre-inch denominator, which is identical for both options (both deliver the same required flow), so acreage alone cannot flip the recommendation."],
        ["MA4", "Installation labor rate", "$25.00/ft", "Published trenching-cost ranges for underground utility and irrigation lines run from roughly $5–$12/ft for basic, shallow residential-scale work up to $13–$40/ft for deeper, larger-diameter, more complex installations (contractor-cost survey aggregators, 2026). No agriculture-specific contractor rate for large-diameter ag mainline (deeper bury depth, backfill compaction, thrust blocks, valve stands) could be found publicly. $25/ft was chosen from the upper part of that range to reflect that added complexity.", "LOW — applied as a flat rate per foot, independent of pipe diameter, so it is identical in dollar terms for both options at a given run length and does not change which option wins."],
        ["MA5", "Annual system operating hours", "1,200 hr/yr", "General Great Plains extension guidance for a full-season row-crop irrigation system commonly cites roughly 1,000–1,500 operating hours per season; 1,200 is used as a round mid-range figure. No single citable “typical annual hours” figure specific to a mainline (as opposed to a whole pivot system) could be found.", "MODERATE — scales annual pump energy cost linearly for both options at once, widening or narrowing the absolute energy-cost gap without changing its direction."],
        ["MA6", "Competing contractor's total quoted price, out-of-pocket, net of EQIP (USD)", "$24,000", "This case's own scenario constraint (explicitly not an external figure — no real competing bid exists for a fictional farm). Chosen to sit meaningfully between the two options' realistic net installed costs so Denise's own bid has real stakes on both designs.", "Sets the stakes for Denise's own bid, a business constraint distinct from the A-vs-B cost/certification comparison the Challenges ask you to solve."],
        ["MA7", "Pump power source (fuel type)", "Electricity (grid-powered pump)", "Chosen because it lets the case cite a current, dated, national reference price (a public utility-scale rate) rather than a regionally variable diesel or propane price, and because grid power is common for stationary agricultural mainline and center-pivot pumps on grid-served farms.", "LOW — a different real fuel choice (diesel, propane) would change the absolute annual energy-cost figures for both options together via a different price and conversion factor, but would not on its own flip which option has the lower friction loss."],
      ], [700, 1600, 2000, 2900, 2300]),
      p("Modeling Assumptions are cross-referenced above as [MA#]. See RESEARCH_LOG.md for the specific searches run and why each of these could not be sourced to a real, dated, citable figure for this farm.", { italics: true, color: GREY, size: 18 }),

      h2("Appendix G: Sources"),
      new Table({
        width: { size: 9500, type: WidthType.DXA },
        columnWidths: [500, 2200, 1900, 2900, 1000, 1000],
        rows: [
          new TableRow({ tableHeader: true, children: ["#", "Claim", "Value", "Source", "Date", "Confidence"].map((t, i) => cell(t, { width: [500, 2200, 1900, 2900, 1000, 1000][i], header: true, shade: NAVY })) }),
          ...sources.map((s, ri) => new TableRow({
            children: [
              cell(s[0], { width: 500, shade: ri % 2 ? "F7F9FB" : null }),
              cell(s[1], { width: 2200, shade: ri % 2 ? "F7F9FB" : null }),
              cell(s[2], { width: 1900, shade: ri % 2 ? "F7F9FB" : null }),
              new TableCell({
                width: { size: 2900, type: WidthType.DXA },
                shading: ri % 2 ? { type: ShadingType.CLEAR, fill: "F7F9FB" } : undefined,
                margins: { top: 80, bottom: 80, left: 100, right: 100 },
                children: [new Paragraph({ children: sourceUrls[s[0]] ? [hyperlink(s[3], sourceUrls[s[0]])] : [new TextRun({ text: s[3], size: 20 })] })],
              }),
              cell(s[4], { width: 1000, shade: ri % 2 ? "F7F9FB" : null }),
              cell(s[5], { width: 1000, shade: ri % 2 ? "F7F9FB" : null }),
            ],
          })),
        ],
      }),
      p("A note on Appendix D's velocity ceiling. An earlier concept note for this case assumed Code 430's velocity ceiling was 7 ft/sec. That figure is real, but it belongs to a different standard — NRCS Code 443 (Irrigation System, Surface and Subsurface) allows up to 7 ft/sec with surge protection, and a 7 ft/sec flush velocity is separately permitted in microirrigation submains under Code 441. Code 430 itself — the standard that actually governs this pipeline — sets the plastic-pipe ceiling at 5 ft/sec (S1), confirmed identically in both the 2020R and the current November 2024 revision of the standard. This case uses 5 ft/sec throughout, because that is the number Denise would actually be certifying against.", { italics: true, color: GREY, size: 18 }),

      h3("Appendix H — “How To…” Math Questions To Research"),
      p("Vocabulary terms", { bold: true }),
      bullet("Variable"),
      bullet("Constant"),
      bullet("Coefficient"),
      bullet("Term"),
      bullet("Like Terms"),
      bullet("Distributive property"),
      p("“How to…” questions", { bold: true }),
      bullet("How to evaluate a variable expression (Substitution Property)"),
      bullet("How to add and subtract an expression with variables"),
      bullet("How to solve a one-step equation"),
      bullet("How to solve a multi-step equation with a variable on one side"),
      bullet("How to solve a multi-step equation with a variable on both sides"),
    ],
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync("cases/the-mainline-margin/published/The Mainline Margin - Case Study.docx", buf);
  console.log("wrote The Mainline Margin - Case Study.docx", buf.length, "bytes");
});
