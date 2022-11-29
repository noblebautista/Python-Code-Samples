# Program Name: Mod8Prob5.py
# Noble Bautista
# November 17th, 2022
# Purpose of this program: Write a function that prints “All items are ready.”
# if your game character has picked up all the items needed to perform certain task.
# And checks the character’s defuff state is the same as that of the task.
# If character’s state is the same as the debuff state at the time of performing the task,
# then print as follows.


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    '''
    Why do you need  the following methods for this problem?
    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses
    '''   
    def checks(self, p):
        print("Checks function")
        task = input("What task will the character perform? Choose: (Write,climb,cook)")
        # What is needed for cooking
        if task == "cook":
            if p.weaknesses == "small":
                print("The character can not cook")
            #items needed
            elif ('pan' in p.weapons) and ('groceries' in p.weapons):
                print("All items are ready!")

            else:
                print("The character will not Cook")
        # What is needed for climbing
        elif task == "climb":
            if p.weaknesses != "slow":
                print("The character can not climb the mountain")
                # items needed
            elif ('rope' in p.weapons) and ('coat' in p.weapons) and ("first aid kit") in p.weapons:
                print("All items are ready!")

            else:
                print("The character will not climb a mountain")
        # What is needed for writing
        elif task == "write":
            if p.weaknesses != "confusion":
                print("The character can not write a book")
            # items needed
            elif ('pen' in p.weapons) and ('paper' in p.weapons) and ("idea") in p.weapons:
                print("All items are ready!")

            else:
                print("The character will not write a book")


player1 = character('', '', '')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'coat', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

player1.checks(player1)
