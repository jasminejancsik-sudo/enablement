"""Single source of truth for the NORAM Account Executive onboarding programme (v2).

Both deliverables are generated from this file:
  python3 onboarding/ae/build/build.py
    -> onboarding/ae/ae-onboarding-program.html   (leadership view)
    -> onboarding/ae/ae-onboarding-tracker.xlsx   (working tracker)

Timeline rules (agreed 1 Oct 2026):
  * Days are WORKING days. Week N, weekday D -> working day (N-1)*5 + D.
  * Day 30 = end of Week 6, Day 60 = end of Week 12, Day 90 = end of Week 18.
  * Cohorts start on the 1st and the 15th. Live sessions can run on a
    repeating 2-week cycle so the second cohort can join sessions already running.
"""

PROGRAM = {
    "title": "NORAM Account Executive Onboarding",
    "subtitle": "90 working days from Day 1 to a winning proposal, built for selling payments at Checkout.com",
    "owner": "Jasmine Jancsik, Lead Enablement, US",
    "version": "v2 draft, October 2026",
    "sources": [
        ("2025 Q4 USA New Hire Plan", "https://docs.google.com/spreadsheets/d/1Unozpi3AXkMcAO_rXoDNjW9CjWenfUTZv7BK6xwydi4/edit"),
        ("New York Sales Class: Onboarding Repository", "https://docs.google.com/spreadsheets/d/1cqKzHDs9KVDS616wynbUgFgrgOKayOayA8B7-XgqDqI/edit"),
        ("Karlie Chen: Onboarding Tracker (Q3 2026)", "https://docs.google.com/spreadsheets/d/1rb2HY82xgeAExbIBVEK1Wx7vHRnb4yQT_ddAv_rbqk4/edit"),
        ("Commercial Onboarding Sessions (global catalogue)", "https://docs.google.com/spreadsheets/d/1CG5SWjQS1IQTrWM3tjcbiglEulbibzpy6NINS-vebws/edit"),
    ],
}

STATUSES = ["Ready", "Refresh", "Build"]
STATUS_LABEL = {"Ready": "Ready today", "Refresh": "Needs refresh", "Build": "To build"}
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]

BLOCKS = [
    {"key": "B0", "name": "Before Day 1", "days": "Pre-board", "weeks": [0], "theme": "Arrive ready",
     "goal": "Tools, plan, tracker and buddy are in place, so Day 1 is about people, not passwords.", "selling": "0%"},
    {"key": "B1", "name": "Days 1–30", "days": "Weeks 1–6", "weeks": [1, 2, 3, 4, 5, 6], "theme": "Get certified",
     "goal": "Learn payments and the five pillars, master the Explore call and the first-meeting pitch, and certify on both by Day 30.", "selling": "≤20%"},
    {"key": "B2", "name": "Days 31–60", "days": "Weeks 7–12", "weeks": [7, 8, 9, 10, 11, 12], "theme": "Build pipeline",
     "goal": "Go deep on NORAM verticals and the deal machine while prospecting, then follow a real deal through every team in the Day 60 Follow the Flow workshop.", "selling": "50%"},
    {"key": "B3", "name": "Days 61–90", "days": "Weeks 13–18", "weeks": [13, 14, 15, 16, 17, 18], "theme": "Win deals",
     "goal": "Price, structure and negotiate, then present a full proposal for a live deal in the Day 90 Deal Room.", "selling": "70%"},
    {"key": "B4", "name": "After Day 90", "days": "Ongoing", "weeks": [19], "theme": "Keep growing",
     "goal": "Monthly skills sessions, call clinics and a yearly recertification.", "selling": "90%+"},
]

MILESTONES = [
    {"day": 25, "week": 5, "dow": "Fri", "name": "Explore Call Certification", "type": "cert",
     "what": "Live simulated Explore call against a standard payments persona", "pass": "≥ 80% and no section below 3/5"},
    {"day": 30, "week": 6, "dow": "Fri", "name": "Pitch Deck Certification", "type": "cert",
     "what": "First-meeting deck for a standard case, presented to a panel", "pass": "≥ 80% and no section below 3/5"},
    {"day": 60, "week": 12, "dow": "Wed", "name": "Follow the Flow", "type": "stack",
     "what": "Half-day workshop: one real deal through every partner team", "pass": "Coaching · leave with your deal's flow map"},
    {"day": 90, "week": 18, "dow": "Wed", "name": "Deal Room", "type": "stack",
     "what": "Present a full proposal for your top live deal, pricing included", "pass": "Coaching · graduates to everboarding"},
]

# ---------------------------------------------------------------------------
# Sessions
# s(week, day, title, objective, fmt, minutes, owner, status, note, cat_id, bdr, tag)
#   day   : Mon..Fri (or "" for pre-board / ongoing)
#   fmt   : Live | Self-paced | Practice | Certification
#   cat_id: ID in the global Commercial Onboarding Sessions catalogue ("" if NORAM-only)
#   bdr   : True if also relevant for BDR onboarding (to develop later)
#   tag   : "Explore cert" | "Pitch cert" | "Follow the Flow" | "Deal Room" | ""
# ---------------------------------------------------------------------------
S = []
def s(week, day, title, objective, fmt, minutes, owner, status, note="", cat_id="", bdr=False, tag=""):
    block = next(b["key"] for b in BLOCKS if week in b["weeks"])
    wd = (week - 1) * 5 + DAYS.index(day) + 1 if (day and 1 <= week <= 18) else None
    S.append(dict(block=block, week=week, day=day, wd=wd, title=title, objective=objective, fmt=fmt,
                  minutes=minutes, owner=owner, status=status, note=note, cat_id=str(cat_id), bdr=bdr, tag=tag))

TBD = "TBD with team lead"

# ---------- Before Day 1 ----------
s(0, "", "Welcome pack, 90-day map & personal tracker", "Arrive knowing the path, milestones and who to ask",
  "Self-paced", 30, "Enablement", "Build", "Send the personal tracker and programme map before Day 1.")
s(0, "", "Tool access requested (Salesforce, Clari, Apollo, LinkedIn Sales Nav, Glean)", "Log in to every sales tool on Day 1",
  "Self-paced", 0, "Enablement + IT", "Ready", "Automated message in the onboarding channel requests licences on Jira.", bdr=True)
s(0, "", "Buddy assigned + manager welcome call", "Know your manager's expectations and your day-to-day buddy",
  "Live", 30, "Line manager", "Refresh", "Formalise buddies with a one-page guide and a weekly 30-minute slot.")

# ---------- Days 1–30: Get certified ----------
# Week 1 · Arrive & orient
s(1, "Mon", "IT, People & Benefits inductions", "Have your laptop, accounts and benefits set up", "Live", 180, "People Team", "Ready", bdr=True)
s(1, "Mon", "Your onboarding plan: 90-day kickoff", "Explain your milestones, certifications and how you'll be supported", "Live", 30, "Enablement", "Ready", bdr=True)
s(1, "Mon", "Meet your pod + buddy coffee", "Know your pod, your buddy and how the team works", "Practice", 60, "Pod leader", "Ready", bdr=True)
s(1, "Tue", "Intro to Checkout's Revenue Organisation (NORAM)", "Describe how the revenue org is structured and the sales opportunity cycle", "Live", 60, "Jasmine Jancsik", "Ready", cat_id=4, bdr=True)
s(1, "Tue", "Regional Intro to Rev Org: NORAM", "Know the NORAM leaders, pods and hubs (NY, ATL, SF)", "Live", 30, "Jasmine Jancsik", "Ready", cat_id=13, bdr=True)
s(1, "Tue", "Payments at Checkout in 60 minutes", "Tell the story of a card payment, where Checkout earns, and why merchants switch", "Live", 60, "Enablement + Solutions Engineering", "Build",
  "Story-led primer that complements Payments Academy and gives context before the curriculum starts.", bdr=True)
s(1, "Wed", "Sales Tools & Chrome Extensions", "Log in and use Groove, Apollo, LinkedIn Sales Nav, SimilarWeb and Wappalyzer", "Live", 90, "Jasmine Jancsik", "Ready", cat_id=26, bdr=True)
s(1, "Wed", "Finding answers: Drive, Confluence & Glean", "Find any deck, case study or answer in under a minute", "Live", 30, "Enablement", "Refresh",
  "Update for the move away from Highspot to Drive, and for Glean adoption.", cat_id=8, bdr=True)
s(1, "Thu", "Mandatory compliance training (Spark)", "Complete all mandatory compliance modules", "Self-paced", 180, "New hire", "Refresh",
  "Moving from Nova to Spark.", bdr=True)
s(1, "Thu", "RevWay 0–1: Intro to Revenue Way & Buyer Psychology", "Explain how buyers make decisions and the Checkout Revenue Way", "Self-paced", 150, "Self-directed", "Ready", bdr=True)
s(1, "Fri", "Office hours with the NORAM GM", "Hear the NORAM vision and ask leadership anything", "Live", 30, "Zack Levine", "Ready", bdr=True)
s(1, "Fri", "Friday knowledge check (Kahoot), runs weekly", "Check what stuck this week, with pod leads", "Practice", 30, "Enablement + pod leads", "Ready", bdr=True)

# Week 2 · Payments & market
s(2, "Mon", "Payments Academy: Foundations 1–3", "Explain basic payment concepts, payment methods and the merchant value proposition", "Self-paced", 60, "Self-directed", "Refresh",
  "Paced across Week 2 instead of Day 2, with a Friday live debrief.", bdr=True)
s(2, "Mon", "Competitive Landscape (global + NORAM)", "Compare next-gen and legacy PSPs, and position against our three key competitors", "Live", 120, "Michel Tornabene", "Ready",
  "Need a refreshed NORAM deck.", cat_id="12, 17", bdr=True)
s(2, "Tue", "Intro to Top of Funnel Onboarding", "Know the Top of Funnel e-learning path and how to use it", "Live", 30, "J.J. Henry", "Ready", cat_id=31, bdr=True)
s(2, "Tue", "International Outlook: acquiring set-ups & cross-border", "Explain Checkout's three acquiring set-ups and regional payment methods", "Live", 45, "Enablement", "Ready", cat_id=39, bdr=True)
s(2, "Wed", "Payments Academy: Foundations 4–6", "Map the key players and the life cycle of a transaction", "Self-paced", 60, "Self-directed", "Refresh", bdr=True)
s(2, "Wed", "Buyer personas in payments", "Tailor your message to a Head of Payments, CFO, CPO or engineering lead", "Live", 60, "J.J. Henry", "Ready",
  "Uses the 2023 Buyer Persona deck; check if it needs a refresh.", bdr=True)
s(2, "Wed", "RevWay 2–3: DEPTH Selling & Managing Pipeline", "Use the DEPTH stages to qualify and manage your pipeline", "Self-paced", 150, "Self-directed", "Ready")
s(2, "Thu", "Territory planning (STP), Rules of Engagement & Incentive Ratings", "Know your territory, account tiers and how deals are credited", "Live", 60, "Francesco Falcone", "Ready",
  "Must be live and finished by the end of Week 2.", bdr=True)
s(2, "Thu", "Commercial Risk", "Explain MCC risk, the BMG tool and minimum acceptance criteria for higher-risk merchants", "Live", 30, "Enablement", "Ready", cat_id=30, bdr=True)
s(2, "Fri", "Payments Academy: Foundations 7–10 + live debrief", "Explain payments economics, regulation and risk in your own words", "Self-paced", 90, "Enablement", "Refresh",
  "The debrief turns the modules into talk tracks.", bdr=True)

# Week 3 · Product & the five pillars
s(3, "Mon", "Product Foundations: Connect & Move", "Explain the value of the Connect and Move pillars", "Self-paced", 120, "Self-directed", "Ready", bdr=True)
s(3, "Mon", "Pillars in live deals: Connect & Move", "See how Connect and Move win real NORAM deals", "Live", 60, "Pod leads", "Refresh",
  "Replace generic sales-perspective sessions with 30-minute live-deal walk-throughs built on a vertical use case.")
s(3, "Tue", "Salesforce, Clari & pipeline hygiene", "Create and update opportunities and forecast in Clari", "Live", 60, "Enablement", "Refresh",
  "Material still to be put together.", bdr=True)
s(3, "Tue", "Intro to Deal Management", "Know who Deal Management are, what they do and when to engage them", "Live", 30, "Faith Bergman", "Ready", cat_id=34)
s(3, "Wed", "Product Foundations: Protect, Boost & Manage", "Explain the value of the Protect, Boost and Manage pillars", "Self-paced", 150, "Self-directed", "Ready", bdr=True)
s(3, "Thu", "Pillars in live deals: Protect, Boost & Manage", "See how Protect, Boost and Manage win real NORAM deals", "Live", 60, "Pod leads", "Refresh")
s(3, "Thu", "Intro to Issuing (NORAM)", "Explain Checkout Issuing and when it fits a merchant", "Live", 30, TBD, "Build",
  "Exists for UK/EEA only today (catalogue #48). Build a NORAM version.", cat_id="48 (UK/EEA)")
s(3, "Fri", "Payment Performance AMA (Boost)", "Ask our payments performance lead how Boost lifts acceptance", "Live", 60, "Daniel Linder", "Ready")

# Week 4 · Explore
s(4, "Mon", "RevWay 4–5: Discovery & Explore phases", "Prepare and structure an Explore call", "Self-paced", 150, "Self-directed", "Ready", tag="Explore cert")
s(4, "Mon", "Discover (SAT style) (NORAM)", "Run discovery the way the Strategic Accounts Team does", "Live", 30, TBD, "Build",
  "Exists for UK/EEA only today (catalogue #41). Build a NORAM version.", cat_id="41 (UK/EEA)", tag="Explore cert")
s(4, "Tue", "Explore Call Masterclass", "Run an Explore call with an agenda, upfront contract and DEPTH funnel", "Live", 90, "Enablement + top AE", "Build", tag="Explore cert")
s(4, "Tue", "AI in Commercial", "Use Checkout's AI tools for research, prep and follow-up", "Live", 60, "Molly McKenna", "Ready", cat_id=50, bdr=True)
s(4, "Wed", "Payments discovery question bank & value hypothesis", "Ask the right questions for each persona and pillar, and form a value hypothesis", "Live", 60, "Enablement + Solutions Engineering", "Build", tag="Explore cert")
s(4, "Wed", "Intro to Commercial & Merchant Insights (NORAM)", "Use merchant data and insights to sharpen discovery", "Live", 30, TBD, "Build",
  "Exists for UK/EEA only today (catalogue #47). Build a NORAM version.", cat_id="47 (UK/EEA)")
s(4, "Thu", "Pause and Play: Explore call gametapes", "Spot what great discovery sounds like on real Clari calls", "Practice", 60, "Enablement", "Ready",
  "Runs weekly from Week 4; this week uses an Explore-only playlist.", tag="Explore cert")
s(4, "Fri", "Explore role-play sprint", "Practise three timed Explore calls against three personas, scored on the rubric", "Practice", 90, "Pod leads + buddy", "Ready", tag="Explore cert")

# Week 5 · Explore certification
s(5, "Mon", "Elevator pitch + five-pillar knowledge check", "Deliver a 60-second pitch and explain all five pillars", "Practice", 60, "Line manager + Enablement", "Refresh",
  "Practice step, not a gate. Combines today's pitch reviews and pillar Kahoots.")
s(5, "Mon", "Account list review: your Top 70", "Prioritise your accounts and know why each one is a fit", "Practice", 60, "Line manager", "Ready")
s(5, "Tue", "Outreach lab: openers, email personalisation & gatekeepers", "Write outreach that books meetings and get past gatekeepers", "Live", 120, "Jasmine Jancsik", "Ready", bdr=True)
s(5, "Wed", "Cold-call role play", "Open a cold call confidently and book a next step", "Practice", 30, "Jasmine Jancsik", "Ready", bdr=True)
s(5, "Thu", "Storyline workshop: the first-meeting pitch deck", "Build a first-meeting deck: insight → value → proof → next steps", "Live", 90, "Enablement + Product Marketing", "Build",
  "Uses the standard certification case and the Great Decks library.", tag="Pitch cert")
s(5, "Fri", "★ Explore Call Certification (Day 25)", "Pass a live Explore call against a standard payments persona", "Certification", 45, "Pod leads + Enablement", "Build",
  "Run as a batch certification day. Retake by Day 35, with supplemental materials.", tag="Explore cert")

# Week 6 · Pitch certification & strategy
s(6, "Mon", "RAC Plans: NORAM", "Build your RAC plan and know your path to target", "Live", 45, "Michel Tornabene", "Ready", cat_id=58)
s(6, "Mon", "Regional BPs & Commercial Strategy (NORAM)", "Explain the NORAM strategy, which accounts we go after and how BPs help", "Live", 45, "Eliza Chew", "Ready", cat_id=60, bdr=True)
s(6, "Tue", "Commercial OKRs", "Know the commercial OKRs and how your work ladders up", "Live", 45, "Nicole Molina", "Ready", cat_id=59, bdr=True)
s(6, "Tue", "Intro to Commercial Product Partnership", "Know how to bring Product into a deal", "Live", 30, "Nicolas Maalouf", "Ready", cat_id=62)
s(6, "Wed", "Deck dry run with buddy & pod", "Rehearse your pitch and tighten it with feedback", "Practice", 60, "Buddy + pod", "Build", tag="Pitch cert")
s(6, "Fri", "★ Pitch Deck Certification (Day 30)", "Present a first-meeting deck for the standard case to a panel", "Certification", 30, "Pod leads + Enablement", "Build",
  "Run as a batch certification day. Retake by Day 35, with supplemental materials.", tag="Pitch cert")
s(6, "Fri", "Day 30 review", "Agree certification results and your Days 31–60 plan with your manager", "Practice", 30, "Line manager", "Build")

# ---------- Days 31–60: Build pipeline ----------
s(7, "Mon", "Certification retakes + supplemental materials (as needed)", "Close any certification gaps by Day 35", "Practice", 60, "Enablement", "Build",
  "Only for AEs who need a retake. Everyone else keeps prospecting.")
s(7, "Mon", "Intro to NORAM verticals & where we win", "Name the NORAM verticals where Checkout wins, and why", "Live", 45, "Enablement", "Refresh",
  "Pair this with the North America Vertical List.", bdr=True)
s(7, "Tue", "Vertical deep dives: Digital Content and Ecommerce", "Prospect and qualify subscription, digital and ecommerce merchants", "Live", 90, "Jules Gay / Katie Wile", "Ready", bdr=True)
s(7, "Thu", "Vertical deep dives: Neobank & Remittance, Consumer Lending & Proptech", "Prospect and qualify fintech merchants (AFT/OCT use cases)", "Live", 90, "Olivia Smith / Octavio Balcazar", "Ready", bdr=True)
s(7, "Fri", "Build your prospecting cadence (Apollo)", "Launch a multi-touch cadence for your Top 70", "Practice", 30, "Ronak Bali", "Ready", bdr=True)

s(8, "Mon", "Underwriting Overview NORAM", "Know what underwriting needs and how to avoid delays", "Live", 60, "Jack Pontarelli", "Ready", cat_id=52)
s(8, "Tue", "Intro to Pricing (NORAM)", "Explain how Checkout prices and who approves it", "Live", 30, TBD, "Build",
  "Exists for UK/EEA only today (catalogue #46). Build a NORAM version.", cat_id="46 (UK/EEA)")
s(8, "Wed", "Partner ecosystem: who we sell with and how", "Spot partner opportunities (orchestration, ERP, fraud, platforms)", "Live", 60, "Jim Cho / Francesco Falcone / Jaime Yeager", "Ready")
s(8, "Wed", "ISV, Marketplace & MoR deep dive", "Qualify platform and marketplace deals", "Live", 30, "Michael Taylor", "Ready")
s(8, "Thu", "Payment performance metrics that matter", "Quantify auth rates, declines, tokens and cost in a merchant's numbers", "Live", 60, "Solutions Engineering + Product", "Build",
  "Builds on the Decline Code and PPA cheat sheets.")

s(9, "Mon", "Pay to Card, Pay to Bank & FX", "Position payouts and FX with real use cases", "Live", 60, "Olivia Smith", "Ready")
s(9, "Tue", "Visa Direct: AFTs & card payouts", "Explain AFTs and card payouts with Visa Direct", "Live", 30, "Sydney", "Refresh",
  "Paused while partnership terms are revamped.")
s(9, "Wed", "Technical integration & merchant onboarding experience", "Explain integration timelines, sandbox and go-live", "Live", 30, "Michael Taylor + Faith Bergman", "Ready")
s(9, "Thu", "RevWay 6–7: Questioning, funnel technique & listening", "Deepen discovery with funnelling, listening and summarising", "Self-paced", 180, "Self-directed", "Ready")
s(9, "Fri", "Canada & the Canadian market", "Prospect Canadian merchants with the right context", "Live", 30, "Yousef Almawy", "Ready")

s(10, "Tue", "Voice of the customer: Head of Payments panel", "Hear from Heads of Payments what resonates and what doesn't", "Live", 90, "Jaime Yeager / Jim Cho", "Build",
  "Planned before but never scheduled.")
s(10, "Wed", "Top-rep Q&A, every two weeks", "Learn habits from top reps (Sam B, Louis Taupin)", "Live", 30, "Sam Boukhiam / Louis Taupin", "Build",
  "Planned before but never started.", bdr=True)
s(10, "Thu", "Vertical deep dives: Insurance and Gaming & Gambling", "Qualify insurance and gaming merchants", "Live", 60, "Olivia Smith / Aaron Popack", "Refresh",
  "On hold. Run Insurance virtually first.")
s(10, "Fri", "Competitive deal clinic + refreshed battlecards", "Win head-to-head against the incumbent", "Live", 60, "Jim Cho", "Refresh",
  "'Why Checkout Wins' battlecard is outdated; release refreshed cards with this session.", bdr=True)

s(11, "Mon", "Regional Deal Management Best Practice: NORAM", "Handle DSRs, Ironclad, NDAs and MAFs without delays", "Live", 60, "Faith Bergman", "Ready", cat_id=68)
s(11, "Wed", "Role play with your pod lead", "Practise a live deal scenario and get coaching", "Practice", 30, "Pod leads", "Ready")
s(11, "Thu", "Working with Marketing & the Strategic Accounts Team", "Bring Marketing and SAT into your deals", "Live", 60, "Marketing + Cyril Chemla", "Ready")

# Day 60 stack: Follow the Flow (Week 12)
FLOW_NOTE = "Station in the Follow the Flow workshop. Also covers the NORAM gap intro for this team (UK/EEA-only in the catalogue)."
s(12, "Wed", "Follow the Flow · Authorise: Deal Desk", "Get your deal's structure and pricing approved", "Practice", 30, "Faith Bergman", "Build", "Station in the Follow the Flow workshop.", tag="Follow the Flow")
s(12, "Wed", "Follow the Flow · Risk check: Underwriting", "Prepare a submittal that gets approved fast", "Practice", 30, "Underwriting", "Build", "Station in the Follow the Flow workshop.", tag="Follow the Flow")
s(12, "Wed", "Follow the Flow · Tokenise & integrate: Solutions Engineering", "Scope the integration for your prospect", "Practice", 30, TBD, "Build", FLOW_NOTE, cat_id="45 (UK/EEA)", tag="Follow the Flow")
s(12, "Wed", "Follow the Flow · Route: Partnerships + Financial Partnerships", "Find the partner angle in your deal", "Practice", 30, TBD, "Build", FLOW_NOTE, cat_id="43 (UK/EEA)", tag="Follow the Flow")
s(12, "Wed", "Follow the Flow · Settle: Account Management", "Plan a clean handover from signature to go-live", "Practice", 30, TBD, "Build", FLOW_NOTE, cat_id="44 (UK/EEA)", tag="Follow the Flow")
s(12, "Wed", "Follow the Flow · Reconcile: RevOps & BDR", "Tidy your pipeline and plan with your BDR", "Practice", 30, "Sandra Suen", "Build", "Station in the Follow the Flow workshop.", tag="Follow the Flow")
s(12, "Fri", "Day 60 review", "Review pipeline, activity and ramp, and agree your Days 61–90 plan", "Practice", 30, "Line manager", "Build")

# ---------- Days 61–90: Win deals ----------
s(13, "Mon", "Propose Masterclass", "Structure a proposal that moves a deal forward", "Live", 90, "Enablement", "Ready")
s(13, "Tue", "Pricing guidance & take rate", "Price within guidance and explain take rate", "Live", 60, "Jim Cho + Francesco Falcone", "Build",
  "Listed before but never scheduled.")
s(13, "Thu", "RevWay 8–9: Propose & Presentation Skills", "Present a proposal with confidence", "Self-paced", 210, "Self-directed", "Ready")

s(14, "Mon", "Pricing calculator walk-through (real deal)", "Build a pricing model with the calculator", "Live", 60, "Jim Cho", "Ready")
s(14, "Tue", "AFT/OCT pricing calculator walk-through", "Price an AFT/OCT deal", "Live", 30, "Vladimir Sterenko", "Ready")
s(14, "Thu", "Payments economics: interchange++, fee & cost analysis", "Build a cost comparison against a merchant's current provider", "Live", 90, "Deal Management + Solutions Engineering", "Build",
  "Examples exist (Gopuff and Rhino + Jetty cost analyses, L2/L3) but there's no session.")

s(15, "Mon", "Trade, deal structure & negotiation case studies", "Negotiate terms, get pricing approved and set minimum billing", "Live", 60, "Pod lead (TBD)", "Build")
s(15, "Wed", "Underwriting from the UW lens + MAF & questionnaires", "Complete MAFs and questionnaires right the first time", "Live", 60, "Jarett Israel + Rithvik Nair", "Ready")
s(15, "Thu", "Objection handling drill + RevWay 10", "Handle pricing and competitive objections live", "Practice", 90, "Enablement", "Refresh",
  "Self-paced only today; add a live drill using the competitive defense playbook.")

s(16, "Mon", "How to ramp a merchant: what happens after 'yes'", "Get a new merchant live and processing", "Live", 30, "Nicholas Schaffer", "Ready")
s(16, "Tue", "QBR walk-through", "Run a strong QBR with an existing merchant", "Live", 30, "Perrin Heyka", "Ready")
s(16, "Thu", "MBO, quota mechanics & your path to quota", "Explain quota retirement, consumption and your path to target", "Live", 60, "Francesco Falcone + Jim Cho", "Refresh",
  "Reschedule to 60 minutes with Jim, and invite newer hires.")

s(17, "Tue", "Business case lab: quantify the value", "Turn your value hypothesis into a business case", "Practice", 60, "Solutions Engineering + Deal Management", "Build", tag="Deal Room")
s(17, "Thu", "Proposal dry run with buddy", "Rehearse your Deal Room proposal", "Practice", 45, "Buddy", "Build", tag="Deal Room")

# Day 90 stack: Deal Room (Week 18)
s(18, "Wed", "Deal Room: present your top live deal", "Present a full proposal, pricing included, and get coaching from your manager and Deal Desk", "Practice", 60, "Line manager + Deal Desk", "Build",
  "Coaching, not scored; certifications are done by Day 30.", tag="Deal Room")
s(18, "Fri", "Day 90 review & graduation", "Review ramp against quota trajectory and set a Days 91–180 development plan", "Practice", 30, "Line manager + Enablement", "Build", tag="Deal Room")

# ---------- After Day 90 ----------
s(19, "", "Monthly sales skills session", "Keep sharpening one skill a month", "Live", 60, "Enablement", "Ready")
s(19, "", "'How We Did It' at the sales all-hands", "Learn from recent wins", "Live", 30, "Octavio Balcazar / Olivia Smith", "Ready")
s(19, "", "Call recording clinic, every two months", "Review calls as a team", "Practice", 45, "Jim Cho + Francesco Falcone", "Ready")
s(19, "", "Yearly recertification: Explore & Pitch", "Keep the bar consistent for tenured AEs", "Certification", 60, "Enablement", "Build")

SESSIONS = S

STACKS = {
    "Follow the Flow": {
        "title": "Follow the Flow",
        "when": "Day 60 · Week 12 · Wednesday (half day)",
        "why": "By Day 60 the AE has live deals and real questions. Their deal moves through every partner team the way a payment moves through the payment chain, so team intros happen when they're useful, not on Day 5.",
        "objectives": [
            "Know who to bring into a deal, when, and what each team needs from you",
            "Get structure and pricing approved without back-and-forth",
            "Prepare an underwriting submittal that gets approved fast",
            "Scope the integration and find the partner angle in your deal",
            "Leave with a one-page flow map for your deal, with a named contact at every step",
        ],
    },
    "Deal Room": {
        "title": "Deal Room",
        "when": "Day 90 · Week 18 · Wednesday",
        "why": "Pricing, payments economics and negotiation land in Weeks 13–16. The AE then brings their top live deal and presents the full proposal. It's coaching, not a certification, and it's the graduation from onboarding.",
        "objectives": [
            "Present a full proposal for a live deal, pricing included",
            "Back the value with a business case built on the merchant's data",
            "Handle pricing and competitive objections",
            "Agree a mutual action plan to signature and go-live",
        ],
    },
}

CERTS = [
    {
        "name": "Explore Call Certification",
        "when": "Day 25 · Week 5 · Friday",
        "format": "A 30-minute live, simulated Explore call. The assessor plays a standard scripted persona: the Head of Payments at a mid-market US subscription merchant. Recorded in Clari.",
        "assessors": "Pod leads + Enablement, calibrated on the same rubric. Run as one batch day per cohort.",
        "pass": "≥ 80% overall (28/35) and no section below 3/5. Retake by Day 35, with supplemental materials from Enablement.",
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
        "when": "Day 30 · Week 6 · Friday",
        "format": "A first-meeting deck for the same standard case everyone gets: a fictional mid-market US subscription merchant on a legacy PSP, with involuntary churn and plans to expand into Canada. 15-minute presentation plus 10 minutes of panel Q&A. No pricing at this stage.",
        "assessors": "Pod leads + Enablement, as a batch day per cohort",
        "pass": "≥ 80% overall (28/35) and no section below 3/5. Retake by Day 35, with supplemental materials.",
        "rubric": [
            ("Merchant insight", "Opens with the merchant's world and priorities, not ours"),
            ("Value narrative", "Connects their goals to the right Checkout pillars"),
            ("Relevant proof", "Uses case studies or references for the vertical"),
            ("Competitive positioning", "Positions against a legacy PSP without disparaging it"),
            ("Clear ask & next steps", "Ends with a specific next meeting and the stakeholders to bring"),
            ("Deck craft", "Clean, concise, on-brand, using the Great Decks standards"),
            ("Presence & Q&A", "Confident, concise, handles questions calmly"),
        ],
    },
]

CHANGES = [
    ("Payments Academy on Day 2, with about 5 hours in Week 1",
     "A 60-minute payments story in Week 1, then Payments Academy paced through Week 2 with a live debrief"),
    ("Certifications spread out to Day 60 and Day 90",
     "Both certifications done by Day 30: Explore on Day 25 and the first-meeting pitch on Day 30, in batch days for each cohort"),
    ("Six team intros in Week 2, before AEs have context",
     "Follow the Flow at Day 60: a real deal goes through every partner team, framed as a payment flow"),
    ("Sessions placed by calendar day and spread unevenly",
     "Working days in a Week + weekday format, so both cohorts (starting on the 1st and the 15th) follow the same map"),
    ("Seven intros run for UK/EEA but not NORAM",
     "NORAM versions of Pricing, Issuing, Merchant Insights and SAT Discover; Solutions Engineering, Account Management and Partnerships are covered in Follow the Flow"),
    ("Pricing, payments economics and negotiation never scheduled",
     "Sequenced in Weeks 13–16, right before the Day 90 Deal Room that uses them"),
]

METRICS = [
    ("Explore certification first-time pass rate", "≥ 80%"),
    ("Pitch Deck certification first-time pass rate", "≥ 80%"),
    ("Time to first meeting booked", "≤ Day 30"),
    ("Time to first qualified opportunity", "≤ Day 60"),
    ("Ramp vs. cohort trajectory at Day 90", "On or ahead of plan"),
    ("New-hire onboarding NPS (Day 30 / 90 pulse)", "≥ +50"),
]
