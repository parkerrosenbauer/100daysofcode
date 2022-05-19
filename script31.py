# Day 31 of 100 Days of Code Challenge
# Language Flash Card App
from tkinter import *
import pandas as pd
import random
# ---------------------------- CONSTANTS/VARIABLES ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = "Ariel", 40, "italic"
WORD_FONT = "Ariel", 60, "bold"
SEC_BETWEEN_FLIP = 3
LANGUAGE_FILE = 'data/french_words.csv'
word_bank = pd.read_csv(LANGUAGE_FILE)
index = 0

# ---------------------------- CORRECT GUESS ------------------------------- #


def correct():
    global word_bank
    try:
        word_bank.drop([index], inplace=True)
    except KeyError:
        word_bank = pd.read_csv(LANGUAGE_FILE)
    finally:
        to_language()

# ---------------------------- CARD FLIP ------------------------------- #


def to_english():
    try:
        english_word = word_bank.English.loc[index]
    except KeyError:
        pass
    else:
        canvas.itemconfig(flash_card, image=back_side)
        canvas.itemconfig(word, text=english_word, fill='white')
        canvas.itemconfig(language, text="English", fill='white')


def to_language():
    global index
    try:
        index = random.choice(word_bank.index.to_list())
    except IndexError:
        canvas.itemconfig(language, text="Select the ✔ to start again")
        canvas.itemconfig(word, text="Vocab Mastered")
    else:
        language_word = word_bank.French.loc[index]
        canvas.itemconfig(flash_card, image=front_side)
        canvas.itemconfig(language, text="French", fill='black')
        canvas.itemconfig(word, text=language_word, fill='black')
        root.after(3000, to_english)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
root.title("Flash Cards")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_side = PhotoImage(file="images/card_front.png")
back_side = PhotoImage(file="images/card_back.png")
flash_card = canvas.create_image(400, 263, image=front_side)
word = canvas.create_text(400, 263, text="trouve", font=WORD_FONT)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
canvas.grid(row=0, column=0, columnspan=2, pady=15)

# Buttons
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=to_language)
wrong_button.grid(row=1, column=0)
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)

to_language()

root.mainloop()
