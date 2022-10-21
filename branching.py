# Program Name: branching.py
# Purpose of a program: A time traveler has suddenly appeared in your classroom!
# The travelor enters his/her year of origin
# Program returns a greeting message according to the year.
# Distant Past: Before 1900
# Present Era-Years between 1900-2020
# Far Future: After 2020
########################################################################################
# Noble Bautista = Editor

year = int(input("Greetings! What is your year of origin? "))

if year < 1900:
    print("Woah, that's the past!")
elif year >= 1900 & year <= 2020:
    print("That's totally the present!")
elif year > 2020:
    print("Far out, that's the future!!")
