# Notify

A lightweight CRUD notes app built with Flask and SQLAlchemy. Users can create, read, update, and delete notes stored in a local SQLite database.

---

## Features

- Create notes with a title and content
- View all notes on the home page
- Edit existing notes
- Delete notes
- Data persisted in a local SQLite database

---

## Tech Stack

| Layer    | Tool              |
|----------|-------------------|
| Backend  | Python / Flask    |
| Database | SQLite            |
| ORM      | Flask-SQLAlchemy  |
| Frontend | HTML / Jinja2     |

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/notify.git
cd notify
```

**2. Create and activate a virtual environment**
```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
flask --app app run
```

**5. Open in your browser**
```
http://127.0.0.1:5000
```

---

## Project Structure

```
notify/
├── app.py               # Flask app, routes, and database models
├── requirements.txt     # Project dependencies
├── PLANNING.md          # Project planning document
├── LEARNING_NOTES.md    # Flask + SQLAlchemy reference notes
└── templates/
    ├── home.html        # Home page — list of all notes
    ├── create.html      # Create a new note
    └── edit.html        # Edit an existing note
```

---

## Routes

| Route          | Method | Description                  |
|----------------|--------|------------------------------|
| `/`            | GET    | Display all notes            |
| `/create`      | GET    | Show create note form        |
| `/create`      | POST   | Save new note to database    |
| `/edit/<id>`   | GET    | Show edit form for a note    |
| `/save/<id>`   | POST   | Save updated note            |
| `/delete/<id>` | POST   | Delete a note                |

---

## Author

Issah Sonsori Abdul-Wasiu  
BSc Computer Science, KNUST — Class of 2028  
[GitHub](https://github.com/SonsoriIssah)
