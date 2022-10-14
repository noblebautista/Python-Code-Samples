###################################################
# Program Name: Mod3Question5.py
# Author: Noble Bautista
# Date: October 13th, 2022
# Purpose of the program: Write a program that computes the MPG (Miles per Gas) for a car.
# Prompt the user to enter the number of miles driven and the number of gallons it used.
# Print the answer with a message.
###################################################

milesDriven = input("How many miles have you driven in your car? Please enter a number: ")
# (above) asks user for number of miles driven in car.
milesDriven = float(milesDriven)  #declares that variable must be a number.
galUsed = input("how many gallons of gas were used? Please enter a number: ")
# (above) asks user how many gallons of gas were used in car.
galUsed = float(galUsed)  #declares that variable must be a number.
mpg = milesDriven / galUsed  #algorithm/formula for miles per gallon calculation.
mpg = float(mpg)  #declares that variable must be a number.
print("The miles per gas (MPG) calculation for your car is", mpg)
# (above) shows final MPG calculation to user w/ message.
