# Day 8 of 100 Days of Code Challenge
# Caesar Cipher
from cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, plain_text, shift_amount):
    stat = "encrypted"
    if direction == "decode":
        shift_amount *= -1
        stat = "decrypted"

    cipher_text = ''
    for letter in plain_text:
        if letter in alphabet:
            pos = alphabet.index(letter)
            pos = (pos + shift_amount) % len(alphabet)
            cipher_text += alphabet[pos]
        else:
            cipher_text += letter

    print(f"The {stat} text is: {cipher_text}")


print(logo)
restart = "Y"

while restart == "Y":
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))

    caesar(option, text, shift)

    restart = input(
        "Would you like to go again? Type 'Y' to use the program again or 'N' to end\n")
