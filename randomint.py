# Program Name: randomint.py
# Noble Bautista
# November 3rd, 2022
# CSS-225
# Description: Use random.randint to print an odd integer between 0 and 100.

import random # makes sure random is referenced
r1 = random.randint(0, 101) # defines randint range as variable
print(r1) # prints random number Awithin defined range

#make the randomly generated number be odd.
#while True:
#    num = random.randint(0, 101)
#    if num % 2 != 0:
#        break
#print("Odd number is", num)
