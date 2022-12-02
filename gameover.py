# Program Name: gameover.py
# Noble Bautista
# November 14th, 2022
# This is the module that will be referenced whenever the player's journey comes to an end (game over)

def GameOver(chaptername):
    decision = input("GAME OVER...Would you like to restart (Yes) or quit (no)? ")
    # (Above) gives user input to chose yes or no (either restarting or quitting).
    decisionvalid = False
    while decisionvalid == False:
        if decision.lower() == "yes" or decision.lower() == "y":
            print("Restarting from Chapter 1") # restarts game if given "yes" or "y" as input.
            decisionvalid = True
            if chaptername == 1:
                import Chapter1
                Chapter1.Main1()
            elif chaptername == 2:
                import Chapter2
                Chapter2.Main2()
            elif chaptername == 3:
                import Chapter3
                Chapter3.Main3()
            elif chaptername == 4:
                import Chapter4
                Chapter4.Main4()
            elif chaptername == 5:
                import Chapter5
                Chapter5.Main5()
                # (Above) all elif statements correspond to every chapter module within the game
            else:
                print("Error, unknown chapter. Restarting from Chapter 1")
                GameOver(1)
        elif decision.lower() == "no" or decision.lower() == "n":
            decisionvalid = True
            quit() # quits game if given "no" or "n" as input.
        else:
            decision = input("Unknown answer. Please answer Yes or No.")
            # (Above) prints this statement in input does not allign with the acceptable answers. Allows for another opportunity to input.
GameOver(1)
