# Program Name: Chapter4.py
# Noble Bautista
# November 13th, 2022
# This is the code for Chapter 4 of 5 in this text-based adventure game.


import time  # imports time module
import Chapter3  # imports chapter 3 module (If player is sent back)
import Chapter5  # imports chapter 5 module (if player progresses)

a = 2
b = 1
c = 0.08
# (above) variables set equal to values in seconds that wil be called in the time.sleep() function
# (This dictates how long each message will take to generate on the screen.

def Chapter4_intro(): # Function prints the intro for chapter 4
    print()
    print("You have gotten familiar with Pahoa’s ways, but you are not out of the woods yet")
    time.sleep(a)
    print("Do NOT get comfortable with her supposed kindness. When she strikes, you'll pay!")
    time.sleep(a)
    print("BEHOLD! The powerful and all-omniscient MO’O! A fierce lizard dragon that rules this island.")
    time.sleep(a)
    print("It is just you, her and the jungle now...How will you survive her wrath?")
    time.sleep(b)
    print()

def Fight(): # Function prints the outcome for one of the options (See Main4 function)
    print()
    print("You have chosen to fight. You are armed with nothing but the tools in your backpack. Here are your weapons: ")
    time.sleep(a)
    print(" 1. A bottle of pepper spray")
    time.sleep(b)
    print(" 2. A phone charging cord")
    time.sleep(b)
    print(" 3. A broken metal compass")
    time.sleep(b)
    print()
    # This outcome has lead to another decision with more options listed as print statements (above)
    while True:
        option = input("Which option do you select? (1-3)")
        if option == '1':
            print()
            print("The mace has agitates Mo'o even further, causing her to strike with an intense rage! You are taken down.")
            time.sleep(a)
            print()
            import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1.
            gameover.GameOver(4)
        if option == '2':
            print()
            print("The cord is long enough to use as a lasso. You swing it around and wrap it around Mo'o's neck!")
            time.sleep(a)
            print("You tighten the cord until Mo'o loses enough oxygen...She passes out with a great thud on the Pahoan floor.")
            time.sleep(a)
            print()
            CordLassoAnswer = input("Pahoa beckons you to the final chapter...Continue? (Y/N)")
            if CordLassoAnswer.upper() == 'Y':
                print("Moving along...")
                Chapter5.Main5() # Moves player along to the next chapter
            else:
                print("Now you can exit this game.")
                quit()
            print("Returning to the Main Module...")
        if option == '3':
            print()
            print("The compass is dense and heavy, making it a perfect weapon to strike with! You aim for Mo'os head...")
            time.sleep(a)
            print("Oh no! Your aim is horrid, and it only grazes Mo'os forehead")
            time.sleep(b)
            print("This agitates him greatly, and he takes her rage out on you!")
            time.sleep(b)
            print()
            import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1.
            gameover.GameOver(4)
        return True
def FlightAhead():  # Function prints the outcome for one of the options (See Main4 function)
    print()
    print("You sprint as fast as you can going around Mo'o. She shrieks in feral rage!")
    time.sleep(a)
    print("Although she is mighty and powerful, her waddle is slow, therefore you are able to outrun her!")
    time.sleep(a)
    print("Congratulations! You have thrown Mo'o off your track, so you are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    FlightAheadAnswer = input("Pahoa beckons you to the final chapter... Continue? (Y/N)")
    if FlightAheadAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter5.Main5() # Player progresses to the next chapter
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True

def FlightAway(): # Function prints the outcome for one of the options (See Main4 function)
    print()
    print("You stand in utter terror of Mo's presence, so you dare not even enter her vicinity! You run back to where you came from.")
    time.sleep(a)
    print("Although she is mighty and powerful, her waddle is slow, therefore you are able to outrun her!")
    time.sleep(a)
    print("Congratulations! You have thrown Mo'o off your track, so you are rewarded by progressing in this journey...")
    time.sleep(b)
    print()
    FlightAwayAnswer = input("Pahoa is not through with you...Continue? Continue? (Y/N)")
    if FlightAwayAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter3.Main3() # Player is sent back to chapter 3 as punishment
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True


def Main4():
    global move
    Chapter4_intro() # Prints the function for this chapters intro when Main4() is called
    print()
    print("There are three options you can choose.")
    time.sleep(a)
    print(" 1. Stay and fight! ")
    time.sleep(b)
    print(" 2. Sprint as fast as you can ONWARD!")
    time.sleep(b)
    print(" 3. Run for your life...back from where you came!")
    time.sleep(b)
    print()
    # (Above) All initial options for this game's chapter are listed above as print statements

    while True:
        option = input("Which option do you select? (1-3)")
        if option == '1':
            move = Fight()
        elif option == '2':
            move = FlightAhead()
        elif option == '3':
            move = FlightAway()
        else:
            print("Invalid entry, try again")
        if move == True:
            break
# (above) this while statement takes the user to the function that corresponds with the number chosen.


