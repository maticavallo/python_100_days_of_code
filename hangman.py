import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_the_game = False


while end_of_the_game == False:
    guess = input("Guess a letter: ").lower()
    
    for blank in range(word_length):
        display += "_"

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_the_game = True
    print('You win.')