# 🚨 Don't change the code below 👇
from itertools import count
from re import U


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
combined_string = combined_string.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l + o + v + e
score = int(str(true) + str(love))


if (score < 10) or (score > 90) :
   print(f'Your score is {score}, you go together like coke and mentos.') 
elif (score >= 40) or (score <= 50) :
   print(f'Your score is {score}, you are alright togeter.') 
else:
    print(f'Your score is{score}.')

