"""
Erkinbek
11/15/2022
Write a Python function that takes a list of numbers and returns a new list with
unique elements of the first list. Use the append() function.
"""
my_list = [1, 3, 3, 3, 6, 2, 3, 5, 100, 100, 47, 85, 94, 47]
# output = [1, 2, 3, 100, 5, 6, 47, 85, 94]

# First approach
def unique_function(list_numbers):
    new_list = list(set(list_numbers))
    return new_list

# Second approach
def unique_val(list):
    new_nums = []
    for num in list:
        if num in new_nums:
            continue
        else:
            new_nums.append(num)
    return new_nums