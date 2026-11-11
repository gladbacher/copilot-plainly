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
SITE = "Copilot Flight Deck"
VERIFIED = "6 November 2026"
OWNER = "Chris Kenny"  # name in the copyright notice
YEAR = "2026"
LICENCE_URL = "https://creativecommons.org/licenses/by-nc-nd/4.0/"
AI_BOTS = ["GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-Web", "anthropic-ai", "CCBot", "Google-Extended", "PerplexityBot", "Bytespider", "Applebot-Extended", "Amazonbot", "cohere-ai", "Meta-ExternalAgent", "FacebookBot", "Diffbot", "Omgilibot", "ImagesiftBot"]
SITE_URL = "https://gladbacher.github.io/copilot-plainly/"  # public address; used for share tags, sitemap and the 404 page
BASE_PATH = "/" + SITE_URL.split("/", 3)[3]
FAVICON = "data:image/svg+xml," + urllib.parse.quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0b6e6e"/><path d="M14 36l36-16-10 30-8-12z" fill="#fff"/></svg>')
MARKER = ".copilot-plainly-build"

# Pages must be self-sufficient: never send readers to "IT".
# "IT" is matched in capitals only, so "ask it to..." is fine.
ASK_IT = re.compile(r"\b(?i:ask|tell|check with|contact)\s+(?i:your\s+)?IT\b|\bIT team\b|\bto IT\b")

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


def load_refs():
    """Citation key -> (title, url), from research/00-references.md."""
    refs = {}
    f = ROOT / "research" / "00-references.md"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"- \*\*2026([a-z]+)\.\*\* .*?\*(.+?)\*.*?(https://\S+)", line)
            if m:
                refs[m.group(1)] = (m.group(2).rstrip(".?") + ("?" if m.group(2).endswith("?") else ""), m.group(3))
    return refs


def strip_cites(body, refs):
    """Source files keep (Microsoft, 2026x) citation keys. Readers get clean text
    plus one 'Where this comes from' list per page."""
    keys = []
    for k in re.findall(r"2026([a-z]{1,2})\b", body):
        if k in refs and k not in keys:
            keys.append(k)
    body = re.sub(r"Sources?(?: for the recipe and tips)?: Microsoft \([^)]*\)(?:, Microsoft \([^)]*\))*(?:, [a-z ]+)?\.\s*", "", body)
    body = re.sub(r"\s*\((?:Microsoft, )?2026[a-z]{1,2}(?:, 2026[a-z]{1,2})*\)", "", body)
    body = re.sub(r'<p class="meta">\s*</p>\n?', "", body)
    seen, items = set(), ""
    for k in keys:
        title, url = refs[k]
        if url not in seen:
            seen.add(url)
            items += f'<li><a href="{html.escape(url)}">{html.escape(title)}</a></li>'
    src = f'<details class="src"><summary>Where this comes from ({len(seen)} Microsoft page{'' if len(seen) == 1 else 's'})</summary><ul>{items}</ul></details>' if items else ""
    return body, src


TIER_H2 = re.compile(r'<h2[^>]*class="tiered"[^>]*>\s*<span class="tier tier-(chat|premium)">')
PROMPTBOX = re.compile(r'<div class="promptbox"><span class="label">(.*?)</span><pre>(.*?)</pre></div>', re.S)


def text_of(fragment):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", re.sub(r'<span class="tier[^>]*>.*?</span>', "", fragment))).strip()


def wrap_tiers(body):
    """Wrap each tier section so the licence switch can hide the other one.
    With JavaScript off nothing is hidden."""
    out = []
    for part in re.split(r"(?=<h2[ >])", body):
        m = TIER_H2.match(part)
        out.append(f'<section class="tier-sec" data-tier="{m.group(1)}">{part}</section>' if m else part)
    body = "".join(out)
    return re.sub(r'<li><span class="tier tier-(chat|premium)">', r'<li data-tier="\1"><span class="tier tier-\1">', body)


def collect_prompts(pages, hubs):
    """Every prompt box on the site, for the searchable library."""
    items, seen = [], set()
    for meta, body in pages:
        slug = meta["slug"]
        if not slug or slug == "troubleshooting":
            continue
        sec = meta.get("section", "")
        cat = "Everyday" if slug == "prompts" else hubs.get(sec, meta["navlabel"]) if sec in ("playbooks", "agents", "start") else meta["navlabel"]
        for part in re.split(r"(?=<h2[ >])", body):
            m = TIER_H2.match(part)
            tier = m.group(1) if m else ""
            for pb in PROMPTBOX.finditer(part):
                key = re.sub(r"\s+", " ", pb.group(2)).strip()
                if key in seen:
                    continue
                seen.add(key)
                h3s = re.findall(r"<h3[^>]*>(.*?)</h3>", part[: pb.start()], re.S)
                h3 = text_of(h3s[-1]) if h3s else ""
                label = text_of(pb.group(1))
                if slug == "prompts":
                    title = h3 or "Prompt"
                elif h3:
                    title = f'{meta["navlabel"]}: {h3}'
                elif not label.lower().startswith(("prompt", "chat", "premium")):
                    title = f'{meta["navlabel"]}: {label}'
                else:
                    title = meta["navlabel"]
                items.append({"tier": tier, "cat": cat, "title": title, "slug": slug, "page": meta["navlabel"], "text": pb.group(2)})
    return items


def render_library(items, href):
    out = ['<div class="lib-tools"><label for="libq">Search the prompts</label><input type="search" id="libq" class="filter" data-target=".pitem" placeholder="e.g. email, meeting, formula"><span id="libcount" class="meta"></span></div>',
           '<div class="chips" id="libcats" hidden></div>']
    for it in items:
        tier = f' data-tier="{it["tier"]}"' if it["tier"] else ""
        badge = f'<span class="tier tier-{it["tier"]}">{it["tier"].capitalize()}</span>' if it["tier"] else ""
        src = "" if it["slug"] == "prompts" else f' <span class="meta">From <a href="{href(it["slug"])}">{html.escape(it["page"])}</a></span>'
        out.append(f'<div class="pitem"{tier} data-cat="{html.escape(it["cat"])}"><h3>{badge}{html.escape(it["title"])}</h3>{src}'
                   f'<div class="promptbox"><span class="label">{html.escape(it["cat"])}</span><pre>{it["text"]}</pre></div></div>')
    return "\n".join(out)


def index_sections(meta, body, url):
    """Split a processed page into searchable sections."""
    out = []
    for part in re.split(r"(?=<h2[ >])", body):
        m = TIER_H2.match(part)
        h = re.match(r'<h2(?: id="([^"]+)")?[^>]*>(.*?)</h2>', part, re.S)
        text = re.sub(r"\s+([.,;:)])", r"\1", html.unescape(text_of(re.sub(r"<[^>]+>", " ", re.sub(r'<span class="tier[^>]*>.*?</span>', "", part)))))
        if len(text) < 25:
            continue
        out.append({
            "u": url + ("#" + h.group(1) if h and h.group(1) else ""),
            "p": meta["title"],
            "h": html.unescape(text_of(h.group(2))) if h else "",
            "t": m.group(1) if m else "",
            "x": text,
        })
    return out


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
<!-- (c) {YEAR} {OWNER}. Licensed CC BY-NC-ND 4.0 ({LICENCE_URL}). Copying, adapting or selling this site is not permitted. -->
<html lang="en"><head><meta charset="utf-8"><title>Copilot at {name}</title>
<style>body{{font:16px/1.6 Segoe UI,Arial,sans-serif;max-width:46rem;margin:2rem auto;padding:0 1rem;color:#222}}h1{{font-size:1.9rem}}h2{{font-size:1.25rem;margin-top:1.8em;border-bottom:1px solid #ddd;padding-bottom:.2em}}</style>
</head><body>
<h1>Copilot at {name}</h1>
<p>Everything {name}-specific that goes with the independent guide <em>{SITE}</em>.</p>
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

    refs = load_refs()
    nav_pages = [m for m, _ in pages if m.get("nav") == "yes"]
    hubs = {m["slug"]: m["navlabel"] for m in nav_pages}
    library = collect_prompts(pages, hubs)
    # Reading order for pagers: nav pages, with each section's sub-pages right after its hub.
    sequence = []
    for m, _ in pages:
        if m.get("nav") == "yes":
            sequence.append(m)
            sequence.extend(s for s, _ in pages if s.get("section") == m["slug"] and s is not m)
    seq_slugs = [m["slug"] for m in sequence]

    search_index = []
    for meta, body in pages:
        slug = meta["slug"]
        is404 = slug == "404"
        if is404 and org:
            continue
        up = "" if slug == "" else BASE_PATH if is404 else "../"
        href = lambda s: up + (s + "/" if s else "") if s else (up or "./")
        section = meta.get("section", "")
        current = section or slug
        nav = "".join(
            f'<a href="{href(m["slug"])}"{" aria-current=page" if m["slug"] == current else ""}>{html.escape(m["navlabel"])}</a>'
            for m in nav_pages
        )
        body = fill_asides(body, org)
        if "<!--LIBRARY-->" in body:
            a, b = body.index("<!--LIB-SRC-->"), body.index("<!--/LIB-SRC-->")
            body = body[:a] + body[b:]
            body = body.replace("<!--LIBRARY-->", render_library(library, href))
        if "<!--PLAYBOOKS-->" in body:
            cards = "".join(
                f'<li><a class="card" href="{href(m["slug"])}"><b>{html.escape(m["navlabel"])}</b><span>{html.escape(m["desc"])}</span></a></li>'
                for m, _ in pages if m.get("section") == "playbooks" and m["slug"] != "playbooks")
            body = body.replace("<!--PLAYBOOKS-->", f'<ul class="cards">{cards}</ul>')
        body = body.replace("{SITE_URL}", SITE_URL.split("//", 1)[1].rstrip("/"))
        body = body.replace("{HOME}", BASE_PATH)
        body, sources = strip_cites(body, refs)
        if slug not in ("search", "404") and meta.get("cheat") != "yes":
            search_index += index_sections(meta, body, (slug + "/") if slug else "")
        body = wrap_tiers(body)
        heads = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', body, flags=re.S)
        has_toc = meta.get("toc") == "yes" and len(heads) > 1
        toc = ""
        if has_toc:
            items = "".join(
                f'<li{" data-tier=" + i_ if i_ in ("chat", "premium") else ""}><a href="#{i_}">{re.sub(r"<[^>]+>", "", re.sub(r"<span class=.sec-num.>.*?</span>", "", re.sub(r"<span class=.tier [^>]*>(.*?)</span>", r"\1: ", t))).strip()}</a></li>'
                for i_, t in heads
            )
            toc = f'<nav class="toc" aria-label="On this page"><details class="toc-in" open><summary>On this page</summary><ol>{items}</ol></details></nav>'

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
            verified = f'{sources}<p class="meta">Last checked against Microsoft\'s documentation: {meta.get("checked", VERIFIED)}. Copilot changes often.</p>'

        # No public feedback link. An organisation edition can supply its own internal route.
        fb_url = (org or {}).get("answers", {}).get("feedback", {}).get("url", "")
        feedback = f'<p class="feedback">Was this useful? <a href="{html.escape(fb_url)}">Send feedback</a>.</p>' if fb_url else ""
        badge = f'<span class="orgbadge">{html.escape(org["name"])} edition</span>' if org else ""

        page = f"""<!doctype html>
<!-- (c) {YEAR} {OWNER}. Licensed CC BY-NC-ND 4.0 ({LICENCE_URL}). Copying, adapting or selling this site is not permitted. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(meta['desc'])}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(meta['desc'])}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta name="theme-color" content="#0b6e6e">
<meta name="author" content="{OWNER}">
<meta name="copyright" content="&copy; {YEAR} {OWNER}. CC BY-NC-ND 4.0">
<meta name="robots" content="noai, noimageai">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="{up}assets/style.css">
<script>try{{var d=document.documentElement,t=localStorage.getItem('tier'),h=localStorage.getItem('theme');if(t==='chat'||t==='premium')d.setAttribute('data-tier',t);if(h==='light'||h==='dark')d.setAttribute('data-theme',h)}}catch(e){{}}</script>
</head>
<body{' class="cheat"' if meta.get("cheat") == "yes" else ''}>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar"><div class="topbar-in">
<a class="brand" href="{href('')}">Copilot <span>Flight Deck</span></a>{badge}
<div class="tierswitch" id="tierswitch" role="group" aria-label="Show guidance for my licence" hidden><span>My licence</span><button type="button" data-t="chat">Chat</button><button type="button" data-t="premium">Premium</button><button type="button" data-t="both">Both</button></div>
<a class="searchlink" href="{href('search')}"{" aria-current=page" if slug == "search" else ""}>Search</a>
<button type="button" class="theme" id="theme">Dark mode</button>
<nav class="nav" aria-label="Main">{nav}</nav>
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
<p>&copy; {YEAR} {OWNER}. Licensed under <a href="{LICENCE_URL}">CC BY-NC-ND 4.0</a>: you may share it with credit, but you may not sell it or change it. All text here is original. Prices and features change, so check Microsoft's own pages.</p>
</div></footer>
{f'<script src="{up}assets/search-index.js" defer></script>' if slug == "search" else ""}
<script src="{up}assets/app.js" defer></script>
</body>
</html>
"""
        dest = out / "404.html" if is404 else out / slug / "index.html" if slug else out / "index.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")

    (out / "assets" / "search-index.js").write_text("window.SEARCH_INDEX=" + json.dumps(search_index, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")
    if org:
        write_summary(out, org)
    else:
        urls = "".join(f"<url><loc>{SITE_URL}{m['slug'] + '/' if m['slug'] else ''}</loc></url>" for m, _ in pages if m["slug"] not in ("404", "search"))
        (out / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
        blocks = "".join(f"User-agent: {b}\nDisallow: /\n\n" for b in AI_BOTS)
        (out / "robots.txt").write_text(f"{blocks}User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    print(f"built {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main()
