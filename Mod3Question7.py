###################################################
# Program Name: Mod3Question7.py
# Author: Noble Bautista
# Date: October 13th, 2022
# Purpose of the program: It is possible to name the days 0 through 6 where day 0 is
# Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (Wednesday)
# and you return home after 10 nights, then you would return home on Saturday (day 6).
# Write a general version of the program which asks for the starting day number,
# and the length of your stay, and it will tell you the number of the day you will return on.
###################################################
vacationStart = int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for monday, etc.) '))
#User's answer is the start day of the vacation.
vacationStart = float(vacationStart) #declares that variable must be a number.
#vacation_start = int(input("What day are you leaving? "))


vacationLength = int(input('How many days will your vacation be? '))
#User's answer is the length of the vacation.
vacationLength = float(vacationLength) #declares that variable must be a number.

#length_stay = int(input("How long will you stay ? "))
returnDay = (vacationLength + vacationStart) % 7 #algorithm that calculates the number of the day you'll return.
returnDay = float(returnDay) #declares that variable must be a number.
print("The number of the day you’ll return: ", returnDay) #prints number of day you will return.

