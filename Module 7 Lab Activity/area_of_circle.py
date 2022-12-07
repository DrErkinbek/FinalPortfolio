"""
Erkinbek
11/15/22
Write a function areaOfCircle(r) which returns the 
area of a circle of radius r.# Make sure you use 
the math module in your solution.
"""""
import math
def area_of_circle(r):
    area = math.pi * math.pow(r, 2)
    print(area)
area_of_circle(4)