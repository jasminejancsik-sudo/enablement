# NORAM Account Executive Onboarding Programme

A 90-day onboarding programme for AEs at Checkout.com: what exists today, what needs refreshing, and what needs to be built.

| File | Use it for |
|---|---|
| [`ae-onboarding-program.html`](ae-onboarding-program.html) | **Leadership view.** Open it in a browser. It covers the journey, the weekly learning load, readiness by phase, the build list, the Day 60/90 stacks, the certifications, what changes from today, success measures, and a searchable session inventory. Works in light and dark mode and prints cleanly. |
| [`ae-onboarding-tracker.xlsx`](ae-onboarding-tracker.xlsx) | **Working tracker.** Tabs: Programme (every session by week and weekday, with objective, status, catalogue ID and feedback columns) · Build Plan · Explore Call Cert and Pitch Deck Cert scorecards · New Hire Tracker · Who to Meet. |
| [`build/program_data.py`](build/program_data.py) | **Single source of truth.** Sessions, phases, stacks, rubrics and metrics. |

## Programme at a glance (v2)
- **Working days.** Week N, weekday D = working day (N−1)×5 + D. Day 30 = end of Week 6, Day 60 = end of Week 12, Day 90 = end of Week 18. Cohorts start on the 1st and the 15th.
- **Blocks:** Before Day 1 → Days 1–30 *Get certified* → Days 31–60 *Build pipeline* → Days 61–90 *Win deals* → After Day 90.
- **Certifications, both by Day 30:** Explore Call Certification (Day 25, Week 5 Fri) and Pitch Deck Certification (Day 30, Week 6 Fri). The pitch is a first-meeting deck for a standard case. Each runs as a batch day per cohort; retakes by Day 35, with supplemental materials.
- **Day 60, Follow the Flow** (Week 12 Wed): one real deal goes through every partner team as a payment flow (Authorise → Risk check → Tokenise & integrate → Route → Settle → Reconcile).
- **Day 90, Deal Room** (Week 18 Wed): the AE presents a full proposal for their top live deal. Coaching, not scored.
- **Catalogue alignment:** sessions from the global Commercial Onboarding Sessions catalogue carry their catalogue ID. NORAM versions are added for intros that exist only for UK/EEA.
- **Tracker:** each tab has a leadership summary block at the top. The New Hire Tracker fills in target dates from the start date using WORKDAY.

## Updating
Edit `build/program_data.py`, then run:

```bash
python3 onboarding/ae/build/build.py
```

This regenerates both the HTML page and the Excel tracker. The Excel tracker is rebuilt from scratch, so copy any progress you've entered (e.g. in Build Backlog) somewhere else before regenerating, or track progress in a Google Sheets copy.

## Sources
Built from the [2025 Q4 USA New Hire Plan](../sales/q4-2025-usa-new-hire-plan-notes.md), the [NY Sales Class repository](../sales/ny-sales-class-onboarding-repository.md) and the [new hire tracker template](../sales/new-hire-onboarding-tracker-template.md), including Francesco's feedback from previous cohorts.
