# Program Name: Mod8Prob2.py
# Noble Bautista
# November 17th, 2022
# Purpose of this program: Generates three integer values using random.randint(1, 30)
# and prints the largest number without using max().

import random  # imports the random module
num1 = random.randint(1, 30)
num2 = random.randint(1, 30)
num3 = random.randint(1, 30)
# (above) defines number variables that will select a number randomly from given range
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
# (above) if statement (takes three inputs and finds the largest one, returns largest value).
print(num1, num2, num3)
print("The largest number is", largest)