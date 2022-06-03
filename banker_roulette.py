
import random
from secrets import choice
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
qty_items = len(names)
random_choice = random.randint(0, qty_items - 1 )
name_of_choice = names[random_choice] 

print(f'{name_of_choice} is going to buy the meal today!')



