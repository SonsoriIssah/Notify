# Notify — Project Planning

## Description
Notify is a CRUD-based notes app that stores text directly in a SQLite database and allows users to create, read, update, and delete notes through a web interface.

---

## Data Model

### Table: `Note`

| Column      | Type    | Description                        |
|-------------|---------|------------------------------------|
| `id`        | INTEGER | Primary key, auto-incremented      |
| `file_name` | TEXT    | Title/name of the note             |
| `content`   | TEXT    | Full text content of the note      |

---

## Routes

| Route           | Method | Description                                              |
|-----------------|--------|----------------------------------------------------------|
| `/`             | GET    | Home page — display list of all notes with delete buttons |
| `/create`       | POST     shows a form with file_name and content fields`    |
| `/edit/<id>`    | GET    | Open a note — display its content in an editable page    |
| `/save/<id>`    | POST   | Save updated note content, redirect back to `/`          |
| `/delete/<id>`  | POST   | Delete a note from the database, redirect back to `/`    |

---

## Pages (HTML Templates)

| Template        | Description                                              |
|-----------------|----------------------------------------------------------|
| `home.html`     | Lists all notes, input to create new note, delete buttons |
| `edit.html`     | Text area to edit note content, save button, back button  |

---

## User Flow

1. User lands on `/` — sees list of existing notes and a "create new note" input
2. User types a note name and clicks Create → POST to `/create` → redirects to `/`
3. New note appears in the list on home page
4. User clicks a note name → GET `/edit/<id>` → opens edit page with note content
5. User edits text and clicks Save → POST to `/save/<id>` → redirects to `/`
6. User clicks Delete next to a note → POST to `/delete/<id>` → redirects to `/`
7. User clicks Back on edit page → redirects to `/`

---

## Tech Stack

| Layer      | Tool              |
|------------|-------------------|
| Backend    | Flask (Python)    |
| Database   | SQLite            |
| ORM        | Flask-SQLAlchemy  |
| Frontend   | HTML + Jinja2     |
| Dev server | Flask built-in    |

---

## Imports Needed

```python
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
```

---

## Notes
- Pattern used: POST-Redirect-GET (submit data → redirect → display updated page)
- No deployment for now — localhost only
- No user authentication — single user app
- Content stored directly as TEXT in SQLite (no file storage on disk)