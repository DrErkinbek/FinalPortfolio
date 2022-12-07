# Erkinbek
# 11/8/2022
# Write a program that takes a number from a user and calculates the factorial of that
# number in two ways:
# 1) Using a for loop to calculate the factorial of a user input value.
# 2) Using the math module. You’ll need to do some research to find the function you need.
# Be sure to print both answers.

user_input = int(input("Enter a number "))
factorial = 1
for i in range(1, user_input + 1):
    factorial = factorial * i
print(factorial)

import math
print(math.factorial(user_input))