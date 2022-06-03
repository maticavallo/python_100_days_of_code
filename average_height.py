# 🚨 Don't change the code below 👇
from audioop import avg
from zoneinfo import available_timezones


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height


n_students = 0
for number in student_heights:
    n_students += 1


avg_height = total_height / n_students
print(round(avg_height))


    


