# Problem5_Mod5Lab.py
# Noble Bautista
# October 30th, 2022
# Choose one of the following drawings (shown in word file)
# Then write a program to draw what you choose with the turtle methods
# provided in Summary of Turtle Methods.

import turtle

# creates object for turtle
tr = turtle.Turtle()

# sets thickness for each ring
tr.pensize(5)

tr.color("blue")
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(45)
#draws blue circle

tr.color("black")
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(45)
#draws black circle

tr.color("red")
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(45)
#draws red circle

tr.color("yellow")
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(45)
#draws yellow circle

tr.color("green")
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(45)
#draws green circle

