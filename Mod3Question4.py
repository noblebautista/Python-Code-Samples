###################################################
# Program Name: Mod3Question4.py
# Author: Noble Bautista
# Date: October 13th, 2022
# Purpose of the program: Write a program that computes the area of a circle.
# Prompt the user to enter the radius and print the answer with a nice message
###################################################

r = input("Input the radius of the circle : ")  # you can do it at once: r = float(input("Enter a radius"))
# asks user for input statement (radius of the circle)
r = float(r) #declares that variable must be a number.
pi = 3.14 # pi (rounded)
circleArea = (pi * r ** 2) #algorithm to calculate the area of the circle (given user input's info)
print("Nice! Looks like the area of the circle is ", circleArea)
# (above) shows user final calculation for the circle's area with a message
