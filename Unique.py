# Program Name: Unique.py
# Noble Bautista
# November 8th, 2022
# Purpose of Program: Write a Python function Unique(lst) that takes a
# list of numbers and returns a new list with unique elements of the given list.
# Use lst = [1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]. Use the append function to
# create a new list where elements are unique. The count function should
# not be used to identify elements that appear more than once in a list.

def Unique(lst): # defines new function "Unique"
  x = []
  for a in lst: # for loop used to ensure repeated digits are omitted
    if a not in x:
      x.append(a)
  return x  #returns value of x
print(Unique([1, 3, 3, 3, 6, 2, 3, 6, 5, 4, 2]))
# (above) prints list of numbers given parameters listed under "Unique" function


