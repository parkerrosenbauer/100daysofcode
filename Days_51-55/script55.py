# Day 55 of 100 Days of Code
# Higher and lower game website

# -----------------------// Imports //----------------------- #
from flask import Flask
import random

# -----------------------// Variables //----------------------- #
app = Flask(__name__)
random_num = random.randint(0, 9)

# -----------------------// Pages //----------------------- #


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def check(guess):
    if guess < random_num:
        return '<h1 style="color: red">Too low, try again!</h1>' \
               '<img src="https://media1.giphy.com/media/IevhwxTcTgNlaaim73/200w.webp?cid=ecf05e47211f2z5njrmu68f1x' \
               'yomtt1ar1z427c2ebnjtdr9&rid=200w.webp&ct=g">'
    elif guess > random_num:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
               '<img src="https://media0.giphy.com/media/YpfevjbcK4HWjjIQGL/200.webp?cid=ecf05e473tfaxh75qh794shyivrt' \
               '9o5sc25l3y4pdxp627zm&rid=200.webp&ct=g">'
    elif guess == random_num:
        return '<h1 style="color: green">You found me!</h1>' \
               '<img src="https://media0.giphy.com/media/XkGXBa01dxNIvjAJHl/200w.webp?cid=ecf05e47atpvcx2x1px9z56l' \
               '59ojtbps2xqkna3elrvm0xww&rid=200w.webp&ct=g">'


# -----------------------// Run //----------------------- #
if __name__ == "__main__":
    app.run(debug=True)
