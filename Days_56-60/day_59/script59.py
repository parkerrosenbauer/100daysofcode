# Day 59 of 100 Days of Code Challenge
# Improved Blog Website
# This website is based off a free theme found at: https://startbootstrap.com/previews/clean-blog
# A preview of the website can be seen in the preview image file in the folder
# Note, the static files weren't uploaded for this project

"""
Accomplished tasks:
- Integrated the website template to best fit the needs of the project
- Separated the header and footer into separate files to easily edit either across all pages
- Adjusted the website to personalize it with html
- Imported blog posts and used Jinja to dynamically insert them into the html
"""

from flask import Flask, render_template
import requests

URL = "https://api.npoint.io/743f42c2d701b97ee0f7"
r = requests.get(URL)
all_posts = r.json()
app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template('index.html', posts=all_posts)


@app.route('/about.html')
def get_about():
    return render_template('about.html')


@app.route('/contact.html')
def get_contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def show_post(index):
    chosen_post = None
    for post in all_posts:
        if post['id'] == index:
            chosen_post = post
    return render_template("post.html", post=chosen_post)


if __name__ == "__main__":
    app.run(debug=True)
