# Erkinbek
# 1 October 2022
# This function prints hello world string 100 times with for loop
# for i in range(1, 100):
#     print("Hello World")


# Erkinbek
# 1 October 2022
# This program runs in list and makes new value by doubling each value
# num_lists = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#
# for num in num_lists:
#     square = num**2
#     print(f'Original number is {num} and square is {square}')


"""
 Write a program that uses a for loop and the turtle module to do the following:
 Ask the user for the length of a side, a fill color, and what shape they would like to draw
(either a triangle or a square)
 Use a loop to draw the shape the user chose with their chosen side length and fill color
o Each angle in a triangle is 60°, each angle in a square is 90
"""
import turtle as t
Tom = t.Turtle()
Tom.pencolor("blue")
Tom.forward(200)
Tom.right(45)
Tom.forward(200)
Tom.left(-135)
Tom.forward(500)
input()

