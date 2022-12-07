"""
Erkinbek
11/15/2022
Write a Python function to check whether a number is between 1 and 10. The
function should take a number as a parameter and return True if the number is between 1 and
10, and False if the number is not between 1 and 10.
"""
def check_range(number):
    if 1 <= number <= 10:
        return True
    else:
        return False
print(check_range(12))
