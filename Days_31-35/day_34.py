# Day 34 of 100 Days of Code
# Quiz App
from tkinter import *
import requests
from html import unescape

# ---------------------------- CONSTANTS/VARIABLES ------------------------------- #
APP_COLOR = "#3E5075"
RIGHT_COLOR = "#5FB45E"
WRONG_COLOR = "#CA3F41"
BUTTON_FONT = "Ariel", 35, "bold"
Q_FONT = "Ariel", 12, "italic"
score: int
correct_answer: str

# ---------------------------- RETRIEVE QUESTIONS ------------------------------- #


def get_question():
    global correct_answer
    response = requests.get(url="https://opentdb.com/api.php?amount=1&type=boolean")
    response.raise_for_status()

    data = response.json()
    question = data["results"][0]["question"]
    canvas.itemconfig(q_text, text=unescape(question))

    correct_answer = data["results"][0]["correct_answer"]


# ---------------------------- BUTTON FUNCTIONS ------------------------------- #


def answered(answer: str):
    global score
    if answer == correct_answer:
        canvas.config(bg=RIGHT_COLOR)
        root.after(300, lambda: canvas.config(bg='white'))
        score += 1
        score_label.config(text=f"Score: {score}")
    else:
        canvas.config(bg=WRONG_COLOR)
        root.after(300, lambda: canvas.config(bg='white'))

    get_question()


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Quizzler")
root.config(pady=20, padx=20, bg=APP_COLOR)

score_label = Label(text="Score: 0", bg=APP_COLOR, fg="white")
score_label.grid(row=0, column=1, sticky="e")

canvas = Canvas(width=200, height=200, highlightthickness=0)
q_text = canvas.create_text(100, 100, text="Quiz question here", font=Q_FONT, width=180, justify='center')
canvas.grid(row=1, column=0, columnspan=2, pady=20)

true_button = Button(text="✔", font=BUTTON_FONT, bg=RIGHT_COLOR, fg="white", command=lambda: answered("True"))
true_button.grid(row=2, column=0, padx=5)

false_button = Button(text="✘", font=BUTTON_FONT, bg=WRONG_COLOR, fg="white", command=lambda: answered("False"))
false_button.grid(row=2, column=1, padx=5)

get_question()

root.mainloop()
