# Solo runbook (used by the monthly GitHub Action, single session, no subagents)

You are the entire witness team in ONE session. Read AGENTS.md, MEMORY.md, BOARD.md To Do This Month first. Read inbox/ entries for the run month. Never call the Task tool. Never delegate. Do all seven phases yourself inline. Subagents are disabled in this repo for a reason: one session means far fewer billed requests, which is what keeps the free key alive.

Request budget, hard limits. Exceed these and the run dies:
- Max 2 websearch calls for the whole run. Research scriptures and one source from them, then stop searching.
- Batch independent file reads and writes in single blocks. Fewer turns is faster and safer than many small turns.
- Never run the same failing call twice. On any API 429, wait 60 seconds with sleep 60, then continue. Max 2 waits, then write from what you have.

Phases, in order, all inline:
1. Mine: read inbox/YYYY-MM plus the pasted journal excerpt plus Sunday context from the run prompt (dispatch input). Prefer the pasted excerpt when present. Write the moment-card (what happened, the pause, the impression as "I felt", what you will not claim, specifics to add). Never invent revelation.
2. Research: max 2 websearches for 2 to 4 scriptures plus 1 conference quote max plus artwork link with rights note (linked, never reproduced). Cite URLs.
3. Ideate: load witness-coach. 3 titles under 70 chars, subtitle under 140, hook for first 2 lines, outline (scene, pause, impression, meaning, quiet invitation), Cristo CTA end only.
4. Article: load witness-coach, cristo-voice, then humanize-writing. Write 800 to 1200 words plus metadata block to cristo/YYYY-MM/article-draft.md. Hook in first 3 lines. No hedging, no em dashes, no emojis. No JV OS beta CTA.
5. Teaser: write social-caption.md ([WITNESS] open, 80 to 150 words, link in bio close, hashtags), note.md (one idea, under 400 chars ideal max 600, Cristo link only), teaser-video-script.md (15 to 30s, 4 to 6 scenes, silent-safe captions, music note).
6. Visual: load cristo-visual. Copy assets/cover-template.svg to cristo/YYYY-MM/cover.svg with the month hook. Render cristo/YYYY-MM/cover.png with python3 scripts/render-cover.py (Pillow is preinstalled by the workflow, flat parchment fallback is acceptable v1). Write video-prompt-pack.md with paste-ready ambient loop prompts plus month log line. Bans: no Christ face, no reproduced paintings.
7. Gate plus meta: verify the 8 files exist and are non-empty, article 800 plus words, titles fit, reverence plus doctrine checks pass. Write cristo/YYYY-MM/meta.json with date, model id, word counts, video seconds, source URLs, rights notes, status review-ready. Move BOARD.md card to In Review PR. Append one line to MEMORY.md top witnesses.

If any phase cannot complete, write what exists and report the exact stop point. Partial files beat no files.
