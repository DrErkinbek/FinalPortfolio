# Erkinbek
# 11/5/2022
#  Write a program that uses a for loop and the turtle module to do the following:
#  Ask the user for the length of a side, a fill color, and what shape they would like to draw
# (either a triangle or a square)
#  Use a loop to draw the shape the user chose with their chosen side length and fill color
# o Each angle in a triangle is 120°, each angle in a square is 90°

import turtle as t
Tom = t.Turtle()

length = int(input("Enter a length of side "))
color = input("Enter a color of shape ")
shape_form = input("triangle or square ")
Tom.pencolor("black")
Tom.fillcolor(color)
Tom.begin_fill()
if shape_form == "triangle":
    for num in range(1, 3):
        Tom.forward(length)
        Tom.right(length)

else:
    for num in range(1, 4):
        Tom.forward(length)
        Tom.right(length)
Tom.end_fill()

