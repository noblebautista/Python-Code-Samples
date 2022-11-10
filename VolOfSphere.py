# Program Name: VolOfSphere.py
# Noble Bautista
# November 8th, 2022
# Purpose of Program: Write a function VolOfSphere(r) which returns
# the volume of a sphere of radius r. Make sure you use the
# math module in your solution.

import math  # imports math module
def VolOfSphere(r): # defines volume of sphere
    return (4 / 3 * math.pi * r ** 3)
    # (above) returns formula for sphere volume
r = int(input("please enter a to calculate the volume of the sphere: "))
# (above) defines radius (r) as user input)
print(VolOfSphere(r))
# (above) prints sphere volume equation answer using r (user input)
