# Program Name: Mod8Prob4.py
# Noble Bautista
# November 17th, 2022
# Purpose of this program: Write a function that takes each element of a list called years
# and returns True if it is a leap year or False otherwise. Create a list of leap years that includes
# leap years only after checking each element of the list years. Your result should be checked
# with the calendar.isleap() function

import calendar #imports calendar module for later use

def Years(year): # Function years calculates/determines if a year is a leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    

yearList = [1940, 1900, 1992, 1978, 2004, 2032, 2022, 2026, 2000, 2018, 1720]
# (above) list of years to check if they are leap years (True) or not (False)

#You are supposed to collect only leap years into Leap_years list instead of printing true and false.
Leap_years = []
for i in yearList:
    if Years(i):
        Leap_years.append(i)
        
#print(list(map(Years, yearList))) # prints results from list using the algorithm

# (Below) double checks using calendar if True values from function above are actually leap years
print(calendar.isleap(1940))
print(calendar.isleap(1992))
print(calendar.isleap(2004))
print(calendar.isleap(2032))
print(calendar.isleap(2000))
print(calendar.isleap(1720))

