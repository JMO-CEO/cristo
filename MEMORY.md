# MEMORY.md - long term facts for agents. No secrets here, ever.

## Voice
- Reverent, plain, specific. First person witness. Never hedge. Never use em dashes. No emojis in published copy.
- CTA is always the Cristo section https://jaredmoss.substack.com/s/cristo plus reply to cristo@jaredmoss.com. End of article only, never mid article. Never the JV OS beta CTA here.

## Brand v1 (LOCKED 2026-09-21, anchors: Alabaster collection plus Tebow Foundation; mantra deferred; no YouTube)
- Canvas Temple White #FFFFFF, cards Warm Parchment #F5F0E6, ink Deep Night #1A1A2E, body Soft Gray #5A5A6A, accent Muted Gold #C9A86A hairlines only.
- Headlines: reverent serif (candidate: Cormorant Garamond 500, alt EB Garamond). Subtext Montserrat 400/600. Protest Guerrilla, Carter One, Last Shuriken all banned here.
- Teaser letterbox: Deep Night #0A0328 bars top and bottom for the vertical cut only, bridges one social handle.

## Style anchors (cristo examples)
- 2026-09 Lindon Temple cleaning pilot (pending): white jumpsuits 9:45 to 11:45pm, 25 from Midway, frames not glass, pause at the foot, "You are worthy, my son." Link Al Young O Divine Redeemer, never reproduce pixels.

## Top witnesses that worked
- 2026-09-25: "At 9:45 PM on a Tuesday, twenty-five men from Midway stepped through the side doors of the Lindon Temple wearing white jumpsuits." (pilot review-ready)

## Pipeline facts
- Public drafts repo: JMO-CEO/cristo (see README-PUSH.md). Text model: google/gemini-3.5-flash-lite. Secret GEMINI_API_KEY must be exported as env GOOGLE_GENERATIVE_AI_API_KEY in the workflow, that is the exact name the Google provider reads. Zero image spend v1: code built SVG/PNG plus prompt packs.
- Cloud runbook is SOLO, one session, Task tool disabled via subagent_depth 0. Solo run with batched tool calls and max 2 websearches fits in 30. Subagent team stays for local runs only.
- Cloud pacing law: batch independent calls per block to cut billed requests, never delegate, max 2 websearches per run, sleep 60 on 429 max twice. Free key allows about 5 requests per minute.
- Job timeout is 30 min. PR step runs on always() so partial drafts are preserved instead of vanishing.
- Monthly folder: cristo/YYYY-MM with article-draft.md, social-caption.md, note.md, teaser-video-script.md, music-ask.md, cover.svg, cover.png, video-prompt-pack.md, meta.json. Source journal stays in inbox/, never published verbatim.
- Single handle rule: social captions start with [WITNESS], hashtags #WitnessOfChrist #Priesthood, link in bio to Cristo section week of publish.

## Corrections log
- Music system: Substack artists first (Contemplative Cadences, Piano and Prayer, Praying at the Piano, lady chapel, Walking Hymnal). Written permission before use, 7-day window, Sound Collection or voiceover fallback. Never borrowed trending sounds.
- 2026-09-21: brand v1 LOCKED plus music collab workflow built. Mantra deferred to emerge over months. YouTube out of scope.
