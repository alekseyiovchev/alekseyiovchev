"""Render the static SVG assets of the profile README in a light and a dark variant.

Run from the repository root:  python scripts/build_assets.py
Every asset is written as assets/<name>-light.svg and assets/<name>-dark.svg; the README
picks one through <picture> and prefers-color-scheme. Edit the data below and re-run.
"""

from __future__ import annotations

import textwrap
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

FONT = "'Segoe UI', Ubuntu, -apple-system, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Liberation Mono', monospace"

THEMES = {
    "light": {
        "bg_from": "#f8fafc",
        "bg_to": "#eef2ff",
        "card_bg": "#ffffff",
        "border": "#d0d7de",
        "title": "#6d28d9",
        "text": "#1f2937",
        "muted": "#57606a",
        "accent_a": "#7c3aed",
        "accent_b": "#0891b2",
        "chip_bg": "#f3f0ff",
        "chip_text": "#5b21b6",
        "blob_opacity": "0.28",
        "dot": "#94a3b8",
    },
    "dark": {
        "bg_from": "#0b1020",
        "bg_to": "#111827",
        "card_bg": "#0d1117",
        "border": "#30363d",
        "title": "#c4b5fd",
        "text": "#e6edf3",
        "muted": "#8b949e",
        "accent_a": "#a78bfa",
        "accent_b": "#22d3ee",
        "chip_bg": "#1e1b3a",
        "chip_text": "#c4b5fd",
        "blob_opacity": "0.35",
        "dot": "#334155",
    },
}

REDUCED_MOTION = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }"

PROJECTS = [
    {
        "slug": "cef-syslog-udp-proxy",
        "title": "cef-syslog-udp-proxy",
        "desc": (
            "Async UDP proxy that parses CEF/Syslog events, filters them by rules "
            "and forwards the original bytes to ELK. Admin API and UI, counters, "
            "JSON logs, CI with quality and security checks."
        ),
        "chips": ["Python 3.12", "asyncio", "FastAPI", "Docker", "CI"],
    },
    {
        "slug": "rag-document-search-api",
        "title": "rag-document-search-api",
        "desc": (
            "RAG service: indexes TXT and PDF documents into Qdrant and answers "
            "questions with the source chunks it used, filtering out weak matches "
            "by a similarity threshold."
        ),
        "chips": ["FastAPI", "Qdrant", "PostgreSQL", "LLM", "pytest"],
    },
    {
        "slug": "csv-worker-api",
        "title": "csv-worker-api",
        "desc": (
            "Upload a CSV, get a task id back at once; a Celery worker processes "
            "the file in the background, status and results come from the API."
        ),
        "chips": ["FastAPI", "Celery", "RabbitMQ", "Redis", "PostgreSQL"],
    },
]


def banner(t: dict[str, str]) -> str:
    w, h = 900, 230
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Oleksii Iovchev, Backend Lead">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t["bg_from"]}"/>
      <stop offset="1" stop-color="{t["bg_to"]}"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0" spreadMethod="repeat">
      <stop offset="0" stop-color="{t["accent_a"]}"/>
      <stop offset="0.5" stop-color="{t["accent_b"]}"/>
      <stop offset="1" stop-color="{t["accent_a"]}"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1 0" dur="9s" repeatCount="indefinite"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="42"/></filter>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.1" fill="{t["dot"]}" opacity="0.55"/>
    </pattern>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>
  <style>
    .blob {{ opacity: {t["blob_opacity"]}; transform-box: fill-box; transform-origin: center; }}
    .b1 {{ animation: drift1 16s ease-in-out infinite alternate; }}
    .b2 {{ animation: drift2 20s ease-in-out infinite alternate; }}
    .b3 {{ animation: drift3 18s ease-in-out infinite alternate; }}
    @keyframes drift1 {{ to {{ transform: translate(120px, 30px) scale(1.15); }} }}
    @keyframes drift2 {{ to {{ transform: translate(-140px, -20px) scale(0.9); }} }}
    @keyframes drift3 {{ to {{ transform: translate(60px, -40px) scale(1.2); }} }}
    .cursor {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .fade {{ opacity: 0; animation: fadein 0.9s ease-out forwards; }}
    .d1 {{ animation-delay: 0.1s; }} .d2 {{ animation-delay: 0.45s; }} .d3 {{ animation-delay: 0.8s; }}
    @keyframes fadein {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    {REDUCED_MOTION}
    @media (prefers-reduced-motion: reduce) {{ .fade {{ opacity: 1; }} }}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="url(#bg)"/>
    <g filter="url(#blur)">
      <circle class="blob b1" cx="150" cy="60" r="110" fill="{t["accent_a"]}"/>
      <circle class="blob b2" cx="760" cy="170" r="120" fill="{t["accent_b"]}"/>
      <circle class="blob b3" cx="520" cy="20" r="80" fill="{t["accent_a"]}"/>
    </g>
    <rect width="{w}" height="{h}" fill="url(#dots)"/>
    <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="18" fill="none" stroke="{t["border"]}" stroke-opacity="0.8"/>
    <g font-family="{MONO}" font-size="16" fill="{t["muted"]}" class="fade d1">
      <text x="56" y="70">~/alekseyiovchev <tspan fill="{t["accent_b"]}">$</tspan> whoami<tspan class="cursor" fill="{t["accent_a"]}"> ▍</tspan></text>
    </g>
    <text x="54" y="132" font-family="{FONT}" font-size="54" font-weight="700" fill="url(#name)" class="fade d2">Oleksii Iovchev</text>
    <text x="57" y="175" font-family="{FONT}" font-size="20" fill="{t["text"]}" class="fade d3">Backend Lead <tspan fill="{t["muted"]}">·</tspan> Python <tspan fill="{t["muted"]}">·</tspan> Distributed systems <tspan fill="{t["muted"]}">·</tspan> a bit of Rust</text>
  </g>
</svg>
"""


def divider(t: dict[str, str]) -> str:
    w, h = 900, 12
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="presentation">
  <defs>
    <linearGradient id="base" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t["accent_a"]}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{t["accent_a"]}" stop-opacity="0.45"/>
      <stop offset="1" stop-color="{t["accent_b"]}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="glow" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t["accent_b"]}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{t["accent_b"]}"/>
      <stop offset="1" stop-color="{t["accent_a"]}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .run {{ animation: run 5s cubic-bezier(.45,0,.55,1) infinite; }}
    @keyframes run {{ from {{ transform: translateX(-200px); }} to {{ transform: translateX({w}px); }} }}
    {REDUCED_MOTION}
  </style>
  <rect x="0" y="5" width="{w}" height="2" rx="1" fill="url(#base)"/>
  <rect class="run" x="0" y="4.5" width="200" height="3" rx="1.5" fill="url(#glow)"/>
</svg>
"""


def _chip_width(label: str) -> float:
    return len(label) * 6.9 + 20


def project_card(t: dict[str, str], p: dict) -> str:
    lines = textwrap.wrap(p["desc"], width=60)[:4]
    rows = max(min(len(textwrap.wrap(q["desc"], width=60)), 4) for q in PROJECTS)  # same height for all cards
    chips_y = 76 + (rows - 1) * 19 + 16
    w, h = 440, chips_y + 20 + 20
    desc = "\n".join(
        f'    <text x="24" y="{76 + i * 19}">{escape(line)}</text>' for i, line in enumerate(lines)
    )
    chips, x = [], 24.0
    for label in p["chips"]:
        cw = _chip_width(label)
        chips.append(
            f'    <g transform="translate({x:.1f} {chips_y})">'
            f'<rect width="{cw:.1f}" height="20" rx="10" fill="{t["chip_bg"]}"/>'
            f'<text x="{cw / 2:.1f}" y="14" text-anchor="middle">{escape(label)}</text></g>'
        )
        x += cw + 6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(p["title"])}">
  <defs>
    <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{t["accent_a"]}"/>
      <stop offset="1" stop-color="{t["accent_b"]}"/>
    </linearGradient>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="12"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="{t["card_bg"]}"/>
    <rect width="4" height="{h}" fill="url(#bar)"/>
  </g>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="none" stroke="{t["border"]}"/>
  <g transform="translate(24 24)" fill="{t["muted"]}">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"/>
  </g>
  <text x="48" y="37" font-family="{FONT}" font-size="17" font-weight="600" fill="{t["title"]}">{escape(p["title"])}</text>
  <g font-family="{FONT}" font-size="13" fill="{t["text"]}">
{desc}
  </g>
  <g font-family="{FONT}" font-size="11.5" font-weight="600" fill="{t["chip_text"]}">
{chr(10).join(chips)}
  </g>
</svg>
"""


FLOW_NODES = ["request", "api", "queue", "worker", "db"]


def flow(t: dict[str, str]) -> str:
    """A request travelling api -> queue -> worker -> db, with a retry loop back to the queue.

    One packet runs the whole chain in CYCLE seconds; each node lights up as the packet
    passes it, and a second packet takes the retry loop worker -> queue.
    """
    w, h, cx, nw, nh, top, step, cycle = 300, 392, 130, 150, 36, 52, 70, 5
    centers = [top + nh / 2 + i * step for i in range(len(FLOW_NODES))]
    first, last = centers[0], centers[-1]
    nodes, edges = [], []
    for i, (label, cy) in enumerate(zip(FLOW_NODES, centers, strict=True)):
        delay = cycle * (cy - first) / (last - first) * 0.8
        nodes.append(
            f'  <rect class="node" style="animation-delay:{delay:.2f}s" x="{cx - nw / 2}" y="{cy - nh / 2}" '
            f'width="{nw}" height="{nh}" rx="10" fill="{t["card_bg"]}" stroke="{t["border"]}" stroke-width="1.5"/>\n'
            f'  <text x="{cx}" y="{cy + 5}" text-anchor="middle">{label}</text>'
        )
        if i:
            edges.append(f'M{cx} {centers[i - 1] + nh / 2} V{cy - nh / 2}')
    queue_y, worker_y = centers[2], centers[3]
    right = cx + nw / 2
    loop = f"M{right} {worker_y} H{right + 22} Q{right + 38} {worker_y} {right + 38} {worker_y - 16} V{queue_y + 16} Q{right + 38} {queue_y} {right + 22} {queue_y} H{right + 6}"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="request, api, queue, worker, db: at-least-once delivery with retries, idempotent write">
  <defs>
    <pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="{t["dot"]}" opacity="0.45"/>
    </pattern>
    <marker id="arrow" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M0 0 L8 4 L0 8 z" fill="{t["accent_a"]}"/>
    </marker>
    <clipPath id="frame"><rect width="{w}" height="{h}" rx="16"/></clipPath>
  </defs>
  <style>
    .node {{ animation: hit {cycle * 0.8 + 1:.1f}s linear infinite; }}
    @keyframes hit {{ 0% {{ stroke: {t["accent_b"]}; }} 14% {{ stroke: {t["border"]}; }} 100% {{ stroke: {t["border"]}; }} }}
    .ok {{ animation: ok {cycle * 0.8 + 1:.1f}s ease-out infinite; animation-delay: {cycle * 0.8:.2f}s; opacity: 0.35; }}
    @keyframes ok {{ 0% {{ opacity: 1; }} 60% {{ opacity: 1; }} 100% {{ opacity: 0.35; }} }}
    {REDUCED_MOTION}
  </style>
  <g clip-path="url(#frame)">
    <rect width="{w}" height="{h}" fill="{t["card_bg"]}"/>
    <rect width="{w}" height="{h}" fill="url(#dots)"/>
  </g>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="{t["border"]}"/>
  <text x="20" y="30" font-family="{MONO}" font-size="11" fill="{t["muted"]}"># life of a request</text>
  <path d="{" ".join(edges)}" stroke="{t["border"]}" stroke-width="2" fill="none"/>
  <path id="loop" d="{loop}" stroke="{t["accent_a"]}" stroke-width="1.5" stroke-dasharray="4 4" fill="none" marker-end="url(#arrow)" opacity="0.8"/>
  <circle r="4.5" fill="{t["accent_b"]}">
    <animateMotion dur="{cycle * 0.8 + 1:.1f}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;{cycle * 0.8 / (cycle * 0.8 + 1):.3f};1" calcMode="linear" path="M{cx} {first} V{last}"/>
  </circle>
  <circle r="4" fill="{t["accent_a"]}">
    <animateMotion dur="{cycle * 0.8 + 1:.1f}s" begin="{cycle * 0.8 * 0.75:.2f}s" repeatCount="indefinite" keyPoints="0;1;1" keyTimes="0;0.35;1" calcMode="linear"><mpath href="#loop"/></animateMotion>
  </circle>
  <g font-family="{MONO}" font-size="14" font-weight="600" fill="{t["text"]}">
{chr(10).join(nodes)}
  </g>
  <g font-family="{MONO}" font-size="10.5" fill="{t["accent_a"]}">
    <text x="{right + 46}" y="{(queue_y + worker_y) / 2 - 3}">retry</text>
    <text x="{right + 46}" y="{(queue_y + worker_y) / 2 + 11}">+jitter</text>
  </g>
  <text x="{cx + 8}" y="{(queue_y + worker_y) / 2 + 4}" font-family="{MONO}" font-size="10" fill="{t["muted"]}">at-least-once</text>
  <text class="ok" x="{right + 10}" y="{last + 5}" font-family="{MONO}" font-size="10.5" font-weight="600" fill="{t["accent_b"]}">✓ idempotent</text>
</svg>
"""


# Decorative, hand-set shares (not computed from the GitHub API).
LANGUAGES = [
    ("Python", 75, "#3572a5"),
    ("JavaScript", 15, "#f1e05a"),
    ("Rust", 10, "#f46623"),
]

# (service, status label, level) — level picks the dot colour.
STATUS = [
    ("idempotent handlers", "operational", "ok"),
    ("observability", "operational", "ok"),
    ("migrations", "forward-only", "ok"),
    ("load tests · k6", "passing", "ok"),
    ("rust", "learning", "warn"),
    ("friday deploys", "disabled", "off"),
]

LEVELS = {
    "light": {"ok": "#1a7f37", "warn": "#9a6700", "off": "#cf222e"},
    "dark": {"ok": "#3fb950", "warn": "#d29922", "off": "#f85149"},
}

PANEL_W, PANEL_H = 440, 236


def _panel(t: dict[str, str], title: str, subtitle: str, body: str, style: str = "") -> str:
    w, h = PANEL_W, PANEL_H
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
  <defs><clipPath id="frame"><rect width="{w}" height="{h}" rx="12"/></clipPath></defs>
  <style>
    {style}
    {REDUCED_MOTION}
  </style>
  <rect width="{w}" height="{h}" rx="12" fill="{t["card_bg"]}" clip-path="url(#frame)"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="none" stroke="{t["border"]}"/>
  <text x="24" y="38" font-family="{FONT}" font-size="17" font-weight="600" fill="{t["title"]}">{escape(title)}</text>
  <text x="24" y="58" font-family="{MONO}" font-size="11" fill="{t["muted"]}">{escape(subtitle)}</text>
{body}
</svg>
"""


def languages(t: dict[str, str]) -> str:
    bar_x, bar_y, bar_w = 24, 78, PANEL_W - 48
    track_x, track_w = 130, PANEL_W - 24 - 48 - 130
    segs, rows, x = [], [], float(bar_x)
    for i, (name, pct, color) in enumerate(LANGUAGES):
        sw = bar_w * pct / 100
        segs.append(f'    <rect x="{x:.1f}" y="{bar_y}" width="{sw:.1f}" height="10" fill="{color}"/>')
        x += sw
        y = 126 + i * 38
        fill_w = track_w * pct / 100
        shimmer = ' fill="url(#shine)"' if name == "Rust" else ""
        row = [
            f'  <circle cx="30" cy="{y - 4}" r="5" fill="{color}"/>',
            f'  <text x="44" y="{y}" fill="{t["text"]}">{name}</text>',
            f'  <rect x="{track_x}" y="{y - 8}" width="{track_w}" height="8" rx="4" fill="{t["border"]}" opacity="0.6"/>',
            f'  <rect x="{track_x}" y="{y - 8}" width="{fill_w:.1f}" height="8" rx="4" fill="{color}"/>',
        ]
        if shimmer:
            row.append(f'  <rect x="{track_x}" y="{y - 8}" width="{fill_w:.1f}" height="8" rx="4"{shimmer}/>')
        row.append(f'  <text x="{PANEL_W - 24}" y="{y}" text-anchor="end" fill="{t["muted"]}">{pct}%</text>')
        rows.append("\n".join(row))
    body = f"""  <defs>
    <clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="10" rx="5"/></clipPath>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0" spreadMethod="repeat">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="-1 0" to="1 0" dur="2.4s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <g clip-path="url(#bar)">
{chr(10).join(segs)}
  </g>
  <g font-family="{FONT}" font-size="14" font-weight="500">
{chr(10).join(rows)}
  </g>"""
    return _panel(t, "Languages", "# what my keyboard types most", body)


def status_page(t: dict[str, str]) -> str:
    lv = LEVELS["light" if t is THEMES["light"] else "dark"]
    rows = []
    for i, (service, label, level) in enumerate(STATUS):
        y = 88 + i * 22
        rows.append(
            f'  <text x="24" y="{y}" fill="{t["text"]}">{escape(service)}</text>'
            f'<circle class="dot {level}" cx="{PANEL_W - 24 - len(label) * 7 - 12}" cy="{y - 4}" r="4" fill="{lv[level]}"/>'
            f'<text x="{PANEL_W - 24}" y="{y}" text-anchor="end" fill="{lv[level]}">{escape(label)}</text>'
        )
    # 45 days of "uptime"; the one amber bar is that Friday.
    bars = []
    n, gap = 45, 2
    bw = (PANEL_W - 48 - gap * (n - 1)) / n
    for i in range(n):
        color = lv["warn"] if i == 31 else lv["ok"]
        bars.append(f'    <rect x="{24 + i * (bw + gap):.1f}" y="{PANEL_H - 30}" width="{bw:.1f}" height="14" rx="1.5" fill="{color}" opacity="0.85"/>')
    pill_w = 96
    body = f"""  <g transform="translate({PANEL_W - 24 - pill_w} 22)">
    <rect width="{pill_w}" height="22" rx="11" fill="{lv["ok"]}" opacity="0.14"/>
    <circle class="dot ok" cx="14" cy="11" r="4" fill="{lv["ok"]}"/>
    <text x="{pill_w / 2 + 8}" y="15" text-anchor="middle" font-family="{FONT}" font-size="11.5" font-weight="600" fill="{lv["ok"]}">all good</text>
  </g>
  <g font-family="{MONO}" font-size="12.5">
{chr(10).join(rows)}
  </g>
{chr(10).join(bars)}"""
    style = (
        ".dot { transform-box: fill-box; transform-origin: center; }\n"
        "    .ok { animation: pulse 2.4s ease-in-out infinite; }\n"
        "    .warn { animation: pulse 1.1s ease-in-out infinite; }\n"
        "    @keyframes pulse { 50% { opacity: .35; transform: scale(.75); } }"
    )
    return _panel(t, "status.alekseyiovchev", "# uptime of the things I care about", body, style)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    for name, t in THEMES.items():
        (ASSETS / f"banner-{name}.svg").write_text(banner(t), encoding="utf-8")
        (ASSETS / f"flow-{name}.svg").write_text(flow(t), encoding="utf-8")
        (ASSETS / f"languages-{name}.svg").write_text(languages(t), encoding="utf-8")
        (ASSETS / f"status-{name}.svg").write_text(status_page(t), encoding="utf-8")
        (ASSETS / f"divider-{name}.svg").write_text(divider(t), encoding="utf-8")
        for p in PROJECTS:
            (ASSETS / f"card-{p['slug']}-{name}.svg").write_text(project_card(t, p), encoding="utf-8")
    print(f"written to {ASSETS}")


if __name__ == "__main__":
    main()
