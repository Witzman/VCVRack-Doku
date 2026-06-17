#!/usr/bin/env python3
"""
Generate HTML documentation from htmldoku/*.md
No external dependencies — uses stdlib only.
Output: docs/Rack-Doku/
"""
import os
import re
import shutil
import html as html_mod

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
OUT_DIR = os.path.join(BASE_DIR, "docs", "Rack-Doku")
os.makedirs(OUT_DIR, exist_ok=True)

SIDEBAR = [
    ("Common", [
        ("Overview", "readme"),
        ("Signal Flow & Concepts", "mental-model"),
        ("How a Patch Works", "how-a-patch-works"),
        ("Glossary", "glossary"),
        ("Using VCV Rack", "userguide"),
        ("Patching Use Cases", "patching-use-cases"),
        ("FAQ", "faq"),
    ]),
    ("Modules", {
        "Sound Generation": [
            ("VCO", "vco"),
            ("Noise", "noise"),
            ("Wavetable", "wavetable"),
        ],
        "Sound Shaping": [
            ("VCF", "vcf"),
            ("VCA", "vca"),
            ("Waveshaper & Distortion", "waveshaper-distortion"),
            ("Delay, Reverb & Chorus", "delay-reverb-chorus"),
        ],
        "Modulation / Control": [
            ("Envelopes", "envelope"),
            ("LFO", "lfo"),
            ("Sequencers", "sequencer"),
            ("Sample & Hold", "sample-hold"),
        ],
        "Utilities": [
            ("Mixer", "mixer"),
            ("Attenuverter", "attenuverter"),
            ("Mult & Splitter", "mult-splitter"),
            ("Quantizer", "quantizer"),
            ("Clock", "clock"),
            ("Logic", "logic"),
        ],
        "MIDI / I/O": [
            ("MIDI to CV", "midi-cv"),
            ("Audio Output", "audio-output"),
        ],
    }),
    ("Tutorials", [
        ("Your First Patch", "first-patch"),
        ("Intermediate Patch", "intermediate-patch"),
        ("Slow Psybient", "slow-psybient"),
    ]),
]

CSS = """\
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 16px;
    line-height: 1.65;
    color: #222;
    background: #f9f9f9;
}
#layout { display: flex; min-height: 100vh; }
#sidebar {
    width: 280px;
    flex-shrink: 0;
    background: #1e1e2e;
    color: #cdd6f4;
    padding: 1.5rem 0;
    position: fixed;
    top: 0; left: 0;
    height: 100vh;
    overflow-y: auto;
}
#sidebar h1 {
    font-size: 1rem;
    font-weight: 700;
    color: #cba6f7;
    padding: 0 1.25rem 1rem;
    margin: 0;
    border-bottom: 1px solid #313244;
    letter-spacing: 0.03em;
}
#sidebar .section-title {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #6c7086;
    padding: 1rem 1.25rem 0.25rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    user-select: none;
}
#sidebar .section-title:hover { color: #bac2de; }
#sidebar .section-title .arrow { transition: transform 0.2s; }
#sidebar .section-title.open .arrow { transform: rotate(90deg); }
#sidebar .section-content { display: none; }
#sidebar .section-content.open { display: block; }
#sidebar a {
    display: block;
    padding: 0.35rem 1.25rem 0.35rem 1.6rem;
    color: #bac2de;
    text-decoration: none;
    font-size: 0.9rem;
    border-left: 3px solid transparent;
}
#sidebar a::before { content: "· "; color: #6c7086; }
#sidebar a:hover { background: #313244; color: #cdd6f4; }
#sidebar a[aria-current="page"] {
    background: #313244;
    color: #cba6f7;
    border-left-color: #cba6f7;
    font-weight: 600;
}
#sidebar a[aria-current="page"]::before { color: #cba6f7; }
#content { margin-left: 280px; flex: 1; display: flex; flex-direction: column; }
header {
    background: #fff;
    border-bottom: 1px solid #e5e7eb;
    padding: 0.75rem 2rem;
    font-size: 0.85rem;
    color: #6c7086;
}
header strong { color: #222; }
main { flex: 1; padding: 2rem 2.5rem; max-width: 860px; }
article h1 { font-size: 1.9rem; margin-top: 0; color: #1e1e2e; }
article h2 { font-size: 1.3rem; margin-top: 2rem; color: #1e1e2e; border-bottom: 1px solid #e5e7eb; padding-bottom: 0.3rem; }
article h3 { font-size: 1.1rem; margin-top: 1.5rem; color: #313244; }
article p { margin: 0.75rem 0; }
article a { color: #7c3aed; }
article a:hover { color: #5b21b6; }
article table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.9rem; }
article th { background: #1e1e2e; color: #cdd6f4; text-align: left; padding: 0.5rem 0.75rem; font-weight: 600; }
article td { padding: 0.45rem 0.75rem; border-bottom: 1px solid #e5e7eb; vertical-align: top; }
article tr:nth-child(even) td { background: #f3f4f6; }
article code {
    background: #1e1e2e; color: #a6e3a1;
    padding: 0.15em 0.4em; border-radius: 3px;
    font-size: 0.85em;
    font-family: "JetBrains Mono","Fira Code",monospace;
}
article pre { background: #1e1e2e; color: #cdd6f4; padding: 1rem 1.25rem; border-radius: 6px; overflow-x: auto; margin: 1rem 0; }
article pre code { background: none; padding: 0; font-size: 0.85rem; }
article ul, article ol { padding-left: 1.5rem; }
article li { margin: 0.3rem 0; }
article hr { border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }
article blockquote { border-left: 4px solid #cba6f7; margin: 1rem 0; padding: 0.5rem 1rem; background: #f3f4f6; color: #555; }
.mermaid { background: #fff; border: 1px solid #e5e7eb; border-radius: 6px; padding: 1rem; margin: 1rem 0; text-align: center; }
article img { max-width: 120px; float: right; margin: 0 0 1rem 1.5rem; border: 1px solid #e5e7eb; border-radius: 4px; background: #fff; padding: 4px; }
footer { padding: 1rem 2.5rem; font-size: 0.8rem; color: #9ca3af; border-top: 1px solid #e5e7eb; }
#sidebar .sub-section-title {
    font-size: 0.65rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #45475a;
    padding: 0.6rem 1.25rem 0.2rem 1.6rem;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    user-select: none;
}
#sidebar .sub-section-title:hover { color: #bac2de; }
#sidebar .sub-section-title .arrow { transition: transform 0.2s; }
#sidebar .sub-section-title.open .arrow { transform: rotate(90deg); }
#sidebar .sub-content { display: none; }
#sidebar .sub-content.open { display: block; }
#sidebar a.sub-link {
    padding-left: 2rem;
    font-size: 0.85rem;
}
@media (max-width: 900px) {
    #layout { flex-direction: column; }
    #sidebar { width: 100%; height: auto; position: static; }
    #content { margin-left: 0; }
    main { padding: 1.25rem; }
}
"""


def build_sidebar(current_slug):
    parts = ['<nav id="sidebar">', '<h1>VCV Rack Handbook</h1>']
    sec_id = 0
    for section_title, entries in SIDEBAR:
        sid = f"sec-{sec_id}"; sec_id += 1
        if isinstance(entries, dict):
            active = any(slug == current_slug for subs in entries.values() for _, slug in subs)
        else:
            active = any(slug == current_slug for _, slug in entries)
        open_cls = " open" if active else ""
        parts.append(f'<div class="section-title{open_cls}" onclick="toggle(\'{sid}\')">{section_title}<span class="arrow">›</span></div>')
        parts.append(f'<div class="section-content{open_cls}" id="{sid}">')
        if isinstance(entries, dict):
            sub_id = 0
            for sub_title, sub_entries in entries.items():
                ssid = f"{sid}-sub-{sub_id}"; sub_id += 1
                sub_active = any(slug == current_slug for _, slug in sub_entries)
                sopen = " open" if sub_active else ""
                parts.append(f'<div class="sub-section-title{sopen}" onclick="event.stopPropagation();toggle(\'{ssid}\')">{sub_title}<span class="arrow">›</span></div>')
                parts.append(f'<div class="sub-content{sopen}" id="{ssid}">')
                for name, slug in sub_entries:
                    cur = ' aria-current="page"' if slug == current_slug else ""
                    parts.append(f'<a href="{slug}.html"{cur} class="sub-link">{name}</a>')
                parts.append('</div>')
        else:
            for name, slug in entries:
                cur = ' aria-current="page"' if slug == current_slug else ""
                parts.append(f'<a href="{slug}.html"{cur}>{name}</a>')
        parts.append('</div>')
    parts.append('</nav>')
    parts.append('''<script>
function toggle(id){
  var c=document.getElementById(id);
  var h=c.previousElementSibling;
  c.classList.toggle("open");
  h.classList.toggle("open");
}
</script>''')
    return "\n".join(parts)


# ─── Minimal Markdown → HTML converter ──────────────────────────────────────

def extract_fenced_blocks(text):
    """Extract ```lang ... ``` blocks, replace with tokens. Returns (text, blocks_list)."""
    blocks = []
    def replacer(m):
        lang = (m.group(1) or "").strip()
        content = m.group(2)
        blocks.append((lang, content))
        return f"\n\n%%FENCED_{len(blocks)-1}%%\n\n"
    text = re.sub(r'```(\w*)\n(.*?)```', replacer, text, flags=re.DOTALL)
    return text, blocks


def inline(text):
    """Apply inline markdown formatting."""
    # Escape HTML first (we'll unescape tokens after)
    text = html_mod.escape(text)
    # Code spans (already escaped so backtick content is safe)
    text = re.sub(r'`([^`]+)`', lambda m: f'<code>{m.group(1)}</code>', text)
    # Bold + italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Images (before links)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)([^)]*)\)',
                  lambda m: f'<a href="{m.group(2)[:-3]}.html{m.group(3)}">{m.group(1)}</a>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def parse_table(lines):
    """Parse a GitHub-style table from a list of lines."""
    rows = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        rows.append(cells)
    if len(rows) < 2:
        return None
    # rows[1] is the separator row
    header = rows[0]
    body = rows[2:]
    html = ['<table>']
    html.append('<tr>' + ''.join(f'<th>{inline(c)}</th>' for c in header) + '</tr>')
    for row in body:
        # Pad or trim to match header length
        while len(row) < len(header):
            row.append('')
        html.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in row[:len(header)]) + '</tr>')
    html.append('</table>')
    return '\n'.join(html)


def is_table_line(line):
    return '|' in line and line.strip().startswith('|')


def is_separator_line(line):
    return bool(re.match(r'^\|?[\s\-|:]+\|?$', line.strip()))


def md_to_html(text):
    text, fenced = extract_fenced_blocks(text)
    lines = text.split('\n')
    out = []
    i = 0

    def flush_para(buf):
        if buf:
            content = inline(' '.join(buf))
            out.append(f'<p>{content}</p>')
            buf.clear()

    para_buf = []

    while i < len(lines):
        line = lines[i]

        # Fenced block token
        m = re.match(r'^%%FENCED_(\d+)%%$', line.strip())
        if m:
            flush_para(para_buf)
            idx = int(m.group(1))
            lang, content = fenced[idx]
            escaped = html_mod.escape(content.rstrip())
            if lang == 'mermaid':
                out.append(f'<div class="mermaid">{content.strip()}</div>')
            else:
                out.append(f'<pre><code class="language-{html_mod.escape(lang)}">{escaped}</code></pre>')
            i += 1
            continue

        # Headings
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            flush_para(para_buf)
            level = len(m.group(1))
            content = inline(m.group(2))
            out.append(f'<h{level}>{content}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r'^---+$', line.strip()) or re.match(r'^\*\*\*+$', line.strip()):
            flush_para(para_buf)
            out.append('<hr>')
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            flush_para(para_buf)
            content = inline(line[1:].strip())
            out.append(f'<blockquote><p>{content}</p></blockquote>')
            i += 1
            continue

        # Table detection
        if is_table_line(line):
            flush_para(para_buf)
            table_lines = []
            while i < len(lines) and is_table_line(lines[i]):
                table_lines.append(lines[i])
                i += 1
            table_html = parse_table(table_lines)
            if table_html:
                out.append(table_html)
            continue

        # Unordered list
        if re.match(r'^[-*+]\s+', line):
            flush_para(para_buf)
            items = []
            while i < len(lines) and re.match(r'^[-*+]\s+', lines[i]):
                items.append(f'<li>{inline(re.sub(r"^[-*+]\s+", "", lines[i]))}</li>')
                i += 1
            out.append('<ul>' + '\n'.join(items) + '</ul>')
            continue

        # Ordered list
        if re.match(r'^\d+\.\s+', line):
            flush_para(para_buf)
            items = []
            while i < len(lines) and re.match(r'^\d+\.\s+', lines[i]):
                items.append(f'<li>{inline(re.sub(r"^\d+\.\s+", "", lines[i]))}</li>')
                i += 1
            out.append('<ol>' + '\n'.join(items) + '</ol>')
            continue

        # Empty line → paragraph break
        if line.strip() == '':
            flush_para(para_buf)
            i += 1
            continue

        # Regular text → accumulate paragraph
        para_buf.append(line.strip())
        i += 1

    flush_para(para_buf)
    return '\n'.join(out)


def get_title(md_text):
    m = re.search(r'^#\s+(.+)', md_text, re.MULTILINE)
    return m.group(1).strip() if m else "VCV Rack"


def convert_page(slug):
    src = os.path.join(SRC_DIR, f"{slug}.md")
    with open(src, encoding="utf-8") as f:
        md_text = f.read()

    title = get_title(md_text)
    body_html = md_to_html(md_text)
    sidebar_html = build_sidebar(slug)

    has_mermaid = 'class="mermaid"' in body_html
    mermaid_script = (
        '<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>\n'
        '<script>mermaid.initialize({startOnLoad:true,theme:"neutral"});</script>'
    ) if has_mermaid else ""

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_mod.escape(title)} — VCV Rack Handbook</title>
  <link rel="stylesheet" href="style.css">
  {mermaid_script}
</head>
<body>
<div id="layout">
{sidebar_html}
<div id="content">
  <header>VCV Rack Handbook — <strong>{html_mod.escape(title)}</strong></header>
  <main>
    <article>
{body_html}
    </article>
  </main>
  <footer>VCV Rack Patcher's Handbook · 2026</footer>
</div>
</div>
</body>
</html>
"""
    out_path = os.path.join(OUT_DIR, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    return out_path


def main():
    with open(os.path.join(OUT_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    for _, entries in SIDEBAR:
        if isinstance(entries, dict):
            for _, sub_entries in entries.items():
                for _, slug in sub_entries:
                    convert_page(slug)
                    print(f"  ✓ {slug}.html")
        else:
            for _, slug in entries:
                convert_page(slug)
                print(f"  ✓ {slug}.html")

    shutil.copy(
        os.path.join(OUT_DIR, "readme.html"),
        os.path.join(OUT_DIR, "index.html")
    )
    print("  ✓ index.html (copy of readme.html)")

    # Remove replaced and stale HTML files
    for stale in ["fundamental-modules.html", "befaco-modules.html",
                  "kernablauf.html", "anwendungsfaelle.html"]:
        stale_path = os.path.join(OUT_DIR, stale)
        if os.path.exists(stale_path):
            os.remove(stale_path)
            print(f"  ✗ removed {stale}")

    print(f"\nDone. Output: {OUT_DIR}")


if __name__ == "__main__":
    main()
