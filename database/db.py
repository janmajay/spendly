import sqlite3
from flask import g, current_app
from werkzeug.security import generate_password_hash


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT    NOT NULL,
            email         TEXT    NOT NULL UNIQUE,
            password_hash TEXT    NOT NULL,
            created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS expenses (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL REFERENCES users(id),
            title      TEXT    NOT NULL,
            amount     REAL    NOT NULL,
            category   TEXT,
            date       TEXT    NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    db.commit()


def create_user(name, email, password):
    db = get_db()
    db.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        (name, email, generate_password_hash(password)),
    )
    db.commit()


def seed_db():
    db = get_db()

    db.execute(
        "INSERT OR IGNORE INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Nitish Kumar", "nitish@example.com", generate_password_hash("password123")),
    )
    db.execute(
        "INSERT OR IGNORE INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Priya Sharma", "priya@example.com", generate_password_hash("password123")),
    )
    db.commit()

    user = db.execute("SELECT id FROM users WHERE email = 'nitish@example.com'").fetchone()
    if user:
        uid = user["id"]
        sample_expenses = [
            (uid, "Grocery run",       45.50,  "Food",          "2026-04-10"),
            (uid, "Metro card top-up", 20.00,  "Transport",     "2026-04-12"),
            (uid, "Netflix",           15.99,  "Entertainment", "2026-04-14"),
            (uid, "Coffee shop",        4.75,  "Food",          "2026-04-16"),
        ]
        db.executemany(
            "INSERT INTO expenses (user_id, title, amount, category, date) VALUES (?, ?, ?, ?, ?)",
            sample_expenses,
        )
        db.commit()
