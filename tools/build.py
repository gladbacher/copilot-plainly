#!/usr/bin/env python3
"""Build the static site: src/pages/*.html -> docs/. No dependencies.

Each page file starts with header lines then a line '---', then the body.
Header keys: slug, title, nav, navlabel, desc, toc, order, verified, section, cheat.

  python3 tools/build.py                                   public site -> docs/
  python3 tools/build.py --org ORG.json --out /abs/dir     organisation edition -> /abs/dir

See README.md ("Organisation edition") and org-pack/TEMPLATE.md.
"""
import argparse
import html
import json
import re
import shutil
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC, DOCS = ROOT / "src", ROOT / "docs"
SITE = "Copilot, plainly"
VERIFIED = "6 November 2026"
ISSUES = "https://github.com/gladbacher/copilot-plainly/issues/new"
MARKER = ".copilot-plainly-build"

# Pages must be self-sufficient: never send readers to "IT".
ASK_IT = re.compile(r"(?i:\b(ask|tell|check with|contact)\s+(your\s+)?IT\b)|\bIT team\b|to IT\b")

# Keys an organisation can fill in. Each appears as <aside class="org" data-key="..."></aside>.
ORG_KEYS = {
    "policy": "AI / Copilot use policy",
    "support": "Where to get help",
    "tiers": "Who gets which licence, and how to request one",
    "agents": "Approved or recommended agents",
    "agent-sharing": "Rules for building and sharing your own agents",
    "retention": "How long chats are kept",
    "data-rules": "Classification, customer data and personal data rules",
    "report-oversharing": "How to report something you shouldn't see",
    "feedback": "Where to send feedback on this guide",
    "training": "Internal training and champions network",
}
ASIDE = re.compile(r'<aside class="org" data-key="([a-z-]+)"></aside>')


def parse(path):
    head, body = path.read_text(encoding="utf-8").split("\n---\n", 1)
    meta = {}
    for line in head.strip().splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body.strip()


def org_box(key, org):
    ans = org.get("answers", {}).get(key)
    if not ans:
        return ""
    links = "".join(
        f'<li><a href="{html.escape(l["url"])}">{html.escape(l["text"])}</a></li>' for l in ans.get("links", [])
    )
    links = f"<ul>{links}</ul>" if links else ""
    todo = " todo" if "TODO" in ans.get("html", "") else ""
    return (
        f'<aside class="org-box{todo}" data-key="{key}"><p class="org-h">At {html.escape(org["name"])}</p>'
        f'{ans.get("html", "")}{links}</aside>'
    )


def fill_asides(body, org):
    return ASIDE.sub(lambda m: org_box(m.group(1), org) if org else "", body)


def check_org(org):
    for k in ("name", "answers"):
        if k not in org:
            sys.exit(f"org file is missing '{k}'")
    unknown = set(org["answers"]) - set(ORG_KEYS)
    if unknown:
        sys.exit(f"org file has unknown keys: {sorted(unknown)}")


def prepare_out(out):
    if out.exists():
        if any(out.iterdir()) and not (out / MARKER).exists() and out != DOCS:
            sys.exit(f"refusing to wipe {out}: not empty and not a previous build")
        for child in out.iterdir():
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    out.mkdir(parents=True, exist_ok=True)


def write_summary(out, org):
    rows = ""
    for key, label in ORG_KEYS.items():
        ans = org["answers"].get(key)
        if not ans:
            continue
        links = "".join(
            f'<li><a href="{html.escape(l["url"])}">{html.escape(l["text"])}</a></li>' for l in ans.get("links", [])
        )
        links = f"<ul>{links}</ul>" if links else ""
        rows += f"<h2>{html.escape(label)}</h2>\n{ans.get('html', '')}{links}\n"
    name = html.escape(org["name"])
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Copilot at {name}</title>
<style>body{{font:16px/1.6 Segoe UI,Arial,sans-serif;max-width:46rem;margin:2rem auto;padding:0 1rem;color:#222}}h1{{font-size:1.9rem}}h2{{font-size:1.25rem;margin-top:1.8em;border-bottom:1px solid #ddd;padding-bottom:.2em}}</style>
</head><body>
<h1>Copilot at {name}</h1>
<p>Everything {name}-specific that goes with the independent guide <em>Copilot, plainly</em>.</p>
{rows}
</body></html>
"""
    (out / "org-summary.html").write_text(page, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--org", help="absolute path to an org pack JSON file")
    ap.add_argument("--out", help="absolute output directory (required with --org; must be outside the repo)")
    args = ap.parse_args()

    org = None
    if args.org:
        if not args.out:
            sys.exit("--org needs --out")
        org = json.loads(Path(args.org).read_text(encoding="utf-8"))
        check_org(org)
    out = DOCS
    if args.out:
        out = Path(args.out).resolve()
        if out == ROOT or ROOT in out.parents or DOCS in out.parents or out == DOCS:
            sys.exit("--out must be outside the repository")
    elif org:
        sys.exit("--org needs --out")

    pages = [parse(p) for p in sorted((SRC / "pages").glob("*.html"))]
    pages.sort(key=lambda m: int(m[0]["order"]))

    # Build guard: no "ask IT" in page text.
    bad = []
    for meta, body in pages:
        for m in ASK_IT.finditer(body):
            bad.append(f'{meta["slug"] or "index"}: "{m.group(0)}"')
    if bad:
        sys.exit("build failed: 'ask IT' wording found:\n  " + "\n  ".join(bad))

    prepare_out(out)
    if out != DOCS:
        (out / MARKER).write_text("")
    (out / "assets").mkdir()
    for f in (SRC / "assets").iterdir():
        shutil.copy(f, out / "assets" / f.name)
    (out / ".nojekyll").write_text("")

    nav_pages = [m for m, _ in pages if m.get("nav") == "yes"]
    # Reading order for pagers: nav pages, with each section's sub-pages right after its hub.
    sequence = []
    for m, _ in pages:
        if m.get("nav") == "yes":
            sequence.append(m)
            sequence.extend(s for s, _ in pages if s.get("section") == m["slug"] and s is not m)
    seq_slugs = [m["slug"] for m in sequence]

    for meta, body in pages:
        slug = meta["slug"]
        up = "" if slug == "" else "../"
        href = lambda s: up + (s + "/" if s else "") if s else (up or "./")
        section = meta.get("section", "")
        current = section or slug
        nav = "".join(
            f'<a href="{href(m["slug"])}"{" aria-current=page" if m["slug"] == current else ""}>{html.escape(m["navlabel"])}</a>'
            for m in nav_pages
        )
        body = fill_asides(body, org)
        heads = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', body, flags=re.S)
        has_toc = meta.get("toc") == "yes" and len(heads) > 1
        toc = ""
        if has_toc:
            items = "".join(
                f'<li><a href="#{i_}">{re.sub(r"<[^>]+>", "", re.sub(r"<span class=.sec-num.>.*?</span>", "", re.sub(r"<span class=.tier [^>]*>(.*?)</span>", r"\1: ", t))).strip()}</a></li>'
                for i_, t in heads
            )
            toc = f'<nav class="toc" aria-label="On this page"><div class="toc-in"><h2>On this page</h2><ol>{items}</ol></div></nav>'

        secnav = ""
        if section:
            members = [m for m in sequence if m["slug"] == section or m.get("section") == section]
            links = "".join(
                f'<a href="{href(m["slug"])}"{" aria-current=page" if m["slug"] == slug else ""}>{html.escape(m.get("secLabel") or m["navlabel"])}</a>'
                for m in members
            )
            secnav = f'<nav class="secnav" aria-label="In this section">{links}</nav>'

        pager = ""
        if slug in seq_slugs:
            i = seq_slugs.index(slug)
            prev_ = sequence[i - 1] if i > 0 else None
            next_ = sequence[i + 1] if i + 1 < len(sequence) else None
            pager = '<div class="pager">'
            pager += f'<a href="{href(prev_["slug"])}">&larr; {html.escape(prev_["navlabel"])}</a>' if prev_ else "<span></span>"
            pager += f'<a href="{href(next_["slug"])}">{html.escape(next_["navlabel"])} &rarr;</a>' if next_ else "<span></span>"
            pager += "</div>"

        title = meta["title"] if slug == "" else f'{meta["title"]} | {SITE}'
        verified = ""
        if meta.get("verified") == "yes":
            verified = f'<p class="meta">Last checked against Microsoft\'s documentation: {VERIFIED}. Copilot changes often, so check the sources at the end of the page.</p>'

        if org and org["answers"].get("feedback", {}).get("url"):
            fb_url = org["answers"]["feedback"]["url"]
        else:
            fb_url = ISSUES + "?title=" + urllib.parse.quote("Feedback: " + meta["title"])
        feedback = f'<p class="feedback">Was this useful? <a href="{html.escape(fb_url)}">Report a problem or suggest a fix</a>.</p>'
        badge = f'<span class="orgbadge">{html.escape(org["name"])} edition</span>' if org else ""

        page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(meta['desc'])}">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body{' class="cheat"' if meta.get("cheat") == "yes" else ''}>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar"><div class="topbar-in">
<a class="brand" href="{href('')}">Copilot<span>, plainly</span></a>{badge}
<nav class="nav" aria-label="Main">{nav}</nav>
<button type="button" class="theme" id="theme">Dark mode</button>
</div></header>
<div class="wrap">
<div class="layout{' has-toc' if has_toc else ''}">
{toc}
<main id="main"><article>
{secnav}
{body}
{verified}
{pager}
</article></main>
</div>
</div>
<footer><div class="wrap">
{feedback}
<p>An independent guide for people who use Microsoft Copilot at work. It is not made by, endorsed by, or affiliated with Microsoft. Microsoft, Copilot, Word, Excel, PowerPoint, Outlook and Teams are trademarks of Microsoft.</p>
<p>Content is licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Format inspired by <a href="https://www.guidesforhumans.com/">Guides for Humans</a>. All text here is original. Prices and features change, so check Microsoft's own pages.</p>
</div></footer>
<script src="{up}assets/app.js" defer></script>
</body>
</html>
"""
        dest = out / slug / "index.html" if slug else out / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")

    if org:
        write_summary(out, org)
    print(f"built {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
