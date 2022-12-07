"""
Erkinbek
11/15/2022
Write a program with the following chunk of code. Modify this code to produce the
image shown on the right:
"""
import turtle
t = turtle.Turtle()

def drawSquare(t, sz):
    # Get turtle t to draw a square of sz size
    for i in range(4):
        t.forward(sz)
        t.left(sz)
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()

drawSquare(4, 100)