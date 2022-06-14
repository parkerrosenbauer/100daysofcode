# Day 56 of 100 Days of Code Challenge
# Virtual Business Card
# Checkout the preview image to see what it looks like

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def greet():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

