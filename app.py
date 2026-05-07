from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///notes.db"

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    file_name = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable = True)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    notes = Note.query.all()
    return render_template('home.html',notes = notes)

@app.route('/create',methods = ['GET', 'POST'])
def create():
    if request.method =='POST':
        file_name = request.form['file_name']
        content = request.form['content']
        new = Note(file_name=file_name,content = content)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('edit',id = new.id))
    else:
        return render_template('create.html')
    
@app.route('/edit/<id>')
def edit(id):
    notes = Note.query.get(id)
    return render_template('edit.html',notes = notes)

@app.route('/save/<id>', methods = ['GET','POST'])
def save(id):
    if request.method == 'POST':
        note = Note.query.get(id)
        note.file_name = request.form['file_name']
        note.content = request.form['content']
        db.session.commit()
        return redirect(url_for('edit', id = id))
    else:
        return redirect(url_for('edit', id = id))
    
@app.route('/delete/<id>', methods = ['GET','POST'])
def delete(id):
    if request.method == 'POST':
        note = Note.query.get(id)
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))