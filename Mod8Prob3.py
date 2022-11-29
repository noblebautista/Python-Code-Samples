# Program Name: Mod8Prob3.py
# Noble Bautista
# November 17th, 2022
# Purpose of this program: Write a function that takes a list containing five numbers generated
# by random.randint(1, 5) and prints whether the value 4 is in that list.

import random  # imports random module

#function argument is a list
def checkIfMatch(lis):  # function that checks to see if 4 exists in the list
    specificNum = 4
    if specificNum in lis:
        print("The value '4' is in this list")  # if a four is found, then this message prints.
    else:
        print("The value '4' does not exist in this list")  # if a four is found, then this message prints.
        
def main():        
    lis = []  # defines the list (lis)
    for i in range(5):  # four loop to chose 5 random numbers
        lis.append(random.randint(1, 5))  # uses random to chose numbers within range 1-5.
    print(lis)
    checkIfMatch(lis)

main()
