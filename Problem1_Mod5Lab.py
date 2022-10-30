# Problem1_Mod5Lab.py
# Noble Bautista
# October 26th, 2022
# This program asks the user to enter a number
# and prints “Hello World” by that number.

print("How many time to Print? enter a number: ")
# asks user for number.
tot = int(input())
# declares that user input must be a number.

for i in range(tot):
    print("Hello World!")
    # prints "hello world" however many times "tot" is called.
