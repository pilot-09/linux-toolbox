# Inner Shell Build Script

This folder uses a small Python script to generate the final HTML pages.

## How it works
- **Edit source content:** `content-src/*.md` (main pages) and `content-src/chapters__chapter-#.md` (chapter pages)
- **Edit layout:** `templates/layout.html` (shared header/nav/subnav)
- **Build pages:** `python3 build.py`

The script renders markdown into HTML fragments, injects each page into the shared layout, and writes full HTML pages to:
- `inner-shell/*.html`
- `inner-shell/chapters/chapter-#.html`

It also keeps generated fragments in sync at:
- `content/*.html`

## Typical workflow
1) Edit a markdown file in `content-src/` (or the layout file)
2) Run: `python3 build.py`
3) Open the generated HTML pages

## Notes
- Source of truth for writing is now `content-src/` and `templates/`.
- `content/*.html` and top-level/chapter HTML pages are generated artifacts.
- Legacy fallback: if a markdown source file is missing, `build.py` will read from `content/*.html`.
