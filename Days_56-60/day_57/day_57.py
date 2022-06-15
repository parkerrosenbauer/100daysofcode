# Day 57 of 100 Days of Code Challenge
# Dynamic Blog Page

import requests
from post import Post
from flask import Flask, render_template

URL = "https://api.npoint.io/c790b4d5cab58020d391"
r = requests.get(url=URL)
all_posts = []
for post in r.json():
    post_obj = Post(index=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
    all_posts.append(post_obj)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    chose_post = None
    for one_post in all_posts:
        if one_post.index == index:
            chose_post = one_post
    return render_template("post.html", post=chose_post)


if __name__ == "__main__":
    app.run(debug=True)

