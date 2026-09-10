const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, ShadingType, AlignmentType, LevelFormat, convertInchesToTwip,
} = require("docx");

const NAVY = "1a3a5c";

const numbering = {
  config: [
    {
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: convertInchesToTwip(0.35), hanging: convertInchesToTwip(0.2) } } } }],
    },
  ],
};

function h1(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_1, spacing: { before: 300, after: 150 } }); }
function h2(text) { return new Paragraph({ text, heading: HeadingLevel.HEADING_2, spacing: { before: 260, after: 120 } }); }
function p(text, opts = {}) { return new Paragraph({ children: [new TextRun({ text, ...opts })], spacing: { after: 120 } }); }
function pRuns(runs) { return new Paragraph({ children: runs, spacing: { after: 120 } }); }
function bullet(text) { return new Paragraph({ text, numbering: { reference: "bullets", level: 0 }, spacing: { after: 60 } }); }
function bold(text) { return new TextRun({ text, bold: true }); }

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
  numbering,
  styles: { default: { document: { run: { font: "Calibri", size: 22 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    children: [
      new Paragraph({ children: [new TextRun({ text: "Case Study: The Weekly Rate", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("MS | Math | Case Study | 2026-27 | Adventure", { italics: true, size: 20 }),

      h1("Overview"),
      p("The index card is zip-tied to Dara Voss's handlebars, laminated against the rain, and by 9:00 p.m. on a Tuesday it is covered in Sharpie numbers nobody else would bother to write down. Four deliveries in the last forty minutes. Battery running low. A pothole on 9th Avenue she has now hit twice this month and needs to remember to route around."),
      p("She used to enter numbers into other people's spreadsheets for a living — three years at a claims office before it downsized her out — and the habit never left. Every Sunday night she totals the card: miles ridden, weeks on the job, what she paid Zoomo for the bike she's been renting since her first shift."),
      p("Her phone buzzes against the handlebar mount. It's the email she's been waiting for all week: she's been accepted into a paralegal certificate program, evenings and weekends, starting in three weeks — a set, fixed length she already knows by heart. She can keep dashing the whole way through it — the schedule works — but the acceptance email has a tuition deadline attached, and tuition deadlines make a person look hard at every other number in their life."),
      p("Dara pulls over under an awning, phone in one hand, the rain-spotted index card in the other, and opens the calculator app. Two numbers are about to tell her something the card alone can't: whether the smarter move, for as long as the certificate program runs, is to keep paying Zoomo every week — or to walk into the shop three blocks from her apartment and just buy the bike outright."),

      h1("Background"),
      pRuns([new TextRun("Dara Voss delivers full-time for two food-delivery apps in New York City, riding an e-bike six days a week. She is not an employee of either app — she is an independent contractor who supplies her own transportation, the same as roughly 80,000 other app-based delivery workers citywide (SEE APPENDIX D) "), new TextRun("[S6]")]),
      pRuns([new TextRun("Every e-bike and battery she rides has to carry UL safety certification to be used for app-based delivery in NYC as of a rule that took effect January 26, 2026 (SEE APPENDIX D) "), new TextRun("[S6]"), new TextRun(" — a requirement both options in this case already satisfy, since Dara only ever considers bikes from established, certified sellers.")]),
      pRuns([new TextRun("Since her first shift, Dara has rented her e-bike week to week from "), bold("Zoomo"), new TextRun(", a delivery-e-bike rental company. Zoomo's current Standard Plan costs "), bold("$39 per week"), new TextRun(" and includes the bike, a charger, a U-lock, GPS tracking, and — critically — full maintenance and wear-and-tear coverage (SEE APPENDIX A) "), new TextRun("[S1]"), new TextRun(". Dara has never owned an e-bike before and has never had to budget for her own repairs.")]),
      p("The certificate-program acceptance email puts a fixed horizon on the question for the first time: Dara plans to keep dashing for 21 months (91 weeks) while she completes the program, and to stop dashing once it's done (SEE APPENDIX C). That horizon — not “forever,” not “one more week” — is what she has to plan against."),
      pRuns([bold("The Ownership Path. "), new TextRun("Buy a Rad Power Bikes RadRunner 3 Plus outright from the shop near her apartment for a one-time price, then pay her own electricity to charge it and her own money for maintenance and repairs out of pocket for as long as she owns it (SEE APPENDICES A AND C).")]),
      pRuns([bold("The Subscription Path. "), new TextRun("Keep paying Zoomo's $39-per-week Standard Plan for the full 21 months, with maintenance, repairs, and the bike itself already included in that weekly price (SEE APPENDIX A).")]),
      p("Every figure in this case is either cited to a real, named source or disclosed as a stated Modeling Assumption (SEE APPENDICES C AND D) — never invented quietly. Appendix B carries a plan from a different e-bike rental company, Whizz, that Dara is not choosing between — real pricing, deliberately included so you have to decide for yourself whether it belongs in your answer. The vocabulary and “how to…” skills this case will ask you to research are listed in Appendix E — that is where Challenge 1 sends you."),

      h1("Dilemma"),
      p("You are Dara Voss."),
      p("Do you:"),
      pRuns([bold("A.) "), new TextRun("Take The Ownership Path — buy the RadRunner 3 Plus outright now, and pay your own electricity and maintenance costs out of pocket for the next 21 months OR")]),
      pRuns([bold("B.) "), new TextRun("Take The Subscription Path — keep paying Zoomo's $39-per-week Standard Plan, maintenance and repairs fully included, for the same 21 months")]),

      h1("Challenges"),
      p("1.) Research and find an online resource that answers one of the “how to…” questions from the case study launch. Post a link to the resource as your submission."),
      p("2.) Post 250 or more “excellent” words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:"),
      p("    a.) Use of the “how to…” resource you researched in Challenge 1."),
      p("    b.) At least one original visual display of the data."),
      p("3.) Your pitch must include:"),
      pRuns([bold("D1. "), new TextRun("A weekly cost-function derivation. Using the itemized rate components in Appendix A, write each option's total cost as a function of the number of weeks, w, in simplified slope-intercept form: C(w) = mw + b. Show the distributive-property step that combines Option A's separate per-week charges into a single weekly rate, and show any like terms you combine along the way.")]),
      pRuns([bold("D2. "), new TextRun("A break-even system. Set the two cost functions from D1 equal to each other as a system of two linear equations, and solve algebraically for the break-even number of weeks. Round your answer to a sensible whole number of weeks and show your work.")]),
      pRuns([bold("D3. "), new TextRun("A net-savings x-intercept. Define a net-savings function, S(w), as Option B's cost function minus Option A's cost function, simplify it to a single weekly term (combining like terms), and solve algebraically for its x-intercept. In your own words, explain what the x-intercept represents in Dara's decision, and separately what S(0) — the y-intercept — represents.")]),
      pRuns([bold("D4. "), new TextRun("A distractor read. Appendix B graphs a real weekly-plus-deposit pricing plan from Whizz, a different e-bike rental company Dara is not actually choosing between. From the graph, identify its slope and y-intercept, write its linear equation, and explain in 2–3 sentences why this plan is not actually relevant to Dara's Ownership-vs-Subscription decision.")]),
      pRuns([bold("D5. "), new TextRun("A graph of both real options. On one set of labeled axes, graph Option A's and Option B's cost functions from D1 for w = 0 to at least 130 weeks. Mark and label the break-even intersection point from D2, and mark which option is cheaper on each side of it.")]),
      pRuns([bold("D6. "), new TextRun("A total-cost-at-horizon comparison. Evaluate both cost functions at Dara's actual 21-month (91-week) horizon, find the dollar difference between the two totals, and convert that difference to a percent margin of the more expensive option. State which option you recommend and why.")]),
      p("4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count."),
      p("5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 “excellent” words on the questions above."),

      h1("Appendix A — Cost Components"),
      pRuns([bold("The Subscription Path (Zoomo Standard Plan). "), new TextRun("$39.00 per week, all-inclusive: the e-bike itself, a charger, a U-lock, GPS tracking, and full maintenance/wear-and-tear coverage "), new TextRun("[S1]"), new TextRun(". No purchase price, no separate repair bills.")]),
      pRuns([bold("The Ownership Path (Rad Power Bikes RadRunner 3 Plus).")]),
      table(["Component", "Value", "Source"], [
        ["Purchase price (one-time)", "$2,299.00", "[S2]"],
        ["Battery capacity", "672 Wh (48V, 14Ah)", "[S2]"],
        ["Manufacturer real-world range per full charge", "25–45 miles", "[S2]"],
        ["U.S. average residential electricity price", "$0.1834 per kWh (June 2026)", "[S3]"],
        ["Annual e-bike maintenance, casual rider", "under $200/year", "[S4]"],
        ["Annual e-bike maintenance, regular commuter", "$400/year or more", "[S4]"],
        ["Electricity cost, 2,000–5,000 mi/year rider", "$10–$30/year", "[S4]"],
      ], [3800, 3200, 2000]),
      p("The purchase price does not include electricity or repairs — those are Dara's to pay as the owner. Nothing in this appendix tells you how many miles Dara rides in a week or what her own maintenance bill will actually be at her much heavier delivery mileage than a “regular commuter” — those figures are stated as Modeling Assumptions (SEE APPENDIX C), not looked up, because no public source publishes them for a full-time delivery courier's actual riding load."),

      h1("Appendix B — A Different Company's Plan (Not Dara's Choice)"),
      p("Whizz, a different e-bike rental company operating in the same cities as Zoomo, sells its own weekly plans to delivery riders — plans Dara is not considering, because she only ever compares Zoomo's Standard Plan against buying outright. Whizz's Philadelphia-market Storm-1 weekly plan costs $69.00 per week, and every Whizz weekly plan requires a mandatory $99.00 one-time deposit on top of the weekly rate [S5b]."),
      p("The published Interactive HTML renders this as a labeled line graph: total amount paid to Whizz under the Storm-1 weekly plan as a function of weeks, with two points marked — (0, $99) and (4, $375)."),

      h1("Appendix C — Modeling Assumptions"),
      p("These figures are not sourced. They are stated scenario assumptions chosen by the case author. A Hero may challenge them in discussion — that is a legitimate move.", { italics: true }),
      table(["#", "Assumption", "Value", "Basis"], [
        ["MA1", "Dara's average weekly mileage", "200 mi/week", "No public figure exists; consistent with 6 shifts/week at ~33 mi/shift."],
        ["MA2", "Charging efficiency used", "25 mi/charge (low end of range)", "A loaded delivery e-bike with frequent stops realistically lands near the low end of the manufacturer's stated range."],
        ["MA3", "Dara's own annual maintenance if she owns", "$900.00/year", "Scaled up from the sourced $400+/year 'regular commuter' figure for her much heavier delivery mileage."],
        ["MA4", "Dara's decision horizon", "21 months (91 weeks)", "Set by the length of the paralegal certificate program she has just been accepted into."],
      ], [900, 2600, 2500, 3000]),

      h1("Appendix D — Sources"),
      table(["#", "Claim", "Source", "Date", "Conf."], [
        ["S1", "Zoomo Standard Plan weekly price", "ridezoomo.com/us/home", "2026-09-10", "MEDIUM"],
        ["S2", "RadRunner 3 Plus price/battery/range", "electricbikereview.com", "2026-09-10", "MEDIUM"],
        ["S3", "U.S. average residential electricity price", "eia.gov Table 5.6.A", "2026-06", "HIGH"],
        ["S4", "Annual e-bike maintenance by rider type", "hovsco.com", "2026-09-10", "MEDIUM"],
        ["S5b", "Whizz weekly plan pricing & deposit", "getwhizz.com", "2026-09-10", "MEDIUM"],
        ["S6", "NYC delivery workforce scale & UL rule", "nyc.gov Mayor's Office", "2026-04", "HIGH"],
      ], [700, 3100, 2600, 1400, 1200]),

      h1("Appendix E — “How To…” Math Questions To Research"),
      h2("Vocabulary terms"),
      bullet("Variable"), bullet("Constant"), bullet("Coefficient"), bullet("Term"), bullet("Like Terms"),
      bullet("Distributive property"), bullet("X-Intercept"), bullet("Y-Intercept"), bullet("Slope"),
      bullet("System Of Equations"), bullet("Percent"), bullet("Addition"), bullet("Multiplication"), bullet("Rounding"),
      h2("“How to…” questions"),
      bullet("How to evaluate a variable expression (Substitution Property)"),
      bullet("How to add and subtract an expression with variables"),
      bullet("How to solve a multi-step equation with a variable on one side"),
      bullet("How to solve a multi-step equation with a variable on both sides"),
      bullet("How to identify the slope of a line given a set of data, or a graph of a line of a set of data, or its linear equation"),
      bullet("How to write a linear equation given a set of data"),
      bullet("How to write a linear equation given a graph of a line of a set of data"),
      bullet("How to draw a line of a set of data given its linear equation"),
      bullet("How to solve a system of linear equations"),
      bullet("How to find the percent of a number"),
      bullet("How to convert numbers to percents"),
      bullet("How to round a number to a specified place value"),
      bullet("How to add multi-digit numbers"),
      bullet("How to multiply any two numbers"),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("The Weekly Rate - Case Study.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
