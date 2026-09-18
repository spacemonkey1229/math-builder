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
function link(text, url) {
  const { ExternalHyperlink } = require("docx");
  return new ExternalHyperlink({
    link: url,
    children: [new TextRun({ text, style: "Hyperlink" })],
  });
}

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
      new Paragraph({ children: [new TextRun({ text: "Case Study: The Manifest Split", bold: true, size: 40, color: NAVY })], spacing: { after: 80 } }),
      p("MS | Math | Case Study | 2026-27 | Adventure", { italics: true, size: 20 }),

      h1("Overview"),
      p("Marcus Feld is standing at the gate-scan terminal at 9:40 at night, watching the flagged-container count keep climbing on the screen, when the yard supervisor leans over his shoulder and says the sentence he was hoping to avoid: “Cutoff’s in four hours, and the lane’s already backing up.”"),
      p("Every container on tonight’s sailing that got flagged during the gate scan — because a hazmat placard triggered the sensor, or because a reefer plug request hit the system — has to clear inspection before it can be loaded. Marcus doesn’t decide how many containers got flagged. He decides how they get processed. Right now, every flagged container funnels into one lane, one crew, checking for both hazmat compliance and reefer temperature control on whatever rolls up next. It’s simple. It’s also slow, and getting slower by the minute."),
      p("There’s a second option sitting in his terminal-ops binder, dog-eared from the last planning meeting: split the lane in two. One crew does nothing but hazmat placard and documentation checks. Another does nothing but reefer plug and setpoint checks. Faster, specialist crews — except for the containers that are both hazmat and reefer, which would have to get pulled off one lane, hauled across the yard, and re-queued on the other."),
      p("The yard supervisor is still standing there. The gate-scan screen is still climbing."),
      p("Marcus opens the manifest count on his tablet and does not press submit on either lane assignment yet."),

      h1("Background"),
      pRuns([new TextRun("Marcus Feld is the customs and logistics coordinator on the night shift at a mid-sized container terminal. He is personally accountable for making sure every container flagged for hazardous-materials or refrigerated-cargo inspection clears before the ship’s loading cutoff — a container that misses cutoff gets bumped to the next sailing, which costs the terminal a contractual penalty and costs the shipper a customer relationship. Containerized cargo moves the overwhelming majority of world trade by volume — maritime transport alone carries more than 80% of goods traded worldwide (SEE APPENDIX E) — and a terminal’s inspection lane is one of the few places in that whole chain where a single bottleneck can hold up an entire vessel.")]),
      pRuns([new TextRun("Two categories of flagged cargo drive tonight’s bottleneck. "), bold("Hazmat-flagged containers"), new TextRun(" carry cargo regulated under one of the International Maritime Organization’s nine hazard classes — from flammable liquids to the lithium-ion batteries now common in consumer electronics and e-bike shipments (SEE APPENDIX A) — and require a placard and documentation check before loading. "), bold("Reefer-flagged containers"), new TextRun(" carry temperature-controlled cargo and require a plug and setpoint verification before loading. Some containers are flagged for both reasons at once: a temperature-sensitive hazardous cargo, or — increasingly, per a supplemental compliance bulletin the terminal follows — a refrigerated shipment of lithium-ion cells that also needs hazmat placarding.")]),
      pRuns([new TextRun("Marcus has exactly two lane configurations available for tonight’s flagged pool, and the terminal’s operations manual requires he commit to one before the crew shift locks in (SEE APPENDIX B for the flagged counts and SEE APPENDIX C for the per-container inspection and re-handling times each configuration requires). "), bold("The Combined Lane"), new TextRun(" runs every flagged container through one generalist crew certified to check both hazmat and reefer requirements — no re-handling, but every check the crew performs runs slower because the crew has to stay ready to switch procedures container to container. "), bold("The Split Lanes"), new TextRun(" run two specialist crews, each faster at its own single job — but any container flagged for both categories has to be physically pulled from one lane, re-handled across the yard, and re-queued on the other, which costs real time neither specialist check requires on its own.")]),
      p("Every figure in this case is either cited to a real source or disclosed as a stated Modeling Assumption (SEE APPENDIX D). The vocabulary and “how to…” skills this case will ask you to research are listed in Appendix F — that is where Challenge 1 sends you."),

      h1("Dilemma"),
      p("You are Marcus Feld."),
      p("Do you:"),
      pRuns([bold("A.) "), new TextRun("Run The Combined Lane — one generalist crew, certified for both hazmat and reefer checks, no re-handling required OR")]),
      pRuns([bold("B.) "), new TextRun("Run The Split Lanes — two specialist crews, each faster at its own single check, but any dual-flagged container must be re-handled between lanes")]),

      h1("Challenges"),
      p("1.) Research and find an online resource that answers one of the “how to…” questions from the case study launch. Post a link to the resource as your submission."),
      p("2.) Post 250 or more “excellent” words pitching a firm stance to your audience on which you would choose and why. Your pitch must include:"),
      p("    a.) Use of the “how to…” resource you researched in Challenge 1."),
      p("    b.) At least one original visual display of the data."),
      p("3.) Your pitch must include:"),
      pRuns([bold("D1 — A labeled Venn diagram of tonight’s flagged manifest. "), new TextRun("Using Appendix B’s counts for the hazmat-flagged set (H), the reefer-flagged set (R), and the total number of distinct flagged containers (the union, H ∪ R, read directly off the gate-scan log), calculate how many containers are flagged for both categories (the intersection, H ∩ R). Draw a Venn diagram showing H, R, their overlap, and every region’s correct count. Show the arithmetic — do not just state the intersection count.")]),
      pRuns([bold("D2 — A total-inspection-time table for each lane configuration. "), new TextRun("Using Appendix C’s per-container check times, compute the total inspector-minutes The Combined Lane requires and the total inspector-minutes The Split Lanes requires (including the re-handling time for every container in the intersection you found in D1). Convert both totals to inspector-hours.")]),
      pRuns([bold("D3 — A containers-cleared-per-inspector-hour comparison. "), new TextRun("Using D1’s union count (the total distinct containers cleared, which is the same under either configuration) and D2’s inspector-hours, compute the containers-cleared-per-inspector-hour rate for each lane configuration, and the percent margin between them. State which configuration wins on tonight’s numbers.")]),
      pRuns([bold("D4 — A one-paragraph written recommendation. "), new TextRun("Name which lane configuration you are submitting and why, using D3’s numbers. Then answer directly: if the intersection you found in D1 had instead been the empty set — no container flagged for both categories at all — would the two configurations’ rates differ? Explain why or why not, using what a Venn diagram with no overlap actually shows about each container’s inspection path.")]),
      p("4.) An appendix showing evidence of your original thinking, work, calculations and processes you used to complete the challenges (pictures, screenshots, notes, etc.). Your work in the appendix does not count toward your word count."),
      p("5.) Participate twice or more in the Case Study discussion. *If you are absent the day of a discussion post 500 “excellent” words on the questions above."),

      h1("Appendix A — Hazmat Classification: The IMDG Code"),
      p("Referenced in Background and Challenge 3 (D1). The International Maritime Organization’s International Maritime Dangerous Goods (IMDG) Code defines nine hazard classes that govern which containers get hazmat-flagged at the gate scan [S1]:"),
      table(["Class", "Category"], [
        ["1", "Explosives"],
        ["2", "Gases (compressed, liquefied, or dissolved under pressure)"],
        ["3", "Flammable liquids"],
        ["4", "Flammable solids"],
        ["5", "Oxidizing substances and organic peroxides"],
        ["6", "Toxic and infectious substances"],
        ["7", "Radioactive materials"],
        ["8", "Corrosive substances"],
        ["9", "Miscellaneous dangerous goods (includes lithium-ion batteries and dry ice)"],
      ], [1200, 7800]),
      p("Class 9 is the category driving tonight’s overlap: lithium-ion battery shipments — increasingly shipped inside refrigerated containers to protect battery performance and safety in transit — are frequently both Class 9 hazmat-flagged and reefer-flagged at once. This case does not need the details of Classes 1–8; they are included here because the classification system is real and the manifest a real terminal works from genuinely lists all nine."),

      h1("Appendix B — Tonight’s Flagged Manifest"),
      p("Referenced in Background and Challenge 3 (D1, D2, D3)."),
      table(["Set", "Count", "How it’s known"], [
        ["Hazmat-flagged containers (H)", "90", "Gate-scan hazmat placard/documentation trigger count, this sailing"],
        ["Reefer-flagged containers (R)", "130", "Gate-scan reefer plug-request count, this sailing"],
        ["Total distinct flagged containers (H ∪ R)", "195", "Total unique container IDs that triggered either flag, read directly off the gate-scan log"],
        ["Flagged for both (H ∩ R)", "(Challenge D1 — calculate this)", "—"],
      ], [3400, 2000, 3600]),
      p("These three given counts (H, R, and the union) are specific to tonight’s sailing and are disclosed Modeling Assumptions, not published statistics — see Appendix D, MA1."),

      h1("Appendix C — Inspection and Re-Handling Times"),
      p("Referenced in Background and Challenge 3 (D2, D3)."),
      table(["Configuration", "Check", "Time per container"], [
        ["The Combined Lane", "Hazmat check (generalist crew)", "8 minutes"],
        ["The Combined Lane", "Reefer check (generalist crew)", "7 minutes"],
        ["The Split Lanes", "Hazmat check (specialist crew)", "6 minutes"],
        ["The Split Lanes", "Reefer check (specialist crew)", "5 minutes"],
        ["The Split Lanes", "Re-handle (crane pull, yard move, re-queue) — only for containers flagged for both categories", "11 minutes"],
      ], [2400, 4900, 1700]),
      p("How to read this table: In The Combined Lane, a container flagged for only one category gets only that one check; a container flagged for both gets both checks back-to-back, in the same lane, with no re-handling. In The Split Lanes, a container flagged for only one category goes to that one specialist lane; a container flagged for both must complete a check in one lane, then be re-handled to the other lane to complete the second check — paying the specialist lane’s faster check times, plus the 11-minute re-handle cost, for each of those containers."),
      p("All five times in this table are disclosed Modeling Assumptions — see Appendix D, MA2–MA6."),

      h1("Appendix D — Modeling Assumptions"),
      p("These figures are not sourced from an external publisher. No public dataset reports a specific terminal’s per-sailing hazmat/reefer flag counts or its internal crew inspection times — that information is operational and proprietary to individual terminals. They are stated scenario assumptions chosen by the case author. A Hero may challenge any of these numbers in discussion — that is a legitimate move.", { italics: true }),
      table(["#", "Assumption", "Value used", "Basis", "Sensitivity"], [
        ["MA1", "Tonight’s flagged-manifest counts (H, R, and H ∪ R)", "H = 90, R = 130, H ∪ R = 195", "No public source publishes a specific terminal’s per-sailing hazmat/reefer flag breakdown for a single vessel call — this is internal gate-scan data. Set at a scale consistent with a mid-sized container terminal processing a multi-thousand-TEU vessel call, where flagged cargo is a real but small fraction of the total manifest.", "The case’s whole comparison is sensitive to these counts — a different union total, or a different split between H and R, changes the intersection size Challenge D1 asks you to find, which is the whole basis of the decision."],
        ["MA2", "The Combined Lane hazmat check time", "8 minutes/container", "No public source publishes a generalist crew’s per-container hazmat check time. Set higher than the specialist figure (MA4) to reflect that a crew certified for both hazmat and reefer procedures must stay ready to switch checklists container to container, which real operations-management literature on task-switching generally associates with a time cost relative to single-task specialization — no terminal-specific figure exists to cite directly.", "The case’s numbers are sensitive to this figure."],
        ["MA3", "The Combined Lane reefer check time", "7 minutes/container", "Same basis and same sensitivity class as MA2, applied to the reefer half of the combined check.", "Same sensitivity class as MA2."],
        ["MA4", "The Split Lanes hazmat check time", "6 minutes/container", "Set below MA2 to reflect a specialist crew running one procedure repeatedly rather than switching between two. No public source publishes a terminal-specific hazmat check duration; informed only by the general principle that task specialization is faster than task-switching.", "Sensitive to this figure."],
        ["MA5", "The Split Lanes reefer check time", "5 minutes/container", "Same basis as MA4, applied to the specialist reefer lane. A real, published pre-trip reefer inspection guide describes this class of check (setpoint verification, plug/genset condition) as short — on the order of a few minutes — which is consistent with, but not a direct source for, this specific value [S2].", "Same sensitivity class as MA4."],
        ["MA6", "Re-handle time for a dual-flagged container", "11 minutes/container", "No public source publishes a terminal’s specific inter-lane container transfer time. A real, published container-terminal productivity benchmark states that top terminals reach more than 30 yard-crane movements per hour — a floor of roughly 2 minutes per crane movement alone [S3] — but a full re-handle is more than one crane cycle: it includes potentially un-stacking other containers, the yard-truck move itself, and re-queuing at the second lane. This value is set above the crane-cycle floor to reflect that fuller process, as a disclosed assumption rather than a directly sourced figure.", "The case’s numbers are highly sensitive to this figure."],
      ], [700, 2100, 1900, 3200, 1100]),

      h1("Appendix E — Sources"),
      table(["#", "Claim", "Value", "Source", "Date", "Conf."], [
        ["S1", "The IMDG Code defines nine hazard classes for maritime dangerous goods, including Class 9 (misc., incl. lithium batteries and dry ice)", "9 classes", "IMO — IMDG Code (imo.org); cross-checked against Wikipedia’s “Dangerous goods” article", "IMDG Code in force 2026", "HIGH"],
        ["S2", "Pre-trip reefer container inspections (genset, setpoint, seal check) are short, on the order of a few minutes", "“a five-minute inspection”", "Royal Cold Storage — How to Test Reefer Unit Temperature Before Port Pickup", "accessed 2026-09-17", "MEDIUM"],
        ["S3", "Container-terminal yard-crane productivity benchmark", "“more than 30 movements per hour per crane”", "Envision Technology — Top 10 Container Terminal Performance Metrics", "accessed 2026-09-17", "MEDIUM"],
        ["S4", "Maritime transport carries more than 80% of goods traded worldwide by volume", ">80%", "UN Trade and Development (UNCTAD) — Review of Maritime Transport 2025", "2025", "HIGH"],
      ], [500, 2700, 1600, 2600, 1200, 900]),
      p("Full source links: S1 — https://www.imo.org/en/OurWork/Safety/Pages/DangerousGoods-default.aspx  ·  S2 — https://royalcoldstorage.com/how-to-test-reefer-unit-temperature-before-port-pickup/  ·  S3 — https://www.envisionesl.com/blog/top-10-container-terminal-performance-metrics  ·  S4 — https://unctad.org/system/files/official-document/rmt2025_en.pdf", { size: 18, italics: true }),

      h1("Appendix F — “How To…” Math Questions To Research"),
      h2("Vocabulary terms"),
      bullet("Set"), bullet("Subset"), bullet("Union"), bullet("Intersection"), bullet("Empty Set"), bullet("Venn Diagram"),
      h2("“How to…” questions"),
      bullet("How to find the union and intersection of two sets"),
      bullet("How to represent a set relationship using a Venn diagram"),
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("The Manifest Split - Case Study.docx", buf);
  console.log("wrote docx", buf.length, "bytes");
});
