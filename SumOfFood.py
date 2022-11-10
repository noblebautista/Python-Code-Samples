# Program Name: SumOfFood.py
# Noble Bautista
# November 8th, 2022
# Purpose of Program: Write a Python function SumOfFood(foodDict)
# that sums the price of each food item in a dictionary. Use foodDict
# = {“Pizza”: 3.50, “Sandwich”: 5.30, “Hamburger”: 9.45, “Spaghetti”: 5.75}

def SumOfFood(foodDict): # defines new function "SumOfFood"
    list = []
    for i in foodDict: # for loop for foodDict
        list.append(foodDict[i])
    final = sum(list) # ensures that foodDict prints out the total of items in list
    return final # returns value from the list

foodDict = {"Pizza": 3.50, "Sandwich": 5.30, "Hamburger": 9.45, "Spaghetti": 5.75}
# (above) list of food items in dictionary with prices
print("Sum of food item prices in dictionary ($) =", SumOfFood(foodDict))
# (above) prints sum of all food items in foodDict
