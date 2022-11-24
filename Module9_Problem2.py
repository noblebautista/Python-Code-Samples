# Noble Bautista
# November 23rd, 2022
# File Name: Module9_Problem2.py
# Description: Using a while loop, create a list called L that contains the numbers 0 to 10.
# On each iteration, the loop should append the current value of a counter variable to the list
# and then increase the counter by 1. The while loop should stop once the counter variable is greater than 10.

L = []  # defines list called "L"
i = 0  # sets variable "i" equal to 0

while i <= 10: # sets range so that the while loop stops once the counter variable is greater than 10
    L.append(i) # appends value of the counter variable to the list, then increases the counter by 1
    i=i+1

print(L)