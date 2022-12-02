# Program Name: Chapter2.py
# Noble Bautista
# November 9th, 2022
# This is the code for Chapter 2 of 5 in this text-based adventure game.


import time  # Imports the time module
import Chapter3  # Imports the module Chapter3

a = 2
b = 1
c = 0.08
# (above) variables set equal to values in seconds that wil be called in the time.sleep() function
# (This dictates how long each message will take to generate on the screen.

def Chapter2_intro(): # Function prints the intro for chapter 2
    print()
    print("The jungle proved grueling despite her mystic beauty...Alas! You hear water rushing!")
    time.sleep(a)
    print("Could it be water to quench your thirst? Or just another one of Pahoa’s tricks?")
    time.sleep(b)
    print("You have made it to the next step, but beware...for a sip may prove to be fatal!")
    time.sleep(a)
    print("Before you stand two strange waterfalls in the wilderness...One has a verdant tint,")
    time.sleep(b)
    print("the other a crimson hue. You are absolutely parched, so do not be picky...")
    time.sleep(a)
    print()

def VerdantDrinker(): # Function prints the outcome for one of the options (See Main2 function)
    print()
    print("The water tastes sweet...but oh no! The water is tainted with a poisonous moss! ")
    time.sleep(a)
    print("Perhaps if fate had been more mellow, you would still be alive. Your journey ends here.")
    time.sleep(b)
    print()
    import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1.
    gameover.GameOver(2)
    return True

def CrimsonTaster(): # Function prints the outcome for one of the options (See Main2 function)
    print()
    print("The water has a bitter taste, but thankfully the hue is from an edible algae bloom!")
    time.sleep(a)
    print("Congratulations, this is the safest decision so far! You are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    CrimsonTasterAnswer = input("Pahoa beckons you to Chapter 3. Continue? (Y/N)")
    if CrimsonTasterAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter3.Main3() #Moves player along to the next chapter
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True

def PuddleSipper(): # Function prints the outcome for one of the options (See Main2 function)
    print()
    print("Holding your nose, you chug the rancid liquid. It burns in your stomach. But, there are no other side"
          "effects!")
    time.sleep(a)
    print("Congratulations, this is the safest decision so far! You are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    CrimsonTasterAnswer = input("Pahoa beckons you to Chapter 3. Continue? (Y/N)")
    if CrimsonTasterAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter3.Main3() # Moves player along to the next chapter
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True

def NoDrink(): # Function prints the outcome for one of the options (See Main2 function)
    print()
    print("You wander through the wilderness for hours on end. No water or sign of civilization in sight!")
    time.sleep(a)
    print("Days pass and you succumb to the delirium. For dehydration finally hugs you with her cold embrace.")
    time.sleep(b)
    print()
    import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1.
    gameover.GameOver(2)
    return True


def Main2():
    global move
    Chapter2_intro() # Prints the intro from chapter one when Main2() is called
    print()
    print("There are four options you can choose.")
    time.sleep(a)
    print(" 1. Chose to sip the waterfall with the strangely verdant tint")
    time.sleep(c)
    print(" 2. Chose to sip the waterfall with the oddly crimson hue")
    time.sleep(c)
    print(" 3. Chose to drink murky water from nearby puddles instead")
    time.sleep(c)
    print(" 4. Decides choices are too risky, continues marching without drinking anything")
    time.sleep(c)
    print()
    # (Above) all options for this game's chapter are listed above as print statements
    while True:
        option = input("Which option do you select? (1-4)")
        if option == '1':
            move = VerdantDrinker()
        elif option == '2':
            move = CrimsonTaster()
        elif option == '3':
            move = PuddleSipper()
        elif option == '4':
            move = NoDrink()
        else:
            print("Invalid entry, try again")
        if move == True:
            break
# (above) this while statement takes the user to the function that corresponds with the number chosen.