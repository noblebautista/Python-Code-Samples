# Program Name: Flower.py
# Noble Bautista
# November 8th, 2022
# Purpose of Program: Write a Python function Flower(t, sz) using the polygon program
# from the last module. Call the function in a way to create a pattern similar to below.
# Use t as an instance of turtle object and sz as length of each side.


import turtle  # imports turtle module

def Flower(t, sz) :  # defines Flower function (turtle, size)
    for i in range(6): # has six sides
        t.forward(sz)
        t.left(60)  # angles of each side

def main():
    wn = turtle.Screen()
    your_turtle = turtle.Turtle()
    your_turtle.pensize(3)
    wn.bgcolor("white") # changes background color to white
    your_turtle.pencolor("hot pink") # changes turtle color to hot pink
    for i in range(1, 10): # for loop creates rotation of 9 polygons
        Flower(your_turtle, 60)
        your_turtle.left(15)
        your_turtle.fd(13.5)
        your_turtle.left(25)
        your_turtle.down()

main()  # executes turtle design
wn.exitonclick()