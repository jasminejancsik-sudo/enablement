# NORAM Account Executive Onboarding Programme

A 90-day onboarding programme for AEs at Checkout.com: what exists today, what needs refreshing, and what needs to be built.

| File | Use it for |
|---|---|
| [`ae-onboarding-program.html`](ae-onboarding-program.html) | **Leadership view.** Open it in a browser. It covers the journey, the weekly learning load, readiness by phase, the build list, the Day 60/90 stacks, the certifications, what changes from today, success measures, and a searchable session inventory. Works in light and dark mode and prints cleanly. |
| [`ae-onboarding-tracker.xlsx`](ae-onboarding-tracker.xlsx) | **Working tracker.** Tabs: Overview (live counts) · Inventory (status dropdown) · Build Backlog (track progress as content is built) · Explore Call Cert and Pitch Deck Cert scorecards (auto-score with PASS/RETAKE) · New Hire Tracker (enter a start date and target dates fill in; copy it for each AE) · Who to Meet. |
| [`build/program_data.py`](build/program_data.py) | **Single source of truth.** Sessions, phases, stacks, rubrics and metrics. |

## Programme at a glance
- **Phases:** Pre-board → Land (D1–14) → Learn (D15–30) → Practice (D31–60) → Perform (D61–90) → Everboard.
- **Gates:** Day 30 Checkpoint (elevator pitch + five-pillar check) · **Day 60 Explore Call Certification** · **Day 90 Pitch Deck Certification**.
- **Stacked moments:** *Explore Week* (Days 56–60) and *Propose Week* (Days 86–90). Related sessions are grouped right before each certification, each with focused learning objectives.
- **Pacing:** Payments Academy moves from Day 2 to Week 2. A 60-minute "Payments at Checkout" story comes first. Weekly structured learning drops from about 15 hours to about 5 hours as selling time grows.
- **Inventory:** 83 sessions. 51 are ready today, 14 need a refresh and 18 need to be built.

## Updating
Edit `build/program_data.py`, then run:

```bash
python3 onboarding/ae/build/build.py
```

This regenerates both the HTML page and the Excel tracker. The Excel tracker is rebuilt from scratch, so copy any progress you've entered (e.g. in Build Backlog) somewhere else before regenerating, or track progress in a Google Sheets copy.

## Sources
Built from the [2025 Q4 USA New Hire Plan](../sales/q4-2025-usa-new-hire-plan-notes.md), the [NY Sales Class repository](../sales/ny-sales-class-onboarding-repository.md) and the [new hire tracker template](../sales/new-hire-onboarding-tracker-template.md), including Francesco's feedback from previous cohorts.
