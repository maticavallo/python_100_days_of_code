# 🚨 Don't change the code below 👇
from re import L, M, S
from tkinter import N, Y


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#realized that must input capital letters to previous functions, if not it's gonna take 0 value.
#also, if the user press other letter, it's going to understand as 0 value, so could order free pizza. Should loop first if.
# it could be improved but i don't have the resources yet.

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
     bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
if extra_cheese == "Y":
    bill += 1

print(f'Your final bill is ${bill}.')
