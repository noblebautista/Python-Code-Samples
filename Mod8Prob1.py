# Program Name: Mod8Prob1.py
# Noble Bautista
# November 17th, 2022
# Purpose of this program: Two numbers are randomly generated between 1 and 20 (boundary inclusive).
# To test for equality, write a function that returns True if two numbers are equal and False otherwise.
# The program repeats until two identical numbers are produced.
# Once equal, it prints the two numbers as well as the number of times the function called.

import random #imports the random module to use random functions

x = random.randint(0, 20)
y = random.randint(0, 20)
#variables defining two random numbers between selected range
count = 1

def isEqual(x, y): #function to determine when x is equal to y (false if not equal)
    if x == y:
        result = True
    else:
        result = False
    return result
print(isEqual(x, y)) #prints function
print("The numbers", x, "and", y, "are found after", count, "repetitions")
# (above) prints equal values of x and y as well as number of loops
