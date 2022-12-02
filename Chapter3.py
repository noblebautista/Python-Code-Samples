# Program Name: Chapter3.py
# Noble Bautista
# November 11th, 2022
# This is the code for Chapter 3 of 5 in this text-based adventure game.


import time  # imports time module
import Chapter2  # imports chapter 2 module (If player is sent back)
import Chapter4  # imports chapter 4 module (if player progresses)


a = 2
b = 1
c = 0.08
# (above) variables set equal to values in seconds that wil be called in the time.sleep() function
# (This dictates how long each message will take to generate on the screen.

def Chapter3_intro(): # Function prints the intro for chapter 3
    print()
    print("Although Pahoa let you be quenched, will she let you be fed?")
    time.sleep(a)
    print("May the fruits of your labor grow ripe from your wit!")
    time.sleep(a)
    print("Now you are starving after wandering for days. Ahead there is food!")
    time.sleep(a)
    print("There are foreign trees with unknown fruit before you...")
    time.sleep(a)
    print("There is (1) a palm with little brown fruits, a fern with juicy red berries,")
    time.sleep(a)
    print("a shrub with long, purple peppers, and a patch of seemingly edible leaves.")
    time.sleep(a)
    print("Choose wisely, my friend!")
    time.sleep(b)
    print()

def BrownFruits(): # Function prints the outcome for one of the options (See Main3 function)
    print()
    print("The fruit tastes absolutely scrumptious! Thankfully it is 100% edible!")
    time.sleep(a)
    print("Congratulations, you selected the correct food! You are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    BrownFruitsAnswer = input("Pahoa beckons you to Chapter 4. Continue? (Y/N)")
    if BrownFruitsAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter4.Main4() # Moves player along to the next chapter
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True

def RedBerries(): # Function prints the outcome for one of the options (See Main3 function)
    print()
    print("The fruit is tasty at first, but then your taste buds begins to ache. The fruits are poisonous! ")
    time.sleep(a)
    print("Perhaps if fate had been more mellow, you would have survived. This marks the end of your journey.")
    time.sleep(b)
    print()
    import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1.
    gameover.GameOver(3)
    return True

def PurplePeppers(): # Function prints the outcome for one of the options (See Main3 function)
    print()
    print("The fruit is edible! But the heat of the peppers is extreme...It must be over 1 billion Scovilles!")
    time.sleep(a)
    print("Your journey has not ceased, but you must be sent back to find water to cool your tongue!")
    time.sleep(b)
    print()
    BrownFruitsAnswer = input("Pahoa is not through with you...Continue? (Y/N)")
    if BrownFruitsAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter2.Main2() # Moves player back to the last chapter as punishment
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True

def Greenleaves(): # Function prints the outcome for one of the options (See Main3 function)
    print()
    print("The unknown lettuce is a bit sour, but crisp and refreshing. Your hunger has been satisfied!")
    time.sleep(a)
    print("Congratulations, you selected the correct food! You are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    GreenleavesAnswer = input("Pahoa beckons you to Chapter 4. Continue? (Y/N)")
    if GreenleavesAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter4.Main4() # Moves player along to the next chapter
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True


def Main3():
    global move
    Chapter3_intro() #Prints the function for this chapters intro when Main3() is called
    print()
    print("There are four options you can choose.")
    time.sleep(a)
    print(" 1. You eat from the palm with little brown fruits. ")
    time.sleep(c)
    print(" 2. You eat from the fern with juicy red berries ")
    time.sleep(c)
    print(" 3. You eat from the shrub with long, purple peppers. ")
    time.sleep(c)
    print(" 4. You eat from the bush with patches of green leaves")
    time.sleep(c)
    print()
    # (Above) Options for this game's chapter are listed above as print statements

    while True:
        option = input("Which option do you select? (1-4)")
        if option == '1':
            move = BrownFruits()
        elif option == '2':
            move = RedBerries()
        elif option == '3':
            move = PurplePeppers()
        elif option == '4':
            move = Greenleaves()
        else:
            print("Invalid entry, try again")
        if move == True:
            break
# (above) this while statement takes the user to the function that corresponds with the number chosen.

