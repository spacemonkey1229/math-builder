const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType,
} = require("docx");

const NAVY = "1a3a5c";

function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 100 } }); }
function p(text, opts = {}) { return new Paragraph({ children: [new TextRun({ text, ...opts })], spacing: { after: 120 } }); }
function cell(text, opts = {}) {
  return new TableCell({
    width: { size: opts.width || 2000, type: WidthType.DXA },
    shading: opts.header ? { type: ShadingType.CLEAR, color: "auto", fill: NAVY } : undefined,
    children: [new Paragraph({ children: [new TextRun({ text: String(text), bold: !!opts.header, color: opts.header ? "FFFFFF" : undefined, size: 20 })] })],
  });
}
function table(headers, rows, widths) {
  const w = widths || headers.map(() => Math.floor(9000 / headers.length));
  return new Table({
    width: { size: 9000, type: WidthType.DXA },
    columnWidths: w,
    rows: [
      new TableRow({ children: headers.map((h, i) => cell(h, { header: true, width: w[i] })) }),
      ...rows.map(r => new TableRow({ children: r.map((c, i) => cell(c, { width: w[i] })) })),
    ],
  });
}

const doc = new Document({
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    children: [
      new Paragraph({ children: [new TextRun({ text: "Facilitator Guide: The Weekly Rate", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("FACILITATOR ONLY — contains the balance argument, the margin, and the trap. Do not distribute to Heroes.", { bold: true, color: "a3312a" }),
      p("Case: The Weekly Rate  ·  Tier: T3  ·  Band: MS-stretch / HS-entry  ·  Studio: Adventure"),
      p("Standards: see case.json.standards[] (28 skills — variable, constant, coefficient, term, like terms, distributive property, x-intercept, y-intercept, slope, system of equations, percent, rounding, addition, multiplication, and their paired “how to…” skills)."),

      h1("The Balance Argument (Answer Key — Facilitator Only)"),
      p("Argument for A (Ownership): Weekly rate ~$18.2937 vs. B's ~$39.986, after the one-time $2,299.00 purchase. Every week past the break-even point (~105.98 weeks), Ownership is strictly cheaper, and stays that way for as long as Dara keeps the bike after her 21-month program ends."),
      p("Argument for B (Subscription): Zero upfront cost, and covers every repair no matter what breaks. At Dara's actual, fixed 91-week horizon, Subscription's total cost ($3,638.72) is lower than Ownership's ($3,963.72) by $325.00, about 8.2% — because 91 weeks falls about 15 weeks short of the ~105.98-week break-even point."),
      p("Margin at the base 91-week horizon: 8.20%, Subscription (B) wins.", { bold: true }),
      p("The Trap: most Heroes will compute the break-even point (~105.98 weeks), see that Ownership wins “eventually,” and declare Ownership the obvious right answer — without checking that 91 (Dara's actual horizon) is less than 105.98."),

      h1("Facilitator Notes"),
      h2("Intro"),
      p("Frame the format: a real personal-finance decision built from real, currently-live company pricing. Name the opener: “Dara rides six days a week for two delivery apps. Every week, she pays a company named Zoomo thirty-nine dollars to rent the e-bike she rides. Today she has to decide whether to keep paying that, or to walk into a bike shop and just buy one.”"),
      h2("Launch"),
      p("Read the Overview aloud, then Background's first three paragraphs. Do not show Appendix A's dollar figures yet. Ask: “Just from what you've heard — does 'the one with no upfront cost' sound like it settles this, or not?”"),
      h2("Anchor 1 — Take a stand and vote"),
      p("TAKE A STAND AND VOTE. No reasoning yet, just commit. “Buy the bike, or keep the subscription?” Show of hands, no discussion yet."),
      h2("Anchor 2 — What is the problem we're solving?"),
      p("“Is this the right question?” · “What do you mean by 'cheaper'?” Push on what “cheaper” actually means — starting tomorrow, over Dara's whole career, or over her specific 21-month horizon."),
      h2("Anchor 3 — What is the process?"),
      p("“If we go through this process and find the data, how will we decide?” Name the steps: cost per week (Appendix A), deriving equations (D1), the break-even point (D2), what the crossing point means for a fixed horizon (D3, D6)."),
      h2("Anchor 4 — What don't we know?"),
      p("Surface Appendix C's four Modeling Assumptions as a group before anyone computes anything. MA4 (91-week horizon) is the single most load-bearing assumption; MA3 ($900/yr maintenance) is a close second; MA1 and MA2 barely move the answer."),
      h2("Data Deep Dive"),
      p("Walk D1, D2, and D6 together as a room. Show the actual split: Option A total $3,963.72 (purchase $2,299.00 + $18.2937/week × 91 weeks); Option B total $3,638.72 ($39.986/week × 91 weeks). Margin: 8.20%, B cheaper."),
      h2("Twist — drop at roughly the 20-minute mark"),
      p("Deliver: Zoomo's own blog documents raising an equivalent plan from $39/week to $49/week (~26%) once already. Suppose that happens again, halfway through Dara's 91 weeks (weeks 1-40 at $39, weeks 41-91 at $49.14). Recomputed Option B total: $4,155.86 — now Option A ($3,963.72) is cheaper, by about 4.62%. The recommendation flips."),
      p("Twist soundness: grounded in a real, cited precedent (Zoomo's own blog, S5a); changes no stated Modeling Assumption; sensitivity_model.py's evaluate_twist() confirms the recompute mechanically."),
      h2("Immediate recommit / Close"),
      p("Re-vote immediately after the twist, then again after full discussion. Ask what math was new today and how they attacked it."),
      h2("Lessons Learned"),
      p("“Eventually cheaper” and “cheaper for the time period you actually have” are two different questions. A margin that looks decisive (8.20%) can flip entirely on one input outside anyone's control."),

      h1("Five Socratic Questions"),
      p("1. Dara's break-even point is about 105.98 weeks, but her actual horizon is 91 weeks — what would her decision horizon have to become before Ownership wins instead of Subscription, and how far is that from where she actually is?"),
      p("2. Appendix C sets Dara's own maintenance cost at $900/year, extrapolated upward from a $400+/year 'regular commuter' figure — if that extrapolation is wrong by 50% in either direction, does the recommendation change, and by how much does the margin move?"),
      p("3. D3 asks for the x-intercept of the net-savings function and, separately, its y-intercept — what does each one mean in plain English, and why is the y-intercept negative?"),
      p("4. Appendix B graphs a Whizz plan Dara isn't choosing between — what makes its equation structurally different from Option B's, and why doesn't that difference matter to Dara's actual decision?"),
      p("5. A friend asks Dara: 'Why not just buy the bike right before your program ends, once you're sure Subscription won by the horizon that actually happened?' — using the case's own equations, what's wrong with that plan as a general strategy?"),

      h1("Sensitivity Note (SPEC §6 — boxed)"),
      p("The 8.20% base margin is sensitive to MA4 (decision horizon) and MA3 (annual maintenance). A +50% swing on decision_horizon_weeks (to 136.5 weeks) flips the winner to A at a 12.13% margin; a -50% swing (to 45.5 weeks) keeps B winning but pushes the margin to 41.90%, over the SPEC §2 20% cap. A -50% swing on annual_maintenance_cost flips the winner to A at 12.71%; a +50% swing keeps B winning at 23.42%, also over the cap. See sensitivity_model.py FLEX and case.json's sensitivity_disclosure[]."),

      h1("What a Strong Defense Sounds Like"),
      p("Not an answer key — a Hero defending either option well will: state which time window they're optimizing for and why; show the break-even algebra, not just the horizon evaluation; name which Modeling Assumption their answer is most sensitive to; address the Twist directly rather than ignoring it."),

      h1("Cohort Bands"),
      table(["Band", "What changes"], [
        ["Full (12-20)", "Anchors 2-3 run as written; room splits into factions before the Twist forces a recompute."],
        ["Compressed (6-11)", "Anchors 2-3 combine into one pass; D1 worked as one shared example."],
        ["1:1 / pair (1-2)", "No vote; Anchor 1 becomes a stated position; facilitator plays devil's advocate."],
      ], [3000, 6000]),

      h1("45-Minute Socratic Plan"),
      p("Timings below are minutes elapsed from the start of the discussion (mm:ss), not case data."),
      table(["Time", "Move"], [
        ["0-3 min", "Cold-call launch, stand/sit vote (Anchor 1) — no explanation"],
        ["3-8 min", "Position defense: convince us it's right for Dara's actual timeline"],
        ["8-13 min", "Define the process (Anchor 3)"],
        ["13-20 min", "Data Deep Dive: derive functions, solve break-even, evaluate at 91 weeks — name the trap"],
        ["at 20 min", "DROP THE TWIST — Zoomo's 26% price-increase precedent"],
        ["20-25 min", "Immediate recommit"],
        ["25-35 min", "Threaded deep conflict: (1) 'eventually cheaper' vs. horizon-matched cheaper; (2) a margin that flips on one cited precedent"],
        ["35-45 min", "Close, re-vote, reflection, Lessons Learned"],
      ], [2200, 6800]),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("The Weekly Rate - Facilitator Guide.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
