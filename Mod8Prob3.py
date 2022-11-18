# Program Name: Mod8Prob3.py
# Noble Bautista
# November 17th, 2022
# Purpose of this program: Write a function that takes a list containing five numbers generated
# by random.randint(1, 5) and prints whether the value 4 is in that list.

import random  # imports random module

lis = []  # defines the list (lis)
for _ in range(5):  # four loop to chose 5 random numbers
    lis.append(random.randint(1, 5))  # uses random to chose numbers within range 1-5.
print(lis)

specificNum = 4  # specifies variable that we are looking for in list is 4


def checkIfMatch(specificNum):  # function that checks to see if 4 exists in the list
    if specificNum in lis:
        print("The value '4' is in this list")  # if a four is found, then this message prints.


checkIfMatch(specificNum)
