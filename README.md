# Copilot, plainly

Unofficial, plain-English guides to Microsoft Copilot for people who use it at work.
Not made by, endorsed by, or affiliated with Microsoft.

## Layout
- `src/pages/*.html` page content (header lines, then `---`, then the body)
- `src/assets/` shared CSS and JS
- `tools/build.py` builds `src/` into `docs/` (no dependencies: `python3 tools/build.py`)
- `docs/` the generated site, served by GitHub Pages
- `org-pack/` template and fictional example for organisation editions
- `ROLLOUT.md` generic notes for rolling the guide out in an organisation
- `research/` source notes with URLs and retrieval dates. Every factual claim on the site should trace back to one of these.

## Editing
1. Edit a file in `src/pages/`.
2. Run `python3 tools/build.py`.
3. Preview: `cd docs && python3 -m http.server 8765`, then open http://localhost:8765/.
4. Commit `src/` and `docs/` together.

## Page header keys
`slug`, `title`, `nav` (yes/no), `navlabel`, `desc`, `toc` (yes/no), `order` (integer; pages sort by it), `verified` (yes adds the "last checked" line), plus:
- `section: agents` marks a sub-page of a section. The build adds a section mini-nav and a pager that runs through the section. The top-nav item whose slug equals the section name shows as current. Sub-pages are `nav: no`. `secLabel` (optional) overrides the label in the mini-nav.
- `cheat: yes` marks a printable cheat sheet (one A4 page via `@media print`).

Orders go up in tens (agents sub-pages are 81 to 86) so a page such as a Cowork bonus can drop in at 90 without renumbering.

## Tier sections
Every guide that differs by licence has `<h2 id="chat" class="tiered">` and `<h2 id="premium" class="tiered">` sections, each starting with a badge: `<span class="tier tier-chat">Chat</span>` or `<span class="tier tier-premium">Premium</span>`. Shared material goes before them. Never mix the tiers in one paragraph or table. The homepage tracks deep-link to these anchors.

## Organisation edition
Public pages contain empty `<aside class="org" data-key="KEY"></aside>` slots that render nothing. An organisation fills them from a JSON pack (see `org-pack/TEMPLATE.md`):

```bash
python3 tools/build.py --org /abs/path/org.json --out /abs/path/outside-repo
```

It adds "At <name>" boxes, a top-bar badge, routes feedback to the org's `feedback` URL, and writes `org-summary.html` (one paste-ready page). `--out` must be outside the repo. Keep real packs outside the repo; only `org-pack/example.json` is tracked.

## The "ask IT" guard
The build fails if a page matches wording such as "ask IT", "tell IT", "check with IT", "contact IT", "IT team" or "to IT". The site must stand on its own: say what the reader can check themselves, or state "this is an organisation setting".

## Cheat sheets
`cheatsheet-chat` and `cheatsheet-premium` are one-page printable sheets. Print CSS hides the nav and footer.

## Content rules
- Prices and features need a Microsoft source and a retrieval date in `research/`.
- If Microsoft's documentation and other reports disagree, say so on the page.
- Update the "last checked" date in `tools/build.py` (`VERIFIED`) whenever pages are re-verified.

## Licence
Content and code: [CC BY 4.0](LICENSE). Reuse with credit.
