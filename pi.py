# Program Name: pi.py
# Noble Bautista
# November 3rd, 2022
# CSS-225
# Description: Calculate an approximation for pi using Leibniz’s formula,
# which is one of algorithms calculating the mathematical constant pi.
# Write a program that approximates π  according to the Leibniz’s formula
# using the following pseudo codes.
# Then compare the result with the value of math.pi in the math module.

import math  # imports math module


def Leibniz_pi_calculation():
    pi = 0
    n = 10 ** 7
    add = True

    for i in range(1, n, 2):  # range (FOR i = 0 to 100000)
        if add:
            pi += 1 / i  # if statement is true (even), use this formula
        else:
            pi -= 1 / i  # if statement is false (odd), use this formula
        add = not add
    return pi * 4

print("PI = ", Leibniz_pi_calculation())
print("math.pi answer for comparison =", math.pi)
# (above) print statements. first prints pi that I calculated,
# second prints pi that's imported from math module for comparison.
