# Day 5 of 100 Days of Code Challenge
# Password Generator
import random

# Letters, Numbers, Symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
letter_count = int(
    input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
num_count = int(input("How many letters would you like?\n"))


password = ""
for num in range(0, letter_count):
    password += random.choice(letters)

for num in range(0, symbol_count):
    password += random.choice(symbols)

for num in range(0, num_count):
    password += random.choice(numbers)

password = ''.join(random.sample(password, k=len(password)))
print(f"Your password is: {password}")
