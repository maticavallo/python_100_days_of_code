 #Remember to use the random module
    #Hint: Remember to import the random module here at the top of the file. 🎲
        
    # 🚨 Don't change the code below 👇
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
    # 🚨 Don't change the code above 👆 It's only for testing your code.
        
    #Write the rest of your code below this line 👇

random_side = random.randint(0,1)
if random_side == 1:
        print(f'Heads')     
else:
        print('Tails')
