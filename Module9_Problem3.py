# Noble Bautista
# November 23rd, 2022
# File Name: Module9_Problem3.py
# Description: Using a while loop, ask the user to enter a number.
# Append each entered number to a list and add them together.
# Continue asking for a number until the sum of the list of numbers is greater than 100.

L = [] # defines list named "L"

while sum(L) < 100: # Keep asking for user input and adding input value to list until the sum of list L exceeds 100
    n = int(input("Enter a value to compute: "))
    L.append(n)
print(sum(L))



