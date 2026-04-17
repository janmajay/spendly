# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run development server (http://localhost:5001)
python app.py

# Run tests
pytest

# Run a single test file
pytest tests/test_auth.py

# Install dependencies
pip install -r requirements.txt
```

## Architecture

**Spendly** is a Flask-based expense tracking web app using server-side rendering with Jinja2 templates. There is no JavaScript framework — the frontend is vanilla JS with custom CSS.

**Stack:**
- Backend: Flask (Python), SQLite database
- Frontend: Jinja2 templates, vanilla JS, custom CSS
- Testing: pytest + pytest-flask

**Key files:**
- `app.py` — Flask app entry point; all routes defined here
- `database/db.py` — SQLite helpers: `get_db()`, `init_db()`, `seed_db()` (students implement this in Step 1)
- `templates/base.html` — base layout inherited by all pages
- `static/css/style.css` — global design system (CSS variables for color, typography)
- `static/css/landing.css` — landing page styles

**Routing:** All routes are in `app.py`. Many are placeholder stubs marked with step numbers (Steps 1–9) that correspond to a guided implementation sequence. Forms in `login.html` and `register.html` POST to their respective endpoints, but the handlers are not yet implemented.

**Database:** SQLite, excluded from git (`expense_tracker.db`). The `database/db.py` module is expected to provide a `get_db()` connection (with `row_factory` and foreign keys enabled), `init_db()` for schema creation, and `seed_db()` for dev data.

**Design tokens** (defined as CSS variables in `style.css`): colors use `--ink`, `--paper`, `--accent`, `--danger`; typography uses DM Serif Display (headings) and DM Sans (body).

**Implementation roadmap** (steps referenced in code comments):
1. Database setup (`database/db.py`)
2. Registration
3. Login / logout
4. Profile page
5–6. Dashboard / expense listing
7. Add expense
8. Edit expense
9. Delete expense
