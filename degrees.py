# Program Name: degrees.py
# Noble Bautista
# November 3rd, 2022
# CSS-225
# Description: Convert radians to degrees using 2π rad = 360°.
# Write a program to convert a user input value in radians to the
# value in degrees. Print this value to compare it to a value computed
# using the degrees function in the math module for the same input value.

import math  # imports math module
radian = int(input("enter a radian value to convert it into degrees: "))
# (above) prompts user to enter value for radian
pi = 3.14159  # value of pi (rounded)
degree = radian * (180 / pi)  # formula for conversion
print("degree = ", degree)  # prints conversion
#  (below) separate calculation using math's degrees function
#  (no user input). In this case, value matches user input for
#  the sake of this comparison.
print(math.degrees(45))