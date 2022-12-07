"""
Erkinbek
11/29/2022
Write a function that takes a list and
prints if the value 5 is in that list
"""
list_of_numbers = [4, 5, 2, 6, 7, 9, 3, 5, 9, 10, 32]
list_of_nums = [2,3,4, 6, 9, 32, 12]

def is_five_here(list):
    if 5 in list:
        print("I have found 5 in here")
    else:
        print("The list is clear")

is_five_here(list_of_numbers)
is_five_here(list_of_nums)