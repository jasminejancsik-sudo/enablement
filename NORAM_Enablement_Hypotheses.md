# NORAM Enablement Hypotheses & Priorities
*Checkout.com · Revenue Enablement · Draft v1 · Source: NORAM pipeline velocity review, Eliza / Jasmine, 30 Sep 2026 (Gemini notes + transcript)*

> **Caveat:** Everything here comes from one walkthrough of the NORAM pipeline dashboards and the commercial time study, presented by Fonda (NYC). Treat each item as a hypothesis to test with reps, managers and Salesforce data before we commit to building anything.

---

## 1. What the data is telling us

| # | Signal | Evidence from the review | Funnel stage |
|---|---|---|---|
| S1 | **Explore is a parking lot** | On average 265 days from Explore to Propose. Explore losses are mostly "delayed project / change in priorities". Reps keep opps open "in hope of an RFP". | Explore |
| S2 | **Activity metrics get gamed** | Ramping reps and BDRs are measured on Explore meetings booked (Silver/Gold only), which leads to superficial meetings, favours called in and people added to meetings for credit. | Discover → Explore |
| S3 | **Deals die late at underwriting** | Handover losses are going up. Reps spend 12–18 months on a deal and then underwriting kills it: restricted vertical, missing licences, or it fails MAC. Our ICP is concentrated in high-risk verticals, and there are two sponsor banks (CRB and Pathway) with different criteria. | Handover |
| S4 | **Qualification is inconsistent** | An audit found top performers (e.g. Olivia) apply real qualification criteria while others push deals forward optimistically to hit KPIs. The result is bloated pipeline and poor forecast accuracy. | Explore → Propose |
| S5 | **Gold deals stall** | Gold opps (companies with $1B+ revenue) average about 900 days to close, 2–3x the normal ~18 months. Reps hold them with no active buying window. | All |
| S6 | **Pipeline hygiene isn't enforced** | There are no clear rules of engagement or exit criteria. Reps get past the 90-day touchpoint rule with superficial outreach. Pod leaders don't enforce, partly because rolling-12-month comp rewards big pipelines (e.g. Revolve). | All |
| S7 | **Only 35% of seller time is selling** | 45% goes on admin and internal meetings (system admin ~10%, approvals, escalations, pipeline reviews). Reps reconcile Looker against Salesforce by hand, Clari is being cut, and documentation is scattered across Highspot and Confluence, which overwhelms ramping reps. | Productivity |
| S8 | **Top-of-funnel stops at months 13–14** | Quota ramps 0% → 25% (month 13) → 50% (month 14) → 100%. Once reps start closing, they stop prospecting. Nick and Olivia keep fixed weekly and monthly outbound targets. | Ramp |
| S9 | **Winners pick niches** | Top reps target overlooked, low-risk niche verticals with complex fund flows: remittance (Olivia), rent payments (Nick), large Gold deals (Octavia, Whoop, 1,000% attainment). They avoid crowded retail. | Strategy |
| S10 | **Handoffs break after close** | Underwriting is manual (about 100 email threads, checklists) and the Merchant Risk Committee meets only monthly. SE and sandbox delays stall deals after handover. The Sales → AM handoff is undefined because AMs are at capacity, and ENR tiers 4–5 are unmanaged. | Post-handover |

**NORAM OKRs these signals affect:** front-book NR YTD, 50% YoY back-book NR growth, and **15 Gold go-lives / 50 total go-lives** (a Gold go-live is ≥ $100K TPV in a single month).

---

## 2. Hypotheses

Each hypothesis uses the format *If we… then… because…* and comes with a leading and a lagging metric so we can prove or disprove it.

### H1. Upfront risk qualification (MAC screening)
**If** reps screen every opportunity against MAC and sponsor-bank criteria (using the Glean risk agent) before it leaves Discover/Explore, **then** handover losses will fall and time-to-revenue will shorten, **because** most late losses are risks we could have known about early (vertical, licences, fund flow).
- *Build:* a short "risk-first qualification" module covering the CRB vs Pathway basics, restricted verticals and red flags. A required Glean agent check, with the output attached to the opp. A cheat sheet of "questions to ask in the first call". Manager inspection of the check in deal reviews.
- *Leading metric:* % of opps with the MAC check logged before Explore exit.
- *Lagging metrics:* handover loss rate, days from submission to underwriting decision, and number of opps sent to the Merchant Risk Committee.
- *Charter pillar:* 2 (Sell the Checkout Way) and 4 (Glean adoption).

### H2. Explore exit criteria and a qualification standard
**If** we define and certify clear Explore exit criteria (a real buying window, a compelling event, MAC-cleared, a named champion) and add a legitimate "nurture / not now" path, **then** Explore aging and the 265-day Explore → Propose cycle will fall and forecast accuracy will improve, **because** reps currently have no agreed bar and no legitimate place to park deals that are good fits but not active.
- *Build:* DEPTH Explore-stage reinforcement based on Olivia's qualification approach, deal-review role-plays, and a Salesforce stage checklist (with Ops).
- *Leading metrics:* % of Explore opps meeting exit criteria, and opps in Explore for more than 90 days.
- *Lagging metrics:* Explore → Propose conversion and days, and forecast accuracy.
- *Charter pillar:* 2 (current priority #2).

### H3. Codified top-performer playbooks
**If** we capture how Nick, Olivia and Octavia pick verticals, qualify and prospect, and teach it as vertical plays, **then** the middle of the team will build higher-quality pipeline faster, **because** the difference in results comes from repeatable choices (niche, complex fund flows, low risk, steady outbound), not from talent alone.
- *Build:* structured interviews (already a next step), 2–3 vertical play cards (remittance, rent, plus one fintech/FS), and a Gold-account approach from Octavia.
- *Leading metric:* adoption of the plays (opps tagged by play).
- *Lagging metrics:* win rate and cycle time for play-tagged vs other opps, and NR per rep.
- *Charter pillars:* 2 and 3. **This also feeds H1, H2 and H4, so do it first.**

### H4. A quality-based ramp pathway with sustained prospecting
**If** the ramp pathway measures quality milestones (MAC-screened, exit-criteria-met Explores; first Propose) rather than raw Explore counts, and builds a non-negotiable prospecting rhythm that carries past months 13–14, **then** new AEs will ramp to real pipeline and avoid the cliff after ramp, **because** today's activity metrics reward superficial Explores and prospecting drops away once closing starts.
- *Build:* 30/60/90 plus month 6/9/12 milestones for AEs and BDRs, a weekly prospecting cadence taken from Nick and Olivia, and one curated "start here" path instead of the Highspot/Confluence sprawl.
- *Leading metrics:* ramp milestone completion and weekly outbound activity in months 12–18.
- *Lagging metrics:* time to first Propose and first go-live, and attainment in months 13–18.
- *Charter pillar:* 1 (current priority #1). Changing the *comp* metric is outside our scope; see §4.

### H5. Recognition that rewards quality over volume
**If** all-hands leaderboards and shout-outs celebrate early disqualifications, pipeline clean-ups, MAC-cleared submissions and go-lives alongside activity, **then** reps will see those behaviours as valued, **because** what gets celebrated in public signals what really matters, beyond comp.
- *Build:* redesign the leaderboard with Fonda for the upcoming all-hands, and add a "clean pipeline" or "smart DQ of the month" recognition.
- *Leading metrics:* DQ rate at Discover/Explore, and pipeline removed in clean-ups.
- *Lagging metric:* pipeline quality ratio (go-lives ÷ Explores).
- *Charter pillars:* 2 and 4 (communications). **Quick win.**

### H6. Manager pipeline-inspection rhythm
**If** pod leaders run a standard pipeline inspection (exit criteria, 90-day touch quality, aging) in their 1:1s and deal reviews, **then** hygiene will improve and pipeline inflation will drop, **because** without an agreed standard, managers focused on near-term closes default to looking the other way.
- *Build:* a manager inspection toolkit, question bank and dashboard views, plus a coaching cadence. Include this in the new pod-leader transition for Olivia and Octavia next year.
- *Leading metric:* inspections completed.
- *Lagging metrics:* Explore aging, stale opps and forecast accuracy by pod.
- *Charter pillar:* 2 (manager coaching). Depends heavily on leadership backing and the comp design.

### H7. Seller time back through foundations and AI
**If** we give reps one source of truth for "how we sell in NORAM" (Drive plus Glean) and AI workflows for admin (CRM updates, call notes after Clari is cut, underwriting submission packs), **then** selling time will rise from 35%, **because** a large share of the 45% admin time is spent searching, reconciling and re-keying information.
- *Build:* a NORAM process hub, Glean prompts and agents for common admin, a rep-facing guide on which data source to trust (Looker vs Salesforce, with Ops), and commercial AI training.
- *Leading metrics:* Glean and AI usage, and search success.
- *Lagging metric:* the time-study rerun (% active selling).
- *Charter pillar:* 4 (current priorities #3 and #4).

### H8. Deal-readiness standards at every handoff
**If** reps submit a complete, standard "deal-readiness pack" to underwriting and to SE, and follow a defined Sales → AM handoff, **then** back-and-forth and the delays after handover will shrink, **because** incomplete submissions make underwriting act as a manual sanity checker.
- *Build:* a submission checklist and template (co-owned with Underwriting and Deal Management), SE engagement guidance, and a handoff playbook with AM.
- *Leading metric:* % of submissions complete first time.
- *Lagging metrics:* days from handover to go-live, and the number of email threads per deal.
- *Charter pillar:* 2. Process ownership sits with partners; we enable adoption.

### H9. Gold account strategy
**If** reps working Gold accounts use an account-planning and buying-window approach (compelling-event mapping, multithreading, a nurture status instead of an open opp), **then** Gold cycle time will fall and the Gold go-live target will be easier to forecast, **because** today's ~900-day cycle is inflated by accounts held open with no active buying window.
- *Build:* a Gold account-planning template, taught with Octavia's approach.
- *Metrics:* Gold cycle time, Gold go-lives against the target of 15, and Gold opps without a compelling event.
- *Charter pillar:* 2. **Validate first:** how much of the 900 days is a real long cycle, and how much is hoarding?

---

## 3. Prioritisation

Each hypothesis is scored 1–5 on three dimensions:
- **Impact:** effect on the OKRs (NR, Gold go-lives).
- **Confidence:** strength of the evidence.
- **Ease:** effort and time needed.

**Control** is how much of the fix sits inside enablement's remit.

| Rank | Hypothesis | Impact | Confidence | Ease | Score | Control | Tier |
|---|---|---|---|---|---|---|---|
| 1 | **H1** Upfront risk / MAC qualification | 5 | 4 | 4 | **13** | High (agent exists) | **Now** |
| 2 | **H3** Top-performer playbooks | 4 | 3 | 5 | **12** | High | **Now** (enabler) |
| 3 | **H2** Explore exit criteria | 5 | 4 | 3 | **12** | Medium (needs Ops for Salesforce) | **Now** |
| 4 | **H5** Quality-based recognition | 3 | 3 | 5 | **11** | Medium (with Fonda) | **Now** (quick win) |
| 5 | **H4** Quality ramp pathway | 4 | 4 | 2 | **10** | Medium | **Next** |
| 6 | **H7** Foundations and AI for seller time | 3 | 4 | 3 | **10** | High | **Next** |
| 7 | **H6** Manager inspection rhythm | 4 | 4 | 2 | **10** | Low (needs leadership and comp) | **Next** |
| 8 | **H8** Handoff readiness | 4 | 3 | 2 | **9** | Low (process owned by partners) | **Later** / partner-led |
| 9 | **H9** Gold account strategy | 4 | 2 | 2 | **8** | Medium | **Later** (validate first) |

**Why this order:** H1 and H2 address the two largest measurable leaks (late underwriting kills and the 265-day Explore stage) and connect directly to the go-live OKR. H3 is cheap and supplies the content for H1, H2 and H4. H5 is a visible early win that uses a moment already planned. H4 and H6 matter a lot but take longer and depend on incentive changes, so they're better positioned for the FY27 Kick Off.

### Suggested sequencing
- **Next 30 days:**
  - Run the top-performer interviews (H3).
  - Pilot the Glean MAC check with one pod (H1).
  - Co-design the all-hands leaderboard with Fonda (H5).
  - Validate S1–S4 with 5–6 rep calls and a Salesforce aging pull.
- **60–90 days:**
  - Roll out risk-first qualification and Explore exit criteria across all four pods (H1, H2).
  - Draft the NORAM sales framework with Fonda.
  - Launch the process hub (H7).
- **FY27 Kick Off / Q1 2027:**
  - Launch the quality ramp pathway (H4).
  - Launch the manager inspection toolkit, built into the new pod-leader roles (H6).
  - Run the handoff playbooks with partners (H8).
  - Run the Gold account planning (H9).

---

## 4. Out of enablement scope: raise with NORAM leadership
Enablement can reinforce behaviour, but these root causes sit in comp, ops or capacity. Training alone won't fix them.
1. **Ramp and BDR incentives** reward Explore *volume*. Consider quality gates, e.g. credit only for MAC-screened Explores or Explores that progress.
2. **Pod-leader rolling-12 comp** rewards large pipelines and works against hygiene enforcement.
3. **Rules of engagement, account ownership and exit criteria** need to be set in policy and Salesforce (Sales Ops).
4. **Merchant Risk Committee cadence** (monthly) and **manual underwriting workflow**.
5. **AM capacity** and coverage of ENR tiers 4–5. **SE / sandbox capacity.**
6. **Looker vs Salesforce data conflicts** and the replacement for Clari.

---

## 5. Validation plan and open questions
- **Data pull (Sales Ops):**
  - Explore aging distribution by pod and rep.
  - Handover loss reasons over time.
  - Gold cycle time with vs without an active RFP.
  - Explore → Propose conversion for ramping vs tenured reps.
- **Rep interviews:**
  - Top performers: Nick, Olivia, Octavia.
  - Two or three mid-performers and two ramping AEs (e.g. Dominic), to test whether the gaps are *skill*, *will* or *system* gaps.
- **Underwriting (Antoine) and the Merchant Risk Committee:**
  - Top five reasons deals are killed.
  - What "a complete submission" looks like.
  - Whether the Glean agent's output is trusted.
- **Open questions:**
  - Has the Glean agent been tested against past killed deals?
  - Who owns the Salesforce stage-criteria changes?
  - Is Jim open to changing ramp incentives for 2027?
