# Day 66 of 100 Days of Code
# Creating a REST API

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)
API_KEY = "TopSecretAPIKey"

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def make_cafe_json(c):
    cafe = jsonify(can_take_calls=c.can_take_calls,
                   coffee_price=c.coffee_price,
                   has_sockets=c.has_sockets,
                   has_toilet=c.has_toilet,
                   has_wifi=c.has_wifi,
                   id=c.id,
                   img_url=c.img_url,
                   location=c.location,
                   map_url=c.map_url,
                   name=c.name,
                   seats=c.seats)
    return cafe


@app.route("/")
def home():
    return "<h1>Welcome to the Cafe & Wifi API</h1>"


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    query = db.session.query(Cafe).all()
    rand_cafe = choice(query)
    cafe_json = jsonify(cafe=make_cafe_json(rand_cafe).json)
    return cafe_json


@app.route("/all")
def all_cafes():
    query = db.session.query(Cafe).all()
    cs = [make_cafe_json(cafe).json for cafe in query]
    cafes = jsonify(cafes=cs)
    return cafes


@app.route("/search")
def search_cafes():
    location = request.args.get("loc").title()
    query = db.session.query(Cafe).all()
    cs = [make_cafe_json(cafe).json for cafe in query if cafe.location == location]
    if len(cs) == 0:
        msg = {"Not Found": "Sorry, we don't have a cafe at that location."}
        return jsonify(error=msg)
    cafes = jsonify(cafes=cs)
    return cafes


# HTTP POST - Create Record
def str_to_bool(v):
    if v in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False


@app.route("/add", methods=["GET", "POST"])
def add_a_cafe():
    new_cafe = Cafe(name=request.form["name"],
                    map_url=request.form["map_url"],
                    img_url=request.form["img_url"],
                    location=request.form["location"],
                    seats=request.form["seats"],
                    has_toilet=str_to_bool(request.form["has_toilet"]),
                    has_wifi=str_to_bool(request.form["has_wifi"]),
                    has_sockets=str_to_bool(request.form["has_sockets"]),
                    can_take_calls=str_to_bool(request.form["can_take_calls"]),
                    coffee_price=request.form["coffee_price"]
                    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price", methods=["PATCH", "POST"])
def update_price():
    index = request.args.get("id")
    coffee_to_update = Cafe.query.get(index)
    if coffee_to_update:
        coffee_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    else:
        msg = {"Not Found": "Sorry a cafe with that id was not found in the database."}
        return jsonify(error=msg)


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE", "POST"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") == API_KEY:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            Cafe.query.filter_by(id=cafe_id).delete()
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe"})
        else:
            msg = {"Not Found": "Sorry a cafe with that id was not found in the database."}
            return jsonify(error=msg), 404
    else:
        return jsonify(response={"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
