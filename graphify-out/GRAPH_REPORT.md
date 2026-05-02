# Graph Report - .  (2026-04-19)

## Corpus Check
- Corpus is ~2,199 words - fits in a single context window. You may not need a graph.

## Summary
- 49 nodes · 53 edges · 9 communities detected
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Flask Route Handlers|Flask Route Handlers]]
- [[_COMMUNITY_Landing & Auth Pages|Landing & Auth Pages]]
- [[_COMMUNITY_Layout & Design System|Layout & Design System]]
- [[_COMMUNITY_App Config & Dependencies|App Config & Dependencies]]
- [[_COMMUNITY_Database Layer|Database Layer]]
- [[_COMMUNITY_DB Docs & Roadmap|DB Docs & Roadmap]]
- [[_COMMUNITY_Database Package Init|Database Package Init]]
- [[_COMMUNITY_Frontend JavaScript|Frontend JavaScript]]
- [[_COMMUNITY_Werkzeug Dependency|Werkzeug Dependency]]

## God Nodes (most connected - your core abstractions)
1. `base.html (Base Layout Template)` - 8 edges
2. `Landing Page` - 7 edges
3. `database/db.py (SQLite helpers)` - 5 edges
4. `Register Page (Create Account)` - 5 edges
5. `Spendly Application` - 4 edges
6. `Privacy Policy Page` - 4 edges
7. `get_db()` - 3 edges
8. `app.py (Flask entry point)` - 3 edges
9. `Google Fonts (DM Serif Display + DM Sans)` - 3 edges
10. `Terms and Conditions Page` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Spendly Application` --conceptually_related_to--> `Landing Page`  [INFERRED]
  CLAUDE.md → templates/landing.html
- `base.html (Base Layout Template)` --references--> `static/css/style.css (global design system)`  [EXTRACTED]
  templates/base.html → CLAUDE.md
- `Landing Page` --references--> `static/css/landing.css`  [EXTRACTED]
  templates/landing.html → CLAUDE.md
- `Google Fonts (DM Serif Display + DM Sans)` --conceptually_related_to--> `Design Tokens (CSS Variables)`  [INFERRED]
  templates/base.html → CLAUDE.md
- `Spendly Application` --references--> `flask==3.1.3`  [EXTRACTED]
  CLAUDE.md → requirements.txt

## Hyperedges (group relationships)
- **Authentication Flow (Register + Login + app.py routes)** — register_registerform, login_loginform, claudemd_apppy [EXTRACTED 0.95]
- **Legal Pages (Terms + Privacy linked from Footer)** — terms_termsconditions, privacy_privacypolicy, base_footer [EXTRACTED 0.95]
- **Landing Page Conversion Path (Hero + CTA -> Register)** — landing_herosection, landing_ctasection, register_registerpage [INFERRED 0.85]

## Communities

### Community 0 - "Flask Route Handlers"
Cohesion: 0.18
Nodes (0): 

### Community 1 - "Landing & Auth Pages"
Cohesion: 0.24
Nodes (10): Navbar Component, static/css/landing.css, CTA Section, Demo Video Modal (YouTube), Features Section, Hero Section (hero2), Landing Page, Modal JS (open/close logic) (+2 more)

### Community 2 - "Layout & Design System"
Cohesion: 0.39
Nodes (8): base.html (Base Layout Template), Footer Component, Google Fonts (DM Serif Display + DM Sans), static/js/main.js, Design Tokens (CSS Variables), static/css/style.css (global design system), Privacy Policy Page, Terms and Conditions Page

### Community 3 - "App Config & Dependencies"
Cohesion: 0.29
Nodes (7): app.py (Flask entry point), Spendly Application, Login Form (POST /login), Register Form (POST /register), flask==3.1.3, pytest==8.3.5, pytest-flask==1.3.0

### Community 4 - "Database Layer"
Cohesion: 0.6
Nodes (3): get_db(), init_db(), seed_db()

### Community 5 - "DB Docs & Roadmap"
Cohesion: 0.4
Nodes (2): database/db.py (SQLite helpers), Implementation Roadmap (Steps 1-9)

### Community 6 - "Database Package Init"
Cohesion: 1.0
Nodes (0): 

### Community 7 - "Frontend JavaScript"
Cohesion: 1.0
Nodes (0): 

### Community 8 - "Werkzeug Dependency"
Cohesion: 1.0
Nodes (1): werkzeug==3.1.6

## Knowledge Gaps
- **9 isolated node(s):** `werkzeug==3.1.6`, `pytest==8.3.5`, `static/css/landing.css`, `Implementation Roadmap (Steps 1-9)`, `static/js/main.js` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Database Package Init`** (1 nodes): `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Frontend JavaScript`** (1 nodes): `main.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Werkzeug Dependency`** (1 nodes): `werkzeug==3.1.6`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Landing Page` connect `Landing & Auth Pages` to `Layout & Design System`, `App Config & Dependencies`?**
  _High betweenness centrality (0.239) - this node is a cross-community bridge._
- **Why does `Spendly Application` connect `App Config & Dependencies` to `Landing & Auth Pages`, `DB Docs & Roadmap`?**
  _High betweenness centrality (0.210) - this node is a cross-community bridge._
- **Why does `base.html (Base Layout Template)` connect `Layout & Design System` to `Landing & Auth Pages`?**
  _High betweenness centrality (0.174) - this node is a cross-community bridge._
- **What connects `werkzeug==3.1.6`, `pytest==8.3.5`, `static/css/landing.css` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._