import random
from hangman_wordslist import word_list
from hangman_art import stages, logo


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_the_game = False
lives = 6

print(logo)
for _ in range(word_length):
    display += "_"

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'you\'ve repeated letter \'{guess}\', try again')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f'You\'ve selected Letter {guess}, which is not in the word, also you \'ve lost a lie. You have {lives} lives remaining')
    if lives == 0:
       end_of_game = True
       print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_the_game = True
        print('You win.')
    print(stages[lives])    