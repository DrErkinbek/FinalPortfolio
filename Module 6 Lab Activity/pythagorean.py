# Erkinbek
# 11/8/2022
# Write a program that takes two user inputs, a and b, and uses them to calculate the
# Pythagorean theorem using the sqrt() and pow() functions found in the math module.
import math
num1 = float(input("Enter a "))
num2 = float(input("Enter b "))
c = math.sqrt((math.pow(num1, 2) + math.pow(num2, 2)))
print(f'C = {c}')