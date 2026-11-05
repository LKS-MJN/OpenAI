# Interview with a vampire

A complete, dependency-free branching Halloween game. Six questions, 729 possible answer sequences, three endings, an original SVG study, optional procedural sound, local ending collection, keyboard controls, and reduced-motion support. No API keys or remote assets required.

## Run

Requires Node.js 18+ and Python 3. From this checkout:

```sh
npm run dev
```

Open port 5173 in your development environment. To build a static release:

```sh
npm test
npm run build
npm run preview
```

The preview serves `dist/` on port 4173. No dependency installation is needed. The deployable files are in `dist/`.

## Test the main flow

Select **Enter the interview**, then answer six questions with buttons or keys 1–3. Consistently choosing 1 earns the night shift; choosing 2 earns the estate; choosing 3 escapes. Mixed answers use accumulated attitude, with caution taking precedence in ties. Replay to collect all three endings. Inspect the sparkle in the study for a new clue each round. **How to play** and clues open keyboard-accessible dialogs; Escape closes them. Sound is off by default. Ending collection persists in this browser; unavailable storage displays a notice without blocking play.

`npm test` checks all 729 routes and the three consistent-answer outcomes. `python3 tests/browser.py` runs the browser smoke test when Python Playwright and Chromium at `/usr/bin/chromium` are installed and the dev server is running. It checks desktop/mobile, all endings, replay, collection, dialogs, keyboard input, and sound control. Screenshots are saved under `/tmp`.

## Publish a playable link

This is a static site and works from a subdirectory, including GitHub Pages.

- **GitHub Pages:** Push the project to the repository. In Settings → Pages, choose Deploy from a branch, then `main` and `/ (root)`. The root files are directly playable; no Actions workflow or build is needed. GitHub will display the playable URL when deployment completes.
- **Netlify:** Run `npm run build`, then upload `dist/` using Netlify’s manual deployment page. Alternatively connect the repository with build command `npm run build` and publish directory `dist`.
- **Vercel:** Import the repository, select Other framework, use build command `npm run build`, and output directory `dist`.

The GitHub Pages address will be https://lks-mjn.github.io/OpenAI/ once Pages is enabled and its deployment completes. Configure it at https://github.com/LKS-MJN/OpenAI/settings/pages using the `main` branch and `/ (root)`.
