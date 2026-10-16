#!/usr/bin/env python3
"""Build the static site: src/pages/*.html -> docs/. No dependencies.

Each page file starts with header lines (slug, title, nav, desc, toc) then a line '---', then the body.
h2 elements with ids become the table of contents.
"""
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "src", ROOT / "docs"
SITE = "Copilot, plainly"
VERIFIED = "16 October 2026"


def parse(path):
    head, body = path.read_text(encoding="utf-8").split("\n---\n", 1)
    meta = {}
    for line in head.strip().splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body.strip()


def main():
    pages = [parse(p) for p in sorted((SRC / "pages").glob("*.html"))]
    pages.sort(key=lambda m: int(m[0]["order"]))
    OUT.mkdir(exist_ok=True)
    for child in OUT.iterdir():
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    (OUT / "assets").mkdir()
    for f in (SRC / "assets").iterdir():
        shutil.copy(f, OUT / "assets" / f.name)
    (OUT / ".nojekyll").write_text("")

    nav_pages = [(m, b) for m, b in pages if m.get("nav") == "yes"]
    for i, (meta, body) in enumerate(pages):
        slug = meta["slug"]
        up = "" if slug == "" else "../"
        href = lambda s: up + (s + "/" if s else "") if s else (up or "./")
        nav = "".join(
            f'<a href="{href(m["slug"])}"{" aria-current=page" if m["slug"] == slug else ""}>{html.escape(m["navlabel"])}</a>'
            for m, _ in nav_pages
        )
        heads = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', body, flags=re.S)
        has_toc = meta.get("toc") == "yes" and len(heads) > 1
        toc = ""
        if has_toc:
            items = "".join(
                f'<li><a href="#{i_}">{re.sub(r"<[^>]+>", "", re.sub(r"<span class=.sec-num.>.*?</span>", "", t)).strip()}</a></li>'
                for i_, t in heads
            )
            toc = f'<nav class="toc" aria-label="On this page"><div class="toc-in"><h2>On this page</h2><ol>{items}</ol></div></nav>'
        prev_ = pages[i - 1] if i > 0 and pages[i - 1][0].get("nav") == "yes" and meta.get("nav") == "yes" else None
        next_ = pages[i + 1] if i + 1 < len(pages) and pages[i + 1][0].get("nav") == "yes" and meta.get("nav") == "yes" else None
        pager = ""
        if prev_ or next_:
            pager = '<div class="pager">'
            pager += f'<a href="{href(prev_[0]["slug"])}">&larr; {html.escape(prev_[0]["navlabel"])}</a>' if prev_ else "<span></span>"
            pager += f'<a href="{href(next_[0]["slug"])}">{html.escape(next_[0]["navlabel"])} &rarr;</a>' if next_ else "<span></span>"
            pager += "</div>"
        title = meta["title"] if slug == "" else f'{meta["title"]} | {SITE}'
        verified = ""
        if meta.get("verified") == "yes":
            verified = f'<p class="meta">Last checked against Microsoft\'s documentation: {VERIFIED}. Copilot changes often, so check the sources at the end of the page.</p>'
        page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(meta['desc'])}">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar"><div class="topbar-in">
<a class="brand" href="{href('')}">Copilot<span>, plainly</span></a>
<nav class="nav" aria-label="Main">{nav}</nav>
<button type="button" class="theme" id="theme">Dark mode</button>
</div></header>
<div class="wrap">
<div class="layout{' has-toc' if has_toc else ''}">
{toc}
<main id="main"><article>
{body}
{verified}
{pager}
</article></main>
</div>
</div>
<footer><div class="wrap">
<p>An independent guide for people who use Microsoft Copilot at work. It is not made by, endorsed by, or affiliated with Microsoft. Microsoft, Copilot, Word, Excel, PowerPoint, Outlook and Teams are trademarks of Microsoft.</p>
<p>Content is licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Format inspired by <a href="https://www.guidesforhumans.com/">Guides for Humans</a>. All text here is original. Prices and features change; the <a href="{up}references/">sources page</a> links to Microsoft's own pages.</p>
</div></footer>
<script src="{up}assets/app.js" defer></script>
</body>
</html>
"""
        dest = OUT / slug / "index.html" if slug else OUT / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")

    print(f"built {len(pages)} pages -> {OUT}")


if __name__ == "__main__":
    main()
