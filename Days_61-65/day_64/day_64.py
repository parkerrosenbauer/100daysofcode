# Day 64 of 100 Days of Code
# Top 10 Movie List

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'
FIND_MOVIE_URL = 'https://api.themoviedb.org/3/movie/'
IMAGE_URL = 'https://image.tmdb.org/t/p/w500'
MOVIE_DB_KEY = os.environ.get('MOVIE_DB_KEY')
app = Flask(__name__)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


# Create the table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title


db.create_all()


# Edit a movie's rating/review
class EditForm(FlaskForm):
    new_rating = StringField('Rating Out of 10', validators=[DataRequired()])
    new_review = StringField('Movie Review', validators=[DataRequired()])
    submit = SubmitField('Update')


# Search for a new movie to add
class AddForm(FlaskForm):
    add_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


# Home Page
# Edits the rankings of the movies so the highest rated is always rank #1 and the lowest rated is the highest ranking
@app.route("/")
def home():
    query = db.session.query(Movie).order_by(Movie.rating.desc()).all()
    rank = 1
    for movie in query:
        movie.ranking = rank
        rank += 1
    return render_template("index.html", movies=db.session.query(Movie).order_by(Movie.ranking).all())


# Creates the edit form and updates the movie with the new data entered
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    movie = Movie.query.get(index)
    form = EditForm()
    if form.validate_on_submit():
        movie.rating = form.new_rating.data
        movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', title=movie.title, form=form)


# Deletes a movie from the db
@app.route("/delete/<int:index>", methods=["POST", "GET"])
def delete(index):
    movie_to_delete = Movie.query.get(index)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


# Creates the search form and then loads the selection page which shows all movies that came up in the search
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        search_title = form.add_title.data
        movie_params = {"api_key": MOVIE_DB_KEY,
                        "query": search_title}
        r = requests.get(url=SEARCH_URL, params=movie_params)
        movie_data = r.json()["results"]

        # show all titles on screen that have a release date
        db_titles = {}
        for data in movie_data:
            try:
                if data["release_date"] != "":
                    db_titles[data['title']] = {"date": data["release_date"], "id": data["id"]}
            except KeyError:
                pass

        # drop any movies that are already in the database or that don't have a release date
        existing_db_titles = [movie.title for movie in db.session.query(Movie).all()]
        my_titles = {}
        for title, key in db_titles.items():
            if title not in existing_db_titles:
                my_titles[title] = key

        return render_template('select.html', movies=my_titles)
    else:
        return render_template('add.html', form=form)


# Adds the movie of the user's choice to the db
@app.route("/choose-movie/<int:index>", methods=["POST", "GET"])
def choose_movie(index):
    r = requests.get(url=f"{FIND_MOVIE_URL}{index}", params={"api_key": MOVIE_DB_KEY})
    movie_data = r.json()
    new_movie = Movie(title=movie_data["title"],
                      year=int(movie_data["release_date"][:4]),
                      description=movie_data["overview"],
                      rating=0,
                      ranking=0,
                      review="",
                      img_url=f"{IMAGE_URL}{movie_data['poster_path']}")
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', index=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
