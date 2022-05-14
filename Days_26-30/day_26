# Day 26 of 100 Days of Code Challenge
# NATO phonetic alphabet converter
import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

user_word = input("Enter a word: ").upper()

nato_list = [nato_dict[letter] for letter in user_word if letter in nato_dict]

print(nato_list)

