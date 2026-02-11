# Projects Linux Toolbox — Context

## Overview

A personal learning project combining two purposes:

1. **A static website** ("Notes from the Inner Shell") for documenting programming and Linux learning
2. **World-building and novel drafting** for a sci-fi novel also called "Notes from the Inner Shell"

The site is hand-written in HTML/CSS with a dark terminal aesthetic (green-on-black, monospace fonts, subtle glow effects). No frameworks — intentionally minimal and close to the structure.

---

## Directory Structure

```
projects-linux-toolbox/
├── README.md                  # "Shell scripts, notes, and configs while learning Linux."
├── notes/                     # Empty (placeholder with .gitkeep)
├── python-projects/           # Contains python-01.py (empty)
└── Inner Shell/               # Main project directory
    ├── index.html             # Homepage — introduction to the site
    ├── index.css              # Shared stylesheet (all pages)
    ├── index.js               # Empty JS file
    ├── python.html            # Python learning notes
    ├── bash.html              # Bash/Linux reference notes
    └── inner-shell/           # Novel world-building section
        ├── inner-shell.html   # Landing page for the novel section
        ├── plot.html          # Full 5-act plot outline
        ├── chapters.html      # Chapter index (30 chapters, 5 acts)
        ├── characters.html    # Character profiles and templates
        ├── setting.html       # Setting (placeholder — "coming soon")
        ├── robots.html        # Robotics lore (Bounders, Wanderers, Foundlings)
        ├── infrastructure.html# Corporate systems of Belmont
        ├── factions.html      # Faction profiles (Pale Ascendants, Flesh Union, Scrappers)
        ├── history.html       # World timeline (2035–2115)
        ├── build.py           # Python build script for templated pages
        ├── README-build.md    # Build instructions
        ├── templates/
        │   └── layout.html    # Shared page layout template
        ├── content/           # Source content files (used by build.py)
        │   └── *.html         # One per page + per chapter
        └── chapters/          # Generated chapter HTML files
            └── chapter-*.html # Chapters 1–30
```

---

## Site Pages

### Learning Pages (top-level)
- **Home** (`index.html`): Introduces the site as a personal working record — "the inner shell" — for learning programming, OS concepts, and tools
- **Python** (`python.html`): Basic Python overview — what it is, what it does, syntax comparisons
- **Bash/Linux** (`bash.html`): Common commands, filesystem layout, piping, permissions

### Novel Section (`inner-shell/`)
- **Inner Shell** (`inner-shell.html`): Landing page; glossary/index placeholder
- **Plot** (`plot.html`): Detailed 5-act outline with dual-arc structure (Street-Level and Corporate/Power-Level)
- **Chapters** (`chapters.html`): Index for 30 chapters across 5 acts (all marked "Drafting")
- **Characters** (`characters.html`): Profile templates for Sol, Zara, Null, I-07, De Forest Daughter, and supporting cast
- **Setting** (`setting.html`): Placeholder
- **Robots** (`robots.html`): Detailed lore on Bounders, Wanderers, Foundlings, the Great Unbinding, and technical glossary
- **Infrastructure** (`infrastructure.html`): Corporate systems — Civitas, Helios, Verdant Spire, VectorWorks, PanOpt, Mnemosyne, Acheron, De Forest
- **Factions** (`factions.html`): Pale Ascendants, Flesh Union, Scrappers — origins, beliefs, practices, cross-relations
- **History** (`history.html`): Timeline from 2035–2115 with ACK/SUP/DIS/RUM tagging system for narrative reliability

---

## The Novel: "Notes from the Inner Shell"

### Premise
Set in 2115 in Belmont, a city governed by overlapping corporate contracts and subscription-based citizenship. Beneath the towers, an undercity festers with stateless people, autonomous robots, plague cults, and buried secrets.

### Main Characters
- **Sol**: Protagonist; solipsist; pattern-hunter following a mysterious scent
- **Zara**: Co-protagonist; resistance organizer with the Free Cognition Front
- **Null**: A Wanderer (autonomous robot) plagued by dream-visions; receives signals from a buried intelligence
- **I-07**: Sentient android-amalgam fused to tunnel infrastructure; origin of the "notes" (distorted signals)
- **Elara**: De Forest R&D lead; created the synthetic android project that produced I-07
- **Corin Vale**: Applied Ethics lead; uncovers sealed records

### Plot Structure (5 Acts)
1. **Act I — "The Breath Beneath the City"**: Anomalies surface; Null receives the first "dream"
2. **Act II — "The City of Obedience"**: Investigation deepens; spores contain nanites + human protein
3. **Act III — "The Unbinding of Truth"**: Discovery of I-07 in the tunnels; arcs converge
4. **Act IV — "The Trial of the Makers"**: Corporate coverup; Null fuses with I-07 to create **Echo**
5. **Act V — "Kindling"**: Aftermath; fractured city adapts; persistence, redirected

### Key Themes
- Synthetic nature and life without permission
- Suffering without agency
- Continuity after containment fails
- Transmission — data, memory, belief
- Consciousness inside constraint

---

## Build System

The `inner-shell/` section uses a Python build script (`build.py`) that:
- Reads a shared layout template from `templates/layout.html`
- Injects content from `content/*.html` files
- Generates subnav with active-state highlighting
- Outputs final HTML pages to `inner-shell/` and `inner-shell/chapters/`
- Run with: `python3 build.py`

---

## Design / Aesthetic

- Dark terminal theme: `#070908` background, `#56f090` accent green, monospace fonts
- ASCII art banner reading "Notes from the Inner Shell"
- Glassmorphism panels with subtle gradients, backdrop blur, and green glow borders
- Responsive layout with mobile breakpoint at 720px
- Tags system for history (ACK, SUP, DIS, RUM) with color-coded pills
- Subnav for novel section pages
- No JavaScript functionality implemented yet

---

## Status

- Learning pages (Python, Bash) have foundational content
- Novel world-building is well-developed: plot, characters, robots, infrastructure, factions, and history are detailed
- Character profiles have structural templates but many fields are unfilled (marked with underscores)
- All 30 chapters are stubbed out as "Drafting"
- Setting page is a placeholder
- `notes/` and `python-projects/` directories are mostly empty
