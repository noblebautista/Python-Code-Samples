###################################################
# Program Name: Mod3Question6.py
# Author: Noble Bautista
# Date: October 13th, 2022
# Purpose of the program: Write a program that prints the balance of an account
# after the first, second, and third year. The account has an initial balance of
# $1,000 and earns 5 percent interest per year.
###################################################
initialBalance = 1000 #1,000 dollars in bank to start with.
initialBalance = float(initialBalance) #declares that variable must be a number.
yearlyInterest = 0.05 #5 percent interest annually
yearlyInterest = float(yearlyInterest) #declares that variable must be a number. #not necessary 


#to get balance B for Nth year ends with interest rate R, initial balance P: B = P * ( 1+ N * R)
y0 = initialBalance   #redundant code
y1 = initialBalance * yearlyInterest + initialBalance #Algorithm(s) to calculate new net balance
y2 = y1 * yearlyInterest + initialBalance
y3 = y2 * yearlyInterest + initialBalance

#ONE, TWO, THREE = 1, 2, 3
#y1 = initial_bal * ( 1 + rate * ONE)
#y2 = initial_bal * ( 1 + rate * TWO)
#y3 = initial_bal * ( 1 + rate * THREE)


print("Year one = ", y1) #print statements showing user all yearly balances
#print("The balance after the first year ends is ${}.".format(y1))
print("Year two = ", y2)
print("year three = ", y3)
