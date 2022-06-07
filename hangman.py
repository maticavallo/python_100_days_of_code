import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_the_game = False

for _ in range(word_length):
    display += "_"

while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_the_game = True
        print('You win.')