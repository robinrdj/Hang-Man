# Hangman
import random
import hangman_stages_and_logo
from hangman_stages_and_logo import stages
import hangman_words

# Welcoming
print("Welcome to the Hangman! ")
print(hangman_stages_and_logo.logo)

# choosing a word
chosen_word = random.choice(hangman_words.word_list)

# displaying dashes in place of chosen word
display = []
for char in chosen_word:
    display += "_"
print(display)

# getting inputs and checking them with the chosen word
word_length = len(chosen_word)
no_of_lives = 6
end_of_game = False
while not end_of_game:
    guess = input("guess a letter: ").lower()
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess
    print(display)
    if "_" not in display:
        end_of_game = True
        print("U win !")
    if guess not in display:
        no_of_lives -= 1
        print(stages[no_of_lives])
        if no_of_lives == 0:
            end_of_game = true
            print("U lose")
