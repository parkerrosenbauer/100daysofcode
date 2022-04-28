# Day 7 of 100 Days of Code Challenge
# Hangman
import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

# displaying logo
print(hangman_art.logo)

# creating blanks to disply to the user
display = []
for x in range(word_length):
    display.append('_')

# while loop to run game
while not end_of_game:
    # take user input
    guess = input("Guess a letter ").lower()

    # if the user has already guessed their guess
    if guess in display:
        print(
            f"The letter you guessed was {guess}. You have already guessed that letter.")

    # updating display if the letter is present in the chosen word
    for pos in range(word_length):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in display:
        print(f"You guessed {guess}, that's not in the word.")
        lives -= 1

    # print display
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

    # checking win/lose conditions
    if lives == 0:
        print(f'You lose. The word was {chosen_word}')
        end_of_game = True
    elif '_' not in display:
        print('You win!')
        end_of_game = True
