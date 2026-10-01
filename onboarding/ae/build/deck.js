// Builds onboarding/ae/ae-onboarding-v2-slides.pptx with pptxgenjs.
// Needs deck.json (exported from program_data.py) in the working directory: see README.
const pptxgen = require("pptxgenjs");
const D = require("./deck.json");
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.title = "NORAM AE Onboarding v2";

const C = { navy: "0B1F3A", navy2: "13345F", blue: "2A78D6", ice: "CADCFC", mint: "1BAF7A", white: "FFFFFF",
  ink: "1A1A1A", muted: "5A5A5A", card: "F3F6FA", line: "D9DEE6", good: "0CA30C", warn: "FAB219", crit: "D03B3B" };
const H = "Arial", B = "Calibri";
const W = 13.333, M = 0.5;

const txt = (s, t, o) => s.addText(t, Object.assign({ isTextBox: true, fontFace: B, color: C.ink, margin: 0, valign: "top" }, o));
const title = (s, t, sub, dark) => {
  txt(s, t, { x: M, y: 0.4, w: W - 2 * M, h: 0.7, fontFace: H, fontSize: 32, bold: true, color: dark ? C.white : C.navy, valign: "middle" });
  if (sub) txt(s, sub, { x: M, y: 1.08, w: W - 2 * M, h: 0.45, fontSize: 15, color: dark ? C.ice : C.muted });
};
const node = (s, x, y, d, label, fill, color) => {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } });
  txt(s, label, { x, y, w: d, h: d, align: "center", valign: "middle", fontFace: H, bold: true, fontSize: d > 0.5 ? 16 : 11, color });
};
const card = (s, x, y, w, h, fill) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill || C.card }, line: { color: fill || C.card } });
const bullets = (items, size, color) => items.map((t, i) => ({ text: t, options: { bullet: { indent: 12 }, breakLine: i < items.length - 1, fontSize: size, color: color || C.ink, paraSpaceAfter: 4 } }));

// ---------- 1. Title ----------
{
  const s = pres.addSlide(); s.background = { color: C.navy };
  txt(s, "NORAM REVENUE ENABLEMENT  ·  ONBOARD → RAMP → EVERBOARD", { x: M, y: 0.7, w: 10, h: 0.35, fontSize: 12, bold: true, color: C.ice, charSpacing: 2 });
  txt(s, "Account Executive Onboarding", { x: M, y: 1.15, w: 12, h: 0.9, fontFace: H, fontSize: 44, bold: true, color: C.white });
  txt(s, "90 working days from Day 1 to a winning proposal, built for selling payments at Checkout.com", { x: M, y: 2.05, w: 11, h: 0.5, fontSize: 18, color: C.ice });
  const st = D.status, tiles = [["Sessions mapped", D.sessions.length, C.ice], ["Ready today", st.Ready, C.good], ["Need refresh", st.Refresh, C.warn], ["To build", st.Build, C.crit]];
  tiles.forEach(([l, v, c], i) => {
    const x = M + i * 3.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 3.1, w: 2.9, h: 1.55, rectRadius: 0.08, fill: { color: C.navy2 }, line: { color: C.navy2 } });
    s.addShape(pres.shapes.OVAL, { x: x + 0.25, y: 3.32, w: 0.22, h: 0.22, fill: { color: c }, line: { color: c } });
    txt(s, l, { x: x + 0.55, y: 3.28, w: 2.2, h: 0.3, fontSize: 13, color: C.ice });
    txt(s, String(v), { x: x + 0.25, y: 3.65, w: 2.5, h: 0.85, fontFace: H, fontSize: 48, bold: true, color: C.white });
  });
  const ms = [["Day 25", "Explore Call Certification"], ["Day 30", "Pitch Deck Certification"], ["Day 60", "Follow the Flow"], ["Day 90", "Deal Room"]];
  ms.forEach(([d, n], i) => {
    const x = M + i * 3.1;
    node(s, x, 5.2, 0.42, d.replace("Day ",""), C.blue, C.white);
    txt(s, d, { x: x + 0.55, y: 5.17, w: 2.3, h: 0.28, fontSize: 14, bold: true, color: C.white });
    txt(s, n, { x: x + 0.55, y: 5.45, w: 2.3, h: 0.3, fontSize: 12, color: C.ice });
  });
  txt(s, "Jasmine Jancsik, Lead Enablement, US  ·  v2 draft, October 2026  ·  Days are working days", { x: M, y: 6.75, w: 12, h: 0.3, fontSize: 11, color: C.ice });
}

// ---------- 2. Journey ----------
{
  const s = pres.addSlide(); s.background = { color: C.white };
  title(s, "The 90-day journey", "Three 30-working-day blocks, each with one job. Both cohorts (starting on the 1st and the 15th) follow the same map.");
  const widths = [1.55, 2.95, 2.95, 2.95, 1.55], gap = 0.095;
  let x = M;
  D.blocks.forEach((b, i) => {
    const w = widths[i], big = i >= 1 && i <= 3, y = 1.75, h = 3.5;
    card(s, x, y, w, h, big ? C.card : "F7F8FA");
    txt(s, b.days.toUpperCase(), { x: x + 0.18, y: y + 0.2, w: w - 0.36, h: 0.25, fontSize: 10, bold: true, color: C.blue, charSpacing: 1 });
    txt(s, b.name, { x: x + 0.18, y: y + 0.47, w: w - 0.3, h: 0.4, fontFace: H, fontSize: big ? 20 : 13, bold: true, color: C.navy });
    txt(s, b.theme, { x: x + 0.18, y: y + 0.9, w: w - 0.36, h: 0.3, fontSize: 13, bold: true });
    txt(s, b.goal, { x: x + 0.18, y: y + 1.25, w: w - 0.36, h: 1.45, fontSize: big ? 12 : 10.5, color: C.muted });
    const ms = D.milestones.filter(m => b.weeks.includes(m.week));
    ms.forEach((m, j) => {
      const yy = y + h - 0.4 - (ms.length - 1 - j) * 0.36;
      node(s, x + 0.18, yy, 0.28, "", m.type === "cert" ? C.blue : C.mint, C.white);
      txt(s, `Day ${m.day} · ${m.name.replace(' Certification',' cert')}`, { x: x + 0.52, y: yy, w: w - 0.65, h: 0.28, fontSize: 11, bold: true, color: C.navy, valign: "middle" });
    });
    x += w + gap;
  });
  // 18-week strip
  txt(s, "18 working weeks", { x: M, y: 5.5, w: 4, h: 0.3, fontSize: 12, bold: true, color: C.muted });
  const sw = (W - 2 * M - 17 * 0.06) / 18, mw = Object.fromEntries(D.milestones.map(m => [m.week, m]));
  for (let i = 0; i < 18; i++) {
    const xx = M + i * (sw + 0.06), m = mw[i + 1];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: xx, y: 5.85, w: sw, h: 0.32, rectRadius: 0.05, fill: { color: m ? (m.type === "cert" ? C.blue : C.mint) : "E4E8EE" }, line: { color: m ? (m.type === "cert" ? C.blue : C.mint) : "E4E8EE" } });
    txt(s, String(i + 1), { x: xx, y: 5.85, w: sw, h: 0.32, align: "center", valign: "middle", fontSize: 10, bold: !!m, color: m ? C.white : C.muted });
    if (m) txt(s, `Day ${m.day}\n${{"Explore Call Certification":"Explore cert","Pitch Deck Certification":"Pitch cert"}[m.name] || m.name}`, { x: xx - 0.35, y: 6.25, w: sw + 0.7, h: 0.6, align: "center", fontSize: 9.5, color: C.navy, bold: true });
  }
}

// ---------- 3. Days 1–30 by week ----------
{
  const s = pres.addSlide(); s.background = { color: C.white };
  title(s, "Days 1–30: get certified", "Week by week, every session builds toward the two certifications at the end of Weeks 5 and 6.");
  const weeks = [
    ["Arrive & orient", ["Inductions + 90-day kickoff", "Intro to Revenue Org (NORAM)", "Payments at Checkout in 60 min", "Sales tools & finding answers", "Compliance + RevWay 0–1"]],
    ["Payments & market", ["Payments Academy, paced + debrief", "Competitive Landscape", "Buyer personas", "STP, Rules of Engagement & incentives", "Commercial Risk · International Outlook"]],
    ["The five pillars", ["Product Foundations: all five pillars", "Pillars in live deals", "Salesforce, Clari & pipeline", "Intro to Deal Management", "Issuing · Boost AMA"]],
    ["Explore", ["RevWay 4–5: Discovery & Explore", "Explore Call Masterclass", "Discovery question bank", "SAT-style Discover", "Pause and Play · role-play sprint"]],
    ["Certify: Explore", ["Elevator pitch + pillar check", "Top 70 account review", "Outreach lab · cold calls", "Pitch storyline workshop"], "Explore Call Cert · Day 25"],
    ["Certify: Pitch", ["RAC plans & NORAM strategy", "Commercial OKRs · Product Partnership", "Deck dry run with buddy", "Day 30 review"], "Pitch Deck Cert · Day 30"],
  ];
  const cw = (W - 2 * M - 5 * 0.15) / 6;
  weeks.forEach(([theme, items, cert], i) => {
    const x = M + i * (cw + 0.15), y = 1.75, h = 5.2;
    card(s, x, y, cw, h, cert ? "EAF2FC" : C.card);
    node(s, x + 0.15, y + 0.18, 0.42, String(i + 1), cert ? C.blue : C.navy, C.white);
    txt(s, `WEEK ${i + 1}`, { x: x + 0.67, y: y + 0.2, w: cw - 0.75, h: 0.2, fontSize: 10, bold: true, color: C.blue });
    txt(s, `Days ${i * 5 + 1}–${i * 5 + 5}`, { x: x + 0.67, y: y + 0.4, w: cw - 0.75, h: 0.2, fontSize: 10, color: C.muted });
    txt(s, theme, { x: x + 0.15, y: y + 0.75, w: cw - 0.3, h: 0.3, fontFace: H, fontSize: 13, bold: true, color: C.navy });
    s.addText(bullets(items, 12), { isTextBox: true, x: x + 0.12, y: y + 1.25, w: cw - 0.22, h: 2.9, fontFace: B, margin: 0, valign: "top" });
    if (cert) {
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.12, y: y + h - 0.95, w: cw - 0.24, h: 0.78, rectRadius: 0.06, fill: { color: C.blue }, line: { color: C.blue } });
      txt(s, cert, { x: x + 0.22, y: y + h - 0.9, w: cw - 0.44, h: 0.68, fontSize: 12, bold: true, color: C.white, valign: "middle" });
    }
  });
}

// ---------- 4. Certifications ----------
{
  const s = pres.addSlide(); s.background = { color: C.white };
  title(s, "Two certifications, both by Day 30", "Standard persona and standard case, so every AE is scored the same way. Batch day per cohort; retakes by Day 35.");
  const facts = [
    ["Day 25", "Explore Call Certification", "30-minute live, simulated Explore call against a standard Head of Payments persona (mid-market US subscription merchant). Recorded in Clari."],
    ["Day 30", "Pitch Deck Certification", "First-meeting deck for the same standard case everyone gets. 15-minute presentation + 10-minute panel Q&A. No pricing at this stage."],
  ];
  D.certs.forEach((c, i) => {
    const x = M + i * 6.25, y = 1.75, w = 6.0, h = 5.25;
    card(s, x, y, w, h);
    txt(s, facts[i][0], { x: x + 0.3, y: y + 0.25, w: 2, h: 0.6, fontFace: H, fontSize: 30, bold: true, color: C.blue });
    txt(s, facts[i][1], { x: x + 2.0, y: y + 0.3, w: 3.8, h: 0.5, fontFace: H, fontSize: 18, bold: true, color: C.navy, valign: "middle" });
    txt(s, facts[i][2], { x: x + 0.3, y: y + 0.95, w: w - 0.6, h: 0.75, fontSize: 12, color: C.muted });
    txt(s, "Pass: ≥ 80% and no section below 3/5  ·  Assessors: pod leads + Enablement", { x: x + 0.3, y: y + 1.72, w: w - 0.6, h: 0.3, fontSize: 11.5, bold: true, color: C.navy });
    c.rubric.forEach(([sec, good], j) => {
      const yy = y + 2.15 + j * 0.42;
      node(s, x + 0.3, yy, 0.3, String(j + 1), C.navy, C.white);
      txt(s, sec, { x: x + 0.72, y: yy - 0.02, w: 2.0, h: 0.36, fontSize: 11, bold: true, valign: "middle" });
      txt(s, good, { x: x + 2.75, y: yy - 0.02, w: w - 3.0, h: 0.36, fontSize: 10, color: C.muted, valign: "middle" });
    });
  });
}

// ---------- 5. Follow the Flow ----------
{
  const s = pres.addSlide(); s.background = { color: C.navy };
  title(s, "Day 60 · Follow the Flow", "One real deal, every desk. The AE's deal moves through the partner teams the way a payment moves through the payment chain.", true);
  const st = [["Authorise", "Deal Desk", "Get structure and pricing approved"], ["Risk check", "Underwriting", "Prepare a submittal that gets approved fast"],
    ["Tokenise & integrate", "Solutions Engineering", "Scope the integration for your prospect"], ["Route", "Partnerships + Financial Partnerships", "Find the partner angle in your deal"],
    ["Settle", "Account Management", "Plan a clean handover to go-live"], ["Reconcile", "RevOps & BDR", "Tidy your pipeline and plan with your BDR"]];
  const cw = (W - 2 * M - 5 * 0.15) / 6, y0 = 2.3;
  s.addShape(pres.shapes.LINE, { x: M + 0.4, y: y0 + 0.35, w: W - 2 * M - 0.8, h: 0, line: { color: C.blue, width: 3 } });
  st.forEach(([step, team, ex], i) => {
    const x = M + i * (cw + 0.15);
    node(s, x + cw / 2 - 0.35, y0, 0.7, String(i + 1), C.blue, C.white);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: y0 + 0.95, w: cw, h: 2.6, rectRadius: 0.08, fill: { color: C.navy2 }, line: { color: C.navy2 } });
    txt(s, step, { x: x + 0.15, y: y0 + 1.1, w: cw - 0.3, h: 0.6, fontFace: H, fontSize: 15, bold: true, color: C.white });
    txt(s, team, { x: x + 0.15, y: y0 + 1.72, w: cw - 0.3, h: 0.55, fontSize: 11.5, bold: true, color: C.ice });
    txt(s, ex, { x: x + 0.15, y: y0 + 2.3, w: cw - 0.3, h: 1.1, fontSize: 11.5, color: C.white });
  });
  txt(s, "Half-day workshop · Week 12 Wednesday · 30 minutes per station", { x: M, y: 6.2, w: 7, h: 0.3, fontSize: 13, bold: true, color: C.ice });
  txt(s, "The AE leaves with a one-page flow map for their deal, with a named contact at every step. This replaces the six team intros that used to sit in Week 2.", { x: M, y: 6.5, w: 12.3, h: 0.5, fontSize: 12, color: C.white });
}

// ---------- 6. Days 31–90 ----------
{
  const s = pres.addSlide(); s.background = { color: C.white };
  title(s, "Days 31–90: build pipeline, then win deals", "Once certified, AEs learn from their own deals. Learning steps back as selling time grows from 50% to 70%.");
  const cols = [
    ["Days 31–60 · Weeks 7–12", "Build pipeline", ["W7  Retakes · NORAM verticals · vertical deep dives · Apollo cadence", "W8  Underwriting · Intro to Pricing (NORAM) · partners · payment metrics", "W9  Payouts & FX · Visa Direct · integration · RevWay 6–7 · Canada", "W10  Head of Payments panel · top-rep Q&A · battlecards", "W11  Deal Management best practice · role play · Marketing & SAT", "W12  Follow the Flow · Day 60 review"]],
    ["Days 61–90 · Weeks 13–18", "Win deals", ["W13  Propose Masterclass · pricing guidance · RevWay 8–9", "W14  Pricing calculators · payments economics & cost analysis", "W15  Negotiation case studies · MAF & questionnaires · objections", "W16  Merchant ramp · QBRs · path to quota", "W17  Business case lab · proposal dry run", "W18  Deal Room · Day 90 review & graduation"]],
  ];
  cols.forEach(([wk, th, items], i) => {
    const x = M + i * 6.25, y = 1.75;
    card(s, x, y, 6.0, 3.45);
    txt(s, wk.toUpperCase(), { x: x + 0.3, y: y + 0.25, w: 5.4, h: 0.25, fontSize: 10.5, bold: true, color: C.blue });
    txt(s, th, { x: x + 0.3, y: y + 0.52, w: 5.4, h: 0.45, fontFace: H, fontSize: 22, bold: true, color: C.navy });
    s.addText(bullets(items, 13), { isTextBox: true, x: x + 0.25, y: y + 1.1, w: 5.5, h: 2.25, fontFace: B, margin: 0, valign: "top" });
  });
  // Deal Room callout
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y: 5.5, w: W - 2 * M, h: 1.3, rectRadius: 0.08, fill: { color: C.navy }, line: { color: C.navy } });
  node(s, M + 0.3, 5.87, 0.55, "90", C.mint, C.white);
  txt(s, "Day 90 · Deal Room", { x: M + 1.1, y: 5.72, w: 4, h: 0.4, fontFace: H, fontSize: 17, bold: true, color: C.white });
  txt(s, "The AE presents a full proposal for their top live deal, pricing included, to their manager and Deal Desk. Coaching, not a score, and it's the graduation from onboarding.", { x: M + 1.1, y: 6.12, w: 11.0, h: 0.55, fontSize: 13, color: C.ice });
}

// ---------- 7. Readiness & build list ----------
{
  const s = pres.addSlide(); s.background = { color: C.white };
  title(s, "What exists today, and what we need to build", `${D.sessions.length} sessions mapped from four sources. ${D.status.Ready} are ready today, ${D.status.Refresh} need a refresh and ${D.status.Build} need to be built.`);
  const labels = D.blocks.map(b => b.name);
  const ser = ["Ready", "Refresh", "Build"].map(k => ({ name: { Ready: "Ready today", Refresh: "Needs refresh", Build: "To build" }[k], labels, values: D.blocks.map(b => (D.byBlock[b.key] || {})[k] || 0) }));
  s.addChart(pres.charts.BAR, ser, { x: M, y: 1.7, w: 6.6, h: 5.2, barDir: "bar", barGrouping: "stacked", chartColors: [C.good, C.warn, C.crit],
    showLegend: true, legendPos: "b", legendFontSize: 11, showValue: true, dataLabelPosition: "ctr", dataLabelColor: C.white, dataLabelFontSize: 10,
    catAxisLabelColor: C.ink, catAxisLabelFontSize: 11, catAxisOrientation: "maxMin", valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
    showTitle: true, title: "Sessions by block and status", titleFontSize: 13, titleColor: C.navy, barGapWidthPct: 60 });
  const p1 = D.sessions.filter(x => x.status !== "Ready" && x.priority === "P1");
  const groups = [
    ["Certification build-up", p1.filter(x => x.tag === "Explore cert" || x.tag === "Pitch cert").length, "Masterclass, question bank, storyline workshop, both certifications"],
    ["Follow the Flow", p1.filter(x => x.tag === "Follow the Flow").length, "Six stations, one per partner team"],
    ["Deal Room", p1.filter(x => x.tag === "Deal Room").length, "Business case lab, dry run, Deal Room, Day 90 review"],
    ["NORAM intros", D.sessions.filter(x => x.cat_id.includes("UK/EEA") && !x.tag).length, "Pricing, Issuing, Merchant Insights, SAT Discover"],
    ["Day 1 payments primer", 1, "Payments at Checkout in 60 minutes"],
  ];
  card(s, 7.45, 1.7, 5.38, 5.2);
  txt(s, "P1: needed for the next cohort", { x: 7.7, y: 1.9, w: 5, h: 0.35, fontFace: H, fontSize: 16, bold: true, color: C.navy });
  groups.forEach(([g, n, d], i) => {
    const y = 2.45 + i * 0.85;
    node(s, 7.7, y, 0.55, String(n), C.crit, C.white);
    txt(s, g, { x: 8.42, y: y - 0.02, w: 4.2, h: 0.3, fontSize: 13, bold: true });
    txt(s, d, { x: 8.42, y: y + 0.28, w: 4.2, h: 0.35, fontSize: 11, color: C.muted });
  });
}

// ---------- 8. What changes + measures ----------
{
  const s = pres.addSlide(); s.background = { color: C.navy };
  title(s, "What changes, and how we'll measure it", null, true);
  const ch = [["Payments Academy on Day 2", "60-minute payments story first, Academy paced through Week 2"],
    ["Certifications at Days 60 and 90", "Both certified by Day 30, in batch days per cohort"],
    ["Six team intros in Week 2", "Follow the Flow at Day 60, using a real deal"],
    ["Calendar days, spread unevenly", "Working days, Week + weekday, same map for both cohorts"],
    ["UK/EEA-only intros", "NORAM versions of Pricing, Issuing, Merchant Insights, SAT Discover"],
    ["Pricing & negotiation never scheduled", "Weeks 13–16, right before the Deal Room"]];
  txt(s, "TODAY  →  NEW PROGRAMME", { x: M, y: 1.3, w: 7, h: 0.3, fontSize: 11, bold: true, color: C.ice, charSpacing: 1 });
  ch.forEach(([a, b], i) => {
    const y = 1.7 + i * 0.84;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y, w: 7.4, h: 0.72, rectRadius: 0.06, fill: { color: C.navy2 }, line: { color: C.navy2 } });
    txt(s, a, { x: M + 0.2, y: y + 0.08, w: 2.7, h: 0.56, fontSize: 11.5, color: C.ice, valign: "middle" });
    txt(s, "→", { x: M + 2.95, y: y + 0.08, w: 0.35, h: 0.56, fontSize: 16, bold: true, color: C.blue, align: "center", valign: "middle" });
    txt(s, b, { x: M + 3.35, y: y + 0.08, w: 3.9, h: 0.56, fontSize: 12, bold: true, color: C.white, valign: "middle" });
  });
  txt(s, "SUCCESS MEASURES", { x: 8.3, y: 1.3, w: 4.5, h: 0.3, fontSize: 11, bold: true, color: C.ice, charSpacing: 1 });
  D.metrics.forEach(([l, v], i) => {
    const y = 1.7 + i * 0.84;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.3, y, w: 4.53, h: 0.72, rectRadius: 0.06, fill: { color: C.white }, line: { color: C.white } });
    txt(s, v, { x: 8.45, y: y + 0.08, w: 1.75, h: 0.56, fontFace: H, fontSize: 14, bold: true, color: C.blue, valign: "middle" });
    txt(s, l, { x: 10.2, y: y + 0.08, w: 2.55, h: 0.56, fontSize: 10.5, color: C.ink, valign: "middle" });
  });
}

pres.writeFile({ fileName: "ae-onboarding-v2.pptx" }).then(f => console.log("wrote", f));
