# Noble Bautista
# November 23rd, 2022
# File Name: Module9_Problem4.py
# Description: Create a while loop that initializes a counter at 0 and will run until the counter reaches 50.
# If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirm the list results using a print statement.

counter = 0 # sets counter equal to 0
tens = [] # creates list named tens

while(counter <= 50): # While loop runs until counter reaches 50
    if counter % 10 == 0:
        tens.append(counter) # appends the value to the "tens" list if the value is divsible by ten
    counter = counter + 1
print(tens)