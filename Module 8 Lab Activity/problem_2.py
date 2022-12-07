"""
Erkinbek
11/29/2022
Write a function that takes two inputs from
a user and prints whether the sum is
greater than 10, less than 10, or equal to 10
"""
num1 = int(input("first num "))
num2 = int(input("second num "))

def check_sum(num1, num2):
    sum = num1 + num2
    if sum > 10:
        print("Sum is greater than 10")
    elif sum == 10:
        print("Sum is equal to 10")
    else:
        print("Sum is less than 10")

check_sum(num1, num2)