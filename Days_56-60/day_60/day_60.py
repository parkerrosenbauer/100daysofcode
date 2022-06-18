# Day 60 of 100 Days of Code Challenge
# Improved Blog Website
# This website is based off a free theme found at: https://startbootstrap.com/previews/clean-blog

"""
Accomplished tasks:
- Pulled data from the contact form into python variables
- Sent an email to myself with the details whenever the contact form is filled out
"""

from flask import Flask, render_template, request
import requests
import smtplib
import os

CONTACT_EMAIL = "pythonbot97@gmail.com"
PASS = os.environ.get("EMAIL_PASS")
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


@app.route("/form-entry", methods=["POST"])
def receive_data():
    u_name = request.form["u-name"].title()
    u_email = request.form["u-email"]
    u_phone = request.form["u-phone"]
    u_message = request.form["u-message"]
    send_email(u_name, u_email, u_phone, u_message)
    return f"<h1>Your message was successfully sent, {u_name}.</h1>"


def send_email(sender, s_email, s_phone, s_message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=CONTACT_EMAIL, password=PASS)
        connection.sendmail(
            from_addr=CONTACT_EMAIL,
            to_addrs=CONTACT_EMAIL,
            msg=f"Sender: {sender}\nEmail: {s_email}\nPhone: {s_phone}\nMessage: {s_message}")


if __name__ == "__main__":
    app.run(debug=True)
