"""Build the AE onboarding deliverables from program_data.py.

    python3 onboarding/ae/build/build.py
"""
import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import program_data as D  # noqa: E402

OUT = os.path.dirname(HERE)
BLOCK = {b["key"]: b for b in D.BLOCKS}


def when(x):
    if x["week"] == 0:
        return "Before Day 1"
    if x["week"] == 19:
        return "After Day 90"
    return f'Week {x["week"]} · {x["day"]}'


def priority(x):
    p1 = x["tag"] or x["fmt"] == "Certification" or x["title"].startswith("Payments at Checkout")
    return "P1" if p1 else "P2"


def summary():
    st = Counter(x["status"] for x in D.SESSIONS)
    by_block = {b["key"]: Counter(x["status"] for x in D.SESSIONS if x["block"] == b["key"]) for b in D.BLOCKS}
    load = defaultdict(lambda: {"Live": 0.0, "Self-paced": 0.0, "Practice": 0.0})
    for x in D.SESSIONS:
        k = "Practice" if x["fmt"] in ("Practice", "Certification") else x["fmt"]
        load[x["week"]][k] += x["minutes"] / 60
    return st, by_block, [dict(week=w, **{k: round(v, 2) for k, v in load[w].items()}) for w in sorted(load)]


def build_html():
    st, by_block, load = summary()
    sessions = [dict(x, when=when(x), priority=priority(x)) for x in D.SESSIONS]
    data = dict(program=D.PROGRAM, blocks=D.BLOCKS, milestones=D.MILESTONES, sessions=sessions,
                stacks=D.STACKS, certs=D.CERTS, changes=D.CHANGES, metrics=D.METRICS,
                status=dict(st), byBlock={k: dict(v) for k, v in by_block.items()}, load=load)
    html = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    html = html.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    html = html.replace("__TITLE__", D.PROGRAM["title"])
    path = os.path.join(OUT, "ae-onboarding-program.html")
    open(path, "w", encoding="utf-8").write(html)
    return path


def build_xlsx():
    from openpyxl import Workbook
    from openpyxl.formatting.rule import CellIsRule, FormulaRule
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation

    NAVY, GREY = "0B1F3A", "52514E"
    head_font = Font(bold=True, color="FFFFFF")
    head_fill = PatternFill("solid", fgColor=NAVY)
    sum_fill = PatternFill("solid", fgColor="F0EFEC")
    fb_fill = PatternFill("solid", fgColor="EAF2FC")
    fb_head = PatternFill("solid", fgColor="2A78D6")
    thin = Side(style="thin", color="D9D9D6")
    border = Border(bottom=thin)
    wrap = Alignment(wrap_text=True, vertical="top")
    fills = {"Ready": "DFF3DF", "Refresh": "FDF0CF", "Build": "F8DCDC"}
    label = D.STATUS_LABEL

    wb = Workbook()

    def title(ws, text, sub):
        ws["A1"] = text
        ws["A1"].font = Font(bold=True, size=16, color=NAVY)
        ws["A2"] = sub
        ws["A2"].font = Font(italic=True, color=GREY)

    def summary_block(ws, row, rows, ncols):
        """Leadership summary block: list of (label, value-or-formula) pairs laid out in pairs per row."""
        ws.cell(row, 1, "Leadership summary").font = Font(bold=True, color=NAVY, size=12)
        r = row + 1
        for i in range(0, len(rows), 3):
            for j, (k, v) in enumerate(rows[i:i + 3]):
                c1, c2 = ws.cell(r, 1 + j * 2, k), ws.cell(r, 2 + j * 2, v)
                c1.font = Font(bold=True, color=GREY)
                c2.font = Font(bold=True, size=12, color=NAVY)
                c2.alignment = Alignment(wrap_text=True, vertical="top", horizontal="left")
            for c in range(1, ncols + 1):
                ws.cell(r, c).fill = sum_fill
            r += 1
        return r + 1

    def table(ws, r0, headers, rows, widths, feedback_cols=()):
        for i, h in enumerate(headers, 1):
            c = ws.cell(r0, i, h)
            c.font, c.fill, c.alignment = head_font, head_fill, Alignment(vertical="center", wrap_text=True)
            if h in feedback_cols:
                c.fill = fb_head
        for r, row in enumerate(rows, r0 + 1):
            for i, v in enumerate(row, 1):
                c = ws.cell(r, i, v)
                c.alignment, c.border = wrap, border
                if headers[i - 1] in feedback_cols:
                    c.fill = fb_fill
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = ws.cell(r0 + 1, 3)
        ws.auto_filter.ref = f"A{r0}:{get_column_letter(len(headers))}{r0 + len(rows)}"
        return r0 + 1, r0 + len(rows)

    def status_cf(ws, col, first, last):
        rng = f"{col}{first}:{col}{last}"
        for k, color in fills.items():
            ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{label[k]}"'], fill=PatternFill("solid", fgColor=color)))

    def dv_list(ws, rng, items):
        dv = DataValidation(type="list", formula1='"' + ",".join(items) + '"')
        ws.add_data_validation(dv)
        dv.add(rng)

    # ---------- 1. Programme ----------
    ws = wb.active
    ws.title = "Programme"
    title(ws, D.PROGRAM["title"] + ": Programme", f'{D.PROGRAM["subtitle"]} · {D.PROGRAM["version"]} · Days are working days')
    ms = " · ".join(f'Day {m["day"]} {m["name"]} (Week {m["week"]} {m["dow"]})' for m in D.MILESTONES)
    headers = ["Block", "When", "Working day", "Session", "After this, the AE can…", "Format", "Minutes", "Owner", "Status",
               "Milestone / stack", "Notes & next step", "Catalogue ID", "Also for BDR", "Keep / Change / Cut", "Your feedback"]
    rows = [[BLOCK[x["block"]]["name"], when(x), x["wd"] or "", x["title"], x["objective"], x["fmt"], x["minutes"], x["owner"],
             label[x["status"]], x["tag"], x["note"], x["cat_id"], "Yes" if x["bdr"] else "", "", ""] for x in D.SESSIONS]
    # summary block above the table, with live formulas over the table
    tbl_top = 9
    first, last = tbl_top + 1, tbl_top + len(rows)
    rng = lambda col: f"${col}${first}:${col}${last}"
    srows = [("Sessions", f"=COUNTA({rng('D')})"),
             ("Ready today", f'=COUNTIF({rng("I")},"{label["Ready"]}")'),
             ("Needs refresh", f'=COUNTIF({rng("I")},"{label["Refresh"]}")'),
             ("To build", f'=COUNTIF({rng("I")},"{label["Build"]}")'),
             ("Days 1–30: to build", f'=COUNTIFS({rng("A")},"Days 1–30",{rng("I")},"{label["Build"]}")'),
             ("Milestones", ms)]
    summary_block(ws, 3, srows, 15)
    ws.merge_cells(start_row=5, start_column=6, end_row=5, end_column=15)
    first, last = table(ws, tbl_top, headers, rows, [12, 15, 9, 46, 46, 13, 9, 26, 14, 15, 50, 12, 9, 14, 40],
                        feedback_cols=("Keep / Change / Cut", "Your feedback"))
    status_cf(ws, "I", first, last)
    dv_list(ws, f"I{first}:I{last + 50}", [label[k] for k in D.STATUSES])
    dv_list(ws, f"N{first}:N{last + 50}", ["Keep", "Change", "Cut", "Discuss"])
    ws.conditional_formatting.add(f"A{first}:O{last}", FormulaRule(formula=[f'LEFT($D{first},1)="★"'], font=Font(bold=True, color=NAVY)))

    # ---------- 2. Build Plan ----------
    ws = wb.create_sheet("Build Plan")
    title(ws, "Build Plan", "Everything to build or refresh. P1 = needed for the next cohort (certifications, Follow the Flow, Deal Room, Day 1 payments primer).")
    todo = sorted([x for x in D.SESSIONS if x["status"] != "Ready"], key=lambda x: (priority(x), x["status"] != "Build", x["week"]))
    headers = ["Priority", "Type", "Session", "When", "Proposed owner", "Owner agreed?", "Target date", "Progress", "Content link", "Brief"]
    rows = [[priority(x), label[x["status"]], x["title"], when(x), x["owner"], "", "", "Not started", "", x["note"] or x["objective"]] for x in todo]
    tbl_top = 9
    first, last = tbl_top + 1, tbl_top + len(rows)
    rng = lambda col: f"${col}${first}:${col}${last}"
    srows = [("Items", f"=COUNTA({rng('C')})"), ("P1 items", f'=COUNTIF({rng("A")},"P1")'), ("P1 done", f'=COUNTIFS({rng("A")},"P1",{rng("H")},"Done")'),
             ("To build", f'=COUNTIF({rng("B")},"{label["Build"]}")'), ("To refresh", f'=COUNTIF({rng("B")},"{label["Refresh"]}")'),
             ("Owners agreed", f'=COUNTIF({rng("F")},"Yes")&" of "&COUNTA({rng("C")})')]
    summary_block(ws, 3, srows, 10)
    first, last = table(ws, tbl_top, headers, rows, [9, 14, 50, 15, 30, 16, 13, 13, 30, 70])
    status_cf(ws, "B", first, last)
    dv_list(ws, f"H{first}:H{last + 50}", ["Not started", "In design", "In review", "Pilot", "Done"])
    dv_list(ws, f"F{first}:F{last + 50}", ["Yes", "No - suggest other", "TBD"])
    ws.conditional_formatting.add(f"H{first}:H{last}", CellIsRule(operator="equal", formula=['"Done"'], fill=PatternFill("solid", fgColor=fills["Ready"])))

    # ---------- 3–4. Certification scorecards ----------
    for c in D.CERTS:
        ws = wb.create_sheet(c["name"].replace(" Certification", " Cert"))
        title(ws, c["name"], "One scorecard per AE. Copy the tab for each assessment.")
        r = summary_block(ws, 3, [("When", c["when"]), ("Pass mark", c["pass"]), ("Assessors", c["assessors"])], 6)
        ws.cell(r, 1, "Format").font = Font(bold=True, color=GREY)
        ws.cell(r, 2, c["format"]).alignment = wrap
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
        ws.row_dimensions[r].height = 48
        r += 2
        for k in ("AE name", "Assessor", "Date"):
            ws.cell(r, 1, k).font = Font(bold=True)
            r += 1
        hr = r + 1
        for i, h in enumerate(("Section", "What good looks like", "Score (1–5)", "Evidence / coaching notes"), 1):
            cell = ws.cell(hr, i, h)
            cell.font, cell.fill = head_font, head_fill
        for j, (sec, good) in enumerate(c["rubric"], hr + 1):
            ws.cell(j, 1, sec).alignment = wrap
            ws.cell(j, 2, good).alignment = wrap
        lastr = hr + len(c["rubric"])
        dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5")
        ws.add_data_validation(dv)
        dv.add(f"C{hr + 1}:C{lastr}")
        mx = 5 * len(c["rubric"])
        ws.cell(lastr + 2, 1, "Total").font = Font(bold=True)
        ws.cell(lastr + 2, 3, f"=SUM(C{hr + 1}:C{lastr})")
        ws.cell(lastr + 2, 4, f"out of {mx}")
        ws.cell(lastr + 3, 1, "Result").font = Font(bold=True)
        ws.cell(lastr + 3, 3, f'=IF(COUNT(C{hr + 1}:C{lastr})<{len(c["rubric"])},"Incomplete",IF(AND(SUM(C{hr + 1}:C{lastr})>={mx}*0.8,MIN(C{hr + 1}:C{lastr})>=3),"PASS","RETAKE by Day 35"))')
        ws.conditional_formatting.add(f"C{lastr + 3}", CellIsRule(operator="equal", formula=['"PASS"'], fill=PatternFill("solid", fgColor=fills["Ready"])))
        ws.conditional_formatting.add(f"C{lastr + 3}", CellIsRule(operator="equal", formula=['"RETAKE by Day 35"'], fill=PatternFill("solid", fgColor=fills["Build"])))
        for col, w in zip("ABCDEF", (32, 60, 14, 50, 14, 14)):
            ws.column_dimensions[col].width = w

    # ---------- 5. New Hire Tracker ----------
    ws = wb.create_sheet("New Hire Tracker")
    title(ws, "AE Onboarding Tracker", "Make a copy for each new hire. Enter the start date and every target date fills in (working days).")
    labels = (("Name", "Region"), ("Start date", "Line manager"), ("Cohort", "Buddy"))
    r = 4
    for a, b in labels:
        ws.cell(r, 1, a + ":").font = Font(bold=True)
        ws.cell(r, 4, b + ":").font = Font(bold=True)
        r += 1
    ws["B5"].number_format = "yyyy-mm-dd"
    hr = 12
    track = [x for x in D.SESSIONS if x["week"] != 19]
    lr = hr + len(track)
    for i, (k, v) in enumerate((("Progress", f'=IFERROR(COUNTIF(F{hr + 1}:F{lr},TRUE)/COUNTA(C{hr + 1}:C{lr}),0)'),
                                ("Explore cert (Day 25)", '=IF($B$5="","",WORKDAY($B$5,24))'),
                                ("Pitch Deck cert (Day 30)", '=IF($B$5="","",WORKDAY($B$5,29))'),
                                ("Follow the Flow (Day 60)", '=IF($B$5="","",WORKDAY($B$5,57))'),
                                ("Deal Room (Day 90)", '=IF($B$5="","",WORKDAY($B$5,87))'))):
        ws.cell(4 + i, 6, k).font = Font(bold=True, color=GREY)
        c = ws.cell(4 + i, 7, v)
        c.font = Font(bold=True, color=NAVY)
        c.number_format = "0%" if i == 0 else "ddd d mmm yyyy"
        ws.cell(4 + i, 6).fill = ws.cell(4 + i, 7).fill = sum_fill
    for i, h in enumerate(("When", "Target date", "Session", "Format", "Owner", "Complete?", "My notes"), 1):
        c = ws.cell(hr, i, h)
        c.font, c.fill = head_font, head_fill
    for r, x in enumerate(track, hr + 1):
        ws.cell(r, 1, when(x))
        ws.cell(r, 2, f'=IF($B$5="","",WORKDAY($B$5,{x["wd"] - 1}))' if x["wd"] else ('=IF($B$5="","",WORKDAY($B$5,-3))' if x["week"] == 0 else ""))
        ws.cell(r, 2).number_format = "ddd d mmm"
        ws.cell(r, 3, x["title"]).alignment = wrap
        ws.cell(r, 4, x["fmt"])
        ws.cell(r, 5, x["owner"]).alignment = wrap
        ws.cell(r, 6, False)
    dv_list(ws, f"F{hr + 1}:F{lr}", ["TRUE", "FALSE"])
    ws.conditional_formatting.add(f"A{hr + 1}:G{lr}", FormulaRule(formula=[f"$F{hr + 1}=TRUE"], fill=PatternFill("solid", fgColor=fills["Ready"])))
    for col, w in zip("ABCDEFG", (15, 13, 56, 13, 30, 22, 30)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = ws.cell(hr + 1, 1)

    # ---------- 6. Who to Meet ----------
    ws = wb.create_sheet("Who to Meet")
    title(ws, "Who to Meet", "Finish within the first 30 working days. Partner teams are met properly at Follow the Flow (Day 60).")
    people = [("P0", "Line manager & buddy", "Your manager and day-to-day guide"), ("P0", "Jim Cho", "VP Sales"),
              ("P1", "Jasmine Jancsik", "Lead Enablement, US"), ("P1", "Zack Levine", "NORAM GM"),
              ("P1", "Jaime Yeager / Louis Taupin / Luke Brauer", "Pod leaders (ATL / SF / NY)"),
              ("P1", "Faith Bergman / Rithvik Nair", "Deal Management"), ("P1", "Sandra Suen", "BDR lead + RevOps strategy"),
              ("P2", "Teammates in your pod", "Coffee in Weeks 1–2"), ("P2", "Sam Boukhiam", "Top rep: tips & tricks"),
              ("P2", "Marketing team", "Local marketing")]
    r = summary_block(ws, 3, [("People", len(people)), ("Met", f'=COUNTIF(D{8}:D{7 + len(people)},TRUE)'), ("Deadline", "Day 30 (Week 6)")], 4)
    table(ws, 7, ["Priority", "Name", "Why", "Met?"], [list(p) + [False] for p in people], [10, 40, 40, 10])

    path = os.path.join(OUT, "ae-onboarding-tracker.xlsx")
    wb.save(path)
    return path


if __name__ == "__main__":
    print(build_html())
    print(build_xlsx())
