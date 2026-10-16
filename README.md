# Copilot, plainly

Unofficial, plain-English guides to Microsoft Copilot for people who use it at work.
Not made by, endorsed by, or affiliated with Microsoft.

## Layout
- `src/pages/*.html` page content (header lines, then `---`, then the body)
- `src/assets/` shared CSS and JS
- `tools/build.py` builds `src/` into `docs/` (no dependencies: `python3 tools/build.py`)
- `docs/` the generated site, served by GitHub Pages
- `research/` source notes with URLs and retrieval dates. Every factual claim on the site should trace back to one of these.

## Editing
1. Edit a file in `src/pages/`.
2. Run `python3 tools/build.py`.
3. Preview: `cd docs && python3 -m http.server 8765`, then open http://localhost:8765/.
4. Commit `src/` and `docs/` together.

## Content rules
- Prices and features need a Microsoft source and a retrieval date in `research/`.
- If Microsoft's documentation and other reports disagree, say so on the page.
- Update the "last checked" date in `tools/build.py` (`VERIFIED`) whenever pages are re-verified.

## Licence
Content and code: [CC BY 4.0](LICENSE). Reuse with credit.
