# Problem3_Mod5Lab.py
# Noble Bautista
# October 26th, 2022
# Consider a program that prints the integers from 1 to 50.
# If a number is multiples of three, then prints “Divisible by three”
# instead of printing the number and for the multiples of seven prints “Divisible by seven”.
# For numbers which are multiples of both three and seven print “Divisible by both”.

for i in range(0,51):  # for loop that prints the integers from 1 to 50
    print(i)  # prints list of numbers

    if (i % 3 == 0 and i % 7 == 0):
        print("Divisible By Both")  # if number is divisible by both 3 & 7, statement prints
        # statement instead of number.
    elif (i % 3 == 0):
        print("Divisible by Three")  # if number is divisible by 3, statements prints
        # statement instead of number.
    elif (i % 7 == 0):
        print("Divisible by Seven")  # if number is divisible by 7, statements prints
        # statement instead of number.
