# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_as_float = float(height)
weight_as_int = int(weight)
bmi = round(weight_as_int / height_as_float ** 2)

bmi = int(bmi)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight')
elif bmi <25:
    print(f'Your BMI is {bmi}, you have a normal weight')   
elif bmi <30:
    print(f'Your BMI is {bmi}, you are slightly overweight')
elif bmi <33:
    print(f'Your BMI is {bmi}, you are obese') 
elif bmi <40:
    print(f'Your BMI is {bmi}, you are a clinically obese')
     