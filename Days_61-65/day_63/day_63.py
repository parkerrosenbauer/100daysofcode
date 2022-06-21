# Day 63 of 100 Days of Code Challenge
# Personal Library tracker
# Displays a list of books and their ratings, storing the books in a sqlite database
# Allows users to add new books, edit their ratings, and delete books from the library

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title


db.create_all()


@app.route('/')
def home():
    return render_template('index.html', books=db.session.query(Book).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(title=request.form["title"].title(),
                    author=request.form["author"].title(),
                    rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    book = Book.query.get(index)
    if request.method == "POST":
        book.rating = request.form["new-rating"]
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=book)


@app.route("/delete/<int:index>", methods=["POST", "GET"])
def delete(index):
    book_to_delete = Book.query.get(index)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
