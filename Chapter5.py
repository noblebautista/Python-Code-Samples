# Program Name: Chapter5.py
# Noble Bautista
# November 14th, 2022
# This is the code for Chapter 5 of 5 in this text-based adventure game.


import time #imports the module for time
import Chapter2 #imports the Chpater2 module (if player is sent back)


a = 2
b = 1
c = 0.08
# (above) variables set equal to values in seconds that wil be called in the time.sleep() function
# (This dictates how long each message will take to generate on the screen.

def Chapter5_intro(): # Function prints the intro for chapter 5
    print()
    print("Just as Pahoa is about to have her way with you, weary traveler,")
    time.sleep(a)
    print("the sound of pitter patter and chitter chatter sings a hopeful tune to you!")
    time.sleep(a)
    print("You hear people, stumbles upon a back road with people and two vehicles.")
    time.sleep(a)
    print("Both offer to help by giving you a ride. One is a van with a family of five.")
    time.sleep(a)
    print("The other is a rickshaw with a married couple. How will you proceed?")
    time.sleep(c)
    print()

def FamilyVan(): # Function prints the outcome for one of the options (See Main5 function)
    print()
    print("You have fallen right into their trap. This is a family of murderers! But alas you have a fighting chance. You can: ")
    time.sleep(a)
    print(" 1. Smash the window open with headrest and escape moving car")
    time.sleep(b)
    print(" 2. Attempt to take control of the wheel")
    time.sleep(b)
    print(" 3. Try to reason with them by giving an emotional plea")
    time.sleep(b)
    print()
    # This outcome has lead to another decision with more options listed as print statements (above)
    while True:
        option = input("Which option do you select? (1-3)")
        if option == '1':
            print()
            print("You escape successfully, but you have quite a fall. No one is there to tend to your wounds, so you perish.")
            time.sleep(a)
            print()
            import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1 OR quits.
            gameover.GameOver(5)
        if option == '2':
            print()
            print("During the mayhem the rest of the family tries to stop you...")
            time.sleep(a)
            print("The car crashes off of a cliff into the Pacific. Pahoa has reclaimed more victims")
            time.sleep(a)
            print()
            import gameover # imports the game over module, and runs the GameOver function to restart from chapter 1 OR quits.
            gameover.GameOver(5)
        if option == '3':
            print()
            print("For some divine reason, they are touched by your cry, and question their ways...you changed their hearts for the better")
            time.sleep(a)
            print("They clothe you, feed you and even drive you to the airport with a paid ticket back home. ")
            time.sleep(a)
            print()
            print("CONGRATULATIONS! YOU WON!")
            time.sleep(a)
            print()
            import gameover # You win...imports the game over module, and runs the GameOver function to restart from chapter 1 OR quits.
            gameover.GameOver(5)
            return True

def CoupleInRickshaw(): # Function prints the outcome for one of the options (See Main5 function)
    print()
    print("This lovely couple drives you to the main road. From there you can:")
    time.sleep(a)
    print("charge your phone at a local business, take out some cash, and take a shuttle to the airport...")
    time.sleep(a)
    print("BUT you do not have enough money for a ticket home! What shall you do from here?")
    time.sleep(a)
    print(" 1. Sit and beg for money. Wait for a kind stranger to buy you a plane ticket back home to Chicago.")
    time.sleep(b)
    print(" 2. Ask for a job at the airport in exchange for a plane ticket back home.")
    time.sleep(b)
    print(" 3. Ask the Rickshaw couple for some money for a plane ticket")
    time.sleep(b)
    print()
    # This outcome has lead to another decision with more options listed as print statements (above)
    while True:
        option = input("Which option do you select? (1-3)")
        if option == '1':
            print()
            print("No one comes to your aid. Nightfall comes, and security forces you to leave the premises. You are more alone than ever before.")
            time.sleep(a)
            print()
            import gameover  # imports the game over module, and runs the GameOver function to restart from chapter 1 OR quits.
            gameover.GameOver(5)
        if option == '2':
            print()
            print("Your request is successful. After hours of working as a receptionist...")
            time.sleep(a)
            print("You get enough money to get a plane back home to Chicago. Home sweet home!")
            time.sleep(a)
            print("CONGRATULATIONS! YOU WON!")
            time.sleep(a)
            print()
            import gameover  #  You win..imports the game over module, and runs the GameOver function to restart from chapter 1 OR quits.
            gameover.GameOver(5)
            return True
        if option == '3':
            print()
            print("The couple insists that they have already done a good deed and are very insulted by this request!")
            time.sleep(a)
            print("You get into a verbal altercation with them which leads to your arrest. You are stuck!")
            time.sleep(a)
            print()
            import gameover  # imports the game over module, and runs the GameOver function to restart from chapter 1 OR quits.
            gameover.GameOver(5)
            return True

def LoneHiker(): # Function prints the outcome for one of the options (See Main5 function)
    print()
    print("You have overestimated your level of endurance and become famished.")
    time.sleep(a)
    print("You have no choice but to retrace your steps to seek food and water")
    time.sleep(a)
    print()
    LoneHikerAnswer = input("You have been sent back... would you like to continue this game? (Y/N)")
    if LoneHikerAnswer.upper() == 'Y':
        print("Moving along...")
        Chapter2.Main2() # Player is sent back to chapter 2 as punishment
    else:
        print("Now you can exit this game.")
        quit()
    print("Returning to the Main Module...")
    return True


def Main5():
    global move
    Chapter5_intro() #Prints the function for this chapters intro when Main5() is called
    print()
    print("There are three options you can choose.")
    time.sleep(b)
    print(" 1. Accompany the family of five in their van")
    time.sleep(b)
    print(" 2. Join the couple in the rickshaw.")
    time.sleep(b)
    print(" 3. Decline both offers and trust your wit. Hike up the road alone")
    time.sleep(b)
    print()
    # (Above) All initial options for this game's chapter are listed above as print statements

    while True:
        option = input("Which option do you select? (1-3)")
        if option == '1':
            move = FamilyVan()
        elif option == '2':
            move = CoupleInRickshaw()
        elif option == '3':
            move = LoneHiker()
        else:
            print("Invalid entry, try again")
        if move == True:
            break
# (above) this while statement takes the user to the function that corresponds with the number chosen.

