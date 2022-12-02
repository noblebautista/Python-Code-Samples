# Program Name: Main.py
# Noble Bautista
# November 9th, 2022
# This is the main module for my adventure text-based game.


import Chapter1 # imports chapter 1 module
import time # imports time module

a = 2
b = 1
c = 0.08
# (above) variables set equal to values in seconds that wil be called in the time.sleep() function
# (This dictates how long each message will take to generate on the screen.

def game_intro():
    # Function prints game introduction
    print()
    print("It was a crisp and cool morning in the Polynesian jungle of Pahoa")
    time.sleep(a)
    print("The morning dew caressed the lush jungle’s foliage as the salty air lingered on your taste buds. ")
    time.sleep(a)
    print("Oh, how the beauty of it all mocks what misfortune comes your way, young traveler!")
    time.sleep(a)
    print("To set the scene...you are a young solo traveler lost in the Polynesian wilderness of Pahoa.")
    time.sleep(a)
    print("There's nothing but your backpack, the clothes off of your back, and your smarts. ")
    time.sleep(a)
    print("In this game, you must make a series of choices to make it out alive. Trust your intuitions!")
    time.sleep(a)
    print()


def Main(): # Function includes all possible choices for this py file
    game_intro() # Prints the main intro when Main() is called
    player_name = input("Enter your name here: ")
    answer = input("Greetings, {}, would you like to start the game JOURNEY THROUGH PAHOA? (Y/N)".format(player_name))
    # Prompts for user input, regurgitates name that is typed.
    if answer.upper() == 'Y':
        print("Calling the Chapter 1 module...")
        Chapter1.Main1()
        # If the player answers Y for yes, they proceed to chapter 1. Otherwise, the game quits.
    else:
        print("Now you can exit this game.")
        quit()
    print("Now you'll return to Main...")


Main()