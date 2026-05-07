# Flask + SQLAlchemy Quick Reference

## Routing
redirect to a named route          → redirect(url_for('home'))
redirect with an id parameter      → redirect(url_for('edit', id=note.id))

## Database Queries
fetch one record by id             → Note.query.get(id)
fetch all records                  → Note.query.all()

## Database Operations
add a new record                   → db.session.add(new_note)
delete a record                    → db.session.delete(note)
save changes to database           → db.session.commit()

## Request Data
get value from a submitted form    → request.form['field_name']
# Flask + SQLAlchemy Learning Notes

## Redirecting to a route with an id
After creating or saving a note, send the user to the edit page for that note.
The id must be passed as a keyword argument.
    return redirect(url_for('edit', id=note.id))

## Fetching a single record from the database
Use .get() when you already have the id. Returns the full object with all columns.
    note = Note.query.get(id)
    note.id / note.file_name / note.content

## Fetching all records
Returns a list of all rows in the table.
    notes = Note.query.all()

## Deleting a record
First fetch the record, then delete it, then commit.
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

## Getting form data
Flask stores submitted form fields in request.form like a dictionary.
The key must match the name="" attribute in your HTML input.
    file_name = request.form['file_name']