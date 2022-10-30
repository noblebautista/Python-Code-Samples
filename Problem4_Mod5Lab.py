# Problem4_Mod5Lab.py
# Noble Bautista
# October 30th, 2022
# Write a program that asks the user for the number of sides,
# the length of the side, the color of the line,
# and the fill color of a regular polygon.
# The program should draw the polygon and then fill it with the user inputted color.

import turtle
from turtle import Turtle

polygon_sides = [int(input("Please enter the number of sides of the polygon "
                           "you want the turtle to draw: (as a number) "))]
length_side = int(input("Enter the length of the side: (as a number) "))
color_side = input("Which color do you want the pen to be? ")
fill_polygon = input("With which color do you want to fill the polygon? ")

    # (above) input statements asking for personalized turtle graphic.
wn = turtle.Screen()
wn.bgcolor("darkblue")
noble = turtle.Turtle()
noble.shape("turtle")

noble.begin_fill()

for i in range(polygon_sides[0]):
    noble.color(color_side, fill_polygon)
    noble.forward(length_side)
    noble.left(180 - (180 * (polygon_sides[0] - 2)) // polygon_sides[0])
#  for loop which configures all of the actions (side lengths, colors, etc) onto the turtle.
noble.end_fill()

wn.exitonclick()