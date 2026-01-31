# Inner Shell Build Script

This folder uses a small Python script to generate the final HTML pages.

## How it works
- **Edit content:** `content/*.html` (main pages) and `content/chapters__chapter-#.html` (chapter pages)
- **Edit layout:** `templates/layout.html` (shared header/nav/subnav)
- **Build pages:** `python3 build.py`

The script injects each content file into the shared layout and writes full HTML pages to:
- `inner-shell/*.html`
- `inner-shell/chapters/chapter-#.html`

## Typical workflow
1) Edit a content file or the layout file
2) Run: `python3 build.py`
3) Open the generated HTML pages

## Notes
- The generated HTML files are the ones you view in the browser.
- If you only want a single source of truth, edit files in `content/` and `templates/` only.
