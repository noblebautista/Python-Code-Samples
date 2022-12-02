# Program Name: Chapter1.py
# Noble Bautista
# November 9th, 2022
# This is the code for Chapter 1 of 5 in this text-based adventure game.

import Chapter2 # Imports the module Chapter2
import time # Imports the time module

a = 2
b = 1
c = 0.08
# (above) variables set equal to values in seconds that wil be called in the time.sleep() function
# (This dictates how long each message will take to generate on the screen.

def Chapter1_intro(): # Function prints the intro for chapter 1
    print()
    time.sleep(a)
    print("Hours into your joyous hike, you reach an oceanside cliff after seeing nothing but wilderness.")
    time.sleep(a)
    print("You reach for tools in your bag and find your compass smashed and phone completely dead. ")
    time.sleep(a)
    print("What a panic! You scramble to find any sign of civilization. ")
    time.sleep(a)
    print("Behold! a lighthouse stands way in the distant fog. ")
    time.sleep(a)
    print("Where do you go from here?")
    time.sleep(a)
    print()

def JumpAndSwim(): # Function prints the outcome for one of the options (See Main1 function)
    print()
    print("You underestimated how choppy the waves were. Your energy is depleting fast!")
    time.sleep(a)
    print("You fight the current but you unfortunately capsize. Your journey ends here.")
    time.sleep(b)
    print()
    import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1.
    gameover.GameOver(1)
    return True

def JunglePromenade(): # Function prints the outcome for one of the options (See Main1 function)
    print()
    print("You've now entered the wilderness about to embark on the trek of a lifetime.")
    time.sleep(a)
    print("Congratulations, this is the safest decision so far! You are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    JunglePromenadeAnswer = input("Pahoa beckons you to Chapter 2. Continue? (Y/N)")
    if JunglePromenadeAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter2.Main2() # Moves player to Chapter2 module
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True

def RaftAndPaddle(): # Function prints the outcome for one of the options (See Main1 function)
    print()
    print("Despite the choppy waves, you travel far! But just meters before you reach the coast, the raft fails!")
    time.sleep(a)
    print("You tumble to your watery grave as the raft tears in shambles. Your journey ends here.")
    time.sleep(b)
    print()
    import gameover   # imports the game over module, and runs the GameOver function to restart from chapter 1.
    gameover.GameOver(1)
    return True

def BuildFire(): # Function prints the outcome for one of the options (See Main1 function)
    print()
    print("You successfully made a fire! the smoke and light travel far into the night")
    time.sleep(a)
    print("However, no one has or will come to your rescue. Out of stubbornness you stay and try again,")
    time.sleep(b)
    print("But, your stomach goes empty, and your mouth goes parched. Jaded, you turn to the wilderness in hopes of "
          "finding water and sustenance.")
    time.sleep(a)
    print()
    BuildFireAnswer = input("Pahoa beckons you to Chapter 2. Continue? (Y/N)")
    if BuildFireAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter2.Main2() # Moves player to Chapter2 module
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True


def Main1():
    global move
    Chapter1_intro() # Prints the intro from chapter one when Main1() is called
    print()
    print("There are four options you can choose.")
    time.sleep(a)
    print(" 1. Jump into the Pacific and swim towards the distant light house")
    time.sleep(c)
    print(" 2. Walk into the jungle to retrace steps and find a way towards civilization")
    time.sleep(c)
    print(" 3. Construct a raft with natural materials and paddle your way to light house shoal")
    time.sleep(c)
    print(" 4. Build a fire to keep warm, set up camp and signal for help from a potential passer byer")
    print()
    # (Above) all options for this game's chapter are listed above as print statements

    while True:
        option = input("Which option do you select? (1-4)")
        if option == '1':
            move = JumpAndSwim()
        elif option == '2':
            move = JunglePromenade()
        elif option == '3':
            move = RaftAndPaddle()
        elif option == '4':
            move = BuildFire()
        else:
            print("Invalid entry, try again")
        if move == True:
            break
# (above) this while statement takes the user to the function that corresponds with the number chosen.

