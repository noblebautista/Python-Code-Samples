# Program Name: Squares.py
# Noble Bautista
# November 8th, 2022
# Purpose of Program: Write a Python function Squares(t, sz)
# using the following chunk of code as a base to produce the image shown.
# Assume the innermost square is 20 units per side, and each successive square
# is 20 units bigger per side, than the one inside it. below.
# Use t as an instance of turtle object and sz as length of each side.

import turtle  # imports turtle module

def Squares(t, sz):  # defines square function (turtle, size)
    for i in range(4): # for loop creates single square
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    your_turtle = turtle.Turtle()
    your_turtle.pensize(3)
    wn.bgcolor("white") # changes background color to white
    your_turtle.pencolor("blue")  # changes turtle color to blue
    for i in range(1, 6): # for loop creates six squares (around original square)
        Squares(your_turtle, 20 * i) # (to left and below) instructions for creating design
        your_turtle.up()
        your_turtle.right(135)
        your_turtle.fd(14.5)  # this represents the distance between each square
        your_turtle.left(135)
        your_turtle.down()

main() # executes turtle design
wn.exitonclick()
