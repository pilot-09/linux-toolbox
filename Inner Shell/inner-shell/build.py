from __future__ import annotations

from pathlib import Path

base_dir = Path(__file__).resolve().parent

template_path = base_dir / "templates" / "layout.html"
content_dir = base_dir / "content"

template = template_path.read_text()

subnav_items = [
    {"key": "plot", "label": "Plot", "href": "plot.html"},
    {"key": "chapters", "label": "Chapters", "href": "chapters.html"},
    {"key": "characters", "label": "Characters", "href": "characters.html"},
    {"key": "setting", "label": "Setting", "href": "setting.html"},
    {"key": "technology", "label": "Technology", "href": "technology.html"},
    {"key": "history", "label": "History", "href": "history.html"},
]

pages = [
    {
        "output": base_dir / "inner-shell.html",
        "content": "inner-shell.html",
        "title": "Notes from the Inner Shell",
        "active_subnav": None,
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "plot.html",
        "content": "plot.html",
        "title": "Plot | Notes from the Inner Shell",
        "active_subnav": "plot",
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "chapters.html",
        "content": "chapters.html",
        "title": "Chapters | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "characters.html",
        "content": "characters.html",
        "title": "Characters | Notes from the Inner Shell",
        "active_subnav": "characters",
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "setting.html",
        "content": "setting.html",
        "title": "Setting | Notes from the Inner Shell",
        "active_subnav": "setting",
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "technology.html",
        "content": "technology.html",
        "title": "Technology | Notes from the Inner Shell",
        "active_subnav": "technology",
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "history.html",
        "content": "history.html",
        "title": "History | Notes from the Inner Shell",
        "active_subnav": "history",
        "root": "..",
        "inner_shell_base": ".",
    },
    {
        "output": base_dir / "chapters" / "chapter-1.html",
        "content": "chapters__chapter-1.html",
        "title": "Chapter 1 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-2.html",
        "content": "chapters__chapter-2.html",
        "title": "Chapter 2 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-3.html",
        "content": "chapters__chapter-3.html",
        "title": "Chapter 3 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-4.html",
        "content": "chapters__chapter-4.html",
        "title": "Chapter 4 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-5.html",
        "content": "chapters__chapter-5.html",
        "title": "Chapter 5 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-6.html",
        "content": "chapters__chapter-6.html",
        "title": "Chapter 6 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-7.html",
        "content": "chapters__chapter-7.html",
        "title": "Chapter 7 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-8.html",
        "content": "chapters__chapter-8.html",
        "title": "Chapter 8 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-9.html",
        "content": "chapters__chapter-9.html",
        "title": "Chapter 9 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-10.html",
        "content": "chapters__chapter-10.html",
        "title": "Chapter 10 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-11.html",
        "content": "chapters__chapter-11.html",
        "title": "Chapter 11 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-12.html",
        "content": "chapters__chapter-12.html",
        "title": "Chapter 12 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-13.html",
        "content": "chapters__chapter-13.html",
        "title": "Chapter 13 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-14.html",
        "content": "chapters__chapter-14.html",
        "title": "Chapter 14 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-15.html",
        "content": "chapters__chapter-15.html",
        "title": "Chapter 15 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-16.html",
        "content": "chapters__chapter-16.html",
        "title": "Chapter 16 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-17.html",
        "content": "chapters__chapter-17.html",
        "title": "Chapter 17 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-18.html",
        "content": "chapters__chapter-18.html",
        "title": "Chapter 18 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-19.html",
        "content": "chapters__chapter-19.html",
        "title": "Chapter 19 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-20.html",
        "content": "chapters__chapter-20.html",
        "title": "Chapter 20 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-21.html",
        "content": "chapters__chapter-21.html",
        "title": "Chapter 21 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-22.html",
        "content": "chapters__chapter-22.html",
        "title": "Chapter 22 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-23.html",
        "content": "chapters__chapter-23.html",
        "title": "Chapter 23 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-24.html",
        "content": "chapters__chapter-24.html",
        "title": "Chapter 24 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-25.html",
        "content": "chapters__chapter-25.html",
        "title": "Chapter 25 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-26.html",
        "content": "chapters__chapter-26.html",
        "title": "Chapter 26 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-27.html",
        "content": "chapters__chapter-27.html",
        "title": "Chapter 27 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-28.html",
        "content": "chapters__chapter-28.html",
        "title": "Chapter 28 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-29.html",
        "content": "chapters__chapter-29.html",
        "title": "Chapter 29 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
    {
        "output": base_dir / "chapters" / "chapter-30.html",
        "content": "chapters__chapter-30.html",
        "title": "Chapter 30 | Notes from the Inner Shell",
        "active_subnav": "chapters",
        "root": "../..",
        "inner_shell_base": "..",
    },
]

def indent_content(html: str) -> str:
    lines = html.rstrip().split("\n")
    return "\n".join(("        " + line) if line else "" for line in lines) + "\n"


def build_subnav(active_key: str | None, base: str) -> str:
    links = []
    for item in subnav_items:
        active_class = " class=\"active\"" if item["key"] == active_key else ""
        if base == ".":
            href = item["href"]
        else:
            href = f"{base}/{item['href']}"
        links.append(f"            <a{active_class} href=\"{href}\">{item['label']}</a>")
    links_html = "\n".join(links)
    return f"        <div class=\"subnav\">\n{links_html}\n        </div>"


for page in pages:
    content_path = content_dir / page["content"]
    if not content_path.exists():
        raise FileNotFoundError(f"Missing content file: {content_path}")

    content = indent_content(content_path.read_text())
    subnav = build_subnav(page["active_subnav"], page["inner_shell_base"])

    html = (
        template.replace("{{title}}", page["title"])
        .replace("{{root}}", page["root"])
        .replace("{{innerShellBase}}", page["inner_shell_base"])
        .replace("{{subnav}}", subnav)
        .replace("{{content}}", content)
    )

    page["output"].write_text(html)

print(f"Built {len(pages)} pages.")
