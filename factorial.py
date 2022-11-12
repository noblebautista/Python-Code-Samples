# Program Name: factorial.py
# Noble Bautista
# November 3rd, 2022
# CSS-225
# Description: Write a program that uses a for loop to compute
# the factorial of a user input value.
# Print the result to compare to be compared with the calculated value
# using the factorial function in the math module.

import math  # imports math module
num = int(input("enter a number: "))
# (above) prompts user to enter number value (int)
fac = 1
for i in range(1, num + 1):
    fac = fac * i  # calculation for factorial
print("factorial of ", num, " is ", fac)  # prints result from calculation
#  (below) separate calculation using math's factorial function
#  (no user input). In this case, value matches user input for
#  the sake of this comparison.
print(math.factorial(22))

#Compare your result with the value obtaining from the function using same input value.
print(math.factorial(num))
