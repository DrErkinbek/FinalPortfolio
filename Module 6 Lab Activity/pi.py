# Erkinbek
# 11/8/2022
# Write a program that will compute the area of a circle.
# Prompt the user to enter the radius and
# print a nice message back to the user with the answer.”
# But this time, use math.pi from the math module in the question
import math
radius = float(input("Enter a radius "))
area = math.pi * math.pow(radius, 2)
print(f'Are of circle equals is {area}')