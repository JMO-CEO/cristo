# Push cristo-substack-scaffold to JMO-CRISTO/cristo-substack (beginner steps)

This folder is the full contents of the public repo. The private JV OS repo stays private.

## 1. Create the public repo
1. Go to github.com, log in as JMO-CRISTO (or your account that will own it).
2. New repository, name `cristo-substack`, Public, no README (this folder has the files).
3. Copy the repo URL, it looks like https://github.com/JMO-CRISTO/cristo-substack.git

## 2. Push these files
1. On your PC, open a terminal in the `cristo-substack-scaffold` folder.
2. Run: git init -b main
3. Run: git add .
4. Run: git commit -m "monthly witness pipeline v1"
5. Run: git remote add origin https://github.com/JMO-CRISTO/cristo-substack.git
6. Run: git push -u origin main

## 3. Add the Gemini secret
1. On github.com, open JMO-CRISTO/cristo-substack, Settings, Secrets and variables, Actions.
2. New repository secret, name `GEMINI_API_KEY`, value is your AI Studio key.
3. Save. Never paste the key in any file or chat.

## 4. Enable Actions plus PR permissions
1. Settings, Actions, General: allow all actions.
2. Workflow permissions: Read and write permissions plus Allow GitHub Actions to create and approve pull requests.

## 5. Test before the monthly run
1. Actions tab, pick Monthly Witness, press Run workflow.
2. Wait for green check, then open the Pull requests tab and review the 8 files in cristo/YYYY-MM.
3. The schedule fires on the 25th monthly as a reminder. Your real trigger is manual Run workflow on the Sunday you build.

## What lives here
- .github/workflows/monthly-witness.yml: the always on runner, PC off safe.
- .opencode/agents plus commands plus skills: cristo copies. persuasion-coach and EMPIRE substack-visual are intentionally NOT vendored here so business copy can never leak into testimony.
- prompts: short entry prompts plus orchestrate.md used by the Action.
- assets/cover-template.svg plus scripts/render-cover.py: zero spend visual builder, reverent v0 tokens.
- inbox/: drop daily journal entries here during the month. Never published verbatim.
- Substack/examples: empty until the Lindon pilot ships, then the pilot becomes anchor 1.
