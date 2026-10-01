"""Single source of truth for the NORAM Account Executive onboarding programme.

Both deliverables are generated from this file:
  python3 onboarding/ae/build/build.py
    -> onboarding/ae/ae-onboarding-program.html   (leadership view)
    -> onboarding/ae/ae-onboarding-tracker.xlsx   (working tracker)

Edit the lists below, then re-run the build.
"""

PROGRAM = {
    "title": "NORAM Account Executive Onboarding",
    "subtitle": "From Day 1 to first Propose: a 90-day path built for selling payments at Checkout.com",
    "owner": "Jasmine Jancsik, Lead Enablement, US",
    "version": "v1 draft, October 2026",
    "sources": [
        ("2025 Q4 USA New Hire Plan", "https://docs.google.com/spreadsheets/d/1Unozpi3AXkMcAO_rXoDNjW9CjWenfUTZv7BK6xwydi4/edit"),
        ("New York Sales Class: Onboarding Repository", "https://docs.google.com/spreadsheets/d/1cqKzHDs9KVDS616wynbUgFgrgOKayOayA8B7-XgqDqI/edit"),
        ("Karlie Chen: Onboarding Tracker (Q3 2026)", "https://docs.google.com/spreadsheets/d/1rb2HY82xgeAExbIBVEK1Wx7vHRnb4yQT_ddAv_rbqk4/edit"),
    ],
}

# Status vocabulary
#   Ready   = exists today and runs as-is
#   Refresh = exists, but needs re-sequencing, an update, or is paused
#   Build   = missing today; needs to be created
STATUSES = ["Ready", "Refresh", "Build"]

PHASES = [
    {"key": "P0", "name": "Pre-board", "days": "Before Day 1", "weeks": [0],
     "theme": "Arrive ready",
     "goal": "Day 1 is about people, not passwords. Tools, plan and buddy are in place before the AE walks in.",
     "selling": "0%"},
    {"key": "P1", "name": "Land", "days": "Days 1–14", "weeks": [1, 2],
     "theme": "Belong & orient",
     "goal": "Understand how Checkout sells, who's who, the territory and the rules of engagement. Payments is told as a story first, then studied as a curriculum.",
     "selling": "≤10%"},
    {"key": "P2", "name": "Learn", "days": "Days 15–30", "weeks": [3, 4],
     "theme": "Payments & product fluency",
     "goal": "Explain all five pillars in a merchant's language, see each pillar in live deals, and start call reviews and account planning.",
     "selling": "20%"},
    {"key": "P3", "name": "Practice", "days": "Days 31–60", "weeks": [5, 6, 7, 8, 9],
     "theme": "Verticals, process & discovery",
     "goal": "Go deep on NORAM verticals and the deal machine (deal desk, underwriting, partners), then prove discovery skills in the Day 60 Explore stack.",
     "selling": "50%"},
    {"key": "P4", "name": "Perform", "days": "Days 61–90", "weeks": [10, 11, 12, 13],
     "theme": "Price, propose & close",
     "goal": "Price a deal, build a business case and present a tailored Checkout pitch. Graduation is the Day 90 Pitch Deck Certification.",
     "selling": "70%"},
    {"key": "P5", "name": "Everboard", "days": "Day 90+", "weeks": [14],
     "theme": "Keep growing",
     "goal": "Recurring skills sessions, call clinics and yearly recertification keep tenured AEs sharp.",
     "selling": "90%+"},
]

MILESTONES = [
    {"day": 30, "week": 4, "name": "Day 30 Checkpoint", "type": "checkpoint",
     "what": "Elevator pitch sign-off + five-pillar knowledge check",
     "pass": "Pitch approved by manager · ≥ 80% on the pillar knowledge check"},
    {"day": 60, "week": 9, "name": "Explore Call Certification", "type": "cert",
     "what": "Live simulated Explore call with a payments persona, scored on a 7-part rubric",
     "pass": "≥ 80% overall and no section below 3/5"},
    {"day": 90, "week": 13, "name": "Pitch Deck Certification", "type": "cert",
     "what": "Tailored pitch deck for a real territory account, presented to a panel",
     "pass": "≥ 80% overall and no section below 3/5"},
]

# Session inventory.
# fields: phase, week, title, cat, fmt, hrs, owner, status, note, source
#   cat  : Foundations | Payments & Product | Sales Skills | Tools & Process | People & Network | Certification
#   fmt  : Live | Self-paced | Practice | Certification
#   hrs  : planned hours for the new hire (0 = no time cost to the new hire)
#   source: Q4 Plan | NY Repository | Karlie Tracker | New
S = []
def s(phase, week, title, cat, fmt, hrs, owner, status, note="", source="Q4 Plan", stack=None):
    S.append(dict(phase=phase, week=week, title=title, cat=cat, fmt=fmt, hrs=hrs,
                  owner=owner, status=status, note=note, source=source, stack=stack))

# ---------- P0 Pre-board ----------
s("P0", 0, "Welcome pack, 90-day plan & personal tracker issued", "Foundations", "Self-paced", 0.5,
  "Enablement", "Build",
  "Send the personal tracker (Karlie Chen format) and this 90-day map before Day 1 so the new hire arrives knowing the path.",
  "Karlie Tracker")
s("P0", 0, "Tool access pre-provisioned (Salesforce, Clari, Apollo, LinkedIn Sales Nav, Highspot, Glean)", "Tools & Process", "Self-paced", 0,
  "Enablement + IT", "Refresh",
  "Today this takes a Day 1 session. Request access at offer-accept so Day 1 can go to people and context.")
s("P0", 0, "Buddy assigned + manager welcome call", "People & Network", "Live", 0.5,
  "Line manager", "Refresh",
  "Buddies are used informally (elevator pitch, role plays). Formalise it with a one-page buddy guide and a weekly 30-minute slot.",
  "Karlie Tracker")

# ---------- P1 Land: weeks 1-2 ----------
s("P1", 1, "IT, People & Benefits inductions", "Foundations", "Live", 3, "People Team", "Ready")
s("P1", 1, "Your onboarding plan: the 30/60/90 kickoff", "Foundations", "Live", 0.5, "Enablement", "Ready")
s("P1", 1, "Intro to Checkout's Revenue Org (Global + NORAM)", "Foundations", "Live", 1.5, "Michel Tornabene", "Ready",
  "", "Karlie Tracker")
s("P1", 1, "Mandatory compliance training (Nova)", "Foundations", "Self-paced", 3, "New hire", "Ready")
s("P1", 1, "Payments at Checkout in 60 minutes", "Payments & Product", "Live", 1, "Enablement + Solutions Engineering", "Build",
  "A story-led primer: the life of a card transaction, where Checkout earns, and why merchants switch. It replaces the Day 2 deep dive into Payments Academy and gives context before the curriculum starts.",
  "New")
s("P1", 1, "Sales Tools & Chrome Extensions", "Tools & Process", "Live", 1, "J.J. Henry", "Ready", "", "Karlie Tracker")
s("P1", 1, "Finding answers: Highspot, Confluence & Glean", "Tools & Process", "Live", 1, "Enablement", "Refresh",
  "Update for the Highspot→Drive transition and Glean adoption (charter priority 3).")
s("P1", 1, "Office hours with the NORAM GM", "People & Network", "Live", 0.5, "Zack Levine", "Ready")
s("P1", 1, "RevWay 0–1: Intro to Revenue Way & Buyer Psychology", "Sales Skills", "Self-paced", 2.5, "Self-directed", "Ready")
s("P1", 1, "Meet your pod + buddy coffee", "People & Network", "Practice", 1, "Pod leader", "Ready")

s("P1", 2, "Buyer personas in payments (Head of Payments, CFO, CPO, Eng)", "Sales Skills", "Live", 1, "J.J. Henry", "Ready",
  "", "Karlie Tracker")
s("P1", 2, "Competitive Landscape", "Payments & Product", "Live", 1, "Michel Tornabene", "Ready")
s("P1", 2, "Territory planning (STP), Rules of Engagement & Incentive Ratings", "Tools & Process", "Live", 1, "Francesco Falcone", "Ready",
  "Must be live and finished by the end of Week 2. Francesco asked for this ASAP, early Week 3 at the latest.")
s("P1", 2, "Salesforce, Clari & pipeline hygiene", "Tools & Process", "Live", 1, "Francesco Falcone", "Ready", "", "Q4 Plan")
s("P1", 2, "AI in Commercial", "Tools & Process", "Live", 1, "Molly McKenna", "Ready")
s("P1", 2, "Meet the team: Sales, AM, Financial Partnerships, Partnerships, SE, RevOps", "People & Network", "Live", 3, "Team leads", "Ready",
  "Six 30-minute intros, using the prioritised Who-to-Meet list from the NY repository.", "NY Repository")
s("P1", 2, "Payments Academy: Foundations modules 1–5", "Payments & Product", "Self-paced", 2.5, "Self-directed", "Refresh",
  "Moved from Day 2 to Week 2 and paced at about 30 minutes a day, after the 60-minute primer, with a Friday live debrief.")
s("P1", 2, "RevWay 2–3: DEPTH Selling & Managing Pipeline", "Sales Skills", "Self-paced", 2.5, "Self-directed", "Ready")
s("P1", 2, "Friday knowledge check (Kahoot, pod leads join), runs weekly", "Payments & Product", "Practice", 0.5, "Enablement + pod leads", "Ready")

# ---------- P2 Learn: weeks 3-4 ----------
s("P2", 3, "Payments Academy: Foundations 6–10 + live debrief", "Payments & Product", "Self-paced", 3, "Enablement", "Refresh",
  "Finish the Foundations here, not in Week 1. The debrief turns the modules into talk-tracks.")
s("P2", 3, "Product Foundations: Connect & Move", "Payments & Product", "Self-paced", 2, "Self-directed", "Ready", "", "Karlie Tracker")
s("P2", 3, "Pillars in live deals: Connect & Move (30 min each)", "Payments & Product", "Live", 1, "Pod leads", "Refresh",
  "Replace the generic 'sales perspective' sessions with 30-minute walk-throughs of live deals, built on a vertical use case (Francesco's feedback).")
s("P2", 3, "International Outlook: acquiring set-ups & cross-border", "Payments & Product", "Live", 0.75, "Michel Tornabene", "Ready")
s("P2", 3, "Commercial Risk", "Payments & Product", "Live", 0.5, "Michel Tornabene", "Ready", "", "Karlie Tracker")
s("P2", 3, "Intro to NORAM verticals & where we win", "Payments & Product", "Live", 0.75, "Francesco Falcone", "Ready",
  "Pair this with the North America Vertical List in the NY repository.")
s("P2", 3, "Weekly call-review hour begins (Clari gametapes)", "Sales Skills", "Practice", 1, "Jim Cho + Francesco Falcone", "Ready",
  "Starts in Week 3, not Week 1, then runs weekly (Francesco's feedback).")
s("P2", 3, "Outreach lab: openers, email personalisation & gatekeepers", "Sales Skills", "Live", 2, "J.J. Henry", "Ready", "", "Karlie Tracker")

s("P2", 4, "Product Foundations: Protect, Boost & Manage", "Payments & Product", "Self-paced", 2.5, "Self-directed", "Ready", "", "Karlie Tracker")
s("P2", 4, "Pillars in live deals: Protect, Boost & Manage", "Payments & Product", "Live", 1, "Pod leads", "Refresh",
  "Same 30-minute live-deal format as Week 3.")
s("P2", 4, "Payment Performance AMA (Boost)", "Payments & Product", "Live", 1, "Daniel Linder", "Ready",
  "Focus on Boost, Daniel's pillar.")
s("P2", 4, "Account list review: your Top 70", "Sales Skills", "Practice", 1, "Line manager", "Ready", "", "Karlie Tracker")
s("P2", 4, "RevWay 4–5: Discovery & Explore phases", "Sales Skills", "Self-paced", 2.5, "Self-directed", "Ready")
s("P2", 4, "Cold-call role play", "Sales Skills", "Practice", 0.5, "J.J. Henry", "Ready", "", "Karlie Tracker")
s("P2", 4, "Day 30 Checkpoint: elevator pitch + five-pillar knowledge check", "Certification", "Certification", 1, "Line manager + Enablement", "Refresh",
  "Combine today's elevator-pitch reviews and pillar Kahoots into one recorded gate.", "Karlie Tracker", stack="D30")

# ---------- P3 Practice: weeks 5-9 ----------
s("P3", 5, "Vertical deep dives: Digital Content and Ecommerce", "Payments & Product", "Live", 1.5, "Jules Gay / Katie Wile", "Ready")
s("P3", 5, "Vertical deep dives: Neobank & Remittance (AFT/OCT), Consumer Lending & Proptech", "Payments & Product", "Live", 1.5, "Olivia Smith / Octavio Balcazar", "Ready")
s("P3", 5, "Intro to Deal Management & Deal Desk", "Tools & Process", "Live", 0.5, "Faith Bergman", "Ready", "", "Karlie Tracker")
s("P3", 5, "Partner ecosystem: who we sell with and how", "Payments & Product", "Live", 1, "Jim Cho / Francesco Falcone / Jaime Yeager", "Ready")
s("P3", 5, "Build your prospecting cadence (Apollo)", "Sales Skills", "Practice", 0.5, "Ronak Bali", "Ready")

s("P3", 6, "ISV, Marketplace & MoR deep dive", "Payments & Product", "Live", 0.5, "Michael Taylor", "Ready")
s("P3", 6, "Pay to Card, Pay to Bank & FX", "Payments & Product", "Live", 1, "Olivia Smith", "Ready")
s("P3", 6, "Visa Direct: AFTs & card payouts", "Payments & Product", "Live", 0.5, "Amber McClure", "Refresh",
  "Paused while partnership terms are revamped. Bring it back when the new terms are ready.")
s("P3", 6, "Technical integration & merchant onboarding experience", "Tools & Process", "Live", 0.5, "Michael Taylor + Faith Bergman", "Ready")
s("P3", 6, "Underwriting overview", "Tools & Process", "Live", 1, "Jack Pontarelli", "Ready", "", "Karlie Tracker")
s("P3", 6, "RevWay 6–7: Questioning, funnel technique & listening", "Sales Skills", "Self-paced", 3, "Self-directed", "Ready")

s("P3", 7, "Voice of the customer: Head of Payments panel", "Payments & Product", "Live", 1.5, "Jaime Yeager / Jim Cho", "Build",
  "Planned in both SME trackers but never scheduled. Heads of Payments share what resonated in outreach and what didn't.")
s("P3", 7, "Top-rep Q&A, every two weeks", "People & Network", "Live", 0.5, "Sam Boukhiam / Louis Taupin", "Build",
  "Planned to 'start in Month 2' but never started. Sam's notes in the Q4 plan are the starting agenda.")
s("P3", 7, "Vertical deep dives: Insurance and Gaming & Gambling", "Payments & Product", "Live", 1, "Olivia Smith / Aaron Popack", "Refresh",
  "Both on hold ('wait for now'). Run Insurance virtually first.")
s("P3", 7, "Canada & the Canadian market", "Payments & Product", "Live", 0.5, "Yousef Almawy", "Ready")
s("P3", 7, "Role play with your pod lead", "Sales Skills", "Practice", 0.5, "Pod leads", "Ready")

s("P3", 8, "Competitive deal clinic + refreshed battlecards", "Sales Skills", "Live", 1, "Jim Cho", "Refresh",
  "The 'Why Checkout Wins' battlecard is flagged as outdated. Release refreshed battlecards with this session.", "NY Repository")
s("P3", 8, "Payment performance metrics that matter (auth rates, declines, tokens, cost)", "Payments & Product", "Live", 1, "Solutions Engineering + Product", "Build",
  "The numbers an AE has to quantify in discovery. Builds on the Decline Code and PPA cheat sheets.", "New")
s("P3", 8, "Explore call gametapes: what great sounds like", "Sales Skills", "Practice", 1, "Jim Cho + Francesco Falcone", "Refresh",
  "Curate an Explore-only playlist in the Clari USA call repo, with timestamps to listen for.", "NY Repository")

# Day 60 stack: week 9
s("P3", 9, "Explore Call Masterclass: running discovery the Checkout way", "Sales Skills", "Live", 1.5, "Enablement + top AE", "Build",
  "Live, AE-specific application of RevWay 5–6: agenda, upfront contract, DEPTH funnel and summarise-to-commit.", "New", stack="D60")
s("P3", 9, "Payments discovery question bank & value hypothesis", "Sales Skills", "Live", 1, "Enablement + Solutions Engineering", "Build",
  "Questions by persona and pillar, plus a one-page value-hypothesis template (auth uplift, fraud, cost, APM coverage, payouts).", "New", stack="D60")
s("P3", 9, "Explore role-play sprint", "Sales Skills", "Practice", 1.5, "Pod leads + buddy", "Ready",
  "Three timed reps against three personas, with feedback on the certification rubric.", "Q4 Plan", stack="D60")
s("P3", 9, "★ Explore Call Certification", "Certification", "Certification", 1, "Pod lead + Enablement", "Build",
  "See the certification rubric.", "New", stack="D60")
s("P3", 9, "Day 60 review: pipeline, activity & ramp check", "Tools & Process", "Practice", 0.5, "Line manager", "Build",
  "A structured 1:1 on pipeline created, meetings booked and cert results, with the next 30-day plan.", "New", stack="D60")

# ---------- P4 Perform: weeks 10-13 ----------
s("P4", 10, "Propose Masterclass", "Sales Skills", "Live", 1.5, "Enablement", "Ready")
s("P4", 10, "Pricing guidance & take rate", "Tools & Process", "Live", 1, "Jim Cho + Francesco Falcone", "Build",
  "Listed in the Q3 SME tracker but never scheduled. Covers guardrails, approvals and how to talk about price.")
s("P4", 10, "Pricing calculator walk-through (real deal example)", "Tools & Process", "Live", 1, "Jim Cho", "Ready")
s("P4", 10, "AFT/OCT pricing calculator walk-through", "Tools & Process", "Live", 0.5, "Vladimir Sterenko", "Ready")
s("P4", 10, "RevWay 8–9: Propose & Presentation Skills", "Sales Skills", "Self-paced", 3.5, "Self-directed", "Ready")

s("P4", 11, "Payments economics: interchange++, fee & cost analysis", "Payments & Product", "Live", 1.5, "Deal Management + Solutions Engineering", "Build",
  "The resources exist (Gopuff and Rhino + Jetty cost analyses, L2/L3 interchange) and are tagged 'cover later', but there's no session.", "NY Repository")
s("P4", 11, "Trade, deal structure & negotiation case studies", "Sales Skills", "Live", 1, "Pod lead (TBD)", "Build",
  "Negotiation, getting pricing approved, and minimum billing. The owner is still TBD in the SME tracker.")
s("P4", 11, "Underwriting from the UW lens + MAF & questionnaires", "Tools & Process", "Live", 1, "Jarett Israel + Rithvik Nair", "Ready")
s("P4", 11, "Objection handling drill + RevWay 10", "Sales Skills", "Practice", 1.5, "Enablement", "Refresh",
  "Self-paced only today. Add a live drill that uses the competitive defense playbook.")

s("P4", 12, "How to ramp a merchant: what happens after 'yes'", "Tools & Process", "Live", 0.5, "Nicholas Schaffer", "Ready")
s("P4", 12, "QBR walk-through", "Tools & Process", "Live", 0.5, "Perrin Heyka", "Ready")
s("P4", 12, "MBO, quota mechanics & your path to quota", "Tools & Process", "Live", 1, "Francesco Falcone + Jim Cho", "Refresh",
  "Reschedule to 60 minutes with Jim, and invite newer hires.")
s("P4", 12, "Working with Marketing & the Strategic Accounts Team", "People & Network", "Live", 1, "Marketing + Cyril Chemla", "Ready")

# Day 90 stack: week 13
s("P4", 13, "Storyline workshop: building a Checkout pitch deck", "Sales Skills", "Live", 1.5, "Enablement + Product Marketing", "Build",
  "Insight → value → proof → plan, using the Great Decks library (GM, 1800 Contacts, Flutter RFP, Caesars).", "NY Repository", stack="D90")
s("P4", 13, "Business case lab: quantify the value", "Sales Skills", "Practice", 1, "Solutions Engineering + Deal Management", "Build",
  "Turn the Day 60 value hypothesis into numbers using the pricing model and cost-analysis examples.", "New", stack="D90")
s("P4", 13, "Deck peer review & dry run", "Sales Skills", "Practice", 1, "Buddy + pod", "Build",
  "", "New", stack="D90")
s("P4", 13, "★ Pitch Deck Certification", "Certification", "Certification", 1, "Panel: pod lead, SE, Enablement, guest leader", "Build",
  "See the certification rubric.", "New", stack="D90")
s("P4", 13, "Day 90 review & graduation to everboarding", "Tools & Process", "Practice", 0.5, "Line manager + Enablement", "Build",
  "Ramp review against quota trajectory, certifications logged, and an individual development plan for Days 91–180.", "New", stack="D90")

# ---------- P5 Everboard ----------
s("P5", 14, "Monthly sales skills session", "Sales Skills", "Live", 1, "Enablement", "Ready")
s("P5", 14, "'How We Did It' at the sales all-hands", "Sales Skills", "Live", 0.5, "Octavio Balcazar / Olivia Smith", "Ready")
s("P5", 14, "Call recording clinic, every two months", "Sales Skills", "Practice", 0.75, "Jim Cho + Francesco Falcone", "Ready")
s("P5", 14, "Yearly recertification: Explore & Pitch", "Certification", "Certification", 1, "Enablement", "Build",
  "Keeps the bar consistent for tenured AEs (charter pillar 1: recertification rate).", "New")

SESSIONS = S

# Learning objectives for the stacked moments
STACKS = {
    "D60": {
        "title": "Day 60 stack: Explore Week",
        "days": "Days 56–60 · Week 9",
        "why": "By Day 60 an AE has the product fluency, verticals and first conversations to make discovery stick. Stacking everything about Explore into one week, right before the certification, helps the skill stick and avoids spreading it thin across two months.",
        "objectives": [
            "Open an Explore call with an agenda and an upfront contract that the buyer agrees to",
            "Run a DEPTH questioning funnel that uncovers payments pain: auth rates, fraud and disputes, cost, APM coverage, payouts",
            "Quantify at least one pain point in the merchant's own numbers",
            "Map the pains you hear to the right Checkout pillar, without pitching too early",
            "Summarise, confirm and secure a committed next step with a date",
        ],
    },
    "D90": {
        "title": "Day 90 stack: Propose Week",
        "days": "Days 86–90 · Week 13",
        "why": "Propose builds on pricing, deal structure and payments economics. Those land in Weeks 10–12, so the AE comes into Week 13 ready to build and defend a real deck. The certification doubles as graduation from onboarding.",
        "objectives": [
            "Build a deck storyline for a real territory account: insight → value → proof → plan",
            "Present a business case grounded in the merchant's data, with pricing positioned in line with guidance",
            "Use proof points (case studies, NPS, references) for the right vertical",
            "Handle competitive and pricing objections with the defense playbook",
            "Close the presentation with a mutual action plan",
        ],
    },
    "D30": {
        "title": "Day 30 checkpoint",
        "days": "Day 30 · Week 4",
        "why": "A short gate that confirms the foundations before practice starts.",
        "objectives": [
            "Deliver a 60-second Checkout elevator pitch tailored to one NORAM vertical",
            "Explain the value of each of the five pillars in a merchant's language",
        ],
    },
}

CERTS = [
    {
        "name": "Explore Call Certification",
        "when": "Day 60 (Week 9)",
        "format": "A 30-minute live, simulated Explore call. The assessor plays a scripted payments persona (e.g. Head of Payments at a mid-market subscription merchant). Recorded in Clari.",
        "assessors": "Pod lead + Enablement (calibrated on the same rubric)",
        "pass": "≥ 80% overall (28/35) and no section below 3/5. One retake within 10 working days, with coaching.",
        "rubric": [
            ("Pre-call research & hypothesis", "Knows the merchant's model, footprint, likely PSP set-up and a starting hypothesis"),
            ("Opening & upfront contract", "Clear agenda, time check and agreed outcome for the call"),
            ("DEPTH questioning funnel", "Moves from broad to specific, with open questions and no early pitching"),
            ("Payments pain quantified", "Uncovers and sizes at least one pain: auth rate, fraud, cost, APMs or payouts"),
            ("Pillar mapping", "Links the pains to the right Checkout pillar and capability"),
            ("Listening & summarising", "Listens far more than talks, and plays the summary back accurately"),
            ("Committed next step", "A dated next step with the right stakeholders"),
        ],
    },
    {
        "name": "Pitch Deck Certification",
        "when": "Day 90 (Week 13)",
        "format": "A tailored deck for a real territory account: a 20-minute presentation plus 10 minutes of panel Q&A, with the panel playing the buying committee.",
        "assessors": "Pod lead, Solutions Engineer, Enablement, plus a guest leader",
        "pass": "≥ 80% overall (32/40) and no section below 3/5. Exemplary decks go into the Great Decks library.",
        "rubric": [
            ("Merchant insight", "Opens with the merchant's world and priorities, not ours"),
            ("Value narrative", "Story connects their goals to Checkout pillars with clear outcomes"),
            ("Business case", "Quantified value (auth uplift, cost, fraud, ops) using their data"),
            ("Proof", "Relevant case studies, references or NPS evidence for the vertical"),
            ("Competitive differentiation", "Positions against the incumbent without disparaging them"),
            ("Pricing narrative", "Commercials framed within guidance, linked to value"),
            ("Mutual action plan", "Clear path to signature, integration and go-live"),
            ("Executive presence & Q&A", "Confident, concise, handles objections calmly"),
        ],
    },
]

# What changes vs. today (before/after)
CHANGES = [
    ("Payments Academy starts on Day 2, with about 5 hours in Week 1",
     "A 60-minute payments story on Day 1–5, then Payments Academy paced from Week 2 with live debriefs"),
    ("Generic 'pillar sales perspective' sessions",
     "30-minute 'pillars in live deals' walk-throughs built on vertical use cases"),
    ("Call reviews begin in Week 1",
     "A weekly call-review hour from Week 3, once there's context to learn from"),
    ("No formal skill gates after the elevator pitch",
     "Three gates: the Day 30 Checkpoint, Explore Certification at Day 60 and Pitch Deck Certification at Day 90"),
    ("Topics spread evenly across Months 2–3",
     "Learning stacked into an Explore Week (Day 60) and a Propose Week (Day 90), each with focused objectives"),
    ("Pricing, payments economics and negotiation sessions not scheduled",
     "Sequenced in Weeks 10–11, so they land just before the Propose stack that uses them"),
    ("A separate plan, repository and tracker per cohort",
     "One programme map, one session inventory and one personal tracker per AE"),
]

METRICS = [
    ("Time to first meeting booked", "≤ Day 30"),
    ("Time to first qualified opportunity", "≤ Day 60"),
    ("Explore certification first-time pass rate", "≥ 80%"),
    ("Pitch deck certification first-time pass rate", "≥ 80%"),
    ("Ramp attainment vs. cohort trajectory at Day 90", "On or ahead of plan"),
    ("New-hire onboarding NPS (Day 30 / 90 pulse)", "≥ +50"),
]
