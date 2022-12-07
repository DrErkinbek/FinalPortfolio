"""
Erkinbek
11/29/2022
Write a function that takes two inputs from a
user and prints whether they are equal or not.
"""
arg1 = int(input("Enter first value "))
arg2 = int(input("Enter second value "))

def equal_or_not(arg1, arg2):
    if arg1 == arg2:
        print("Equal")
    else:
        print("Not equal")

equal_or_not(arg1, arg2)