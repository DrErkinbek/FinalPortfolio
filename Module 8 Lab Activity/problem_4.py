"""
Erkinbek
11/29/2022
Write a function that takes a year as a parameter and returns
True if the year is a leap year, False if it is otherwise.
Consider the requirements of a leap year:
- The year is evenly divisible by 4
- If the year can be evenly devided by 100 it is not a leap year, unless:
    - If the year is also evenly divisible by 400, then it is a leap year.
"""

def check_is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(check_is_leap(2020)) # true
print(check_is_leap(2021)) # false

