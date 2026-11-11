# Call Review: Pause & Play Finder

Turns a call transcript into coached "pause and play" moments (each 4 minutes max) for AE enablement sessions.

## How to use
1. Open this repo in Claude Code (or a Claude session on it).
2. Run `/call-review` and paste the transcript, or give a file path, for example `/call-review calls/acme_discovery.txt`.
3. Optionally add context: `AE: Sam · Mid-market retail · 2nd call · focus on objection handling`.

Tip: keep transcripts in a `calls/` folder, and anonymise names/pricing before showing clips to a group.

## What you get
Call snapshot, scorecard across agenda setting, discovery, sales acumen, product knowledge, objection handling, competitive positioning, storytelling and next steps, then 4-6 ranked clips each with set-up, pause point, facilitator questions, coaching tips, a better talk track and a role-play rep. It also gives patterns, a session plan and a verify list.

## Tuning
Edit `.claude/skills/call-review/SKILL.md` to add your methodology (DEPTH definitions already live in `DEPTH_Definitions.md` there), your own scorecard, or product facts to check claims against.

## Webpage version
Open `call-review.html` in a browser (double-click, no hosting or API key needed).
1. Paste the transcript and click **Build prompt**; it copies a full prompt (rules, DEPTH, JSON format).
2. Paste that into Claude, copy Claude's reply back into step 2, and click **Render review**.
3. **Review** shows the full write-up (toggle facilitator notes, print to PDF). **Present** shows one clip at a time with the pause point and questions, and reveals coaching on click (arrow keys to move).
