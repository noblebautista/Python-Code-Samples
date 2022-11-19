# Program Name: CheckRange.py
# Noble Bautista
# November 8th, 2022
# Purpose of Program: Write a Python function CheckRange(number) to check
# whether a number is in a given range (1, 10). The number should be
# randomly generated 20 times in the range (1, 15).
# Print how many times a number is in a given range.


import random # imports random module
#numRange = {'inRange': 0, 'outofRange': 0}

def CheckRange(number):
   # for inRange in range(20): # makes sure it generates 20 results
   #     n = random.randint(1, 15) # random numbers from said range (1-15)
   #if 1 <= n <= 10: # if number falls within range (1-10)
   #   numRange['inRange'] += 1
   #   print('%d  inRange' % n)  # prints that # is within said range
   #elif 11 <= n <= 15: # if number falls out of range (11-15)
   #     numRange['outofRange'] += 1
   #     print('%d  outofRange' % n) # prints that # is NOT within said range
   
    if number in range(1, 10):
        return  True
    else:
        return False

def main():
    count = 0
    #generate 20 numbers in main
    for i in range(20): # makes sure it generates 20 results
        n = random.randint(1, 15) # random numbers from said range (1-15)
        if CheckRange(n):
            count += 1
        else:
            pass  #do nothing
    print('The randomly generatd numbers are in the range %d times' % count)
    # (above) prints how many times a randomly generated number fell within the range
    #print('Shows numbers out of the range %d times' % numRange['outofRange'])
    # (above) prints how many times a randomly generated number fell out of the range
main()
