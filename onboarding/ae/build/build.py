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


def summary():
    st = Counter(x["status"] for x in D.SESSIONS)
    by_phase = {p["key"]: Counter(x["status"] for x in D.SESSIONS if x["phase"] == p["key"]) for p in D.PHASES}
    load = defaultdict(lambda: {"Live": 0.0, "Self-paced": 0.0, "Practice": 0.0})
    for x in D.SESSIONS:
        k = "Practice" if x["fmt"] in ("Practice", "Certification") else x["fmt"]
        load[x["week"]][k] += x["hrs"]
    return st, by_phase, [dict(week=w, **load[w]) for w in sorted(load)]


def build_html():
    st, by_phase, load = summary()
    data = dict(program=D.PROGRAM, phases=D.PHASES, milestones=D.MILESTONES, sessions=D.SESSIONS,
                stacks=D.STACKS, certs=D.CERTS, changes=D.CHANGES, metrics=D.METRICS,
                status=dict(st), byPhase={k: dict(v) for k, v in by_phase.items()}, load=load)
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

    NAVY = "0B1F3A"
    head_font = Font(bold=True, color="FFFFFF")
    head_fill = PatternFill("solid", fgColor=NAVY)
    thin = Side(style="thin", color="D9D9D6")
    border = Border(bottom=thin)
    wrap = Alignment(wrap_text=True, vertical="top")
    fills = {"Ready": "DFF3DF", "Refresh": "FDF0CF", "Build": "F8DCDC"}
    phase_name = {p["key"]: f'{p["name"]} ({p["days"]})' for p in D.PHASES}

    wb = Workbook()

    def sheet(ws, title, headers, rows, widths, note=None):
        ws.title = title
        r0 = 1
        if note:
            ws.cell(1, 1, note).font = Font(italic=True, color="52514E")
            r0 = 3
        for i, h in enumerate(headers, 1):
            c = ws.cell(r0, i, h)
            c.font, c.fill, c.alignment = head_font, head_fill, Alignment(vertical="center", wrap_text=True)
        for r, row in enumerate(rows, r0 + 1):
            for i, v in enumerate(row, 1):
                c = ws.cell(r, i, v)
                c.alignment, c.border = wrap, border
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w
        ws.freeze_panes = ws.cell(r0 + 1, 1)
        ws.auto_filter.ref = f"A{r0}:{get_column_letter(len(headers))}{r0 + len(rows)}"
        return r0

    def status_cf(ws, col, first, last):
        rng = f"{col}{first}:{col}{last}"
        for k, color in fills.items():
            ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=[f'"{k}"'], fill=PatternFill("solid", fgColor=color)))

    fb_fill = PatternFill("solid", fgColor="EAF2FC")

    def feedback_fill(ws, cols, r0, n):
        for col in cols:
            ws[f"{col}{r0}"].fill = PatternFill("solid", fgColor="2A78D6")
            for r in range(r0 + 1, r0 + n + 1):
                ws[f"{col}{r}"].fill = fb_fill

    # 0. Feedback on the programme design
    ws = wb.active
    ws.title = "Feedback"
    ws["A1"] = "Review the programme: what should we keep, change or cut?"
    ws["A1"].font = Font(bold=True, size=16, color=NAVY)
    ws["A2"] = "Fill in the blue columns here for big-picture decisions, and the blue columns on the Inventory and Build Backlog tabs for individual sessions."
    ws["A2"].font = Font(italic=True, color="52514E")
    items = [("Phases", f'{p["name"]} ({p["days"]})', f'{p["theme"]}: {p["goal"]} Target selling time {p["selling"]}.') for p in D.PHASES]
    items += [("Gates", f'Day {m["day"]}: {m["name"]}', f'{m["what"]}. Pass: {m["pass"]}.') for m in D.MILESTONES]
    items += [("Stacks", D.STACKS[k]["title"], D.STACKS[k]["days"] + ". " + D.STACKS[k]["why"] + " Objectives: " + "; ".join(D.STACKS[k]["objectives"]) + ".") for k in ("D60", "D90")]
    items += [("Certifications", c["name"], f'{c["format"]} Assessors: {c["assessors"]}. Pass: {c["pass"]} Rubric: ' + "; ".join(a for a, _ in c["rubric"]) + ".") for c in D.CERTS]
    items += [("What changes", a, "New: " + b) for a, b in D.CHANGES]
    items += [("Success measures", a, "Target: " + b) for a, b in D.METRICS]
    r0 = 4
    for i, h in enumerate(("Area", "Item", "Detail", "Keep / Change / Cut", "Your feedback"), 1):
        c = ws.cell(r0, i, h)
        c.font, c.fill, c.alignment = head_font, head_fill, Alignment(vertical="center", wrap_text=True)
    for r, row in enumerate(items, r0 + 1):
        for i, v in enumerate(row, 1):
            c = ws.cell(r, i, v)
            c.alignment, c.border = wrap, border
    feedback_fill(ws, ("D", "E"), r0, len(items))
    dv = DataValidation(type="list", formula1='"Keep,Change,Cut,Discuss"')
    ws.add_data_validation(dv)
    dv.add(f"D{r0 + 1}:D{r0 + len(items)}")
    for col, w in zip("ABCDE", (16, 40, 90, 16, 50)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "A5"

    # 1. Overview
    ws = wb.create_sheet()
    ws.title = "Overview"
    ws["A1"] = D.PROGRAM["title"]
    ws["A1"].font = Font(bold=True, size=18, color=NAVY)
    ws["A2"] = D.PROGRAM["subtitle"]
    ws["A3"] = f'{D.PROGRAM["owner"]} · {D.PROGRAM["version"]}'
    ws["A3"].font = Font(italic=True, color="52514E")
    ws["A5"], ws["B5"] = "Sessions mapped", "=COUNTA(Inventory!C4:C500)"
    for i, k in enumerate(D.STATUSES):
        ws.cell(6 + i, 1, {"Ready": "Ready today", "Refresh": "Need refresh", "Build": "To build"}[k])
        ws.cell(6 + i, 2, f'=COUNTIF(Inventory!H4:H500,"{k}")')
    ws["A10"], ws["B10"] = "Build/refresh items done", '=COUNTIF(\'Build Backlog\'!I4:I500,"Done")'
    for r in range(5, 11):
        ws.cell(r, 1).font = Font(bold=True)
    r = 12
    for h, i in (("Phase", 1), ("Days", 2), ("Theme", 3), ("Goal", 4), ("Target selling time", 5)):
        c = ws.cell(r, i, h)
        c.font, c.fill = head_font, head_fill
    for p in D.PHASES:
        r += 1
        for i, v in enumerate((p["name"], p["days"], p["theme"], p["goal"], p["selling"]), 1):
            ws.cell(r, i, v).alignment = wrap
    r += 2
    for h, i in (("Milestone", 1), ("Day", 2), ("What", 3), ("Pass mark", 4)):
        c = ws.cell(r, i, h)
        c.font, c.fill = head_font, head_fill
    for m in D.MILESTONES:
        r += 1
        for i, v in enumerate((m["name"], m["day"], m["what"], m["pass"]), 1):
            ws.cell(r, i, v).alignment = wrap
    for col, w in zip("ABCDE", (30, 16, 34, 70, 18)):
        ws.column_dimensions[col].width = w

    # 2. Inventory
    ws = wb.create_sheet()
    rows = [[phase_name[x["phase"]], x["week"], x["title"], x["cat"], x["fmt"], x["hrs"], x["owner"], x["status"],
             {"D30": "Day 30", "D60": "Day 60 stack", "D90": "Day 90 stack"}.get(x["stack"], ""), x["note"], x["source"], "", ""]
            for x in D.SESSIONS]
    r0 = sheet(ws, "Inventory",
               ["Phase", "Week", "Session", "Category", "Format", "Hours", "Owner", "Status", "Stack", "What needs to happen / notes", "Source", "Keep / Change / Cut", "Your feedback"],
               rows, [22, 7, 52, 18, 13, 7, 30, 10, 13, 70, 14, 16, 50],
               note="Every AE onboarding session: what exists today (Ready), what needs updating (Refresh) and what's missing (Build).")
    dv = DataValidation(type="list", formula1='"Ready,Refresh,Build"', allow_blank=False)
    ws.add_data_validation(dv)
    dv.add(f"H{r0 + 1}:H500")
    status_cf(ws, "H", r0 + 1, 500)
    dv = DataValidation(type="list", formula1='"Keep,Change,Cut,Discuss"')
    ws.add_data_validation(dv)
    dv.add(f"L{r0 + 1}:L500")
    feedback_fill(ws, ("L", "M"), r0, len(rows))

    # 3. Build backlog
    ws = wb.create_sheet()
    todo = [x for x in D.SESSIONS if x["status"] != "Ready"]
    prio = lambda x: "P1" if (x["stack"] or x["cat"] == "Certification" or x["title"].startswith("Payments at Checkout")) else "P2"
    todo.sort(key=lambda x: (prio(x), x["status"] != "Build", x["week"]))
    rows = [[prio(x), x["status"], x["title"], phase_name[x["phase"]], x["week"], x["owner"], "", "", "Not started", "", x["note"]] for x in todo]
    r0 = sheet(ws, "Build Backlog",
               ["Priority", "Type", "Session", "Phase", "Week", "Proposed owner", "Owner agreed?", "Target date", "Progress", "Content link", "Brief"],
               rows, [9, 9, 50, 22, 7, 30, 14, 13, 13, 30, 70],
               note="P1 = needed for the next cohort (certifications, Day 60/90 stacks, Day 1 payments primer). Update Progress as content is built.")
    dv = DataValidation(type="list", formula1='"Not started,In design,In review,Pilot,Done"')
    ws.add_data_validation(dv)
    dv.add(f"I{r0 + 1}:I500")
    dv = DataValidation(type="list", formula1='"Yes,No - suggest other,TBD"')
    ws.add_data_validation(dv)
    dv.add(f"G{r0 + 1}:G500")
    status_cf(ws, "B", r0 + 1, 500)
    feedback_fill(ws, ("G",), r0, len(rows))
    ws.conditional_formatting.add(f"I{r0 + 1}:I500", CellIsRule(operator="equal", formula=['"Done"'], fill=PatternFill("solid", fgColor=fills["Ready"])))

    # 4. Certification scorecards
    for c in D.CERTS:
        ws = wb.create_sheet(c["name"].replace(" Certification", " Cert"))
        ws["A1"] = c["name"]
        ws["A1"].font = Font(bold=True, size=16, color=NAVY)
        for i, (k, v) in enumerate((("When", c["when"]), ("Format", c["format"]), ("Assessors", c["assessors"]), ("Pass mark", c["pass"])), 2):
            ws.cell(i, 1, k).font = Font(bold=True)
            ws.cell(i, 2, v).alignment = wrap
        ws["A7"], ws["A8"], ws["A9"] = "AE name", "Assessor", "Date"
        for a in ("A7", "A8", "A9"):
            ws[a].font = Font(bold=True)
        hr = 11
        for i, h in enumerate(("Section", "What good looks like", "Score (1–5)", "Evidence / coaching notes"), 1):
            cell = ws.cell(hr, i, h)
            cell.font, cell.fill = head_font, head_fill
        for j, (sec, good) in enumerate(c["rubric"], hr + 1):
            ws.cell(j, 1, sec).alignment = wrap
            ws.cell(j, 2, good).alignment = wrap
        last = hr + len(c["rubric"])
        dv = DataValidation(type="whole", operator="between", formula1="1", formula2="5")
        ws.add_data_validation(dv)
        dv.add(f"C{hr + 1}:C{last}")
        mx = 5 * len(c["rubric"])
        ws.cell(last + 2, 1, "Total").font = Font(bold=True)
        ws.cell(last + 2, 3, f"=SUM(C{hr + 1}:C{last})")
        ws.cell(last + 2, 4, f"out of {mx}")
        ws.cell(last + 3, 1, "Result").font = Font(bold=True)
        ws.cell(last + 3, 3, f'=IF(COUNT(C{hr + 1}:C{last})<{len(c["rubric"])},"Incomplete",IF(AND(SUM(C{hr + 1}:C{last})>={mx}*0.8,MIN(C{hr + 1}:C{last})>=3),"PASS","RETAKE"))')
        ws.conditional_formatting.add(f"C{last + 3}", CellIsRule(operator="equal", formula=['"PASS"'], fill=PatternFill("solid", fgColor=fills["Ready"])))
        ws.conditional_formatting.add(f"C{last + 3}", CellIsRule(operator="equal", formula=['"RETAKE"'], fill=PatternFill("solid", fgColor=fills["Build"])))
        for col, w in zip("ABCD", (32, 60, 12, 50)):
            ws.column_dimensions[col].width = w

    # 5. New hire tracker template
    ws = wb.create_sheet("New Hire Tracker")
    ws["A1"] = "AE Onboarding Tracker: make a copy for each new hire"
    ws["A1"].font = Font(bold=True, size=16, color=NAVY)
    labels = (("Name", "Region"), ("Job title", "Line manager"), ("Start date", "Enablement manager"), ("Buddy", "Cohort"))
    for i, (a, b) in enumerate(labels, 3):
        ws.cell(i, 1, a + ":").font = Font(bold=True)
        ws.cell(i, 4, b + ":").font = Font(bold=True)
    ws["B5"].number_format = "yyyy-mm-dd"
    hr = 8
    for i, h in enumerate(("Week", "Target date", "Session", "Format", "Owner", "Complete?", "My notes"), 1):
        c = ws.cell(hr, i, h)
        c.font, c.fill = head_font, head_fill
    r = hr
    for x in D.SESSIONS:
        if x["phase"] == "P5":
            continue
        r += 1
        ws.cell(r, 1, f"Week {x['week']}" if x["week"] else "Pre-board")
        ws.cell(r, 2, f'=IF($B$5="","",$B$5+{max(0, (x["week"] - 1) * 7 + 4)})' if x["week"] else '=IF($B$5="","",$B$5-3)')
        ws.cell(r, 2).number_format = "ddd d mmm"
        ws.cell(r, 3, x["title"]).alignment = wrap
        ws.cell(r, 4, x["fmt"])
        ws.cell(r, 5, x["owner"]).alignment = wrap
        ws.cell(r, 6, False)
    dv = DataValidation(type="list", formula1='"TRUE,FALSE"')
    ws.add_data_validation(dv)
    dv.add(f"F{hr + 1}:F{r}")
    ws.conditional_formatting.add(f"A{hr + 1}:G{r}", FormulaRule(formula=[f"$F{hr + 1}=TRUE"], fill=PatternFill("solid", fgColor=fills["Ready"])))
    ws["F2"], ws["G2"] = "Progress", f'=IFERROR(COUNTIF(F{hr + 1}:F{r},TRUE)/COUNTA(C{hr + 1}:C{r}),0)'
    ws["G2"].number_format = "0%"
    ws["F2"].font = ws["G2"].font = Font(bold=True, size=14, color=NAVY)
    for col, w in zip("ABCDEFG", (11, 13, 56, 13, 30, 11, 40)):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = ws.cell(hr + 1, 1)

    # 6. Who to meet
    ws = wb.create_sheet("Who to Meet")
    people = [
        ("P0", "Line manager & buddy", "Your manager and day-to-day guide"), ("P0", "Jim Cho", "VP Sales"),
        ("P1", "Michel Tornabene", "Revenue Enablement"), ("P1", "Zack Levine", "NORAM GM"),
        ("P1", "Faith Bergman", "Deal Management lead"), ("P1", "Rithvik Nair", "Your Deal Management contact"),
        ("P1", "Sandra Suen", "BDR lead + RevOps strategy"), ("P1", "Jarett Israel + team", "Underwriting"),
        ("P1", "Jaime Yeager / Louis Taupin / Luke Brauer", "Pod leaders (ATL / SF / NY)"),
        ("P1", "Matt Baum, Mike O'Connor & Ezra Cohen", "Financial Partnerships"),
        ("P1", "Cyril Chemla", "Strategic Accounts Team"), ("P2", "Michael Taylor", "TAM & SE lead"),
        ("P2", "Jeff Schmidt", "Sales Engineering lead"), ("P2", "Adam Manassero / Perrin Heyka", "Account Management"),
        ("P2", "Ginny Huber / Phoebe Caine", "Partnerships"), ("P2", "Marketing team", "Local marketing"),
        ("P2", "Max Totilo", "US Compliance"), ("P3", "Sam Boukhiam", "Top rep: tips & tricks"),
    ]
    r0 = sheet(ws, "Who to Meet", ["Priority", "Name", "Why", "Met?"], [list(p) + [False] for p in people], [9, 40, 40, 8],
               note="Aim to finish within your first month. Adapted from the NY Sales Class repository and Karlie Chen's tracker; update names per cohort.")

    path = os.path.join(OUT, "ae-onboarding-tracker.xlsx")
    wb.save(path)
    return path


if __name__ == "__main__":
    print(build_html())
    print(build_xlsx())
