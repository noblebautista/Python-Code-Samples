# Problem2_Mod5Lab.py
# Noble Bautista
# October 26th, 2022
# Assume you have a list of numbers 4, 10, 13, 3, 6, 7, 42, 9, 20. (2 pts)
# Write a loop that prints each of the numbers on a new line.
# Then, write a loop that prints each number and its cube on each line.

nums = [4, 10, 13, 3, 6, 7, 42, 9, 20]  # list of numbers
for i in nums:
    print(i)  # for loop that prints every number on a new line

cubed = []  # gets number for cubed from list

for i in nums:
    square = i * i  # formula for squared number
    cube = square * i  # formula for cubed number
    print("{}       {}      {}".format(i, square, cube))
    # prints original number from list + squared + cubed on each line
