# Day 56 of 100 Days of Code Challenge
# Virtual Business Card

# This day involved learning how to incorperate html and css style sheets into flask, 
# first testing with previous html/css projects, then looking at using free online resources. I did not upload all of the resources from the online template
# as there were a lot

# Checkout the preview image to see what it looks like

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def greet():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
