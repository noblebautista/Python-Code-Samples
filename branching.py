# Program Name: branching.py
# Purpose of a program: A time traveler has suddenly appeared in your classroom!
# The travelor enters his/her year of origin
# Program returns a greeting message according to the year.
# Distant Past: Before 1900
# Present Era-Years between 1900-2020
# Far Future: After 2020
########################################################################################
# Noble Bautista = Editor

year = int(input("Greetings! What is your year of origin? ")) #asks for user input (specifies it is an integer, defines variable as year).

if year < 1900:
    print("Woah, that's the past!") #if the user puts in a year before 1900, the message displays.
elif year >= 1900 & year <= 2020:
    print("That's totally the present!") #if the user puts in a year between 1900-2020, the message displays.
elif year > 2020:
    print("Far out, that's the future!!")  #if the user puts in a year after 2020, the message displays.
